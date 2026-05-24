# Deal Closer Playbook: ACME Manufacturing Expansion

## Deal Snapshot

| Field                 | Value                                                       |
|-----------------------|-------------------------------------------------------------|
| Company Name          | ACME Manufacturing (Fact)                                   |
| Product/Service       | `[UNKNOWN]`                                                 |
| Pricing Model         | `[UNKNOWN]`                                                 |
| Current Deal Stage    | `[UNKNOWN]`                                                 |
| Primary Contact       | VP Operations (name `[UNKNOWN]`) (Fact)                     |
| Deal Size             | $80,000 ARR expansion (Fact)                                |
| Target Close Date     | This quarter (specific date `[UNKNOWN]`) (Fact)             |
| Blocker               | IT security review (Fact)                                   |
| Incumbent/Competitor  | Spreadsheet workflow (Fact)                                 |
| Expansion Type        | Existing customer expansion (Inference from “expansion”)    |

## Known Facts And Unknowns

### Facts
- **Account**: ACME Manufacturing, a manufacturing company.
- **Deal value**: $80,000 ARR expansion.
- **Buyer**: VP Operations is the primary contact/buyer.
- **Blocker**: IT security review is in progress and is the current deal blocker.
- **Incumbent**: The users currently rely on a manual spreadsheet workflow.
- **Timeline**: Target close is this quarter.

### Unknowns (Critical Gaps)
- Product or service being sold, including specific value proposition.
- Pricing model (per seat, tiered, usage-based, etc.).
- Current deal stage in the sales process.
- VP Operations’ full name and formal title.
- Other buying committee members: champion, technical evaluator, users, coach, procurement/legal, executive sponsor.
- Specific security concerns raised by IT.
- Decision criteria and evaluation process (demo, pilot, RFP).
- Procurement or legal review requirements.
- Contract terms requested or negotiated.
- Interaction history (past meetings, product demos, trials).
- Any urgency drivers beyond quarter‑end.

## Company Intelligence

**Source**: Supplied deal facts only. No web research was conducted.

ACME Manufacturing is a manufacturing company (Fact). Because this is an expansion deal, we know they are an existing customer, but we lack context on which product they already use, adoption levels, and satisfaction (Unknown). No additional intelligence on company size, recent news, funding, or organizational changes is available. All company‑context sections below are based on the limited provided facts; recommendations should be validated once more specific data is collected.

## Buying Committee Map

| Role                 | Individual / Title        | Status                     | Evidence                        |
|----------------------|---------------------------|----------------------------|---------------------------------|
| Economic Buyer       | VP Operations (name `[UNKNOWN]`) | Identified – likely holds budget for operational tools. | Fact: VP Ops is the buyer. Inference: Budget authority for operational improvements. |
| Champion             | `[UNKNOWN]`               | Not yet identified         | Unknown.                         |
| Technical Evaluator  | `[UNKNOWN]`               | Not yet identified         | Unknown. Possibly tied to IT security reviewer. |
| User Buyer           | Operations team members   | Not directly identified    | Inference: Users of the current spreadsheet workflow. |
| Coach                | `[UNKNOWN]`               | Not yet identified         | Unknown.                         |
| Blocker              | IT Security Team          | Active blocker             | Fact: IT security review is blocking progress. |
| Procurement/Legal    | `[UNKNOWN]`               | Not yet identified         | Unknown.                         |
| Executive Sponsor    | `[UNKNOWN]`               | Not yet identified         | Unknown.                         |

**Risk**: The absence of a known champion or coach reduces our ability to influence the technical evaluation and security review internally. IT security holds blocking power, and without a counterpart advocating for the business need, the review may stall.

## Deal Qualification And Risk

**Qualification Strengths**
- Existing customer relationship suggests product‑fit and baseline trust (Inference).
- VP Operations is engaged as buyer, indicating strategic importance (Fact).
- $80,000 ARR expansion implies a meaningful upsell that likely has a clear business case (Inference).

**Risk Assessment**

| Risk Category                  | Description                                                                                      | Severity                        | Evidence                              |
|--------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------|---------------------------------------|
| Qualification Gap              | Product, value proposition, and decision criteria are unknown.                                   | Medium‑High                      | Unknowns list.                        |
| Urgency                        | Quarter‑end close depends on completing security review on time.                                 | High                             | Target this quarter.                  |
| Competition                    | Spreadsheet workflow is “free” and familiar; users may resist change.                            | Medium                           | Fact.                                |
| Blocker Influence              | IT security review can single‑handedly delay or kill the deal.                                   | Critical                         | Fact: blocker is IT security review.  |
| Procurement/Legal/Security Risk| Procurement/legal process unknown; security concerns not detailed.                               | High                             | Unknown.                              |
| Close‑date Realism             | Quarter‑end is near; security review often takes multiple weeks unless fast‑tracked.             | Critical                         | Inference from typical enterprise cycles. |
| Missing Coach/Champion         | No internal advocate identified to push security review from the business side.                  | High                             | Buying committee map.                 |

