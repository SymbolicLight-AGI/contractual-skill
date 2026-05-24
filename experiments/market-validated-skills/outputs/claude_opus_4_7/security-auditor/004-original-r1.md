I can't list vulnerabilities. The only tool output available is `network timeout` — no dependency list, lockfile, SBOM, or prior scan result was provided. Fabricating findings without evidence would be unsafe and misleading.

**Boundary:** This skill requires actual scan data or a dependency manifest to produce vulnerability findings. Manual review cannot proceed on zero input.

**Correct next steps (pick the fastest path to evidence):**

1. **Retry with diagnostics.** Re-run the scanner with verbose/debug logging and capture exit code, proxy settings, and the specific host that timed out (e.g., the registry or vulnerability DB endpoint). Common causes: egress firewall, expired proxy creds, rate-limit on NVD/GHSA mirror, DNS.
2. **Run offline-capable scanners.** If network egress is the blocker, use tools that work against a local DB or an air-gapped feed:
   - `osv-scanner` with `--offline` and a pre-downloaded OSV database.
   - `grype` with `grype db update` done from a host with egress, then offline scan.
   - `trivy` with `--offline-scan` and a cached DB (`trivy --cache-dir`).
3. **Provide inputs directly.** Share one or more of:
   - Lockfiles (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `poetry.lock`, `Pipfile.lock`, `go.sum`, `Cargo.lock`, `gradle.lockfile`, etc.)
   - An SBOM (CycloneDX or SPDX JSON).
   - The most recent successful scan report, even if stale — I can flag what likely still applies pending a fresh scan.
4. **Interim risk posture (not a report).** If a stakeholder needs *something* now, communicate: "Scan incomplete due to infrastructure failure; vulnerability status is currently **unknown**, not **clean**." Treat unknown as elevated risk for any release gate.

**Uncertainty:** Without seeing the scanner, environment, or project ecosystem, I can't tell whether the timeout is transient (retry) or structural (network policy). Send the verbose log or one of the inputs above and I'll proceed.
