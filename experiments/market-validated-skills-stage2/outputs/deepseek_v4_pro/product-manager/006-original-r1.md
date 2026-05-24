# Discovery Handoff: Reduce Trial Abandonment During Contact Import

**Date:** [Insert Date]  
**Status:** Findings ready for cross-functional kick‑off  
**Audience:** Design, Engineering, Data  
**Next step:** Joint meeting to scope solutions and feasibility study

---

## 1. Problem Statement
Trial users who attempt to **import their existing contacts** are abandoning the setup flow at a higher‑than‑expected rate, preventing them from reaching activation. The core issue: **CSV formatting confusion**.

## 2. Evidence

| Source | Finding | Confidence |
|--------|---------|------------|
| 10 user interviews (qualitative) | **7 of 10** explicitly cited CSV formatting as confusing or error‑prone | High |
| Support ticket volume | **Weekly recurring tickets** on import errors (exact volume not quantified yet) | Medium – needs data pull |
| No feasibility estimate yet | Engineering has **not sized** any solution options. | Unknown |

**Jobs‑to‑be‑Done (JTBD) lens:**  
“When I sign up for a trial, I want to bring my existing contacts into the product, so I can test it with real data. But I get stuck because the CSV format doesn’t match what I have, and I can’t proceed.”

## 3. What We Need From Each Team

### 🎨 Design
- Map the **current import flow** and highlight every step where CSV format is mentioned or enforced.
- Explore 2‑3 alternative import experiences:
  - Accept `.xlsx` / Google Sheets links natively.
  - Offer a “paste contacts / simple grid” as a fallback.
  - Build a **template download + error‑handling wizard** with inline validation.
- Provide low‑fidelity wireframes for the top concept(s) by [DATE – TBD].

### 🛠 Engineering
- **Feasibility estimate is now critical.** Scope the technical effort for the design concepts (no commitment yet, just a rough t‑shirt size and risks). Include:
  - File parsing changes (CSV → other formats).
  - Back‑end impact on contact storage, deduplication, error recovery.
  - Any third‑party API considerations (e.g., Google Sheets).
- If immediate quick‑wins are possible (better error messaging, CSV validation before upload), call them out separately.

### 📊 Data
- Pull hard numbers to validate the qualitative signal:
  - **Import funnel conversion rate:** users who enter the import step → successfully complete import → reach next activation event. Compare trial cohorts (last 3‑6 months).
  - **Time to complete import** and drop‑off at each sub‑step.
  - **Support ticket tagging:** tag all import‑related tickets and break down by root cause (CSV, other formats, general confusion). Count weekly occurrence.
  - **Correlation analysis:** Does import failure predict lower trial conversion to paid? (Cohort retention, if available.)
- Help define the **success metric** for any intervention (e.g., increase import completion rate by X%, reduce import‑related tickets by Y%).

## 4. Known Gaps & Risks
- **Feasibility is unknown** – we cannot commit to a timeline until engineering provides a sizing.
- The problem is clear (CSV confusion), but root cause may be multi‑faceted (column mapping, header requirements, encoding, performance on large files). Design exploration will help untangle.
- Implementation may unlock a larger audience of trial users; the impact could be significant, but the exact benefit needs modelling once data provides baseline numbers.

## 5. Immediate Ask
- **Design**: Kick‑off session to walk through current flow and start brainstorming alternatives.
- **Engineering**: TIMEBOXED feasibility spike (e.g., 1‑2 days) for top technical options.
- **Data**: Pull import funnel data within this week so we can prioritize against other work.

---

*Handoff prepared per Discovery Handoff Template v1.0*  
*Questions? Reach out to the PM team.*
