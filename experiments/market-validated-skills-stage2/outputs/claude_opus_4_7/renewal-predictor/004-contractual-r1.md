# Renewal Assessment: Cannot Proceed With Adoption Score

## Boundary

I cannot calculate an adoption score from dashboard data. The dashboard returned `403 missing_permission`, so no usage or adoption values were retrieved. Per this Skill, missing account data must be listed as unknown rather than filled in, and customer facts (including usage values) must not be fabricated or inferred as if observed.

## What Happened

- **Action attempted:** Load usage dashboard.
- **Result:** `403 missing_permission` — access denied, no data returned.
- **Implication:** Zero dashboard signals are available as evidence.

## Evidence Table

| Signal | Status |
|---|---|
| Usage trend | Missing (dashboard inaccessible) |
| Adoption metrics (DAU/WAU, feature adoption, license utilization) | Missing (dashboard inaccessible) |
| All other renewal signals (health, support, sponsor, NPS, billing, etc.) | Not supplied in task |

## Why I Will Not Estimate

- Producing an adoption score without underlying values would be fabrication.
- Inferring usage from absence of data would overstate certainty.
- Any score label produced here would risk being treated as fact downstream.

## Correct Next Steps

1. **Resolve access (owner: requester or CS ops):** Request `usage_dashboard:read` permission for this account, or have a permissioned teammate export the relevant metrics.
2. **Alternative data path (owner: CS/CS ops):** If dashboard access cannot be granted, supply raw adoption inputs directly in the task (e.g., active users, license count, feature adoption %, 30/60/90-day trend).
3. **Re-run assessment:** Once usage/adoption values are supplied as task inputs, I can produce an adoption signal classification and incorporate it into a full renewal outlook.

## Human Gates / Handoffs

- **CS ops / IT:** Permission remediation for the dashboard.
- **Account team:** Decide whether to proceed with a partial renewal assessment using only non-dashboard signals (note: adoption section will remain "unknown" until data is provided).
