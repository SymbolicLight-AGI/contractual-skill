# Discovery Handoff: Trial Users Abandon Setup After Contact Import

## 1. Summary

Discovery indicates a meaningful onboarding drop-off after trial users attempt to import contacts. The strongest signal is confusion around CSV formatting requirements.

**Known facts:**
- 7 of 10 interviewed trial users mentioned CSV formatting confusion.
- Support receives weekly tickets related to contact import.
- No engineering feasibility estimate has been completed yet.

**Current hypothesis:**
Trial users are abandoning setup because the CSV import experience does not clearly explain formatting requirements, error states, or next steps when imports fail.

---

## 2. Problem Statement

Trial users who are trying to complete onboarding by importing contacts are getting stuck after the CSV import step, likely due to formatting confusion. This creates friction during initial setup and may reduce activation and trial conversion.

---

## 3. User Segment

**Primary users:**
- Trial users setting up the product for the first time.
- Users importing contacts via CSV during onboarding.

**Likely characteristics:**
- Limited familiarity with the product’s expected CSV structure.
- May be migrating from spreadsheets, CRMs, or other contact databases.
- May not understand required fields, accepted formats, or how to fix validation errors.

---

## 4. Evidence From Discovery

| Signal | Evidence | Confidence |
|---|---:|---|
| CSV formatting is confusing | 7 of 10 interviewees mentioned confusion | Medium-high |
| Import issues are recurring | Support sees weekly import tickets | Medium |
| Setup abandonment occurs after importing contacts | Discovery finding | Medium |
| Engineering complexity is unknown | No feasibility estimate yet | Unknown |

---

## 5. User Need / Job-to-be-Done

**When** I am setting up my account during a trial,  
**I want** to quickly import my existing contacts without formatting errors,  
**so that** I can start using the product and evaluate its value without needing support.

---

## 6. Key Questions to Answer

### For Design
1. Where exactly are users getting confused?
   - Before uploading the CSV?
   - During field mapping?
   - After validation errors?
   - After a successful import?
2. Are users given a clear template or sample CSV?
3. Are required fields, accepted formats, and common mistakes visible before upload?
4. Are error messages specific and actionable?
5. Is there a recovery path when an import fails?

### For Engineering
1. What validation logic currently exists for CSV imports?
2. What types of formatting errors are most common?
3. Can we detect and explain row-level and column-level errors?
4. Can we support more flexible parsing or automatic column mapping?
5. What is the feasibility of:
   - Providing a downloadable CSV template?
   - Showing inline validation before final import?
   - Auto-detecting common field names?
   - Improving error messages?
   - Allowing users to fix errors in-product?

### For Data
1. What is the current drop-off rate at the contact import step?
2. How many trial users attempt CSV import?
3. What percentage of import attempts fail?
4. What are the most common error types?
5. How does import failure correlate with:
   - Activation?
   - Trial conversion?
   - Support contact?
   - Time to first value?

---

## 7. Proposed Opportunity Area

### Opportunity
Reduce onboarding abandonment by making CSV contact import easier, clearer, and more recoverable.

### Desired outcome
More trial users successfully complete contact import and continue setup without needing support.

### Potential product outcomes
- Increased import success rate.
- Reduced onboarding drop-off after import.
- Reduced support tickets related to CSV import.
- Improved trial activation.
- Potentially improved trial-to-paid conversion.

---

## 8. Candidate Solutions for Exploration

These are not finalized requirements. They should be evaluated by design and engineering.

### Option A: Downloadable CSV Template
Provide users with a pre-formatted CSV template before import.

**Potential value:**
- Low complexity.
- Reduces ambiguity before upload.
- Helps users understand required fields.

**Open questions:**
- Is the current required format stable?
- Do different user types need different templates?

---

### Option B: Clear Formatting Guidance Before Upload
Add visible guidance explaining required fields, accepted formats, and examples.

**Potential value:**
- Helps users prepare files correctly.
- May reduce preventable errors.

**Examples:**
- “Required columns: First Name, Last Name, Email”
- “Phone numbers should include country code”
- “Dates should use YYYY-MM-DD format”

**Open questions:**
- Which rules are currently most important to surface?
- Can we tailor guidance based on common support issues?

---

### Option C: Improved Error Messages
Replace generic import errors with specific, actionable messages.

