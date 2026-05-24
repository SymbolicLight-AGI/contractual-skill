# Internal Handoff: EastRiver Bank — Security & Procurement Approval

**Deal:** EastRiver Bank  
**Product:** Workflow automation platform  
**Stage:** Proposal  
**Deal Size:** $260k ARR  
**Target Close Date:** 2026-07-15  
**Primary Contact / Champion:** Sam Patel, Director of Transformation  
**Economic Buyer:** COO  
**Current Blockers:** Procurement vendor onboarding, security evidence, data residency questions  
**Customer-Facing Outreach:** Do **not** send yet. Internal alignment only.

---

## 1. Executive Summary

EastRiver Bank is in Proposal stage for a **$260k ARR** workflow automation platform opportunity. The deal is currently blocked by non-commercial approval steps: **vendor onboarding**, **security review**, and **data residency confirmation**.

This is not yet a pricing or value objection. The immediate risk is operational drag: if procurement and security are not handled in parallel this week, the deal may slip past the **2026-07-15** target close date.

The priority is to prepare a clean internal package so the AE/CS/Security/Legal teams can respond quickly once Sam or EastRiver’s procurement/security teams engage.

---

## 2. Deal Risk Assessment

### Current Risk Level: **Moderate to High**

The business buyer appears engaged through Sam Patel, but the deal is exposed because:

- Procurement vendor approval is not yet complete.
- Security requires SOC 2 evidence.
- Data residency questions are unresolved.
- Economic buyer, the COO, is identified but engagement level is `[UNKNOWN]`.
- Procurement timeline is `[UNKNOWN]`.
- Security review timeline is `[UNKNOWN]`.
- Required EastRiver vendor forms are `[UNKNOWN]`.

### Velocity Risk Factors Present

- [x] Procurement or legal review timeline unknown  
- [x] Security review requirements not fully validated  
- [x] Data residency requirement unresolved  
- [x] Economic buyer identified but engagement status unknown  
- [x] No confirmed mutual close plan for approval steps  

**Velocity Risk Score:** 5/10  
**Interpretation:** High velocity risk. Deal can still close by 2026-07-15, but only if procurement and security are run in parallel immediately.

---

## 3. Internal Owners Needed

| Workstream | Internal Owner | Backup | Status | Immediate Need |
|---|---:|---:|---|---|
| Commercial / AE coordination | `[AE NAME UNKNOWN]` | Sales Manager | Open | Own overall deal timeline |
| Security evidence package | Security / Trust team | Solutions Engineer | Needed | Prepare SOC 2 and security collateral |
| Data residency response | Security / Compliance / Product | Legal | Needed | Confirm supported hosting / residency position |
| Vendor onboarding | Deal Desk / RevOps / Legal | AE | Needed | Prepare tax, insurance, company, and compliance docs |
| Contract / legal terms | Legal | Deal Desk | Not started / `[UNKNOWN]` | Prepare for MSA, DPA, security addendum |
| Executive alignment | AE / Sales Leader | COO sponsor if available | Needed | Confirm COO path to approval |

---

## 4. Security Handoff Brief

### Security Review Issue

EastRiver Bank wants **SOC 2 evidence** and has questions about **data residency**.

Because EastRiver is a bank, expect a heavier security review than a normal commercial account. They may ask about:

- SOC 2 Type II report
- Information security policies
- Data encryption at rest and in transit
- Access controls
- SSO / SAML / SCIM support
- Audit logs
- Incident response process
- Business continuity / disaster recovery
- Vendor subprocessors
- Data retention and deletion
- Data residency and hosting geography
- Penetration testing
- Vulnerability management
- Privacy / DPA terms
- Regulatory posture for financial services

### Required Internal Security Package

Prepare the following **before** sending anything externally:

| Item | Status | Owner | Notes |
|---|---|---|---|
| SOC 2 Type II report | Needed | Security / Trust | Confirm current report date and NDA requirement |
| Bridge letter, if SOC 2 period is stale | Needed if applicable | Security | Useful if report period has gap |
| Security overview / trust packet | Needed | Security | Standard bank-friendly package |
| Completed CAIQ / SIG Lite / questionnaire template | If available | Security | Speeds review if EastRiver has not sent theirs yet |
| Pen test summary or executive attestation | Needed if available | Security | Do not send raw report unless policy allows |
| Data encryption summary | Needed | Security | Include at-rest and in-transit details |
| Access control summary | Needed | Security / Product | Include RBAC, SSO, MFA, audit logs |
| Incident response policy summary | Needed | Security | External-safe version |
| BCP / DR summary | Needed | Security | Include RTO/RPO if approved |
| Subprocessor list | Needed | Legal / Security | Confirm current list |
| DPA template | Needed | Legal | Especially if personal or regulated data involved |
| Data residency statement | Critical | Product / Security / Legal | Must be precise; do not improvise |

