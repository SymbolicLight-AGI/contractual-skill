# Renewal Forecast

Generated: 2023-10-24
Accounts Analyzed: 1
Data Sources: Synthetic user prompt signals

## Executive Summary

The portfolio consists of 1 account currently evaluated as At Risk, representing $120,000 in ARR. The primary systemic threat is the departure of the executive sponsor combined with deteriorating product usage (18% drop in weekly active users) and rising support ticket volume. With the renewal window closing in 75 days, the single most urgent action item is to execute an Executive Sponsor Alignment play to identify and secure a new decision-maker before the renewal date.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Synthetic Account | 53 | At Risk | Low | $120,000 | T+75 Days | Executive Sponsor Departure + Usage Decline | Executive Sponsor Alignment |

## Detailed Assessments

### Synthetic Account -- At Risk

**Health Score: 53/100 | Confidence: Low | ARR: $120,000 | Renewal: T+75 Days**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 60 | 20% | 12 | Down |
| Support Ticket Volume/Sentiment | 50 | 15% | 7.5 | Down |
| Feature Adoption | 60 | 20% | 12 | Stable |
| NPS/CSAT | 50 | 10% | 5 | Unknown |
| Billing History | 50 | 10% | 5 | Unknown |
| Stakeholder Continuity | 50 | 10% | 5 | Down |
| Usage Trends | 40 | 15% | 6 | Down |
| **Total** | | **100%** | **53** | |

#### Active Signals

**Churn Signals:**
- Executive Turnover: The executive sponsor has left the organization. While the admin champion remains engaged, the lack of an executive sponsor with 75 days to renewal creates a critical vulnerability for budget approval.
- Usage Decline: Weekly active users (WAU) have dropped by 18%.
- Support Escalation Risk: Support ticket volume is trending upward, indicating potential friction or platform instability that may be driving the usage decline.

**Expansion Signals:**
- None detected.

#### Evidence

- **Stakeholder Continuity**: "Executive sponsor left, admin champion still engaged"
- **Usage Trends**: "Weekly active users down 18%"
- **Support**: "Support tickets up"
- **Feature Adoption**: "Two key workflows adopted"
- **Missing Data**: NPS/CSAT and Billing History were not provided and have been scored at a neutral 50.

#### Recommended Action

**Priority**: Critical
**Action**: Executive Sponsor Alignment. CS leadership must request an immediate meeting with the client's new decision-maker or department head. Frame as a partnership review. Come with a value summary of the two adopted workflows and a plan to address the rising support tickets.
**Owner**: CS Leader
**Deadline**: Within 5 business days
**Expected Outcome**: Meeting scheduled and held with the new executive sponsor; renewal path and budget secured.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Synthetic Account | Executive Sponsor Alignment | CS Leader | Within 5 business days | Account will churn due to lack of budget authority and declining perceived value. |

## Early Warning Watchlist

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| None | N/A | N/A | N/A | N/A |

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Synthetic Account | NPS/CSAT Scores | Reduced confidence to Low; forced neutral score (50). | Trigger an out-of-cycle pulse survey to the admin champion. |
| Synthetic Account | Billing History | Reduced confidence to Low; forced neutral score (50). | Query billing platform for payment history and discount dependency. |
| Synthetic Account | Support Ticket Sentiment & Severity | Unable to determine if rising tickets are critical bugs or minor questions. | Audit recent support tickets for P0/P1 tags and negative sentiment keywords. |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2023-10-24
- Data coverage period: Trailing 30-90 days (implied)
- Known limitations: Assessment relies on limited synthetic signals. Missing dimensions (NPS, Billing) were scored at a neutral 50 per scoring guidelines, which may artificially inflate or deflate the true health score. Confidence is capped at Low due to missing data across 3 dimensions.
