# AGENTS.md — Chuẩn Mở Cho Project Context

> Bạn chuyển từ Claude Code sang Cursor — và agent mới **không hiểu gì** về project. Mỗi lần phải giải thích lại từ đầu. AGENTS.md ra đời để **chuẩn hóa project context** cho mọi agent.

---

## 🔥 Thực Trạng

**Trước AGENTS.md:**

Mỗi tool có cách riêng:

| Tool | File | Format |
|------|------|--------|
| Claude Code | `CLAUDE.md` | Markdown |
| Cursor | `.cursorrules` | Markdown |
| Windsurf | `windsurf.md` | Markdown |
| Devin | `AGENTS.md` | Markdown |

→ Muốn dùng 3 tool → viết 3 file, cập nhật 3 chỗ mỗi khi project thay đổi.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Hiểu AGENTS.md là open standard (Linux Foundation)
- ✅ Phân biệt được AGENTS.md vs CLAUDE.md vs .cursorrules
- ✅ Tạo được AGENTS.md cho project của mình (dưới 100-150 lines)

---

## 📖 AGENTS.md Là Gì

**AGENTS.md = "README cho robots"**

Nơi bạn đặt tất cả thông tin mà agent cần để hoạt động hiệu quả.

```
├── AGENTS.md                    # Root — đọc trước tiên
├── packages/
│   ├── core/
│   │   └── AGENTS.md           # Nested — override cho package đó
│   └── web/
│       └── AGENTS.md
```

→ Agent đọc **AGENTS.md gần nhất** với file đang làm việc.

---

## 📋 Cấu Trúc AGENTS.md

### Required Sections

```markdown
# [Project Name]

## Build & Test
[exact commands: install, build, test, lint]

## Code Style
[naming conventions, patterns to follow, patterns to avoid]

## Project Structure
[directory layout và purpose]

## Git Workflow
[branch conventions, PR format]
```

### Optional Sections

```markdown
## Boundaries
[Những gì agent KHÔNG nên làm]

## Architecture
[Key modules, relationships]

## Common Patterns
[how things are typically done here]
```

---

## ❌ Anti-Pattern: Ném Tất Cả Vào AGENTS.md

**Sai lầm phổ biến:**

```
❌ "Tôi muốn agent hiểu TẤT CẢ → viết TẤT CẢ vào AGENTS.md"
```

Bạn cài 15 skills, 5 MCP servers, 50 rules → đổ hết vào AGENTS.md.

**Kết quả:**

| Vấn đề | Hệ quả |
|--------|--------|
| **Context overflow** | Agent chỉ đọc được ~200 lines đầu tiên |
| **Contradicting instructions** | Skills conflict, agent không biết ưu tiên |
| **Token cost spike** | Mỗi message đều mang toàn bộ AGENTS.md |
| **Agent paralysis** | Quá nhiều instruction → không làm gì cả |

---

### 📊 Nghiên Cứu: Bao Nhiêu Lines Là Đủ?

**ETH Zurich study (2026):** 10 repositories, 124 PRs

| Metric | Không có AGENTS.md | Có AGENTS.md tối ưu |
|--------|-------------------|---------------------|
| Median runtime | 98.57s | **70.34s (-28%)** |
| Output tokens | 5,744 | **4,591 (-20%)** |

> 📌 **Files dưới 150 lines** có hiệu quả cao nhất.

---

## 🏗️ Separation of Concerns — Đặt Content Đúng Chỗ

### Nguyên tắc: Mỗi thứ đúng vị trí

| Content Type | Đặt ở đâu | Tại sao |
|--------------|-----------|---------|
| **Skills** | `skills.sh` (installed separately) | Task-level, reusable across projects |
| **MCP servers** | `claude_desktop_config.json` | Tool-level, not markdown content |
| **Project rules** | `AGENTS.md` (dưới 150 lines) | Project-level, specific conventions |
| **Detailed workflows** | `.claude/rules/*.md` | Modular, path-scoped |

### Decision Tree: Content đi đâu?

```
Content bạn muốn thêm là gì?
│
├── SKILL? (reusable workflow)
│   └── → skills.sh — KHÔNG viết vào AGENTS.md
│
├── MCP/Tool config? (server, credentials)
│   └── → Tool config file — KHÔNG viết vào AGENTS.md
│
├── PROJECT CONVENTION? (how we do things here)
│   └── → AGENTS.md — tối đa 100-150 lines
│
├── MULTI-STEP WORKFLOW? (complex process)
│   └── → .claude/rules/workflow.md — reference từ AGENTS.md
│
└── AGENT-SPECIFIC? (Claude Code only)
    └── → CLAUDE.md
```

---

## ✅ Good AGENTS.md Structure (Dưới 100 lines)

```markdown
# Project Name

## Build & Test (CRITICAL — đặt ĐẦU TIÊN)
- Install: npm install
- Build: npm run build
- Test: npm test && npm run lint

## Project Structure (KEY paths only)
├── src/        # Source code
├── tests/      # Test files
└── docs/       # Documentation

## Code Conventions (3-5 rules TỐI ĐA)
- Naming: camelCase functions, PascalCase components
- Error handling: always try/catch on external calls
- Never use `as any`

## Boundaries (WHAT NOT TO DO — 3-5 items)
- NEVER commit directly to main
- NEVER push secrets to repo
- NEVER modify tests to make them pass

## (Optional) Workflow Reference
→ Detailed workflows → see .claude/rules/
→ Skills installed → see skills.sh list
→ MCP servers → see .claude/config.json
```

---

## ⚖️ AGENTS.md vs CLAUDE.md

| | AGENTS.md | CLAUDE.md |
|--|-----------|-----------|
| **Standard** | Open (Linux Foundation) | Claude Code only |
| **Tool support** | 25+ tools | Claude Code only |
| **Nested files** | ✅ | ✅ |
| **Scope** | Cross-tool | Claude Code only |

**Dùng cái nào?**

```
Nếu bạn chỉ dùng Claude Code:
  → Dùng CLAUDE.md (Claude Code ưu tiên đọc trước)

Nếu bạn dùng nhiều tools:
  → Dùng AGENTS.md (chuẩn mở, tất cả tools đọc được)

Nếu bạn dùng Claude Code + muốn multi-tool:
  → AGENTS.md làm base + CLAUDE.md cho Claude-specific tweaks
```

**Claude Code đọc cả hai:**
```
1. Tìm CLAUDE.md trước (most specific location)
2. Sau đó tìm AGENTS.md
3. Merge cả hai vào context
```

---

## 🚀 Quick Start

```bash
# Tạo AGENTS.md cho project hiện tại
cat > AGENTS.md << 'EOF'
# [Project Name]

## Build & Test
- Install:
- Build:
- Test:

## Code Style
-

## Project Structure
-

## Boundaries
- NEVER [action]
EOF
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu AGENTS.md là open standard
- [ ] Phân biệt được AGENTS.md vs CLAUDE.md vs .cursorrules
- [ ] Biết cách agent đọc và resolve AGENTS.md
- [ ] Tạo được AGENTS.md cho project của mình
- [ ] KHÔNG ném tất cả vào AGENTS.md — Separation of Concerns
- [ ] Giữ AGENTS.md dưới 100-150 lines

---

## 🔗 Liên Quan

- **Chi tiết hơn:** [FUNDAMENTALS/03: Skill, Rule, Plugin, MCP](./03-skill-rule-plugin-mcp.md)
- **Thực hành:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)
- **Use case:** [USE-CASES/01: Debug Code](../USE-CASES/01-debug-code.md)