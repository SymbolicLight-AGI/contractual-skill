## Handoff: Bulk Contact Import API

**To:** Security, Frontend, QA, Documentation  
**From:** API Design (Reviewer)  
**Subject:** API contract readiness review for asynchronous bulk contact import with duplicate detection and PII

The following outlines what each team should validate against the current draft API specification. The API is designed as a RESTful, asynchronous service. The core flow: initiate import, poll job status, retrieve results. Duplicate detection is built into the processing pipeline. PII is handled throughout.

### 1. Security Team
- **Authentication & Authorization**  
  Confirm that the endpoints require proper authentication (token-based, OAuth2). Validate that the required OAuth scope or permission is clearly defined (e.g., `contacts:import`), and that only authorized roles can initiate and view imports.

- **PII Protection**  
  - Verify that PII fields are transmitted only over TLS (HTTPS) and never logged or returned in error messages in plain text.  
  - Ensure the import payload/file is scanned for malicious content (if file upload).  
  - Check that any temporary storage of the uploaded data is encrypted at rest and purged according to a documented retention policy.  
  - Confirm that duplicate detection does not leak PII of existing contacts (e.g., by returning full details of matched records without proper masking). The API should return only non‑PII duplicate indicators (e.g., `duplicate: true`, `duplicate_of: contact_id`), or require explicit consent for full disclosure.

- **Rate Limiting & Abuse Prevention**  
  Look for rate limiting on the import initiation endpoint to prevent enumeration or DoS attacks, especially given PII. Idempotency keys should be supported and enforced.

- **Audit & Compliance**  
  The API must generate audit events for import attempts, including success/failure and processing outcomes, without exposing PII in logs.

### 2. Frontend Team
- **Endpoints and Asynchronous Flow**  
  The draft should include:
  - `POST /v1/imports` – Initiates an import. Request body: multipart upload or JSON payload. Response: `202 Accepted` with `Location` header pointing to the job resource (`/v1/imports/{jobId}`) and a representation of the job (status = `pending`).
  - `GET /v1/imports/{jobId}` – Returns current job status and progress.

- **Progress States & UI Mapping**  
  The `status` field must be one of: `pending`, `processing`, `completed`, `failed` (optionally `cancelled`). Additional fields needed by the UI:
  - `progress_percent` (integer 0–100)
  - `total_records`, `processed`, `duplicates_found`, `errors_count`
  - A link or flag for a review step when duplicates were detected (`review_required: true`)
  - The completed state must provide a `results_url` to fetch the final report (possibly paginated).

- **Error Handling**  
  Consistent error response format (`error_code`, `message`, `details`). Frontend must handle:
  - Network failures (retry polling with caution)
  - 4xx/5xx status (display user-friendly messages)
  - Long‑running imports (timeout considerations, push notification fallback if feasible)

- **Practical Recommendations**  
  - The draft should specify polling interval guidance (e.g., `Retry-After` header).  
  - Clarify whether the final results endpoint supports pagination if many duplicates/errors are returned.

### 3. QA Team
- **Test Scenarios to Validate Against the Contract**
  - **Happy Path:** Small valid import file, no duplicates → `completed` with correct counts.
  - **Duplicate Detection:**  
    - Exact match on email/phone → `duplicates_found` > 0, review flag set, no sensitive data leaked.  
    - Fuzzy matching rules (if any) → verify intent.
  - **Edge Cases:**  
    - Empty file or no records → appropriate error.  
    - Unsupported file formats → `400` with clear error.  
    - Maximum file size limit → `413` or rejected in request validation.  
    - Missing required fields → `422` with field‑level errors.
  - **Asynchronous Behavior:**  
    - Polling returns correct state transitions (pending → processing → completed/failed).  
    - Status endpoint returns consistent data across multiple calls.  
    - Job cancellation (if supported) and concurrent imports.
  - **Authentication/Authorization:** invalid/expired token, insufficient scope → `401`/`403`.
  - **Rate Limiting:** rapid successive imports → `429` with `Retry-After`.
  - **PII & Logging:** confirm that errors/logs do not echo plain PII from the request.

- **Non‑functional Checks**  
  - Performance under load for large import files (time to first status update).  
  - Duplicate detection accuracy (provide sample datasets).

### 4. Documentation Team
- **API Reference Content**  
  The draft must define all endpoints with:
  - HTTP method, URL path (versioned), headers (Authentication, Content‑Type, Idempotency‑Key).
  - Request body schema (field names, types, constraints, example).
  - Response schemas for both 2xx and error cases.
  - Status codes and their meaning (202, 200, 400, 401, 403, 404, 413, 422, 429, 500).

- **Asynchronous Workflow Description**  
  Step‑by‑step guide with code snippets (cURL, maybe one language). Explain polling, job states, and how to retrieve results.

- **Duplicate Detection**  
  Explain what qualifies as a duplicate, how it is handled, and what the consumer should do when `review_required` is true. Never expose raw PII of existing contacts. Provide example response showing a duplicate report (masked).

- **Authentication & Authorization**  
  Clearly specify the OAuth flow, required scopes, and how to obtain a token for testing.

- **Error Reference**  
  Table of all error codes with descriptions and resolution hints.

- **PII & Security Notice**  
  Prominent callout that the API handles Personally Identifiable Information, and consumers are responsible for securing tokens and respecting data retention policies.

### Missing Information / Next Steps
The draft should explicitly define:
- Whether file uploads are accepted (multipart) or only JSON/CSV strings in the request body.
- The exact fields that trigger duplicate detection (e.g., email, phone, external_id).
- The retention period for import jobs and their results.

Please review the actual specification against these checkpoints and raise any gaps. Once approved by all teams, the API can move to environment‑specific validation and implementation.

**Boundary note:** This handoff is based on REST API design principles. If the underlying contract is GraphQL, adjust the interaction patterns accordingly (mutations, subscriptions for progress), but the same security, PII, duplicate detection, and documentation principles apply.
