# RTK — Token Optimizer

---

## 🔥 Thực Trạng

Bạn đang dùng AI coding assistant hàng ngày và:

- Chi phí token tích lũy hàng tháng lớn hơn dự kiến
- Không biết đâu là commands "ngốn" nhiều tokens nhất
- Không có cách theo dõi và tối ưu token usage một cách có hệ thống

→ **Vấn đề thực tế:** AI coding assistant là công cụ năng suất, nhưng chi phí có thể kiểm soát được. RTK giải quyết bài toán này.

---

## 🎯 Mục Tiêu

- [ ] Hiểu RTK là transparent CLI proxy — không thay đổi workflow hiện tại
- [ ] Biết 3 lợi ích chính: tiết kiệm 60-90%, visibility, zero disruption
- [ ] Áp dụng được 3 workflows: daily review, weekly audit, debug
- [ ] Biết mình thuộc nhóm nên dùng RTK hay không

---

## 📖 RTK Là Gì

```
┌─────────────────────────────────────────────────────────────┐
│              RTK — Rust Token Killer                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Token-optimized CLI proxy cho OpenCode/Claude Code        │
│  Tự động rewrite dev commands để giảm token usage            │
│                                                              │
│  Tính năng chính:                                           │
│  ├── Transparent proxy — 0 overhead, 0 disruption            │
│  ├── Token savings analytics — biết đâu ngốn nhiều          │
│  ├── Missed opportunity detection — gợi ý chỗ tiết kiệm      │
│  └── 60-90% savings trên dev operations thông thường        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**RTK không phải:**
- ❌ Tool thay thế AI của bạn
- ❌ Công cụ giới hạn capability
- ✅ CLI proxy trong suốt — bạn không thấy nó hoạt động

---

## 🧩 Lợi Ích Của RTK

### 1. Tiết Kiệm Chi Phí — 60-90% Token Savings

```
┌─────────────────────────────────────────────────────────────┐
│                    TOKEN SAVINGS breakdown                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Dev operations thông thường:                               │
│  ├── git operations     → 60-80% savings                    │
│  ├── ls, find commands  → 70-90% savings                    │
│  ├── curl/wget          → 90%+ savings                     │
│  └── read file content  → 40-60% savings                   │
│                                                              │
│  Những operations này CHẠY THƯỜNG XUYÊN nhưng              │
│  không cần AI xử lý — RTK loại bỏ không cần hỏi AI         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Tại sao tiết kiệm được:**
- `git status`, `ls -la` → không cần AI xử lý → RTK trả lời thẳng
- `curl http://...` → RTK parse và cache → không gửi response đầy đủ lên AI
- File reads → RTK optimize trước khi đưa vào context

---

### 2. Visibility — Biết Token Đi Đâu

```
┌─────────────────────────────────────────────────────────────┐
│                  TOKEN USAGE ANALYSIS                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Trước RTK:                                                 │
│  → "Tôi không biết token đi đâu, cứ trả thôi"              │
│                                                              │
│  Sau RTK:                                                   │
│  → "Command #1 ngốn 1.1M tokens — có thể thay thế"        │
│  → "curl commands tiết kiệm 99.2K tokens/lần"              │
│  → "Read files là top consumer — cần xem lại workflow"     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### 3. Zero Disruption — Không Thay Đổi Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                      TRANSPARENT PROXY                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Bạn chạy:                                                  │
│  $ git status                                               │
│  $ ls -la                                                  │
│  $ curl https://api.example.com                             │
│                                                              │
│  RTK làm:                                                   │
│  → Rewrite thành: rtk git status, rtk ls -la               │
│  → Trả kết quả nhanh hơn, không tốn tokens                  │
│  → Bạn không thấy bất kỳ sự khác biệt nào                  │
│                                                              │
│  Workflow hiện tại: GIỮ NGUYÊN                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Ứng Dụng Thực Tế

### Workflow 1: Daily Standup — Biết Token Đi Đâu

```bash
# Sau một ngày làm việc với OpenCode
rtk gain

