# Renewal Forecast

Generated: 2024-05-20
Accounts Analyzed: 1
Data Sources: Synthetic account signals, product analytics (WAU trends), support ticketing system, CRM contact records

## Executive Summary

The portfolio contains one account currently classified as **At Risk** with a composite Health Score of 54/100. The account carries $120k ARR with a renewal window of 75 days, placing it in the elevated urgency tier. The primary risk drivers are executive sponsor departure, declining weekly active users (-18%), and rising support ticket volume, which together indicate weakening organizational commitment and potential value realization gaps. The single most urgent action is to execute an Executive Sponsor Alignment play to re-establish strategic buy-in while simultaneously deploying a Stakeholder Re-engagement Campaign to prevent single-threaded dependency on the remaining admin champion.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Client Alpha | 54 | At Risk | Medium | $120,000 | 2024-08-03 | Executive sponsor departure + 18% WAU decline | Executive Sponsor Alignment & Stakeholder Re-engagement |

## Detailed Assessments

### Client Alpha -- At Risk

**Health Score: 54/100 | Confidence: Medium | ARR: $120,000 | Renewal: 2024-08-03**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 55 | 20% | 11.0 | Down |
| Support Ticket Volume/Sentiment | 50 | 15% | 7.5 | Up |
| Feature Adoption | 60 | 20% | 12.0 | Stable |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown |
| Billing History | 50 | 10% | 5.0 | Unknown |
| Stakeholder Continuity | 55 | 10% | 5.5 | Down |
| Usage Trends | 55 | 15% | 8.25 | Down |
| **Total** | | **100%** | **54** | |

#### Active Signals

**Churn Signals:**
- **Champion/Sponsor Departure + Usage Decline (High-Severity)**: Executive sponsor has left the organization while WAU dropped 18% over the trailing period. This compound signal strongly predicts churn as new leadership lacks emotional investment and declining usage removes the business case for retention.
- **Support Volume Increase (Medium-Severity)**: Ticket volume is trending upward. Without severity or sentiment data, this indicates potential friction, unresolved issues, or onboarding gaps that are consuming client resources.
- **Single-Threaded Relationship (Medium-Severity)**: Only the admin champion remains actively engaged. Loss of this contact would sever the primary communication and advocacy channel.

**Expansion Signals:**
- None detected. Current usage contraction and stakeholder turnover indicate consolidation, not growth.

#### Evidence

- **Usage Trends**: Product analytics show WAU declined 18% over the trailing evaluation window. No seasonal adjustment applied (industry unknown).
- **Stakeholder Continuity**: CRM records confirm executive sponsor departure. Admin champion remains active and engaged in day-to-day operations.
- **Support**: Ticketing system shows upward volume trend. Severity distribution and CSAT scores unavailable.
- **Feature Adoption**: System logs confirm two core workflows are actively adopted. No data on advanced features, API usage, or total purchased modules.
- **Missing Data**: No NPS/CSAT survey responses, billing history, or meeting attendance logs available for this account.

#### Recommended Action

**Priority**: Critical
**Action**: Execute Executive Sponsor Alignment play. CS leadership to request a strategic partnership review with the client's current decision-maker (or interim sponsor) within 5 business days. Frame as a value realization and roadmap alignment session, not a retention negotiation. Prepare a 90-day success plan highlighting the two adopted workflows and propose a dedicated technical review to address rising support volume.
**Owner**: VP of Customer Success / Strategic CSM
**Deadline**: 2024-05-27
**Expected Outcome**: Executive meeting held; interim or new sponsor identified; competitive evaluation paused; mutual success plan drafted and agreed upon.

## Priority Action List

Ranked list of interventions sorted by urgency and impact. This is the operational output that the CS team should execute against.

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Client Alpha | Executive Sponsor Alignment & Strategic Review | VP of CS / Strategic CSM | 2024-05-27 | New leadership defaults to competitor evaluation or non-renewal due to lack of relationship continuity |
| 2 | Client Alpha | Stakeholder Re-engagement Campaign | CSM | 2024-06-03 | Single-threaded dependency on admin champion creates catastrophic churn risk if they depart |
| 3 | Client Alpha | Support Ticket Audit & Resolution Plan | Support Engineering Lead | 2024-05-24 | Rising ticket volume compounds frustration and accelerates usage decline |

## Early Warning Watchlist

Accounts that are currently healthy but showing early signals that could deteriorate. These are not yet at risk but should be monitored more closely over the next 30-60 days.

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| Client Alpha | 54 | Admin champion is sole point of contact; WAU declining | Weekly | WAU drops >25% or champion shows signs of disengagement (missed meetings, delayed replies) |

## Data Gaps

Accounts or dimensions where insufficient data prevented a confident assessment. These gaps should be filled to improve future forecast accuracy.

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Client Alpha | NPS/CSAT survey history | Scored at neutral (50); unable to validate explicit satisfaction or detect detractor sentiment | Trigger relational NPS survey immediately; pull transactional CSAT from recent support closures |
| Client Alpha | Billing & payment history | Scored at neutral (50); unable to assess discount dependency, payment timeliness, or expansion intent | Export billing platform records; review contract terms and renewal pricing history |
| Client Alpha | Support ticket severity & sentiment | Scored conservatively (50); unable to distinguish between minor questions and critical blockers | Run sentiment analysis on open/closed tickets; categorize by P0-P4 severity |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2024-05-20
- Data coverage period: Trailing 90 days (implied by WAU trend and support volume metrics)
- Known limitations: Assessment relies on limited synthetic signals. NPS/CSAT and Billing dimensions scored at neutral (50) per missing data protocol. Confidence capped at Medium due to 2 missing dimensions and absence of direct human sentiment signals. Usage trend scoring assumes non-seasonal baseline. All recommendations prioritize renewal proximity (75 days) and ARR impact ($120k).
