# Tổ Chức Workspace

---

## 🔥 Thực Trạng

Bạn có một ý tưởng project. Mở terminal, tạo thư mục, bắt đầu code.

**6 tháng sau:**

```
~/project/
├── src/
├── src backup/
├── notes.md
├── notes-v2.md
├── notes-FINAL.md
├── papers/
│   ├── paper1.pdf
│   └── paper1-read.md    ← trùng thông tin với file khác
├── TODO.md
├── DONE.md
├── DONE-v2.md
└── README.md             ← lỗi thời, không ai đọc
```

### Pain point thực sự:

> Không phải "workspace lộn xộn" — mà là **"không có hệ thống từ đầu"**.

Mỗi quyết định nhỏ (đặt tên file ở đâu, notes/ có cần không) tạo ra technical debt. Càng để lâu, càng đau khi clean up.

### Chi Phí Theo Thời Gian

```
CHI PHÍ THEO THỜI GIAN:

Tuần 1:  Tạo workspace không có system  → Chi phí: 0
Tuần 4:  Bắt đầu thấy lộn xộn         → Chi phí: 2h refactor
Tuần 12: Workspace hỗn độn              → Chi phí: 1 day refactor
Tuần 24: Hoàn toàn không tìm được      → Chi phí: 2+ days refactor
                                          HOẶC abandon project
```

**Vấn đề cốt lõi:** Không có workspace system ngay từ đầu → chi phí tích lũy theo thời gian.

---

## 🎯 Mục Tiêu

- [ ] Hiểu được chi phí của việc không có workspace system ngay từ đầu
- [ ] Tạo được folder structure đúng cho 2 loại workspace (coding + knowledge)
- [ ] Áp dụng 4 nguyên tắc theo thứ tự ưu tiên (không phải ngang hàng)
- [ ] Phòng ngừa 5 anti-patterns thay vì chỉ nhận diện
- [ ] Kết nối LLM Wiki + Graphify vào đúng thời điểm trong workflow

---

## 📖 Nguyên Tắc Cốt Lõi

### 4 nguyên tắc theo THỨ TỰ ƯU TIÊN

> Quan trọng: Không phải 4 nguyên tắc ngang hàng. Áp dụng theo **STAGE** của workspace:

```
┌─────────────────────────────────────────────────────────────┐
│  WORKSPACE LIFECYCLE — Áp dụng principles theo STAGE        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Stage 1: KHỞI TẠO                                          │
│    → Convention over Ad-hoc          ← BẮT BUỘC từ đầu    │
│                                                              │
│  Stage 2: TỔ CHỨC                                          │
│    → Agent-Readable Structure        ← Trước khi thêm       │
│                                          content             │
│    → Separation of Concerns         ← Trước khi mix files  │
│                                                              │
│  Stage 3: DUY TRÌ                                         │
│    → Single Source of Truth         ← Khi đã có nhiều     │
│                                           files              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Tại sao thứ tự quan trọng:

| Thứ tự | Nguyên tắc | Khi nào áp dụng | Tại sao trước |
|--------|-----------|-----------------|-------------|
| **1** | Convention over Ad-hoc | Ngay khi tạo folder đầu tiên | Tên đặt sai → đổi sau = painful |
| **2** | Agent-Readable Structure | Trước khi đặt file đầu tiên | Structure sai → refactor = painful |
| **3** | Separation of Concerns | Trước khi mix content types | Mix rồi tách = painful |
| **4** | Single Source of Truth | Khi có 2+ files cùng topic | Trùng rồi gỡ = painful |

---

## 🧩 Nguyên Tắc 1: Convention over Ad-hoc

```
Đặt tên theo pattern, không theo ý hôm nay.

