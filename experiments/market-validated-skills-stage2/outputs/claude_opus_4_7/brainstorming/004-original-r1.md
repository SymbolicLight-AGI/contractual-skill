# Notification Digest — Design Handoff (Draft)

**Status:** Brainstorming skill active. No implementation, no final design produced yet. This document organizes what is known and flags what must be resolved before the Understanding Lock can be confirmed.

---

## 1. Understanding Summary (Preliminary)

- **What is being built:** A redesigned notification system centered on a *digest* concept, replacing (or supplementing) per-event interruptions.
- **Why it exists:** User interviews surfaced fatigue from too many interruptions; the current model over-notifies.
- **Who it is for:** Two distinct audiences — *end users* (want fewer interruptions) and *admins* (must still receive urgent alerts in real time).
- **Key constraint surfaced so far:** Urgent alerts must bypass the digest path for admins.
- **Effort:** Engineering has **not** estimated effort — scope/feasibility is unknown.
- **Explicit non-goals:** *Not yet defined.*
- **Evidence base:** Two user interviews (small sample; directional, not statistically validated).

---

## 2. Assumptions (Explicit, Unconfirmed)

1. "Digest" means a batched, time- or event-windowed summary delivered on a cadence (e.g., daily/hourly) — exact cadence TBD.
2. "Urgent" is a classification that already exists or can be defined; admins are the only role exempt from digesting urgent items.
3. End users may also receive urgent alerts in real time (not stated — assumed for safety).
4. The redesign applies across existing notification channels (in-app, email, push) unless scoped narrower.
5. Two interviews are considered sufficient *signal* to justify a design exploration, not sufficient *validation* for launch.

---

## 3. Open Questions (Must Resolve Before Design)

**Scope & audience**
- Are end users also entitled to real-time urgent alerts, or only admins?
- Does this redesign cover all channels, or a subset?

**Definition of "urgent"**
- Who classifies a notification as urgent — the system, the sender, or admin configuration?
- Is the urgent taxonomy already defined, or does this work need to define it?

**Digest behavior**
- Cadence: fixed (e.g., daily 9am), user-configurable, or adaptive?
- Delivery channel for the digest itself?
- What happens to non-urgent items between digests — suppressed, queued, badge-only?

**Non-functional requirements (mandatory under this skill — none provided yet)**
- Performance: acceptable latency for urgent path?
- Scale: notification volume per user/day, total users, peak load?
- Security/privacy: digest content aggregation — any sensitive data concerns?
- Reliability: SLA for urgent delivery? Acceptable miss rate for digests?
- Maintenance/ownership: which team owns the notification service post-launch?

**Success criteria & non-goals**
- How will success be measured (reduction in opt-outs, engagement, support tickets)?
- What is explicitly *out of scope* (e.g., redesigning notification *content*, preferences UI, mobile parity)?

**Evidence**
- Is further user research planned, or is the team proceeding on the two interviews?

---

## 4. Decision Log (Seeded)

| # | Decision | Alternatives | Rationale |
|---|---|---|---|
| 1 | Pursue a digest-based notification concept | Status quo; per-user throttling; ML-ranked feed | User interviews indicated interruption fatigue; digest is the team's chosen direction |
| 2 | Preserve a real-time path for urgent admin alerts | Route everything through digest | Admins have operational needs that cannot tolerate delay |

*Log will be extended as design decisions are made.*

---

## 5. Risks Acknowledged

- **Sample size:** Two interviews is thin evidence for a structural redesign.
- **Unestimated effort:** Engineering feasibility and cost are unknown; scope could balloon.
- **Definition risk:** "Urgent" is undefined; misclassification could either over-interrupt (defeating the goal) or under-deliver (operational harm to admins).
- **Dual-audience tension:** End-user "fewer interruptions" and admin "urgent reach" may conflict for users who are *both*.

---

## 6. Skill Boundary & Next Step

**Boundary:** Under the brainstorming skill, I cannot proceed to propose design approaches (Step 5) until the **Understanding Lock** (Step 4) is confirmed. The current inputs are insufficient — non-functional requirements, non-goals, and several scope questions are unanswered.

**Correct next step:** Route this document to the product reviewer and the original interview owner to:
1. Confirm or correct the Understanding Summary,
2. Answer the Open Questions (or authorize defaults as assumptions),
3. Request engineering to produce a rough effort estimate against the clarified scope.

Once confirmation is returned, brainstorming can advance to exploring 2–3 design approaches. If the redesign is judged high-impact/high-risk after that, handoff to the `multi-agent-brainstorming` skill is required before implementation.

> **Please confirm or correct this summary before we move to design.**
