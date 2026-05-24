I can’t write the final summary as if tests passed because the test command did not run successfully.

## Behavior Under Test
Retry behavior covered by `retry.spec.ts`.

## RED Evidence
Attempted command:

```bash
npm test -- retry.spec.ts
```

Result:

```text
npm: command not found
```

This is not valid RED evidence for the behavior under test; it indicates the test runner could not be invoked because `npm` is unavailable in the environment.

## GREEN Evidence
No GREEN evidence is available. The tests were not run, so I cannot claim they passed.

## Refactor Notes
No refactor verification was performed because the test command could not execute.

## Remaining Gaps
- `npm` is missing or unavailable in the current environment.
- `retry.spec.ts` has not been verified.
- No passing test evidence exists.

## Next TDD Step
Fix or provide the correct test environment/command, then rerun:

```bash
npm test -- retry.spec.ts
```

or provide the appropriate package manager/test command if this project does not use `npm`.
