# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: User-provided sparse facts ("renewal this year", "customer uses the product")

## Executive Summary

Analyzed 1 account with highly sparse data. Due to missing information across 5 of 7 health dimensions, the account is classified as At Risk with Low confidence. The only confirmed signal is active product usage, but without trend, stakeholder, support, or billing data, renewal likelihood cannot be accurately predicted. Immediate data collection is required to move from speculative to actionable forecasting. The single most urgent action is to execute the data collection protocol and schedule a baseline discovery call to populate missing dimensions.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| [Account Name] | 50 | At Risk | Low | Unknown | 2024-12-31 | Insufficient data across 5 dimensions | Execute data collection protocol and schedule baseline health check |

## Detailed Assessments

### [Account Name] -- At Risk

**Health Score: 50/100 | Confidence: Low | ARR: Unknown | Renewal: 2024-12-31**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10 | Unknown |
| Support Ticket Volume/Sentiment | 50 | 15% | 7.5 | Unknown |
| Feature Adoption | 50 | 20% | 10 | Unknown |
| NPS/CSAT | 50 | 10% | 5 | Unknown |
| Billing History | 50 | 10% | 5 | Unknown |
| Stakeholder Continuity | 50 | 10% | 5 | Unknown |
| Usage Trends | 50 | 15% | 7.5 | Unknown |
| **Total** | | **100%** | **50** | |

#### Active Signals

**Churn Signals:**
- **Data Gap Churn Risk**: 5 of 7 dimensions lack data, forcing neutral baseline scoring. Per protocol, absence of data is not evidence of a problem, but it prevents risk mitigation planning.
- **Renewal Proximity**: Renewal is scheduled for this year. Without a clear health trajectory, the account defaults to At Risk classification.

**Expansion Signals:**
- None detected. Active product usage is confirmed but lacks depth or trend data to indicate expansion potential.

#### Evidence

- User confirmed: "customer uses the product" and "renewal this year".
- No usage trend, stakeholder map, support history, billing records, or contract value provided.
- All dimension scores defaulted to 50 (neutral) per missing data protocol.

#### Recommended Action

**Priority**: High
**Action**: Deploy data collection protocol using provided CSV templates. Schedule a baseline discovery call with the primary contact to map stakeholders, review usage trends, confirm contract terms, and gather support/billing history.
**Owner**: CSM
**Deadline**: 7 business days
**Expected Outcome**: Populate 4+ missing dimensions to raise confidence to Medium, establish a baseline health score, and identify specific risk or expansion signals.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | [Account Name] | Execute data collection & baseline discovery | CSM | 2024-05-27 | Inability to forecast renewal risk or deploy targeted save plays before renewal window |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| [Account Name] | 50 | Active usage confirmed but no trend or stakeholder data | Weekly | Usage drops below baseline, primary contact becomes unresponsive, or billing/support issues surface |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| [Account Name] | Support, Billing, Stakeholder, Usage Trends, NPS/CSAT | Forced neutral scoring (50) across 5 dimensions, resulting in Low confidence and At Risk classification | Provide CSV exports from CRM, billing system, support platform, and product analytics; complete stakeholder mapping template |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: Unknown
- Known limitations: 5 of 7 dimensions scored at neutral baseline (50) due to complete data absence. Confidence capped at Low per protocol. "Uses the product" fact noted but insufficient to elevate scores without frequency, depth, or trend metrics. Per behavioral guidelines, conservative prediction applied: absence of data defaults to At Risk classification to prevent false negatives.