**Potential value:**
- Helps users recover from failed imports.
- Reduces support dependency.

**Example:**
Instead of:  
> Import failed.

Use:  
> 14 rows could not be imported because the email field is missing or invalid. Download the error report or fix the highlighted rows.

**Open questions:**
- Does the backend currently return structured validation errors?
- Can we expose row-level errors?

---

### Option D: CSV Field Mapping
Allow users to map their CSV columns to product fields.

**Potential value:**
- Reduces dependency on exact column names.
- Better supports CSVs exported from other tools.

**Open questions:**
- How many fields need to be mapped?
- Can we auto-suggest mappings?
- Is this too complex for initial onboarding?

---

### Option E: In-Product Error Review and Fix
Let users correct CSV issues directly in the product before importing.

**Potential value:**
- High-quality recovery path.
- Could significantly reduce abandonment.

**Risks:**
- Likely higher engineering and design complexity.
- May not be necessary for MVP.

---

## 9. Recommended Next Step

Run a short cross-functional scoping session with design, engineering, data, support, and product.

### Goal
Align on the highest-impact, lowest-complexity improvement to test first.

### Suggested agenda
1. Review discovery findings.
2. Review current CSV import flow.
3. Review support ticket examples.
4. Identify top error types.
5. Assess technical feasibility.
6. Select MVP solution.
7. Define success metrics and instrumentation needs.

---

## 10. Suggested MVP Scope

Pending feasibility, the likely MVP should focus on reducing confusion before and after upload.

### MVP candidate
1. Downloadable CSV template.
2. Clear formatting guidance on the import screen.
3. More actionable error messaging.
4. Basic tracking of import attempt, success, failure, and abandonment.

### Out of scope for MVP, unless engineering says otherwise
- Full in-product spreadsheet editor.
- Advanced auto-cleaning of CSV data.
- Complex multi-step import wizard.
- Bulk data enrichment.
- Automated migration from external CRMs.

---

## 11. Success Metrics

### Primary metric
**CSV import success rate**

Formula:  
`CSV Import Success Rate = Successful CSV Imports / Total CSV Import Attempts`

### Secondary metrics
| Metric | Formula / Definition |
|---|---|
| Import step abandonment rate | Users who start import but do not complete setup / Users who start import |
| Import failure rate | Failed CSV imports / Total CSV import attempts |
| Support ticket rate for import issues | Import-related tickets / Trial users attempting import |
| Trial activation rate | Trial users reaching activation milestone / Total trial users |
| Time to successful import | Median time from import start to successful completion |
| Trial-to-paid conversion | Paid conversions / Trial users |

---

## 12. Data Instrumentation Requests

Data should confirm whether we currently track the following events. If not, these should be added.

### Recommended events
| Event | Description |
|---|---|
| `contact_import_started` | User opens or begins the import flow |
| `csv_file_uploaded` | User uploads a CSV file |
| `csv_validation_failed` | CSV fails validation |
| `csv_validation_succeeded` | CSV passes validation |
| `contact_import_completed` | Contacts are successfully imported |
| `contact_import_abandoned` | User leaves flow before completion |
| `csv_template_downloaded` | User downloads the template |
| `import_error_viewed` | User sees an import error |
| `support_contacted_from_import` | User contacts support from import flow, if applicable |

### Event properties
- User ID
- Account ID
- Trial status
- File size
- Number of rows
- Number of columns
- Error type
- Error count
- Required fields missing
- Invalid email count
- Invalid phone count
- Duplicate row count
- Timestamp
- Import flow version

---

## 13. Design Handoff

### Design objectives
- Make CSV requirements understandable before upload.
- Help users recover from failed imports.
- Reduce cognitive load during onboarding.
- Avoid forcing users to contact support.

### Design should explore
1. Current import screen clarity.
2. Placement and content of CSV requirements.
3. Template download entry point.
4. Error state UX.
5. Empty, loading, success, partial success, and failure states.
6. Whether a lightweight step-by-step import wizard is warranted.

### Needed design artifacts
- Current-state flow review.
- Proposed UX flow.
- Low-fidelity wireframes.
- Error state content recommendations.
- Final UI design for MVP scope.
- Copy recommendations for formatting guidance.

---

## 14. Engineering Handoff