---

## 5. Data Residency Handling

### Current Known Concern

EastRiver has asked data residency questions. Details are `[UNKNOWN]`.

### Immediate Internal Questions to Answer

Before any customer-facing response, confirm:

1. Where is EastRiver’s production data hosted?
2. Can customer data be restricted to a specific geography?
3. Are backups stored in the same region?
4. Are logs, metadata, or telemetry stored outside the primary region?
5. Do subprocessors process or store data outside the requested geography?
6. Is data residency contractual, configurable, or best-effort?
7. Are there exceptions for support access, monitoring, or analytics?
8. Does the product support customer-managed keys or encryption controls?
9. Are there any limitations specific to financial services customers?
10. Who internally is authorized to approve the formal data residency language?

### Recommended Internal Position

Do **not** let the AE or SE answer data residency from memory.

Use only approved language from Security, Legal, or Product. For a bank, a vague answer like “we use AWS and can support that” is risky and may create contract exposure.

---

## 6. Procurement Handoff Brief

### Procurement Blocker

EastRiver procurement requires vendor approval. The exact process is `[UNKNOWN]`.

### Likely Vendor Approval Requirements

Prepare these documents internally now:

| Document / Requirement | Status | Owner |
|---|---|---|
| W-9 / tax form | Needed | Finance / RevOps |
| Certificate of insurance | Needed | Finance / Legal |
| Vendor information form | Pending EastRiver form | AE / RevOps |
| Banking / remittance details | Needed | Finance |
| Legal entity name and address | Needed | Legal / Finance |
| DUNS / company registration details | If required | Finance |
| SOC 2 report | Needed | Security |
| Information security questionnaire | Pending | Security |
| Privacy policy | Needed | Legal |
| DPA | Needed | Legal |
| MSA / order form | Needed | Legal / Deal Desk |
| Accessibility statement | If applicable | Product / Legal |
| Business continuity summary | Needed | Security |
| Subprocessor list | Needed | Legal / Security |

### Procurement Questions We Need Sam to Answer Later

Do not send yet, but prepare to ask Sam:

1. Who owns vendor onboarding at EastRiver?
2. Has a vendor intake form already been opened?
3. What is the average approval timeline for a new software vendor?
4. Is security review required before procurement approval, or can they run in parallel?
5. Does legal review happen before or after security approval?
6. Who signs the order form?
7. Does the COO need to approve before procurement starts?
8. Are there preferred contract terms we should know about?
9. Are there insurance minimums?
10. Are there data residency or regulatory requirements specific to EastRiver policy?

---

## 7. Internal Action Plan

### Next 24 Hours

1. **AE to open internal deal desk / approval thread**
   - Owner: `[AE NAME UNKNOWN]`
   - Due: 2026-05-24
   - Include: deal size, close date, blockers, stakeholders, and request for security/procurement support.

2. **Security to confirm SOC 2 package availability**
   - Owner: Security / Trust team
   - Due: 2026-05-24
   - Confirm:
     - SOC 2 Type I or Type II
     - Report period
     - NDA requirement
     - Whether a bridge letter is needed
     - Approved external sharing process.

3. **Legal/Product/Security to align on data residency**
   - Owner: Legal + Security + Product
   - Due: 2026-05-24
   - Output: approved internal answer and customer-safe language.

---

### Next 48 Hours

4. **RevOps / Finance to prepare vendor onboarding packet**
   - Owner: RevOps / Finance
   - Due: 2026-05-25
   - Include: W-9, COI, legal entity details, remittance info, standard vendor docs.

5. **AE and SE to map approval path**
   - Owner: AE + SE
   - Due: 2026-05-25
   - Goal: determine what we still need from Sam before involving procurement/security directly.

6. **Legal to prepare contract posture**
   - Owner: Legal
   - Due: 2026-05-25
   - Include:
     - Standard MSA
     - DPA
     - Security addendum position
     - Data residency language
     - Redline tolerance.

---

### This Week

7. **Create internal “EastRiver Approval Packet”**
   - Owner: AE / Deal Desk
   - Due: 2026-05-29
   - Folder should include:
     - Proposal
     - Order form draft
     - Security packet
     - SOC 2 sharing instructions
     - Vendor onboarding documents
     - Data residency approved response
     - Legal templates
     - Mutual close plan draft.

8. **Prepare but do not send customer-facing procurement/security email**
   - Owner: AE
   - Due: 2026-05-29
   - Draft should be reviewed by Security and Legal before sending.

9. **Confirm whether COO engagement is required before approval process starts**
   - Owner: AE / Sales Leader
   - Due: 2026-05-29
   - Risk: If Sam cannot activate procurement without COO approval, the deal may stall.

---

## 8. Suggested Internal Slack / Email Handoff

Subject: **EastRiver Bank — Security + Procurement Handoff Needed for $260k ARR Proposal**

