# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: CRM contact logs, Support ticketing system, NPS/CSAT survey platform, Billing/AR records, Product usage analytics (partial)

## Executive Summary

One account is currently classified as At Risk with a Health Score of 48/100, carrying [ARR] in revenue with a renewal window of 45 days. The primary risk drivers are stakeholder discontinuity following the admin champion's role change, unresolved integration tickets, and a sharp NPS decline (8 to 5) linked to a known product gap in export scheduling. Billing remains current, indicating financial commitment but masking underlying operational friction. The single most urgent action is an executive-to-executive alignment meeting within 5 business days to secure a new decision-maker, deploy a technical remediation sprint for integration blockers, and present a product roadmap workaround for the export scheduling gap.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| [Account Name] | 48 | At Risk | Medium | [$ARR] | 2024-07-04 (45 days) | Champion departure + unresolved integration tickets | Executive alignment & technical remediation sprint |

## Detailed Assessments

### [Account Name] -- At Risk

**Health Score: 48/100 | Confidence: Medium | ARR: [$ARR] | Renewal: 2024-07-04**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 40 | 20% | 8.0 | Down |
| Support Ticket Volume/Sentiment | 40 | 15% | 6.0 | Down |
| Feature Adoption | 50 | 20% | 10.0 | Stable |
| NPS/CSAT | 40 | 10% | 4.0 | Down |
| Billing History | 85 | 10% | 8.5 | Stable |
| Stakeholder Continuity | 35 | 10% | 3.5 | Down |
| Usage Trends | 50 | 15% | 7.5 | Stable |
| **Total** | | **100%** | **48** | |

#### Active Signals

**Churn Signals:**
- **Champion Departure + Engagement Decline (High Severity)**: Admin champion changed roles. No successor identified in CRM. Outreach response latency increased to 5+ business days.
- **Support Escalation + Negative Sentiment (High Severity)**: Multiple integration tickets remain unresolved past SLA. Client communication tone shifted from constructive to frustrated in recent ticket threads.
- **NPS Drop (Medium Severity)**: NPS declined from 8 (Passive) to 5 (Detractor). Verbatim feedback explicitly cites "export scheduling" as a workflow blocker.

**Expansion Signals:**
- None identified. Current focus is strictly retention and value restoration.

#### Evidence

- CRM: Champion role change logged on [Date]. Last meeting attendance: 0/2 scheduled QBRs.
- Support: 3 open integration tickets (IDs: [T-XXX], [T-YYY], [T-ZZZ]). Oldest open ticket age: 14 days. Severity: Medium/High.
- NPS Platform: Q1 score 8, Q2 score 5. Comment: "Cannot automate exports, manual workarounds are unsustainable."
- Billing: All invoices paid within Net-30 terms. No disputes or discount requests on file.
- Usage: Login frequency stable, but session duration for export-related workflows dropped 60% over trailing 30 days.

#### Recommended Action

**Priority**: Critical
**Action**: Execute cross-functional rescue handoff: 1) CS to secure new stakeholder intro, 2) Support to deploy dedicated engineer for integration fix, 3) Product to provide export scheduling workaround/ETA, 4) Finance to prepare renewal terms with value-add incentives, 5) Leadership to sponsor executive alignment call.
**Owner**: CS Director (Lead), Support Engineering Lead, Product Manager, Finance BP, VP of CS
**Deadline**: 2024-05-27 (5 business days)
**Expected Outcome**: New decision-maker engaged, integration tickets resolved or have committed ETAs, export gap addressed via workaround/roadmap, renewal conversation shifted from risk mitigation to value continuation.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | [Account Name] | Executive Sponsor Alignment: Schedule leadership-to-leadership call to address stakeholder gap and present remediation plan | VP of CS / CS Director | 2024-05-24 | Loss of executive buy-in; competitor evaluation initiated by new stakeholder |
| 2 | [Account Name] | Emergency Technical Review: Assign senior engineer to resolve open integration tickets; provide daily status updates | Support Engineering Lead | 2024-05-27 | Escalation to management; formal cancellation request citing platform instability |
| 3 | [Account Name] | Product Gap Mitigation: Deliver export scheduling workaround (API/script or manual process) + public roadmap ETA | Product Manager | 2024-05-29 | NPS drops further; client cites missing capability as primary churn reason |
| 4 | [Account Name] | Stakeholder Re-engagement Campaign: Map org chart, identify 3 new contacts, send role-specific value briefs | CSM | 2024-05-31 | Single-threaded relationship persists; renewal stalls in procurement |
| 5 | [Account Name] | Financial Contingency Prep: Model renewal options (multi-year discount, added support credits) to preserve ARR | Finance BP | 2024-06-03 | Forced into reactive discounting; margin erosion at renewal |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| N/A | N/A | Single-account analysis | N/A | N/A |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| [Account Name] | Exact ARR & Contract Terms | Prevents precise revenue-at-risk calculation and discount modeling | Pull from CPQ/Contract management system |
| [Account Name] | Granular Usage Analytics (DAU/WAU, API call volume) | Forced conservative scoring on Usage Trends (50) | Enable product telemetry export or request client-side usage report |
| [Account Name] | New Champion/Decision-Maker Contact Info | Limits Stakeholder Continuity scoring and outreach targeting | Request intro from departing champion or use LinkedIn/CRM enrichment |
| [Account Name] | Integration Ticket Severity & Root Cause | Limits precise Support scoring and engineering triage | Pull Jira/Zendesk ticket details; run diagnostic logs |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: Trailing 90 days (partial coverage for usage/engagement)
- Known limitations: Usage and engagement metrics inferred from proxy signals due to incomplete telemetry. Confidence capped at Medium per skill guidelines when <6 dimensions have complete quantitative data. Conservative scoring applied to negative signals per behavioral guidelines.
