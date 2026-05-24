# Roadmap Prioritization Recommendation

## 📊 Assumptions & Data Gaps
`[Uncertainty]` Exact user volumes, engineering capacity, and baseline performance metrics are not provided. The following values are illustrative assumptions required to run the prioritization framework. Real-world sequencing must be validated against your product analytics and engineering capacity planning.

- **Assumed Baseline:** 1,000 MAU, ~150 new SMB signups/quarter, current onboarding completion rate: 65%, monthly gross churn: 4.5%.
- **Effort Scale:** Person-months of dedicated engineering + design time.
- **Impact Scale:** 0.25 (minimal) → 3 (massive), aligned to strategic North Star (reducing onboarding friction & improving early retention).

## 🧮 Framework Application: RICE Scoring
**Formula:** `(Reach × Impact × Confidence) / Effort`

| Candidate | Reach (users/qtr) | Impact (0.25–3) | Confidence | Effort (person-mos) | RICE Score |
|:---|:---:|:---:|:---:|:---:|:---:|
| **A: Guided Import Wizard** | 450 (new SMBs) | 3 (Massive) | 80% | 3 | **360** |
| **B: AI Report Writer** | 300 (active users) | 2 (High) | 60% | 4 | **90** |
| **C: Dashboard Theme** | 1,000 (all MAU) | 0.5 (Low) | 90% | 0.5 | **900** |

*Note on RICE Output:* Candidate C scores highest mathematically due to low effort and broad reach. However, RICE must be filtered through **Strategic Alignment**. Since the stated problem is SMB onboarding time, Candidate A receives a strategic override despite a lower raw score.

## 📈 SaaS Metrics & Projected Impact
| Candidate | Primary Metric Targeted | Secondary Metric Impact | Expected Direction |
|:---|:---|:---|:---|
| **A: Guided Import Wizard** | `Activation Rate` / `Time-to-Value (TTV)` | `Gross Churn Rate`, `Net Revenue Retention (NRR)` | ↑ Activation, ↓ Early Churn, ↑ NRR |
| **B: AI Report Writer** | `Feature Adoption Rate` | `Expansion MRR`, `CAC Payback Period` | ↑ Upsell potential, but ROI delayed until validation |
| **C: Dashboard Theme** | `CSAT / NPS` | `Daily Active Users (DAU)` | Marginal UX lift, negligible impact on retention or revenue |

## 🎯 Recommendation & Sequencing
1. **Priority 1: Candidate A (Guided Import Wizard)**  
   Directly addresses the core SMB onboarding complaint. Highest strategic ROI. Expected to reduce setup confusion, accelerate `Time-to-Value`, and improve early-stage retention.
2. **Priority 2: Candidate C (Dashboard Theme)**  
   Low-effort quick win. Can be executed in parallel with A or slotted into a maintenance sprint. Provides minor UX polish without diverting core resources.
3. **Priority 3: Candidate B (AI Report Writer)**  
   Defer to discovery phase. Sales-driven requests often lack validated user demand. Requires JTBD interviews, prototype testing, and clear success criteria before committing engineering cycles.

## 🛠 Next Steps & Validation
- **Instrument Baselines:** Track `Onboarding Completion Rate`, `Day-7 Retention`, and `Support Tickets/Setup` before and after A's launch.
- **Define Success Criteria for A:** Reduce average setup time by ≥30%, increase activation rate to ≥80%, decrease setup-related churn by ≥15%.
- **Run Discovery for B:** Apply an Opportunity Solution Tree + 5–7 SMB interviews to validate demand, map to `Expansion MRR` potential, and estimate realistic effort.
- **Boundary Note:** This prioritization operates within product strategy, discovery, and analytics domains. Final sequencing requires engineering capacity mapping, dependency resolution, and stakeholder sign-off. If technical constraints or compliance requirements alter effort estimates, re-run the RICE model with updated inputs.
