# Handoff: Bulk Contact Import API

## 1. Design Summary

Asynchronous bulk contact import with duplicate detection, PII handling, and frontend-visible progress states. This handoff packages what is known from the task and routes open questions to the correct downstream reviewers. No design decisions have been finalized; no implementation, deployment, or documentation has occurred.

## 2. Supplied Facts vs. Inferences

**Supplied by task:**
- Imports are asynchronous.
- Duplicate detection is required.
- PII is involved.
- Frontend needs progress states.

**Not supplied (must be confirmed before design lock):**
- Input format (CSV, JSON, multipart upload, presigned URL).
- Maximum batch size and rate limits.
- Duplicate-detection key(s) and conflict resolution policy (skip, overwrite, merge).
- Auth model and tenant scoping.
- Retention policy for uploaded files and intermediate state.
- Versioning policy and existing conventions.
- Specific PII fields and jurisdictions.
- Failure semantics (partial success vs. all-or-nothing).

These gaps are flagged as **assumptions** below where a placeholder shape is shown. All examples are illustrative.

## 3. Proposed API Shape (Illustrative, For Reviewer Discussion)

Asynchronous job pattern with a submission endpoint, a job status endpoint, and an optional results endpoint.

**Submit import (illustrative):**
```
POST /v1/contact-imports
Idempotency-Key: <client-generated UUID>
Content-Type: application/json

{
  "source": "<format-to-be-confirmed>",
  "duplicate_policy": "skip | overwrite | merge",   // TBD with product
  "contacts": [ /* or a file reference */ ]
}

202 Accepted
{
  "job_id": "imp_...",
  "status": "queued",
  "status_url": "/v1/contact-imports/imp_..."
}
```

**Poll status (illustrative):**
```
GET /v1/contact-imports/{job_id}

200 OK
{
  "job_id": "imp_...",
  "status": "queued | running | completed | failed | partially_completed",
  "progress": {
    "total": 10000,
    "processed": 4200,
    "succeeded": 4100,
    "duplicates": 80,
    "failed": 20
  },
  "errors_url": "/v1/contact-imports/imp_.../errors",
  "created_at": "...",
  "updated_at": "..."
}
```

**Per-row errors (illustrative):**
```
GET /v1/contact-imports/{job_id}/errors?cursor=...&limit=...
```

Notes:
- `Idempotency-Key` on submission prevents duplicate jobs from retried client calls (distinct from row-level duplicate detection).
- Progress fields are enumerated to give the frontend deterministic state transitions.
- Errors are paginated because PII row counts may be large.
- Webhook/event delivery as an alternative to polling is **not proposed here** — flag for product decision.

## 4. Key Tradeoffs

- **Polling vs. webhooks/SSE:** Polling is simpler and matches the stated "progress states" need; webhooks reduce client load but add delivery and auth complexity. Decision needed.
- **Inline payload vs. file upload:** Inline JSON is simpler for small batches; file upload (or presigned URL) scales further but adds storage, retention, and PII-at-rest concerns.
- **Duplicate policy as request parameter vs. tenant configuration:** Per-request is flexible but increases surface area; tenant-level is simpler but less expressive.
- **Partial success semantics:** `partially_completed` plus an errors endpoint is explicit but adds states the frontend must handle. All-or-nothing is simpler but worse UX for large imports.
- **Synchronous duplicate detection vs. eventual:** Affects whether `progress.duplicates` is authoritative mid-run.

## 5. Risks and Human Gates

**Risks:**
- PII in request bodies, logs, error payloads, and job-status responses. Unbounded log retention is a likely exposure point.
- Error endpoints may echo PII back to any caller with the `job_id`; authorization scoping is required.
- Idempotency-key collisions across tenants if not namespaced.
- Long-running jobs vs. token/session expiry.
- Backward compatibility once consumers depend on progress field names and status enum values.

**Human gates required before finalization:**
- Security sign-off on PII handling, auth scope, and retention.
- Product sign-off on duplicate-resolution policy and partial-success semantics.
- Platform sign-off on versioning, idempotency, and rate-limit conventions.
- Any commitment to a public/partner contract.

## 6. Handoff Packages

### → Security
Please review:
- PII fields in request, response, and error payloads. Confirm which fields may appear in `GET /errors` responses.
- Auth model: who can submit imports, who can read job status and errors, cross-tenant isolation of `job_id`.
- Logging and tracing redaction rules for PII.
- Retention of uploaded payloads, intermediate state, and error records.
- Transport requirements (TLS, signed URLs if file-based).
- Jurisdictional constraints (e.g., regional data residency) — not specified in task.

### → Frontend
Please review and confirm needs:
- Status enum: `queued | running | completed | failed | partially_completed` — sufficient?
- Progress shape: `total / processed / succeeded / duplicates / failed` — are additional buckets needed (e.g., `invalid_format`, `skipped`)?
- Polling cadence expectations and whether SSE/websocket is desired instead.
- How duplicates should be surfaced to end users (per-row reasons via the errors endpoint?).
- Cancellation requirement — not addressed; please confirm if needed.
- Resumability or retry-from-failure expectations.

### → QA
Test scope to define:
- Contract tests for submit, status, and errors endpoints against the agreed schema.
- Idempotency-Key behavior: same key returns same job; different payload + same key returns conflict.
- Duplicate detection across each agreed policy (skip/overwrite/merge).
- Partial success: mixed valid/invalid rows produce correct counts and error records.
- PII redaction in logs and error messages.
- Authorization: cross-tenant `job_id` access is denied.
- Large-batch behavior, timeouts, and pagination of errors.
- Status transitions are monotonic and terminal states do not regress.
- **Note:** No tests have been written or run; this is a proposed test scope only.

### → Docs
Material to prepare once the contract is approved:
- Endpoint reference for submit, status, and errors.
- Status lifecycle diagram with all transitions.
- Duplicate policy semantics with worked examples.
- Idempotency-Key usage guidance and client retry pattern.
- Error model and per-row error format.
- PII handling note for integrators (what they may and may not send).
- Versioning and deprecation policy reference.
- **Note:** No documentation has been published.

## 7. Verification Checklist (Pre-Implementation)

- [ ] Resource and method choices reviewed against existing conventions (not supplied).
- [ ] Status enum and progress schema confirmed with frontend.
- [ ] Duplicate policy confirmed with product.
- [ ] PII fields enumerated and reviewed by security.
- [ ] Idempotency semantics documented and tested.
- [ ] Error model paginated and PII-safe.
- [ ] Auth and tenant isolation reviewed.
- [ ] Versioning decision recorded.
- [ ] Contract tests defined by QA.
- [ ] Breaking-change and public-commitment gates cleared before release.

## Boundary Notes

- All endpoint shapes, field names, and status values above are **illustrative** and derived from the four supplied facts plus standard async-job patterns. They are not copied from a provided schema.
- This Skill cannot approve the design, write code, run tests, publish docs, or confirm deployment. Those require the respective reviewers and the human gates listed above.
