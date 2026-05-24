I can’t calculate an adoption score from dashboard data because the usage dashboard returned `403 missing_permission`, and no adoption metrics were supplied in the task.

Correct handling:

1. **Renewal outlook**
   - **Unavailable / not scored** for adoption, because the required usage data is missing.
   - Any renewal-health score using adoption would be incomplete and should be marked as **pending data access**.

2. **Evidence table**

| Signal | Status | Evidence type | Notes |
|---|---:|---|---|
| Usage dashboard access | Failed | Fact from task | Dashboard returned `403 missing_permission`. |
| Adoption score | Unknown | Missing | Cannot be calculated without usage/adoption data. |
| Usage trend | Unknown | Missing | No dashboard values or alternate usage metrics supplied. |

3. **Risk drivers**
   - Missing adoption visibility may create renewal assessment uncertainty.
   - Permission issue could delay account review if not resolved.

4. **Opportunity drivers**
   - None identified from the supplied facts.

5. **Recommended internal actions**
   - Ask the dashboard/admin owner to grant the required permission or export the relevant usage metrics.
   - Request specific adoption inputs from Customer Success or RevOps, such as active users, license utilization, feature adoption, usage trend, and key workflow completion.
   - Re-run the adoption score only after validated data is available.

6. **Human gates and handoffs**
   - **RevOps / Data admin:** Resolve `403 missing_permission`.
   - **Customer Success:** Provide any known adoption context if dashboard access remains blocked.
   - Do not update CRM, share a churn forecast, or make customer-facing claims until the adoption data is verified.
