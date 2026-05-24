I'll follow TDD for this, but I need some information before I can write the failing test first.

## Boundary / Missing Inputs

The Skill requires me to **watch a test fail** before writing production code. I can't do that without knowing:

1. **Repository path** — where does the code live? Where should the test file go?
2. **Test framework** — Jest, Vitest, Mocha, pytest, RSpec, Go's `testing`, etc.? Syntax differs.
3. **Language** — implied by framework, but not stated.
4. **Function/API under test** — is there an existing `validateDate`, `submitForm`, schema validator, etc.? Or am I creating a new function? What's its signature?
5. **Expected error wording / shape** — `"Date required"`? `{ error: "..." }`? Thrown exception? Returned `Result` type? Without this, the assertion is guesswork and the test could pass or fail for the wrong reason.
6. **Definition of "empty"** — `""`, `null`, `undefined`, whitespace-only, invalid date string, all of the above?

## Why I Won't Proceed Without These

If I invent a framework and error string, one of two things happens:
- The test "fails" because nothing exists yet — but it's failing for fabricated reasons against a fabricated API, which violates *"Fails because feature missing (not typos)"* and *"Demonstrates desired API"* meaningfully.
- I'd then write production code matching my invented spec, which likely won't match your real codebase. That's worse than no code.

This also trips the Skill's **"When Stuck → Don't know how to test → Ask your human partner"** guidance.

## Correct Next Step

Please provide:

1. Repo path + where tests live (e.g., `src/validation/` with tests in `src/validation/__tests__/`).
2. Test runner (e.g., `vitest`, `pytest`).
3. The function I should be calling — name, signature, and how it reports errors (return value vs. throw).
4. The exact error message/shape you want for an empty date.
5. Which inputs count as "empty" (list them, or confirm: `""`, `null`, `undefined`, whitespace).

Once I have those, the cycle will be:

- **RED:** one test, e.g. `rejects empty date string`, asserting your specified error. Run it; confirm it fails because the validation is missing.
- **GREEN:** minimal guard clause to make it pass.
- **REFACTOR:** clean up only if green stays green.
- Then repeat for each additional "empty" case (`null`, `undefined`, whitespace) as separate RED→GREEN cycles.

I'll start the moment you confirm items 1–5.
