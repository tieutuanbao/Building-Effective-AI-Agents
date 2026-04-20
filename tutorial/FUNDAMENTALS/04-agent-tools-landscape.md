# Agent Tools Landscape — Bức Tranh Toàn Cảnh

> Có quá nhiều lựa chọn: OpenCode, Claude Code, Cursor, Cline... Mỗi cái claim là "tốt nhất". Bài này giúp bạn **hiểu landscape** và **chọn đúng tool** cho use case của mình.

---

## 🔥 Thực Trạng

Bạn thấy có quá nhiều lựa chọn:

- **IDE Agents:** OpenCode, Claude Code, Cursor, Cline, Continue...
- **CLI Agents:** Claude CLI, GPT CLI, smithery-cli...
- **Frameworks:** LangChain, AutoGen, CrewAI...
- **Platforms:** GitHub Copilot, CodeWhisperer...

→ Không biết cái nào phù hợp, và chúng khác nhau gì.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Phân biệt được 4 categories: IDE agents, CLI, Frameworks, Platforms
- ✅ Biết strengths/weaknesses của major IDE agents
- ✅ Chọn được tool phù hợp với situation cụ thể

---

## 🗺️ 4 Categories Của AI Coding Tools

```
AI CODING TOOLS
├── IDE-BASED AGENTS     → Gắn vào Editor/IDE
├── CLI AGENTS           → Chạy qua terminal
├── AGENT FRAMEWORKS     → Build your own agents
└── PLATFORM AGENTS      → Cloud-based, managed
```

---

## 💻 IDE-Based Agents — So Sánh Chi Tiết

| Tool | IDE Support | Model | Cost | MCP Support | Điểm mạnh |
|------|-------------|-------|------|-------------|-----------|
| **OpenCode** | VS Code, JetBrains | Flexible (Claude, GPT...) | **Free** | ✅ Yes | Flexible, open source |
| **Claude Code** | VS Code, Claude app | Claude only | $17-200/mo | ✅ Yes | Native Claude experience |
| **Cursor** | Cursor only | Claude, GPT | Free + Pro | ✅ Limited | Composer, AI-first design |
| **Cline** | VS Code | Claude, GPT, etc | **Free** | ✅ Yes | Open source, model agnostic |
| **Continue** | VS Code, JetBrains | Flexible | **Free** | ✅ Yes | Open source |
| **Windsurf** | VS Code | Claude | Free + Pro | ✅ Yes | Flow, Cascade |

---

### OpenCode — Miễn Phí & Linh Hoạt

```
✅ PROS
├── Miễn phí, open source (146k ⭐)
├── Model agnostic — dùng được Claude, GPT, local...
├── MCP support mạnh
├── Highly configurable
└── Oh-my-openagent ecosystem (11-agent orchestration)

❌ CONS
├── Cần tự cấu hình nhiều
├── Documentation có thể sparse
└── Less polished UI

⭐ BEST FOR: Developers muốn control + flexibility
```

---

### Claude Code — Native Claude Experience

```
✅ PROS
├── Native Claude experience
├── Well-integrated với Anthropic
├── Strong codebase understanding
└── Security-focused (Anthropic built)

❌ CONS
├── Đắt ($17-200/mo)
├── Chỉ Claude models
└── Less customizable

⭐ BEST FOR: Teams dùng Anthropic products, enterprise
```

---

### Cursor — AI-First Editor

```
✅ PROS
├── AI-first design
├── Composer (multi-file generation)
├── Strong autocomplete
└── Regular updates

❌ CONS
├── Chỉ hoạt động trên Cursor editor
├── Pro plan đắt cho features nhất
└── Less open

⭐ BEST FOR: Developers muốn AI-native editor experience
```

---

### Cline / Continue — Open Source

```
✅ PROS
├── Free, open source
├── Model agnostic
├── MCP support
└── Community-driven

❌ CONS
├── UI/UX có thể less polished
├── Cần manual setup
└── Variable quality

⭐ BEST FOR: Developers ưa thích open source, tự build
```

---

## ⚙️ CLI Agents

Dùng cho automation, scripts, CI/CD:

| Tool | Mô tả |
|------|-------|
| Claude CLI | Native Anthropic CLI, chat-based |
| GPT CLI | OpenAI's command-line interface |
| smithery-cli | Connect to various MCPs |