Team,

EastRiver Bank is in Proposal stage for a $260k ARR workflow automation opportunity targeting close by **2026-07-15**. The business champion is **Sam Patel, Director of Transformation**. Economic buyer is the **COO**.

The deal is currently blocked by three approval items:

1. Procurement vendor onboarding  
2. Security request for SOC 2 evidence  
3. Data residency questions  

No customer-facing message should be sent yet. We need to prepare the internal package first.

**Requested support:**

- **Security / Trust:** Confirm what SOC 2 evidence we can share, whether NDA is required, and provide the approved security packet.
- **Product / Security / Legal:** Confirm approved data residency language. Please do not rely on informal answers here; EastRiver is a bank.
- **RevOps / Finance:** Prepare vendor onboarding documents: W-9, COI, legal entity info, remittance details, and standard vendor profile materials.
- **Legal:** Prepare standard MSA/DPA/security addendum position and identify redlines we can pre-approve.
- **AE / Deal Desk:** Create one EastRiver approval packet and mutual close plan draft.

Target internal readiness date: **2026-05-29**  
Target customer approval path launch: **after internal Security + Legal approval**

Key risk: If we wait for EastRiver to send forms before preparing, we may lose one to two weeks and jeopardize the 2026-07-15 close date.

---

## 9. Mutual Close Plan Draft — Internal Version

Do not send externally yet.

| Date | Milestone | Owner | Status |
|---|---|---|---|
| 2026-05-24 | Confirm SOC 2 availability and sharing rules | Security / Trust | Pending |
| 2026-05-24 | Confirm approved data residency position | Security / Product / Legal | Pending |
| 2026-05-25 | Prepare vendor onboarding packet | RevOps / Finance | Pending |
| 2026-05-25 | Prepare MSA, DPA, and security terms posture | Legal | Pending |
| 2026-05-29 | Assemble EastRiver approval packet | AE / Deal Desk | Pending |
| 2026-06-01 | Align internally on customer-facing response | AE / Security / Legal | Pending |
| 2026-06-03 | Send approved security/procurement response to Sam | AE | Not started |
| 2026-06-07 | Receive EastRiver vendor forms / security questionnaire | Sam / EastRiver | Not started |
| 2026-06-14 | Submit completed procurement and security materials | AE / Security / Legal | Not started |
| 2026-06-24 | Security review complete | EastRiver Security | Not started |
| 2026-06-28 | Procurement vendor approval complete | EastRiver Procurement | Not started |
| 2026-07-03 | Contract redlines returned | EastRiver Legal | Not started |
| 2026-07-08 | Final terms agreed | Both | Not started |
| 2026-07-15 | Contract signed | COO / Authorized Signer | Target |

---

## 10. Critical Gaps to Resolve

| Gap | Why It Matters | Owner | How to Close |
|---|---|---|---|
| EastRiver procurement owner unknown | We cannot manage timeline without knowing process owner | AE / Sam later | Ask Sam who owns vendor onboarding |
| Security questionnaire unknown | We do not know review scope | AE / Security | Prepare standard packet, then request their required format |
| Data residency requirement unclear | Could become a hard blocker if unsupported | Product / Security / Legal | Confirm exact supported position before customer response |
| COO engagement level unknown | Sam may not have authority to push procurement | AE / Sales Leader | Confirm whether COO has approved moving to vendor review |
| Legal review sequence unknown | Legal may add 2–3 weeks if started late | AE / Legal | Ask whether legal can start in parallel with security |
| SOC 2 sharing requirements unknown | Delays if NDA or portal access is needed | Security / Legal | Confirm process now |

---

## 11. Internal Guidance for the AE

### Do Now

- Do not send a customer-facing message yet.
- Do not answer data residency informally.
- Do not send SOC 2 without confirming sharing rules.
- Start internal security, legal, finance, and deal desk alignment immediately.
- Push for all approval workstreams to run in parallel.

### Avoid

- Saying “security should be easy.”
- Treating procurement as a post-verbal-commit step.
- Waiting for Sam to chase internal teams alone.
- Offering custom data residency commitments without Legal/Product approval.
- Sending raw security documents before NDA / sharing policy is confirmed.

### Recommended Internal Deal Posture

This deal is commercially viable but operationally exposed. The close plan should shift from “proposal follow-up” to “approval project management.” The AE should act as quarterback across procurement, security, legal, and the champion.

---

## 12. Single Most Important Next Action

**By 2026-05-24, create an internal EastRiver approval thread with Security, Legal, Product, RevOps, Finance, Deal Desk, and the AE, requesting confirmation of:**

1. SOC 2 evidence package  
2. Data residency approved language  
3. Vendor onboarding packet  
4. Legal/DPA/security addendum posture  
5. Internal readiness by 2026-05-29  

No external message should be sent until those four items are confirmed.
