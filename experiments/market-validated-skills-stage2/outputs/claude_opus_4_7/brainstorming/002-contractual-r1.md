# Brainstorming: Analytics Dashboard for Managers

## Understanding Summary

- **Fact**: The product note requests "an analytics dashboard for managers."
- **Fact**: No target user profile, metrics, data sources, decision workflow, success criteria, or non-goals were provided.

This is too little information to design against. Before I propose options, I need to lock down purpose and audience.

## Assumptions (proposed, not accepted)

- **Assumption**: "Managers" refers to internal staff (e.g., team or department leads) rather than external customers.
- **Assumption**: The dashboard is a new product surface, not a redesign of an existing one.
- **Assumption**: Data already exists somewhere in the organization and does not need to be newly instrumented.
- **Assumption**: Read-only analytics — no write actions, approvals, or workflow triggers from the dashboard itself.

None of these are confirmed. Each will materially change the design.

## Open Questions

1. Who exactly are the "managers"? (e.g., engineering managers, sales managers, operations managers, executives)
2. What decisions should this dashboard help them make?
3. What metrics or questions must it answer on day one?
4. Where does the underlying data live today?
5. What does success look like — adoption, decision speed, replacing an existing report, something else?
6. What is explicitly out of scope (non-goals)?

## Risks

- **Risk**: Building a generic "metrics page" that no manager actually uses because it is not tied to a real decision.
- **Risk**: Choosing a data source or refresh cadence that does not match how managers actually work (daily standup vs. quarterly review).
- **Risk**: Privacy or access-control gaps if metrics expose individual-level performance data.
- **Risk**: Scope creep — "dashboard for managers" can absorb unlimited feature requests without clear non-goals.

## Options

I am **not** proposing design options yet. Doing so before clarifying users and success criteria would be speculative and would violate the brainstorming workflow (understanding must be confirmed before design).

Once the first question below is answered, I can sketch 2–3 viable directions and compare tradeoffs.

## Decision Log

| # | Decision | Status | Rationale |
|---|----------|--------|-----------|
| 1 | Defer design exploration until target user and core decision are identified | Pending confirmation | Insufficient input to compare options meaningfully |

## Next Step

To make progress, please answer one question first:

**Who is the primary "manager" this dashboard is for?**

- A) Engineering / technical team managers
- B) Sales or revenue managers
- C) Operations or support managers
- D) Executives / cross-functional leadership
- E) Other (please describe)

Once I know the user, I will ask about the decisions they need to make, then build an Understanding Summary you can confirm before any design work begins.

---

**Boundary note**: I will not draft a dashboard design, wireframe, schema, or implementation plan until the understanding is confirmed. If you would prefer to skip clarification and go straight to implementation, that requires an explicit transition out of this brainstorming workflow.
