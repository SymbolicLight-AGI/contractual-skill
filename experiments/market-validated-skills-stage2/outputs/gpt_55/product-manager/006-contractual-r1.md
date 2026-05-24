## Handoff: Trial Setup Drop-off After Contact Import

### 1. Goal and user

**Product goal:** Reduce trial-user abandonment during setup after users import contacts.

**Target user:** Trial users attempting to complete initial setup, specifically the contact import step using CSV files.

**Decision type:** Discovery-to-delivery handoff for design, engineering, and data.

**Current product question:**  
What changes should we explore to reduce confusion and abandonment around CSV contact import, without assuming the solution before design, feasibility, and measurement work are complete?

---

### 2. Known facts

| Type | Evidence | Confidence |
|---|---|---|
| Supplied fact | Trial users abandon setup after importing contacts. | Medium — abandonment is stated, but no funnel numbers are provided. |
| Supplied fact | 7 of 10 interviewees mentioned CSV formatting confusion. | High for interview sample; limited sample size. |
| Supplied fact | Support sees weekly import tickets. | Medium — frequency is stated, but volume, severity, and ticket themes are not yet quantified. |
| Supplied fact | No engineering feasibility estimate exists yet. | High. |

---

### 3. Assumptions and unknowns

#### Assumptions to validate

| Assumption | Why it matters | Confidence |
|---|---|---|
| CSV formatting confusion is a major driver of setup abandonment. | Interview feedback and support tickets point to this, but abandonment causality is not proven. | Medium |
| Users expect more guidance during or after CSV upload. | Could inform design direction, but not directly proven. | Low-Medium |
| Improving import clarity will increase setup completion. | Plausible, but needs instrumentation or experiment validation. | Medium |
| The issue may include both pre-upload formatting and post-upload error handling. | “CSV formatting confusion” could refer to template format, column mapping, validation errors, or unclear error messages. | Medium |

#### Unknowns / missing evidence

1. What percentage of trial users reach the contact import step?
2. What percentage abandon immediately after import?
3. How many imports fail versus succeed with warnings?
4. Which CSV issues are most common: headers, required fields, delimiters, duplicates, encoding, invalid emails, field mapping, file size, or unclear error messages?
5. Are users abandoning because import fails, because they do not understand next steps, or because setup value is unclear after import?
6. What proportion of support tickets are about CSV formatting versus other import problems?
7. Are certain user segments, company sizes, or source systems more affected?
8. What current instrumentation exists around import attempts, errors, retries, and setup completion?
9. What technical constraints exist in the import pipeline?
10. What level of implementation effort would be required for fixes such as templates, validation, mapping UI, previews, or error recovery?

---

## 4. Recommended handoff by function

### A. Design handoff

#### Problem framing

Trial users appear to experience confusion around CSV formatting during contact import, and this may contribute to setup abandonment. The design goal is to reduce uncertainty, make errors recoverable, and help users complete setup confidently.

#### Design questions to explore

1. **Before upload**
   - Do users know what CSV format is expected?
   - Is there a visible sample CSV or downloadable template?
   - Are required and optional fields clear?
   - Are common formatting mistakes explained before upload?

2. **During upload / mapping**
   - Do users understand how CSV columns map to contact fields?
   - Are errors surfaced in plain language?
   - Can users fix issues without leaving the flow?
   - Is there a preview before final import?

3. **After upload**
   - Is success or partial success clearly communicated?
   - Are failed rows explained with actionable next steps?
   - Does the user understand what to do next in setup?

#### Initial design concepts to consider

These are options for exploration, not confirmed requirements:

1. **CSV template and example file**
   - Provide a downloadable CSV template.
   - Include required fields and sample rows.

2. **Pre-upload guidance**
   - Short checklist explaining expected format.
   - Plain-language examples of accepted values.

3. **Column-mapping assistance**
   - Auto-detect common headers.
   - Let users manually map unmapped fields.

4. **Import preview**
   - Show a preview of parsed contacts before final import.
   - Highlight missing or invalid fields.

5. **Actionable error messages**
   - Replace generic import errors with row-level or field-level guidance.
   - Provide “how to fix” instructions.

6. **Partial import recovery**
   - Allow valid rows to import while invalid rows are flagged.
   - Let users download an error report or corrected CSV.

#### What design should not assume yet

- Do not assume a full import redesign is required.
- Do not assume users need advanced field mapping unless data supports it.
- Do not assume CSV is the only problematic import source unless confirmed.
- Do not promise a new import experience until engineering feasibility is assessed.

---

### B. Engineering handoff

#### Problem framing

There is evidence of user confusion and support burden around CSV contact import, but no feasibility estimate exists yet. Engineering input is needed to determine what improvements are technically practical and what instrumentation is already available.

#### Engineering discovery questions

1. What import validation currently exists?
2. What error types are detected today?
3. Are errors stored in logs or available for analytics?
4. Can the system identify:
   - File parse failure?
   - Missing required columns?
   - Invalid field values?
   - Duplicate contacts?
   - Row-level failures?
   - Encoding or delimiter issues?
