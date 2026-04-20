# Viết Prompt Hiệu Quả

---

## 🔥 Thực Trạng

Bạn viết prompt, agent trả lời lạc đề. Hoặc output format không như mong đợi. Hoặc agent hỏi lại thông tin đã cung cấp.

**Nguyên nhân gốc:** Prompt không rõ ràng, thiếu cấu trúc, và không định hướng agent một cách chính xác.

→ Prompt yếu → Output lệch hướng → Tốn token để sửa → Chi phí tăng.

---

## 🎯 Mục Tiêu

- [ ] Viết prompt theo cấu trúc 5 thành phần (ROLE/TASK/CONTEXT/OUTPUT/CONSTRAINT)
- [ ] Phân biệt khi nào dùng **Chain-of-Thought** vs **Few-Shot** vs **Role Assignment**
- [ ] Tránh 5 pitfalls phổ biến khi viết prompt
- [ ] Tối ưu prompt existing để agent output đúng expected format
- [ ] Hiểu cách prompt tốt kết hợp với context management

---

## 📖 Prompt Structure: 5 Thành Phần

Prompt hiệu quả gồm **5 phần bắt buộc**:

```
[ROLE]      → Agent là ai? (Perspective)
[TASK]      → Cần làm gì? (Action verb)
[CONTEXT]   → Thông tin nền cần thiết (Background)
[OUTPUT]    → Format trả về mong đợi (Format)
[CONSTRAINT]→ Ràng buộc nếu có (Limitations)
```

> ⚠️ **Thiếu bất kỳ phần nào → Prompt yếu → Agent đoán.**

---

## 🧩 Role Assignment

Gán role cụ thể giúp agent có "perspective" phù hợp.

| Yếu | Mạnh |
|-----|------|
| "viết code" | "Bạn là Senior Backend Engineer với 10 năm kinh nghiệm Python" |
| "phân tích lỗi" | "Bạn là DevOps Engineer chuyên về debugging Docker containers" |
| "tóm tắt" | "Bạn là Technical Writer chuyên viết docstring cho Python" |

> 💡 **Tip:** Role càng cụ thể → Agent càng hiểu mức độ chi tiết mong đợi.

---

## 🧩 Chain-of-Thought vs Few-Shot

| Kỹ thuật | Khi nào dùng | Ví dụ |
|----------|--------------|-------|
| **Chain-of-Thought (CoT)** | Task cần reasoning, logic từng bước | "Giải thích tại sao thuật toán này là O(n²)" |
| **Few-Shot** | Task cần pattern cụ thể | "Viết docstring theo format Google style" |
| **Role Assignment** | Task cần perspective đặc biệt | "Bạn là Security Engineer, review code này" |

### CoT prompt mẫu:

> Hãy giải quyết bài toán theo 3 bước:
> 1. Phân tích input và constraints
> 2. Đề xuất thuật toán
> 3. Implement code
>
> Show reasoning trước khi đưa ra final solution.

### Few-shot prompt mẫu:

Viết docstring theo format sau:

```python
def func(param: str) -> bool:
    """
    Mô tả ngắn gọn chức năng.

    Args:
        param: Mô tả tham số

    Returns:
        Mô tả giá trị trả về
    """
```

Hãy viết docstring cho function sau theo format trên.

---

## 🧩 Output Format Specification

Luôn chỉ định **rõ ràng và cụ thể**.

| Mơ hồ | Cụ thể |
|-------|--------|
| "liệt kê" | "Liệt kê dạng bullet points, mỗi point không quá 20 từ" |
| "code" | "Code Python với type hints và docstring" |
| "giải thích" | "Giải thích ngắn gọn trong 2-3 câu, dùng ngôn ngữ kỹ thuật" |
| "trả lời" | "Trả lời dạng JSON: {status: string, result: array}" |

---

## 🛠️ Best Practices

### 1. Viết Prompt Theo Template

```
[ROLE] Bạn là [vai trò cụ thể]
[TASK] Nhiệm vụ: [mô tả chính xác bằng động từ]
[CONTEXT] Thông tin: [context liên quan — CHỈ liên quan]
[OUTPUT] Format: [format cụ thể]
[CONSTRAINT] Ràng buộc: [các giới hạn nếu có]
```

**Ví dụ hoàn chỉnh:**

```
[ROLE] Bạn là Senior Python Backend Engineer
[TASK] Viết function sort một list các số nguyên theo thứ tự tăng dần
[CONTEXT] Input: list có thể rỗng, chứa số nguyên bất kỳ (âm, dương, trùng lặp)
[OUTPUT] Trả về list đã sort
[CONSTRAINT] Không dùng built-in sort(), viết thuật toán từ đầu
[FORMAT] Code Python, có docstring và type hints

Ví dụ:
Input: [3, 1, 4, 1, 5, 9]
Output: [1, 1, 3, 4, 5, 9]
```

---

### 2. Chia Nhỏ Thay Vì Gộp Chung

| ❌ Một prompt dài | ✅ Nhiều prompt nhỏ |
|------------------|---------------------|
| "Viết API, test, và documentation cho module này" | Prompt 1: Viết API → Prompt 2: Viết test → Prompt 3: Viết docs |
| Agent hoảng, làm half-baked | Agent tập trung, làm tốt từng bước |

> 📌 **Nguyên tắc:** Mỗi prompt = một task rõ ràng.

---

### 3. Dùng Delimiters Cho Code

Khi yêu cầu agent viết code, dùng delimiters để phân tách rõ ràng phần code vs phần yêu cầu:

**Ví dụ:**

Triển khai function sau:

```python
# [mô tả function]
def example():
    pass
```

> 💡 **Tip:** Dùng triple backticks để agent hiểu đâu là code cần refactor, đâu là yêu cầu.

