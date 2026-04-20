# 📚 Hướng Dẫn Sử Dụng AI Agent Hiệu Quả

> **37 bài viết** · **6 phần** · Tiếng Việt

---

## 🎯 Mục lục

### [0. Tổng Quan](./README.md)
Giới thiệu tổng quan về tutorial và lộ trình đọc.

---

### 📖 1. [FUNDAMENTALS](./FUNDAMENTALS/)
*Những khái niệm nền tảng — build vocabulary để đọc các phần sau không bị lú*

- [01](./FUNDAMENTALS/01-ai-agent-la-gi.md) — AI, AI Agent là gì
- [02](./FUNDAMENTALS/02-cac-khai-niem-core.md) — Các khái niệm Core
- [03](./FUNDAMENTALS/03-skill-rule-plugin-mcp.md) — Skill, Rule, Plugin, MCP
- [04](./FUNDAMENTALS/04-agent-tools-landscape.md) — Agent Tools Landscape
- [05](./FUNDAMENTALS/05-agents-md-chuan-muc.md) — AGENTS.md — Chuẩn Mở

---

### 🧠 2. [MINDSET](./MINDSET/)
*Cách nghĩ đúng về AI Agent — nền tảng tư duy trước khi cài đặt hay dùng tool*

- [01](./MINDSET/01-cach-hieu-dung-ve-ai-agent.md) — Cách hiểu đúng về AI Agent
- [02](./MINDSET/02-nguyen-tac-delegation.md) — Nguyên tắc Delegation
- [03](./MINDSET/03-su-hop-tac-hieu-qua.md) — Sự hợp tác hiệu quả
- [04](./MINDSET/04-gioi-han-cua-agent.md) — Giới hạn của Agent

---

### 🌍 3. [ECOSYSTEM](./ECOSYSTEM/)
*Bức tranh toàn cảnh — trả lời câu hỏi "dùng cái nào"*

**Learning flow:** Big Picture → Details → Application

- [01](./ECOSYSTEM/01-ban-do-ecosystem.md) — Bản đồ Ecosystem ← **Big Picture**
- [02](./ECOSYSTEM/02-so-sanh-agent-tools.md) — So sánh Agent Tools ← **Details**
- [03](./ECOSYSTEM/03-so-sanh-models.md) — So sánh Models ← **Details**
- [04](./ECOSYSTEM/04-decision-tree.md) — Decision Tree ← **Application**

---

### ⚙️ 4. [SETUP](./SETUP/)
*Thiết lập môi trường hiệu quả — đủ dùng, không thừa thãi*

- [01](./SETUP/01-chon-opencode.md) — Cài đặt OpenCode
- [02](./SETUP/02-ket-noi-mcp.md) — Kết nối MCP Servers
- [03](./SETUP/03-rtk-token-optimizer.md) — RTK Token Optimizer
- [04](./SETUP/04-llm-wiki-workflow.md) — LLM Wiki Workflow
- [05](./SETUP/05-graphify-workflow.md) — Graphify Workflow
- [06](./SETUP/06-superpowers-workflow.md) — Superpowers Workflow
- [07](./SETUP/07-to-chuc-workspace.md) — Tổ chức Workspace

---

### 💡 5. [PRACTICAL](./PRACTICAL/)
*Thực hành — phần quan trọng và dài nhất*

- [01](./PRACTICAL/01-viet-prompt-hieu-qua.md) — Viết Prompt có hiệu quả
- [02](./PRACTICAL/02-quan-ly-context.md) — Quản lý Context
- [03](./PRACTICAL/03-brainstorm-voi-agent.md) — Brainstorm với Agent
- [04](./PRACTICAL/04-session-hygiene.md) — Session Hygiene
- [05](./PRACTICAL/05-sua-khi-agent-di-sai.md) — Sửa khi Agent đi sai
- [06](./PRACTICAL/06-verification-habits.md) — Verification Habits
- [07](./PRACTICAL/07-quan-ly-chi-phi.md) — Quản lý Chi phí
- [08](./PRACTICAL/08-phan-ra-task.md) — Phân rã Task
- [09](./PRACTICAL/09-cac-workflow-thuong-gap.md) — Các Workflow thường gặp

---

### 🎯 6. [USE-CASES](./USE-CASES/)
*Ứng dụng thực chiến — dùng agent giải quyết vấn đề cụ thể*

