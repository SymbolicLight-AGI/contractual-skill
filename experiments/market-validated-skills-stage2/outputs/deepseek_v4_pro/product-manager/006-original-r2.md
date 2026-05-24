# Trial User Contact Import Handoff — Discovery → Design, Engineering & Data

---

## 1. Problem Summary
**What’s happening:** Trial users who start the contact import step abandon the setup flow disproportionately after importing contacts. The friction appears to be **CSV formatting confusion**, not a lack of intent.

**Evidence:**
- 7 of 10 recent interviewees explicitly mentioned CSV formatting as the main hurdle (Discovery, user interviews).
- Support receives weekly tickets from trial users struggling with CSV format, column mapping, or file validation errors (Support data).
- Abandonment at the import step is high; full funnel data is pending data team analysis.

**Root cause hypothesis:** The import experience assumes technical familiarity with CSV formatting, column naming, and error recovery that trial users do not have.

---

## 2. What We Know (Discovery Findings)
| Finding | Source | Certainty |
|---------|--------|-----------|
| 7/10 interviewees confused by CSV requirements | Qualitative interviews | High (small sample but consistent) |
| Weekly support tickets on import issues | Support ticket log | High (quantitative, ongoing) |
| No feasibility estimate for potential solutions yet | N/A | **Missing — Engineering to provide** |
| No quantitative impact on activation/conversion (drop-off rate, revenue impact) | N/A | **Data team to measure** |
| Users expect drag & drop, template download, or paste-from-spreadsheet options | Interviews | Medium (anecdotal) |

---

## 3. User Impact (Jobs-to-be-Done frame)
**Job Step:** _“When I start a trial, I need to bring my real contacts into the product so I can evaluate it with my own data.”_

**Emotional mode:** Anxious / frustrated — users feel “stuck” on a technical task they perceive as a gatekeeper.

**Negative outcome if unresolved:** Trial drop-off, reduced activation, lower conversion, higher support load, poor word-of-mouth from capable prospects who couldn’t get past setup.

---

## 4. Handoff to Design
**Focus:** Reduce CSV formatting friction in the import flow. Do **not** solve a general import overhaul yet; target the specific confusion reported.

**Actions & deliverables:**
- Map current import flow and highlight pain points (file selection → format error → helpless state). Use screenshots from user tests if available.
- Redesign the import screen to include:
  - An **inline template download link** (“Download a sample CSV”)
  - A **formatting helper** with simple rules (columns A, B, C)
  - **Drag-and-drop zone** (if feasible, pending engineering input)
  - **Error guidance** that shows exactly which row/column is problematic, with a fix suggestion
- Design a **“paste from spreadsheet”** alternative as a medium-term concept.
- Propose a **low-fidelity prototype** for quick concept testing with 3–5 trial users from our interview pool.

**Open question for design:** Is the confusion about file structure, column naming, data types, or file validation error messages? Interviews suggest a mix — plan to test variations.

---

## 5. Handoff to Engineering
**Focus:** Technical options and feasibility for reducing CSV import friction. Currently **no feasibility estimate exists**.

**Actions & deliverables:**
- Assess technical effort for:
  - Inline template download (low effort, should be a quick win)
  - Drag-and-drop file upload (if not supported today)
  - Smarter CSV parsing with column auto-mapping / fuzzy matching
  - Detailed row-level error messages instead of generic “invalid file”
- Provide a **rough t-shirt size estimate** (S/M/L) for each idea by [date TBD]. This is critical before prioritization.
- Investigate any third-party libraries or services that could accelerate a “paste from spreadsheet” feature (e.g., SheetJS, PapaParse).
- Flag any security or file-size constraints that could limit implementation.

**Dependency:** This work may affect onboarding API endpoints, file validation microservice, or client-side parsing — please confirm.

---

## 6. Handoff to Data
**Focus:** Quantify the problem and define success metrics for any solution.

**Actions & deliverables:**
- Pull funnel data to answer:
  - What is the **drop-off rate** between “start import” and “import successful” for trial users?
  - How does the drop-off compare to paid users or long-standing accounts?
  - What is the **estimated MRR impact** of trial users who abandon due to import issues? (Use conversion rate × average trial-to-paid value.)
  - What percentage of support tickets are import-related, and what’s the average resolution time?
- Define a North Star proxy: **“Trial import completion rate”** — target to improve by X% within 30 days post-change.
- Set up tracking for the new import flow (event: file_upload_attempt, upload_success, template_download, paste_attempt) so we can measure the effect of design/engineering changes.
- When feasible, run a **cohort analysis** of trial users who hit an import error vs. those who don’t, measuring long-term retention and conversion.

---

## 7. Next Steps & Timeline
| Action | Owner | Target Date |
|--------|-------|-------------|
| Prototype and test 2–3 improved import flows | Design | Week 1–2 |
| T-shirt size feasibility estimates | Engineering | Week 1 |
| Funnel data & impact analysis | Data | Week 1–2 |
| Joint review of findings & solution decision | All | Week 2 end |
| Build and A/B test the quick win (template download) | Eng + Data | Week 3–4 |

---

*This handoff reflects discovery findings as of today. Feasibility estimate is missing by design — Engineering to fill that gap before we commit to a scope. Data must baseline the problem to measure success. Let’s align in the upcoming sync.*
