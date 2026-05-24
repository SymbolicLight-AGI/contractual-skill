# Product Management Response: PRD Cannot Be Completed Yet — Evidence Gap Identified

A PRD for **“AI insights for all users”** cannot be responsibly written as a delivery-ready requirement because the request is missing the core evidence needed to define the problem, target user, workflow, data inputs, expected value, and success criteria.

Instead of pretending those answers exist, I would frame this as a **discovery-stage PRD brief** and define the decisions required before moving into solution design or engineering execution.

---

## 1. Current Request

> “Build AI insights for all users.”

## 2. Product Assessment

This request is currently too broad to convert into a PRD because it lacks:

| Missing Area | Why It Matters |
|---|---|
| User segment | “All users” may hide very different needs, permissions, data access, and value drivers |
| User problem | We do not know what decision, task, or pain point the AI insight should improve |
| Workflow context | Insights are only useful if delivered at the right moment in the user journey |
| Data source | AI output quality depends on available, reliable, permissioned data |
| Success metric | We cannot evaluate impact, prioritize tradeoffs, or define launch readiness |
| Trust requirements | AI-generated recommendations may require explainability, confidence, or auditability |
| Business goal | The feature could aim to improve activation, retention, monetization, productivity, or satisfaction — these imply different products |

---

# Discovery-Stage PRD Brief

## Working Title

**AI Insights — Discovery Brief**

## Status

Discovery required before PRD approval.

## Problem Statement

We have a stakeholder request to provide AI-generated insights to users, but we do not yet have validated evidence that identifies:

- Which users need these insights
- What problem the insights solve
- Where the insights should appear
- What data should power them
- What measurable outcome would define success

Until these are clarified, the team should not commit to scope, timeline, or engineering implementation.

---

## Objective

Determine whether there is a valuable, feasible, and measurable opportunity to provide AI-generated insights within the product.

---

## Key Product Questions

### User

1. Which user segment is this for?
   - New users?
   - Power users?
   - Admins?
   - Analysts?
   - Managers?
   - Paying customers only?
   - Enterprise customers?
2. What user job are we helping with?
3. What decision or action should the user take after seeing an insight?
4. How do users solve this problem today?
5. How frequent and painful is the problem?

### Workflow

6. Where in the product journey should the insight appear?
7. Is the insight proactive, reactive, or user-requested?
8. Should it be shown in dashboards, reports, notifications, search, chat, or a workflow-specific surface?
9. What action should be available from the insight?
10. What happens if the user ignores it?

### Data

11. What data sources are available?
12. Are the data sources structured, reliable, and permissioned?
13. Is the data real-time, historical, or batch-processed?
14. Are there privacy, compliance, or tenant-isolation concerns?
15. Are there gaps that would make generated insights inaccurate or misleading?

### AI Behavior

16. What type of insight is expected?
   - Trend detection?
   - Anomaly detection?
   - Recommendation?
   - Summary?
   - Forecast?
   - Explanation?
   - Benchmark?
17. Does the insight need a confidence score?
18. Does it need citations or source traceability?
19. Should users be able to give feedback?
20. What failure modes are unacceptable?

### Business

21. What business outcome should this support?
   - Activation
   - Retention
   - Expansion
   - Engagement
   - Conversion
   - Support deflection
   - Productivity
22. Is this a differentiator, table-stakes feature, or revenue opportunity?
23. Is there competitive pressure or customer demand?
24. Which customers or deals are asking for this?
25. What is the cost of not building it?

---

# Proposed Discovery Plan

## Phase 1: Stakeholder Intake

Goal: Clarify business intent and constraints.

Recommended participants:

- Product stakeholder
- Product manager
- Design
- Engineering
- Data/ML lead
- Customer success or sales
- Legal/security if customer data is involved

Output:

- Target user hypothesis
- Business outcome hypothesis
- Initial use-case candidates
- Known data sources
- Constraints and risks

---

## Phase 2: Customer Evidence Gathering

Goal: Validate whether users actually need AI-generated insights and where they would create value.

Recommended research:

- 5–8 customer interviews for the most likely target segment
- Review support tickets, sales calls, customer requests, and usage analytics
- Identify repeated workflows where users currently interpret data manually
- Capture examples of decisions users struggle to make

Evidence to collect:

| Evidence Type | Example |
|---|---|
| User pain | “I don’t know what changed or why.” |
| Current workaround | Exporting data to spreadsheets or asking analysts |
| Frequency | Daily, weekly, monthly |
| Impact | Lost time, missed revenue, risk, poor decisions |
| Desired action | What the user would do differently with an insight |

---

## Phase 3: Opportunity Framing

Use an **Opportunity Solution Tree** or **Jobs-to-be-Done** framing.

Example structure:

```markdown
Business Outcome:
TBD

Target User:
TBD

User Job:
When [situation], I want to [motivation], so I can [desired outcome].

Opportunity:
TBD

Potential AI Insight:
TBD

Expected User Action:
TBD

Success Metric:
TBD
```

---

# PRD Readiness Criteria

A full PRD should not be written until the following are known:

| Readiness Requirement | Status |
|---|---|
| Target user segment identified | Missing |
| User problem validated | Missing |
| Workflow location defined | Missing |
| Data source confirmed | Missing |
| AI output type defined | Missing |
| User action clarified | Missing |
| Success metric selected | Missing |
| Technical feasibility assessed | Missing |
| Trust and safety requirements identified | Missing |
| Launch scope agreed | Missing |

---

# Draft PRD Skeleton

This is the structure I would use once discovery answers are available.

## 1. Overview

### Product Area

TBD

### Feature Name

AI Insights

### Status

Discovery

### Owner

TBD

