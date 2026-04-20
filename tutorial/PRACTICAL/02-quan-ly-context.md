# Quản Lý Context Trong Thực Tế

---

## 🔥 Thực Trạng

Context ngày càng dài. Agent bắt đầu "quên" thông tin từ đầu session. Chi phí token tăng vọt vì context chứa lịch sử hội thoại. Đôi khi agent lặp lại thông tin đã nói hoặc mâu thuẫn với những gì đã được xác nhận.

→ **Bài này tập trung vào thực hành** — không định nghĩa lại khái niệm.

---

## 🎯 Mục Tiêu

- [ ] Áp dụng 5 kỹ thuật quản lý context hiệu quả
- [ ] Biết khi nào **tóm tắt** vs **reset session**
- [ ] Tối ưu chi phí token bằng cách giữ context sạch
- [ ] Tích hợp RTK Token Optimizer khi cần
- [ ] Tránh context explosion trong session dài

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. System Prompt Thông Minh

Đặt vào system prompt **thiết yếu và ngắn gọn**:

```
✅ NÊN đặt:
- Vai trò và giới hạn của agent
- 3-5 quy tắc quan trọng nhất
- Format preference cụ thể

❌ KHÔNG đặt:
- Documentation dài (đặt vào file riêng)
- List quá dài rules (agent sẽ ignore)
- Thông tin mơ hồ, không actionably
```

> 💡 **Tip:** System prompt tối ưu = dưới 100 lines. Agent đọc được ~200 lines đầu tiên.

---

### 2. Tóm Tắt Trước Khi Tiếp Tục

Khi session dài (>20 messages), yêu cầu agent tóm tắt:

```
Tóm tắt cuộc hội thoại trong 5 câu:
- Quyết định đã đưa ra
- Task đã hoàn thành
- Task còn lại
```

**Khi nào áp dụng:**
- Sau mỗi 20-30 messages
- Khi thấy agent bắt đầu "lặp"
- Trước khi chuyển sang task mới

---

### 3. Tách Session Theo Topic

Mỗi session nên tập trung vào **một task/project cụ thể**.

```
✅ NÊN:
- Session 1: Refactor function A
- Session 2: Viết unit test cho B
- Session 3: Review code C

❌ KHÔNG NÊN:
- Một session làm cả 3 trên cùng lúc
```

**Lợi ích:**
- Context luôn clean, không overflow
- Chi phí thấp hơn
- Agent tập trung hơn

---

### 4. Dùng Tool Đọc File Thay Vì Paste

**❌ SAI (tốn tokens, context overflow):**

```
Đọc code sau và refactor:

[file1.py - 500 lines]
[file2.py - 300 lines]
[file3.py - 200 lines]
```

**✅ ĐÚNG (dùng tool):**

```
Dùng tool đọc src/utils/helpers.py
Chỉ refactor function `parse_date` và `format_currency`.
Không cần đọc các function khác.
```

> 📌 **Nguyên tắc:**
> - Dùng tool đọc file → agent tự extract phần cần
> - Paste content → tốn tokens, có thể miss context quan trọng

---

### 5. Xóa/Archive Message Không Cần Thiết

Sau khi hoàn thành một subtask:

1. **Xóa** messages không còn liên quan
2. **Archive** decisions quan trọng vào file riêng
3. **Keep** chỉ context cần thiết cho task hiện tại

```
Sau khi hoàn thành subtask:
→ Xóa messages về research phase
→ Keep decisions và code changes
→ Tiếp tục với context sạch
```

---

## ⚖️ So Sánh: Paste vs Tool

| Sai | Đúng |
|-----|------|
| Paste toàn bộ file vào prompt | Dùng tool đọc file, chỉ định phần cần |
| Đổ tất cả vào context | Progressive disclosure — chỉ cung cấp khi cần |
| Một session cho nhiều task | Tách session theo topic |

---

## 🔄 RTK Integration (Khi Cần)

Khi context gần đầy nhưng không muốn reset:

**RTK Token Optimizer** giúp:
- Tóm tắt context tự động
- Tối ưu token usage
- Giữ context sạch mà không mất thông tin quan trọng

**Khi nào dùng RTK thay vì manual:**
- Session dài hơn 50 messages
- Cần giữ lịch sử quan trọng
- Chi phí token là ưu tiên

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Paste toàn bộ file | Context overflow, agent miss phần quan trọng | Dùng tool đọc file + chỉ định phần cần |
| Session quá dài mà không summarize | Agent "quên" quyết định đầu session | Tóm tắt sau 20-30 messages |
| System prompt quá dài | Agent bỏ qua hoặc confuse | Giữ dưới 100 lines, chỉ essential rules |
| Mix nhiều topics trong một session | Context bị noise, quyết định lẫn lộn | Tách session theo topic |
| Không track token usage | Chi phí phát sinh không kiểm soát | Dùng RTK hoặc check context size định kỳ |

---

## ✅ Checkpoint

- [ ] System prompt có chứa essential rules và dưới 100 lines?
- [ ] Bạn có tóm tắt khi session dài (>20 messages)?
- [ ] Session hiện tại có tập trung vào một topic không?
- [ ] Bạn có dùng tool đọc file thay vì paste?
- [ ] Bạn có xóa/archive nội dung không cần thiết?
- [ ] Bạn có track token usage trong session?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [FUNDAMENTALS/02](../FUNDAMENTALS/02-cac-khai-niem-core.md) | Phân tầng Engineering — lý thuyết Context Engineering |
| [SETUP/03](../SETUP/03-rtk-token-optimizer.md) | RTK Token Optimizer — tự động tối ưu |
| [PRACTICAL/01](./01-viet-prompt-hieu-qua.md) | Viết Prompt — kết hợp với context management |
| [PRACTICAL/04](./04-session-hygiene.md) | Session Hygiene — duy trì context sạch |