### Engineering objectives
- Assess feasibility of import UX improvements.
- Identify current validation capabilities and limitations.
- Support actionable error messaging where possible.
- Enable necessary analytics events.

### Engineering should investigate
1. Current CSV parsing and validation architecture.
2. Required and optional fields.
3. Current error handling and error codes.
4. Whether validation errors can be returned at row and field level.
5. Whether we can generate or host a CSV template.
6. Feasibility of field mapping or auto-mapping.
7. Required effort for instrumentation.

### Feasibility estimate needed for
| Capability | Feasibility Needed |
|---|---|
| Downloadable CSV template | Unknown |
| Formatting guidance in UI | Unknown |
| Specific validation error messages | Unknown |
| Row-level error reporting | Unknown |
| Partial import support | Unknown |
| CSV column auto-mapping | Unknown |
| Analytics instrumentation | Unknown |

---

## 15. Data Handoff

### Data objectives
- Quantify size and severity of the problem.
- Establish baseline funnel metrics.
- Identify common error types.
- Measure impact after improvements ship.

### Data analysis requested
1. Trial onboarding funnel with specific import step drop-off.
2. CSV import attempt volume by trial cohort.
3. CSV import success and failure rates.
4. Most common validation errors.
5. Relationship between import success and activation.
6. Relationship between import failure and support tickets.
7. Relationship between import success and trial conversion.

### Baseline metrics needed before release
- Current import success rate.
- Current import failure rate.
- Current import abandonment rate.
- Current import-related support ticket rate.
- Current activation rate for users who succeed vs. fail import.
- Current trial conversion rate for users who succeed vs. fail import.

---

## 16. Risks and Assumptions

### Risks
- We may overbuild a complex import solution before validating the simplest fix.
- Interview sample is small: 10 users.
- Support ticket signal is directional but not yet quantified.
- Engineering feasibility is unknown.
- CSV issues may be only one cause of abandonment.

### Assumptions
- CSV formatting confusion is a major driver of import abandonment.
- Clearer guidance and better error recovery will improve import completion.
- Import completion is meaningfully related to activation.
- Trial users have contacts ready to import during onboarding.

---

## 17. Open Questions

1. What is the exact abandonment rate after the import step?
2. What percentage of trial users use CSV import versus other import methods?
3. What specific CSV formatting issues are most common?
4. Are errors mostly caused by missing fields, invalid values, duplicate records, or unsupported headers?
5. Do users understand the value of importing contacts before they reach this step?
6. Does the product support partial imports today?
7. Are import-related support tickets tagged consistently?
8. What is the minimum improvement we can ship quickly?
9. What activation milestone depends on successful contact import?

---

## 18. Proposed Decision Framework

Use **RICE** to prioritize candidate solutions after feasibility and data inputs are available.

| Solution | Reach | Impact | Confidence | Effort | RICE Score |
|---|---:|---:|---:|---:|---:|
| CSV template | TBD | TBD | Medium | TBD | TBD |
| Formatting guidance | TBD | TBD | Medium | TBD | TBD |
| Improved error messages | TBD | TBD | Medium | TBD | TBD |
| Field mapping | TBD | TBD | Low-medium | TBD | TBD |
| In-product error fixing | TBD | TBD | Low | TBD | TBD |

Formula:  
`RICE = Reach × Impact × Confidence / Effort`

Current recommendation: do not finalize prioritization until engineering provides effort estimates and data provides reach.

---

## 19. Immediate Action Items

### Product
- Schedule cross-functional scoping session.
- Share interview notes and support ticket examples.
- Define activation milestone connected to contact import.

### Design
- Review current CSV import UX.
- Draft MVP concepts for template, guidance, and error states.

### Engineering
- Provide feasibility estimate for MVP options.
- Document current validation and error handling.
- Confirm instrumentation effort.

### Data
- Pull onboarding funnel and import success/failure baseline.
- Identify available import error taxonomy.
- Confirm whether import-related support tickets can be joined to trial user behavior.

### Support
- Provide recent examples of CSV import tickets.
- Summarize top user complaints and common resolutions.

---

## 20. Recommended Framing for the Team

This is not yet a fully specified feature request. It is a discovery-backed opportunity to reduce onboarding friction. The next step is to quantify the drop-off, understand technical constraints, and select the smallest solution that helps trial users successfully complete contact import without support.
