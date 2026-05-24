I have enough deal facts to build a useful internal playbook, but several items are `[UNKNOWN]` and I'll mark them honestly rather than invent them. Per skill rules, I will not fabricate company research — I have no verified information about "ACME Manufacturing" (a generic name) and will flag the research section as a gap with specific actions to fill it, rather than running speculative WebSearches that produce false intelligence.

Writing the playbook now to `deal-playbook.md`.

---

# Deal Playbook: ACME Manufacturing

Generated: [TODAY]
Deal Owner: [UNKNOWN — rep to fill in]
Deal Stage: Expansion (assumed Evaluation/Proposal — confirm)
Deal Size: $80,000 ARR (expansion)
Target Close: End of current quarter
Confidence: **MEDIUM-LOW** — single-threaded to VP Ops, active IT security blocker, no confirmed compelling event tied to quarter-end

---

## 1. Company Intelligence

**GAP — NOT RESEARCHED.** "ACME Manufacturing" was supplied as a synthetic/generic name. I did not run WebSearch because any result would not reliably map to the actual customer. Before the next customer-facing meeting, fill in:

- Company size, locations, product lines
- Recent news (last 90 days): earnings, layoffs, leadership changes, M&A
- Strategic initiatives (digital transformation, ERP migrations, lean/Six Sigma programs)
- Hiring signals (Ops, IT Security, Data/Analytics roles)
- Existing tech stack and integrations
- Since this is an **expansion**, pull internal data first: current usage, adoption by team, support tickets, NPS, QBR notes, existing contract terms and renewal date.

**Action:** Rep to populate this section from CRM + internal CSM notes within 24 hours. This is the single biggest gap in the playbook.

---

## 2. Buying Committee Map

### Known
**Name:** [UNKNOWN]
**Title:** VP Operations
**Role in Deal:** Primary contact; likely Economic Buyer for an $80k expansion in an Ops-owned tool, but confirm
**Disposition:** Supportive (assumed — they are taking the meeting and entertaining expansion)
**Key Concern:** Operational outcomes — throughput, error rate, visibility across the workflow currently in spreadsheets
**Communication Style:** [UNKNOWN]
**What They Care About:** Replacing manual spreadsheet workflow with something defensible; not getting blocked by IT
**How to Win Them:** Quantified ROI vs. spreadsheet status quo + a clean path through IT security
**Risk If Ignored:** N/A — already engaged

### Known Blocker
**Name:** [UNKNOWN]
**Title:** [UNKNOWN — IT Security lead / CISO / Security Architect]
**Role in Deal:** Security/Procurement gatekeeper
**Disposition:** Skeptical (assumed by default for security reviewers; treat as neutral-skeptical until proven otherwise)
**Key Concern:** Data handling, access controls, SOC 2 / ISO posture, integration risk, vendor risk management
**How to Win Them:** Proactive security packet, direct technical conversation, references from peers in manufacturing
**Risk If Ignored:** **This is the deal killer.** Security review timelines in manufacturing routinely run 4–8 weeks. If not started immediately, quarter-end close is unrealistic.

### Stakeholder Gaps (Must Identify This Week)
- **Economic Buyer confirmation** — Does VP Ops have $80k signing authority, or does this route to CFO/COO?
- **Technical Evaluator inside Ops** — Who actually uses the tool and validates fit?
- **Champion verification** — Is VP Ops a true champion (will sell internally) or just a supportive contact?
- **Procurement** — Vendor onboarding process, MSA on file from initial deal?
- **End users** — Who runs the spreadsheets today? Their buy-in matters for expansion adoption.

### Relationship Strength Assessment
| Stakeholder | Access | Disposition | Next Action |
|---|---|---|---|
| VP Operations | Direct | Supportive | Confirm budget authority + ask for intro to IT Security |
| IT Security lead | None | Skeptical (assumed) | Get warm intro this week; send security packet |
| End users (Ops team) | None | Unknown | Request a working session to see current spreadsheet workflow |
| Procurement | None | Unknown | Confirm whether existing MSA covers expansion |

### Multi-Threading Strategy
1. **This week:** Ask VP Ops directly: "Who in IT Security will own the review, and can you make the intro this week so we don't lose quarter-end?"
2. **This week:** Ask for a 30-min session with 1–2 end users to document current spreadsheet pain (also builds champions).
3. **Next week:** If procurement involvement is required, get that thread opened in parallel, not in series.

---

## 3. Deal Qualification (MEDDIC)

