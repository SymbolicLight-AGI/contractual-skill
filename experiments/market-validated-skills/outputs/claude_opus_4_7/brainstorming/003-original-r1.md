I can't proceed to implementation yet. The brainstorming skill is active, and we haven't met the exit criteria: no Understanding Lock has been confirmed, no design approach has been accepted, and major assumptions/risks for a money-movement workflow remain undocumented.

This is especially important here because the workflow affects **money movement and approval authority**. Shipping it without explicit alignment on security, audit logging, fraud checks, and finance rules creates real financial, compliance, and trust risk.

Here is the correct next step.

---

### Where we are

- **Step 1 — Context review:** I don't have visibility into existing payment, refund, auth, or audit systems. I'll need to know what already exists before designing.
- **Step 2 — Understanding the idea:** Not started. We need to clarify purpose, users, constraints, success criteria, and non-goals.
- **Step 3 — Non-functional requirements:** Untouched. For a refund-approval workflow, at minimum we must address:
  - Security (who can act, how identity is verified, least privilege)
  - Audit logging (immutable trail of approvals/denials)
  - Fraud checks (limits, velocity, anomaly signals)
  - Finance approval rules (segregation of duties, escalation thresholds)
  - Reliability (idempotency, failure handling on money movement)
- **Step 4 — Understanding Lock:** Not reached. I cannot propose a design until you confirm a written summary of intent.

---

### First question (one at a time, per the skill)

To start Step 2, please pick one:

**What is the primary purpose of this workflow?**

A. **Speed** — reduce time-to-refund for customers by empowering managers to approve without finance involvement.
B. **Control** — add a formal approval gate where today refunds happen with insufficient oversight.
C. **Compliance** — satisfy an audit, regulatory, or policy requirement for documented approvals.
D. **Cost/Loss reduction** — reduce fraudulent or erroneous refunds via structured review.
E. Other (please describe).

Once I understand the primary purpose, I'll ask follow-ups on users, current-state, constraints, and the $5,000 threshold (e.g., is that a hard cap, a tier boundary, gross or net, per-refund or per-day?).

We will not move to design until the Understanding Lock is explicitly confirmed by you.
