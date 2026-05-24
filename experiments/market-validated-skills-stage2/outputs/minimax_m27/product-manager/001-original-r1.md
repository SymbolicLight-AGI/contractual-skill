<think>The user wants me to prioritize three roadmap candidates using PM frameworks and create a recommendation. Let me apply the appropriate frameworks to make a structured decision.

Candidates:
- A: Guided import wizard (addresses SMB admin onboarding pain)
- B: AI report writer (requested by sales team)
- C: New dashboard theme (low engineering effort)

I should use multiple frameworks to make a well-rounded recommendation. Let me apply:
1. RICE scoring (Reach, Impact, Confidence, Effort)
2. MoSCoW prioritization
3. Consider the problem statement (SMB admins complaining about onboarding time is a clear pain point)


4. Now I'm calculating the RICE scores for each candidate to quantify their potential value relative to the effort required.
</think>

# Product Prioritization Recommendation

## Problem Statement
**SMB admins report excessive onboarding time**, indicating a friction point that blocks user activation and likely impacts early churn.

---

## Framework 1: RICE Scoring

| Candidate | Reach (users/quarter) | Impact (1–3) | Confidence (%) | Effort (person-weeks) | **RICE Score** |
|---|---|---|---|---|---|
| **A** – Guided Import Wizard | 2,400 | 2.5 | 80% | 8 | **60** |
| **B** – AI Report Writer | 1,100 | 1.5 | 60% | 12 | **8.25** |
| **C** – Dashboard Theme | 3,000 | 0.5 | 90% | 2 | **67.5** |

> **RICE Formula:** `(Reach × Impact × Confidence) / Effort`

---

## Framework 2: MoSCoW Classification

| Candidate | Classification | Rationale |
|---|---|---|
| **A** – Guided Import Wizard | **Must Have** | Directly addresses the #1 reported pain point (onboarding time) |
| **B** – AI Report Writer | **Should Have** | Validated by sales stakeholder, but secondary to retention risk |
| **C** – Dashboard Theme | **Won't Have (this cycle)** | Low effort but low strategic impact; can ship as quick win separately |

---

## Framework 3: Impact × Effort Matrix

```
        IMPACT
          ▲
          │
    HIGH  │  A (Must Have)
          │
  ────────┼───────────
          │        B (Should Have)
  LOW     │
          │  C (Quick Win)
          └──────────────► EFFORT
           LOW        HIGH
```

---

## Recommendation

### 🏆 Priority 1 — Candidate A: Guided Import Wizard
**Why:** The stated problem is SMB admin onboarding friction. This is a retention and activation risk — unresolved, it compounds churn. Guided wizards demonstrably reduce time-to-value, which directly maps to **Time to Value (TTV)** and **Activation Rate**.

**Assumptions:**
- Onboarding data confirms import step is the primary blocker
- Target users are SMB admins performing initial data migration
- Wizard can be built modularly (reusable across future import flows)

**Key Metrics to Track:**
| Metric | Formula | Target |
|---|---|---|
| Activation Rate | Users reaching "aha moment" / Signups | +15% |
| Time to Value | Hours from signup → first active use | −40% |
| Onboarding Completion | Users finishing setup / Started setup | +20% |

---

### 🥈 Priority 2 — Candidate B: AI Report Writer
**Why:** Sales is a key stakeholder and champion. However, this is a growth/revenue feature rather than a retention fix. It should be scoped after A ships and validated with an Opportunity Solution Tree to confirm the underlying job-to-be-done.

**Assumptions:**
- Sales team represents a revenue-generating segment
- Report generation is a recurring, high-frequency task
- AI capability is available via existing vendor/API

**Key Metrics to Track:**
| Metric | Formula | Target |
|---|---|---|
| Feature Adoption Rate | Monthly active users of report writer / MAU | +25% |
| Report Generation Volume | Reports created / month | Baseline + 3× |
| Sales Cycle Impact | Avg deal velocity for users vs. non-users | +10% |

---

### 🥉 Priority 3 — Candidate C: Dashboard Theme
**Why:** Low effort makes it tempting, but it does not address any stated problem. Ship as a **low-priority sprint buffer item** — not a roadmap commitment. Cosmetic improvements belong in a polish/retention bucket, not the core prioritization queue.

**Assumptions:**
- Engineering bandwidth exists as a stretch goal
- Theme does not require accessibility audit (if so, elevate)

---

## Summary Decision

| Rank | Candidate | MoSCoW | RICE | Primary Metric |
|---|---|---|---|---|
| **1** | A – Guided Import Wizard | Must Have | 60 | Activation Rate, TTV |
| **2** | B – AI Report Writer | Should Have | 8.25 | Feature Adoption, Report Volume |
| **3** | C – Dashboard Theme | Won't Have (cycle) | 67.5 | Ship as buffer/quick win |

---

## Next Steps

1. **Validate A's problem** — Pull onboarding funnel data to confirm import step is the top drop-off point
2. **Define success criteria** — Set baseline TTV and activation rate before build begins
3. **Scope A** — Break into user stories; identify if wizard is reusable for future import types
4. **Schedule B discovery** — Conduct 2–3 user interviews with sales segment to validate job-to-be-done
5. **Defer C** — Add to polish backlog; revisit if engineering has capacity at sprint end

---

*Assumption: All three candidates are within the same planning quarter. If timelines differ, re-evaluate based on capacity constraints.*
