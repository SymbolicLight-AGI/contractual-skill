<think>The user is asking me to apply the "brainstorming-contractual" skill to a scenario where the product requirement is extremely vague: "Build an analytics dashboard for managers."

According to the skill, I need to:
1. Not implement anything
2. Ask one question at a time
3. Mark assumptions clearly
4. Create an understanding summary
5. Explore options only after sufficient clarification
6. Not proceed to design until the user confirms understanding

The skill explicitly says: "If key context is missing, continue only by marking assumptions and asking one focused question at a time."

So I should:
- Acknowledge the missing information
- Mark what's unknown as "Open question"
- Propose assumptions as "Assumption"
- Ask ONE focused clarifying question
- Not jump to solutions or design

Let me craft a response that follows the skill's workflow properly. I should start by acknowledging what I know vs don't know, then ask a single clarifying question.

The most fundamental question here would be about the purpose/decision workflow - what decisions will managers make with this dashboard? That's the core of the "clarify purpose" step in the workflow.
</think>

# Understanding Summary

## What We Know
- **Fact:** A product requirement exists to build an analytics dashboard.
- **Fact:** The intended audience is "managers."

## What Is Missing (Open Questions)

| Missing Information | Why It Matters |
|---------------------|----------------|
| Which managers? | Sales? Engineering? Operations? Executive? Each has radically different needs. |
| What decisions will this inform? | Without a decision workflow, we cannot define success. |
| What metrics or KPIs are relevant? | We cannot design data visualization without knowing what to show. |
| Where does the data live? | We cannot specify data sources, pipelines, or refresh cadence. |
| What existing tools or systems exist? | We risk duplicating effort or creating integration gaps. |
| Who owns the data and dashboard? | We cannot define maintenance, access control, or SLA. |
| What is the success criteria? | We cannot validate delivery without measurable outcomes. |
| What is explicitly out of scope? | We cannot bound the work without non-goals. |

## Proposed Assumptions (Not Yet Accepted)

| Assumption | Default | Rationale |
|------------|---------|-----------|
| Manager role | Not yet defined | Could span multiple teams with conflicting needs. |
| Metric domain | Not yet defined | Could be operational, financial, customer, or product metrics. |
| Data source | Unknown | Could require new instrumentation or existing warehouse access. |
| Refresh cadence | Not yet defined | Real-time vs daily vs weekly changes architecture significantly. |
| Deployment context | Unknown | On-prem, cloud, or SaaS affects data access patterns. |

## Risks

- **Risk:** Building a generic dashboard that serves no one well.
- **Risk:** Selecting metrics that don't drive actionable decisions.
- **Risk:** Designing for the wrong data granularity or latency.
- **Risk:** Creating a dashboard that duplicates existing tooling.

---

## Next Step

Before exploring any design options, I need to understand the **decision workflow**.

**Question:** What specific decisions will managers make using this dashboard that they cannot make today?

For example:
- A) Track team performance against quarterly targets
- B) Identify operational bottlenecks or SLA violations
- C) Monitor revenue, costs, or budget utilization
- D) Review customer health, retention, or churn signals
- E) Something else (please describe)

This will anchor the dashboard to real business outcomes rather than generic data display.
