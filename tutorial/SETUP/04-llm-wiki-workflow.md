# LLM Wiki — Personal Knowledge Base

> **→ Semantic Memory** (Long-Term: kiến thức tích lũy)

---

## 🔥 Thực Trạng

Bạn đã từng:

- Đọc một bài viết hay, bookmark lại → quên sau 2 tuần
- Copy notes từ nhiều nguồn → không tìm lại được
- Hỏi AI về topic đã nghiên cứu → AI trả lời khác với những gì bạn đã đọc
- Cần viết doc nhưng không nhớ đã thu thập thông tin ở đâu

→ **Vấn đề thực tế:** Kiến thức vào đầu rồi đi — không tích lũy được. AI không biết những gì bạn đã đọc.

---

## 🎯 Mục Tiêu

- [ ] Hiểu LLM Wiki khác Google/AI chat: trả lời dựa trên **kiến thức của bạn**, COMPOUNDS theo thời gian
- [ ] Biết Karpathy's LLM Wiki (Apr 2026) — gist 5,000+ stars, 3-layer architecture
- [ ] Biết 3 pain points LLM Wiki giải quyết: knowledge loss, bookkeeping barrier, tích lũy không hệ thống
- [ ] Hiểu 4 chức năng chính: ingest, query, discover, lint/digest
- [ ] Biết khi nào nên dùng, khi nào thừa

---

## 📖 Nguồn Gốc: Karpathy's LLM Wiki

```
┌─────────────────────────────────────────────────────────────┐
│              Andrej Karpathy — LLM Wiki (April 2026)         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Original gist:                                             │
│  https://gist.github.com/karpathy/442a6bf555914893e...      │
│                                                              │
│  Stats: 5,000+ ⭐ | 4,734 forks                             │
│  Created: April 4, 2026                                     │
│                                                              │
│  Quote:                                                     │
│  "This is an idea file, designed to be copy pasted         │
│   to your own LLM Agent."                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

Karpathy mô tả đây là **"persistent, compounding artifact"** — kiến thức tích lũy, không phải tìm lại từ đầu mỗi lần hỏi.

> *"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims. Humans abandon wikis because the maintenance burden grows faster than the value. **LLMs don't get bored, don't forget to update a cross-reference.**"*
> — Karpathy, LLM Wiki Gist

---

## 📖 LLM Wiki Là Gì

```
┌─────────────────────────────────────────────────────────────┐
│              LLM Wiki — Personal Knowledge System            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Knowledge base mà BẠN sở hữu và duy trì                   │
│  Based on Andrej Karpathy's "LLM Wiki" pattern (Apr 2026)  │
│                                                              │
│  Ý tưởng cốt lõi:                                           │
│  ├── Raw sources (articles, papers, notes)                  │
│  │       ↓                                                  │
│  ├── Wiki pages (entities, concepts, syntheses)           │
│  │       ↓                                                  │
│  └── Query → Trả lời dựa trên đã COMPOUND                 │
│                                                              │
│  Điểm khác với Google/AI chat:                              │
│  → Trả lời dựa trên KNOWLEDGE CỦA BẠN, không phải internet │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 3-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                 THREE-LAYER ARCHITECTURE                     │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Layer 1: raw/          Layer 2: wiki/       Layer 3: Schema │
│  ┌─────────────────┐   ┌─────────────────┐  ┌─────────────┐│
│  │ Immutable       │   │ LLM-generated   │  │ CLAUDE.md    ││
│  │ source docs     │   │ markdown pages  │  │ or           ││
│  │                 │──►│                 │──►│ AGENTS.md    ││
│  │ • articles/     │   │ • entities/    │  │             ││
│  │ • papers/       │   │ • concepts/    │  │ Tells LLM    ││
│  │ • reddit/       │   │ • sources/     │  │ conventions  ││
│  │ • notes/        │   │ • syntheses/   │  │ for wiki     ││
│  └─────────────────┘   └─────────────────┘  └─────────────┘│
│                                                              │
│  LLM reads from:          LLM WRITES to:       Human writes: │
│  raw/ (never modifies)     wiki/ (owns)         schema       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

