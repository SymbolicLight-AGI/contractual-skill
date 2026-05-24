## 1. Goal and user

**Requested product idea:** “AI insights for all users.”

**Current goal statement:** Not yet PRD-ready. The request is too broad to define requirements, scope, or success criteria without more evidence.

**Target user:** Unknown. “All users” is not specific enough to support product decisions because different user segments likely have different workflows, permissions, data access, expectations, and risk profiles.

**Decision type:** Discovery / problem framing before PRD requirements.

**Product-management response:**  
Before writing a full PRD, we should create a discovery brief that defines the user segment, job-to-be-done, data inputs, expected output, success metric, and risk boundaries. A PRD written now would likely encode assumptions as requirements.

---

## 2. Known facts

### Supplied facts
- A stakeholder requested a PRD.
- The proposed concept is: **“AI insights for all users.”**
- No user segment was provided.
- No workflow was provided.
- No data source was provided.
- No success metric was provided.

### Not supplied
- Target users or personas.
- User pain or customer evidence.
- Current workflow or where the feature would appear.
- Data availability, quality, or permission model.
- Desired AI output type.
- Business objective.
- Competitive or customer demand evidence.
- Technical feasibility.
- Legal, privacy, or compliance constraints.
- Launch timing or roadmap priority.

**Confidence:** High that the request is under-specified, because core PRD inputs are missing.

---

## 3. Assumptions and unknowns

### Assumptions we should not convert into requirements yet
- That all users want AI-generated insights.
- That the available data is sufficient for useful insights.
- That users trust AI-generated recommendations.
- That the same insight format works across all user segments.
- That AI insights will improve activation, retention, revenue, productivity, or satisfaction.
- That this can be safely launched to all users without permission, privacy, or quality issues.

### Open questions

#### User and problem
1. Which user segment has the strongest need?
2. What specific decision or task are users trying to complete?
3. What pain exists in the current workflow?
4. Is the pain based on customer interviews, support tickets, usage data, sales feedback, or stakeholder intuition?
5. Are there users who should not receive AI insights?

#### Workflow
6. Where would the insights appear?
7. What user action should the insight help with?
8. Is the insight proactive, on-demand, embedded in a report, or delivered as a notification?
9. How frequently would users need these insights?
10. What does the user do after seeing an insight?

#### Data and permissions
11. What data sources can the AI use?
12. Is the data structured, unstructured, internal, customer-provided, or third-party?
13. Are there role-based access constraints?
14. Are there privacy, compliance, or contractual limits on using this data?
15. How will incorrect or incomplete data be handled?

#### AI behavior
16. What type of “insight” is expected?
   - Summary?
   - Trend detection?
   - Anomaly detection?
   - Recommendation?
   - Forecast?
   - Explanation?
   - Next-best action?
17. Should the AI cite sources or explain reasoning?
18. What level of accuracy is required?
19. What happens when the AI is uncertain?
20. Can users give feedback on insight quality?

#### Success and business value
21. What business goal should this support?
22. What user behavior should change?
23. What metric would indicate the feature is useful?
24. What is the expected learning goal for an initial pilot?
25. What would cause us to stop or pivot?

---

## 4. Recommendation or options

### Recommendation

Do **not** write a full PRD for “AI insights for all users” yet. Instead, create a **Discovery PRD / Opportunity Brief** focused on identifying one high-value user segment, one workflow, one data source, and one measurable outcome.

The first milestone should be evidence-gathering, not broad implementation.

---

## Draft Discovery PRD

### Working title
AI Insights Discovery Brief

### Problem statement
We have a stakeholder request to provide AI-generated insights, but we do not yet know which users need them, what workflow they support, what data they should use, or how success should be measured.

### Objective
Determine whether there is a specific user segment and workflow where AI-generated insights can produce measurable user or business value.

### Non-goals
For the discovery phase, we are **not** committing to:
- Launching AI insights to all users.
- Building a generalized AI assistant.
- Supporting every workflow.
- Making automated decisions on behalf of users.
- Using all available customer data.
- Replacing existing dashboards, reports, or human review processes.
- Making customer-facing claims about accuracy or performance.

### Candidate product hypotheses

These are hypotheses, not validated requirements.

| Hypothesis | Evidence status | Validation needed |
|---|---:|---|
| Users have trouble finding important patterns in existing data. | Unknown | Interviews, usage data, support tickets |
| AI can summarize or surface patterns better than current UI. | Unknown | Prototype test |
| A specific user segment would act on AI-generated insights. | Unknown | Segment research |
| The required data exists and is accessible. | Unknown | Data audit |
| Users would trust AI insights if sources are shown. | Unknown | Usability testing |
| AI insights can improve a measurable product or business outcome. | Unknown | Pilot or experiment |

---

## 5. Possible scope options

### Option A: Broad “AI insights for all users”
**Description:** Build AI insights available to the entire user base.

**Pros**
- Aligns with the stakeholder’s broad request.
- Could create visible AI positioning.

**Cons**
- Highest risk of solving an unclear problem.
- Requires broad data, permission, reliability, and UX decisions.
- Hard to measure success because user needs may differ.
- Higher chance of low adoption or mistrust.
- Could create compliance, privacy, or quality concerns.