| Element | Status | Evidence | Gap |
|---|---|---|---|
| **Metrics** | WEAK | None supplied | No quantified pain from spreadsheet workflow yet — need error rate, hours/week, rework cost |
| **Economic Buyer** | MODERATE | VP Ops engaged | Authority for $80k not confirmed |
| **Decision Criteria** | UNKNOWN | None supplied | Need explicit criteria — especially security requirements |
| **Decision Process** | WEAK | Security review identified | Full path to signature, procurement steps, signature authority all unclear |
| **Identify Pain** | MODERATE | Spreadsheet workflow implied as inadequate | Pain not quantified or tied to a business event |
| **Champion** | UNKNOWN | VP Ops is supportive | Has VP Ops sold internally on our behalf yet? Unverified |

**Overall Qualification: WEAK-to-MODERATE.** Enough to work, not enough to forecast commit.

### Velocity Risk Factors
- [x] No confirmed budget allocation for the expansion amount
- [ ] Economic buyer not identified (VP Ops is likely but unconfirmed)
- [x] Single-threaded (only VP Ops engaged)
- [x] No compelling event driving quarter-end urgency (quarter-end is *our* deadline, not theirs)
- [x] Procurement/legal/security timeline unknown — **and security is already flagged as a blocker**
- [x] Competitor has incumbent advantage (status quo spreadsheet is "free" and embedded)
- [ ] Champion too junior (VP Ops is senior enough — if they truly champion)
- [x] Technical requirements not validated
- [x] No mutual close plan in place
- [ ] Deal has not slipped from a previous close date (assumed)

**Score: 6/10 — HIGH velocity risk.** This deal is unlikely to close this quarter without immediate intervention on (a) security and (b) compelling event.

### Critical Gaps to Address (Ordered)
1. **Open IT security review NOW** — it is the longest pole in the tent.
2. **Manufacture or surface a compelling event** — why this quarter and not next?
3. **Quantify the cost of spreadsheets** — turn "spreadsheets are bad" into dollars.
4. **Confirm signing authority** — do not assume VP Ops can sign $80k unilaterally.
5. **Multi-thread to at least one end user and one IT contact.**

---

## 4. Objection Playbook

### Anticipated: "IT Security has concerns about the platform."
**Why they say this:** Security teams are measured on risk reduction, not deal velocity. Default posture is "no" or "slow."
**Response:**
1. Acknowledge: "Totally fair — a thorough security review is exactly what I'd want if I were in their seat."
2. Reframe: "Most of our manufacturing customers have run us through the same review. Let me get them what they need on day one rather than playing email tag for three weeks."
3. Evidence: Send SOC 2 report, pen test summary, standard security questionnaire pre-filled, list of similar manufacturing customers who passed review.
4. Confirm: "If I send the full packet by [date], can we get a 30-minute call with your security lead this week to walk through it?"

**Example:** "Security reviews tend to expand to fill the time available. The best thing we can do is get your security lead everything they need up front and offer a live walkthrough. I'll send the packet today — can you make the intro by Wednesday?"

**If they push back:** Offer to have our Head of Security or a Solutions Engineer join a call directly with their security team. Removes the rep as a translation layer.

### Anticipated: "We've always just used spreadsheets — what's the real ROI?"
**Why they say this:** Status quo bias + sunk cost in existing process. Real question: "Justify the $80k."
**Response:**
1. Acknowledge: "Spreadsheets work — until they don't. The question isn't whether they function, it's what they cost you that you're not measuring."
2. Reframe: Get specific. Hours per week spent maintaining sheets, version-control errors, delayed reporting to leadership, audit risk.
3. Evidence: Walk through ROI model using *their* numbers gathered in discovery.
4. Confirm: "Does that math line up with what you're seeing on your team?"

**If they push back:** Offer a 30-day side-by-side with one team. Define success metrics up front.

### Anticipated: "Can we revisit next quarter?"
**Why they say this:** No urgency, or budget pressure, or competing priorities.
**Response:** Do not push back hard. Ask: "What changes between now and next quarter that makes this easier?" If the answer is vague, the deal was never closing this quarter and you need to know that now. If the answer is concrete (budget cycle, headcount, etc.), build the close plan around it honestly.

### Anticipated: "$80k is a lot for an expansion."
**Response:** Anchor to value, not price. "$80k against [X hours/week × loaded labor cost × 52 weeks] is a [Y]-month payback. The question is whether we're confident in those numbers — let's pressure-test them together."

### Known Objection: [None explicitly raised yet]
**Action:** In the next call, ask directly: "What concerns do you have that we haven't talked about?" Surface objections early — unspoken objections kill deals at the finish line.

---

## 5. Competitive Positioning

### Competitor: Incumbent Spreadsheet Workflow (Status Quo)

