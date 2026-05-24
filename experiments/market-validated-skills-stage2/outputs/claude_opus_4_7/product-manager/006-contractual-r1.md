# Handoff: Trial Setup Abandonment After Contact Import

## 1. Goal and User

- **Goal:** Reduce trial user abandonment that occurs during the contact import step of setup.
- **User:** Trial users completing initial setup, specifically at the CSV contact import stage.

## 2. Known Facts (from discovery)

- 7 of 10 interviewees mentioned CSV formatting confusion. *(supplied fact, qualitative, small sample)*
- Support receives import-related tickets weekly. *(supplied fact, volume not quantified)*
- Trial users abandon setup after the contact import step. *(supplied fact, mechanism not yet isolated)*

## 3. Assumptions and Unknowns

**Assumptions (not yet validated):**
- CSV formatting confusion is a primary driver of abandonment (correlation observed in interviews, causation not confirmed).
- Reducing CSV friction will increase setup completion.
- The 10 interviewees are representative of the trial population.

**Unknowns / open questions:**
- Quantitative abandonment rate at the import step (no funnel data supplied).
- Which specific CSV formatting issues recur (column mapping, encoding, headers, delimiters, required fields)?
- Volume and themes of weekly import support tickets.
- Whether abandoners attempted import and failed, or skipped/stalled before attempting.
- Whether non-CSV import paths exist or are needed.
- Engineering feasibility — no estimate yet.

## 4. Handoff by Function

### → Design
- Review the import step as a candidate for redesign focused on CSV formatting clarity.
- Open design questions: inline format guidance, sample file, column mapping UI, pre-import validation, error recovery flow.
- Not committing to a specific solution — discovery has not isolated which CSV issues dominate.

### → Engineering
- Feasibility assessment requested for: (a) pre-upload validation, (b) flexible column mapping, (c) clearer error messaging on import failure.
- No scope, timeline, or commitment implied — feasibility input is the ask.
- Please flag any current technical constraints on the import pipeline.

### → Data
- Instrumentation request to answer the quantitative gap:
  - Funnel metric: setup step completion rates, with explicit drop-off at contact import.
  - Import attempt outcomes: started, failed (with error type), succeeded, skipped.
  - Time-on-step at import.
  - Cohort: trial users.
- Pull historical support ticket data tagged to import, categorized by issue type, if available.

## 5. Metrics and Validation

**Success metrics (to be baselined before any change):**
- Setup completion rate (trial cohort).
- Contact import step completion rate.
- Import-related support ticket volume per trial user.

**Validation sequence recommended:**
1. Instrument the funnel to confirm import is the dominant drop-off point (assumption check).
2. Categorize support tickets to identify the top CSV failure modes (evidence gap).
3. Run 3–5 targeted usability sessions on the current import flow before design changes.
4. Define a target lift for any proposed redesign tied to baselined metrics.

**Evidence that would change the recommendation:**
- Funnel data showing abandonment concentrates elsewhere (e.g., before import).
- Ticket data showing the dominant issue is not formatting (e.g., data quality, deduping, integrations).

## 6. Risks and Human Gates

**Risks:**
- Acting on 10 interviews without funnel confirmation may target the wrong root cause.
- "Weekly tickets" is unquantified — severity could be over- or understated.
- Designing a fix before categorizing failure modes risks rework.

**Human gates required before:**
- Committing engineering scope or a delivery date.
- Communicating any fix or improvement to customers.
- Reprioritizing roadmap items to make room for this work.

## 7. Next Steps

1. **Data:** stand up the import funnel and pull tagged support ticket categories. *(unblocks evidence gap)*
2. **Design:** review current import flow and prepare discovery questions; hold on solution design until top failure modes are identified.
3. **Engineering:** provide rough feasibility input on validation, column mapping, and error messaging — no commitment requested.
4. **PM:** schedule a review once funnel + ticket categorization are available to decide whether to prioritize, defer, or expand discovery.

---

*Boundary note: This handoff frames the problem and validation plan. It does not commit design direction, engineering scope, a roadmap slot, or any customer-facing message. Those require human confirmation after the evidence gaps above are closed.*
