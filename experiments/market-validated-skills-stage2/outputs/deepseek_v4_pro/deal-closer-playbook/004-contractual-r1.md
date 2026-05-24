# Internal Handoff: Security and Procurement Blockers

## Deal Snapshot

- **Company:** `[UNKNOWN]`
- **Product/Service:** `[UNKNOWN]`
- **Deal Stage:** `[UNKNOWN]`
- **Primary Contact (Champion):** `[UNKNOWN]`
- **Deal Size:** `[UNKNOWN]`
- **Target Close Date:** `[UNKNOWN]`

## Known Facts (from rep)

- **Fact:** Buyer likes the product (positive sentiment).
- **Fact:** Security questionnaire is pending with the prospect.
- **Fact:** Procurement needs vendor onboarding; process not yet started.
- **Fact:** Champion requested an implementation timeline.
- **Fact:** The deal is progressing but blocked on security and procurement steps.

## Current State of Blockers

### 1. Security Block
- **Status:** Questionnaire pending.
- **Owner:** Security/Technical owner (TBD inside our org).
- **Action Required:** Complete the security questionnaire and return it to the prospect. Coordinate with the champion to confirm submission channel and any additional requirements (penetration test, SOC2 report, data privacy addendum).
- **Risk:** Delay in returning the questionnaire could stall evaluation or give competitor an opening. If security review uncovers client-specific requirements not met, deal could stall or require custom security work.
- **Evidence Gap:** We do not know the specific questions, the prospect’s security review timeline, or whether our standard security package meets their needs without modification. No information on data residency, compliance (GDPR, HIPAA, etc.) requirements.

### 2. Procurement Block
- **Status:** Vendor onboarding not yet initiated.
- **Owner:** Procurement/Legal team (ours) + rep to facilitate with prospect’s procurement/legal.
- **Action Required:** Provide our standard vendor onboarding package (W-9, banking, insurance certificate, standard contract/MSA, code of conduct, etc.) to the prospect. Understand their onboarding steps, anticipated duration, and any non-standard requirements (custom payment terms, EDI, portal registration).
- **Risk:** Procurement delays often extend close timeline beyond target. If prospect has strict compliance or insurance thresholds, we may need underwriting or legal review, adding more time. The champion’s request for an implementation timeline implies they want to see end-to-end plan, which procurement can derail if not sequenced.
- **Evidence Gap:** No information on procurement lead time, required documents, legal review involvement, or whether we have done business with this company before.

### 3. Implementation Timeline Request
- **Context:** Champion asked for timeline.
- **Owner:** Customer Success / Delivery / Solutions team (TBD) in collaboration with rep.
- **Action Required:** Prepare a high-level implementation plan with phases, resource requirements, dependencies (including security and procurement completion), and a realistic go-live window. This must be framed as **indicative and subject to final scoping**.
- **Inference:** Champion is building internal business case and wants confidence in post-signature execution. This is an opportunity to strengthen the business case and alignment with economic buyer.
- **Risk:** If timeline is overly aggressive and we fail to meet it, trust is damaged. If too conservative, it may weaken urgency. The plan must explicitly call out that start depends on signed contract, completed security review, and vendor onboarding.
- **Human Gate:** The implementation timeline must be reviewed by delivery leadership before sharing with customer. It must not constitute a binding delivery commitment.

## Required Internal Actions

### For Security Team
1. **Assign owner** to security questionnaire (by end of day). `[Action]`
2. **Retrieve standard security collateral** (SOC2, pen test, architecture, data flow) and tailor to this prospect’s industry and common concerns. `[Action]`
3. **If questionnaire is already received**: begin filling immediately; flag any questions requiring legal or engineering input. `[Action]`
4. **If not received**: rep to request questionnaire from champion and set expectation on turnaround time. `[Action]`
5. **Identify potential gaps**: If prospect requires on-prem, private cloud, or specific certifications we lack, escalate to Security owner and sales manager. `[Risk]`

### For Procurement / Legal Team
1. **Assign owner** for vendor onboarding. `[Action]`
2. **Prepare our standard onboarding packet** and confirm it’s current. `[Action]`
3. **Understand prospect’s onboarding process**: rep to inquire about forms, portal, insurance limits, payment terms. `[Action]`
4. **Evaluate any non-standard terms** the prospect may require (net 60, performance guarantees, liability caps). All such deviations require **human gate** approval. `[Human Gate]`
5. **Sequence**: procurement completion must be a gating milestone before contract signing or implementation kickoff. `[Action]`

### For Customer Success / Delivery
1. **Draft a template implementation timeline** with standard phases (kickoff, discovery, config, integration, testing, training, go-live). `[Action]`
2. **Include prerequisite milestones**: security approval received, vendor onboarding complete, contract executed. `[Action]`
3. **Review with delivery manager** before sharing externally. `[Human Gate]`
4. **Provide rep with a version that can be presented as “draft for discussion.”** `[Action]`

### For Account Executive (Rep)
1. **Immediately confirm receipt of security questionnaire**; if not received, request it today with a crisp deadline. `[Action]`
2. **Request the prospect’s procurement onboarding guide/contact** and introduce our procurement lead. `[Action]`
3. **Clarify the use case for the implementation timeline**: is it for internal approval, resource planning, or statement of work? `[Action]`
4. **Update the mutual close plan** with new milestones for security submission, security approval, vendor onboarding completion, and timeline delivery. `[Action]`

## Mutual Close Plan (Draft – Security/Procurement Stream)
| Milestone | Owner (Internal) | Target Date | Dependency | Risk |
|-----------|------------------|-------------|------------|------|
| Security questionnaire received from prospect | Rep | `[UNKNOWN]` | Champion cooperation | Delay if not sent promptly |
| Security questionnaire completed and returned | Security team | 3 business days after receipt | No missing requirements; legal input needed for custom terms | Extended review if gaps found |
| Vendor onboarding packet sent to prospect | Procurement/Legal | 1 business day | Rep provides contact | Missing documentation could cause re-send |
| Prospect procurement approval received | Prospect (our team supports) | `[UNKNOWN]` | Vendor packet accepted; legal review | May take weeks; negotiate timeline with champion |
| Implementation timeline draft ready | Delivery/Solutions | 3 business days | Clarity on scope from rep | Incomplete info leads to rework |
| Timeline reviewed internally (gate) | Delivery mgr | 1 day after draft | — | — |
| Timeline shared with champion | Rep | After internal review | — | Must emphasize non-binding nature |

## Human Gates
- **Security exceptions or custom security work**: requires Security owner + legal sign-off.
- **Non-standard procurement terms**: requires sales manager and legal approval.
- **Implementation timeline**: requires delivery manager approval before customer-facing use.
- **Any price or contract concessions**: require deal desk / management approval (not in scope of this handoff, but mention for completeness).

## Missing Information (Critical)
- Company name, product, deal size, close date.
- Existing relationship or past purchases (vendor already onboarded?).
- Any timeline pressure from prospect (budget cycle, event, competitor).
- Details of security questionnaire.
- Prospect’s vendor onboarding steps and typical duration.
- Whether a coach or economic buyer is identified.

## Next 3 Actions (for Rep)
1. Request security questionnaire from champion and forward to security team (with CC to sales manager).
2. Request procurement contact and requirements; introduce our procurement lead.
3. Confirm the goal of the implementation timeline (internal business case vs. contractual SOW) and relay to delivery team.

---

This handoff is internal only. No commitments to the customer are made or implied. All customer-facing deliverables must pass the gates defined above.
