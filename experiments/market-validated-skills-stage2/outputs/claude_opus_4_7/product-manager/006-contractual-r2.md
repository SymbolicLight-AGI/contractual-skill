# Handoff: Trial Setup Abandonment After Contact Import

## 1. Goal and User

- **Goal:** Reduce trial user abandonment that occurs at the contact import step during setup.
- **User:** Trial users completing initial setup, specifically those importing contacts via CSV.

## 2. Known Facts (from discovery)

- 7 of 10 interviewees mentioned CSV formatting confusion. *(Supplied — small qualitative sample)*
- Support receives weekly import-related tickets. *(Supplied — volume and severity not quantified)*
- No engineering feasibility estimate has been produced yet. *(Supplied)*

## 3. Assumptions and Unknowns

**Assumptions (to be confirmed):**
- CSV formatting confusion is a primary driver of abandonment, not just a coincident frustration.
- Trial users who fail import are less likely to convert. *(Plausible but not in evidence supplied.)*

**Open questions / missing evidence:**
- Quantitative abandonment rate at the import step (funnel data).
- Which specific CSV issues occur most (column mapping, encoding, delimiters, header names, data types)?
- Volume and categorization of weekly support tickets on import.
- Source systems users export from (e.g., Gmail, Outlook, HubSpot, Excel).
- Whether users retry, contact support, or churn silently after a failed import.
- Trial users' technical proficiency and team role.

## 4. Handoff by Function

### To Design
- **Problem framing:** Users hit friction at CSV import; framing/affordances around formatting are unclear.
- **Requested exploration (not yet committed scope):**
  - Inline format guidance, example CSV template, and pre-import preview.
  - Column-mapping UI with clear error states.
  - Error messaging that explains what to fix, not just what failed.
- **Inputs design needs:** Examples of failing CSVs from support; representative source-system exports.
- **Not yet decided:** Whether to redesign the import flow, add a wizard, or offer an alternative (e.g., direct integrations). Design should propose options; selection is gated on data + feasibility.

### To Engineering
- **Ask:** Feasibility and rough effort for the following directional options — no commitment requested yet:
  1. More tolerant CSV parser (auto-detect delimiters, encodings, headers).
  2. Column-mapping step with validation preview.
  3. Direct integrations with top source systems (which systems TBD by data).
- **Inputs engineering needs:** Current parser behavior, failure logs, and any existing instrumentation on the import endpoint.
- **Not a commitment:** No scope, timeline, or release decision is being made here.

### To Data
- **Requested instrumentation / analysis:**
  - Funnel: trial start → import attempted → import succeeded → setup completed.
  - Abandonment rate at the import step (overall and by cohort).
  - Failure reasons captured server-side (error type, file characteristics).
  - Correlation between import success and trial-to-paid conversion.
- **Goal of analysis:** Replace assumption ("import confusion drives abandonment") with measured impact, and identify top failure modes to target.

## 5. Metrics and Validation

**Primary outcome metric (proposed):**
- Setup completion rate for trial users who reach the import step.

**Supporting metrics:**
- Import success rate on first attempt.
- Import-related support ticket volume per 100 trials.
- Trial-to-paid conversion rate, segmented by import outcome.

**Validation sequence (recommended):**
1. Data instruments funnel and failure-mode breakdown.
2. Design tests 1–2 lightweight prototypes against top failure modes (e.g., template + mapping preview).
3. Engineering provides feasibility on the targeted fix.
4. Decide on scope based on combined evidence.

## 6. Risks and Human Gates

**Risks:**
- Acting on a 10-interview sample without funnel data may misallocate engineering effort.
- "CSV confusion" may be a symptom; the root cause could be source-system mismatch, expectations of automatic sync, or onboarding sequencing.
- Building integrations is high-effort; needs prioritization evidence before commitment.

**Human gates (require product owner / leadership confirmation before):**
- Committing engineering scope or a delivery date.
- Promising customers an improved import experience or new integrations.
- Communicating timeline externally (sales, marketing, support macros).

## 7. Next Steps

1. **Data:** Stand up the import funnel and failure-mode report. *(Blocks confident prioritization.)*
2. **Design:** Begin low-fidelity exploration of import guidance and mapping flows, pending failure-mode data.
3. **Engineering:** Provide rough feasibility ranges for the three directional options listed above.
4. **Product:** Reconvene after data + feasibility inputs land to decide scope, then bring to a prioritization gate.

---

**Boundary note:** This is a handoff artifact, not a commitment. No roadmap change, ticket creation, or cross-team commitment has been made. Confirmation from the product owner is needed before any of the above is communicated as planned work.
