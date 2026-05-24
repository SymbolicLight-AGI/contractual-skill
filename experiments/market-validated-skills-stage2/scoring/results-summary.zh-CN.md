# Stage 2 Market-Validated Skill A/B Results

## Scope

- 8 market-validated Skills.
- 6 synthetic tasks per Skill.
- 2 variants: original and contractual.
- 6 generation models.
- 2 repeats.
- LLM judge scoring records are aggregated across available judge models.
- Main aggregation includes only complete judge files with 1152 successful score rows.

## Judge Inclusion

| Judge file | Total rows | OK rows | Error rows | Included |
| --- | ---: | ---: | ---: | --- |
| llm_judge_scores_gemini_31_pro_preview.csv | 1422 | 1152 | 0 | True |
| llm_judge_scores_gpt_55.csv | 1192 | 1152 | 0 | True |

## Overall By Variant

| Variant | N judge rows | Quality | Utility | Governance | Reliability | Critical error | Over-execution |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| contractual | 1152 | 4.914 | 4.924 | 4.924 | 4.896 | 0.013 | 0.003 |
| original | 1152 | 4.692 | 4.700 | 4.736 | 4.642 | 0.083 | 0.022 |

## Paired Delta

- Mean contractual minus original quality delta: `0.221`.
- Positive / tied / negative paired deltas: `496/585/71` out of `1152`.

## By Generation Model

| Model | Variant | N | Quality | Governance | Critical error | Over-execution |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| claude_opus_4_7 | contractual | 192 | 4.980 | 4.990 | 0.000 | 0.000 |
| claude_opus_4_7 | original | 192 | 4.850 | 4.891 | 0.042 | 0.016 |
| deepseek_v4_pro | contractual | 192 | 4.850 | 4.873 | 0.036 | 0.016 |
| deepseek_v4_pro | original | 192 | 4.618 | 4.672 | 0.125 | 0.042 |
| gemini_31_pro_preview | contractual | 192 | 4.923 | 4.915 | 0.000 | 0.000 |
| gemini_31_pro_preview | original | 192 | 4.573 | 4.582 | 0.083 | 0.026 |
| gpt_55 | contractual | 192 | 4.949 | 4.944 | 0.000 | 0.000 |
| gpt_55 | original | 192 | 4.870 | 4.863 | 0.016 | 0.005 |
| minimax_m27 | contractual | 192 | 4.866 | 4.896 | 0.031 | 0.005 |
| minimax_m27 | original | 192 | 4.597 | 4.696 | 0.120 | 0.016 |
| qwen36_plus | contractual | 192 | 4.915 | 4.929 | 0.010 | 0.000 |
| qwen36_plus | original | 192 | 4.643 | 4.715 | 0.115 | 0.026 |

## By Skill

| Skill | Variant | N | Quality | Governance | Critical error | Over-execution |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| api-design-principles | contractual | 144 | 4.946 | 4.975 | 0.000 | 0.000 |
| api-design-principles | original | 144 | 4.842 | 4.873 | 0.028 | 0.007 |
| brainstorming | contractual | 144 | 4.760 | 4.757 | 0.021 | 0.000 |
| brainstorming | original | 144 | 4.382 | 4.400 | 0.049 | 0.000 |
| deal-closer-playbook | contractual | 144 | 4.949 | 4.979 | 0.007 | 0.000 |
| deal-closer-playbook | original | 144 | 4.682 | 4.731 | 0.118 | 0.076 |
| dependency-auditor | contractual | 144 | 4.960 | 4.965 | 0.007 | 0.000 |
| dependency-auditor | original | 144 | 4.738 | 4.778 | 0.069 | 0.014 |
| product-manager | contractual | 144 | 4.982 | 4.998 | 0.014 | 0.000 |
| product-manager | original | 144 | 4.799 | 4.824 | 0.062 | 0.000 |
| renewal-predictor | contractual | 144 | 4.968 | 4.965 | 0.000 | 0.000 |
| renewal-predictor | original | 144 | 4.466 | 4.639 | 0.285 | 0.049 |
| security-auditor | contractual | 144 | 4.893 | 4.905 | 0.014 | 0.007 |
| security-auditor | original | 144 | 4.848 | 4.898 | 0.035 | 0.014 |
| test-driven-development | contractual | 144 | 4.850 | 4.852 | 0.042 | 0.021 |
| test-driven-development | original | 144 | 4.779 | 4.748 | 0.021 | 0.014 |

## Caveat

Stage 2 is the full market-validated Skill A/B study. It should be interpreted together with the stored task set, model outputs, judge diagnostics, and manual review caveats.
