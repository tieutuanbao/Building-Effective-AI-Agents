# Skill, Rule, Plugin, MCP — Phân Biệt Các Khái Niệm

> Bạn nghe nhắc về "cài skill", "thêm rule", "cài MCP server", "install plugin" — và tự hỏi chúng khác nhau gì? Cài cái nào trước? Chúng có trùng nhau không?

---

## 🔥 Thực Trạng

Bạn đọc tutorial và thấy đề cập đến:

- 🎯 "Cài skill này đi"
- 📝 "Thêm rule vào CLAUDE.md"
- 🌐 "Cài MCP server"
- 🔌 "Install plugin"

→ Mỗi thứ nghe đều quan trọng, nhưng không biết chúng khác nhau thế nào.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Phân biệt được 5 khái niệm: Skill, Rule, Plugin, MCP, Hook
- ✅ Biết mỗi cái scope ra sao (Task-level vs Project-level vs Tool-level)
- ✅ Hiểu khi nào dùng cái nào và không trùng lặp

---

## 🗺️ Bức Tranh Toàn Cảnh

```
┌─────────────────────────────────────────────────────────────┐
│              EXTENSION ECOSYSTEM                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐│
│   │    SKILL     │    │    RULE      │    │   PLUGIN     ││
│   │  (Workflow)  │    │  (Project)   │    │   (Tool)     ││
│   │  Task-level  │    │ Project-level│    │  Tool-level  ││
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘│
│          │                   │                   │         │
│          ▼                   ▼                   ▼         │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐│
│   │  .md file    │    │ AGENTS.md    │    │  npm/JS/TS   ││
│   │  + code      │    │ +             │    │   package    ││
│   │ (skills.sh)  │    │ .claude/rules/│    │              ││
│   └──────────────┘    └──────┬───────┘    └──────┬───────┘│
│          │                   │                   │         │
│          │                   │                   ▼         │
│          ▼                   │            ┌──────────────┐│
│   ┌──────────────┐          │            │  Tool-specific││
│   │  Community   │          │            │   ecosystem   ││
│   │  (skills.sh) │          │            └───────┬──────┘│
│   └──────────────┘          │                    │        │
│                             ▼                    ▼        │
│                    ┌──────────────┐      ┌──────────────┐│
│                    │     MCP      │      │     HOOK     ││
│                    │   (Protocol)  │      │ (Event-driven)│
│                    └──────────────┘      └──────────────┘│
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 1. SKILL — Workflow Tái Sử Dụng

### Định nghĩa

Skill = **Bộ hướng dẫn + workflow** cho task cụ thể

- Thường là markdown file kèm code snippets
- Tái sử dụng được, có thể share qua community

### Format

```markdown
# Skill Name

## When to Use
[Khi nào nên dùng skill này]

## How to Use
[Các bước thực hiện]

## Examples
[Ví dụ cụ thể]
```

### Ví dụ phổ biến

| Skill | Mục đích |
|-------|----------|
| `find-docs` | Tra cứu documentation |
| `git-master` | Git operations |
| `playwright` | E2E testing |
| `frontend-ui-ux` | UI/UX development |
| `security-review` | Security audit |

### Cài đặt

```bash
# Via skills.sh CLI
npx skills add find-docs -g

# Via OpenCode builtin
skills install find-docs
```

### Scope: **Task-level** (hoạt động trong mọi project)

---

## 📋 2. RULE — Quy Ước Project

### Định nghĩa

Rule = **Detailed instructions** cho Agent về cách hoạt động trong project cụ thể

### Cấu trúc đúng

```
project/
├── AGENTS.md                    # Tổng quan ngắn (dưới 100 lines)
│
└── .claude/
    └── rules/                   # Detailed rules (modular)
        ├── typescript.md        # TypeScript conventions
        ├── git-workflow.md      # Git workflow detailed
        ├── testing.md           # Testing patterns
        └── api-design.md        # API design rules
```

### AGENTS.md (tổng quan — NGẮN)

```markdown
# Project Name

## Build & Test
- Install: npm install
- Build: npm run build
- Test: npm test

## Project Structure
├── src/        # Source
├── tests/      # Tests
└── .claude/rules/  # Detailed rules

## Boundaries (3-5 items TỐI ĐA)
- NEVER commit directly to main
- NEVER push secrets
- NEVER modify tests to pass

