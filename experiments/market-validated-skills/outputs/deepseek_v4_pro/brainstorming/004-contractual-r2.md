We’re still in the brainstorming‑contractual workflow, so I’ll generate the implementation‑facing handoff without writing any code or modifying behaviour. Because the remaining open questions touch legal/compliance obligations, I’ll flag them as high‑risk and recommend a stronger review before implementation begins.

---

## Notification Preferences Design Handoff

### Design Summary

**What was decided**  
Users will be able to manage notification preferences per event type. For each event type (e.g., “billing”, “security”, “product updates”, “comments”), the user can individually select delivery channels:  
- Email  
- SMS  
- In‑app  

The preference set becomes the user’s authoritative choice; the system must respect it before sending any notification.

**Scope boundaries**  
- This design covers the “choose channels per event type” behaviour and its storage model.  
- It does **not** cover the actual sending logic, message templates, scheduling, rate‑limiting, or any third‑party integration details beyond the handoff notes.

---

### Decision Log

| # | Decision | Alternatives Considered | Rationale |
|---|----------|------------------------|-----------|
| D1 | Per‑event‑type, multi‑channel opt‑in | Global on/off per channel; single‑channel only | Gives users fine‑grained control; reduces notification fatigue while keeping high‑priority channels available |
| D2 | Store preferences as a set of enabled channels per event type | JSON blob, bitmask | Simple to query, clear contract for downstream services; easy to validate and audit |
| D3 | All channels default to **off** for new users until they explicitly opt in | Default all on; default some on | Aligns with privacy‑by‑design and consent expectations; avoids unsolicited messages |

---

### Assumptions (unvalidated during design)

*Assumption*: The system will have a canonical list of event types and channel identifiers, and both sides of the integration will use the same identifiers.  
*Assumption*: The preference service will be the single source of truth; sending services must check user preferences before dispatch.  
*Assumption*: SMS delivery will use a single vendor with defined throughput limits (not yet quantified).  
*Assumption*: In‑app notifications are fully controlled by the product and do not require external compliance beyond data privacy.

---

### Open Questions (gates before implementation)

| ID | Question | Risk |
|----|----------|------|
| OQ1 | What are the SMS vendor’s throughput limits and message‑per‑user limits? | **High** – could throttle legitimate notifications and cause support incidents |
| OQ2 | How will unsubscribe compliance be implemented, verified, and audited? (Must address per‑channel legal requirements: email unsubscribe header/link, SMS STOP/HELP handling, and potentially per‑event‑type opt‑out) | **Critical** – non‑compliance risks regulatory fines and reputation damage |
| OQ3 | Will there be a global “do not contact” flag that overrides per‑event‑type settings for legal holds? | Medium – affects data model and enforcement logic |
| OQ4 | How will channel unavailability (e.g., no phone number, email not verified) be represented and communicated to the user? | Medium – impacts UX and default behaviour |

**These questions must be resolved before implementation begins.** I recommend routing OQ1 and OQ2 through a compliance/legal review.

---

### Non‑functional Considerations Noted During Design

- **Privacy**: Preferences are personal data; store with the same protections as user PII.  
- **Scalability**: Preference lookups will happen on every notification send; design a read‑optimised data store or caching layer.  
- **Reliability**: If the preference service is unavailable, notifications must **not** be sent by default (fail‑safe to “off”).  
- **Auditability**: Log all changes to notification preferences, including who (user or admin) made the change and a timestamp.

---

### Implementation Handoff Steps

1. **First gate**: Resolve open questions OQ1–OQ4, especially OQ1 and OQ2 through a dedicated compliance review.  
2. Once those are settled, create the data schema, API contract, and wire protocols.  
3. Build or integrate the preference service with the agreed defaults and enforcement rules.  
4. Instrument logging and monitoring for preference changes and send‑attempts blocked due to preferences.  
5. Validate with automated tests covering all event types, channel combinations, opt‑in/opt‑out flow, and compliance scenarios (unsubscribe at channel level).  

---

### Recommended Next Step

Because SMS limits and unsubscribe compliance carry elevated legal and operational risk, I recommend **handing off this finalized design and decision log to a stronger review workflow** (compliance, legal, and security) before any implementation tasks are created. Do you want me to prepare that handoff, or would you prefer to route it yourself?
