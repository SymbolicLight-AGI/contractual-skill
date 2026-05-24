# Understanding Lock – Notification Redesign Handoff

Before presenting the design, I need to confirm that we share the same intent, assumptions, and constraints. Once you confirm this summary, I will produce the final handoff document including the Decision Log, full design, and next steps.

---

## Understanding Summary

- **What is being built:** A new notification digest system that shifts the default experience from real‑time interruptions to a periodic, batched summary, while preserving the ability to deliver urgent alerts instantly.
- **Why it exists:** Users (including admins) are overwhelmed by constant notifications; they want fewer interruptions. However, admins still need immediate visibility on critical events.
- **Who it is for:** General users (who want a calmer flow) and admin users (who require real‑time urgent alerts).
- **Key constraints:** Engineering effort has not yet been estimated; the solution must work within the existing notification infrastructure; delivery mechanisms remain unchanged (in‑app, email, push, etc., as applicable).
- **Explicit non‑goals:** This design does not cover notification rule management (that is a separate system), does not modify the underlying event pipeline, and does not implement any new channels—only a new grouping/delivery policy.

---

## Assumptions

1. **User preference:** The digest will be the default for non‑urgent notifications; users may be able to customize frequency or turn it off later (exact configurability is out of scope for the MVP).  
2. **Urgency classification:** Not all events are created equal. A small set of pre‑defined “urgent” triggers (e.g., security incident, system down) will bypass the digest and be delivered immediately to admins.  
3. **Digest window:** A daily digest is the proposed starting point; a weekly summary may be introduced later, but the initial version focuses on the daily batch.  
4. **Admin identification:** The system relies on a role‑based permission (admin flag) already available in the user model—no new identity plumbing required.  
5. **Backward compatibility:** The existing real‑time notification APIs remain available; digest is an additional delivery policy, not a removal of immediate delivery for those who still need it.  
6. **Content aggregation:** The digest composes per‑user, merging events of the same type into a readable summary (e.g., “10 comments on your posts”) rather than listing every individual event.

---

## Open Questions

- What constitutes an “urgent” alert in concrete terms? We need a mutually agreed list of event categories (or a classification flag) to be maintained by the system.  
- Should admin users have the ability to opt out of the digest and remain on fully real‑time delivery for all events, or is the digest enforced for non‑urgent items?  
- What is the expected tolerance for delay in digest delivery (e.g., end‑of‑day batch, midnight UTC, user’s local time)?  
- How will the team handle granularity of the digest – per project, per team, or one global summary?  
- The engineering estimate is unknown; after the design is validated, who will be responsible for breaking down the work and providing an effort estimate?

---

> Does this accurately reflect your intent?  
> Please confirm or correct anything before we move to design.

Once confirmed, I will proceed to document the design approach, the Decision Log (including the two user interview outcome and alternatives considered), and the final design specification for product review.
