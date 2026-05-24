<think>The user is asking me to prioritize three roadmap candidates using the product-manager-contractual skill. Let me follow the workflow and output format specified in the skill.

The task provides:
- Product idea: SMB admins complain about onboarding time
- Candidate A: guided import wizard, expected to reduce setup confusion
- Candidate B: AI report writer, requested by sales
- Candidate C: new dashboard theme, low engineering effort

I need to create a product prioritization recommendation with assumptions and metrics, following the format:
1. Goal and user
2. Known facts
3. Assumptions and unknowns
4. Recommendation or options
5. Metrics and validation
6. Risks and human gates
7. Next steps

I should NOT fabricate data - I need to be clear about what's known vs assumed. I should not claim customer validation, market sizing, or revenue impact unless evidence is provided.

Let me structure this properly.
</think>

# Product Prioritization Recommendation

## 1. Goal and User

**Goal:** Reduce SMB admin onboarding time and improve setup experience.

**Target User:** SMB administrators setting up the product for the first time.

---

## 2. Known Facts

| Source | Fact |
|--------|------|
| Customer feedback | SMB admins complain about onboarding time (source: unspecified feedback channel) |
| Stakeholder request | Sales team has requested an AI report writer feature |
| Engineering estimate | New dashboard theme has low engineering effort |

---

## 3. Assumptions and Unknowns

| Category | Item |
|----------|------|
| **Assumption** | Guided import wizard will address the root cause of setup confusion, not just surface symptoms |
| **Assumption** | Sales request for AI report writer reflects a revenue-adjacent need, not necessarily a user pain point |
| **Assumption** | Low engineering effort for dashboard theme is accurately estimated |
| **Unknown** | Volume or frequency of SMB admin complaints |
| **Unknown** | Whether setup confusion is caused by import complexity, documentation gaps, or other factors |
| **Unknown** | What evidence supports the AI report writer request (customer quotes, usage data, competitive pressure?) |
| **Unknown** | Whether dashboard theme impacts user activation or retention |

---

## 4. Recommendation or Options

### Recommended Priority Order

| Rank | Candidate | Rationale |
|------|-----------|-----------|
| **1** | **A: Guided Import Wizard** | Directly addresses stated user pain (onboarding time). Aligns with SMB admin complaints. |
| **2** | **B: AI Report Writer** | Addresses stakeholder request but lacks user pain evidence. Defer until validated. |
| **3** | **C: Dashboard Theme** | Low effort is attractive, but no evidence ties it to user or business outcomes. |

### Tradeoffs Made Explicit

- **Candidate A** is prioritized over B and C because it links to a documented user complaint. However, we have not validated that import complexity is the actual bottleneck.
- **Candidate B** is deprioritized because sales requests ≠ user needs. It may be a valid feature, but the evidence chain is weak.
- **Candidate C** is lowest priority because "low effort" is not a reason to build—it is a reason to consider building *if* the feature matters.

---

## 5. Metrics and Validation

| Candidate | Success Metric | Validation Step |
|-----------|----------------|-----------------|
| A: Guided Import Wizard | Time-to-first-success for SMB admins; support tickets tagged "import" | Instrument onboarding flow before/after; run 5 admin interviews on import pain |
| B: AI Report Writer | Not recommended for roadmap until validated | Conduct 3–5 customer interviews to confirm report pain; check if competitors offer this |
| C: Dashboard Theme | Not recommended without outcome link | Define what business metric this would move before prioritizing |

---

## 6. Risks and Human Gates

| Risk | Mitigation |
|------|------------|
| **A may not fix onboarding** | Validate root cause before building. If confusion stems from elsewhere, wizard won't help. |
| **B may be a sales promise** | Do not commit to sales without user validation. Requires human confirmation before any customer-facing commitment. |
| **C has no clear ROI** | Low effort ≠ high value. Requires product owner decision on whether to include as "filler" work. |

**Human Gates Required:**
- Before committing Candidate A to a sprint, confirm root cause with 3–5 SMB admin interviews.
- Before promising Candidate B to sales, require evidence of user demand or competitive necessity.
- Before adding Candidate C to roadmap, define what outcome it serves.

---

## 7. Next Steps

1. **Validate Candidate A:** Interview 3–5 SMB admins to confirm import complexity is the primary onboarding bottleneck. If confirmed, draft wizard scope. If not, identify actual bottleneck.
2. **Validate Candidate B:** Gather 3–5 customer quotes or usage data supporting the report writer need. If absent, close the request with rationale.
3. **Decide on Candidate C:** Product owner decides whether low-effort polish belongs on roadmap without a defined outcome link.
4. **Re-prioritize:** After validation, revisit this matrix with evidence rather than assumptions.

---

*This recommendation is based on the supplied context. No market data, revenue projections, or customer validation has been assumed.*
