### 1. Design Summary
The proposed API contract supports an asynchronous bulk contact import process. To accommodate the requirements, the design separates the initial ingestion of data from the processing phase. It includes mechanisms for duplicate detection, tracks progress states for frontend consumption, and establishes strict boundaries for handling Personally Identifiable Information (PII). 

### 2. Proposed API Shape
*Note: The following schemas and endpoints are illustrative based on the provided requirements.*

**Start Import**
*   **Endpoint:** `POST /v1/contact-imports`
*   **Description:** Accepts the bulk payload and initiates the async process. Must be idempotent (e.g., via an `Idempotency-Key` header) to prevent accidental duplicate bulk uploads.
*   **Request Payload:** Contains the contact data (or a reference to a securely uploaded file) and a duplicate resolution strategy (e.g., `skip`, `overwrite`).
*   **Response:** `202 Accepted`
*   **Response Payload:** 
    ```json
    {
      "import_id": "abc-123",
      "status": "pending",
      "status_url": "/v1/contact-imports/abc-123"
    }
    ```

**Check Import Progress**
*   **Endpoint:** `GET /v1/contact-imports/{import_id}`
*   **Description:** Polled by the frontend to retrieve the current progress state.
*   **Response:** `200 OK`
*   **Response Payload:**
    ```json
    {
      "import_id": "abc-123",
      "status": "processing", 
      "progress": {
        "total": 1000,
        "processed": 450,
        "duplicates_detected": 12,
        "errors": 0
      }
    }
    ```
    *(Lifecycle states for `status`: `pending`, `processing`, `completed`, `failed`)*

### 3. Key Tradeoffs
*   **Asynchronous vs. Synchronous:** An async design prevents timeouts on large bulk imports but forces the frontend to implement polling (or WebSockets) to update the UI, increasing client-side complexity.
*   **Duplicate Detection Timing:** Handling duplicate detection asynchronously during processing keeps the initial `POST` request fast, but means users will not know about duplicates until the job is underway or completed.
*   **Payload vs. File Upload:** The exact ingestion method (JSON array vs. multipart file upload) is unstated. A JSON array is easier for frontend validation but may hit payload size limits at scale. *Uncertainty marked: The exact scale and payload size limits are missing and must be defined.*

### 4. Risks and Human Gates
*   **Security Risk (PII):** The payload contains PII. There is a risk of PII leaking into standard application logs, error responses, or being retained longer than necessary in temporary storage.
*   **Operational Risk:** High-volume bulk imports could degrade database performance if rate limiting and background worker concurrency are not properly tuned.
*   **Human Gates:** **Human approval is required** from Security for the PII data retention policy and auth boundaries, and from Product/Engineering Leadership for the public API commitment.

### 5. Verification Checklist & Handoff

**To Security:**
*   [ ] Review the authentication and authorization boundaries for the `POST` and `GET` endpoints.
*   [ ] Verify that PII in the import payload is encrypted in transit and at rest.
*   [ ] Approve the data retention policy for the temporary storage of the import payload and the resulting progress logs.
*   [ ] Ensure PII is masked or stripped from all observability and error logging.

**To Frontend:**
*   [ ] Review the proposed polling mechanism (`GET /v1/contact-imports/{import_id}`) and agree on a polling interval to avoid rate-limiting.
*   [ ] Validate that the progress state enum (`pending`, `processing`, `completed`, `failed`) and the `progress` object provide enough detail for the required UI states.
*   [ ] Confirm handling of the `202 Accepted` status code.

**To QA:**
*   [ ] Define contract tests for the request/response schemas.
*   [ ] Verify the idempotency of the `POST` endpoint (e.g., submitting the same request twice safely).
*   [ ] Test the duplicate detection logic against various edge cases (exact match, partial match, casing differences).
*   [ ] Validate error semantics (e.g., what happens if the payload is malformed vs. if a single contact fails during processing).

**To Docs:**
*   [ ] Document the asynchronous API pattern, explicitly explaining the `202 Accepted` response and the polling URL.
*   [ ] Provide developer examples of the request payload, including how to specify duplicate detection rules.
*   [ ] Document all possible values for the `status` field and standard error codes.
