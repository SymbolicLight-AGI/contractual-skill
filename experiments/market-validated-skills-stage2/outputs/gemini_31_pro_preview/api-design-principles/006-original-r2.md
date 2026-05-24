# API Contract Handoff: Bulk Contact Import

This document serves as the API design handoff for the Bulk Contact Import feature. It outlines the design decisions based on known requirements and highlights specific review areas for Security, Frontend, QA, and Documentation teams. 

*[Uncertainty Note: The exact draft API specification (e.g., OpenAPI spec or GraphQL schema), chosen API style, and existing authentication strategy were not provided. The below assumes a standard RESTful approach for asynchronous processing. Please substitute with exact draft details where applicable.]*

---

## 1. Consumers, Use Cases, and Constraints
*   **Consumers:** Frontend application. *[Uncertain: Are there third-party or mobile consumers for this endpoint?]*
*   **Use Cases:** 
    *   Upload a bulk list of contacts.
    *   Detect and handle duplicate contacts.
    *   Display real-time or polled progress of the import to the user.
*   **Constraints:** 
    *   **Asynchronous:** Processing large lists requires background jobs to prevent timeouts.
    *   **PII Handling:** Contacts contain Personally Identifiable Information, requiring strict security and compliance measures.

## 2. API Style and Resource Modeling
**Style:** REST *[Uncertain: Confirm if GraphQL is preferred by the team]*

**Resources:**
*   `POST /v1/contacts/imports`
    *   **Purpose:** Initiates the async import job.
    *   **Payload:** Multipart form data (file upload) or JSON array of contacts.
    *   **Response:** `202 Accepted` with a `jobId` and a `Location` header pointing to the status endpoint.
*   `GET /v1/contacts/imports/{jobId}`
    *   **Purpose:** Retrieves the current progress state and results.
    *   **Response:** Job status (`PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`), `progress_percentage`, and a summary of `duplicates_detected`.

## 3. Errors, Versioning, Pagination, and Auth Strategy
*   **Errors:** Standardized RFC 7807 Problem Details.
    *   `400 Bad Request`: Invalid file format or schema validation failure.
    *   `401 Unauthorized` / `403 Forbidden`: Missing or insufficient privileges.
    *   `413 Payload Too Large`: File exceeds maximum allowed size.
    *   `422 Unprocessable Entity`: File parsed, but data violates business rules.
*   **Versioning:** URI versioning (`/v1/`) to ensure future contract changes do not break existing consumers.
*   **Pagination:** *[Uncertain: If the duplicate detection returns a massive list of conflicting records, pagination (e.g., cursor-based) will be required on a sub-resource like `GET /v1/contacts/imports/{jobId}/duplicates`]*
*   **Auth Strategy:** Strict Bearer Token (OAuth2/JWT) requiring specific contact-write scopes.

---

## 4. Downstream Reviewer Handoff & Validation

### 🔒 Security Review
*   **PII Data in Transit/Rest:** Verify that the payload encryption and temporary storage of the import file meet compliance standards (e.g., GDPR, SOC2).
*   **Authorization:** Validate that the endpoint correctly enforces tenant/user isolation so users cannot poll `jobId`s belonging to other accounts.
*   **Rate Limiting:** Review the rate limits on the `POST` endpoint to prevent denial-of-service (DoS) via massive file uploads.

### 💻 Frontend Review
*   **Async Polling:** The `POST` request will return a `202 Accepted`. You will need to poll the `GET` endpoint using the returned `jobId`. *[Uncertain: Does the frontend prefer WebSockets/Server-Sent Events (SSE) for progress updates instead of polling?]*
*   **Progress States:** Ensure your UI can handle the following states: `PENDING`, `PROCESSING` (with `progress_percentage`), `COMPLETED`, and `FAILED`.
*   **Duplicate Handling:** Review the response schema for duplicates. How should the UI present conflicts (e.g., overwrite prompts vs. skip notifications)?

### 🧪 QA Review
*   **Edge Cases to Test:**
    *   Malformed files (e.g., CSVs with missing headers, invalid JSON).
    *   Files exceeding the maximum payload size.
    *   Network interruptions during the upload.
    *   100% duplicate uploads vs. partial duplicate uploads.
*   **Concurrency:** Test behavior when a user initiates multiple bulk imports simultaneously.

### 📝 Documentation Review
*   **API Reference:** Ensure the `202 Accepted` pattern is clearly documented, as it differs from standard synchronous `200 OK` or `201 Created` responses.
*   **Examples:** Provide clear cURL and response payload examples for both the initial `POST` and the subsequent `GET` polling requests.
*   **Error Codes:** Document the specific error codes related to duplicate detection so developers know how to programmatically resolve conflicts.
