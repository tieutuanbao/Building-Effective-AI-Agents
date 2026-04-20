# Học Công Nghệ Mới & Onboard Codebase

## 🔥 Thực Trạng

Bạn join project mới, nhờ agent giải thích codebase. Agent đọc vài file rồi đưa overview: "Đây là REST API với Express, có auth middleware, database PostgreSQL." Nghe có vẻ hợp lý nhưng bạn vẫn không biết user click "Submit Order" thì chuyện gì xảy ra phía dưới. Agent đi surface level, đưa label thay vì explain flow. Bạn hỏi "tại sao order service gọi inventory service trước" thì agent lại bắt đầu đọc file tiếp, không trả lời được.

Vấn đề cốt lõi: agent được train để answer questions, không phải để teach understanding. Kết quả: overview pass nhưng mental model không có.

---

## 🎯 Mục Tiêu

- Trace một feature end-to-end mà không bị ngập context
- Dùng agent như interactive tutor thay vì documentation reader
- Build mental model của codebase bằng cách đi từ entry point, không đi từ overview
- Tránh bị overwhelm khi đọc codebase lớn lần đầu

---

## 🧩 Best Practices

### Core Workflow

```
Entry point → Trace flow → Mental model → Test understanding
    ↑            ↑              ↑              ↑
 Bạn define   Agent trace   Agent summarize  Agent hỏi
 entry point   từng layer    key decisions    lại bạn
```

### Agent Role: Interactive Tutor

Agent TRONG vai trò onboard:
- Hỏi lại bạn sau mỗi 3 bước: "Đã hiểu chỗ này chưa?"
- Dừng lại khi bạn chưa sẵn sàng cho detail tiếp theo
- Correct misunderstanding ngay lập tức thay vì tiếp tục

Agent KHÔNG PHẢI:
- Lecturer đọc slide (one-way, không tương tác)
- Documentation reader (đọc file rồi paste content)
- Architecture diagram generator (vẽ diagram không giải thích)

### Before/After: Interactive Onboard Prompt

**Before** — passive learning:

```
❌ "Explain codebase này giùm tôi"
→ Agent: "Đây là project structure: src/controllers, src/services, src/models..."
→ Bạn: nghe overview xong nhưng không biết gì thêm
```

**After** — interactive trace:

```
✅ "Tôi mới join project. Đang đọc src/.

Explain flow: user click 'Submit Order' → chuyện gì xảy ra end-to-end?

Bắt đầu từ frontend handler, trace qua API → service → DB.
Mỗi layer: file nào, function nào, data transform gì.

SAU MỖI 3 BƯỚC, DỪNG LẠI VÀ HỎI:
'Đã hiểu phần này chưa? Có cần tôi giải thích lại không?'

Nếu tôi nói 'ok' → tiếp tục.
Nếu tôi hỏi → trả lời và đợi tôi confirm.
Nếu tôi nói 'bỏ qua' → skip detail, đi tiếp overview."
```

### Mẫu Interactive Prompt Cho Learning Mới

```
"Tôi muốn hiểu concept: [Ownership trong Rust]

Approach:
1. Explain concept ngắn gọn (2-3 sentences) — không code
2. Nêu analogy từ ngôn ngữ bạn đã biết (Python/JavaScript)
3. Đợi tôi confirm: 'đúng chưa?'
4. Nếu đúng → ví dụ code đơn giản
5. Nếu sai → correct và giải thích tại sao

SAU MỖI BƯỚC, HỎI: 'Đã clear chưa? Hay cần thêm ví dụ?'

Tôi không muốn 10 ví dụ một lần. Một ví dụ → tôi hiểu → next."
```

### Khi nào KHÔNG dùng pattern này

- **Quick lookup**: "syntax của Rust Result type" → không cần interactive tutor, chỉ cần docs
- **Debug session**: đang fix bug, cần trace nhanh → dùng grep thay vì onboard pattern
- **Trusted codebase**: bạn đã hiểu architecture rồi, chỉ cần verify detail

---

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Onboard Codebase Mới — Trace Order Flow

**Prompt:**

```
Tôi mới join project, đang đọc src/.

Trace flow: user click 'Submit Order' → chuyện gì xảy ra end-to-end?

Rules:
- Start từ frontend handler (src/frontend/...)
- Mỗi layer: [file]:[function] → data transform gì
- Không paste code, chỉ paste signature + docstring
- Đi qua: frontend → API route → controller → service → repository → DB

SAU 3 STEPS, DỪNG VÀ HỎI: "Bạn đã hiểu flow chưa? Hay cần giải thích lại?"

Nếu tôi hỏi "tại sao" → trả lời và đợi confirm trước khi đi tiếp.
```

**Result:**

```
✅ Agent trace được: submitOrder() → POST /api/orders → OrderController.create() →
OrderService.create() → InventoryService.checkStock() → OrderRepository.insert()

✅ Agent hỏi đúng lúc: "Đã hiểu chỗ InventoryService check stock trước khi tạo order chưa?"

✅ Agent chỉ paste signature, không paste full body → tiết kiệm context

⚠️ Agent bắt đầu paste quá nhiều → prompt tiếp: "Chỉ paste function signature, không body"
```

