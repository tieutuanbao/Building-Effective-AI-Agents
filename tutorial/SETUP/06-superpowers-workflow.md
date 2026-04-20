# Superpowers — Structured Workflow Cho Agent

---

## 🔥 Thực Trạng

Bạn dùng AI agent và gặp cảnh này:

```
Bạn: "thêm chức năng login"
Agent: *viết code ngay* → *viết thêm* → *viết tiếp* → "xong rồi!"
Bạn check: 3 bug runtime, 2 security issues, 1 endpoint không handle error
```

### Vấn đề cốt lõi:

| Vấn đề | Chi tiết |
|--------|----------|
| **Jumping to code** | Agent code ngay — không hỏi spec, không có design |
| **Inconsistent results** | Lần được lần không |
| **No checkpoint** | Agent tự quyết định "xong" khi chưa xong |
| **No verification** | Bug đến production mới biết |
| **No review** | Code pass là pass |

Bạn muốn: quy trình rõ ràng, agent hỏi trước khi code, có checkpoint, verify trước khi claim done.

→ **Superpowers** là framework cho structured agent workflow.

---

## 🎯 Mục Tiêu

- [ ] Hiểu pain point: agent jumping to code → cần structured workflow
- [ ] Biết 7 workflows từ brainstorming → finishing
- [ ] Biết brainstorming = Socratic Q&A trước khi code
- [ ] Biết TDD = RED-GREEN-REFACTOR bắt buộc
- [ ] Biết Superpowers ≠ oh-my-openagent (bổ sung nhau)
- [ ] Tham khảo được documentation để setup khi cần

---

## 📖 Superpowers Structured Workflow

### Before/After Comparison

| Khía cạnh | **Không có Superpowers** | **Có Superpowers** |
|-----------|--------------------------|-------------------|
| **Trước khi code** | Agent code ngay | Agent **hỏi spec** qua brainstorming |
| **Planning** | Ad-hoc, agent tự quyết | Structured plan với exact file paths |
| **Testing** | Code trước, test sau (hoặc không) | **TDD enforced** — test trước |
| **Giữa chừng** | Agent tự đánh giá "xong" | **Checkpoint + review** trước khi continue |
| **Kết quả** | Inconsistent | **Consistent** — theo quy trình |

### Workflow Overview (7 Bước)

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUPERPOWERS WORKFLOW                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. brainstorming      → Hiểu spec thật sự (Socratic Q&A)       │
│         ↓                                                      │
│  2. writing-plans     → Task breakdown có verify steps          │
│         ↓                                                      │
│  3. subagent-driven   → Execute với parallel agents             │
│         ↓                                                      │
│  4. test-driven-development → RED-GREEN-REFACTOR                 │
│         ↓                                                      │
│  5. requesting-code-review → Review against plan                │
│         ↓                                                      │
│  6. finishing-a-development-branch → Merge/PR decision          │
│                                                                  │
│  ✦ Skills check TRƯỚC MỖI TASK — mandatory, not optional        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧩 Skills Library

### Core Workflow Skills

| Skill | Trigger | Mục đích |
|-------|---------|----------|
| **brainstorming** | Trước khi code | Socratic questioning — hiểu spec thật sự trước khi implement |
| **writing-plans** | Sau design approved | Task breakdown rõ ràng, mỗi task có verify steps |
| **executing-plans** | Có plan sẵn | Batch execution với checkpoints |
| **subagent-driven-development** | Có plan sẵn | Parallel agents với two-stage review |

### Quality Assurance Skills

| Skill | Trigger | Mục đích |
|-------|---------|----------|
| **test-driven-development** | During implementation | RED-GREEN-REFACTOR cycle — test trước, không ngoại lệ |
| **systematic-debugging** | Bug/tunnel vision | 4-phase root cause process |
| **verification-before-completion** | Trước khi claim done | Ensure fix actually works |
| **requesting-code-review** | Giữa các tasks | Review against plan, report by severity |
| **receiving-code-review** | Khi nhận feedback | Respond có verification |

### Collaboration Skills

| Skill | Trigger | Mục đích |
|-------|---------|----------|
| **using-git-worktrees** | Sau design approved | Isolated branch per feature, clean workspace |
| **finishing-a-development-branch** | Task complete | Verify → merge/PR/keep/discard decision |

---

## 📖 Chi Tiết: brainstorming

### Vấn đề

Agent nhận task → code ngay → hiểu sai spec → rewrite nhiều lần → frustrated.

### Giải pháp

brainstorming skill kích hoạt **TRƯỚC KHI CODE**:

```
You: "thêm chức năng login"
Agent: "Trước khi code, tôi có vài câu hỏi:
  1. Login bằng gì? (email/password, OAuth, SSO?)
  2. User roles? (admin, user, guest?)
  3. Session duration? (remember me?)
  4. Login errors: hiển thị thế nào?
  5. Security requirements? (rate limiting, brute force protection?)"
```

### Output

Design document đã được human approve. Agent không proceed cho đến khi human đồng ý.

---

## 🧩 Chi Tiết: test-driven-development

### Vấn đề

Viết code → viết test → test pass → commit → production fail vì case chưa test.

### Giải pháp

**BẮT BUỘC RED-GREEN-REFACTOR:**

```
1. RED    → Viết test fail trước (test mới feature)
2. GREEN  → Viết MINIMAL code để test pass
3. REFACTOR → Cải thiện code mà test vẫn pass
4. COMMIT → Sau mỗi cycle
```

> ⚠️ **Agent không được viết code trước test.**

---

## 📊 So Sánh: Superpowers vs oh-my-openagent

| Khía cạnh | **Superpowers** | **oh-my-openagent** |
|-----------|-----------------|-------------------|
| **Focus** | Workflow methodology | Agent orchestration |
| **Agents** | 1 agent (workflows) | Multi-agent (5+ chạy song song) |
| **Trigger** | Automatic per task | Manual via commands |
| **TDD** | ✅ Enforced | ❌ Không có |
| **Model routing** | Manual | ✅ Auto fallback |
| **Stars** | 162k | 52.9k |

> 💡 **Có thể dùng cả hai** — oh-my-openagent cho parallel execution, superpowers cho structured workflow.

---

## ✅ Khi Nào Dùng Superpowers

| Situation | Recommendation |
|-----------|-----------------|
| New feature | ✅ Superpowers workflow |
| Bug fix | ✅ systematic-debugging + verification |
| Complex task (>1h) | ✅ superpowers + oh-my-openagent ulw |
| Quick hotfix | ❌ Too heavy — dùng trực tiếp |
| Research/exploration | ❌ Too heavy — open interaction |

---

## 📚 Tham Khảo Thêm

| Resource | Link |
|----------|------|
| **Trang chủ Superpowers** | [ECC Superpowers](https://github.com/eclabcode/superpowers) |
| **Marketplace** | [superpowers-marketplace](https://github.com/obra/superpowers-marketplace) |

---

## ⚠️ Limitation

| Limitation | Chi tiết |
|------------|----------|
| **Overhead cho task nhỏ** | Not worth cho quick fixes |
| **Learning curve** | 7 workflows mới — cần thời gian adopt |
| **Platform-specific** | Một số skills hoạt động khác nhau giữa các coding agents |

---

## 🔗 Liên Quan

| Bài | Nội dung |
|-----|----------|
| [SETUP/01](./01-chon-opencode.md) | oh-my-openagent — plugin ecosystem cho OpenCode |
| [ECOSYSTEM/02](../ECOSYSTEM/02-so-sanh-agent-tools.md) | So sánh Agent Tools — chi tiết hơn |