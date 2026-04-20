# So Sánh Models Cho AI Agent

> Quá nhiều models: Claude 4.5/4.6, GPT-4o, o1, o3, Gemini 2.5... Không biết cái nào cho task nào, và khi nào upgrade lên model đắt hơn.

---

## 🔥 Thực Trạng

Bạn thấy có quá nhiều models:

- 🤖 Claude 4.5/4.6 Sonnet, Opus, Haiku...
- 🤖 GPT-4o, GPT-4o-mini, o1, o3, o3-mini...
- 🤖 Gemini 2.5 Flash, Pro, Ultra...
- 🤖 Llama 4, Qwen 3, DeepSeek...

→ Không biết cái nào cho task nào.

---

## 🎯 Mục Tiêu

Sau bài này, bạn sẽ:

- ✅ Hiểu 3 tier: Cao cấp, Trung bình, Nhanh
- ✅ Chọn model theo độ phức tạp task (không dựa vào benchmark)
- ✅ Áp dụng tối ưu chi phí (task routing, progressive context)

---

## 📊 3 Tiers Của Models

```
┌────────────────────────────────────────────────────────────┐
│                    BỨC TRANH MODELS (2026)                │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  🔴 TIER CAO CẤP                                           │
│     (Mạnh nhất, đắt nhất)                                  │
│     Claude Opus 4.6, GPT-o1/o3, Gemini 2.5 Ultra          │
│                                                             │
├────────────────────────────────────────────────────────────┤
│  🟡 TIER TRUNG BÌNH                                        │
│     (Cân bằng giữa khả năng và chi phí)                   │
│     Claude Sonnet 4.6, GPT-4o, Gemini 2.5 Pro              │
│                                                             │
├────────────────────────────────────────────────────────────┤
│  🟢 TIER NHANH / TIẾT KIỆM                                 │
│     (Nhanh, rẻ, cho tác vụ đơn giản)                       │
│     Claude Haiku 4, GPT-4o-mini, Gemini 2.5 Flash         │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## 💰 So Sánh Giá (Per 1M Tokens — Approximate)

| Tier | Model | Input | Output |
|------|-------|-------|--------|
| **Cao cấp** | Claude Opus 4.6 | $15-18 | $75 |
| **Cao cấp** | GPT-o3 | $15 | $60 |
| **Cao cấp** | GPT-o3-mini | $1.10 | — |
| **Trung bình** | Claude Sonnet 4.6 | $3 | $15 |
| **Trung bình** | GPT-4o | $2.50 | $10 |
| **Trung bình** | Gemini 2.5 Pro | $1.25 | $5 |
| **Nhanh** | Claude Haiku 4 | $0.25 | $1.25 |
| **Nhanh** | GPT-4o-mini | $0.15 | $0.60 |
| **Nhanh** | Gemini 2.5 Flash | $0.10 | $0.40 |

---

## 🤖 Claude Family (2026)

| Model | Context | Điểm mạnh | Phù hợp cho |
|-------|---------|-----------|-------------|
| **Opus 4.6** | 200K | Top-tier reasoning, best coding | Novel problems, critical tasks |
| **Sonnet 4.6** | 200K | Best balance coding/price | Complex coding, daily use |
| **Haiku 4** | 200K | Fast, cheap | Quick edits, simple refactors |

---

## 🤖 GPT Family (2026)

| Model | Context | Điểm mạnh | Phù hợp cho |
|-------|---------|-----------|-------------|
| **GPT-4o** | 128K | Balanced, good coding + creative | General purpose, mid-tier |
| **GPT-4o-mini** | 128K | Fast, cheap | Quick tasks, automation |
| **o3** | 128K | Best reasoning, chain-of-thought | Research, complex logic |
| **o3-mini** | 128K | Compact reasoning, faster | Reasoning với budget |

---

## 🤖 Gemini Family (2026)

| Model | Context | Điểm mạnh | Phù hợp cho |
|-------|---------|-----------|-------------|
| **Ultra** | 1M | Best context window, multimodal | Long documents, research |
| **Pro** | 1M | Long context, good reasoning | Document analysis, codebases |
| **Flash** | 1M | Fast, cheap, long context | Fast tasks, budget |

---

## 🤖 Open Source / Alternative (2026)

| Model | Context | Điểm mạnh | Phù hợp cho |
|-------|---------|-----------|-------------|
| **Llama 4 70B** | 128K | Self-hostable, no API cost | Cost-sensitive, privacy, local |
| **Qwen 3** | 128K | Good coding, multilingual | Non-English, cost-sensitive |
| **DeepSeek V3** | 128K | Strong coding, open source, cheap | Coding tasks, budget |

---

## 🎯 Chọn Model Theo Độ Phức Tạp

```
TASK ĐƠN GIẢN:
├── Quick edits, simple refactors, documentation
│
└──→ GPT-4o-mini hoặc Claude Haiku 4
    Chi phí: ~$0.01-0.05/task

