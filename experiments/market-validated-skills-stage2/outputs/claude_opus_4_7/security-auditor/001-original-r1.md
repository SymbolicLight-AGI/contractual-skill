# Security Audit: `GET /accounts/{accountId}/reports`

## Scope Confirmation

**In scope:** Single API endpoint authorization review (synthetic pattern, code/architecture not provided).
**Out of scope / unknown:** Full system architecture, threat model, deployment environment, compliance regime (assumed sensitive given billing + PII). Findings below are based solely on the described pattern; environment-specific validation is required.

---

## Finding 1: Broken Object-Level Authorization (IDOR) — **CRITICAL**

**OWASP mapping:** A01:2021 — Broken Access Control (specifically IDOR / BOLA, OWASP API Security Top 10 #1).

**Description:**
The endpoint authenticates the caller (proves *who* they are) but does not authorize the caller against the requested resource (`accountId`). Any authenticated user can enumerate or guess `accountId` values and retrieve another tenant's reports.

**Data flow trace (as described):**
```
Client → [AuthN: logged-in check ✅] → Handler → DB query by accountId → Response
                                          ▲
                                          └── MISSING: membership check on (user, accountId)
```
The trust boundary between "authenticated" and "authorized for this account" is collapsed. This is the classic privileged-fetch-ignores-tenancy pattern.

**Business impact:**
- **Confidentiality breach** of billing totals (financial data) and user emails (PII).
- Likely triggers breach-notification obligations under GDPR (Art. 33/34), CCPA, and may implicate PCI-DSS scope if billing data is cardholder-adjacent and SOC 2 CC6.1 (logical access).
- Enumeration of `accountId` (especially if sequential/integer) enables mass scraping.

**CVSS 3.1 (estimated, pending environment confirmation):**
`AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N` → **8.3 High** (Critical in practice if accountIds are guessable and reports include many users).

---

## Finding 2: Sensitive Data Exposure — **HIGH**

Reports combine **billing totals** (financial) and **user emails** (PII / contact identifiers). Even with proper authZ, consider:
- Whether emails are required in the report payload (data minimization, GDPR Art. 5(1)(c)).
- Whether billing totals require additional role gating (e.g., `billing.read`) beyond mere account membership.

---

## Finding 3: Likely Adjacent Weaknesses (assumed, verify)

Given the primary defect, audit these typically-co-located issues:
1. **Other `/accounts/{accountId}/*` routes** — same authZ middleware gap is probably systemic.
2. **Logging** — are un
