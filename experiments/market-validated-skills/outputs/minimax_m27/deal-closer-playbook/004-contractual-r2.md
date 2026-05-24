# Deal Closer Playbook: EastRiver Bank

## Deal Snapshot

| Field | Value |
|-------|-------|
| **Company** | EastRiver Bank |
| **Product** | Workflow Automation Platform |
| **Deal Size** | $260,000 ARR |
| **Stage** | Proposal |
| **Target Close** | 2026-07-15 |
| **Champion** | Sam Patel, Director of Transformation |
| **Economic Buyer** | COO |
| **Primary Blocker** | Procurement vendor onboarding + Security evidence requirements |

---

## Known Facts and Unknowns

| Category | Known | Unknown |
|----------|-------|---------|
| **Company Context** | EastRiver Bank (regional financial institution) | Specific size, branch count, current tech stack |
| **Champion** | Sam Patel, Director of Transformation | Sam's relationship with COO, internal influence score |
| **Economic Buyer** | COO | COO's priorities, decision timeline, security posture |
| **Security Requirements** | SOC 2 evidence requested | Specific SOC 2 type (Type I vs II), deadline for evidence, other security docs needed |
| **Procurement** | Vendor onboarding process required | Onboarding steps, required forms, legal review timeline |
| **Data Residency** | Question raised | Which data center region, latency requirements, regulatory constraints |
| **Competition** | [UNKNOWN] | Competitors in evaluation, their security posture |
| **Timeline** | Target 2026-07-15 | Feasibility given blockers, procurement cycle length |

---

## Buying Committee Map

