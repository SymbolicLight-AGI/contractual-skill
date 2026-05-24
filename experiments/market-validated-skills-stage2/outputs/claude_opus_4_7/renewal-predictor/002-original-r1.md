# Renewal Prediction Request — Insufficient Data

I cannot produce a defensible renewal forecast from the information provided. The Health Score model requires evidence across seven dimensions, and the supplied facts ("renewal this year" and "customer uses the product") only touch one dimension (Usage) at the lowest possible resolution — presence, not trend.

## What I Have

| Dimension | Data Provided | Inferable Score |
|---|---|---|
| Engagement Frequency | None | — |
| Support Ticket Volume/Sentiment | None | — |
| Feature Adoption | None | — |
| NPS/CSAT | None | — |
| Billing History | None | — |
| Stakeholder Continuity | None | — |
| Usage Trends | "Uses the product" (binary, no trend) | — |

Per the skill's scoring rules, absence of data is not evidence of a problem, so I will not score dimensions at 0. Per the confidence rules, with data on ≤1 of 7 dimensions, confidence would be **Low** and the forecast would be effectively non-informative.

## Prediction

**Cannot be issued with meaningful confidence.** Producing a Health Score here would constitute false precision, which the skill explicitly prohibits.

## What I Need to Produce a Forecast

Please populate any subset of the following. Even partial data across 4+ dimensions will yield a Medium-confidence forecast.

### Minimum viable inputs (prioritized)

1. **Contract basics** — ARR, renewal date, contract start, tier, seats purchased, auto-renew status
2. **Usage trend** — DAU/WAU/MAU or session counts over the trailing 30/60/90 days (not just "uses it")
3. **Stakeholder map** — Champion name + title + last activity, executive sponsor, any known departures
4. **Support history** — Ticket count last 90 days, any P0/P1 or escalations, recent CSAT
5. **Satisfaction** — Most recent NPS or CSAT score and date
6. **Billing** — Payment timeliness, any disputes, discount history, recent up/downgrades
7. **Engagement** — QBR attendance, response latency to CSM outreach, recent meeting notes

### Templates you can populate

```csv
# account_overview.csv
account_name,arr,renewal_date,contract_start,contract_term_months,tier,seats_purchased,csm_name,champion_name,champion_title

# usage_metrics.csv
account_name,date,dau,wau,mau,sessions,api_calls,features_used_count,total_features_available

# support_tickets.csv
account_name,ticket_id,created_date,resolved_date,severity,sentiment,csat_score,escalated,summary

# nps_csat.csv
account_name,survey_date,survey_type,score,verbatim_comment

# billing.csv
account_name,invoice_date,amount,due_date,paid_date,days_late,dispute_flag,discount_pct

# stakeholders.csv
account_name,contact_name,title,last_activity_date,status,notes
```

## Recommended Next Step

Drop any of the above files into the working directory (or paste the data inline) and re-invoke. I will:

1. Score each dimension with cited evidence
2. Compute a weighted Health Score
3. Issue a prediction with a calibrated confidence level
4. Generate `renewal-forecast.md` with a prioritized action plan

## If You Need an Answer Right Now

The single highest-signal question you can answer without any system data:

> **"In the last 30 days, has the primary champion been responsive, and is usage stable or growing?"**

- **Yes to both** → Provisionally lean *Likely to Renew*, Low confidence, monitor.
- **No to either** → Provisionally lean *At Risk*, Low confidence, trigger a stakeholder check-in within 10 business days.

This is a heuristic, not a forecast. It should not be used for revenue planning or save-play prioritization without the underlying data.
