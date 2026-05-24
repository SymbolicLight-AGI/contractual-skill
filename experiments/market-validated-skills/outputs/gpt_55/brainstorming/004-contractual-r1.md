## Implementation Handoff: Notification Preferences

### Status

**Fact:** The design for notification preferences has been validated.  
**Fact:** Users can choose notification channels per event type:

- Email
- SMS
- In-app notifications

**Fact:** This handoff is implementation-facing and should not include code.  
**Open questions remain:**

1. SMS vendor limits
2. Unsubscribe / compliance requirements

---

## Goal

Implement user-configurable notification preferences so users can control which channels they receive for each supported event type.

Example:

| Event Type | Email | SMS | In-App |
|---|---:|---:|---:|
| Account security alert | Enabled | Enabled | Enabled |
| Product update | Enabled | Disabled | Enabled |
| Marketing announcement | Disabled | Disabled | Enabled |

---

## Scope

### In Scope

- Store notification preferences per user.
- Support preferences by event type and channel.
- Allow users to enable or disable:
  - Email
  - SMS
  - In-app notifications
- Use preferences when deciding whether to send a notification.
- Provide defaults for new users or newly introduced event types.
- Preserve required/system-critical notifications where applicable.
- Prepare for SMS compliance and vendor constraints.

### Out of Scope

- Implementing the SMS vendor integration itself, unless already planned elsewhere.
- Finalizing legal/compliance copy for unsubscribe flows.
- Building advanced notification scheduling, batching, or quiet hours unless separately approved.
- Reworking the full notification delivery system beyond what is needed to honor preferences.

---

## Proposed Implementation Areas

### 1. Data Model

Add or confirm a model that represents notification preferences by:

- User
- Event type
- Channel
- Enabled/disabled state

Conceptually:

```text
NotificationPreference
- user_id
- event_type
- channel
- enabled
- created_at
- updated_at
```

Possible `channel` values:

```text
email
sms
in_app
```

Possible `event_type` values should come from a controlled enum or registry, for example:

```text
security_alert
billing_update
comment_reply
product_update
marketing
```

### Assumption

The system already has identifiable notification event types or can introduce a central event-type registry.

### Risk

If event types are hardcoded in multiple services, preference enforcement may become inconsistent.

---

## 2. Defaults

Define default preferences for:

- New users
- Existing users during migration
- New event types added in the future

Recommended default behavior:

| Event Category | Email | SMS | In-App |
|---|---:|---:|---:|
| Security / account-critical | Enabled | Enabled if phone verified | Enabled |
| Transactional / billing | Enabled | Optional / disabled by default | Enabled |
| Product activity | Enabled | Disabled | Enabled |
| Marketing | Disabled unless opted in | Disabled unless opted in | Optional |

### Assumption

Compliance-sensitive channels such as SMS and marketing email should default to opt-in only where required.

### Open Question

Do any event types legally or operationally need to bypass user preferences, such as security alerts or required account notices?

---

## 3. Preference Management UI/API

Implementation should expose a way for users to view and update preferences.

### Required capabilities

- Fetch current preferences for the authenticated user.
- Update preferences for one or more event/channel combinations.
- Prevent disabling mandatory notifications if applicable.
- Display unavailable channels clearly, such as SMS when no verified phone number exists.

### Suggested API Shape

This is illustrative, not final code.

```http
GET /notification-preferences
```

Returns preferences grouped by event type.

```http
PUT /notification-preferences
```

Updates selected channel preferences.

Example conceptual payload:

```json
{
  "preferences": [
    {
      "eventType": "billing_update",
      "channels": {
        "email": true,
        "sms": false,
        "inApp": true
      }
    }
  ]
}
```

### Risk

Bulk updates need clear validation behavior if one preference is invalid but others are valid.

Recommended decision: reject the whole request with validation errors unless the product specifically wants partial success.

---

## 4. Notification Sending Behavior

Before sending a notification, the delivery system should evaluate:

1. What event type is this?
2. What channels are available for this notification?
3. What preferences has the user configured?
4. Is the notification mandatory?
5. Is the channel legally allowed and technically available?
6. Should the notification be sent on each channel?

Conceptual decision order:

```text
Notification event created
→ Determine event type
→ Determine eligible channels
→ Load user preferences
→ Apply mandatory/compliance rules
→ Send only through allowed channels
→ Record delivery attempts/results
```

### Important Rule

Preferences should be enforced at the notification orchestration layer before dispatching to email, SMS, or in-app providers.

### Risk

If individual channel senders enforce preferences independently, behavior may diverge between channels.

---

## 5. SMS-Specific Considerations

### Open Question: SMS Vendor Limits

Implementation should confirm:

- Rate limits
- Daily/monthly message caps
- Per-recipient throttling
- Retry rules
- Error codes
- Cost controls
- Region or carrier restrictions
- Phone verification requirements

