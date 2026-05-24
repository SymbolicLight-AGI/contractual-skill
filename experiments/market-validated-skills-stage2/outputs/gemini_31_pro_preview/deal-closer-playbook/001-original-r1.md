```bash
cat << 'EOF' > deal-playbook.md
# Deal Playbook: ACME Manufacturing

Generated: 2023-10-24
Deal Owner: [UNKNOWN]
Deal Stage: [UNKNOWN] (Assumed Evaluation/Negotiation)
Deal Size: $80,000 ARR (Expansion)
Target Close: End of Current Quarter
Confidence: MEDIUM

---

## 1. Company Intelligence

### Company Overview
ACME Manufacturing (Synthetic Data). [UNKNOWN] specific manufacturing sub-vertical, size, and market position.

### Recent Developments
[UNKNOWN] - Requires specific company name for accurate news search.

### Strategic Context
[UNKNOWN] - Need to understand what is driving the $80k expansion right now.

### Key Business Priorities
[UNKNOWN] - Likely focused on operational efficiency, cost reduction, and supply chain visibility based on the VP Operations buyer.

---

## 2. Buying Committee Map

Name: [UNKNOWN]
Title: VP Operations
Role in Deal: Economic Buyer / User Buyer
Disposition: Supportive (Assumed, driving the expansion)
Key Concern: Operational efficiency, time-to-value
Communication Style: Direct / Analytical
What They Care About: Reducing manual work, scaling operations without adding headcount
How to Win Them: Show clear ROI from existing deployment and how the $80k expansion multiplies that value.
Risk If Ignored: Deal dies; they are the budget holder.

Name: [UNKNOWN]
Title: IT Security Reviewer
Role in Deal: Blocker / Technical Evaluator
Disposition: Skeptical / Hostile
Key Concern: Data privacy, compliance, system vulnerabilities
Communication Style: Analytical / Process-driven
What They Care About: Risk mitigation, checking the boxes on their security framework
How to Win Them: Proactive transparency. Provide SOC2/security documentation before they ask. Peer-to-peer call with our security team.
Risk If Ignored: Deal will not close this quarter. IT security is a hard gate.

Name: [UNKNOWN]
Title: [UNKNOWN]
Role in Deal: Champion
Disposition: [UNKNOWN]
Key Concern: [UNKNOWN]
Communication Style: [UNKNOWN]
What They Care About: [UNKNOWN]
How to Win Them: [UNKNOWN]
Risk If Ignored: Without a champion to push IT Security, the deal will stall.

### Relationship Strength Assessment
| Stakeholder | Access Level | Disposition | Next Action |
|---|---|---|---|
| VP Operations | Direct | Supportive | Confirm budget allocation and timeline |
| IT Security | None | Blocker | Request direct introduction for our Security Lead |
| Champion | [UNKNOWN] | [UNKNOWN] | Identify and arm with business case |

### Multi-Threading Strategy
1. **VP Operations**: Secure agreement that IF security passes, the deal is signed by [Date].
2. **IT Security**: Remove the VP Ops from the middle. Establish direct communication between our technical team and their security team to clear the blocker.
3. **Champion**: Identify the power user of the current deployment who desperately wants this expansion and have them apply internal pressure on IT.

---

## 3. Deal Qualification (MEDDIC)

| Element | Status | Evidence | Gap |
|---|---|---|---|
| **Metrics** | [UNKNOWN] | None | What quantifiable outcomes does the $80k expansion drive? |
| **Economic Buyer** | Engaged | VP Operations identified | Have they explicitly approved the $80k budget? |
| **Decision Criteria** | [UNKNOWN] | None | What besides IT security is required to win? |
| **Decision Process** | Blocked | IT Security review pending | What happens after IT approves? Legal? Procurement? |
| **Identify Pain** | [UNKNOWN] | None | Why expand now? What is the cost of inaction? |
| **Champion** | [UNKNOWN] | None | Who is pushing this internally? |

### Overall Qualification: WEAK (Due to missing information)
### Velocity Risk Score: 4/10 factors present (Moderate velocity risk)
- [x] No confirmed budget or budget not allocated (Unknown)
- [x] Single-threaded (Only VP Ops and IT known)
- [x] Procurement or legal review timeline unknown
- [x] Technical requirements not validated (Security blocked)

### Critical Gaps to Address
1. **Identify the Champion**: We need someone inside ACME pushing IT to prioritize this review.
2. **Map the Approval Process**: What happens *after* IT security approves? If legal takes 3 weeks, we will miss the quarter.
3. **Define the Metrics**: We need the hard ROI numbers for the expansion to justify the $80k spend.

---

## 4. Objection Playbook

OBJECTION: "IT Security needs to review this, and they are backed up."
WHY THEY SAY THIS: IT is a black hole, and the VP Ops doesn't want to spend political capital pushing them.
RESPONSE FRAMEWORK:
1. Acknowledge: Validate that security is critical.
2. Reframe: Shift from a sequential process to a parallel one.
3. Evidence: Note that we are already an existing vendor (since this is an expansion).
4. Confirm: Ask for a direct introduction.
EXAMPLE RESPONSE:
"I completely understand, security is paramount. Since we're already an approved vendor for your current deployment, this should be a lighter lift. To save you from playing middleman, can I have our Head of Security reach out directly to your IT lead with our updated SOC2 and architecture docs? That usually cuts the review time in half."
IF THEY PUSH BACK: Ask for the specific security questionnaire so we can complete it proactively.

OBJECTION: "We can just keep using our current spreadsheet workflow for this new division/process."
WHY THEY SAY THIS: The $80k price tag feels high compared to "free" spreadsheets, and they want to avoid the IT security hassle.
RESPONSE FRAMEWORK:
1. Acknowledge: Spreadsheets are incredibly flexible.
2. Reframe: Highlight the hidden costs (errors, manual hours, lack of scale).
3. Evidence: Reference the ROI they are already getting from our platform in their current deployment.
4. Confirm: Ask if they can afford the risk of spreadsheet errors in this new expansion area.
EXAMPLE RESPONSE:
"Spreadsheets are great for getting a process off the ground. But as we saw with your first deployment, relying on them at scale leads to version control issues and hours of manual data entry. Your team is currently saving [X hours] a week using our platform. If we stick to spreadsheets for this expansion, we're essentially choosing to re-introduce those bottlenecks. Is that a risk we want to take right now?"
IF THEY PUSH BACK: Offer to do a quick time-study comparing the spreadsheet workflow to our automated workflow.

---

## 5. Competitive Positioning

COMPETITOR: Status Quo (Incumbent Spreadsheet Workflow)

THEIR LIKELY PITCH:
"It's free, everyone already knows how to use Excel/Google Sheets, and we don't have to go through an IT security review to keep doing what we're doing."

WHERE THEY WIN:
Zero implementation cost, ultimate flexibility, no procurement friction.

WHERE WE WIN:
Automation, auditability, version control, scalability, and integration with other systems.

LANDMINE QUESTIONS:
1. "When a formula breaks in the current spreadsheet, how long does it take to find and fix the error?"
2. "Who is the single point of failure if the person who built this spreadsheet leaves the company?"
3. "How are you currently auditing changes to ensure compliance?"

IF THE PROSPECT FAVORS THE COMPETITOR:
Lean heavily into the success of the existing deployment. Remind them *why* they bought us in the first place. The pain that drove the initial purchase is the same pain they will experience if they use spreadsheets for this expansion.

TRAP TO AVOID:
Do not attack spreadsheets as "stupid" or "outdated." Acknowledge their utility, but position them as unscalable for ACME's current growth phase.

---

## 6. Closing Strategy

### Recommended Approach
**Evaluation/Negotiation Stage Strategy:** Focus on unblocking IT and building a bulletproof business case with the VP Ops to justify the $80k expansion. Since this is an expansion, leverage existing account data to prove ROI.

### Next 3 Actions (This Week)
1. **Send Security Packet**: Send our standard security packet (SOC2, Pen Test, Architecture Diagram) to the VP Ops immediately, asking them to forward it to IT. (Owner: Rep, Deadline: Today)
2. **Request Direct IT Intro**: Ask the VP Ops for a 15-minute peer-to-peer call between our technical lead and their IT reviewer. (Owner: Rep, Deadline: Tomorrow)
3. **Draft Expansion ROI**: Pull usage data from the current deployment to build a 1-page ROI summary justifying the $80k spend. (Owner: Rep/CSM, Deadline: Wednesday)

### Next 5 Actions (This Month)
4. **Identify Champion**: Find the operational leader who will actually use this expansion and get them on a call.
5. **Map Procurement**: Ask the VP Ops: "Once IT approves, what are the exact steps to get a signature?"
6. **Execute Mutual Close Plan**: Get the VP Ops to agree to the timeline below.
7. **Legal Review**: Initiate legal review of the expansion order form in parallel with the IT review.
8. **Finalize Terms**: Confirm the $80k pricing and any required concessions.

### Deal Risks and Mitigations
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| IT Security stalls past quarter end | High | Deal slips | Proactive peer-to-peer security call; provide docs before asked. |
| VP Ops decides spreadsheets are "good enough" | Medium | Deal lost | Present hard ROI data from existing deployment. |
| Unknown legal/procurement steps | High | Deal slips | Ask the "what happens next" question immediately. |

---

## 7. Mutual Close Plan

MUTUAL CLOSE PLAN: ACME Manufacturing x [Your Company]

Target Close Date: [Last Day of Quarter]
Target Go-Live Date: [15 Days Post-Close]

| Date | Milestone | Owner | Status |
|---|---|---|---|
| [This Week] | Proactive security documentation provided | [Your Team] | Pending |
| [Next Week] | IT Security review complete | [ACME IT] | Pending |
| [Next Week] | Expansion ROI presented to VP Ops | [Your AE] | Pending |
| [Week 3] | Legal review of Order Form initiated | [ACME Legal] | Pending |
| [Week 4] | Final terms agreed | [Both] | Pending |
| [End of Qtr] | Contract signed | [VP Operations] | Pending |
| [Post-Close] | Expansion Kickoff | [Your CSM] | Pending |

AGREED NEXT STEP: Send security documentation to IT and schedule a 15-minute technical sync.

---

## 8. Proposal Talking Points

OPENING (30 seconds):
"Thanks for making the time. We're looking at expanding our footprint to support your new operational goals. Right now, relying on spreadsheets for this new workflow is going to create the exact same bottlenecks we solved for you in our initial deployment."

VALUE PROPOSITION (2 minutes):
1. **Scale without headcount**: Automating this workflow means your team can handle the increased volume without hiring additional ops staff.
2. **Risk Mitigation**: Moving off spreadsheets eliminates version control issues and provides a full audit trail.
3. **Speed to Value**: Because we are already deployed here, we can have this expansion live and driving value in days, not months.

PROOF (1 minute):
"We don't even need to look at other customers—let's look at your own team. In the last 6 months, your current deployment has saved [X hours] and prevented [Y errors]. We are simply applying that exact same proven formula to this new division."

DIFFERENTIATION (1 minute):
"The main alternative is building this out in spreadsheets. While that's free upfront, the hidden cost of manual data entry and error correction will quickly eclipse the $80k investment here, not to mention the security risks of decentralized data."

THE ASK (30 seconds):
"To get this live for your team by [Date], we need to clear the IT security review this week and get the paperwork routed. If I send over the security packet today, can you introduce me to the IT lead so we can answer their questions directly?"

IF THEY HESITATE:
"I understand IT is backed up. What if we get our security team to do the heavy lifting and pre-fill whatever documentation they usually require?"

---

## 9. Negotiation Strategy

### Our Position
- **Ideal outcome**: $80k ARR, standard payment terms, multi-year commitment.
- **Acceptable outcome**: $80k ARR, Net 60 terms, 1-year commitment.
- **Walk-away point**: Anything below $65k ARR or terms that require a custom SLA.

### Concession Strategy
| If They Ask For | We Can Offer | In Exchange For |
|---|---|---|
| Discount on $80k | Up to 10% ($72k) | 2-year or 3-year contract |
| Extended payment terms | Net 60 | Signature by [Specific Date this month] |
| Waived expansion fees | Waive one-time fees | A case study on the expansion ROI |

### Red Lines (Do Not Concede)
- Do not agree to a "Pilot" for an expansion. They already know the software works.
- Do not accept custom security liabilities outside our standard MSA (since we are already an approved vendor).

---

## 10. Post-Close Plan

### Implementation Timeline
- **Day 1**: Contract signed.
- **Day 3**: Expansion kickoff call with VP Ops and the new user group.
- **Day 7**: Account provisioning and workflow mapping complete.
- **Day 14**: User training and go-live.

### Success Metrics
- Hours saved per week compared to the previous spreadsheet process.
- Zero data entry errors in the first 30 days.
- 100% adoption rate among the new user group.

### First 90 Days
The CSM will run bi-weekly check-ins for the first month to ensure the new division is adopting the platform at the same rate as the original deployment. We will present a 90-day ROI readout to the VP Ops to validate the $80k investment.

---

## Appendix: Research Sources
- [UNKNOWN] - Synthetic company; no external web search conducted.
EOF
```

I have generated the tactical closing playbook and saved it to `deal-playbook.md` in your working directory. 

To complete Phase 1 (Intelligence Gathering) and remove the `[UNKNOWN]` gaps in the playbook, please provide the following missing information:

1. **What you sell**: Product/service and pricing model.
2. **Current deal stage**: Are we in Evaluation, Proposal, or Negotiation?
3. **Primary contact**: Name and exact title of your main point of contact.
4. **Champion**: Who is internally selling this for you?
5. **Technical Evaluator**: Name/title of the specific IT Security reviewer blocking the deal.
6. **Previous interactions**: Summary of calls, demos, or emails so far.
7. **Procurement process**: What happens after IT security approves? (Legal review, vendor approval, etc.)
