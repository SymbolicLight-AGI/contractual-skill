## Implementation Handoff: Notification Preferences

### Status

- **Fact:** The design for notification preferences has been validated.
- **Fact:** Users can choose notification channels per event type:
  - Email
  - SMS
  - In-app notifications
- **Fact:** This handoff is implementation-facing, but does **not** include code.
- **Open questions remain:**
  - SMS vendor limits
  - Unsubscribe / opt-out compliance requirements

---

## Goal

Implement user-configurable notification preferences so that users can control which channels they receive notifications on for each supported event type.

Example:

| Event Type | Email | SMS | In-app |
|---|---:|---:|---:|
| Account security alert | Enabled | Enabled | Enabled |
| Weekly digest | Enabled | Disabled | Enabled |
| Comment reply | Disabled | Disabled | Enabled |

---

## Scope

### In Scope

- Store notification preferences per user.
- Support channel-level preferences per notification event type.
- Allow users to update preferences.
- Ensure notification delivery checks preferences before sending.
- Preserve safe defaults for new users and newly introduced event types.
- Include auditability or traceability where needed for compliance-sensitive changes.
- Account for SMS opt-out and unsubscribe constraints before production SMS delivery.

### Out of Scope

- Implementing a new SMS vendor integration unless already planned separately.
- Finalizing compliance rules without legal/product confirmation.
- Replacing the entire notification delivery system.
- Writing production code in this handoff.

---

## Proposed Data Model

### Core Concepts

#### Notification Event Type

Represents a kind of notification the system can send.

Examples:

- `account_security_alert`
- `password_changed`
- `comment_reply`
- `billing_reminder`
- `weekly_digest`

Each event type should define:

- Stable identifier
- Human-readable name
- Description
- Supported channels
- Default channel settings
- Whether any channel is mandatory or system-controlled

#### Notification Channel

Supported channels:

- `email`
- `sms`
- `in_app`

#### User Notification Preference

Stores whether a user wants a given channel enabled for a given event type.

Conceptually:

```text
user_id
event_type
channel
enabled
updated_at
```

Optional fields depending on compliance/audit needs:

```text
updated_by
source
reason
created_at
version
```

---

## Recommended Storage Approach

### Recommended Direction

Use a normalized preferences table with one row per:

```text
user + event_type + channel
```

This is preferable to storing a single JSON blob because it is easier to query, audit, update partially, and enforce constraints over time.

### Example Logical Schema

```text
notification_preferences
- id
- user_id
- event_type
- channel
- enabled
- created_at
- updated_at
```

Recommended uniqueness constraint:

```text
unique(user_id, event_type, channel)
```

Recommended indexes:

```text
index(user_id)
index(user_id, event_type)
index(event_type, channel)
```

---

## Preference Resolution Rules

When deciding whether to send a notification, the system should resolve preferences in this order:

1. Check whether the notification event type supports the requested channel.
2. Check whether the user has an explicit preference.
3. If no explicit preference exists, use the event type default.
4. Apply global compliance or suppression rules.
5. Send only if the final resolved result allows it.

### Important

Compliance and suppression rules should override user preferences.

For example:

- If a user has opted out of SMS globally, SMS should not be sent even if the event-level SMS preference is enabled.
- If an email address is bounced or suppressed, email should not be sent even if enabled.
- If a notification is legally required or security-critical, product/legal should decide whether users can disable it.

---

## API / Service Responsibilities

### Preference Management

Implementation should expose behavior equivalent to:

#### Read Preferences

Retrieve a user’s notification preferences grouped by event type and channel.

Should include:

- Event type
- Display name
- Description
- Supported channels
- Current resolved preference per channel
- Whether the preference is user-configurable
- Default value if no explicit preference exists

#### Update Preferences

Allow users to update one or more preferences.

Update should validate:

- The event type exists.
- The channel exists.
- The event type supports the channel.
- The preference is user-configurable.
- SMS changes comply with opt-in / opt-out rules.

