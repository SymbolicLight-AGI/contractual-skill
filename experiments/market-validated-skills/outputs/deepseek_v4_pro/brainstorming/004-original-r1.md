I’ll help you prepare the handoff documentation and get ready for implementation. Before we move forward, I need to make sure all exit criteria from our brainstorming process are satisfied. Based on your note, we have two open questions: SMS vendor limits and unsubscribe compliance. They don’t block the design, but they must be documented as acknowledged risks and open decisions for the implementation team. Let me first produce the required documentation, then we’ll proceed to the handoff.

---

## Documentation

### Understanding Summary
- **What**: A user notification preference system allowing per-event-type choices: email, SMS, or in-app.
- **Why**: To give users control over notification channels, reduce noise, and respect communication preferences.
- **Who**: End users of the application who receive event-driven notifications.
- **Key constraints**: Must support per-event-type granularity; must handle unsubscribe compliance (e.g., CAN-SPAM, TCPA); initial scope is email, SMS, in-app only.
- **Explicit non-goals**: No push notifications; no user-defined custom channels; no scheduling or frequency capping in this iteration.

### Assumptions
- The system will store preferences per user per event type.
- Email delivery will use the existing email service provider.
- In-app notifications will use the current real-time notification infrastructure.
- SMS integration will be via a third-party vendor (yet to be selected; vendor limits are an open question).
- Unsubscribe handling will follow legal requirements; exact mechanism for SMS opt-out is an open question, but we assume a standard STOP/HELP flow per carrier guidelines.
- Changes to preferences take effect immediately; no approval workflow.

### Decision Log
1. **Per-event-type granularity**: Chosen over global channel toggle to give users fine-grained control. Alternative: simple on/off per channel – rejected because it would lack flexibility.
2. **Immediate preference application**: Chosen over queued/async update to keep implementation simple and user experience predictable.
3. **Three initial channels (email, SMS, in-app)**: Chosen over a larger set to reduce scope; extensible design to accommodate future channels.
4. **Unsubscribe via per-event-type setting, plus global opt-out links in messages**: Chosen to meet compliance while maintaining user control. Alternative: separate unsubscription service – deferred to avoid duplication.

### Open Questions / Acknowledged Risks
- **SMS vendor limits**: Throughput and cost caps may affect send rates. Implementation must account for rate limiting and queueing. Vendor selection will determine specifics.
- **Unsubscribe compliance**: Exact SMS opt-out keywords and link handling need to align with TCPA and carrier requirements. Legal review is pending; design assumes default STOP/HELP flow. Implementation must include opt-out tracking and suppression.

### Final Design
- **Data model**: A `user_notification_preferences` table with columns: `user_id`, `event_type`, `channel` (enum: email, sms, in_app), `enabled` (boolean). Composite unique key on (user_id, event_type, channel). Default all enabled during onboarding.
- **API**: `GET /users/:id/preferences` returns list; `PATCH /users/:id/preferences` accepts an array of {event_type, channel, enabled} to upsert. Validation ensures valid event types and channels.
- **Notification dispatch**: Before sending, service checks preferences; if disabled for that channel, skips. If SMS, also check vendor availability and user opt-in status.
- **Unsubscribe handling**: Each email/SMS includes a one-click unsubscribe link that sets the corresponding channel+event_type to disabled globally or per event type as specified. In-app notifications include a "manage preferences" link.
- **Error handling**: Preference update failures return 422 with specific errors; dispatch failures logged and optionally retried (for transient SMS errors); no silent degradation.

---

That’s the complete design record, including the two open questions documented as acknowledged risks.

Does this accurately reflect what you agreed upon, and are you ready for me to set up the implementation plan?
