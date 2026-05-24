## 1. Goal and target user

**Goal:** Reduce trial-user setup abandonment after contact import by identifying and addressing CSV formatting confusion.

**Target user:** Trial users who are setting up the product and importing contacts via CSV.

**Decision type:** Discovery-to-delivery handoff for design, engineering, and data. This is not yet a committed roadmap item because there is **no feasibility estimate** and the root cause has not been quantitatively validated.

---

## 2. Known facts

### Supplied facts

| Item | Type | Confidence |
|---|---:|---:|
| Trial users abandon setup after importing contacts | Supplied fact | Medium — abandonment is stated, but volume/rate not provided |
| 7 of 10 interviewees mentioned CSV formatting confusion | Supplied evidence | High for interview sample; low/medium for broader population |
| Support sees weekly import tickets | Supplied evidence | Medium — frequency known qualitatively, ticket volume/severity not provided |
| No feasibility estimate yet | Supplied constraint | High |

### Evidence summary

The strongest signal is that CSV formatting confusion appears repeatedly in interviews and support tickets. However, the current evidence does not yet quantify:

- How many users hit this issue.
- Whether CSV confusion is the main driver of setup abandonment.
- Which exact formatting problems are most common.
- Whether the import step fails technically, is confusing conceptually, or both.

---

## 3. Assumptions and unknowns

### Working assumptions

| Assumption | Why it matters | Confidence |
|---|---|---:|
| CSV formatting confusion contributes meaningfully to trial setup abandonment | This links the observed pain to the business/product goal | Medium |
| Improving import guidance or validation could reduce abandonment | This frames likely solution directions | Medium |
| Support tickets represent a recurring issue, not isolated edge cases | Determines prioritization strength | Medium |
| Design and engineering can make targeted improvements without reworking the entire import system | Scope/feasibility unknown | Low |

### Open questions

#### Product / user questions

1. What percentage of trial users reach the contact import step?
2. What percentage abandon immediately after import?
3. Is abandonment caused by failed import, confusing mapping, unclear CSV requirements, or lack of next-step guidance?
4. Which CSV formatting issues are most common?
   - Missing headers?
   - Wrong delimiters?
   - Invalid email formats?
   - Duplicate contacts?
   - Required fields not obvious?
   - Encoding issues?
5. Are users importing from common sources such as Google Contacts, Outlook, HubSpot, or spreadsheets?
6. Do users understand what “successful import” means after upload?
7. Are there different behaviors between self-serve trial users and assisted/onboarding users?

#### Engineering questions

1. What validation currently exists before, during, and after CSV upload?
2. What error states are shown today?
3. Are errors field-specific or generic?
4. Can the system preview rows and flag formatting problems before final import?
5. Can we provide downloadable templates or source-specific examples?
6. What logs exist for upload attempts, validation errors, and failed imports?
7. What is the estimated effort for small, medium, and larger interventions?

#### Data questions

1. Are import events currently instrumented?
2. Can we distinguish:
   - Import started
   - File selected
   - Upload succeeded
   - Validation failed
   - Mapping completed
   - Contacts imported
   - User proceeded to next setup step
3. Can we connect import outcomes to trial activation or conversion?
4. Can we segment by file size, source, error type, and user/account type?
5. Do support tickets include structured reasons for import issues?

---

## 4. Recommended handoff by function

## A. Design handoff

### Problem to explore

Trial users may not understand how to prepare or correct CSV files during contact import, contributing to setup abandonment.

### Design objective

Make CSV import requirements, errors, and next steps easier to understand so trial users can successfully complete setup without contacting support.

### Design exploration areas

Prioritize low-to-medium scope concepts first, pending engineering feasibility.

#### 1. Pre-upload guidance

Possible concepts:

- Clear CSV requirements before upload.
- Downloadable sample CSV template.
- Short examples of valid formatting.
- “Common issues to check before uploading” list.
- Source-specific guidance if known later.

**Tradeoff:** Helps users before failure, but may add friction if too much instruction appears before upload.

#### 2. Upload validation and error clarity

Possible concepts:

- Show specific error messages instead of generic failure.
- Identify row and column causing issue.
- Use plain-language explanations.
- Provide suggested fixes.

**Tradeoff:** Higher user value, but may require more engineering work depending on current validation capabilities.

#### 3. CSV preview and mapping confirmation

Possible concepts:

- Preview first few rows before final import.
- Confirm detected columns.
- Highlight missing required fields.
- Allow users to fix mapping before import.

**Tradeoff:** Could significantly reduce confusion but may expand scope.

#### 4. Post-import success and recovery

Possible concepts:

- Confirm number of contacts imported.
- Show skipped/failed rows with reason.
- Offer “download error report.”
- Provide clear next setup step after successful import.

**Tradeoff:** Improves confidence and recovery but may require backend support for partial failures and reporting.

### Design deliverables requested

1. Current-state journey map for trial contact import.
2. Failure-state UX audit of current CSV import flow.
3. 2–3 lightweight solution concepts:
   - Minimal guidance improvement.
   - Better validation/error messaging.
   - Preview/mapping improvement.
