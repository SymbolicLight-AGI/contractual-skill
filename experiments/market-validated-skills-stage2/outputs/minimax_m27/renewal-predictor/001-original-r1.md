<think>The user wants me to produce a renewal-forecast.md file based on the synthetic account data they've provided. Let me analyze the data:

**Account Data:**
- Renewal in 75 days (within 90-day urgency window)
- ARR: $120k
- Weekly active users down 18% (usage decline)
- Support tickets up (negative signal)
- Executive sponsor left (stakeholder continuity issue)
- Admin champion still engaged (partial positive)
- Two key workflows adopted (feature adoption signal)

Let me score each dimension:

**1. Engagement Frequency (20%)**
- WAU down 18% - this is a notable decline
- Admin champion still engaged - positive
- No mention of QBR attendance, meeting responsiveness, etc.
- Score: 50-69 range. Let's say 55 (declining but champion still active)

**2. Support Ticket Volume and Sentiment (15%)**
- Tickets are up - negative signal
- No mention of severity, CSAT, or sentiment
- Score: 50-69 range. Let's say 55 (volume up but no severity details)

**3. Feature Adoption (20%)**
- Two key workflows adopted
- No mention of total features purchased vs. used
- Score: 50-69 range. Let's say 60 (core workflows active, but limited info on breadth)

**4. NPS/CSAT Scores (10%)**
- No data provided
- Score: 50 (neutral, data gap)

**5. Billing History (10%)**
- No data provided
- Score: 50 (neutral, assume good unless stated otherwise)

**6. Stakeholder Continuity (10%)**
- Executive sponsor left - major red flag
- Admin champion still engaged - partial positive
- Score: 30-49 range. Let's say 40 (champion active but executive sponsor gone)


- Usage trending downward at 18% decline over the past month suggests potential churn risk. Score: 35-45 range. Let's say 40 (declining but not catastrophic yet)

**Composite Score:**
(55 × 0.20) + (55 × 0.15) + (60 × 0.20) + (50 × 0.10) + (50 × 0.10) + (40 × 0.10) + (40 × 0.15) = 11 + 8.25 + 12 + 5 + 5 + 4 + 6 = 51.25 → 51

This puts the account in the 40-59 "At Risk" band, with medium confidence given limited data across several dimensions. The combination of declining usage, rising support volume, and executive sponsor departure creates meaningful churn risk, especially with renewal approaching in 75 days. I should flag this as requiring immediate intervention and prepare the renewal-forecast.md output.
</think>

