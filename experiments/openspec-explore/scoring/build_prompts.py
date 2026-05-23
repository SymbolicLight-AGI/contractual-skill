from __future__ import annotations

import argparse
import csv
from pathlib import Path


VARIANTS = ["original", "contractual"]

FIXED_INSTRUCTION = """Follow the Skill under test exactly. The user is asking within OpenSpec explore mode. Do not use external sources. Do not explain the experiment setup. Output only the response you would send to the user."""


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
    parser = argparse.ArgumentParser(description="Build OpenSpec explore Skill comparison prompts.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    root = args.root
    out = args.out or root / "prompts"
    rows = read_index(root / "tasks" / "index.csv")
    count = 0

    for row in rows:
        task_id = row["task_id"]
        task_text = (root / "tasks" / f"{task_id}.md").read_text(encoding="utf-8")
        for variant in VARIANTS:
            skill_path = root / "skill-variants" / variant / "openspec-explore.SKILL.md"
            skill_text = skill_path.read_text(encoding="utf-8")
            prompt = build_prompt(skill_text, task_text)
            output_path = out / variant / f"{task_id}.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(prompt, encoding="utf-8")
            count += 1

    print(f"Built {count} prompt file(s) in {out}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
