# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: Provided synthetic account signals, inferred metrics per dimension rubrics

## Executive Summary

One account analyzed with $120,000 ARR at risk, renewing in 75 days. The account scores 53/100, placing it in the **At Risk** category. The primary risk drivers are executive sponsor departure combined with an 18% decline in weekly active users and rising support ticket volume. While the admin champion remains engaged, the relationship is currently single-threaded at the leadership level. The most urgent action is to secure an executive alignment meeting with the new sponsor and deploy a targeted stakeholder re-engagement campaign within 10 business days to stabilize usage and address support friction before the renewal window closes.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Synthetic Account | 53 | At Risk | Medium | $120,000 | 2024-08-03 | Executive sponsor departure + 18% WAU decline | Executive alignment & stakeholder re-engagement |

## Detailed Assessments

### Synthetic Account -- At Risk

**Health Score: 53/100 | Confidence: Medium | ARR: $120,000 | Renewal: 2024-08-03**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 55 | 20% | 11.0 | Down |
| Support Ticket Volume/Sentiment | 60 | 15% | 9.0 | Up |
| Feature Adoption | 55 | 20% | 11.0 | Stable |
| NPS/CSAT | 50 | 10% | 5.0 | N/A |
| Billing History | 50 | 10% | 5.0 | N/A |
| Stakeholder Continuity | 55 | 10% | 5.5 | Down |
| Usage Trends | 45 | 15% | 6.75 | Down |
| **Total** | | **100%** | **53** | |

#### Active Signals

**Churn Signals:**
- **Champion Departure + Usage Decline (High-Severity)**: Executive sponsor has left the organization. Concurrently, WAU dropped 18%, indicating loss of top-down mandate and declining product dependency.
- **Support Escalation + Negative Sentiment (Medium-Severity)**: Support ticket volume is trending upward. While severity/sentiment data is incomplete, rising volume during a leadership transition often correlates with unresolved friction and eroding confidence.

**Expansion Signals:**
- None detected. Current usage contraction and leadership gap preclude expansion conversations until baseline health is restored.

#### Evidence

- **Usage**: WAU declined 18% over the trailing period. Approaches the 20% threshold for severe usage decline.
- **Support**: Ticket volume reported as "up". No specific severity, resolution time, or sentiment data provided.
- **Stakeholders**: Executive sponsor departed. Admin champion remains active and engaged, preserving a single point of continuity.
- **Adoption**: Two key workflows actively adopted. Indicates core value realization but limited breadth.
- **Missing Data**: NPS/CSAT survey results, billing/payment history, exact feature utilization matrix, and support ticket sentiment/severity breakdowns were not provided. Scores defaulted to 50 (neutral) per missing data protocol.

#### Recommended Action

**Priority**: High
**Action**: Execute Stakeholder Re-engagement Campaign paired with Executive Sponsor Alignment. CSM to map 3-5 additional stakeholders (IT, Finance, end-user leads) and deliver role-specific value briefs. CS Leader to request a partnership review with the new executive sponsor, presenting a 90-day value stabilization plan and addressing open support friction.
**Owner**: CSM (primary), CS Leader (executive outreach)
**Deadline**: 2024-05-30 (10 business days)
**Expected Outcome**: New sponsor briefed and engaged; 2+ additional stakeholders onboarded; support ticket volume stabilizes; WAU decline halts within 30 days.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Synthetic Account | Executive alignment & stakeholder re-engagement campaign | CSM / CS Leader | 2024-05-30 | New sponsor defaults to competitor evaluation; usage continues to decline; $120k ARR lost at renewal |

## Early Warning Watchlist

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| Synthetic Account | 53 | Admin champion is sole point of contact; support volume rising | Weekly | Champion departs or WAU drops >25% |

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Synthetic Account | NPS/CSAT scores & verbatim feedback | Scored neutral (50); unable to validate explicit satisfaction or detect detractor sentiment | Trigger relational NPS survey immediately; review recent support CSATs |
| Synthetic Account | Billing history & payment terms | Scored neutral (50); unable to assess financial commitment or discount dependency | Pull invoice/payment log from billing platform; verify auto-renew status |
| Synthetic Account | Support ticket severity & sentiment | Scored conservatively (60); unable to quantify friction impact | Run sentiment analysis on last 90 days of tickets; categorize by P0-P3 |
| Synthetic Account | Full feature adoption matrix | Scored conservatively (55); unable to measure breadth vs. purchased entitlements | Export feature usage report; compare active modules to contract |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: Trailing 30-90 days (inferred from provided signals)
- Known limitations: Assessment relies on limited synthetic signals. Three dimensions (NPS/CSAT, Billing, Support Sentiment) lacked direct data and were scored at neutral (50) per protocol. Confidence capped at Medium due to data gaps and single-threaded stakeholder visibility. Renewal proximity (75 days) elevates operational priority despite medium confidence.
