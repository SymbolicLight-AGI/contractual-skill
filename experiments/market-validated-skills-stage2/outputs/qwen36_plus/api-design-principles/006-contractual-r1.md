1. Design summary.
Supplied facts: imports are asynchronous, duplicate detection is required, PII is involved, and frontend needs progress states. Inferred design choice: a job-based resource model (`ContactImport`) with a submission endpoint and a status/polling endpoint. Assumptions: authentication is token-based, webhooks are not required, and duplicate handling should not block the entire batch. The design exposes a `POST` to initiate the import and a `GET` to track progress, returning aggregated counts and masked error details to satisfy frontend state requirements while minimizing PII exposure.

2. Proposed API shape.
*(Note: Examples are illustrative and derived from task requirements. Actual schemas require platform validation.)*
- `POST /v1/contact-imports`
  - Headers: `Idempotency-Key: <uuid>` (required for write safety)
  - Body: `{ "source_url": "string", "dedup_strategy": "email|phone|custom_id" }`
  - Response: `202 Accepted` → `{ "id": "imp_abc123", "status": "queued", "created_at": "ISO8601" }`
- `GET /v1/contact-imports/{id}`
  - Response: `200 OK` → `{ "id": "imp_abc123", "status": "queued|processing|completed|failed", "progress": { "total_records": 1000, "processed": 450, "succeeded": 400, "duplicates": 30, "failed": 20 }, "result_url": "string (presigned, expires)", "errors": [ { "row": 12, "field": "email", "message": "invalid_format" } ] }`
- Error semantics: HTTP 4xx/5xx reserved for transport/auth/validation failures. Job-level failures are surfaced in the `status` and `errors` fields to preserve async contract semantics.
- Uncertainty markers: Auth model, exact PII fields, rate limits, and data retention policy are unspecified and marked for downstream review.

3. Key tradeoffs.
- Async polling vs. webhooks: Polling is selected to satisfy frontend progress requirements without requiring consumer infrastructure. Tradeoff: increased client complexity and potential polling overhead. Resolution: recommend exponential backoff and configurable polling intervals.
- Duplicate handling strategy: Continue-with-reporting vs. fail-fast. Continue-with-reporting is chosen to prevent single duplicates from blocking entire batches. Tradeoff: requires partial-success state handling and more complex frontend reconciliation.
- PII visibility in status: Aggregated counts with masked error details vs. full record exposure. Aggregation minimizes PII exposure during polling. Tradeoff: reduces debugging granularity. Resolution: provide a secure, time-limited `result_url` for full audit/review.

4. Risks and human gates.
- Security & PII risks: Data in transit/at rest, access control granularity, audit logging, and secure result URL expiration. Human gate: Security team must approve data handling, encryption standards, and access boundaries before contract finalization.
- Frontend integration risks: State machine mapping, polling frequency vs. rate limits, UX for partial failures/duplicates. Human gate: Frontend team must validate progress state transitions and error handling UX.
- QA & contract risks: Race conditions in async state transitions, large payload handling, idempotency enforcement, duplicate edge cases. Human gate: QA must approve contract tests and load scenarios before production migration.
- Documentation risks: Clear state diagrams, error semantics, rate limits, and migration notes. Human gate: Docs team must review developer ergonomics and example accuracy.
- Additional gates: Any changes to auth scopes, public API commitments, or data retention policies require explicit product and security approval.

5. Verification checklist.
- [ ] Contract tests cover all status transitions (`queued` → `processing` → `completed`/`failed`).
- [ ] JSON Schema validation enforces required fields, type constraints, and enum values.
- [ ] Idempotency key handling verified for duplicate `POST` submissions.
- [ ] PII fields are masked in logs, status responses, and error payloads.
- [ ] Rate limiting and polling backoff behavior documented and tested.
- [ ] Consumer review completed with frontend team for state mapping and UX.
- [ ] Security review completed for auth boundaries, data retention, and secure result delivery.
- [ ] Documentation includes illustrative examples, state transition diagram, and error handling guide.
