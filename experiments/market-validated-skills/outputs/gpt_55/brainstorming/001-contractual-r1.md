Understood — we’ll keep this in design exploration only, with no implementation or change plan yet.

### Current Understanding

**Fact:** The current internal document editor supports:
- Single-user editing
- Comments

**Fact:** The desired direction is:
- Multiple people should be able to work together in the same document “somehow”
- The exact collaboration behavior is not yet defined

**Fact:** No implementation work has been approved.

**Goal for this exploration:** Clarify the intended collaboration experience, constraints, risks, and success criteria before proposing design options.

### Initial Assumptions

**Assumption:** “Real-time collaboration” could mean one or more of the following:
- Multiple users editing the document body at the same time
- Seeing other users’ cursors or selections
- Seeing presence indicators, such as “Alice is viewing this doc”
- Live comment updates
- Conflict prevention or automatic merge behavior
- Version history or restore points
- Permission-aware editing

These are not yet accepted requirements.

### Open Question 1

Which collaboration experience are you primarily imagining?

A. **Live co-editing** — multiple users can type in the document at the same time  
B. **Presence + comments only** — users can see who is present and comment live, but document editing remains controlled  
C. **Turn-based editing / locking** — one person edits at a time while others view or comment  
D. **Not sure yet** — you want help comparing these models first
