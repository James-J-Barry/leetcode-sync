from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv

from .client import LeetCodeAuthError, LeetCodeClient
from .sync import render_readme, sync


def run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        capture_output=True,
        text=True,
    )


def git_has_changes(repo_root: Path) -> bool:
    result = run_git(repo_root, "status", "--porcelain")
    return bool(result.stdout.strip())


def commit_and_maybe_push(repo_root: Path, push: bool) -> None:
    run_git(repo_root, "add", "-A")
    if not git_has_changes(repo_root):
        print("No changes to commit.")
        return
    commit = run_git(repo_root, "commit", "-m", "Sync LeetCode submissions")
    if commit.returncode != 0:
        print(commit.stdout, commit.stderr, file=sys.stderr)
        sys.exit(1)
    print(commit.stdout.strip())
    if push:
        push_result = run_git(repo_root, "push")
        if push_result.returncode != 0:
            print(push_result.stdout, push_result.stderr, file=sys.stderr)
            sys.exit(1)
        print("Pushed to remote.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync your accepted LeetCode submissions into this git repo."
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the git repo to sync into (default: current directory).",
    )
    parser.add_argument(
        "--push", action="store_true", help="Push to the configured git remote after committing."
    )
    parser.add_argument(
        "--no-commit",
        action="store_true",
        help="Write files and README only; skip git add/commit.",
    )
    parser.add_argument(
        "--env-file", default=".env", help="Path to the .env file with LeetCode credentials."
    )
    args = parser.parse_args()

    load_dotenv(args.env_file)
    session_cookie = os.environ.get("LEETCODE_SESSION")
    csrf_token = os.environ.get("LEETCODE_CSRF_TOKEN")
    if not session_cookie or not csrf_token:
        print(
            "Missing LEETCODE_SESSION / LEETCODE_CSRF_TOKEN.\n"
            "Copy .env.example to .env and fill in your cookie values "
            "(see SETUP.md for how to extract them from your browser).",
            file=sys.stderr,
        )
        sys.exit(1)

    repo_root = Path(args.repo).resolve()
    client = LeetCodeClient(session_cookie, csrf_token)

    print("Fetching submissions from LeetCode...")
    try:
        all_meta = sync(client, repo_root)
    except LeetCodeAuthError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    readme = render_readme(all_meta)
    (repo_root / "README.md").write_text(readme)
    print(f"Synced {len(all_meta)} problems. Wrote README.md and solutions/.")

    if not args.no_commit:
        commit_and_maybe_push(repo_root, push=args.push)


if __name__ == "__main__":
    main()
