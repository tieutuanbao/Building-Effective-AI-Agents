# Decision Tree — Khi Nào Dùng Tool Nào, Model Nào

> Bạn có một task và không biết: Nên dùng agent nào? Nên dùng model nào? Cần setup gì?

---

## 🔥 Thực Trạng

Bạn có một task và không biết:

- 🤔 Nên dùng agent nào?
- 🤔 Nên dùng model nào?
- 🤔 Cần setup gì?

→ Đây là decision tree để answer những câu hỏi đó một cách systematic.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Classify task vào đúng category (Code/Research/Creative)
- ✅ Chọn tool phù hợp với task type
- ✅ Chọn model phù hợp với complexity + budget
- ✅ Hiểu 2026 consensus: dùng 2-3 tools, không chỉ 1

---

## 🎯 Quick Decision Matrix

| Task | Recommended Model | Alternative |
|------|-----------------|------------|
| **Quick edit** (<5 min) | Claude Haiku 4 / GPT-4o-mini | — |
| **Bug fix** (known pattern) | Claude Haiku 4 / GPT-4o-mini | Sonnet 4.6 for complex |
| **Feature dev** | Claude Sonnet 4.6 / GPT-4o | Opus 4.6 for novel |
| **Code review** | Claude Sonnet 4.6 | Opus 4.6 for deep |
| **Architecture** | Claude Opus 4.6 | GPT-o3 with reasoning |
| **Documentation** | GPT-4o / Claude Sonnet 4.6 | — |
| **Research** | Gemini 2.5 Flash / Claude Sonnet 4.6 | Opus 4.6 |
| **Complex reasoning** | Claude Opus 4.6 | GPT-o3 |

---

## 🔧 Code Tasks Decision Tree

```
Task: Code
│
├── Debug/bug fix?
│   └──→ Claude Haiku 4 / GPT-4o-mini
│
├── Write new feature?
│   ├── Simple, well-defined → Claude Sonnet 4.6 / GPT-4o
│   └── Complex, novel → Claude Sonnet 4.6 + human verify
│
├── Refactor?
│   ├── Small, safe → Cline / Codex CLI
│   └── Large, risky → Claude Code + human oversight
│
├── Code review?
│   └──→ Claude Sonnet 4.6
│
├── Write tests?
│   └──→ Claude Sonnet 4.6 + testing skill
│
├── Documentation?
│   └──→ Claude Sonnet 4.6 / GPT-4o
│
└── Need parallel agents?
    ├──→ Cursor 3 Agents Window (visual, team-friendly)
    └──→ Claude Agent Teams (CLI, complex orchestration)
```

---

## 🔬 Research Tasks Decision Tree

```
Task: Research
│
├── Documentation lookup?
│   └──→ find-docs skill + Context7 MCP
│
├── Web search/current info?
│   ├── Simple → Exa MCP / Browser MCP
│   └── Complex → Claude Sonnet 4.6 + browse
│
├── Code search GitHub patterns?
│   └──→ Grep App MCP
│
├── Analyze long document?
│   └──→ Gemini 2.5 Flash / Claude Sonnet 4.6
│
├── Learn new codebase?
│   └──→ Claude Code + graphify skill
│
└── Market/competitor research?
    └──→ Claude Sonnet 4.6 + web search + Exa MCP
```

---

## 🎨 Creative Tasks Decision Tree

```
Task: Creative
│
├── Write/blog/documentation?
│   ├── Technical → Claude Sonnet 4.6
│   └── Marketing → GPT-4o
│
├── Architecture design?
│   └──→ Claude Opus 4.6 + human review
│
├── UI/UX ideation?
│   ├── Wireframes → Minimax MCP
│   └── Structure → Claude Sonnet 4.6 + brainstorming
│
└── Brainstorm/ideation?
    └──→ Any agent + Claude Opus 4.6
```

---

## 💰 Cost vs Quality Decision

