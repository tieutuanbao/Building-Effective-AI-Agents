# Nguyên Tắc Delegation — Khi Nào Giao, Khi Nào Giữ

> Bạn đang chia sẻ: giao việc cho Agent xong, nó làm lung tung. Hoặc tự làm hết mọi thứ vì sợ Agent làm sai. Đây là vấn đề về **delegation** — biết khi nào giao, khi nào giữ lại.

---

## 🔥 Thực Trạng

Bạn có thể đã gặp:

- 😰 Giao việc cho Agent xong, nó làm lung tung
- 🔒 Tự làm hết mọi thứ vì sợ Agent làm sai
- 🤦 Cứ hỏi Agent cái gì cũng được, nhưng kết quả không tốt
- ❓ Chần chừ không biết task nào nên giao, task nào nên tự làm

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Biết khi nào NÊN và KHÔNG NÊN delegate
- ✅ Hiểu Task Size Matters — nhỏ quá hoặc lớn quá đều không tốt
- ✅ Tránh 3 anti-patterns phổ biến về delegation

---

## 🤔 Tại Sao Ta Ngại Delegation?

| Lý do | Giải thích |
|-------|------------|
| **Loss aversion** | Sợ mất control |
| **Perfectionism** | Muốn everything đúng theo ý mình |
| **Context gap** | Agent không có full context như ta |
| **Trust issues** | Đã bị Agent làm sai trước đó |

**Ngược lại — Tại sao ta delegation quá nhiều?**

| Lý do | Giải thích |
|-------|------------|
| **Overwhelm** | Quá nhiều thứ cần làm |
| **Misplaced confidence** | Nghĩ Agent giỏi hơn thực tế |
| **Lazy delegation** | "Cứ hỏi Agent đi" |

→ **Cả hai extreme đều có hại.** Delegation hiệu quả là một skill.

---

## ✅ KHI NÀO NÊN Delegation

| Characteristics | Tại sao |
|----------------|--------|
| **Repetitive tasks** | Agent không chán, làm đúng pattern |
| **Well-defined output** | Agent biết target là gì |
| **Research-heavy** | Agent đọc nhanh hơn nhiều |
| **Boilerplate code** | Agent viết nhanh, ít sai sót |
| **Documentation** | Agent generate nhanh |
| **Debug familiar errors** | Agent pattern-match tốt |

---

## ❌ KHI NÀO KHÔNG NÊN Delegation

| Characteristics | Tại sao |
|----------------|--------|
| **Novel architecture** | Cần creative judgment, domain expertise |
| **Ambiguous requirements** | Agent sẽ guess sai |
| **Business-critical decisions** | Cần human context |
| **Security-sensitive** | Risk quá cao nếu sai |
| **First time exploration** | Cần hiểu trước, không đủ context |

---

## ⚠️ DELEGATE CẨN THẬN Khi

| Characteristics | Cần làm gì |
|----------------|-----------|
| **Requires domain expertise** | Agent cần full context + human verify |
| **Complex coordination** | Agent cần clear boundaries |
| **Long-term maintainable** | Agent cần conventions + human review |

---

## 📏 Task Size Matters

| Task size | Agent suitable? | Why |
|----------|----------------|-----|
| **Too small** (< 5 min) | ❌ | Overhead cao hơn benefit |
| **Medium** (15-60 min) | ✅ | Vừa đủ để Agent shine |
| **Large** (> 2 hours) | ⚠️ | Cần break into chunks |

---

## ❌ 3 Anti-Patterns Về Delegation

### Anti-pattern 1: "Cứ hỏi Agent cái gì"

```markdown
# Bad ❌
"Tôi muốn build một startup, nói tôi biết làm gì"

# Good ✅
"Tôi có ý tưởng về [product].
Trước mắt tôi cần:
1. Research market size cho [specific niche]
2. Danh sách competitors chính
3. Technical stack recommendation
Chỉ làm research, không implement."
```

### Anti-pattern 2: Dump everything vào một prompt

```markdown
# Bad ❌
"Đây là 50 files code, sửa hết bug trong đó"

# Good ✅
"Trong codebase hiện tại, có 3 bug areas chính:
1. Auth - không redirect sau login
2. API - endpoint /users trả về 500
3. UI - form không validate
Chúng ta sẽ fix từng cái. Bắt đầu với Auth."
```

### Anti-pattern 3: Delegate mà không verify

```markdown
# Bad ❌
"Agent làm đúng hết rồi, perfect"

# Good ✅
"Code mới được generated. Tôi cần verify:
□ Tests pass
□ Logic đúng với requirements
□ No security issues
□ Consistent với existing patterns"
```

---

## 🎯 Decision Framework

```
Bạn có task cần làm
│
├── Task đã có clear spec?
│   ├── YES → Well-defined?
│   │         ├── YES → Delegate to Agent
│   │         └── NO → Human does (cần làm rõ spec trước)
│   └── NO → Agent explore/troubleshoot trước
│             Sau đó define spec
│
└── Complex?
    ├── YES → Break into smaller chunks
    └── NO → OK với agent help
```

---

## 💡 Ví Dụ Thực Tế: Refactoring Module

**Scenario: Refactoring một module**

```markdown
# Bad ❌ — Delegation quá nhiều, không clear
"Refactor toàn bộ auth module đi"

# Good ✅ — Clear spec, human does high-level design
"Auth module hiện tại có 3 issues:
1. Password stored plain text
2. No refresh token
3. Session không timeout

Tôi muốn:
1. Đầu tiên bạn đọc code và suggest approach cho từng issue
2. Tôi sẽ approve approach
3. Sau đó bạn implement từng phần, tôi verify sau mỗi step

Bắt đầu với issue #1."
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu khi nào NÊN và KHÔNG NÊN delegate
- [ ] KHÔNG dump everything một lần — chia nhỏ
- [ ] Well-defined output = clear acceptance criteria
- [ ] LUÔN verify output, đặc biệt với security-critical tasks
- [ ] Delegate theo chunks, không phải one-shot

---

## 🔗 Liên Quan

- **Tiếp theo:** [03. Sự Hợp Tác Hiệu Quả](./03-su-hop-tac-hieu-qua.md)
- **Thực hành:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)
- **Memory:** [PRACTICAL/04: Session Hygiene](../PRACTICAL/04-session-hygiene.md)