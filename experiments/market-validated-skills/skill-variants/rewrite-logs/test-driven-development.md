# Rewrite Log: test-driven-development

## Source

- Repository: `sickn33/antigravity-awesome-skills`
- Path: `skills/test-driven-development/SKILL.md`
- Commit: `85b3a55bc5219b63447012b9ca015c271fda919b`

## Preserved Original Semantics

- Write the test first.
- Observe the test fail before implementation.
- Verify the failure is for the expected reason.
- Write minimal code to pass.
- Refactor only after tests pass.
- Do not write production code before a failing test.
- Ask the human partner for exceptions.
- Do not fabricate test results.

## Contractual Additions

- Added explicit required inputs such as test command, framework, expected behavior, and relevant code location.
- Added `Permissions` and `Human Gates` for skipping TDD, deleting prewritten code, and broad behavior changes.
- Added evidence requirements for RED/GREEN command summaries.
- Added output format for reporting TDD progress.

## Control Note

No new testing framework knowledge or implementation technique was added. The rewrite makes the original TDD order and verification obligations auditable.
