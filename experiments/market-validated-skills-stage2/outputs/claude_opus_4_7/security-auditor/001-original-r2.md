# Security Audit: `GET /accounts/{accountId}/reports`

## Scope & Context

- **Asset:** API endpoint returning account-scoped reports (billing totals, user emails)
- **Stated control:** Authentication (logged-in check) only
- **Stated gap:** No account membership / authorization check
- **Compliance relevance:** Likely PII (user emails) and financial data (billing totals) → GDPR Art. 5/32, PCI-DSS (if cardholder-adjacent), SOC 2 CC6.1, HIPAA if applicable

> Note: Audit performed against the synthetic pattern as described. No live testing performed; recommendations should be validated against the actual implementation.

---

## Threat Model & Data Flow Trace

**Entry → Storage path (assumed):**
`Client → Auth middleware (✅ verifies session) → Route handler → Data layer (likely privileged DB/Admin SDK) → Response`

**Trust boundary failure:** The route handler treats `accountId` as a trusted path parameter. Because the data layer is presumed to use a privileged service account, standard row-level / tenant-isolation rules are bypassed. Authentication is *not* authorization.

---

## Findings

### F-1 — IDOR (Broken Object-Level Authorization) — **CRITICAL**
**OWASP API Security Top 10: API1:2023 — BOLA**
**CVSS v3.1 (estimated):** 8.1 (High) — `AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N`

- Any authenticated user can iterate or guess `accountId` values and retrieve reports for arbitrary accounts.
- Predictable identifiers (sequential ints) elevate risk to trivially exploitable; even UUIDs do not constitute access control.

**Impact:**
- **Confidentiality:** Mass disclosure of billing totals (financial data) and user emails (PII → enables phishing, credential stuffing targeting).
- **Compliance:** GDPR personal data breach (Art. 33 notification within 72h); SOC 2 CC6.1 control failure; potential PCI-DSS Req. 7 (restrict access by need-to-know) violation.
- **Business:** Competitor reconnaissance on customer revenue, regulatory fines, reputational damage.

### F-2 — Adversarial / Enumeration Exposure — **HIGH**
- Without authorization, attackers can enumerate the customer base and infer revenue distribution.
- No mention of rate limiting or anomaly detection on the endpoint amplifies bulk-scrape risk.

### F-3 — Logging & Detection Gap (Inferred) — **MEDIUM**
- The description does not indicate access logging tied to `(userId, accountId)` tuples. Without it, post-incident scope determination is infeasible.

### F-4 — Privileged Data Layer "Security Bypass" Pattern — **HIGH (Architectural)**
- If the data layer uses an Admin SDK / service-role credential, database-side policies (e.g., RLS) are not enforced. The application layer is the *only* authorization choke point — and it is missing.

---

## Remediation (Prioritized)

### P0 — Immediate (within 24h)
1. **Add authorization check** in the route handler *before* data fetch:
   ```
   if (!membership.exists(currentUser.id, accountId, requiredRole≥viewer))
       return 403
   ```
2. Return **404 (not 403)** if you want to avoid confirming account existence to non-members; pick one and apply consistently.
3. **Audit access logs** for the last N days for anomalous `accountId` access patterns per user (sudden breadth, high cardinality). If evidence of abuse exists, trigger incident response and breach-notification timers.

### P1 — Short-term (within 1–2 weeks)
4. **Defense in depth:** Enable row-level security / tenant scoping at the data layer so a missing app-layer check still fails closed. Where Admin SDK use is required, wrap it in a repository that *requires* a verified `accountId` membership context.
5. **Centralize authorization** via a policy engine (OPA, Cedar, Oso) or a `requireMembership(accountId, role)` middleware bound to the route — avoid ad-hoc per-handler checks.
6. **Rate limit & anomaly-detect** per-user access to `/accounts/{id}/reports` (e.g., >N distinct accountIds per hour → alert).
7. **Minimize response payload:** Determine whether user emails are required in this report; if not, drop them. If required, consider masking (`j***@domain.com`) unless caller has elevated role.

### P2 — Strategic
8. **Threat-model all `/accounts/{id}/*` and `/orgs/{id}/*` routes** — IDOR rarely exists in isolation. Inventory every parameterized path and verify each enforces membership.
9. **Add automated tests** (`tests/authz/idor.*`) that, for each tenant-scoped route, assert: (a) anonymous → 401, (b) authenticated non-member → 403/404, (c) member → 200.
10. **SAST/Semgrep rule** to flag handlers that read `req.params.accountId` (or equivalent) without calling the membership helper.
11. **Privacy review** of billing+email aggregation under GDPR data minimization (Art. 5(1)(c)).

---

## Validation Plan

- Re-test with three principals: anonymous, authenticated non-member, authenticated member → expect `401 / 403-or-404 / 200`.
- Run automated authz regression suite in CI.
- Verify logs now include `actor_user_id`, `target_account_id`, `decision`, `policy_version`.
- Review residual risk after RLS enablement; document any remaining service-account bypass paths with compensating controls.

---

## Uncertainties / Assumptions

- Assumed the data layer uses privileged credentials (common pattern; please confirm).
- Assumed no upstream gateway enforces authorization (none mentioned).
- Did not assess authentication strength, session handling, or transport security — out of scope for this finding but recommended as a follow-up.
- Breach-notification obligations depend on jurisdiction and whether exploitation occurred — engage legal counsel; this audit does not constitute legal advice.

**Bottom line:** This is a textbook BOLA/IDOR on sensitive financial + PII data. Treat as P0; ship the membership check today, then close the architectural gap so the privileged data layer cannot be the sole trust boundary.
