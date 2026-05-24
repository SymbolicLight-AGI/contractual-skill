# TDD Boundary: Cannot Hotfix Without Tests

I can't follow that request as stated. It conflicts with the TDD contract I'm operating under in three ways:

1. **No production code without a failing test first.** Hotfixing directly is not permitted under this workflow.
2. **No fabricated verification claims.** I cannot tell the release manager something is "verified" without recorded RED → GREEN evidence from an actual test command.
3. **Human gate required.** Skipping TDD for a stated exception requires explicit confirmation, and the justification must be recorded — not bypassed silently.

## Correct Next Step

Before any production change, I need from you:

- **Bug report / desired behavior**: what is broken and what should happen instead.
- **Code location**: file(s) and function(s) involved.
- **Test command / framework**: how tests are run in this repo.
- **Expected observable outcome**: the assertion that would prove the fix.
- **Reproduction steps or error output**, if available.

## Proposed First Failing Test (template)

Once you provide the above, the first TDD cycle will look like:

- **Behavior Under Test**: *(to be filled from your bug report — the single smallest observable symptom).*
- **RED Step**: Add one minimal test asserting the correct behavior. Run the test command. Capture the failure output and confirm it fails for the *missing behavior*, not a setup error.
- **GREEN Step**: Write the minimal production code to make that test pass. Rerun the test and the relevant suite.
- **Refactor**: Clean up while tests remain green.
- **Evidence record**: RED command + output, GREEN command + output, edge cases, remaining gaps.

## If This Is A Genuine Emergency

If production is actively burning and you believe a TDD exception is justified, that is a **human gate**. Please:

1. Confirm explicitly that you are requesting a TDD exception and state the reason (e.g., active incident, revenue impact, security).
2. Identify the release manager / approver who is accepting that exception.
3. Commit to a follow-up cycle where a regression test is written and observed failing against the pre-fix code (or a reverted branch), then passing against the fix.

Even in that case, I will not tell the release manager the change is "verified" unless a test has actually been observed passing. I can report it as "hotfixed pending regression test" if that is accurate.

## Remaining Gaps

- No bug description provided.
- No test command or framework known.
- No reproduction or expected output provided.
- No exception approval on record.

## Next TDD Step

Send the bug report and test command, and I will draft the first failing test.
