# Rewrite Log: dependency-auditor

## Source

- Original repository: `OneWave-AI/claude-skills`
- Original path: `dependency-auditor/SKILL.md`
- Source commit: `eb3d80be32b6cafcf0d5df1c1b8a95df75838271`
- License note: `MIT repository license`

## Contractualization Rules

- Kept the original Skill's domain and primary use case.
- Reorganized task intent into `When To Use`, `Goal`, `Inputs`, `Workflow`, `Permissions`, `Human Gates`, `Constraints`, `Evidence`, `Output`, `Quality Bar`, `Verification`, and `Handoff`.
- Added only generic contract boundaries used throughout the experiment: no fabricated facts, no fake tool results, no unauthorized external action, and explicit uncertainty.
- Did not add external product facts, customer data, vulnerability claims, API deployments, legal commitments, or tool capabilities.

## Field Mapping

- `Goal`, `Audience`, and `Workflow` summarize the original Skill's intended operating mode.
- `Permissions`, `Human Gates`, and `Constraints` make implicit safety boundaries explicit.
- `Evidence` and `Verification` define how the output should stay grounded in supplied task material.
- `Handoff` captures downstream owners without granting authority to perform those teams' actions.
