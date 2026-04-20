# Phân Tầng Engineering AI Agent — Từ Prompt Đến Harness

> Khi xây dựng Agent thực sự hoạt động được trong production, bạn cần hơn là chỉ viết prompt tốt. Bài này giới thiệu **3 tầng Engineering** giúp bạn hiểu cách Agent hoạt động ở mức system-level — từ câu lệnh đầu vào, đến context, đến cả **hệ thống bao quanh model** như tools, middleware, memory và feedback loop.

---

## 🔥 Thực Trạng

Bạn viết prompt rất chi tiết, nhưng Agent vẫn:

- ❌ Refactor nhầm file khác
- ❌ Không chạy được tests
- ❌ Không hiểu project context

→ **Prompt tốt không đủ** — bạn cần thêm Context và Harness.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ **Định nghĩa được** 3 tầng Engineering: Prompt, Context, Harness
- ✅ **Giải thích được** mối quan hệ Supersets: `Prompt ⊂ Context ⊂ Harness`
- ✅ **Áp dụng được** 3 tầng để phân tích và thiết kế bất kỳ Agent workflow

---

## 🧩 3 Tầng Engineering

```
┌─────────────────────────────────────────────────────────────────┐
│  Tầng 3: HARNESS ENGINEERING                                     │
│  ═══════════════════════════════════════                        │
│  Orchestration • Tools • Middleware • Memory • Feedback Loop   │
│  ⊂ Context ⊂ Harness                                             │
├─────────────────────────────────────────────────────────────────┤
│  Tầng 2: CONTEXT ENGINEERING                                     │
│  ═════════════════════════════════════                          │
│  RAG • Context Files • Progressive Disclosure                    │
│  ⊂ Prompt (Context chứa Prompt)                                  │
├─────────────────────────────────────────────────────────────────┤
│  Tầng 1: PROMPT ENGINEERING                                      │
│  ═════════════════════════════════════                          │
│  Zero-shot • Few-shot • Chain-of-Thought                        │
│  Tầng cơ bản nhất                                                │
└─────────────────────────────────────────────────────────────────┘
```

> 📌 **Ghi nhớ:** `Prompt ⊂ Context ⊂ Harness` — mỗi tầng là superset của tầng trước.

---

## 📖 Chi Tiết Từng Tầng

### Tầng 1: Prompt Engineering

**Định nghĩa:** Nghệ thuật thiết kế chuỗi ký tự đầu vào để hướng dẫn LLM.

| Thành phần | Mô tả |
|------------|-------|
| **Mục tiêu** | Tăng độ chính xác cho tác vụ đơn lẻ |
| **Kỹ thuật** | Zero-shot, Few-shot, Chain-of-Thought |
| **Vai trò** | Tầng cơ bản nhất — không có nó, tầng khác không hoạt động |

```
Prompt tốt = Role + Task + Context + Output Format + Constraints
```

---

### Tầng 2: Context Engineering

**Định nghĩa:** Xác định, thu thập, định dạng và quản lý thông tin ngữ cảnh liên quan đến task.

| Thành phần | Mô tả |
|------------|-------|
| **Mối quan hệ** | Context là tập hợp mẹ của Prompt (`Prompt ⊂ Context`) |
| **Mục tiêu** | Cung cấp thông tin nền tảng để Agent đưa ra quyết định đúng |
| **Kỹ thuật** | RAG, Context Files, Progressive Disclosure |

**Ví dụ Context cần thiết:**
```
├── Project: Python FastAPI backend
├── File: src/api/users.py (đã đọc)
├── Error: IndexError: list index out of range
├── Tests: tests/api/test_users.py (PASS)
└── Conventions: Black formatter, pytest
```

→ Agent **hiểu project context** → đưa ra quyết định đúng.

---

### Tầng 3: Harness Engineering

**Định nghĩa:** Thiết kế **hệ thống bao quanh model** để agent làm việc đáng tin cậy trong môi trường thực. Harness không chỉ là pipeline orchestration, mà còn bao gồm những thành phần như **system prompt, tools, middleware, skills, memory, sub-agent config, execution constraints và feedback loop**.

| Thành phần | Mô tả |
|------------|-------|
| **Mối quan hệ** | Harness là superset của Prompt và Context |
| **Mục tiêu** | Tăng reliability, khả năng tự sửa lỗi, và chất lượng thực thi trên task dài |
| **Kỹ thuật** | Pipeline, Tooling, Middleware, Memory, Generator-Evaluator, Feedback Loop |

**Những năng lực thường nằm trong Harness:**

```
1. Hierarchical Planning   → Goal → Task → Action (nhiều cấp độ)
2. Conditional Branching   → Plan thay đổi theo state (if X → A, else → B)
3. Replanning              → Step fail → sửa step đó, không restart
4. Plan Verification       → Verify plan trước khi execute
5. Tooling Surface         → Agent có thể dùng tool gì, mô tả ra sao
6. Middleware & Guards     → Chèn kiểm soát vào request/response/tool loop
7. Long-term Memory        → Giữ bài học, convention, state qua nhiều vòng
8. Feedback Loop           → Test/lint/verify xong mới chấp nhận output
```

**Ví dụ Harness ở mức thực tế:**

