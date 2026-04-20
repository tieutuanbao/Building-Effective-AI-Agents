# Bản Đồ Ecosystem — Big Picture

> Bạn đang debug một vấn đề với AI agent: "Agent respond chậm → check ở đâu?", "Context tràn → vấn đề ở layer nào?", "Muốn thêm capability mới → Skill hay MCP?" — **Bài này là bản đồ** giúp bạn DEBUG và SELECT đúng layer.

---

## 🔥 Thực Trạng

Bạn đang debug hoặc **chọn tool mới**:

- 🤔 "Cursor 3 Agents Window" là cái gì, ở layer nào?
- 🤔 "oh-my-openagent" khác "Claude Agent Teams" chỗ nào?
- 🤔 MCP có phải là skill không?

→ **Bài này là bản đồ** — giúp bạn DEBUG và SELECT đúng layer, không phải memorize stats.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ **Đọc được** architecture của bất kỳ agent tool nào
- ✅ **Debug được** bằng cách xác định vấn đề thuộc layer nào
- ✅ **Chọn được** đúng component (Skill vs MCP vs Rule)
- ✅ **Hiểu được** tradeoffs khi thay đổi một component

---

## 🗺️ Ecosystem Map — 5 Layers

```
┌─────────────────────────────────────────────────────────────────┐
│  5-LAYER ARCHITECTURE                                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 1️⃣ USER LAYER — Bạn trong loop                             │  │
│  │    • Định nghĩa requirements                               │  │
│  │    • Provide context                                       │  │
│  │    • Make decisions                                        │  │
│  │    • Verify output                                         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              ↓                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 2️⃣ INTERFACE LAYER — Tool bạn tương tác                    │  │
│  │    • IDE Agents: Cursor 3, Claude Code, OpenCode          │  │
│  │    • CLI Agents: Claude Code, Codex CLI, Cline CLI         │  │
│  │    • Platforms: GitHub Copilot, Windsurf                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              ↓                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 3️⃣ AGENT LAYER — Core Intelligence                        │  │
│  │    • Orchestration: Multi-agent systems                    │  │
│  │    • Memory: Session state, persistent storage              │  │
│  │    • LLM: Reasoning brain                                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              ↓                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 4️⃣ EXTENSION LAYER — Capabilities                          │  │
│  │    • Skills: Task-specific workflows                       │  │
│  │    • Rules: Project conventions (AGENTS.md)                │  │
│  │    • MCP: External tool protocols                         │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              ↓                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 5️⃣ PROVIDER LAYER — Infrastructure                         │  │
│  │    • Anthropic → Claude 4.x                               │  │
│  │    • OpenAI → GPT-4o, o1/o3                               │  │
│  │    • Google → Gemini 2.5                                   │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

```
User input (requirement)
       ↓
Interface receives (prompt)
       ↓
Agent processes (LLM reasoning)
       ↓
Extensions used (Skills, MCP tools)
       ↓
Provider API called (model inference)
       ↓
Response returned (output)
       ↓
User reviews (verify)
```

---

## 🔍 Diagnostic Use Cases

### Case 1: "Agent respond sai"

**Dấu hiệu:** Agent đưa ra thông tin không chính xác, hallucinate

**Diagnostic:**
```
Layer 1 (User): Prompt rõ ràng chưa? → Thử rõ ràng hơn
Layer 3 (Agent): LLM issue? → Thử model khác
Layer 4 (Extension): MCP gọi đúng source chưa? → Check MCP config
Layer 5 (Provider): API issue? → Check provider status
```

### Case 2: "Context tràn"

**Dấu hiệu:** Context window full, agent bỏ qua phần quan trọng

**Diagnostic:**
```
Layer 3 (Agent): Memory management? → Dùng summarize/reset
Layer 4 (Extension): MCP trả quá nhiều data? → Filter MCP output
```

### Case 3: "Muốn thêm capability mới"

**Câu hỏi đầu tiên:** Capability này thuộc layer nào?

| Capability | Layer | Component | Ví dụ |
|------------|-------|-----------|--------|
| Tra cứu docs | Extension | MCP | `context7` |
| Git workflow | Extension | Skill | `git-master` |
| Code style | Extension | Rule | `AGENTS.md` |
| Model routing | Agent | Orchestration | oh-my-openagent |

### Case 4: "Chọn tool mới"

**Dùng map để so sánh:**

| Tool | Interface | Agent | Extension | Provider |
|------|-----------|-------|-----------|----------|
| **Cursor 3** | IDE (VS Code fork) | Built-in | MCP (limited) | Claude/GPT |
| **Claude Code** | Terminal/IDE | Native Claude | Full MCP | Claude only |
| **OpenCode** | Multiple | Flexible | Any MCP | Any model |
| **Cline** | VS Code | Flexible | MCP Marketplace | Any API |

---

## 🧩 Skills vs Rules vs MCP — Quick Selector

```
Muốn hướng dẫn agent cách LÀM task?        → Skill
Muốn định nghĩa convention cho project?      → Rule
Muốn kết nối với external tool/service?     → MCP
```

| Component | Level | Purpose | Example |
|-----------|-------|---------|---------|
| **Skill** | Task-level | Workflow cho specific task | `find-docs`, `git-master`, `playwright` |
| **Rule** | Project-level | Conventions cho codebase | `AGENTS.md`, `.claude/rules` |
| **MCP** | Protocol | External tool integration | `context7`, `chrome-devtools`, `exa` |

---

## 🔗 Multi-Agent Systems

| System | Architecture | Best For |
|--------|--------------|----------|
| **oh-my-openagent** | 11 specialized agents | Complex, autonomous tasks |
| **Cursor 3 Agents Window** | Visual parallel | Team collaboration |
| **Claude Agent Teams** | CLI orchestration | Enterprise workflows |

---

## 📊 Layer Quick Reference

| Layer | What It Does | Example Components |
|-------|--------------|---------------------|
| **Interface** | How you interact | Cursor 3, Claude Code, Codex CLI |
| **Agent** | Orchestration + reasoning | oh-my-openagent, Claude Agent Teams |
| **Extension** | Add capabilities | Skills, MCP, Rules |
| **Provider** | Model infrastructure | Claude 4.x, GPT-4o, Gemini 2.5 |

### Key Relationships — If This Fails, Check This Layer

| If This Fails | Check This Layer |
|---------------|------------------|
| "Agent không hiểu prompt" | User Layer (prompt quality) |
| "Agent respond chậm" | Provider Layer (API latency) |
| "Agent thiếu capability" | Extension Layer (MCP/Skill missing) |
| "Tool không tương thích" | Interface Layer (tool choice) |

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Đọc được 5-layer architecture
- [ ] Xác định được vấn đề thuộc layer nào
- [ ] Chọn đúng component (Skill/MCP/Rule) cho use case
- [ ] Dùng map để debug khi có vấn đề
- [ ] So sánh tools dựa trên layer position

---

## 🔗 Liên Quan

- **Chi tiết:** [02: So Sánh Agent Tools](./02-so-sanh-agent-tools.md)
- **Chi tiết:** [03: So Sánh Models](./03-so-sanh-models.md)
- **Áp dụng:** [04: Decision Tree](./04-decision-tree.md)