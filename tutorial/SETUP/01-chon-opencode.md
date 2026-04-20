# OpenCode & oh-my-openagent — Hướng Dẫn Thiết Lập

---

## 🔥 Thực Trạng

Bạn muốn dùng AI coding agent nhưng:

- Lựa chọn nào tốt? Chi phí bao nhiêu?
- Model nào phù hợp — Claude, GPT, Gemini, hay local?
- oh-my-openagent là gì? Có cần không?
- Cài sao cho đúng và không tốn nhiều thời gian?

→ **Bài này tập trung vào thực hành** — cài đặt OpenCode + oh-my-openagent, hiểu cách chúng hoạt động, và bắt đầu dùng được ngay.

---

## 🎯 Mục Tiêu

- [ ] Hiểu tại sao tutorial này chọn OpenCode (provider-agnostic, open source, skills)
- [ ] Biết oh-my-openagent giải quyết vấn đề gì (edit reliability, autonomous workflow)
- [ ] Sẵn sàng bắt đầu — qua official documentation và configuration guidance

---

## 📖 Tại Sao Tutorial Này Chọn OpenCode

Tutorial này chọn OpenCode vì nó giải quyết **3 vấn đề thực tế** của người dùng AI agent:

### 1. Provider-agnostic — Không bị lock vào một model

OpenCode dùng được **75+ providers** — Claude, GPT, Gemini, Minimax, local models. Khi model mới ra, bạn đổi config là dùng được.

```json
// opencode.json
{
  "providers": {
    "minimax": { "model": "MiniMax-M2.7", "api_key": "..." },
    "anthropic": { "model": "claude-sonnet-4-6", "api_key": "..." }
  }
}
```

> 📌 **Tại sao quan trọng:** Claude Code lock vào Anthropic. Cursor lock vào proprietary. Tutorial dạy "cách dùng OpenCode + concepts" → skills và workflow chuyển được sang tool khác.

### 2. 100% Open Source — Inspect, extend, verify

| Stats | Value |
|------|-------|
| **GitHub stars** | **146k** ⭐ (largest open-source AI coding agent) |
| **Releases** | 770+ |
| **Contributors** | 864 |
| **License** | MIT |

Mọi thứ đều public. Code có vấn đề → đọc source, fix, hoặc báo issue. Không có "magic black box" đằng sau.

### 3. Skills System — Reusable, self-documenting

Skills là các file `SKILL.md` đặt trong project hoặc global config:

```
~/.config/opencode/skills/<name>/SKILL.md   # Global skill
.claude/skills/<name>/SKILL.md              # Claude-compatible
```

Mỗi skill có frontmatter + nội dung markdown. Agent load skill khi cần, tự động.

> 📌 **Tại sao quan trọng:** Bạn viết một skill một lần → dùng lại ở mọi project. Tutorial cung cấp **skills đã viết sẵn** cho workflow phổ biến.

---

## 🧩 Bonus Features

| Feature | Benefit |
|---------|---------|
| **Client/server architecture** | Drive từ xa, programmatic usage |
| **TUI-first** | Low barrier — terminal là đủ |
| **AGENTS.md** | Project context file — dạy agent hiểu codebase |
| **/share** | Share conversation public |
| **Multi-platform** | macOS, Linux, Windows, Docker |
| **10+ install methods** | `curl`, `brew`, `npm`, `choco` — ai cũng cài được |

---

## ⚖️ So Sánh Các AI Coding Agents

> ⚠️ **Benchmark scores không đáng tin cậy:** Không tool nào công bố SWE-bench scores chính thức. Cursor tự xây CursorBench nội bộ vì SWE-bench bị nhiễm dữ liệu training. OpenAI dừng báo cáo SWE-bench Verified từ tháng 2/2026 vì 59.4% test cases có lỗi.

| Tiêu chí | **OpenCode** | **Claude Code** | **Cursor** | **Cline** |
|---|---|---|---|---|
| **GitHub stars** | **146k** ⭐ | N/A (closed) | ~60k | ~60.5k |
| **Open source** | ✅ MIT | ❌ | ❌ | ✅ Apache-2.0 |
| **Model providers** | **Any** (75+) | Claude only | Multi | **Any via API** |
| **Interface** | TUI + Desktop + IDE | Terminal + IDE | IDE (fork VS Code) | VS Code extension |
| **MCP support** | ✅ Full | ✅ Full | ✅ (Pro+) | ✅ + auto-create |
| **Skills system** | ✅ SKILL.md | ✅ SKILL.md | ❌ | ❌ |
| **Free tier** | ✅ (GitHub Copilot, ChatGPT) | ❌ | Limited | ✅ (BYOK) |
| **Cost** | **Free** | $17-200/mo | $40-200/mo | Free |

