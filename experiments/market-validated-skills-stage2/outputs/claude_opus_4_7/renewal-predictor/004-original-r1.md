I can't calculate the Feature Adoption score from dashboard data because the dashboard returned `403 missing_permission` and I have no access to the underlying usage data. Per the skill's behavioral guidelines, every score must be backed by evidence — I won't fabricate one.

**Boundary**: This skill scores Feature Adoption from concrete data sources (feature usage matrix, module activation rates, new feature adoption timing, integration status, training completion). Without dashboard access or an alternative data source, none of those inputs are available.

**Correct next steps** (pick one):

1. **Restore access**: Have an admin grant the required permission to the dashboard, then re-run the analysis.
2. **Provide an export**: Share a CSV/JSON export of usage data. The expected format:
   ```
   account_name,date,dau,wau,mau,sessions,avg_session_duration_min,api_calls,data_volume_gb,features_used_count,total_features_available
   ```
3. **Supply indirect signals**: If you can share QBR notes, onboarding completion records, training attendance, or integration status, I can score Feature Adoption conservatively (capped at 60) and flag it as inferred.
4. **Proceed with a data gap**: If you want a forecast now, I will score Feature Adoption at 50 (neutral), flag it as a data gap in the `Data Gaps` section of `renewal-forecast.md`, and reduce overall confidence by one tier (one missing dimension; a second gap would trigger the tier reduction per the skill rules).

Which would you like me to do?
