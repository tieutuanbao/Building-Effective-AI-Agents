#!/usr/bin/env python3
"""
LLM Wiki — Generate WIKI_SUMMARY.md

Creates a one-page summary of the wiki for agent context.
Run after /llm-wiki ingest or as part of the workflow.

Usage:
    python scripts/generate-summary.py
    python scripts/generate-summary.py --wiki ./wiki --output ./wiki/SUMMARY.md
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if match:
        import yaml
        try:
            frontmatter = yaml.safe_load(match.group(1)) or {}
            body = match.group(2)
            return frontmatter, body
        except yaml.YAMLError:
            pass
    return {}, text


def count_wiki_pages(wiki_dir: Path) -> dict:
    """Count pages in each wiki category."""
    counts = {
        "entities": 0,
        "concepts": 0,
        "sources": 0,
        "syntheses": 0,
    }
    for category in counts:
        dir_path = wiki_dir / category
        if dir_path.exists():
            counts[category] = len(list(dir_path.glob("*.md")))
    return counts


def get_top_pages(wiki_dir: Path, category: str, limit: int = 5) -> list[dict]:
    """Get most-linked pages in a category."""
    pages = []
    dir_path = wiki_dir / category
    if not dir_path.exists():
        return pages

    for md_file in dir_path.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            link_count = content.count("[[")
            pages.append({
                "name": md_file.stem,
                "label": _file_to_label(md_file.stem),
                "links": link_count,
            })
        except Exception:
            pass

    pages.sort(key=lambda x: x["links"], reverse=True)
    return pages[:limit]


def _file_to_label(name: str) -> str:
    """Convert kebab-case filename to readable label."""
    return name.replace("-", " ").replace("_", " ").title()


def get_recent_activity(log_file: Path, limit: int = 10) -> list[str]:
    """Get recent entries from LOG.md."""
    if not log_file.exists():
        return []

    content = log_file.read_text(encoding="utf-8")
    entries = re.findall(r"^## \[([^\]]+)\] (\w+) \| (.+)$", content, re.MULTILINE)
    return [f"- [{date}] {action}: {desc}" for date, action, desc in entries[-limit:]]


def get_gaps(gaps_file: Path, limit: int = 5) -> list[str]:
    """Get knowledge gaps from gaps.json."""
    if not gaps_file.exists():
        return []

    try:
        data = json.loads(gaps_file.read_text(encoding="utf-8"))
        gaps = data.get("gaps", [])
        return [g.get("description", str(g)) if isinstance(g, dict) else str(g) for g in gaps[:limit]]
    except (json.JSONDecodeError, OSError):
        return []


def get_contradictions(outputs_dir: Path) -> list[str]:
    """Find contradiction reports in outputs/."""
    contradictions = []
    if not outputs_dir.exists():
        return contradictions

    for report in outputs_dir.glob("**/lint-*.md"):
        try:
            content = report.read_text(encoding="utf-8")
            if "contradiction" in content.lower():
                contradictions.append(f"- [[{report.stem}]]")
        except Exception:
            pass
    return contradictions[:5]


def get_orphan_pages(wiki_dir: Path) -> list[str]:
    """Find orphan pages (no incoming wiki links)."""
    orphans = []

    all_links: set[str] = set()
    for category in ["entities", "concepts", "sources", "syntheses"]:
        dir_path = wiki_dir / category
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
                links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content)
                all_links.update(lnk.lower().strip() for lnk in links)
            except Exception:
                pass

    for category in ["entities", "concepts", "sources", "syntheses"]:
        dir_path = wiki_dir / category
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("*.md"):
            name = md_file.stem.lower()
            if name not in all_links and name != "index" and name != "log":
                orphans.append(f"- [[{md_file.stem}]]")
    return orphans[:10]


def get_topics(config_file: Path) -> list[str]:
    """Extract topic names from config.yaml."""
    if not config_file.exists():
        return []
    try:
        import yaml
        config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
        topics = config.get("topics", [])
        return [t.get("name", str(t)) if isinstance(t, dict) else str(t) for t in topics]
    except (yaml.YAMLError, OSError):
        return []


def get_active_feeds(config_file: Path) -> list[str]:
    """Extract enabled feed names from config.yaml."""
    if not config_file.exists():
        return []
    try:
        import yaml
        config = yaml.safe_load(config_file.read_text(encoding="utf-8"))
        feeds = config.get("feeds", {})
        active = []
        for name, settings in feeds.items():
            if isinstance(settings, dict) and settings.get("enabled"):
                active.append(name)
            elif isinstance(settings, list) and settings:
                active.append(name)
        return active
    except (yaml.YAMLError, OSError):
        return []


def get_raw_stats(raw_dir: Path) -> dict:
    """Get raw/ directory statistics."""
    stats = {"total": 0, "articles": 0, "papers": 0, "notes": 0, "media": 0}
    if not raw_dir.exists():
        return stats

    for category in ["articles", "papers", "notes", "media"]:
        dir_path = raw_dir / category
        if dir_path.exists():
            count = len(list(dir_path.glob("*.*")))
            stats[category] = count
            stats["total"] += count
    return stats


def generate_summary(
    wiki_dir: Path,
    output_path: Path,
    raw_dir: Optional[Path] = None,
    discoveries_dir: Optional[Path] = None,
    outputs_dir: Optional[Path] = None,
    config_file: Optional[Path] = None,
) -> None:
    """Generate WIKI_SUMMARY.md from wiki data."""

    wiki_dir = Path(wiki_dir)
    raw_dir = Path(raw_dir) if raw_dir else wiki_dir.parent / "raw"
    discoveries_dir = Path(discoveries_dir) if discoveries_dir else wiki_dir.parent / ".discoveries"
    outputs_dir = Path(outputs_dir) if outputs_dir else wiki_dir.parent / "outputs"
    config_file = Path(config_file) if config_file else wiki_dir.parent / "config.yaml"

    counts = count_wiki_pages(wiki_dir)
    top_entities = get_top_pages(wiki_dir, "entities", limit=5)
    top_concepts = get_top_pages(wiki_dir, "concepts", limit=5)

    log_file = wiki_dir / "LOG.md"
    recent_activity = get_recent_activity(log_file, limit=10)

    gaps_file = discoveries_dir / "gaps.json"
    gaps = get_gaps(gaps_file, limit=5)

    orphans = get_orphan_pages(wiki_dir)

    topics = get_topics(config_file)
    active_feeds = get_active_feeds(config_file)

    raw_stats = get_raw_stats(raw_dir)

    lines = []
    lines.append("# LLM Wiki Summary")
    lines.append("")
    lines.append(f"**Last updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Stats")
    lines.append("")
    lines.append(f"- **{counts['entities']}** entities · **{counts['concepts']}** concepts · **{counts['sources']}** sources · **{counts['syntheses']}** syntheses")
    lines.append(f"- **{raw_stats['total']}** raw sources (articles: {raw_stats['articles']}, papers: {raw_stats['papers']}, notes: {raw_stats['notes']})")
    lines.append("")
    lines.append("## Top Entities (most referenced)")
    lines.append("")
    if top_entities:
        for p in top_entities:
            lines.append(f"- [[{p['name']}]] — {p['links']} links")
    else:
        lines.append("_No entities yet._")
    lines.append("")
    lines.append("## Top Concepts (most referenced)")
    lines.append("")
    if top_concepts:
        for p in top_concepts:
            lines.append(f"- [[{p['name']}]] — {p['links']} links")
    else:
        lines.append("_No concepts yet._")
    lines.append("")
    lines.append("## Recent Activity")
    lines.append("")
    if recent_activity:
        for entry in recent_activity:
            lines.append(entry)
    else:
        lines.append("_No recent activity._")
    lines.append("")
    lines.append("## Health")
    lines.append("")
    if orphans:
        lines.append(f"- **{len(orphans)}** orphan pages (no incoming links):")
        for o in orphans[:5]:
            lines.append(f"  {o}")
        if len(orphans) > 5:
            lines.append(f"  _...and {len(orphans) - 5} more_")
    else:
        lines.append("- ✅ No orphan pages detected")
    if gaps:
        lines.append(f"- **{len(gaps)}** knowledge gaps identified:")
        for g in gaps:
            lines.append(f"  - {g}")
    else:
        lines.append("- ✅ No knowledge gaps identified")
    lines.append("")
    lines.append("## Topics & Feeds")
    lines.append("")
    if topics:
        lines.append(f"**Topics:** {', '.join(topics)}")
    else:
        lines.append("_No topics configured._")
    if active_feeds:
        lines.append(f"**Active feeds:** {', '.join(active_feeds)}")
    else:
        lines.append("_No feeds enabled._")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Read [[wiki/INDEX.md]] for full catalog.")
    lines.append("Run `/llm-wiki lint` for detailed health check.")
    lines.append("Run `/llm-wiki query \"...\"` to ask questions based on this wiki.")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"WIKI_SUMMARY.md generated: {output_path}")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate LLM Wiki summary")
    parser.add_argument(
        "--wiki",
        type=Path,
        default=Path("wiki"),
        help="Path to wiki directory (default: wiki)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path (default: wiki/SUMMARY.md)",
    )
    parser.add_argument(
        "--raw",
        type=Path,
        default=None,
        help="Path to raw directory (default: ../raw)",
    )
    parser.add_argument(
        "--discoveries",
        type=Path,
        default=None,
        help="Path to .discoveries directory (default: ../.discoveries)",
    )
    parser.add_argument(
        "--outputs",
        type=Path,
        default=None,
        help="Path to outputs directory (default: ../outputs)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to config.yaml (default: ../config.yaml)",
    )

    args = parser.parse_args()

    if args.output is None:
        args.output = args.wiki / "SUMMARY.md"

    generate_summary(
        wiki_dir=args.wiki,
        output_path=args.output,
        raw_dir=args.raw,
        discoveries_dir=args.discoveries,
        outputs_dir=args.outputs,
        config_file=args.config,
    )


if __name__ == "__main__":
    main()