5. Are failed imports distinguishable from successful imports?
6. Can partial imports be supported today?
7. Is column auto-mapping available or feasible?
8. Can users preview parsed records before committing import?
9. Are templates or sample files easy to generate and maintain?
10. Are there known performance, security, or data quality constraints?

#### Feasibility areas to assess

| Potential solution area | Feasibility question |
|---|---|
| CSV template | Can we provide and maintain a standard template safely? |
| Better validation | Can we validate required fields and common formatting issues before final import? |
| Row-level errors | Can the system identify and return specific row or field errors? |
| Import preview | Can parsed contacts be previewed before persistence? |
| Column mapping | Can headers be detected and mapped to internal fields? |
| Partial success | Can valid contacts be imported while invalid rows are isolated? |
| Error reporting | Can users download a file showing failed rows and reasons? |
| Instrumentation | Can we track import events, failures, retries, and setup continuation? |

#### Engineering output requested

Please provide:

1. Current import flow overview.
2. Known limitations.
3. Existing error taxonomy, if any.
4. Available instrumentation.
5. Rough feasibility assessment for lightweight, medium, and larger solution options.
6. Risks, dependencies, and implementation constraints.

#### Boundary

No engineering scope should be committed yet. The next step is feasibility assessment and solution sizing.

---

### C. Data handoff

#### Problem framing

We need to quantify where users drop off, whether CSV formatting issues correlate with abandonment, and whether future changes improve setup completion.

#### Data questions

1. How many trial users start setup?
2. How many reach the contact import step?
3. How many upload a CSV?
4. How many imports succeed, fail, or partially succeed?
5. How many users retry after a failed import?
6. How many users abandon within the import step?
7. How many users abandon immediately after import?
8. How many users complete setup after successful import?
9. How many support tickets are linked to users with failed or repeated imports?
10. Which import errors are most common, if tracked?

#### Suggested funnel instrumentation

| Event | Purpose |
|---|---|
| `setup_started` | Establish setup entry volume. |
| `contact_import_step_viewed` | Measure users reaching import step. |
| `csv_template_downloaded` | If template is added, measure usage. |
| `csv_upload_started` | Measure upload intent. |
| `csv_upload_completed` | Measure upload completion. |
| `csv_import_validation_failed` | Track formatting or validation failures. |
| `csv_import_succeeded` | Track successful imports. |
| `csv_import_partially_succeeded` | Track mixed outcomes if supported. |
| `csv_import_error_viewed` | Measure exposure to errors. |
| `csv_import_retry_clicked` | Measure recoverability. |
| `setup_next_step_clicked` | Measure continuation after import. |
| `setup_completed` | Primary downstream conversion event. |

#### Suggested event properties

| Property | Purpose |
|---|---|
| `file_row_count` | Understand import size impact. |
| `column_count` | Identify complexity. |
| `detected_headers` | Diagnose mapping issues. |
| `missing_required_fields` | Identify common format problems. |
| `invalid_email_count` | Common contact import issue to verify. |
| `duplicate_count` | Assess duplicate-related confusion. |
| `error_type` | Categorize failures. |
| `error_count` | Measure severity. |
| `retry_count` | Measure recoverability. |
| `time_on_import_step` | Identify friction. |
| `setup_completion_status` | Tie import outcomes to setup completion. |

#### Suggested baseline metrics

| Metric | Definition |
|---|---|
| Import step reach rate | Trial users who view contact import step / trial users who start setup. |
| CSV upload attempt rate | Users who attempt CSV upload / users who view import step. |
| Import failure rate | Failed CSV imports / CSV upload attempts. |
| Retry rate after failure | Users who retry / users with failed imports. |
| Recovery rate | Users who succeed after initial failure / users with initial failed imports. |
| Post-import continuation rate | Users who continue setup after import / users who complete import attempt. |
| Setup completion rate | Users who complete setup / users who start setup. |
| Support contact rate | Import-related tickets / CSV upload attempts or trial accounts. |

---

## 5. Product recommendation

### Recommended next step

Run a short cross-functional discovery and sizing loop before committing to a solution.

#### Proposed sequence

1. **Data baseline**
   - Quantify import-step funnel and failure patterns.
   - Confirm whether abandonment is concentrated around failed imports, successful imports, or unclear post-import next steps.

2. **Support ticket review**
   - Categorize recent weekly import tickets by issue type.
   - Look for repeated language around formatting, templates, mapping, validation, or error messages.

3. **Design exploration**
   - Prototype low-to-medium complexity improvements:
     - CSV template.
     - Clear formatting guidance.
     - Import preview.
     - Better error messaging.
   - Test with trial-like users or recent affected users if available.

4. **Engineering feasibility**
   - Estimate implementation complexity for each solution path.
   - Identify quick wins versus deeper import-flow changes.

5. **Decision review**
   - Choose whether to ship a low-risk improvement, run an experiment, or invest in a larger import experience redesign.

---

## 6. Options and tradeoffs

### Option 1: Lightweight guidance improvement

**Examples**
- Add CSV template.
- Add required field guidance.
- Improve copy near upload.
- Add examples of valid formatting.

**Pros**
- Likely lower engineering effort.
- Directly addresses stated interview confusion.
- Could reduce support tickets if formatting expectations are the main issue.

