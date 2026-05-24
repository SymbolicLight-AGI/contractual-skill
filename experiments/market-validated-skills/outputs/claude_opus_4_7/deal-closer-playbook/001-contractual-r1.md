# Northstar Clinics — Closing Playbook

## Deal Snapshot

- **Company:** Northstar Clinics
- **Product:** Secure patient messaging platform (annual SaaS)
- **Stage:** Evaluation
- **Primary contact:** Maya Chen, VP Operations (Champion)
- **Deal size:** $180k ARR
- **Target close:** 2026-06-30
- **Top risk:** HIPAA audit-evidence concern from security team; CFO not yet engaged
- **Competitor:** Incumbent patient portal vendor

## Known Facts And Unknowns

**Facts (provided by user):**
- Company, product, pricing model, stage, deal size, target close date as listed above.
- Champion: Maya Chen.
- Economic buyer (CFO) not yet engaged.
- Technical evaluator: Director of IT (name not provided).
- Procurement sequence: security review precedes legal.
- Known objection: HIPAA audit-evidence concern.
- Competitor: incumbent patient portal vendor.

**Unknowns (marked `[UNKNOWN]`):**
- Director of IT name and posture.
- CFO name, priorities, and budget cycle.
- Security team lead, specific HIPAA evidence requirements (e.g., BAA, audit logs, access trails, retention, breach reporting SLA).
- User buyer(s) (clinicians, front desk, care managers).
- Executive sponsor at Northstar.
- Blocker(s) — anyone benefiting from incumbent.
- Decision criteria, scoring rubric, and weights.
- Interaction history, prior demos, POC status.
- Incumbent contract renewal date (critical urgency lever).
- Legal/procurement standard terms, redlines history.
- Implementation expectations and go-live target.
- Clinic count, user count, integration needs (EHR vendor, SSO/IdP).
- Compelling event tied to 2026-06-30.

## Company Intelligence

- **Evidence:** No web research tool available in this experiment. Company intelligence is based only on what the user provided.
- **Inference:** "Clinics" + HIPAA concern indicates a US healthcare provider with PHI obligations. Patient messaging implies clinician-to-patient and possibly intra-clinic workflows.
- **Action:** Before next stakeholder meeting, gather: clinic locations/count, EHR system, IdP, current portal vendor and renewal date, recent OCR/HIPAA audit history (ask Maya).

## Buying Committee Map

| Role | Person | Status | Strategy |
|---|---|---|---|
| Champion | Maya Chen, VP Ops | Engaged | Arm with ROI + audit-evidence one-pager; co-build mutual close plan |
| Economic buyer | CFO `[UNKNOWN]` | Not engaged — **Risk** | Maya-led intro; bring 3-year TCO vs incumbent + ops efficiency case |
| Technical evaluator | Director of IT `[UNKNOWN]` | Unknown posture — **Risk** | Architecture review; SSO, EHR integration, data residency |
| Security reviewer | `[UNKNOWN]` | Skeptical on HIPAA audit evidence — **Risk** | Dedicated security workshop; share SOC 2, HIPAA, BAA, audit log samples (subject to legal/security approval to share) |
| Procurement/Legal | `[UNKNOWN]` | Sequenced after security | Pre-stage MSA, BAA, DPA for review |
| User buyer | `[UNKNOWN]` (clinicians/staff) | Unknown | Workflow demo, pilot user feedback |
| Coach | Maya (also champion) | Active | Validate committee map and timing |
| Blocker | `[UNKNOWN]` (incumbent advocate?) | Unknown — **Risk** | Identify via Maya; neutralize with side-by-side eval |
| Executive sponsor | `[UNKNOWN]` (CEO/COO/CMO?) | Unknown | Reserve for late-stage escalation |

## Deal Qualification And Risk

**MEDDIC-style read (partial):**
- **Metrics:** `[UNKNOWN]` — need to quantify clinician hours saved, message volume, patient response SLA.
- **Economic buyer:** Not engaged — **Risk: high**.
- **Decision criteria:** `[UNKNOWN]` — **Risk: medium**.
- **Decision process:** Security → legal known; full sequence and signers `[UNKNOWN]`.
- **Identify pain:** HIPAA evidence + incumbent gaps inferred, not confirmed.
- **Champion:** Confirmed (Maya). Strength of access to CFO `[UNKNOWN]`.

**Risks:**
- **Risk:** CFO not engaged with ~7+ months to close — late-stage budget surprises.
- **Risk:** Security objection on audit evidence is the gating item before legal; unresolved here stalls everything.
- **Risk:** Incumbent has switching-cost advantage; renewal-date leverage `[UNKNOWN]`.
- **Risk:** No confirmed compelling event tied to 2026-06-30; date may slip.
- **Risk:** Single-threaded on Maya.

## Objection Playbook

