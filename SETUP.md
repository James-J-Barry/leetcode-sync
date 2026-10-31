# leetcode-sync setup

A small CLI that pulls every **Accepted** submission from your LeetCode
account and syncs it into this repo:

- `solutions/<id>-<slug>/solution.<ext>` for each problem (one file per
  language you solved it in)
- `README.md` regenerated as a table of every problem you've solved, with
  difficulty, topics, and a link to the solution

LeetCode has no public API for submissions, so this authenticates the same
way your browser does: by replaying your logged-in session cookie. It never
touches your LeetCode password.

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

(Use a virtualenv if you prefer: `python3 -m venv .venv && source .venv/bin/activate`.)

## 2. Get your LeetCode cookies

1. Log in to https://leetcode.com in your browser.
2. Open DevTools → Application (Chrome) or Storage (Firefox) → Cookies →
   `https://leetcode.com`.
3. Copy the values of:
   - `LEETCODE_SESSION`
   - `csrftoken`

## 3. Configure

```bash
cp .env.example .env
```

Paste the two values into `.env`:

```
LEETCODE_SESSION=<paste LEETCODE_SESSION cookie value>
LEETCODE_CSRF_TOKEN=<paste csrftoken cookie value>
```

`.env` is gitignored — never commit it. These cookies expire periodically
(LeetCode logs you out), so if the tool starts getting 401/403 errors,
re-extract fresh values.

## 4. Point it at a GitHub repo (optional)

By default the tool syncs into the repo it's run from. To push to GitHub:

```bash
git remote add origin git@github.com:<you>/<your-repo>.git
git push -u origin main   # first push, once the repo has a commit
```

After that, `--push` will push subsequent syncs automatically.

## 5. Run it

```bash
python -m leetcode_sync.cli
```

This fetches your submissions, writes solution files, regenerates
`README.md`, and commits the result. Add `--push` to also push:

```bash
python -m leetcode_sync.cli --push
```

Other flags:

- `--repo <path>` — sync into a different repo than the current directory.
- `--no-commit` — just write the files, skip git entirely.

### Re-running

Safe to run anytime. Only new or changed Accepted submissions produce a
diff; question metadata (difficulty/topics) is cached in
`.leetcode_meta_cache.json` so re-runs don't re-fetch it.

### Automating it

To keep this up to date automatically, set up a cron job or a GitHub
Action (running on a schedule, with your cookies as repo secrets) that
calls `python -m leetcode_sync.cli --push`.
