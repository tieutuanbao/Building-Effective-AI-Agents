# Viết Docs & Content

## 🔥 Thực Trạng

Agent viết README xong, đọc lại thấy generic quá. "Leveraging cutting-edge technology to deliver robust solutions" — ai vậy? Code của mình đâu? API thực tế đâu? Agent sinh content theo template, không có project-specific detail. Giọng AI rõ rệt: "seamless", "powerful", "seamlessly integrates" — thứ mà không developer nào viết trong docs thật. Và khi bạn cần hướng dẫn technical blog, agent viết marketing copy thay vì technical content.

Đây là failure mode phổ biến: agent làm ghostwriter mà không có voice guide. Output đọc được nhưng không phải của bạn, không match project thật.

## 🎯 Mục Tiêu

- Viết prompt cho docs/content với voice constraints rõ ràng
- Phân biệt được khi nào agent là co-writer vs ghostwriter
- Build structure outline trước khi draft
- Tránh giọng AI generic bằng explicit ban list
- Verify code examples match actual implementation

## 🧩 Best Practices

### Core Workflow

```
Audience → Structure → Draft with examples → Voice iteration
```

**Audience**: Xác định reader trước. JS dev đọc khác data engineer. Beginner khác experienced.

**Structure**: Outline trước, không prompt thẳng "viết README". Bạn define structure, agent fill content.

**Draft with examples**: Yêu cầu agent trích dẫn code thực từ project. Không placeholder.

**Voice iteration**: Sau draft đầu, review voice. Nếu generic, thêm constraints và iterate.

### Agent Role

```
LÀ: co-writer (bạn outline, agent expand, bạn edit)
KHÔNG PHẢI: ghostwriter (agent tự do generate từ đầu)
```

Agent không biết voice của bạn/project. Bạn phải guide.

### Before/After

**❌ BAD — no voice constraints:**
```
Viết README cho project này.
```

Agent sinh generic intro, marketing language, không có specific details.

**✅ GOOD — structured prompt với voice guide:**
```
Viết README cho library date-utils.
Audience: JS devs cần date formatting, đã quen với vanilla Date API.
Structure:
  1) One-line description (dưới 15 words)
  2) Install (npm command)
  3) Quick start (3 examples thực tế, mỗi example là code chạy được)
  4) API reference (mỗi method có signature + 1 example)

Tone: concise, technical, không emoji.
Ban words: "robust", "seamless", "leveraging", "cutting-edge", "powerful", "game-changer".
Mỗi example phải là code thực từ src/ folder, không placeholder.
```

Agent có structure, audience, tone, và constraint cụ thể. Output match project thật.

### Khi nào KHÔNG dùng pattern

- Quick inline comments trong code (dùng thường xuyên, không cần formal prompt)
- Change log ngắn, repetitive format (agent hơi overkill cho 2-line entries)
- Content cần personal voice quá mạnh (personal blog, newsletter — bạn viết draft đầu rồi mới nhờ agent edit)

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: API documentation từ codebase

**Prompt:**
```
Generate API docs cho src/api/ folder.

1. Đọc tất cả export functions từ index.ts và các submodules
2. Với mỗi function, trích:
   - Function signature (copy exact từ source)
   - Parameters (name + type + description nếu có)
   - Return value
   - Example usage (VIẾT CODE THỰC, không placeholder)

Output format:
## [functionName]
\`\`\`typescript
[exact signature]
\`\`\`
Description: [1-2 sentences]

Parameters:
- [name]: [type] — [description]

Returns: [type]

Example:
\`\`\`typescript
[real example from actual usage]
\`\`\`

Voice constraints:
- Description ngắn gọn, mô tả WHAT không phải WHY
- Không marketing language ("powerful", "flexible")
- Technical terms giữ nguyên English (callback, promise, async)
- Code example phải run được, copy từ thực tế hoặc viết theo pattern trong source

Ban words: "robust", "seamless", "leveraging", "intuitive", "powerful", "seamlessly"
```

**✅ What happens**: Agent parse source, extract exact signatures, generate docs với real examples.

**⚠️ Watch for**: Agent extrapolate function behavior từ tên function. Verify examples bằng cách check xem code actually chạy được không.

---

### Scenario 2: Technical blog post từ implementation experience

