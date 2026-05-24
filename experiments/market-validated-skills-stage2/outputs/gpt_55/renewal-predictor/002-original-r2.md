I cannot confidently answer “Will this customer renew?” from the supplied facts alone.

With only:

- Renewal is this year
- Customer uses the product

there is not enough evidence to make a reliable renewal prediction. Product usage is a positive signal, but without usage trend, depth of adoption, stakeholder health, support sentiment, billing history, satisfaction, ARR, or renewal timing, the forecast must be treated as low confidence.

## Provisional Forecast

| Field | Assessment |
|---|---|
| Prediction | **At Risk / Insufficient Data** |
| Health Score | **50/100 provisional** |
| Confidence | **Low** |
| Reason | Most renewal-risk dimensions are missing, so they must be scored neutral rather than assumed healthy |
| ARR at Risk | **Unknown** |
| Urgency | **Unknown until renewal date and ARR are provided** |

## Dimension Scores

| Dimension | Score | Rationale |
|---|---:|---|
| Engagement Frequency | 50 | Customer uses the product, but frequency/depth is unknown |
| Support Ticket Volume/Sentiment | 50 | No support history provided |
| Feature Adoption | 50 | No feature usage or module adoption data provided |
| NPS/CSAT | 50 | No satisfaction data provided |
| Billing History | 50 | No payment or invoice data provided |
| Stakeholder Continuity | 50 | No champion, sponsor, or stakeholder map provided |
| Usage Trends | 50 | No trailing 30/60/90-day trend provided |

Composite Health Score:

```text
50/100
```

By the model threshold, 50 falls into **At Risk**, but this is driven by missing data rather than confirmed churn signals. Absence of data is not evidence of churn, so the correct interpretation is:

> **Renewal likelihood is unknown. Treat as low-confidence At Risk until key renewal signals are collected.**

## Immediate Recommended Action

**Priority:** Medium, elevated to High if renewal is within 90 days  
**Owner:** CSM  
**Action:** Schedule a renewal health check with the customer and collect the minimum data needed to validate renewal likelihood.  
**Deadline:** Within 5 business days, or immediately if renewal is within 90 days.  
**Expected Outcome:** Confirm business value, stakeholder ownership, satisfaction, renewal intent, and any blockers.

## Minimum Data Needed

To produce a useful renewal forecast, collect:

```csv
account_name,arr,renewal_date,product_usage_last_30_days,product_usage_last_90_days,features_used,total_features_available,open_support_tickets,critical_support_tickets,nps_or_csat_score,invoice_status,champion_name,executive_sponsor,renewal_intent_notes
```

## Key Questions to Ask Now

1. Is usage increasing, stable, or declining over the last 90 days?
2. Who is the current champion, and are they still engaged?
3. Has the customer expressed renewal intent, budget concerns, or dissatisfaction?
4. Are there unresolved support issues?
5. Are invoices current?
6. How much ARR is up for renewal?
7. When exactly is the renewal date?

Until those answers are available, the responsible response is:

> **We do not have enough evidence to predict renewal confidently. The customer should be monitored as low-confidence At Risk, with immediate data collection and a renewal health check as the next step.**
