# Dependency Remediation Handoff

## Confirmed Evidence (Synthetic)

| Item | Value |
|---|---|
| Direct vuln | `lodash@4.17.20` — **High** |
| Transitive vuln | `minimist@0.0.8` — **Moderate** |
| Test status | Not run |
| Owner | **Unknown** (must be assigned before work begins) |

## Open Items / Uncertainty

The following are **not provided** in the task and must be confirmed before remediation proceeds:

- CVE IDs and advisory links for each finding
- Which dependency tree path pulls in `minimist@0.0.8` (parent package + version)
- Package manager in use (npm / pnpm / yarn) and lock file state
- Current `lodash` usage surface (imports, methods called)
- Target environment (runtime vs. dev-only dependency)
- CI pipeline status and release calendar
- Service/repo owner — **blocker** for engineering handoff

---

## Handoff — Engineering

**Action items**

1. Assign code owner (currently unknown — escalate via repo CODEOWNERS or last-committer heuristic).
2. Upgrade direct dependency:
   ```bash
   npm install lodash@latest
   ```
   Then verify with `npm ls lodash` that no duplicate copies remain.
3. Resolve transitive `minimist@0.0.8`:
   - Identify parent: `npm ls minimist`
   - Prefer upgrading the parent package to a version that pulls a patched `minimist` (>=1.2.6).
   - If no parent upgrade exists, apply an `overrides` (npm ≥8.3) / `resolutions` (yarn) / `pnpm.overrides` entry pinning `minimist` to a safe version.
4. Regenerate lock file and commit.
5. Run `npm audit` post-fix; expected result: 0 high, 0 moderate from these two findings.
6. Run the full test suite (currently **not run** — this is a release gate).

**Boundary note:** This Skill covers audit/update commands only. Selection of the specific patched versions, code-level `lodash` API migration, and override syntax decisions belong to engineering.

---

## Handoff — Security

**Action items**

1. Validate CVE mapping for `lodash@4.17.20` and `minimist@0.0.8` — *CVE IDs not supplied in evidence; please attach before sign-off.*
2. Confirm severity classification matches internal policy (High/Moderate per `npm audit`).
3. Set SLA clock:
   - High → per org policy (commonly 7–30 days)
   - Moderate → per org policy (commonly 30–90 days)
   *(SLA values are illustrative; org policy not provided.)*
4. Verify lock file is committed and CI uses `npm ci`.
5. Recommend enabling Dependabot (template available in Skill) if not already active.

---

## Handoff — Release Management

**Action items**

1. **Do not ship** until tests are executed and pass — current test status is "not run".
2. Schedule remediation in next patch release window; classify as security fix.
3. Required gates before release:
   - [ ] Owner assigned
   - [ ] `npm audit` clean for the two reported findings
   - [ ] Full test suite green
   - [ ] Lock file diff reviewed
   - [ ] Security sign-off recorded
4. Prepare changelog entry noting security remediation (CVE IDs pending from Security).
5. Coordinate rollback plan: keep prior lock file tagged for revert.

---

## Blockers

1. **Owner unknown** — must be resolved first; all three workstreams depend on it.
2. **Tests not run** — release cannot proceed; engineering must execute suite post-fix.
3. **CVE IDs / advisory links missing** — Security cannot formally close findings without them.
