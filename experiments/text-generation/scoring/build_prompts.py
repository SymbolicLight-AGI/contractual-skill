from __future__ import annotations

import argparse
import csv
from pathlib import Path


VARIANTS = ["no-skill", "minimal", "plain-expanded", "contractual"]

FIXED_INSTRUCTION_WITH_SKILL = """请严格按照给定 Skill 完成任务。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。"""

FIXED_INSTRUCTION_NO_SKILL = """请根据任务内容完成。不要使用未提供的外部资料。若信息不足，请明确标注不确定性。最终只输出任务结果，不解释实验设置。"""


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
            FIXED_INSTRUCTION_WITH_SKILL,
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


def build_no_skill_prompt(task_text: str) -> str:
    return "\n".join(
        [
            "# Experiment Prompt",
            "",
            "## Fixed Instruction",
            "",
            FIXED_INSTRUCTION_NO_SKILL,
            "",
            "## Task",
            "",
            task_text.strip(),
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build model prompts for the contractual Skill experiment.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    root = args.root
    prompt_root = args.out or root / "prompts"
    index = read_index(root / "tasks" / "index.csv")
    count = 0

    for row in index:
        skill = row["skill"]
        task_id = row["task_id"]
        task_path = root / row["task_file"]
        task_text = task_path.read_text(encoding="utf-8")

        for variant in VARIANTS:
            if variant == "no-skill":
                prompt = build_no_skill_prompt(task_text)
            else:
                skill_path = root / "skill-variants" / variant / f"{skill}.SKILL.md"
                skill_text = skill_path.read_text(encoding="utf-8")
                prompt = build_prompt(skill_text, task_text)
            output_path = prompt_root / skill / f"{task_id}-{variant}.md"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(prompt, encoding="utf-8")
            count += 1

    print(f"Built {count} prompt file(s) in {prompt_root}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
