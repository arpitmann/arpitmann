"""Rewrite the 'Latest activity' block of README.md from public GitHub events.

Run by .github/workflows/activity.yml once a day. Only public events are
visible, so private repositories never appear. Standard library only.
"""
import json, os, re, sys, urllib.request
from datetime import datetime

USER = "arpitmann"
README = "README.md"
MAX_ITEMS = 6
START, END = "<!--ACTIVITY:START-->", "<!--ACTIVITY:END-->"


def fetch_events():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/events/public?per_page=100",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-activity"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def describe(ev):
    """Return a markdown line for an event, or None to skip it."""
    repo = ev["repo"]["name"]
    if repo == f"{USER}/{USER}":          # don't list edits to this profile itself
        return None
    link = f"[{repo.split('/')[1]}](https://github.com/{repo})"
    t, p = ev["type"], ev.get("payload", {})
    if t == "PushEvent":
        n = p.get("size") or len(p.get("commits", [])) or 1
        return f"pushed {n} commit{'s' if n != 1 else ''} to {link}"
    if t == "CreateEvent" and p.get("ref_type") == "repository":
        return f"created {link}"
    if t == "ReleaseEvent" and p.get("action") == "published":
        tag = p.get("release", {}).get("tag_name", "")
        return f"released {tag} of {link}"
    if t == "PublicEvent":
        return f"made {link} public"
    if t == "WatchEvent":
        return f"starred {link}"
    return None


def build(events):
    lines, seen = [], set()
    for ev in events:
        text = describe(ev)
        if not text:
            continue
        day = datetime.strptime(ev["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b %Y")
        key = (day, text)                 # collapse repeats on the same day
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- `{day}` {text}")
        if len(lines) == MAX_ITEMS:
            break
    return "\n".join(lines) or "_No public activity in the last 90 days._"


def main(events=None):
    events = fetch_events() if events is None else events
    body = build(events)
    text = open(README, encoding="utf-8").read()
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 f"{START}\n{body}\n{END}", text, flags=re.S)
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main(json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None)
