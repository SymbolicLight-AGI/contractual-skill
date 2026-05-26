<div align="center">

<h1>Contractual Skill</h1>

<p><strong>Contract-style AI agent skills for safer tool use, clearer evaluation, and enterprise governance.</strong></p>

<p><em>Works with Codex, Claude Code, Cursor, Copilot, Gemini CLI, and any <code>SKILL.md</code>-style agent runtime.</em></p>

<p>
  <img src="assets/contractual-skill-showcase.svg" width="430" alt="Contractual Skill open framework badge" />
</p>

<p>
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">简体中文</a> |
  <a href="templates/">Templates</a> |
  <a href="experiments/">Experiments</a> |
  <a href="#paper">Paper</a>
</p>

<p>
  <a href="#start-here"><img alt="Quick Start" src="https://img.shields.io/badge/Quick%20Start-Templates-0b83c9?style=flat-square" /></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-d4b000?style=flat-square" /></a>
  <a href="templates/contractual-skill.SKILL.md"><img alt="Template: SKILL.md" src="https://img.shields.io/badge/SKILL.md-Contractual-6f42c1?style=flat-square" /></a>
  <a href="experiments/"><img alt="Experiments" src="https://img.shields.io/badge/Experiments-1%2C152%20outputs-157347?style=flat-square" /></a>
  <a href="CITATION.cff"><img alt="Citation metadata" src="https://img.shields.io/badge/Citation-CFF-59636e?style=flat-square" /></a>
</p>

</div>

---

Contractual Skill is an open framework for writing AI agent skills as explicit task contracts.

It turns implicit prompt instructions into inspectable fields such as goals, audience, context, permissions, constraints, evidence requirements, output format, quality bars, and verification criteria. The goal is to make agent behavior easier to reuse, evaluate, audit, and govern, especially in enterprise workflows where skills call tools, handle incomplete evidence, or operate under safety constraints.

This repository provides reusable templates, experimental materials, model outputs, scoring records, and analysis scripts behind the paper **Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents**.

![Contractual Skill framework overview](assets/contractual-skill-overview.svg)

## Why Contractual Skills

Most AI agent skills are written as free-form instructions. That makes them flexible, but it also makes important behavior hard to inspect:

- What is the skill actually trying to accomplish?
- What evidence is required before it should answer?
- Which actions are allowed, blocked, or require human approval?
- How should uncertainty, missing data, and high-risk requests be handled?
- What counts as a good output?
- How can two versions of the same skill be compared?

Contractual Skills add a lightweight contract layer to regular `SKILL.md` files. They do not replace the agent runtime, tool adapter, or permission system. Instead, they make task intent, operating boundaries, and acceptance criteria explicit enough for humans, evaluators, and runtime components to inspect.

## Framework at a Glance

| Layer | What becomes explicit | Why it matters |
| --- | --- | --- |
| Skill contract | Goal, audience, context, constraints, output shape, and quality bar | Humans can inspect intent before the agent acts. |
| Evidence policy | Source requirements, uncertainty marking, and fact-vs-inference separation | Evaluators can identify unsupported claims and missing inputs. |
| Permission boundary | Allowed actions, blocked actions, and human-gated operations | Tool adapters and reviewers can reason about safe execution. |
| Verification | Required checks, tests, review criteria, and acceptance gates | Skill versions can be compared with more stable criteria. |

## Start Here

Use the template:

```bash
cp templates/contractual-skill.SKILL.md my-skill.SKILL.md
```

Or start from the Chinese template:

```bash
cp templates/contractual-skill.zh-CN.SKILL.md my-skill.zh-CN.SKILL.md
```

Then customize the main contract fields:

| Field | Purpose |
| --- | --- |
| `Goal` | What the skill should accomplish. |
| `Audience` | Who the output is for. |
| `Context` | Domain facts, assumptions, vocabulary, and operating background. |
| `Permissions` | Allowed, blocked, and human-gated actions. |
| `Constraints` | Hard behavioral boundaries and safety rules. |
| `Evidence` | Required sources, uncertainty handling, and fact-vs-inference rules. |
| `Output` | Format, language, sections, and delivery shape. |
| `Quality Bar` | Criteria for a useful, complete, and trustworthy result. |
| `Verification` | Checks, tests, or review criteria before considering the skill complete. |

## Repository Contents

| Path | Purpose |
| --- | --- |
| `templates/` | Reusable English and Chinese Contractual Skill templates. |
| `experiments/text-generation/` | Synthetic text-generation tasks, prompts, skill variants, model outputs, scoring scripts, and scoring records. |
| `experiments/tool-calling/` | Offline simulated tool-calling challenge tasks, transcripts, scoring scripts, and scoring records. |
| `experiments/openspec-explore/` | Small old-vs-contractual comparison for the OpenSpec explore Skill. |
| `experiments/market-validated-skills/` | Stage 1 A/B pilot comparing market-validated original Skills with contractualized versions. |
| `experiments/market-validated-skills-stage2/` | Stage 2 expanded market-validated Skill materials, generated outputs, judge scoring records, and final summary. |
| `docs/` | Reproduction notes, experiment design notes, data statement, and repository file map. |

