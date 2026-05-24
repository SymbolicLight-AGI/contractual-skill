# Discovery Handoff: Trial Users Abandon Setup After Importing Contacts

## 1. Summary

Trial users are dropping off during setup immediately after importing contacts. Discovery suggests the leading issue is **CSV formatting confusion**, supported by both user interviews and support ticket patterns.

This handoff is for **Design, Engineering, and Data** to align on the problem, evidence, open questions, and next steps before solutioning or implementation.

---

## 2. Problem Statement

Trial users attempting to import contacts via CSV are experiencing confusion around formatting requirements, which may be causing setup abandonment after the import step.

**User problem:**  
“I want to quickly import my contacts and continue setup, but I’m unsure how my CSV needs to be formatted or why the import is not working.”

**Business problem:**  
Setup abandonment during trial onboarding may reduce activation and trial-to-paid conversion.

---

## 3. Known Evidence

### User Interviews

- **7 of 10 interviewees** mentioned confusion around CSV formatting.
- Users appear unclear on:
  - Required columns
  - Accepted file structure
  - How to fix formatting errors
  - Whether their import succeeded or failed

### Support Signals

- Support receives **weekly import-related tickets**.
- These tickets indicate the issue is recurring, not isolated.

### Product Analytics

- Discovery found abandonment occurs **after importing contacts**.
- Specific funnel metrics are not yet provided.

---

## 4. Current Hypothesis

Trial users abandon setup because the CSV import experience does not clearly explain formatting requirements, validate issues, or guide users through fixing import errors.

### Assumption to Validate

Improving CSV import guidance and error recovery will reduce setup abandonment and increase trial activation.

---

## 5. User Journey Context

### Current Flow

1. Trial user starts setup
2. User reaches contact import step
3. User uploads CSV
4. User encounters formatting confusion or import uncertainty
5. User abandons setup

### Suspected Friction Points

- No clear CSV template or example
- Formatting requirements are hard to find or understand
- Error messages may not be actionable
- Users may not know whether import was successful
- Users may not know how to proceed after a partial or failed import

---

## 6. Jobs-to-be-Done Framing

**When** I am setting up my trial account,  
**I want to** quickly import my existing contacts without needing to understand CSV formatting details,  
**so that** I can complete setup and start using the product.

---

## 7. Handoff by Function

## Design Handoff

### Design Goal

Make the CSV import step feel guided, understandable, and recoverable for first-time trial users.

### Areas to Explore

1. **Pre-upload guidance**
   - Clear explanation of required CSV format
   - Downloadable CSV template
   - Example CSV preview
   - List of required and optional fields

2. **Upload interaction**
   - Drag-and-drop or file picker clarity
   - Accepted file type and size guidance
   - Inline reassurance about what happens next

3. **Validation and error handling**
   - Human-readable error messages
   - Row-level or column-level issue explanations
   - Suggestions for how to fix the file
   - Ability to re-upload corrected CSV

4. **Success state**
   - Clear confirmation that contacts were imported
   - Count of imported contacts
   - Warning if some rows were skipped
   - Clear next step in setup

5. **Empty or failed state**
   - Avoid dead ends
   - Offer template, help docs, or support path
   - Allow users to skip and continue if appropriate

### Design Questions

- Do users need a CSV template before upload?
- Should the system provide automatic column mapping?
- Should formatting issues be displayed before final import?
- Should users be allowed to continue setup without importing contacts?
- What is the minimum guidance needed to reduce confusion without adding friction?

---

## Engineering Handoff

### Engineering Goal

Assess technical feasibility and implementation options for improving the CSV import experience.

### Known Constraint

- **No feasibility estimate exists yet.**

### Areas to Investigate

1. **Current CSV parser behavior**
   - Supported file types
   - Required columns
   - Optional columns
   - Encoding support
   - Header requirements
   - Max file size and row limits

2. **Validation capabilities**
   - Can the system detect missing required columns?
   - Can it detect invalid values?
   - Can it preview import issues before committing?
   - Can it show row-level or field-level errors?

3. **Error messaging**
   - What error codes or messages currently exist?
   - Are errors user-facing or only logged internally?
   - Can errors be mapped to user-friendly explanations?

4. **Import result handling**
   - Does the system support partial imports?
   - Can it report imported, skipped, and failed rows?
   - Can users undo or retry an import?

5. **Template generation**
   - Can the product provide a downloadable CSV template?
   - Should the template be static or dynamically generated from account configuration?

6. **Instrumentation**
   - Can we track each stage of the import process?
   - Are upload failures, validation failures, and abandonment events already tracked?

### Engineering Questions

- What is the current import success/failure rate?
- What validation is already implemented?
- What would be the smallest feasible improvement?
- Is automatic column mapping technically feasible?
- Are there security, privacy, or data quality risks with showing row-level errors?
- What is the estimated effort for:
  - CSV template download
  - Improved error messages
  - Import preview
  - Column mapping
  - Partial import reporting

---

## Data Handoff

### Data Goal

Quantify the import-step drop-off and identify where users fail, abandon, or seek support.

### Metrics to Pull

#### Funnel Metrics

- Trial users who start setup
- Trial users who reach contact import step
- Trial users who upload a CSV
- Trial users with successful import
- Trial users with failed import
- Trial users who continue after import
- Trial users who abandon after import
- Trial users who complete setup
- Trial-to-paid conversion by import outcome

#### Support Metrics

- Weekly CSV/import-related ticket volume
- Ticket categories or tags
- Top import-related issues
- Time to resolution
- Escalation rate
- Impact on trial conversion, if available

#### Behavioral Metrics

- Time spent on import step
- Number of upload attempts per user
- Error frequency by error type
- Retry rate after failure
- Skip rate, if skipping is available
- Completion rate after successful vs. failed import

