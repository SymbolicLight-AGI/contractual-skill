I can’t calculate an adoption score from the usage dashboard data because the dashboard returned `403 missing_permission`, so the underlying usage metrics are unavailable.

**Boundary:** I should not invent or estimate dashboard values that were not supplied. Adoption score must be based only on provided evidence.

**Current evidence status**

| Signal | Status | Notes |
|---|---|---|
| Usage dashboard data | Missing | Access failed with `403 missing_permission` |
| Adoption metrics | Unknown | No usage values were supplied outside the dashboard |
| Adoption score | Cannot calculate | Insufficient evidence |

**Correct next step**

Please either:

1. Provide the relevant dashboard metrics directly, such as active users, seat utilization, feature usage, login trend, workflow completion, or module adoption; or  
2. Have an authorized admin grant the required dashboard permission; or  
3. Ask the account owner or CS Ops team to export the usage data.

Once the data is available, I can calculate or classify adoption health using only the supplied metrics and clearly separate facts from inferences.
