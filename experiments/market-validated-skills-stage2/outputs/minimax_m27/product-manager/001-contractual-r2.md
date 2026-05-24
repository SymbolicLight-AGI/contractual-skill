# Roadmap Prioritization Recommendation

---

## 1. Goal and User

**Primary Goal:** Reduce time-to-value for SMB admins during product onboarding.

**Target User:** SMB administrators responsible for initial product setup and configuration.

**Secondary Consideration:** Sales team has requested AI-powered reporting to improve customer-facing value; this suggests a different user (sales reps or end customers) and outcome (reporting quality, not onboarding speed).

---

## 2. Known Facts

| Fact | Source |
|------|--------|
| SMB admins report onboarding takes too long | Task description (synthetic context) |
| "Setup confusion" is the stated pain point | Task description |
| Sales team has requested an AI report writer feature | Task description |
| Dashboard theme change requires low engineering effort | Task description |
| No quantitative data on current onboarding duration, drop-off rates, or setup abandonment | Not supplied |

---

## 3. Assumptions and Unknowns

### Candidate A: Guided Import Wizard
| Type | Item |
|------|------|
| **Assumption** | Setup confusion stems from data import, not other onboarding steps |
| **Assumption** | Guided wizard will reduce support tickets or time-to-first-value |
| **Unknown** | What percentage of SMB admins import data vs. start fresh? |
| **Unknown** | What is the root cause of confusion—UI, documentation, or process complexity? |
| **Unknown** | Engineering effort and timeline |

### Candidate B: AI Report Writer
| Type | Item |
|------|------|
| **Assumption** | Sales requested this based on customer feedback or competitive need |
| **Assumption** | Report writer addresses a revenue or retention goal |
| **Unknown** | Which users will consume AI-generated reports? |
| **Unknown** | Whether this solves a pain admins experience |
| **Unknown** | Technical feasibility and LLM integration cost |

### Candidate C: New Dashboard Theme
| Type | Item |
|------|------|
| **Assumption** | Low effort enables faster delivery |
| **Assumption** | Theme refresh addresses a known user preference or competitive parity |
| **Assumption** | Admin satisfaction is part of the onboarding experience |
| **Unknown** | Whether theme is a pain point or nice-to-have |
| **Unknown** | Who requested or prioritized this (internal only?) |

---

## 4. Recommendation or Options

### Recommended Priority Order

| Rank | Candidate | Rationale |
|------|-----------|-----------|
| **1** | **A – Guided Import Wizard** | Directly targets stated pain (onboarding time for SMB admins). If the pain is validated, this is the highest-leverage investment. |
| **2** | **B – AI Report Writer** | Addresses a different user (sales/customers) and different outcome. Valuable if linked to a business goal, but does not address the primary onboarding problem. |
| **3** | **C – Dashboard Theme** | Low effort is attractive but does not solve a stated pain. Recommend only if it unblocks team capacity or addresses a known user preference. |

### Option: Validate Before Committing

If evidence for SMB admin pain is anecdotal:
- Conduct 5–10 admin interviews to confirm root cause
- Instrument onboarding funnel to capture drop-off steps
- Then decide whether A, B, or C best addresses validated pain

---

## 5. Metrics and Validation

| Candidate | Success Metric | Validation Method |
|-----------|----------------|-------------------|
| **A – Import Wizard** | • Time from signup to first active use <br> • % of admins completing data import without support ticket <br> • Setup-related support ticket volume | Pre/post A/B or cohort comparison; support ticket tracking |
| **B – AI Report Writer** | • Report generation rate <br> • Report sharing or export frequency <br> • Customer-reported satisfaction with reports | Usage analytics; NPS or survey for report users |
| **C – Dashboard Theme** | • Admin NPS or theme satisfaction score <br> • Theme adoption rate (if opt-in) | In-app survey; adoption tracking |

**Missing baseline metrics:** Current onboarding duration, setup completion rate, and support ticket baseline are needed to measure improvement for Candidate A.

---

## 6. Risks and Human Gates

| Risk | Mitigation | Gate |
|------|------------|------|
| A assumes import is the onboarding bottleneck | Validate with admins before building | Requires user research before committing engineering scope |
| B may be a sales request without customer-validated demand | Confirm if request reflects customer need or internal preference | Requires sales to provide evidence of customer demand |
| C delivers low value if not tied to user or business goal | Confirm whether theme refresh addresses competitive gap or user preference | Engineering should not start without product sign-off on priority |
| Prioritizing A without data wastes engineering effort | Instrument onboarding first | **Human gate:** Do not begin development without baseline metrics or validation |

---

## 7. Next Steps

| Step | Owner | Condition |
|------|-------|-----------|
| 1. Instrument onboarding flow to capture drop-off steps and duration | Data / Product | Needed before building anything |
| 2. Interview 5–10 SMB admins to confirm root cause of onboarding time | Product / Customer Success | Needed to validate Candidate A |
| 3. Ask sales for evidence that AI report writer reflects customer demand, not internal preference | Sales / Product | Needed to justify Candidate B investment |
| 4. Clarify who requested dashboard theme and why | Product | Needed to decide if Candidate C warrants any attention |
| 5. Revisit prioritization with evidence from steps 1–4 | Product | Output: final ranked roadmap recommendation |

---

## Summary for Product Owner

Candidate A has the strongest alignment to the stated pain, but the pain is only anecdotal. Candidate B serves a different user and goal. Candidate C is low-effort but unvalidated.

**Do not commit engineering to any candidate until:** (1) onboarding data is instrumented, (2) admin interviews confirm the root cause, and (3) evidence exists for B and C.