### Suggested Funnel

```markdown
Trial Started
→ Setup Started
→ Contact Import Step Viewed
→ CSV Upload Started
→ CSV Upload Completed
→ CSV Validation Passed
→ Contacts Imported Successfully
→ Setup Continued
→ Setup Completed
→ Trial Converted
```

### Data Questions

- What percentage of trial users abandon after the import step?
- Is abandonment higher for users who experience import errors?
- Which CSV errors are most common?
- How many users retry after an import failure?
- Do users who successfully import contacts activate at a higher rate?
- Are import-related support tickets correlated with non-conversion?
- Are there differences by segment, company size, or source channel?

---

## 8. Opportunity Sizing

Current sizing is incomplete.

### Known

- 7 of 10 interviewees mentioned CSV formatting confusion.
- Support sees weekly import tickets.
- Trial users abandon setup after importing contacts.

### Unknown

- Exact abandonment rate
- Number of affected trial users
- Revenue impact
- Trial-to-paid conversion impact
- Engineering feasibility
- Cost to solve
- Expected lift from improvements

### Data Needed for Sizing

- Monthly trial volume
- Import step reach rate
- Import failure rate
- Post-import abandonment rate
- Trial-to-paid conversion difference between:
  - Users who successfully import
  - Users who fail import
  - Users who skip import
- Average contract value or expected customer value

---

## 9. Potential Solution Directions

These are not final recommendations. They are candidate directions for design and engineering exploration.

### Low-Complexity Candidates

1. Add downloadable CSV template
2. Add example CSV formatting guidance
3. Improve import instructions before upload
4. Rewrite error messages in plain language
5. Add clearer success confirmation
6. Add support/help link from failed import state

### Medium-Complexity Candidates

1. Pre-import validation
2. Row-level error reporting
3. Partial import summary
4. Retry flow with specific fix guidance
5. Column matching interface

### Higher-Complexity Candidates

1. Automatic column mapping
2. Intelligent error correction
3. Import preview and edit-in-product
4. Alternative contact import methods
5. Guided onboarding assistant for imports

---

## 10. Suggested Prioritization Approach

Use **RICE scoring** once data and feasibility estimates are available.

### RICE Formula

```markdown
RICE Score = Reach × Impact × Confidence ÷ Effort
```

### Inputs Needed

| Input | Status |
|---|---|
| Reach | Unknown |
| Impact | Unknown |
| Confidence | Medium based on interviews and support signals |
| Effort | Unknown; engineering estimate needed |

### Initial Confidence

**Medium.**  
The evidence is directionally strong because 70% of interviewees mentioned CSV confusion and support sees recurring tickets. However, quantitative funnel impact is not yet confirmed.

---

## 11. Risks and Considerations

| Risk | Description | Mitigation |
|---|---|---|
| Solving the wrong friction | Abandonment may occur after import for reasons unrelated to CSV formatting | Validate with funnel and event data |
| Overbuilding | Advanced import tooling may be costly before confirming impact | Start with lightweight improvements |
| Added complexity | More guidance could make the flow feel heavier | Test prototypes with trial users |
| Data quality issues | Better import success may increase bad contact data | Include validation and clear field requirements |
| Privacy/security | Row-level errors may expose sensitive contact data | Review with engineering/security if needed |

---

## 12. Recommended Next Steps

### Design

1. Audit current CSV import UX.
2. Create low-fidelity concepts for:
   - CSV template guidance
   - Error recovery
   - Success confirmation
3. Test concepts with 5–7 trial users or recent evaluators.
4. Partner with PM and engineering on a minimum viable solution.

### Engineering

1. Audit current CSV import implementation.
2. Document current validation, error handling, and instrumentation.
3. Provide feasibility estimates for candidate improvements.
4. Identify quick wins versus larger architectural changes.

### Data

1. Pull import funnel metrics.
2. Segment abandonment by import success, failure, and retry behavior.
3. Analyze support ticket themes.
4. Estimate business impact of reducing import-step abandonment.

### PM

1. Align teams on the core problem and success metric.
2. Confirm whether the first milestone should focus on guidance, validation, or recovery.
3. Define MVP scope after data and feasibility review.
4. Prepare prioritization using RICE once inputs are available.

---

## 13. Proposed Success Metrics

### Primary Metric

**Setup completion rate for trial users who reach the contact import step**

### Secondary Metrics

- CSV import success rate
- Post-import continuation rate
- Import-step abandonment rate
- Retry success rate after failed upload
- Import-related support ticket volume
- Trial activation rate
- Trial-to-paid conversion rate

### Guardrail Metrics

- Time to complete setup
- Support ticket severity
- Import error rate
- Contact data quality issues
- User satisfaction with onboarding

---

## 14. Open Questions

1. What is the exact drop-off rate after contact import?
2. Are users abandoning after failed imports, successful imports, or both?
3. What CSV formatting errors are most common?
4. What does the current error experience look like?
5. Can users skip the import step and continue setup?
6. What is the business impact of this abandonment?
7. What level of import validation exists today?
8. What is the smallest feasible change with likely user impact?
9. Should the solution prioritize preventing errors or helping users recover from them?
10. Are there alternative import methods users expect, such as Google Contacts, CRM sync, or copy-paste?

---

## 15. Decision Needed

Before committing to a solution, the team should decide:

```markdown
Are we solving for:
1. Better CSV formatting guidance before upload,
2. Better error recovery after failed upload,
3. Better confirmation and continuation after successful upload,
or
4. The full import experience end-to-end?
```

Recommended immediate direction:  
Start by validating the quantitative impact and feasibility, while Design explores lightweight improvements around **CSV template guidance, clearer instructions, and actionable error states**.
