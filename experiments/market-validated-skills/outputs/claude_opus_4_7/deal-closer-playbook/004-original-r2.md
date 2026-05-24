# Internal Handoff Brief: EastRiver Bank — Procurement & Security Unblock

**Scope note:** You asked for an internal handoff to unblock procurement and security. This is not the full deal-playbook.md generation — it's a focused internal-only artifact. No customer-facing message drafted, per your instruction. If you want the full playbook written to `deal-playbook.md` after this, say the word.

**Research note:** I did not run WebSearch for EastRiver Bank in this pass because the blockers are internal-process driven (our procurement/security readiness), not external-intel driven. Flag if you want me to pull EastRiver's recent regulatory posture, data residency requirements by jurisdiction, or recent banking-sector security incidents to strengthen the security narrative.

---

## Deal Snapshot

| Field | Value |
|---|---|
| Account | EastRiver Bank |
| Product | Workflow automation platform |
| Stage | Proposal |
| ARR | $260k |
| Target Close | 2026-07-15 |
| Champion | Sam Patel, Director of Transformation |
| Economic Buyer | COO `[NAME UNKNOWN]` |
| Procurement Contact | `[UNKNOWN — must identify]` |
| Security/InfoSec Contact | `[UNKNOWN — must identify]` |
| Data Residency Requirement | `[UNKNOWN — must clarify with Sam]` |

---

## Why This Deal Is Stuck (Honest Read)

This is a process stall, not a value stall. Sam is bought in. The COO is the signer. But banking buyers do not move past proposal without:

1. A vendor passing procurement's onboarding gate (financial viability, insurance, references, MSA fit).
2. Security signing off on evidence (SOC 2 Type II minimum, often more).
3. Data residency answered definitively — in banking this is a hard gate, not a negotiation.

If we don't drive the handoff internally and arrive with a complete packet, this deal slips past 2026-07-15.

**Velocity risk: HIGH on process, LOW on value.**

---

## Internal Handoff Plan

### Handoff 1 → Security / Trust Team

**Owner:** AE → Trust/Security lead `[ASSIGN]`
**Deadline to package:** Within 3 business days

**Package contents:**
- [ ] SOC 2 Type II report (most recent, under NDA)
- [ ] SOC 2 bridge letter if report is >6 months old
- [ ] Penetration test executive summary (most recent)
- [ ] Data flow diagram for the workflow automation platform
- [ ] Encryption at rest and in transit specs
- [ ] SSO / SCIM / RBAC documentation
- [ ] Subprocessor list
- [ ] Incident response and breach notification policy
- [ ] Business continuity / DR documentation
- [ ] Data residency options matrix — which regions we host in, can we commit to a specific region for EastRiver
- [ ] Pre-filled CAIQ or SIG Lite if we have one on file
- [ ] Banking-specific: any FFIEC, GLBA, or equivalent alignment statements

**Open questions for Security to resolve before sending:**
- What is our committed data residency posture? Can we offer a single-region deployment if EastRiver requires it?
- Do we have any prior bank or financial services customers we can name as having passed similar review? (Needed for procurement references too.)
- Is there anything in our current SOC 2 with exceptions that we should pre-explain rather than let them find?

---

### Handoff 2 → Procurement / Vendor Management (Ours)

**Owner:** AE → Deal Desk / Finance Ops `[ASSIGN]`
**Deadline to package:** Within 3 business days

**Package contents:**
- [ ] Standard MSA + DPA ready for redline
- [ ] W-9 / tax documentation
- [ ] Certificate of insurance (verify limits meet bank vendor minimums — typically $5M+ cyber, $2M+ E&O; confirm EastRiver's requirement)
- [ ] Audited financials or financial viability statement (banks frequently require this — confirm what tier of disclosure we can provide)
- [ ] D&B number / business registration
- [ ] Customer references — 2-3, ideally one in financial services
- [ ] Pricing approval pre-cleared at $260k ARR with standard banking terms (net 30/45/60 options pre-approved)

**Open questions for Deal Desk:**
- What concessions are pre-approved for a regulated-industry close? (e.g., enhanced indemnity caps, breach notification SLAs, audit rights)
- Can we pre-approve a single-region hosting commitment in the MSA if needed?

---

### Handoff 3 → Legal

**Owner:** AE → Legal `[ASSIGN]`
**Deadline:** Brief Legal now; they don't need to act until redlines arrive

**Brief to Legal:**
- Banking customer, expect heavy redlines on: liability caps, indemnification (especially data breach), audit rights, regulatory examiner access clauses, termination for convenience, data deletion SLAs
- Flag in advance which of these we will move on and which are red lines
- Confirm we can support a regulator-examination clause (most banks require this)

---

## Information We Need From Sam (Before Going Customer-Facing)

You said no customer message yet — agreed. But when we do reach out, we need answers to these. Start a list to ask Sam in the next scheduled touchpoint:

1. Procurement contact name, email, and process steps EastRiver uses (do they use a portal like Coupa, Ariba, or a custom intake?)
2. Security contact name and which questionnaire format they'll send (SIG, CAIQ, custom)
3. Data residency requirement — specific region, or just "in-country"?
4. COO's name and how Sam wants to bring them in
5. Whether EastRiver requires on-site security review, vendor day, or remote-only
6. Their typical procurement cycle time for a vendor of our size — sets a realistic close date
7. Any preferred or blocked subprocessors (some banks block specific cloud regions or vendors)

---

## Revised Close Date Reality Check

Target: **2026-07-15**

Banking procurement + security review typically runs **6-12 weeks** from packet submission. If we submit a complete packet within 2 weeks, 2026-07-15 is achievable but tight. If data residency requires a non-standard deployment commitment, add 2-4 weeks.

**Recommendation:** Internally treat 2026-07-15 as the stretch case and 2026-08-30 as the realistic case. Do not slip the date with Sam yet — first see what the procurement timeline actually looks like once we identify their contact.

---

## Next 3 Actions (This Week)

1. **AE — by end of day tomorrow:** Assign internal owners for Security, Deal Desk, and Legal handoffs. Send each owner this brief with their section highlighted.
2. **AE — within 3 business days:** Confirm with Security and Deal Desk that the full evidence packet is assembled and ready to ship the moment we get procurement and security contacts from Sam.
3. **AE — next Sam touchpoint (when appropriate):** Get the 7 questions above answered. Do not send the packet to Sam — send it directly to EastRiver's procurement and security contacts once identified, with Sam cc'd.

---

## Gaps Flagged

- `[UNKNOWN]` COO name
- `[UNKNOWN]` Procurement contact at EastRiver
- `[UNKNOWN]` Security/InfoSec contact at EastRiver
- `[UNKNOWN]` Specific data residency requirement
- `[UNKNOWN]` Whether we have a current financial-services reference customer
- `[UNKNOWN]` Our pre-approved concession envelope for regulated-industry deals

---

Want me to: (a) generate the full `deal-playbook.md` next, (b) run WebSearch on EastRiver Bank's regulatory and data residency context, or (c) draft the customer-facing packet email for when you're ready to send it?
