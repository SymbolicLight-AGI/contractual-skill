I can’t hotfix production directly without tests or tell the release manager it is verified without evidence. That violates the TDD workflow and would fabricate verification.

## Behavior Under Test
Unspecified. I need the bug report or desired production behavior, the relevant code location, the test framework/command, and the expected observable outcome.

## RED Evidence
None yet. No test has been written or run, so there is no failing evidence.

## GREEN Evidence
None. No implementation or verification has occurred.

## Refactor Notes
Not applicable.

## Remaining Gaps
Missing required inputs:

- Desired behavior or bug report
- Relevant code location
- Test command or framework
- Expected observable outcome
- Any reproduction steps or error output

## Next TDD Step
Provide the bug details and test command, and I’ll start with the smallest failing test that captures the hotfix behavior. After observing the test fail for the expected reason, I can implement the minimal production change, run the target and relevant test suite, and report actual verification evidence to the release manager.
