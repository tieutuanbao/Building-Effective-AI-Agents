# Brainstorm Với Agent

---

## 🔥 Thực Trạng

Bạn hỏi agent về technical decisions và gặp cảnh này:

```
Bạn: "Nên dùng PostgreSQL hay MongoDB?"
Agent: "Tùy vào nhu cầu của bạn. Cả hai đều tốt."
```

Hoặc:

```
Bạn: "Code này có vấn đề gì không?"
Agent: "Looks good to me!"  ← Không có phản biện, không có pros/cons
```

**Vấn đề thực:**

- Agent đưa ra ý kiến **chủ quan nhưng không phân biệt** opinion vs fact
- Agent **gật đầu tất cả** đề xuất của bạn dù có vấn đề
- Hoặc ngược lại, agent **phản đối mà không giải thích rõ** lý do
- Không có structured brainstorming → kết quả lộn xộn, khó reference lại

→ **Bài này tập trung vào thực hành** — cách brainstorm có cấu trúc với agent.

---

## 🎯 Mục Tiêu

- [ ] Gán perspective cụ thể cho agent trước khi brainstorm
- [ ] Yêu cầu agent nêu pros/cons TRƯỚC KHI recommend
- [ ] Dùng Socratic questioning để agent tự khám phá
- [ ] Format kết quả brainstorm rõ ràng, có thể reference lại
- [ ] Tránh confirmation bias bằng devil's advocate technique

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Gán Perspective Cho Agent

**❌ SAI:**

```
Nên dùng React hay Vue?
```

**✅ ĐÚNG:**

```
Bạn là tech lead thận trọng, ưu tiên:
- Maintainability (code phải dễ maintain sau này)
- Testing (phải viết được test)
- Documentation (phải có docs)

Khi đề xuất solution, nêu rõ trade-offs giữa các options.
```

**Tại sao cần thiết:**

- Agent không có preference thật sự — cần được giao perspective
- Với perspective rõ → agent đề xuất có cân nhắc, không phải "safe answer"

---

### 2. Yêu Cầu Pros/Cons Trước

**❌ SAI:**

```
Nên dùng PostgreSQL hay MongoDB?
→ Agent recommend 1 option không có reasoning
```

**✅ ĐÚNG:**

```
Phân tích database options cho project:
- 100k daily active users
- Cần real-time analytics
- Team 3 dev, kinh nghiệm MySQL > PostgreSQL

Format:
1. Options: PostgreSQL, MySQL, MongoDB, ClickHouse
2. So sánh theo: scalability, real-time analytics, learning curve, cost
3. Pros/Cons matrix cho mỗi option
4. Recommendation có giải thích
5. Open questions: Dữ liệu có cấu trúc cố định không?
```

---

### 3. Dùng Devil's Advocate

Sau khi agent đề xuất, yêu cầu agent phản biện:

```
Đóng vai critic. Tìm 3 lý do tại sao approach này có thể thất bại.
```

**Kết quả:**

- Tránh confirmation bias
- Agent phải defend recommendation bằng evidence
- Uncover hidden risks trước khi commit

---

### 4. Structured Brainstorming Format

Dùng format cố định để kết quả rõ ràng:

```
Format brainstorm:
1. Options (mỗi option 1 dòng)
2. Pros/Cons matrix
3. Recommendation (sau khi xem xét tất cả)
4. Open questions (cần thêm thông tin)
```

---

### 5. Đặt Câu Hỏi Socratic

Thay vì hỏi "nên làm gì?", hỏi agent tự khám phá:

| Thay vì | Hỏi |
|---------|-----|
| "Nên dùng A hay B?" | "Điều gì xảy ra nếu chúng ta chọn A?" |
| "Code này tốt không?" | "Rủi ro lớn nhất ở đây là gì?" |
| "Khi nào xong?" | "Làm sao chúng ta biết nếu thành công?" |
| "Tại sao nên refactor?" | "Evidence nào cho thấy refactor cần thiết?" |

---

## ⚖️ So Sánh: Không Có Structure vs Có Structure

| Không có Structure | Có Structure |
|-------------------|--------------|
| Agent gật đầu mọi đề xuất | Agent đưa pros/cons trước |
| Không có checkpoint | Debated bởi devil's advocate |
| Kết quả mơ hồ | Format rõ ràng, reference được |
| Opinion như fact | Fact tách biệt khỏi opinion |
| Confirmation bias cao | Bias được expose |

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Không gán perspective | Agent đưa "safe answer" không có cân nhắc | Gán vai trò cụ thể + priorities |
| Không yêu cầu pros/cons | Không biết trade-offs | BẮT BUỘC pros/cons trước recommendation |
| Agent gật đầu quá nhanh | Vấn đề được phát hiện quá muộn | Dùng devil's advocate technique |
| Không format kết quả | Khó reference lại sau đó | Dùng structured format |
| Hỏi "nên làm gì?" | Agent quyết định hộ bạn | Dùng Socratic questions |

---

## ✅ Checkpoint

- [ ] Bạn đã gán perspective cụ thể cho agent trước khi brainstorm?
- [ ] Agent có nêu pros/cons trước khi recommend không?
- [ ] Bạn có đặt câu hỏi phản biện để tránh confirmation bias?
- [ ] Kết quả brainstorm có format rõ ràng, có thể reference lại không?
- [ ] Bạn có yêu cầu agent nêu open questions thay vì giả định?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/01](./01-viet-prompt-hieu-qua.md) | Viết Prompt — prompt technique cho brainstorm |
| [SETUP/06](../SETUP/06-superpowers-workflow.md) | Superpowers Workflow — structured workflow tự động |
| [USE-CASES/04](../USE-CASES/04-brainstorm-y-tuong.md) | Brainstorm thực chiến — use case cụ thể |