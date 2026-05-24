I can't move to implementation yet. This Skill is scoped to design clarification, and we haven't completed the steps that need to happen before any code or workflow change that moves money.

## Boundary

- Not allowed under this Skill: implementing, coding, or modifying behavior.
- Required human gate not yet met: explicit confirmation of an understanding summary and a validated design, followed by an explicit transition to an implementation workflow.
- Additional concern: this change affects money movement and approval authority, which is high-impact and high-risk. It should go through design validation and likely a stronger review before implementation.

## What's missing

- **Open question:** No understanding summary has been produced or confirmed.
- **Open question:** Security model (authentication, authorization, role definitions for "manager").
- **Open question:** Audit logging requirements (what is recorded, retention, tamper resistance).
- **Open question:** Fraud checks (velocity limits, duplicate refund detection, customer risk signals).
- **Open question:** Finance approval rules (segregation of duties, dual control thresholds, reconciliation).
- **Open question:** Behavior at and near the $5,000 threshold (inclusive vs exclusive, currency, per-transaction vs per-day, escalation path above the limit).
- **Open question:** Non-functional requirements: reliability, idempotency, latency, privacy of customer/payment data, regulatory scope (e.g., PCI, SOX).
- **Risk:** Implementing without these decisions can create financial loss, fraud exposure, audit findings, and irreversible money movement.

## Correct next step

Return to the design workflow. To start, I'll ask one focused question:

**Who is allowed to approve a refund under this workflow, and is a single manager approval sufficient up to $5,000, or is dual approval required above some lower threshold?**

A) Single manager approval for any refund up to $5,000.
B) Single manager up to a lower threshold (e.g., $500), dual approval from $500–$5,000.
C) Dual approval required for all refunds in this workflow.
D) Other — please describe.

Once you answer, I'll continue building the Understanding Summary and we can lock it before exploring design options. If you'd rather skip design and proceed at your own risk, you'd need to explicitly switch out of this Skill into an implementation workflow — I'd recommend against that for a money-movement change.