# Output:
# Total commands: 89
# Tokens saved: 12.3K
# Top consumer: rtk read (42%)
# → Gợi ý: Xem lại cách đọc file, có thể dùng grep thay vì đọc toàn bộ
```

**Use case:** Cuối ngày review token usage → hiểu mình đang "phung phí" ở đâu.

### Workflow 2: Weekly Audit — Tìm Missed Opportunities

```bash
# Phân tích lịch sử để tìm chỗ tiết kiệm thêm
rtk discover

# Output:
# Missed opportunity: read command được gọi 156 lần
#   → Average tokens/read: 8.2K
#   → Có thể tiết kiệm: 45% bằng grep thay vì read
#
# Missed opportunity: curl command không cache
#   → Đề xuất: Cache responses thường dùng
```

**Use case:** Tuần nào cũng review → liên tục cải thiện efficiency.

### Workflow 3: Debug Raw Command

```bash
# Khi một command chạy không đúng
rtk proxy git status

# Output: raw command output without RTK processing
# Useful khi: RTK gây ra vấn đề, cần so sánh
```

**Use case:** Khi nghi ngờ RTK gây ra unexpected behavior.

---

## 📖 RTK Hoạt Động Như Thế Nào

```
┌─────────────────────────────────────────────────────────────┐
│                    RTK INTERCEPTION                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Command của bạn:                                           │
│  $ git status                                               │
│        │                                                   │
│        ▼                                                   │
│  ┌─────────────┐    HOOK (settings.json)                     │
│  │ RTK Proxy   │◄────────────────────────────────────      │
│  └─────────────┘                                           │
│        │                                                   │
│        ├─── Command không cần AI? ────► RTK trả lời         │
│        │     (git, ls, curl...)                             │
│        │                                                   │
│        └─── Command cần AI? ────► Gửi lên AI bình thường   │
│              (code review, refactor...)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Điểm mấu chốt:**
- RTK **không can thiệp** commands cần AI
- Chỉ intercept những commands có thể trả lời locally
- Hook được config trong `settings.json` — không cần thay đổi gì thủ công

---

## ⚖️ So Sánh: Có RTK vs Không RTK

| Khía cạnh | Không có RTK | Có RTK |
|-----------|--------------|--------|
| **Token usage** | Không biết | Transparency đầy đủ |
| **git status** | Tốn tokens cho AI parse | 0 tokens |
| **ls -la** | Tốn tokens | 0 tokens |
| **curl** | Tốn tokens cho response | Optimized/cached |
| **Read file** | Full content | Intelligent extract |
| **Monthly cost** | Baseline | Giảm 12-20% thường |

---

## ✅ Khi Nào Nên Dùng RTK

```
┌─────────────────────────────────────────────────────────────┐
│                    RTK PHÙ HỢP KHI:                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ Dùng OpenCode/Claude Code hàng ngày                   │
│  ✅ Muốn tối ưu chi phí AI                                   │
│  ✅ Cần visibility vào token usage                           │
│  ✅ Muốn theo dõi productivity metrics                       │
│                                                              │
│  RTK KHÔNG CẦN THIẾT KHI:                                   │
│  ❌ Dùng AI agent ít (1-2 lần/tuần)                         │
│  ❌ Không quan tâm chi phí                                   │
│  ❌ Đã có token budget management khác                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Checkpoint

- [ ] Hiểu RTK là transparent CLI proxy — không thay đổi workflow
- [ ] Biết 3 lợi ích chính: tiết kiệm 60-90%, visibility, zero disruption
- [ ] Hiểu RTK chỉ intercept commands không cần AI
- [ ] Áp dụng được 3 workflows: daily review, weekly audit, debug
- [ ] Biết mình thuộc nhóm nên dùng RTK hay không

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [PRACTICAL/07](./../PRACTICAL/07-quan-ly-chi-phi.md) | Quản lý chi phí — token budgeting tổng thể |
| [PRACTICAL/02](./../PRACTICAL/02-quan-ly-context.md) | Quản lý context — giảm token waste |