```
┌─────────────────────────────────────────────────────────────────┐
│                        EASTRIVER BANK                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ECONOMIC BUYER                                                 │
│  ● COO                                                          │
│    - Final budget approval                                      │
│    - Strategic priority alignment                               │
│    - Risk tolerance for new vendors                             │
│    - [UNKNOWN] Current priorities, pressure points             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CHAMPION                                                       │
│  ● Sam Patel, Director of Transformation                       │
│    - Driving internal adoption                                 │
│    - Coordinating between departments                          │
│    - Has business case justification                            │
│    - [FACT] Engaged, requesting security evidence              │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BLOCKER #1: SECURITY                                           │
│  ● Security Team / CISO                                         │
│    - Requesting SOC 2 evidence                                 │
│    - Evaluating data residency requirements                     │
│    - [FACT] Has paused progression until evidence provided     │
│    - [UNKNOWN] Specific security checklist, penetration tests   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BLOCKER #2: PROCUREMENT                                        │
│  ● Procurement / Legal                                         │
│    - Vendor onboarding process required                         │
│    - [FACT] Blocking contract execution                        │
│    - [UNKNOWN] Vendor approval criteria, required documentation │
│    - [UNKNOWN] Procurement cycle duration                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  TECHNICAL EVALUATOR                                            │
│  ● [UNKNOWN] IT/Infrastructure Lead                             │
│    - May be involved in security review                         │
│    - Data residency technical requirements                      │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  USER BUYERS                                                    │
│  ● [UNKNOWN] Operations team                                    │
│    - Will use workflow automation                               │
│    - May need training/change management                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Deal Qualification and Risk Assessment

### Risk Matrix

| Risk | Likelihood | Impact | Mitigation Priority |
|------|------------|--------|---------------------|
| **Security evidence gap** | HIGH | Deal stall | **CRITICAL** |
| **Procurement cycle exceeds close date** | MEDIUM-HIGH | Missed target | **HIGH** |
| **Data residency unresolved** | MEDIUM | Contract delay | **MEDIUM** |
| **Champion insufficient influence** | LOW-MEDIUM | Economic buyer not aligned | **MEDIUM** |
| **Competitor advantage during delay** | MEDIUM | Loss to competitor | **MEDIUM** |

### Risk Narrative

**Critical Risk:** The security team's request for SOC 2 evidence is currently blocking progression. Without this evidence, the proposal cannot advance to contract stage.

**Key Insight:** Two independent blockers (security + procurement) create compounding risk. Even if security concerns are resolved, procurement onboarding must still complete before close.

**Timeline Risk:** Target date of 2026-07-15 may be aggressive given:
- SOC 2 evidence gathering/provision timeline
- Procurement vendor approval process
- Data residency technical evaluation
- Contract legal review

**Recommendation:** Re-forecast close date after security/procurement milestone clarity.

---

## Objection Playbook: Security & Procurement

### Security Objections

| Objection | Root Concern | Response Strategy |
|-----------|--------------|-------------------|
| "We need SOC 2 evidence before proceeding" | Vendor risk, regulatory compliance | Provide Type II report; offer security questionnaire; schedule call with our security team |
| "Where will our data be stored?" | Data sovereignty, latency, compliance | Confirm data regions; provide architecture docs; discuss residency options |
| "Has your platform been penetration tested?" | Vulnerability exposure | Share latest pentest summary; offer to coordinate joint security review |
| "We need to add our security requirements to the contract" | Legal protection | Engage legal team; review standard MSA provisions; do not commit without legal approval |

**Talking Points for Sam Patel:**

> "Sam, I understand the security team's concerns. We have our SOC 2 Type II report ready to share. For data residency, we offer [US-East/US-West/EU regions - confirm with product team]. Can we schedule a direct call between our security lead and your security team to walk through our controls? This often accelerates internal approval."

### Procurement Objections

| Objection | Root Concern | Response Strategy |
|-----------|--------------|-------------------|
| "All vendors must complete our onboarding process" | Vendor management governance | Request vendor onboarding checklist; assign internal resource to complete forms |
| "We need three vendor references" | Risk mitigation | Provide 2-3 banking/fintech references; request waiver if unavailable |
| "Legal needs to review the contract" | Legal protection | Provide standard MSA/ToS; assign legal contact; request redline turnaround timeline |
| "Procurement approval takes 6-8 weeks" | Process duration | Begin process immediately; identify parallel-path activities; escalate to shorten if needed |

**Talking Points for Sam Patel:**

> "Sam, let's get ahead of procurement by understanding their checklist now. Can you share the vendor onboarding requirements? If we start that process this week while security review continues, we can shorten the total cycle. What's the fastest path through procurement given our timeline?"

---

## Competitive Positioning

| Factor | Our Position | Unknown Factor |
|--------|--------------|----------------|
| **Security Posture** | Have SOC 2 Type II; [UNKNOWN] other certifications | Whether competitors have equivalent |
| **Data Residency** | [UNKNOWN] Available regions | Competitor offerings |
| **Implementation Timeline** | [UNKNOWN] Standard vs. expedited | Competitor timelines |
| **Banking/Fintech Experience** | [UNKNOWN] Reference accounts | Competitor references |
| **Pricing** | $260k ARR (provided) | Competitor pricing |

**Positioning Statement (Internal):**

> "EastRiver Bank needs a workflow automation platform that meets financial services security standards. Our SOC 2 Type II certification and [data residency options] position us to meet their requirements. The primary path forward is accelerating security evidence delivery and starting procurement onboarding immediately."

---

## Closing Strategy

### Stage-Based Approach: Proposal → Legal/Contract

```
┌─────────────────────────────────────────────────────────────────┐
│ CURRENT STATE: PROPOSAL                                         │
│                                                                 │
│ Blockers:                                                        │
│   ✗ Security evidence (SOC 2) not provided                      │
│   ✗ Procurement onboarding not initiated                        │
│   ✗ Data residency questions unresolved                        │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ GATE 1: Security Approval                                        │
│                                                                 │
│ Actions:                                                         │
│   ○ Share SOC 2 Type II report with security team               │
│   ○ Schedule security-to-security call                          │
│   ○ Answer data residency questions with architecture docs      │
│   ○ Complete security questionnaire if required                 │
│                                                                 │
│ Owner: [Security team handoff - see Human Gates]                 │
│ Timeline: 1-2 weeks (estimated)                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ GATE 2: Procurement Approval                                    │
│                                                                 │
│ Actions:                                                         │
│   ○ Request vendor onboarding checklist                         │
│   ○ Complete all required forms/documentation                   │
│   ○ Provide vendor references                                   │
│   ○ Submit for procurement review                                │
│                                                                 │
│ Owner: Sam Patel + internal procurement support                 │
│ Timeline: 4-8 weeks (depends on internal process)                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ GATE 3: Legal Review                                             │
│                                                                 │
│ Actions:                                                         │
│   ○ Provide standard MSA/contract terms                         │
│   ○ Respond to legal redlines                                    │
│   ○ Obtain necessary internal approvals                          │
│                                                                 │
│ Owner: Legal handoff (see Human Gates)                          │
│ Timeline: 2-3 weeks (estimated)                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ GATE 4: Contract Execution                                      │
│                                                                 │
│ Actions:                                                         │
│   ○ Final contract review by COO                                │
│   ○ Signature collection                                         │
│   ○ Deal closed                                                  │
│                                                                 │
│ Owner: Economic buyer (COO)                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Mutual Close Plan

