# Internal Handoff Brief — Security & Procurement Unblock

**Note on Skill boundary:** The `deal-closer-playbook` skill produces a full `deal-playbook.md` covering company intelligence, buying committee, MEDDIC, objections, competitive positioning, closing strategy, mutual close plan, talking points, and negotiation. The user's task is narrower: an *internal handoff* to unblock security review, procurement onboarding, and an implementation timeline request.

I will stay inside the skill by treating this as a **Negotiation/Close stage** subset focused on **Step 7 (Closing Strategy — paper process)** and **Step 8 (Mutual Close Plan)**. I will not generate the full playbook because most required inputs are missing. Critical gaps below.

---

## Missing Inputs (Marked `[UNKNOWN]`)

To produce a complete playbook I would need the following. I am proceeding with a handoff brief and flagging each gap:

- Company name — `[UNKNOWN]`
- Product / pricing model — `[UNKNOWN]`
- Deal size (ARR/TCV) — `[UNKNOWN]`
- Target close date — `[UNKNOWN]`
- Target go-live date — `[UNKNOWN]`
- Champion name and title — `[UNKNOWN]`
- Economic buyer — `[UNKNOWN]`
- Security questionnaire scope (SOC 2, ISO, HIPAA, GDPR, custom?) — `[UNKNOWN]`
- Procurement system / vendor onboarding portal — `[UNKNOWN]`
- Data residency, SSO, or compliance requirements — `[UNKNOWN]`
- Implementation model (self-serve, PS-led, hybrid) — `[UNKNOWN]`

Because of these gaps, I cannot run **Phase 1 Step 2 (Company Research via WebSearch)** meaningfully, and I cannot produce dated milestones. I will deliver the handoff in a template the rep can populate immediately.

---

## Internal Handoff Brief — Template

### 1. Deal Snapshot (for internal recipients)

| Field | Value |
|---|---|
| Account | `[UNKNOWN — fill in]` |
| Stage | Negotiation / Verbal-leaning |
| Deal size | `[UNKNOWN]` |
| Target close | `[UNKNOWN]` |
| Target go-live | `[UNKNOWN]` |
| Buyer sentiment | Positive — product fit confirmed |
| Active blockers | Security questionnaire, Vendor onboarding, Implementation timeline request |
| Champion | `[UNKNOWN]` |
| Economic Buyer | `[UNKNOWN]` |

### 2. What the Buyer Has Said

- Product is a fit; they want to move forward.
- Security team has issued a questionnaire (pending response).
- Procurement requires vendor onboarding before contract execution.
- Champion has explicitly asked for an implementation timeline — this is a buying signal; treat it as a closing milestone, not a generic request.

### 3. Handoff to Security Team

**Owner needed:** Security / GRC lead
**SLA target:** Return completed questionnaire within 5 business days of receipt (adjust to internal SLA).

Action items:
1. Receive questionnaire from AE; confirm format (spreadsheet, Whistic, OneTrust, custom doc) — `[UNKNOWN]`.
2. Identify any non-standard questions requiring engineering or legal input within 24 hours of receipt.
3. Bundle response with standard trust artifacts: SOC 2 report, pen test summary, DPA, sub-processor list, architecture diagram.
4. Flag any answers requiring caveats so AE can pre-frame with the buyer.
5. Return to AE with a single deliverable package, not piecemeal.

AE-side prep needed:
- Confirm with champion: who on buyer side reviews answers, and what is *their* SLA back to us?
- Ask: "Is there a specific control or question we should prioritize?" — surfaces hidden objections.

### 4. Handoff to Procurement / Deal Desk

**Owner needed:** Deal Desk or Finance Ops
**SLA target:** Vendor onboarding package submitted within 2 business days of buyer providing portal access.

Action items:
1. Obtain buyer's vendor onboarding portal link and required forms from procurement contact — `[UNKNOWN]`.
2. Prepare standard vendor package: W-9 / tax forms, banking / ACH details, insurance certificates (COI), DEI / ESG attestations if required, MSA / DPA templates.
3. Identify the buyer's procurement reviewer by name and add to mutual close plan.
4. Confirm payment terms expectation early — if buyer requires Net 60+ and our standard is Net 30, escalate now, not at redline.

