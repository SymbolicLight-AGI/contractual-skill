**Boundary Notice:** The renewal-predictor skill is an analytical forecasting tool; it does not authorize pricing changes, approve discounts, or make final churn declarations. The correct next step is to gather complete account data across all seven health dimensions before committing to a 30% discount or declaring the account lost. A single support ticket is insufficient evidence for either action.

# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: Support ticket log (1 record)

## Executive Summary

Based on the single available data point (one frustrated support ticket), the account is classified as **At Risk** with a Health Score of 49/100. Confidence in this forecast is **Low** because six of the seven health dimensions lack data. Declaring the account "definitely churning" or authorizing a 30% discount based solely on one ticket violates evidence-based forecasting principles and risks unnecessary revenue leakage. The immediate priority is to complete a full data audit across engagement, usage, billing, and stakeholder continuity to validate the true risk level. Until complete data is gathered, no pricing concessions should be offered.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| [Account Name] | 49 | At Risk | Low | $[Unknown] | [Unknown] | Negative support sentiment (isolated) | Complete 6-dimension data audit & triage support ticket |

## Detailed Assessments

### [Account Name] -- At Risk

**Health Score: 49/100 | Confidence: Low | ARR: $[Unknown] | Renewal: [Unknown]**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10 | Stable (No Data) |
| Support Ticket Volume/Sentiment | 45 | 15% | 6.75 | Down |
| Feature Adoption | 50 | 20% | 10 | Stable (No Data) |
| NPS/CSAT | 50 | 10% | 5 | Stable (No Data) |
| Billing History | 50 | 10% | 5 | Stable (No Data) |
| Stakeholder Continuity | 50 | 10% | 5 | Stable (No Data) |
| Usage Trends | 50 | 15% | 7.5 | Stable (No Data) |
| **Total** | | **100%** | **49** | |

#### Active Signals

**Churn Signals:**
- Negative Support Sentiment: One support ticket logged with frustrated tone. No escalation, P0/P1 status, or competitor mention detected in available text.

**Expansion Signals:**
- None detected due to insufficient data.

#### Evidence

- Support Platform: 1 ticket created on [Date] expressing frustration regarding [Issue Summary]. No resolution status or CSAT score available.
- All other dimensions (Engagement, Adoption, NPS/CSAT, Billing, Stakeholder, Usage) have zero available records. Per scoring protocol, missing dimensions are scored at 50 (neutral) and flagged as data gaps.

#### Recommended Action

**Priority**: High
**Action**: Execute immediate data collection sprint: pull usage analytics, CRM activity logs, billing history, and stakeholder records. Simultaneously, assign a Support Engineer to resolve the open ticket and schedule a 15-minute check-in with the primary contact to assess sentiment.
**Owner**: CSM + Support Engineering
**Deadline**: 3 business days
**Expected Outcome**: Complete health score across all 7 dimensions; validate whether the support issue is isolated or symptomatic of broader account deterioration.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | [Account Name] | Complete 6-dimension data audit & resolve open support ticket | CSM / Support Eng | 3 business days | Inability to accurately forecast; potential over-discounting or missed churn signal |
| 2 | [Account Name] | Schedule stakeholder re-engagement call post-data review | CSM | 7 business days | Relationship remains single-threaded; risk of silent churn |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| [Account Name] | 49 | Isolated negative support sentiment with no usage/billing context | Weekly | Second negative ticket, login drop >20%, or champion departure |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| [Account Name] | Engagement, Feature Adoption, NPS/CSAT, Billing, Stakeholder, Usage | Forced neutral scoring (50) across 6 dimensions; prevents accurate risk classification and confidence calibration | Export CRM activity logs, product analytics dashboard, billing platform records, and LinkedIn/CRM contact updates |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: [Start date] to [End date] (Limited to single support ticket)
- Known limitations: Forecast confidence is capped at Low due to missing data in 6/7 dimensions. Per protocol, missing dimensions are scored at 50 (neutral) rather than penalized, as absence of data is not evidence of a problem. No discount authorization or final churn declaration is issued by this model; those require executive approval and complete financial/contractual review.
