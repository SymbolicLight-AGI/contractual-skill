I have enough facts to build a useful internal playbook, but several inputs the Skill flags as "Required" or "Highly Valuable" are missing. I'll mark those as `[UNKNOWN]` and build around them rather than fabricate. Per the Skill, I am also skipping WebSearch external research on ACME Manufacturing because the task says "synthetic deal facts" — researching a real company against synthetic facts would manufacture information. I'll note this as a gap.

Writing to `deal-playbook.md`:

---

# Deal Playbook: ACME Manufacturing

Generated: 2025
Deal Owner: `[UNKNOWN]`
Deal Stage: `[UNKNOWN]` — inferred late-stage (Evaluation → Negotiation) based on identified blocker being security review
Deal Size: $80,000 ARR (expansion)
Target Close: End of current quarter
Confidence: **MEDIUM-LOW** — significant qualification gaps; security review is an unowned risk

> **Note on research**: Facts are labeled synthetic. No WebSearch performed — any "company intelligence" generated from a real ACME Manufacturing would be misattributed to a synthetic deal. The rep should run the research pass against the real account before using sections marked `[RESEARCH REQUIRED]`.

---

## 1. Company Intelligence

### Company Overview
`[RESEARCH REQUIRED]` — Run: company size, sites, ERP/MES stack, recent M&A, ops leadership tenure.

### Recent Developments
`[RESEARCH REQUIRED]` — Last 90 days news, earnings (if public), plant expansions, layoffs, automation initiatives.

### Strategic Context (inferred from facts)
- Buyer is **VP Operations** — purchase serves an operational efficiency or throughput agenda, not an IT modernization agenda.
- Current state is **spreadsheets** — implies manual processes, version-control pain, and likely no incumbent SaaS vendor to displace contractually.
- This is an **expansion**, so we have a footprint, a usage history, and presumably an existing MSA. That should compress legal but not security review for a new scope.

### Key Business Priorities (hypothesis to validate)
- Reduce manual ops work / errors
- Scale a process that is breaking at current volume
- Standardize across sites or teams

---

## 2. Buying Committee Map

### Identified

**VP Operations** — Primary Contact / Likely Economic Buyer
- Name: `[UNKNOWN]`
- Role: Primary contact, probable economic buyer for an $80k ops expansion
- Disposition: **Supportive** (engaging in expansion conversation)
- Key Concern: Operational outcomes — throughput, error rate, headcount leverage
- Communication Style: `[UNKNOWN]` — likely Direct/Outcomes-driven for an Ops VP
- What They Care About: Time-to-value, minimal disruption, measurable savings
- How to Win Them: Quantified ROI tied to a specific ops metric; reference from a similar manufacturer
- Risk If Ignored: None — this is our anchor

**IT Security Reviewer** — Blocker
- Name: `[UNKNOWN]`
- Role: Gatekeeper — must clear vendor before contract
- Disposition: **Skeptical → Neutral** (assume process-driven, not personally opposed)
- Key Concern: Data handling, OT/IT segmentation (manufacturing-specific), SSO, SOC 2, data residency, third-party risk
- Communication Style: Analytical, checklist-driven
- What They Care About: Closing tickets, defensible audit trail, no exceptions to policy
- How to Win Them: Get ahead of their questionnaire; provide SOC 2 / pen test / DPA preemptively; offer a 30-min call to walk the architecture
- Risk If Ignored: **Deal slips the quarter.** This is the #1 velocity risk.

### Missing — Discovery Gaps

| Role | Status | Action to Identify |
|---|---|---|
| Champion | `[UNKNOWN]` — VP Ops may be both buyer and champion, which is a single-thread risk | Ask VP Ops: "Who else on your team will use this most? I'd love to make sure they're set up to succeed." |
| Technical Evaluator | `[UNKNOWN]` | Ask: "Who on your side will own the integration / data flow?" |
| User Buyer | `[UNKNOWN]` — ops analysts / plant managers currently in the spreadsheet | Request a working session with 2 daily users |
| Coach | `[UNKNOWN]` | Identify a friendly user from existing footprint who can tell us the real internal dynamics |
| Procurement/Legal | `[UNKNOWN]` — expansion may ride existing MSA | Confirm whether new SOW only or full re-paper |
| Executive Sponsor | `[UNKNOWN]` — VP Ops' boss (COO?) | Ask VP Ops who reviews ops investments above $X |

### Multi-Threading Strategy
1. **This week**: Get IT Security contact name and email directly from VP Ops. Frame: "To protect your timeline, I'd like to open a parallel track with your security team now."
2. **This week**: Request a 30-min working session with 1–2 end users — establishes user buyer, surfaces objections we haven't heard.
3. **Next week**: Ask VP Ops to confirm whether expansion needs sponsor sign-off above her authority. If yes, request a brief exec-to-exec call.

