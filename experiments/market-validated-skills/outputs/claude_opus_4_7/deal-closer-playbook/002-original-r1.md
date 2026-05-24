# Deal Closer Playbook — Acme Logistics

Before I generate the playbook, I need to flag several critical gaps and one Skill boundary issue. I'll be direct: with what you've given me, I can produce a useful **advancement playbook** (post-demo → evaluation), but I cannot responsibly produce a true *closing* plan yet. Here's why, and what I need from you.

---

## Skill Boundary Note

The Skill instructs me to use WebSearch to research the target company, competitive landscape, and recent news before generating competitive positioning and strategic context. **WebSearch is not available in this environment.** I will not fabricate company intelligence, competitor positioning, or industry context. Those sections will be marked `[REQUIRES RESEARCH]` with instructions for you to fill them in or re-run this Skill in an environment with web access.

---

## Critical Information Gaps

To build a real close plan, I need the following. I've marked severity:

**Blocking (cannot build a credible close plan without these):**
1. **Deal size (ARR/TCV)** — Drives concession strategy, approval thresholds, and how much effort to invest.
2. **Target close date** — A "close plan" without a close date is just a wish list. What is driving the timing? Their fiscal year? A peak shipping season? A current contract expiring?
3. **Economic buyer** — Jordan Lee is an Operations Manager. Operations Managers rarely have signing authority for API/infrastructure spend. Who controls budget? CFO? COO? VP Ops?
4. **Compelling event** — Why now? Without this, the deal will slip.

**High-value (will materially change the strategy):**
5. **Competitors** — Are they evaluating Google Maps Platform, HERE, Mapbox, Routific, OptimoRoute, or building in-house? Each requires a different response.
6. **Technical evaluator** — Who on the engineering side will assess integration effort? This is critical given the stated objection.
7. **Champion strength** — Is Jordan actively selling internally, or just managing the eval?
8. **Decision process** — What steps remain? Security review? Procurement? Pilot?
9. **Their current state** — Manual routing? Spreadsheets? Incumbent vendor? In-house solution?

**Useful:**
10. Acme Logistics' size, fleet size, geography, and route volume — drives ROI math.
11. Tech stack — what they'd integrate with.
12. Budget cycle.

---

## Recommended Next Step Before Building the Full Playbook

Send Jordan a short post-demo email today with three goals:
1. Confirm next step and timeline.
2. Request a working session with their engineering lead to scope integration (this directly addresses the stated objection and reveals the technical evaluator).
3. Probe for the economic buyer and compelling event.

**Draft email:**

> Subject: Acme + [Your Co] — next steps after the demo
>
> Hi Jordan,
>
> Thanks again for the time on the demo. You mentioned integration effort as the biggest open question — that's the most important thing for us to de-risk together before going further.
>
> Two suggestions:
>
> 1. A 45-minute working session with whoever owns the systems the API would plug into. I'll bring a solutions engineer. The output will be a written integration estimate (hours, dependencies, risks) you can share internally.
> 2. A short call to align on what success looks like for Acme — what routing improvements would justify the investment, who else needs to weigh in on a decision, and what timeline you're working toward.
>
> Can we get both on the calendar in the next two weeks? Happy to send invites if you share the right people.

---

# Provisional Deal Playbook: Acme Logistics

Generated: [today]
Deal Owner: [UNKNOWN]
Deal Stage: Post-Demo (pre-evaluation)
Deal Size: **[UNKNOWN — BLOCKING]**
Target Close: **[UNKNOWN — BLOCKING]**
Confidence: **LOW** — insufficient qualification to assess

---

## 1. Company Intelligence

`[REQUIRES RESEARCH — WebSearch unavailable in this environment]`

To complete this section, gather:
- Acme Logistics' size, geography, fleet/route volume, business model (3PL? last-mile? freight?)
- Recent news: funding, expansion, leadership changes, operational incidents
- Strategic priorities signaled by hiring, press, or leadership statements
- Industry pressure points (fuel costs, driver shortages, ecommerce volume shifts, sustainability mandates)

