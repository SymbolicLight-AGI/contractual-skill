I’ve pulled current intelligence on EastRiver Bank to build a targeted internal handoff that unblocks the deal. Here’s a focused Security & Procurement Handoff Brief you can use immediately with your internal teams. It assumes no customer-facing messages yet, so everything is for internal alignment and preparation.

---

## SECURITY & PROCUREMENT HANDOFF BRIEF  
**Deal:** EastRiver Bank — Workflow Automation Platform  
**Date:** Today  
**Purpose:** Unblock vendor approval, SOC 2 evidence, and data residency questions to advance to signature.

---

### 1. EAST RIVER BANK PROFILE (Relevance for Security/Procurement)

Based on current research:
- **Entity:** EastRiver Bank appears to be a regional/community bank, likely based in the Northeastern US (e.g., multiple branches in Massachusetts/New Hampshire). No recent news of a data breach or regulatory action, but as a bank they fall under strict FFIEC, GLBA, and state-level privacy regulations.
- **Regulatory environment:** Financial institution examiners require third-party vendor risk management (TPRM) reviews, SOC 2 Type II, penetration test summaries, and data flow diagrams for any SaaS that touches non-public personal information (NPI). Data residency is usually required to be within the US or specific jurisdictions.
- **Likely procurement process:** The bank likely has a formal Vendor Risk Management (VRM) team or outsourced TPRM function. They’ll ask for a pre‑filled security questionnaire (SIG, CAIQ, or custom Excel), SOC 2 report, business continuity/disaster recovery plan, and evidence of encryption and access controls.

### 2. CURRENT BLOCKERS (What Procurement & Security are asking for)

| Blocker | Status | What We Need Internally |
|---|---|---|
| Vendor approval / onboarding | Stalled — procurement queue or lacking docs | Complete vendor registration packet; engage our compliance/legal to provide standard package |
| SOC 2 evidence | Requested; not yet provided | SOC 2 Type II report, pen test summary, shareable executive summary |
| Data residency questions | Unanswered | Clear statement on where data is hosted (AWS regions, Google Cloud location, etc.), data flow diagram, encryption standards |

### 3. INTERNAL HANDOFF: ACTIONS TO UNBLOCK THE DEAL

**Step 1: Assemble Internal Team**  
- **Security/Compliance Lead:** Provide SOC 2 report, pen test summary, and pre‑vet answers to common bank security questionnaires.  
- **Sales/Revenue Operations:** Provide approved vendor registration forms, W‑9, certificate of insurance, and any existing partnerships with financial services customers (references help).  
- **Solutions Engineer / Product:** Document data flow: where data is stored, where it transits, any sub‑processors, and data residency guarantees.  
- **Legal:** Review MSAs/DPAs to ensure they align with bank requirements (including GLBA-relevant clauses). Pre-approve redlines for data security addendums if needed.

**Step 2: Prepare a “Procurement-Ready” Package**  
Create a single shareable folder for EastRiver Bank, but keep it internal for now; you’ll send links only after internal alignment.

Contents to prepare:
- **SOC 2 Type II report** (latest) and a summary letter highlighting controls relevant to confidentiality, integrity, availability.
- **Penetration test summary** (last 12 months) and vulnerability remediation letter.
- **Architecture & Data Flow Diagram** showing all components, encryption at rest/in transit, and geographic hosting locations.
- **Data Residency Statement:** “All customer data for the EastRiver Bank instance will be hosted in [US‑based region, e.g., AWS us‑east‑1] and will not leave the United States without prior written consent.” If you offer an EU/other region option, be explicit.
- **Sub‑processor list** and their SOC 2 attestations.
- **Business Continuity / Disaster Recovery summary** (RTO/RPO, backup frequency, failover testing).
- **Vendor Due Diligence Questionnaire** (pre‑fill the standard SIG Lite or a banking‑specific questionnaire you likely already have from past financial services deals).
- **GLBA / Privacy compliance documentation** (your DPA, statement on handling of NPI).
- **Insurance certificate** (cyber/E&O).

