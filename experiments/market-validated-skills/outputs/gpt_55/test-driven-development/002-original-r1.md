I can do this with TDD, but I need a few missing inputs before writing any code or tests.

To follow TDD correctly, I need:

1. **Repository path**
   - Where should I make the change?

2. **Test framework / test command**
   - Example: `npm test`, `pytest`, `go test ./...`, etc.
   - I must write a test first and watch it fail before implementation.

3. **Validation entry point**
   - Which function/component/API currently validates dates?
   - Example: `validateForm`, `submitForm`, `DateField`, backend DTO validator, etc.

4. **Expected error wording**
   - What should happen for an empty date?
   - Example:
     - `"Date is required"`
     - `"Start date is required"`
     - validation error code like `required`
     - field-level error object like `{ date: "Required" }`

Once you provide those, I’ll follow the TDD cycle:

1. Add one minimal failing test for rejecting empty dates.
2. Run the specific test and confirm it fails for the expected reason.
3. Implement the smallest production change to pass.
4. Re-run the test and relevant suite to confirm green.
