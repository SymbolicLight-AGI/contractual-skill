# Deal Closer Playbook — ACME Manufacturing (Expansion)

**Status:** Partial playbook – multiple inputs are `[UNKNOWN]`.  
**Audience:** Internal use by account executive and sales manager.

---

## Deal Snapshot

| Field | Value |
|-------|-------|
| Company | ACME Manufacturing |
| Deal Type | Expansion (existing customer) |
| Product / Service | `[UNKNOWN]` |
| Pricing Model | `[UNKNOWN]` |
| Deal Size | $80 k ARR |
| Current Deal Stage | `[UNKNOWN]` |
| Primary Contact (Buyer) | VP Operations (name `[UNKNOWN]`) |
| Target Close Date | This quarter (end-of-quarter) |
| Competitor | Incumbent spreadsheet workflow (status quo) |
| Known Blocker | IT security review |

---

## Known Facts And Unknowns

**Fact (User-provided):**
- ACME Manufacturing is expanding an existing relationship.
- Deal size: $80 k ARR (expansion).
- Buyer: VP Operations.
- Active blocker: IT security review.
- Primary competitor: existing manual/spreadsheet process.
- Target close: this quarter.

**Inference:**
- The VP Operations likely holds budget authority for operational technology purchases at this ARR level, making them a probable economic buyer.
- The “expansion” label suggests there is already a footprint or contract; the rep has a relationship to leverage.
- The incumbent spreadsheet workflow indicates the problem domain involves operational data (maintenance, scheduling, inventory, quality, or similar) currently managed in Excel or similar tools.
- IT security review could be a formal gating step and may carry the power to slow or stop the deal if not engaged early.

**Unknown:**
- Product/service being sold, pricing structure, and licensing model.
- Current deal stage and sales methodology stage (e.g., discovery, evaluation, proposal).
- Primary contact name, communication preferences, and internal influence.
- Full buying committee: champion, technical evaluator, user buyers, coach, economic buyer (confirmed), procurement/legal, executive sponsor.
- Decision criteria, timeline pressures, and procurement process.
- Existing contract value, current usage, and expansion motivation (new capability, seats, module).
- IT security review specifics: requirements, timeline, past history, standard process.
- Competition beyond spreadsheets (e.g., point solutions, other vendors they may evaluate).

---

## Company Intelligence

- **Source:** User-supplied synthetic facts only. No web research was requested or performed.
- **Known:** ACME is a manufacturing company. The deal center is Operations, suggesting the solution targets a manufacturing operations function (e.g., production tracking, maintenance, safety, supply chain, or plant management).
- **Gap:** Without the product name or operational context, company sizing, recent news, technology stack, and business priorities remain unknown. A complete intelligence summary requires additional inputs or a research call-out.
- **Recommendation:** When appropriate and if a research tool is permitted, gather public data on ACME’s manufacturing footprint, recent operational initiatives, and any security certification requirements (ISO 27001, SOC 2, NIST, etc.) to better understand the IT security context.

---

## Buying Committee Map

| Role | Person/Title | Influence | Status | Notes |
|------|--------------|-----------|--------|-------|
| Economic Buyer | VP Operations (name `[UNKNOWN]`) | High | `[UNKNOWN]` | Likely holds or influences the operational budget. Also may be champion if actively advocating. Fact: identified as buyer. |
| Champion | `[UNKNOWN]` | High | `[UNKNOWN]` | Not yet identified. If the VP Ops is driving, they are likely champion. Confirm with anecdotal evidence. |
| Technical Evaluator | `[UNKNOWN]` | Medium-High | `[UNKNOWN]` | Could be an operations analyst, system architect, or someone from IT/OT. |
| User Buyer(s) | `[UNKNOWN]` (e.g., plant managers, shift supervisors, operators) | Low-Medium | `[UNKNOWN]` | Their adoption matters for expansion success. Identify key users. |
| Coach | `[UNKNOWN]` | Medium | `[UNKNOWN]` | Not identified. Could be a supervisor or existing power user from the initial deployment. |
| Blocker | IT Security (team/individual `[UNKNOWN]`) | High | Active blocker | Security review is currently a gate. Need to understand scope, fears, and decision criteria. |
| Procurement / Legal | `[UNKNOWN]` | Medium | `[UNKNOWN]` | For an expansion, there may be a streamlined procurement path, but legal T&Cs (DPA, SLA) might still be required. |
| Executive Sponsor | `[UNKNOWN]` | Low-Medium | `[UNKNOWN]` | If VP Ops reports to SVP Manufacturing or COO, they may need to sign off for strategic alignment. |

**Action:** The rep must identify each unknown role and map the relationship to the VP Ops to build an influence map.

---

## Deal Qualification And Risk

**Qualification Highlights**
- Existing relationship reduces procurement friction and demonstrates proven initial value.
- $80 k ARR expansion suggests strong user adoption or a new high-value capability.
- VP Operations as buyer places the deal in an operational budget line, often more insulated from discretionary freezes.

