# Understanding Phase: Real-Time Collaboration In The Document Editor

Before exploring designs, I need to understand the problem space with you. I'll ask one focused question at a time and lock the shared understanding before proposing any approach.

## What I Know So Far

- **Fact**: The current editor supports single-user editing and comments.
- **Fact**: You want to add real-time collaboration so multiple people can work together in the same document.
- **Fact**: No implementation work is approved; this is design exploration only.
- **Assumption**: "Real-time" means changes from one user become visible to others within seconds, not minutes or on refresh. I'll confirm this later.
- **Open question**: What "working together" means in your context (simultaneous typing? viewing? suggesting?).

## First Clarifying Question

To shape the rest of the exploration, I'd like to start with **purpose and user intent**, since the right collaboration model depends heavily on how people are expected to interact.

**Which of the following best describes the primary collaboration behavior you want users to have? (Pick one; we can refine later.)**

A. **Simultaneous co-editing** — multiple people typing in the same document at the same time, seeing each other's cursors and edits live (Google Docs–style).

B. **Turn-based or locked editing** — one person edits at a time while others view live, with handoff or section-level locks.

C. **Live viewing + async suggestions** — others see edits live but contribute through suggestions, comments, or change requests rather than direct edits.

D. **Something else / not sure yet** — describe what you have in mind, even loosely.

Once you answer, I'll continue narrowing down users, constraints, and success criteria before we look at any design options.
