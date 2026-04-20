# Tìm Giải Pháp Kỹ Thuật

## 🔥 Thực Trạng

Bạn hỏi agent "nên dùng cái gì cho project của mình" và nhận lại một câu trả lời generic kiểu "theo best practice thì nên dùng X". Bạn implement theo, tốn 2 tuần, rồi phát hiện X không phù hợp với constraints của team mình. Điều này xảy ra vì tool landscape thay đổi nhanh hơn training data của model. Agent recommend phổ biến thay vì phù hợp, và bạn không có framework để đánh giá quality của recommendation.

---

## 🎯 Mục Tiêu

- Viết prompt để agent phân tích options thay vì recommend đại khái
- Trình bày constraints để agent đưa ra tradeoff analysis có cơ sở
- Nhận diện khi nào agent đang recommend popular thay vì optimal
- Tránh research loop tốn token bằng cách đặt scope rõ ràng

---

## 🧩 Best Practices

### Core Workflow

```
Constraints → Options Generation → Tradeoff Analysis → Decision (evidence-based)
```

| Phase | Agent Role | User Role |
|-------|------------|-----------|
| **Constraints** | Clarify và validate | Cung cấp thông tin thực tế |
| **Options** | List alternatives với technical details | Review và loại bỏ bất khả thi |
| **Tradeoffs** | Phân tích pros/cons theo constraints | So sánh và đánh giá |
| **Decision** | Present evidence, KHÔNG quyết định | Chịu trách nhiệm cuối cùng |

**Agent LÀ analyst — phân tích options và tradeoffs.**
**Agent KHÔNG PHẢI decision maker — bạn quyết định và chịu trách nhiệm.**

### Before/After Comparison

```
❌ BAD: "Nên dùng state management nào cho React app?"

✅ GOOD: "Context: React app, 3 devs, complex form state, bundle size < 50KB.
So sánh Zustand vs Jotai vs Redux Toolkit theo:
- Learning curve (1-5)
- Bundle size overhead
- DevTools quality
- TypeScript support
Recommend 1 với rationale rõ ràng. Nếu không chắc, list tradeoffs."
```

### Khi nào KHÔNG dùng pattern này

- Task đã có best practice cố định (VD: "dùng HTTPS" — không cần tradeoff)
- Bạn đã có đủ domain knowledge để tự quyết định
- Đang debugging/fix bug — không phải lúc architecture decision

---

## 🛠️ Ví Dụ Thực Tế

**Scenario 1**: Chọn database cho startup

```
❌ BAD Prompt:
"Startup nên dùng database gì? PostgreSQL vs MongoDB?"

✅ GOOD Prompt:
"Context: Startup Phase 1, 1 backend dev, budget $50/tháng, cần đẩy nhanh time-to-market.
Dataset: < 10K rows, không có relation phức tạp, có thể thay đổi schema.

So sánh PostgreSQL vs MongoDB vs Supabase theo:
- Setup time (giờ)
- Maintenance burden (tự manage vs managed)
- Scaling cost (0-100K users)
- Learning curve cho dev mới

Recommendation 1-2 options phù hợp với Phase 1 constraints.
Warning: những gì sẽ phải trả giá khi scale."
```

**Scenario 2**: Chọn architecture pattern cho microservice

```
❌ BAD Prompt:
"Nên dùng monolith hay microservices?"

✅ GOOD Prompt:
"Context: Team 4 devs, startup với product-market fit chưa rõ, potential 50K-500K users.
Current: Django monolith, deploy single server, đang bắt đầu thấy pain points.

Tính theo dimensions:
1. Development velocity (feature delivery time)
2. Operational complexity (SRE effort)
3. Cost at 50K / 500K users
4. Team organization (4 devs, no dedicated SRE)

Recommend approach nào PHÙ HỢP với current stage.
Điều kiện nào trigger phải thay đổi sang architecture khác?"
```

---

## 🚧 Pitfalls & Recovery

**1. Agent recommend popular tool thay vì optimal**
- **Dấu hiệu**: Agent nói "đây là best practice phổ biến nhất" mà không cite evidence
- **Recovery**: Yêu cầu agent justify theo constraints cụ thể của bạn
  ```
  "Tại sao X phù hợp hơn Y cho case này? Trình bày theo criteria [list constraints]"
  ```

**2. Training data outdated → recommend deprecated library**
- **Dấu hiệu**: Version được mention trong recommendation đã cũ (VD: React Router v5, Babel 6)
- **Recovery**: Check date và ask cho version hiện tại
  ```
  "Library X version nào là stable release hiện tại? Check date của docs"
  ```

**3. Research loop tốn token khi không constrain scope**
- **Dấu hiệu**: Agent hỏi follow-up questions liên tục, mỗi lần thêm context
- **Cost awareness**: Đặt token budget cho research phase trước khi bắt đầu
  ```
  "Phân tích max 2000 tokens. Nếu cần more info, hỏi 1 lần duy nhất ở cuối."
  ```

---

## ✅ Checkpoint

**Pattern Cheat Sheet:**

| Step | Action |
|------|--------|
| 1 | Define constraints trước (team size, budget, timeline) |
| 2 | Ask analyst, not decision maker |
| 3 | Require tradeoff matrix thay vì single recommendation |
| 4 | You own the decision |
| 5 | Document rationale để future-you hiểu |

**Checklist trước khi hỏi agent về technical decisions:**

- [ ] Đã list rõ constraints (team, budget, timeline)?
- [ ] Đã xác định evaluation criteria?
- [ ] Đã specify scope (chỉ Phase 1 hay long-term)?
- [ ] Sẵn sàng chịu trách nhiệm quyết định?

## 🔗 Liên Quan

- [PRACTICAL/01-viet-prompt-hieu-qua.md](../PRACTICAL/01-viet-prompt-hieu-qua.md) — Prompt structure cơ bản để apply vào đây
- [PRACTICAL/03-brainstorm-voi-agent.md](../PRACTICAL/03-brainstorm-voi-agent.md) — Khi cần explore nhiều options trước khi narrow down

---

*Đọc thêm: [ECOSYSTEM/02-so-sanh-agent-tools.md](../ECOSYSTEM/02-so-sanh-agent-tools.md) để hiểu tool landscape chung*