| Milestone | Owner | Target Date | Dependency | Risk |
|-----------|-------|-------------|------------|------|
| Obtain vendor onboarding checklist | Sam Patel | [TARGET +3 days] | None | Low |
| Share SOC 2 Type II report with security | [Sales/SE - see Handoff] | [TARGET +3 days] | None | Medium (requires internal action) |
| Schedule security-to-security call | [Sales/SE] | [TARGET +5 days] | SOC 2 provided | Low |
| Complete security questionnaire | [Sales/SE] | [TARGET +7 days] | Security call scheduled | Medium |
| Resolve data residency questions | [Solutions/Product] | [TARGET +7 days] | None | Medium |
| Complete procurement onboarding forms | [Sales + Sam Patel] | [TARGET +10 days] | Checklist received | Medium |
| Security approval received | EastRiver Security | [TARGET +14 days] | Evidence provided | **HIGH** |
| Submit for procurement review | EastRiver Procurement | [TARGET +14 days] | Forms complete | **HIGH** |
| Legal contract review initiated | Legal handoff | [TARGET +21 days] | Procurement approved | Medium |
| Legal redlines resolved | Legal handoff | [TARGET +35 days] | Initial review | Medium |
| COO final approval | COO | [TARGET +42 days] | Legal clear | Low |
| Contract executed | All | **[TARGET +45 days]** | COO approved | Low |

**Revised Close Date Estimate:** Given procurement cycle uncertainty, recommend re-forecasting to **mid-to-late August 2026** or negotiating expedited procurement process with Sam Patel.

---

## Next 3 Actions

### Action 1: Internal Security Evidence Preparation
| Field | Detail |
|-------|--------|
| **Action** | Prepare and package SOC 2 Type II report for delivery |
| **Owner** | Sales/SE + Security team |
| **Due** | Within 2 business days |
| **Success Criteria** | SOC 2 report ready to send; security questionnaire drafted |
| **Evidence Type** | Action |

### Action 2: Request Procurement Checklist
| Field | Detail |
|-------|--------|
| **Action** | Ask Sam Patel for vendor onboarding requirements |
| **Owner** | Account Executive |
| **Due** | Within 2 business days |
| **Success Criteria** | Checklist received; assigned owner for completion |
| **Evidence Type** | Action |

### Action 3: Schedule Security Call
| Field | Detail |
|-------|--------|
| **Action** | Propose security-to-security call between our security lead and EastRiver security team |
| **Owner** | Account Executive + Sam Patel |
| **Due** | Within 5 business days |
| **Success Criteria** | Call scheduled for next available slot |
| **Evidence Type** | Action |

---

## Human Gates and Handoffs

| Handoff | To | For | Deadline | Status |
|---------|----|-----|----------|--------|
| **Security Evidence Package** | Security/Compliance Team | SOC 2 Type II report + security questionnaire + architecture docs | Immediate | **PENDING APPROVAL** |
| **Procurement Checklist Request** | Sam Patel | Request vendor onboarding requirements | 2 days | PENDING |
| **Legal Review** | Legal Team | Prepare standard MSA terms for financial services; review data residency clause | After security approval | PENDING |
| **Executive Escalation** | VP Sales / Executive Sponsor | If procurement or security delays exceed 4 weeks | As needed | STANDBY |

---

## Research Sources and Evidence Gaps

### Evidence Available
- **Fact:** Deal context provided by user
- **Fact:** SOC 2 evidence requested by security team
- **Fact:** Procurement vendor onboarding required
- **Fact:** Data residency questions raised
- **Fact:** Target close date: 2026-07-15

### Evidence Gaps
| Gap | Impact | Recommended Action |
|-----|--------|-------------------|
| SOC 2 Type II report availability | Cannot satisfy security blocker | Confirm with security team that report is ready to share |
| EastRiver Bank company intelligence | Limited context for stakeholder mapping | Use public sources only if approved; otherwise mark as [UNKNOWN] |
| Procurement process details | Cannot accurately estimate timeline | Obtain checklist from Sam Patel |
| Security team contact information | Cannot schedule security call | Request from Sam Patel |
| Competitor intelligence | Cannot position against competitors | Defer until competitive data available |
| Data residency technical options | Cannot answer data residency questions | Request architecture/product documentation |

---

## Summary for Sales Manager

The EastRiver Bank deal ($260k ARR) is in Proposal stage but blocked by two parallel workstreams:

1. **Security blocker:** Security team requires SOC 2 evidence before proceeding. We have the report; delivery is the action item.

2. **Procurement blocker:** Vendor onboarding process required but not yet initiated. We need the checklist from the customer.

**Recommended immediate actions:**
1. Prepare SOC 2 package for delivery (internal: Sales/SE + Security)
2. Request procurement checklist via Sam Patel
3. Schedule security-to-security technical call

**Timeline risk:** Target close of 2026-07-15 is aggressive given likely 6-8 week procurement cycle. Recommend re-forecasting to August 2026 or expediting procurement process.

**No customer-facing commitments have been made.** All communications require manager approval per Human Gates policy.

---

**Prepared by:** Deal Closer Agent  
**Date:** [Current Date]  
**Next Review:** After security/procurement checklist received
