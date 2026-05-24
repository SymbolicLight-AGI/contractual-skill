# Response to PRD Request: "AI Insights for All Users"

I can't produce a complete PRD yet — the request is missing the inputs a PRD requires. Writing one anyway would fabricate customer evidence, target segments, and success criteria, which is the most common cause of failed launches. Here is what I can do instead.

---

## 1. What's Missing (and Why It Blocks a PRD)

| PRD Section | Missing Input | Why It Matters |
|---|---|---|
| **Target user** | No segment defined ("all users" is not a segment) | Different personas have different decision contexts; "insights" means different things to an admin vs. an analyst vs. an end consumer |
| **Problem / JTBD** | No workflow or job articulated | Without a Job-to-be-Done, we can't tell if AI is the right solution or a solution looking for a problem |
| **Evidence** | No interviews, support tickets, usage data, or win/loss signal | Risk of building on opinion rather than demand |
| **Data source** | Unknown what the AI would reason over | Determines feasibility, latency, cost, and accuracy ceiling |
| **Success metric** | Undefined | Cannot prioritize, scope, or evaluate launch |
| **Constraint set** | No timeline, budget, compliance, or model preference | Cannot make tradeoffs |

**Uncertainty flag:** Everything below — scope, users, value — is currently unsupported by evidence. Do not treat any of it as validated.

---

## 2. Recommended Next Step: Discovery Brief Before PRD

I recommend we **replace the PRD request with a one-week discovery sprint**, structured around an **Opportunity Solution Tree**, then return with either a scoped PRD or a "do not build" recommendation.

### Discovery Brief (One-Pager)

**Desired outcome (to be confirmed by stakeholder):**
> *What business result does "AI insights" exist to move? (e.g., activation, retention, expansion, support deflection, time-to-value)*

**Candidate opportunities to investigate:**
- Which user segment(s) currently lose time interpreting data in our product?
- Where do users today export data to spreadsheets or BI tools? (signal of unmet insight need)
- What questions do users ask support/CS that an AI surface could answer?

**Disqualifiers (kill criteria):**
- No identifiable segment with a recurring, high-frequency job
- No accessible, high-quality data source to ground the AI on
- No measurable behavior we expect to change

---

## 3. Questions I Need Answered to Write the PRD

Please provide, or authorize discovery to find:

1. **Outcome** — Which company/product metric should this move? (Pick one primary.)
2. **Segment** — Which user role and what tier/plan?
3. **Job** — What decision or task is the user trying to complete when they would invoke "insight"?
4. **Evidence** — Do we have interviews, tickets, NPS verbatims, or usage data pointing to this need? If not, can we run 5–8 interviews?
5. **Data surface** — What data would the AI analyze? Is it in our system, governed, and permissioned?
6. **Success metric** — How will we know in 90 days post-launch whether this worked? (e.g., % of WAU using insights, action-taken rate, retention lift in cohort)
7. **Constraints** — Deadline driver, budget, compliance (PII, SOC2, regional), build-vs-buy stance on models.
8. **Non-goals** — What is explicitly out of scope to keep this shippable?

---

## 4. Skeleton PRD (To Be Filled — Not a Commitment)

I'll stage this so it's ready the moment inputs arrive.

```
PRD: [Feature Name] — DRAFT, AWAITING DISCOVERY

1. Problem & Evidence          [BLOCKED — needs interviews / data]
2. Target User & JTBD          [BLOCKED — needs segment + job]
3. Desired Outcome & Metric    [BLOCKED — needs primary metric]
4. Solution Hypothesis         [BLOCKED — pending problem definition]
5. Scope (In / Out / Later)    [BLOCKED]
6. Data & Model Approach       [BLOCKED — needs data source review]
7. Risks & Assumptions         Known: scope ambiguity, evidence gap
8. Launch Plan & Rollout       [BLOCKED]
9. Success Criteria (90-day)   [BLOCKED]
10. Open Questions             See Section 3 above
```

---

## 5. Frameworks I'll Apply Once Inputs Exist

- **Jobs-to-be-Done** — to define the job, not the feature
- **Opportunity Solution Tree** — to ensure the AI solution maps to a validated opportunity
- **RICE** — to prioritize against other roadmap candidates once reach/impact are estimable
- **North Star Metric alignment check** — to confirm this feature moves the metric that matters
- **Kano** — to test whether "AI insights" is a delighter, performance, or basic expectation for the chosen segment

---

## Recommendation

**Do not approve a PRD for "AI insights for all users" as stated.** Approve a 1-week discovery instead. If discovery surfaces a specific segment, job, data source, and measurable outcome, I will return with a complete PRD. If it does not, I will return with a written "do not build / build later" rationale so the team can redeploy capacity.