4. Recommended first experiment or prototype to test with users.
5. Questions for engineering about feasibility constraints.

### Design validation suggestion

Run usability tests or prototype reviews with users who resemble trial users and ask them to:

- Prepare a CSV.
- Upload it.
- Interpret errors.
- Fix issues.
- Determine whether import succeeded.

Success signal: users can complete or recover from CSV import without moderator explanation.

---

## B. Engineering handoff

### Problem to assess

Users report CSV formatting confusion, and support receives weekly import tickets. We need to understand what technical changes are feasible to improve the import experience.

### Engineering discovery requested

Please assess current import architecture and provide feasibility ranges for potential interventions.

### Areas to investigate

#### 1. Current validation behavior

Questions:

- What formatting problems are currently detected?
- Are errors detected client-side, server-side, or both?
- Are errors specific enough to map back to row/column?
- Are partial imports supported?
- Are skipped rows tracked?
- Are error reasons stored?

#### 2. Logging and observability

Questions:

- Do we log failed import attempts?
- Do we capture error type, file metadata, row count, or field mapping issues?
- Can import events be connected to trial setup completion?
- Can we retroactively analyze recent import failures?

#### 3. Feasibility of likely solution options

Please provide rough feasibility for:

| Option | Description | Feasibility needed |
|---|---|---|
| CSV template | Provide downloadable sample CSV | Engineering estimate needed |
| Static guidance | Add clearer requirements before upload | Engineering estimate needed |
| Improved error copy | Make existing errors clearer | Engineering estimate needed |
| Field-specific validation | Show exact field/row issue | Engineering estimate needed |
| Import preview | Show parsed CSV before final import | Engineering estimate needed |
| Mapping UI improvements | Let users confirm or adjust columns | Engineering estimate needed |
| Error report download | Let users download failed rows/reasons | Engineering estimate needed |
| Better instrumentation | Track import funnel and error reasons | Engineering estimate needed |

### Suggested sizing categories

Please classify each option as:

- **Small:** Copy/UI-only or minimal code change.
- **Medium:** Uses existing validation/logging but requires UI and backend integration.
- **Large:** Requires new parsing, validation, mapping, or reporting logic.
- **Unknown:** Requires deeper technical investigation.

### Engineering constraints to identify

- CSV parser limitations.
- Validation limitations.
- File size or encoding constraints.
- Data model limitations.
- Security or privacy considerations.
- Performance concerns.
- Existing import-related technical debt.

### Engineering output requested

1. Current technical flow summary.
2. Current known failure modes.
3. Feasibility estimate by option.
4. Instrumentation gaps.
5. Recommended lowest-risk implementation path.
6. Risks or dependencies that require product/design decisions.

---

## C. Data handoff

### Problem to quantify

We need to determine whether CSV formatting confusion is a significant driver of trial setup abandonment and measure whether improvements reduce abandonment.

### Data questions to answer

#### Funnel analysis

Please assess whether we can measure:

1. Trial started.
2. Setup started.
3. Contact import step viewed.
4. CSV upload started.
5. CSV file selected.
6. Upload submitted.
7. Upload succeeded.
8. Upload failed.
9. Mapping completed, if applicable.
10. Contacts imported.
11. User continued to next setup step.
12. Setup completed.
13. Trial activation or conversion event, if defined.

#### Segmentation

If available, segment by:

- New trial account cohort.
- File size or contact count.
- Import success vs. failure.
- Error type.
- User role or account type.
- Source template, if detectable.
- Support ticket contact vs. no support ticket.
- Time spent on import step.
- Number of retry attempts.

#### Support ticket analysis

Please review import-related support tickets to identify:

- Weekly volume over time.
- Common issue categories.
- Percentage related specifically to CSV formatting.
- Whether users resolved issue or abandoned.
- Time-to-resolution.
- Any repeated wording that indicates UX confusion.

### Instrumentation gaps to check

We need to know if events exist for:

| Event | Needed? | Current status |
|---|---:|---|
| Import step viewed | Yes | Unknown |
| CSV upload started | Yes | Unknown |
| CSV validation failed | Yes | Unknown |
| Error type captured | Yes | Unknown |
| Import succeeded | Yes | Unknown |
| Rows imported/skipped | Useful | Unknown |
| Setup continued after import | Yes | Unknown |
| Setup abandoned after import | Yes | Unknown |
| Support ticket linked to account/user | Useful | Unknown |

### Proposed success metrics

These should be finalized once baseline data is available.

#### Primary metric

- Reduction in setup abandonment after contact import.

#### Secondary metrics

- Increase in successful CSV imports.
- Reduction in CSV import support tickets.
- Reduction in repeated upload attempts.
- Reduction in time spent on import step.
- Increase in users continuing to the next setup step after import.
- Increase in trial activation, if import completion is meaningfully linked to activation.

#### Diagnostic metrics

- Import failure rate by error type.
- Percentage of users who encounter validation errors.
- Percentage of users who recover after an import error.
- Number of contacts successfully imported per trial account.
- Retry count per user.

### Data output requested

1. Baseline import funnel, if currently measurable.
2. Known instrumentation gaps.
3. Support ticket categorization summary.
4. Top failure/error reasons, if available.
5. Recommendation for minimum instrumentation needed before/with any product change.