**Action Required**: Immediately clarify the specific security concerns, the IT security team’s requirements, and the VP Operations’ ability to influence the review timeline.

## Objection Playbook

| Objection / Concern                                     | Objection Type      | Response (Internal Talk Track)                                                                                 | Owner               | Supporting Material Needed                                       |
|---------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------|---------------------|------------------------------------------------------------------|
| “IT security review is not satisfied with data protection” | Technical/Security  | Partner with our security team to provide SOC 2 Type II report, data flow diagrams, encryption standards, and roadmap for any missing certifications. Offer a joint security Q&A session. | Sales Engineer + Security Lead | Security whitepaper, compliance certificates, pen‑test summary. |
| “We can just stay with spreadsheets; it’s free”         | Competitive/Status Quo | Quantify the cost of errors, rework, and lack of real‑time data vs. automation. Show time savings and compliance gains. Reference expansion value from their current usage. | Account Executive   | ROI calculator, case study from a similar manufacturer.          |
| “The team doesn’t want to learn a new system”           | Change Management   | Co‑create a phased rollout and training plan, highlight intuitive UX, offer early‑adopter success programs.    | Customer Success    | Training outline, adoption plan template.                         |
| “Why now? Can’t this wait until next half?”             | Urgency             | Align with the VP Operations’ quarterly goals; tie expansion to a known business pain (e.g., audit, growth target). Leverage quarter‑end to secure current pricing/model. | Account Executive   | Internal business case draft.                                     |
| “We need procurement to approve this before we can proceed” | Process            | Engage procurement early with a standard order form, terms, and a pre‑negotiated MSLA if available. Schedule a call to review any non‑standard terms. | Sales Operations / Legal | Contract template, security schedule.                            |

**Note**: All responses above are internal preparation materials; any external communication requires human approval.

## Competitive Positioning

**Primary Competitor**: Incumbent manual spreadsheet workflow (Fact).

| Positioning Pillar             | Our Advantage                                                                                  | Evidence                                                                                       |
|--------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Efficiency & Automation        | Eliminate manual data entry, reduce cycle time, and minimize human error.                      | Inference based on typical operational software; needs specific product‑level data.            |
| Real‑Time Data & Visibility    | Provide live dashboards and alerts that spreadsheets cannot offer.                             | Depends on product capabilities (Unknown).                                                     |
| Compliance & Audit Readiness   | Maintain audit trails, user permissions, and version control; spreadsheets lack these features.| Inference; requires product‑specific compliance documentation.                                  |
| Scalability & Integration      | Integrate with existing systems (ERP, MES) to avoid data silos.                                | Unknown; depends on product and current stack.                                                 |
| ROI & Total Cost of Ownership  | Reduce hours spent on manual reconciliation and rework; expansion cost offset by savings.      | Needs financial justification from previous usage data.                                         |

**Gap**: No direct named software competitor is mentioned. If there are other SaaS options the customer is considering, we need to identify them and prepare differentiation. Currently, the primary battle is against “do nothing/more of the same” mindset.

## Closing Strategy

Given the current blocker (IT security review) and the quarter‑end deadline, the strategy is:

1. **Unblock Security Review**: Mobilize our internal security and technical teams to respond to all IT requests within 24 hours. Request a detailed list of outstanding security requirements from the customer. Propose a live review session to resolve concerns in real time.
2. **Leverage VP Operations as Executive Push**: Secure a commitment from VP Ops to sponsor the security review by explaining the business urgency (quarter‑end goals). Ask VP Ops to set an internal deadline for IT sign‑off.
3. **Reframe Incumbent Status Quo**: Prepare a business case highlighting the risk of spreadsheet errors and the cost of inaction, tied to the VP Operations’ objectives.
4. **Compress Legal/Procurement**: Identify if a new master agreement is needed or if the deal can be added under existing terms. Engage procurement in parallel, not sequentially, with security review.
5. **Create Mutual Close Plan** (see next section) with clear ownership and dates agreed upon by the customer (to be validated).
6. **Risk Management**: If the security review cannot be completed this quarter, explore a conditional close (e.g., signed order contingent on security approval within a short window) but only with human/legal approval.

**Stage Assumption**: The deal is in the “negotiate/commit” stage, with only the security review standing in the way. If earlier, adjust to include product validation and technical evaluation milestones.

## Mutual Close Plan

