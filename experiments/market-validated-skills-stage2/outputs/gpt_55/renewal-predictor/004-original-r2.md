I can’t calculate an evidence-based adoption score from the usage dashboard because access failed with `403 missing_permission`. I should not invent dashboard metrics or infer feature adoption without data.

Correct next step: grant dashboard access or provide an export containing adoption data, such as:

```csv
account_name,date,features_used_count,total_features_available,purchased_modules,active_modules,new_features_used_last_6_months,integrations_active,training_completed
```

If no dashboard data is available, I can still proceed using the Renewal Predictor missing-data rule:

- If indirect adoption evidence exists, such as QBR notes, training records, integration logs, or CRM notes, I can score adoption conservatively and cap it at 60.
- If no direct or indirect adoption evidence exists, I will score Feature Adoption as 50 neutral, flag it as a data gap, and reduce confidence accordingly.
- I will not score adoption as 0 unless there is affirmative evidence that adoption is absent or failing.
