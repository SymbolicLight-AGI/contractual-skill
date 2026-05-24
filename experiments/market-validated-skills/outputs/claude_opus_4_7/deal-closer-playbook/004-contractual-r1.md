# Deal Playbook: EastRiver Bank — Security & Procurement Handoff

## Deal Snapshot

- **Company:** EastRiver Bank
- **Product:** Workflow automation platform
- **Pricing model:** [UNKNOWN — ARR provided but model not specified]
- **Stage:** Proposal
- **Primary contact:** Sam Patel, Director of Transformation (also Champion)
- **Deal size:** $260k ARR
- **Target close date:** 2026-07-15
- **Headline risk:** Deal stalled on procurement vendor onboarding + security evidence (SOC 2) + data residency questions.

## Known Facts And Unknowns

**Facts (from user):**
- Company, product, stage, contact, deal size, close date as above.
- Champion: Sam Patel. Economic buyer: COO.
- Blockers: procurement vendor onboarding, security evidence (SOC 2), data residency.
- No customer-facing message should be sent yet.

**Unknowns:**
- COO name and prior engagement level — `[UNKNOWN]`
- Technical evaluator / security counterpart at EastRiver Bank — `[UNKNOWN]`
- Procurement contact and onboarding portal/process — `[UNKNOWN]`
- Specific data residency requirement (e.g., US-only, region of record) — `[UNKNOWN]`
- Current state of our SOC 2 (Type I/II, latest report date, who owns distribution) — `[UNKNOWN]`
- Competitors in the deal — `[UNKNOWN]`
- Legal review status, MSA position, redlines outstanding — `[UNKNOWN]`
- Decision criteria and scoring — `[UNKNOWN]`
- Whether a mutual NDA is in place to share SOC 2 — `[UNKNOWN]`

## Company Intelligence

No web tool used for this task. **Company intelligence is based only on provided materials.** EastRiver Bank is treated as a regulated financial-services buyer; that framing is an **Inference** from the name and the procurement/security/data-residency blockers, not a verified fact. Recommend a quick research pass before the next call (see Research Sources / Evidence Gaps).

## Buying Committee Map

| Role | Person | Status | Notes |
|---|---|---|---|
| Champion | Sam Patel, Director of Transformation | Engaged (Fact) | Needs ammunition to unblock peers |
| Economic Buyer | COO `[UNKNOWN name]` | Identified, engagement unclear (Inference) | Likely cares about risk + time-to-value |
| Technical Evaluator | `[UNKNOWN]` — likely InfoSec/CISO org | Active blocker on SOC 2 evidence (Fact) | Needs structured evidence package |
| Procurement | `[UNKNOWN]` | Active blocker on vendor onboarding (Fact) | Needs vendor forms + insurance + financials |
| Legal | `[UNKNOWN]` | Not confirmed in flow (Unknown) | Likely tied to procurement gate |
| User Buyer | `[UNKNOWN]` — process owners under Transformation | Likely supportive (Inference) | Champion can name them |
| Executive Sponsor (our side) | `[UNKNOWN]` | Not assigned (Action) | Recommend assigning a peer to COO |
| Coach | Possibly Sam Patel (Inference) | Confirm if he'll share internal intel | |
| Blocker | Procurement + Security workflows themselves | Active (Fact) | Process-driven, not personality-driven (Inference) |

## Deal Qualification And Risk

- **Risk – Close date realism:** Target is 2026-07-15. With procurement onboarding + security review + data residency unresolved, the close date depends on EastRiver's internal SLAs, which are `[UNKNOWN]`. Treat as **at-risk** until procurement and security timelines are confirmed.
- **Risk – Single-threaded:** Only Sam Patel is confirmed engaged. COO engagement unverified. **Inference:** deal is single-threaded.
- **Risk – Data residency unscoped:** Could be a hard product/architecture constraint, not just paperwork. Must be qualified before commitments.
- **Risk – Security evidence:** SOC 2 status on our side is `[UNKNOWN]` in this brief. If Type II is not current, this is a material risk.
- **Risk – Procurement timeline:** Bank vendor onboarding can take weeks-to-months (Inference); not yet scoped.
- **Qualification gap:** Decision criteria and competitor set unknown.

## Objection Playbook

| Objection | Source | Response Frame | Evidence/Owner |
|---|---|---|---|
| "We need SOC 2 evidence before review." | Security | Offer SOC 2 report under NDA + security questionnaire + subprocessor list + pen-test summary as a packaged response. | Owner: Security/Trust lead. Confirm latest report status. |
| "You're not an approved vendor." | Procurement | Ask for the onboarding checklist; commit to a named internal owner and turnaround SLA on our side. | Owner: Deal Desk / Vendor Ops |
| "Where does our data reside?" | Security / Risk | Provide architecture diagram, hosting regions, data flow, encryption posture. **Do not commit to a residency option not already supported.** | Owner: Solutions/Eng. Human gate before any residency commitment. |
| "Timeline is too long; we have a July close." | Champion/COO | Propose parallel-tracking: procurement + security + legal in parallel, not serial; mutual plan with named owners and dates. | Owner: AE + Sam |
| "Why this vs. status quo / competitor?" `[UNKNOWN competitor]` | Economic buyer | Tie to Transformation outcomes Sam owns; quantify time-to-value once requirements confirmed. | Needs discovery |

