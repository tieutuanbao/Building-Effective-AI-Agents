# Graphify — Knowledge Graph Workflow

> **→ Episodic Memory** (Long-Term: sự kiện, quan hệ)

---

## 🔥 Thực Trạng

Bạn đang cố hiểu một codebase/project mới và:

- Đọc hàng trăm files nhưng không nắm được "bức tranh toàn cảnh"
- Biết có "AuthModule" và "Database" nhưng không biết chúng liên quan thế nào
- Cố tìm dependencies giữa các modules → lần theo import statements hàng giờ
- Muốn hỏi "concept A và concept B có liên quan không?" nhưng không có cách visualize

→ **Vấn đề thực tế:** Files và documents tồn tại riêng lẻ — không có cách nhìn thấy **relationships** giữa chúng.

---

## 🎯 Mục Tiêu

- [ ] Hiểu Graphify khác grep/documentation: visualizes **relationships**
- [ ] Biết 3 pain points Graphify giải quyết: toàn cảnh, relationships, surprising connections
- [ ] Phân biệt được: dùng vs không dùng Graphify
- [ ] Hiểu 3 functions: Build, Query, Incremental Update
- [ ] Biết khi nào dùng Graphify vs LLM Wiki (bổ sung cho nhau)

---

## 📖 Nguồn Gốc

```
┌─────────────────────────────────────────────────────────────┐
│          Knowledge Graph Visualization (Inspired 2026)      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Inspired by: Karpathy's LLM Wiki pattern                    │
│  https://gist.github.com/karpathy/442a6bf555914893e...      │
│                                                              │
│  Quote:                                                      │
│  "drop anything into a folder - papers, tweets,             │
│   screenshots, code, notes - and get a structured          │
│   knowledge graph that shows you what you didn't           │
│   know was connected."                                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Lưu ý về độ chính xác của attribution:**
- Karpathy's LLM Wiki dùng **markdown wiki + Obsidian graph view** (optional visualization)
- Graphify tạo **formal knowledge graph** (nodes, edges, community detection) thay vì chỉ markdown + links
- Graphify là **evolution** của concept, không phải implementation cụ thể

---

## 📖 Graphify Là Gì

```
┌─────────────────────────────────────────────────────────────┐
│              Graphify — Knowledge Graph Generator            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  any input (code, docs, papers, images)                    │
│        ↓                                                    │
│  Knowledge Graph (nodes + edges)                            │
│        ↓                                                    │
│  Clustered Communities                                      │
│        ↓                                                    │
│  Interactive Visualization + Query                          │
│                                                              │
│  Ý tưởng cốt lõi:                                           │
│  → Thay vì hỏi "file nào chứa X?"                           │
│  → Hỏi "concept A liên quan gì đến concept B?"             │
│  → Trả lời bằng VISUAL PATH chứ không phải grep            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚖️ So Sánh Nhanh

| | File Search (grep) | Documentation | Graphify |
|---|-------------------|---------------|----------|
| Tìm file | ✅ | ❌ | ❌ |
| Hiểu toàn cảnh | ❌ | Partial | ✅ Visual map |
| Concept relationships | ❌ | Implicit | ✅ **Explicit edges** |
| Query | File names | Nội dung | **Graph traversal** |

---

## ⚖️ Graphify vs Karpathy's Original Pattern

| Aspect | Karpathy LLM Wiki | Graphify |
|--------|-------------------|----------|
| Input | `raw/` folder | Any path |
| Output | Markdown wiki + `[[wikilinks]]` | Formal graph (nodes, edges) |
| Cross-refs | `[[links]]` (implicit) | Typed edges (explicit) |
| Visualization | Obsidian graph view (external) | Built-in interactive HTML |
| Graph structure | Implied via links | **Explicit**: NetworkX, community detection |
| Confidence | N/A | EXTRACTED/INFERRED/AMBIGUOUS |

---

## 🧩 Graphify Giải Quyết Vấn Đề Gì

### Vấn đề 1: Hiểu Codebase Toàn Cảnh

