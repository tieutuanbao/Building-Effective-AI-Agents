# Brainstorm & Đề Xuất Ý Tưởng

## 🔥 Thực Trạng

Bạn nhờ agent đề xuất feature mới. Agent trả về 5 ý: dark mode, push notification, offline mode, search, sharing. Bạn đã nghĩ đến tất cả những cái này từ trước. Hoặc tệ hơn, agent liệt kê đúng những gì competitor đang làm và gọi đó là "best practice phổ biến." Không có gì surprise, không có gì mới. Cảm giác AI chỉ là công cụ search Wikipedia đắt tiền hơn. Vấn đề không phải agent "ngu" mà là bạn đang dùng nó như idea generator, trong khi agent hoạt động tốt nhất như thinking partner. Không có constraints, không có friction, agent sẽ mặc định trả về safe answers vì safe answers không bao giờ sai. Sycophancy không chỉ là gật đầu khi bạn nói điều gì đó, mà còn là đề xuất những thứ "ai cũng biết" để tránh bị phản bác.

---

## 🎯 Mục Tiêu

- Biết tại sao prompt "cho tôi ý tưởng" luôn ra kết quả generic và cách fix nó
- Áp dụng workflow 4 bước: Constraints seeding → Perspective assignment → Devil's advocate → Convergence
- Nhận ra 3 dấu hiệu session đang đi sai hướng và cách kéo lại
- Phân biệt bài này với PRACTICAL/03 — bài đó dạy kỹ thuật riêng lẻ, bài này dạy cách kết hợp thành workflow hoàn chỉnh

---

## 🧩 Best Practices

### Core Workflow: 4 bước

```
Constraints seeding → Perspective assignment → Devil's advocate → Convergence
```

**Bước 1: Constraints seeding** — Cho agent biết context cụ thể trước khi hỏi ý tưởng. Không phải "app của tôi" mà là: product là gì, pain point là gì, giới hạn là gì (tech, timeline, resource). Constraints tạo ra friction. Friction tạo ra ý tưởng thú vị.

**Bước 2: Perspective assignment** — Giao cho agent một góc nhìn cụ thể khi phân tích. "Phân tích dưới góc độ user mới lần đầu dùng" cho kết quả khác với "phân tích dưới góc độ power user." Chi tiết hơn ở PRACTICAL/03.

**Bước 3: Devil's advocate** — Sau khi có danh sách ý tưởng, yêu cầu agent đóng vai critic. Không phải để loại bỏ ý tưởng mà để tìm weakness trước khi bạn đầu tư vào nó.

**Bước 4: Convergence** — Không để agent tự chọn. Bạn quyết định dựa trên output của 3 bước trên. Agent tổng hợp lại, bạn làm trọng tài.

---

### Agent Role

| Agent LÀ | Agent KHÔNG PHẢI |
|-----------|------------------|
| Thinking partner với perspective được giao | Idea generator tự phát |
| Người phân tích feasibility theo framework | Người biết business của bạn tốt hơn bạn |
| Devil's advocate khi được yêu cầu | Critic tự động (sẽ sycophantic nếu không bị push) |
| Bộ nhớ ngắn hạn trong session | Thay thế cho domain expertise của bạn |

---

### Before/After

**Prompt tệ:**

```
Cho tôi ý tưởng feature mới cho app này
```

Kết quả: danh sách 5 features generic, không có context, agent không biết nên ưu tiên gì. Output có thể đúng nhưng vô dụng vì bạn đã biết hết rồi.

**Prompt tốt (constraint-seeded):**

```
Product: task manager cho freelancers.
Pain point cốt lõi: user quên follow-up sau meeting với client.
Constraints cứng:
  - Offline-first (không có server push)
  - Không dùng push notification (user đã tắt hết)
  - Team 2 người, deadline 3 tuần

Đề xuất 5 giải pháp cho pain point trên. Với mỗi giải pháp, cho tôi:
  - Feasibility (1-5, 5 là dễ nhất)
  - User impact (1-5, 5 là cao nhất)
  - Dev effort (S/M/L)
  - Một assumption ẩn có thể sai

Sau đó đóng vai devil's advocate cho top 2 giải pháp có điểm cao nhất.
```

Kết quả: agent phải nghĩ trong khuôn khổ cụ thể, không thể đề xuất "thêm push notification" vì đó đã bị loại trừ. Friction đó buộc agent phải sáng tạo hơn.

---

### Khi Nào KHÔNG Dùng Pattern Này

- Khi bạn chưa biết gì về domain — hãy research trước, brainstorm sau
- Khi bạn cần một câu trả lời rõ ràng có/không — đây là open-ended ideation, không phải decision tool
- Khi constraints chưa được xác định — "tôi không biết giới hạn là gì" thì cần clarification trước, không phải brainstorm

---

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Feature ideation cho product mới

**Context**: Bạn đang build app quản lý chi tiêu cho cặp đôi. User pain point: tranh cãi về ai mua gì.

```
Product: expense tracking app cho couples.
Core pain: conflict về shared expenses ("ai đã mua cái này?")
Constraints:
  - Không sync real-time (chi phí infra)
  - Cả hai người không nhất thiết phải online cùng lúc
  - MVP: chỉ 2 người per account

Góc nhìn: product manager có 5 năm experience với fintech consumer apps.

Đề xuất 4 hướng giải quyết pain "ai mua cái này." Với mỗi hướng:
  - Giải thích cơ chế hoạt động
  - User story ngắn (1-2 câu)
  - Risk chính
  - Có thể build trong 2 tuần không (yes/no + lý do)
```