```markdown
# Renewal Forecast

Generated: 2025-01-17
Accounts Analyzed: 1
Data Sources: Synthetic account signals (provided by user)

---

## Executive Summary

**Portfolio Health Summary:** This single account is classified as **At Risk** with a Health Score of 51/100. The account carries $120,000 ARR and renews in 75 days, placing it within the critical 90-day renewal window.

**Key Risk Drivers:**
- Executive sponsor departure (critical stakeholder continuity gap)
- 18% decline in weekly active users (usage momentum negative)
- Support ticket volume increase (strain on relationship)

**Top Systemic Theme:** Stakeholder disruption combined with usage decline is the primary risk vector. The admin champion remains engaged, which provides a re-engagement anchor, but the absence of executive sponsorship leaves the account vulnerable to competitive evaluation.

**Most Urgent Action:** Schedule an executive alignment meeting within 5 business days to replace the departed executive sponsor and reaffirm strategic commitment before the renewal window closes.

---

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Synthetic Account | 51 | At Risk | Medium | $120,000 | 2025-04-02 | Executive sponsor departed; WAU down 18% | Executive sponsor re-engagement campaign |

---

## Detailed Assessments

### Synthetic Account -- At Risk

**Health Score: 51/100 | Confidence: Medium | ARR: $120,000 | Renewal: 2025-04-02**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|
| Engagement Frequency | 55 | 20% | 11.0 | Down |
| Support Ticket Volume/Sentiment | 55 | 15% | 8.25 | Down |
| Feature Adoption | 60 | 20% | 12.0 | Stable |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown |
| Billing History | 50 | 10% | 5.0 | Unknown |
| Stakeholder Continuity | 40 | 10% | 4.0 | Down |
| Usage Trends | 40 | 15% | 6.0 | Down |
| **Total** | | **100%** | **51.25 → 51** | |

#### Active Signals

**Churn Signals:**
- **Executive Sponsor Departure**: The executive sponsor has left the organization. No replacement has been identified or introduced to the CS team. This creates a power vacuum at the decision-making level and increases vulnerability to competitive evaluation by incoming leadership.
- **Usage Decline (18% WAU Drop)**: Weekly active users have declined 18% over the trailing period. This indicates reduced organizational investment in the product and may signal that the remaining champion is struggling to maintain internal advocacy without executive cover.
- **Support Ticket Volume Increase**: Ticket volume has increased, suggesting either product friction, workflow complexity, or declining user proficiency. Without sentiment data, the severity is unclear, but upward volume trends are a warning sign.

**Expansion Signals:**
- No expansion signals detected. The account is in a defensive posture.

#### Evidence

| Signal | Evidence |
|---|---|
| Executive sponsor departure | User-supplied signal: "executive sponsor left" |
| WAU decline | User-supplied signal: "weekly active users down 18%" |
| Support volume increase | User-supplied signal: "support tickets up" |
| Champion still engaged | User-supplied signal: "admin champion still engaged" |
| Workflow adoption | User-supplied signal: "two key workflows adopted" |
| Renewal timing | 75 days from generation date |
| ARR | $120,000 |

**Data Gaps:**
- NPS/CSAT scores: No survey data available
- Billing history: No payment or contract data available
- Support ticket severity and sentiment: Volume is up, but severity and CSAT are unknown
- Meeting attendance and QBR history: Not provided
- Feature adoption breadth: Only "two key workflows" mentioned; total purchased features unknown

#### Recommended Action

**Priority**: High
**Action**: Initiate an executive sponsor re-engagement campaign. The CSM should request an introduction to the new executive sponsor (or the replacement for the departed sponsor) within 5 business days. Prepare a value summary document that includes: (1) ROI realized to date, (2) product roadmap highlights relevant to their business objectives, and (3) a proposed executive business review. Frame the meeting as a strategic partnership check-in, not a renewal pitch.
**Owner**: CSM (primary); CS Leader (escalation if introduction is not granted within 5 days)
**Deadline**: 2025-01-24 (5 business days from generation)
**Expected Outcome**: Meeting scheduled with new executive sponsor; champion is positioned as internal advocate; renewal conversation timeline is established

---

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Synthetic Account | Schedule introduction to new executive sponsor; prepare value summary and executive business review deck | CSM | 2025-01-24 | Without executive alignment, the renewal lacks institutional support and is vulnerable to budget review or competitive evaluation |
| 2 | Synthetic Account | Investigate root cause of 18% WAU decline; identify which user cohorts are declining and why | CSM + Product Analytics | 2025-01-28 | Continued usage decline will erode champion's ability to justify renewal internally |
| 3 | Synthetic Account | Review all open support tickets; assess severity, age, and sentiment; create resolution plan for any tickets over 5 business days | Support Manager | 2025-01-22 | Rising ticket volume with unresolved issues signals product failure to the client |

---

## Early Warning Watchlist

No additional accounts in portfolio. This account is already on the watchlist as At Risk.

---

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Synthetic Account | NPS/CSAT scores | Cannot assess explicit satisfaction; scored at neutral (50) which may understate or overstate risk | Request latest survey results from NPS platform or conduct a pulse survey |
| Synthetic Account | Billing history | Cannot confirm payment reliability or discount dependency; assumed neutral | Pull billing records for last 12 months |
| Synthetic Account | Support ticket details (severity, sentiment, CSAT) | Volume increase is flagged as negative, but severity is unknown; may be over- or under-weighted | Request support ticket export with severity, category, and CSAT fields |
| Synthetic Account | Feature adoption breadth | "Two key workflows" is positive but total purchased features unknown; adoption rate cannot be calculated | Pull feature usage matrix from product analytics |

---

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: Not specified (using default weights from skill definition)
- Data coverage period: Synthetic data provided at point of analysis
- Known limitations: 
  - Only 5 of 7 dimensions have direct signals; NPS and Billing are scored at neutral (50) due to absence of data
  - Confidence capped at Medium due to data gaps (2 dimensions missing)
  - No temporal depth: trailing period for usage and support trends not specified
  - No direct human signals (meeting notes, email sentiment, verbatim survey comments) available
```
