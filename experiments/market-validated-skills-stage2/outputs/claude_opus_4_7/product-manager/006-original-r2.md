# Discovery Handoff: Trial Setup Abandonment After Contact Import

**Owner:** Product Manager
**Audience:** Design, Engineering, Data
**Status:** Discovery complete → Definition phase
**Confidence:** Medium (qualitative signal strong; quantitative baseline incomplete)

---

## 1. Problem Statement

Trial users abandon setup at the **contact import** step. Qualitative evidence points to **CSV formatting confusion** as the dominant friction.

**Jobs-to-be-Done framing:**
> When I'm setting up a trial, I want to load my existing contacts quickly, so I can evaluate the product with real data — without becoming a data-cleaning expert.

---

## 2. Evidence Summary

| Source | Signal | Strength |
|---|---|---|
| User interviews (n=10) | 7/10 explicitly mentioned CSV formatting confusion | Strong qualitative |
| Support tickets | Weekly recurring import-related tickets | Strong operational |
| Product analytics | Abandonment occurs after import step | Directional |

**Gaps (flagged):**
- No conversion/funnel baseline shared in this handoff (abandonment rate %, time-to-abandon, retry counts).
- No segmentation by CSV source (Gmail, Outlook, HubSpot, custom, etc.).
- No feasibility estimate yet — engineering input required.
- Interview sample (n=10) is small; treat as directional, not statistically representative.

---

## 3. Hypothesized Opportunity (Opportunity Solution Tree, partial)

**Outcome:** Increase trial→activation rate by reducing setup abandonment.

**Opportunity:** "I can't get my contacts in without errors."

**Candidate solutions (not yet prioritized — pending design/eng input):**
1. Auto-detect common CSV schemas (Gmail, Outlook, LinkedIn, HubSpot export formats)
2. Inline column-mapping UI with previews and validation
3. Pre-import template download + sample file
4. Error reporting that points to specific rows/columns with fixes
5. Skip-import path ("Add contacts later") to unblock activation
6. Native integrations (out of scope for v1, parking lot)

---

## 4. Asks by Function

### Design
- Map the current import flow end-to-end; identify decision points where users hesitate or fail.
- Sketch 2–3 concepts for the column-mapping and error-feedback experience.
- Validate concepts with 3–5 trial users (lightweight usability tests) before engineering lock-in.
- **Deliverable:** Flow diagram + low-fi concepts. **Target:** 1 week.

### Engineering
- Provide a **feasibility estimate** (T-shirt: S/M/L) for:
  - Schema auto-detection for top 3 CSV sources
  - Inline column-mapping with validation
  - Row-level error reporting
- Surface technical constraints (parser limits, file size, encoding, async vs. sync processing).
- **Deliverable:** Feasibility note + risks. **Target:** 3–5 days.

### Data
- Establish the **baseline funnel:** trial-start → import-attempt → import-success → activation.
- Report: abandonment rate at import step, retry counts, time-on-step, error-type distribution (if logged).
- Segment by CSV file characteristics if available (size, source app, column count).
- **Deliverable:** Funnel dashboard + top error patterns. **Target:** 1 week.

---

## 5. Success Metrics (proposed — confirm after baseline)

- **North Star contribution:** Trial activation rate
- **Primary:** % of trials completing contact import successfully (target TBD after baseline)
- **Secondary:** Median time to complete import; import-related support tickets/week
- **Guardrails:** No regression in import data quality; no increase in post-import data-cleanup actions

---

## 6. Open Questions

1. What % of trials actually reach the import step vs. abandon earlier?
2. Are the 7/10 interviewees representative of the broader trial population, or a specific segment?
3. Is "skip and add later" acceptable to GTM, or does import gate meaningful activation?
4. Are there compliance/PII constraints on storing failed-import files for debugging?

---

## 7. Next Step

**Trio sync (PM + Design + Eng lead + Data) within 5 business days** to:
- Align on problem framing
- Review baseline data once available
- Confirm feasibility and pick 1–2 solutions to prototype

---

## Uncertainty Notes
- Quantitative funnel data and engineering feasibility are **not yet available**; this handoff initiates that work rather than concluding it.
- Solution candidates above are hypotheses, **not commitments**. Final scope depends on design validation, feasibility, and baseline data.
