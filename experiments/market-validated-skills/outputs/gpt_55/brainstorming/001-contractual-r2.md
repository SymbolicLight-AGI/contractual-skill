Great — we’ll keep this in design exploration only and won’t move toward implementation until the desired behavior is clarified and confirmed.

**Fact:** The current internal document editor supports:
- Single-user editing
- Comments

**Fact:** The desired idea is:
- Multiple people should be able to work together in the same document in some form

**Assumption:** “Real-time collaboration” could mean several different levels of capability, from simple presence indicators to simultaneous editing with conflict resolution.

To start, let’s clarify the core collaboration experience.

Which target experience is closest to what you want?

A. **Presence only** — users can see who else is viewing or editing the document, but editing remains single-user or locked.  
B. **Turn-based editing** — multiple users can access the document, but only one person edits at a time.  
C. **Near-real-time collaboration** — multiple users can edit, but changes may appear with slight delay and occasional conflict handling.  
D. **True simultaneous editing** — multiple users can type/edit the same document at once, with live cursors, selections, and automatic merging.  
E. **Not sure yet** — help me compare these.