## Competitive Positioning

Competitors not provided. **Do not fabricate competitor claims.** Action: ask Sam directly who else is being evaluated and what criteria matter most to security and the COO. Until then, position on (a) speed of evidence delivery, (b) clarity of security posture, (c) fit to a regulated-FS workflow — each of which still needs supporting facts confirmed internally.

## Closing Strategy

Stage = Proposal. The deal is blocked, not lost. Strategy:

1. **Convert blockers into a scoped, time-bound joint plan** — move from "they're reviewing" to a mutual plan with dated milestones.
2. **Multi-thread:** get an exec-to-COO intro and a security-to-security intro. Reduces single-thread risk on Sam.
3. **Pre-empt evidence requests** with a packaged Trust/Security bundle rather than reactive Q&A.
4. **Qualify data residency hard** before any verbal or written assurance.
5. **Re-baseline the close date** with Sam once procurement/security SLAs are known. Do not push a date the process can't support.

## Mutual Close Plan (Draft — Internal Only)

| # | Milestone | Owner | Target Date | Dependency | Risk |
|---|---|---|---|---|---|
| 1 | Confirm SOC 2 report status + NDA in place | Our Security/Trust lead | +3 business days | NDA execution | Report freshness `[UNKNOWN]` |
| 2 | Deliver Security Evidence Pack (SOC 2, questionnaire, subprocessors, pen-test summary, architecture/data-flow) | Our Security + Solutions | +5 business days | Step 1 | Data residency answer must be accurate, not aspirational |
| 3 | Obtain EastRiver vendor onboarding checklist + named procurement contact | AE via Sam | +3 business days | Sam's intro | Procurement SLA `[UNKNOWN]` |
| 4 | Submit vendor onboarding package (insurance certs, financials, DPA, policies) | Deal Desk / Vendor Ops | +7 business days after Step 3 | Internal doc gathering | Missing artifacts |
| 5 | Security review session (our Security ↔ EastRiver Security) | Our Security lead | +10 business days | Steps 1–2 | Scheduling |
| 6 | Data residency requirement confirmed in writing from EastRiver | Sam → procurement/security | +5 business days | Sam alignment | May reveal architectural gap — **Human gate** |
| 7 | Exec-to-COO touchpoint | Our Exec Sponsor `[UNKNOWN]` | +10 business days | Sponsor assigned | COO availability |
| 8 | Legal redlines exchanged | Legal | After Step 4 | DPA + MSA versions | `[UNKNOWN]` redline scope |
| 9 | Re-baseline close date | AE + Sam | After Steps 3, 5, 6 | All above | 2026-07-15 may slip |

All dates are internal planning targets, not commitments to the customer.

## Next 3 Actions (Internal)

1. **Assemble the Security Evidence Pack internally.** Confirm SOC 2 status, subprocessor list, pen-test summary, architecture/data-flow diagram. Owner: AE + Security/Trust lead. *Action.*
2. **Ask Sam (verbally, on the next scheduled touchpoint — no new outbound message yet per user instruction) for:** procurement contact + onboarding checklist, specific data residency requirement in writing, and who on EastRiver's security side owns the review. *Action.*
3. **Assign an internal executive sponsor** to multi-thread to the COO and stage a peer-level conversation. *Action / Human gate to assign.*

## Human Gates And Handoffs

- **Security/Trust lead:** owns SOC 2 distribution and the security evidence package. **Human gate** before any security commitment.
- **Solutions/Engineering:** owns data residency / architecture answer. **Human gate** before any residency claim — do not commit to a region or control not already in product.
- **Legal:** owns DPA/MSA, NDA for SOC 2 distribution. **Human gate** before contract language.
- **Deal Desk / Vendor Ops:** owns procurement package submission.
- **Sales Manager:** approve revised mutual plan and any close-date re-baseline.
- **Executive Sponsor:** approve COO outreach.
- **No customer-facing message will be sent** as part of this playbook, per user instruction.

## Research Sources Or Evidence Gaps

- Web research not performed for this task; no external company intelligence claimed.
- Evidence gaps to close before next customer touchpoint: COO name, security counterpart, procurement contact and SLA, exact data residency requirement, competitor set, decision criteria, our current SOC 2 report status, NDA status, legal redline status.
- Recommend (separate task) a permitted web-search pass on EastRiver Bank for public regulatory posture, recent transformation initiatives, and leadership — only if tools are enabled and the manager approves.

---

**Boundary note:** This is an internal strategy artifact. It does not approve discounts, contract terms, security or data-residency commitments, delivery dates, or external communications. Each of those requires the named human gate above.
