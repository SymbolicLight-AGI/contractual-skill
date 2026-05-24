# Internal Handoff Brief: Security, Procurement & Implementation Coordination

**Purpose:** Coordinate internal teams to unblock the three pending workstreams the buyer is waiting on.
**Status:** Buyer is positively disposed. Champion is actively engaged. Risk is execution friction, not selling.

---

## ⚠️ Information Gaps (Need from Deal Owner Before Handoff Lands)

The following deal facts were not provided. The handoff template below is structured, but these fields must be filled in before sending to internal teams. Marked as `[UNKNOWN]` throughout.

- Company name
- Champion name and title
- Economic buyer name
- Deal size (ARR/TCV)
- Target close date / requested go-live date
- Product/SKU being sold
- Security questionnaire format (SIG, CAIQ, custom)
- Procurement portal or vendor onboarding system in use (e.g., Coupa, Ariba, ServiceNow)
- Region/regulatory scope (GDPR, HIPAA, SOC2 expectations)
- Contract paper (your paper vs. theirs)

**Skill boundary note:** This skill produces a closing playbook and handoff structure. It does not have access to your internal security docs, SOC2 reports, or procurement contacts. Fill in `[UNKNOWN]` fields and route to the named functions below.

---

## Handoff Summary (Top of Email/Slack)

> **Deal:** `[Company Name]` — `[$ARR]`
> **Stage:** Late-stage; buyer verbally favorable, working through paper process.
> **Target close:** `[DATE]`
> **What I need from you (this week):**
> 1. **Security:** Complete questionnaire turnaround — target `[DATE]`
> 2. **Procurement/Legal:** Vendor onboarding packet ready — target `[DATE]`
> 3. **Professional Services / Implementation:** Draft implementation timeline for champion — target `[DATE]`
>
> **Risk if we slip:** Champion loses momentum with internal stakeholders. Deal slips out of `[QUARTER]`.

---

## 1. Security Handoff → Security / InfoSec Team

**Owner requested:** Security Engineer or TPM assigned to vendor questionnaires
**SLA needed:** `[X business days]` — recommend 5 business days max

### Context for the security team
- Buyer has signaled intent to purchase. Questionnaire is the active gating item.
- Questionnaire format: `[UNKNOWN — SIG Lite / SIG Core / CAIQ / custom spreadsheet]`
- Data sensitivity scope: `[UNKNOWN — what data will the customer send through the product]`
- Regulatory frame: `[UNKNOWN — SOC2 Type II, ISO 27001, HIPAA, GDPR]`

### What to provide
- [ ] Completed questionnaire
- [ ] Current SOC 2 Type II report (under NDA if needed)
- [ ] Pen test summary (most recent)
- [ ] Data flow diagram for the product
- [ ] Subprocessor list
- [ ] Incident response policy summary
- [ ] DPA template (if EU/UK data)

### Known sensitive questions to pre-empt
- Data residency and where customer data is stored
- Encryption at rest and in transit (cipher specifics)
- SSO / SAML / SCIM support
- Audit log retention
- Right-to-delete / data export on termination

### Escalation path
If a question requires a control we do not currently have, route to `[Head of Security]` for a compensating-control response rather than leaving blank. Blanks kill deals.

---

## 2. Procurement / Vendor Onboarding Handoff → Finance / Legal Ops

**Owner requested:** Deal Desk or Legal Ops lead
**SLA needed:** Vendor packet returned within `[X]` business days of buyer's procurement portal invite

### Context
- Buyer's procurement team will issue a vendor onboarding request. This typically includes:
  - W-9 / W-8BEN
  - Banking/ACH information
  - Certificate of insurance (COI) — confirm coverage limits buyer requires
  - Diversity certifications (if applicable)
  - Anti-bribery / code of conduct attestations
  - Financial stability documentation (sometimes audited financials or D&B number)

### What to prepare now (before the portal invite arrives)
- [ ] Standard vendor onboarding packet pre-assembled
- [ ] COI request submitted to insurance broker — buyer may require named additional insured
- [ ] MSA / order form in `[your paper / their paper]` ready for legal review
- [ ] Pre-approved redline positions for: liability cap, indemnification scope, auto-renewal, data ownership, termination for convenience

### Known friction points to flag to Legal
- `[UNKNOWN — whether buyer has rejected our standard MSA terms before]`
- Procurement may require flow-through of buyer's terms; pre-clear with Legal which we accept

### Escalation path
Any redline outside pre-approved positions → `[Head of Legal / GC]` within 24 hours. Deal-side and Legal should be on the same thread, not relay-racing emails.

---

## 3. Implementation Timeline → Professional Services / Customer Success

**Owner requested:** PS Lead or CS Manager
**SLA needed:** Draft timeline within `[3 business days]` for champion to circulate internally.

### Context
- Champion specifically asked for this. That is a buying signal — they are selling internally and need ammunition.
- The timeline is a **sales asset first, an implementation artifact second.** It must make the buyer confident in time-to-value, not just document scope.

### What the timeline must include
- [ ] **Kickoff** — date assumes contract signed by `[target close date]`
- [ ] **Phase 1: Setup & configuration** — duration, who from buyer's team is needed, what they need to prepare
- [ ] **Phase 2: Integration** — list of integrations based on their stated tech stack `[UNKNOWN]`
- [ ] **Phase 3: User onboarding / training** — number of sessions, format, materials
- [ ] **Phase 4: Go-live** — definition of "live," success criteria
- [ ] **First value milestone** — when does the buyer see the first measurable outcome (this is the number the champion will quote upward)
- [ ] **30/60/90 day check-ins** — named CSM, cadence

### Format
One-page visual (Gantt or swimlane) + one-page narrative. Champion should be able to drop it into a slide deck without reformatting.

### Caveats to include
- Timeline is contingent on contract signature by `[date]` and buyer-side resource availability
- Assumes standard integration scope; custom work would adjust dates

---

## Coordination Mechanics

### Single source of truth
Create a shared internal channel: `#deal-[company-name]-close`
Members: AE (you), SE, Security lead, Legal/Deal Desk, PS Lead, AE Manager.

### Weekly checkpoint
15-min standup until close. Agenda:
1. What moved this week
2. What is blocked
3. What does the buyer see next

### External-facing artifact
All three workstreams feed into the **Mutual Close Plan** shared with the champion. Update it weekly so the buyer sees momentum.

---

## Suggested Next Action (You, Today)

1. Fill in the `[UNKNOWN]` fields above from CRM.
2. Send three separate handoff messages (Security, Procurement/Legal, PS) — do not bundle into one. Each owner needs a clean ask.
3. Reply to the champion within 24 hours with: "I have engaged our security, procurement, and implementation teams. You will have the timeline by `[date]`, and we are turning around the security questionnaire by `[date]`. I will share both with you directly."
4. Schedule a 15-min internal sync within 48 hours to align all three owners on the close date.

---

**Boundary note:** A full `deal-playbook.md` was not generated because the task scoped to the internal handoff only. If you want the full playbook (company intelligence, MEDDIC, objection matrix, negotiation strategy, mutual close plan), provide the deal context fields listed at the top and I will produce it.
