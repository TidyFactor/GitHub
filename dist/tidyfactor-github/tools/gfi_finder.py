#!/usr/bin/env python3
"""
gfi_finder.py — Good First Issue Candidate Finder & Scoper
Inspects repository issues, filters by complexity and scope, and formats beginner-ready issues.
"""

import sys
import os
import json
import subprocess

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def find_gfi_candidates(repo=None):
    print("=" * 70)
    print("  GOOD FIRST ISSUE (GFI) CANDIDATE FINDER")
    print("=" * 70)

    cmd = ["gh", "issue", "list", "--limit", "30", "--json", "number,title,labels,body"]
    if repo:
        cmd.extend(["--repo", repo])

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode != 0 or not res.stdout.strip():
            print("  ℹ️ No issues found or gh CLI not configured for target repo.")
            return []
        issues = json.loads(res.stdout)
    except Exception as e:
        print(f"  ℹ️ Could not query GitHub issues: {e}")
        return []

    candidates = []
    for iss in issues:
        title = iss.get("title", "").lower()
        body = iss.get("body", "").lower()
        labels = [l.get("name", "").lower() for l in iss.get("labels", [])]

        # Scoring heuristics
        is_beginner = False
        difficulty = "Medium"
        effort = "2-4 hours"

        if "doc" in title or "typo" in title or "readme" in title or "documentation" in labels:
            is_beginner = True
            difficulty = "Easy"
            effort = "30-60 mins"
        elif "good first issue" in labels or "help wanted" in labels:
            is_beginner = True
            difficulty = "Easy"
            effort = "1-2 hours"
        elif len(body) < 500 and "bug" in labels:
            is_beginner = True
            difficulty = "Medium"
            effort = "2-3 hours"

        if is_beginner:
            candidates.append({
                "number": iss.get("number"),
                "title": iss.get("title"),
                "difficulty": difficulty,
                "estimated_effort": effort,
                "labels": labels
            })

    print(f"\n  Found {len(candidates)} Good First Issue candidates:\n")
    for c in candidates:
        print(f"  #{c['number']:<4} [{c['difficulty']}] {c['title']} (Effort: {c['estimated_effort']})")
    print("=" * 70)
    return candidates

if __name__ == "__main__":
    repo_arg = sys.argv[1] if len(sys.argv) > 1 else None
    find_gfi_candidates(repo_arg)
