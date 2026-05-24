<think>The user wants me to prioritize three roadmap candidates using PM frameworks and structured analysis. Let me apply the right frameworks to make a clear recommendation.

Candidates:
- A: Guided import wizard (addresses SMB admin onboarding pain)
- B: AI report writer (requested by sales team)
- C: New dashboard theme (low engineering effort)

I should use multiple frameworks:
1. RICE scoring for prioritization
2. MoSCoW for categorization
3. Consider impact vs effort
4. Consider strategic alignment

Let me structure this properly with assumptions, metrics, and a clear recommendation.
</think>

# Product Prioritization Recommendation

## Assumptions

| Assumption | Basis |
|------------|-------|
| SMB admins = primary user segment | Stated in context |
| Onboarding time is top friction point | Explicit complaint data |
| Sales team influence on roadmap is high | Request origin noted |
| Engineering capacity is limited | Implied by "low effort" framing |
| Dashboard theme has no revenue impact | Not mentioned as business goal |

---

## Framework 1: RICE Scoring

| Candidate | Reach | Impact | Confidence | Effort | **RICE Score** |
|-----------|-------|--------|------------|--------|----------------|
| **A: Import Wizard** | High (all new SMBs) | 3 (high) | 80% | Medium | **~144** |
| **B: AI Report Writer** | Medium (sales team) | 2 (medium) | 60% | High | **~48** |
| **C: Dashboard Theme** | Low (existing users) | 1 (low) | 90% | Low | **~30** |

---

## Framework 2: MoSCoW Classification

| Priority | Candidate | Rationale |
|----------|-----------|-----------|
| **Must Have** | A | Directly addresses #1 user complaint |
| **Should Have** | B | Revenue-adjacent (sales productivity) |
| **Could Have** | C | Nice-to-have, low strategic value |
| **Won't Have** | — | None excluded |

---

## Framework 3: Impact × Confidence / Effort Matrix

```
                    IMPACT
                      ↑
                      │    [B] AI Writer
                      │
                      │              [A] Import Wizard
              Medium  │
                      │
                      │    [C] Theme
                      │
                      └──────────────────────→ EFFORT
                      Low          Medium         High
```

---

## Recommendation

### 🥇 Priority 1: Candidate A — Guided Import Wizard

**Why:**
- Targets the highest-severity user pain (onboarding time)
- Affects all new customers → highest reach
- Directly supports retention and time-to-value metrics

**Key Metrics to Track:**
| Metric | Formula | Target |
|--------|---------|--------|
| Time to First Value (TTFV) | Days from signup to first meaningful action | Reduce by 40% |
| Onboarding Completion Rate | % users completing setup | > 85% |
| Support Tickets per Onboarding | Tickets / new customer | Reduce 30% |

---

### 🥈 Priority 2: Candidate B — AI Report Writer

**Why:**
- Addresses internal stakeholder request (sales)
- Potential for expansion into upsell/cross-sell use cases
- Medium effort, medium return

**Key Metrics to Track:**
| Metric | Formula | Target |
|--------|---------|--------|
| Feature Adoption Rate | Monthly active users of feature | > 25% |
| Sales Team NPS Contribution | NPS change attributable to feature | +5 points |

---

### 🥉 Priority 3: Candidate C — Dashboard Theme

**Why:**
- Low effort enables fast win
- Low strategic priority — defer until capacity allows
- Consider as engineering morale/quick wins project

---

## Summary Decision

| Rank | Candidate | RICE | MoSCoW | Go/No-Go |
|------|-----------|------|--------|----------|
| 1 | A: Import Wizard | 144 | Must Have | ✅ **Build** |
| 2 | B: AI Report Writer | 48 | Should Have | ✅ **Build** (Q2) |
| 3 | C: Dashboard Theme | 30 | Could Have | ⏳ **Defer** |

---

**Next Step:** Validate onboarding friction data with 5–10 SMB admin interviews before committing engineering resources to Candidate A.