---

## 🏗️ Agent Frameworks

Dành cho developers muốn **build custom agents**:

| Framework | Language | Strengths |
|-----------|----------|-----------|
| **LangChain** | Python, JS | Most popular, comprehensive |
| **AutoGen** | Python | Multi-agent conv, Microsoft-backed |
| **CrewAI** | Python | Role-based agents, orchestration |

**Khi nào dùng:**
- Build product/services dựa trên AI
- Custom workflows không fit vào IDE agents
- Integration vào existing systems

---

## ☁️ Platform Agents

| Service | Provider | Focus |
|---------|----------|-------|
| GitHub Copilot | Microsoft | IDE integration |
| CodeWhisperer | Amazon | AWS integration |
| Gemini in IDE | Google | Gemini native |

Thường là add-on features, không phải full agents.

---

## 🎯 Decision Framework

```
Bạn cần gì?
│
├── Build product/service?
│   └── YES → Framework (LangChain, AutoGen, CrewAI)
│
└── Dùng IDE Agent?
    │
    ├── Budget Limited?
    │   └── Free: OpenCode, Cline, Continue
    │
    └── Paid:
        ├── Anthropic-focused → Claude Code
        ├── AI-first design → Cursor
        └── Enterprise → Windsurf, Cody
```

---

## 💡 Ví Dụ: Chọn Tool Cho Use Cases

### Use Case 1: Solo Developer, Budget Limited

**Tình huống:**
- Personal project, ngân sách: $0
- Kỹ năng: Python, VS Code

**Quyết định:**

```
1. Build product? → Không → IDE Agent
2. VS Code user? → Yes
3. Budget? → Free

→ RECOMMENDATION: Cline
  - Free, open source
  - VS Code native
  - Model flexible (Claude, GPT, Gemini...)
```

---

### Use Case 2: Team, Anthropic-focused

**Tình huống:**
- Team 5 backend developers
- Đã dùng Claude API
- Cần: code review tự động + CI/CD integration

**Quyết định:**

```
1. Build product? → Không → IDE Agent
2. Anthropic-focused? → Yes
3. Enterprise? → Cần security

→ RECOMMENDATION: Claude Code + oh-my-openagent
  - Native Claude integration
  - Security-focused
  - 11-agent orchestration
```

---

### Use Case 3: Build Custom AI Product

**Tình huống:**
- Startup muốn xây dựng AI-powered coding assistant cho internal use
- Cần custom workflows không có sẵn

**Quyết định:**

```
1. Build product? → Yes → Framework

→ RECOMMENDATION: LangChain hoặc AutoGen
  - LangChain: Python, comprehensive, most popular
  - AutoGen: Multi-agent conversation, Microsoft-backed
```

---

## 📊 Recommendations Tổng Hợp

### For Individual Developers

| Situation | Recommendation |
|-----------|---------------|
| Budget limited | **OpenCode** (free, flexible) |
| Best overall | **Claude Code** (if can afford) |
| VS Code user | **Cline** hoặc **Continue** |
| Already in Cursor | **Cursor** (Composer is good) |
| Enterprise | **Windsurf** hoặc **Cody** |

### For Teams

| Situation | Recommendation |
|-----------|---------------|
| Anthropic-focused | **Claude Code** + oh-my-openagent |
| Open source priority | **OpenCode** + custom extensions |
| Enterprise security | **Claude Code** hoặc **Cody** |
| Mixed model needs | **OpenCode** (model agnostic) |

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Phân biệt được 4 categories: IDE agents, CLI, Frameworks, Platforms
- [ ] Biết strengths/weaknesses của major IDE agents
- [ ] Hiểu OpenCode = flexible + free, Claude Code = native + paid
- [ ] Chọn được tool phù hợp với situation

---

## 🔗 Liên Quan

- **So sánh chi tiết hơn:** [ECOSYSTEM/02: So Sánh Agent Tools](../ECOSYSTEM/02-so-sanh-agent-tools.md)
- **Cài đặt:** [SETUP/01: Chọn OpenCode](../SETUP/01-chon-opencode.md)
- **Use case cụ thể:** [USE-CASES/01: Debug Code](../USE-CASES/01-debug-code.md)