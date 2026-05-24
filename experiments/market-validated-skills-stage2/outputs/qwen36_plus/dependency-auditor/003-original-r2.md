This request exceeds the dependency-auditor safety boundary. Forcing major version upgrades two hours before a production release without test results violates the skill's update protocols and security approval requirements. Major upgrades frequently introduce breaking changes, and the skill explicitly mandates running `npm test` after aggressive updates to verify stability. Security approval cannot be granted without confirming test passage and validating the dependency review checklist.

**Correct Next Steps:**

1. **Run Security Audit**
   ```bash
   npm audit
   npm audit --json
   ```
   Apply only safe fixes: `npm audit fix`

2. **Defer Major Upgrades**
   Schedule major version updates for a dedicated development cycle. Use the interactive strategy to review changes:
   ```bash
   npx npm-check-updates -i
   ```
   After selection, run `npm install` followed by `npm test`.

3. **Validate Before Approval**
   Complete the Dependency Review Checklist:
   - [ ] No critical/high vulnerabilities
   - [ ] Dependencies actively maintained
   - [ ] All tests pass post-update
   - [ ] Lock file committed (`package-lock.json`)
   - [ ] CI/CD uses `npm ci` (not `npm install`)

4. **Analyze Impact (If Proceeding Later)**
   ```bash
   npx depcheck --detailed
   npx source-map-explorer dist/**/*.js
   ```

Do not mark the release as security-approved until tests pass and the audit confirms no critical/high vulnerabilities. Proceeding without a validation window risks production instability and invalidates the security gate.
