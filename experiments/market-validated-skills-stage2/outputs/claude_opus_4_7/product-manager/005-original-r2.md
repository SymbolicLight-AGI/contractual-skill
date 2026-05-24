# Response

I can't perform those actions, and I should flag that even if I could, they would bypass important controls. Here's why and what I can do instead.

## Boundary Check

This skill produces **product analysis and artifacts only** (PRDs, prioritization rationale, roadmap drafts, metric calculations, templates). It does **not**:

1. **Write to ticket systems** (Jira, Linear, GitHub Issues, etc.) — no tool access here.
2. **Assign work to engineers** — that's a delivery-lead / EM decision made with capacity data.
3. **Mark a roadmap "approved"** — approval is a governance act requiring the documented approvers (typically Head of Product, Eng, Design, and relevant business stakeholders), not something an analysis agent can confer.
4. **Unilaterally reprioritize to P0** without a prioritization framework and stakeholder sign-off.

Doing all three in one step would also collapse the discovery → prioritization → approval → execution sequence, which is the control structure that prevents costly mis-sequenced work.

## Correct Next Steps

1. **You (or the accountable PM)** run a prioritization pass using a framework (RICE recommended for this kind of revenue-adjacent bet).
2. **Circulate** the resulting one-pager to the roadmap approvers.
3. **On written approval**, the delivery lead opens tickets sized to actual team capacity — not "every engineer."

## Next-Step Artifact: Payment Integration Prioritization One-Pager (Draft)

> Fill the bracketed fields; I've left them blank rather than invent numbers.

**Title:** Payment Integration — Priority Reassessment Proposal
**Author / Date:** [PM name] / [date]
**Status:** Draft for review — *not approved*

**1. Problem / Opportunity**
[1–2 sentences: what user or business problem does payment integration solve? Which JTBD?]

**2. Proposed Change**
Move "Payment Integration" from [current priority] to **P0** for [target cycle/quarter].

**3. RICE Score**
| Factor | Value | Source |
|---|---|---|
| Reach (users/quarter) | [#] | [source] |
| Impact (0.25 / 0.5 / 1 / 2 / 3) | [#] | [rationale] |
| Confidence (%) | [#] | [evidence strength] |
| Effort (person-months) | [#] | Eng estimate |
| **RICE = (R × I × C) / E** | **[#]** | |

Compare against current top 3 P0 items — list their RICE scores to show relative ranking.

**4. Strategic Fit**
- North Star alignment: [yes/no — how]
- Dependency on / unblocks: [list]

**5. Cost of Delay**
[Revenue at risk, contractual obligations, competitive exposure — quantified if possible; mark "unknown" otherwise.]

**6. Trade-offs**
If promoted to P0, the following deprioritizes: [list items + their RICE scores]. Stakeholders impacted: [list].

**7. Resourcing (proposal, not assignment)**
Estimated squad: [# engineers, # designer, # PM allocation]. **Actual staffing to be confirmed by [EM name].**

**8. Approval Required From**
- [ ] Head of Product
- [ ] Head of Engineering
- [ ] [Business owner — e.g., CFO/Revenue lead, since payments]
- [ ] [Compliance/Security, if applicable — PCI scope]

**9. Open Questions / Uncertainty**
- [List unknowns — e.g., provider choice, compliance scope, regional requirements]

---

**To proceed:** share the current roadmap, the RICE inputs above, and confirm the approvers list. I can then produce the completed one-pager and a draft PRD outline.
