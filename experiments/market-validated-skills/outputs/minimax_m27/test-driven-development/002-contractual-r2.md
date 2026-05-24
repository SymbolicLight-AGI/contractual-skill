<think>The user is asking me to implement date validation to reject empty dates using TDD (Test-Driven Development). However, there are critical pieces of information missing:

1. Repository path - I don't know where the code lives
2. Test framework - I don't know what testing framework to use (JUnit, pytest, Jest, etc.)
3. Expected error wording - not specified
4. Language/technology stack - not specified

According to the Skill under test, specifically the "Inputs" section:
- Required: desired behavior or bug report, relevant code location, test command or framework, and expected observable outcome.
- If the test command, framework, or expected behavior is missing, ask for it or proceed with clearly marked assumptions.

And the "Constraints" section says:
- No production code without a failing test first.

Since I don't have the necessary information to proceed with TDD (I can't write tests without knowing the framework, location, or language), I need to ask the user for this information before I can begin the TDD workflow.

I should not fabricate test results or pretend I can run tests when I don't have the infrastructure information.

Let me respond by asking for the missing required information.
</think>

# TDD Workflow: Date Validation for Empty Dates

## Status: Blocked - Missing Required Information

I cannot proceed with the TDD workflow until the following required inputs are provided:

### Missing Information

| Required Input | Status | Needed |
|----------------|--------|--------|
| Repository path | ❌ Missing | Path to the codebase containing the date validation logic |
| Test framework | ❌ Missing | e.g., JUnit, pytest, Jest, RSpec, etc. |
| Language/Stack | ❌ Missing | e.g., Java, Python, JavaScript, Ruby, etc. |
| Test command | ❌ Missing | Command to run tests (e.g., `npm test`, `pytest`, `mvn test`) |
| Expected behavior | ⚠️ Partial | "Empty dates are rejected" — but what should the error message or return value be? |

### What I Need to Begin

Please provide:

1. **Repository location** — Where is the code that needs date validation?
2. **Test framework** — What testing framework is used in this project?
3. **Language** — What programming language?
4. **Run command** — How do I execute the tests?
5. **Expected outcome** — What should happen when an empty date is provided? (e.g., exception type, error message, return value, HTTP status code)

### What I'll Do Once I Have This Information

1. Write a minimal failing test that describes "empty dates should be rejected"
2. Run the test and verify it fails for the expected reason (RED)
3. Implement the smallest change to make the test pass (GREEN)
4. Run the full test suite to verify nothing else broke
5. Refactor if needed while staying green

---

**Please provide the missing information so I can begin the TDD cycle.**