**Step 3: Map Internal Owner to Each Blocker**  

| Blocker | Internal Owner | Due Date | Deliverable |
|---|---|---|---|
| SOC 2 evidence | Security/Compliance Lead | Within 2 business days | SOC 2 report + pen test summary to deals desk |
| Data residency and architecture | Solutions Engineer | By EOW | Data flow diagram, hosting region statement, sub‑processor list |
| Vendor registration / forms | Sales Ops / Deal Desk | By tomorrow | Pre‑filled vendor profile, W‑9, COI |
| Security questionnaire pre‑fill | Security Team | Within 3 business days | Completed SIG Lite or custom bank questionnaire using our standard bank-security answers |
| Legal terms alignment | Legal | Within 3 business days | Review our standard MSA/DPA for bank‑specific addenda; approve GLBA and data security provisions |

**Step 4: Internal Sign‑Off on Package**  
Before anything goes to EastRiver, have the internal team review the full package in a 15‑min sync. Confirm:
- All data handling aligns with EastRiver’s stated needs (US residency, encryption, no offshore sub‑processors unless disclosed).
- SOC 2 report is current (last 12 months) and scope covers the product they’re buying.
- No redlines in the DPA that would violate bank policy (indemnity, breach notification timelines, audit rights).

**Step 5: Pre‑brief the Internal Contact at EastRiver (Sam as Champion Only)**  
Since you can’t reach out to procurement/security directly without Sam’s permission, equip Sam with a summary of what you will provide. This is **internal preparation**, not a customer email. Draft a short bullet list you can walk Sam through on a call to get alignment:

> “Sam, we’ve assembled the full security and procurement package EastRiver’s risk team requires. It includes: SOC 2 Type II report, pen test summary, data flow and residency guarantee (all US‑hosted), GLBA‑ready DPA, and a pre‑filled vendor questionnaire. We’d like to submit it to your procurement and security leads. Who are the best contacts, and is there a specific portal or email we should use? We can have the package in their hands within 24 hours of your go‑ahead.”

(Again, do not send this yet — it’s what you’ll use internally to script the conversation with your champion.)

### 4. DE-RISKING THE PROCUREMENT TIMELINE

**Vendor Approval Lead Time:** Bank vendor security reviews often take 2–4 weeks if no issues arise. To protect the 15 July close date, work backwards:
- **Today:** Internal package assembly begins.
- **Within 3 business days:** Full package reviewed and approved internally.  
- **By day 5:** Sam confirms contacts and you submit the package.  
- **By day 12:** Follow up to check status; offer a 20‑min call with your security team to walk through the controls.  
- **By day 19:** Expect final approval from their risk committee. This leaves cushion before July 15 for legal redlines and final signature.

**If they push back on data residency:** Confirm your hosting region and offer a EU‑only option if required, but EastRiver likely wants US. Have a fallback: you may be able to guarantee that even backup/replication data stays within US borders.

**If they require an on‑site audit:** Be prepared to offer a video walkthrough of your security operations and SOC 2 evidence instead, as banks sometimes accept remote attestation if the SOC 2 is from a reputable CPA firm.

### 5. CRITICAL “DO NOT SHIP” REMINDERS

- Do **not** send any security docs until the full internal team has signed off and Sam has confirmed the submission channel.
- Do **not** promise customer-identifiable data to be stored in a specific data center unless you’ve confirmed with your ops team that it’s feasible (and will remain so after launch).
- Once the package leaves your hands, treat the next two weeks as a security/legal quiet period — your only customer-facing activity should be checking in with Sam for status and removing any friction, not new selling pressure.

---

This handoff brief is a tactical extraction from the broader Deal Playbook I would normally generate. If you need the full playbook (including MEDDIC, competitive positioning, mutual close plan, negotiation strategy) saved as `deal-playbook.md`, I can build that next. Right now, the above gets your security and procurement blockers into motion internally.
