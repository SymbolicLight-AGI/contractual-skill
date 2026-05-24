### 1. Design Summary
The proposed API contract facilitates asynchronous bulk contact imports. It is designed to handle long-running import processes, enforce duplicate detection, securely process Personally Identifiable Information (PII), and expose lifecycle states to allow frontend consumers to track import progress. 

*Uncertainty Note:* The exact authentication model, duplicate detection rules, and specific PII fields were not provided in the task. The design below uses illustrative assumptions that must be finalized by the respective teams.

### 2. Proposed API Shape (Illustrative)
Since the exact draft schema was not provided, the following is an illustrative RESTful shape based on the known facts:

**Initiate Import**
*   **Endpoint:** `POST /v1/contacts/bulk-imports`
*   **Request:** Contains the bulk payload (e.g., JSON array or file upload reference).
*   **Response:** `202 Accepted`
*   **Body:** Returns an `import_id` and a `status` of `PENDING`.

**Check Import Progress**
*   **Endpoint:** `GET /v1/contacts/bulk-imports/{import_id}`
*   **Response:** `200 OK`
*   **Body:** 
    ```json
    {
      "import_id": "abc-123",
      "status": "PROCESSING", 
      "progress": {
        "total_records": 1000,
        "processed_records": 450,
        "duplicates_detected": 12
      },
      "created_at": "2023-10-27T10:00:00Z"
    }
    ```
*   **Lifecycle States:** `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`, `PARTIAL_SUCCESS`.

### 3. Key Tradeoffs
*   **Asynchronous Polling vs. Webhooks/WebSockets:** The design assumes the frontend will poll the `GET` endpoint for progress states. This is simpler to implement but may increase read load on the API. WebSockets would provide real-time updates but require higher infrastructure complexity.
*   **Duplicate Handling (Fail vs. Skip):** It is currently undefined whether a duplicate fails the entire batch or if the API skips duplicates and continues. A `PARTIAL_SUCCESS` state is proposed to handle skipped duplicates, trading strict data rejection for a better user experience.
*   **Payload Size vs. Pagination:** For massive imports, accepting a direct JSON payload might cause memory issues. A tradeoff to consider is requiring a pre-signed URL upload first, though this adds friction to the developer experience.

### 4. Risks and Human Gates
*   **Security Risk (PII):** Bulk contact data inherently contains PII. There is a risk of PII leaking into standard application logs, error responses, or being exposed to unauthorized users via the `GET` endpoint.
*   **Operational Risk:** High-frequency polling from the frontend could overwhelm the database if the progress state is not cached.
*   **Human Gates:** 
    *   **Security Approval:** Required for PII handling, data retention policies on the imported files, and authorization boundaries for the `GET` endpoint.
    *   **Product/Frontend Approval:** Required for public API commitments regarding the progress state machine and duplicate resolution behavior.

### 5. Verification Checklist
- [ ] **Method/Resource Consistency:** Ensure `POST` returns `202 Accepted` and `GET` is used for idempotent status checks.
- [ ] **Schema Clarity:** Verify that the progress state enums are strictly defined and documented.
- [ ] **Error Handling:** Ensure validation errors (e.g., malformed files) are returned synchronously on the `POST`, while processing errors are returned asynchronously via the `GET` status.
- [ ] **Auth Boundary:** Verify that users can only request the status of `import_id`s they own or have tenant access to.
- [ ] **Idempotency:** Ensure retrying the same bulk import payload (e.g., via an `Idempotency-Key` header) does not create duplicate jobs.

---

### Downstream Handoff Notes

**To Security:**
*   **Action Required:** Review the PII handling boundary. 
*   **Focus Areas:** Ensure the bulk payload is encrypted in transit and at rest during the async processing phase. Verify that PII is stripped from any asynchronous processing logs or error messages. Confirm the authorization model prevents IDOR (Insecure Direct Object Reference) on the `GET /bulk-imports/{import_id}` endpoint.

**To Frontend:**
*   **Action Required:** Review the asynchronous polling contract and progress states.
*   **Focus Areas:** Validate if the proposed lifecycle states (`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`, `PARTIAL_SUCCESS`) meet the UI requirements for progress bars. Confirm the acceptable polling frequency (e.g., every 3-5 seconds) and handling of rate-limit (`429 Too Many Requests`) responses.

**To QA:**
*   **Action Required:** Define contract and integration tests.
*   **Focus Areas:** Test the asynchronous state transitions. Verify duplicate detection logic (e.g., exact match vs. fuzzy match, depending on business rules). Ensure idempotency works for the `POST` endpoint. Validate that malformed payloads are rejected synchronously before a job is created.

**To Docs (Developer Experience):**
*   **Action Required:** Draft developer-facing examples.
*   **Focus Areas:** Document the asynchronous pattern clearly, as consumers might expect a synchronous response. Provide code snippets demonstrating how to initiate the import, extract the `import_id`, and implement a polling loop to check for completion. Document the exact duplicate detection rules once finalized.
