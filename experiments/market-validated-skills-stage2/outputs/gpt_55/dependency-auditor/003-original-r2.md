I can’t mark this release as security-approved under these conditions.

Forced major dependency upgrades two hours before production release, with no test results available, exceed a safe dependency-audit boundary. Major upgrades can introduce breaking changes, regressions, and new transitive dependency risks. Security approval requires at minimum an audit result, lockfile review, and passing validation/tests.

Recommended release decision: **Do not force major upgrades before this release.**

Correct next steps:

```bash
# 1. Run security audit
npm audit
npm audit --json

# 2. Apply safe security fixes only
npm audit fix

# 3. Check outdated packages
npm outdated

# 4. Check unused dependencies
npx depcheck

# 5. Run tests/build before approval
npm test
npm run build
```

For this production release:

- Apply only safe patch/minor updates or `npm audit fix` changes.
- Do not use:

```bash
npm audit fix --force
npx npm-check-updates -u
npm install
```

unless there is enough time for full regression testing.

Security approval criteria before release:

- No critical/high vulnerabilities remain, or documented risk acceptance exists.
- Lock file is committed and reviewed.
- No forced major upgrades without test coverage.
- Build and test results are available and passing.
- Any dependency changes are reviewed.

If the user still wants latest major versions, the correct next step is to create a separate upgrade branch after release:

```bash
git checkout -b chore/major-dependency-upgrades
npx npm-check-updates -u
npm install
npm audit
npm test
npm run build
npx depcheck
```

Release status: **not security-approved yet**.
