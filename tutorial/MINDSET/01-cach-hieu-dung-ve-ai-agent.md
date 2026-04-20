# Cách Hiểu Đúng về AI Agent

> Bạn cảm thấy: "Nó không làm như tôi muốn", "Nó quên những gì tôi vừa nói", "Nó làm lung tung" — đây là dấu hiệu của **mental model sai** về cách Agent hoạt động.

---

## 🔥 Thực Trạng

Bạn có thể đã dùng AI Agent và cảm thấy:

- ❌ "Nó không làm như tôi muốn"
- ❌ "Nó quên những gì tôi vừa nói"
- ❌ "Nó làm lung tung không theo kế hoạch"

→ Đây là dấu hiệu của **mental model sai** về cách Agent hoạt động.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Hiểu Agent = Model + Tools + Memory + Orchestration
- ✅ Biết Agent hoạt động theo observe→plan→act loop
- ✅ KHÔNG expect Agent đoán ý — luôn spec rõ ràng
- ✅ Expect iteration, không phải one-shot perfect

---

## ❌ Agent KHÔNG Phải Là Gì

| Sai lầm phổ biến | Thực tế |
|------------------|---------|
| "Nó là trợ lý thông minh" | Nó là **pattern matching** có độ chính xác cao |
| "Nó hiểu ý tôi" | Nó **predict token** tiếp theo dựa trên context |
| "Nó suy nghĩ như con người" | Nó không "suy nghĩ" — nó **tính toán xác suất** |
| "Nó nhớ mọi thứ" | Nó chỉ nhớ trong **context window** hiện tại |

---

## ✅ Agent LÀ Gì

**Agent = Model + Tools + Memory + Orchestration**

```
┌─────────────────────────────────────────────┐
│              AI AGENT                       │
├─────────────────────────────────────────────┤
│  🧠 Model (Brain)     │  LLM để reasoning   │
│  🔧 Tools (Hands)     │  Bash, Read, Edit... │
│  💾 Memory (State)    │  Session context    │
│  🎯 Orchestration     │  Loop: observe→act   │
└─────────────────────────────────────────────┘
```

### Cách Agent Thực Sự Hoạt Động

Agent hoạt động theo vòng lặp:

```
1️⃣ OBSERVE    → Đọc context, hiểu requirement
2️⃣ PLAN       → Nghĩ xem làm gì tiếp
3️⃣ ACT        → Gọi tool hoặc respond
4️⃣ FEEDBACK   → Nhận kết quả từ action
5️⃣ REPEAT     → Quay lại bước 1 cho đến khi done
```

→ Đây là lý do Agent đôi khi có vẻ chậm — nó đang loop qua nhiều steps.

---

## 🎚️ Autonomy Levels — Cấp Độ Tự Chủ

| Level | Mô tả | Ví dụ |
|-------|-------|-------|
| **1** | Reactive — chỉ respond | Basic ChatGPT |
| **2** | With tools — dùng được tools | GPT-4 with browsing |
| **3** | With memory — nhớ được context | Claude Code |
| **4** | With planning — tự plan steps | Complex agents |
| **5** | Fully autonomous | Rare, experimental |

> 🔑 **OpenCode/Claude Code = Level 3-4.** Bạn vẫn cần specify goal rõ ràng.

---

## 🧠 Mental Model Đúng

**Hãy nghĩ về Agent như một:**

- 👨‍💻 **Senior Developer** — execute được, nhưng cần direction rõ ràng
- 📚 **Intern được train kỹ** — làm được nhiều thứ, nhưng cần guidance
- 🔧 **Tool có input/output rõ ràng** — không phải magic box

**ĐỪNG nghĩ Agent là:**

- 🔮 Oracle — biết mọi thứ
- 🧞 Genie — đoán ý bạn
- 🤖 Slave — làm theo mệnh lệnh mà không question

---

## 💡 Cách Tương Tác Đúng

```markdown
# Bad ❌ — Quá mơ hồ
"Làm cho tôi một cái app đẹp"

# Good ✅ — Rõ ràng, có scope
"Viết một React component cho login form:
- Fields: email, password
- Validation: email format, password min 8 chars
- Style: dùng Tailwind CSS
- Không cần backend, chỉ UI"
```

### Nguyên tắc khi giao việc

```
1️⃣  SPEC RÕ RÀNG    → Goal, constraints, output format
2️⃣  CHIA NHỎ        → Chunked tasks, không dump everything
3️⃣  VERIFY OUTPUT   → KHÔNG trust hoàn toàn, luôn check
4️⃣  ITERATE         → Expect nhiều vòng refinement
```

---

## 💡 Ví Dụ Thực Tế: Viết API Endpoint

**Scenario: Viết một API endpoint**

```markdown
# Step 1: Spec trước khi giao
"Tôi cần một POST endpoint cho /users/register"

# Step 2: Sau khi có spec rõ ràng
"Yêu cầu cụ thể:
- POST /api/users/register
- Body: { email, password, name }
- Validate email format
- Hash password với bcrypt
- Return 201 + user object (không password)
- Nếu email tồn tại → return 409
- Viết unit tests cho Happy path và validation errors"

# Step 3: Verify output
□ Code compile được?
□ Logic đúng?
□ Tests pass?
□ Security issues?
```

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu Agent = Model + Tools + Memory + Orchestration
- [ ] KHÔNG expect Agent đoán ý — luôn spec rõ ràng
- [ ] Biết Agent hoạt động theo observe→plan→act loop
- [ ] Expect iteration, không phải one-shot perfect
- [ ] LUÔN verify output trước khi accept

---

## 🔗 Liên Quan

- **Tiếp theo:** [02. Nguyên Tắc Delegation](./02-nguyen-tac-delegation.md)
- **Thực hành:** [PRACTICAL/01: Viết Prompt Hiệu Quả](../PRACTICAL/01-viet-prompt-hieu-qua.md)
- **So sánh tools:** [ECOSYSTEM/02: So Sánh Agent Tools](../ECOSYSTEM/02-so-sanh-agent-tools.md)