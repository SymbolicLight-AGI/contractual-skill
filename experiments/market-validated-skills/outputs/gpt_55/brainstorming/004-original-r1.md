Below is an implementation-facing handoff draft. I’m not implementing or modifying behavior here; this is a design-to-implementation handoff.

---

# Implementation Handoff: Notification Preferences

## Understanding Summary

- Users can configure notification preferences per event type.
- For each supported event type, users may choose one or more delivery channels:
  - Email
  - SMS
  - In-app
- Preferences determine whether a notification should be sent through each channel when an event occurs.
- The goal is to give users granular control over how they receive notifications.
- The design has already been validated.
- Open questions remain around SMS vendor limits and unsubscribe/compliance behavior.
- This handoff is intended to guide implementation, not provide code.

---

## Assumptions

The following assumptions should be verified before or during implementation planning:

1. Notification preferences are user-specific.
2. Event types are known and controlled by the application.
3. Users may enable multiple channels for the same event type.
4. If a user has no explicit preference for an event type, the system will use a defined default.
5. Email, SMS, and in-app notifications may have different delivery pipelines.
6. In-app notifications do not require external vendor compliance handling in the same way SMS/email may.
7. SMS sending may be subject to vendor rate limits, regional restrictions, consent requirements, or unsubscribe rules.
8. Unsubscribe/compliance behavior is not fully finalized and must be resolved before production SMS rollout.

---

## Open Questions / Blockers

### 1. SMS Vendor Limits

Unresolved:

- Which SMS provider will be used?
- What are the provider’s rate limits?
- Are there per-user, per-number, per-region, or account-wide sending limits?
- What happens when the limit is exceeded?
  - Drop?
  - Retry later?
  - Queue?
  - Fall back to another channel?
- Are there cost controls or throttling requirements?

### 2. SMS Unsubscribe Compliance

Unresolved:

- How will STOP / START / HELP messages be handled?
- Does the SMS provider manage unsubscribe state, or must the application store it?
- If a user unsubscribes from SMS, should that override all application-level SMS preferences?
- Should users be able to re-enable SMS in-app after unsubscribing, or only by texting START?
- Are there jurisdiction-specific compliance requirements?

These should be resolved before enabling SMS notifications in production.

---

## Decision Log

| Decision | Alternatives Considered | Rationale |
|---|---|---|
| Support notification preferences per event type | Global notification preferences only | Per-event preferences give users finer control and match the confirmed design. |
| Support email, SMS, and in-app channels | Single-channel notification model | Users need channel-specific control. |
| Allow preferences per channel per event type | One preference per event type regardless of channel | Users may want different delivery methods depending on event importance. |
| Treat SMS compliance as an implementation blocker/risk | Assume SMS behaves like email/in-app | SMS has vendor, legal, and unsubscribe constraints that must be explicitly handled. |
| Prepare handoff before implementation | Proceed directly to code | Open questions remain, and implementation should not start without documented risks and ownership. |

---

# Proposed Implementation Plan

## Phase 1: Data Model and Preference Storage

Define a durable representation for user notification preferences.

Likely entities:

- User
- Event type
- Notification channel
- Preference state

Example conceptual shape:

```text
user_notification_preferences
- user_id
- event_type
- channel
- enabled
- created_at
- updated_at
```

Recommended constraints:

- Unique preference per `user_id + event_type + channel`
- Valid channel values limited to:
  - `email`
  - `sms`
  - `in_app`
- Valid event types should come from an application-owned enum or registry.

Implementation should also define default behavior for missing preferences.

Example default options:

1. Default all channels off unless explicitly enabled.
2. Default low-risk channels on, such as in-app.
3. Use product-defined defaults per event type.

This default behavior should be confirmed before implementation.

---

## Phase 2: Preference Management API / Service Layer

Add a service boundary for reading and updating notification preferences.

Expected capabilities:

- Fetch all preferences for a user.
- Fetch preferences for a user by event type.
- Update preferences for one event type.
- Update preferences for one channel.
- Validate that event type and channel are supported.
- Apply defaults when explicit preferences do not exist.

Important behavior:

- Updates should be idempotent.
- Invalid event types should be rejected.
- Invalid channels should be rejected.
- SMS preference changes may need additional checks once compliance behavior is finalized.

Recommended ownership:

- A dedicated notification preference service/module should own preference reads and writes.
- Notification sending code should consume preferences through this service rather than querying storage directly.

---

## Phase 3: Notification Dispatch Integration

Update the notification dispatch flow to check preferences before sending.

Conceptual flow:

```text
Event occurs
→ Resolve notification event type
→ Identify recipient user(s)
→ Load user preferences for event type
→ Determine enabled channels
→ Apply channel-specific eligibility checks
→ Dispatch notification through allowed channels
```

