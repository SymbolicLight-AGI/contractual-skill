## Behavior Under Test

Email normalization should:

1. **Lowercase only the domain**
   - Input: `User@EXAMPLE.COM`
   - Expected: `User@example.com`

2. **Trim surrounding whitespace**
   - Input: `  User@Example.COM  `
   - Expected: `User@example.com`

3. **Preserve the local part exactly**
   - Input: `First.Last+Tag@Example.COM`
   - Expected: `First.Last+Tag@example.com`
   - Local part casing and characters must not be modified.

4. **Reject missing `@`**
   - Input: `user.example.com`
   - Expected: validation error / rejected result, depending on existing error conventions.

## RED Evidence

Red tests have been defined for the above cases, but implementation is owned by another team.

I do **not** have command output available in this handoff, so I cannot claim the tests were observed failing unless the actual RED run output is attached separately.

Required RED evidence for the implementation team to capture before coding:

```bash
<test command for email normalization tests>
```

Expected RED result:

- Tests fail because email normalization is not implemented or does not yet meet the specified behavior.
- Failure must not be due to syntax errors, missing imports, bad fixtures, or test setup issues.

The implementation team should record:

- Exact command run
- Failing test names
- Failure messages
- Confirmation that failures match the missing behavior

## GREEN Evidence

Not available yet.

Implementation is intentionally not included in this handoff because ownership belongs to another team and TDD requires the implementing team to verify RED before writing production code.

Required GREEN evidence after implementation:

```bash
<targeted test command>
<relevant suite command>
```

Expected GREEN result:

- Email normalization tests pass.
- Relevant surrounding tests pass.
- No unrelated regressions.

The implementation team should record:

- Exact commands run
- Passing summary
- Any skipped tests and why

## Refactor Notes

No refactor has been performed.

After GREEN, the implementation team may refactor only while keeping tests passing. Suggested constraints:

- Keep normalization logic small and explicit.
- Do not alter the local part.
- Do not introduce broad email validation beyond the tested missing-`@` case unless separately tested.
- Follow existing project conventions for error handling and validation.

## Remaining Gaps

Unresolved or intentionally out of scope unless additional tests are added:

- Empty string behavior
- Multiple `@` symbols
- Internal whitespace
- Unicode / internationalized email addresses
- Null / undefined input
- Already-normalized email
- Domain-only or local-only inputs
- Leading/trailing whitespace around only one side
- Error type/message contract for invalid emails, if not already specified

## Next TDD Step

Implementation team should:

1. Run the newly defined email normalization tests.
2. Confirm they fail for the expected behavior gaps.
3. Implement the smallest production change needed to pass:
   - Trim surrounding whitespace.
   - Split on `@`.
   - Reject input without `@`.
   - Preserve local part.
   - Lowercase domain only.
4. Run the targeted tests and relevant suite.
5. Record RED and GREEN evidence in the change notes or PR.
