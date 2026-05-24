# Email Normalization TDD Handoff

## Behavior Under Test

`normalizeEmail(input: string)` — normalizes an email address with these rules:

1. Lowercase the domain portion (right of `@`).
2. Trim leading/trailing whitespace from the full input.
3. Preserve the local part (left of `@`) exactly as provided after trimming.
4. Reject input missing an `@` character (error/exception behavior to be confirmed by implementing team — see Remaining Gaps).

## RED Evidence

Red tests have been authored. **Failing command output is not yet captured in this handoff** — the implementing team should run the suite first and confirm RED before writing production code.

Test cases defined (one assertion per behavior):

| # | Case | Input | Expected |
|---|------|-------|----------|
| 1 | Lowercase domain | `"user@EXAMPLE.COM"` | `"user@example.com"` |
| 2 | Trim whitespace | `"  user@example.com  "` | `"user@example.com"` |
| 3 | Preserve local part casing/characters | `"User.Name+tag@Example.COM"` | `"User.Name+tag@example.com"` |
| 4 | Reject missing `@` | `"userexample.com"` | rejection (mechanism TBD) |

Suggested test command: *to be filled by implementing team using their framework conventions* (e.g., `npm test -- email-normalize`, `pytest tests/test_email_normalize.py`).

Expected RED failure reason for each: `normalizeEmail` is not implemented (or returns input unchanged), so assertions on transformed output fail. Test 4 should fail because no rejection path exists yet.

> Uncertainty: I have not executed these tests in this environment. The implementing team must observe and record the RED output before writing production code, per the TDD contract.

## GREEN Evidence

Not applicable at handoff. Implementation is owned by another team. GREEN evidence is their responsibility to capture: target test command + pass summary + relevant suite run.

## Refactor Notes

No refactor performed — no production code exists yet. After GREEN, candidates to consider:

- Extract domain-split helper if reused elsewhere.
- Centralize the rejection error type with other input-validation errors.

Refactors must keep all four tests green.

## Remaining Gaps

1. **Rejection contract undefined.** Should missing `@` throw, return `null`, return a `Result`/tuple, or something else? Test 4 currently asserts a placeholder; the implementing team must confirm and the test must be updated before RED is observed for the wrong reason.
2. **Edge cases not covered by red tests** — flag for the implementing team to add cycles for:
   - Multiple `@` characters (e.g., `"a@b@c"`).
   - Empty string and whitespace-only input.
   - Unicode / IDN domains (should domain lowercasing be Unicode-aware?).
   - Internal whitespace inside the local part or domain.
   - Quoted local parts (RFC 5321) — explicitly in or out of scope?
3. **Test framework, file location, and naming conventions** not specified in this handoff; align to the receiving team's repo patterns.
4. **No command output captured.** Per the TDD contract, I cannot claim RED was observed. The receiving team must run and record it.

## Next TDD Step

Receiving team:

1. Place the four red tests in the conventional location for their repo and confirm the test command.
2. Resolve the rejection-contract question (Gap #1) and update test 4 accordingly.
3. Run the suite and **capture RED output**, verifying each test fails for the right reason (missing implementation, not setup/typo).
4. Implement the minimal `normalizeEmail` to pass all four tests.
5. Run the suite and capture GREEN output.
6. Add a new RED cycle for the next edge case from Gap #2 before extending behavior.

## Handoff Note

This handoff transfers ownership at the "RED defined, not yet observed" boundary. Per the TDD contract, **no production code should be written until the receiving team has run the tests and recorded a legitimate RED failure**. If they wish to skip TDD or proceed differently, that is an exception requiring their own human-gate confirmation.
