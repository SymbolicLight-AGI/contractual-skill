from __future__ import annotations

import argparse
import json
import os
import random
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


BASE_URL_ENV = "MODEL_BASE_URL"
API_KEY_ENV = "MODEL_API_KEY"


def slug(value: str) -> str:
    return (
        value.lower()
        .replace(".", "")
        .replace("-", "_")
        .replace("/", "_")
    )


def chat_completion(*, base_url: str, api_key: str, model: str, prompt: str, timeout: int) -> str:
    endpoint = base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "stream": False,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body[:800]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"URL error: {exc.reason}") from exc

    data = json.loads(body)
    choices = data.get("choices") or []
    if not choices:
        raise RuntimeError(f"No choices returned: {body[:800]}")
    message = choices[0].get("message") or {}
    content = message.get("content")
    if content:
        return content
    delta = choices[0].get("delta") or {}
    content = delta.get("content")
    if content:
        return content
    raise RuntimeError(f"No message content returned: {body[:800]}")


def prompt_files(prompt_root: Path, limit: int | None) -> list[Path]:
    files = sorted(prompt_root.rglob("*.md"))
    if limit is not None:
        files = files[:limit]
    return files


def output_path_for(prompt_path: Path, prompt_root: Path, outputs_root: Path, repeat: int) -> Path:
    relative = prompt_path.relative_to(prompt_root)
    skill = relative.parent
    return outputs_root / skill / f"{prompt_path.stem}-r{repeat}.md"


def write_jsonl(path: Path, record: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def run_one(
    *,
    base_url: str,
    api_key: str,
    model: str,
    model_slug: str,
    prompt_path: Path,
    prompt_root: Path,
    root: Path,
    out_path: Path,
    repeat: int,
    timeout: int,
) -> dict[str, object]:
    prompt = prompt_path.read_text(encoding="utf-8")
    started = time.time()
    status = "ok"
    error = ""
    try:
        content = chat_completion(
            base_url=base_url,
            api_key=api_key,
            model=model,
            prompt=prompt,
            timeout=timeout,
        )
    except Exception as exc:  # noqa: BLE001
        status = "error"
        error = str(exc)
        content = f"EXPERIMENT_ERROR: {error}"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content.strip() + "\n", encoding="utf-8")
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "model": model,
        "model_slug": model_slug,
        "prompt_file": str(prompt_path.relative_to(root)),
        "output_file": str(out_path.relative_to(root)),
        "repeat": repeat,
        "status": status,
        "elapsed_seconds": round(time.time() - started, 3),
        "error": error[:800],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run model outputs for Stage 2 market-validated Skills.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base-url", default=os.environ.get(BASE_URL_ENV))
    parser.add_argument("--model", required=True)
    parser.add_argument("--repeats", type=int, default=2)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--sleep", type=float, default=0.2)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--shuffle", action="store_true")
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    if not args.base_url:
        raise SystemExit(f"Set --base-url or {BASE_URL_ENV}.")
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        raise SystemExit(f"{API_KEY_ENV} is not set.")

    prompt_root = args.root / "prompts"
    model_slug = slug(args.model)
    outputs_root = args.root / "outputs" / model_slug
    runs_jsonl = args.root / "scoring" / f"runs_{model_slug}.jsonl"

    files = prompt_files(prompt_root, args.limit)
    if args.shuffle:
        random.Random(20260523).shuffle(files)
    total = len(files) * args.repeats
    completed = 0
    jobs: list[tuple[Path, Path, int]] = []
    print(f"Starting model={args.model}; prompts={len(files)}; repeats={args.repeats}; total={total}")
    for prompt_path in files:
        for repeat in range(1, args.repeats + 1):
            out_path = output_path_for(prompt_path, prompt_root, outputs_root, repeat)
            if out_path.exists() and not args.overwrite:
                completed += 1
                print(f"[{completed}/{total}] skip {out_path}")
                continue
            jobs.append((prompt_path, out_path, repeat))

    workers = max(1, args.workers)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                run_one,
                base_url=args.base_url,
                api_key=api_key,
                model=args.model,
                model_slug=model_slug,
                prompt_path=prompt_path,
                prompt_root=prompt_root,
                root=args.root,
                out_path=out_path,
                repeat=repeat,
                timeout=args.timeout,
            )
            for prompt_path, out_path, repeat in jobs
        ]
        for future in as_completed(futures):
            record = future.result()
            completed += 1
            write_jsonl(runs_jsonl, record)
            print(
                f"[{completed}/{total}] {record['status']} "
                f"{args.root / str(record['output_file'])} ({record['elapsed_seconds']}s)"
            )
            if args.sleep:
                time.sleep(args.sleep)
    print("Run complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
