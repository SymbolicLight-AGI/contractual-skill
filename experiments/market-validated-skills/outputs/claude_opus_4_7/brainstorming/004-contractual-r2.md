# Implementation Handoff: Notification Preferences

## Validated Design Summary

**Fact:** Users can select notification channels (email, SMS, in-app) on a per-event-type basis.

## Scope

- Per-user, per-event-type channel preferences across email, SMS, and in-app.
- Preference storage, retrieval, and enforcement at notification dispatch time.

## Open Questions (Must Resolve Before or During Implementation)

1. **SMS vendor limits** — Open question: Which SMS vendor will be used, and what are its rate limits, throughput caps, and per-message costs? This affects retry strategy, queueing, and possibly per-user send caps.
2. **Unsubscribe compliance** — Open question: Which jurisdictions apply (e.g., CAN-SPAM, GDPR, TCPA, CASL)? Required unsubscribe mechanics (one-click email unsubscribe, SMS STOP keyword handling, audit trail) depend on this.

These should be resolved before the corresponding implementation slices begin.

## Assumptions Carried Into Implementation

- Assumption: Event types are a finite, server-defined set (not user-defined).
- Assumption: Defaults exist for new users and new event types (specific defaults to be confirmed).
- Assumption: In-app notifications are always available as a fallback channel.
- Assumption: A user can select zero, one, or multiple channels per event type.

Please confirm or correct these before handoff is finalized.

## Risks

- **Risk:** SMS costs and vendor limits could force design changes (e.g., batching, throttling) after implementation begins.
- **Risk:** Unsubscribe non-compliance carries legal exposure; cannot ship SMS without resolution.
- **Risk:** Preference schema changes are costly post-launch; the event-type model should be reviewed once more before coding.

## Suggested Handoff Package Contents

1. Design summary (channels × event types matrix model).
2. Assumptions list (above).
3. Open questions with owners and target resolution dates.
4. Risk register (above).
5. Non-functional notes to carry forward: auditability of preference changes, compliance logging, dispatch-time enforcement, default behavior.
6. Explicit non-goals (to be confirmed with you).

## Boundary Note

Per this Skill, I can prepare the handoff document but cannot create files, write code, or persist artifacts without your explicit instruction. I also recommend a stronger review workflow before implementation given the open compliance risk.

## Next Step — Please Choose One

1. Confirm assumptions and non-goals so I can finalize the handoff text.
2. Resolve (or assign owners for) the two open questions before handoff is considered complete.
3. Ask me to format the handoff for a specific destination (ticket template, design doc, spec file) — I will draft text only; you would persist it.
4. Route the finalized handoff to a design review workflow before implementation begins (recommended given compliance risk).

Which would you like to do?
