"""Thin client for the (unofficial) LeetCode submissions API.

LeetCode has no public OAuth API for submissions, so this authenticates the
same way the website does in your browser: by replaying your logged-in
session cookie. See the top-level README for how to obtain the cookie
values.
"""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

import requests

LEETCODE_BASE = "https://leetcode.com"
GRAPHQL_URL = f"{LEETCODE_BASE}/graphql"
SUBMISSIONS_URL = f"{LEETCODE_BASE}/api/submissions/"

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    topicTags {
      name
    }
  }
}
"""


class LeetCodeAuthError(RuntimeError):
    pass


@dataclass
class Submission:
    id: int
    title: str
    title_slug: str
    status_display: str
    lang: str
    timestamp: int
    code: str

    @property
    def is_accepted(self) -> bool:
        return self.status_display == "Accepted"


@dataclass
class QuestionMeta:
    frontend_id: str
    title: str
    title_slug: str
    difficulty: str
    topics: list[str]


class LeetCodeClient:
    def __init__(self, session_cookie: str, csrf_token: str, request_delay: float = 0.75):
        self.session = requests.Session()
        self.session.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
        self.session.cookies.set("csrftoken", csrf_token, domain="leetcode.com")
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (leetcode-sync personal tool)",
                "Referer": "https://leetcode.com/",
                "x-csrftoken": csrf_token,
                "Content-Type": "application/json",
            }
        )
        self.request_delay = request_delay

    def _get(self, url: str, params: dict[str, Any]) -> dict[str, Any]:
        resp = self.session.get(url, params=params, timeout=30)
        if resp.status_code in (401, 403):
            raise LeetCodeAuthError(
                "LeetCode rejected the request (401/403). Your LEETCODE_SESSION "
                "or csrftoken cookie is likely missing or expired — re-extract "
                "them from your browser and update your .env file."
            )
        resp.raise_for_status()
        return resp.json()

    def iter_all_submissions(self):
        """Yield every submission (any status/language), newest first."""
        offset = 0
        limit = 20
        last_key: str | None = None
        while True:
            params: dict[str, Any] = {"offset": offset, "limit": limit}
            if last_key:
                params["lastkey"] = last_key
            data = self._get(SUBMISSIONS_URL, params)
            dump = data.get("submissions_dump", [])
            if not dump:
                break
            for item in dump:
                yield Submission(
                    id=item["id"],
                    title=item["title"],
                    title_slug=item["title_slug"],
                    status_display=item["status_display"],
                    lang=item["lang"],
                    timestamp=int(item["timestamp"]),
                    code=item.get("code", ""),
                )
            if not data.get("has_next"):
                break
            offset += limit
            last_key = data.get("last_key")
            time.sleep(self.request_delay)

    def get_question_meta(self, title_slug: str) -> QuestionMeta:
        payload = {
            "operationName": "questionData",
            "query": QUESTION_QUERY,
            "variables": {"titleSlug": title_slug},
        }
        resp = self.session.post(GRAPHQL_URL, json=payload, timeout=30)
        if resp.status_code in (401, 403):
            raise LeetCodeAuthError("LeetCode rejected the GraphQL request (401/403).")
        resp.raise_for_status()
        q = resp.json()["data"]["question"]
        return QuestionMeta(
            frontend_id=q["questionFrontendId"],
            title=q["title"],
            title_slug=q["titleSlug"],
            difficulty=q["difficulty"],
            topics=[t["name"] for t in q["topicTags"]],
        )