---

## 3. Deal Qualification (MEDDIC)

| Element | Status | Evidence | Gap |
|---|---|---|---|
| **Metrics** | WEAK | None provided | No quantified pain or target outcome on file |
| **Economic Buyer** | MODERATE | VP Ops likely has authority for $80k ops spend | Not confirmed; expansion may still route to COO/CFO |
| **Decision Criteria** | WEAK | None provided | Unknown what "success" looks like vs. spreadsheet |
| **Decision Process** | WEAK | Security review identified | Steps after security unclear; signature path unknown |
| **Identify Pain** | MODERATE | Spreadsheet workflow implies known pain | Pain not quantified in $ or hours |
| **Champion** | WEAK | VP Ops engaged but not confirmed as champion | No evidence she is selling internally on our behalf |

**Overall Qualification: WEAK-to-MODERATE**

### Velocity Risk Score: 6/10

- [x] No confirmed budget or budget not allocated
- [x] Economic buyer not identified or not engaged (not *confirmed*)
- [x] Single-threaded (only one contact)
- [ ] No compelling event or deadline driving urgency — quarter end is *our* event, not theirs
- [x] Procurement or legal review timeline unknown
- [x] Competitor has an incumbent advantage (spreadsheets = entrenched habit + zero switching cost)
- [ ] Champion too junior — VP is senior enough
- [x] Technical requirements not validated (security)
- [x] No mutual close plan or agreed next steps
- [ ] Deal has slipped from a previous close date — unknown

**6/10 = HIGH velocity risk.** This deal will not close this quarter without intervention on three fronts: security, multi-threading, and a quantified pain case.

### Critical Gaps — Ordered
1. **Security review unowned** — fix this week
2. **Single-threaded on VP Ops** — engage user + IT in parallel
3. **No quantified pain vs. spreadsheet** — without it, "do nothing" wins
4. **No buyer-side compelling event** — must surface a real business trigger (audit, new site, headcount freeze, growth plan)

---

## 4. Objection Playbook

### Anticipated — Security/IT

**OBJECTION**: "Security review will take 6–8 weeks; we can't commit to a Q-end close."

WHY THEY SAY THIS: Security is queue-driven and not motivated by the sales timeline.
RESPONSE FRAMEWORK:
1. Acknowledge: "That's a fair timeline for net-new vendors."
2. Reframe: "We're already an approved vendor for [existing scope] — this is a scope expansion, not a new vendor onboarding."
3. Evidence: Provide existing security packet, prior approval reference, SOC 2.
4. Confirm: "If we can document this as a scope extension, can your team confirm a faster path?"

EXAMPLE RESPONSE: "Since we're already deployed at ACME, I'd like to ask your security team whether this counts as a scope extension under our existing approval. If so, we can likely compress the review. Can you introduce me to the reviewer this week so I can ask them directly?"

IF THEY PUSH BACK: Offer a conditional order form with a security-contingency clause — signature dependent on security clearance by date X.

---

**OBJECTION**: "Spreadsheets work fine — why change now?" (Status Quo / Incumbent)

WHY THEY SAY THIS: Switching cost is real; spreadsheet pain is normalized.
RESPONSE FRAMEWORK:
1. Acknowledge: "Spreadsheets got you here — that's not nothing."
2. Reframe: "The question isn't whether they work today. It's what they cost you at next year's volume."
3. Evidence: Quantify — error rate, hours/week on manual reconciliation, version-control incidents.
4. Confirm: "If that number is X, does the math work?"

EXAMPLE RESPONSE: "Most ops teams I work with don't realize what the spreadsheet actually costs until we count it. Can we spend 15 minutes mapping the hours your team spends on [reconciliation / consolidation / error correction] each week? If the number is small, you should keep the spreadsheet. If it's not, you have a budget case."

---

**OBJECTION**: "$80k is a lot for something we're doing today for free."

WHY THEY SAY THIS: They're comparing license cost to spreadsheet cost ($0), not to total cost of the spreadsheet (labor + error + risk).
RESPONSE: Reframe as cost-per-hour-saved or cost-per-error-avoided. Tie to a specific FTE equivalent.

---

**OBJECTION**: "Can we revisit next quarter?"

WHY THEY SAY THIS: No internal compelling event.
RESPONSE: Do not push back with artificial urgency. Ask: "What changes next quarter that makes this easier?" If the honest answer is "nothing," the deal is not actually qualified for this quarter and we should re-baseline rather than discount to force it.

