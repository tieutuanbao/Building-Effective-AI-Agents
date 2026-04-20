# Research & Tìm Kiếm Thông Tin

## 🔥 Thực Trạng

Agent trả lời rất confident nhưng sai. Không phải "không biết" mà là "nói sai như đúng". Bạn hỏi về API của thư viện, agent trả version number, method signature, release date như thể đang đọc official docs. Kết quả: bạn implement theo thông tin sai, mất 2 tiếng debug, và cuối cùng phát hiện agent hallucinate. Google search sai còn có snippet link để kiểm tra. Agent sai thì silent — không có nguồn, không có trace, không có cách verify nhanh.

Đây là failure mode nguy hiểm nhất của research task. Google sai thì bạn biết đang đọc docs của ai. Agent confident nhưng sai thì bạn trust hoàn toàn, rồi burn.

## 🎯 Mục Tiêu

- Viết prompt research có scope rõ ràng, không ambiguous
- Triangulate thông tin từ nhiều nguồn để grounding facts
- Chọn đúng MCP tool (Context7 vs WebSearch vs Exa) cho từng loại câu hỏi
- Nhận dạng hallucination và recover bằng fact-checking protocol
- Quản lý token budget khi research loop dài

## 🧩 Best Practices

### Core Workflow

```
Question Framing → Multi-source → Fact Grounding → Synthesis
```

**Question Framing**: Đặt câu hỏi có boundary — scope, use case, constraints, format mong đợi. Không có framing thì agent fill in gaps bằng assumption → hallucination.

**Multi-source**: Không dùng single source. Cross-reference ít nhất 2 nguồn độc lập. Nếu 2 nguồn conflict, keep both và flag uncertainty.

**Fact Grounding**: Mỗi claim cần có source reference. Nếu agent không cite được nguồn, flag là unverified.

**Synthesis**: Tổng hợp bằng structure — pros/cons, comparison table, recommendation với confidence level.

### Agent Role

```
LÀ: research assistant với MCP tools
KHÔNG PHẢI: encyclopedia (biết hết mọi thứ)
```

Agent biết cách tìm, không biết hết mọi thứ. Prompt phải reflect cái này.

### Before/After

**❌ BAD — ambiguous question:**
```
GraphQL có tốt hơn REST không?
```

Agent trả lời general, confident, không có context. "GraphQL tốt hơn vì flexibility, less over-fetching" — nghe đúng nhưng useless cho decision making thực tế.

**✅ GOOD — framed question:**
```
So sánh GraphQL vs REST cho:
- E-commerce API, 50 endpoints
- Team 4 devs quen REST, chưa dùng GraphQL
- Migration budget: 2 sprints
Focus: migration cost, performance N+1, tooling maturity
Cite sources. Nếu không chắc, nói rõ uncertainty level.
```

Agent có context để answerable, có constraints để scope, có format để synthesis.

### Khi nào KHÔNG dùng pattern

- Quick fact lookup mà bạn có thể Google trong 10s (ví dụ: "Python version hiện tại là gì")
- Niche historical knowledge mà không có digital source (agent sẽ hallucinate date)
- Subjective opinion aggregation (Reddit threads, community debates — dùng Exa nhưng expectation khác)

## 🛠️ Ví Dụ Thực Tế

### Scenario 1: Research thư viện mới cho project

**Prompt:**
```
Tôi cần chọn state management library cho React app mới:
- 50+ components, moderate complexity
- Team 3 devs, TypeScript intermediate
- Performance critical: 60fps interactions
- Không dùng Redux trước đó

Research: so sánh Zustand vs Jotai vs Valtio
Mỗi cái: bundle size, learning curve, TypeScript support, maintenance status
Dùng Context7 để check official docs cho syntax examples
Output: comparison table + recommendation với confidence score
Nếu claim gì về version hay release date, cite source.
```

**✅ What happens**: Agent dùng Context7 check docs thực, trả về accurate comparison với source links.

**⚠️ Watch for**: Agent extrapolate từ old docs. Check release date của docs context7 trả về.