AE-side prep needed:
- Ask champion for procurement contact and timeline expectations.
- Ask: "Are there any vendor approval steps beyond standard onboarding — InfoSec sign-off, ABAC, board approval?"

### 5. Handoff to Professional Services / Implementation

**Owner needed:** PS / Onboarding lead
**Deliverable:** Branded implementation timeline document, sent to champion within 3 business days.

The implementation timeline must include:
- Kickoff date (placeholder tied to target close + 5 business days)
- Phase 1: Provisioning, SSO, integrations — `[duration]`
- Phase 2: Configuration and data migration — `[duration]`
- Phase 3: User training and rollout — `[duration]`
- Go-live milestone
- 30 / 60 / 90 day success checkpoints
- Named PS owner on our side
- Resource asks from buyer (admin, IT contact, integration owner)

AE-side framing for champion:
> "Here is the implementation plan. To hit the [go-live date] you mentioned, we would need to countersign by [date]. I have built the plan backward from that. Does this work for your team?"

This converts the timeline request into a close lever.

### 6. Mutual Close Plan (paper process subset)

| Date | Milestone | Owner | Status |
|---|---|---|---|
| `[DATE]` | Security questionnaire returned to buyer | Our Security Lead | Pending |
| `[DATE]` | Buyer security team review complete | Buyer Security | Pending |
| `[DATE]` | Vendor onboarding submitted | Our Deal Desk | Pending |
| `[DATE]` | Vendor approved in buyer's system | Buyer Procurement | Pending |
| `[DATE]` | Implementation timeline delivered to champion | Our PS Lead | Pending |
| `[DATE]` | MSA / order form to buyer legal | Our Legal | Pending |
| `[DATE]` | Redlines returned | Buyer Legal | Pending |
| `[DATE]` | Final terms agreed | Both | Pending |
| `[DATE]` | Signature | Economic Buyer (`[UNKNOWN]`) | Pending |
| `[DATE]` | Kickoff | Both | Pending |

**Agreed next step:** `[Fill: single most important action, owner, date — e.g., "AE forwards questionnaire to Security by EOD Tuesday; Security returns by following Tuesday."]`

### 7. Risks in This Handoff Phase

| Risk | Mitigation |
|---|---|
| Security questionnaire becomes a multi-week round-trip | Pre-schedule a joint security review call to resolve open items live |
| Procurement adds steps AE was unaware of (InfoSec re-review, board approval) | Ask champion now: "Walk me through every step from yes to signature" |
| Implementation timeline becomes a wish-list instead of a close lever | Tie the timeline to a signature-by date in the same document |
| Champion goes quiet during procurement | Schedule a 15-min weekly sync until contract is signed; do not rely on email |
| Single-threaded — only the champion is engaged | Use the implementation timeline as a reason to introduce PS lead to buyer's IT/admin owner — adds a second thread |

### 8. Recommended Next 3 Actions (this week)

1. **AE → Champion (today):** Acknowledge receipt of the three requests, confirm owners on our side, and ask the four discovery questions embedded above (security reviewer, procurement contact, full step list, target go-live).
2. **AE → Internal (today):** Forward questionnaire to Security, request vendor onboarding kit from Deal Desk, brief PS on implementation timeline ask with target close date.
3. **AE → Champion (within 3 business days):** Deliver implementation timeline framed as a backward-planned close plan; request signature target date confirmation.

---

## Boundary Note

If you want the **full `deal-playbook.md`** generated as the skill specifies (company intelligence via WebSearch, full buying committee map, MEDDIC, objections, competitive positioning, negotiation strategy), provide the `[UNKNOWN]` fields above — at minimum company name, product, deal size, champion, economic buyer, and target close date. I did not invent these because Behavioral Rule 6 prohibits manufacturing information.
