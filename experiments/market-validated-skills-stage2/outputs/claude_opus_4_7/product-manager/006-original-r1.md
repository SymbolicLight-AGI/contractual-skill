# Discovery Handoff: Trial Setup Abandonment at Contact Import

**Owner:** Product Management
**Audience:** Design, Engineering, Data
**Status:** Discovery complete → Solution exploration
**Date:** [Insert]

---

## 1. Problem Statement

Trial users abandon setup after attempting to import contacts. The friction point appears concentrated at the CSV import step.

## 2. Evidence (What We Know)

| Source | Finding | Strength |
|---|---|---|
| User interviews | 7 of 10 interviewees explicitly mentioned CSV formatting confusion | Qualitative, small-N but consistent signal |
| Support tickets | Weekly recurring volume of contact-import tickets | Operational signal, recurring |
| Funnel | Abandonment concentrated post-import-attempt | Behavioral (needs quantification — see gaps) |

## 3. Opportunity Framing (Jobs-to-be-Done lens)

- **Job:** "When I start a trial, I want to load my existing contacts quickly so I can evaluate the product with real data."
- **Current outcome:** Users hit CSV formatting friction, lose momentum, and abandon before reaching value.
- **Hypothesis:** Reducing CSV import friction will increase trial activation. (Unvalidated — magnitude unknown.)

## 4. Known Gaps & Uncertainty

Marking these explicitly so downstream teams scope appropriately:

- **No feasibility estimate yet** — engineering input required.
- **No quantified abandonment rate** — % of trials that drop at this step is not stated in inputs.
- **Root cause within "CSV formatting" not decomposed** — column names? delimiters? encoding? required fields? Unknown from given data.
- **No segmentation** — unclear if confusion concentrates in a specific persona, source CRM, or contact-list size.
- **N=10 interviews** is directional, not statistically representative.

## 5. Asks by Function

### Design
- Map the current import flow end-to-end; identify decision/error points.
- Explore solution directions (non-exhaustive, for divergence):
  - Guided import wizard with column mapping
  - Template/sample CSV download
  - Inline validation with row-level error messaging
  - Native integrations as an alternative entry path
- Produce 2–3 low-fidelity concepts for review before committing to fidelity.

### Engineering
- Provide **feasibility + rough sizing (T-shirt)** for:
  1. Column auto-mapping
  2. Pre-upload validation
  3. Error reporting UX hooks
- Surface technical constraints (file size, parsing library, encoding support).
- Flag any platform/architectural risks early.

### Data
- Quantify the funnel:
  - Trial → import attempted → import succeeded → activated
  - Abandonment rate at each step, last 90 days
- Decompose CSV failure modes from logs (parse errors, missing required fields, encoding, duplicates).
- Segment by signup source, plan, and list size if available.
- Propose a **North Star / activation metric** candidate tied to successful import (e.g., % of trials reaching N imported contacts within 24h).

## 6. Success Criteria (Draft — to refine with team)

- **Primary:** Increase % of trials completing contact import.
- **Secondary:** Reduce import-related support tickets per 100 trials.
- **Guardrail:** No regression in data quality (duplicates, malformed records).

Targets to be set after Data delivers baseline.

## 7. Out of Scope (for this round)

- Full CRM integration build-out (may surface as follow-on).
- Pricing/packaging changes.
- Post-import onboarding redesign beyond the import step.

## 8. Proposed Next Steps & Sequence

1. **Data (week 1):** baseline funnel + failure-mode breakdown.
2. **Engineering (week 1):** feasibility on top 3 solution directions.
3. **Design (week 1–2):** concept exploration informed by 1 & 2.
4. **PM (end of week 2):** prioritize using RICE once Reach (from Data) and Effort (from Eng) are known.
5. **Joint review:** align on scoped V1 and success metrics.

## 9. Open Questions for the Team

- Is there existing telemetry on CSV parse failures, or do we need to instrument?
- Are there contractual/enterprise constraints on supported CSV schemas?
- Should native integrations be considered in-scope as an alternative path, or treated as a separate initiative?

---

**Uncertainty flags:** Abandonment magnitude, root-cause decomposition, feasibility, and segmentation are all unconfirmed. This handoff is intended to *initiate* solution exploration, not to specify a solution. A PRD will follow once Data and Engineering inputs land.
