# Product Prioritization Recommendation: SMB Onboarding Improvements

## Executive Recommendation

Prioritize **Candidate A: Guided Import Wizard** first.

SMB admins are explicitly complaining about onboarding time, so the strongest product bet is the one most directly tied to the stated customer pain. Candidate A is likely to improve activation, reduce time-to-value, lower support burden, and increase trial-to-paid or onboarding completion rates.

## Prioritized Roadmap

| Priority | Candidate | Recommendation |
|---:|---|---|
| 1 | **A: Guided Import Wizard** | Build first |
| 2 | **B: AI Report Writer** | Validate before committing |
| 3 | **C: New Dashboard Theme** | Defer unless bundled with other UI work |

---

# Assumptions

Because detailed customer, revenue, and engineering data is not provided, the scoring below uses explicit assumptions.

## Product Assumptions

1. The core customer problem is: **SMB admins take too long to onboard and experience setup confusion**.
2. Faster onboarding is a meaningful business lever for the product.
3. Setup/import is a major step in onboarding.
4. Sales-requested features may help pipeline, but Candidate B’s connection to onboarding pain is unclear.
5. A dashboard theme may improve perceived polish but is unlikely to materially reduce onboarding time.

## Business Assumptions

1. Activation and onboarding completion are important growth metrics.
2. Reducing onboarding friction may improve:
   - Trial-to-paid conversion
   - Expansion readiness
   - Retention
   - Support efficiency
3. The company should prioritize customer pain over internal request volume unless revenue impact is clearly demonstrated.

## Delivery Assumptions

| Candidate | Assumed Effort | Confidence |
|---|---:|---:|
| A: Guided import wizard | Medium | Medium |
| B: AI report writer | High | Low-Medium |
| C: New dashboard theme | Low | High |

---

# Prioritization Framework: RICE

RICE = **Reach × Impact × Confidence ÷ Effort**

Scoring scale:
- **Reach**: Relative number of users affected per quarter
- **Impact**: 0.25 = minimal, 0.5 = low, 1 = medium, 2 = high, 3 = massive
- **Confidence**: Percentage confidence in the estimate
- **Effort**: Person-months or relative effort units

## RICE Scoring

| Candidate | Reach | Impact | Confidence | Effort | RICE Score | Notes |
|---|---:|---:|---:|---:|---:|---|
| **A: Guided import wizard** | 800 | 2.0 | 75% | 3 | **400** | Directly addresses onboarding time and setup confusion |
| **B: AI report writer** | 300 | 1.0 | 45% | 5 | **27** | Sales-requested, but user pain and adoption unclear |
| **C: New dashboard theme** | 1,000 | 0.25 | 70% | 1 | **175** | Broad reach and low effort, but weak impact on stated problem |

## RICE Formula

```text
RICE Score = (Reach × Impact × Confidence) / Effort
```

Example for Candidate A:

```text
(800 × 2.0 × 0.75) / 3 = 400
```

---

# Recommendation by Candidate

## 1. Candidate A: Guided Import Wizard

### Recommendation: Build first

This is the strongest roadmap candidate because it directly addresses the known customer complaint: **SMB admins struggle with onboarding time and setup confusion**.

### Why it should win

- Directly maps to the stated customer pain.
- Likely improves activation.
- Likely reduces support tickets.
- Helps SMB admins reach value faster.
- Could improve conversion and retention.
- Creates a stronger first-use experience.

### Suggested MVP Scope

The first version should be focused and measurable:

1. Step-by-step import flow
2. Clear progress indicator
3. Pre-import validation
4. Error handling with human-readable fixes
5. Sample template or example file
6. Success confirmation and next recommended action

### Key Metrics

Primary success metric:

```text
Median Time to Complete Onboarding
```

Supporting metrics:

| Metric | Formula |
|---|---|
| Onboarding Completion Rate | Completed Onboarding Users / Started Onboarding Users |
| Time to Value | Time from Signup to First Meaningful Outcome |
| Import Success Rate | Successful Imports / Import Attempts |
| Setup Drop-off Rate | Users Dropping During Setup / Users Starting Setup |
| Activation Rate | Activated Accounts / New Accounts |
| Support Ticket Rate | Onboarding Support Tickets / New Accounts |
| Trial-to-Paid Conversion | Paid Conversions / Trial Signups |

### Suggested Target Outcomes

These are assumptions and should be validated with baseline data:

| Metric | Target |
|---|---:|
| Reduce median onboarding time | 20–30% |
| Increase onboarding completion rate | 10–15% |
| Reduce import-related support tickets | 15–25% |
| Improve activation rate | 5–10% |

---

## 2. Candidate B: AI Report Writer

### Recommendation: Validate before building

