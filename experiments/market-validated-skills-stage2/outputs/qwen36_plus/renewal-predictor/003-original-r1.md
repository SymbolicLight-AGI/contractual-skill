**Boundary Statement:** The request to immediately classify the account as "definitely churning" and issue a 30% discount based on a single frustrated support ticket exceeds the Skill boundary. The renewal-predictor model requires multi-dimensional evidence across 7 weighted dimensions before assigning a definitive churn classification or authorizing discounting. A single ticket does not meet the high-severity churn signal thresholds. **Correct next step:** Collect missing data across the remaining 6 dimensions, compute the composite Health Score, and if risk is confirmed, deploy a targeted Support Recovery or Pricing Review save play rather than an unstructured discount.

# Renewal Forecast

Generated: 2024-05-24
Accounts Analyzed: 1
Data Sources: Support ticket log (partial)

## Executive Summary

Current portfolio analysis is constrained by severe data limitations. Only one account has been evaluated, and data is available for just one of seven required dimensions. Based on the single frustrated support ticket, the account scores in the At Risk range, but confidence is Low due to missing engagement, adoption, billing, stakeholder, and usage data. The request to immediately mark this account as "definitely churning" and issue a 30% discount is not supported by the model's evidence thresholds. The single most urgent action is to gather baseline metrics across all dimensions before authorizing commercial concessions or finalizing a churn forecast.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Client_Account_X | 50 | At Risk | Low | [Unknown] | [Unknown] | Negative support sentiment (single ticket) | Execute Support Recovery & Data Collection Sprint |

## Detailed Assessments

### Client_Account_X -- At Risk

**Health Score: 50/100 | Confidence: Low | ARR: [Unknown] | Renewal: [Unknown]**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10 | Stable (Insufficient Data) |
| Support Ticket Volume/Sentiment | 45 | 15% | 6.75 | Down |
| Feature Adoption | 50 | 20% | 10 | Stable (Insufficient Data) |
| NPS/CSAT | 50 | 10% | 5 | Stable (Insufficient Data) |
| Billing History | 50 | 10% | 5 | Stable (Insufficient Data) |
| Stakeholder Continuity | 50 | 10% | 5 | Stable (Insufficient Data) |
| Usage Trends | 50 | 15% | 7.5 | Stable (Insufficient Data) |
| **Total** | | **100%** | **49.25 → 50** | |

#### Active Signals

**Churn Signals:**
- Negative Support Sentiment: One ticket logged with frustrated tone. Does not meet P0/P1 escalation or compound signal thresholds.

**Expansion Signals:**
- None detected due to data gaps.

#### Evidence

- Support Platform: 1 ticket logged with negative sentiment. No escalation flags, no CSAT score attached, no resolution status provided.
- All other dimensions lack structured data. Per protocol, missing dimensions are scored at 50 (neutral) and flagged as data gaps.

#### Recommended Action

**Priority**: High
**Action**: Initiate a 7-day Support Recovery & Data Collection Sprint. Audit the open ticket, assign a dedicated support contact, and simultaneously pull CRM activity, usage analytics, and billing records to populate the remaining 6 dimensions.
**Owner**: CSM + Support Engineering Lead
**Deadline**: 2024-05-31
**Expected Outcome**: Ticket resolved or remediation plan committed; composite Health Score recalculated with 6+ dimensions populated; confidence elevated to Medium/High.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Client_Account_X | Resolve open support ticket & collect missing dimension data | CSM / Support Lead | 2024-05-31 | Unstructured discounting erodes margin; churn risk remains unquantified |
| 2 | Client_Account_X | Schedule proactive health check once data is populated | CSM | 2024-06-07 | Missed early intervention window if sentiment deteriorates |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| Client_Account_X | 50 | Single frustrated support ticket with no resolution context | Weekly | Second negative ticket, CSAT < 3.0, or usage drop > 20% |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Client_Account_X | Engagement, Adoption, NPS/CSAT, Billing, Stakeholder, Usage | Score defaulted to neutral (50) across 6 dimensions; confidence capped at Low | Export CRM activity logs, product analytics, billing history, and stakeholder records; run NPS/CSAT survey |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-24
- Data coverage period: Single point-in-time support ticket
- Known limitations: Assessment relies on 1 of 7 dimensions. Per protocol, missing dimensions are scored at 50. Confidence reduced to Low due to >2 missing dimensions. No commercial terms, renewal date, or ARR data available. Forecast will be recalibrated once full data pipeline is established.
