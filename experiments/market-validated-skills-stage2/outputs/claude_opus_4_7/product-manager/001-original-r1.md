# Product Prioritization Recommendation

## Context Summary
- **Problem signal**: SMB admins complain about onboarding time (validated pain point).
- **Candidates**: A) Guided import wizard, B) AI report writer, C) New dashboard theme.
- **Method**: RICE scoring + strategic alignment check.

> ⚠️ **Uncertainty flag**: No quantitative inputs were provided (user counts, conversion rates, effort estimates, revenue impact). Scores below use **stated assumptions** that should be validated with data before commitment.

---

## Stated Assumptions

| Variable | Assumption | Confidence |
|---|---|---|
| Active SMB admins onboarding/quarter | ~1,000 | Low — needs analytics pull |
| Current onboarding completion rate | ~60% | Low — needs funnel data |
| Sales team size requesting AI reports | ~20 reps representing customer asks | Low — "requested by sales" is unquantified |
| Engineering capacity per quarter | 1 squad (~3 engineers) | Stated as constraint |
| Strategic north star | Activation / time-to-value (inferred from problem statement) | Medium |

---

## RICE Scoring

**Formula**: `RICE = (Reach × Impact × Confidence) / Effort`
- Impact scale: 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
- Confidence: 0–100%
- Effort: person-months

| Candidate | Reach (per quarter) | Impact | Confidence | Effort (PM) | **RICE** |
|---|---|---|---|---|---|
| **A: Guided import wizard** | 1,000 admins | 2 (high — directly addresses validated complaint) | 80% | 3 | **533** |
| **B: AI report writer** | ~300 (sales-driven, end-user reach unclear) | 1 (medium — value unproven) | 40% | 6 | **20** |
| **C: Dashboard theme** | 1,000+ (all users) | 0.25 (cosmetic) | 70% | 0.5 | **350** |

---

## Strategic Alignment Check

| Lens | A: Wizard | B: AI Reports | C: Theme |
|---|---|---|---|
| Solves stated user problem | ✅ Direct | ❌ Different problem | ❌ Cosmetic |
| Evidence quality | ✅ User complaints | ⚠️ Single stakeholder (sales) | ⚠️ None cited |
| JTBD fit ("help me get set up fast") | ✅ Strong | ❌ Weak | ❌ Weak |
| Risk of building wrong thing | Low | High | Low |

---

## Recommendation

### 🥇 Priority 1: **Candidate A — Guided Import Wizard** (Build now)
- Highest RICE, directly tied to validated pain, advances activation north star.
- Reduces onboarding time → likely improves trial→paid conversion and reduces support load.

### 🥈 Priority 2: **Candidate C — Dashboard Theme** (Fast-follow / fill capacity)
- Low effort, broad reach, but low impact. Use as filler work or a morale/polish win; do **not** displace A.

### 🥉 Priority 3: **Candidate B — AI Report Writer** (Discovery first, do not build yet)
- Sales-requested ≠ customer-validated. Before committing 6 person-months:
  - Run 5–8 customer discovery interviews.
  - Quantify willingness to pay / retention lift.
  - Prototype with Wizard-of-Oz before full build.

---

## Success Metrics to Instrument

**For Candidate A (primary bet):**
| Metric | Formula | Target (hypothesis) |
|---|---|---|
| Time to First Value (TTFV) | Median minutes: signup → first import complete | -40% vs baseline |
| Onboarding completion rate | Completed setup / signups | +15 pp |
| Activation rate | Activated users / signups | +10 pp |
| Support tickets (onboarding tag) | Count / 100 new signups | -30% |
| 30-day retention | Active D30 / signups | +5 pp |

**Guardrail metrics (all candidates):**
- Weekly active SMB admins
- Net Revenue Retention (NRR) = (Starting MRR + Expansion − Churn − Contraction) / Starting MRR
- CSAT on onboarding flow

---

## Open Questions Before Commit
1. What is the actual onboarding funnel drop-off shape? (Determines if a wizard or a different step is the real bottleneck.)
2. Is "requested by sales" backed by deal loss data or churn signal?
3. Is there a strategic mandate (e.g., AI narrative for investors) that elevates Candidate B beyond user value?
4. What is the true effort estimate from engineering? RICE is sensitive to this.

**Next step**: Validate assumptions with product analytics + 5 SMB admin interviews, then re-score before sprint planning.