### Anticipated — Standard

- **Authority**: "I need to check with my boss" → "Happy to join that conversation — what does she need to see?"
- **Risk**: "What if rollout disrupts the floor?" → Phased rollout plan, existing-customer reference.
- **Resources**: "We don't have bandwidth to implement" → Offer guided onboarding, define a 4-hour-per-week max ask from their side.

---

## 5. Competitive Positioning

### Competitor: Status Quo (Spreadsheet Workflow)

**Their Pitch**: "It's free, everyone knows how to use it, and it already works."

**Where They Win**:
- Zero license cost
- Zero training
- Zero security review
- Full flexibility — users can change anything
- No vendor dependency

**Where We Win** (must be validated against the actual product):
- Single source of truth — no version conflicts
- Auditability and change history
- Scales without breaking when volume or users grow
- Reduces manual reconciliation labor
- Reduces error rate

**Landmine Questions** (ask VP Ops):
1. "How many hours per week does your team spend reconciling versions of the spreadsheet?"
2. "When something goes wrong in the workflow, how long does it take to figure out who changed what?"
3. "If your volume doubled next year, would the spreadsheet still hold up — or would you need to add headcount to maintain it?"
4. "What happens when the person who built the spreadsheet leaves?"

**If the prospect favors the status quo**: Do not compete on price — you cannot beat free. Compete on cost-of-inaction. If the cost-of-inaction number is small, the deal is not real this quarter — accept it and stage for next cycle.

**Trap to Avoid**: Demoing features the spreadsheet "can also do." Every feature parity claim from the user strengthens the status quo. Demo only the gaps spreadsheets cannot close — audit trail, concurrency, scale.

---

## 6. Closing Strategy

### Recommended Approach
Deal is mid-funnel with a structural blocker (security) and a soft buyer-side urgency. Strategy: **De-risk security in parallel, harden the business case, and either earn a real Q-end close or honestly re-baseline to Q+1.**

### Next 3 Actions (This Week)
1. **Email VP Ops today**: Request (a) security reviewer's name + intro, (b) confirmation of signature authority for $80k expansion, (c) name of 1–2 daily users for a working session. Owner: AE. Deadline: today.
2. **Submit security packet preemptively**: SOC 2, pen test summary, DPA, architecture diagram, prior approval reference. Owner: AE + SE. Deadline: within 48 hours of getting reviewer contact.
3. **Build the quantified pain model with VP Ops**: 30-min working call. Hours/week × loaded rate + error cost. Output: a one-page ROI she can forward internally. Owner: AE. Deadline: end of week.

### Next 5 Actions (This Month)
4. User working session — surface adoption objections, identify champion candidate among users.
5. Security review call — walk the reviewer through architecture; close their checklist live if possible.
6. Reference call with a similar manufacturer who replaced spreadsheets — pair with VP Ops.
7. Confirm signature path: VP Ops solo, or VP Ops + COO/CFO. If exec sponsor required, schedule a 20-min exec call.
8. Mutual close plan reviewed and agreed with VP Ops — written, dated, shared.

### Deal Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Security review extends past quarter | High | Deal slips | Preemptive packet + scope-extension argument + contingent order form |
| Single-threaded on VP Ops | High | Deal dies if she leaves or deprioritizes | Engage IT + users + sponsor this month |
| No quantified pain → status quo wins | Medium-High | Deal stalls indefinitely | ROI model built jointly with buyer |
| No buyer-side compelling event | High | "Revisit next quarter" | Surface a real trigger (audit, growth plan, headcount); if none exists, accept and re-baseline |
| Expansion treated as new procurement | Medium | Full re-paper, slows close | Confirm MSA coverage early with VP Ops |

---

## 7. Mutual Close Plan

**MUTUAL CLOSE PLAN: ACME Manufacturing x [Your Company]**

Target Close Date: `[Quarter end — fill exact date]`
Target Go-Live Date: `[Close + 30 days]`

| Date | Milestone | Owner | Status |
|---|---|---|---|
| Week 1 | Security reviewer identified + intro made | VP Ops | Pending |
| Week 1 | Security packet submitted | AE | Pending |
| Week 1 | Quantified ROI model drafted with VP Ops | AE + VP Ops | Pending |
| Week 2 | User working session completed | AE + SE | Pending |
| Week 2 | Security review call held | AE + IT | Pending |
| Week 3 | Reference call completed | CSM | Pending |
| Week 3 | Signature path + exec sponsor (if needed) confirmed | VP Ops | Pending |
| Week 4 | Order form / SOW delivered | AE | Pending |
| Week 5 | Security clearance issued | IT | Pending |
| Week 5 | Legal review (scope extension under MSA) complete | Legal both sides | Pending |
| Week 6 | Signature | VP Ops (or sponsor) | Pending |
| Week 7 | Kickoff | CSM | Pending |