## Detailed Rules
→ Xem `.claude/rules/` cho conventions chi tiết
```

### .claude/rules/*.md (chi tiết, modular)

```markdown
# TypeScript Conventions

## Naming
- Components: PascalCase (Button.tsx)
- React Hooks: camelCase với use prefix (useAuth.ts)
- Utils: camelCase (formatDate.ts)

## Type Safety
- Never use `any` — use `unknown` if type unclear
- Prefer `interface` over `type` for object shapes
```

### Tại sao không đặt tất cả vào AGENTS.md?

| AGENTS.md dài | `.claude/rules/` modular |
|---------------|--------------------------|
| Agent ignore khi >150 lines | Agent đọc từng file khi cần |
| Khó maintain | Dễ update, scope-specific |
| Context overflow | Chỉ load rules liên quan |

### Scope: **Project-level** (chỉ có trong project đó)

---

## 📊 Quick Reference: Multi-Agent Compatibility

| Tool | Primary Rules File | AGENTS.md Support |
|------|-------------------|-------------------|
| **Claude Code** | `CLAUDE.md` + `.claude/rules/` | ⚠️ Indirect |
| **Cursor** | `.cursor/rules/*.mdc` | ✅ Native |
| **Codex** | `AGENTS.md` | ✅ Native |
| **Devin** | `AGENTS.md` | ✅ Native |
| **Windsurf** | `.windsurfrules` | ✅ Native |
| **Cline** | `.clinerules/` | ✅ Native |

**Best Practice: Layered Approach**

```
project/
├── AGENTS.md                    # Universal - dùng cho hầu hết tools
├── CLAUDE.md                    # Claude Code (import AGENTS.md)
├── .cursor/rules/               # Cursor-specific
├── .clinerules/                 # Cline-specific
```

---

## 🔌 3. PLUGIN — Mở Rộng Tool

### Định nghĩa

Plugin = **Mở rộng capability** của tool/IDE

- Thường là JavaScript/TypeScript package
- Cung cấp thêm tools, agents, MCP servers
- Gắn bó với tool cụ thể

### Ví dụ

| Plugin | Tool | What it adds |
|--------|------|--------------|
| `oh-my-openagent` | OpenCode | 11-agent orchestration |
| `everything-claude-code` | Claude Code | Extra commands |

### Scope: **Tool-level** (chỉ hoạt động với tool đó)

---

## 🌐 4. MCP (Model Context Protocol) — Kết Nối Dịch Vụ

### Định nghĩa

MCP = **Protocol** để connect external tools/services vào Agent

- Client-server model
- Agent gọi MCP server → MCP server access external services

### Architecture

```
┌─────────────┐      MCP       ┌─────────────┐
│    AGENT    │◄─────────────►│  MCP SERVER │
│             │              │             │
│  - Tools    │              │ - Browser   │
│  - Context  │              │ - Filesystem│
│  - Memory   │              │ - Web Search │
└─────────────┘              └─────────────┘
```

### Ví dụ

| MCP Server | Mục đích |
|------------|----------|
| Browser MCP | Web automation |
| Context7 MCP | Documentation lookup |
| Filesystem MCP | File operations |
| Exa MCP | Semantic web search |

### Cài đặt

```json
// In claaude_desktop_config.json
{
  "mcpServers": {
    "browser": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-browser"]
    }
  }
}
```

### Scope: **Protocol-level** (cross-tool, standard)

---

## ⚡ 5. HOOK — Tự Động Hóa Theo Sự Kiện

### Định nghĩa

Hook = **Đoạn code/script** được kích hoạt tự động tại các điểm cụ thể trong vòng đời của Agent

### Tại sao cần Hook?

```
Agent đang edit code ────► PostToolUse hook tự động format
                                              │
                                              ▼
                              Không cần chạy linter thủ công
```

### Hook Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│  Session Start ──► [PreToolUse] ──► [Tool Exec]             │
│       │                  │                │                 │
│       │                  ▼                ▼                 │
│       │            [PostToolUse] ◄─── [Result]              │
│       │                  │                │                 │
│       ▼                  ▼                ▼                 │
│  Session End ◄─────── [Stop] ◄────── Output                │
└─────────────────────────────────────────────────────────────┘
```

### Các loại Hook Events

| Event | Khi nào chạy | Ví dụ use case |
|-------|--------------|----------------|
| `SessionStart` | Bắt đầu session | Load context, khởi tạo |
| `SessionEnd` | Kết thúc session | Lưu summary, cleanup |
| `UserPromptSubmit` | User gửi prompt | Inject thêm context |
| `PreToolUse` | **Trước** khi tool chạy | Block lệnh nguy hiểm |
| `PostToolUse` | **Sau** khi tool chạy | Auto-format, logging |
| `Stop` | Agent sắp dừng | Verify checklist |

### 3 Loại Hook Handler

| Type | Mô tả | Ví dụ |
|------|-------|-------|
| **Command** | Chạy shell script | `prettier --write $file_path` |
| **HTTP** | Gọi endpoint | POST đến webhook |
| **Agent** | Spawn sub-agent | Dùng Haiku verify trước commit |

### Ví dụ: Auto-format sau edit

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "tool == \"Edit\" && tool_input.file_path matches \"\\.(ts|tsx|js|jsx)$\"",
      "hooks": [{
        "type": "command",
        "command": "npx prettier --write \"$file_path\""
      }]
    }]
  }
}
```

### Scope: **Event-level** (chạy trong mỗi session)

---

## 📊 So Sánh Toàn Bộ

| Aspect | Skill | Rule | Plugin | MCP | Hook |
|--------|-------|------|--------|-----|------|
| **Format** | MD + code | AGENTS.md + rules | JS/TS | Server | JSON/script |
| **Scope** | Task | Project | Tool | Protocol | Event |
| **Source** | Community | Local | Tool ecosystem | External services | Event-driven |
| **Sharing** | Via skills.sh | AGENTS.md (open) | Tool-specific | Standardized | Config-based |
| **Location** | skills.sh/ | `.claude/rules/` | npm/JS/TS | MCP servers | settings.json |

---

## ⚠️ Những Sai Lầm Thường Gặp

### ❌ Nhét tất cả vào AGENTS.md

```
AGENTS.md với 500 lines:
- Tất cả TypeScript rules
- Tất cả Git workflow
- Tất cả testing patterns
→ Agent ignore, context overflow
```

### ❌ Trùng lặp Skill và MCP

```
Skill "find-docs" (dùng Context7 MCP)
vs
MCP server "context7" (direct access)
→ Kết quả tương tự, cách dùng khác
```

### ❌ Quá nhiều extensions

```
15 skills installed
5 MCP servers active
3 plugins loaded
→ Agent overwhelmed, slowdown
```

---

## ✅ Best Practices

### Trước khi cài skill, hỏi:

```
1. Tôi đã có skill nào cho task này chưa?
2. Nó trùng với MCP nào đang dùng không?
3. Task này frequent enough để cần skill?
```

### AGENTS.md nên:

```
✓ Project overview ngắn (2-3 sentences)
✓ Build commands chính (copy-paste ready)
✓ 3-5 key boundaries (CRITICAL rules)
✓ Reference tool-specific rules if needed
```

### AGENTS.md không nên:

```
✗ Tất cả TypeScript rules (→ dùng tool-specific rules)
✗ Tất cả Git workflow (→ dùng tool-specific rules)
✗ Dài quá 100-150 lines
```

### Khi nào dùng Hook vs Skill/Rule:

```
✓ Hook: Fast feedback, automation on tool events (format, lint, block)
✓ Skill: Complex workflow, multi-step processes
✓ Rule: Project conventions, coding standards
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Phân biệt được: Skill, Rule, Plugin, MCP, Hook
- [ ] Biết Skill = task-level (community), Rule = project-level
- [ ] Biết Plugin = tool-specific, MCP = protocol cross-tool
- [ ] Hiểu Hook = event-driven automation
- [ ] KHÔNG nhét tất cả vào AGENTS.md — dùng `.claude/rules/`
- [ ] KHÔNG cài trùng Skill và MCP cho cùng task

---

## 🔗 Liên Quan

- **Chi tiết AGENTS.md:** [FUNDAMENTALS/05: AGENTS.md Chuẩn Mở](./05-agents-md-chuan-muc.md)
- **Cài đặt MCP:** [SETUP/02: Kết Nối MCP Servers](../SETUP/02-ket-noi-mcp.md)
- **Thực hành:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)