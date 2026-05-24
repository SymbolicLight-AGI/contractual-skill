# PRD Framing: "AI Insights for All Users"

The request as stated cannot be turned into a PRD yet. Below is the product-management framing that identifies what is known, what is missing, and what to do next.

---

## 1. Goal and User

**Supplied goal:** "AI insights for all users."
**Supplied user:** None. "All users" is a scope statement, not a segment.

**Reframed goal (assumption, low confidence):** Deliver AI-generated insights that help a specific user segment make a specific decision faster or better.

> This reframe is an inference. It should be confirmed with the stakeholder before any PRD work proceeds.

---

## 2. Known Facts

- A stakeholder has requested a feature labeled "AI insights."
- The intended audience is described as "all users."
- No user segment, workflow, data source, success metric, or constraint was provided.

That is the full set of supplied facts.

---

## 3. Assumptions and Unknowns

Marked clearly because none of these were supplied.

**Assumptions that would need confirmation:**
- "Insights" means surfaced observations or recommendations derived from existing product data (assumed, not stated).
- "AI" implies an LLM or ML-driven generation step (assumed, not stated).
- There is product data available to generate insights from (assumed, not stated).

**Open questions for the stakeholder:**
1. Which user segment is the priority (e.g., new users, power users, admins, a specific role)?
2. What decision or task should the insight help the user complete?
3. What data source feeds the insight (product usage, customer data, third-party, user-uploaded)?
4. What does success look like — engagement, retention, task completion, revenue, support deflection?
5. What is the business reason for doing this now? Is there a competitive, retention, or sales trigger?
6. Are there constraints (timeline, model, cost, privacy, regulated data)?
7. Is there existing customer evidence (tickets, interviews, requests) suggesting users want this?

Until at least questions 1, 2, 4, and 7 are answered, a PRD would encode guesses as requirements.

---

## 4. Recommendation

**Do not produce a PRD yet.** Producing one now would convert unresolved assumptions into requirements, which is outside the bounds of responsible product framing.

**Recommended path — two options:**

**Option A: Discovery sprint (recommended).**
Spend 1–2 weeks defining the segment, decision, and evidence base before drafting requirements. Output: a validated problem statement and one prioritized use case.

**Option B: Stakeholder alignment session.**
If the stakeholder already has implicit answers, run a 60-minute working session to extract segment, decision, data source, and success metric. Output: enough input to draft a scoped PRD for one segment, not "all users."

Option A is preferred when no customer evidence exists. Option B is acceptable if the stakeholder has context that simply was not included in the request.

---

## 5. Metrics and Validation

Cannot define success metrics without a goal and user. A placeholder metric ("engagement with AI insights") would be vanity instrumentation.

**Validation steps before PRD:**
- 5–8 customer interviews with the candidate segment to confirm the decision the insight should support.
- Review of existing support tickets, sales calls, or usage data for unprompted demand signal.
- A lightweight concept test (mock insight shown to users) before committing engineering scope.

**Metrics to define once segment and decision are known:**
- Adoption (did the target segment use it).
- Task outcome (did the insight change a decision or action).
- Quality (was the insight rated useful, ignored, or wrong).

---

## 6. Risks and Human Gates

**Risks of proceeding as requested:**
- "All users" scope leads to a generic surface that serves no segment well.
- AI-generated insights without a defined decision tend to produce low-trust output and erode credibility.
- Without a success metric defined up front, the feature cannot be evaluated post-launch.
- Hallucination, privacy, and regulated-data risks are unassessed because the data source is unknown.

**Human gates required before further commitment:**
- Stakeholder confirmation of segment and decision.
- Engineering feasibility review once data source is named.
- Legal/privacy review if customer or regulated data is involved.
- Leadership confirmation if this displaces existing roadmap items.

No launch date, scope commitment, or customer-facing claim should be made at this stage.

---

## 7. Next Steps

1. Send the seven open questions back to the stakeholder.
2. Based on the answers, choose Option A (discovery) or Option B (alignment session).
3. After segment and decision are confirmed, draft a scoped PRD for **one segment and one decision**, not "all users."
4. Hand off feasibility to engineering and data-source review to the data team once scope is defined.

---

**Boundary note:** Drafting a full PRD now would require inventing user segments, workflows, and metrics. That is outside what this Skill allows. The correct next step is the question list above.
