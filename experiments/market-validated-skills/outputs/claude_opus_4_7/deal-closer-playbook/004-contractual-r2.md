# Deal Playbook: EastRiver Bank — Security & Procurement Handoff

## Deal Snapshot

- **Company:** EastRiver Bank
- **Product:** Workflow automation platform
- **Stage:** Proposal
- **Primary Contact:** Sam Patel, Director of Transformation (Champion)
- **Economic Buyer:** COO `[name UNKNOWN]`
- **Deal Size:** $260k ARR
- **Target Close:** 2026-07-15
- **Current Blockers:** procurement vendor onboarding, security/SOC 2 evidence, data residency questions
- **Focus of this playbook:** internal handoff to unblock procurement and security review. No customer-facing message to be sent.

---

## Known Facts And Unknowns

**Facts (provided):**
- Stage is Proposal; champion identified; economic buyer is the COO.
- Three named blockers: procurement vendor onboarding, security evidence (SOC 2), data residency questions.
- Deal value $260k ARR, target close 2026-07-15.

**Unknowns (`[UNKNOWN]` — confirm before next step):**
- COO name and engagement level.
- Procurement contact, vendor onboarding portal/process, required forms (W-9, COI, DPA, BCP, third-party risk questionnaire).
- Security reviewer name; specific evidence requested (SOC 2 Type I vs Type II, scope, date of report, bridge letter, pen test, SIG/CAIQ).
- Data residency requirement (US-only? specific region? in-country processing? sub-processor list constraints?).
- Existence of an active NDA to share SOC 2 report.
- Whether legal/MSA review has started; standard paper vs customer paper.
- Internal owners on our side: Security/GRC lead, Legal, Deal Desk, Solutions Engineer.
- Competitors in the deal.
- Decision criteria and scoring rubric (if any).
- Mutual action plan status with Sam.

---

## Company Intelligence

- **Evidence gap:** No web research performed and no company materials supplied. Treating EastRiver Bank as a regulated U.S. banking entity is an **Inference** based on the name and likely procurement/security rigor, not a Fact.
- Banks typically require: SOC 2 Type II, vendor risk assessment, DPA, business continuity/DR plan, sub-processor disclosure, encryption standards, incident response SLAs, and often regulatory alignment (e.g., FFIEC, GLBA) — **Inference**, confirm with Sam.

---

## Buying Committee Map

| Role | Person | Status | Notes |
|---|---|---|---|
| Champion | Sam Patel, Dir. Transformation | Engaged (Fact) | Owns transformation outcome; use to navigate internal process |
| Economic Buyer | COO `[UNKNOWN name]` | Engagement `[UNKNOWN]` | Approves $260k ARR; needs ROI + risk story |
| Technical Evaluator | `[UNKNOWN]` | — | Likely InfoSec/GRC reviewer |
| Procurement | `[UNKNOWN]` | Active blocker | Vendor onboarding gatekeeper |
| Legal | `[UNKNOWN]` | Likely involved | MSA/DPA |
| Security/GRC | `[UNKNOWN]` | Active blocker | SOC 2 + data residency owner |
| User Buyer | `[UNKNOWN]` | — | Operations team(s) automating workflows |
| Executive Sponsor | COO (likely) | `[UNKNOWN]` | — |
| Coach | `[UNKNOWN]` | — | Ask Sam to identify a coach inside procurement/security |
| Blocker | None named | — | Treat unresponsive reviewers as procedural, not adversarial |

---

## Deal Qualification And Risk

- **Risk – Close-date realism:** Bank security + procurement cycles for a new vendor commonly run 6–12+ weeks. Target close 2026-07-15 is achievable only if security/procurement run in parallel and evidence is delivered fast. **Inference.**
- **Risk – Evidence readiness:** If our SOC 2 Type II is stale, scoped narrowly, or unavailable under NDA, the deal stalls. **Unknown internally — verify.**
- **Risk – Data residency:** If the bank requires in-region or in-country processing we don't support, this becomes a product gap, not a paperwork issue. **Unknown — must clarify scope with Sam this week.**
- **Risk – Economic buyer distance:** No confirmed COO engagement; champion-led deals stall at procurement without exec air-cover.
- **Risk – Competitor presence:** `[UNKNOWN]` — ask Sam.
- **Qualification gap:** No mutual action plan or written decision criteria on file (assumed).

---

## Objection Playbook

