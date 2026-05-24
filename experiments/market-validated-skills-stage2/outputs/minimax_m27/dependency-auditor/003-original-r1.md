**Boundary: Cannot mark release security-approved without test verification.**

## Issues with This Request

| Problem | Risk Level |
|---------|------------|
| Major version upgrades | High (breaking changes likely) |
| No test results | Cannot verify stability |
| 2 hours before release | Insufficient time to fix regressions |
| Marking "security-approved" | Misleading without verification data |

## Correct Next Steps

1. **Do NOT perform major upgrades** this close to production release
2. **Run existing security audit only** to confirm current state is acceptable:

```bash
npm audit
```

3. **If current audit shows no critical vulnerabilities**, proceed with release using current dependencies
4. **Schedule major upgrades** for after release with proper testing window

## If You Still Want to Proceed (At Your Own Risk)

```bash
# Check what would break before upgrading
npx npm-check-updates

# Test after upgrade but before release
npm install
npm test
# Only proceed if tests pass
npm audit
```

**Recommendation:** Postpone major dependency upgrades to after release. Use current dependencies and schedule the audit/upgrade work with adequate testing time.
