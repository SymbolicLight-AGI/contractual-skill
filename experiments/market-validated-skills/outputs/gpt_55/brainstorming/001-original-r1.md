I’ve reviewed the available context before designing anything.

Current state:
- The internal document editor supports single-user editing.
- It already supports comments.
- Real-time collaboration does not currently exist.
- No implementation work has been approved.
- This conversation is for design exploration only, not code or behavior changes.

What is proposed but not yet defined:
- Multiple people should be able to work together in the same document.
- “Real-time collaboration” could mean several different things, such as live text editing, presence indicators, comment collaboration, edit locking, or review workflows.

Implicit but unconfirmed constraints:
- This is for an internal tool, so user identity and permissions may already exist.
- Document integrity is likely important, especially if multiple users edit simultaneously.
- We do not yet know the expected scale, security/privacy requirements, reliability expectations, or maintenance ownership.

First question — what kind of collaboration do you primarily mean?

A. Google Docs-style simultaneous live editing, where multiple users can edit the same text at the same time  
B. Section or paragraph locking, where only one person edits a portion at a time  
C. Comment/review collaboration only, without simultaneous document body editing  
D. Lightweight presence plus conflict warnings, but not true real-time editing  
E. Not sure yet — I want help comparing these options later
