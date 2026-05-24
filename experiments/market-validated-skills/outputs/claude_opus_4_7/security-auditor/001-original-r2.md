# Security Review: `PATCH /projects/{projectId}/settings`

## Scope Confirmation

- **Asset**: Single synthetic API endpoint design
- **Review type**: Manual design review (no tools/scans, per instruction)
- **Trust boundary in focus**: Authenticated client → Handler → Project data store
- **Compliance context**: Not provided — findings stated framework-agnostic

---

## Data Flow Trace

```
Client (authenticated) 
  → PATCH /projects/{projectId}/settings
  → Handler: verifies session/login  ✅
  → Handler: [MISSING] verify project ∈ user's organizations
  → Handler: [UNKNOWN] verify user role within that organization
  → Persistence: writes billingContactEmail, webhookUrl
```

The `projectId` is a **client-supplied identifier referencing a global resource**. Authentication alone proves *who* the caller is, not *what they may touch*.

---

## Findings

### 🔴 F1 — IDOR / Broken Object-Level Authorization (Critical)
**OWASP API Top 10: API1:2023 — BOLA**

Any authenticated user (from *any* organization) can submit a `projectId` belonging to a different organization and mutate its settings. Login ≠ authorization.

**Impact**:
- **`billingContactEmail`
