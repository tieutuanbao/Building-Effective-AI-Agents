# AI và AI Agent — Lịch Sử Hình Thành

> Bạn từng nghe: AI, LLM, GPT, Agent, Prompt Engineering, RAG, Agentic AI... nhưng không biết chúng liên quan như thế nào? Bài này sẽ giúp bạn.

---

## 🔥 Thực Trạng

Bạn đang đọc tutorial về AI Agent và bị choáng ngợp bởi:

- **Thuật ngữ:** AI, LLM, GPT, Agent, Prompt Engineering, RAG, Agentic AI...
- **Models:** Claude, Gemini, ChatGPT, Copilot...
- **Concepts:** Prompt Engineering, RAG, Fine-tuning, Agentic AI...

→ Mỗi thứ nghe đều quan trọng, nhưng không biết bắt đầu từ đâu.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Phân biệt được **sự khác biệt cốt lõi** giữa LLM và AI Agent
- ✅ Hiểu **4 thành phần tạo nên sức mạnh** của một Agent
- ✅ Biết cách **xác định cấp độ tự chủ** (Autonomy) của các công cụ đang dùng

---

## 📖 Từ AI Đến AI Agent

### Timeline — 75 Năm Cuộc Cách Mạng

```
1950s    Turing đặt nền móng cho AI
1960s    AI Winter — overhyped, underdelivered
1990s    Machine Learning emergence
2012     Deep Learning breakthrough (AlexNet) 🔥
2017     Transformer — kiến trúc nền tảng
2018-20  LLM emerge (BERT, GPT-1,2,3)
2022     ChatGPT — AI goes mainstream
2023     GPT-4, Claude 1, Gemini — cuộc đua bắt đầu
2024     Claude 3.5, Claude Code — Agent features
NOW      AI Agents = LLM + Tools + Memory + Planning
```

> 📌 **Ghi nhớ:** 2017 là năm quan trọng nhất — Transformer là base architecture cho tất cả LLMs hiện đại.

---

### 4 Cấp Độ Phát Triển

```
┌─────────────────────────────────────────────────────┐
│  Level 1: Pure AI                                    │
│  Input → AI Model → Output                           │
│  Chỉ predict, không làm gì khác                     │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  Level 2: AI + Tools (LLM + Tools)                   │
│  LLM + Tools (Bash, Browser, File System)            │
│  = Can take actions, không chỉ predict              │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  Level 3: AI + Memory (LLM + Tools + Memory)          │
│  Session context = Remember within conversation      │
│  ⚠️ Vẫn reset mỗi session                            │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  Level 4: AI Agent (LLM + Tools + Memory + Planning)  │
│  Loop: Observe → Plan → Act → Feedback              │
│  = Autonomous behavior 🚀                            │
└─────────────────────────────────────────────────────┘
```

---

### Các Loại AI — Mối Quan Hệ

```
                    AI (umbrella term)
                         │
            ┌────────────┴────────────┐
            │                          │
            ▼                          ▼
    Machine Learning              Deep Learning
            │                          │
            └──────────┬───────────────┘
                       ▼
              Large Language Model (LLM)
                       │
                       ▼
                 AI AGENT 🔑
        (LLM + Tools + Memory + Planning)
```

---

## 🧩 Agent = Model + Tools + Memory + Orchestration

### 4 Thành Phần Cốt Lõi

| Thành phần | Vai trò | Ví dụ tool |
|------------|---------|------------|
| **🧠 Model (Brain)** | Reasoning, generation | Claude, GPT-4 |
| **🔧 Tools (Hands)** | Actions — đọc, viết, chạy lệnh | Bash, Read, Edit, Browse |
| **💾 Memory (State)** | Lưu context — session hoặc persistent | Session context, LLM Wiki |
| **🎯 Orchestration (Cognition)** | Điều phối — planning, loop, self-correct | Observe→Plan→Act→Feedback |

### Orchestration — Trái Tim Của Agent

```
Planning        →  Chia goal thành hierarchical steps
Loop            →  observe → plan → act → feedback
Self-correction →  Step fail → replan từ step đó, không restart
Branching       →  Plan thay đổi theo state (if X → path A, else → path B)
```

---

## 💾 Memory Architecture — 4 Tiers

Memory không chỉ là "session context". Nó có **4 tiers**:

```
├── Working Memory ────► Context window (reset mỗi session)
├── Short-Term Memory ──► Session state (không persistent)
├── Long-Term Memory
│   ├── Episodic ─────► Graphify (sự kiện, quan hệ)
│   ├── Semantic ─────► LLM Wiki (kiến thức tích lũy)
│   └── Procedural ──► Skills/Rules (hành vi đã học)
└── External Memory ───► MCP/RAG (tra cứu)
```

