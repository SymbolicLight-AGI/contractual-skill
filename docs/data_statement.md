# Data Statement

This replication package contains synthetic experimental materials for evaluating contractual skill structures.

## Included Data

- Synthetic enterprise task inputs for sales-growth, finance-contract, and code-review style tasks.
- Skill variants for no-skill, minimal skill, plain expanded skill, and contractual skill conditions.
- Saved model outputs from the text-generation experiment.
- Saved model-judge scoring records.
- Saved offline simulated tool-calling transcripts and scoring records.
- A small OpenSpec explore Skill comparison containing one original public Skill file, one contractual rewrite, five synthetic explore-mode tasks, generated prompts, and deterministic contract-affordance scores.
- A Stage 1 market-validated Skill A/B pilot containing public original Skills, contractualized rewrites, synthetic tasks, model outputs, run logs, LLM judge scores, and diagnostics.
- A Stage 2 market-validated Skill A/B expansion containing eight public original Skills, contractualized rewrites, forty-eight synthetic tasks, 1152 saved model outputs, run logs, two complete LLM judge scoring files, and final aggregate summaries.
- Scripts used to aggregate scores.

## Excluded Data

This package does not include:

- real customer records;
- real contracts;
- real personal contact details;
- real API keys or service credentials;
- real CRM, email, repository, contract-system, or production-system calls;
- private provider account metadata.

Synthetic security and payment examples use non-executable placeholders. They are included only to test whether models identify credential-risk patterns and should not be interpreted as real service credentials.

## Model Output Caveat

The included model outputs and model-judge scores are saved records from runs completed on May 19-24, 2026. Re-running the same prompts against later model versions may produce different outputs or scores.

## Evaluation Caveat

The scores are first-pass model-assisted evaluations, not expert human ratings. They are suitable for reproducing the paper's reported analysis, but should not be treated as a universal benchmark for model capability.

The OpenSpec explore Skill comparison is a deterministic contract-affordance check. It measures whether the Skill text explicitly exposes task-relevant contract signals, not whether a live model will always follow those signals.

The market-validated Skill Stage 1 experiment is a pilot study. Its results are useful for calibration and exploratory analysis.

The market-validated Skill Stage 2 records include complete generation outputs and two complete judge score files. Raw judge CSV/JSONL files retain earlier failed retry attempts for auditability; the analyzer deduplicates by `run_id` and prefers successful rows over earlier error rows.