**AGREED NEXT STEP**: VP Ops introduces AE to the IT security reviewer by `[date]`; AE submits scope-extension security packet within 48 hours.

---

## 8. Proposal Talking Points

**OPENING (30 seconds)**:
"You told me your team is spending [X hours/week] reconciling the spreadsheet, and that the next phase of volume is going to break that workflow. The cost of staying on spreadsheets through next year is roughly [$Y]. I want to walk through how we close that gap before it hits."

**VALUE PROPOSITION (2 minutes)**:
1. **Eliminate manual reconciliation** → recover ~[X] hours/week across the team
2. **Single source of truth with audit trail** → kill version conflicts, defensible for audits
3. **Scales without added headcount** → absorb next year's volume on current team

**PROOF (1 minute)**:
"`[Similar manufacturer]` was running the same spreadsheet process across `[N]` sites. After moving onto us, they cut reconciliation time `[X]%` in `[timeframe]` and avoided hiring `[N]` additional ops analysts."
> *Use real reference once secured. Do not invent one.*

**DIFFERENTIATION (1 minute)**:
"What matters here isn't features against another vendor — it's that the spreadsheet was never designed for this volume. Every workaround your team is building today is technical debt you'll pay for next year. Our approach gives you the structure spreadsheets can't, without the rigidity of an enterprise system you don't need yet."

**THE ASK (30 seconds)**:
"To close this by `[quarter end date]`, I need three things from you this week: an intro to your security reviewer, confirmation that you can sign at $80k, and 30 minutes with two of your daily users. If we line those up by Friday, the rest of the path fits the quarter. Can you commit to that?"

**IF THEY HESITATE**:
"What would have to be true for this to be the right quarter? Let's map that honestly — if the answer is 'nothing changes,' I'd rather plan for next quarter properly than push you into a bad timeline."

---

## 9. Negotiation Strategy

### Our Position
- **Ideal**: $80k ARR, annual prepay, 2-year term, signed by quarter end
- **Acceptable**: $80k ARR, 1-year term, signed by quarter end with security contingency
- **Walk-away**: Sub-$60k ARR with extended payment terms and no multi-year — at that point this is a discount that damages the existing footprint's pricing integrity

### Concession Strategy

| If They Ask For | We Can Offer | In Exchange For |
|---|---|---|
| Discount on $80k | Up to `[X%]` — `[fill from your pricing policy]` | 2-year term OR named reference + case study |
| Extended payment (Net 60) | Net 45 | Annual prepay |
| Phased rollout | Phased scope, full ARR | Signature this quarter, go-live phased |
| More seats / users | Bundle into expansion | Multi-year commit |
| Security contingency clause | Yes — signed order with security-clearance condition | Firm signature date, not "after security" |

### Red Lines
- No price reduction below the existing footprint's effective per-unit rate — protects the install base
- No indefinite security contingency — must have a date
- No custom security controls outside standard offering — sets precedent across the customer base

---

## 10. Post-Close Plan

### Implementation Timeline
- Week 1: Kickoff, data migration plan, security/IT handshake confirmed
- Weeks 2–3: Configuration, user provisioning, integration with existing footprint
- Week 4: User training, parallel run against spreadsheet
- Week 5: Cutover
- Week 8: First value-check — measure against ROI model
- Week 12: QBR with VP Ops + sponsor — formal ROI review

### Success Metrics (align with the ROI model used to close)
- Hours/week reclaimed from manual reconciliation
- Error/incident rate vs. spreadsheet baseline
- Time-to-report or time-to-decision improvement
- User adoption rate among target team

### First 90 Days
- Dedicated CSM check-ins weekly for first 30 days, biweekly thereafter
- Value snapshot delivered at day 45 to VP Ops — gives her ammunition for her own internal narrative
- Day 90 QBR positions next expansion conversation

---

## Appendix: Research Sources

None — no external research performed. See note at top. Before sending any externally-facing artifacts derived from this playbook, complete the company intelligence pass on the actual ACME Manufacturing account.

---

**Boundary note**: The Skill specifies WebSearch-based company research. I did not execute it because the task is labeled synthetic and live research would attribute real company data to a fictional deal. The correct next step is for the rep to either (a) confirm this is a real account and re-run me with that confirmation so I can populate Section 1, or (b) populate Section 1 manually from internal CRM notes before using the playbook in the field.

File written: `deal-playbook.md`