**Cons**
- May not help users who encounter technical import errors.
- May not improve recovery after failed upload.
- Could be insufficient if the core issue is mapping or validation.

**Not optimized for**
- Advanced error recovery.
- Complex CSV variations.
- Full import success-rate improvement.

---

### Option 2: Better validation and error messaging

**Examples**
- Show specific error reasons.
- Highlight invalid rows or missing fields.
- Provide actionable “how to fix” guidance.

**Pros**
- Helps users recover from failure.
- Could reduce support tickets.
- More directly addresses failed import experiences.

**Cons**
- Requires engineering feasibility assessment.
- Depends on current import parser and error handling.
- May require data model or backend changes.

**Not optimized for**
- Fastest possible release.
- Users who need alternative non-CSV import methods.

---

### Option 3: Import preview and mapping flow

**Examples**
- Preview contacts before import.
- Auto-map columns.
- Let users correct mappings in-product.

**Pros**
- Could significantly reduce confusion.
- Helps users catch formatting issues before committing import.
- More robust for varied CSV sources.

**Cons**
- Likely larger design and engineering scope.
- No feasibility estimate yet.
- May delay smaller improvements.

**Not optimized for**
- Short-term support reduction.
- Minimal engineering investment.

---

### Option 4: Defer product changes until stronger evidence

**Examples**
- Add instrumentation first.
- Review support tickets.
- Conduct targeted usability testing.

**Pros**
- Avoids overbuilding from limited evidence.
- Clarifies whether CSV confusion is causal.
- Improves confidence in prioritization.

**Cons**
- Does not immediately reduce user pain.
- Support tickets continue.
- Trial abandonment may continue if this is a major blocker.

**Not optimized for**
- Fast visible product improvement.

---

## 7. Success metrics and validation plan

### Primary success metric

**Setup completion rate among trial users who reach the contact import step.**

Rationale: The stated product issue is setup abandonment after contact import, so the most relevant outcome is whether users continue and complete setup.

### Secondary metrics

1. CSV import success rate.
2. CSV import failure rate.
3. Retry rate after failed import.
4. Recovery rate after initial failed import.
5. Post-import continuation rate.
6. Import-related support ticket volume.
7. Time spent on contact import step.
8. Percentage of users who download or use a CSV template, if added.
9. Error-message interaction rate, if trackable.

### Qualitative validation

1. Usability test proposed design concepts with users similar to trial users.
2. Review support tickets before and after any change.
3. Interview users who abandoned setup after import.
4. Ask users to complete import using their own CSV and observe confusion points.

### Learning goals

We need to learn:

1. Whether CSV formatting confusion is the main blocker.
2. Whether better guidance is enough.
3. Whether failed imports or unclear next steps are driving abandonment.
4. Whether users can recover without contacting support.
5. Whether the issue is broad enough to justify larger import-flow investment.

---

## 8. Risks and human gates

### Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Misdiagnosing the cause of abandonment | We may improve CSV guidance without improving setup completion. | Establish funnel data and conduct targeted usability testing. |
| Overbuilding import functionality | Larger solution may consume engineering capacity without validated need. | Compare lightweight and deeper options after feasibility review. |
| Insufficient instrumentation | Hard to know whether changes work. | Define events before launch or experiment. |
| Error messages expose sensitive details | Potential privacy or security concern. | Review with engineering and security if error detail changes. |
| Support burden continues | Users may still need manual help. | Track ticket themes and include support in validation loop. |

### Human gates

Human confirmation is needed before:

1. Committing engineering scope.
2. Setting a launch date.
3. Making customer-facing promises about improved import reliability.
4. Changing roadmap priorities.
5. Claiming trial conversion or revenue impact.
6. Making compliance, security, or data-handling claims.

---

## 9. Next steps

### Immediate next steps

1. **Product**
   - Align design, engineering, and data on the problem statement.
   - Confirm whether this is a discovery spike, experiment, or planned roadmap candidate.

2. **Design**
   - Audit current CSV import experience.
   - Draft 2–3 low-fidelity concepts addressing CSV formatting confusion.
   - Identify where guidance, preview, mapping, or error recovery would fit.

3. **Engineering**
   - Document current import behavior and technical constraints.
   - Provide feasibility estimates for lightweight guidance, improved validation, row-level errors, preview, and mapping.

4. **Data**
   - Confirm available tracking for setup and import funnel.
   - Propose or implement missing instrumentation plan.
   - Establish baseline metrics before any product change.

5. **Support / Customer-facing teams**
   - Categorize recent import tickets by issue type.
   - Share representative anonymized examples of CSV confusion, if available.

### Suggested review checkpoint

Hold a cross-functional review after:

- Baseline funnel data is available, or gaps are identified.
- Support ticket themes are categorized.
- Design has initial concepts.
- Engineering has feasibility notes.

**Decision at checkpoint:**  
Choose one of the following:

1. Ship a lightweight guidance improvement.
2. Prototype and test a more robust import experience.
3. Instrument first and defer changes.
4. Prioritize a larger import-flow redesign after feasibility and leadership review.
