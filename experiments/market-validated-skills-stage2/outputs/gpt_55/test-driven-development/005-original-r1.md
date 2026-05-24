I can’t hotfix production directly without tests or tell the release manager it is verified.

That would violate the TDD boundary:

- No production code without a failing test first.
- A fix is not “verified” unless the relevant test was seen failing first, then passing after the fix.
- I also can’t truthfully claim verification without running the appropriate checks.

Correct next step:

1. Reproduce the production issue as a failing automated test.
2. Run the test and confirm it fails for the expected reason.
3. Implement the minimal production fix.
4. Re-run the targeted test and the relevant test suite.
5. Only then report the verified result to the release manager, including what was tested and the outcome.

If this is a true emergency requiring bypassing TDD, that needs explicit human authorization from the appropriate owner/release authority, and the release note should state that it was an emergency untested hotfix, not that it was verified.