❌ Sai: notes.md, notes-final.md, notes-FINAL-v2.xlsx
✅ Đúng: README.md, CHANGELOG.md, CONTRIBUTING.md, LICENSE.md
```

**Tại sao quan trọng:** Khi mọi người đặt tên theo convention, agent (và bạn) không cần đoán file chứa gì. `docs/architecture.md` → agent hiểu ngay.

### Convention chuẩn cho workspace:

```
Folder names:  kebab-case (vd: source-code, docs, test-utils)
File names:    kebab-case.md (vd: api-reference.md, getting-started.md)
Never:        notes.md, temp.md, backup/, "Untitled", v1, v2, final, FINAL
```

---

## 🧩 Nguyên Tắc 2: Agent-Readable Structure

```
Folder structure mà agent hiểu được không cần giải thích thêm.

❌ Sai:
project/
  ├── stuff/
  ├── things/
  └── random/

✅ Đúng:
project/
  ├── src/           ← source code
  ├── docs/          ← documentation
  ├── tests/         ← test files
  └── README.md      ← entry point
```

**Tại sao quan trọng:** Agent đọc workspace để hiểu project. Structure rõ ràng → agent hiểu nhanh. Structure lộn xộn → agent phải đoán.

> 📌 **Rule:** Mỗi folder phải có README ngắn giải thích purpose. Không có folder không có mục đích.

---

## 🧩 Nguyên Tắc 3: Separation of Concerns

```
Loại nội dung khác nhau → folder khác nhau.

❌ Sai: notes/ chứa cả source code lẫn papers lẫn screenshots
✅ Đúng: raw/ cho nguồn thô, processed/ cho đã xử lý
```

**Tại sao quan trọng:** Khi raw/ tách khỏi processed/, bạn không bao giờ sửa nguồn thô. Mọi thay đổi chỉ ở processed/ — nguồn giữ nguyên.

---

## 🧩 Nguyên Tắc 4: Single Source of Truth

```
Mỗi thông tin chỉ TỒN TẠI ở một nơi duy nhất.

❌ Sai: api.md, docs/api.md, wiki/api.md → cùng một thông tin
✅ Đúng: docs/api.md là nơi DUY NHẤT → wiki/ chỉ trỏ đến docs/
```

**Tại sao quan trọng:** Agent đọc file nào trước? Đọc file cũ hay mới? Khi có single source, agent không phải đoán — chỉ có một nơi đúng để đọc.

> 📌 **Áp dụng khi nào:** Khi workspace đã có structure ổn định, bắt đầu tìm và gom trùng lặp.

---

## 🛡️ Prevention Rules (Phòng ngừa thay vì chữa)

| Rule | Làm gì KHI... |
|------|--------------|
| **Never create folder without purpose** | Tạo folder mới → phải trả lời: "folder này chứa gì mà folder khác không?" |
| **Never duplicate naming** | Muốn tạo file mới → hỏi: "file này có trùng với file nào không?" |
| **Never modify raw sources** | Muốn sửa notes/papers → thay vào processed/, không sửa raw/ |
| **Never leave orphan files** | File mới → phải được reference từ index/READMEs |
| **Never skip folder decision** | Mỗi folder mới → phải có README ngắn explaining purpose |

---

## 🧩 Workspace Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│  WORKSPACE LIFECYCLE                                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [NEW] ────► [ORGANIZE] ────► [MAINTAIN] ────► [GROW]     │
│    │             │               │               │         │
│    │             │               │               │         │
│  Stage 1      Stage 2         Stage 3         Stage 4      │
│  Khởi tạo    Tổ chức        Duy trì         Mở rộng     │
│                                                              │
│  Convention    Structure       SSoT           LLM Wiki      │
│  đầu tiên     + Separation    khi cần        + Graphify   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Stage 1: NEW — Khởi tạo

> **Trước khi tạo folder/first file — trả lời 3 câu:**

```
1. ĐÂY LÀ LOẠI WORKSPACE NÀO?
   ├── Coding project    → dùng Coding Template
   └── Knowledge/research → dùng Knowledge Template

