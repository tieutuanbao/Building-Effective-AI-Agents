# Quản Lý Chi Phí

---

## 🔥 Thực Trạng

Cuối tháng nhận bill API cao bất thường. Không biết tại sao token usage lại lớn như vậy. Không theo dõi được session nào tốn nhiều tokens. Model đắt tiền được dùng cho task đơn giản có thể dùng model rẻ hơn.

→ Token budgeting là kỹ năng cần thiết — không phải optional mà là **bắt buộc** khi dùng AI agent production.

---

## 🎯 Mục Tiêu

- [ ] Theo dõi token usage mỗi session
- [ ] Đặt budget trước khi bắt đầu task lớn
- [ ] Chọn model phù hợp với độ phức tạp của task
- [ ] Tối ưu prompt để giảm tokens mà không mất chất lượng
- [ ] Summary thay vì keep full context khi có thể

---

## 📖 Core Concepts

### Token Là Gì

Token là đơn vị xử lý ngôn ngữ. Mỗi word tiếng Anh ~ 1.25 tokens. Tiếng Việt tốn nhiều tokens hơn. Cả input và output đều tính tokens.

### Token Budgeting

Đặt ra giới hạn token cho mỗi task/session. Theo dõi usage để không vượt budget.

### Model Selection for Cost Efficiency

Không phải task nào cũng cần model đắt nhất:

| Task Complexity | Model Recommendation |
|----------------|---------------------|
| Simple tasks (format text, simple edits) | Cheapest model |
| Complex tasks (reasoning, code) | Mid-range model |
| Very complex (multi-step planning) | Most capable model |

### Context Caching

Một số provider cho phép cache lại context đã dùng, không phải trả tiền lại cho phần trùng lặp.

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Theo Dõi Token Usage

Mỗi response thường show token usage. Hãy để ý và ghi lại:

```
Session này đã dùng:
- Input tokens: 12,000
- Output tokens: 8,500
- Total: 20,500 tokens
```

---

### 2. Đặt Budget Cho Task

```
Task này budget: 50,000 tokens.
Nếu approach cần nhiều hơn, hãy thông báo trước khi tiếp tục.
```

---

### 3. Dùng Model Phù Hợp

| Task | Model phù hợp | Tại sao |
|------|---------------|---------|
| "Fix typo trong đoạn này" | Cheapest | Không cần reasoning |
| "Viết function sort" | Mid-range | Cần code generation |
| "Redesign entire API architecture" | Premium | Cần complex planning |

---

### 4. Tối Ưu Prompt Để Giảm Tokens

Thay vì:
```
Hãy giải thích chi tiết từng bước của thuật toán sorting.
Bao gồm time complexity, space complexity.
Liệt kê các edge cases.
So sánh với các sorting algorithms khác.
```

Dùng:
```
Explain quicksort: algorithm steps, Big-O, edge cases. Max 10 sentences.
```

---

### 5. Summary Thay Vì Full Context

Khi cần reference nhiều nội dung:

```
Thay vì paste 50 messages vào context
-> Tóm tắt trong 500 tokens
-> Tiết kiệm ~90% tokens
```

---

### 6. Batch Operations

Nhiều simple tasks:

```
❌ Sai: Gọi agent 10 lần cho 10 files riêng
✅ Đúng: 1 call với 10 files, instruction chung
```

---

## 📝 Ví Dụ Thực Tế: 3 Patterns

### Pattern 1: Không Có Budget

```
User: [Unlimited context]
Agent: [Verbose explanation với nhiều iterations]
Bill: $50 cho một task có thể làm với $5
```

### Pattern 2: Có Budget

```
User:
Task: Review code cho 5 files
Budget: 30,000 tokens
Format response: bullet points, concise

Agent:
[Điều chỉnh output để fit budget]
[Tiết kiệm ~60% cost]
```

### Pattern 3: Model Selection

```
Task đơn giản: "Fix typo trong đoạn này"
-> Không cần Claude Opus
-> Dùng Haiku hoặc Sonnet

Task phức tạp: "Redesign entire API architecture"
-> Cần Sonnet hoặc Opus
-> Worth it vì quality impact cao
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Không track token usage | Bill cao bất thường | Check usage sau mỗi session, ghi lại |
| Dùng premium model cho simple task | Lãng phí 90% budget | Match model với task complexity |
| Prompt verbose không cần thiết | Tokens tăng nhanh | Tối ưu: be specific, limit output length |
| Keep full context thay vì summary | Session dài = tokens tăng | Summary sau 20 messages |
| Không đặt budget trước | Task "vô tận" → bill cao | "Budget: X tokens. Nếu cần more, hỏi trước" |

---

## ✅ Checkpoint

- [ ] Bạn có theo dõi token usage của mỗi session không?
- [ ] Bạn có đặt budget trước khi bắt đầu task lớn không?
- [ ] Model selection có phù hợp với task không? (Đắt cho task rẻ?)
- [ ] Prompt có được tối ưu để tránh verbose output không?
- [ ] Bạn có summary/thay vì keep full context khi possible?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [SETUP/03](../SETUP/03-rtk-token-optimizer.md) | RTK Token Optimizer — tự động tối ưu |
| [PRACTICAL/02](./02-quan-ly-context.md) | Quản lý Context — giảm token waste |
| [PRACTICAL/04](./04-session-hygiene.md) | Session Hygiene — tránh session dài không cần thiết |