# Remediation Handoff — Synthetic Findings

**Scope note:** Findings provided are synthetic/pre-triaged. CVSS scores below are advisory estimates based on description only; environment-specific factors (data sensitivity, exposure, compensating controls) were not provided and should be validated by the receiving teams. No live testing was performed.

---

## Finding Summary

| ID | Title | Severity (est.) | OWASP | Primary Owner |
|---|---|---|---|---|
| F-1 | Missing object-level authorization on `/reports` | **High** | A01:2021 Broken Access Control (IDOR) | Engineering (Reports service) |
| F-2 | Session cookies missing `Secure` attribute | **Medium** | A05
