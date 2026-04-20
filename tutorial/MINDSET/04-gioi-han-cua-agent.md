# Giới Hạn Của AI Agent — Biết Để Dùng Đúng

> Bạn expect Agent làm mọi thứ và thất vọng khi nó fail. Bạn nghĩ Agent "ngốc" khi nó không làm được việc simple. Bạn tin tưởng output mà không verify → ship bug ra production. Đây là vấn đề về **unrealistic expectations**.

---

## 🔥 Thực Trạng

Bạn có thể đã:

- 😤 Expect Agent làm mọi thứ và thất vọng khi nó fail
- 🤦 Nghĩ Agent "ngốc" khi nó không làm được việc simple
- ⏰ Spend hours debug chỉ để find ra Agent đã "hallucinate"
- 🚀 Tin tưởng output mà không verify → ship bug ra production

→ Đây là vấn đề về **unrealistic expectations**.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Hiểu technical limits (context, tokens, knowledge cutoff)
- ✅ Hiểu capability limits (hallucination, no real-time)
- ✅ LUÔN verify factual claims
- ✅ Setup memory system cho cross-session persistence

---

## 🤔 Tại Sao Chúng Ta Expect Quá Nhiều

| Lý do | Giải thích |
|-------|------------|
| **Marketing hype** | AI được khoe là "magical" |
| **Anthropomorphism** | Tự nhiên nghĩ máy "nghĩ" như người |
| **Base rate neglect** | Thấy vài lần thành công → expect always success |
| **Automation bias** | Nghĩ máy tự động = không sai |

---

## ❌ Sự Thật Về AI Agent

| Perception | Reality |
|------------|---------|
| "Nó hiểu tôi" | Nó predict tokens, không "hiểu" |
| "Nó biết mọi thứ" | Knowledge cutoff tồn tại |
| "Nó không bao giờ quên" | Chỉ nhớ trong context window |
| "Nó luôn đúng" | Có thể hallucinate facts |
| "Nó autonomous" | Cần human guidance thường xuyên |

---

## ⚙️ Technical Limits

### 1. Context Window

```
- Claude 3.5: 200K tokens context
- GPT-4o: 128K tokens
- Gemini 1.5: 1M tokens (nhưng đắt hơn)
```

→ Có thể bị overflow, context không lưu được hết.

### 2. Token Budget = Money

```
Input tokens (prompt + context) → cost
Output tokens (response) → cost
```

→ Mỗi request đều có chi phí.

### 3. Knowledge Cutoff

```
- Knowledge trained đến một date cụ thể
- Không biết events sau cutoff
- Cần browse để có current info
```

### 4. Computation

```
- Reasoning tốn time
- Complex tasks có thể chậm
- Có rate limits
```

---

## 🧠 Capability Limits

### 1. Hallucination

```
Agent có thể "bịa" facts nếu:
- Không đủ context
- Prompt ambiguous
- Confidence cao nhưng sai
```

→ **LUÔN verify factual claims.**

### 2. No Persistent Memory

```
Mỗi session = fresh start (thường)
Cần external storage để remember
Cần tools như graphify, llm-wiki
```

→ **"Memory resets"** = đang dùng **sai tier**.

---

## 💾 Memory Stack — Problem vs Solution

**PROBLEM:** Agent dùng Working Memory (context window) cho nhu cầu Long-Term Memory
→ Context window reset mỗi session = KHÔNG persistent

**SOLUTION:** Chọn tier đúng cho nhu cầu đúng

| Tier | Tool | Dùng khi | Reference |
|------|------|----------|-----------|
| **SHORT-TERM** | Session recap/summary | Agent nhớ context TRONG session | `PRACTICAL/04` |
| **EPISODIC** | Graphify | Nhớ SỰ KIỆN, QUAN HỆ đã làm | `SETUP/05` |
| **SEMANTIC** | LLM Wiki | Nhớ KIẾN THỨC đã học | `SETUP/04` |
| **PROCEDURAL** | Skills/Rules | Agent HỌC CÁCH làm thay vì nhắc lại | `FUNDAMENTALS/03` |
| **EXTERNAL** | MCP/RAG | TRA CỨU thông tin bên ngoài | `SETUP/02` |