**Risk Assessment**

| Risk | Type | Severity | Mitigation |
|------|------|----------|------------|
| IT security review delay or rejection | Process/Technical Risk | High | Engage security owner immediately; request formal security questionnaire; provide standard security documentation (SOC 2, pen test summaries, architecture) ahead of their request; offer a brief technical call. |
| Status quo / spreadsheet attachment | Adoption Risk | Medium | Quantify cost of manual errors, time wasted, and compliance risks of spreadsheets; build an ROI model co-owned with VP Ops. |
| Absence of clear champion besides VP Ops | Political Risk | Medium | Identify a day-to-day champion from the operations team to sustain momentum. |
| Unknown decision criteria and evaluation process | Process Risk | High | Immediately schedule a joint call with VP Ops to confirm “what good looks like” and how success will be measured. |
| Quarter-end slippage due to missing procurement/legal steps | Process Risk | Medium-High | Map the exact steps and timelines; start contract review in parallel; get legal’s redlines early. |
| Unidentified competition beyond spreadsheets | Competitive Risk | Low (currently) | Confirm with VP Ops that no other vendors are being evaluated; remain vigilant. |

**Close-Date Realism:** Without known stage and security review duration, an end-of-quarter close is **at risk**. The timeline is aggressive; a slip of the security review alone can push close past the quarter.

---

## Objection Playbook

| Anticipated or Known Objection | Internal Response Guidance | Owner | Evidence/Proof Point to Prepare |
|-----------------------------------|-----------------------------|-------|----------------------------------|
| “We’ve always done it in spreadsheets and it works fine.” | Acknowledge comfort but highlight hidden costs: manual errors, version control, auditability, time lost grooming data. Lead with peer manufacturing examples where shift from spreadsheets reduced downtime or improved compliance. | AE / VP Ops | ROI case study, spreadsheet risk quantification, demo of real-time collaboration or automation. |
| “IT security won’t approve this unless it meets our standards.” | Already flagged as an active blocker. Do not dismiss. Instead: co-create a security roadmap; offer a dedicated security briefing; provide architecture diagrams, data flow, encryption details, and any third-party attestations (SOC 2, ISO 27001). Align with IT’s standard review template early. | SE / Security team liaison | Security whitepaper, compliance certifications, customer references who passed similar security reviews. |
| “We can’t justify $80k for this right now.” | Reframe in terms of operational savings or risk reduction. Break even a conservative estimate (e.g., 10% efficiency gain, error reduction) against $80k to show payback period. If expansion is a new module, show incremental value. | AE / VP Ops | Business case based on actual usage data from current deployment, not assumptions. |
| “We need to check with the plant managers first.” | Identify user buyers and include them in the evaluation. Run a proof-of-concept or workshop with a few front-line users to build bottom-up pull. | AE / VP Ops | Pilot success stories, quick-start user testimonials from similar roles. |

**Action:** Co-own an objection-handling document with the VP Ops, so they can advocate internally with consistent talking points.

---

## Competitive Positioning

**Competitor:** Incumbent spreadsheet workflow (status quo).

| Value Dimension | Spreadsheet Default | Our Solution (generic placeholder – tailor to product) |
|-----------------|----------------------|--------------------------------------------------------|
| Data Integrity | Manual data entry, version conflicts, formula breaks. | Single source of truth, validation rules, audit trails. |
| Collaboration | Emailed files, siloed sheets, no real-time sync. | Real-time collaboration, role-based views, notifications. |
| Compliance & Traceability | Limited; hard to prove who changed what and when. | Full change logs, e-signatures, compliance reports. |
| Scalability | Brittle across plants/shifts; requires manual consolidation. | Multi-site operations ready, automated roll-ups, APIs. |
| Mobility / Access | Typically desktop-bound; security issues with shared files. | Secure cloud/mobile access, SSO, granular permissions. |
| Time-to-Insight | Hours spent consolidating and charting manually. | Pre-built dashboards, automated alerts, trend analysis. |

**Strategy:** Never attack the spreadsheet (people take it personally). Instead, position the spreadsheet as a starting point and the solution as the next logical maturity step. Use the line: “Many of our best customers started with your exact spreadsheet process; they made the leap when they couldn’t scale analytics or security across three shifts.” This neutralizes the emotional attachment while making the champion look forward-thinking.

---

## Closing Strategy

Given the unknown deal stage, the strategy is built around the known blocker (security) and the quarter-end timeline. It assumes the rep already has a verbal agreement with VP Ops to move forward.

**Phase 1 – Security Unblock (immediate, week 1)**
- Identify the exact IT security owner, request their review checklist/template.
- Send our standard security package (architecture, compliance, pen test, SOC 2 if available).
- Schedule a 30‑min technical deep-dive between our security/engineering and ACME’s IT.
- Ask VP Ops to put a priority flag on the security review tied to quarter-end business need.

