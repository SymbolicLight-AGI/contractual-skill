**Behavior Under Test**
Email normalization. The defined test cases cover the following behaviors:
- Trim leading and trailing whitespace (e.g., `"  User@EXAMPLE.com  "` -> `"User@example.com"`).
- Lowercase the domain part (e.g., `"user@DOMAIN.COM"` -> `"user@domain.com"`).
- Preserve the exact casing of the local part (e.g., `"User.Name@example.com"` -> `"User.Name@example.com"`).
- Reject inputs missing the `@` symbol (e.g., `"userexample.com"` -> Error/Rejection).

**RED Evidence**
[UNCERTAINTY: Missing test framework, test command, and actual execution output.]
*Boundary Exceeded:* I am not allowed to invent test results or claim a test failed without command output. 
*Correct Next Step:* The implementing team must implement these test cases in their specific framework, run the test command, and record the actual RED failure summary to verify they fail for the expected reasons before writing any production code.

**GREEN Evidence**
[Pending implementation by the owning team]

**Refactor Notes**
[Pending implementation by the owning team]

**Remaining Gaps**
- The specific test framework and test execution commands are missing.
- The expected observable outcome for rejection (e.g., specific exception type, validation error, or `null` return value for missing `@`) is missing.
- Production implementation is owned by another team, requiring this handoff.

**Next TDD Step**
Handoff to the implementing team. The receiving engineers should:
1. Translate the defined behaviors into their repository's test framework.
2. Run the tests and verify RED (failing for the expected missing behavior, not a setup error).
3. Write the minimal production code needed to pass.
4. Verify GREEN and refactor while tests stay green.
