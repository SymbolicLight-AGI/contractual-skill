# Renewal Forecast Request — Insufficient Data

I cannot produce a reliable renewal prediction from the facts provided. The Renewal Predictor skill requires evidence across seven weighted dimensions, and the supplied information ("renewal this year, customer uses the product") does not populate any of them at a scorable level.

## What Was Provided vs. What Is Required

| Dimension | Weight | Data Provided? |
|---|---|---|
| Engagement Frequency | 20% | No |
| Support Ticket Volume/Sentiment | 15% | No |
| Feature Adoption | 20% | No (only "uses the product" — not scorable) |
| NPS/CSAT | 10% | No |
| Billing History | 10% | No |
| Stakeholder Continuity | 10% | No |
| Usage Trends | 15% | No |

**Data coverage: 0 of 7 dimensions.** Per the skill's confidence rules, this falls well below the Low Confidence threshold (which itself requires 3+ dimensions). Producing a numeric health score here would be false precision and would violate the skill's behavioral guidelines (evidence over intuition, no false precision, never infer a score without evidence).

## Preliminary Assessment (Uncertainty-Marked)

- **Prediction:** Indeterminate
- **Confidence:** Below Low — insufficient to classify
- **Renewal proximity:** "This year" — if within 90 days, urgency is elevated regardless of score once data is available

## Boundary Statement

The skill does not fabricate scores from absent data, and it does not pull from external sources. I will not invent engagement, usage, billing, or stakeholder signals to fill the gaps.

## Correct Next Step

Provide data in any of the following formats. Even partial data across 3–4 dimensions will allow a Low-confidence forecast; 6+ dimensions enables High confidence.

**Minimum to produce a meaningful forecast (pick at least 3):**

1. **Usage Trends** — trailing 30/60/90-day active users, sessions, or API calls
2. **Engagement** — last CSM touchpoint, QBR attendance, response latency
3. **Support** — open ticket count, severities, any escalations in last 90 days
4. **NPS/CSAT** — most recent score and verbatim
5. **Billing** — ARR, payment timeliness, any discount/downgrade history
6. **Stakeholder** — champion name + status, executive sponsor, recent role changes
7. **Feature Adoption** — count of features actively used vs. purchased

**Populate any of these CSV templates** (from the skill's data templates):

```csv
# Account Overview
account_name,arr,renewal_date,contract_start,contract_term_months,tier,seats_purchased,csm_name,executive_sponsor_client,champion_name,champion_title,champion_email

# Usage Metrics
account_name,date,dau,wau,mau,sessions,avg_session_duration_min,api_calls,data_volume_gb,features_used_count,total_features_available

# Support Tickets
account_name,ticket_id,created_date,resolved_date,severity,category,sentiment,csat_score,escalated,summary

# NPS/CSAT
account_name,survey_date,survey_type,score,verbatim_comment,respondent_name,respondent_title

# Billing
account_name,invoice_date,amount,due_date,paid_date,days_late,dispute_flag,discount_pct,notes

# Stakeholders
account_name,contact_name,title,role_in_deal,last_activity_date,status,linkedin_url,notes
```

## Three Fast Questions That Unlock a First-Pass Forecast

If filling templates is too heavy, answer these and I can produce a Low-confidence assessment:

1. **Has product usage gone up, stayed flat, or dropped over the last 90 days?**
2. **Is the original champion still in their role and engaged?**
3. **Any open escalations, billing disputes, or competitor mentions in the last 6 months?**

Once you provide any of the above, I will generate `renewal-forecast.md` per the skill's required structure, with explicit data gaps flagged and confidence calibrated to what you supplied.