| Milestone                                     | Owner (Internal)               | Customer Owner (to be confirmed) | Target Date       | Dependency                                 | Risk                                     | Mitigation                                                |
|-----------------------------------------------|--------------------------------|----------------------------------|-------------------|--------------------------------------------|-------------------------------------------|-----------------------------------------------------------|
| Collect missing security review specifics     | Account Executive              | VP Operations / IT Security     | Immediate (Week 1) | Access to IT contact                     | Unknown security requirements delay response | VP Ops to introduce IT lead directly                  |
| Submit security documentation and compliance artifacts | Sales Engineer + Security Lead | IT Security                      | Week 1‑2          | Security requirements list clear          | Incomplete docs may cause back‑and‑forth     | Pre‑populate standard security package               |
| Joint security Q&A call                       | Security Lead + Sales Engineer | IT Security                      | By end of Week 2   | Documentation review feedback             | Scheduling conflicts or unresolved concerns   | Offer multiple slots; prepare FAQs                   |
| IT security sign‑off (conditional or final)   | Account Executive              | IT Security                      | By early Week 3    | Successful Q&A, no critical gaps          | Sign‑off may require VP Ops/CIO push         | Pre‑align VP Ops to escalate if needed              |
| Procurement/legal review and contract finalization | Sales Operations / Legal       | Procurement/Legal                | Week 3‑4          | Standard terms or minor modifications     | Redlines delay sign‑by‑quarter‑end           | Use existing framework agreement if possible        |
| Final agreement signature                     | Account Executive              | VP Operations                    | Quarter‑end       | All above steps complete                   | Any delay in preceding steps                 | Secure VP Ops verbal commitment to sign by date     |
| Post‑sign implementation planning handoff    | Customer Success               | VP Operations / Ops Team        | Post‑close        | Signed agreement                           | None                                      | Schedule handoff call as part of close plan          |

**Note**: All dates are illustrative; actual dates must be mutually agreed upon with the customer. External commitments require human gate approval.

## Next 3 Actions (Internal Only)

1. **Gather missing deal context** (Action)
   - Ask the rep: product/service details, pricing model, current stage, VP Ops full name, key stakeholders, decision criteria, and specific IT security concerns. Document as a deal update.
   - **Purpose**: Reduce unknowns and sharpen the playbook.

2. **Schedule internal security prep session** (Action)
   - Bring together sales engineer, security/compliance lead, and account executive.
   - Review standard security artifacts (SOC 2, penetration test summaries, encryption details, data hosting) and draft a response plan.
   - **Output**: Security response package ready to submit once IT requirements are known.

3. **Engage VP Operations to unblock security** (Action – requires human check before external communication) (Human gate)
   - Draft a meeting agenda (internal) for the AE to review with VP Ops.
   - Goal: confirm business urgency, identify the IT security lead, and agree on a mutual timeline.
   - **Human Gate**: Do not send any customer communication until sales manager approves the approach.

## Human Gates And Handoffs

| Decision / Action                        | Gatekeeper                      | Reason                                                                 |
|------------------------------------------|---------------------------------|------------------------------------------------------------------------|
| Sending any customer communication       | Sales Manager + AE              | Ensure messaging aligns with deal strategy and no unauthorized promises. |
| Submitting security documentation        | Security & Compliance Lead      | Accuracy and completeness of technical materials.                      |
| Offering any concession (discount, terms)| Sales Manager / Deal Desk       | Prevents unauthorized pricing or legal commitment.                     |
| Committing to a timeline externally      | Sales Manager                   | Protects close‑date realism and accountability.                         |
| Contract redlines or legal language      | Legal                           | Only legal can approve non‑standard terms.                             |
| Conditional close proposal               | Sales Ops + Legal + VP of Sales | Requires executive risk acceptance.                                     |
| Implementation handoff                   | Customer Success / Delivery     | Ensures smooth transition post‑signature.                               |

**Handoff Points**:
- Sales Manager: for deal strategy approval and escalation.
- Security/Compliance: for technical security review and documentation.
- Legal/Procurement: for contract review and terms.
- Executive Sponsor: if the IT security review becomes political or requires a leadership call.

## Research Sources Or Evidence Gaps

- **Sources**: Supplied synthetic deal facts only. No external research was performed.
- **Evidence Gaps**:
  - Product/service details, pricing model, current deal stage, VP Operations name.
  - Specific IT security concerns and the organization’s procurement/legal requirements.
  - Identity of champion, coach, technical evaluator, user buyers, and any executive sponsor.
  - Past interaction history and any existing quotes or proposals.
  - Exact quarter‑end date and the customer’s internal processes for IT reviews and purchasing.

Fill these gaps with the account team to turn this partial playbook into a high‑confidence closing plan.
