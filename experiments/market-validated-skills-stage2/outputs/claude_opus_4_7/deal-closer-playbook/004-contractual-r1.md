# Deal Closer Playbook — Internal Handoff for Security & Procurement Blockers

## Deal Snapshot

- Company: `[UNKNOWN]`
- Product / pricing model: `[UNKNOWN]`
- Deal stage: Late-stage / pre-close (inferred from active security questionnaire, procurement onboarding, and implementation timeline request)
- Primary contact / title: `[UNKNOWN]`
- Deal size: `[UNKNOWN]`
- Target close date: `[UNKNOWN]`

## Known Facts And Unknowns

**Facts (from task):**
- Buyer likes the product.
- Security questionnaire is pending.
- Procurement requires vendor onboarding.
- Champion has asked for an implementation timeline.

**Unknowns (`[UNKNOWN]`):**
- Company name, product/pricing, deal size, target close date.
- Primary contact, champion identity, economic buyer, technical evaluator.
- Security questionnaire owner on buyer side, scope (SOC 2, ISO 27001, custom), and deadline.
- Procurement onboarding requirements (forms, insurance, W-9/W-8, banking, DPA, MSA redlines).
- Existing MSA/DPA status, data residency or regulatory constraints.
- Competitors, prior pricing discussions, discount expectations.
- Implementation scope, integrations, go-live target.

## Company Intelligence

Not available. No company name was provided and the task did not authorize external research. Company intelligence is limited to the four facts above.

## Buying Committee Map

| Role | Identified? | Notes |
|---|---|---|
| Champion | Yes (unnamed) — asked for implementation timeline | Inference: actively pulling the deal forward |
| Economic buyer | `[UNKNOWN]` | Confirm sign-off authority before close |
| Technical evaluator | `[UNKNOWN]` | Likely owner of security questionnaire |
| User buyer | `[UNKNOWN]` | |
| Procurement | Active (vendor onboarding in flight) | Owner name `[UNKNOWN]` |
| Security / InfoSec | Active (questionnaire pending) | Owner name `[UNKNOWN]` |
| Legal | `[UNKNOWN]` | Likely surfaces during MSA/DPA |
| Executive sponsor | `[UNKNOWN]` | |
| Blocker | None identified | Risk: procurement or security can become de facto blockers if unmanaged |

## Deal Qualification And Risk

- **Risk:** Security questionnaire pending without a named owner or SLA on our side can slip the close date.
- **Risk:** Vendor onboarding often introduces forms (insurance certs, financials, DPA, supplier portal) that add 1–4 weeks if started late.
- **Risk:** Implementation timeline requests near close can imply assumed start dates the rep has not confirmed — risk of soft commitments.
- **Risk:** Economic buyer not confirmed; champion enthusiasm ≠ signature authority.
- **Inference:** Deal is technically won on product fit; remaining risk is procedural, not commercial.

## Objection Playbook

| Likely Objection | Response Frame |
|---|---|
| "Security review will take weeks." | Offer pre-completed SOC 2 / security packet (if available — confirm internally) and a dedicated security point of contact to accelerate Q&A. |
| "Procurement onboarding is slow." | Request the onboarding checklist now; run security and procurement workstreams in parallel, not serial. |
| "We need a firm go-live date." | Provide a *conditional* implementation timeline tied to contract signature date; mark dates as estimates pending signature. **Human gate** before sending. |
| "Can you commit to X security control / SLA?" | Do not commit. Route to Security owner. |

## Competitive Positioning

No competitor information was provided. Not generated to avoid fabrication.

## Closing Strategy

Stage-appropriate strategy: **de-risk procedural blockers in parallel and protect the close date.**

1. Run security questionnaire, procurement onboarding, and implementation planning as three parallel tracks with named internal owners.
2. Convert champion's implementation timeline request into a **mutual close plan** that binds buyer-side actions (signature, security responses, procurement forms) to our delivery dates.
3. Confirm economic buyer and signature path before final redlines.

## Mutual Close Plan (Draft — Internal)

