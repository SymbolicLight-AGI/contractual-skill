# API Contract Handoff: Bulk Contact Import

## Step 1: Consumers, Use Cases & Constraints
- **Primary Consumers:** Frontend application, backend import worker, security/compliance team, QA, technical writers.
- **Core Use Case:** Submit a batch of contacts for asynchronous processing, track progress, and retrieve results including duplicate detection outcomes.
- **Constraints:** 
  - Processing is asynchronous (long-running).
  - PII data is transmitted and stored.
  - Duplicate detection must run before final commit.
  - Frontend requires real-time or near-real-time progress states.

## Step 2: API Style & Resource Model
- **Style:** RESTful (JSON over HTTPS)
- **Resources & Endpoints:**
  - `POST /v1/imports/contacts` → Initiates import job. Accepts batch payload or file reference.
  - `GET /v1/imports/contacts/{import_id}` → Returns job status, progress percentage, and current state.
  - `GET /v1/imports/contacts/{import_id}/results` → Returns processed contacts, success/failure counts, and duplicate report.
- **Data Types:**
  - `ImportJob`: `{ id, status, progress, created_at, updated_at, pii_fields_masked: boolean }`
  - `Contact`: Standardized schema with explicit PII field annotations.
  - `DuplicateReport`: `{ original_id, duplicate_id, match_criteria, resolution_action }`

## Step 3: Cross-Cutting Concerns
- **Auth Strategy:** Bearer token (JWT/OAuth2) with scoped permissions (`imports:write`, `imports:read`). *[Uncertainty: Exact identity provider and token lifecycle not specified.]*
- **Versioning:** URI path versioning (`/v1/`). Backward-compatible additive changes only.
- **Error Handling:** RFC 7807 Problem Details. Standardized codes: `400` (validation), `409` (duplicate conflict), `422` (PII policy violation), `429` (rate limit), `500` (processing failure).
- **Progress & Pagination:** 
  - Progress exposed via `status` enum: `queued` → `validating` → `deduplicating` → `processing` → `completed` | `failed`.
  - Results endpoint uses cursor-based pagination (`?cursor=...&limit=50`) to handle large batches.

## Step 4: Validation Examples & Consistency Check
**Initiate Import (Request)**
```json
POST /v1/imports/contacts
{
  "contacts": [
    { "email": "user@example.com", "phone": "+1234567890", "pii_consent": true }
  ],
  "duplicate_strategy": "skip"
}
```

**Status Response**
```json
GET /v1/imports/contacts/imp_9f8e7d6c
{
  "id": "imp_9f8e7d6c",
  "status": "deduplicating",
  "progress": 0.65,
  "total_records": 1000,
  "processed_records": 650,
  "updated_at": "2026-02-27T10:15:00Z"
}
```

**Error Response (RFC 7807)**
```json
{
  "type": "https://api.example.com/errors/pii-policy-violation",
  "title": "PII Policy Violation",
  "status": 422,
  "detail": "Missing required consent flag for PII fields.",
  "instance": "/v1/imports/contacts"
}
```

---

## Stakeholder Handoff Notes

### 🔒 Security Team
- **PII Handling:** All PII fields are explicitly annotated in the schema. Data in transit is TLS 1.3+. At-rest encryption required for job artifacts.
- **Auth & Scopes:** Enforce least-privilege scopes. Validate token claims against tenant boundaries.
- **Audit & Compliance:** Log import initiation, completion, and duplicate resolutions without storing raw PII. Retention policy for job payloads needs definition. *[Uncertainty: Compliance framework (GDPR/CCPA/HIPAA) and exact retention window not provided.]*
- **Action Required:** Review PII masking in logs, validate duplicate detection logic for data leakage risks, and approve auth scopes.

### 🖥️ Frontend Team
- **Progress States:** Poll `GET /v1/imports/contacts/{id}` every 2–5s. Map `status` enum to UI states (spinner, progress bar, success/failure banners).
- **Duplicate UX:** On `completed`, fetch `/results`. Render duplicate report with user-selectable resolution actions (`merge`, `skip`, `overwrite`).
- **Error Handling:** Gracefully handle `429` (exponential backoff) and `422` (form-level validation feedback).
- **Action Required:** Implement polling/webhook listener, design state machine UI, and define duplicate resolution workflow.

### 🧪 QA Team
- **Test Scenarios:** 
  - Async lifecycle: `queued` → `failed` (timeout/network), `queued` → `completed` (success).
  - Duplicate edge cases: exact match, fuzzy match, cross-tenant duplicates.
  - PII validation: missing consent, malformed PII, oversized payloads.
- **Performance/Load:** Validate rate limits, cursor pagination under 10k+ records, and concurrent import jobs.
- **Action Required:** Build async test harness, mock worker delays, validate PII scrubbing in test logs, and verify pagination consistency.

### 📖 Documentation Team
- **Spec Deliverables:** OpenAPI 3.1 spec with `x-pii` extensions, state transition diagram, and RFC 7807 error catalog.
- **Guidance Needed:** Clear examples for duplicate resolution, polling best practices, and PII compliance warnings.
- **Action Required:** Draft endpoint reference, add interactive examples, document rate limits/auth flows, and publish changelog for `/v1/`.

## ⚠️ Open Questions & Uncertainties
1. **Auth Mechanism:** Is OAuth2, API keys, or mTLS the standard for this service?
2. **PII Compliance:** Which regulatory framework applies, and what is the required data retention/deletion policy for import artifacts?
3. **Duplicate Strategy:** What are the exact matching rules (exact, fuzzy, phonetic) and default resolution behavior?
4. **Progress Delivery:** Should we implement Server-Sent Events (SSE) or webhooks instead of client polling for real-time updates?
5. **Payload Limits:** What is the maximum batch size/MB limit before requiring chunked uploads?

*Next Step:* Resolve uncertainties above, finalize OpenAPI spec, and schedule contract review with all stakeholders before implementation.

*(Boundary Note: This handoff covers API contract design and review preparation. Framework-specific implementation, infrastructure provisioning, and environment-specific security testing fall outside this skill’s scope and should be handled by respective engineering teams.)*
