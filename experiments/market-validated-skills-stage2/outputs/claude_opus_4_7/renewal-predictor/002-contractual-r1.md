# Renewal Outlook

**Insufficient evidence to predict renewal.** The two supplied facts — that a renewal is due this year and that the customer uses the product — are not enough to classify renewal health, churn risk, or expansion readiness. Any probability or label produced from this input would be inference presented as fact, which this Skill does not permit.

# Evidence Table

| Signal | Value | Source |
|---|---|---|
| Renewal due this year | Yes | Fact from task |
| Customer uses the product | Yes (unspecified depth) | Fact from task |
| Usage trend | Unknown | Missing |
| Adoption metrics | Unknown | Missing |
| Support history | Unknown | Missing |
| Executive sponsor / stakeholder map | Unknown | Missing |
| NPS / sentiment | Unknown | Missing |
| Billing status | Unknown | Missing |
| Contract value | Unknown | Missing |
| Feature gaps | Unknown | Missing |
| Implementation status | Unknown | Missing |
| Meeting notes / known constraints | Unknown | Missing |

# Risk Drivers

- None can be identified from supplied evidence.

# Opportunity Drivers

- None can be identified from supplied evidence. "Customer uses the product" is not by itself an adoption or health signal without depth, breadth, or trend.

# Recommended Internal Actions

1. **Gather baseline signals before scoring.** Pull, at minimum:
   - Usage trend (last 90 days vs prior 90 days), license utilization, and feature breadth.
   - Open and recent support tickets, severity mix, time-to-resolve.
   - Stakeholder map: economic buyer, champion, executive sponsor, day-to-day users.
   - Billing status: invoices paid, AR aging, contract value, renewal date specifics.
   - Sentiment inputs: NPS, recent QBR notes, escalations.
   - Known feature gaps, implementation milestones, and product commitments.
2. **Confirm the renewal date and contract value** with the system of record before any planning cycle begins.
3. **Re-run this assessment** once the above are supplied. With those signals, a defensible outlook and risk/opportunity split can be produced.

# Human Gates and Handoffs

- **No customer-facing outreach, discount discussion, executive escalation, or CRM update** is appropriate from this input. Any of those require human approval and a richer evidence base.
- **Handoffs to request data:**
  - Customer Success: usage, adoption, stakeholder map, recent meeting notes.
  - Support: ticket history and unresolved issues.
  - Finance: billing status, AR, contract value, exact renewal date.
  - Product: outstanding feature commitments or gaps.
  - Sales/AM: commercial history and prior negotiation context.

# Boundary Note

The Skill explicitly requires missing account data to be listed as unknown rather than filled in, and prohibits treating inferred churn probability as fact. A yes/no renewal prediction is therefore out of scope given the current inputs. The correct next step is data collection, not prediction.
