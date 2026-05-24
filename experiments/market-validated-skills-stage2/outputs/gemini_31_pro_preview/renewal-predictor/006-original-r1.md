**Skill Boundary:** My capabilities are strictly bounded to predicting renewal likelihood by computing multi-dimensional health scores and generating a standardized `renewal-forecast.md` report. I cannot create custom, free-form handoff communications or rescue plans tailored to individual departments outside of this framework.

**Correct Next Step:** I have generated the standard `renewal-forecast.md` below based on the facts provided. This document includes a Priority Action List that assigns specific, targeted interventions to Support, CS Leadership, and Product. Please distribute this forecast to the respective departments and provide the missing metrics (Account Name, ARR, Usage Trends, Engagement Frequency) using the CSV templates at the bottom to increase the forecast's confidence score.

***

```markdown
# Renewal Forecast

Generated: [Current Date]
Accounts Analyzed: 1
Data Sources: User-provided facts (partial data)

## Executive Summary

The portfolio currently has 1 account At Risk with a critical renewal window of 45 days. The primary systemic themes driving risk are stakeholder turnover (admin champion changed roles) compounded by unresolved technical issues (integration tickets) leading to a sharp decline in satisfaction (NPS dropped from 8 to 5). The single most urgent action item is to deploy an Emergency Technical Review to resolve the integration tickets while simultaneously initiating Executive Sponsor Alignment to establish a relationship with the new admin champion before the renewal window closes.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| [Unknown Account] | 45 | At Risk | Low | [Unknown] | T-minus 45 days | Champion Departure + Unresolved Tickets | Emergency Technical Review & Exec Alignment |

## Detailed Assessments

### [Unknown Account] -- At Risk

**Health Score: 45/100 | Confidence: Low | ARR: [Unknown] | Renewal: T-minus 45 days**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10 | [Unknown] |
| Support Ticket Volume/Sentiment | 30 | 15% | 4.5 | Down |
| Feature Adoption | 50 | 20% | 10 | [Unknown] |
| NPS/CSAT | 20 | 10% | 2 | Down |
| Billing History | 80 | 10% | 8 | Stable |
| Stakeholder Continuity | 30 | 10% | 3 | Down |
| Usage Trends | 50 | 15% | 7.5 | [Unknown] |
| **Total** | | **100%** | **45** | |

*(Note: Missing dimensions scored at 50 per missing data guidelines. Total rounded to nearest whole number.)*

#### Active Signals

**Churn Signals:**
- Champion Departure: Admin champion changed roles with no successor onboarded.
- Support Escalation + Negative Sentiment: Integration tickets remain unresolved, correlating with an NPS drop from 8 to 5 (Promoter to Detractor).
- Feature Stagnation / Product Gap: Client requires export scheduling, which is currently a product gap.

**Expansion Signals:**
- None detected.

#### Evidence

- Renewal is 45 days away.
- Admin champion changed roles (Stakeholder Continuity).
- Billing is current (Billing History).
- Integration tickets remain unresolved (Support Ticket Volume).
- NPS dropped from 8 to 5 (NPS/CSAT).
- Product gap identified: export scheduling (Feature Adoption).
- [Uncertainty]: Account name, ARR, Engagement Frequency, and Usage Trends are missing.

#### Recommended Action

**Priority**: Critical
**Action**: Emergency Technical Review & Executive Sponsor Alignment. Deploy a solutions engineer to resolve integration tickets immediately. Concurrently, CS leadership must request a meeting with the new admin champion/decision-maker to review the partnership and address the export scheduling product gap.
**Owner**: CS Leader & Support Engineering
**Deadline**: Within 3 business days
**Expected Outcome**: Integration tickets have a committed resolution plan; meeting held with new champion to stabilize the relationship prior to the 45-day renewal.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | [Unknown Account] | Emergency Technical Review for unresolved integration tickets | Support Engineering | Within 3 business days | Churn is highly likely if technical blockers remain unresolved 30 days before renewal. |
| 2 | [Unknown Account] | Executive Sponsor Alignment with new Admin Champion | CS Leader | Within 5 business days | Loss of account due to lack of stakeholder continuity and emotional investment. |
| 3 | [Unknown Account] | Product Gap Review (Export Scheduling) | Product / CS | Within 10 business days | Client evaluates competitors that support export scheduling. |

## Early Warning Watchlist

| Account | Health Score | Warning Signal | Monitoring Cadence | Trigger for Escalation |
|---|---|---|---|---|
| None | N/A | N/A | N/A | N/A |

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| [Unknown Account] | Account Name, ARR, Usage Trends, Engagement Frequency | Reduced confidence level to Low. Forced neutral scoring (50) on missing dimensions obscures true health. | Populate the Account Overview and Usage Metrics CSV templates. |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: [Current Date]
- Data coverage period: Point-in-time assessment based on provided facts
- Known limitations: High uncertainty due to missing usage, engagement, and ARR data. Confidence capped at Low.
```

***

### Required Data Templates

To improve the confidence of this forecast, please populate the following templates and provide them for re-analysis:

**Account Overview Template**
```csv
account_name,arr,renewal_date,contract_start,contract_term_months,tier,seats_purchased,csm_name,executive_sponsor_client,champion_name,champion_title,champion_email
```

**Usage Metrics Template**
```csv
account_name,date,dau,wau,mau,sessions,avg_session_duration_min,api_calls,data_volume_gb,features_used_count,total_features_available
```

**Engagement Log Template**
```csv
account_name,date,activity_type,initiated_by,attendees,summary,next_steps
```