---

### Scenario 2: Học Framework Mới — Rust Ownership

**Prompt:**

```
Tôi biết Python và JavaScript, đang học Rust.

Mục tiêu: hiểu Ownership concept

Approach theo từng bước:
1. Explain ngắn: Ownership là gì, tại sao Rust cần nó (30 giây đọc)
2. Analogy: so sánh với Python's garbage collector và JS's reference counting
3. Ví dụ code đơn giản: function nhận value vs borrow
4. Đợi tôi nói "ok" hoặc "chưa hiểu"

SAU MỖI STEP, HỎI: "Đã clear chưa?"

Không đưa 10 ví dụ một lần. Tôi muốn 1 concept → hiểu → next.
```

**Result:**

```
✅ Agent giải thích đúng level: "Ownership = Rust's way để track ai responsible cho memory"
✅ Agent dùng analogy đúng: Python (GC) vs Rust (compile-time tracking)
✅ Agent chờ tôi confirm trước khi đi tiếp

⚠️ Agent muốn đi qua 5 concepts cùng lúc → recovery: "Một concept một lần. Ownership trước."
```

---

## 🚧 Pitfalls & Recovery

### 1. Context Ngập — Agent Paste Toàn Bộ File

**Dấu hiệu:**
- Agent bắt đầu paste code block dài 50+ lines
- Context usage tăng vọt mà bạn chưa hiểu gì thêm
- Bạn thấy "nghe có lý nhưng không nhớ gì"

**Recovery:**
```
"Stop. Chỉ paste:
- Function signature (1 line)
- Docstring (2-3 lines max)
- Input/Output types

KHÔNG paste function body.
Tôi muốn hiểu architecture, không phải đọc code."
```

---

### 2. Surface Level — Agent Explain Line-by-Line Thay vì Architecture

**Dấu hiệu:**
- Agent nói: "function này làm X, function kia làm Y" — không connect
- Bạn hiểu từng function nhưng không hiểu tại sao chúng kết nối
- Không có câu "đây là decision vì..."

**Recovery:**
```
"Dừng. Tôi muốn hiểu ARCHITECTURE trước.
Thay vì line-by-line, explain:
- Tại sao data flow này được thiết kế như vậy
- Decision nào được made ở mỗi layer
- Dependency direction: service nào phụ thuộc service nào, tại sao"

Nếu agent không biết answer: "Note lại, tôi sẽ hỏi maintainer. Đi tiếp phần bạn biết."
```

---

### 3. Overwhelm — Quá Nhiều Detail Khi Bạn Chưa Sẵn Sàng

**Dấu hiệu:**
- Agent đi qua 7 layers trong 1 prompt response
- Bạn mất track từ layer 3 trở đi
- mental model không có hình dạng

**Recovery:**
```
"Chậm lại. Tôi muốn overview TRƯỚC, deep dive SAU.

Hỏi tôi ở mỗi layer:
'Bạn muốn deep dive hay skip qua?'
- Deep dive → giải thích chi tiết + example
- Skip → 1-sentence summary, đi tiếp

Ví dụ:
Layer 1: SubmitOrderButton (frontend) → Submit order form
Layer 2: POST /api/orders (API route) → validate request format

Sau layer 2: hỏi 'Continue deep dive hay skip to summary?'"
```

### Cost Awareness

- **Bad**: Load 10 files cùng lúc → 80k tokens, 0% retain
- **Good**: Trace 3 files → confirm → repeat → 15k tokens, 80% retain

---

## ✅ Checkpoint

### Pattern Cheat Sheet

```
1. ENTRY POINT: "Trace [action] từ [start] qua [layers]"
2. INTERACTIVE: "Sau 3 steps, hỏi tôi 'hiểu chưa?'"
3. SIGNATURE ONLY: "Chỉ paste signature + docstring, không body"
4. ARCHITECTURE FIRST: "Explain decision, không explain line-by-line"
5. PAUSE POINT: "Nếu tôi hỏi 'tại sao' → trả lời và đợi confirm"
```

### Onboard Checklist

- [ ] Define entry point rõ ràng (user action, không phải file list)
- [ ] Agent hỏi "hiểu chưa?" sau mỗi 3 steps
- [ ] Chỉ signature + docstring được paste, không body
- [ ] Architecture explanation trước, line-by-line sau
- [ ] Agent dừng khi bạn overwhelm

## 🔗 Liên Quan

| Bài | Liên quan |
|-----|-----------|
| [PRACTICAL/02](../PRACTICAL/02-quan-ly-context.md) | Quản lý Context — tránh ngập context khi onboard |
| [PRACTICAL/08](../PRACTICAL/08-phan-ra-task.md) | Phân rã Task — break down large codebase thành traceable chunks |

---

## 📌 Bonus: Tool Integration

**Khi nào dùng Context7 cho docs:**
```
"Tôi đang học Rust lifetime syntax.
Dùng Context7 tìm documentation về:
- 'lifetime elision rules'
- 'common compiler errors'
```

**Khi nào dùng Grep cho code search:**
```
"Search codebase: có bao nhiêu places call OrderService.create()?
List ra: [file]:[line] — không cần full context"
```