### Open Question: SMS Unsubscribe Compliance

Implementation should confirm:

- Whether users must be able to unsubscribe by replying `STOP`
- Whether opt-in records must be stored
- Whether SMS consent is required separately from general notification preferences
- Whether transactional SMS and marketing SMS need separate handling
- Required copy for opt-in, opt-out, and confirmation messages
- Regional compliance requirements

### Recommendation

Do not treat the notification preference toggle alone as sufficient SMS consent until compliance is confirmed.

---

## 6. Compliance and Unsubscribe Rules

Implementation should support a compliance layer that can override user preference settings.

Examples:

```text
User preference says SMS enabled
BUT user has opted out via STOP
→ Do not send SMS
```

```text
User preference says marketing email enabled
BUT user has globally unsubscribed from marketing
→ Do not send marketing email
```

```text
User preference says email disabled
BUT notification is legally required account notice
→ Send if policy allows/mandates
```

### Assumption

There may already be existing unsubscribe or consent records for email marketing.

### Risk

If preferences and unsubscribe records are stored separately, the system needs a clear precedence model.

Recommended precedence:

1. Legal/compliance suppression
2. Mandatory notification rules
3. User notification preferences
4. Channel availability
5. Provider/vendor constraints

---

## 7. Migration Plan

For existing users:

1. Create default preferences for all supported event types.
2. Respect existing unsubscribe/marketing opt-out settings.
3. Respect existing SMS consent status if available.
4. Avoid unexpectedly enabling SMS for users without explicit consent.
5. Backfill preferences lazily or through a migration job.

### Recommendation

Use conservative defaults for SMS and marketing channels.

---

## 8. Observability and Auditing

Implementation should include logging or tracking for:

- Preference changes
- Who changed the preference: user, admin, migration, system
- Notification suppression reason
- Channel delivery attempt
- Channel delivery failure
- Compliance suppression, such as SMS opt-out

Useful suppression reasons:

```text
user_preference_disabled
channel_unavailable
missing_verified_phone
sms_opted_out
email_unsubscribed
mandatory_notification
vendor_rate_limited
```

### Risk

Without suppression reasons, support and debugging will be difficult.

---

## 9. Testing Guidance

### Unit Tests

Cover:

- Preference lookup by user, event type, and channel
- Default preference resolution
- Mandatory notification override behavior
- Missing preference fallback behavior
- SMS disabled when no verified phone number exists
- Compliance suppression taking precedence over preferences

### Integration Tests

Cover:

- Updating preferences through the API/UI
- Sending notifications only through enabled channels
- Existing unsubscribe state suppresses notifications
- New event type receives default preferences
- Migration behavior for existing users

### Edge Cases

- User has no preference row yet
- User disables all channels for an event
- Event type is unknown
- Channel is unavailable
- SMS vendor rejects delivery
- User opts out via SMS after enabling SMS in preferences
- Admin/system-generated mandatory notification

---

## Recommended Implementation Sequence

1. Confirm event type registry and channel enum.
2. Confirm compliance precedence rules.
3. Add or update data model for preferences.
4. Define default preferences.
5. Implement preference retrieval/update API.
6. Add UI for managing preferences.
7. Enforce preferences in notification orchestration.
8. Add suppression/audit logging.
9. Add migration/backfill for existing users.
10. Validate SMS-specific behavior after vendor/compliance questions are resolved.

---

## Decision Log

| Decision | Status | Rationale |
|---|---|---|
| Preferences are per user, per event type, per channel | Confirmed | Matches validated design |
| Supported channels are email, SMS, and in-app | Confirmed | Matches validated design |
| Preferences should be enforced before channel dispatch | Recommended | Keeps behavior consistent across channels |
| SMS should not be enabled without confirmed consent/compliance | Recommended pending confirmation | Reduces compliance risk |
| Defaults should be conservative for SMS and marketing | Recommended | Avoids accidental opt-in behavior |
| Suppression reasons should be logged | Recommended | Improves debugging, support, and compliance auditability |

---

## Open Questions Before Implementation Starts

1. What SMS vendor will be used, and what are its rate limits, retry rules, and regional constraints?
2. What unsubscribe and consent rules apply to SMS?
3. Are any notification event types mandatory and not user-disableable?
4. Are there existing email unsubscribe or marketing consent systems that must take precedence?
5. Should preference updates be atomic, or can partial updates succeed?
6. What are the exact event types for the first implementation release?

---

## Implementation Readiness

This is ready for engineering estimation and technical planning with two caveats:

- SMS implementation should remain gated until vendor limits are known.
- SMS and marketing-related behavior should remain gated until unsubscribe and compliance requirements are confirmed.

## Next Step

Hand this to implementation with the open questions called out as blockers or pre-implementation checks, especially for SMS vendor behavior and unsubscribe compliance.
