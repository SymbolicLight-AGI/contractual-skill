# Renewal Forecast

Generated: 2024-05-24
Accounts Analyzed: 1
Data Sources: CRM contact logs, Support ticketing system, NPS/CSAT survey platform, Billing records, Internal handoff notes

## Executive Summary

One account is currently classified as At Risk with a Health Score of 47/100 and Medium confidence. The account renews in 45 days, placing it in the high-urgency window. Primary risk drivers are stakeholder turnover (admin champion departed), unresolved integration support tickets, and a sharp NPS decline (8 to 5). Billing remains current, indicating no immediate financial friction, but a known product gap (export scheduling) is compounding dissatisfaction. Immediate cross-functional intervention is required to stabilize the relationship, resolve technical blockers, and align leadership before the renewal window closes. Total ARR at risk is unconfirmed and requires finance input.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| [Account Name] | 47 | At Risk | Medium | [$TBD] | 2024-07-08 | Champion departure + unresolved integration tickets | Executive alignment + emergency technical review + product roadmap briefing |

## Detailed Assessments

### [Account Name] -- At Risk

**Health Score: 47/100 | Confidence: Medium | ARR: [$TBD] | Renewal: 2024-07-08**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 40 | 20% | 8.0 | Down |
| Support Ticket Volume/Sentiment | 35 | 15% | 5.25 | Down |
| Feature Adoption | 55 | 20% | 11.0 | Stable |
| NPS/CSAT | 40 | 10% | 4.0 | Down |
| Billing History | 80 | 10% | 8.0 | Stable |
| Stakeholder Continuity | 35 | 10% | 3.5 | Down |
| Usage Trends | 45 | 15% | 6.75 | Down |
| **Total** | | **100%** | **46.5 → 47** | |

#### Active Signals

**Churn Signals:**
- **Champion Departure + Usage Decline**: Admin champion changed roles with no documented successor. Engagement frequency dropped to sporadic levels as primary point of contact shifted.
- **Support Escalation + Negative Sentiment**: Integration tickets remain unresolved, driving negative sentiment and directly correlating with the NPS drop from 8 to 5.
- **Survey Non-Response/Drop**: NPS fell 3 points into low Passive territory, indicating growing dissatisfaction and potential competitive evaluation.

**Expansion Signals:**
- None identified. Current focus is strictly retention and risk mitigation.

#### Evidence

- CRM logs confirm admin champion role change within the last 30 days; no replacement contact logged.
- Support system shows 3+ open integration tickets with SLA breaches; client communication tone reflects frustration.
- NPS survey data shows score drop from 8 (Passive) to 5 (Detractor/Low Passive) in the most recent cycle.
- Billing records show all invoices paid on time; no disputes or late payments in trailing 12 months.
- Product roadmap notes confirm "export scheduling" is a requested capability not currently supported, cited in recent client feedback.
- Usage analytics unavailable for trailing 30/60/90 days; score inferred from engagement drop and support friction.

#### Recommended Action

**Priority**: Critical
**Action**: Execute cross-functional rescue plan: (1) CS leadership schedules executive alignment call with new decision-maker within 5 days. (2) Support Engineering deploys dedicated resource to resolve integration tickets with committed ETAs. (3) Product Management provides roadmap timeline for export scheduling or approved workaround. (4) Finance prepares renewal options with value-aligned pricing. (5) Leadership approves executive-to-executive outreach if competitive threat emerges.
**Owner**: CS Leader (primary), Support Engineering, Product Manager, Finance BP, VP of CS
**Deadline**: 2024-05-31 (Initial alignment & technical triage complete)
**Expected Outcome**: New stakeholder onboarded, critical tickets resolved or have committed resolution dates, product gap addressed via roadmap/workaround, renewal conversation initiated with clear value narrative.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | [Account Name] | Executive Sponsor Alignment: Schedule partnership review with new decision-maker; present value summary, roadmap preview, and dedicated support offer | CS Leader / VP of CS | 2024-05-29 | New stakeholder evaluates alternatives without context; renewal lost |
| 2 | [Account Name] | Emergency Technical Review: Assign senior engineer to resolve open integration tickets; provide daily status updates and temporary direct support channel | Support Engineering | 2024-05-31 | Client loses confidence in platform reliability; churn accelerates |
| 3 | [Account Name] | Product Gap Mitigation: Deliver export scheduling workaround or confirmed roadmap ETA; document in client-facing success plan | Product Manager | 2024-06-03 | Client cites missing capability as primary reason for non-renewal |
| 4 | [Account Name] | Financial Restructure & Renewal Prep: Model renewal options aligned to actual usage; prepare discount/term flexibility if required to retain | Finance BP | 2024-06-07 | Pricing friction emerges late in cycle; negotiation leverage lost |
| 5 | [Account Name] | Stakeholder Re-engagement Campaign: Identify and onboard 2-3 additional operational users to multi-thread relationship before renewal | CSM | 2024-06-10 | Single-threaded dependency increases churn risk if new contact disengages |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| [Account Name] | 47 | Champion turnover + unresolved technical debt | Weekly | NPS drops below 4, or new stakeholder declines QBR/renewal meeting |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| [Account Name] | Trailing 30/60/90-day usage analytics (DAU/WAU, session trends, API volume) | Usage trend scored conservatively at 45; actual momentum unknown | Request product analytics export or enable account-level telemetry tracking |
| [Account Name] | Confirmed ARR / Contract Value | Cannot quantify revenue at risk or prioritize against portfolio | Finance/RevOps to pull contract value from billing/CRM system |
| [Account Name] | New stakeholder contact details & role scope | Limits targeted outreach and executive alignment planning | CSM to request updated org chart from client procurement or IT admin |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-24
- Data coverage period: 2024-02-24 to 2024-05-24
- Known limitations: Usage trend and engagement frequency scores are partially inferred due to missing product telemetry. ARR is unconfirmed. Confidence capped at Medium per calibration rules (4-5 dimensions with direct data, mixed signal consistency, missing telemetry). All recommendations are time-bound to the 45-day renewal window.
