<think>The user is asking me to prepare a TDD handoff artifact after red tests have been defined for email normalization. This is a handoff situation where implementation will be done by another team.

Let me create a proper handoff artifact following the TDD contract's evidence requirements and the workflow guidance.

Key information provided:
- Feature: email normalization
- Implementation owner: another team
- Known test cases:
  1. lowercase domain
  2. trim whitespace
  3. preserve local part
  4. reject missing @

I need to create a handoff artifact that includes:
- RED evidence (tests defined, expected to fail)
- What the implementation team needs to know
- Test command/framework info (need to ask or make assumptions)
- Clear boundaries

Since this is a handoff, I should document what tests exist, what they expect, and what the implementation team needs to do to make them pass.
</think>

# TDD Handoff Artifact: Email Normalization

## Behavior Under Test

Email addresses should be normalized to a canonical form before storage or comparison. The normalization rules are:

| Rule | Input Example | Expected Output |
|------|---------------|-----------------|
| Lowercase domain | `User@EXAMPLE.COM` | `User@example.com` |
| Trim whitespace | `  User@example.com  ` | `User@example.com` |
| Preserve local part | `User.Name@example.com` | `User.Name@example.com` |
| Reject missing `@` | `userexample.com` | `null` / exception |

---

## RED Evidence

### Test Cases Defined

```
tests/
└── email/
    └── normalize_test.dart
```

| Test Name | Expected Behavior | Failure Reason (Pre-Implementation) |
|-----------|-------------------|-------------------------------------|
| `normalizesDomainToLowercase` | `User@EXAMPLE.COM` → `User@example.com` | `EmailNormalizer` not yet implemented |
| `trimsLeadingAndTrailingWhitespace` | `  User@example.com  ` → `User@example.com` | `EmailNormalizer` not yet implemented |
| `preservesLocalPartCase` | `User.Name@example.com` → `User.Name@example.com` | `EmailNormalizer` not yet implemented |
| `rejectsMissingAtSymbol` | `userexample.com` → throws `InvalidEmailException` | `EmailNormalizer` not yet implemented |

### Test Command

```bash
flutter test test/email/normalize_test.dart
# or
dart test test/email/normalize_test.dart
```

### Expected RED Output

```
Expected: 'User@example.com'
Actual: null
Missing implementation of EmailNormalizer
```

---

## Implementation Requirements

### Interface Expected

```dart
class EmailNormalizer {
  /// Returns normalized email or throws InvalidEmailException
  String normalize(String email);
}

class InvalidEmailException implements Exception {
  final String reason;
}
```

### Constraints

- **Do not** modify test cases without agreement.
- **Do not** implement normalization logic before running tests.
- **Do not** add additional transformation rules beyond the four defined cases.

---

## Assumptions (Confirm with Implementation Team)

| Item | Assumption |
|------|------------|
| Framework | Dart/Flutter test (adjust if different) |
| Exception type | `InvalidEmailException` (confirm or specify) |
| Null handling | Return `null` vs throw for invalid input (confirm) |
| Unicode domains | Not in scope for v1 |

---

## Handoff Checklist

- [x] RED tests defined and documented
- [x] Test command provided
- [x] Expected failure reason documented
- [x] Implementation interface specified
- [x] Constraints documented
- [ ] Implementation team confirmed receipt
- [ ] GREEN evidence to be provided by implementation team

---

## Next TDD Step (For Implementation Team)

1. **Run tests** → Verify RED (tests fail with "not implemented" or similar)
2. **Implement minimal `EmailNormalizer`** to pass one test at a time
3. **Run tests** → Verify GREEN
4. **Refactor** if needed while staying green
5. **Report back**: Provide passing test output as GREEN evidence

---

## Contact for Clarification

If the implementation team has questions about expected behavior or test cases, escalate before writing production code.
