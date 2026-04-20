# Debug Code Với Agent

## 🔥 Thực Trạng

Bạn paste error log 50 dòng vào agent, nó sửa một chỗ. Chạy lại, lỗi khác xuất hiện. Lại paste, agent lại fix chỗ khác. Vòng lặp cứ tiếp diễn. Hàng giờ trôi qua, bug vẫn còn đó, và bạn bắt đầu tự hỏi: "Tại sao agent không tìm root cause?" Nguyên nhân gốc: prompt không isolate được bug, agent nhảy vào fix symptom thay vì phân tích nguyên nhân. Kết quả là debug loop không bao giờ kết thúc và token usage tăng vô tộc.

---

## 🎯 Mục Tiêu

- Hiểu workflow Isolate → Reproduce → Hypothesize → Fix → Verify
- Viết prompt debug đượcisolated bug, không lan sang context khác
- Phân biệt khi nào agent là debugging partner, khi nào không nên dùng
- Nhận diện và recover khi agent đi sai hướng
- Tránh những pitfalls đặc thù của debug use case

---

## 🧩 Best Practices

### Core Workflow

```
Isolate → Reproduce → Hypothesize → Fix → Verify
    ↑
    Agent role: debugging partner,
    KHÔNG PHẢI oracle hay code replacer
```

### Agent Role

| Agent LÀ | Agent KHÔNG PHẢI |
|----------|------------------|
| Debugging partner | Oracle (biết tất cả) |
| Hypothesis generator | Code replacer (viết thay bạn) |
| Logic analyzer | Stack trace interpreter |

### Before/After Prompt

**Before (BAD):**
```
Code bị lỗi, fix giùm: [paste 200 dòng code]
```

**After (GOOD):**
```
Bug: API trả 500 khi user submit form với email chứa dấu +
Error log:
  TypeError: Cannot read property 'split' of undefined
    at validateEmail (/src/validators/email.ts:12:24)
    at router.post (/src/routes/user.ts:45:30)
File liên quan: src/validators/email.ts
Đã thử: regex ^\S+@\S+\.\S+$ -> vẫn lỗi

Hãy phân tích root cause trước, chưa cần fix.
Chỉ ra cụ thể: tại sao error xảy ra, check nào bị fail.
```

### Khi nào KHÔNG nên dùng pattern này

- Khi bug đã reproduce được và bạn biết exact location → fix trực tiếp
- Khi error liên quan đến race condition hoặc timing issues → cần debugging thủ công
- Khi codebase có security-sensitive operations → verify kỹ hơn bình thường

---

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Backend API Bug (500 Error)

**Prompt:**
```
[Lỗi]
POST /api/users với body: {"email": "test+filter@example.com", "name": "Test"}
Response: 500 Internal Server Error

[Stack trace]
Error: Invalid email format
    at EmailValidator.validate (/src/validators/email.ts:23:19)
    at UserController.create (/src/controllers/user.ts:58:12)

[Hành vi mong đợi]
Email "test+filter@example.com" là hợp lệ (plus sign là valid theo RFC 5321)

[Yêu cầu]
1. Phân tích root cause - tại sao email có dấu + bị reject
2. Chỉ rõ file và dòng gây lỗi
3. Đề xuất fix, nhưng CHƯA apply - đợi tôi review trước
```

**Agent response ( abbreviated):**
```
Root cause: EmailValidator.validate() dùng regex:
  /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/

Regex không include + trong character class đầu tiên.
Dòng 12: regex chặn '+' character.

Fix: Thêm + vào character class -> /^[a-zA-Z0-9._%+-]+@.../

⚠️ Recovery: Regex trên chưa đúng. Theo RFC 5321, part trước @
có thể chứa: letters, numbers, và các ký tự ! # $ % & ' * + - / = ? ^ _ ` . { | } ~
```

✅ **Khi hoạt động tốt:** Bug isolated, error log clear, agent phân tích được root cause mà không cần full codebase.

⚠️ **Khi thất bại:** Agent đề xuất fix mà không verify regex đã đúng chuẩn RFC. Recovery: yêu cầu agent check documentation hoặc test thêm.

---

### Scenario 2: Frontend Rendering Bug

**Prompt:**
```
[Mô tả]
Component UserProfile hiển thị sai khi user có unicode trong tên.
Thay vì "Nguyễn Văn Minh", nó hiển thị "Nguyễn Văn Minh?" hoặc bỏ trống.

