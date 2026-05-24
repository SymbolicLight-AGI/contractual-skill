# Stage 2 Freeze Manifest

## Scope

- Skills: 8.
- Tasks per Skill: 6.
- Variants: original and contractual.
- Generation models planned: `gpt-5.5`, `claude-opus-4-7`, `gemini-3.1-pro-preview`, `DeepSeek-V4-Pro`, `qwen3.6-plus`, `MiniMax-M2.7`.
- Repeats: 2.
- Planned outputs: 1152.
- Planned complete judge files: at least 2, each with 1152 successful rows.

## Design Controls

- Skill variants are paired by Skill, task, model, and repeat.
- Task prompts do not reveal which variant generated the output.
- All task materials are synthetic.
- No real customer data, credentials, production logs, or executable secrets are included.
- `MiniMax-M2.7` may emit `<think>` prefixes; scorer preserves raw output and cleans the prefix only for judge input.
