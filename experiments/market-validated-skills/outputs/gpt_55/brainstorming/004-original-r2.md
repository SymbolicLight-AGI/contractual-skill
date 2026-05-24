Below is an implementation-facing handoff for the confirmed notification preferences design.

No code or behavior changes are included.

---

# Design Handoff: Notification Preferences

## 1. Understanding Summary

- Users can configure notification delivery preferences per event type.
- Supported channels are:
  - Email
  - SMS
  - In-app notifications
- Preferences are user-specific and event-specific.
- The system should respect user preferences before sending notifications.
- The goal is to avoid unwanted notifications while allowing users to receive important updates through preferred channels.
- The design has been validated, but SMS vendor constraints and unsubscribe/compliance handling remain unresolved.
- Implementation should not proceed for SMS production behavior until those open questions are resolved.

---

## 2. Assumptions

The following assumptions should be validated during implementation planning:

1. Each notification event type has a stable identifier, such as `comment_reply`, `billing_failed`, or `security_alert`.
2. A user may enable more than one channel for the same event type.
3. In-app notifications are always technically available unless explicitly disabled by preference.
4. Email delivery infrastructure already exists or will be integrated separately.
5. SMS delivery infrastructure may depend on vendor-specific limits, pricing, throttling, and compliance behavior.
6. Some notification types may eventually be mandatory, such as security or legal notices, but this design currently assumes all listed event types are configurable unless specified otherwise.
7. Preference changes should apply to future notifications only.
8. Historical notification records do not need to be retroactively changed when preferences are updated.
9. The system should default conservatively if a preference is missing.

---

## 3. Open Questions

These must be resolved before full implementation, especially before enabling SMS in production.

### SMS Vendor Limits

- What SMS provider will be used?
- Are there rate limits per account, user, region, or destination number?
- Are there message length limits or segment pricing concerns?
- Are there country-specific restrictions?
- What happens when SMS delivery fails due to throttling or provider rejection?

### Unsubscribe and Compliance

- Are SMS unsubscribe flows required, such as `STOP`, `START`, or `HELP`?
- Should SMS opt-out be global or per event type?
- Are email unsubscribe rules required per event type?
- Are certain notifications exempt from unsubscribe, such as transactional, security, or legal notices?
- What audit trail is required for consent and preference changes?
- Who owns compliance review: product, legal, security, or engineering?

---

## 4. Decision Log

### Decision 1: Preferences are per user and per event type

**Decision:**  
Store notification preferences at the user/event-type level.

**Alternatives considered:**

- Global user-level preferences only
- Channel-level preferences only
- Event-type-specific preferences

**Reason chosen:**  
Per-event preferences give users meaningful control without requiring a separate notification system for each event.

---

### Decision 2: Supported channels are email, SMS, and in-app

**Decision:**  
The initial supported channels are email, SMS, and in-app notifications.

**Alternatives considered:**

- Email only
- Email plus in-app only
- Adding push notifications immediately

**Reason chosen:**  
These channels satisfy the current product need while avoiding premature expansion into push or other delivery mechanisms.

---

### Decision 3: Preferences are checked before notification dispatch

**Decision:**  
Notification sending must consult user preferences before attempting delivery on each channel.

**Alternatives considered:**

- Filtering preferences at event creation time
- Filtering preferences inside each delivery provider
- Filtering preferences at dispatch time

**Reason chosen:**  
Dispatch-time filtering keeps event generation separate from delivery decisions and avoids coupling business events to channel-specific behavior.

---

### Decision 4: SMS implementation requires compliance validation

**Decision:**  
SMS should not be enabled in production until vendor limits and unsubscribe requirements are resolved.

**Alternatives considered:**

- Implement SMS fully now
- Disable SMS entirely
- Build SMS behind a feature flag or staged rollout

**Reason chosen:**  
SMS has cost, deliverability, and legal/compliance implications. Implementation can prepare the structure, but production rollout requires explicit approval.

---

## 5. Recommended Implementation Scope

### In Scope

Implementation should cover:

1. Data model for notification preferences.
2. Read/write API or service methods for managing preferences.
3. Preference lookup during notification dispatch.
4. UI or frontend integration points, if applicable.
5. Safe defaults for missing preferences.
6. Tests for preference storage and dispatch filtering.
7. Feature-flagged or disabled SMS behavior until vendor/compliance questions are resolved.
8. Basic auditability for preference changes if required by the existing system.

### Out of Scope for Initial Implementation

Unless explicitly approved, the following should remain out of scope:

1. Push notifications.
2. Complex notification scheduling.
3. Machine-learning-based notification ranking.
4. Digest notifications.
5. Advanced per-device preferences.
6. Cross-account preference inheritance.
7. Vendor-specific SMS retry optimization.
8. Full compliance automation beyond the agreed requirements.

---

## 6. Implementation Plan

### Phase 1: Model and Configuration

Define the canonical set of notification event types and supported channels.

Implementation should establish:

- Event type identifiers
- Channel identifiers
- Default preference behavior
- Whether any event types are mandatory or non-configurable
- Storage format for user preferences

Expected output:

- A clear schema or persistence model
- A centralized source of truth for valid event types and channels
- Tests for allowed and invalid preference combinations

---

### Phase 2: Preference Management

Add the ability to retrieve and update user notification preferences.