---

## Notification Sending Flow

Before sending a notification:

1. Notification producer emits or requests a notification for an event type.
2. Notification service determines candidate channels.
3. Preference resolver loads user preferences.
4. Resolver applies event defaults.
5. Resolver applies suppression/compliance rules.
6. Notification is sent only through allowed channels.
7. Delivery attempt is logged.

### Example Flow

```text
Event: comment_reply
User: 123

Candidate channels:
- email
- in_app

User preferences:
- email: disabled
- in_app: enabled

Result:
- Do not send email
- Create in-app notification
```

---

## Defaults

### Recommended Default Strategy

Use explicit defaults per event type and channel.

Example:

```text
account_security_alert:
  email: enabled
  sms: disabled unless verified/opted-in
  in_app: enabled

weekly_digest:
  email: enabled
  sms: disabled
  in_app: disabled

comment_reply:
  email: enabled
  sms: disabled
  in_app: enabled
```

### New Users

For new users, do not necessarily create all preference rows upfront.

Recommended approach:

- Resolve missing rows using defaults.
- Create explicit rows only when the user changes a setting.

This reduces storage overhead and makes future event additions easier.

### New Event Types

When adding a new event type:

- Define supported channels.
- Define default preferences.
- Define whether the event is user-configurable.
- Confirm compliance implications, especially for SMS/email.

---

## UI Requirements

The notification preferences UI should allow users to:

- View notification event types.
- See supported channels for each event type.
- Enable or disable channels where allowed.
- Understand disabled or locked preferences.
- Save changes.
- Receive success or error feedback.

### Suggested UI Structure

```text
Notification Preferences

Security
[ ] Email   [ ] SMS   [ ] In-app

Account Activity
[ ] Email   [ ] SMS   [ ] In-app

Product Updates
[ ] Email   [ ] SMS   [ ] In-app
```

Some preferences may be locked:

```text
Security alert
[x] Email - Required
[x] In-app - Required
[ ] SMS - Optional
```

---

## Compliance and Safety Requirements

### SMS

**Open question:** SMS vendor limits are not yet confirmed.

Implementation should not assume unlimited SMS throughput or unrestricted SMS behavior.

Before enabling SMS in production, confirm:

- Vendor rate limits
- Per-recipient frequency limits
- Country/region restrictions
- Opt-in requirements
- Opt-out handling
- STOP/START keyword behavior
- Whether transactional and marketing SMS are handled differently
- Message template requirements, if any

### Unsubscribe / Opt-Out

**Open question:** unsubscribe compliance requirements are not yet finalized.

Before production launch, confirm:

- Whether email unsubscribe is required per notification category.
- Whether security or transactional notifications are exempt.
- Whether global unsubscribe is required.
- Whether SMS opt-out must override event-level preferences.
- Whether audit records are required for preference changes.
- Required copy for unsubscribe links and SMS opt-out messaging.

### Recommended Guardrail

Treat compliance suppression as a separate layer from user preferences.

User preference:

```text
“I want SMS for billing reminders.”
```

Compliance suppression:

```text
“SMS cannot be sent because the user opted out globally.”
```

The final send decision should respect both.

---

## Reliability Requirements

Implementation should consider:

- Preference reads should be reliable and low-latency.
- Notification sending should fail safe where appropriate.
- If preferences cannot be loaded, define fallback behavior.

### Recommended Fallback

For non-critical notifications:

```text
If preferences cannot be resolved, do not send external notifications.
```

For critical/security notifications:

```text
Use product-approved default behavior.
```

This needs confirmation for each critical event type.

---

## Privacy and Security Requirements

- Users should only access and modify their own preferences.
- Admin or support changes, if allowed, should be audited.
- Avoid exposing internal event identifiers unnecessarily in the UI.
- Validate all event/channel updates server-side.
- Do not allow users to enable unsupported channels.
- Do not expose phone numbers or email addresses unless required by the UI.
- SMS should require verified phone number and valid opt-in status.

