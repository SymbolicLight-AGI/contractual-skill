# Product Prioritization Recommendation

## 1. Goal and User

**Goal:** Decide which of three roadmap candidates (A, B, C) to prioritize next.
**Primary user (from prompt):** SMB admins, who report onboarding time as a pain point.
**Secondary stakeholder mentioned:** Sales (requester of Candidate B).

## 2. Known Facts (from prompt)

- **Fact:** SMB admins complain about onboarding time. *(Source: prompt; specific volume, severity, and churn impact not provided.)*
- **Fact:** Candidate A is a guided import wizard, expected to reduce setup confusion.
- **Fact:** Candidate B is an AI report writer, requested by sales.
- **Fact:** Candidate C is a new dashboard theme, described as low engineering effort.

## 3. Assumptions and Unknowns

| # | Assumption | Confidence | Why it matters |
|---|---|---|---|
| A1 | Onboarding time is a top-tier driver of SMB admin dissatisfaction or churn | Low — only "complaints" are cited | Determines whether onboarding work outranks revenue-side asks |
| A2 | Setup confusion (not data quality, integrations, or permissions) is the dominant onboarding blocker | Low | Determines whether a guided import wizard actually addresses the root cause |
| A3 | Sales' request for an AI report writer reflects deal-blocking demand, not anecdote | Unknown | Determines whether B has revenue urgency |
| A4 | "Low engineering effort" for Candidate C is confirmed by engineering | Unverified — needs eng input | Affects opportunity cost calculation |
| A5 | Engineering effort for A and B is non-trivial but unspecified | Inferred | Needed for any real prioritization scoring |

**Open questions (missing evidence):**
- How long does onboarding currently take, and what is the target?
- How many SMB admins are affected, and is there churn or conversion data tied to onboarding?
- How many deals has the AI report writer been requested in, and what is the deal value?
- What is the engineering estimate for A, B, and C?
- Are there compliance or data-handling constraints on an AI report writer?
- Is the dashboard theme tied to a known user complaint, or is it cosmetic?

## 4. Recommendation (Options Framing)

Because evidence is thin, this is a **provisional ranking**, not a committed prioritization. A product owner should validate A1–A5 before committing.

**Provisional ranking:**

1. **Candidate A — Guided import wizard.** Directly maps to the only user pain stated in the prompt. Highest alignment with the stated user goal, conditional on A2 holding.
2. **Candidate C — Dashboard theme.** If engineering effort is genuinely low (A4) and it can ship without displacing A, it is a low-cost parallel item. If it competes with A for the same resources, defer it.
3. **Candidate B — AI report writer.** Requested by sales but with no evidence of user pain, deal impact, or feasibility. Park pending discovery, not rejected.

**Tradeoffs being made explicit:**
- Optimizing for: addressing the one stated user complaint.
- Not optimizing for: short-term sales asks, visual polish, or surface-area expansion.
- Risk of this ranking: if A2 is wrong, A ships and onboarding complaints persist.

## 5. Metrics and Validation

**For Candidate A (if pursued):**
- Leading: % of new SMB accounts completing import on first attempt; time-to-first-successful-import; drop-off rate per onboarding step.
- Lagging: onboarding-stage support ticket volume; activation rate (define with data team); 30-day retention for new SMB cohorts.
- Validation before build: 5–8 SMB admin interviews or session recordings of current onboarding to confirm setup confusion is the dominant blocker.

**For Candidate B (before prioritizing):**
- Discovery: sales to list deals where AI report writer was raised, with stage and ACV.
- Validation: 3–5 customer interviews on report-writing workflow; check whether existing reports are even being used.

**For Candidate C (before prioritizing):**
- Confirm engineering estimate.
- Define what success looks like (is there a user request behind it, or only internal preference?). If neither, deprioritize.

## 6. Risks and Human Gates

- **Risk:** Building A on the assumption that "setup confusion" = "import problems" without user research. *Mitigation:* short discovery sprint.
- **Risk:** Declining B without giving sales a clear "why and when we'd revisit." *Mitigation:* shared discovery criteria.
- **Risk:** "Low effort" for C being inaccurate. *Mitigation:* engineering estimate before scheduling.

**Human gates required before proceeding:**
- Engineering: feasibility and effort estimates for A, B, C.
- Sales / CS: evidence backing the AI report writer request.
- Leadership: confirmation that onboarding is the current strategic priority before committing roadmap slots.
- No roadmap commitment, launch date, or customer-facing message should be made from this artifact alone.

## 7. Next Steps

1. Share this artifact with engineering for effort estimates on all three candidates.
2. Run a 1-week discovery on onboarding (interviews + funnel data) to confirm A2.
3. Ask sales for a structured list of deals tied to Candidate B.
4. Decide on C only after engineering confirms effort and a user-facing rationale exists.
5. Reconvene to confirm ranking with evidence before adding anything to the roadmap.

---

**Boundary note:** This Skill can produce the prioritization artifact but cannot commit roadmap slots, confirm engineering effort, validate sales claims, or approve a launch. Those require the handoffs listed in step 1–4 above.