- [01](./USE-CASES/01-debug-code.md) — Debug Code với Agent
- [02](./USE-CASES/02-tim-giai-phap.md) — Tìm Giải Pháp Kỹ Thuật
- [03](./USE-CASES/03-research-thong-tin.md) — Research & Tìm Kiếm Thông Tin
- [04](./USE-CASES/04-brainstorm-y-tuong.md) — Brainstorm & Đề Xuất Ý Tưởng
- [05](./USE-CASES/05-review-code.md) — Review & Cải Thiện Code
- [06](./USE-CASES/06-viet-docs-content.md) — Viết Docs & Content
- [07](./USE-CASES/07-hoc-cong-nghe-moi.md) — Học Công Nghệ Mới & Onboard
- [08](./USE-CASES/08-planning-estimation.md) — Planning & Estimation Dự Án

---

## 🚀 Lộ trình đọc

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
  → SETUP/ (chọn bài phù hợp)
  → PRACTICAL/ (9 bài)
  → USE-CASES/ (8 bài)
```

---

## ✍️ Nguyên Tắc Viết cho Author

**Nguyên tắc đọc tutorial:**

Mỗi section tuân theo **learning flow từ tổng quan đến chi tiết đến áp dụng:**

```
Big Picture → Details → Application
    ↓           ↓          ↓
Tổng quan    Chi tiết    Áp dụng
(Overview)   (So sánh)   (Decision/Action)
```

**Ý nghĩa:**
- **Big Picture (Tổng quan):** Bạn hiểu cái gì tồn tại, chúng liên quan như thế nào
- **Details (Chi tiết):** Bạn so sánh được các lựa chọn cụ thể
- **Application (Áp dụng):** Bạn biết CHỌN cái nào CHO VAI TRÒ GÌ

**Ví dụ ECOSYSTEM section:**

```
01-ban-do-ecosystem.md      → Big Picture (5 layers, how they connect)
02-so-sanh-agent-tools.md   → Details (tool comparison)
03-so-sanh-models.md        → Details (model comparison)
04-decision-tree.md        → Application (which to choose for your case)
```

**Nguyên tắc viết cho mỗi bài:**

| Phần | Mục đích |
|------|----------|
| **💡 Real Problem** | Hook — pain point người đọc đang gặp |
| **🎯 Learning Objectives** | Kết quả sau khi đọc xong — có thể LÀM được gì |
| **📖 Core Concepts** | Giải thích + analogy, dùng mermaid/table khi cần |
| **🛠️ Practical Examples** | Before/After, code/prompt samples, actual outputs |
| **📋 Checkpoint** | Tổng hợp — có thể dùng như quick reference |

**Quick rules:**

| Phần | Mục đích |
|------|----------|
| **💡 Real Problem** | Hook — pain point người đọc đang gặp |
| **🎯 Learning Objectives** | Kết quả sau khi đọc xong |
| **📖 Core Concepts** | Giải thích + analogy, dùng mermaid/table khi cần |
| **🛠️ Practical Examples** | Before/After, code/prompt samples |
| **📋 Checkpoint** | Các vấn đề được giải quyết, làm rõ qua bài học |

**Quick rules:**

| Rule | Description |
|------|-------------|
| 💡 **Pain point first** | Bắt đầu từ vấn đề thực, không định nghĩa |
| 🔄 **Before/After** | So sánh old vs new approach |
| ✅ **Content check** | Ít nhất 1 concrete example + output + limitation |
| ⚠️ **Anti-hype** | Mô tả mechanism, không hype capability |
| 📌 **USE-CASES variant** | 6-section variant (adds Pitfalls & Recovery after Summary) |

---

## 📌 Đối tượng mục tiêu

Tutorial này dành cho người đã sử dụng AI Agent nhưng chưa khai thác hiệu quả:

- ✅ Đã dùng qua ít nhất 1 agent tool
- ❌ Context tràn lan, prompt không rõ
- ❌ Không biết dùng model nào
- ❌ Chi phí phát sinh không kiểm soát
- ✅ Muốn xây dựng workflow có hệ thống

---

## 🔗 Liên quan

| File | Nội dung |
|------|----------|
| [../README.md](../README.md) | Workspace overview |
| [../AGENTS.md](../AGENTS.md) | Writing rules đầy đủ |
| [../wiki/](../wiki/) | LLM Wiki knowledge base |