**Their pitch (internal advocates for spreadsheets will say):**
- "It's free."
- "Everyone already knows how to use it."
- "We can change it whenever we want."
- "No security review needed."

**Where they win:**
- Zero procurement friction
- Zero training cost (perceived)
- Total flexibility for power users
- No vendor risk
- Familiar to leadership

**Be honest — these are real advantages.** Do not dismiss them.

**Where we win:**
- Data integrity and version control (no more "final_v7_USE_THIS.xlsx")
- Auditability and traceability for compliance
- Real-time visibility across the Ops team, not one person's laptop
- Scales without linear human effort
- Reporting that doesn't require a person assembling it

### Landmine Questions (Ask VP Ops)
1. "When the person who maintains the master spreadsheet is out, what happens to the workflow?"
2. "How long does it take to produce the weekly/monthly Ops report leadership asks for? How much of that is manual assembly?"
3. "If you got audited tomorrow on [specific compliance area], could you trace how a number was calculated three months ago?"
4. "How many times in the last quarter did a spreadsheet error require rework or a corrected report?"
5. "If your team grew 50% next year, would the spreadsheet workflow scale, or would you need to hire someone to maintain it?"

These let VP Ops articulate the cost of the status quo themselves. Do not answer for them.

### If the Prospect Stays with Spreadsheets
- Do not bash spreadsheets. They are not wrong to value them.
- Offer a narrower-scope expansion: cover the highest-pain workflow first, prove ROI, expand later.
- Walk-away is fine — losing to "no decision" is more common than losing to a competitor and usually fixable next cycle.

### Trap to Avoid
Telling VP Ops "spreadsheets are not a real system." They built the spreadsheet workflow. You are insulting their work. Position the spreadsheet as a *successful first version* that has outgrown itself.

### Competitive Landscape Summary
| Competitor | Threat | Their Advantage | Our Advantage | Strategy |
|---|---|---|---|---|
| Spreadsheet status quo | HIGH | Free, familiar, no IT review | Scale, audit, real-time | Quantify hidden cost; let buyer self-discover |

---

## 6. Closing Strategy

Deal is in evaluation/proposal territory with a security blocker. Strategy: **build consensus while removing security risk in parallel.**

### Next 3 Actions (This Week)
1. **By Wednesday:** Email VP Ops requesting (a) intro to IT Security lead, (b) confirmation of signing authority for $80k, (c) 30 minutes with 1–2 end users. Owner: Rep.
2. **By Thursday:** Send pre-filled security packet (SOC 2, questionnaire, pen test summary, manufacturing customer reference list) to VP Ops to forward to IT Security. Owner: Rep + Solutions/Security.
3. **By Friday:** Draft and send the Mutual Close Plan (Section 7) to VP Ops for review. Frame as "let's make sure we both know what has to happen to hit your timeline."

### Next 5 Actions (This Month)
4. Run live security walkthrough with IT Security lead.
5. Complete end-user discovery session; build quantified ROI model with their numbers.
6. Deliver ROI model + proposal to VP Ops with a clear ask and date.
7. Confirm procurement path and any MSA amendment language needed.
8. Final objection sweep call: "Is there anything we haven't addressed that would keep this from closing by [date]?"

### Deal Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Security review extends past quarter-end | HIGH | Deal slips | Start review this week; offer live walkthrough |
| No real compelling event for Q-end | HIGH | Deal slips | Ask VP Ops what *their* deadline is; align to that, not ours |
| VP Ops lacks signing authority | MED | Adds approval step | Confirm this week; if no, get to actual EB |
| End users resist replacing spreadsheets | MED | Adoption + internal pushback | Engage them now as co-designers, not recipients |
| Status quo wins ("revisit next quarter") | MED | Deal stalls | Quantify cost of waiting; offer narrow-scope start |

---

## 7. Mutual Close Plan

**MUTUAL CLOSE PLAN: ACME Manufacturing × [Your Company]**

Target Close Date: [Last business day of current quarter]
Target Go-Live Date: [+30 days from signature]

| Date | Milestone | Owner | Status |
|---|---|---|---|
| Week 1 | Intro to IT Security; security packet sent | VP Ops + Rep | Pending |
| Week 1 | End-user discovery session | Rep + Ops team | Pending |
| Week 1 | Mutual close plan agreed | Both | Pending |
| Week 2 | Security questionnaire returned + walkthrough call | IT Security + Rep | Pending |
| Week 2 | ROI model delivered to VP Ops | Rep | Pending |
| Week 3 | Proposal delivered | Rep | Pending |
| Week 3 | Procurement/MSA path confirmed | VP Ops + Procurement | Pending |
| Week 4 | Security approval secured | IT Security | Pending |
| Week 4 | Final terms agreed | Both | Pending |
| Week 5 | Contract signed | Economic Buyer | Pending |
| Week 6 | Kickoff | Both | Pending |

