---
name: worklog
description: Ghi log công việc của session hiện tại vào WORKLOG/YYYY-MM-DD-slug.md. Tự động tổng hợp nội dung session để tạo entry có cấu trúc. Slug từ topic chính của session.
---

# worklog — Session Work Logger

## Mục đích

Khi gọi `/worklog`, hệ thống sẽ:
1. Đọc nội dung session hiện tại để tổng hợp
2. Ghi entry vào `WORKLOG/YYYY-MM-DD-slug.md` (slug từ topic)
3. Follow progressive disclosure principle

## Cấu trúc Worklog

```
WORKLOG/
├── 2026-04-22-memory-fix.md    # YYYY-MM-DD-title (slug)
├── 2026-04-21-planning.md
└── ...
```

> **Format:** `YYYY-MM-DD-slug.md` — date + short descriptive slug, lowercase, hyphenated
> **Ví dụ:** `2026-04-23-memory-architecture-fix.md`, `2026-04-22-tutorial-review.md`

## Entry Format

**Header (file name):** `WORKLOG/YYYY-MM-DD-slug.md`
- Format: `YYYY-MM-DD-slug.md`
- Slug: 2-5 words, lowercase, hyphenated
- Ví dụ: `2026-04-23-memory-architecture-fix.md`

**Header (content):**
```markdown
# Worklog — YYYY-MM-DD

## HH:MM [type] Topic ngắn

**Session:** ses_xxxxx

**Tóm tắt:**
- Mô tả ngắn gọn những gì đã làm
- Kết quả đạt được (nếu có)

**Files tạo mới:**
- `path/to/file.md` — mục đích

**Files đã đọc:**
- `path/to/file.md` — lý do đọc

**Files thay đổi:**
- `path/to/file.md` — thay đổi gì

**Tiếp theo:**
- [ ] Task cần làm tiếp
- [ ] Open question

---

```

## Type Tags

| Tag | Khi nào dùng |
|-----|---------------|
| `review` | Đánh giá, review nội dung |
| `idea` | Ý tưởng phát triển |
| `research` | Nghiên cứu, tìm hiểu nguồn |
| `draft` | Viết nháp nội dung |
| `edit` | Chỉnh sửa cải thiện |
| `feedback` | Phản hồi từ review |
| `setup` | Thiết lập workspace, cấu hình |
| `publish` | Hoàn thành và publish |

## Quy trình khi gọi `/worklog`

### Bước 1: Xác định Workspace Root

Tìm thư mục chứa:
- `WORKLOG/` directory
- `tutorial/` directory
- `wiki/` directory

### Bước 2: Tạo Entry

1. **Xác định slug** từ topic chính (2-5 words, lowercase, hyphenated)
2. **Tạo file:** `WORKLOG/YYYY-MM-DD-slug.md`
3. **Ghi content** với format trên
4. **Topic** = từ 3-5 words mô tả chủ đề chính
5. **Tóm tắt** = 2-3 sentences max, không cần chi tiết
6. **Files** = chỉ list, không copy nội dung
7. **Tiếp theo** = 1-2 items, không quá 3

> **Slug examples:**
> - Topic: "Memory Architecture Gap — Implementation" → `2026-04-23-memory-architecture-fix.md`
> - Topic: "Tutorial Review" → `2026-04-22-tutorial-review.md`
> - Topic: "Setup MCP Servers" → `2026-04-21-setup-mcp-servers.md`

### Bước 3: Báo cáo

```
✅ Đã ghi worklog: WORKLOG/YYYY-MM-DD-slug.md
📝 Entry: HH:MM [type] Topic
📋 Session: ses_xxxxx
```

## Quy tắc

| Rule | Giải thích |
|------|------------|
| **Concise** | Tóm tắt ngắn gọn, không chi tiết dài dòng |
| **References only** | Không copy nội dung, chỉ link đến files |
| **Progressive disclosure** | Entry ngắn + files = đủ để recreate context |
| **Type tag** | Luôn có tag để filter/sort được |
| **Next steps** | Quan trọng — giúp session tiếp theo nhanh vào guốc |

## Ví dụ

**Input:** `/worklog` (topic: "Memory Architecture Fix")

**Output được ghi vào `WORKLOG/2026-04-23-memory-architecture-fix.md`:**

```markdown
# Worklog — 2026-04-23

## 14:30 [edit] Memory Architecture Fix

**Session:** ses_abc123

**Tóm tắt:**
- Fix GAP 1: Memory Architecture — Oversimplified
- Thêm Memory Architecture overview vào FUNDAMENTALS/01
- Mở rộng No Persistent Memory section trong MINDSET/04
- Thêm memory tier tags vào SETUP/04 và SETUP/05 headers

**Files thay đổi:**
- `tutorial/FUNDAMENTALS/01-ai-agent-la-gi.md` — thêm Memory Architecture section
- `tutorial/MINDSET/04-gioi-han-cua-agent.md` — mở rộng No Persistent Memory
- `tutorial/SETUP/04-llm-wiki-workflow.md` — thêm Semantic Memory tag
- `tutorial/SETUP/05-graphify-workflow.md` — thêm Episodic Memory tag

**Tiếp theo:**
- [ ] GAP 2: Planning Systems
- [ ] Feedback cho author gốc

---

```
