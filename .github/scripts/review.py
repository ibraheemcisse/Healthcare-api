import anthropic
import requests
import argparse
import os
import json

ARCH_CONTEXT = """
Healthcare Appointment System — Python 3.12 REST API.
Owner: Ibrahim Cisse — Infrastructure & SRE Engineer

Structure:
- app/models.py       -> Data models and validation
- app/registry.py     -> Core business logic (isolated from transport layer)
- app/utils.py        -> Utilities
- test_modules.py     -> Integration tests

Key design decisions:
- Business logic MUST stay in registry.py, never in route handlers
- UUID-based identifiers throughout
- Input validation lives in models.py
- JSON file persistence currently (migrating to PostgreSQL)
- FastAPI REST endpoints being added in Phase 2

Phases:
- Phase 1 COMPLETE: core logic, validation, file-based storage
- Phase 2 IN PROGRESS: FastAPI REST endpoints
- Phase 3 UPCOMING: PostgreSQL + migrations
- Phase 4 UPCOMING: Docker deployment
- Phase 5 PLANNED: Prometheus metrics, health checks, SLOs
"""

RULES = """
- Business logic must stay in registry.py, never in route handlers
- No direct JSON file reads/writes inside routes
- Patient PII must never appear in logs or error messages
- All ID parameters must be validated as UUIDs
- New routes must have tests in test_modules.py
- No hardcoded file paths, use config or environment variables
- Flag patterns that will break the upcoming PostgreSQL migration
- Check for race conditions in appointment scheduling
- Warn about missing error handling on file I/O operations
"""

def run_review(diff: str) -> dict:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        system="""You are a senior engineer reviewing a PR for a Python healthcare API.
Be specific, reference actual lines from the diff, and be concise.
Respond ONLY in valid JSON with no markdown fences:
{
  "summary": "2-3 sentence assessment",
  "verdict": "approve" | "request_changes" | "comment",
  "issues": [
    {
      "severity": "critical" | "warning" | "info",
      "title": "short title",
      "body": "specific explanation referencing actual code",
      "file": "filename"
    }
  ]
}""",
        messages=[{
            "role": "user",
            "content": f"ARCHITECTURE:\n{ARCH_CONTEXT}\n\nRULES:\n{RULES}\n\nDIFF:\n{diff}"
        }]
    )
    return json.loads(response.content[0].text)

def post_comment(repo: str, pr_number: int, review: dict):
    token = os.environ["GH_TOKEN"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    verdict_emoji = {
        "approve": "✅",
        "request_changes": "❌",
        "comment": "💬"
    }
    sev_emoji = {
        "critical": "🔴",
        "warning": "🟡",
        "info": "🔵"
    }

    emoji = verdict_emoji.get(review["verdict"], "💬")
    body = f"## {emoji} AI Review — {review['verdict'].replace('_', ' ').title()}\n\n"
    body += f"{review['summary']}\n\n"

    if review["issues"]:
        body += "### Issues\n\n"
        for issue in review["issues"]:
            e = sev_emoji.get(issue["severity"], "⚪")
            body += f"{e} **{issue['title']}**"
            if issue.get("file"):
                body += f" — `{issue['file']}`"
            body += f"\n\n{issue['body']}\n\n---\n\n"
    else:
        body += "✅ No issues found.\n"

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    response = requests.post(url, headers=headers, json={"body": body})
    print(f"Comment posted: {response.status_code}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--diff", required=True)
    parser.add_argument("--pr-number", type=int, required=True)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()

    with open(args.diff) as f:
        diff = f.read()

    if not diff.strip():
        print("Empty diff, nothing to review.")
        exit(0)

    review = run_review(diff)
    post_comment(args.repo, args.pr_number, review)
    print(f"Review complete: {review['verdict']}")
