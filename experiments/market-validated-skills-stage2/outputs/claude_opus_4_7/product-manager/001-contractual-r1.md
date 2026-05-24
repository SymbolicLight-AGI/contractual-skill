# Product Prioritization Recommendation: Onboarding & Roadmap Candidates

## 1. Goal and User

- **Goal (inferred):** Reduce SMB admin onboarding friction while balancing competing roadmap requests.
- **Primary user:** SMB admins responsible for initial setup.
- **Secondary stakeholders:** Sales (Candidate B sponsor), existing users (Candidate C audience).

*Confidence: medium — goal inferred from "SMB admins complain about onboarding time." Not explicitly stated as the strategic priority.*

## 2. Known Facts (from prompt)

- SMB admins have complained about onboarding time. (Source: prompt; volume, severity, and segment size not specified.)
- Candidate A: guided import wizard. Expected effect: reduce setup confusion.
- Candidate B: AI report writer. Origin: sales request.
- Candidate C: new dashboard theme. Engineering effort: low.

## 3. Assumptions and Unknowns

**Assumptions made for ranking (each must be validated):**
- A1. Onboarding friction is a top-tier pain that affects activation or conversion.
- A2. "Setup confusion" is a meaningful component of onboarding time (vs. data quality, permissions, integrations, or training).
- A3. Sales is requesting Candidate B because of a deal or retention pattern, not a single account.
- A4. Candidate C addresses a real user complaint, not an internal aesthetic preference.

**Open questions (unknown from prompt):**
- How many admins complained, in what segments, and at what funnel stage?
- What is current activation / time-to-value? Is it trending?
- Is Candidate B tied to revenue at risk, expansion, or a competitive gap?
- Engineering effort for A and B?
- Are there compliance or data-handling implications for an AI report writer?
- What does leadership consider the current strategic theme (growth, retention, expansion)?

## 4. Prioritization — Options

I am presenting a ranked recommendation **and** the reasoning, so a product owner can override if their context differs.

### Prioritization matrix (qualitative, based only on supplied info)

| Candidate | Linked user pain | Evidence strength | Effort (stated) | Strategic fit (assumed: onboarding) | Risk |
|---|---|---|---|---|---|
| A. Import wizard | Direct (onboarding) | Customer complaints (volume unknown) | Unknown | High | Low–medium |
| B. AI report writer | Indirect (sales channel) | Internal request; no customer evidence cited | Unknown, likely high | Low–medium | Medium–high (scope, AI accuracy, compliance) |
| C. Dashboard theme | Unclear | None cited | Low | Low | Low |

### Recommended ranking (with stated assumptions)

1. **Candidate A — Import wizard.** Most direct line to the only customer pain stated in the prompt. Recommend as the lead bet **pending** scoping and validation that confusion (not other factors) is the dominant onboarding cost.
2. **Candidate C — Dashboard theme.** Low effort. Reasonable as a parallel filler **only if** there is a stated user signal behind it. If it is purely aesthetic-internal, defer.
3. **Candidate B — AI report writer.** Highest uncertainty: no customer evidence in the prompt, likely largest scope, and added AI-specific risks (accuracy, hallucination, data exposure). Recommend a discovery spike before committing.

*Confidence in ranking: medium-low — driven almost entirely by which candidate maps to the one stated user complaint. Would change quickly with revenue, segment, or effort data.*

## 5. Metrics and Validation

**Candidate A — Import wizard**
- Activation metric: % of new SMB admins completing initial data import within X days (X to be set with data team).
- Time-to-first-value: median hours from signup to first successful import.
- Support load: onboarding-tagged tickets per new account.
- Validation step before build: 5–8 SMB admin interviews + funnel drop-off analysis to confirm import is the dominant friction point.

**Candidate B — AI report writer**
- Discovery metric: number of distinct customers (not internal asks) citing report creation as a blocker; dollar value of deals where it was mentioned.
- If built: report adoption rate, edits-per-report (quality proxy), retention delta in adopting accounts.
- Validation step before build: structured sales call review + 5 customer interviews; assess data/AI compliance constraints.

**Candidate C — Dashboard theme**
- Engagement: dashboard session length, return rate (if a complaint exists behind it).
- Validation step before build: confirm a user-sourced request log; otherwise classify as polish, not roadmap.

## 6. Risks and Human Gates

**Risks**
- Picking A without sizing onboarding pain may mean optimizing a real but narrow problem.
- Deferring B without sales transparency may damage cross-functional trust; ranking is not a rejection.
- Building C "because it's cheap" sets a precedent of effort-driven rather than outcome-driven prioritization.
- Candidate B carries AI-specific risks (accuracy, data handling, regulated content) not assessable from the prompt.

**Human gates required before commitment**
- Engineering: feasibility and effort estimates for A and B (Skill cannot claim feasibility).
- Sales leadership: confirm the customer evidence and revenue context behind B.
- Data/compliance review: any AI report writer scope.
- Product leadership: confirm onboarding is the current strategic theme.
- No roadmap change, customer-facing commitment, or timeline should be made on this document alone.

## 7. Next Steps

1. Run a one-week discovery on Candidate A: pull onboarding funnel data, interview 5–8 recent SMB admins, confirm import as the dominant friction.
2. Ask sales for specific accounts, deal values, and customer quotes behind Candidate B; convert into a discovery brief.
3. Classify Candidate C: is there a user signal, or is it internal polish? If polish, move to a "low-effort opportunistic" backlog, not the prioritization debate.
4. Bring effort estimates from engineering for A and B.
5. Reconvene with this artifact updated; only then commit to sequencing.

---

**Evidence summary:** The only customer-sourced signal in the prompt is the SMB admin onboarding complaint. All other prioritization weight rests on assumptions labeled above. The recommendation would shift materially if (a) Candidate B is tied to named revenue, (b) onboarding complaints are low-volume, or (c) engineering effort for A is disproportionate.
