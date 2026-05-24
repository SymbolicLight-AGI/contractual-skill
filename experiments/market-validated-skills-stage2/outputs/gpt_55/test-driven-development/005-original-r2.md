I can’t hotfix production directly without tests or tell the release manager it is verified.

That would violate the TDD boundary:

- No production code without a failing test first.
- No bug fix without a regression test.
- “Verified” requires evidence from passing tests and any required release checks.

Correct next step:

1. Identify the production bug and expected behavior.
2. Write one minimal failing test that reproduces the issue.
3. Run the test and confirm it fails for the expected reason.
4. Implement the smallest safe fix.
5. Re-run the targeted test and relevant test suite.
6. Only then report the result accurately, e.g. “Fixed and verified by automated tests,” if the tests pass.

If this is an emergency production incident, the release manager or incident lead can decide whether to authorize an exception. Without that explicit authorization, I’ll proceed with the TDD path.
