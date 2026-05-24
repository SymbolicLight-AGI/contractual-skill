I've reviewed the available context: the current editor supports single‑user editing and comments, with no collaboration features in place yet. I’ll treat everything else as unconfirmed.

Let’s begin exploring the idea one step at a time. The most important first question is **what kind of real‑time collaboration you envision**. This will guide all later decisions about architecture, conflicts, and user experience.

**Which of the following best matches the experience you’re aiming for?**

1) **Real‑time simultaneous editing** – multiple users can type and see each other’s changes instantly, like Google Docs or Microsoft Loop. Cursors and selections are visible, edits appear as they happen.
2) **Turn‑based or section‑locking** – only one person can edit a specific section at a time, with clear ownership and no live merge conflicts (similar to a checkout/lock model).
3) **Asynchronous collaboration with live presence** – users see who else is in the document, but changes are saved/committed manually or via a “save and share” flow, not streamed in real time.
4) **Unclear yet** – you just know you need “multiple people working together,” and we should flesh that out first.

Please pick the one that fits your vision (or describe a mix). Once I understand this, we’ll dig into the target users and specific constraints.
