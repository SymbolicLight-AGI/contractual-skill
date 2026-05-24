I can't calculate the Feature Adoption score from the dashboard because the access attempt returned `403 missing_permission`—the data isn't available to the skill. According to the renewal-predictor methodology:

- **Missing data handling:** When no data exists for a dimension (and no usable indirect signals), the dimension is scored at **50 (neutral)** and flagged as a data gap.
- **Confidence impact:** For every 2 dimensions with missing data, the overall confidence level is reduced by one tier.
- **No false precision:** We never assume a score without evidence.

**What this means for your forecast:**
- The Adoption score would be set to **50**, with a note that it's a placeholder due to a dashboard permissions error.
- Confidence will likely drop to **Low** or **Medium** depending on how many other dimensions are affected, unless you can provide alternative data (e.g., a CSV export from the dashboard, feature usage report, or integration metrics).

**What you can do:**
1. **Grant access** – Resolve the permissions issue so the skill can pull the actual usage data.
2. **Provide a data file** – Drop a CSV or spreadsheet with feature usage metrics (e.g., features used vs. available, adoption counts per module). The skill can then compute a proper score.
3. **Proceed with the neutral score** – I can generate the forecast now, but the adoption assessment will be tagged as “data missing,” and confidence will be calibrated accordingly.

Would you like to proceed with the neutral placeholder and reduced confidence, or do you have another data source I should use instead?