---

### Scenario 2: Fact-check technical claim

**Prompt:**
```
Claim: "FastAPI throughput cao hơn 3x so với Flask"

Kiểm tra claim này:
1. Tìm source gốc của benchmark
2. Tìm independent benchmark cùng test conditions
3. Nếu không tìm được source, note là "unverified"

Dùng WebSearch cho benchmark articles, Exa cho academic papers.
Output format:
- Verified: [source]
- Unverified: [reason]
- Conflicting: [sources]
```

**✅ What happens**: Nếu claim không có source hoặc benchmark không independent, agent flag là unverified thay vì confirm.

**⚠️ Watch for**: Agent tìm được 1 benchmark và present nó như universal truth. Recovery: "Benchmark này test conditions là gì? Có independent reproduction không?"

---

## 🚧 Pitfalls & Recovery

**1. Hallucination facts/dates/APIs**
Dấu hiệu: Agent trả version number, release date, method signature với format cố định như "from version 3.2.1", "deprecated since 2022", "method signature: `query(selector, options)`".
Recovery: "Source nào? Check official docs bằng Context7."
Protocol: Yêu cầu agent cite source link sau mỗi factual claim.

**2. Confident về thứ không biết (no uncertainty signal)**
Dấu hiệu: Agent trả lời bằng câu chắc nịch — "Definitely", "Always", "The correct approach is" — cho topic niche hoặc recent changes.
Recovery: "Bạn có chắc không? Tỷ lệ confident là bao nhiêu? Nếu dưới 80%, note uncertainty."
Protocol: Khi prompt, include phrase: "Nếu không chắc, nói rõ uncertainty."

**3. Context ngập khi research results pile up**
Dấu hiệu: Bạn thấy agent đã đọc 10+ sources nhưng bắt đầu contradict itself ở responses gần đây.
Recovery: Dừng research, summarize findings trước khi continue.
Protocol: Sau mỗi 3 findings, pause và synthesize. "Tổng hợp những gì tìm được: [list]. Tiếp tục hay dừng?"

**Cost awareness**: Research loops không set scope sẽ burn token nhanh. Mỗi MCP call = $$. Đặt "research budget" trong prompt: "Tối đa 3 sources cho quick check, 10 sources cho deep research." Đây là cách giảm token mà không mất quality.

## ✅ Checkpoint

### Pattern Cheat Sheet

```
Question Framing:
  - Scope (use case, constraints)
  - Format (table, list, essay)
  - Uncertainty flag ("nếu không chắc, nói rõ")

Multi-source Triangulation:
  - ≥2 independent sources
  - Conflict = keep both + flag

Fact Grounding:
  - Mỗi claim = source link
  - No source = unverified

Synthesis:
  - Confidence score per recommendation
  - Limitation acknowledgment
```

### MCP Tool Decision Matrix

| Tool | Use khi | Không dùng khi |
|------|---------|----------------|
| **Context7** | Cần API reference cụ thể, library docs, syntax examples | Muốn opinion, comparison, general overview |
| **WebSearch** | Cần fresh info, tutorials, community discussions, current events | Cần academic sources, deep technical comparison |
| **Exa** | Cần deep research, academic papers, comprehensive search, company info | Quick fact lookup, single docs check |

Tool stack: Context7 → WebSearch → Exa (escalating scope và cost).

### Checklist

- [ ] Prompt có boundary rõ (scope, format, constraints)
- [ ] Yêu cầu cite source cho mỗi factual claim
- [ ] Include uncertainty flag ("nếu không chắc, nói rõ")
- [ ] Dùng đúng MCP tool cho query type
- [ ] Fact-check version number, dates, method signatures
- [ ] Pause sau mỗi 3 findings để synthesize
- [ ] Đặt token budget cho research loop

## 🔗 Liên Quan

- **PRACTICAL/02-quan-ly-context.md** — Quản lý context khi research nhiều sources, tránh context overflow
- **PRACTICAL/06-verification-habits.md** — Verification protocol cho factual claims, cách setup fact-checking loop