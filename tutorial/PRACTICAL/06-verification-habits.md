# Verification Habits

---

## 🔥 Thực Trạng

Agent viết code xong, bạn chạy thử thấy lỗi. Hoặc agent tổng hợp thông tin, bạn phát hiện sai sót. Hoặc agent đưa ra "fact" mà bạn biết sai.

→ Verification không phải thiếu tin tưởng — đó là **good engineering practice**.

---

## 🎯 Mục Tiêu

- [ ] Yêu cầu agent self-verify trước khi output hoàn thành
- [ ] Thực hiện sanity check sau mỗi output quan trọng
- [ ] Verify facts từ agent bằng cross-check
- [ ] Test code standalone trước khi integrate vào project
- [ ] Dùng comparative verification khi có nhiều output

---

## 📖 Core Concepts

### Output Verification

Verification là quá trình kiểm tra output của agent để đảm bảo:

- **Correct** (đúng về mặt logic/fact)
- **Complete** (đủ theo yêu cầu)
- **Consistent** (không contradictory)
- **Usable** (có thể dùng được)

### Self-Checking

Agent có thể và nên được yêu cầu self-check. Đây không phải thiếu tin tưởng, mà là good engineering practice.

### Test-After-Writing

Sau khi agent viết code, viết test để verify. Hoặc yêu cầu agent viết test song song với code.

### Sanity Checks

Những kiểm tra nhanh để phát hiện obvious errors:

- Code có chạy được không?
- Logic có sense không?
- Output có match spec không?

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Yêu Cầu Agent Self-Verify

```
Viết function X. Sau khi viết xong, chạy 3 test cases để verify nó hoạt động.
```

---

### 2. Luôn Có Sanity Check Step

Sau khi nhận output:

```
Trước khi tiếp tục, xác nhận:
1. Code có syntax correct không?
2. Logic có đúng với spec không?
3. Edge cases đã được handle chưa?
```

---

### 3. Verify Facts

Khi agent đưa ra thông tin:

```
Bạn nói library X version 2.0 có feature Y.
Tôi cần verify: cho tôi link đến documentation của claim này.
```

---

### 4. Test Trước Khi Integrate

Khi agent viết component:

```
Trước khi integrate vào codebase, hãy tách test riêng:
- Chạy standalone được không?
- Unit test pass không?
```

---

### 5. Comparative Verification

Khi có nhiều output:

```
So sánh output của bạn với kỳ vọng:
Expected: [mô tả]
Actual: [mô tả output agent]
Match? [yes/no/partially]
```

---

## 📝 Ví Dụ Thực Tế: 3 Patterns

### Pattern 1: Không Verify

```
Agent: Viết function sort
User: OK good
[Chạy thử sau đó -> lỗi]
```

### Pattern 2: Có Verify

```
Agent: Viết function sort

User: Trước khi xong, verify:
- Input [5, 1, 4] -> Output [1, 4, 5]?
- Input [] -> Output []?
- Input [2, 2, 2] -> Output [2, 2, 2]?

Agent: Đã test, đúng.
User: OK, integrate vào project.
```

### Pattern 3: Verify Information

```
Agent: Node.js version 20 LTS released tháng 4/2023

User: Verify claim này. Link documentation?

Agent: Tôi không chắc 100%. Hãy check nodejs.org để confirm.
```

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Accept output mà không verify | Lỗi discovered quá muộn | Luôn yêu cầu self-verify trước khi finish |
| Không test standalone | Lỗi discovered khi integrate | Test riêng trước, integrate sau |
| Tin facts mà không cross-check | Thông tin sai được dùng | Yêu cầu source/link cho claims |
| Accept "looks good" mà không kiểm tra | Agent có thể hallucinate | Đặt câu hỏi cụ thể: "test với input X" |
| Không feedback khi phát hiện lỗi | Agent tiếp tục sai | Feedback để agent học và self-correct |

---

## ✅ Checkpoint

- [ ] Bạn có yêu cầu agent self-verify trước khi output hoàn thành?
- [ ] Code từ agent có được test standalone trước khi integrate?
- [ ] Facts từ agent có được cross-check không?
- [ ] Bạn có chạy thử code, hay accept ngay vì "nó là AI"?
- [ ] Khi phát hiện lỗi, bạn có feedback lại để agent học không?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [USE-CASES/05](../USE-CASES/05-review-code.md) | Review Code — verification thực chiến |
| [USE-CASES/01](../USE-CASES/01-debug-code.md) | Debug Code — verification khi fix bug |
| [PRACTICAL/02](./02-quan-ly-context.md) | Context Management — verify trong session dài |