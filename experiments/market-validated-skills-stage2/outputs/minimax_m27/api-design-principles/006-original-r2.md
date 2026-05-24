# Bulk Contact Import API — Handoff Document

## Overview

| Attribute | Value |
|-----------|-------|
| **Feature** | Bulk Contact Import |
| **Processing Model** | Asynchronous |
| **Data Sensitivity** | PII (Personally Identifiable Information) |
| **Status** | Draft — Pending Review |

---

## 1. API Contract Summary

### 1.1 Endpoints

```
POST   /v1/imports              → Initiate import job
GET    /v1/imports/{jobId}      → Get job status
GET    /v1/imports/{jobId}/contacts   → List processed contacts
DELETE /v1/imports/{jobId}      → Cancel job
POST   /v1/imports/{jobId}/abort      → Abort in-progress job
```

### 1.2 Core Request/Response Shapes

#### Initiate Import
```json
// POST /v1/imports
// Request
{
  "file": "base64-encoded-csv-or-vcard",
  "fileFormat": "csv | vcard",
  "duplicatePolicy": "skip | update | error",
  "notifyWebhook": "https://example.com/import-callback"  // optional
}

// Response: 202 Accepted
{
  "jobId": "uuid-v4",
  "status": "queued",
  "createdAt": "ISO-8601",
  "estimatedContacts": 1500
}
```

#### Poll Job Status
```json
// GET /v1/imports/{jobId}
// Response
{
  "jobId": "uuid-v4",
  "status": "queued | processing | completed | failed | cancelled",
  "progress": {
    "total": 1500,
    "processed": 750,
    "imported": 720,
    "duplicates": 25,
    "failed": 5
  },
  "startedAt": "ISO-8601",
  "completedAt": "ISO-8601 | null"
}
```

#### Fetch Processed Contacts
```json
// GET /v1/imports/{jobId}/contacts?page=1&perPage=50&filter=imported
// Response
{
  "contacts": [
    {
      "id": "contact-uuid",
      "importStatus": "imported | duplicate | failed",
      "originalRow": 5,
      "failureReason": null
    }
  ],
  "pagination": {
    "page": 1,
    "perPage": 50,
    "totalItems": 1500,
    "totalPages": 30
  }
}
```

---

## 2. Duplicate Detection Strategy

| Policy | Behavior |
|--------|----------|
| `skip` | Skip duplicate, count as `duplicates` |
| `update` | Overwrite existing contact with imported data |
| `error` | Mark row as failed, include reason in response |

**Detection Keys** (in priority order):
1. Email address
2. Phone number (normalized to E.164)
3. External ID (if provided in file)

> ⚠️ **Security Note**: Email/phone normalization must be applied server-side to prevent timing attacks.

---

## 3. Security Requirements

| Concern | Mitigation |
|---------|------------|
| **PII Handling** | TLS 1.2+ required; file content held in memory only during processing, purged immediately after |
| **Access Control** | User can only query their own jobs (`/imports/{jobId}` scoped to auth token) |
| **Rate Limiting** | 5 import requests per hour per user; 100 status polls per minute |
| **Audit Trail** | All import operations logged with user ID, timestamp, IP, file hash |
| **Webhook Security** | Optional HMAC signature on callback payload (`X-Import-Signature`) |

### Required from Security Team
- [ ] Confirm PII field list (email, phone, name, address?)
- [ ] Review retention policy for uploaded files
- [ ] Validate webhook signature approach
- [ ] Check rate limit thresholds acceptable

---

## 4. Frontend Integration Guide

### 4.1 Recommended UX Flow

```
1. User uploads file
   ↓
2. POST /v1/imports → get jobId
   ↓
3. Poll GET /v1/imports/{jobId} every 2 seconds
   ↓
4. Render progress bar using progress.{total, processed, imported}
   ↓
5. On status === "completed" → fetch contacts page to display summary
```

### 4.2 Status → UI State Mapping

| Status | UI State |
|--------|----------|
| `queued` | "Preparing import..." |
| `processing` | Show progress bar with `imported` / `total` |
| `completed` | Success summary modal with counts |
| `failed` | Error banner with "View failures" CTA |

### 4.3 Error Handling

