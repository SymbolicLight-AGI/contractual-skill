# Deal Closer Playbook — Acme Logistics

Before I can produce a credible, tactical playbook, I need to flag what's missing and what I can still deliver right now. I'm going to be direct with you because a playbook built on guesses is worse than no playbook at all.

---

## Information Gaps (Required Before Full Playbook)

The following are **required** inputs I do not have. Please provide them so I can finalize the playbook:

1. **Deal size (ARR/TCV)** — `[UNKNOWN]`. Without this, I cannot size the negotiation strategy, concession ladder, or determine whether this deal warrants executive sponsorship on your side.
2. **Target close date** — `[UNKNOWN]`. Without this, there is no mutual close plan to build backward from, and no way to assess velocity risk.
3. **Pricing model** for the route optimization API (per-call, per-vehicle, per-route, flat platform fee, tiered?) — needed to anticipate procurement and budget objections.

## Highly Valuable Gaps

4. **Economic buyer** — Jordan Lee is an Operations Manager. That title rarely owns budget for an API purchase at a logistics company. Who signs?
5. **Technical evaluator** — Critical given the stated integration objection. Likely an Engineering Lead, VP Engineering, or Head of Platform.
6. **Champion strength** — Is Jordan actively selling internally, or just evaluating?
7. **Competitors** — `[UNKNOWN]`. At minimum, you are competing against status quo (current routing system or manual dispatch) and likely against in-house build.
8. **Compelling event** — What is driving urgency? Peak season? A failed routing system? A new contract win that exceeds current capacity?

## Skill Boundary

The Skill instructs me to use WebSearch to research the target company (recent news, leadership, hiring signals, tech stack). **WebSearch is unavailable in this environment**, so I cannot produce the "Company Intelligence" section with current, verified information. I will not fabricate it.

**Correct next step**: Either (a) provide a brief on Acme Logistics yourself (size, locations, fleet type, current tech stack, recent news), or (b) re-run this in an environment with WebSearch enabled.

---

## What I Can Deliver Now

Given Demo-completed stage, an Operations Manager contact, and an integration objection, here is a **provisional advancement playbook** (not a close plan — it is too early in the deal for that). I'll write the partial playbook to `deal-playbook.md` and call out every `[UNKNOWN]` clearly.

---

## Provisional Playbook: Acme Logistics

### Honest Deal Assessment

- **Stage reality check**: You said "make a close plan," but this deal is post-demo with a single mid-level contact, no identified economic buyer, no close date, no deal size, and an unresolved technical objection. **This is not a closing deal — it is an advancement deal.** Treating it as a close-ready opportunity will cause you to skip the qualification work that actually moves it forward.
- **Velocity risk score**: At minimum 6 of 10 risk factors present (no confirmed budget, EB not identified, single-threaded, no compelling event documented, procurement timeline unknown, technical requirements not validated). **High velocity risk.**
- **MEDDIC qualification**: **WEAK**. You have a contact and a demo. You do not yet have Metrics, Economic Buyer, Decision Criteria, Decision Process, identified Pain (beyond a generic interest), or a confirmed Champion.

### The Single Most Important Next Action

**Book a 30-minute follow-up with Jordan Lee within 5 business days with this agenda:**

1. Validate the integration concern in technical detail (what systems, what data flow, what their engineering capacity looks like).
2. Ask Jordan to bring or introduce the engineering lead who would own integration.
3. Discover the business driver: "What changed in the last 6 months that put route optimization on your priority list?"
4. Surface budget and timeline: "If we proved the integration was straightforward, what would the path to a decision look like on your side?"

### Integration Objection — Response Framework

**OBJECTION**: "Integration effort may be too high."

**WHY THEY SAY THIS** (root cause hypotheses — confirm which is real):
- Engineering team is under-resourced and protective of their roadmap.
- They have been burned by a previous API integration that took longer than promised.
- Jordan does not have the technical depth to assess effort and is hedging.
- A competitor or in-house option appears lower-friction.

**RESPONSE**:
1. **Acknowledge**: "That is the right thing to be cautious about — a routing API that takes six months to integrate is not actually saving you anything."
2. **Reframe**: "Integration effort is really two questions: how much engineering time on day one, and how much ongoing maintenance. Can we walk through both with whoever owns your dispatch or TMS platform?"
3. **Evidence**: [Insert your shortest-time-to-integration customer story with a comparable stack — `[UNKNOWN - rep to supply]`]
4. **Confirm**: "If we could show you a 2-week integration path with a reference customer who looks like you, would that change how you are thinking about this?"

**Fallback**: Offer a **scoped technical discovery session** with your solutions engineer and their engineering lead. This converts an objection into a multi-threading opportunity.

### Competitive Positioning — Status Quo (the only competitor I can name without research)

**COMPETITOR**: Their current routing approach (manual, spreadsheet-based, or legacy TMS module).

**Where status quo wins**: Zero integration cost. Familiar. No vendor risk.

**Where you win**: [Rep to insert specific differentiators — route quality, fuel savings %, driver-hour reduction, API flexibility]. **Quantify it.** "X% reduction in miles driven" beats "better optimization."

**Landmine questions to ask Jordan**:
1. "How are you measuring route quality today, and how confident is the team in those numbers?"
2. "When fuel prices moved 15% last year, how quickly were you able to re-optimize your network?"
3. "If a dispatcher is out sick, how does routing get done that day?"

### Multi-Threading Plan

Jordan alone cannot close this. Within the next two meetings, you need to reach:

| Role | Target Title at Acme | Why |
|---|---|---|
| Economic Buyer | VP Operations, COO, or CFO | Owns budget for ops tooling |
| Technical Evaluator | Eng Lead / VP Engineering / Head of Platform | Owns the integration objection |
| Executive Sponsor | COO or CEO (if Acme is small) | Connects this to a strategic priority |

**How to ask Jordan**: "To make sure we are not wasting your time, who else on your side would need to weigh in before this becomes a real decision? I want to make sure we bring the right expertise to the next conversation."

### What I Am NOT Writing Yet (and Why)

- **Mutual close plan**: Cannot build without a target close date and identified signers.
- **Negotiation strategy / concession ladder**: Cannot build without deal size or pricing model.
- **Full competitive positioning**: Cannot build without knowing actual competitors or completing company research.
- **Company intelligence section**: Requires WebSearch, which is unavailable.
- **Proposal talking points**: Premature — you have not yet validated the business pain or quantified value.

---

## File Output

I am writing this provisional playbook to `deal-playbook.md` now, with every gap clearly marked `[UNKNOWN]` so you can fill them in and re-run.

```
Writing: ./deal-playbook.md
Status: PROVISIONAL — advancement playbook, not close plan
Blocking gaps: deal size, close date, economic buyer, competitors, company research
```

**Please send me**: deal size estimate, target close date, what you know about Acme's size and current routing setup, and the names of anyone besides Jordan you've interacted with. With that, I can produce a full playbook.
