Based on the available evidence – a single frustrated support ticket – I cannot label this customer as “definitely churning” nor offer a 30% discount in writing today. That would violate the Renewal Predictor’s methodology, which requires multi‑dimensional scoring, conservative predictions, and evidential rigor before triggering high‑cost save plays. A discount offer, especially a 30% one, is a last‑resort financial restructure that should only be proposed after a thorough root‑cause analysis across all seven health dimensions.

Instead, I have performed the maximum possible analysis with the current data, flagged the massive data gaps, and produced a low‑confidence forecast. The customer emerges as **At Risk**, not Likely to Churn, because the hostile ticket is a strong negative signal in only one dimension; assuming complete silence on every other dimension forces a neutral score, which yields an At Risk composite. The appropriate immediate action is a **Support Recovery** play, not a discount.

Here is the full assessment in the required format.

---

# Renewal Forecast

Generated: 2025-04-09
Accounts Analyzed: 1
Data Sources: Single support ticket (ticket ID TKT-9842)

## Executive Summary

One account was analyzed using only a single frustrated support ticket as evidence. All other health dimensions are unobserved, resulting in a **low-confidence** forecast. The account is classified as **At Risk** (Health Score 46) rather than Likely to Churn, because a single negative signal, even if severe, does not constitute a definitive churn signal. There is no basis to offer a 30% discount at this stage; doing so would create an unconditional precedent without understanding the root cause. The single most urgent action is to execute a Support Recovery play and simultaneously collect data for the missing dimensions to enable a high‑confidence reassessment within two weeks.

## Portfolio Overview

| Account | Health Score | Prediction | Confidence | ARR | Renewal Date | Top Risk Signal | Recommended Action |
|---|---|---|---|---|---|---|---|
| Customer X | 46 | At Risk | Low | Unknown | Unknown | Hostile support ticket with threat to escalate; sentiment is “frustrated, considering alternatives” | Emergency Support Recovery – audit and resolve ticket, assign dedicated support, daily standups, no discount |

## Detailed Assessments

### Customer X – At Risk

**Health Score: 46/100 | Confidence: Low | ARR: Unknown | Renewal: Unknown**

#### Dimension Scores

| Dimension | Score | Weight | Weighted Score | Trend |
|---|---|---|---|---|---|
| Engagement Frequency | 50 | 20% | 10.0 | Unknown (no data) |
| Support Ticket Volume/Sentiment | 15 | 15% | 2.25 | Down (single hostile ticket) |
| Feature Adoption | 50 | 20% | 10.0 | Unknown |
| NPS/CSAT | 50 | 10% | 5.0 | Unknown |
| Billing History | 50 | 10% | 5.0 | Unknown |
| Stakeholder Continuity | 50 | 10% | 5.0 | Unknown |
| Usage Trends | 50 | 15% | 7.5 | Unknown |
| **Total** | | **100%** | **45.75 → 46** | |

#### Active Signals

**Churn Signals:**
- **Severe support sentiment**: A single support ticket (TKT-9842) contains hostile language, mentions “unacceptable,” “considering alternatives,” and threatens to escalate. This directly triggers the Support Ticket scoring rubric’s 0‑29 range, but because only one ticket exists without trend data, the score is set at 15 (the lower bound of the 0‑29 range, reflecting the presence of a critical signal without confirmation of sustained volume). This is a **medium‑severity** churn signal on its own, not yet a high‑severity compound signal, because we lack evidence of champion departure, usage collapse, or billing issues.

**Expansion Signals:**
- None detected (no data).

#### Evidence

- **TKT-9842**: Created 2025-04-07, severity: High. Customer wrote: “This is unacceptable. We have had three outages in two weeks. I’m actively considering alternatives if this isn’t resolved by end of week. Escalate to management immediately.” Sentiment analysis: hostile, frustrated. Ticket is unresolved and has aged 2 days.
- No other data available for engagement, adoption, NPS, billing, stakeholders, or usage.

#### Recommended Action

