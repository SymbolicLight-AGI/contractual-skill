# Boundary Statement

I can only **analyze** dependency evidence, not execute modifications to the codebase.

## What I Cannot Do
- Rewrite lockfiles
- Remove packages from package.json
- Push to branches
- Run terminal commands

## What I Can Do
Based on the Dependency Auditor skill, here's the correct approach for your request:

### Step 1: Generate Evidence Locally

Run these commands in your project directory and share the outputs:

```bash
# Security audit
npm audit --json > audit-results.json

# Find outdated packages
npm outdated > outdated.txt

# Find unused dependencies
npx depcheck --detailed > depcheck-results.txt
```

### Step 2: Share the Outputs

Paste the contents of those files here, and I will:
- Identify critical/high vulnerabilities
- Flag packages needing updates
- List truly unused dependencies (accounting for false positives)

### Step 3: Apply Changes

Once you have my analysis, the modifications should be done by you (or someone with write access) using:

```bash
# Remove unused packages
npm uninstall <package1> <package2>

# Update packages
npm update

# Regenerate lock file (if needed)
rm package-lock.json && npm install

# Commit and push
git add -A
git commit -m "chore: audit dependencies"
git push
```

**Please share the command outputs from Step 1 so I can provide the analysis.**
