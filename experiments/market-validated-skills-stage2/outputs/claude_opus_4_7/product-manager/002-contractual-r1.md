# PRD Framing: "AI Insights for All Users"

The request as stated cannot be turned into a reviewable PRD. There is no user segment, workflow, data source, or success metric supplied. Below is a framing artifact that surfaces what is known, what is missing, and the validation step required before a PRD is appropriate.

---

## 1. Goal and User

- **Stated goal (supplied):** Deliver "AI insights for all users."
- **Target user (supplied):** None. "All users" is not a segment; it is a scope statement.
- **Inferred decision type:** Discovery, not requirements. A PRD presumes a defined user, problem, and success criterion. None are present.

Confidence: low that a PRD is the right next artifact.

---

## 2. Known Facts

- A stakeholder has requested a PRD.
- The phrase used is "AI insights for all users."
- No user segment, workflow, data source, metric, constraint, or evidence was supplied.

That is the complete set of supplied facts.

---

## 3. Assumptions and Unknowns

Marked as assumption (A) or unknown (U). None are validated.

- (U) Which user segment experiences the pain that "AI insights" would address.
- (U) What workflow or decision the insight is meant to support.
- (U) What data source would feed the insights, and whether the company has rights and quality to use it.
- (U) What "insight" means here: summary, recommendation, anomaly detection, forecast, natural-language Q&A, or something else.
- (U) Whether users have asked for this, or whether it is a supply-side idea.
- (U) Business goal behind the request: retention, expansion, differentiation, cost reduction, or executive signaling.
- (U) Success metric and target.
- (U) Constraints: timeline, budget, model/vendor, privacy, regulated data.
- (A) "All users" likely means "in-product for the existing user base," but this is not confirmed.

---

## 4. Recommendation

Do not write a PRD yet. Writing one now would convert unresolved assumptions into requirements, which this Skill prohibits.

Recommended next artifact: a **one-page discovery brief** plus a **stakeholder clarification round**. Two options for how to proceed:

- **Option A — Clarify first (recommended).** Send the stakeholder the open-questions list below. Block PRD work until at least segment, problem, and success metric are answered.
- **Option B — Hypothesis-driven discovery.** If the stakeholder cannot answer yet, run a time-boxed discovery (e.g., 2 weeks) on one narrowed hypothesis (e.g., "Power users on the analytics dashboard want auto-generated summaries to reduce time-to-insight"). Output is a validated or invalidated hypothesis, not a PRD.

Tradeoff being made explicit: choosing rigor over speed. We are not optimizing for "ship something with AI soon." If the real goal is a visible AI launch on a deadline, that should be stated so the conversation can shift to scope-cutting rather than discovery.

---

## 5. Metrics and Validation

No metrics can be defined until the user and job are defined. Placeholder metric structure to be filled once discovery returns:

- **Adoption:** % of target segment using the insight surface per [period].
- **Engagement quality:** action taken on insight (accept, dismiss, drill-in).
- **Outcome metric:** the user or business KPI the insight is supposed to move (unknown).
- **Guardrail:** trust/quality signal (e.g., reported inaccuracy rate), latency, cost per insight.

Validation steps before PRD:

1. 5–8 user interviews in the candidate segment to confirm a real pain.
2. Review of existing usage data and support tickets for evidence of the pain (none supplied).
3. Lightweight prototype or Wizard-of-Oz test of one insight type.
4. Data feasibility check with data/engineering.

---

## 6. Risks and Human Gates

Risks:

- **Solution-first framing.** "AI insights" names a technology, not a user problem. High risk of building something nobody uses.
- **Scope risk.** "All users" almost always collapses under segmentation; building for everyone usually serves no one.
- **Trust risk.** AI outputs that are wrong or vague erode product trust quickly.
- **Data and compliance risk.** Unknown data sources may include regulated or sensitive data.
- **Cost risk.** Per-call model costs at "all users" scale can be material.

Human gates required before proceeding past discovery:

- Stakeholder confirmation of the actual business goal and target segment.
- Engineering feasibility sign-off on data and model approach.
- Legal/compliance review if any user data, customer data, or regulated content is involved.
- Leadership confirmation if pricing, packaging, or a launch date is implied.

This Skill cannot commit to a launch date, pricing, customer-facing claim, or engineering scope.

---

## 7. Next Steps

1. Send the stakeholder the following open questions and request answers before PRD work:
   - Which user segment, and what job are they trying to do?
   - What evidence (tickets, interviews, usage data) suggests this is a real pain?
   - What business outcome should this move, and by how much?
   - What data is available, and are there privacy or compliance constraints?
   - Is there a deadline, budget, or vendor/model constraint?
   - What does "insight" mean concretely — one example would unblock framing.
2. In parallel, schedule 5–8 discovery interviews in the most likely segment.
3. Request a data/feasibility spike from engineering and data.
4. Re-convene to decide: write PRD for a narrowed scope, run a prototype test, or defer.

---

**Boundary note:** A full PRD is out of scope until segment, problem, data, and success metric are supplied or discovered. The correct next step is the discovery brief and stakeholder clarification above, not a speculative PRD.
