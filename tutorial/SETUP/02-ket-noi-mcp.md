# MCP Servers — Giới Thiệu & Tại Sao Cần

---

## 🔥 Thực Trạng

AI agent sinh ra để giúp bạn hoàn thành task. Nhưng agent chỉ biết những gì có trong conversation — không biết documentation của thư viện bạn dùng, không tìm được code pattern trên GitHub, không browse được web để verify thông tin.

Bạn phải paste documentation vào context, tốn tokens. Hoặc agent "hallucinate" thông tin vì không có nguồn chính xác.

→ **MCP (Model Context Protocol)** giải quyết vấn đề này bằng cách cho phép agent tự tra cứu thông tin từ external tools khi cần.

---

## 🎯 Mục Tiêu

- [ ] Hiểu MCP là gì và giải quyết vấn đề gì
- [ ] Biết các MCP servers phổ biến và use cases
- [ ] Nhận diện được khi nào cần thêm MCP cho workflow
- [ ] Biết cách tìm thêm MCP servers khi cần

---

## 📖 MCP Là Gì

### Định Nghĩa

**MCP (Model Context Protocol)** là một giao thức chuẩn hóa cách AI agents kết nối với external tools và data sources.

```
┌─────────────────────────────────────────────────────────────────┐
│                      KHÔNG CÓ MCP                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User → "Explain React hooks" → Agent                           │
│         Agent: (hallucinates hoặc paste lại docs đã biết)        │
│                                                                  │
│  → Không có cách verify, không có source mới, context limited   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      CÓ MCP                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  User → "Explain React hooks" → Agent                           │
│         Agent → gọi Context7 MCP → tra docs thực từ React        │
│         Agent → trả lời với source link cụ thể                  │
│                                                                  │
│  → Có verification, có source, context không bị tràn            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧩 Hai Loại MCP Trong Hệ Sinh Thái

```
┌─────────────────────────────────────────────────────────────┐
│                   MCP TYPES                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. SKILL-EMBEDDED (built-in)                               │
│     ├── Đi kèm khi cài oh-my-openagent                       │
│     ├── Tự động có sẵn, không cần config thêm                │
│     └── Ví dụ: context7, grep_app, websearch                 │
│                                                              │
│  2. EXTERNAL (thêm vào riêng)                                │
│     ├── Cần install riêng qua opencode.json                  │
│     ├── Ví dụ: chrome-devtools, custom MCPs                  │
│     └── Thường là các tools không phải built-in               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Các MCP Servers Phổ Biến

### 📚 Documentation Lookup — context7

**Use khi:** Cần tra cứu official documentation của library/framework.

```
Task Example:
→ "How to use useEffect cleanup in React?"
→ Agent gọi context7 → lấy docs thực từ React
→ Trả lời với syntax example từ official docs
```

**Phù hợp cho:**
- API reference lookup
- Library syntax examples
- Framework-specific patterns

---

### 💻 GitHub Code Search — grep_app

**Use khi:** Cần tìm code pattern từ real-world repositories.

```
Task Example:
→ "Show me how other projects handle JWT auth in Express"
→ Agent gọi grep_app → tìm code thực từ GitHub
→ Trả lời với ví dụ có source link
```

**Phù hợp cho:**
- Finding implementation patterns
- Learning from real codebases
- Checking if patterns are commonly used

---

### 🌐 Web Research — websearch / Exa MCP

**Use khi:** Cần thông tin current events, tutorials, community discussions.

```
Task Example:
→ "What are the best practices for React 19?"
→ Agent gọi websearch → tìm articles, discussions
→ Trả lời với sources và perspectives
```

**Phù hợp cho:**
- Fresh information (post-2024)
- Community opinions and debates
- Tutorials and how-to guides

---

### 🖥️ Browser Automation — chrome-devtools

**Use khi:** Cần automate browser interactions.

```
Task Example:
→ "Take a screenshot of example.com"
→ Agent gọi chrome-devtools → navigate và screenshot
→ Trả về image hoặc page state
```

**Phù hợp cho:**
- Web scraping
- UI verification
- Automated testing workflows

---

## 📊 MCP Decision Matrix

| Tool | Use khi | Không dùng khi |
|------|---------|----------------|
| **context7** | Cần official docs, API reference | Muốn opinion, general discussion |
| **grep_app** | Tìm code patterns trên GitHub | Cần documentation cụ thể |
| **websearch** | Fresh info, tutorials, current events | Cần academic sources, deep comparison |
| **chrome-devtools** | Browser automation, screenshots | Không liên quan đến web browsing |

---

## 🤔 Khi Nào Cần Thêm MCP

### Dấu Hiệu Cần Thêm MCP

1. **Agent hallucinate thông tin** — trả lời confident nhưng sai fact
2. **Phải paste documentation vào context** — tốn tokens, context tràn
3. **Thiếu external data access** — agent không browse được web
4. **Workflow cần automated browser** — scraping, testing

### Cách Tìm MCP Mới

```
1. Xác định workflow gap — agent thiếu capability gì?
2. Tìm kiếm MCP marketplace: opencode mcp marketplace search
3. Hoặc tự viết MCP nếu có internal tools cần kết nối
```

---

## ⚠️ Lưu Ý Quan Trọng

### MCP KHÔNG Phải Magic

- MCP cho agent **khả năng tra cứu**, không phải **memory** mới
- Agent vẫn cần prompt rõ ràng để biết khi nào gọi MCP
- Một số MCP có chi phí sử dụng (token, API calls)

### Benchmark Scores Không Đáng Tin

> ⚠️ **Benchmark scores không đáng tin cậy:** Không tool nào công bố SWE-bench scores chính thức. Cursor tự xây CursorBench nội bộ vì SWE-bench bị nhiễu dữ liệu training. OpenAI dừng báo cáo SWE-bench Verified từ tháng 2/2026 vì 59.4% test cases có lỗi.

---

## ✅ Checkpoint

### MCP Benefits

| Benefit | Chi tiết |
|---------|----------|
| **Truy cập Documentation** | Agent tra cứu official docs khi cần |
| **Code Pattern Search** | Tìm real-world examples từ GitHub |
| **Fresh Information** | Web search cho current info |
| **Browser Automation** | Automated web interactions |

### MCP Selection Quick Guide

| Nhu cầu | MCP khuyến nghị |
|---------|-----------------|
| Tra cứu library docs | context7 |
| Tìm code patterns | grep_app |
| Research current info | websearch / Exa |
| Browser automation | chrome-devtools |

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [FUNDAMENTALS/03](../FUNDAMENTALS/03-skill-rule-plugin-mcp.md) | Skill, Rule, Plugin, MCP — chi tiết kỹ thuật |
| [SETUP/01](./01-chon-opencode.md) | oh-my-openagent — plugin ecosystem cho OpenCode |