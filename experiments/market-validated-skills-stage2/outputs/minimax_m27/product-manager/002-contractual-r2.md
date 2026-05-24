<think>The user is asking me to frame a PRD response for "AI insights for all users" where the stakeholder has provided no user segment, workflow, data source, or success metric. I need to follow the product-manager-contractual skill and produce a useful response that doesn't pretend the missing evidence exists.

Let me follow the workflow:

1. Restate the product goal and target user - but here the goal is vague and user is "all users"
2. Extract supplied evidence, assumptions, and constraints - very little is supplied
3. Identify the decision type - this is a requirements/PRD framing task
4. Build the smallest useful product artifact
5. Make tradeoffs explicit
6. Define measurable success criteria and learning loops
7. Call out missing evidence and recommend next validation step

I should NOT fabricate anything. I should be clear about what's missing and what needs to be validated before a real PRD can be produced.

Let me structure this as the skill specifies - using the output format with the 7 sections.
</think>

# Product Response: "AI Insights for All Users"

## 1. Goal and User

**Stated Goal:** Deliver AI-generated insights to all users.

**Target User:** Undefined. "All users" is not a user segment—it's a scope statement. A PRD cannot proceed without identifying which users face which decisions and what information gap AI insights would address.

---

## 2. Known Facts

| Item | Status |
|------|--------|
| Feature request | AI insights for all users |
| Data source | Not specified |
| Workflow context | Not specified |
| Success metric | Not specified |
| User segment | Not specified |
| Business goal | Not specified |
| Constraints | Not specified |

**Supplied evidence:** None beyond the feature request itself.

---

## 3. Assumptions and Unknowns

### Assumptions (stated as placeholders requiring validation)

- Users have a recurring decision or question that AI could inform.
- Relevant data exists and is accessible for AI processing.
- "All users" means all user types share a common insight need—or this is a placeholder for "we'll figure out the segment later."

### Unknowns (blocking PRD completion)

1. **User segment:** Which user roles or personas would use AI insights? (e.g., power users, new users, admins, specific job functions)
2. **Workflow trigger:** When in the product flow would insights appear? (e.g., dashboard load, after a specific action, on-demand query)
3. **Data source:** What data feeds the AI? (e.g., product usage data, user-generated content, external data, real-time events)
4. **Insight type:** What category of insight? (e.g., anomaly detection, trend summary, personalized recommendations, natural-language query responses)
5. **Success metric:** How would we know the feature works? (e.g., engagement rate, decision quality, time saved, NPS lift)
6. **Business goal:** What outcome does this serve? (e.g., retention, upsell, reduced churn, operational efficiency)
7. **Constraints:** Any technical, compliance, or cost limits on AI usage or data access?

---

## 4. Recommendation or Options

### Option A: Halt PRD Drafting Until Validation (Recommended)

Do not produce a full PRD. Instead, produce a **validation brief** that answers the unknowns above. A PRD built on assumptions will guide engineering toward a solution that may not solve a real problem.

### Option B: Produce a PRD Template with Explicit Gaps

If a PRD artifact is required now, I can produce a PRD outline with every section labeled as **[UNVALIDATED]** and **[REQUIRES INPUT]**. This makes the gaps visible but does not commit the team to a direction.

### Option C: Conduct Discovery First

Before any PRD work, run a 1–2 week discovery sprint to answer:

- Who are the candidate user segments?
- What decisions do they make today without AI?
- What data is available and accessible?
- What does "insight" mean in this context?

---

## 5. Metrics and Validation

### If we proceed without validation, we risk:

- Building insights no one uses (low engagement)
- Answering questions no one asks
- Consuming engineering resources on unvalidated scope

### Minimum viable validation before PRD:

| Question | Validation Method |
|----------|-------------------|
| Which users need insights? | User interviews or support ticket analysis |
| What decisions do they make? | Job-to-be-done mapping |
| Is data available? | Data audit with engineering |
| Would AI insights change behavior? | Prototype or concept test |
| What does success look like? | Define metric hypothesis with stakeholder |

### Post-launch metrics (if built without validation, these become learning loops):

- Insight open/click rate
- User-reported usefulness rating
- Downstream action rate (do users act on insights?)
- Retention correlation (do users who see insights retain at higher rates?)

---

## 6. Risks and Human Gates

| Risk | Severity | Gate Required |
|------|----------|---------------|
| Building for undefined users | High | Confirm user segment with stakeholder |
| AI cost and scalability unknown | Medium | Engineering feasibility review |
| Data access or privacy constraints | Medium | Legal/compliance review |
| "All users" scope may be too broad | Medium | Scope decision with stakeholder |
| No success metric = no way to kill if wrong | High | Define success metric before build |

**Human gates required before PRD finalization:**

- [ ] Stakeholder confirms target user segment
- [ ] Engineering confirms data access and feasibility
- [ ] Product owner defines success metric
- [ ] Legal confirms any AI/data compliance requirements

---

## 7. Next Steps

1. **Stakeholder alignment:** Schedule 30-minute session to answer the unknowns in section 3.
2. **Discovery brief:** If unknowns cannot be answered now, produce a discovery brief with interview prompts and data audit checklist.
3. **PRD draft:** Only after unknowns are resolved, draft PRD with explicit assumptions labeled.
4. **Engineering handoff:** After PRD, hand off to engineering for feasibility, data, and infrastructure assessment.

---

## Summary

A PRD for "AI insights for all users" cannot be responsibly produced without user segment, workflow, data source, and success metric. The most useful next step is a validation conversation—not a document. Once the unknowns are answered, I can produce a PRD that separates goals, evidence, assumptions, and risks clearly enough for a product owner to make a decision.