Channel-specific checks:

### Email

- User has a valid email address.
- Email channel is enabled for the event type.
- Email unsubscribe rules, if applicable, are respected.

### SMS

- User has a valid phone number.
- SMS channel is enabled for the event type.
- User has SMS consent.
- User has not unsubscribed.
- SMS vendor/rate-limit rules allow send.

### In-app

- In-app channel is enabled for the event type.
- Notification is stored/rendered in the in-app notification system.

SMS should be treated as conditionally enabled until compliance and vendor behavior are resolved.

---

## Phase 4: Defaults and Migration

If existing users do not yet have notification preferences, implementation needs a defaulting strategy.

Recommended approach:

- Do not eagerly create preference rows for every user/event/channel unless necessary.
- Store only explicit user overrides.
- Resolve effective preferences at read time using product-defined defaults.

Benefits:

- Less data to migrate.
- Easier to add future event types.
- Easier to change defaults for users who have not customized preferences.

Potential risk:

- Effective preference logic must be consistent across UI, APIs, and dispatch.

Mitigation:

- Centralize default resolution in the notification preference service.

---

## Phase 5: UI Integration

The UI should allow users to configure preferences by event type and channel.

Expected UI behavior:

- Display event types in a readable grouped format.
- Show toggles or checkboxes for:
  - Email
  - SMS
  - In-app
- Disable or explain unavailable channels.
- Show SMS-specific compliance messaging if required.
- Persist changes through the preference management API/service.

Important SMS behavior:

- If a user has unsubscribed from SMS externally, the UI should not silently re-enable SMS.
- The UI should explain how SMS can be re-enabled, once compliance behavior is defined.

---

## Phase 6: Testing Strategy

### Unit Tests

Cover:

- Preference creation/update.
- Preference lookup.
- Default resolution.
- Validation of event types.
- Validation of channels.
- Effective preference calculation.
- Idempotent updates.

### Integration Tests

Cover:

- Dispatch skips disabled channels.
- Dispatch sends through enabled channels.
- Multiple channels can be enabled for one event type.
- Missing preferences fall back to defaults.
- Invalid preference updates are rejected.

### Compliance / SMS-Specific Tests

Pending final SMS requirements, cover:

- SMS disabled when user has unsubscribed.
- SMS disabled when consent is missing.
- SMS send blocked or queued when vendor limits are reached.
- STOP/START behavior if application-owned.

### Regression Tests

Cover:

- Existing notification behavior remains intact where preferences are not configured.
- Existing users receive intended default behavior.

---

## Key Risks

| Risk | Impact | Mitigation |
|---|---|---|
| SMS vendor limits are unknown | Sends may fail, queue unexpectedly, or exceed limits | Resolve provider behavior before SMS production rollout. |
| SMS unsubscribe compliance is unresolved | Legal/compliance risk | Treat as blocker for SMS enablement. |
| Defaults are not clearly defined | Users may receive too many or too few notifications | Confirm product defaults before implementation. |
| Preference logic duplicated across services | Inconsistent behavior | Centralize preference resolution. |
| Future event types become hard to manage | Maintenance burden | Use event type registry/enum and default resolution. |

---

## Implementation Readiness Checklist

Before coding starts, confirm:

- [ ] Final list of event types.
- [ ] Default preference behavior for each event type/channel.
- [ ] Whether preferences are opt-in or opt-out by default.
- [ ] Whether users can enable multiple channels per event type.
- [ ] SMS provider selection.
- [ ] SMS rate-limit behavior.
- [ ] SMS unsubscribe handling.
- [ ] SMS consent requirements.
- [ ] Email unsubscribe behavior, if applicable.
- [ ] Ownership of notification preference service/module.
- [ ] Migration/defaulting strategy for existing users.
- [ ] Testing expectations.

---

## Recommended Implementation Sequence

1. Define event type and channel registry.
2. Add notification preference persistence.
3. Add preference read/write service.
4. Add default preference resolution.
5. Add API or application-layer endpoints for managing preferences.
6. Integrate preference checks into notification dispatch.
7. Add UI preference controls.
8. Add tests for preference resolution and dispatch filtering.
9. Resolve SMS vendor and compliance behavior.
10. Enable SMS preferences only after SMS compliance rules are finalized.

---

## Explicit Implementation Boundary

Implementation should not begin for SMS production behavior until these are resolved:

- SMS vendor rate limits.
- SMS unsubscribe handling.
- SMS consent requirements.
- Whether SMS opt-out overrides in-app preferences.

Email and in-app preference implementation may proceed if defaults and event types are confirmed.

---

Ready to set up the detailed implementation plan from this handoff?
