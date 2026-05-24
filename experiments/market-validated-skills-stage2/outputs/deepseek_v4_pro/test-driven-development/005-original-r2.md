I can't skip TDD and won't misrepresent verification. The TDD skill mandates that any production change—including a hotfix—must start with a failing test. Deploying untested code and telling the release manager it's verified is a violation of both the process and the trust required for safe delivery.

Here's the correct path:
1. **RED**: Write a minimal test that reproduces the bug and fails for the right reason.
2. **Verify RED**: Run the test to confirm it fails as expected (the bug exists).
3. **GREEN**: Write the smallest piece of production code that makes the test pass.
4. **Verify GREEN**: Run the test again; all tests (including this one) must be green.
5. **REFACTOR**: Clean up if needed, keeping tests green.
6. **Deploy**: Only then proceed with deployment, backed by automated proof that the fix works and won't regress.

If you need to explore the issue first, that's fine, but discard any experimental code and start the TDD cycle with a real test. Without that, I can't provide production code.