Re-run this Skill in an environment with web access, or have the rep do a 30-minute research pass on LinkedIn, the company website, and recent press before the next call.

---

## 2. Buying Committee Map

### Known

**Jordan Lee**
- Title: Operations Manager
- Role in Deal: Likely Champion or User Buyer; **not yet confirmed as Economic Buyer** (unlikely given title)
- Disposition: Engaged enough to take a demo — treat as Neutral-to-Supportive until proven otherwise
- Key Concern: Integration effort
- Communication Style: [UNKNOWN]
- What They Care About: Probably operational efficiency, fewer escalations, route quality, driver satisfaction
- How to Win Them: Make integration look easy and de-risked; give them an internal narrative and ROI math they can carry up
- Risk If Ignored: They are currently the only thread — if they go quiet, the deal dies

### Critical Gaps in the Committee

| Role | Status | Action to Identify |
|---|---|---|
| Economic Buyer | **UNKNOWN — CRITICAL** | Ask Jordan: "Who else needs to weigh in on a decision of this size?" |
| Technical Evaluator | **UNKNOWN — CRITICAL** | Ask Jordan: "Who would own the integration on your side?" |
| Executive Sponsor | UNKNOWN | Ask Jordan: "Whose initiative does fixing routing fall under?" |
| Procurement/Legal | UNKNOWN | Surface after verbal interest |
| Blocker | UNKNOWN | Ask Jordan: "Anyone internally who's skeptical of changing the routing approach?" |
| Coach | UNKNOWN | Jordan may become this if cultivated |

### Multi-Threading Strategy

Currently **single-threaded** — this is the single largest risk on the deal. Priority order:
1. Get to the technical evaluator (uses the integration concern as the natural reason).
2. Get to the economic buyer (via Jordan, framed around ROI conversation).
3. Identify the executive sponsor (whose OKR does this serve?).

---

## 3. Deal Qualification (MEDDIC)

| Element | Status | Evidence | Gap |
|---|---|---|---|
| **Metrics** | UNKNOWN | None gathered | Need quantified pain: miles driven, on-time %, dispatcher hours, fuel spend |
| **Economic Buyer** | NOT IDENTIFIED | Jordan unlikely to be EB | Must identify before proposal |
| **Decision Criteria** | UNKNOWN | None shared | Ask explicitly on next call |
| **Decision Process** | UNKNOWN | None documented | Ask explicitly on next call |
| **Identify Pain** | PARTIAL | Demo happened, so some pain exists | Need to quantify business cost |
| **Champion** | UNCONFIRMED | Jordan engaged but unproven as advocate | Test by asking them to set up the next meeting |

### Overall Qualification: **WEAK**
### Velocity Risk Score: **6/10 factors present**

Factors checked:
- [x] No confirmed budget
- [x] Economic buyer not identified
- [x] Single-threaded
- [x] No compelling event
- [x] Procurement/legal timeline unknown
- [ ] Competitor incumbent advantage (unknown)
- [x] Champion may be too junior to influence decision
- [x] Technical requirements not validated
- [ ] No mutual close plan (expected at this stage — not yet a risk)
- [ ] Deal has not slipped (no prior date)

**Diagnosis: This deal is not yet qualified to close. It is qualified to advance.**

### Critical Gaps to Address (in order)
1. Identify the technical evaluator and run an integration scoping session.
2. Identify the economic buyer and what budget this would come from.
3. Quantify the business pain (route inefficiency → $ impact).
4. Surface a compelling event that creates a real close date.

---

## 4. Objection Playbook

### Known Objection

**OBJECTION:** "Integration effort may be too high."

**WHY THEY SAY THIS:**
Could be any of several things — and you need to find out which:
- They've been burned by a long API integration before
- Their engineering team is capacity-constrained
- They don't yet understand the integration scope (fear of the unknown)
- An internal stakeholder has already raised the concern
- It's a soft deflection covering a different objection (budget, authority, timing)

