from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from .client import LeetCodeClient, QuestionMeta
from .languages import extension_for

@dataclass
class SolvedProblem:
    meta: QuestionMeta
    solved_at: int  # unix timestamp of the most recent Accepted submission


def collect_latest_accepted(client: LeetCodeClient) -> dict[str, dict]:
    """Walk the submission history and keep the newest Accepted submission
    per (problem, language) pair, so multi-language solutions are all kept."""
    latest: dict[tuple[str, str], dict] = {}
    for sub in client.iter_all_submissions():
        if not sub.is_accepted:
            continue
        key = (sub.title_slug, sub.lang)
        existing = latest.get(key)
        if existing is None or sub.timestamp > existing["timestamp"]:
            latest[key] = {
                "title": sub.title,
                "title_slug": sub.title_slug,
                "lang": sub.lang,
                "timestamp": sub.timestamp,
                "code": sub.code,
            }
    # group by slug -> {lang: entry}
    by_slug: dict[str, dict] = {}
    for (slug, lang), entry in latest.items():
        by_slug.setdefault(slug, {})[lang] = entry
    return by_slug


def load_meta_cache(cache_path: Path) -> dict[str, dict]:
    if cache_path.exists():
        return json.loads(cache_path.read_text())
    return {}


def save_meta_cache(cache_path: Path, cache: dict[str, dict]) -> None:
    cache_path.write_text(json.dumps(cache, indent=2, sort_keys=True))


def sync(
    client: LeetCodeClient,
    repo_root: Path,
    solutions_dirname: str = "solutions",
    cache_filename: str = ".leetcode_meta_cache.json",
) -> list[SolvedProblem]:
    solutions_dir = repo_root / solutions_dirname
    solutions_dir.mkdir(parents=True, exist_ok=True)
    cache_path = repo_root / cache_filename
    meta_cache = load_meta_cache(cache_path)

    by_slug = collect_latest_accepted(client)
    solved: list[SolvedProblem] = []

    for slug, by_lang in sorted(by_slug.items()):
        if slug in meta_cache:
            cached = meta_cache[slug]
            meta = QuestionMeta(
                frontend_id=cached["frontend_id"],
                title=cached["title"],
                title_slug=cached["title_slug"],
                difficulty=cached["difficulty"],
                topics=cached["topics"],
            )
        else:
            meta = client.get_question_meta(slug)
            meta_cache[slug] = {
                "frontend_id": meta.frontend_id,
                "title": meta.title,
                "title_slug": meta.title_slug,
                "difficulty": meta.difficulty,
                "topics": meta.topics,
            }
        solved_at = max(entry["timestamp"] for entry in by_lang.values())
        solved.append(SolvedProblem(meta=meta, solved_at=solved_at))

        problem_dir = solutions_dir / f"{meta.frontend_id}-{slug}"
        problem_dir.mkdir(parents=True, exist_ok=True)
        for lang, entry in by_lang.items():
            ext = extension_for(lang)
            (problem_dir / f"solution.{ext}").write_text(entry["code"])

    save_meta_cache(cache_path, meta_cache)
    return sorted(solved, key=lambda s: s.solved_at, reverse=True)


def render_readme(solved: list[SolvedProblem], solutions_dirname: str = "solutions") -> str:
    lines = [
        "# LeetCode Progress",
        "",
        f"Synced {len(solved)} solved problems, most recently submitted first.",
        "",
        "| Submitted | # | Title | Difficulty | Topics | Solution |",
        "|-----------|---|-------|------------|--------|----------|",
    ]
    for s in solved:
        m = s.meta
        date = datetime.fromtimestamp(s.solved_at, tz=timezone.utc).strftime("%Y-%m-%d")
        topics = ", ".join(m.topics)
        link = f"{solutions_dirname}/{m.frontend_id}-{m.title_slug}/"
        lc_link = f"https://leetcode.com/problems/{m.title_slug}/"
        lines.append(
            f"| {date} | {m.frontend_id} | [{m.title}]({lc_link}) | {m.difficulty} | {topics} | [solution]({link}) |"
        )
    lines.append("")
    return "\n".join(lines)