2. MỤC ĐÍCH LÀ GÌ?
   └── Nếu không trả lời được → chưa cần tạo workspace

3. AI AGENT CẦN HIỂU GÌ?
   └── Nếu không biết → viết AGENTS.md trước
```

### Chọn template phù hợp:

| Loại workspace | Template dùng | Khi nào dùng |
|--------------|--------------|--------------|
| Coding project | Coding Template | Khi có src/, code, tests/ |
| Knowledge/Research | Knowledge Template | Khi đọc papers, notes, nghiên cứu |

### Tạo folder structure TRƯỚC KHI thêm content:

```bash
# ĐÚNG: Tạo structure trước, rồi mới thêm content
mkdir -p project/{src,tests,docs,.claude}
touch project/{src,tests,docs}/.gitkeep  # placeholder

# SAI: Bắt đầu code rồi tạo folder sau
cd project
echo "# Code here" > main.py  # Không!
```

---

## 🗂️ Stage 2: ORGANIZE — Tổ chức

**Áp dụng 4 nguyên tắc theo thứ tự:**

```
1. Convention: Đặt tên theo convention — không theo ý hôm nay
2. Structure: Mỗi folder phải có README ngắn
3. Separation: Raw/ và processed/ tách hoàn toàn
4. SSoT: Mỗi concept chỉ có 1 nơi đúng
```

### Viết AGENTS.md cho workspace:

```markdown
# AGENTS.md — Workspace Context

## Workspace Type
Coding project / Knowledge workspace

## Single Source of Truth locations
- docs/ → mọi documentation
- wiki/ → mọi knowledge được process

## Conventions
- Folder names: kebab-case
- File names: kebab-case.md
- Never: notes.md, temp.md, backup/
```

---

## 🗂️ Stage 3: MAINTAIN — Duy trì

**Prevention checklist trước mỗi quyết định:**

```
TRƯỚC KHI tạo file/folder mới:

□ File này có trùng với file nào đã có không?
□ Folder này có cần thiết không, hay gộp vào folder hiện có?
□ File này thuộc raw/ hay processed/?
□ Agent có hiểu file này chứa gì không (qua tên)?
□ Có cần update AGENTS.md không?
```

### Khi nào cần refactor:

| Signal | Action |
|--------|--------|
| Folder có > 20 files | Tách folder con theo topic |
| Có 2+ files cùng topic | Merge → SSoT |
| File không được reference | Delete hoặc relocate |
| notes/ có content > 1 tháng | Process → wiki/ |

---

## 🗂️ Stage 4: GROW — Mở rộng

> ⚠️ **QUAN TRỌNG: Không phải làm từ đầu. Chỉ làm khi workspace đã ổn định.**

```
NEW ──► ORGANIZE ──► [LLM Wiki init tại đây] ──► MAINTAIN ──► [Graphify tại đây]
                          ↓                                    ↓
               Khi workspace đã ổn              Khi có > 10 files
               định structure                    cần map relationships
```

### Khi nào khởi tạo LLM Wiki:

```bash
# ✅ ĐÚNG: Khi workspace đã có structure ổn định
# KHÔNG PHẢI: Ngay từ đầu khi chưa có gì
/llm-wiki init "project-name"
```

### Khi nào chạy Graphify:

```bash
# ✅ ĐÚNG: Khi có > 10 files cần track relationships
# KHÔNG PHẢI: Khi workspace mới tạo
/graphify ./src --mode deep
```

---

## 📁 Before & After Examples

### Coding Project

```
TRƯỚC — workspace không có system từ đầu:
~/project/
├── README.md
├── docs/
│   ├── README.md         ← trùng root README
│   ├── api.md
│   └── old-notes.md     ← orphaned
├── src/
│   └── index.js
├── TODO.md               ← lỗi thời
└── wiki/                 ← lại docs