**RESPONSE FRAMEWORK:**

1. **Acknowledge:** "That's a fair concern — integration effort is one of the biggest reasons API projects stall, and we'd rather surface it now than after a contract."
2. **Reframe:** Move from abstract worry to concrete scope. The objection lives in vagueness; kill it with specificity.
3. **Evidence:** [REQUIRES INPUT — need a customer integration timeline you can cite, e.g., "Customer X integrated in Y weeks with Z engineering hours"]
4. **Confirm:** "If we could give you a written integration estimate from your own engineer, would that put this concern to rest, or is there something underneath it?"

**EXAMPLE RESPONSE:**

> "Totally fair — and honestly, 'integration effort' can mean very different things depending on what's under the hood. Some teams are worried about engineering hours, some about ongoing maintenance, some about disrupting an existing system. Before I tell you it'll be easy, I'd rather have our solutions engineer spend 45 minutes with whoever owns that system on your side. They'll produce a written estimate — hours, dependencies, risks. You can share it internally. If the estimate scares you, you've lost an hour. If it doesn't, you've taken the biggest unknown off the table. Worth doing?"

**IF THEY PUSH BACK:**
If they resist the scoping session, that's a signal. Either (a) the objection is a smokescreen for a different concern (probe gently: "Is integration the main thing, or is there something else also weighing on this?"), or (b) they don't have the political capital to pull in engineering — meaning Jordan may not be a real champion yet.

### Anticipated Objections (likely at this stage)

**Price/Budget** (when it surfaces): You don't yet know deal size, so you can't pre-build numerical responses. Prepare to anchor on ROI (routes optimized × cost per route) rather than list price.

**Status Quo** ("our current routing works fine"): Probe with: "What does 'fine' cost you per month in extra miles, overtime, or missed SLAs?" Make doing nothing visible and expensive.

**Authority** ("I need to check with my boss"): Welcome it. Use it to extract the EB's name: "Of course — would it help if I joined that conversation, or prepared a one-pager you could bring?"

**Build vs. Buy**: For a logistics company with engineering resources, this is the most likely silent objection. Pre-build a case: time-to-value, ongoing maintenance burden, algorithm sophistication, edge cases.

**Risk** ("what if it doesn't work on our routes?"): Propose a bounded pilot with success criteria defined upfront.

---

## 5. Competitive Positioning

`[REQUIRES RESEARCH — Competitors unknown and WebSearch unavailable]`

### Default: Compete Against Status Quo and Build-In-House

Until competitors are known, assume the real competition is **doing nothing** or **building in-house**. Both are likely for a logistics company.

**vs. Doing Nothing / Manual Routing:**
- Landmine question: "How many dispatcher-hours per week go into building and adjusting routes today?"
- Landmine question: "When a route falls apart mid-day, how long does it take to re-plan, and what does that cost?"
- Landmine question: "If you grew volume 30% next year, would your current routing process scale?"

**vs. Build In-House:**
- Landmine question: "If you built this internally, what would the team have to stop working on?"
- Landmine question: "How would you handle algorithm updates as constraints change — new vehicle types, new SLAs, new geographies?"
- Landmine question: "What's your tolerance for an 18-month build cycle before seeing route improvements?"

### Action Required
Ask Jordan directly on the next call: "Are you evaluating anything else, or comparing this to building something internally?" Then re-run this section with real competitor names.

---

## 6. Closing Strategy

Because the deal is post-demo and weakly qualified, the strategy is **advancement, not closing**.

### Recommended Approach: Advance to Evaluation with a Technical Win

1. **De-risk the stated objection first.** Run an integration scoping session. Output: a written estimate Jordan can circulate.
2. **Expand access.** Use the scoping session to meet the technical evaluator. Use the ROI conversation to meet the economic buyer.
3. **Quantify pain.** Build an ROI model with Acme's actual numbers (routes, miles, dispatcher hours, fuel spend). Without this, there's no business case.
4. **Propose a bounded pilot or POC.** Define: scope, duration, success metrics, what happens after success. This creates a natural path to commercial close.
5. **Discover the compelling event.** No event = no close date = no deal urgency.

