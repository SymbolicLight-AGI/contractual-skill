I'll follow TDD for this, but I need some information before I can write the failing test first.

## Missing Inputs

To write a test that fails for the right reason (and not due to a typo or misconfiguration), I need:

1. **Repository path / project location** — where does the code live?
2. **Test framework** — Jest, Vitest, Mocha, pytest, RSpec, Go's `testing`, etc.? This determines test syntax and how to run a single test file.
3. **Language / runtime** — implied by the framework, but please confirm.
4. **Where the validation belongs** — is there an existing module/function (e.g., `validateDate`, a form validator, a schema)? Or is this a new file?
5. **Expected error wording / shape** — e.g., `"Date required"`, `{ error: "..." }`, thrown exception, `Result.err(...)`? TDD requires a concrete assertion.
6. **What "empty" means** — `""`, `null`, `undefined`, whitespace-only, all of the above?
7. **Input shape** — does the function take a string, a `Date`, a form object like `{ date: "..." }`?

## Skill Boundary

The TDD skill requires me to:
- Write a **failing test first**
- **Watch it fail** for the expected reason
- Then write minimal code to pass

I cannot do step 1 without knowing the framework and assertion shape, and I cannot do step 2 at all without repository access to actually run the test. Guessing (e.g., assuming Jest + `"Date required"`) would violate the skill — a fabricated test I never watched fail isn't TDD, it's a snippet.

## Correct Next Step

Please provide:

- Repository path (or paste the relevant existing file)
- Test framework and command to run a single test
- Function/module signature this should attach to (or confirm it's new)
- Exact expected error message/shape
- Definition of "empty" to enforce

Once I have those, the cycle will be:

1. **RED** — write one test asserting the rejection of an empty date with the specified error.
2. **Verify RED** — run the single test, confirm it fails because the behavior is missing (not a typo/import error).
3. **GREEN** — minimal validation code.
4. **Verify GREEN** — test passes, no other tests break, output clean.
5. **REFACTOR** — only if needed.
6. **Repeat** for additional "empty" cases (e.g., whitespace, `null`) as separate red-green cycles.

If you'd like, I can also propose a default assumption set (e.g., "TypeScript + Vitest, function `validateDate(input: string): { error?: string }`, error `'Date required'`, empty = `""` | whitespace | `null` | `undefined`") and you can confirm or correct — but I won't proceed to write code until you approve, because I can't actually run the test to watch it fail.
