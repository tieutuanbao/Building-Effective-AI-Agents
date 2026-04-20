# AI Usage Tutorial Workspace

**Type:** Documentation — AI Agent Usage Guide (Vietnamese)
**Generated:** 2026-04-17

## Overview

Tutorial **"Hướng Dẫn Sử Dụng AI Agent Hiệu Quả"** — tiếng Việt.

**Mục tiêu:** Giúp tech professionals xây dựng workflow có hệ thống khi dùng AI coding agent (OpenCode, Claude Code, Cursor, Cline).

**Đối tượng:** Đã dùng AI agent nhưng chưa khai thác hiệu quả.

## Workspace Structure

```
./
├── tutorial/              # Nội dung chính (40 files, 7 sections)
│   ├── FUNDAMENTALS/      # 5 bài — khái niệm nền tảng
│   ├── MINDSET/          # 4 bài — tư duy đúng
│   ├── ECOSYSTEM/        # 4 bài — so sánh tools/models
│   ├── SETUP/            # 6 bài — thiết lập môi trường
│   ├── PRACTICAL/        # 9 bài — workflow thực tế
│   ├── USE-CASES/       # 8 bài — ứng dụng thực chiến
│   └── RESOURCES/        # 3 bài — tài nguyên
├── WORKLOG/              # Session logs
├── custom/skill/         # Skill backups (copy → ~/.claude/skills/)
├── raw/                  # Nguồn nghiên cứu
├── wiki/                 # LLM Wiki knowledge base
├── README.md             # Workspace overview
└── AGENTS.md            # This file
```

## Reading Paths

### Fast path (experienced)
```
FUNDAMENTALS/05-agents-md-chuan-muc.md
  → FUNDAMENTALS/03-skill-rule-plugin-mcp.md
  → PRACTICAL/01-viet-prompt-hieu-qua.md
  → PRACTICAL/02-quan-ly-context.md
```

### Full path (newcomers)
```
FUNDAMENTALS/ (5 bài)
  → MINDSET/ (4 bài)
  → PRACTICAL/ (9 bài)
```

## Tool Stack

| Tool | Location | Purpose |
|------|----------|---------|
| **RTK** | tutorial/SETUP/03-rtk-token-optimizer.md | Token optimization |
| **LLM Wiki** | tutorial/SETUP/04-llm-wiki-workflow.md | Knowledge compound |
| **Graphify** | tutorial/SETUP/05-graphify-workflow.md | Knowledge graph |
| **MCP** | tutorial/SETUP/02-ket-noi-mcp.md | Chrome, Context7, GrepApp, WebSearch |

## Writing Guidelines

**Location:** [tutorial/README.md](./tutorial/README.md) — Writing Rules, Research Rules, Content Boundaries

**Quick rules:**

| Rule | Description |
|------|-------------|
| **Pain point first** | Mỗi bài bắt đầu từ vấn đề thực |
| **Before/After** | So sánh old vs new approach |
| **5 sections** | Real Problem → Learning Objectives → Core Concepts → Practical Examples → Summary |
| **File naming** | `01-ten-bai.md` (2-digit, kebab-case, không dấu) |
| **Anti-hype** | Mô tả mechanism, không hype capability |

## Knowledge Base

**LLM Wiki:** `wiki/` — compound knowledge theo Karpathy pattern
**Graphify:** `graphify-out/` — knowledge graph visualization

```
/llm-wiki query "<question>"
/graphify query "<question>"
```

## Contributing

1. Đọc `tutorial/README.md` cho writing guidelines đầy đủ
2. Theo 5-section structure
3. Mỗi bài phải có:
   - ✓ Ít nhất 1 concrete example
   - ✓ Output/result được show
   - ✓ Limitation được nêu rõ
4. File naming: `01-ten-bai.md`