**AGREED NEXT STEP:** VP Ops introduces Rep to IT Security lead by end of this week so the security review starts immediately.

---

## 8. Proposal Talking Points

**OPENING (30 sec):**
"When we last talked, you described [specific Ops pain — fill in]. Today I want to show you exactly what it would look like to move that workflow off spreadsheets this quarter, and how we get through IT security cleanly."

**VALUE PROPOSITION (2 min):**
1. **Eliminate manual spreadsheet assembly** → [X hours/week recovered] → [translate to dollars or headcount]
2. **Auditable, real-time visibility for leadership** → faster reporting cycle, fewer "where did this number come from?" conversations
3. **Scales without linear hiring** → as Ops grows, the tool absorbs it instead of needing another analyst

*All three figures must be populated from the discovery session — do not present generic numbers.*

**PROOF (1 min):**
"[Manufacturing reference customer] ran the same workflow in spreadsheets. After expanding with us, they reduced [specific metric] by [X%] in [Y months] and passed their next audit without manual prep." *Replace with a real reference customer the CSM team can confirm.*

**DIFFERENTIATION (1 min):**
"The honest comparison here isn't us versus another vendor — it's us versus the spreadsheet workflow your team built, which has served you well. The question is whether that workflow scales with where Ops is going in the next 12 months. We've already proven we work in your environment — this is about expanding that to the part of the workflow that hurts the most."

**THE ASK (30 sec):**
"To go live by [date], we'd need contract signed by [date], which means security review wrapped by [date]. I'd like to propose we move forward at $80k for [scope]. Can we agree to the close plan I sent so both teams know what has to happen?"

**IF THEY HESITATE:**
"Got it. What's the one thing standing between today and you feeling confident about moving forward? Let's name it."

---

## 9. Negotiation Strategy

### Our Position
- **Ideal:** $80k ARR, multi-year (2–3 yr) with modest annual uplift, standard payment terms, signature this quarter
- **Acceptable:** $80k ARR, 1-year, standard terms, signature this quarter
- **Walk-away:** Sub-$60k or open-ended security review with no committed close date — better to push to next quarter cleanly than chase

### Concession Strategy (Every Concession Is a Trade)
| If They Ask For | We Can Offer | In Exchange For |
|---|---|---|
| Discount | Up to [X%] off — confirm with management | Multi-year commitment OR signed case study OR reference call |
| Extended payment terms | Net 45–60 | Signature this quarter OR larger scope |
| Phased rollout | Start with highest-pain workflow | Commitment to expand by [date] |
| Free onboarding hours | Bundle [N] hours | Multi-year OR reference |

### Red Lines (Do Not Concede)
- Indefinite security review with no committed timeline — this is how deals die quietly
- Discount without a corresponding trade — sets a renewal precedent
- Custom security/legal terms outside standard MSA without legal review
- "Pilot" with no defined success criteria or commitment to expand

---

## 10. Post-Close Plan

### Implementation Timeline (Share with Prospect)
- Week 1 post-signature: Kickoff, success criteria documented
- Weeks 2–3: Configuration + data migration from existing spreadsheets
- Week 4: User training, parallel run with spreadsheet workflow
- Week 5+: Cutover, first reporting cycle on new system

### Success Metrics (Agree with VP Ops Pre-Close)
- [Hours/week saved on Ops reporting] — target [X]
- [Error/rework incidents] — target reduction of [Y%]
- [Time to produce monthly leadership report] — target [Z]

### First 90 Days
- 30-day check-in with VP Ops and end users
- 60-day adoption review with CSM
- 90-day business review with VP Ops, with measured results against agreed metrics — sets up the next expansion conversation

---

## Appendix: Research Sources

**None used.** Company research was not performed because "ACME Manufacturing" is a generic placeholder and any WebSearch result would not reliably correspond to the actual customer. Rep should populate Section 1 from internal CRM, CSM notes, and verified public sources before the next customer meeting.

---

## Skill Boundary Note

Two things this playbook deliberately does not do:

1. **Fabricate company intelligence.** The skill explicitly instructs "Do not manufacture information." With a generic company name and no real-world anchor, doing research would produce plausible-looking but unreliable output. Flagged as a gap with clear ownership instead.
2. **Forecast confidence as HIGH.** Based on the supplied facts — single-threaded, active security blocker, no compelling event tied to quarter-end, no quantified pain — an honest read is MEDIUM-LOW confidence on quarter-end close. The skill's behavioral rule #1 is to be honest about deal risk.

File written to: `deal-playbook.md`
