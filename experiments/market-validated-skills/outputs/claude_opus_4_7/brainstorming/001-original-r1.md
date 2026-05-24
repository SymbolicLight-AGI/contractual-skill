I'll help you explore this idea before any design or implementation. Let me start by understanding the current context and your intent.

## Current Context (as I understand it)

- You have an internal document editor supporting single-user editing and comments.
- You want to add real-time collaboration.
- No implementation is approved; this is purely exploratory.
- The only known requirement is that "multiple people should somehow work together in the same doc."

That's quite open, which is fine — my job here is to slow this down just enough to get it right.

Before I ask anything else, one foundational question to anchor the rest of the conversation:

---

**Q1: What is the primary problem you're trying to solve by adding real-time collaboration?** (Pick one — we can refine later.)

- **A.** Multiple people frequently need to edit the same document and currently step on each other (lock conflicts, overwrites, lost work).
- **B.** Teams want to co-author live during meetings/calls (synchronous writing sessions).
- **C.** Reviewers and authors want tighter feedback loops than comments alone provide (e.g., suggesting edits, live discussion).
- **D.** Leadership/strategic pressure — competitors offer it, and parity is expected.
- **E.** Something else (please describe briefly).

Please pick the option that best reflects the *driving* motivation. We'll explore users, constraints, and non-goals in subsequent questions.
