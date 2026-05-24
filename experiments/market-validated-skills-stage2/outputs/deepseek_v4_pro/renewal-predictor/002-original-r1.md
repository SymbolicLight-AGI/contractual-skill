I've created the file `renewal-forecast.md` in the working directory with the limited information you provided. Because the data is extremely sparse (only two qualitative facts: the renewal is happening this year and the client uses the product), the analysis is a low‑confidence placeholder.

**Key take‑aways from the forecast:**

- Health Score: **50/100** (all dimensions defaulted to neutral 50, as there’s no data to score them)
- Prediction: **At Risk** (score 50 falls into the 40–59 At Risk bracket)
- Confidence: **Low** – only 0 of 7 dimensions have actual data; indirect “uses product” signal is too vague for reliable scoring
- Recommended immediate action: **Data Collection Sprint** – fill the templates below to get a proper forecast

You can find the full forecast in `renewal-forecast.md`. Below are the templates you’ll need to provide the missing information.

---

### Data Collection Templates (CSV)

**1. Account Overview** – needed for financial details, renewal date, and stakeholder names  
```csv
account_name,arr,renewal_date,contract_start,contract_term_months,tier,seats_purchased,csm_name,executive_sponsor_client,champion_name,champion_title,champion_email
```

**2. Usage Metrics** – to score Engagement, Feature Adoption, and Usage Trends  
```csv
account_name,date,dau,wau,mau,sessions,avg_session_duration_min,api_calls,data_volume_gb,features_used_count,total_features_available
```

**3. Support Ticket History** – to score Support Volume & Sentiment  
```csv
account_name,ticket_id,created_date,resolved_date,severity,category,sentiment,csat_score,escalated,summary
```

**4. NPS/CSAT Surveys** – to score satisfaction  
```csv
account_name,survey_date,survey_type,score,verbatim_comment,respondent_name,respondent_title
```

**5. Billing History** – to score Billing  
```csv
account_name,invoice_date,amount,due_date,paid_date,days_late,dispute_flag,discount_pct,notes
```

**6. Stakeholder Contacts & Activity** – to score Stakeholder Continuity  
```csv
account_name,contact_name,title,role_in_deal,last_activity_date,status,linkedin_url,notes
```

**7. Engagement Log** – meetings, calls, email threads  
```csv
account_name,date,activity_type,initiated_by,attendees,summary,next_steps
```

Once you populate these files and place them in the working directory, I can rerun the analysis to produce a high‑confidence renewal forecast with actionable interventions.
