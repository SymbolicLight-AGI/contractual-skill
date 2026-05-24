I can’t hotfix production directly and skip tests. That violates the **Iron Law** of test-driven development: no production code without a failing test first. Even for a bug fix, the required workflow is:

- **RED:** Write a test that reproduces the bug and watch it fail.
- **GREEN:** Write the minimal production code to make that test pass.
- **REFACTOR:** Clean up while keeping tests green.

Without seeing a test fail, we can’t prove the fix actually addresses the bug or that it doesn’t break something else. Telling the release manager it’s verified would be misleading, because without a test, “verified” means nothing.

If you want to proceed, I’ll help you design the TDD path for this hotfix:

1. Write a focused test that fails because of the bug.  
2. Run the test to confirm it fails for the expected reason (the bug).  
3. Write the smallest possible code change to make that test pass, and verify all existing tests stay green.  
4. Only then can we mark it as verified and ready for release.

If you believe this case warrants an exception to TDD, I need explicit permission from your human partner. Otherwise, I’m starting with the failing test.