```json
// Error response format (all errors follow this shape)
{
  "error": {
    "code": "IMPORT_003",
    "message": "Duplicate detection policy violation",
    "details": {
      "conflictingContactId": "uuid",
      "conflictKey": "email"
    }
  }
}
```

**Error Codes for Frontend**:

| Code | Meaning | User Message |
|------|---------|--------------|
| `IMPORT_001` | Invalid file format | "File format not supported. Use CSV or vCard." |
| `IMPORT_002` | File too large | "File exceeds 10MB limit." |
| `IMPORT_003` | Duplicate conflict | "Duplicate found (see details)" |
| `IMPORT_004` | Malformed row | "Row {n}: {specific issue}" |
| `IMPORT_005` | Job not found | "Import session expired" |
| `AUTH_001` | Unauthorized | "Please log in again" |

### 4.4 Required from Frontend Team
- [ ] Confirm polling interval (2s recommended, adjust if needed)
- [ ] Request additional progress metadata (e.g., current file row?)
- [ ] Clarify success/failure report display requirements

---

## 5. QA Test Scenarios

### 5.1 Happy Path
- [ ] Import CSV with 1000 contacts → verify 1000 processed
- [ ] Import vCard with contacts having special characters (ü, é, 😀)
- [ ] Completed job shows accurate `progress` counts

### 5.2 Duplicate Scenarios
- [ ] Email match → correctly categorized per policy
- [ ] Phone match (varied formats: +1-555, (555) 555, 5555) → normalized correctly
- [ ] Both email + phone match → email takes priority

### 5.3 Error Handling
- [ ] Malformed CSV → 10 failed rows, 990 imported
- [ ] File > 10MB → immediate 400 error
- [ ] Auth token expired mid-import → job remains, auth error on poll
- [ ] Network interruption during upload → retryable error returned

### 5.4 Concurrency
- [ ] User initiates 2nd import while 1st is processing → both succeed
- [ ] 100 concurrent users importing → no job ID collisions

### 5.5 Security
- [ ] User A cannot access User B's job via direct API call
- [ ] PII not logged in plaintext
- [ ] Malformed webhook URL → import still succeeds (webhook is optional)

---

## 6. Documentation Requirements

### 6.1 Docs Sections to Author

1. **Quick Start** — Upload file → poll status → done (5-step tutorial)
2. **API Reference** — Full endpoint specs with examples
3. **Error Codes** — Lookup table with troubleshooting
4. **Best Practices** — Batch size recommendations, webhook setup
5. **Rate Limits** — Document current limits and retry guidance

### 6.2 Example Snippets Needed

```bash
# Initiate import
curl -X POST https://api.example.com/v1/imports \
  -H "Authorization: Bearer {token}" \
  -d '{"file": "...", "fileFormat": "csv", "duplicatePolicy": "skip"}'

# Poll status
curl https://api.example.com/v1/imports/{jobId} \
  -H "Authorization: Bearer {token}"
```

### 6.3 Required from Docs Team
- [ ] Confirm preferred format (OpenAPI 3.0 spec or manual docs?)
- [ ] Identify any missing example use cases
- [ ] Request changelog for future versions

---

## 7. Open Questions

| # | Question | Owner | Blocking? |
|---|----------|-------|-----------|
| 1 | Max file size limit — 10MB or configurable? | Backend | No |
| 2 | Support for partial contact fields? | Product | Yes |
| 3 | Retention period for import jobs? | Security | Yes |
| 4 | Webhook retry policy (retries, TTL)? | Backend | No |
| 5 | Bulk delete of imported contacts? | Product | No |

---

## 8. Versioning Plan

- **Initial Version**: `/v1/imports`
- **Breaking changes** require `/v2/` namespace with 6-month deprecation window
- **Non-breaking additions** (new fields, optional params) can be added to `/v1/`

---

## Sign-Off Checklist

| Reviewer | Status | Comments |
|----------|--------|----------|
| Security | ⬜ Pending | |
| Frontend | ⬜ Pending | |
| QA | ⬜ Pending | |
| Docs | ⬜ Pending | |
| Backend (Owner) | ✅ Approved | |

---

**Questions for Reviewers?**  
Reply to this thread with concerns or approval. Blockers marked above require resolution before implementation begins.