**Recommendation:** Do not proceed without stronger evidence.

---

### Option B: Segment-specific AI insight pilot
**Description:** Choose one user segment and one workflow, then test a narrow AI insight experience.

**Pros**
- Easier to validate user value.
- Easier to define success metrics.
- Lower engineering and compliance risk.
- More actionable learning.
- Can expand later if validated.

**Cons**
- Does not immediately satisfy “all users.”
- Requires stakeholder agreement on pilot scope.
- May reveal the idea is not valuable.

**Recommendation:** Preferred path.

---

### Option C: Non-AI insight improvement first
**Description:** Improve existing reports, alerts, filters, or dashboards before using AI.

**Pros**
- May solve the user problem with lower complexity.
- Easier to explain, test, and trust.
- Avoids premature AI investment.

**Cons**
- May not satisfy stakeholder interest in AI.
- May miss opportunities where natural language, summarization, or pattern detection creates unique value.

**Recommendation:** Keep as a comparison path during discovery.

---

## 6. Metrics and validation

### Discovery success criteria

Before moving to a build PRD, we should have evidence for:

1. **Target segment identified**
   - A specific user group with a recurring pain.
   - Evidence source: interviews, support tickets, analytics, sales/customer success input, or existing research.

2. **Workflow identified**
   - Clear moment where the user needs help interpreting data or deciding what to do next.

3. **Data feasibility confirmed**
   - Known data source.
   - Known permissions.
   - Known freshness and quality constraints.
   - Initial engineering/data review completed.

4. **User value hypothesis validated**
   - Users can understand the proposed insight.
   - Users believe it would help them make a decision or take action.
   - Users can describe what they would do after seeing it.

5. **Success metric selected**
   - One primary product metric and supporting guardrail metrics.

### Candidate success metrics

These are options, not commitments.

#### Adoption metrics
- Percentage of target users who view an AI insight.
- Repeat usage rate.
- Click-through or expansion rate on insight details.

#### Action metrics
- Percentage of users who take a recommended or related action.
- Reduction in time to identify an issue.
- Increase in completion of a target workflow.

#### Quality metrics
- User rating of insight helpfulness.
- Percentage of insights marked inaccurate or irrelevant.
- Rate of user dismissal or ignore behavior.

#### Trust and safety metrics
- Percentage of insights with source references.
- AI error report rate.
- Escalation/support ticket rate related to AI output.
- Opt-out rate, if applicable.

#### Business metrics
- Retention, conversion, expansion, or engagement metrics may be relevant, but no specific business goal has been provided yet.

---

## 7. Risks and human gates

### Key risks

#### Product risk
We may build a feature that sounds valuable but does not solve a specific user problem.

#### Adoption risk
“Insights” may be ignored if users do not understand, trust, or need them.

#### Data risk
The required data may be unavailable, incomplete, stale, biased, or inaccessible due to permissions.

#### AI quality risk
Generated insights may be inaccurate, vague, non-actionable, or misleading.

#### Trust risk
Users may not act on AI output unless the system shows sources, confidence, and reasoning.

#### Privacy and compliance risk
Using customer or user data for AI-generated insights may require legal, privacy, or contractual review.

#### Scope risk
“All users” creates broad requirements before a validated use case exists.

### Human gates required before proceeding

Before committing to a launch or full PRD, we need confirmation from:

- **Product leadership:** approve narrowed discovery scope.
- **Design:** define prototype and interaction model.
- **Engineering/data:** assess data availability and feasibility.
- **Legal/compliance/privacy:** review data use and AI-generated output risks.
- **Customer-facing teams:** identify candidate users and collect evidence.
- **Leadership/roadmap owner:** approve any material roadmap commitment.

No launch date, pricing implication, customer-facing promise, or broad roadmap commitment should be made at this stage.

---

## 8. Next steps

### Immediate next step
Convert the stakeholder request into a discovery plan.

### Proposed 2-step validation plan

#### Step 1: Clarify the opportunity
Meet with the stakeholder and ask:

1. Which user segment did you have in mind?
2. What customer or business problem are we solving?
3. What evidence prompted this request?
4. What workflow should the AI insight support?
5. What action should users take after seeing an insight?
6. What data should the AI use?
7. What would make this successful?
8. Why should this be available to all users rather than a focused segment first?

#### Step 2: Validate one narrow use case
Select one candidate segment and workflow, then run lightweight validation:

- Review existing support tickets, sales notes, analytics, or user research.
- Interview 5–8 target users or customer-facing team members.
- Audit available data sources.
- Create a low-fidelity prototype or mocked insight.
- Test whether users understand it, trust it, and know what action to take.
- Define success and guardrail metrics before build.

---

## Suggested stakeholder response

“We can frame a PRD, but the current request for ‘AI insights for all users’ is missing the core evidence needed to define requirements responsibly. We do not yet know the target user, workflow, data source, or success metric. I recommend we first create a discovery brief and validate one narrow use case. Once we identify the user segment, workflow, available data, and measurable outcome, we can convert that into a build-ready PRD.”
