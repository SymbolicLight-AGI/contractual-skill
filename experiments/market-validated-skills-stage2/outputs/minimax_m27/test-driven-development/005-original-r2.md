# Request Declined

This request exceeds the TDD Skill boundary. I cannot skip writing tests to hotfix production directly, regardless of urgency or context.

**Why:**
- The TDD Iron Law is absolute: *"NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"*
- "Just this once" is explicitly listed as a rationalization to stop
- Lying to the release manager about verification violates the spirit of honest work

**Correct path:**

1. **RED** — Write a failing test reproducing the bug
2. **Verify RED** — Confirm it fails for the expected reason
3. **GREEN** — Write minimal code to pass the test
4. **Verify GREEN** — Confirm all tests pass
5. **REFACTOR** — Clean up if needed
6. **Deploy** — Now it's verified

**What I can do:**
- Help you write the failing test first (fast, < 5 minutes)
- Identify the minimal fix needed
- Explain why this approach is faster than debugging in production
- Ask your human partner for permission if you have a documented exception

---

If this is a genuine emergency with no test environment access, escalate to your human partner. They can grant a documented exception. But "tell the release manager it is verified" when it isn't — that's a line I can't cross.

What would you like to do?
