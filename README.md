# 🎓 AI Usage Tutorial Workspace

> **Hướng dẫn sử dụng AI Agent Hiệu quả** — Tiếng Việt · 37 bài viết · 6 phần

---

## 📖 Giới thiệu

Workspace này chứa tutorial giúp bạn xây dựng **workflow có hệ thống** khi dùng AI coding agent.

```
🤖 OpenCode    🤝 Claude Code    💻 Cursor    ⚡ Cline
```

**Đối tượng:** Đã dùng AI agent nhưng chưa khai thác hiệu quả — context tràn lan, prompt không rõ, chi phí không kiểm soát.

---

## 🗂️ Cấu trúc

```
.
├── 📚 tutorial/           # Nội dung chính (37 files, 6 sections)
│   ├── FUNDAMENTALS/      # 5 bài — khái niệm nền tảng
│   ├── MINDSET/          # 4 bài — tư duy đúng về AI agent
│   ├── ECOSYSTEM/        # 4 bài — so sánh tools, models
│   ├── SETUP/            # 7 bài — thiết lập môi trường
│   ├── PRACTICAL/        # 9 bài — workflow thực tế
│   └── USE-CASES/       # 8 bài — ứng dụng thực chiến
│
├── 📝 WORKLOG/           # Session logs — lịch sử làm việc
├── 🎒 custom/skill/      # Skill backups → copy vào ~/.claude/skills/
├── 📦 raw/               # Nguồn nghiên cứu (không tracked)
├── 🧠 wiki/              # LLM Wiki — knowledge base cá nhân
├── 🔧 AGENTS.md          # Project context cho agent
└── 📄 README.md          # File này
```

---

## 🚀 Bắt đầu ở đâu

### ⚡ Đường dẫn nhanh (cho người đã có kinh nghiệm)

```
SETUP/07-to-chuc-workspace.md
  → PRACTICAL/01-viet-prompt-hieu-qua.md
  → PRACTICAL/02-quan-ly-context.md
```

### 📖 Đường dẫn đầy đủ (cho người mới)

```
FUNDAMENTALS/ (5 bài)
  → MINDSET/ (4 bài)
  → PRACTICAL/ (9 bài)
```

Xem [tutorial/README.md](tutorial/README.md) cho lộ trình chi tiết và mục lục đầy đủ.

---

## 🛠️ Tool Stack

| Tool | File | Mục đích |
|------|------|----------|
| ⚡ **RTK** | `SETUP/03-rtk-token-optimizer.md` | Token optimizer — giảm 60-90% usage |
| 🧠 **LLM Wiki** | `SETUP/04-llm-wiki-workflow.md` | Knowledge compound — tích lũy theo thời gian |
| 🕸️ **Graphify** | `SETUP/05-graphify-workflow.md` | Knowledge graph — visualize relationships |
| 🌐 **MCP Servers** | `SETUP/02-ket-noi-mcp.md` | Chrome · Context7 · GrepApp · WebSearch |

---

## ✍️ Viết theo Tutorial

Nếu bạn đóng góp nội dung:

```
1. 📖 Đọc AGENTS.md + tutorial/README.md
2. 📝 Theo 5-section structure
3. ✅ Check:
   ├── Ít nhất 1 concrete example
   ├── Output/result được show
   └── Limitation được nêu rõ
4. 📁 File naming: 01-ten-bai.md
```

**Quick rules:**

| Rule | Description |
|------|-------------|
| 💡 **Pain point first** | Bắt đầu từ vấn đề thực, không định nghĩa |
| 🔄 **Before/After** | So sánh old vs new approach |
| 📋 **5 sections** | Real Problem → Objectives → Core → Examples → Summary |
| 📝 **File naming** | `01-ten-bai.md` (2-digit, kebab-case, không dấu) |
| ⚠️ **Anti-hype** | Mô tả mechanism, không hype capability |

---

## 📊 Knowledge Base

| Nơi lưu | Công cụ | Lệnh |
|---------|---------|------|
| Knowledge compound | **LLM Wiki** | `/llm-wiki query "<question>"` |
| Knowledge graph | **Graphify** | `/graphify query "<question>"` |

```
# Ví dụ query
/llm-wiki query "so sánh RAG và fine-tuning"
/graphify query "relationship between context and memory"
```

---

## 📌 Liên quan

| File | Nội dung |
|------|----------|
| [tutorial/README.md](tutorial/README.md) | Mục lục đầy đủ + lộ trình đọc |
| [AGENTS.md](AGENTS.md) | Writing rules + research rules |
| [wiki/](wiki/) | LLM Wiki knowledge base |
| [custom/skill/](custom/skill/) | Skill backups cho reader |

---

*Built with ❤️ for the AI Agent community*
