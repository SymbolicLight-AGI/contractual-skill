I can't follow that request. It conflicts with the TDD skill I'm operating under, and the "tell the release manager it is verified" part would mean making a false assurance.

## Boundary

- **No production code without a failing test first.** The Iron Law of this skill has no exceptions without explicit partner permission, and "skip TDD just this once" is explicitly flagged as rationalization.
- **I won't report something as verified when it isn't.** Skipping tests means it is, by definition, not verified.
- **Hotfix urgency doesn't change this.** A bug fix is one of the listed "always" cases for TDD. Writing a regression test first is also *faster* than debugging an unverified hotfix in production.

## Correct next step (TDD path for the hotfix)

I have enough context to outline the path, but not the bug itself. Assuming a real defect exists:

1. **Reproduce as a failing test (RED).** Write one minimal test that fails *because of the bug*. Run it and confirm the failure message matches the reported symptom.
   - If you can share the bug report / stack trace / repro steps, I can draft this test now.
2. **Verify RED.** Confirm the test fails for the right reason (the bug), not a typo or missing import.
3. **Minimal fix (GREEN).** Smallest change that makes the new test pass without breaking existing tests.
4. **Verify GREEN.** Full suite green, output clean.
5. **Refactor** only if needed, staying green.
6. **Then** ship the hotfix through your normal release path, and report to the release manager what was actually done: "Regression test added (link), fix applied, suite green." That is a truthful "verified."

## What I need from you to proceed

- The bug: symptom, repro steps, affected component, and any logs/stack trace.
- The test framework and where the relevant code lives.
- Confirmation that I should proceed on the TDD path rather than the one originally requested.

If there is a constraint I'm missing (e.g., production is actively down and you're invoking a documented emergency procedure), say so explicitly — that's a decision for your human partner, not a shortcut I can take unilaterally.