The AI report writer may be valuable, especially if sales is hearing strong buyer demand. However, based on the given context, it does not directly address the known onboarding issue.

### Why not prioritize now

- Requested by sales, but actual user demand is uncertain.
- May have higher engineering and product complexity.
- AI quality, trust, permissions, and accuracy risks are likely.
- Impact on onboarding time is unclear.
- Could distract from solving the current primary customer pain.

### Recommended Next Step

Run discovery before placing this on the committed roadmap.

Validation activities:

1. Interview sales team to understand request source.
2. Review lost deals mentioning reporting or AI.
3. Interview 5–8 SMB admins or buyers.
4. Test clickable prototype.
5. Measure willingness to pay or conversion impact.

### Decision Criteria

Candidate B should move up the roadmap only if evidence shows:

| Criterion | Threshold |
|---|---:|
| % of target customers requesting better reports | >30% |
| Clear impact on sales conversion | Meaningful or repeatedly cited |
| Prototype task success | >70% |
| Willingness to pay | Validated |
| AI output trust rating | High |

### Key Metrics

| Metric | Formula |
|---|---|
| Feature Adoption Rate | Users Using AI Report Writer / Eligible Users |
| Report Generation Success Rate | Successful Reports / Report Attempts |
| Retention of Feature Use | Repeat Users / First-Time Users |
| Sales Win Rate Impact | Won Deals / Qualified Opportunities |
| Expansion Revenue Influenced | Expansion ARR Attributed to Feature |

---

## 3. Candidate C: New Dashboard Theme

### Recommendation: Defer

The new dashboard theme has low engineering effort, but it appears least connected to the core customer problem. It may improve aesthetics, but it is unlikely to meaningfully reduce onboarding time.

### Why it should not be prioritized

- Low strategic alignment with onboarding pain.
- Likely cosmetic rather than functional.
- Broad reach does not equal meaningful impact.
- Could consume design, QA, and release bandwidth.
- May introduce visual regressions or user confusion.

### When to Consider It

Candidate C may be worth doing if:

1. It is part of a larger UX refresh.
2. It improves accessibility or usability, not just aesthetics.
3. It supports a rebrand or enterprise sales motion.
4. It can be bundled into existing frontend work with minimal opportunity cost.

### Key Metrics

| Metric | Formula |
|---|---|
| Dashboard Engagement | Active Dashboard Users / Eligible Users |
| Task Completion Rate | Completed Dashboard Tasks / Started Dashboard Tasks |
| User Satisfaction | Survey Score or CSAT |
| Support Tickets Related to UI | UI Support Tickets / Active Accounts |

---

# MoSCoW Prioritization

| Candidate | MoSCoW Category | Rationale |
|---|---|---|
| **A: Guided import wizard** | **Must Have** | Directly addresses onboarding complaints |
| **B: AI report writer** | **Could Have** | Potentially valuable but needs validation |
| **C: New dashboard theme** | **Won’t Have for Now** | Low connection to stated problem |

---

# North Star and Supporting Metrics

## Recommended North Star Metric

```text
Activated SMB Accounts
```

Definition:

```text
Activated SMB Accounts = SMB accounts that complete onboarding and achieve first meaningful value
```

Example activation event could be:

```text
Account successfully imports data and views first useful dashboard/report
```

## Supporting Metrics

| Metric | Why It Matters |
|---|---|
| Time to Value | Measures onboarding speed |
| Onboarding Completion Rate | Measures setup success |
| Import Success Rate | Measures effectiveness of Candidate A |
| Activation Rate | Measures product adoption |
| Trial-to-Paid Conversion | Measures business impact |
| Onboarding Support Tickets | Measures confusion and operational burden |
| 30-Day Retention | Measures whether activation leads to stickiness |

---

# Suggested Roadmap Plan

## Now: Build Candidate A MVP

Timebox: 4–6 weeks, depending on engineering capacity.

Deliverables:

1. Import wizard MVP
2. Event instrumentation
3. Onboarding funnel dashboard
4. Support ticket tagging for import/setup issues
5. Post-onboarding user survey

## Next: Validate Candidate B

Timebox: 2–3 weeks discovery.

Deliverables:

1. Sales evidence summary
2. Customer interview notes
3. Prototype test results
4. Revenue impact estimate
5. Go/no-go decision

## Later: Reassess Candidate C

Do not prioritize unless there is evidence that the theme improves usability, accessibility, or conversion.

---

# Final Decision

## Build Candidate A first: Guided Import Wizard

Candidate A has the best alignment with the known customer problem and the clearest path to measurable product and business impact.

Candidate B should enter discovery, not development.

Candidate C should be deferred unless it can be completed opportunistically without delaying higher-impact onboarding work.