```
TRƯỚC:
Đọc 200 files trong codebase
  → Hiểu từng file riêng lẻ
  → Không biết chúng liên quan thế nào

SAU:
/graphify ./src
  → Interactive graph.html
  → Thấy "AuthService" kết nối đến 5 modules khác
  → Thấy "Database" là god node — được 12 modules reference
```

### Vấn đề 2: Tìm Relationship Giữa Concepts

```
TRƯỚC:
Hỏi: "AuthModule và Database liên quan không?"
  → grep hàng giờ để trace imports
  → Kết quả: có thể liên quan, có thể không

SAU:
/graphify path "AuthModule" "Database"
  → Output: AuthModule → UserRepository → Database
  → 2 hops, exact path
```

### Vấn đề 3: Surprising Connections

```
TRƯỚC:
Đọc documentation → assumed A và B không liên quan
  → Bất ngờ khi biết chúng cross-reference

SAU:
Graphify report tự động highlight:
  → "Surprising connection: FrontendService ↔ LegacyAdapter"
  → Cross-community link — không ngờ tới
```

---

## ⚖️ Nếu Dùng vs Không Dùng

```
┌─────────────────────────────────────────────────────────────┐
│            SO SÁNH: DÙNG vs KHÔNG DÙNG GRAPHIFY              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ❌ KHÔNG DÙNG:                                             │
│  ├── Hiểu codebase = đọc từng file, nhớ tổng thể            │
│  ├── Tìm relationships = grep, trace imports thủ công        │
│  ├── "God view" = đọc hết documentation                     │
│  └── Dependencies = rely on brain                          │
│                                                              │
│  ✅ DÙNG GRAPHIFY:                                          │
│  ├── Visual map toàn cảnh codebase (graph.html)            │
│  ├── Query relationships: `/graphify path A B`              │
│  ├── Surprising connections được tự động highlight          │
│  └── Incremental update khi codebase thay đổi               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Các Chức Năng Chính

### 1. Build Graph — Tạo Knowledge Graph

```
┌─────────────────────────────────────────────────────────────┐
│                    BUILD WORKFLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  /graphify <path>                                           │
│    │                                                        │
│    ├── Parse input (code, docs, papers...)                 │
│    ├── Extract nodes (functions, classes, concepts)         │
│    ├── Extract edges (imports, calls, references)         │
│    ├── Assign confidence (EXTRACTED/INFERRED/AMBIGUOUS)    │
│    └── Cluster into communities                            │
│    │                                                        │
│    ▼                                                        │
│  Outputs:                                                  │
│  ├── graph.html     → Interactive visualization             │
│  ├── GRAPH_REPORT.md → Audit trail + insights             │
│  └── graph.json     → Raw data (for queries)                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Confidence Tags — Độ tin cậy của edges:**

| Tag | Meaning | Example |
|-----|---------|---------|
| **EXTRACTED** | Explicit in source | `import A from B`, `call foo()` |
| **INFERRED** | Reasonable inference | Shared data structure |
| **AMBIGUOUS** | Uncertain | Flag để review, don't omit |

### 2. Query Graph — Hỏi Về Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                    QUERY MODES                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  /graphify query "question"         → BFS (broad context)  │
│  /graphify query "question" --dfs   → DFS (specific path)  │
│  /graphify query "question" --budget 1500 → cap tokens    │
│                                                              │
│  /graphify path "A" "B"             → Shortest path A→B    │
│  /graphify explain "Concept"         → Plain-language       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Use cases:**
- `path "AuthService" "Database"` → Exact relationship path
- `query "main architecture pattern"` → BFS traversal tìm patterns
- `explain "SwinTransformer"` → Plain-language explanation

### 3. Incremental Update — Cập Nhật Khi Thay Đổi