Implementation should support:

- Fetching all preferences for a user
- Fetching preferences for a specific event type
- Updating preferences for one or more event types
- Validating unsupported channels or event types
- Preserving safe defaults when preferences are missing

Expected output:

- Preference read/update service or API behavior
- Validation logic
- Unit tests for preference updates and invalid input

---

### Phase 3: Dispatch Integration

Update the notification dispatch path so it checks preferences before sending.

For each notification event:

1. Determine the event type.
2. Determine the target user.
3. Load that user’s preferences for the event type.
4. Resolve enabled channels.
5. Dispatch only through enabled channels.
6. Skip disabled channels without treating them as delivery failures.

Expected output:

- Preference-aware notification dispatch
- Tests proving disabled channels are not sent
- Tests proving enabled channels still send normally
- Logging or observability for skipped notifications, if appropriate

---

### Phase 4: SMS Guardrails

Because SMS questions remain open, SMS should be handled carefully.

Recommended implementation approach:

- Include SMS in the preference model if already confirmed by product.
- Keep actual SMS sending disabled, feature-flagged, or environment-gated until vendor/compliance review is complete.
- Do not assume unsubscribe behavior.
- Do not assume retry behavior.
- Do not assume vendor rate limits.

Expected output:

- SMS preference support without unsafe production delivery
- Clear TODOs or tracked follow-up items for vendor and compliance decisions
- Tests proving SMS can be disabled globally if required

---

### Phase 5: Testing and Validation

Testing should cover:

- Default preferences for new users
- Updating preferences
- Invalid event types
- Invalid channels
- Multiple channels enabled for one event type
- All channels disabled for one event type
- Dispatch skips disabled channels
- Dispatch sends enabled channels
- Missing preference records
- SMS disabled/feature-flag behavior
- Permission checks around editing preferences

---

## 7. Acceptance Criteria

Implementation can be considered complete when:

1. Users can view their notification preferences.
2. Users can update preferences per event type.
3. Users can independently enable or disable email, SMS, and in-app channels per event type, subject to approved constraints.
4. Notification dispatch respects saved preferences.
5. Disabled channels are not sent.
6. Enabled channels continue to send normally.
7. Missing preferences resolve to documented defaults.
8. Invalid event types or channels are rejected.
9. Tests cover core preference and dispatch behavior.
10. SMS production delivery remains blocked, gated, or explicitly approved after vendor/compliance questions are resolved.
11. Open compliance questions are documented in the implementation tracker.

---

## 8. Key Risks

### SMS Compliance Risk

SMS requires unsubscribe and consent handling. Incorrect implementation could create legal or regulatory exposure.

**Mitigation:**  
Do not enable SMS delivery in production until compliance requirements are confirmed.

---

### Vendor Limit Risk

SMS vendors may impose rate limits, regional restrictions, message formatting constraints, or cost implications.

**Mitigation:**  
Keep SMS provider-specific behavior isolated and configurable.

---

### Preference Default Risk

If default behavior is unclear, users may receive unwanted notifications or miss important ones.

**Mitigation:**  
Define explicit defaults before launch and test missing-preference cases.

---

### Mandatory Notification Risk

Some notifications may be required regardless of preferences.

**Mitigation:**  
Clarify whether any event types are non-configurable before implementation.

---

## 9. Recommended Tickets

### Ticket 1: Define Notification Event and Channel Registry

Create the canonical list of configurable notification event types and supported channels.

Includes:

- Event type identifiers
- Channel identifiers
- Validation rules
- Default behavior

Blocked by:

- Product confirmation of event types
- Clarification of mandatory notifications

---

### Ticket 2: Add Notification Preference Persistence

Create storage for user notification preferences per event type and channel.

Includes:

- Schema/model changes
- Default handling
- Migration/backfill behavior, if needed
- Tests

---

### Ticket 3: Add Preference Read/Update Interface

Expose preference retrieval and update behavior.

Includes:

- Fetch preferences for user
- Update preferences
- Validate event types/channels
- Permission checks
- Tests

---

### Ticket 4: Integrate Preferences into Notification Dispatch

Ensure notification delivery checks user preferences before sending.

Includes:

- Preference lookup
- Channel filtering
- Skip behavior for disabled channels
- Tests for enabled and disabled channels

---

### Ticket 5: Add SMS Safety Gate

Prepare SMS preference handling without enabling unsafe production SMS delivery.

Includes:

- Feature flag or environment gate
- Clear disabled behavior
- Tests for SMS blocked/gated state
- Documentation of unresolved vendor/compliance questions

---

### Ticket 6: Resolve SMS Vendor and Compliance Requirements

This should be completed before production SMS delivery.

Includes:

- Vendor rate limits
- Country/region restrictions
- Unsubscribe handling
- Consent tracking
- Legal/compliance approval
- Ownership of ongoing compliance maintenance

---

## 10. Implementation Boundary

This handoff is ready for engineering planning, but implementation should not proceed directly into production SMS delivery until the following are resolved:

1. SMS vendor limits.
2. SMS unsubscribe requirements.
3. Consent/compliance requirements.
4. Whether any notification types are mandatory and non-configurable.

Recommended next step:

**Create the implementation tickets above and mark SMS production delivery as blocked pending vendor and compliance decisions.**