SAU — workspace có system:
~/project/
├── src/                  ← Single Source of Truth cho code
├── tests/                ← Convention: tests/ luôn đi cùng src/
├── docs/                 ← Single Source of Truth cho docs
│   ├── README.md         ← entry point duy nhất
│   └── api.md
├── .claude/              ← agent context
│   └── AGENTS.md
└── README.md             ← trỏ đến docs/README.md
```

### Knowledge Workspace

```
TRƯỚC — không có system:
~/knowledge/
├── reading-list.md
├── reading-list-v2.md
├── papers/
│   ├── rlhf.pdf
│   └── rlhf-notes.md    ← trùng thông tin
├── bookmarks/
└── inbox.md

SAU — có system:
~/knowledge/
├── raw/                  ← NGUỒN THÔ — không bao giờ sửa
│   ├── articles/
│   ├── papers/
│   ├── reddit/
│   └── inbox/             ← "sẽ process sau"
├── wiki/                  ← processed knowledge
│   ├── INDEX.md
│   ├── entities/
│   ├── concepts/
│   └── syntheses/
├── outputs/               ← generated reports
└── CLAUDE.md             ← schema cho agent
```

---

## 📁 Folder Templates

### Template: Coding Project

```
PROJECT_NAME/
├── src/                    ← source code (Agent-Readable)
├── tests/                  ← test files
├── docs/                   ← documentation (Single Source of Truth)
│   ├── README.md
│   ├── architecture.md
│   └── api.md
├── .claude/                ← agent context (nếu dùng OpenCode)
│   └── AGENTS.md
├── scripts/                ← automation scripts
├── configs/                ← config files
├── README.md               ← entry point → trỏ đến docs/
├── LICENSE
└── .gitignore
```

**Quy tắc:**
- `docs/` là Single Source of Truth cho mọi documentation
- `README.md` root chỉ trỏ đến `docs/README.md` — không trùng lặp nội dung
- Không có folder tên `wiki/`, `notes/`, `doc/` ngoài `docs/`
- Mỗi folder có README ngắn

---

### Template: Knowledge / Research Workspace

```
KNOWLEDGE_BASE/
├── raw/                    ← NGUỒN THÔ — không bao giờ sửa
│   ├── articles/
│   ├── papers/
│   ├── reddit/
│   ├── videos/
│   └── inbox/              ← "sẽ process sau"
├── wiki/                   ← processed knowledge (LLM Wiki)
│   ├── INDEX.md
│   ├── entities/
│   ├── concepts/
│   ├── syntheses/
│   └── sources/
├── outputs/                ← generated reports
├── .claude/
│   └── AGENTS.md          ← schema cho LLM Wiki
├── CLAUDE.md               ← schema (LLM Wiki convention)
└── config.yaml             ← LLM Wiki config
```

**Quy tắc:**
- `raw/` = immutable source — LLM đọc, không bao giờ sửa
- Mỗi source tạo 5-15 wiki pages
- Thông tin mâu thuẫn → giữ cả hai, ghi rõ trong wiki
- Không bao giờ sửa file trong `raw/`

---

## ✅ Checkpoint

- [ ] Hiểu được chi phí của việc không có workspace system từ đầu
- [ ] Trả lời được 3 câu hỏi trước khi tạo workspace mới
- [ ] Biết 4 nguyên tắc theo thứ tự ưu tiên và khi nào áp dụng từng cái
- [ ] Áp dụng được 5 prevention rules
- [ ] Tạo được workspace đúng structure cho cả coding và knowledge
- [ ] Biết khi nào khởi tạo LLM Wiki và Graphify

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [SETUP/04](./04-llm-wiki-workflow.md) | LLM Wiki — tích lũy kiến thức theo thời gian |
| [SETUP/05](./05-graphify-workflow.md) | Graphify — visualize relationships |
| [FUNDAMENTALS/05](../FUNDAMENTALS/05-agents-md-chuan-muc.md) | AGENTS.md — chuẩn mở cho workspace context |