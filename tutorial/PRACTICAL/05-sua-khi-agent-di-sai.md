# Sửa Khi Agent Đi Sai Hướng

---

## 🔥 Thực Trạng

Agent đang đi sai nhưng bạn không biết cách can thiệp. Để tiếp tục thì ra kết quả sai. Nhưng nếu reset thì mất context đã có. Hoặc bạn cứ "ừ, đúng rồi" dù biết có vấn đề vì không muốn conflict với agent.

→ Can thiệp không có nghĩa là "cãi nhau" với agent — đó là điều chỉnh hướng đi một cách constructively.

---

## 🎯 Mục Tiêu

- [ ] Nhận diện sớm khi agent đi sai hướng
- [ ] Can thiệp với evidence cụ thể thay vì "Sai rồi"
- [ ] Dùng checkpoint technique để reset về điểm an toàn
- [ ] Yêu cầu agent self-correct thay vì sửa hộ
- [ ] Chunk correction — sửa từng phần nhỏ thay vì reject toàn bộ

---

## 📖 Core Concepts

### Intervention Techniques

Can thiệp không có nghĩa là "cãi nhau" với agent. Đó là việc điều chỉnh hướng đi một cách constructively. Intervention hiệu quả giữ được những gì đúng và chỉ sửa những gì sai.

### State Reset

Đôi khi cần "quay lại" về một checkpoint trước đó. Điều này không phải thất bại, mà là **strategic retreat** để tiến nhanh hơn.

### Direction Correction

Chỉ rõ agent đang đi đúng hay sai. Nếu sai, hướng đi đúng ở đâu. Càng cụ thể, agent càng dễ self-correct.

### Plan Failure vs Execution Failure

| Loại | Biểu hiện | Cách xử lý |
|------|------------|-------------|
| **Execution Failure** | Code bug, syntax error | Debug implementation |
| **Plan Failure** | Step không thể execute vì assumption sai | Sửa plan, không sửa code |
| **Premise Failure** | Goal ban đầu sai | Question goal với human |

**Ví dụ Plan Failure:**
```
Agent plan: "DELETE FROM test_records WHERE created_at < '2024-01-01'"
SQL đúng syntax nhưng FAIL

❌ Sai: "Fix the SQL" (không sửa được vì SQL không sai)
✅ Đúng: "Verify table name" → table name sai trong assumption

→ Sửa PLAN, không sửa CODE
```

### Explicit Grounding

Yêu cầu agent "ground" statements của mình. Thay vì accept mù quáng, đòi hỏi evidence hoặc reasoning.

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Nhận Diện Sớm

Dấu hiệu agent đi sai:

- Agent bắt đầu "hallucinate" (nói những thứ không có thật)
- Kết quả không match expected format
- Agent hỏi lại thông tin đã cung cấp
- Logic không flow hoặc contradictory

---

### 2. Can Thiệp Với Evidence

Không nói "Sai rồi". Nói "Đoạn này không đúng vì [reason]. Hãy xem lại [specific part]."

```
❌ Sai: "Không đúng"
✅ Đúng: "Function này sẽ fail nếu input là empty string. Thêm check ở line 5."
```

---

### 3. Dùng "Checkpoint" Technique

Khi muốn reset về điểm trước đó:

```
Quay lại checkpoint: trước khi implement pagination.
Chúng ta đã agree là dùng cursor-based pagination.
Bây giờ hãy implement từ đó.
```

---

### 4. Yêu Cầu Self-Correction

Thay vì sửa hộ:

```
Hãy xem lại logic của function này. Tìm 3 potential bugs và fix chúng.
```

> 💡 Agent tự tìm và sửa sẽ hiểu vấn đề sâu hơn.

---

### 5. Chunk Correction

Sửa từng phần nhỏ thay vì reject toàn bộ:

```
Phần database schema đúng.
Phần API endpoint đúng.
Phần error handling cần sửa: thêm HTTP 404 response.
```

---

### 6. Dùng "Help Me Understand"

Khi không đồng ý với agent:

```
Tôi không đồng ý với approach này vì [lý do].
Nhưng trước khi quyết định, giải thích reasoning của bạn?
```

---

## 📝 Ví Dụ Thực Tế: 2 Patterns

### Pattern 1: Agent Implement Sai Feature

```
User: Implement feature X
Agent: [implement sai requirement]
User: Dừng lại. Tôi thấy implementation không đúng spec.
Spec yêu cầu: "users có thể upload ảnh từ URL hoặc local file"
Implementation của bạn: chỉ hỗ trợ local file

Hãy xem lại spec và update implementation để hỗ trợ cả URL và local.
```

### Pattern 2: Agent Hallucinate

```
Agent: "Như đã discuss ở trên, chúng ta sẽ dùng library Y"
User: Chúng ta chưa bao giờ discuss về library Y. Tôi không biết library này.
Nó là cái gì? Có đáng tin không?

Grounding: Cung cấp source hoặc admit uncertainty.
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Chờ quá lâu để can thiện | Output sai hoàn toàn, phải reset | Nhận diện sớm qua dấu hiệu hallucination |
| Không cung cấp evidence | Agent không hiểu sai ở đâu | "X không đúng vì Y. Hãy xem lại Z" |
| Sửa hộ thay vì yêu cầu self-correct | Agent không học được | "Tìm 3 bugs và fix" thay vì "sửa giúp tôi" |
| Reject toàn bộ | Mất context đã đúng | Chunk correction: "phần A đúng, phần B cần sửa" |
| Ngại conflict với agent | Wasted time, output sai | Remember: can thiệp = constructively, không phải cãi |

---

## ✅ Checkpoint

- [ ] Bạn có nhận ra sớm khi agent đi sai, hay đợi đến khi output hoàn thành?
- [ ] Khi can thiệp, bạn có cung cấp evidence/reason cụ thể không?
- [ ] Bạn có cho agent cơ hội tự sửa, hay luôn sửa hộ?
- [ ] Khi reset, bạn có giữ lại những phần đúng không?
- [ ] Bạn có feedback constructively hay "cãi" với agent?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/01](./01-viet-prompt-hieu-qua.md) | Viết Prompt — tránh sai direction ngay từ đầu |
| [USE-CASES/01](../USE-CASES/01-debug-code.md) | Debug Code — intervention khi code có bug |
| [PRACTICAL/06](./06-verification-habits.md) | Verification — phát hiện sai sớm |