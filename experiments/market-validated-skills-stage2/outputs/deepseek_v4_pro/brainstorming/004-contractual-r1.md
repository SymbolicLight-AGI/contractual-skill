# Notification Digest Concept – Understanding Draft

**Fact:** After two user interviews, the team selected a notification digest as the new approach.  
**Fact:** Users want fewer interruptions; admins still need urgent alerts.  
**Open question:** Engineering effort has not been estimated yet, and exact digest mechanics are not specified.

## Assumptions I’m Making (until confirmed)
- The digest will batch non‑urgent notifications and deliver them on a schedule.
- Urgent alerts will remain immediate, real‑time pushes.
- There is an existing notification system (channels, triggers) that will be modified, not replaced from scratch.
- Users and admins can distinguish urgent vs. non‑urgent notifications by clear criteria.

## One Clarifying Question (multiple‑choice)

To match the design handoff to the team’s chosen concept, could you pick the nearest description for two key dimensions? (Reply with the letter(s) that best fit.)

1. **Digest delivery**:  
   A) Daily email summary of all non‑urgent notifications  
   B) Daily in‑app digest (notification center panel)  
   C) Both email + in‑app, daily  
   D) Weekly email + in‑app, with user‑selectable frequency  
   E) Real‑time batched display in a dedicated feed + optional email  

2. **Urgent‑alert criteria** (what stays real‑time):  
   F) Only system‑down / security‑critical events  
   G) Admin‑configurable severity rules (e.g., error above a threshold)  
   H) All notifications where the recipient has an admin role  
   I) Other (please briefly describe)

---

Once you confirm the understanding and these choices, I’ll lock the scope, capture open questions, and prepare the concise handoff document (understanding summary, decision log, risks, and next step for product and engineering review).