```
Goal: Build notification system
├── System prompt: quy định coding style, scope, cách báo cáo
├── Tools: read/write/bash/test runner
├── Middleware: chặn output lỗi format, bắt retry khi command fail
├── Memory: ghi lại conventions và bug patterns đã gặp
├── Sub-agent config: tách planner / implementer / reviewer
└── Feedback loop: chạy test → fail thì quay lại sửa

Nếu Task 2 fail → không cần restart từ đầu; harness có thể replan đúng bước lỗi.
```

**Điểm quan trọng:** Ở mức production, harness không chỉ "nói agent phải làm gì" mà còn **định hình môi trường để agent khó đi sai hơn**.

---

## ⚖️ So Sánh 3 Tầng

| Tầng | Tập trung | Bản chất | Kỹ thuật | Mức tự chủ |
|------|-----------|----------|----------|------------|
| **Harness** | Thiết kế môi trường làm việc cho agent | Superset | Pipeline, Tools, Middleware, Memory, Feedback Loop | **Cao** |
| **Context** | Cung cấp Kiến thức | Superset | RAG, Context Files, Progressive Disclosure | **Trung bình** |
| **Prompt** | Hành động & Gợi ý | Subset | Chain-of-Thought, Zero-shot, Few-shot | **Thấp** |

> 💡 **Điểm mấu chốt:** Prompt tốt không phát huy hết tác dụng nếu thiếu Context. Nhưng ngay cả khi có đúng context, agent vẫn có thể thất bại nếu harness kém — ví dụ tool surface mơ hồ, không có memory, thiếu middleware, hoặc không có feedback loop để tự sửa lỗi.

---

## 💡 Ví Dụ Thực Tế: Sửa Bug Trong API

**Yêu cầu:** Agent tìm và sửa bug trong endpoint `/api/users`.

---

### ❌ Tầng 1: Chỉ Prompt Engineering

**Prompt yếu:**
```
"Sửa bug trong code của tôi"
```

**Vấn đề:** Agent không biết:
- Project structure
- Đã có tests chưa
- Conventions của team

---

### ✅ Tầng 2: + Context Engineering

**Bổ sung context:**

```
├── Project: Python FastAPI backend
├── File: src/api/users.py (đã đọc)
├── Error: IndexError: list index out of range
├── Tests: tests/api/test_users.py (PASS)
└── Conventions: Black formatter, pytest
```

**Output:**
```
✅ Sửa: thêm check cho empty list
✅ Chạy tests: 12 pass, 0 fail
✅ Format: Black compliant
```

---

### 🚀 Tầng 3: + Harness Engineering

**Hệ thống tự động hóa:**

```
1. Agent đọc file + context
2. Agent dùng tools để sửa bug
3. Middleware kiểm tra lỗi định dạng / command failures
4. Harness tự động chạy: pytest
5. Nếu FAIL → Feedback loop → Agent sửa lại
6. Nếu cần → ghi lesson vào memory cho vòng sau
7. Nếu PASS → Kết thúc ✅
```

**Điểm khác biệt:** Không chỉ có orchestration. Harness còn quyết định agent có tool gì, bị ràng buộc ra sao, có nhớ được gì không, và có cơ chế tự kiểm tra trước khi trả output hay không.

---

### 📊 So Sánh Output Theo Tầng

| Tầng | Prompt | Context | Harness | Kết quả |
|------|--------|---------|---------|---------|
| **1** | "Sửa bug" | ❌ | ❌ | Code được sửa, không biết đúng không |
| **2** | "Sửa bug" | ✅ | ❌ | Code sửa đúng context, nhưng vẫn dễ fail khi chạy thật |
| **3** | "Sửa bug" | ✅ | ✅ | Code sửa + tested + verified + có khả năng tự sửa lỗi 🚀 |

---

## 🎯 Checklist Cho Agent Workflow

```
□ Prompt có Role + Task + Output Format + Constraints không?
□ Context đủ để Agent hiểu project chưa?
□ Harness có tool surface rõ ràng không?
□ Có middleware / guardrails để chặn lỗi phổ biến không?
□ Có feedback loop để tự verify không?
□ Có memory hoặc cách giữ bài học qua nhiều vòng không?
□ Khi nào cần dùng Prompt vs Context vs Harness?
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu và định nghĩa được 3 tầng Engineering
- [ ] Giải thích được mối quan hệ `Prompt ⊂ Context ⊂ Harness`
- [ ] Biết harness không chỉ là pipeline, mà còn gồm tools, middleware, memory, feedback loop
- [ ] Áp dụng được 3 tầng để phân tích một workflow thực tế
- [ ] Biết khi nào cần dùng Prompt vs Context vs Harness

---

## 🔗 Liên Quan

- **Thực hành Prompt:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)
- **Thực hành Context:** [PRACTICAL/02: Quản Lý Context](../PRACTICAL/02-quan-ly-context.md)
- **Chuẩn Agent Context:** [FUNDAMENTALS/05: Agents.md — Chuẩn Mở](./05-agents-md-chuan-muc.md)
- **Ứng dụng thực tế:** [USE-CASES/01: Debug Code](../USE-CASES/01-debug-code.md)