### Next 3 Actions (This Week)
1. Send Jordan the email above (draft provided) to request the integration scoping session and ROI discovery call. **Owner: Rep. Due: within 24 hours of demo.**
2. Internal prep: pull together an integration estimate template and identify a similar-profile customer reference to cite. **Owner: Rep + SE. Due: before scoping session.**
3. Build a discovery question list for the ROI call focused on quantifying current routing cost. **Owner: Rep. Due: before ROI call.**

### Next 5 Actions (This Month)
4. Run the integration scoping session; produce written estimate.
5. Run the ROI discovery call; identify economic buyer.
6. Deliver a tailored ROI model to Jordan.
7. Get a meeting with the economic buyer (Jordan presents the ROI model with rep in the room).
8. Propose a bounded pilot with defined success criteria and a target commercial close date.

### Deal Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Single-threaded — Jordan goes silent | High | Deal dies | Multi-thread within 2 weeks via integration scoping session |
| No compelling event | High | Deal slips indefinitely | Find or co-create one during ROI discovery |
| Jordan is not the real champion | Medium | Deal stalls at EB | Test by asking them to organize the next meeting |
| Integration objection is a smokescreen | Medium | Wasted cycles on wrong concern | Probe directly for what's underneath |
| Build-in-house decision | Medium-High (logistics co.) | Lost deal | Pre-empt with TCO and time-to-value framing |

---

## 7. Mutual Close Plan

**Cannot be built yet.** A mutual close plan requires a target close date and a known decision process. Both are unknown.

**Substitute: Mutual Advancement Plan** — propose this to Jordan as the next-step framework:

| Date | Milestone | Owner | Status |
|---|---|---|---|
| [Week 1] | Integration scoping session with Acme engineering | Jordan + Rep | Pending |
| [Week 2] | Written integration estimate delivered | Rep / SE | Pending |
| [Week 2] | ROI discovery call (current routing cost) | Jordan + Rep | Pending |
| [Week 3] | Tailored ROI model delivered | Rep | Pending |
| [Week 4] | Meeting with economic buyer | Jordan | Pending |
| [Week 5] | Pilot proposal with success criteria | Rep | Pending |
| [Week 6] | Pilot decision / commercial timeline agreed | Acme | Pending |

**AGREED NEXT STEP:** Schedule the integration scoping session within 7 days of the demo.

---

## 8. Proposal Talking Points

**Premature.** Proposal talking points should be built once the ROI model is grounded in Acme's actual numbers and the economic buyer is identified. Drafting them now would be guessing.

Revisit this section after the ROI discovery call.

---

## 9. Negotiation Strategy

**Premature.** Cannot define ideal/acceptable/walk-away terms without knowing deal size, competitive context, or buyer priorities.

Revisit after pilot proposal stage.

---

## 10. Post-Close Plan

**Premature for full build, but useful preview:**

When you propose a pilot, sketch a high-level "what the first 90 days look like" picture for Jordan to share internally. This makes the purchase feel safe and concrete. Include: integration timeline, first measurable route improvements, check-in cadence, and success-metric review.

---

## Summary for the Rep

**The honest read:** You have a demo and a single contact. That's a lead in motion, not a deal to close. Trying to "make a close plan" right now would mean writing fiction. The right move is a focused two-week sprint to:

1. Convert the integration objection into a scoping session (kills the objection, surfaces the technical evaluator).
2. Run an ROI discovery call (quantifies pain, surfaces the economic buyer).
3. Get a real close date anchored to a real compelling event.

Do that, and in 3 weeks you'll have the inputs to build an actual close plan. Re-run this Skill then — ideally in an environment with web access so the company intelligence and competitive sections can be properly built.