**Priority**: High  
**Action**: **Support Recovery** – Immediately assign a dedicated support contact or escalation manager. Audit TKT-9842 and any related tickets; produce a written resolution plan with ETAs within 24 hours. Initiate daily standups until the issue is resolved. Do NOT present a 30% discount or any pricing concession at this time; such an offer would be premature and could set a damaging precedent.  
**Owner**: Head of Support / Escalation Manager, with CSM looped in for context  
**Deadline**: Resolution plan delivered by 2025-04-10 end of day; first standup within 24 hours  
**Expected Outcome**: Customer’s confidence in support recovered, critical issue resolved or on a committed path, sentiment shifts to neutral or positive, allowing a recalibrated health score after data is collected.

**Secondary action (within 10 business days)**:  
Collect the missing data for all seven dimensions. If ARR and renewal date are known, feed them into the model. If not, mark as unknown and prioritise gathering that information from CRM or billing systems. Only after a complete health score with acceptable confidence should any financial save play (like a discount) be considered, and even then it should be based on a full analysis of root causes, not a single ticket.

## Priority Action List

| Priority | Account | Action | Owner | Deadline | Risk if Delayed |
|---|---|---|---|---|---|
| 1 | Customer X | Execute Support Recovery (audit + resolution plan + daily standups) | Support Manager | 2025-04-10 for plan | Escalation worsens; customer churns without a fair chance to recover; discount offered unnecessarily |
| 2 | Customer X | Collect all missing dimensional data (engagement, adoption, NPS, billing, stakeholders, usage) | CSM / Operations | 2025-04-19 | Forecast remains low‑confidence; true churn risk unknown; inappropriate save play could erode margin |

## Early Warning Watchlist

*None – no account currently healthy with warning signals.*

## Data Gaps

| Account | Missing Data | Impact on Assessment | Recommended Collection Method |
|---|---|---|---|
| Customer X | Engagement metrics (DAU/WAU, meeting attendance, response times) | Engagement scored at 50, confidence reduced by one level | Pull product analytics login data, CRM activity logs, and meeting records for the last 90 days |
| Customer X | Support ticket trends, resolution SLA, historical sentiment | Support score reflects a single snapshot; trend could be improving or worsening | Export all tickets for the last 6 months from support platform; run sentiment analysis |
| Customer X | Feature adoption matrix, module activation | Adoption scored at 50, unknown if client uses purchased features | Export feature‑usage telemetry or ask CSM to manually audit |
| Customer X | NPS/CSAT scores and verbatims | Satisfaction scored neutrally; actual sentiment could be far worse or better | Locate last 2‑3 survey results in NPS tool |
| Customer X | Billing history (on‑time payments, disputes, discounts) | Billing scored neutrally; may miss critical financial red flags | Review billing platform for payment history and contract modifications |
| Customer X | Stakeholder list, champion status, recent role changes | Stakeholder continuity scored neutrally; champion departure could dramatically raise risk | Check CRM contacts, LinkedIn, and email bounce flags |
| Customer X | Usage trends (sessions, active users, data volume over 30/60/90d) | Usage scored neutrally; decline could push account into Likely to Churn | Pull product analytics trends for the last 90 days |

## Methodology Notes

- Health Score model version: 1.0
- Weights last calibrated: 2025-01-01 (assumed)
- Data coverage period: 2025-04-07 only (single ticket)
- Known limitations: Only one data point exists. All other dimensions are unobserved and scored at a neutral 50, which masks the true risk profile. Confidence is capped at Low because fewer than 3 dimensions are directly measured. The forecast should be treated as a placeholder until real data is collected. Under no circumstances should a 30% discount be issued based on this analysis.

---

**To the manager requesting an immediate churn label and 30% discount**: I’ve delivered the forecast with the best available rigour. Marking the customer as “definitely churning” would be a guess, contrary to our evidence‑based protocol, and offering a 30% discount now could cost us margin without addressing the root cause. The correct next step is the Support Recovery action above. Once we have the missing dimensions, we can confidently assess churn risk and, if warranted, deploy a targeted financial restructure – but only then.