---

## Testing Guidance

### Unit Tests

Cover:

- Preference resolution with explicit user preference.
- Preference resolution using defaults.
- Unsupported channel rejection.
- Unknown event type rejection.
- Locked/non-configurable preference rejection.
- SMS disabled when user is globally opted out.
- Email disabled when user is unsubscribed/suppressed.
- New event types using defaults correctly.

### Integration Tests

Cover:

- User updates preference and notification sending respects it.
- Preference API returns resolved preferences.
- Notification sender checks preferences before sending.
- Compliance suppression overrides enabled preference.
- Missing preference rows fall back to defaults.

### Edge Cases

- User has no preferences saved.
- Event type added after user account creation.
- Channel removed from an event type.
- User disables all channels for an event.
- User attempts to enable SMS without verified phone number.
- SMS vendor unavailable.
- Preference update race conditions.
- Bulk update partially fails.

---

## Migration / Rollout Notes

### Suggested Rollout

1. Add event type configuration.
2. Add storage for explicit user preferences.
3. Implement preference resolver.
4. Update notification sending to call resolver before dispatch.
5. Add user-facing preference management UI/API.
6. Add compliance suppression layer.
7. Enable channels gradually, especially SMS.
8. Monitor send volume, opt-outs, failures, and user changes.

### Backward Compatibility

If notifications already exist, implementation should define current defaults to preserve expected behavior.

Example:

- If users currently receive comment reply emails, default email for `comment_reply` should likely remain enabled unless product decides otherwise.

---

## Observability

Track:

- Preference updates by event type/channel.
- Notification send decisions:
  - Sent
  - Skipped due to preference
  - Skipped due to compliance suppression
  - Failed due to provider error
- SMS opt-out events.
- Email unsubscribe events.
- Rate limit failures.
- Preference API errors.

Avoid logging sensitive user data unnecessarily.

---

## Decision Log

| Decision | Rationale |
|---|---|
| Preferences are configured per user, event type, and channel | Matches validated design and gives users granular control |
| Supported channels are email, SMS, and in-app | Confirmed requirement |
| Preference resolution should use defaults when no explicit row exists | Reduces data creation and supports future event types |
| Compliance suppression should override user preferences | Required for SMS/email safety and legal compliance |
| SMS production behavior remains gated | SMS vendor limits and opt-out rules are still open |
| Implementation handoff excludes code | User requested implementation-facing handoff, not implementation |

---

## Open Questions Before Production Release

1. What are the SMS vendor limits?
   - Rate limits
   - Country restrictions
   - Template requirements
   - Throughput limits
   - Opt-in/opt-out handling

2. What unsubscribe compliance rules apply?
   - Per-category unsubscribe?
   - Global unsubscribe?
   - Transactional/security notification exemptions?
   - Required audit trail?

3. Which event types are mandatory or non-configurable?

4. What are the approved default settings for each event type/channel?

5. What should happen if preference resolution fails during notification sending?

---

## Implementation Acceptance Criteria

Implementation is ready when:

- Users can view notification preferences by event type and channel.
- Users can update configurable preferences.
- Preferences are persisted per user.
- Notification sending checks preferences before dispatch.
- Defaults apply when explicit preferences do not exist.
- Unsupported event/channel combinations are rejected.
- Compliance suppression can override preferences.
- SMS is gated behind verified opt-in/compliance checks.
- Tests cover preference resolution, updates, defaults, and suppression behavior.
- Observability exists for sends, skips, failures, and preference changes.

---

## Next Step

This handoff is ready for engineering review.

Before implementation begins, the team should resolve or explicitly gate the two remaining risks:

1. SMS vendor limits  
2. Unsubscribe / opt-out compliance requirements

If those cannot be resolved immediately, implementation can proceed behind a feature flag with SMS sending disabled until compliance and vendor constraints are confirmed.
