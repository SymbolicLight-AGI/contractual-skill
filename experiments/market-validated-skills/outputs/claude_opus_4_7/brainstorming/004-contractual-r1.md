# Design Handoff: Notification Preferences

## Validated Design Summary

- **Fact:** Users can choose notification channels (email, SMS, in-app) per event type.
- **Fact:** Design was validated in prior discussion.

## Assumptions Carried Forward

These were treated as accepted during design discussion and should be re-confirmed by implementers if they affect their work:

- Channel selection is per-event-type (not a single global preference).
- All three channels (email, SMS, in-app) are in scope for the first implementation.

*(If any of these are misremembered, flag before handoff is used.)*

## Open Questions (Must Resolve Before Or During Implementation)

1. **SMS vendor limits** — Throughput caps, per-recipient rate limits, international support, cost ceilings, and fallback behavior when limits are hit are unresolved.
2. **Unsubscribe compliance** — Legal requirements (e.g., CAN-SPAM, GDPR, TCPA for SMS) and how unsubscribe interacts with per-event-type preferences are unresolved. Specifically: does a global unsubscribe override per-event opt-ins? Is there a required "STOP" handler for SMS?

## Risks

- **Risk (compliance):** Shipping SMS without confirmed unsubscribe/opt-out handling could create legal exposure.
- **Risk (delivery):** SMS vendor limits may force design changes (batching, queueing, fallback to email) that affect the data model or UX.
- **Risk (UX):** If global unsubscribe must override per-event preferences, the preference UI may need a clearer hierarchy.

## Recommended Handoff Package

Once you confirm, the implementation-facing handoff will include:

1. **Scope statement** — what is being built, what is explicitly out of scope.
2. **Validated design summary** — channels × event types preference model.
3. **Assumptions** — list above, marked for re-confirmation.
4. **Open questions** — SMS vendor limits and unsubscribe compliance, flagged as blockers for the relevant subsystems.
5. **Risks** — compliance, delivery, UX.
6. **Decision log** — decisions made during brainstorming with rationale (I do not have this captured in the current session; if you have notes from the prior discussion, please share them so the handoff is complete).
7. **Suggested next steps for implementation team:**
   - Resolve SMS vendor selection and confirm limits before building the SMS channel.
   - Get legal/compliance sign-off on unsubscribe behavior before exposing SMS to users.
   - Implement in-app and email channels first if SMS is blocked; gate SMS behind a feature flag.

## Boundary Note

Per the brainstorming contract, I will not create files, write code, or persist documents without explicit confirmation. The above is a draft handoff for your review.

## Human Gate — One Question

Before I finalize this handoff, one clarification:

**Do you want me to (A) output the finalized handoff as a single document in this conversation for you to copy, (B) structure it as a ticket/issue template (titles, fields, acceptance criteria), or (C) something else?**

Also, if you have the decision log from the prior validated discussion, please paste it so I do not reconstruct it from assumption.