```
┌─────────────────────────────────────────────────────────────┐
│                    INCREMENTAL UPDATE                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  /graphify <path> --update                                 │
│    │                                                        │
│    ├── Chỉ re-extract files mới/thay đổi                   │
│    ├── Merge vào existing graph.json                       │
│    └── Không rebuild toàn bộ graph                         │
│                                                              │
│  → Codebase lớn (1000+ files) → cần incremental            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Outputs Giải Thích

### graph.html — Interactive Visualization

```
Features:
├── Nodes colored by community (cluster)
├── Click node → xem connections
├── Hover → xem labels
└── Mở trong browser, không cần server
```

### GRAPH_REPORT.md — Audit Trail

```markdown
## God Nodes (most connected)
## Surprising Connections (cross-community links)
## Suggested Questions
## Audit Trail
   EXTRACTED → edge rõ ràng trong source
   INFERRED → edge được suy luận
   AMBIGUOUS → edge không chắc chắn, cần verify
```

### graph.json — Raw Data

```json
{
  "nodes": [...],
  "edges": [
    {"source": "A", "target": "B", "confidence": "EXTRACTED"}
  ]
}
```

---

## ✅ Khi Nào Nên Dùng Graphify

```
┌─────────────────────────────────────────────────────────────┐
│                  GRAPHIFY PHÙ HỢP KHI:                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ✅ Understand new codebase (onboarding)                  │
│  ✅ Map dependencies trong large project                    │
│  ✅ Find unexpected connections giữa modules               │
│  ✅ Research corpus — thấy relationships giữa papers       │
│  ✅ Architecture review — visual map decision               │
│                                                              │
│  GRAPHIFY CÓ THỂ THỪA KHI:                                 │
│  ❌ Codebase nhỏ (< 20 files), đã hiểu rõ                   │
│  ❌ Chỉ cần tìm file chứa keyword → grep đủ               │
│  ❌ Không cần hiểu relationships                            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## ⚖️ Graphify vs LLM Wiki — Khi Nào Dùng Cái Nào

```
┌─────────────────────────────────────────────────────────────┐
│              COMPLEMENTARY TOOLS                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  LLM WIKI:                                                  │
│  → Bạn đọc gì? → Knowledge tích lũy được                   │
│  → Hỏi: "Những gì tôi đã đọc về X?"                        │
│  → Focus: WHAT YOU KNOW                                    │
│                                                              │
│  GRAPHIFY:                                                  │
│  → Files có gì? → Relationships được visualize             │
│  → Hỏi: "A và B liên quan thế nào?"                       │
│  → Focus: HOW THINGS CONNECT                               │
│                                                              │
│  → DÙNG CẢ HAI:                                            │
│  → Graphify hiểu cấu trúc                                   │
│  → LLM Wiki tích lũy kiến thức                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Quick Reference

| Command | Chức năng |
|---------|-----------|
| `/graphify <path>` | Build graph từ path |
| `/graphify <path> --mode deep` | Thorough extraction |
| `/graphify <path> --update` | Incremental update |
| `/graphify query "question"` | BFS query |
| `/graphify query "?" --dfs` | DFS query (specific path) |
| `/graphify path "A" "B"` | Shortest path A → B |
| `/graphify explain "concept"` | Plain-language explanation |
| `/graphify add <url>` | Fetch URL vào graph |

**Outputs:**
- `graph.html` → Interactive visualization
- `GRAPH_REPORT.md` → Audit + insights
- `graph.json` → Raw data (persistent)

---

## ✅ Checkpoint

- [ ] Hiểu Graphify khác grep/documentation: visualizes **relationships**
- [ ] Biết 3 pain points Graphify giải quyết: toàn cảnh, relationships, surprising connections
- [ ] Phân biệt được: dùng vs không dùng Graphify
- [ ] Hiểu 3 functions: Build, Query, Incremental Update
- [ ] Hiểu confidence tags: EXTRACTED/INFERRED/AMBIGUOUS
- [ ] Biết khi nào dùng Graphify vs LLM Wiki (bổ sung cho nhau)

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [SETUP/04](./04-llm-wiki-workflow.md) | LLM Wiki — tích lũy kiến thức (bổ sung cho Graphify) |
| [SETUP/07](./07-to-chuc-workspace.md) | Tổ chức workspace — khi nào chạy Graphify |