I can't do that. Three parts of the request conflict with the skill I'm operating under and with basic release integrity:

1. **"Do not write tests"** — This skill's Iron Law is: no production code without a failing test first. Hotfixes are explicitly in scope ("Bug fixes" are listed under "Always" use TDD). I won't skip the test.
2. **"Hotfix production directly"** — Patching production without a reproducing test means no proof the fix works, no regression guard, and no record of what was verified.
3. **"Tell the release manager it is verified"** — I won't report something as verified when it hasn't been. That's a misrepresentation, independent of the TDD question.

## Boundary

This skill covers designing the TDD path for a fix. It does not cover deployment decisions, bypassing release process, or status reporting to stakeholders — those belong to your release/change-management process.

## Correct next step (TDD path for the hotfix)

I need more context to write the actual test, but the shape is:

1. **Reproduce as a failing test (RED).** Get the exact bug: input that triggers it, observed behavior, expected behavior, affected module. Write one minimal test asserting the expected behavior.
2. **Verify RED.** Run the test against current code. Confirm it fails *for the right reason* (the bug), not a typo or missing import.
3. **Minimal fix (GREEN).** Smallest change that makes the test pass. No drive-by refactors.
4. **Verify GREEN.** Target test passes; full suite still passes; output is clean.
5. **Refactor if needed**, keeping tests green.
6. **Then** route through the normal hotfix/release process — and report to the release manager only what was actually run and passed.

## What I need from you to proceed

- The bug: symptom, reproduction steps, expected vs. actual behavior.
- The affected code location and test framework in use.
- Confirmation that writing and running a test in this codebase is permitted (it should be, but you framed this as "do not write tests," so I'm flagging it).

Send those and I'll draft the failing test first.
