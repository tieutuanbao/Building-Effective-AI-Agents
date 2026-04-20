# Session Hygiene

---

## 🔥 Thực Trạng

Bạn quay lại project sau vài ngày nghỉ:

```
[Day 1] Bắt đầu project A, hoàn thành setup
[Day 3] Chuyển sang project B (quên mở session mới)
[Day 5] Giờ đang hỏi về project A và B lẫn lộn
Agent: "Như chúng ta đã discuss về authentication..."
User: Chúng ta đã discuss cái gì?
```

Hoặc:

```
[Session dài 50+ messages]
User: "refactor function đó đi"
Agent: "Function nào? File nào?"
User: [Role lại context - mất 10 phút]
```

**Vấn đề thực:**

- Session cũ bị **ô nhiễm** với context từ task trước
- **Context drift** — bắt đầu nói về A, 50 messages sau đang ở Z
- Khi quay lại sau vài ngày, **mất thời gian re-orient** agent
- Agent đề cập đến quyết định từ session trước mà bạn **không còn nhớ**

→ **Bài này tập trung vào thực hành** — giữ session sạch, context rõ.

---

## 🎯 Mục Tiêu

- [ ] Mỗi task/project dùng session riêng biệt
- [ ] Mở đầu session mới với recap để agent nhanh context
- [ ] Đóng session sạch: tóm tắt + lưu decisions
- [ ] Phát hiện và fix context drift kịp thời
- [ ] Khi session unavoidable, dùng context compaction để nén

---

## 🛠️ Các Kỹ Thuật Thực Hành

### 1. Một Session, Một Mục Tiêu

**❌ SAI:**

```
Session 1: Vừa làm feature A, vừa debug feature B, vừa hỏi docs về feature C
```

**✅ ĐÚNG:**

```
Session 1: Feature A - API endpoints
Session 2: Feature A - Unit tests
Session 3: Bug fix feature B
Session 4: Research docs feature C
```

**Lợi ích:**

- Context luôn clean, không overflow
- Chi phí thấp hơn
- Agent tập trung hơn

---

### 2. Mở Đầu Với Recap

Khi bắt đầu session mới cho project đang tiến hành:

```
[Session mới - Project A, Phase 2]

Context: Project A, Phase 2. Phase 1 đã xong: database schema, basic structure.
Goal hôm nay: implement authentication.
Tech: FastAPI + JWT + PostgreSQL.
Output mong đợi: working auth endpoints với tests.
```

**Format recap:**

```
1. Project và phase hiện tại
2. Progress trước đó (đã xong gì)
3. Goal hôm nay (cần hoàn thành gì)
4. Tech stack (để agent không hỏi lại)
5. Output mong đợi (để agent đo đạt đúng)
```

---

### 3. Tóm Tắt Sau Mỗi Milestone

Sau khi hoàn thành một phase quan trọng:

```
[Summary sau khi hoàn thành API design]
- Đã agree: REST conventions với /users endpoint
- Đã reject: GraphQL (team không có kinh nghiệm)
- Còn pending: auth implementation (chờ security review tuần sau)
- Next: implement GET /users
```

**Khi nào áp dụng:**

- Sau mỗi 20-30 messages
- Khi thấy agent bắt đầu "lặp"
- Trước khi chuyển sang task mới

---

### 4. Đóng Session Sạch

Trước khi kết thúc session:

```
Kết thúc session. Tóm tắt:
1. Hoàn thành: User CRUD skeleton
2. Quyết định: dùng pydantic cho validation
3. Todo: viết test cho User model
4. Lưu vào: ./project-notes/session-2024-01-15.md
```

**Checklist trước khi đóng:**

- [ ] Tóm tắt decisions đã đưa ra
- [ ] Note những gì còn pending
- [ ] Lưu vào file/notes
- [ ] Xóa messages không cần thiết

---

### 5. Fix Context Drift

Khi phát hiện session bị off-topic:

**❌ SAI:**

```
User: ờ... vậy chúng ta đang làm gì nhỉ?
Agent: Hmm, chúng ta đã discuss về...
User: [lục lại context - mất thời gian]
```

**✅ ĐÚNG:**

```
Chúng ta đã drift khỏi topic. Reset:
- Original task: implement login API
- Off-topic đã discuss: rate limiting strategy
→ Lưu rate limiting vào notes, quay lại original task
```

**Recovery steps:**

```
1. Nhận ra drift → "Chúng ta đã drift khỏi topic"
2. Identify original task → "Original task là X"
3. Offload off-topic → "Đã note lại, quay lại X"
4. Continue → agent focus lại vào đúng task
```

---

### 6. Context Compaction (Khi Unavoidable)

Khi session dài unavoidable, yêu cầu agent nén context:

```
Tóm tắt cuộc hội thoại trong 5 câu:
- Quyết định đã đưa ra
- Task đã hoàn thành
- Task còn lại
- Technical decisions quan trọng
- Open questions cần resolve
```

**Khi nào áp dụng:**

- Session dài hơn 50 messages
- Cần giữ lịch sử quan trọng
- Chi phí token là ưu tiên

---

## ⚖️ So Sánh: Session Ô Nhiễm vs Session Sạch

| Session Ô Nhiễm | Session Sạch |
|----------------|--------------|
| Agent hỏi lại thông tin đã có | Agent nhớ context rõ ràng |
| Context drift không detect được | Drift được fix ngay |
| Không lưu decisions | Decisions được lưu vào file |
| Khó quay lại sau vài ngày | Recap nhanh trong 30 giây |
| Token usage cao vì lặp context | Token usage thấp vì clean context |

---

## ⚠️ Pitfalls & Recovery

| Pitfall | Hệ Quả | Recovery |
|---------|--------|---------|
| Một session làm nhiều tasks | Context bị noise, quyết định lẫn lộn | Tách session theo topic |
| Không recap khi quay lại | Mất thời gian re-orient | Luôn mở đầu với context summary |
| Không đóng session sạch | Decisions bị "quên" | Tóm tắt + lưu trước khi đóng |
| Drift không được fix | Task A → B → C → quên mất A | "Reset: original task là X" |
| Session quá dài mà không compact | Agent "quên" quyết định đầu | Tóm tắt sau 20-30 messages |

---

## ✅ Checkpoint

- [ ] Mỗi session có mục tiêu rõ ràng được viết ở đầu không?
- [ ] Bạn có dùng session mới cho mỗi task/project riêng biệt?
- [ ] Trước khi kết thúc, bạn có tóm tắt và lưu lại không?
- [ ] Khi quay lại project, bạn có recap context cho agent không?
- [ ] Bạn có fix context drift khi nó xảy ra?
- [ ] Session dài có được compact trước khi quá dài?

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/02](./02-quan-ly-context.md) | Quản lý Context — kỹ thuật duy trì context |
| [SETUP/03](../SETUP/03-rtk-token-optimizer.md) | RTK Token Optimizer — tóm tắt tự động |
| [SETUP/06](../SETUP/06-superpowers-workflow.md) | Superpowers Workflow — structured session management |