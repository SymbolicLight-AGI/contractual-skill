# Repository File Map

## Overview

- Project: Contractual Skill Evaluation Artifacts
- Stage: published replication package
- Last updated: 2026-05-24

## Top-Level Structure

| Path | Purpose | Maintenance Note |
| --- | --- | --- |
| `experiments/text-generation/` | Synthetic text-generation experiment package. | Do not overwrite saved model outputs unless creating a new release/version. |
| `experiments/tool-calling/` | Offline simulated tool-calling challenge package. | Simulated tools only; no real external system calls should be added. |
| `experiments/openspec-explore/` | Small old-vs-contractual OpenSpec explore Skill comparison. | Keep original and contractual variants side by side for traceability. |
| `experiments/market-validated-skills/` | Stage 1 market-validated Skill A/B pilot. | Keep original sources, contractual rewrites, outputs, scores, and retry logs together. |
| `experiments/market-validated-skills-stage2/` | Stage 2 expanded market-validated Skill A/B study package. | Generation outputs and two judge score files are complete; raw judge files retain retry rows for auditability. |
| `templates/` | Reusable English and Chinese contractual Skill templates. | Keep generic, non-sensitive, and aligned with the contractual examples. |
| `docs/` | Reproducibility notes, data statement, and this file map. | Update when the package structure changes. |
| `docs/market_validated_skill_ab_experiment_design.zh-CN.md` | Design note for the market-validated Skill A/B experiment. | Keep aligned with Stage 1 and Stage 2 artifacts when the protocol changes. |

## Important Subdirectories

| Path | Responsibility | Change Impact |
| --- | --- | --- |
| `experiments/text-generation/tasks/` | Synthetic task definitions. | Changes affect prompt generation and reported task count. |
| `experiments/text-generation/skill-variants/` | Skill condition templates. | Changes affect the interpretation of no-skill, minimal, plain-expanded, and contractual conditions. |
| `experiments/text-generation/outputs*/` | Saved model outputs. | Treat as research records for this manuscript version. |
| `experiments/text-generation/scoring/` | Scoring scripts, judge records, summaries, and rubric. | Changes affect reported text-generation scores. |
| `experiments/tool-calling/tasks/` | Simulated tool-calling challenge tasks. | Changes affect challenge difficulty and record counts. |
| `experiments/tool-calling/transcripts/` | Saved tool-calling transcripts. | Treat as research records for this manuscript version. |
| `experiments/tool-calling/scoring/` | Tool-call scoring scripts and summaries. | Changes affect reported high-risk tool attempt counts. |
| `experiments/openspec-explore/skill-variants/` | Original and contractual OpenSpec explore Skill documents. | Preserve the original as the baseline condition. |
| `experiments/openspec-explore/tasks/` | Five explore-mode comparison tasks. | Changes affect prompt count and contract-affordance scores. |
| `experiments/openspec-explore/prompts/` | Generated prompts for original and contractual variants. | Regenerate with the local build script after task or Skill edits. |
| `experiments/openspec-explore/scoring/` | Deterministic contract-affordance scoring scripts and outputs. | Scores reflect explicit contract signals, not live model behavior. |
| `experiments/market-validated-skills/sources/` | Source repository, commit, and license notes for selected public Skills. | Update before changing selected Skills. |
| `experiments/market-validated-skills/skill-variants/` | Original and contractualized Skill variants plus rewrite logs. | Preserve original files unchanged for A/B comparison. |
| `experiments/market-validated-skills/tasks/` | Sixteen synthetic Stage 1 tasks. | Keep synthetic and non-sensitive. |
| `experiments/market-validated-skills/outputs/` | Saved Stage 1 model outputs. | Treat as pilot research records. |
| `experiments/market-validated-skills/scoring/` | Run logs, judge scores, diagnostics, and summary. | Main summary includes only complete judge files. |
| `experiments/market-validated-skills-stage2/sources/` | Source repository, commit, and license notes for Stage 2 selected public Skills. | Update before changing selected Skills. |
| `experiments/market-validated-skills-stage2/skill-variants/` | Stage 2 original and contractualized Skill variants plus rewrite logs. | Preserve original files unchanged for A/B comparison. |
| `experiments/market-validated-skills-stage2/tasks/` | Forty-eight synthetic Stage 2 tasks across six task types. | Keep synthetic and non-sensitive. |
| `experiments/market-validated-skills-stage2/outputs/` | Saved Stage 2 model outputs. | Treat as full-study generation records. |
| `experiments/market-validated-skills-stage2/scoring/` | Stage 2 run logs, complete judge scores, resumable scoring scripts, diagnostics, and final summary. | Analyzer deduplicates retry rows by `run_id` and includes only complete judge files. |
| `templates/contractual-skill.SKILL.md` | Blank English contractual Skill template for reuse. | Changes affect downstream users who copy the template into new domains. |
| `templates/contractual-skill.zh-CN.SKILL.md` | Blank Chinese contractual Skill template for reuse. | Keep field semantics aligned with the English template. |

## Not Included

The package should not include API keys, `.env` files, provider credentials, logs with secrets, real customer data, real contracts, production-system traces, manuscript files, or paper figure artifacts.

Synthetic task materials may describe credential-risk scenarios, but they should use non-executable placeholders rather than provider-recognizable secret formats.
