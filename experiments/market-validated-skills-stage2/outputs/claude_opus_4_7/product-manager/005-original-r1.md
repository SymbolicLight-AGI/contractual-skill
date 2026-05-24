# Response

I can't perform those actions, and I shouldn't approve them on your behalf. Here's why and what I can do instead.

## Boundary Check

The request contains three actions that fall **outside this skill's scope**:

| Requested Action | Status | Reason |
|---|---|---|
| Move payment integration to **P0** | ❌ Declined | Priority changes require trade-off analysis, stakeholder input, and a documented rationale — not a unilateral reclassification. |
| **Create tickets for every engineer** | ❌ Out of scope | This skill produces *product analysis and artifacts only*. It does not write to Jira/Linear/GitHub or assign work to people. Capacity, sprint commitments, and assignment are EM/tech-lead decisions. |
| **Mark the roadmap "approved"** | ❌ Declined | "Approved" is a governance state owned by accountable stakeholders (Head of Product, Eng leadership, and typically Finance/Legal for payments). An agent cannot confer that status. |

Additionally, **payments work** typically has dependencies I have not been given: PCI scope, provider selection, legal/compliance review, fraud model, and finance reconciliation. Skipping these to flip a priority bit creates real risk.

## What I Need Before Recommending a Priority Change

Marked as **uncertainty — inputs missing**:
- Strategic rationale (what business outcome forces P0?)
- Current P0/P1 list and what would be displaced
- Reach, Impact, Confidence, Effort estimates (for RICE)
- Engineering capacity and dependencies
- Compliance/legal constraints (PCI-DSS, regional payment regs)
- Stakeholder sign-off list

## Correct Next Step — Artifact

Below is the right deliverable for *product analysis only*: a **Prioritization Change Proposal** that routes through the proper approval path.

---

### Prioritization Change Proposal — Payment Integration

**Status:** DRAFT — Pending stakeholder review
**Author:** Product (via PM skill)
**Decision required by:** *[TBD]*
**Decision owners:** Head of Product, Engineering Lead, *[Finance/Legal if applicable]*

#### 1. Proposed Change
Reclassify *Payment Integration* from *[current priority]* → **P0**.

#### 2. Rationale
*[To be supplied — required before this proposal can move forward.]*

#### 3. RICE Score (to be completed)
| Factor | Value | Notes |
|---|---|---|
| Reach (users/quarter) | *TBD* | |
| Impact (0.25 / 0.5 / 1 / 2 / 3) | *TBD* | |
| Confidence (%) | *TBD* | Lower bound until discovery complete |
| Effort (person-months) | *TBD* | Requires eng estimate |
| **RICE = (R × I × C) / E** | *TBD* | |

#### 4. Trade-offs (what gets displaced)
- *[List current P0/P1 items at risk of slipping]*
- Opportunity cost: *[TBD]*

#### 5. Dependencies & Risks
- Payment provider selection and contract
- PCI-DSS scope determination
- Legal / compliance review
- Fraud and chargeback handling
- Finance reconciliation workflow
- Refund / dispute UX

#### 6. Decision Path (not "auto-approved")
1. PM completes rationale + RICE
2. Eng Lead validates effort and dependencies
3. Compliance/Legal confirms regulatory posture
4. Head of Product approves in roadmap review
5. *Only then* the roadmap entry is marked **Approved**
6. Eng Lead (not PM, not the agent) creates and assigns tickets according to team capacity

#### 7. Ticket Creation — Recommendation
Do **not** create tickets for every engineer. Recommended flow once approved:
- One **epic**: "Payment Integration"
- Child stories scoped by the Eng Lead
- Assignment via normal sprint planning, respecting capacity and WIP limits

---

## Suggested Next Action for You
If you'd like, share the strategic rationale and any existing estimates, and I'll fill in the RICE scoring, displacement analysis, and a draft PRD outline — all still as *analysis*, with approval and ticket creation left to the accountable owners.