✅ Output thường có giá trị vì agent phải tôn trọng constraint "không real-time sync" — giải pháp bắt buộc phải khác mainstream.

⚠️ Nếu agent vẫn đề xuất "sync real-time" bất chấp constraint, đó là dấu hiệu sycophancy — agent đang optimize cho "trả lời đầy đủ" thay vì "trả lời đúng yêu cầu."

---

### Scenario 2: Giải pháp cho technical constraint khan hiếm

**Context**: Startup 3 người cần release MVP trong 2 tuần, tech stack không quen.

```
Situation: 3 developer (1 frontend React, 1 backend Node, 1 fullstack junior).
Goal: ship MVP của SaaS B2B trong 2 tuần.
Feature cần thiết: user auth, dashboard cơ bản, export CSV.
Tech risk: chưa ai dùng Supabase trong team.

Đóng vai senior engineer đã từng ship nhiều MVP dưới áp lực timeline.

Câu hỏi 1: Với constraint này, feature nào nên cut khỏi 2-week scope?
Câu hỏi 2: Supabase hay build auth tự bằng JWT — tradeoff cụ thể với team profile này?
Câu hỏi 3: Đâu là hidden risk lớn nhất mà team kiểu này thường bỏ qua?

Không đề xuất solution lý tưởng. Đề xuất solution đủ tốt cho context này.
```

✅ Cụm "Không đề xuất solution lý tưởng" là key. Nó ngăn agent rơi vào "best practice" mode.

⚠️ Nếu agent bắt đầu viết code hoặc setup instructions thay vì phân tích tradeoffs, dừng ngay: "Chưa cần implementation. Chỉ cần analysis và recommendation."

---

## 🚧 Pitfalls & Recovery

**Pitfall 1: Agent cho ý tưởng safe / generic (sycophancy)**

Dấu hiệu: response chứa "best practice phổ biến", "nhiều app lớn đang làm", "đây là approach được khuyến nghị". Không có gì bạn chưa nghe.

Recovery: "Danh sách trên toàn là ideas thông thường. Đề xuất lại 3 ideas có risk cao, unconventional, hoặc counter-intuitive với pain point này. Nếu idea nghe có vẻ kỳ lạ, đó là dấu hiệu tốt."

---

**Pitfall 2: Brainstorm biến thành implementation quá sớm**

Dấu hiệu: agent bắt đầu viết code, schema database, hay checklist cài đặt trong khi bạn còn đang ở giai đoạn ideation. Session drift từ "think" sang "do."

Recovery: "Dừng. Chúng ta vẫn đang ở giai đoạn ideation. Xóa code đó đi. Chỉ liệt kê ideas và tradeoffs, không implement gì cả."

Phòng ngừa: Ghi rõ trong prompt "Chỉ cần analysis. Không cần code. Không cần implementation steps."

---

**Pitfall 3: Agent đồng ý quá dễ, không challenge đủ**

Dấu hiệu: mọi idea bạn đề xuất đều nhận được "Đúng, approach này có ưu điểm là..." Agent không phản biện, không đưa ra counterpoint.

Recovery: "Bạn vừa agree với mọi thứ tôi nói. Đóng vai skeptic. Idea nào trong list này không khả thi với resources hiện tại? Cái nào có hidden assumption sai?"

---

**Cost awareness**: Brainstorm session thường dài vì nhiều back-and-forth. Dùng model rẻ hơn (Flash, Haiku) cho bước đầu divergent thinking. Chỉ switch sang model mạnh khi cần convergence và evaluation sâu.

---

## ✅ Checkpoint

### Pattern Cheat Sheet

```
1. SEED:    Product + Pain point + Constraints cứng
2. ASSIGN:  Góc nhìn cụ thể cho agent (persona / role)
3. DIVERGE: Đề xuất + scoring theo criteria
4. STRESS:  "Đóng vai devil's advocate cho top 2"
5. DECIDE:  Bạn quyết định, agent tổng hợp
```

### Checklist Trước Khi Brainstorm

- [ ] Đã xác định pain point cụ thể (không phải "muốn cải thiện app")
- [ ] Đã liệt kê constraints (tech, timeline, resource)
- [ ] Đã quyết định góc nhìn muốn agent dùng
- [ ] Đã viết criteria đánh giá (feasibility, impact, effort)
- [ ] Đã thêm "Không đề xuất solutions lý tưởng" hoặc "Đề xuất ideas có risk"

### Khi Session Đi Sai

| Dấu hiệu | Recovery ngắn |
|-----------|---------------|
| Generic answers | "Đề xuất lại ideas unconventional hơn" |
| Agent viết code | "Dừng. Chỉ cần analysis." |
| Agent gật đầu tất cả | "Đóng vai skeptic. Cái nào không khả thi?" |

---

## 🔗 Liên Quan Bài này dạy workflow tổng thể. PRACTICAL/03 dạy từng kỹ thuật riêng lẻ như perspective assignment, Socratic questioning, và devil's advocate chi tiết hơn. Đọc PRACTICAL/03 trước nếu bạn muốn hiểu từng building block, hoặc đọc bài này trước nếu bạn muốn thấy cách chúng kết hợp trong một session thực.