### Stakeholders

TBD

---

## 2. Problem Statement

TBD after user research.

Current known issue:

> Stakeholders believe users may benefit from AI-generated insights, but we do not yet have evidence of the specific user problem, workflow, or outcome.

---

## 3. Goals

Potential goals to validate:

- Help users identify important changes or opportunities faster
- Reduce manual analysis effort
- Improve decision quality
- Increase product engagement
- Improve retention or expansion

Final goals: TBD.

---

## 4. Non-Goals

Until further evidence is gathered, the following should be treated as non-goals:

- Building AI insights for every user segment at launch
- Generating insights from unvalidated or low-quality data
- Shipping black-box recommendations without explainability requirements
- Committing to a broad AI platform before validating a specific use case
- Optimizing for novelty rather than measurable user value

---

## 5. Target Users

TBD.

Candidate segments to evaluate:

- New users who need guidance
- Existing users who monitor performance
- Admins who manage teams or accounts
- Analysts who interpret product data
- Executives who need summaries
- Customer-facing teams using account or usage data

No segment should be selected without evidence.

---

## 6. User Needs

TBD through discovery.

Potential user need formats:

```markdown
As a [user segment],
I want to understand [important change, risk, or opportunity],
so that I can [take a specific action].
```

Example placeholder:

```markdown
As a [TBD user],
I want AI to identify [TBD insight],
so that I can [TBD action/outcome].
```

---

## 7. Use Cases

TBD.

Potential categories to evaluate:

| Use Case Type | Description | Evidence Status |
|---|---|---|
| Summarization | Condense large data or activity into key takeaways | Unvalidated |
| Anomaly detection | Identify unusual changes or outliers | Unvalidated |
| Recommendations | Suggest next-best actions | Unvalidated |
| Forecasting | Predict future outcomes | Unvalidated |
| Benchmarking | Compare performance against peers or past behavior | Unvalidated |
| Risk detection | Surface accounts, workflows, or metrics needing attention | Unvalidated |

---

## 8. Requirements

Not ready for final requirements.

Potential requirement areas:

### Functional Requirements

TBD after use case selection.

Could include:

- Generate insight from selected data source
- Explain why the insight was generated
- Link to supporting data
- Allow user feedback
- Allow dismissal or follow-up action
- Respect permissions and data access controls

### Non-Functional Requirements

Likely required:

- Accuracy threshold: TBD
- Latency: TBD
- Data freshness: TBD
- Permissioning: Required
- Auditability: TBD
- Explainability: TBD
- Availability: TBD
- Compliance requirements: TBD

---

## 9. Metrics

Success metrics cannot be finalized yet.

Candidate metric categories:

| Metric Type | Possible Metric | Requires Validation |
|---|---|---|
| Adoption | % of eligible users viewing insights | Yes |
| Engagement | Click-through rate on insights | Yes |
| Usefulness | Positive feedback rate | Yes |
| Actionability | % of insights leading to a user action | Yes |
| Retention | Retention lift for users exposed to insights | Yes |
| Efficiency | Reduction in time spent analyzing data | Yes |
| Trust | Dismissal rate, correction rate, negative feedback rate | Yes |
| Business impact | Expansion, conversion, or churn impact | Yes |

Recommended primary metric once use case is selected:

> Percentage of target users who take the intended action after viewing a relevant AI insight.

But the actual metric remains TBD until we know the workflow and desired behavior.

---

## 10. Risks

| Risk | Description | Mitigation |
|---|---|---|
| Vague target audience | “All users” may lead to generic, low-value output | Start with one validated segment |
| Poor data quality | AI insights may be inaccurate or irrelevant | Data feasibility assessment |
| Low trust | Users may ignore AI if outputs are unexplained | Provide evidence, confidence, and feedback |
| Scope creep | “AI insights” can expand into many products | Define one narrow MVP use case |
| Compliance risk | Sensitive data may be exposed or inferred | Permissioning and security review |
| No measurable value | Feature may drive novelty but not impact | Define success metric before build |
| Over-automation | Users may need support, not decisions made for them | Keep human-in-the-loop where needed |

---

# Recommended MVP Framing

Do not launch “AI insights for all users.”

Instead, identify one narrow wedge:

```markdown
For [specific user segment],
when they are [specific workflow moment],
use [specific data source]
to generate [specific type of insight],
so they can [specific action],
measured by [specific success metric].
```

Example template:

```markdown
For account admins,
when reviewing team performance,
use recent activity and usage data
to surface unusual drops in engagement,
so they can investigate and take corrective action,
measured by the percentage of insights that lead to an investigation or follow-up action.
```

This is only an example format, not a claim about the actual right use case.

---

# Decision Needed

Before a PRD can be completed, the stakeholder should provide or help validate:

1. The intended user segment
2. The user problem or opportunity
3. The workflow where the insight appears
4. The data source available
5. The action users should take
6. The business outcome expected
7. The primary success metric
8. Any constraints around privacy, accuracy, latency, or compliance

---

# Recommended Next Step

Schedule a **60-minute AI Insights Discovery Alignment session**.

## Proposed Agenda

1. Clarify stakeholder intent
2. Identify candidate user segments
3. List available data sources
4. Map possible workflows
5. Define 3–5 candidate use cases
6. Score use cases using RICE or opportunity sizing
7. Select one discovery target
8. Agree on evidence needed before PRD approval

---

# PM Recommendation

I would not proceed with a full PRD or engineering commitment yet.

The correct next step is to run discovery and convert the request from:

> “AI insights for all users”

Into a validated product opportunity:

> “For [specific user], in [specific workflow], using [specific data], provide [specific AI insight] that helps them [specific action], measured by [specific metric].”