────────────────────────────────────────────────────────────

TASK TRUNG BÌNH:
├── Feature development, bug fixes (known patterns)
├── Code reviews, test generation
│
└──→ GPT-4o hoặc Claude Sonnet 4.6
    Chi phí: ~$0.10-0.50/task

────────────────────────────────────────────────────────────

TASK PHỨC TẠP:
├── Novel architecture, complex debugging
├── Multi-file refactors, security reviews
│
└──→ Claude Opus 4.6 hoặc GPT-o1/o3
    Chi phí: ~$0.50-5.00/task

────────────────────────────────────────────────────────────

TASK NGHIÊN CỨU:
├── Exploring new patterns, design decisions
├── Performance optimization
│
└──→ GPT-o3 hoặc Claude Opus 4.6
    Chi phí: ~$1.00-10.00/task
```

---

## 💡 Chọn Model Theo Context Length

```
CONTEXT NGẮN (< 10K tokens):
→ Mọi model đều ổn
→ Chọn theo nhu cầu khả năng

CONTEXT TRUNG BÌNH (10K-50K tokens):
→ Claude 4.x family (200K context)
→ GPT-4o family (128K context)
→ Tránh Gemini 2.5 Pro nếu lo ngại chi phí

CONTEXT DÀI (50K+ tokens):
→ Claude 4.x (200K context) — tốt nhất cho coding
→ Gemini 2.5 family (1M context) — tốt nhất cho documents
→ GPT-4o (128K) — có thể cần chunking
```

---

## ⚠️ Best Practice: Context Window

```
❌ Đừng dùng 100% context window
✅ Dùng tối đa ~50-70%

Tại sao?
├── Model performance degrades near limit
├── Context overflow = truncation
└── Đếm token không hoàn hảo

→ Nếu gần giới hạn → chunk/summarize
```

---

## 💰 Tối Ưu Chi Phí

### Chiến lược 1: Định Tuyến Theo Task

```
Simple tasks → Claude Haiku 4 / GPT-4o-mini (nhanh, rẻ)
Medium tasks → Claude Sonnet 4.6 / GPT-4o (cân bằng)
Complex tasks → Claude Opus 4.6 (chỉ khi cần)
```

### Chiến lược 2: Progressive Disclosure

```
❌ SAI: Đổ tất cả vào context một lần
✅ ĐÚNG: Progressive disclosure

Vòng 1: Tổng quan task (cần làm gì)
Vòng 2: Các file liên quan (chunk 1)
Vòng 3: Thêm context (chỉ khi cần)
Vòng 4: Output cuối cùng

→ Tiết kiệm tokens, cải thiện focus
```

### Chiến lược 3: Caching

```
Nhiều provider cache repeated context:
✓ Đọc file lặp lại → rẻ
✓ Prompt giống nhau lặp lại → không tính phí
→ Tái sử dụng context khi có thể
```

---

## 👥 Recommendations

### Cho Cá nhân

| Tình huống | Model | Lý do |
|-----------|-------|-------|
| Coding hàng ngày | Claude Sonnet 4.6 | Best coding balance |
| Ngân sách hạn chế | GPT-4o hoặc GPT-4o-mini | Rẻ, đủ khả năng |
| Tài liệu dài | Gemini 2.5 Flash | 1M context, rẻ |
| Quick edits, volume | Claude Haiku 4 | Fewer tokens vs Cursor |
| Critical tasks | Claude Opus 4.6 | Top-tier reasoning |

### Cho Teams

| Tình huống | Model | Lý do |
|-----------|-------|-------|
| Tiết kiệm chi phí | GPT-4o-mini + Sonnet | Tối ưu ngân sách |
| Chất lượng là ưu tiên | Claude Sonnet 4.6 | Khả năng coding tốt nhất |
| Enterprise reasoning | Claude Opus 4.6 hoặc GPT-o3 | Top-tier reasoning |
| Mixed workloads | OpenCode + flexible routing | Định tuyến theo task |

---

## 📋 Checkpoint

Kiểm tra lại kiến thức:

- [ ] Hiểu các tier: Cao cấp (Opus 4.6/o3), Trung bình (Sonnet 4.6/GPT-4o), Nhanh (Haiku 4/GPT-4o-mini)
- [ ] Biết giá gần đúng: Haiku $0.25/M vs Opus 4.6 $15-18/M
- [ ] Chọn model theo độ phức tạp của task
- [ ] Áp dụng tối ưu chi phí (task routing, progressive context)
- [ ] KHÔNG dùng Opus cho task đơn giản (lãng phí tiền)

---

## 🔗 Liên Quan

- **So sánh tools:** [02: So Sánh Agent Tools](./02-so-sanh-agent-tools.md)
- **Decision tree:** [04: Decision Tree](./04-decision-tree.md)