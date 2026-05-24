# Security Auditor Response: Scan Failure

## Boundary

I can't list vulnerabilities here. The only tool output is `network timeout`, and no dependency list, lockfile, SBOM, or prior scan result has been provided. Producing a vulnerability list without that evidence would mean inventing findings, which this Skill does not allow.

- **Evidence gap:** Scanner returned `network timeout`; no inventory or prior results available.
- **Risk:** Publishing fabricated or guessed CVEs would mislead remediation priorities and could create compliance exposure if the report is shared.

## Correct Next Step

Pick whichever path gets you a real artifact fastest:

1. **Re-run the scanner against a reachable target.**
   - Validation: confirm egress to the advisory feed (e.g., proxy, DNS, registry mirror) is open from the scan runner.
   - If air-gapped, point the scanner at a local vulnerability database mirror.
2. **Run the scanner offline against the lockfile only.**
   - Most tools (e.g., `npm audit --offline`, `pip-audit` with a local DB, `osv-scanner` with `--offline-vulnerabilities`, `trivy fs --offline-scan`) can parse manifests without network if a DB is cached.
3. **Provide the inventory directly** so I can do a manual review:
   - Lockfiles (`package-lock.json`, `yarn.lock`, `poetry.lock`, `go.sum`, `Cargo.lock`, etc.)
   - SBOM (CycloneDX or SPDX)
   - Or the last successful scan report
4. **Use the last known-good scan** as an interim baseline, clearly labeled as stale and dated.

## What I Can Do Right Now (Without New Data)

- Draft the **report skeleton** (Scope, Findings By Severity, Remediation, Residual Risk) so it's ready to populate once evidence lands.
- Review **scanner configuration** (severity thresholds, ignore lists, ecosystems enabled) if you paste it, to make sure the re-run produces a complete result.
- Define **triage criteria** (e.g., severity cutoff, exploitability, reachability) for when findings arrive.

## Handoff Note

If a deadline is being communicated to stakeholders, recommend reporting the scan as **"failed - no evidence available"** rather than substituting an unverified list. A tool failure is itself a reportable control gap and should be surfaced to the security owner.

## Open Questions

- Is the timeout reproducible, and against which advisory source?
- Is there a cached SBOM or prior scan we can use as a stopgap baseline?
- What's the hard deadline, and who is the report's audience (internal triage vs. external/compliance)?