---

### 4. Chỉ Định Độ Chi Tiết

Nói rõ mức độ chi tiết bạn mong đợi:

- → "liệt kê 3 options" (không hơn, không kém)
- → "giải thích ngắn gọn trong 2 câu" (cụ thể số câu)
- → "phân tích sâu từng bước" (yêu cầu reasoning)

---

### 5. Thêm Constraint Để Tránh Hallucination

> "Nếu không đủ thông tin, hỏi lại thay vì đoán."

**Constraint phổ biến:**

| Constraint | Mục đích |
|------------|----------|
| "Không dùng built-in sort()" | Kiểm soát implementation |
| "Nếu không chắc, hỏi lại" | Tránh hallucination |
| "Chỉ dùng thư viện stdlib" | Kiểm soát dependencies |
| "Format: JSON only" | Đảm bảo output parseable |

---

## 📝 Ví Dụ Thực Tế: 4 Patterns

### Pattern 1: Yêu Cầu Code

**❌ Prompt yếu:**

```
Viết function sort một array
```

**✅ Prompt mạnh:**

```
[ROLE] Bạn là Python developer
[TASK] Viết function sort một list các số nguyên theo thứ tự tăng dần
[CONTEXT] Input: list có thể rỗng, chứa số nguyên bất kỳ (âm, dương, trùng lặp)
[OUTPUT] Trả về list đã sort, không mutate list gốc
[CONSTRAINT] Không dùng built-in sort(), viết thuật toán từ đầu
[FORMAT] Code Python, có docstring và type hints

Ví dụ:
Input: [3, 1, 4, 1, 5, 9]
Output: [1, 1, 3, 4, 5, 9]
```

---

### Pattern 2: Yêu Cầu Debug

**❌ Prompt yếu:**

```
Code này bị lỗi, sửa giúp tôi.
```

**✅ Prompt mạnh:**

```
[ROLE] Bạn là Senior Debug Engineer
[TASK] Tìm và sửa lỗi trong code sau
[CONTEXT]
- Ngôn ngữ: Python 3.9
- Thư viện: pandas, numpy
- Lỗi: "IndexError: list index out of range" khi chạy line 42
[OUTPUT] Trả về code đã sửa + giải thích nguyên nhân lỗi
[CONSTRAINT] Chỉ sửa phần bị lỗi, không thay đổi logic chính
[FORMAT] Code + comment giải thích tại sao sửa như vậy
```

---

### Pattern 3: Yêu Cầu Brainstorm

**❌ Prompt yếu:**

```
Gợi ý cách cải thiện performance.
```

**✅ Prompt mạnh:**

```
[ROLE] Bạn là System Architect
[TASK] Đề xuất 3 cách cải thiện performance cho API endpoint
[CONTEXT]
- Current: 500 req/s, p99 latency 200ms
- Target: 1000 req/s, p99 latency < 50ms
- Tech stack: Python, FastAPI, PostgreSQL
[OUTPUT] Liệt kê 3 options, mỗi option gồm: tên, cách implement, trade-off, estimated improvement
[CONSTRAINT] Ưu tiên options không cần thay đổi infrastructure hiện tại
[FORMAT] Dạng bảng:

| Option | Implementation | Trade-off | Improvement |
|--------|---------------|-----------|-------------|
| 1. ... | ... | ... | ... |
```

---

### Pattern 4: Yêu Cầu Viết Docs

**❌ Prompt yếu:**

```
Viết documentation cho API này.
```

**✅ Prompt mạnh:**

```
[ROLE] Bạn là Technical Writer
[TASK] Viết documentation cho API endpoint sau
[CONTEXT]
- Endpoint: POST /api/v1/users
- Input: {name: string, email: string, age: int}
- Output: {id: string, name: string, email: string}
[OUTPUT] Documentation hoàn chỉnh gồm:
  - Mô tả ngắn (1-2 câu)
  - Request parameters (bảng)
  - Response format (bảng)
  - Error codes (bảng)
  - Example request/response
[FORMAT] Markdown, có code blocks cho examples
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Prompt quá dài với nhiều task | Agent hoảng, làm half-baked | Chia nhỏ: mỗi prompt = một task |
| Không chỉ định format cụ thể | Output không parseable hoặc sai cấu trúc | Yêu cầu lại format: "Trả về JSON với schema..." |
| Thiếu constraint → hallucination | Agent đoán khi thiếu context | Thêm: "Nếu không chắc, hỏi lại thay vì đoán" |
| Role không phù hợp | Agent thiếu perspective đúng | Đổi role cụ thể hơn: "Senior" thay vì "Developer" |
| Không có example cho task phức tạp | Agent bắt chước pattern sai | Thêm 1-2 Few-shot examples |

---

## ✅ Checkpoint

- [ ] Prompt có chỉ rõ **Role** không? Agent có thể đóng vai đó không?
- [ ] **Task description** có động từ rõ ràng (viết, phân tích, so sánh...)?
- [ ] **Output format** có cụ thể không (markdown, JSON, bullet points...)?
- [ ] Bạn đã cung cấp **example** nếu task phức tạp?
- [ ] **Constraint** có được nêu rõ để tránh agent đi tắt?
- [ ] Prompt có dưới **50 lines** không? (prompt dài → agent ignore)

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/02](./02-quan-ly-context.md) | Quản lý Context — kết hợp với prompt tốt |
| [PRACTICAL/04](./04-session-hygiene.md) | Session Hygiene — prompt trong session dài |
| [USE-CASES/01](../USE-CASES/01-debug-code.md) | Debug Code — prompt cho debugging |
| [PRACTICAL/06](./06-verification-habits.md) | Verification — đảm bảo output đúng |