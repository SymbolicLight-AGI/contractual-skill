# Renewal Rescue Handoff

**Account Status**: At Risk | Renewal in 45 days
**Prepared by**: Renewal Predictor (Health Score Model v1.0)

---

## Boundary Note

This task requests a multi-function handoff rather than the standard `renewal-forecast.md` portfolio file. I am producing an abbreviated single-account assessment using the Skill's framework, framed as a handoff. No external data was supplied, so scoring relies only on the seven known facts and is calibrated **Low Confidence** with explicit data gaps. If a full forecast file is needed, provide the account data templates listed in the Skill and re-invoke.

---

## Health Score Snapshot

| Dimension | Score | Weight | Weighted | Basis |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10.0 | No data — neutral default (gap) |
| Support Ticket Volume/Sentiment | 35 | 15% | 5.25 | Unresolved integration tickets; aging open issues |
| Feature Adoption | 50 | 20% | 10.0 | No data — neutral default (gap); export scheduling gap noted separately |
| NPS/CSAT | 40 | 10% | 4.0 | NPS dropped 8 → 5 (Passive → Detractor), 3-point decline |
| Billing History | 80 | 10% | 8.0 | Current; no disputes noted |
| Stakeholder Continuity | 35 | 10% | 3.5 | Admin champion changed roles; successor unknown |
| Usage Trends | 50 | 15% | 7.5 | No data — neutral default (gap) |
| **Total** | | **100%** | **48** | |

**Health Score: 48/100 → At Risk**
**Confidence: Low** (only 4 of 7 dimensions have direct evidence; no usage or engagement data; <30 days of trailing context provided)

---

## Active Signals

**Churn Signals (High Severity):**
- **Champion Departure (Medium→High)**: Admin champion changed roles; no successor identified. Single-threaded relationship risk.
- **NPS Detractor Drop**: 3-point decline (8→5) crosses Passive into Detractor territory. Per rubric, declines of 3+ points are a red flag.
- **Unresolved Support + Product Gap Combined**: Integration tickets open alongside a known product gap (export scheduling). Compounds dissatisfaction.

**Compound Risk**: Champion change + dissatisfaction signals + 45-day renewal window = elevated urgency, even without usage data.

**Expansion Signals**: None identified from available facts.

---

## Cross-Functional Handoff

### 1. Customer Success (Owner: CSM + CS Leader)
**Priority: Critical | Deadline: 5 business days**

- Identify and engage the new admin / successor stakeholder. Confirm whether a replacement exists or if the seat is vacant.
- Multi-thread the account: surface 2–3 additional stakeholders (executive sponsor, end users, IT owner) before the renewal conversation opens.
- Schedule a partnership review (not a save call) with the decision-maker within 10 business days. Bring a value summary, roadmap preview (including export scheduling status), and remediation commitments from support and product.
- Run a **Stakeholder Re-engagement Campaign** (see save plays) in parallel.

**Success metric**: New champion identified and engaged; partnership review scheduled before day 15 of the 45-day window.

### 2. Support / Support Engineering (Owner: Support Manager + assigned engineer)
**Priority: Critical | Deadline: 3 business days for plan, full resolution before day 30**

- Audit every open integration ticket. Produce a written remediation plan with committed ETAs per ticket.
- Assign a dedicated escalation engineer; open a direct channel (Slack or email alias) to the client.
- Daily internal standup until all integration tickets are resolved or have a client-accepted plan.
- Post-resolution CSAT check.

**Success metric**: Zero unresolved integration tickets, or all remaining tickets have client-accepted resolution dates, by day 30.

### 3. Product (Owner: Product Manager for relevant module)
**Priority: High | Deadline: 7 business days for written response**

- Provide a written status on **export scheduling**: on roadmap (with target quarter), in beta, deprioritized, or workaround available.
- If on roadmap: prepare a private preview, design partnership offer, or commitment letter the CSM can present.
- If not on roadmap: provide the supported workaround in writing and an honest expectation-setting message.
- Identify whether this client should be added to a beta or design partner cohort to deepen investment.

**Success metric**: Client receives a credible, specific product answer before the renewal conversation begins.

### 4. Finance (Owner: Deal Desk / Finance Partner)
**Priority: Medium | Deadline: 10 business days**

- Billing is current — preserve that signal. Do **not** preemptively offer a discount; it would set precedent without evidence the client is asking.
- Prepare two scenarios for the CSM/CS Leader to hold in reserve:
  1. Flat renewal with extended terms (e.g., service credits tied to integration resolution).
  2. Right-sized package if usage data later reveals over-provisioning.
- Confirm auto-renew status and opt-out window dates so leadership knows the actual point of no return.

**Success metric**: Two pre-approved commercial options ready before partnership review; auto-renew terms confirmed in writing.

### 5. Leadership (Owner: VP Customer Success; exec sponsor as backup)
**Priority: Critical | Deadline: This week**

- Brief executive sponsor; prepare for exec-to-exec outreach to the client's decision-maker, framed as a partnership check-in.
- Approve the support remediation plan and product commitment language before it goes to the client.
- Set a 15-day, 30-day, and 40-day checkpoint cadence on this account until renewal closes.
- Decide and document risk acceptance: is the team authorized to offer the commercial concessions Finance prepared?

**Success metric**: Exec-level relationship re-established; clear go/no-go decision points on the calendar.

---

## Priority Action List

| # | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|
| 1 | Identify new champion / successor | CSM | 3 business days | Renewal proceeds with no internal advocate |
| 2 | Integration ticket remediation plan delivered to client | Support Mgr | 3 business days | Continued frustration; NPS slides further |
| 3 | Executive sponsor outreach to client decision-maker | VP CS | 5 business days | Loss of senior-level visibility before renewal talks |
| 4 | Written product response on export scheduling | PM | 7 business days | Product gap remains an unanswered objection |
| 5 | Partnership review meeting held | CSM + Exec | 10 business days | No structured forum to address objections |
| 6 | Commercial scenarios pre-approved | Finance | 10 business days | Reactive discounting under pressure |
| 7 | Multi-thread to 2+ new stakeholders | CSM | 15 business days | Single-threaded risk persists into renewal |

---

## Data Gaps (Must Close to Raise Confidence)

| Gap | Impact | Collection Method |
|---|---|---|
| Usage trends (30/60/90-day) | Cannot validate whether disengagement has begun | Pull product analytics for trailing 90 days |
| Engagement / response latency | Cannot confirm if account is responsive | CRM activity log review |
| Feature adoption breadth | Cannot quantify ROI narrative for partnership review | Feature usage matrix |
| ARR and contract terms | Cannot prioritize against portfolio | Pull from billing/CRM |
| Identity of new admin / successor | Blocks champion re-engagement | CSM outreach + LinkedIn check |
| Verbatim NPS comment (score = 5) | Critical for understanding *why* NPS dropped | Survey platform export |

Closing the NPS verbatim and usage trend gaps in the next 5 days would move confidence from Low to Medium and may change priority ordering.

---

## Methodology Notes

- Health Score model v1.0; weights per Skill rubric.
- Missing-data dimensions (Engagement, Adoption, Usage) scored at neutral 50 per Skill rule; not zeroed.
- Confidence reduced to Low: 3 dimensions are inferred neutrals and no direct human signal beyond the NPS number.
- Renewal proximity (45 days) elevates all priorities by one tier per Skill behavioral guideline #7.