**Prompt:**
```
Viết blog post (600-800 words) về topic: "Tại sao tôi chọn Zustand thay vì Redux cho project React của tôi"

Context:
- Project: React dashboard app, 50+ components
- Team: 3 devs, TypeScript intermediate level
- Problem đã solve: Boilerplate Redux quá nhiều, maintainance khó

Voice guide:
- Giọng: first-person narrative, honest, có code thật
- ĐỪNG viết như marketing review
- Include actual code snippets từ project thực
- Balance: đề cập cons của Zustand, không chỉ pros

Structure:
1) Hook (1 paragraph) — tình huống dẫn đến decision
2) Problem với Redux (với code example)
3) Why Zustand (với code example, so sánh line count)
4) Gotchas encountered (thật)
5) Conclusion (recommendation có context, không universal)

Ban words: "game-changer", "revolutionize", "cutting-edge", "robust", "seamless"
Code examples: paste actual code từ src/ store folder. Nếu không có, nói rõ là example thay vì production code.
```

**✅ What happens**: Agent viết content có personality, actual code snippets, honest assessment.

**⚠️ Watch for**: Agent invent code examples không tồn tại. Force agent cite source file: "Example này từ file nào trong project?"

## 🚧 Pitfalls & Recovery

**1. Giọng AI generic (corporate buzzwords)**
Dấu hiệu: Đọc thấy "leveraging", "seamless", "robust", "cutting-edge", "powerful" trong docs. Prompt chứa corporate language hoặc không có voice constraints.
Recovery:
- Thêm explicit ban list trong prompt: "Ban words: X, Y, Z"
- Sau draft đầu, grep cho buzzwords: `grep -i "robust\|seamless\|leveraging" README.md`
- Nếu thấy, feedback: "Voice generic quá. Rewrite với tone: technical, concise, first-person."

**2. Agent bịa code examples không match actual API**
Dấu hiệu: Example trong docs không chạy được khi copy paste. Function signature không match source.
Recovery:
- Prompt phải include: "Trích code từ src/ folder. Nếu không có thực, nói rõ 'example only'."
- Sau draft, run: `node --check` hoặc `tsc --noEmit` trên example code
- Yêu cầu agent cite source file: "Example này từ [filename]:[line]"

**3. Docs drift khỏi code thực tế**
Dấu hiệu: Sau vài commits, docs mô tả API không còn đúng. Agent update docs nhưng không sync với implementation.
Recovery:
- Mỗi khi merge PR, automate check: "Docs có match code không?"
- Pattern: "Update docs = update code first, docs after"
- Agent phải cite version: "Docs này describe code từ commit [hash]"

**4. Agent viết quá dài khi topic cần concise**
Dấu hiệu: 2000-word intro cho tool đơn giản. Over-explanation cho 1-line utility.
Recovery:
- Thêm constraint: "Tối đa [X] words cho section này. Concise là ưu tiên."
- Feedback: "Rút ngắn. Mỗi sentence phải justify sự tồn tại của nó."

## ✅ Checkpoint

### Pattern Cheat Sheet

```
Audience Definition:
  - Ai đọc? (JS dev, data engineer, beginner)
  - Họ đã biết gì?
  - Họ cần gì?

Structure First:
  - Bạn outline, agent fill
  - 1-2-3-4 structure rõ ràng
  - Không "viết X" chung chung

Voice Constraints:
  - Ban list words (robust, seamless, leveraging)
  - Tone: concise vs narrative vs technical
  - First-person vs third-person

Code Examples:
  - Must be real, copy from source
  - Verify runnable (node --check)
  - Cite source file:line

Iteration:
  - Draft 1: structure check
  - Draft 2: voice check (grep buzzwords)
  - Draft 3: code verification
```

### Checklist

- [ ] Prompt có audience definition rõ
- [ ] Structure specified trước khi draft
- [ ] Ban words list trong prompt
- [ ] Yêu cầu code examples từ source, không placeholder
- [ ] Agent cite source file cho mỗi example
- [ ] Sau draft: grep buzzwords, verify code runnable
- [ ] Review voice — first-person vs third-person, tone match project

## 🔗 Liên Quan

- **PRACTICAL/01-viet-prompt-hieu-qua.md** — Prompt structure cơ bản (role, task, context, output format)
- **PRACTICAL/06-verification-habits.md** — Verification protocol cho code examples, cách verify output trước khi ship

(End of file — 232 lines)