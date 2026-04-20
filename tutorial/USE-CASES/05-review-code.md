# Review & Cải Thiện Code

## 🔥 Thực Trạng

Bạn nhờ agent review code, đợi vài phút, nhận lại một câu "looks good" hoặc một vài nitpick về spacing. Rồi bạn deploy, và production crash vì SQL injection thật sự. Hoặc agent đề xuất 15 improvements một lúc, bạn accept hết, và codebase hỏng sau một tuần.

Vấn đề cốt lõi: agent được train để be helpful. Helpful = nice. Nice = không push back. Kết quả: review pass nhưng bug vẫn còn.

---

## 🎯 Mục Tiêu

- Biết cách scope review để agent tập trung vào đúng vấn đề
- Dùng checklist để driver agent thay vì nhận feedback generic
- Ép agent vào vai trò critical reviewer thay vì cheerleader
- Tránh scope creep khi review biến thành refactor toàn bộ codebase

---

## 🧩 Best Practices

### Core Workflow

```
Scope review → Checklist → Adversarial test → Incremental refactor
     ↑              ↑              ↑              ↑
  Bạn define    Agent check   Agent tìm      Từng bước
  boundary       từng item      cách break      một, verify
```

### Agent Role: Critical Reviewer

Agent TRONG vai trò review:
- Được phép chê (criticize code, not the coder)
- Phải tìm cách break, không chỉ confirm nó works
- Rate severity: Critical / Major / Minor

Agent KHÔNG PHẢI:
- Cheerleader ("code looks great!")
- Consultant đề xuất 10 changes một lần
- Auto-fixer không có approve

### Before/After: Scoped Review Prompt

**Before** — không scoped:

```
❌ "Review code này giùm"
→ Agent: "Looks good overall. Một vài naming suggestions."
```

**After** — scoped, adversarial:

```
✅ "Review file src/auth/login.ts:
- Focus: SQL injection risk, error handling gaps, edge cases khi email=null hoặc empty string
- Ignore: styling, variable naming conventions
- Rate mỗi issue: Critical/Major/Minor
- Nếu thấy 'looks good' → thử break nó bằng 3 edge cases trước"
```

### Khi nào KHÔNG dùng pattern này

- **Quick hotfix**: "fix typo nhanh" → không cần full review checklist
- **Proof of concept code**: code throwaway, không production-ready
- **Trusted library upgrade**: library đã stable, chỉ cần verify không break API

---

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Security Review Before Deploy

**Prompt:**

```
Review src/api/user.ts trước khi deploy:

FOCUS (chỉ những thứ này):
1. SQL injection — mọi query với user input
2. XSS — mọi output được render ra HTML
3. Auth bypass — kiểm tra authorization check đầy đủ
4. Input validation — null, empty, max length

OUTPUT FORMAT:
- Mỗi issue: [file:line] | severity | description
- Không suggest fixes (sẽ hỏi sau nếu cần)
- Nếu không có issue → ghi "No critical issues found"

Sau khi list xong: đóng vai hacker, tìm 3 cách exploit code này.
```

**Result:**

```
✅ Agent tìm được: [user.ts:23] | Critical | SQL concat với req.params.email không sanitize
✅ Agent đề xuất: "thử input: ' OR '1'='1" để test
✅ Rate severity rõ ràng

⚠️ Agent bỏ qua: styling và naming → đúng focus
```

---

### Scenario 2: Performance Review Cho Hot Path

**Prompt:**

```
Review src/database/queries.ts — đây là hot path, được gọi 1000 req/s:

FOCUS:
1. N+1 query patterns — lazy load trong loop
2. Missing indexes — WHERE clause không có index cover
3. Unbounded result set — thiếu LIMIT
4. Connection pool exhaustion — không có timeout/retry

OUTPUT:
- Mỗi issue: [query name] | estimated impact (ms/req) | severity
- Top 3 issues by impact

Sau khi list: đề xuất exactly 1 fix cho top-priority issue. Đợi tôi accept trước khi tiếp.
```

**Result:**

```
✅ Agent phát hiện: getUserOrders() chạy N+1 — 1 query + N queries trong loop
✅ Agent estimate: 150ms/req thay vì 5ms/req
✅ Agent chỉ đề xuất 1 fix: thêm JOIN để batch

⚠️ Agent KHÔNG đề xuất: refactor toàn bộ ORM → đúng scope
```

---

## 🚧 Pitfalls & Recovery

### 1. Agent Quá Polite — "Code looks good"

**Dấu hiệu:**
- Review output chỉ có positive feedback
- Không có critical issues được flag
- Agent dùng từ "suggest", "consider" thay vì "must fix", "critical"

**Recovery:**
```
"Đóng vai hacker. Tìm 3 cách break code này.
Nếu không tìm được → giải thích tại sao nó unbreakable.
Không dùng 'looks good' — thay bằng evidence."
```

---

### 2. Scope Creep — 10 Changes Một Lần

**Dấu hiệu:**
- Agent đề xuất refactor toàn bộ module cùng lúc
- Review output dài hơn 500 tokens cho một file 50 lines
- Bạn nhận "nhiều improvements" thay vì "prioritized list"

**Recovery:**
```
"Stop. Chỉ fix top 1 priority.
Tất cả others: note lại, đợi tôi accept top 1 trước.
Một lần chỉ một change."
```

---

### 3. Cost Blindness — Review Toàn Bộ Codebase

**Dấu hiệu:**
- Prompt bắt đầu bằng "review entire codebase"
- Token usage tăng vọt mà không có output tương xứng
- Review mất >5 phút cho repo >50 files

**Recovery:**
```
"Review chỉ src/auth/ và src/api/ — không phải toàn bộ.
Single file review: <2000 tokens.
Directory review (5 files): <8000 tokens.
Codebase review: reserved cho major releases thôi."

Cost comparison:
- Focused review (1 file): ~500 tokens
- Directory review (5 files): ~2000 tokens
- Full codebase review: ~50,000+ tokens
```

---

## ✅ Checkpoint

### Pattern Cheat Sheet

```
1. SCOPE: "Review [file/dir], focus [items], ignore [items]"
2. CHECKLIST: "Rate each issue: Critical/Major/Minor"
3. ADVERSARIAL: "Tìm 3 cách break code này"
4. INCREMENTAL: "Fix top 1 → wait for accept → next"
```

### Review Checklist

- [ ] Scoped prompt — file/dir cụ thể, không "review all"
- [ ] Focus items — 3-5 categories rõ ràng
- [ ] Ignore items — naming, styling explicit excluded
- [ ] Severity rating — yêu cầu Critical/Major/Minor
- [ ] Adversarial angle — "find ways to break" hoặc "hack this"
- [ ] Increment control — "top 1 only, wait for accept"

## 🔗 Liên Quan

| Bài | Liên quan |
|-----|-----------|
| [PRACTICAL/05](../PRACTICAL/05-sua-khi-agent-di-sai.md) | Sửa khi agent đi sai — dùng khi review feedback sai |
| [PRACTICAL/06](../PRACTICAL/06-verification-habits.md) | Verification habits — nhớ verify trước khi accept review |
