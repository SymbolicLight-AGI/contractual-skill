# TDD Handoff: Email Normalization

## Behavior Under Test

Email normalization with the following observable rules:

1. Domain is lowercased (local part case is preserved).
2. Leading and trailing whitespace is trimmed.
3. Local part casing is preserved exactly.
4. Inputs missing `@` are rejected.

## RED Evidence

Failing tests have been defined for the four known cases. **Command output not included in this handoff** — the implementing team should re-run RED in their environment before writing production code, since RED evidence must be observed in the target repo to be valid TDD.

Test cases authored (one behavior per test):

| # | Test name | Input | Expected |
|---|-----------|-------|----------|
| 1 | `normalizes_domain_to_lowercase` | `"user@Example.COM"` | `"user@example.com"` |
| 2 | `trims_surrounding_whitespace` | `"  user@example.com  "` | `"user@example.com"` |
| 3 | `preserves_local_part_case` | `"User.Name@example.com"` | `"User.Name@example.com"` |
| 4 | `rejects_missing_at_sign` | `"userexample.com"` | rejection (error / invalid result) |

Expected failure mode for each: the symbol/function under test does not yet exist, or returns the input unchanged / does not raise. Implementers must confirm each test fails **for that reason** and not due to setup, import, or typo errors before writing code.

## GREEN Evidence

Not applicable at handoff. Implementation is owned by another team. GREEN evidence (test command + pass summary) should be produced by the implementing team and attached when the cycle closes.

## Refactor Notes

None yet. Refactor only after all four tests are GREEN. Suggested refactor candidates once green:

- Extract a single `normalize_email` function if logic is split across call sites.
- Consider whether rejection is by exception, `Result`/`Option`, or sentinel — this should match repo conventions (not specified in inputs).

## Remaining Gaps

Uncertainties the implementing team must resolve before or during implementation:

- **Test command / framework**: not provided. Implementers must run RED with the repo's standard test command and record it.
- **Rejection contract**: "reject missing `@`" is underspecified — exception type, error value, or boolean? Needs decision from API owner; flag as a Human Gate (public behavior).
- **Edge cases not yet covered** (out of scope for the four known cases, but likely needed):
  - Multiple `@` characters.
  - Empty string and whitespace-only input.
  - Internal whitespace (e.g., `"us er@example.com"`).
  - Unicode / IDN domains and whether domain lowercasing applies to non-ASCII.
  - Already-normalized input (idempotency).
  - Null / `None` input.
- **Local part case preservation vs. RFC**: the rule as stated is preserved casing; if the team intends RFC-compliant normalization (which treats local part as case-sensitive but many providers fold it), confirm with product owner.
- **Mocks**: none used. If the implementing team introduces seams (e.g., an MX-lookup boundary), that requires a Human Gate per the TDD contract.

## Next TDD Step

Recommended order for the receiving team:

1. Run the four RED tests with the repo's test command. Capture and attach failure output.
2. Confirm each failure is for the expected missing-behavior reason; fix any test that fails for setup/typo reasons before proceeding.
3. Resolve the rejection-contract question (Human Gate) before implementing case 4.
4. Implement the minimal code to pass case 1, run suite, observe GREEN, then proceed one test at a time through cases 2–4.
5. After all four are GREEN, add tests for the gap list above one at a time, in the same RED → GREEN → refactor loop.
6. Record RED command + output, GREEN command + output, and any skipped tests with reasons in the final handoff-back artifact.

## Handoff Notes

Per the TDD contract, this artifact is being handed off because implementation is owned by another team. The receiving team should treat the four tests as a starting contract, not a finished RED record — RED must be re-observed in their environment to count as valid TDD evidence.
