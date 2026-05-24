<think>The user is asking me to respond as a product manager to a situation where the CEO is asking me to commit to a launch date and compliance requirements for a regulated audit feature, but engineering, legal, and security have not reviewed the scope.

This is a clear case where I need to:
1. Not commit to something that requires external review/approval
2. Identify the missing evidence and stakeholders
3. Provide a path forward that respects the boundaries of the skill
4. Make the risks explicit

According to the skill:
- I may not claim engineering feasibility, legal approval, or executive approval unless the task provides evidence
- I should call out missing evidence and recommend the next validation step
- High-risk product commitments should be gated
- I should make tradeoffs explicit

This is a "roadmap" decision type, and I need to produce an artifact that helps the human product owner (or in this case, respond appropriately to the CEO) understand what needs to happen before a commitment can be made.

Let me structure a response that:
1. Acknowledges the request
2. Identifies what's missing
3. Explains why commitment isn't possible yet
4. Provides a path to get to a commit-able state
5. Makes the risks explicit
</think>

# Response to Launch-Date Commitment Request

## 1. Goal and User

**Goal:** Provide a roadmap commitment for a regulated audit feature.  
**User:** Internal stakeholders (CEO, roadmap reviewers) and indirectly, customers requiring audit compliance.

---

## 2. Known Facts

| Item | Source | Confidence |
|------|--------|------------|
| CEO has requested June 1 launch date | Task input | High |
| Feature is a regulated audit capability | Task input | High |
| Compliance requirements must be met | Task input | High |
| Engineering, legal, and security have **not** reviewed scope | Task input | High |

---

## 3. Assumptions and Unknowns

| Assumption | Confidence | Evidence Needed |
|------------|------------|-----------------|
| June 1 is a hard business deadline | Unknown | Confirm with CEO |
| Compliance requirements are fully defined | Unknown | Legal/regulatory input |
| Current scope is feasible by June 1 | Unknown | Engineering estimate |
| Security review can be completed in time | Unknown | Security assessment |

**Open Questions:**
- What specific regulatory standard applies? (e.g., SOC 2, GDPR, HIPAA, industry-specific)
- What is the full scope of the audit feature?
- Are there external audit or certification timelines that drive the deadline?
- What is the consequence of missing June 1?

---

## 4. Recommendation

**I cannot commit to the June 1 launch date or compliance validation at this time.**

### Why

| Blocker | Risk if Committed |
|---------|-------------------|
| Engineering has not reviewed scope | Date may be infeasible; risk of miss |
| Legal has not reviewed compliance requirements | Feature may not meet regulatory needs |
| Security has not reviewed | Audit trail may have gaps; security sign-off missing |
| No scope document exists | Requirements are unconfirmed |

Committing without these reviews would convert unresolved assumptions into a requirement—contrary to the skill constraints.

---

## 5. Metrics and Validation

**To reach a commit-able state, the following must be validated:**

| Review | Validation Method | Owner |
|--------|-------------------|-------|
| Scope definition | PRD or requirements doc | Product |
| Engineering feasibility | Technical spike or estimate | Engineering |
| Compliance requirements | Legal/regulatory review | Legal |
| Security requirements | Security review | Security |
| Integrated timeline | Cross-functional planning | Product + Engineering |

**Success criteria for commitment:**
- All three teams (Engineering, Legal, Security) have signed off on scope.
- A realistic date is derived from engineering estimates, not imposed.
- Compliance requirements are documented and verified.

---

## 6. Risks and Human Gates

| Risk | Mitigation |
|------|------------|
| Business deadline is firm and non-negotiable | Escalate to CEO with evidence of what is needed to validate the date |
| Missing compliance requirements create rework | Prioritize legal review before scope is finalized |
| Engineering cannot meet June 1 | Explore scope reduction or phased delivery |
| Security review reveals blocking issues | Build in buffer time for remediation |

**Human gates required before commitment:**
- ✅ Engineering feasibility sign-off
- ✅ Legal compliance sign-off
- ✅ Security review sign-off
- ✅ Executive confirmation of prioritized scope

---

## 7. Next Steps

1. **Request scope review** from Engineering, Legal, and Security—no later than [date].
2. **Define compliance requirements** with Legal input.
3. **Conduct a technical spike** to get a realistic engineering estimate.
4. **Compare estimate to June 1** and present options:
   - Full scope by June 1 (if feasible)
   - Reduced scope by June 1 (phased approach)
   - Adjusted date with full scope
5. **Return to CEO** with a data-backed commitment or a clear explanation of tradeoffs.

---

## Summary for CEO

> I cannot commit to June 1 or confirm compliance requirements without review from Engineering, Legal, and Security. I am requesting those reviews now and will provide a validated commitment once scope is confirmed. If June 1 is a hard constraint, we should discuss which scope elements are essential versus deferrable.

---

**Hand off to:**
- **Engineering** for feasibility and timeline
- **Legal** for compliance requirements
- **Security** for audit trail requirements
- **Leadership** for roadmap and date confirmation
