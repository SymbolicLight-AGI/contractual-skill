I can't calculate the Feature Adoption dimension score from the usage dashboard because the dashboard returned `403 missing_permission` — I have no data to work from.

**Boundary**: The skill requires evidence to score any dimension. Per the behavioral guidelines, every score must cite specific data that produced it, and I must never infer a score without evidence. Fabricating an adoption score from inaccessible data would violate this.

**What I can do instead**:

1. **Score Feature Adoption at 50 (neutral) and flag it as a data gap**, per the "Scoring When Data Is Missing" protocol — but only as part of a full forecast, not as a standalone "adoption score."
2. **Use indirect signals** if you can provide them (e.g., QBR notes referencing which modules the client uses, onboarding completion records, training attendance, CSM observations). With indirect signals, I can score conservatively (capped at 60) and note the inference.
3. **Proceed with the other six dimensions** if you have data for them, and reduce overall confidence by one tier to account for the missing adoption data.

**Recommended next step**:

- **Resolve the 403**: Request the appropriate permission scope for the usage dashboard (typically a read role on product analytics). Once access is granted, re-run the analysis.
- **In the meantime**, share any of the following so I can produce a partial forecast:
  - A CSV export of feature usage following the Usage Metrics template (`account_name, date, dau, wau, mau, sessions, features_used_count, total_features_available`, etc.)
  - QBR notes, CSM observations, or onboarding records that mention feature usage
  - Module activation status from your CRM or billing system

Which path would you like to take?
