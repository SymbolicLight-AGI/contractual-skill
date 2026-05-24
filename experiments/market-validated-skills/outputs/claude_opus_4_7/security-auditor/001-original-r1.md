# Authorization Review: `PATCH /projects/{projectId}/settings`

## Scope Confirmation
- Reviewing only the supplied synthetic API design (4 facts listed).
- No tooling, scans, or external assumptions invoked.
- No compliance framework specified; findings are framed against general OWASP A01 (Broken Access Control) and A04 (Insecure Design) principles.

## Data Flow Trace (as described)

```
Client → PATCH /projects/{projectId}/settings
       → Handler: isAuthenticated? ✓
       → [MISSING] Authorization: does projectId belong to an org the user is a member of?
       → [MISSING] Authorization: does the user have a role permitted to mutate settings within that org?
       → Persist billingContactEmail, webhookUrl
```

The trust boundary between "authenticated" and "authorized to mutate this specific project" is not enforced in the described handler.

---

## Findings

### F1 — IDOR on
