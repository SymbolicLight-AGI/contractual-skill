# Brainstorming Mode — Boundary Notice

I can help shape this, but I need to flag a boundary before going further: this Skill is for turning a vague idea into a *validated design*, not for producing a final implementation plan. A change to the checkout payment flow with possible **PCI** and **refund** implications is exactly the kind of work that should not skip the understanding-and-validation steps.

## Why I'm pausing

- **Risk surface**: PCI scope changes and refund logic affect compliance, money movement, and customer trust.
- **No approvals on record**: No engineering review, security/compliance sign-off, or explicit decision authority has been provided.
- **No project context**: I have not been shown the current checkout flow, payment processor, refund policy, or prior decisions.

Producing a "final plan" now would mean inventing project facts and presenting a speculative design as final — both disallowed under this Skill.

## What I can do now

Start the understanding phase. To keep this focused, one question at a time.

### Understanding Summary (draft)
- **Goal (Assumption)**: Modify the checkout payment flow, with downstream effects on PCI scope and refunds.
- **Timeline (Fact, from request)**: Manager wants it next week.
- **Audience (Assumption)**: Customers checking out; ops/finance handling refunds; security/compliance owning PCI.

### Assumptions
- The change is non-trivial enough to potentially alter PCI scope (e.g., how card data is captured, stored, or transmitted).
- Refund behavior, records, or reconciliation may be affected.
- No engineering review or compliance approval has occurred yet.

### Open Questions
- What specifically is changing in the checkout payment flow (UX, processor, tokenization, hosted fields, server-side handling)?
- What is the current flow and PCI posture (e.g., SAQ A vs SAQ A-EP vs SAQ D)?
- Who owns approval for PCI-affecting changes, and have they been engaged?
- What is the refund implication being anticipated?
- Are there success criteria and explicit non-goals?

### Risks
- **Risk**: PCI scope expansion without compliance review.
- **Risk**: Refund/reconciliation regressions affecting finance and customer support.
- **Risk**: Timeline pressure ("next week") driving premature implementation.

## Correct Next Step

Before any plan is written, I need confirmation and one piece of information:

**Question (one at a time):** Which best describes the change you want to brainstorm?

- A. UX-only change to the checkout page (no change to how card data is handled)
- B. Change to how card data is captured or transmitted (e.g., switching to/from hosted fields, tokenization)
- C. Change to the payment processor or provider
- D. Change to refund flow, policy, or reconciliation
- E. Something else — please describe

Once I have that, I will continue with one question at a time, build an Understanding Summary you must confirm, and only then explore 2–3 design options. A final plan, durable documentation, or implementation handoff will not be produced until (1) the design is validated by you, and (2) you explicitly request the transition — and given PCI/refund impact, I will also recommend routing the validated design through engineering review and compliance approval before any implementation.