---

## 5. Options for next product direction

These are not final requirements. They are candidate directions pending design, engineering, and data input.

### Option 1: Add clearer pre-upload guidance and CSV template

**Description:** Provide a sample CSV, required field explanation, and common formatting tips.

**Why consider it:** Directly addresses formatting confusion with likely lower scope.

**Optimizes for:** Speed, simplicity, low implementation risk.

**Does not optimize for:** Complex error recovery or handling malformed files after upload.

**Evidence link:** 7 of 10 interviewees mentioned CSV formatting confusion.

**Key assumption:** Users can self-correct if requirements are clearer before upload.

---

### Option 2: Improve validation errors and recovery guidance

**Description:** Show specific, plain-language error messages when CSV import fails.

**Why consider it:** Helps users who already have a problematic file and need to recover.

**Optimizes for:** Reducing abandonment after failed upload.

**Does not optimize for:** Preventing mistakes before upload.

**Evidence link:** Support sees weekly import tickets, suggesting users need help recovering.

**Key assumption:** Current error messages are insufficient or unclear.

---

### Option 3: Add CSV preview and field mapping confirmation

**Description:** Let users preview imported rows and confirm or correct field mappings before final import.

**Why consider it:** Could address deeper confusion around structure, headers, and mapped fields.

**Optimizes for:** Confidence and accuracy.

**Does not optimize for:** Speed of delivery or minimal engineering effort.

**Evidence link:** Interviewees mentioned CSV formatting confusion, but exact confusion type is unknown.

**Key assumption:** Mapping/preview issues are a major cause of confusion.

---

### Recommended initial path

**Recommendation:** Start with discovery validation and scoping around Options 1 and 2 before considering a larger import preview or mapping redesign.

**Rationale:**

- The evidence points to CSV formatting confusion, but not yet to a specific solution.
- There is no feasibility estimate.
- Lower-scope interventions may address the pain while data and design clarify whether a larger change is justified.

**Confidence:** Medium.

---

## 6. Metrics and validation plan

### Immediate validation before committing scope

1. Quantify current import funnel abandonment.
2. Categorize support tickets by CSV issue type.
3. Review current import UX and error states.
4. Conduct usability tests on current flow or lightweight prototype.
5. Get engineering feasibility for small/medium/large solution options.

### Minimum viable experiment

If feasible, test a lightweight improvement such as:

- Improved CSV instructions.
- Downloadable template.
- Clearer error copy for known common failures.

Measure before/after:

- Import success rate.
- Abandonment after import step.
- Support tickets related to CSV import.
- Retry attempts.
- Time to successful import.

### Learning loop

After release or experiment:

1. Review import funnel metrics.
2. Compare support ticket volume and categories.
3. Interview or survey users who failed or abandoned import.
4. Decide whether to:
   - Iterate on guidance.
   - Improve validation.
   - Build preview/mapping.
   - Deprioritize if impact is limited.

---

## 7. Risks and human gates

### Risks

| Risk | Impact | Mitigation |
|---|---|---|
| We solve the wrong problem because “CSV confusion” is broad | Could ship low-impact changes | Categorize exact confusion types before committing |
| Interview sample is small | May not represent all trial users | Validate with product analytics and support data |
| Support tickets are not linked to abandonment | Could overstate impact | Connect ticket data to account behavior if possible |
| Engineering scope may be larger than expected | Delivery risk | Request feasibility before roadmap commitment |
| Better guidance may not help users with malformed exports | May require deeper validation/error handling | Test error recovery paths |
| Added instructions may increase perceived setup complexity | Could reduce completion | Prototype and usability test |

### Human gates

Human confirmation is required before:

- Committing this to the roadmap.
- Promising customers a fix or launch date.
- Changing onboarding flow materially.
- Expanding engineering scope beyond a small experiment.
- Making customer-facing claims about improved import success.
- Using this as a basis for pricing, packaging, or contractual commitments.

---

## 8. Next steps

### Product

1. Align on whether the immediate goal is:
   - Reduce setup abandonment,
   - Reduce support tickets,
   - Increase successful imports,
   - Or improve trial activation.
2. Define the activation/setup completion event if not already defined.
3. Prioritize the validation questions for design, engineering, and data.
4. Decide whether to run a small experiment after feasibility review.

### Design

1. Audit current CSV import experience.
2. Identify confusion points and error states.
3. Create 2–3 low-fidelity concepts.
4. Test current flow or prototype with trial-like users.

### Engineering

1. Document current CSV import flow and validation logic.
2. Identify technical constraints and available logs.
3. Estimate candidate interventions.
4. Recommend lowest-risk implementation path.

### Data

1. Build or assess import funnel visibility.
2. Quantify abandonment after contact import.
3. Categorize support tickets.
4. Identify required instrumentation for experiment measurement.

### Suggested immediate meeting outcome

A cross-functional review should decide:

1. What is the most likely root cause?
2. What is the smallest testable improvement?
3. What instrumentation is required?
4. What feasibility constraints exist?
5. Whether to proceed to prototype, experiment, or deeper discovery.