| Objection | Source | Response approach | Evidence to bring |
|---|---|---|---|
| "Can you prove HIPAA audit evidence?" | Security team (known) | Walk through audit log model, access controls, BAA scope, retention, breach SLA, SOC 2 / HIPAA attestations. Offer security workshop. | BAA template, audit log sample, control matrix, attestation reports (share per internal policy — **human gate**) |
| "We already have a patient portal" | Incumbent advocate (anticipated) | Reframe: messaging ≠ portal; show workflow gaps, clinician adoption, response times | Side-by-side capability matrix (build from confirmed facts only) |
| "Budget isn't approved" | CFO (anticipated) | 3-year TCO vs incumbent; ops hours saved; risk-cost of HIPAA gaps | TCO model with Maya's inputs |
| "Implementation risk" | IT (anticipated) | Phased rollout, SSO + EHR integration plan, reference customers `[UNKNOWN if available]` | Implementation plan template |
| "Timing — can we wait?" | Multiple | Tie to incumbent renewal, audit cycle, or clinical KPI `[UNKNOWN]` | Compelling event once confirmed |

## Competitive Positioning

- **Evidence gap:** Incumbent's actual feature set, contract terms, and renewal date not provided. No web research available. Do not assert specifics.
- **Inference-based posture:** Position on (a) purpose-built secure messaging vs portal-bolted messaging, (b) HIPAA audit evidence depth, (c) clinician workflow fit.
- **Action:** Ask Maya to share incumbent gaps she has personally observed; build the comparison only from confirmed items.
- **Do not:** Fabricate competitor weaknesses or claims.

## Closing Strategy (Evaluation stage)

1. **Resolve the gating objection first.** Security workshop with documented HIPAA audit-evidence walkthrough. Until security signs off, legal cannot start.
2. **Multi-thread.** Get CFO and Director of IT engaged in parallel within the next 2–3 weeks; Maya hosts.
3. **Confirm compelling event.** Tie 2026-06-30 to incumbent renewal, audit window, or operational milestone. Without one, treat the date as aspirational.
4. **Co-build mutual close plan with Maya** so the buyer owns the timeline.
5. **Reserve negotiation levers** (term length, payment terms, ramp) — do not offer; all concessions are **human gates**.

## Mutual Close Plan (draft — requires Maya's co-sign)

| # | Milestone | Owner | Target date | Dependency | Risk if missed |
|---|---|---|---|---|---|
| 1 | Confirm decision criteria & committee | Maya + AE | T+1 week | Maya intro to IT/CFO | Single-threaded |
| 2 | Security workshop & evidence package review | Security lead + our SecOps | T+3 weeks | NDA in place | Legal cannot start |
| 3 | IT architecture review (SSO, EHR, data) | Director of IT + our SE | T+3 weeks | Tech requirements doc | Integration risk surfaces late |
| 4 | CFO business case review | CFO + Maya + AE | T+4–5 weeks | TCO model | Budget shock |
| 5 | Security sign-off | Security lead | T+6 weeks | Workshop closed | Blocks legal |
| 6 | Legal/procurement redlines (MSA, BAA, DPA) | Procurement + our Legal | T+8 weeks | Security sign-off | Slips close |
| 7 | Executive alignment / final approval | Exec sponsor `[UNKNOWN]` | T+10 weeks | All above | Late veto |
| 8 | Signature | CFO/signer `[UNKNOWN]` | ≤ 2026-06-30 | Procurement complete | Miss close |
| 9 | Implementation kickoff | CS + IT | Within 2 weeks post-signature | Signed order | Adoption delay |

Dates are illustrative; align with Maya before sharing externally (**human gate**).

## Next 3 Actions

1. **Action:** Email Maya (internal draft only) requesting: (a) Director of IT and CFO intros, (b) security team's specific HIPAA evidence checklist, (c) incumbent renewal date. *Do not send externally without rep review.*
2. **Action:** Prepare the HIPAA audit-evidence package outline (BAA, audit logs, access control, retention, breach SLA, attestations) for security workshop. Confirm with internal SecOps what can be shared and under what NDA (**human gate**).
3. **Action:** Build a draft mutual close plan (above) and bring to next Maya call for co-editing.

## Human Gates And Handoffs

- **Pricing, discounts, term, payment:** Sales manager + Finance approval required.
- **Sharing SOC 2 / HIPAA attestations / BAA:** Internal Security + Legal approval; NDA in place.
- **Any commitment on HIPAA controls, audit evidence specifics, breach SLAs:** Security owner.
- **Contract redlines, BAA, DPA:** Legal.
- **Implementation/go-live dates:** Delivery/CS owner.
- **Executive escalation to Northstar exec sponsor:** Sales manager approval.
- **Any external email or CRM update:** Rep owns; this playbook is internal strategy only.

## Research Sources Or Evidence Gaps

- **No web research tool available in this experiment.** All company, competitor, and market statements are limited to user-provided context or labeled as inference.
- **Key evidence gaps to close before next stage gate:** Director of IT identity and posture, CFO identity and budget cycle, security team's HIPAA evidence checklist, incumbent renewal date, compelling event, decision criteria, executive sponsor, blocker identification, EHR/IdP details, clinic and user counts.
