1. Design Summary
[Supplied Facts] Imports are asynchronous, duplicate detection is required, PII is involved, and frontend needs progress states.
[Inferred Design] A RESTful `ContactImport` resource with a two-step lifecycle: submission (`POST`) and status polling (`GET`). The job tracks progress counts and duplicate outcomes. PII is restricted to authorized consumers and masked in logs/status payloads.
[Uncertainty] Exact authentication/authorization model, maximum payload/file size, preferred progress delivery mechanism (polling vs. webhooks), specific PII fields, and duplicate resolution policy (skip, merge, or flag) are not provided. These require explicit definition before implementation.
[Goal Alignment] Provides a consistent, maintainable contract that separates submission from execution, exposes deterministic progress states for frontend consumption, and enforces PII boundaries.

2. Proposed API Shape
[Note: Examples are illustrative and derived from task constraints. Actual schemas require platform validation.]

- `POST /v1/contact-imports`
  - Purpose: Submit a bulk contact import job.
  - Headers: `Idempotency-Key: <uuid>` (required for write safety)
  - Request Body (illustrative):
    ```json
    {
      "source": "presigned_url_or_file_ref",
      "dedup_strategy": "email_or_phone",
      "on_duplicate": "skip"
    }
    ```
  - Response: `202 Accepted`
    ```json
    {
      "id": "imp_9f8e7d6c",
      "status": "queued",
      "created_at": "2024-01-15T10:00:00Z"
    }
    ```

- `GET /v1/contact-imports/{id}`
  - Purpose: Retrieve job status and progress metrics.
  - Response: `200 OK`
    ```json
    {
      "id": "imp_9f8e7d6c",
      "status": "processing",
      "progress": {
        "total_records": 5000,
        "processed": 2100,
        "succeeded": 1950,
        "duplicates_skipped": 120,
        "failed": 30
      },
      "result_url": null,
      "updated_at": "2024-01-15T10:02:15Z"
    }
    ```
  - Terminal States: `completed` (includes `result_url`), `failed` (includes `error_code` and `error_message`).
  - Error Model: Standard HTTP status codes (`400`, `401`, `403`, `404`, `409`, `429`, `500`). Job-level errors surface in the `GET` response, not as HTTP errors, to preserve async semantics.

3. Key Tradeoffs
- Async vs. Sync: Async (`202 Accepted`) prevents request timeouts and supports scale, but requires frontend polling or webhook integration. Tradeoff: increased client complexity vs. backend reliability.
- Duplicate Handling: "Continue with reporting" (partial success) is chosen over "fail-fast" to avoid blocking entire batches. Tradeoff: requires consumers to parse mixed success/duplicate/failure counts.
- Progress Granularity: Record counts are exposed instead of percentages to avoid rounding ambiguity and support accurate UI progress bars. Tradeoff: slightly larger payload size.
- PII Exposure: PII is excluded from status responses and logs. Tradeoff: limits ad-hoc debugging but enforces compliance.

4. Risks and Human Gates
[Security Handoff]
- Review PII encryption in transit/at rest, field-level access controls, and audit logging requirements.
- Validate that `Idempotency-Key` storage does not leak sensitive payloads.
- Gate: Requires explicit approval for auth model, data retention policy, and PII handling boundaries before public commitment.

[Frontend Handoff]
- Map polling intervals to `status` transitions (`queued` → `processing` → `completed`/`failed`).
- Define UX for partial success (duplicates/failures) and error recovery.
- Gate: Requires frontend sign-off on state machine, polling strategy, and error messaging.

[QA Handoff]
- Contract tests must cover all status transitions, idempotency replay, duplicate edge cases, and malformed payloads.
- Load tests required for queue saturation and concurrent job submissions.
- Gate: Requires QA approval of test matrix and observability hooks (metrics, tracing) before production migration.

[Docs Handoff]
- Provide state transition diagram, rate limits, retry guidance, and illustrative examples.
- Clarify `dedup_strategy` and `on_duplicate` behavior with concrete scenarios.
- Gate: Requires documentation review for developer ergonomics and backward compatibility notes.

[General Risks]
- Race conditions if duplicate detection relies on stale indexes.
- Queue backpressure under high concurrency.
- Uncertainty: Webhook vs. polling preference, exact PII fields, and file format constraints must be resolved to finalize the contract.

5. Verification Checklist
- [ ] Method/resource consistency: `POST` creates, `GET` reads status; no `PUT`/`PATCH` on async jobs.
- [ ] Schema clarity: All fields typed, required/optional marked, terminal states explicitly defined.
- [ ] Error handling: HTTP errors for client/server faults; job errors in payload; consistent error codes.
- [ ] Auth boundary: PII access restricted; `Idempotency-Key` enforced for `POST`.
- [ ] Idempotency: Replay of identical `POST` with same key returns original `202` without duplicate jobs.
- [ ] Compatibility: Versioned path (`/v1/`); additive changes only; breaking changes require human gate.
- [ ] Observability: Metrics for queue depth, processing latency, duplicate rates, and failure reasons.
- [ ] Consumer review: Frontend confirms progress state mapping; QA confirms contract test coverage; Security confirms PII controls; Docs confirms example accuracy.
