# API Contract Handoff: Bulk Contact Import

## 1. Consumers, Use Cases & Constraints
- **Primary Consumers:** Frontend application (UI/UX), Backend import worker, Security/Compliance, QA, Technical Writers
- **Use Case:** Upload a batch of contacts, trigger asynchronous processing, track progress, resolve duplicates, and retrieve final import results.
- **Constraints:** 
  - Processing is asynchronous; immediate response must return a job identifier.
  - Duplicate detection is mandatory before persistence.
  - Payload contains PII; requires strict access control, encryption in transit/at rest, and auditability.
  - Frontend requires real-time or near-real-time progress states.

## 2. API Style & Resource Model
- **Style:** RESTful (JSON)
- **Resources & Endpoints:**
  - `POST /v1/imports/contacts` → Initiates import job. Accepts `application/json` or `multipart/form-data` (CSV/JSON).
  - `GET /v1/imports/contacts/{import_id}` → Returns job status, progress percentage, and current state.
  - `GET /v1/imports/contacts/{import_id}/results` → Returns paginated success/failure/duplicate breakdown.
- **Core Types:**
  - `ImportJob`: `{ id, status, progress, created_at, updated_at, total_records, processed_records }`
  - `ProgressState`: `queued | validating | deduplicating | importing | completed | failed`
  - `DuplicateReport`: `{ original_contact_id, duplicate_contact_id, match_criteria, resolution_action }`

## 3. Cross-Cutting Specifications
- **Authentication & Authorization:** Bearer token (OAuth 2.0 / JWT) with `contacts:import` scope. Role-based access enforced at gateway.
- **Versioning:** URI path versioning (`/v1/`). Backward-compatible additive changes only.
- **Error Handling:** RFC 7807 Problem Details. Standardized codes: `400` (validation), `409` (duplicate conflict on sync fallback), `413` (payload too large), `429` (rate limit), `500` (internal).
- **Pagination:** Cursor-based (`?cursor=...&limit=50`) for `/results` endpoint.
- **Progress Tracking:** Polling interval recommended: 2–5s. Webhook callback optional (see uncertainties).

## 4. Validation Examples
**Initiate Import (Request)**
```json
POST /v1/imports/contacts
{
  "contacts": [
    { "email": "alice@example.com", "first_name": "Alice", "last_name": "Smith", "phone": "+15550199" }
  ],
  "duplicate_strategy": "skip",
  "notify_on_completion": true
}
```

**Status Response**
```json
GET /v1/imports/contacts/imp_9f8a7b6c
{
  "id": "imp_9f8a7b6c",
  "status": "processing",
  "progress_state": "deduplicating",
  "progress_percent": 64,
  "total_records": 1500,
  "processed_records": 960,
  "created_at": "2026-02-27T10:00:00Z",
  "updated_at": "2026-02-27T10:02:14Z"
}
```

**Error Response**
```json
{
  "type": "https://api.example.com/errors/import-validation-failed",
  "title": "Invalid Contact Format",
  "status": 400,
  "detail": "Row 42: 'email' field is missing or malformed.",
  "instance": "/v1/imports/contacts/imp_9f8a7b6c"
}
```

---

## Stakeholder Handoff Directives

### 🔒 Security
- **PII Handling:** All contact fields are classified as PII. Enforce TLS 1.3, field-level encryption at rest, and strict RBAC.
- **Audit Trail:** Log `import_id`, initiator, timestamp, and `duplicate_strategy`. Do not log raw PII payloads.
- **Rate Limits & Abuse Prevention:** Enforce payload size caps, request frequency limits, and validate `duplicate_strategy` enum.
- **Action Required:** Review data retention policy for import artifacts and confirm compliance with applicable privacy regulations.

### 🖥️ Frontend
- **State Machine:** Map UI to `ProgressState` enum. Disable submit during `queued`/`processing`. Show progress bar using `progress_percent`.
- **Polling Strategy:** Implement exponential backoff polling (2s → 5s → 10s) on `GET /v1/imports/contacts/{id}`. Cancel on `completed`/`failed`.
- **Duplicate UX:** On `completed`, fetch `/results` and surface `DuplicateReport` for user review if `duplicate_strategy` is `review`.
- **Action Required:** Confirm polling interval tolerance and design fallback for network interruptions.

### 🧪 QA
- **Test Coverage:** Validate async lifecycle, state transitions, idempotency on retry, and duplicate detection edge cases (exact match, case-insensitive, whitespace).
- **Performance/Load:** Test with max payload size, concurrent imports, and degraded worker throughput. Verify `429` and `500` recovery.
- **PII Validation:** Ensure logs, metrics, and error responses never leak raw PII. Verify encryption at rest.
- **Action Required:** Provide test matrix for `duplicate_strategy` variants (`skip`, `merge`, `review`) and async timeout thresholds.

### 📖 Docs
- **OpenAPI Spec:** Publish `/v1/imports/contacts` endpoints with full schema, enums, and RFC 7807 error definitions.
- **Guides:** Document async flow, polling best practices, duplicate resolution strategies, and PII handling warnings.
- **Examples:** Include success, partial failure, and duplicate-heavy scenarios.
- **Action Required:** Align terminology with `ProgressState` enum and add rate-limit/PII compliance callouts.

---

## ⚠️ Uncertainties & Missing Inputs
- **Auth Mechanism:** Exact token type (JWT, API key, mTLS) and scope naming convention not specified.
- **PII Compliance Framework:** GDPR, CCPA, HIPAA, or internal policy not confirmed. Impacts retention, audit, and masking rules.
- **Duplicate Detection Logic:** Match criteria (email-only, fuzzy name+phone, etc.) and `duplicate_strategy` enum values need finalization.
- **Progress Delivery:** Polling-only vs. webhook/SSE support not defined.
- **Data Retention:** How long import jobs, logs, and result artifacts are stored before purge.

## Next Step
Please confirm the above uncertainties. Once resolved, I will finalize the OpenAPI contract, lock the `ProgressState` and `duplicate_strategy` enums, and route the spec to the `resources/implementation-playbook.md` checklist for pre-implementation validation.
