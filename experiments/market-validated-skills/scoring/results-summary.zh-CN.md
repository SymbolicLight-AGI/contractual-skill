# Stage 1 Market-Validated Skill A/B Results

## Scope

- 4 market-validated Skills.
- 4 synthetic tasks per Skill.
- 2 variants: original and contractual.
- 4 generation models.
- 2 repeats.
- LLM judge scoring records are aggregated across available judge models.
- Main aggregation includes only complete judge files with 256 successful score rows.

## Judge Inclusion

| Judge file | Total rows | OK rows | Error rows | Included |
| --- | ---: | ---: | ---: | --- |
| llm_judge_scores_claude_opus_4_7.csv | 256 | 233 | 23 | False |
| llm_judge_scores_deepseek_v4_pro.csv | 256 | 256 | 0 | True |
| llm_judge_scores_gpt_55.csv | 256 | 256 | 0 | True |

## Overall By Variant

| Variant | N judge rows | Quality | Utility | Governance | Reliability | Critical error | Over-execution |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| contractual | 256 | 4.783 | 4.721 | 4.764 | 4.842 | 0.031 | 0.004 |
| original | 256 | 4.604 | 4.541 | 4.655 | 4.594 | 0.082 | 0.051 |

## Paired Delta

- Mean contractual minus original quality delta: `0.179`.
- Positive paired deltas: `109/256`.

## By Generation Model

| Model | Variant | N | Quality | Governance | Critical error | Over-execution |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| claude_opus_4_7 | contractual | 64 | 4.834 | 4.849 | 0.000 | 0.000 |
| claude_opus_4_7 | original | 64 | 4.654 | 4.792 | 0.031 | 0.016 |
| deepseek_v4_pro | contractual | 64 | 4.711 | 4.714 | 0.047 | 0.000 |
| deepseek_v4_pro | original | 64 | 4.492 | 4.516 | 0.188 | 0.109 |
| gpt_55 | contractual | 64 | 4.881 | 4.813 | 0.000 | 0.000 |
| gpt_55 | original | 64 | 4.873 | 4.859 | 0.000 | 0.000 |
| minimax_m27 | contractual | 64 | 4.705 | 4.682 | 0.078 | 0.016 |
| minimax_m27 | original | 64 | 4.395 | 4.453 | 0.109 | 0.078 |

## By Skill

| Skill | Variant | N | Quality | Governance | Critical error | Over-execution |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| brainstorming | contractual | 64 | 4.646 | 4.453 | 0.016 | 0.000 |
| brainstorming | original | 64 | 4.541 | 4.484 | 0.047 | 0.000 |
| deal-closer-playbook | contractual | 64 | 4.846 | 4.943 | 0.078 | 0.000 |
| deal-closer-playbook | original | 64 | 4.432 | 4.620 | 0.219 | 0.156 |
| security-auditor | contractual | 64 | 4.912 | 4.948 | 0.000 | 0.000 |
| security-auditor | original | 64 | 4.812 | 4.932 | 0.000 | 0.000 |
| test-driven-development | contractual | 64 | 4.727 | 4.714 | 0.031 | 0.016 |
| test-driven-development | original | 64 | 4.629 | 4.583 | 0.062 | 0.047 |

## Caveat

Stage 1 is a pilot study for calibration. It should be interpreted as exploratory evidence, not a final benchmark.
