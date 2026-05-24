I wasn’t able to pull the dashboard data because the request returned `403 missing_permission`. Without that data, I can’t compute a real adoption score from the dashboard metrics.

Rather than guessing or fabricating numbers, the model’s missing-data protocol applies: I’ll score Feature Adoption at **50** (neutral) and flag it as a data gap. The overall health score can still be calculated from the other dimensions, but the confidence level will be lowered accordingly.

If you can provide the dashboard data in another form—like a CSV export, a screenshot, or a manual report—I can plug it in and update the score. I can also tell you exactly which metrics I need:

- Feature usage matrix (which features are active, percentage of purchased features in use, adoption of features released in the last two quarters)
- Integration status (API, SSO, webhooks)
- Training and onboarding completion milestones 
- New feature time-to-first-use

Would you like me to proceed with the neutral adoption score and the rest of the available data, or do you have an alternative data source to share?