### Biết Tier Giúp Gì?

| Vấn đề | Nguyên nhân | Giải pháp |
|--------|-------------|-----------|
| "Agent quên sau session" | Thiếu Long-Term Memory | Dùng LLM Wiki / Graphify |
| "Context tràn" | Dùng Working Memory không hiệu quả | Chunk context, summarize |
| "Agent làm lại từ đầu" | Thiếu Procedural Memory | Viết Skills/Rules |

### Tool Mapping

| Tier | Tool | Tutorial |
|------|------|----------|
| Semantic Memory | LLM Wiki | `SETUP/04-llm-wiki-workflow.md` |
| Episodic Memory | Graphify | `SETUP/05-graphify-workflow.md` |
| Procedural Memory | Skills/Rules | `FUNDAMENTALS/03-skill-rule-plugin-mcp.md` |
| External Memory | MCP/RAG | `SETUP/02-ket-noi-mcp.md` |

---

## 🎚️ Autonomy Levels — Cấp Độ Tự Chủ

| Level | Name | Mô tả | Ví dụ |
|-------|------|-------|-------|
| **1** | Reactive | Chỉ respond to input | Basic chatbots |
| **2** | Tool-using | Dùng được tools | GPT-4 + browsing |
| **3** | Context-aware | Nhớ được context | Claude, GPT with memory |
| **4** | Goal-oriented | Tự plan được steps | Complex agents |
| **5** | Fully autonomous | Tự hoàn thành complex tasks | (Still rare/experimental) |

> 🔑 **OpenCode, Claude Code = Level 3-4.** Bạn vẫn cần specify goal rõ ràng.

---

## 💡 Ví Dụ Cụ Thể — Agent Loop Thực Tế

### ❌ Trước: Pure LLM (không có Agent)

```
Input: "Refactor function calculateTotal() trong file utils.py"

Output: [LLM trả lời dựa trên prompt]
❌ KHÔNG thực hiện được — chỉ generate text
```

> **Tại sao?** LLM chỉ generate text — không có Tools để đọc file, không có Memory để hiểu project context.

---

### ✅ Sau: AI Agent (LLM + Tools + Memory + Planning)

**Prompt của bạn:**
```
"Refactor function calculateTotal() trong utils.py để tối ưu performance"
```

**Agent Loop thực thi:**

```
┌─────────────────────────────────────────────────────────────┐
│  1️⃣ OBSERVE                                                 │
│  → Agent đọc utils.py, hiểu function hiện tại              │
│  → User prompt + session context = "hiểu task"             │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  2️⃣ PLAN                                                    │
│  → "Cần: 1) Đọc file  2) Hiểu logic  3) Viết lại  4) Test" │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  3️⃣ ACT                                                     │
│  → Tool: Read file utils.py                               │
│  → Tool: Write refactored function                         │
│  → Tool: Run tests                                         │
└─────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────┐
│  4️⃣ FEEDBACK                                                │
│  → Test pass? → Hoàn thành ✅                               │
│  → Test fail? → Loop lại bước Plan → Sửa                    │
└─────────────────────────────────────────────────────────────┘
```

**Output cuối cùng:**
```
✅ Function đã được refactor
✅ Tests pass
✅ Tokens used: ~12K (thay vì 50K nếu copy/paste toàn bộ file)
```

---

## ⚠️ Những Hiểu Lầm Phổ Biến

| Sai lầm | Thực tế |
|---------|---------|
| "Nó là trợ lý thông minh" | Nó là pattern matching có độ chính xác cao |
| "Nó hiểu ý tôi" | Nó predict token tiếp theo dựa trên context |
| "Nó suy nghĩ như con người" | Nó không "suy nghĩ" — nó tính toán xác suất |
| "Nó nhớ mọi thứ" | Nó chỉ nhớ trong context window hiện tại |

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu AI → ML → DL → LLM → AI Agent hierarchy
- [ ] Biết LLM là prediction engine, Agent là LLM + extra components
- [ ] Phân biệt được: LLM, Prompt Engineering, RAG, Agent
- [ ] Biết OpenCode/Claude Code ở autonomy level 3-4
- [ ] Hiểu các khái niệm: LLM, Tools, Memory, Orchestration
- [ ] Trình bày được Agent Loop: Observe → Plan → Act → Feedback
- [ ] Hiểu tại sao Agent hiệu quả hơn Pure LLM

---

## 🔗 Liên Quan

- **Tiếp theo:** [02. Các Khái Niệm Core](./02-cac-khai-niem-core.md)
- **Xem thêm:** [MINDSET/01: Cách Hiểu Đúng về AI Agent](../MINDSET/01-cach-hieu-dung-ve-ai-agent.md)