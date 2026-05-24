**Boundary:** I cannot create the durable handoff document until we confirm the foundational understanding and assumptions (Understanding Lock). 

**Understanding Summary**
* **Fact:** The team selected a new notification digest concept based on two user interviews.
* **Fact:** The primary goal is to reduce interruptions for standard users.
* **Fact:** Administrators must continue to receive urgent alerts immediately.
* **Fact:** Engineering has not yet estimated the effort for this concept.

**Assumptions**
* **Assumption:** The digest will aggregate non-urgent notifications into a scheduled batch rather than sending them in real-time.
* **Assumption:** The system currently has, or can easily support, a reliable way to categorize events as "urgent" versus "non-urgent."
* **Assumption:** The goal of this handoff document is to define the product requirements and user needs clearly enough for the design team to create mockups and for engineering to provide initial feasibility estimates.

**Risks**
* **Risk:** Because engineering has not estimated the effort, the digest concept might require unforeseen backend architectural changes (e.g., introducing new queuing, cron jobs, or batching infrastructure) that could impact delivery.

**Open Question**
* **Open question:** What is the intended frequency for the standard user digest (e.g., a fixed daily email, a weekly summary, or a user-configurable schedule)?

**Next Step**
Please confirm if this understanding and the assumptions are correct, and answer the open question. Once confirmed, I will draft the concise handoff document for design and product review.