| Milestone | Owner (Internal) | Buyer Owner | Target Date | Dependency | Risk |
|---|---|---|---|---|---|
| Security questionnaire returned | Security / InfoSec lead | Buyer security contact `[UNKNOWN]` | `[UNKNOWN]` | Questionnaire received in full | Scope creep, custom controls |
| Vendor onboarding forms submitted | AE + Finance | Procurement contact `[UNKNOWN]` | `[UNKNOWN]` | Checklist from buyer | Insurance/financial doc delays |
| MSA / DPA review | Legal | Buyer Legal `[UNKNOWN]` | `[UNKNOWN]` | Redlines exchanged | Data residency, liability caps |
| Implementation timeline (conditional) | Solutions / CS | Champion | `[UNKNOWN]` | Signature date assumption | Treated as binding by buyer |
| Signature | AE | Economic buyer `[UNKNOWN]` | `[UNKNOWN]` | All above | Slippage past target close |

All dates `[UNKNOWN]` until target close date is provided.

## Internal Handoff Package (Primary Deliverable)

### 1. Handoff to Security / InfoSec Owner
- **Ask:** Take ownership of the pending security questionnaire.
- **Provide:** Buyer name `[UNKNOWN]`, questionnaire scope `[UNKNOWN]`, deadline `[UNKNOWN]`.
- **Need from owner:** ETA to complete, list of any questions requiring buyer clarification, and any controls we cannot attest to (so AE can manage expectations).
- **Boundary:** Security owner — not AE — confirms any control commitments.

### 2. Handoff to Procurement / Finance / Vendor Ops
- **Ask:** Own buyer-side vendor onboarding.
- **Provide:** Buyer procurement contact `[UNKNOWN]`, onboarding portal/forms `[UNKNOWN]`.
- **Need from owner:** Standard onboarding doc pack (W-9/W-8, insurance certs, banking, supplier diversity if relevant), and confirmation of which buyer-specific forms require Legal sign-off.

### 3. Handoff to Legal
- **Ask:** Stand by for MSA/DPA redlines once procurement releases them.
- **Provide:** Deal size `[UNKNOWN]`, data scope `[UNKNOWN]`.
- **Need from owner:** Pre-approved fallback positions on common redlines (liability, indemnity, data processing).

### 4. Handoff to Solutions / Customer Success (Implementation Timeline)
- **Ask:** Draft a **conditional** implementation timeline for the champion.
- **Provide:** Known scope `[UNKNOWN]`, integrations `[UNKNOWN]`, desired go-live `[UNKNOWN]`.
- **Constraint:** Timeline must be labeled "estimated, contingent on signature date of [TBD]." No firm go-live dates committed externally without sales manager approval.

### 5. Handoff to Sales Manager
- **Ask:** Approve the mutual close plan and the conditional implementation timeline before either is shared externally.
- **Decision needed:** Whether to escalate to an executive sponsor on our side to mirror the champion and unlock procurement velocity.

## Next 3 Actions

1. **Action (AE):** Within 24 hours, confirm named owners on the buyer side for security, procurement, and signature; fill `[UNKNOWN]` fields.
2. **Action (AE → Security & Procurement leads):** Send internal handoff briefs (above) and request ETAs.
3. **Action (AE → Sales Manager):** Submit draft mutual close plan and conditional implementation timeline for approval before sharing with the champion.

## Human Gates And Handoffs

- **Human gate — Sales Manager:** Approve mutual close plan and any externally shared timeline.
- **Human gate — Security owner:** Owns all questionnaire responses and control commitments.
- **Human gate — Legal:** Owns MSA/DPA terms, DPA, liability, indemnity.
- **Human gate — Finance/Procurement:** Owns vendor onboarding submissions and any payment terms.
- **Human gate — Solutions/CS:** Owns implementation feasibility; AE must not commit go-live dates unilaterally.
- **Not permitted in this Skill:** Promising security approvals, procurement timelines, contract terms, discounts, or firm go-live dates.

## Research Sources Or Evidence Gaps

- No external research performed; task did not request it and no company name was supplied.
- Evidence gaps: company, deal size, close date, stakeholder names, questionnaire scope, procurement requirements, contract status, implementation scope. Request these from the AE to upgrade the playbook from partial to complete.
