# Sự Hợp Tác Hiệu Quả với Agent

> Bạn cảm thấy: "Nó làm không như tôi muốn" — sau nhiều lần thử. "Tôi chỉ cần nói một lần" — nhưng Agent vẫn không hiểu. Đây là dấu hiệu của **collaboration pattern** chưa đúng với Agent.

---

## 🔥 Thực Trạng

Bạn có thể đã cảm thấy:

- 😤 "Nó làm không như tôi muốn" — sau nhiều lần thử
- 😓 "Tôi chỉ cần nói một lần" — nhưng Agent vẫn không hiểu
- 🤔 "Nó thay đổi những thứ không liên quan"
- 😫 "Tôi phải kiểm tra từng dòng" — thay vì trust được

→ Đây là dấu hiệu của **collaboration pattern** chưa đúng với Agent.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Tương tác như team member, không phải command
- ✅ Cung cấp WHAT + WHY, để Agent quyết HOW
- ✅ Feedback cụ thể và actionable
- ✅ Expect iteration (2-4 rounds là normal)

---

## ⚖️ Hai Extreme Về Tương Tác

| Extreme | Behavior | Result |
|---------|----------|--------|
| **Micro-management** | Can thiệp mọi thứ, từng dòng code | Agent frustrated, không tự do làm |
| **Laissez-faire** | "Cứ làm đi" — không guide | Agent làm lung tung, waste time |

→ **Cả hai đều sai.** Cần tìm balance.

---

## 🧠 Mental Model Đúng

```
┌─────────────────────────────────────────────────┐
│  USER = Product Owner                           │
│  ├── Định nghĩa WHAT (cái gì cần làm, tại sao) │
│  ├── Cung cấp context (project, constraints)     │
│  └── Verify output (đảm bảo đúng requirement)   │
├─────────────────────────────────────────────────┤
│  AGENT = Senior Developer                       │
│  ├── Đề xuất HOW (làm thế nào)                  │
│  ├── Execute và implement                        │
│  └── Suggest improvements, alternatives          │
└─────────────────────────────────────────────────┘

📌 ĐÂY LÀ TEAM, không phải Master/Slave
```

---

## 💬 Giao Tiếp Như Với Colleague

```markdown
# Bad ❌ — Command mode
"Sửa bug này ngay"

# Good ✅ — Collaboration mode
"Tôi thấy bug này xảy ra khi [circumstance].
Có 2 cách approach:
A. Fix tại source (cleaner nhưng risky)
B. Add validation layer (safer nhưng có overhead)

Tôi ưu tiên A nhưng cần bạn verify risk.
Nếu A quá risky, fallback sang B."
```

---

## ❌ Sai Lầm Thường Gặp

### 1. Không cung cấp đủ context

```markdown
# Bad - Agent phải đoán
"Sửa cái form"

# Good - Rõ ràng context
"Sửa validate cho form register ở /users/register
Input: email, password, confirmPassword
Validate: email format, password >= 8 chars,
          password == confirmPassword
Error message: hiển thị inline dưới field"
```

### 2. Expect Agent nhớ context từ lâu

```markdown
# Bad - Giả định Agent nhớ
"Giờ sửa phần kia đi"

# Good - Nhắc lại context
"Chúng ta đang làm việc trên auth module.
Bạn đã suggest approach A (JWT refresh tokens).
Tôi đã approve. Hãy implement step 1: generate tokens."
```

### 3. Không cho feedback khi có vấn đề

```markdown
# Bad - Implicity feedback
*Lẳng lặng tạo new conversation*

# Good - Explicit feedback
"Sửa không đúng expectation. Cụ thể:
- Bạn thay đổi logic ở chỗ khác không liên quan
- Error handling chưa đủ
Cần bạn redo từ [specific point]."
```

---

## ✅ Communication Patterns

### 1. Direction = WHAT + WHY (không phải HOW)

```markdown
# Good
"Module này cần handle 10K concurrent users.
WHY: Product sắp launch, scale là ưu tiên.
WHAT: Optimize để handle load.
HOW: Agent tự quyết approach, miễn đạt target."
```

### 2. Specificity = proportional to uncertainty

```markdown
# Khi đã có clear path
"Sử dụng approach A đã discussed. Implement it."

# Khi chưa rõ ràng
"Chúng ta có 3 options. Suggest pros/cons của
mỗi approach, tôi sẽ quyết định."
```

### 3. Feedback = specific + actionable

```markdown
# Bad
"Sai rồi"

# Good
"Output không đúng vì:
1. Logic ở line 42 không handle null case
2. Error message không i18n
Hãy fix cả 2 rồi show lại."
```

---

## 🔄 Iteration Workflow

```
┌──────────┐    Task spec    ┌──────────┐
│   USER   │ ──────────────► │  AGENT   │
│          │                 │          │
│          │ ◄────────────── │ Output   │
└──────────┘    Verify       └──────────┘
      │                             │
      │    "Cần adjust [specific]"  │
      │                             │
      └─────────────────────────────┘
              Iterate until OK
```

> 📌 **Số vòng lặp bình thường:** 2-4 rounds cho simple tasks, 5-10 cho complex.

---

## 💡 Ví Dụ: Viết Function

**Scenario: Viết một function**

```markdown
# Round 1: Initial request
"Viết function parseDate(input: string): Date | null"

# Round 2: Feedback
"Logic đúng, nhưng:
- Chưa handle timezone
- Input '' nên throw error thay vì return null
- Cần unit tests"

# Round 3: Feedback
"Almost there:
- timezone handle đúng rồi
- Nhưng '' return null thay vì throw
  (requirement changed: throw for invalid)
- Tests pass nhưng thêm edge case: '2024-13-01'"

# Round 4: Accept
"Perfect. All requirements met."
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Tương tác như team member, không phải command
- [ ] Cung cấp WHAT + WHY, để Agent quyết HOW
- [ ] Feedback cụ thể và actionable
- [ ] Expect iteration (2-4 rounds là normal)
- [ ] Verify trước khi accept output

---

## 🔗 Liên Quan

- **Tiếp theo:** [04. Giới Hạn Của Agent](./04-gioi-han-cua-agent.md)
- **Thực hành:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)
- **Session:** [PRACTICAL/04: Session Hygiene](../PRACTICAL/04-session-hygiene.md)