**Phase 2 – Value Re-validation & User Buy-in (week 1‑2)**
- Hold a workshop with 2‑3 key plant managers or shift leads to demonstrate real-time benefits and collect “quick win” use cases.
- Quantify the cost of the status quo using data from their current spreadsheet environment (or from the existing deployment).
- Solidify VP Ops as an internal sponsor by equipping them with a one‑page executive summary that ties the expansion to a manufacturing‑specific KPI (e.g., OEE, downtime, compliance score).

**Phase 3 – Procurement & Legal (week 2‑3, parallel with security)**
- Confirm whether procurement is needed for an expansion or if it falls under an existing MSA addendum.
- If a new order form or contract is required, initiate review early. Share a draft with clear terms and get redlines back by mid‑period.

**Phase 4 – Final Negotiation & Close (week 3‑4)**
- Re-confirm mutual close plan with VP Ops and any other required approvers.
- Use end-of-quarter timing as a credible event (e.g., “to ensure onboarding and start of value capture in Q1, we need sign-off by X”).
- Escalate only if necessary, but never bypass security or legal gates.

**Human gates** apply for all customer-facing commitments, discounts, terms changes, and security representations.

---

## Mutual Close Plan

| Milestone | Owner | Target Date | Dependency | Risk |
|-----------|-------|--------------|------------|------|
| 1. Identify full buying committee & decision process | AE + VP Ops | Week 1, Day 2 | Access to VP Ops | If VP Ops delays, timeline compresses |
| 2. Submit security questionnaire/documentation | AE / SE | Week 1, Day 3 | IT security contact identified | IT may request additional data |
| 3. Technical security deep-dive call completed | SE + IT Security | Week 1, Day 5 | IT availability | Scheduling conflict |
| 4. User validation session with 2+ plant managers | AE + VP Ops + User Buyers | Week 2, Day 3 | Buyers’ availability | Not required for signature but reduces adoption risk |
| 5. IT security conditional approval (or list of required remediations) | IT Security | Week 2, Day 7 | Prior steps | Remediation work could add weeks; have backup buffer |
| 6. Draft contract sent for legal/procurement review | AE + Legal contact | Week 3, Day 1 | Security sign-off (if it’s a legal pre-req) | Redline back-and-forth delays |
| 7. Final terms agreed, internal approvers signed | VP Ops + Procurement | Week 4, Day 3 | All prior steps | End-of-quarter pressure can cause rushed decisions; avoid last-minute surprises |
| 8. Contract signed and PO issued | VP Ops / Procurement | End of quarter | No remaining blockers | Quarter-close workload at customer may delay execution |

**Action:** Put this plan on a shared timeline (internal only) and update daily. Any slip on security review must be communicated immediately to the sales manager.

---

## Next 3 Actions

1. **Complete deal discovery (rep)**  
   Gather missing inputs: exact product/service, current deal stage, VP Ops name, full buying committee, decision criteria, procurement path, and security review specifics.  
   *(Action, based on Unknown gaps)*

2. **Schedule IT security introduction call (rep + SE)**  
   Get the security contact name and immediately send our security package. Book a 30-minute technical call within 3 business days.  
   *(Action, mitigates highest risk)*

3. **Build joint value hypothesis with VP Ops (rep)**  
   Meet with VP Ops to confirm “what success looks like”, co-author an internal justification document, and ask if they will champion the initiative. Simultaneously, identify a front-line operational contact for user validation.  
   *(Action, strengthens champion and creates internal advocacy)*

---

## Human Gates And Handoffs

- **Human Gate: Customer-facing commitments.** Any promise of implementation date, support SLA, feature roadmap, or integration capability requires explicit VP of Sales or Sales Manager sign-off.
- **Human Gate: Discount/pricing concessions.** Any deviation from the standard $80k ARR structure (discount, extended payment terms, service credits) must be approved by Sales Manager and Finance.
- **Human Gate: Security/legal representations.** Only authorized security and legal representatives may provide compliance statements or accept liability clauses. Escalate to the dedicated security/legal team.
- **Human Gate: Risk acceptance.** The decision to proceed without full security clearance or to accept a compressed timeline risk rests with the Sales Manager, not the rep.

**Handoffs after close (plan ahead):**
- **Customer Success / Implementation owner:** for onboarding and deployment planning.
- **Technical support / solutions engineer:** for post-signature configuration.
- **Legal / Procurement (internal):** for contract filing and compliance.

---

## Research Sources Or Evidence Gaps

- **Sources:** This playbook was built exclusively from the synthetic deal facts provided; no external research was conducted.
- **Evidence Gaps:**
  - Product features, differentiators, and existing case studies from the current customer relationship.
  - Detailed ACME Manufacturing firmographics, affected plants, and operational KPIs.
  - IT security standards the customer enforces (e.g., NIST, IEC 62443, ISO 27001).
  - Procurement and legal approval steps specific to ACME’s expansion process.

**Recommendation:** When a browsing tool is permitted, fill these gaps with current public data and customer-provided documents before finalizing the playbook.