> 📌 **Note:** MCP/RAG = Retrieval, KHÔNG PHẢI persistent memory. Chỉ lấy data, không lưu lại.

### 3 Bước Fix Memory Issues

```
1️⃣ IDENTIFY  → Problem của bạn thuộc tier nào?
2️⃣ MAP       → Tier → Tool (bảng trên)
3️⃣ IMPLEMENT → Xem file được reference
```

---

### 3. No Real-time Info

```
- Không biết current weather, news, prices
- Trừ khi browse web
- Browse tốn thêm time và token
```

### 4. Domain Context Gap

```
- Hiểu general patterns
- KHÔNG hiểu specific business context
- Cần human provide domain knowledge
```

---

## ⚖️ Agent Yếu vs Mạnh

**Agent YẾU khi:**

- 🔴 Novel architecture (chưa từng thấy pattern)
- 🔴 Ambiguous requirements (có thể đoán sai)
- 🔴 Highly specialized domain (thiếu knowledge)
- 🔴 Creative tasks cần unique insight (thường generic)
- 🔴 Tasks cần judgment calls (ethics, risk)

**Agent MẠNH khi:**

- 🟢 Follow patterns đã biết
- 🟢 Well-defined specifications
- 🟢 Repetitive tasks
- 🟢 Research và synthesis
- 🟢 Boilerplate generation

---

## ✅ Working WITH Limits

### 1. Context limits → Chunk wisely

```
❌ Bad: Dump toàn bộ 50 files vào context
✅ Good: Chỉ provide files liên quan đến current task
```

### 2. Memory limits → Externalize

```
❌ Bad: Hy vọng Agent nhớ từ session trước
✅ Good: Document decisions, dùng notes file
```

### 3. Hallucination → Verify facts

```
❌ Bad: "Agent nói là vậy, chắc đúng"
✅ Good: Check source, test claims, verify logic
```

### 4. Token cost → Optimize

```
❌ Bad: Verbose prompts, redundant context
✅ Good: Concise prompts, progressive disclosure
```

---

## 📋 Realistic Expectations Checklist

```
□ Agent là công cụ, không phải magic
□ Output cần verify trước khi trust
□ Complex tasks cần nhiều vòng iteration
□ Context window có giới hạn
□ Tokens = money
□ Hallucination có thể xảy ra
□ Memory không persistent giữa sessions
```

---

## 💡 When Agent Struggles

| Situation | What to do |
|----------|------------|
| **Novel problem** | Human do initial exploration, then Agent |
| **Ambiguous reqs** | Clarify requirements first |
| **High risk task** | Human verify heavily |
| **Domain specific** | Provide domain context + expert verify |

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu technical limits (context, tokens, knowledge cutoff)
- [ ] Hiểu capability limits (hallucination, no real-time)
- [ ] LUÔN verify factual claims
- [ ] Setup memory system cho cross-session persistence
- [ ] Optimistic nhưng realistic — expect iteration

---

## 💡 Ghi Chú Quan Trọng

**Điều tốt nhất bạn có thể làm:**

```
1️⃣  HIỂU LIMITS     → Biết khi nào Agent sẽ struggle
2️⃣  DESIGN WORKFLOWS → Xung quanh limits đó
3️⃣  VERIFY SYSTEMATICALLY → Trust but verify
4️⃣  ITERATE         → Expect nhiều rounds
```

> 🎯 **Agent tốt nhất = Agent được used correctly**
>
> Một Agent với perfect setup và realistic expectations sẽ outperform một Agent được overtrust, overscope.

---

## 🔗 Liên Quan

- **Setup Memory:** [SETUP/04: LLM Wiki Workflow](../SETUP/04-llm-wiki-workflow.md)
- **Session:** [PRACTICAL/04: Session Hygiene](../PRACTICAL/04-session-hygiene.md)
- **Context:** [PRACTICAL/02: Quản Lý Context](../PRACTICAL/02-quan-ly-context.md)