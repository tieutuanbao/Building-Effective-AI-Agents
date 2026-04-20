# Phân Tách Task Phức Tạp

---

## 🔥 Thực Trạng

Đưa task lớn cho agent, nó "choáng ngợp". Output không chi tiết, bỏ sót nhiều phần, hoặc quality không đồng đều. Bạn nhận được một phiên bản "half-baked", thiếu edge cases, không có error handling.

→ **Task decomposition** là kỹ năng cốt lõi — chia nhỏ để conquer.

---

## 🎯 Mục Tiêu

- [ ] Viết task breakdown trước khi giao task lớn
- [ ] Xác định atomic tasks có thể hoàn thành trong một response
- [ ] Phân biệt sequential vs parallel execution
- [ ] Verify sau mỗi step trước khi tiếp task tiếp theo
- [ ] Dùng checklist để track progress

---

## 📖 Core Concepts

### Task Decomposition

Phân chia task lớn thành các atomic tasks nhỏ hơn. Mỗi atomic task nên:

- Có một mục tiêu rõ ràng
- Hoàn thành được trong một "lần gọi" agent
- Có output có thể verify được

### Atomic Tasks

Task nhỏ nhất có thể self-contained. Thay vì "viết app", thành "viết function X", "viết test Y", "setup config Z".

### Sequential vs Parallel Execution

| Type | Description | When |
|------|-------------|------|
| **Sequential** | Task A → Task B → Task C | Khi có dependency |
| **Parallel** | Task A, Task B, Task C | Khi độc lập, có thể chạy đồng thời |

### Dependency Management

Biết task nào phụ thuộc task nào. Task B cần output của Task A thì phải chạy sau.

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Viết Task Breakdown Trước

Trước khi giao task lớn:

```
TASK: Build authentication system

Breakdown:
1. Design database schema (User table)
2. Write password hashing utility
3. Implement registration endpoint
4. Implement login endpoint
5. Write JWT token generation
6. Add authentication middleware
7. Write integration tests

Dependencies:
- Task 2, 3, 4 dependent on Task 1
- Task 5 dependent on Task 3
- Task 7 dependent on Task 5
```

---

### 2. Mỗi Task Một Prompt

Thay vì một prompt dài cho cả project:

```
Prompt 1: Design database schema
Prompt 2: [Sau khi 1 xong] Implement password utility
Prompt 3: [Sau khi 1 xong] Implement registration
...
```

---

### 3. Verify Sau Mỗi Step

Sau mỗi atomic task:

```
Task 1 hoàn thành. Verify:
- Schema có user_id, email, password_hash?
- Index trên email?
- Relationships đúng?

Nếu OK, tiếp Task 2.
```

---

### 4. Dùng Checklist

```
Authentication System Checklist:
[x] Database schema
[x] Password utility
[ ] Registration endpoint
[ ] Login endpoint
[ ] JWT generation
[ ] Middleware
[ ] Tests
```

---

### 5. Nhận Ra Khi Agent Overwhelm

Dấu hiệu:

- Agent bắt đầu với "Sure, I'll do all of this..."
- Output bắt đầu không chi tiết
- Missing edge cases ngay từ đầu

**Khi thấy dấu hiệu: stop, decompose further.**

---

## 📝 Ví Dụ Thực Tế: 3 Patterns

### Pattern 1: Sai — Một Prompt Lớn

```
Build cho tôi một REST API cho blog có:
- User authentication
- CRUD posts
- Comments
- Categories
- Tags
- Search
- Pagination
- File upload
- Email notifications
- Rate limiting

[Output: generic, superficial, missing details]
```

### Pattern 2: Đúng — Phân Ra Từng Bước

```
PHASE 1: Foundation
Task 1: Database schema (users, posts, comments, categories, tags)
Task 2: Basic CRUD skeleton for posts
Task 3: User authentication (register, login, JWT)

PHASE 2: Features
Task 4: Comments system
Task 5: Categories & Tags
Task 6: Search với full-text indexing
Task 7: Pagination

PHASE 3: Polish
Task 8: File upload cho featured images
Task 9: Email notifications
Task 10: Rate limiting

[Output: detailed, well-thought, mỗi phần hoàn chỉnh]
```

### Pattern 3: Parallel Where Possible

```
Task A: Design database schema
Task B: Setup project structure
Task C: Create CI/CD pipeline

[A, B, C independent -> chạy song song]

Sau đó:
Task D: Implement features (dependent on A, B)
Task E: Deploy configuration (dependent on C)
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Giao task lớn không breakdown | Agent overwhelmed, output half-baked | Viết breakdown trước, xác định atomic tasks |
| Không verify sau mỗi step | Lỗi propagate, phải rewrite nhiều | Verify mỗi task trước khi continue |
| Không xác định dependencies | Task chạy sai thứ tự | Map dependencies trước khi execute |
| Atomic task vẫn còn lớn | Agent vẫn overwhelmed | Decompose further: sub-task < 20 lines expected output |
| Checklist không được dùng | Progress không rõ ràng | Dùng checklist cho mỗi phase |

---

## ✅ Checkpoint

- [ ] Trước khi giao task lớn, bạn có viết breakdown không?
- [ ] Mỗi atomic task có hoàn thành được trong một response không?
- [ ] Dependencies được xác định và respected?
- [ ] Có verify sau mỗi step trước khi tiếp task tiếp theo?
- [ ] Checklist có được dùng để track progress?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/09](./09-cac-workflow-thuong-gap.md) | Các Workflow — workflow patterns cho task decomposition |
| [USE-CASES/08](../USE-CASES/08-planning-estimation.md) | Planning & Estimation — planning thực chiến |
| [PRACTICAL/06](./06-verification-habits.md) | Verification — verify sau mỗi step |