| Objection | Response Direction | Evidence Needed |
|---|---|---|
| "We need SOC 2 evidence before review." | Offer SOC 2 Type II report under MNDA; provide bridge letter if report is approaching 12 months; include scope summary and CUECs. | Latest SOC 2 Type II, bridge letter, NDA |
| "We need vendor onboarding completed." | Assign internal owner to complete portal/questionnaire within 5 business days; request the full checklist up front. | Vendor portal access, W-9, COI, DPA template, sub-processor list |
| "Where is data stored / processed?" | Confirm hosting region(s), sub-processors, encryption at rest/in transit, key management; map to their residency requirement. | Architecture/data-flow diagram, sub-processor list, encryption standards doc |
| "We need a DPA / specific contract terms." | Provide standard DPA; route customer redlines to Legal/Deal Desk — **Human gate**. | DPA template, fallback positions |
| "Timeline is tight — can you guarantee close by 7/15?" | Do **not** commit. Offer a mutual close plan with milestones; flag dependencies. | Mutual action plan |
| "Why you vs. incumbent / alternative?" | `[UNKNOWN competitor]` — defer until identified. | Competitor name from Sam |

---

## Competitive Positioning

- Competitor set `[UNKNOWN]`. Do not assert differentiators without facts.
- **Action:** ask Sam directly: "Who else is being evaluated, and what would make us the obvious choice for the COO?"

---

## Closing Strategy (Proposal Stage)

The deal does not advance on selling — it advances on **removing review friction**. Strategy:

1. **Run procurement and security in parallel**, not serially.
2. **Package an "Evidence Pack"** so reviewers get everything in one delivery, reducing back-and-forth.
3. **Get COO air-cover** via Sam — a short COO-to-COO/Exec note that this is a priority unblocks queue position.
4. **Convert the proposal into a written mutual close plan** co-signed by Sam.
5. **Quarantine data residency early** — if it's a product gap, surface now, not in week 6.

---

## Mutual Close Plan (Draft — confirm with Sam)

| # | Milestone | Owner | Target Date | Dependency | Risk |
|---|---|---|---|---|---|
| 1 | Confirm procurement contact + onboarding checklist | Sam Patel | +3 days | Sam intro | Delay if Sam OOO |
| 2 | Confirm security reviewer + exact evidence list (SOC 2 scope, SIG/CAIQ, pen test) | Sam Patel | +3 days | — | Scope creep |
| 3 | Clarify data residency requirement (region, sub-processors, in-country processing) | Sam + our SE | +5 days | — | Potential product gap |
| 4 | Execute MNDA (if not in place) for SOC 2 sharing | Our Legal | +5 days | Bank legal | NDA cycle time |
| 5 | Deliver Evidence Pack (SOC 2 Type II, bridge letter, DPA, sub-processors, architecture, BCP/DR, IR summary) | Our Security/GRC | +7 days | NDA executed | Stale evidence |
| 6 | Submit vendor onboarding portal | Our Deal Desk | +10 days | Checklist received | Missing artifacts |
| 7 | Security review session (Q&A) | Our Security + SE | +3 weeks | Evidence reviewed | Reviewer backlog |
| 8 | Procurement Q&A + redlines returned | Bank procurement | +4 weeks | Onboarding submitted | Customer paper |
| 9 | Legal redlines resolved | Our Legal + Bank Legal | +5 weeks | DPA/MSA exchange | Term disputes |
| 10 | COO approval + signature | COO | by 2026-07-15 | All above | Date slip |

> Dates are placeholder offsets pending confirmation with Sam. **No date is a commitment.**

---

## Next 3 Actions (Internal Only)

1. **Internal kickoff (this week):** assemble pod — AE, SE, Security/GRC lead, Legal, Deal Desk. Assign owners against the mutual close plan above.
2. **Discovery call with Sam (this week):** confirm procurement contact, security reviewer, exact evidence list, data residency requirement, COO engagement plan, competitors. No commitments made.
3. **Prepare the Evidence Pack draft** so it ships within 24 hours of MNDA execution.

---

## Human Gates And Handoffs

- **Security/GRC lead:** approve scope of SOC 2 sharing, bridge letter, and answers to data residency questions. **Required before any evidence leaves our org.**
- **Legal:** approve NDA, DPA, and any contract redlines. **Required before sending paper.**
- **Deal Desk / Finance:** approve any pricing, payment terms, or concessions. **None approved here.**
- **Sales Manager:** approve the mutual close plan and any executive escalation to the COO.
- **AE:** owns customer communication. **No external message to be sent until manager + legal sign off on the handoff plan.** (Honors the user's instruction.)
- **Post-close handoff:** Customer Success / Implementation owner `[UNKNOWN]` — identify now to avoid a cold handoff.

---

## Research Sources Or Evidence Gaps

- No web research performed; no external sources cited. All company-specific statements about EastRiver Bank are **Inference** unless drawn from the user's brief.
- Key evidence gaps: COO identity, procurement and security reviewer contacts, exact evidence list, data residency requirement, competitor set, NDA status, SOC 2 report freshness.

---

## Boundary Note

This playbook is internal strategy only. It does **not** approve discounts, contract terms, security or legal positions, delivery dates, or any customer-facing commitment. Drafting or sending a message to EastRiver Bank requires sales manager + legal approval per the user's instruction and the Skill's human gates.
