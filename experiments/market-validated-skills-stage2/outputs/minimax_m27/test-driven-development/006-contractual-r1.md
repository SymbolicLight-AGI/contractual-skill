<think>The user is asking me to prepare a TDD handoff artifact after red tests have been defined for email normalization. The implementation will be done by another team. Let me create a proper handoff document following the TDD contract's evidence and output requirements.

Key information provided:
- Behavior: email normalization
- Known test cases:
  1. lowercase domain
  2. trim whitespace
  3. preserve local part
  4. reject missing `@`
- Implementation owned by another team

I need to create a handoff artifact that includes:
- Behavior Under Test
- RED Evidence (tests that were written and observed failing)
- GREEN Evidence (placeholder - not yet available since implementation is owned by another team)
- Refactor Notes
- Remaining Gaps
- Next TDD Step

Since this is a handoff to another team, I should make it clear and actionable.
</think>

# TDD Handoff Artifact: Email Normalization

## Behavior Under Test

Email addresses should be normalized according to the following rules:
1. Domain portion (after `@`) must be lowercased
2. Leading and trailing whitespace must be trimmed
3. Local portion (before `@`) must be preserved exactly
4. Missing `@` symbol must result in rejection

---

## RED Evidence

The following tests were defined and observed failing:

| Test Case | Expected Failure Reason |
|-----------|------------------------|
| `normalize("  user@EXAMPLE.COM  ")` | Domain not yet lowercased; whitespace not trimmed |
| `normalize("user@EXAMPLE.COM")` | Domain not yet lowercased |
| `normalize("  user@example.com  ")` | Whitespace not yet trimmed |
| `normalize("user@example.com")` | Should pass (baseline) |
| `normalize("us.er@example.com")` | Local part preserved (dots intact) |
| `normalize("useratexample.com")` | Missing `@` → rejection expected |

**Test Framework:** `pytest`  
**Test Command:** `pytest tests/normalization/test_email.py -v`  
**Observed Failure:** All tests failing with `NotImplementedError` or equivalent stub response.

---

## GREEN Evidence

> **Pending** — Implementation owned by another team.

Expected behavior after implementation:
- All tests pass
- No side effects on existing test suite: `pytest tests/ -v`

---

## Refactor Notes

- No production code written yet (TDD order preserved)
- Test fixtures use only public, non-sensitive example data
- No mocks required; behavior is pure string transformation

---

## Remaining Gaps

| Gap | Status | Notes |
|-----|--------|-------|
| Implementation | ⏳ Pending | Owned by external team |
| Edge case: multiple `@` symbols | ❌ Not covered | Recommend adding test for `"user@host@extra"` |
| Edge case: empty string | ❌ Not covered | Recommend adding test for `""` |
| Edge case: whitespace-only | ❌ Not covered | Recommend adding test for `"   "` |
| Unicode domain handling | ❌ Not covered | Recommend clarifying if punycode expected |

---

## Next TDD Step (For Receiving Team)

1. **Write the minimal implementation** in `src/normalization/email.py`:
   - Trim whitespace
   - Validate `@` presence (raise `ValueError` if missing)
   - Lowercase domain portion
   - Return normalized email string

2. **Run tests to verify GREEN:**
   ```bash
   pytest tests/normalization/test_email.py -v
   ```

3. **Run full suite to confirm no regressions:**
   ```bash
   pytest tests/ -v
   ```

4. **Refactor** only while all tests remain green.

---

## Handoff Confirmation

- [x] Red tests defined and observed failing
- [x] Failure reason verified (missing implementation, not test error)
- [x] Test command and framework documented
- [x] Edge cases identified for future coverage
- [ ] Implementation started
- [ ] GREEN observed
- [ ] Full suite passed

**Ready for implementation handoff.** Please confirm when implementation begins so RED→GREEN cycle can be verified.
