## Behavior Under Test

Email normalization should:

1. **Lowercase the domain only**
   - Input: `User@EXAMPLE.COM`
   - Expected: `User@example.com`

2. **Trim surrounding whitespace**
   - Input: `  User@example.com  `
   - Expected: `User@example.com`

3. **Preserve the local part exactly**
   - Input: `User.Name+Tag@Example.COM`
   - Expected: `User.Name+Tag@example.com`
   - Notes: Do not lowercase or otherwise mutate `User.Name+Tag`.

4. **Reject emails missing `@`**
   - Input: `user.example.com`
   - Expected: validation error / rejection according to the project’s existing error-handling pattern.

## RED Evidence

Red tests have been defined for the above cases, but implementation is owned by another team.

Known RED expectations:

- Tests should fail because email normalization is not yet implemented or does not yet meet the specified behavior.
- The failure should be due to behavior mismatch, not syntax errors, fixture errors, or test setup problems.

If actual RED command output is required for acceptance, the owning team should run the target test command and capture:

```text
Command:
<project test command>

Expected RED summary:
- lowercase domain test fails
- trim whitespace test fails
- preserve local part test fails if implementation lowercases entire email
- missing @ rejection test fails if invalid emails are currently accepted
```

Uncertainty: no concrete command output was provided, so pass/fail status is not claimed here.

## GREEN Evidence

Not available yet.

Implementation is pending with the owning team. After implementation, the owning team should run:

```text
<targeted email normalization test command>
```

Then run the relevant broader suite:

```text
<relevant test suite command>
```

Expected GREEN result:

- All newly defined email normalization tests pass.
- Existing related validation tests continue to pass.
- No public behavior changes occur outside the tested scope.

## Refactor Notes

No refactoring should occur before GREEN.

After the minimal implementation passes:

- Refactor only if needed for clarity or reuse.
- Keep tests green after each refactor.
- Avoid changing public API or validation semantics beyond:
  - trimming outer whitespace,
  - lowercasing domain,
  - preserving local part,
  - rejecting missing `@`.

## Remaining Gaps

- Actual test command/framework was not provided in the handoff context.
- No RED command output was included, so failure evidence must be captured by the owning team.
- Exact rejection mechanism for missing `@` is unspecified:
  - exception,
  - validation error object,
  - `null`/`None`,
  - result type,
  - HTTP 400,
  - etc.

The owning team should align the missing-`@` test with the repository’s existing validation/error pattern.

## Next TDD Step

Owning team should:

1. Run the defined email normalization tests before implementation.
2. Confirm RED failures are for the expected behavior gaps.
3. Implement the smallest production change needed to pass:
   - trim input,
   - split on a single valid `@`,
   - preserve local part,
   - lowercase domain,
   - reject missing `@`.
4. Run targeted tests and capture GREEN evidence.
5. Run relevant suite and capture pass summary.
6. Only then refactor, keeping tests green.
