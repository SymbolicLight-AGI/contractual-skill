# Brainstorming: Analytics Dashboard for Managers

## Understanding Summary

- **Fact:** Product note requests "an analytics dashboard for managers."
- **Fact:** No target user role, metrics, data sources, decision workflows, or success criteria were provided.
- The note is too sparse to design against. We need to clarify purpose and users before exploring approaches.

## Assumptions (proposed, not accepted)

- **Assumption:** "Managers" refers to internal staff rather than external customers.
- **Assumption:** The dashboard is a new artifact, not a modification of an existing one.
- **Assumption:** Some data source already exists somewhere in the system, but its shape is unknown.
- **Assumption:** This is a web-based dashboard rather than embedded in another tool (e.g., Slack, email digest).

These are placeholders only. None should be treated as accepted until you confirm.

## Open Questions (must resolve before design)

1. Who exactly is the "manager"? (e.g., engineering manager, sales manager, operations manager, executive)
2. What decision or action should the dashboard enable? (a dashboard with no decision attached is usually noise)
3. What metrics matter, and who owns their definitions?
4. Where does the underlying data live, and is it already accessible/clean?
5. What does success look like — adoption, faster decisions, replacing a spreadsheet, regulatory reporting, something else?
6. What are explicit non-goals? (e.g., not a BI replacement, not real-time, not for customers)

## Risks

- **Risk:** Building a generic dashboard without a target user typically produces a tool no one uses.
- **Risk:** Unknown data source could make the most desirable metrics infeasible or expensive.
- **Risk:** "Managers" as a category spans wildly different needs; one dashboard rarely serves all of them well.
- **Risk:** Without success criteria, the project cannot be evaluated or shut down.

## Options

I am **not** presenting design options yet. Per the workflow, we should not explore approaches until the purpose and users are clarified. Proposing architectures now would mean inventing project facts.

## Next Step

Per the one-question-at-a-time rule, please answer this first:

**Which best describes the primary "manager" this dashboard is for?**

A. Engineering / technical team manager (e.g., velocity, incidents, on-call)
B. Sales or revenue manager (e.g., pipeline, quota, conversion)
C. Operations manager (e.g., throughput, SLAs, staffing)
D. Executive / cross-functional leader (e.g., high-level KPIs across the business)
E. Other — please describe
F. Unknown — we need to go back to the requester before continuing

Once we lock the user, the next question will be the decision or action the dashboard must support.

---

**Boundary note:** I am in brainstorming mode. I will not draft schemas, pick chart libraries, or produce an implementation plan until (1) understanding is confirmed, (2) options and tradeoffs are reviewed, and (3) you explicitly request a transition to implementation.
