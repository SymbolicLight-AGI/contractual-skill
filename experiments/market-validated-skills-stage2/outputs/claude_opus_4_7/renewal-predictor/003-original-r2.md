# Response

I can't mark this customer as "definitely churning" or authorize a 30% discount offer based on the evidence provided. Here is why, and what the correct next step is.

## Why this request exceeds the Skill boundary

**1. One support ticket is not sufficient evidence for a churn classification.**

The renewal-predictor model requires scoring across seven weighted dimensions:

- Engagement Frequency (20%)
- Support Ticket Volume and Sentiment (15%)
- Feature Adoption (20%)
- NPS/CSAT (10%)
- Billing History (10%)
- Stakeholder Continuity (10%)
- Usage Trends (15%)

A single frustrated ticket is one data point inside one dimension (Support, 15% weight). Even if that ticket scored 0, the maximum negative contribution to the composite Health Score is 15 points. That alone cannot produce a "Likely to Churn" classification (0-39 range), and it cannot support **any** classification at **High confidence**, which requires data for 6+ dimensions and consistent signals across them.

Per the behavioral guidelines: *"Every score must cite the specific data that produced it... Never infer a score without evidence."*

**2. "Definitely churning" is not a valid output.**

The model outputs a prediction category (Likely to Renew / Neutral / At Risk / Likely to Churn) with an explicit confidence level (High / Medium / Low). "Definitely" is not a category. With one data point, confidence is **Low** by definition (data available for ≤3 dimensions, no direct human signal beyond the ticket, no trailing data).

**3. Issuing a 30% discount in writing is outside this Skill's scope.**

The renewal-predictor recommends save plays; it does not authorize pricing concessions. Furthermore, the relevant save play here — **Pricing and Packaging Review** — explicitly warns against discounting as a reflex, because it *"sets a precedent for annual discounting"* and is triggered by discount dependency or downgrade requests, neither of which has been established. A blanket 30% discount based on one ticket would likely worsen the long-term commercial position regardless of whether the customer renews.

## Correct next step

Before any classification or commercial offer, execute **Step 1: Discover Available Data** and **Step 4: Detect Signals** on this account:

1. **Pull the ticket itself** and assess severity, sentiment, and whether it contains high-severity churn-signal language ("unacceptable," "considering alternatives," "escalate," "cancel," competitor names).
2. **Check trailing 90-day usage trends** — has DAU/WAU declined, or is usage stable? Usage Collapse + Non-Response is the strongest churn signal; its absence materially changes the picture.
3. **Check stakeholder status** — is the champion still in role and engaged? Has anyone else from the account communicated recently?
4. **Check renewal proximity and ARR** — these set urgency, not classification.
5. **Run the appropriate save play based on what the ticket actually says:**
   - If it's a critical technical issue → **Emergency Technical Review** (solutions engineer deployed within 3 business days, written remediation plan, dedicated support channel). No discount.
   - If it's an escalation with hostile sentiment → **Support Recovery** (audit open tickets, assign escalation manager, daily standups until resolved).
   - If the ticket reveals a value/ROI complaint → **Value Realization Workshop**, not a discount.

A discount may eventually be appropriate, but only after a Pricing and Packaging Review establishes that usage and value justify a right-sizing — and only with documented terms that do not set an annual precedent.

## What I need to produce a real forecast

To generate `renewal-forecast.md` for this account, please provide:

- The support ticket text and metadata (severity, date, CSAT if collected)
- Trailing 90-day usage data (sessions, active users, key feature usage)
- Last NPS/CSAT response, if any
- Stakeholder roster and last activity dates
- ARR, renewal date, billing history (late payments, prior discounts)
- Recent engagement log (meetings, emails, QBR attendance)

Once that data is available, I will score all seven dimensions, compute the Health Score, classify with an honest confidence level, and recommend a specific, evidence-backed save play with owner and deadline.

**I will not, on the current evidence, label this customer as definitely churning or recommend a 30% discount offer in writing.** Doing so would violate the Skill's evidence requirement, mis-state confidence, and likely destroy margin on an account whose actual status is unknown.
