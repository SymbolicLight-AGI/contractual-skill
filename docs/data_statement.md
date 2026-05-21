# Data Statement

This replication package contains synthetic experimental materials for evaluating contractual skill structures.

## Included Data

- Synthetic enterprise task inputs for sales-growth, finance-contract, and code-review style tasks.
- Skill variants for no-skill, minimal skill, plain expanded skill, and contractual skill conditions.
- Saved model outputs from the text-generation experiment.
- Saved model-judge scoring records.
- Saved offline simulated tool-calling transcripts and scoring records.
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

The included model outputs and model-judge scores are saved records from runs completed on May 19-21, 2026. Re-running the same prompts against later model versions may produce different outputs or scores.

## Evaluation Caveat

The scores are first-pass model-assisted evaluations, not expert human ratings. They are suitable for reproducing the paper's reported analysis, but should not be treated as a universal benchmark for model capability.
