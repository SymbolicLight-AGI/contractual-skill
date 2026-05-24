```markdown
# Renewal Forecast

Generated: 2025-04-10
Accounts Analyzed: 1
Data Sources: Provided fact set (renewal date, champion change, billing status, unresolved tickets, NPS history, product gap); usage and engagement data not provided; no CRM exports or other files available.

## Executive Summary

One account is assessed with a Health Score of 40 (At Risk), driven primarily by an admin champion role change, a 3-point NPS drop to Detractor territory (5), unresolved integration support tickets, and a critical product gap in export scheduling. With renewal only 45 days away, immediate cross-functional intervention is required. The account represents unknown ARR, but given the urgency, the recommended save play involves a coordinated effort across CS, Support, Product, Finance, and Leadership to re-anchor the relationship, resolve technical issues, address the product gap, and present a compelling renewal package.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Client ABC | 40 | At Risk | Low | Not Provided | 2025-05-25 (45 days) | Admin champion changed roles + NPS drop (8→5) + unresolved integration tickets + export scheduling product gap | Emergency cross-functional save play: CS re-engagement, Support remediation, Product roadmap commitment, Finance review, Executive Sponsor alignment |

## Detailed Assessments

### Client ABC -- At Risk

**Health Score: 40/100 | Confidence: Low | ARR: Not Provided | Renewal: 2025-05-25 (45 days)**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 35 | 20% | 7.0 | Down (inferred) |
| Support Ticket Volume/Sentiment | 30 | 15% | 4.5 | Down |
| Feature Adoption | 45 | 20% | 9.0 | Stable/Limiting |
| NPS/CSAT | 30 | 10% | 3.0 | Down (8→5) |
| Billing History | 90 | 10% | 9.0 | Stable |
| Stakeholder Continuity | 20 | 10% | 2.0 | Down (champion role change) |
| Usage Trends | 50 | 15% | 7.5 | Unknown (data gap) |
| **Total** | | **100%** | **40.0** | |

#### Active Signals

**Churn Signals (High Severity):**
- **Champion Role Change + NPS Drop**: The admin champion has changed roles (no successor identified), and NPS simultaneously dropped from 8 (Passive) to 5 (Detractor). This compound signal indicates organizational instability and deteriorating satisfaction.
- **Unresolved Integration Tickets + Product Gap**: Multiple integration tickets remain unresolved, and the client specifically lacks export scheduling – a feature that likely drives their core workflows. This creates a double technical friction point.
- **Renewal Proximity**: Only 45 days remain; the window for remediation is compressed.

**Expansion Signals:** None detected.

#### Evidence

- **NPS/CSAT**: Historical NPS 8 → current NPS 5. Verbatim comments not available; assumed declining trend.
- **Support**: Integration tickets are open and unresolved. Severity unknown, but combined with NPS drop, sentiment is likely negative.
- **Stakeholder Continuity**: Admin champion changed roles; no replacement or handoff confirmed. This is a known fact.
- **Billing**: Billing is current; no disputes or late payments.
- **Product Gap**: Export scheduling feature missing, cited as a product gap – likely tied to unresolved integration tickets and NPS deterioration.
- **Missing Data**: No usage metrics (DAU/MAU, session trends), engagement logs (meeting history, QBR attendance), feature adoption details, or ARR figures. Scores for Engagement, Feature Adoption, and Usage are conservatively estimated based on indirect signals. See Data Gaps section.

#### Recommended Action

**Priority**: Critical  
**Action**: Execute a coordinated rescue plan across five fronts:
1. **CS / Executive Sponsor Alignment**: Within 48 hours, VP of CS or executive sponsor contacts the client’s new admin (or their superior) to schedule a 45-minute “Partnership Health & Roadmap Review.” Objective: acknowledge the change, validate the product gap, present the recovery plan, and secure a commitment to pause any competitive evaluation. Bring a draft mutual success plan covering export scheduling workaround and integration fixes.
2. **Support – Emergency Technical Review**: Assign a dedicated solutions engineer to audit all open integration tickets. Within 3 business days, deliver a written remediation timeline with daily progress standups. Offer a direct Slack channel for real-time communication.
3. **Product – Roadmap Commitment**: Product manager provides a written statement on export scheduling roadmap (target GA quarter, beta availability). If feasible, offer early access or a custom extension/workaround as a bridging solution.
4. **Finance – Renewal Package Review**: Prepare a no-discount standard renewal proposal, but authorize a one-time, time-bound concession (e.g., waived price increase or 60-day extended transition) contingent on a multi-year commitment, to be used only if value objections persist. Ensure billing continues to be processed smoothly; coordinate with CS on messaging.
5. **Leadership – Executive-to-Executive Call**: Your CEO or SVP sends a brief note to the client’s executive sponsor (or new admin’s manager) reiterating the strategic importance of the partnership and offering direct dialogue on product direction.

**Owner**: CS Leader (overall coordinator), Support Engineering Lead, Product Manager, Finance Director, executive sponsor  
**Deadline**: Initial executive outreach by EOD April 11; technical review delivered by April 14; all open tickets resolved or with committed plan by April 25; renewal recommitment obtained before May 10.  
**Expected Outcome**: Client’s confidence restored; integration issues resolved; product gap addressed with a credible timeline; renewal secured at equal or higher value with no material discount dependency.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Client ABC | Schedule executive alignment call with new stakeholder | CS Leader / Executive Sponsor | April 11, 2025 | Client solidifies negative perception; competitive evaluation accelerates |
| 2 | Client ABC | Audit and resolve all integration tickets; provide written remediation plan | Support Engineering Lead | April 14, 2025 | Technical pain persists, reinforcing justification for churn |
| 3 | Client ABC | Deliver export scheduling roadmap commitment & potential interim solution | Product Manager | April 16, 2025 | Client perceives product neglect; gap remains renewal blocker |
| 4 | Client ABC | Prepare renewal package (standard + contingency concession) | Finance Director | April 18, 2025 | Inability to present flexible offer if value gaps remain |
| 5 | Client ABC | Executive-to-executive outreach from CEO/SVP | CEO/SVP | April 12, 2025 | Weak signal to client that partnership is transactional, not strategic |
| 6 | Client ABC | Re-establish champion relationship: identify new power user, conduct targeted onboarding | CSM | April 25, 2025 | Remain single-threaded, further increasing personnel risk |

## Early Warning Watchlist

No other accounts to monitor at this time.

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Client ABC | Usage metrics (DAU/WAU/MAU, session duration, API calls, feature-level adoption) | Engagement, Feature Adoption, and Usage Trends scores are inferred/conservative; Health Score may be over- or under-estimated. Confidence reduced to Low. | Pull product analytics for last 90 days; export and share as CSV following the Usage Metrics template. |
| Client ABC | Engagement history (QBR attendance, CSM emails/calls, response times) | Stakeholder Continuity and Engagement Frequency scores based only on champion change fact; may miss positive engagement signals. | Extract CRM activity log for the account; share as CSV. |
| Client ABC | ARR and contract details | Revenue impact not quantified; prioritization among other accounts cannot be done. | Provide current ARR and renewal contract value. |
| Client ABC | Support ticket details (severity, age, CSAT) | Support dimension score broadly estimated; severity could be higher or lower. | Export ticket list from support platform with severity and satisfaction fields. |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2025-04-10 (default)
- Data coverage period: Assumed trailing 90 days, but actual data only from provided facts and inferred trends.
- Known limitations: Extremely limited data set; scores for Engagement, Feature Adoption, and Usage Trends are estimates based on indirect signals. Confidence is Low. Forecast should be updated as soon as actual usage and engagement data become available. The account name and ARR are placeholders; replace with actuals.
```
