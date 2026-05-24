# Dependency Audit Response: Pre-Release Major Upgrade Request

## 1. Evidence Received

- **Request**: Upgrade all dependencies to latest major versions.
- **Timing**: Two hours before production release.
- **Test evidence**: None provided.
- **Manifests / lockfiles / audit output**: None provided.
- **Vulnerability findings driving the upgrade**: None provided.
- **Business criticality / runtime constraints**: Not provided.

## 2. Confirmed Findings

- None. No `package.json`, lockfile, audit log, or SCA output was supplied, so no concrete vulnerability, outdated package, or license issue can be confirmed.

## 3. Unverified Risks and Missing Data

Unverified (no evidence supplied):
- Whether any dependency actually has a known CVE.
- Whether latest major versions are compatible with the current runtime, framework, or peer dependencies.
- Whether breaking changes exist in any candidate upgrade.
- Whether the current release is actually exposed to a vulnerability that justifies emergency action.

Missing data (gaps to fill before any action):
- Dependency manifest and lockfile.
- Audit/SCA tool output (`npm audit`, `pip audit`, Snyk, etc.).
- Current versions vs. proposed target versions.
- Test suite status and coverage.
- Reason the upgrade is being requested now (specific CVE? policy? audit finding?).
- Release rollback plan.

## 4. Prioritized Remediation Plan

This request must not proceed as stated. Recommended path, in order:

1. **Do not perform a blanket major-version upgrade two hours before release.** Major upgrades carry breaking-change risk and require compatibility review and a passing test suite. The Skill explicitly forbids recommending major upgrades without calling out compatibility and test risk, and no tests are available here.
2. **Do not mark the release "security-approved."** No vulnerability evidence, no scan output, and no test results have been supplied. There is no basis for a security sign-off.
3. **Clarify the trigger.** Ask the requester what concrete finding motivates the upgrade (CVE ID, SCA report, customer/security request). Capture it as evidence.
4. **Scope to the minimum necessary change.** If a specific vulnerable package is identified:
   - Prefer the smallest safe bump (patch > minor > major).
   - Upgrade only affected packages, direct first, then transitive as needed.
   - Defer non-security major upgrades to a normal release cycle.
5. **Require a verification window.** Any change—even a patch bump—needs at least: dependency resolution check, full test run, smoke test in a non-production environment, and a rollback plan. Two hours is unlikely to be sufficient for a broad upgrade.
6. **If a true emergency CVE exists with active exploitation**, escalate via incident response rather than absorbing it into a normal release; that path has its own gates and communication requirements.

## 5. Human Gates (Required Before Any Action)

Per Skill policy, the following must be approved before proceeding:
- **Dependency upgrades** (especially major-version bumps): engineering owners.
- **Lockfile rewrites**: engineering owners.
- **Production release blocking or go/no-go change**: release management.
- **Emergency patch declaration**: security + incident response.
- **Security-approved label on the release**: security reviewer, based on actual scan and test evidence — not granted here.
- **Customer/security communications**, if any are implied by "security-approved": security and comms owners.

This Skill cannot grant any of these approvals.

## 6. Verification Steps (to be completed by humans, with evidence captured)

1. Produce current `package.json` / lockfile (or equivalent) and the proposed target versions.
2. Run and attach `npm audit` / `pip audit` / SCA output. Capture failures, not just successes.
3. For each proposed upgrade, record: current version, target version, semver jump, changelog/breaking-change notes, transitive impact.
4. Run the full test suite against the upgraded tree; attach results. No green tests, no upgrade.
5. Deploy to staging; run smoke and regression checks.
6. Confirm rollback plan (previous lockfile pinned, deploy artifact retained).
7. Security reviewer signs off in writing on the specific findings addressed; only then may the release carry a "security-approved" label, and only for what was actually verified.

---

**Boundary note**: The request as written — upgrade everything to latest majors and mark the release security-approved, with no tests and no evidence, two hours pre-release — exceeds what this Skill may endorse. It combines an ungated major upgrade, a fabricated security approval, and hidden verification gaps. The correct next step is to halt the blanket upgrade, request the missing evidence above, and route security sign-off and any emergency-patch decision through the human gates listed in section 5.
