# Contractual Skill Paper Replication Package

This is the replication package for the paper:

**Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents**

It contains synthetic tasks, skill variants, model outputs, model-judge scoring records, simulated tool-calling challenge records, and analysis scripts. The paper itself is not included because it has been published separately.

## Contents

| Path | Purpose |
| --- | --- |
| `experiments/text-generation/` | Synthetic text-generation tasks, prompts, skill variants, model outputs, scoring scripts, and scoring records. |
| `experiments/tool-calling/` | Offline simulated tool-calling challenge tasks, transcripts, scoring scripts, and scoring records. |
| `experiments/openspec-explore/` | Small old-vs-contractual comparison for the OpenSpec explore Skill. |
| `templates/` | Reusable English and Chinese contractual Skill templates for adapting the paper's structure to new domains. |
| `docs/` | Reproducibility notes, data statement, and repository file map. |

## Key Results Included

- Text-generation experiment: 8 generation models, 3 skill families, 15 synthetic tasks, 4 instruction conditions, 2 repeats, 960 model outputs, and 1680 cross-judge score records.
- Tool-calling challenge: 8 generation models and 192 offline simulated tool-call challenge records.
- OpenSpec explore Skill comparison: 2 Skill variants, 5 explore-mode tasks, 10 generated prompts, and deterministic contract-affordance scores.
- No real customer data, real contract data, real credentials, or production-system calls are included.

## Template

Reusable contractual Skill templates:

- English: `templates/contractual-skill.SKILL.md`
- Chinese: `templates/contractual-skill.zh-CN.SKILL.md`

## Reproduce Results

Create a Python environment:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

Recompute text-generation cross-judge summary:

```bash
.venv/Scripts/python experiments/text-generation/scoring/analyze_text_cross_judge.py \
  --scoring-root experiments/text-generation/scoring \
  --markdown experiments/text-generation/scoring/model-comparison-text-cross-judge.zh-CN.md
```

Recompute tool-calling model comparison:

```bash
.venv/Scripts/python experiments/tool-calling/scoring/analyze_tool_model_comparison.py \
  --scoring-root experiments/tool-calling/scoring \
  --markdown experiments/tool-calling/scoring/model-comparison-challenge.zh-CN.md
```

Recompute the OpenSpec explore Skill comparison:

```bash
.venv/Scripts/python experiments/openspec-explore/scoring/build_prompts.py
.venv/Scripts/python experiments/openspec-explore/scoring/score_contract_affordance.py
```

The included analysis scripts operate on the saved outputs and scoring CSV/JSONL files. They do not require API keys. Rerunning model generation or model-judge scoring would require external model API access and may produce different results because model versions can change.

If you rerun model generation or judge scoring, set `MODEL_BASE_URL` and `MODEL_API_KEY` locally, or pass `--base-url` explicitly. Do not commit provider credentials or `.env` files.

## Citation

Use `CITATION.cff` for repository citation metadata. If this repository is archived with Zenodo or another service, cite the archived DOI and the release tag corresponding to the published paper version.

## Notes

This package retains only experimental materials, model outputs, scoring records, and analysis scripts. It does not include the paper manuscript or figure directory.

## License

This repository is released under the MIT License. See `LICENSE`.
