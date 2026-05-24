## Prioritization Recommendation

### Context
SMB admins report excessive onboarding time. The product goal is to reduce time-to-value for new users. Three roadmap candidates are under consideration:

- **Candidate A: Guided import wizard** – reduces setup confusion.
- **Candidate B: AI report writer** – a feature requested by sales.
- **Candidate C: New dashboard theme** – low engineering effort.

### Assumptions
- The product is a SaaS analytics/dashboard tool for SMBs (teams averaging 5 users).
- Primary metric: **time-to-first-value** (onboarding completion time). Secondary metrics: activation rate, support tickets, NPS.
- Current state: manual data import causes friction, leading to drop-offs and support load.
- Approximate user reach (per quarter):  
  - New sign‑ups: 500 companies (~2,500 new users) – directly impacted by onboarding improvements.  
  - Existing active users: 5,000 (all would see a new theme).  
  - Sales/account teams requesting AI reports: ~200 users.
- Engineering effort estimates: A – 2 person‑months; B – 4 person‑months; C – 0.5 person‑months.

### Prioritization Approach
I apply two complementary frameworks: **RICE scoring** for a quantitative, impact‑over‑effort comparison, and **MoSCoW** to validate strategic alignment against the core onboarding problem.

#### 1. RICE Scoring
Scale: Reach (users/quarter), Impact (0‑3 on target metric), Confidence (%), Effort (person‑months).  
Key metric: reduction in onboarding time.

| Candidate | Reach | Impact | Confidence | Effort | RICE Score = (R×I×C) / E |
|-----------|-------|--------|------------|--------|---------------------------|
| A – Guided import wizard | 2,500 (new users) | 3 (directly cuts setup time) | 80% (strong user complaint signal) | 2 | (2,500×3×0.80)/2 = **3,000** |
| B – AI report writer | 200 (sales users) | 1 (no proven effect on onboarding) | 50% (sales request, unvalidated with end users) | 4 | (200×1×0.50)/4 = **25** |
| C – New dashboard theme | 5,000 (all users) | 0.5 (cosmetic; negligible impact on onboarding time) | 50% (aesthetic preference; no link to onboarding pain) | 0.5 | (5,000×0.5×0.50)/0.5 = **2,500** |

> **Interpretation:**  
> - **A** scores highest because it uniquely addresses the measured problem with high confidence and substantial reach among affected users.  
> - **C** looks attractive due to low effort and broad reach, but its near‑zero impact on the core metric makes it a distraction from the stated pain point.  
> - **B** has minimal linkage to onboarding and low reach, making it the weakest candidate.

#### 2. MoSCoW Categorisation
- **Must have** – *Guided import wizard*: directly solves the top complaint, reduces onboarding time, and improves activation (strategic necessity).
- **Could have** – *AI report writer*: might later support expansion revenue, but does not address the current bottleneck. Needs separate discovery.
- **Won’t have (this cycle)** – *New dashboard theme*: a “lipstick on a pig” change; risks investing in polish while the core experience remains broken. Could be considered as a fast‑follow only after onboarding metrics improve.

### Recommendation
**Prioritise Candidate A (Guided import wizard) for the next development cycle.**  
This choice has the strongest strategic alignment, the highest RICE score when measured against the actual problem, and clear user‑backed confidence. It will deliver tangible improvement in onboarding time, reduce support costs, and increase trial‑to‑paid conversion.

Once the import wizard ships and validates the expected impact, a lightweight version of **Candidate C** could be added as a “quick win” to improve perceived product quality – but only if resources permit and it does not delay the core fix. **Candidate B** should be treated as a separate opportunity, queued after proper discovery (user research, competitive analysis, JTBD) to confirm whether it addresses a widespread need beyond a single sales request.

### Key Metrics to Track Post‑Launch
- **Onboarding time** (time‑to‑first‑value): target ≥30% reduction for new users who use the wizard.
- **Activation rate** (% of new sign‑ups completing key setup action within 7 days).
- **Support tickets** related to data import: expected drop of ≥40%.
- **NPS** from new SMB admins after week‑1 survey.
- **Funnel conversion** (trial → paid) for cohorts that used the guided flow vs. those that did not.

### Limitations & Next Steps
- The absence of direct user research limits confidence levels; quick prototype testing of the import wizard would refine impact estimates.
- The sales‑requested AI report writer requires a separate discovery sprint to define the problem, user personas, and success criteria.
- The dashboard theme, while light, should still be validated through usability testing to ensure it doesn’t introduce new friction.

*This recommendation follows standard Product Manager frameworks and the provided constraints. All assumptions are explicitly stated; missing information (e.g., exact user research data) is acknowledged.*
