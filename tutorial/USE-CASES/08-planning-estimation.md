# Planning & Estimation Dự Án

## 🔥 Thực Trạng

PM hỏi "feature này bao lâu xong?" — bạn nhờ agent estimate, nhận ngay một con số tự tin: "8-10 ngày." Bạn báo lại client. Tuần thứ hai, mới xong 40%. Tuần thứ tư, vẫn còn integration đang lag. Con số thực tế: 22 ngày. Đây không phải lỗi của agent — đây là lỗi của cách bạn hỏi.

Agent có optimism bias cố hữu. Nó được train để be helpful, nên tự nhiên thiên về "cái này đơn giản" thay vì "cái này ẩn nhiều rủi ro." Kết quả: estimate sai 3-5x là chuyện bình thường. Bạn mất credibility với PM và client không phải vì làm chậm — mà vì cam kết số sai.

---

## 🎯 Mục Tiêu

- Dùng 3-point estimate (optimistic/realistic/pessimistic) thay vì single number
- Ép agent vào vai devil's advocate để challenge chính estimate của nó
- Tránh bỏ sót integration, testing, và deployment time trong estimate
- Biết khi nào nên dùng full planning session và khi nào không cần

---

## 🧩 Best Practices

### Core Workflow

```
Decompose → 3-point estimate → Dependency map → Risk buffer → Devil's advocate
```

### Agent Role: Decomposition Assistant + Devil's Advocate

Agent LÀ: công cụ decompose task + devil's advocate challenge estimate + reminder hidden time sinks (testing, review, deploy).

Agent KHÔNG PHẢI: project manager, oracle dự đoán chính xác, hay nguồn estimate có thể quote thẳng với client. Bạn là người quyết con số cuối.

> **Note:** Bài này về human planning VỚI agent assistance. Xem thêm [FUNDAMENTALS/01](../FUNDAMENTALS/01-ai-agent-la-gi.md) cho agent self-planning (hierarchical, conditional, self-correcting).

### Before/After: Prompt Chuẩn

**Before** — single number, không có cấu trúc:

```
❌ "Estimate bao lâu xong auth system?"
→ Agent: "Khoảng 5-7 ngày tùy complexity."
→ Reality: 18 ngày.
```

**After** — decompose, 3-point estimate, devil's advocate:

```
✅ "Break down auth system thành subtasks.
Mỗi subtask cần:
(1) description ngắn gọn
(2) dependencies — cái nào phải xong trước
(3) estimate hours:
   - Optimistic: nếu mọi thứ smooth, không có surprises
   - Realistic: có obstacles có thể xảy ra
   - Pessimistic: worst case, blocked vài lần

Sau khi list subtasks xong:
- Identify top 3 risks có thể delay
- Thêm buffer 20-30% cho integration + testing
- Đóng vai devil's advocate: challenge estimate,
  cái nào có likelihood bị underestimate nhất và tại sao?"
```

**Output nhận được:**

```
Auth System — 5 subtasks với 3-point estimate (giờ):
1. Registration endpoint:  Opt 4h | Real 8h | Pess 12h
2. Login + JWT:            Opt 3h | Real 6h | Pess 10h
3. Refresh token flow:     Opt 3h | Real 7h | Pess 14h
4. Password reset (email): Opt 4h | Real 10h | Pess 16h
5. Integration testing:    Opt 4h | Real 8h | Pess 12h

SUBTOTAL realistic: 39h → Buffer 25% → TOTAL: 49h (~6 ngày)

Top risks: email service 2x; JWT edge cases; test env setup bị quên.

Devil's advocate: Password reset và refresh token bị underestimate.
Email deliverability + token rotation hay vượt pessimistic — dùng
pessimistic cho 2 subtasks này.
```

### Khi Nào KHÔNG Dùng Full Planning Session

- **Task dưới 2h**: estimate ngay trong prompt, không cần session riêng
- **Task quen thuộc**: base estimate từ lịch sử thực tế
- **Spike/investigation**: timebox thay vì estimate giờ ("4h tìm hiểu, sau đó mới estimate")

---

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Sprint Planning Cho Feature Mới

**Tình huống:** PM muốn biết effort cho "notification system" trước sprint planning buổi chiều.

**Prompt:**

```
Tôi cần estimate "notification system" cho sprint planning hôm nay.
Feature scope: in-app notifications + email notifications.

Bước 1 — Decompose thành subtasks (level: có thể làm trong 1-2 ngày mỗi cái).
Bước 2 — Với mỗi subtask, cho 3-point estimate (unit: giờ):
  - Optimistic (không có blockers)
  - Realistic (có 1-2 obstacles nhỏ)
  - Pessimistic (bị blocked, phải dig deeper)
Bước 3 — Map dependencies (thứ tự thực hiện).
Bước 4 — Identify hidden time sinks hay bị quên.
Bước 5 — Đề xuất sprint allocation nếu sprint = 2 tuần, team = 2 devs.

Tech stack: React frontend, Node.js backend, PostgreSQL.
```