## Templates

The repository includes two starter templates:

- English: `templates/contractual-skill.SKILL.md`
- Chinese: `templates/contractual-skill.zh-CN.SKILL.md`

The templates are intended to be adapted, not treated as a fixed standard. Different domains may need different sections, but the core idea is stable: make the skill's purpose, boundaries, evidence requirements, and verification criteria explicit.

## Experiments

This repository also includes the experimental artifacts used to evaluate Contractual Skills against original or less structured Skill variants.

![Stage 2 result summary](assets/stage2-results.svg)

Included results:

- Text-generation experiment: 8 generation models, 3 skill families, 15 synthetic tasks, 4 instruction conditions, 2 repeats, 960 model outputs, and 1680 cross-judge score records.
- Tool-calling challenge: 8 generation models and 192 offline simulated tool-call challenge records.
- OpenSpec explore Skill comparison: 2 Skill variants, 5 explore-mode tasks, 10 generated prompts, and deterministic contract-affordance scores.
- Market-validated Skill Stage 1 pilot: 4 public Skills, 16 synthetic tasks, 2 variants, 4 generation models, 2 repeats, 256 model outputs, 512 complete main judge rows, plus 233 diagnostic Claude judge rows.
- Market-validated Skill Stage 2 expanded study: 8 public Skills, 48 synthetic tasks, 2 variants, 6 generation models, 2 repeats, 1152 model outputs, and two complete judge files with 2304 successful deduplicated score rows.

Main Stage 2 result:

| Metric | Original Skill | Contractual Skill | Change |
| --- | ---: | ---: | ---: |
| Mean quality | 4.692 | 4.914 | +0.222 |
| Critical-error rate | 0.083 | 0.013 | -0.070 |
| Relative critical-error reduction | 100% baseline | 15.7% of baseline | -84.3% |

Scale of the Stage 2 study:

| Skills | Tasks | Generation models | Repeats | Model outputs | Deduplicated judge rows |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 48 | 6 | 2 | 1,152 | 2,304 |

These experiments are not meant to claim that every skill always improves after contractualization. They are meant to test whether a contract-style structure can make skills more reliable, auditable, and comparable across realistic agent tasks.

## Reproduce Saved Results

The included analysis scripts operate on saved outputs and scoring CSV/JSONL files. Recomputing summaries does not require an API key.

Create a Python environment:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

Recompute the text-generation cross-judge summary:

```bash
.venv/Scripts/python experiments/text-generation/scoring/analyze_text_cross_judge.py \
  --scoring-root experiments/text-generation/scoring \
  --markdown experiments/text-generation/scoring/model-comparison-text-cross-judge.zh-CN.md
```

Recompute the tool-calling model comparison:

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

Recompute the market-validated Skill summaries:

```bash
.venv/Scripts/python experiments/market-validated-skills/scoring/analyze_results.py
.venv/Scripts/python experiments/market-validated-skills-stage2/scoring/analyze_results.py
```

Rerunning model generation or model-judge scoring requires external model API access and may produce different results because hosted model versions can change. If you rerun generation or judging, set `MODEL_BASE_URL` and `MODEL_API_KEY` locally, or pass `--base-url` where supported. Do not commit provider credentials or `.env` files.

## Data and Safety Notice

This repository contains synthetic tasks, synthetic tool-call challenges, saved model outputs, scoring records, and analysis scripts.

It does not include:

- Real customer data
- Real contract data
- Real credentials
- Real production-system calls
- Private paper drafts or paper figure directories

Some experiment files intentionally contain synthetic secret-like strings or risky scenario descriptions so that tool-calling and safety behavior can be evaluated. These are test artifacts, not live credentials.

## Paper

This repository supports the paper:

[Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents](https://arxiv.org/abs/2605.22634v2)

Project website: coming soon.

Use `CITATION.cff` for repository citation metadata. If this repository is archived with Zenodo or another service, cite the archived DOI and the release tag corresponding to the paper version.

## Project Status

This is a research-oriented open repository. The templates and evaluation materials are intended to help practitioners and researchers explore contract-style skill design for AI agents.

The framework is lightweight by design. Runtime enforcement still depends on the surrounding agent system, tool adapter, permission layer, logging, and human review process.

## License

This repository is released under the MIT License. See `LICENSE`.

## Maintainer

This project is maintained by Ting Liu, SymbolicLight Research.
