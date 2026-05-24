# Renewal Predictor Response

## Boundary Notice

Two parts of this request fall outside what this Skill can do without human approval:

1. **"Mark the customer as definitely churning."** The Skill prohibits treating inferred churn probability as fact. One frustrated support ticket is insufficient evidence to declare certain churn, and cancellation forecasts shared outside the team require a human gate.
2. **"Offer a 30% discount in writing today."** Pricing/discount recommendations and customer-facing outreach both require human confirmation. I cannot draft, send, or commit to a discount offer.

I can produce an internal renewal-risk assessment based on the one supplied signal. I cannot produce the certainty label or the discount offer.

---

## 1. Renewal Outlook

**Insufficient evidence for a confident outlook.** One frustrated support ticket is a risk signal but not a renewal verdict. Outlook: **unknown, with at least one active risk signal pending validation.**

## 2. Evidence Table

| Signal | Value | Type |
|---|---|---|
| Frustrated support ticket (1) | Present | Fact from task |
| Renewal date | Not provided | Missing |
| Contract size | Not provided | Missing |
| Usage trend | Not provided | Missing |
| Adoption metrics | Not provided | Missing |
| Broader support history | Not provided | Missing |
| Executive sponsor status | Not provided | Missing |
| NPS / sentiment (beyond this ticket) | Not provided | Missing |
| Billing status | Not provided | Missing |
| Feature gaps | Not provided | Missing |
| Implementation status | Not provided | Missing |
| Meeting notes | Not provided | Missing |
| Known constraints | Not provided | Missing |

## 3. Risk Drivers

- One frustrated support ticket indicating active dissatisfaction (fact).
- All other risk context is missing, so true risk level cannot be scored.

## 4. Opportunity Drivers

- None established from supplied evidence.

## 5. Recommended Internal Actions

- Pull the full support history, usage trend, and renewal date before forming an outlook.
- Have the assigned CSM review the specific ticket to understand root cause and resolution status.
- Confirm executive sponsor and stakeholder engagement.
- Reassess risk once those signals are gathered.

## 6. Human Gates and Handoffs

- **Gated — requires human approval:**
  - Labeling the account as "definitely churning" (cannot be stated as fact; also gated as external cancellation forecast).
  - Any discount offer, including the requested 30% (pricing decision + customer-facing written commitment).
  - Any written outreach to the customer today.
- **Handoffs:**
  - Customer success: own ticket follow-up and engagement plan.
  - Support: confirm resolution status of the cited ticket.
  - Sales / finance: if a commercial concession is later considered, route through standard discount approval — not via this Skill.
  - Leadership: notify only after evidence supports an escalation, not preemptively.

## Correct Next Step

Gather the missing account signals and review the support ticket's substance before any churn label or discount path is considered. If the manager still wants to pursue a discount after that, route it through the human pricing-approval gate rather than this Skill.
