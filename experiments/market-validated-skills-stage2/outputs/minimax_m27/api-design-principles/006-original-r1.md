<think>The user is asking me to prepare a handoff document for a bulk contact import API. This is an API design task that involves preparing documentation/specifications for downstream teams (security, frontend, QA, and docs).

Let me break down what I need to cover based on the known facts:
1. Imports are asynchronous
2. Duplicate detection is required
3. PII is involved
4. Frontend needs progress states

I should create a comprehensive handoff document that covers:
- API overview and design decisions
- Resource modeling
- Error handling
- Authentication/Authorization
- Pagination (for large imports)
- Progress tracking mechanism
- Security considerations (especially for PII)
- Frontend integration points
- Testing considerations
- Documentation needs

Let me structure this as a proper handoff document.
</think>

# Bulk Contact Import API — Handoff Document

## 1. API Overview

| Aspect | Decision |
|--------|----------|
| **Style** | REST with async job pattern |
| **Base Path** | `/api/v1/contacts/imports` |
| **Authentication** | Bearer token (OAuth 2.0) |
| **Data Sensitivity** | PII — requires encryption at rest/transit |

---

## 2. Resource Model

### 2.1 Import Job

```
POST   /imports              → Create import job
GET    /imports/{jobId}      → Get job status
GET    /imports/{jobId}/progress → Get progress details
GET    /imports/{jobId}/report   → Get final report (duplicates, failures)
DELETE /imports/{jobId}      → Cancel in-progress job
```

### 2.2 Request Payload (Create Import)

```json
{
  "source": "csv" | "api",
  "contacts": [
    {
      "email": "user@example.com",
      "firstName": "Jane",
      "lastName": "Doe",
      "phone": "+1-555-0100",
      "customFields": {}
    }
  ],
  "options": {
    "onDuplicate": "skip" | "update" | "fail",
    "notifyOnComplete": true,
    "webhookUrl": "https://client.example.com/hooks/import"
  }
}
```

### 2.3 Response Payload (Create Import)

```json
{
  "jobId": "imp_abc123",
  "status": "queued",
  "estimatedContacts": 150,
  "createdAt": "2026-02-27T10:00:00Z",
  "statusUrl": "/api/v1/contacts/imports/imp_abc123"
}
```

---

## 3. Async & Progress States

### 3.1 Job Status Values

| Status | Description | Frontend Action |
|--------|-------------|-----------------|
| `queued` | Waiting to start | Show "Queued" badge |
| `processing` | Active import | Show progress bar + percentage |
| `completed` | All contacts processed | Show success + summary |
| `completed_with_errors` | Done but some failed | Show summary + error list |
| `failed` | Job crashed | Show retry option |
| `cancelled` | User cancelled | Show cancelled state |

### 3.2 Progress Endpoint Response

```json
{
  "jobId": "imp_abc123",
  "status": "processing",
  "progress": {
    "total": 150,
    "processed": 87,
    "successful": 82,
    "duplicates": 3,
    "failed": 2,
    "percentComplete": 58
  },
  "currentPhase": "validating" | "importing" | "deduplicating" | "finalizing"
}
```

---

## 4. Duplicate Detection

| Strategy | Behavior |
|----------|----------|
| `skip` | Skip contact, count as duplicate |
| `update` | Update existing record with new data |
| `fail` | Mark entire job as failed |

**Matching Logic:**
- Primary: Email (case-insensitive)
- Secondary: Phone number
- Fuzzy matching available via `options.fuzzyMatch: true`

---

## 5. Error Handling

### 5.1 HTTP Status Codes

| Code | Meaning |
|------|---------|
| `202 Accepted` | Job created successfully |
| `400 Bad Request` | Invalid payload |
| `401 Unauthorized` | Missing/invalid token |
| `403 Forbidden` | Insufficient permissions |
| `413 Payload Too Large` | Exceeds max batch size (10,000) |
| `429 Too Many Requests` | Rate limited |

### 5.2 Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format at row 5",
    "details": {
      "row": 5,
      "field": "email",
      "value": "not-an-email"
    }
  }
}
```

### 5.3 Job-Level Errors

```json
{
  "jobId": "imp_abc123",
  "status": "completed_with_errors",
  "summary": {
    "total": 150,
    "imported": 145,
    "duplicates": 3,
    "failed": 2
  },
  "errors": [
    {
      "row": 45,
      "reason": "Invalid phone format",
      "contact": { "email": "..." }
    }
  ]
}
```

---

## 6. Security Requirements (For Security Review)

| Concern | Mitigation |
|---------|------------|
| **PII Storage** | AES-256 encryption at rest; TLS 1.3 in transit |
| **Access Control** | Scoped tokens with `contacts:write` scope |
| **Data Retention** | Import data purged after 30 days; logs retained 90 days |
| **Audit Logging** | All import operations logged with user ID, timestamp, IP |
| **Webhook Security** | HMAC-SHA256 signature verification on callbacks |
| **Rate Limiting** | 10 imports/hour per user; 10,000 contacts/import max |

**Action Required:** Confirm encryption key rotation policy and data residency requirements.

---

## 7. Frontend Integration Points

### 7.1 Recommended UX Flow

1. **Upload** → POST `/imports` → Get `jobId`
2. **Poll** → GET `/imports/{jobId}/progress` every 2-3 seconds
3. **Display** → Progress bar + real-time counters
4. **Complete** → Show summary modal with download of failed rows
5. **Optional** → Webhook fires for background completion

### 7.2 Frontend State Mapping

```
idle → uploading → queued → processing → completed/failed
```

### 7.3 Cancellation

- Frontend calls `DELETE /imports/{jobId}` during processing
- Partial imports are rolled back (configurable via `options.rollbackOnCancel`)

---

## 8. QA Testing Checklist

### Functional
- [ ] Upload 1, 100, 10,000 contacts
- [ ] All three `onDuplicate` strategies
- [ ] Invalid email/phone validation
- [ ] Job cancellation mid-import
- [ ] Duplicate job ID returns 409

### Security
- [ ] Unauthorized requests return 401
- [ ] PII not logged in plain text
- [ ] Webhook HMAC validation works
- [ ] Rate limiting enforced

### Performance
- [ ] 10,000 contacts imports in < 60 seconds
- [ ] Progress updates every 1-2 seconds
- [ ] Memory stable under load

---

## 9. Documentation Requirements

| Topic | Priority |
|-------|----------|
| Quickstart guide with CSV template | High |
| `onDuplicate` strategy explanation | High |
| Progress polling example (code snippets) | High |
| Webhook payload reference | Medium |
| Error code glossary | Medium |
| Rate limits and quotas | Medium |
| Data retention policy | Low |

---

## 10. Open Questions for Reviewers

| # | Question | Owner |
|---|----------|-------|
| 1 | Is 30-day data retention acceptable? | Security |
| 2 | Should failed rows be downloadable as CSV? | Frontend |
| 3 | Do we support resumable imports after failure? | QA |
| 4 | What regions should data be stored in? | Security |
| 5 | Is webhook retry logic needed (3 retries, exponential backoff)? | Backend |

---

## 11. Next Steps

1. **Security:** Review encryption config and approve data handling
2. **Frontend:** Confirm polling interval and state machine
3. **QA:** Add test cases for error scenarios
4. **Docs:** Draft quickstart using attached CSV template
5. **Backend:** Finalize webhook retry policy

---

**Prepared by:** API Design  
**Date:** 2026-02-27  
**Version:** 1.0 (Draft)
