# LLM Wiki — CLAUDE.md

## Mục đích
Đây là schema chính cho LLM Wiki. File này quy định mọi quy tắc về cấu trúc, format, và quy trình của wiki.

## Cấu trúc thư mục

```
WIKI_ROOT/
├── CLAUDE.md              # Schema này
├── config.yaml            # Cấu hình wiki
├── wiki/
│   ├── INDEX.md          # Danh mục toàn bộ wiki pages
│   ├── LOG.md            # Nhật ký thay đổi
│   ├── SUMMARY.md        # Tóm tắt nhanh cho agent
│   ├── entities/         # Entity pages (người, tổ chức, sản phẩm)
│   ├── concepts/         # Concept pages (khái niệm, patterns)
│   ├── sources/          # Source summary pages
│   └── syntheses/        # Analysis & synthesis pages
├── raw/
│   ├── articles/        # Bài viết web đã fetch
│   ├── reddit/           # Reddit posts
│   ├── papers/           # Research papers
│   └── notes/           # Notes từ user
├── .discoveries/
│   ├── history.json      # Lịch sử discovery
│   └── gaps.json        # Knowledge gaps
└── outputs/
    ├── lint-*.md        # Lint reports
    ├── digest-*.md      # Daily digests
    ├── pain-rank-*.md   # Pain point rankings
    └── run-*.md          # Run reports
```

## Quy tắc Wiki Pages

### Naming
- File names: tiếng Anh, kebab-case
- Wiki links: `[[kebab-case-name]]`
- Không dùng tiếng Việt trong file names

### Frontmatter (required cho mọi wiki page)
```yaml
---
title: "Descriptive Title"
category: entities | concepts | sources | syntheses
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
---
```

### Content rules
- Wiki content: **tiếng Việt có dấu** (thuật ngữ kỹ thuật giữ tiếng Anh)
- Cross-refs: mỗi trang ít nhất 2 links đến trang khác
- Citations: `[Nguồn: filename](../raw/path)`
- Không bịa thông tin — chỉ viết những gì có trong raw sources

### Categories

| Category | Mô tả | Ví dụ |
|----------|-------|-------|
| **entities** | Người, tổ chức, sản phẩm, công ty | Anthropic, Claude, babyagi |
| **concepts** | Khái niệm, patterns, methodologies | RAG, chain-of-thought, tool use |
| **sources** | Tóm tắt nguồn (article, paper, video) | Summary của 1 bài viết cụ thể |
| **syntheses** | Phân tích, so sánh, tổng hợp nhiều nguồn | Comparison, pattern analysis |

## Quy tắc Raw Sources

### Frontmatter (required cho mọi raw source)
```yaml
---
title: "Tiêu đề gốc"
url: "https://..."
discovered: YYYY-MM-DD
topic: "tên topic"
type: article | reddit | paper | note
---
```

### File naming
- `YYYY-MM-DD-slug.md` — slug derived from title
- Duy trì original formatting của nguồn
- Không sửa đổi nội dung gốc

## Quy tắc Discovery

### Sources prioritization
1. Knowledge gaps từ lint
2. Reddit pain points (high upvotes, clear problem statement)
3. GitHub trending repos
4. Web search theo topic keywords
5. RSS feeds

### Deduplication
- Check URL và title trước khi fetch
- Update existing entries if newer version found

## Quy tắc Ingest

### Process
1. Đọc file raw source
2. Trích xuất key entities → tạo/cập nhật entity pages
3. Trích xuất key concepts → tạo/cập nhật concept pages
4. Tạo source summary page
5. Thêm cross-references vào các trang liên quan
6. Cập nhật INDEX.md
7. Ghi LOG.md

### Cross-reference strategy
- Entity mentions → link đến entity page
- Concept mentions → link đến concept page
- Quote claims → link đến source summary
- Mỗi source ảnh hưởng 5-15 wiki pages

## Quy tắc Lint

### Check categories
- **Contradictions**: thông tin mâu thuẫn (giữ cả hai, ghi rõ)
- **Orphans**: trang không ai link đến (trừ INDEX, LOG, SUMMARY)
- **Missing pages**: `[[link]]` trỏ đến trang chưa tồn tại
- **Stale claims**: thông tin cũ bị nguồn mới bác bỏ
- **Broken links**: link đến raw source không còn tồn tại
- **Gaps**: lĩnh vực quan trọng thiếu coverage
- **Quality**: trang quá ngắn (<100 words), thiếu sources, thiếu cross-refs

## Ngôn ngữ & Format

- Wiki content: **tiếng Việt có dấu**
- Thuật ngữ kỹ thuật: giữ tiếng Anh (API, LLM, RAG, agent...)
- File names: tiếng Anh, kebab-case
- Frontmatter: tiếng Anh
- Wiki links: `[[kebab-case-name]]`
- Output files: tiếng Việt có dấu

## Workflow Summary

```
init → discover → ingest → lint → (gaps → discover) → query/digest/pain-rank
```

- **init**: Khởi tạo wiki mới
- **discover**: Tìm nguồn mới từ internet
- **ingest**: Xử lý raw sources → tạo wiki pages
- **lint**: Kiểm tra sức khỏe wiki
- **query**: Hỏi đáp dựa trên wiki
- **digest**: Daily brief
- **pain-rank**: Xếp hạng pain points theo tiềm năng kinh doanh