[Hành vi]
- Input: { name: "Nguyễn Văn Minh", avatar: "url" }
- Output mong đợi: avatar + name hiển thị đầy đủ
- Output thực tế: avatar hiển thị, name bị cắt hoặc ?

[File]
src/components/UserProfile.tsx

[Yêu cầu]
1. Đọc code và xác định nguyên nhân (encoding? truncation? display issue?)
2. Đề xuất hypothesis - có thể là gì
3. Nếu cần thêm info, hỏi tôi trước khi đoán

⚠️ Lưu ý: Không có screenshot, chỉ mô tả bằng text.
```

**Agent response:**
```
Hypothesis 1: Text truncation do CSS with text-overflow: ellipsis
Hypothesis 2: Encoding issue khi render Unicode
Hypothesis 3: API response bị corrupt ở backend

Cần thêm info:
- Backend có truncate name không?
- CSS có set max-width cho name field không?
- Console có warning gì không?
```

✅ **Khi hoạt động tốt:** Agent đưa ra nhiều hypothesis thay vì guess một cái.

⚠️ **Khi thất bại:** Agent pick một hypothesis và bắt đầu fix mà không verify. Recovery: "Hãy verify hypothesis bằng cách nào trước khi fix?"

---

## 🚧 Pitfalls & Recovery

1. **Agent sửa symptom thay vì root cause**
   - Dấu hiệu: Agent nhảy vào fix ngay, không hỏi gì, bắt đầu bằng "Tôi sẽ fix..."
   - Recovery: "Dừng lại. Trước khi fix, phân tích root cause. Tại sao bug này xảy ra?"

2. **Agent hallucinate stack trace hoặc đề xuất fix cho version cũ**
   - Dấu hiệu: Agent đề xuất deprecated API, hoặc file/function không tồn tại trong codebase
   - Recovery: "API/File này có còn không? Verify lại trong codebase trước."

3. **Context ngập khi paste quá nhiều log files**
   - Dấu hiệu: Context bắt đầu truncated, agent bỏ qua phần quan trọng
   - Recovery: Chỉ paste 5-10 dòng error gần nhất. Dùng "chunk" - tách log thành phần nhỏ.

4. **Agent đi sai hướng giữa debug session**
   - Dấu hiệu: Agent bắt đầu optimize code không liên quan, hoặc đi ra khỏi scope
   - Recovery: Dùng checkpoint - "Quay lại checkpoint: trước khi analyze email validation bug. Đã xác định root cause là regex không include +. Tiếp tục từ đó."

5. **Over-engineer khi bug đã rõ ràng**
   - Dấu hiệu: Agent đề xuất architecture changes, refactor lớn cho một bug nhỏ
   - Recovery: "Fix đơn giản nhất trước. Không cần refactor cho bug này."

> 💰 Cost awareness: Debug loop không isolate trước có thể tốn 3-5x token. Mỗi vòng lặp "fix sai → paste error → fix sai khác" tiêu tốn ~500-2000 tokens. Isolate bug trước = tiết kiệm 60-80% chi phí debug session.

---

## ✅ Checkpoint

### Pattern Cheat Sheet

| Step | Action | Agent Role |
|------|--------|------------|
| 1. Isolate | Tách bug khỏi context rộng | Xác định boundary |
| 2. Reproduce | Xác định điều kiện trigger | Mô tả repro steps |
| 3. Hypothesize | Đưa ra root cause hypothesis | Phân tích, không guess |
| 4. Fix | Đề xuất fix (chưa apply) | Partner, không replacer |
| 5. Verify | Test fix trước khi accept | Self-check + user review |

### Checklist trước khi bắt đầu debug session

- [ ] Đã xác định exact error message chưa?
- [ ] Đã isolate được phạm vi bug chưa (file, function, line)?
- [ ] Đã loại trừ những phần không liên quan chưa?
- [ ] Log được trim còn 5-10 dòng gần nhất?
- [ ] Đã xác định điều kiện reproduce chưa?
- [ ] Agent được yêu cầu phân tích trước khi fix?

## 🔗 Liên Quan

- [PRACTICAL/05: Sửa Khi Agent Đi Sai](../PRACTICAL/05-sua-khi-agent-di-sai.md) — Kỹ thuật can thiệp khi agent debug sai hướng
- [PRACTICAL/06: Verification Habits](../PRACTICAL/06-verification-habits.md) — Verify output trước khi accept fix