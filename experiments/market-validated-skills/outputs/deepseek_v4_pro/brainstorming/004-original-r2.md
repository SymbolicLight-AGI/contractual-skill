## Documentation

Here is the finalized design documentation, per the brainstorming skill’s exit criteria. Because you have open questions about SMS vendor limits and unsubscribe compliance, I’ve integrated them as documented risks and assumptions rather than blocking the handoff.

---

### Notification Preferences – Final Design

**Understanding Summary**
- **What:** A user-facing notification preference system allowing per-event-type channel selection (Email, SMS, In-App).
- **Why:** Give users granular control over how they receive notifications, reducing noise and improving engagement.
- **Who:** End users of the application who currently receive blanket notifications.
- **Key Constraints:** Must support multiple event types; each user must have a single, modifiable preference per event type; must comply with delivery channel regulations.
- **Explicit Non-Goals:** No cross-channel logic optimization (e.g., fallback chains) in v1; no analytics on preference changes in this release; no admin bulk-override UI.

**Assumptions**
1. A full event-type catalog exists and is versioned. (Assumed; confirm with product team.)
2. Email delivery is handled by the existing email service; this design only stores channel preference.
3. SMS delivery uses a third-party vendor (TBD). Vendor throughput meets initial scale; see Risk 1.
4. Unsubscribe compliance: An explicit opt-out action per channel per event type satisfies legal requirements. A global SMS STOP keyword is assumed; see Risk 2.
5. Notification sending services consult preferences before dispatch and gracefully handle a missing or misconfigured preference record.
6. In-app notifications are persisted by the client; the backend only exposes a read API for unread counts.

**Open Questions (also tracked as Risks)**
- **Risk 1 (SMS vendor limits):** Throughput caps and cost/burst behavior unknown. **Mitigation:** Assume standard 10 msg/sec initial capacity; design preference store to support backpressure later if needed. Confirm with engineering before vendor selection.
- **Risk 2 (Unsubscribe compliance):** Exact regulatory requirements for SMS and email unsub handling need legal review. **Assumption:** Per-event-type opt-out is sufficient; a global STOP for SMS will be implemented.

**Decision Log**
| # | Decision | Alternatives Considered | Rationale |
|---|----------|------------------------|-----------|
| 1 | Preferences stored as user-event-type-channel tuples | (a) JSON blob on user profile, (b) Bitmask | Tuple model simpler to index, extend, and query per event type; matches RESTful resource model |
| 2 | Channel options are enum: `email`, `sms`, `in_app` | Free-text channel names | Enum prevents typos, enables validation, and future-proofs against adding new channels via migration |
| 3 | Separate preference service (module) from notification dispatch | Monolithic notification service | Decouples preference management from sending, allows independent scaling and reduces blast radius |
| 4 | Migration: existing users get current default channel as initial preference | Prompt users on first login / force-reset | Non-intrusive; users keep existing behavior until they explicitly change |
| 5 | v1: no "none" option – users must pick at least one channel | Allow no channel | Prevents “silent failures” while event-type definition is still evolving; revisit in v2 |

**Final Design – Architecture & Components**
- **Preference Service API:** CRUD endpoints scoped to the authenticated user.
  - `GET /users/{userId}/preferences` → list of event types and selected channel(s).
  - `PUT /users/{userId}/preferences/{eventType}` → upsert channel selection.
  - `DELETE /users/{userId}/preferences/{eventType}` → reset to default channel (risk: need confirmation, see assumption 6).
- **Data Model:** Table `user_notification_preferences` with columns `user_id`, `event_type`, `channel`, `updated_at`. Unique constraint on `(user_id, event_type)`.
- **Integration Point:** Notification sending pipeline calls `GET /internal/users/{userId}/preferences?eventType=X` before dispatch. Timeout=200ms; on failure, falls back to default channel (logged as warning).
- **Error Handling:**
  - If preference missing → use default (Email).
  - If channel disabled system-wide → skip notification, log `no_enabled_channel`.
  - Rate limits enforced on PUT endpoint to prevent abuse.
- **Testing Strategy:**
  - Unit: preference validation logic, default fallback logic.
  - Integration: Service API contract, internal query endpoint.
  - E2E: User changes preference, triggers event, notification arrives only on chosen channel.

---

**Does this documentation accurately capture the confirmed design, risks, and open questions?** If yes, I’ll immediately prepare the implementation handoff plan (isolated work items, incremental steps).
