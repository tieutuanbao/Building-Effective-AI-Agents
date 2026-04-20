# Các Workflow Thường Gặp

> 💡 **Bài này là bản đồ tổng quan.** Đọc sau khi hoàn thành các bài 01-08. Xem [USE-CASES/](../USE-CASES/) cho workflow chi tiết từng use case.

---

## 🔥 Thực Trạng

Bạn muốn làm gì đó với agent nhưng không biết nên bắt đầu từ đâu. Hoặc cứ làm theo một cách, kết quả không tốt. Hoặc không biết workflow nào phù hợp cho tình huống cụ thể.

→ **Chọn đúng workflow = 50% success** — wrong approach dù có prompt tốt vẫn cho kết quả kém.

---

## 🎯 Mục Tiêu

- [ ] Nhận diện workflow phù hợp với từng task type
- [ ] Áp dụng 4 workflow core một cách có hệ thống
- [ ] Biết khi nào kết hợp nhiều workflows
- [ ] Track được đang ở đâu trong workflow

---

## 📖 4 Workflows Core

| Workflow | Khi nào dùng |
|---------|--------------|
| **Explore-Plan-Execute** | Task cần khám phá trước khi hành động |
| **Read-Edit-Verify** | Task chỉnh sửa code |
| **Research-Synthesize-Write** | Task tạo nội dung |
| **Review-Refactor** | Task cải thiện code |

---

## 🧩 Explore-Plan-Execute

Workflow cho task cần khám phá trước khi hành động:

```
1. EXPLORE → Thu thập thông tin, hiểu problem space
2. PLAN → Đề ra solution approach
3. EXECUTE → Thực hiện theo plan
```

---

## 🧩 Read-Edit-Verify

Workflow cho task chỉnh sửa code:

```
1. READ → Hiểu code hiện tại
2. EDIT → Thực hiện thay đổi
3. VERIFY → Chạy test, kiểm tra output
```

---

## 🧩 Research-Synthesize-Write

Workflow cho task tạo nội dung:

```
1. RESEARCH → Thu thập thông tin từ nhiều nguồn
2. SYNTHESIZE → Tổng hợp thành insights
3. WRITE → Viết draft cuối cùng
```

---

## 🧩 Review-Refactor

Workflow cho task cải thiện code:

```
1. REVIEW → Phân tích code hiện tại, tìm issues
2. REFACTOR → Sửa issues theo từng bước
3. VERIFY → Đảm bảo refactor không break gì
```

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Chọn Workflow Phù Hợp Với Task

| Task Type | Workflow |
|-----------|----------|
| Tìm hiểu codebase mới | Explore-Plan-Execute |
| Sửa bug | Read-Edit-Verify |
| Viết blog/docs | Research-Synthesize-Write |
| Cải thiện code quality | Review-Refactor |
| Build feature mới | Explore-Plan-Execute + Read-Edit-Verify |
| Debug complex issue | Explore (gather facts) → Hypothesis → Test |

---

### 2. Explore-Plan-Execute Chi Tiết

```
EXPLORE:
- Codebase structure như thế nào?
- Feature X đang implement ở đâu?
- Tech stack có những gì?

PLAN:
- Approach 1: pros/cons
- Approach 2: pros/cons
- Recommend approach với rationale

EXECUTE:
- Step 1: [cụ thể]
- Step 2: [cụ thể]
```

---

### 3. Read-Edit-Verify Chi Tiết

```
READ:
- Hiểu function X làm gì
- Hiểu dependencies
- Hiểu expected behavior

EDIT:
- Change 1: [cụ thể]
- Change 2: [cụ thể]

VERIFY:
- Unit tests pass?
- Integration tests pass?
- Manual smoke test?
```

---

### 4. Research-Synthesize-Write Chi Tiết

```
RESEARCH:
- Thu thập 5-10 sources
- Ghi chú key points từ mỗi source

SYNTHESIZE:
- Các sources agree hay disagree?
- Key themes nổi bật?
- Contradictions cần resolve?

WRITE:
- Outline
- Draft
- Edit for clarity
```

---

### 5. Review-Refactor Chi Tiết

```
REVIEW:
- Performance issues?
- Security concerns?
- Code smell?
- Test coverage?

REFACTOR (sequential):
- Round 1: Critical bugs
- Round 2: Major improvements
- Round 3: Minor polish

VERIFY (after each round):
- Tests still pass?
- Functionality preserved?
```

---

## 📝 Ví Dụ Thực Tế: 2 Patterns

### Pattern 1: Thêm Payment Vào E-commerce App

```
WORKFLOW: Explore-Plan-Execute -> Read-Edit-Verify

[EXPLORE]
- Current checkout flow?
- Existing payment integration?
- Database schema for orders?

[PLAN]
- Option 1: Stripe direct (complex, full control)
- Option 2: Stripe Checkout (simpler, less control)
- Recommend: Option 2 vì team nhỏ

[EXECUTE + VERIFY]
Task 1: Setup Stripe account + API keys -> verify
Task 2: Create checkout session endpoint -> verify
Task 3: Add webhook handler -> verify
Task 4: Update order status on success -> verify
```

### Pattern 2: Viết Technical Blog Post

```
WORKFLOW: Research-Synthesize-Write

[RESEARCH]
- Đọc 5 bài về topic
- Note: key concepts, examples,争议 points

[SYNTHESIZE]
- Common themes across sources
- Unique angle cho bài này
- Structure for the post

[WRITE]
- Introduction
- Main concepts (3 sections)
- Code examples
- Conclusion
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Dùng 1 workflow cho tất cả tasks | Kết quả không tối ưu | Match workflow với task type |
| Explore không đủ thông tin | Plan bị sai, execute fail | Dành đủ thời gian explore trước |
| Skip verify step | Lỗi discovered quá muộn | Verify sau mỗi step quan trọng |
| Kết hợp workflow không đúng | Workflow phức tạp không cần thiết | Start simple, combine only when needed |
| Không track đang ở đâu | Context drift, mất orientation | Ghi lại checkpoint sau mỗi phase |

---

## ✅ Checkpoint

- [ ] Bạn có nhận diện được workflow nào phù hợp cho task hiện tại?
- [ ] Explore phase có đủ thông tin trước khi plan/execute?
- [ ] Verify có được thực hiện sau mỗi step quan trọng?
- [ ] Khi task thay đổi scope, workflow có được điều chỉnh không?
- [ ] Bạn có giữ track của đang ở đâu trong workflow?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/01](./01-viet-prompt-hieu-qua.md) | Viết Prompt — prompt cho từng workflow |
| [PRACTICAL/08](./08-phan-ra-task.md) | Phân Tách Task — decompose trước khi workflow |
| [USE-CASES/](../USE-CASES/) | Use Cases — workflow chi tiết từng scenario |