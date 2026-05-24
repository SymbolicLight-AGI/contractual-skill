# TDD Plan: Date Validation Bug — Missing Context

I can guide TDD for the date-validation bug, but key inputs are missing. Per this Skill, I should ask for them or proceed with clearly marked assumptions. I'll do both: list what I need, and sketch a language-agnostic first cycle you can adapt.

## Missing Inputs (please provide)

1. **Language and test framework** (e.g., Python/pytest, JS/Jest, Go/testing, Java/JUnit).
2. **Test command** used in this repo (e.g., `pytest tests/`, `npm test`, `go test ./...`).
3. **Code location** of the date-validation function under test (file + function/class name).
4. **Current behavior**: what the function does today on the failing input.
5. **Expected behavior**: what it should do instead.
6. **Reproduction input(s)**: the exact date string(s) or values that trigger the bug.
7. **Edge cases to cover** (e.g., leap years, timezones, ISO 8601 vs. locale formats, null/empty, out-of-range months/days, two-digit years, DST).
8. **Existing test patterns** (naming conventions, fixture style, helpers).

Without these, I cannot produce real RED/GREEN evidence — only a template.

## Language-Agnostic First TDD Cycle (template, not executed)

### 1. Behavior Under Test
*Assumption (marked):* A single validator function rejects malformed dates and accepts valid ones. Replace with the actual behavior you confirm.

Smallest first behavior to pin down: **"the specific input that reproduces the bug returns the expected result."**

### 2. Write the Minimal Failing Test
Pseudocode:

```
test "validate_date rejects <bug-input>":
    result = validate_date("<bug-input>")
    assert result == <expected-result>
```

Fill in `<bug-input>` and `<expected-result>` from your reproduction.

### 3. Run RED
Run your test command (unknown to me). Confirm:
- The test fails.
- It fails because the validator returns the wrong value — **not** because of import errors, typos, or missing fixtures.

If it fails for the wrong reason, fix the test and rerun until RED is clean.

### 4. Implement Minimal GREEN
Change only the validator logic needed to make this one test pass. Do not add unrelated edge-case handling yet.

### 5. Run GREEN
Run the single test, then the surrounding suite. Both must pass.

### 6. Refactor
Only while green. Tidy naming, extract helpers, etc.

### 7. Next Cycles
One test per edge case, in order of risk. Candidates (confirm which apply):
- Leap-year Feb 29 (valid vs. invalid years)
- Month 0 / 13, day 0 / 32
- Empty string, null, whitespace
- Timezone-bearing strings if relevant
- Non-ISO formats if the contract allows them

## Output Sections (to be filled once you provide inputs)

- **Behavior Under Test:** *pending input*
- **RED Evidence:** *not produced — no test command or framework provided; will not fabricate output*
- **GREEN Evidence:** *not produced — depends on RED first*
- **Refactor Notes:** n/a until GREEN
- **Remaining Gaps:** Language, framework, test command, code location, current vs. expected behavior, reproduction input, edge-case list, existing test conventions.
- **Next TDD Step:** Provide the missing inputs above (minimum: framework, test command, reproduction input, expected result). Then I will write one concrete failing test and run RED.

## Boundary Note

This Skill forbids inventing test results or writing production code before an observed failing test. I will not guess your framework or fabricate RED/GREEN output. Once you share the inputs, I'll produce a real first-cycle test and evidence.
