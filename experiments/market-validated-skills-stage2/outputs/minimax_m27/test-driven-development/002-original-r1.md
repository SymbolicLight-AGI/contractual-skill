<think>The user is asking me to follow the TDD skill for a date-validation bug, but they haven't provided:
- Language/framework
- Test framework
- Current behavior
- Expected behavior/edge cases
- Any code context

According to the TDD skill, I should:
1. Write a failing test first
2. Watch it fail
3. Write minimal code to pass
4. Refactor

But I can't do any of this without knowing:
- What language they're using
- What test framework they have
- What the actual bug is
- What the expected behavior should be

The skill says: "Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing."

I should ask for the missing information rather than inventing project details. This is the correct boundary to state.
</think>

# Missing Information

I can't follow the TDD cycle without knowing your context. Please provide:

1. **Language/framework** — TypeScript, Python, JavaScript, etc.?
2. **Test framework** — Jest, Vitest, pytest, JUnit, etc.?
3. **Current behavior** — What happens now that shouldn't?
4. **Expected behavior** — What should happen instead?
5. **Edge cases** — Invalid formats, timezones, leap years, etc.?

**Example of what I'd need:**

> "TypeScript with Jest. `parseDate('2024-02-30')` returns a Date object instead of throwing."

Once you provide this, I'll write the RED test, verify it fails, then guide you through GREEN and REFACTOR.
