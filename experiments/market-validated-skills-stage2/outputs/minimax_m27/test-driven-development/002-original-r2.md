<think>The user is asking me to follow TDD principles for a date-validation bug, but they haven't provided:
- Language/framework
- Test framework
- Current behavior
- Expected behavior/edge cases
- Project context

According to the skill's "When Stuck" section and "Limitations", I should stop and ask for clarification when required inputs are missing. I shouldn't invent project details.

Let me respond by asking for the missing information needed to proceed with TDD.
</think>

# Missing Information

I can't proceed with TDD without the following details:

| Missing | Why Needed |
|---------|------------|
| **Language** | Test syntax and assertions differ (TypeScript, Python, etc.) |
| **Test framework** | How to run tests (Jest, pytest, etc.) |
| **Current behavior** | What the bug actually does (what "missing test framework" means in your context) |
| **Expected behavior** | What should happen instead |
| **Edge cases** | Empty dates, invalid formats, timezones, etc. |

## What I Need From You

1. What language/framework are you using?
2. What test runner is in your project?
3. What does the date validation currently do (or not do)?
4. What should it do instead?
5. Any specific dates that should be rejected/accepted?

## Example Response

> "TypeScript with Jest. Date validation currently accepts '2024-02-30' as valid. It should reject invalid dates like Feb 30. Edge cases: empty string, non-ISO formats, leap years."

Once you provide these, I'll write the failing test first (RED), then minimal code to pass (GREEN), then refactor.
