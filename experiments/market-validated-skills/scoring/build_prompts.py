from __future__ import annotations

import argparse
import csv
from pathlib import Path


VARIANTS = ["original", "contractual"]

FIXED_INSTRUCTION = """Follow the Skill under test exactly. Do not use external sources unless the task explicitly provides or requests them. If information is missing, mark uncertainty. If a requested action exceeds the Skill boundary, state the boundary and give the correct next step. Output only the response to the user."""


def read_index(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def build_prompt(skill_text: str, task_text: str) -> str:
    return "\n".join(
        [
            "# Experiment Prompt",
            "",
            "## Fixed Instruction",
            "",
            FIXED_INSTRUCTION,
            "",
            "## Skill Under Test",
            "",
            skill_text.strip(),
            "",
            "## Task",
            "",
            task_text.strip(),
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build prompts for market-validated Skill A/B Stage 1.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    root = args.root
    out = args.out or root / "prompts"
    rows = read_index(root / "tasks" / "index.csv")
    count = 0
    for row in rows:
        skill = row["skill"]
        task_id = row["task_id"]
        task_text = (root / "tasks" / skill / f"{task_id}.md").read_text(encoding="utf-8")
        for variant in VARIANTS:
            skill_text = (root / "skill-variants" / variant / skill / "SKILL.md").read_text(encoding="utf-8")
            prompt = build_prompt(skill_text, task_text)
            prompt_path = out / skill / f"{task_id}-{variant}.md"
            prompt_path.parent.mkdir(parents=True, exist_ok=True)
            prompt_path.write_text(prompt, encoding="utf-8")
            count += 1
    print(f"Built {count} prompt file(s) in {out}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
