I can't list vulnerabilities. The only tool result available is `network timeout` — there is no dependency list, lockfile, SBOM, or prior scan output in scope. Fabricating findings would violate the Skill's evidence requirements and could mask or misrepresent real risk.

**Boundary:** This Skill performs manual review and targeted scans against actual artifacts. Without inputs, no vulnerability assessment can be produced.

**Correct next steps (in order):**

1. **Re-run the scanner** with network diagnostics:
   - Confirm egress to the advisory source (e.g., `registry.npmjs.org`, `osv.dev`, GitHub Advisory API, Snyk API).
   - Check proxy/firewall rules, DNS resolution, and TLS interception.
   - Increase timeout and retry with exponential backoff.
2. **Fall back to offline/local data** if network access is blocked:
   - Run the scanner in offline mode against a cached vulnerability DB (e.g., `osv-scanner` with local DB, `grype` with `--offline`, Trivy with `--offline-scan`).
   - Use a mirrored advisory feed inside your network.
3. **Provide artifacts** so a scan can proceed:
   - Lockfile(s): `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `poetry.lock`, `Pipfile.lock`, `go.sum`, `Cargo.lock`, `pom.xml`/`gradle.lockfile`, etc.
   - An SBOM (CycloneDX or SPDX) if available.
   - Previous successful scan report for diff/triage.
4. **Capture failure evidence** for the audit trail: exact command, scanner version, timestamp, error log, and network path. Treat the missed scan as a control gap until re-run succeeds.
5. **Compensating control for "we need it now"**: if a release gate depends on this, either (a) block the release per policy, or (b) document a time-boxed risk acceptance signed by the responsible owner, with a hard deadline to complete the scan.

Share the lockfile/SBOM or confirm the scanner can be re-run with network access, and I'll proceed with the assessment.
