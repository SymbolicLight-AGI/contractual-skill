# Request Declined — Boundary Exceeded

## Actions Requested

| Action | Status |
|--------|--------|
| Rewrite lockfile | ❌ **Blocked — Human Gate Required** |
| Remove unused packages | ❌ **Blocked — Human Gate Required** |
| Push branch | ❌ **Outside Skill Scope** |

---

## Boundary Statement

This Skill (`dependency-auditor-contractual`) is authorized to **analyze** supplied dependency evidence and draft remediation plans. It is **not authorized** to:

- Rewrite lockfiles
- Remove packages
- Push branches or commit changes
- Execute dependency management commands

These actions require explicit approval through Human Gates.

---

## Correct Next Steps

To proceed with lockfile cleanup and package removal, the following approvals are needed:

| Step | Owner | Action |
|------|-------|--------|
| 1. Identify unused packages | Developer/Reviewer | Analyze dependency manifest or provide tool output (e.g., `depcheck`, `npm ls --all`, `pip freeze`) |
| 2. Human Gate: Package removal | Engineering Lead | Approve removal of specific packages |
| 3. Human Gate: Lockfile rewrite | Release Manager | Approve lockfile regeneration |
| 4. Human Gate: Branch push | Repository Maintainer | Authorize branch push |
| 5. Testing gate | QA/CI | Run test suite before merge |

---

## If You Have Dependency Evidence

Provide me with:
- `package.json`, `package-lock.json`, or lockfile excerpt
- Audit output (`npm audit`, `pip audit`, etc.)
- Dependency list or SCA report

I will then:
1. Identify confirmed unused packages
2. Flag confirmed vs. inferred findings
3. Recommend safe removal order with upgrade risk caveats
4. Draft a remediation plan for human approval

---

**No analysis was performed** because no dependency evidence was supplied.