> 💡 **Không so sánh ở đây** — Xem [ECOSYSTEM/02-so-sanh-agent-tools.md](../ECOSYSTEM/02-so-sanh-agent-tools.md) cho comparison chi tiết.

---

## 🧩 oh-my-openagent — Thêm Vào Layer Điều Phối

oh-my-openagent là **third-party plugin** (không phải built-in) bởi [@code-yeongyu](https://github.com/code-yeongyu).

> *"Most agent failures aren't the model. It's the edit tool."*

**Nó giải quyết cái gì:**

- **Hash-anchored edits**: Mỗi dòng code tag hash → edit mismatch → reject trước khi corrupt
- **ultrawork mode**: `ulw <task>` → autonomous workflow đến khi xong, không dừng giữa chừng
- **Model routing tự động**: Agent chọn model phù hợp theo task type, không cần config thủ công

---

## 🧩 11 Agents Chuyên Biệt

| Agent | Priority | Role | Model |
|-------|----------|------|-------|
| **Sisyphus** | 1 | Orchestrator — điều phối mọi task | MiniMax-M2.7 |
| **Hephaestus** | 2 | Deep autonomous worker — "give goal, not recipe" | MiniMax-M2.7 |
| **Prometheus** | 3 | Planner — interview mode trước khi code | Claude Opus 4.6 (max) |
| **Atlas** | 4 | Execution agent — thực thi plan | MiniMax-M2.7 |
| **Oracle** | — | Architecture & debugging consultant | Claude Opus 4.6 (max) |
| **Librarian** | — | Research, documentation lookup | MiniMax-M2.7 |
| **Explore** | — | Fast read-only codebase search | MiniMax-M2.7 |
| **Metis** | — | Pre-planning consultant (ambiguity analysis) | Claude Opus 4.6 (max) |
| **Momus** | — | Plan critic/reviewer | Claude Opus 4.6 (max) |
| **Multimodal-Looker** | — | Image/PDF analysis | Gemini 3.1 Pro |
| **Sisyphus-Junior** | — | Focused task executor, no delegation | MiniMax-M2.7 |

---

## 🧩 ultrawork Mode

Single command → full autonomous workflow. Không cần hướng dẫn từng bước.

```bash
ulw fix the failing tests
ultrawork implement JWT authentication

# Tự động kích hoạt:
# ✅ Parallel background agents (5+ specialists)
# ✅ Todo enforcement — giữ agent đúng task
# ✅ Comment checking — chặn AI slop
# ✅ Hash-anchored edits — không stale-line errors
# ✅ Model fallback — tự động switch model nếu fail
# → Chạy đến khi xong, không dừng giữa chừng
```

---

## 🛡️ Ưu Điểm Của oh-my-openagent

| Ưu điểm | Chi tiết |
|---------|----------|
| **Hash-Anchored Edits** | Mỗi dòng code được tag hash → edit mismatch bị reject → success rate cao hơn |
| **Model Routing tự động** | Agent được routing theo task type (ultrabrain → Opus 4.6, quick → MiniMax-M2.7) |
| **Model Fallback** | Tự động chuyển model nếu primary fail |
| **Parallel Execution** | 5+ agents chạy song song — tốc độ cao hơn sequential |
| **Comment Checking** | Chặn AI slop ngay trong code comments |
| **Todo Enforcement** | Giữ agent tập trung, không drift |

> 💡 **Khi nào dùng:**
> - **Sisyphus + ulw**: Complex tasks, agent tự figure out implementation
> - **Prometheus + Atlas**: Khi cần precise control — plan trước, execute sau

---

## 📚 Tham Khảo Thêm

| Resource | Link |
|----------|------|
| **Trang chủ** | [opencode.ai](https://opencode.ai) |
| **GitHub Repository** | [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) |
| **oh-my-openagent** | [github.com/code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) |

---

## ✅ Checkpoint

- [ ] Hiểu tại sao tutorial này chọn OpenCode (provider-agnostic, open source, skills)
- [ ] Biết oh-my-openagent giải quyết vấn đề gì (edit reliability, autonomous workflow)
- [ ] Biết 11 agents và vai trò của từng agent
- [ ] Biết cách dùng ultrawork mode: `ulw <task>`
- [ ] Hiểu Hash-Anchored Edits: reject edit mismatch trước khi corrupt
- [ ] Tham khảo được official docs cho OpenCode và oh-my-openagent

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [ECOSYSTEM/02](../ECOSYSTEM/02-so-sanh-agent-tools.md) | So sánh chi tiết OpenCode vs Claude Code vs Cursor vs Cline |
| [FUNDAMENTALS/05](../FUNDAMENTALS/05-agents-md-chuan-muc.md) | AGENTS.md — chuẩn mở cho project context |
| [SETUP/06](./06-superpowers-workflow.md) | Superpowers — structured workflow cho agent |