**Result:**

```
✅ 6 subtasks với 3-point estimate, dependency map đầy đủ
✅ Hidden cost được flag: "WebSocket setup thêm 4-6h do CORS + load balancer"
✅ Đề xuất phase: in-app (sprint 1) → email (sprint 2)

⚠️ "Email service integration = 4h optimistic" — thực tế 8-12h.
   Override bằng pessimistic estimate cho item này.
```

---

### Scenario 2: Estimate Cho Client Proposal (SOW)

**Tình huống:** Cần gửi Statement of Work cho client, estimate phải realistic vì dùng để báo giá.

**Prompt:**

```
Tôi cần estimate cho client proposal. Đây là estimate sẽ dùng để báo giá,
nên cần conservative hơn estimate nội bộ.

Feature: E-commerce checkout flow
Scope: cart → payment → order confirmation → email receipt

Yêu cầu:
1. Decompose thành phases (không phải subtasks — level cao hơn)
2. Mỗi phase: 3-point estimate theo ngày (không phải giờ)
3. Explicit nêu những gì KHÔNG bao gồm trong estimate (exclusions)
4. Risk register: top 5 risks kèm probability (Low/Med/High) và impact
5. Recommended buffer: tôi đang dùng T&M contract, nên buffer được?

Đừng underestimate để "trông competitive" — estimate sai gây vấn đề lớn hơn.
```

**Result:**

```
✅ Exclusions tách rõ: "Payment gateway setup, tax, multi-currency = OUT OF SCOPE"
✅ Risk register: "Payment provider API changes: Med prob, High impact"
✅ "SOW estimate nên dùng Pessimistic + 15% management overhead"

⚠️ Buffer agent suggest = 20%. Với T&M + client hay change scope:
   30-35% realistic hơn. Bạn quyết con số cuối.
```

---

## 🚧 Pitfalls & Recovery

### 1. Optimism Bias — Mọi Estimate Đều "Best Case"

**Dấu hiệu:**
- Estimate optimistic và realistic chênh nhau rất ít (< 20%)
- Agent không list risks cụ thể
- Output có câu "if everything goes smoothly" quá nhiều

**Recovery:**

```
"Estimate trông quá optimistic. Thử lại:
- Giả định ít nhất 1 blocker không lường
- Pessimistic: 2 blockers + 1 lần refactor
- List 3 ví dụ cụ thể hay break task dạng này

Tôi cần pessimistic RIÊNG, không phải average."
```

---

### 2. Bỏ Sót Integration, Testing, Deployment Time

**Dấu hiệu:** Estimate chỉ có "development time". Không thấy QA, code review, deploy trong list. Tổng trông quá đẹp.

**Recovery:**

```
"Estimate này thiếu:
- Code review: +10% tổng dev time
- Integration testing: +20-30%
- Deployment + rollback prep: +1 ngày

Recompute với những line items này explicit."
```

### 3. Không Account For Learning Curve Và Tech Unknowns

**Dấu hiệu:** Tech stack mới nhưng estimate giống như technology quen thuộc. Không mention "first time using X".

**Recovery:**

```
"Tech stack này team chưa dùng bao giờ ([tên lib/framework]).
Thêm learning curve: 50% tổng dev estimate cho sprint đầu.
Proof of concept spike: 1-2 ngày trước khi start feature.
Reestimate với assumption: medium-skilled, chưa biết [X]."
```

---

**Cost Awareness:** Full planning session tốn 5,000-15,000 tokens. Task dưới 2h: viết 3-point estimate thẳng vào prompt chính, không cần session riêng. Tiết kiệm 80% token, cùng kết quả.

---

## ✅ Checkpoint

### Pattern Cheat Sheet

```
1. DECOMPOSE: "Break down thành subtasks, level = 1-2 ngày mỗi cái"
2. 3-POINT: "Optimistic / Realistic / Pessimistic cho mỗi subtask"
3. HIDDEN COSTS: "+10% review, +25% testing, +deployment day"
4. DEVIL's ADVOCATE: "Challenge estimate, cái nào bị underestimate nhất?"
5. BUFFER: "Conservative = pessimistic + 15-30% overhead"
```

### Checklist Trước Khi Commit Estimate

- [ ] Đã dùng 3-point estimate, không phải single number
- [ ] Subtask list có integration + testing + deployment explicit
- [ ] Đã chạy devil's advocate step để challenge các con số
- [ ] Learning curve đã tính nếu tech stack mới
- [ ] Buffer được thêm (20% internal, 30%+ cho SOW)
- [ ] Task dưới 2h: dùng inline estimate, không cần planning session riêng

## 🔗 Liên Quan

| Bài | Liên quan |
|-----|-----------|
| [PRACTICAL/08](../PRACTICAL/08-phan-ra-task.md) | Phân rã task — cách decompose trước khi estimate |
| [PRACTICAL/07](../PRACTICAL/07-quan-ly-chi-phi.md) | Quản lý chi phí — tránh tốn token cho planning session nhỏ |
