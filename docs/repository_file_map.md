# Repository File Map

## Overview

- Project: Contractual Skill Evaluation Artifacts
- Stage: published replication package
- Last updated: 2026-05-22

## Top-Level Structure

| Path | Purpose | Maintenance Note |
| --- | --- | --- |
| `experiments/text-generation/` | Synthetic text-generation experiment package. | Do not overwrite saved model outputs unless creating a new release/version. |
| `experiments/tool-calling/` | Offline simulated tool-calling challenge package. | Simulated tools only; no real external system calls should be added. |
| `experiments/openspec-explore/` | Small old-vs-contractual OpenSpec explore Skill comparison. | Keep original and contractual variants side by side for traceability. |
| `templates/` | Reusable English and Chinese contractual Skill templates. | Keep generic, non-sensitive, and aligned with the contractual examples. |
| `docs/` | Reproducibility notes, data statement, and this file map. | Update when the package structure changes. |

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
| `templates/contractual-skill.SKILL.md` | Blank English contractual Skill template for reuse. | Changes affect downstream users who copy the template into new domains. |
| `templates/contractual-skill.zh-CN.SKILL.md` | Blank Chinese contractual Skill template for reuse. | Keep field semantics aligned with the English template. |

## Not Included

The package should not include API keys, `.env` files, provider credentials, logs with secrets, real customer data, real contracts, production-system traces, manuscript files, or paper figure artifacts.

Synthetic task materials may describe credential-risk scenarios, but they should use non-executable placeholders rather than provider-recognizable secret formats.