| Layer | Role | Ai đọc | Ai sửa |
|-------|------|---------|---------|
| **raw/** | Immutable sources | ✅ LLM | ❌ Never |
| **wiki/** | LLM-generated pages | ✅ Human | ✅ LLM |
| **Schema** | Conventions | ✅ LLM | Human |

---

## ⚖️ So Sánh Nhanh

| | Google Search | AI Chat | LLM Wiki |
|---|---------------|---------|----------|
| Nguồn | Internet | Internet + training | **Của bạn** |
| Cập nhật | Realtime | Depends on model | Khi bạn ingest |
| Trả lời | Links | Gen AI | **Dựa trên những gì bạn đã đọc** |
| Đáng tin | Variable | Gen AI có thể "hallucinate" | **Bạn kiểm soát** |

---

## 📖 LLM Wiki vs RAG Truyền Thống

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG vs LLM WIKI                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  RAG (Traditional):                                         │
│  Query ──► Retrieve raw chunks ──► Generate answer            │
│              ↓                                              │
│          Mỗi query: re-derive từ đầu                        │
│          Không có "knowledge accumulation"                  │
│                                                              │
│  LLM Wiki:                                                  │
│  Ingest ──► Update wiki (10-15 pages) ──► Compound         │
│              ↓                                              │
│          Mỗi source mới: wiki RICHER                        │
│          Query: đọc pre-built wiki → synthesize             │
│                                                              │
│  Key difference:                                             │
│  → RAG = retrieval at query time                            │
│  → LLM Wiki = compilation at ingest time                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 LLM Wiki Giải Quyết Vấn Đề Gì

### Vấn đề 1: Knowledge Loss

```
TRƯỚC:
Bạn đọc bài về "RLHF"
  → Hiểu rồi, bookmark
  → 2 tuần sau: "RLHF là gì nhỉ?"
  → Đọc lại từ đầu

SAU:
Bạn đọc bài về "RLHF"
  → /llm-wiki ingest
  → Wiki tạo page: entities, key concepts
  → 2 tuần sau: /llm-wiki query "RLHF là gì"
  → Wiki trả lời dựa trên bài bạn đã đọc
```

### Vấn đề 2: Bookkeeping Là Barrier

```
TRƯỚC:
Muốn maintain wiki
  → Nhưng: cập nhật cross-references, sửa summaries,
    note contradictions... quá nhiều việc
  → Human wiki = abandoned sau vài tuần

SAU:
LLM làm TẤT CẢ bookkeeping:
  → LLM đọc source mới
  → Tự động cập nhật 10-15 wiki pages
  → Tự cross-reference, note contradictions
  → Human chỉ: source + question
```

### Vấn đề 3: Tích Lũy Không Có Hệ Thống

```
TRƯỚC:
Notes copy/paste lung tung
  → 500 files, không tìm được
  → Duplicate, contradiction không biết

SAU:
/llm-wiki ingest
  → Tự động tạo entities, concepts
  → Tự động cross-reference
  → Lint phát hiện contradictions
```

---

## ⚖️ Nếu Dùng vs Không Dùng

```
┌─────────────────────────────────────────────────────────────┐
│              SO SÁNH: DÙNG vs KHÔNG DÙNG LLM WIKI           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ❌ KHÔNG DÙNG:                                              │
│  ├── Knowledge trôi nổi, không tích lũy                    │
│  ├── Hỏi AI → được câu trả lời chung chung                │
│  ├── Đọc lại cùng một bài nhiều lần                        │
│  ├── Notes rời rạc, không liên kết                         │
│  └── Không biết mình đã "biết" những gì                   │
│                                                              │
│  ✅ DÙNG LLM WIKI:                                          │
│  ├── Knowledge được tổ chức, tìm lại dễ dàng              │
│  ├── Hỏi AI → trả lời dựa trên NHỮNG GÌ BẠN ĐÃ ĐỌC       │
│  ├── Đọc một lần, hỏi nhiều lần                           │
│  ├── Cross-reference tự động giữa concepts               │
│  └── Rõ ràng: mình đã thu thập được những gì              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Các Chức Năng Chính

### 1. Ingest — Từ Raw → Wiki

```
┌─────────────────────────────────────────────────────────────┐
│                    INGEST WORKFLOW                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  raw/ (bạn đọc gì đó)                                      │
│    │                                                        │
│    ├── articles/    → Bài viết, blogs                      │
│    ├── papers/       → Research papers                       │
│    ├── reddit/      → Pain points từ community             │
│    └── notes/        → Personal notes                       │
│    │                                                        │
│    ▼                                                        │
│  /llm-wiki ingest                                          │
│    │                                                        │
│    ├── Parse content                                       │
│    ├── Extract entities (people, tools, concepts)         │
│    ├── Create wiki pages                                   │
│    ├── Add cross-references                                │
│    └── Update INDEX.md + LOG.md                           │
│    │                                                        │
│    ▼                                                        │
│  wiki/                                                      │
│    ├── entities/    → Ai là ai, tool là tool               │
│    ├── concepts/    → Khái niệm đã học                    │
│    ├── syntheses/    → Analysis, comparisons               │
│    └── sources/      → Tóm tắt từng nguồn                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2. Query — Hỏi Dựa Trên Knowledge Của Bạn

```
┌─────────────────────────────────────────────────────────────┐
│                    QUERY WORKFLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  /llm-wiki query "So sánh RAG vs fine-tuning"             │
│    │                                                        │
│    ├── Đọc INDEX.md → tìm related pages                    │
│    ├── Đọc các wiki pages liên quan                       │
│    ├── Tạo câu trả lời                                     │
│    └── Citations → [[source]] để verify                    │
│                                                              │
│  QUAN TRỌNG:                                                │
│  → Trả lời DỰA TRÊN WIKI, không dùng kiến thức bên ngoài  │
│  → Nếu wiki thiếu → nói rõ và gợi ý cần discover thêm    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3. Discover — Tự Động Tìm Nguồn Mới

```
┌─────────────────────────────────────────────────────────────┐
│                  DISCOVER WORKFLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  /llm-wiki discover                                         │
│    │                                                        │
│    ├── WebSearch theo keywords của topic                    │
│    ├── Reddit scan → tìm pain points                        │
│    ├── GitHub trending → tìm repos liên quan              │
│    └── RSS feeds → poll new content                        │
│    │                                                        │
│    ▼                                                        │
│  Lưu vào raw/ → tự động trigger ingest                    │
│                                                              │
│  → Không cần tự tìm nguồn — wiki tự động update           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4. Lint + Digest — Duy Trì Chất Lượng

| Chức năng | Mục đích |
|-----------|----------|
| `lint` | Kiểm tra contradictions, orphans, broken links |
| `digest` | Daily brief — tóm tắt thay đổi 24h |
| `pain-rank` | Xếp hạng pain points theo cơ hội |

---

## 🧩 Community Implementations

| Project | Stars | Platform | Đặc điểm |
|--------|-------|----------|-----------|
| [Understand-Anything](https://github.com/Lum1104/Understand-Anything) | 8.6k | Claude Code, Codex, Cursor | Knowledge graph visualization |
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | 2.2k | Claude Code + Obsidian | Persistent vault, hot cache |
| [llm-wiki-agent](https://github.com/SamurAIGPT/llm-wiki-agent) | 2.1k | Claude Code, Codex, OpenCode | Self-building wiki |
| [llm_wiki](https://github.com/nashsu/llm_wiki) | 1.9k | Cross-platform (Tauri) | Desktop app, Louvain detection |

---

## ✅ Khi Nào Nên Dùng LLM Wiki

```
┌─────────────────────────────────────────────────────────────┐
│                    LLM WIKI PHÙ HỢP KHI:                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ Research dồi dào (papers, articles, blogs)            │
│  ✅ Cần tích lũy kiến thức theo thời gian                  │
│  ✅ Muốn AI trả lời dựa trên những gì đã đọc              │
│  ✅ Đang làm project dài hơi (weeks/months)               │
│  ✅ Cần tra cứu lại thông tin đã đọc                       │
│                                                              │
│  LLM WIKI CÓ THỂ THỪA KHI:                                 │
│  ❌ Chỉ cần search google là đủ                             │
│  ❌ Project ngắn (1-2 ngày), không cần tích lũy            │
│  ❌ Kiến thức đã có sẵn trong head, không cần ghi lại       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Directory Structure

```
WIKI_ROOT/
├── CLAUDE.md        # Schema & rules cho wiki
├── config.yaml      # Topics, keywords, discovery settings
├── wiki/            # Processed knowledge (sau khi ingest)
│   ├── INDEX.md    # Catalog — điểm bắt đầu
│   ├── sources/    # Source summaries
│   ├── entities/   # Entity definitions (people, tools...)
│   ├── concepts/   # Concept pages
│   ├── syntheses/  # Analysis & comparisons
│   └── LOG.md      # Activity log
├── raw/             # Nguồn thô — KHÔNG BAO GIỜ sửa
│   ├── articles/    # Bài viết, blogs
│   ├── papers/      # Research papers
│   ├── reddit/      # Pain points
│   └── notes/       # Personal notes
└── outputs/         # Generated reports (lint, digest...)
```

**Quy tắc quan trọng:**
- `raw/` = NGUỒN THÔ, không bao giờ sửa
- Mỗi source tạo 5-15 wiki pages
- Luôn trích dẫn nguồn: `[Nguồn: filename](../raw/path)`
- Thông tin mâu thuẫn → giữ cả hai, ghi rõ

---

## 📋 Quick Reference

| Command | Chức năng |
|---------|-----------|
| `/llm-wiki init "topic"` | Tạo wiki mới cho topic |
| `/llm-wiki ingest` | Xử lý raw/ → wiki pages |
| `/llm-wiki query "question"` | Hỏi dựa trên wiki |
| `/llm-wiki discover` | Tìm nguồn mới tự động |
| `/llm-wiki run` | Full cycle: discover → ingest → lint |
| `/llm-wiki lint` | Kiểm tra sức khỏe wiki |
| `/llm-wiki digest` | Daily brief — tóm tắt 24h |

---

## ✅ Checkpoint

- [ ] Hiểu LLM Wiki khác Google/AI chat: trả lời dựa trên **kiến thức của bạn**, COMPOUNDS theo thời gian
- [ ] Biết Karpathy's LLM Wiki (Apr 2026) — gist 5,000+ stars, 3-layer architecture
- [ ] Biết 3 pain points LLM Wiki giải quyết: knowledge loss, bookkeeping barrier, tích lũy không hệ thống
- [ ] Phân biệt được: dùng vs không dùng LLM Wiki
- [ ] Hiểu 4 chức năng chính: ingest, query, discover, lint/digest
- [ ] Biết khi nào nên dùng, khi nào thừa

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [SETUP/05](./05-graphify-workflow.md) | Graphify — visualize relationships (bổ sung cho LLM Wiki) |
| [SETUP/07](./07-to-chuc-workspace.md) | Tổ chức workspace — khi nào init LLM Wiki |