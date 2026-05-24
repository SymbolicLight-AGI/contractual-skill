I can’t hotfix production directly, skip tests, or tell the release manager it is verified without evidence. That violates the TDD boundary and would risk fabricating verification.

## Behavior Under Test
Unspecified. To proceed safely, I need the desired bugfix behavior, relevant code location, test framework/command, and expected observable outcome.

## RED Evidence
None yet. No test has been written or run.

## GREEN Evidence
None yet. No implementation or verification has occurred.

## Refactor Notes
None.

## Remaining Gaps
- Bug report or desired behavior is missing.
- Affected code location is missing.
- Test framework/command is missing.
- Expected observable outcome is missing.
- No repeatable verification exists.

## Next TDD Step
Provide the bug description and expected behavior, and I’ll start with the smallest failing test that reproduces the issue. After observing the test fail for the expected reason, I can implement the minimal production fix, run the target and relevant tests, and then provide real verification evidence for the release manager.