| Task \ Cost | Low | Medium | High |
|------------|-----|--------|------|
| **Low complexity** | Haiku | Sonnet | Opus |
| **Medium complexity** | Sonnet | Sonnet | Opus |
| **High complexity** | Opus | Opus | Opus |

> 💡 **Best value:** Sonnet (diagonal from low-low to medium-medium)

---

## ⚙️ Setup Requirements By Task

### Minimal Setup (Quick Start)

```
Quick tasks: Documentation, simple edits, questions
├─ OpenCode, Cline, or Claude Code
├─ Claude Haiku 4 / GPT-4o-mini
└─ DONE - works out of box
```

### Standard Setup (Most Tasks)

```
Most development tasks: features, debugging, refactoring
├─ Claude Code hoặc Cursor 3
├─ Model: Claude Sonnet 4.6 hoặc GPT-4o
├─ Essential MCPs: Browser, Context7
└─ Skills: git-master, find-docs, [task-specific]
```

### Advanced Setup (Complex/Enterprise)

```
Complex tasks: architecture, security, large refactors, multi-agent
├─ Claude Code (Agent Teams) + Cursor 3 (Agents Window)
├─ Multiple models (routing by task complexity)
├─ Full MCP stack: Browser, Context7, Exa, Cline MCP Marketplace
├─ Skills: security-review, tdd-workflow, graphify
├─ oh-my-openagent (multi-agent orchestration)
└─ Custom rules in AGENTS.md / CLAUDE.md
```

---

## 💡 2026 Consensus: Multi-Tool Stack

**Dùng 2-3 tools cho full coverage:**

```
┌────────────────────────────────────────────────────────────┐
│  RECOMMENDED STACK (2026)                                   │
├────────────────────────────────────────────────────────────┤
│  Daily IDE:        Cursor 3 (Agents Window)                │
│  Terminal Agent:   Claude Code (hard problems)           │
│  Speed/Volume:     Codex CLI (parallel tasks)              │
│  Safety Net:       GitHub Copilot ($10/mo)                 │
│  Budget:           Cline + Windsurf                         │
└────────────────────────────────────────────────────────────┘

Cost: ~$150-300/month cho full stack
Output: comparable to small engineering team
```

---

## 💡 Practical Examples

### Example 1: "Fix the login bug"

```
Step 1: Classification → Code task → Debug
Step 2: Known pattern? Yes, "login redirect not working"
Step 3: Tool: Claude Code hoặc Cursor 3
        Model: Claude Haiku 4 (simple known fix)
Step 4: If Haiku fails → Retry with Claude Sonnet 4.6
Step 5: If still fails → Human debug, then let Sonnet help
```

### Example 2: "Design the authentication system"

```
Step 1: Classification → Creative → Architecture design
Step 2: Tool: Claude Code với Agent Teams (multi-agent)
        Model: Claude Opus 4.6 (complex reasoning)
Step 3: Agent explores options → Human reviews → Agent details
Step 4: Human verify before implementation
```

### Example 3: "Build features in parallel with team"

```
Step 1: Classification → Multi-agent, parallel work
Step 2: Tool: Cursor 3 Agents Window (visual, team-friendly)
        hoặc Claude Code Agent Teams (CLI, complex)
Step 3: Agent 1: Frontend features
        Agent 2: Backend API
        Agent 3: Tests
Step 4: Human reviews all outputs → Merge + verify + deploy
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Classify task vào đúng category (Code/Research/Creative)
- [ ] Chọn tool phù hợp với task type
- [ ] Chọn model phù hợp với complexity + budget
- [ ] Scale up model khi task cần thiết
- [ ] Use routing để optimize cost
- [ ] KHÔNG dùng model quá mạnh cho simple tasks

---

## 🔗 Liên Quan

- **So sánh tools:** [02: So Sánh Agent Tools](./02-so-sanh-agent-tools.md)
- **So sánh models:** [03: So Sánh Models](./03-so-sanh-models.md)
- **Big picture:** [01: Bản Đồ Ecosystem](./01-ban-do-ecosystem.md)