# Roadmap Prioritization Recommendation

## 1. Context & Assumptions
`[Uncertainty]` Exact baseline metrics, engineering capacity, and active user volume are not provided. The following analysis uses `[Assumption]` SMB SaaS benchmarks and should be validated against your internal analytics before commitment.

- **Strategic North Star:** Reduce Time-to-Value (TTV) and improve Activation Rate for SMB admins.
- **Current Pain Point:** Onboarding friction is driving early-stage drop-off and support ticket volume.
- **Capacity Assumption:** 1 engineering pod (~3 devs, 1 designer) available for the next 2 quarters.

## 2. Prioritization Analysis (RICE Framework)
**Formula:** `RICE Score = (Reach × Impact × Confidence) / Effort`

| Candidate | Reach (Q1 Users) | Impact (0.25–3) | Confidence (%) | Effort (Person-Mo) | RICE Score |
|:---|:---:|:---:|:---:|:---:|:---:|
| **A: Guided Import Wizard** | 400 `[Assumption]` | 3.0 (Massive) | 80% | 2.0 | **480** |
| **B: AI Report Writer** | 150 `[Assumption]` | 2.0 (High) | 60% | 4.0 | **45** |
| **C: Dashboard Theme** | 800 `[Assumption]` | 0.25 (Minimal) | 90% | 0.5 | **360** |

**MoSCoW Mapping:**
- **Must Have:** Candidate A (directly resolves stated user complaint & strategic North Star)
- **Should Have:** Candidate C (low-effort UX polish, improves perceived quality)
- **Could Have:** Candidate B (sales-requested, requires validation before build)
- **Won't Have (Now):** None

## 3. Metric Projections & SaaS KPIs
The following metrics will track success. Formulas are applied to projected baselines.

| Metric | Formula | Projected Impact (Post-A) |
|:---|:---|:---|
| **Activation Rate** | `(Users completing onboarding / Total new sign-ups) × 100` | `+12–18%` (reduces setup confusion) |
| **Time-to-Value (TTV)** | `Σ(Days from signup to first core action) / Total activated users` | `-25%` (guided flow accelerates first value) |
| **Early Churn Rate (0–30d)** | `(Customers lost in first 30d / Customers at start of period) × 100` | `-5–8%` (friction removal improves retention) |
| **Support Ticket Volume** | `Total onboarding-related tickets / Active users` | `-30%` (self-serve wizard deflects L1/L2 queries) |
| **Net Revenue Retention (NRR)** | `((Starting MRR + Expansion MRR - Contraction MRR - Churn MRR) / Starting MRR) × 100` | `+2–4%` (indirect lift via improved activation & reduced churn) |

*Note: Candidate B's primary metric would be Expansion MRR or Feature Adoption Rate, but confidence is too low to project accurately without discovery. Candidate C impacts NPS/CSAT but shows negligible movement on core SaaS retention or revenue metrics.*

## 4. Recommendation & Phased Execution
**Priority Order:** `A → C → B`

1. **P0: Candidate A (Guided Import Wizard)**
   - **Why:** Highest strategic alignment, strongest RICE score, directly addresses the documented SMB admin complaint.
   - **Execution:** Build MVP with step-by-step validation, error handling, and progress tracking. Gate launch on Activation Rate ≥ 70%.

2. **P1: Candidate C (Dashboard Theme)**
   - **Why:** High confidence, minimal effort, quick win. Can be bundled into the same release cycle as A to improve perceived product quality without blocking core value.
   - **Execution:** Implement as a toggleable theme. Measure via CSAT/NPS delta.

3. **P2: Candidate B (AI Report Writer)**
   - **Why:** Sales-requested but unvalidated by end-users. High effort, low confidence. Risk of building unused AI features.
   - **Execution:** Move to Discovery. Run 5–7 SMB admin interviews, prototype a no-code mock, and measure intent-to-use before committing engineering.

## 5. Next Steps & Validation
1. **Instrument Tracking:** Ensure event tracking is in place for `onboarding_step_completed`, `import_success`, and `first_report_generated`.
2. **Define Success Criteria:** Set explicit thresholds (e.g., `Activation Rate ≥ 75%`, `TTV ≤ 2 days`) before sprint kickoff.
3. **Stakeholder Alignment:** Share this RICE breakdown with Sales (for B) and Engineering (for A/C effort validation). Adjust `[Assumption]` values with actual data.
4. **Sprint Planning:** Slot A into the next 2 sprints. Slot C into sprint 2. Park B in the discovery backlog.
