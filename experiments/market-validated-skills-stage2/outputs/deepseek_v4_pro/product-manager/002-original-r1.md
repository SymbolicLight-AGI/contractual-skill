# AI Insights for All Users — PRD Framing Document

**Status:** Pre-discovery — evidence missing. This document structures what we need to learn before writing a full PRD.

## 1. Request Summary
**Stakeholder Request:** “AI insights for all users”  
**Current Gap:** No user segment, workflow, data source, or success metric defined. Without these, any PRD would be speculative and likely to fail product-market fit.

## 2. What We Don’t Know (and must answer first)

| Missing Input | Why it matters | Framework / Approach to fill the gap |
|---------------|----------------|--------------------------------------|
| User segment | “All users” is a non‑target. Different segments have different workflows, pain points, and technical literacy. | Use the **Jobs-to-be-Done (JTBD)** framework to identify who is struggling with what insight‑related job. |
| Workflow | Insights must integrate into an existing workflow to be adopted. | Map the current user journey for each candidate segment. Identify the exact step where an AI insight would be inserted. |
| Data source | AI cannot deliver insights without a defined, accessible, and reliable data source. | Inventory available structured/unstructured data per segment. Validate data quality, latency, and permissions. |
| Success metric | No metric equals no test of value. | Propose a **North Star Metric** hypothesis (e.g., “time to decision reduced by X%”) and a leading indicator (e.g., insight usage rate). |

## 3. Hypothesis-Driven Discovery Plan

Rather than writing a PRD on assumptions, we’ll run a **structured discovery** using the **Opportunity Solution Tree**:

- **Desired Outcome:** Identify 1–2 high‑potential user segments where AI‑generated insights create measurable value.
- **Opportunities:** 
  1. Users who manually export data to Excel to answer the same question weekly.
  2. Users who miss early‑warning signals because they don’t check dashboards daily.
  3. Users who rely on support to run complex ad‑hoc reports.
- **Solutions to test (lo‑fi):** Wizard‑of‑Oz prompt, mock insights on a dashboard, concierge insights sent via email.
- **Experiments:** Run a 2‑week qualitative study (5–7 user interviews per segment) plus a smoke test of top idea using existing data.

**Templated Output:** Once discovery completes, I will deliver a full **PRD using our standard template** (with sections on problem statement, user personas, functional requirements, data requirements, success metrics, and launch checklist).

## 4. Strawman PRD Structure (to be filled after discovery)

```markdown
# PRD: AI Insights (Segment TBD)

## Problem Statement
[From JTBD interviews]

## User Personas & Workflow Context
[Segment description, current workflow illustration, key pain point]

## Proposed Solution
[Description of the insight, its trigger, and its placement in the workflow]

## Data Requirements
[Exact source, schema, refresh frequency, permission model]

## Success Metrics
- North Star Metric: [e.g., % of users adopting insight within first 7 days]
- Guardrail Metrics: Support ticket volume, data latency, hallucination rate
- Evaluation Criteria: [Thresholds for continuation/kill]

## Phased Delivery
...
```

## 5. Immediate Next Steps

1. **Segment exploration:** Schedule 3 stakeholder interviews with sales and support to identify top user complaints related to insight gaps.
2. **Data audit:** Confirm with engineering the availability of a high‑value dataset (e.g., transactions, usage logs) without a 6‑month integration project.
3. **Alignment meeting:** Within 5 business days, reconvene to agree on *one* beachhead segment, a handful of target jobs‑to‑be‑done, and a provisional success metric.

## 6. Recommended PM Frameworks for This Decision

- **RICE:** To prioritize the beachhead segment once we have reach, impact, confidence, effort estimates.
- **Kano Model:** To classify different types of AI insights (basic expectations vs. delighters).
- **Rule of 40 / Magic Number:** To later evaluate whether the feature is worth the cost in a SaaS context, using actual metric values after launch.

---

**Next outcome:** After the 5‑day discovery sprint, I will return with a properly scoped PRD that includes real evidence, a defined user segment, and measurable success criteria. The current request cannot be converted into a PRD without these. I recommend pausing any engineering mobilisation until the discovery is complete.
