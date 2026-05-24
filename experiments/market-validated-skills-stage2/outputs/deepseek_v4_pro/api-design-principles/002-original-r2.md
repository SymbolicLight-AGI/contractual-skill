## API Design Review: `POST /users/{id}/delete-all-data`

**Status: Blocked – Critical missing information**  
The proposed endpoint cannot proceed to implementation until the gaps below are resolved. The following review covers the required elements per our API design principles.

### 1. Auth Model (Missing – must be specified)
- **Authentication:** How is the caller identified? (OAuth 2.0, API key, session token?)  
- **Authorization:** What scopes or roles are required? Examples: `users:purge`, `admin:full-access`. Is a user allowed to delete their own data, or is this admin‑only?  
- **Risk:** Without an auth model, no access control exists. This is a non‑starter.

### 2. Data Retention & Scope Definition (Missing)
- **What data is deleted?** All PII, all platform data, third‑party integrations, backups?  
- **Legal/compliance:** How does this interact with GDPR “right to erasure,” data‑retention regulations, or contractual obligations?  
- **Deletion type:** Is it a hard (irreversible) delete, soft delete (flag + retention period), or anonymisation?  
- **Recovery:** Is there a grace period or “undo” mechanism? Must be documented.

### 3. Audit Policy (Missing)
- **Logging:** Every invocation must produce an immutable audit trail entry containing at least:  
  - Actor (user ID, API client ID)  
  - Timestamp  
  - Target user ID  
  - Result (success, partial, failure)  
  - Details (number of records affected, errors)  
- **Storage:** Where is the audit log stored, and for how long?  
- **Compliance:** If legal holds apply, how does the system prevent deletion?

### 4. Customer Confirmation Flow (Missing)
- **Destructive action safety:** A direct `POST` is too dangerous. Required safeguards:  
  - A confirmation token or two‑step process (e.g., first request returns a unique token, second request sends the token).  
  - Or require re‑authentication (password, MFA) in the request headers/body.  
  - Rate limiting to prevent abuse/mistakes.  
- **Without this, the endpoint violates the principle of least surprise and safety.**

### 5. Additional Design Observations
- **Resource modeling:** `POST /users/{id}/delete-all-data` is an RPC‑style action tacked onto a resource. Better alternatives (depending on semantics):  
  - `POST /users/{id}/purge` with an idempotency key, returning `202 Accepted` if asynchronous.  
  - `POST /data‑erasure‑requests` as a first‑class resource (especially if the flow needs approval or scheduling).  
- **Error handling:** Must define responses for:  
  - `401 Unauthorized` / `403 Forbidden`  
  - `404 Not Found`  
  - `409 Conflict` (e.g., a purge already in progress)  
  - `422 Unprocessable Entity` (missing confirmation, invalid token)  
  - `500 Internal Server Error` with no data leakage  
- **Idempotency:** All destructive `POST` endpoints should require an `Idempotency-Key` header to prevent accidental duplicate deletions.  
- **Versioning:** The endpoint should include a version prefix (e.g., `/v1/users/{id}/purge`) or a version header to allow safe evolution.  
- **Response format:** Clarify if the operation is synchronous or asynchronous. If async, return `202` with a tracking URL; if sync, define the response body (status, affected record counts, errors).  
- **Pagination:** Not directly applicable, but if the response includes a list of deleted items, pagination must be supported.

### Required Next Steps
1. **Supply the missing artefacts:** Auth model & permissions matrix, data scope & retention policy, audit log schema, confirmation mechanism design.  
2. **Conduct a security & privacy review** referencing the design above.  
3. **Use the implementation playbook** (`resources/implementation-playbook.md`) for detailed checklists on error formatting, pagination, and versioning once the foundational gaps are filled.

The proposal is rejected in its current form. Re‑submit with the missing sections for a follow‑up review.
