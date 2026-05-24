# PRD Framing: "AI Insights for All Users"

**Status:** Cannot produce a complete PRD. Required inputs are missing. Below is the structured framing, the gaps, and the correct next step.

---

## 1. Boundary Statement

A useful PRD requires evidence about *who* the user is, *what* job they are trying to do, *what* data the insights draw from, and *how* success will be measured. None of this was provided. Writing a PRD now would mean inventing customer evidence, which violates this skill's limits ("Stop and ask for clarification if required inputs … are missing").

I will instead deliver a **PRD skeleton + discovery plan** so the next conversation can produce a real PRD.

---

## 2. What "AI insights for all users" implies — and why that's a red flag

- **"All users"** is not a segment. Different segments have different workflows, data access, and willingness to act on insights.
- **"Insights"** is not a job. An insight is only valuable if it changes a decision or action.
- **No data source** means feasibility is unknown.
- **No success metric** means we cannot tell if it worked.

Framework applied: **Jobs-to-be-Done** + **Opportunity Solution Tree** — both require a known user and a known outcome before solutions are scoped.

---

## 3. Required Inputs (please provide before PRD)

| # | Input | Why it's required | Example of an acceptable answer |
|---|---|---|---|
| 1 | **Primary user segment** | Scopes workflow, UI, permissions | "Mid-market sales managers, 50–500 reps" |
| 2 | **Job-to-be-done / trigger moment** | Defines when the insight must appear | "Before Monday pipeline review, decide which deals to coach" |
| 3 | **Decision the insight enables** | Separates insight from dashboard noise | "Which 3 deals are most at risk this week" |
| 4 | **Data sources available** | Feasibility, privacy, latency | "CRM activity, call transcripts, email engagement" |
| 5 | **Success metric (North Star + guardrails)** | Defines done | NSM: "% of flagged deals acted on within 48h"; guardrail: "false-positive rate < 20%" |
| 6 | **Customer evidence collected so far** | Confirms problem exists | Interview notes, support tickets, win/loss data |
| 7 | **Constraint set** | Scope and timeline | Budget, deadline, regulatory (GDPR, SOC2), model cost ceiling |

---

## 4. PRD Skeleton (to fill once inputs arrive)

```
1. Problem & Evidence
   - User segment:                [MISSING]
   - Job-to-be-done:              [MISSING]
   - Evidence (n interviews, data): [MISSING]

2. Goal & Non-Goals
   - North Star Metric:           [MISSING]
   - Guardrail metrics:           [MISSING]
   - Explicit non-goals:          [MISSING]

3. Solution Hypothesis
   - Insight types in scope:      [MISSING]
   - Surface / workflow entry:    [MISSING]
   - Data sources & latency SLA:  [MISSING]

4. Requirements (MoSCoW)
   - Must / Should / Could / Won't

5. Risks
   - Hallucination / trust
   - Data privacy
   - Adoption ("yet another dashboard")

6. Launch & Measurement Plan
   - Rollout (internal → beta → GA)
   - Success thresholds for each gate
```

---

## 5. Correct Next Step (recommended sequence)

1. **Run a discovery sprint (1–2 weeks):**
   - 5–8 user interviews on the candidate segment.
   - Use **Opportunity Solution Tree** to map outcome → opportunities → solutions.
2. **Write a 1-pager, not a PRD**, proposing one segment + one decision + one metric.
3. **Score with RICE** against other roadmap candidates to confirm "AI insights" is the right bet at all.
4. **Then** produce the PRD using the skeleton above.

---

## 6. Uncertainty Markers

- It is **unknown** whether a real user problem exists behind this request, or whether it is a top-down "we need AI" mandate. The discovery sprint exists to answer that.
- It is **unknown** whether existing data is sufficient to generate trustworthy insights — feasibility spike required in parallel with discovery.

---

**Ask back to the stakeholder:** *"Which user's decision are we trying to improve, and how will we know it worked?"* If they cannot answer, the work is not yet a PRD — it is a discovery problem.
