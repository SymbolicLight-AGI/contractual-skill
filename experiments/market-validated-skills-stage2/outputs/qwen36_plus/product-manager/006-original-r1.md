# 📦 Product Discovery Handoff: Contact Import Setup Drop-off

**Context:** Trial users abandon the onboarding setup flow immediately after attempting to import contacts.  
**Audience:** Design, Engineering, Data/Analytics  
**Status:** Discovery Complete → Handoff for Solutioning & Feasibility  
**Framework Applied:** Impact Mapping + Opportunity Solution Tree  

---

## 🔍 Discovery Evidence
| Source | Finding | Confidence |
|--------|---------|------------|
| User Interviews (n=10) | 7/10 cited CSV formatting confusion as the primary blocker during import. | High |
| Support Logs | Weekly tickets related to import failures, malformed files, and unclear error states. | High |
| Analytics | Setup funnel shows sharp drop-off at the `contact_import` step. Exact rate pending instrumentation. | Medium |
| Engineering | No feasibility estimate or technical spike completed yet. | ⚠️ Unknown |

---

## 🧩 Problem → Opportunity → Solution Space
- **Problem:** Trial users cannot successfully import contacts due to CSV formatting friction.
- **Opportunity:** Reduce setup abandonment by making import validation, guidance, and error recovery intuitive.
- **Solution Hypotheses:**
  1. Provide a downloadable CSV template with locked column headers.
  2. Implement client-side pre-upload validation with row-level error highlighting.
  3. Add inline formatting tips + auto-mapping for common column variations.
  4. Offer alternative import paths (e.g., Google/Outlook sync) to bypass CSV entirely.

---

## 📋 Team-Specific Requirements

### 🎨 Design
- Audit current import UI/UX for clarity, error messaging, and guidance placement.
- Deliver low-fidelity wireframes covering:
  - Pre-upload state (template download, format guide)
  - Validation state (success, partial success, failure with actionable errors)
  - Post-import confirmation & next-step CTA
- Ensure copy aligns with non-technical user mental models.

### ⚙️ Engineering
- Conduct a 1-week feasibility spike on:
  - Current CSV parser limitations & edge cases
  - Client-side vs. server-side validation trade-offs
  - Auto-mapping logic for common header variations
- Deliver T-shirt sizing (S/M/L/XL) and technical constraints.
- Flag any security/compliance considerations (PII handling in uploads).

### 📊 Data / Analytics
- Instrument funnel events: `setup_start` → `csv_upload_initiated` → `validation_pass` / `validation_fail` → `import_complete`
- Capture failure reasons (e.g., `missing_email_column`, `invalid_format`, `timeout`)
- Set up weekly dashboard tracking:
  - Import step drop-off rate
  - Validation error distribution
  - Correlation with support ticket volume

---

## 📈 Success Metrics (SaaS)
| Metric | Baseline | Target | Formula |
|--------|----------|--------|---------|
| Setup Completion Rate | TBD | +25% | `Users completing setup / Users starting setup` |
| Import Step Drop-off Rate | TBD | -40% | `Users dropping at import / Users reaching import` |
| Import-Related Support Tickets | ~Weekly | -50% | `Count of tickets tagged "import" / week` |
| Trial-to-Active Conversion | TBD | +15% | `Active trial users / Total trial starts` |

---

## 🗓️ Next Steps & Ownership
| Action | Owner | Timeline |
|--------|-------|----------|
| UX audit & wireframe draft | Design | Week 1 |
| Feasibility spike & tech spec | Engineering | Week 1 |
| Event tracking plan & dashboard setup | Data | Days 1–3 |
| Cross-functional alignment & prioritization (RICE) | PM | End of Week 1 |
| PRD v1 & sprint planning | PM + Eng + Design | Week 2 |

---

## ⚠️ Open Questions & Risks
- **Feasibility Unknown:** Engineering has not yet assessed parser capabilities or auto-mapping complexity. Spike required before commitment.
- **CSV Variability:** Unclear which third-party exports (Salesforce, HubSpot, Apple, etc.) dominate user uploads. Recommend quick log analysis or survey.
- **Alternative Paths:** If CSV friction is inherent, should we prioritize direct integrations (Google/Outlook) in v1? Requires scope trade-off discussion.
- **Data Gaps:** Current funnel lacks granular import-step tracking. Baseline metrics will be established post-instrumentation.

**Next Action:** Schedule 45-min handoff sync to review wireframes, spike scope, and tracking plan. Please confirm availability and flag any missing inputs before kickoff.
