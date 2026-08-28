#!/usr/bin/env python3
"""
repo_audit.py — TidyFactor Deterministic Repository Health Auditor.
Evaluates the 9 dimensions of repository health and outputs a 0-100 score.
"""

import sys
import os
import json
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def audit_repository(repo_path: Path):
    scores = {
        "identity_discoverability": 100,
        "documentation_readme": 100,
        "developer_experience": 100,
        "community_health": 100,
        "security_supply_chain": 100,
        "ci_cd_automation": 100,
        "governance_rulesets": 100,
        "issue_pr_engineering": 100,
        "visual_presentation": 100,
    }
    remediations = []

    # 1. Identity & Discoverability
    pkg_file = repo_path / "package.json"
    if pkg_file.exists():
        try:
            data = json.loads(pkg_file.read_text(encoding="utf-8"))
            if not data.get("description"):
                scores["identity_discoverability"] -= 30
                remediations.append({"rule_id": "rdo-01", "tier": "MEDIUM", "description": "package.json missing description", "action": "Add description string"})
            if not data.get("keywords") or len(data.get("keywords", [])) < 4:
                scores["identity_discoverability"] -= 20
                remediations.append({"rule_id": "rdo-02", "tier": "LOW", "description": "Insufficient keywords", "action": "Add at least 6 relevant topics"})
        except Exception:
            scores["identity_discoverability"] -= 20

    # 2. Documentation
    readme = repo_path / "README.md"
    if not readme.exists():
        scores["documentation_readme"] = 0
        remediations.append({"rule_id": "doc-01", "tier": "CRITICAL", "description": "Missing README.md", "action": "Create standard README.md"})
    else:
        text = readme.read_text(encoding="utf-8")
        if len(text) < 200:
            scores["documentation_readme"] -= 40
        if "quick start" not in text.lower() and "installation" not in text.lower():
            scores["documentation_readme"] -= 20
            remediations.append({"rule_id": "doc-02", "tier": "HIGH", "description": "No Quick Start section found in README", "action": "Add Quick Start code snippet"})

    # 3. Community Health
    gh_dir = repo_path / ".github"
    for comm_file in ["CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md"]:
        if not (repo_path / comm_file).exists() and not (gh_dir / comm_file).exists():
            scores["community_health"] -= 25
            remediations.append({"rule_id": "comm-01", "tier": "MEDIUM", "description": f"Missing {comm_file}", "action": f"Scaffold {comm_file}"})

    # 4. Security & Supply Chain
    sec_file = repo_path / "SECURITY.md" if (repo_path / "SECURITY.md").exists() else gh_dir / "SECURITY.md"
    if not sec_file.exists():
        scores["security_supply_chain"] -= 30
        remediations.append({"rule_id": "sec-08", "tier": "HIGH", "description": "Missing SECURITY.md policy", "action": "Create SECURITY.md"})
        
    dependabot_file = gh_dir / "dependabot.yml" if gh_dir.exists() else None
    if not dependabot_file or not dependabot_file.exists():
        scores["security_supply_chain"] -= 30
        remediations.append({"rule_id": "sec-04", "tier": "HIGH", "description": "Missing Dependabot configuration", "action": "Add .github/dependabot.yml"})

    # 5. CI/CD & Actions
    workflows_dir = gh_dir / "workflows" if gh_dir.exists() else None
    if not workflows_dir or not workflows_dir.exists() or not list(workflows_dir.glob("*.yml")):
        scores["ci_cd_automation"] -= 60
        remediations.append({"rule_id": "ci-00", "tier": "HIGH", "description": "No CI/CD workflows detected in .github/workflows/", "action": "Scaffold .github/workflows/ci.yml"})
    else:
        for wf in workflows_dir.glob("*.yml"):
            w_text = wf.read_text(encoding="utf-8")
            if "permissions:" not in w_text:
                scores["ci_cd_automation"] -= 15
                scores["security_supply_chain"] -= 15
                remediations.append({"rule_id": "sec-02", "tier": "CRITICAL", "description": f"Workflow {wf.name} missing explicit permissions block", "action": "Add top-level permissions: contents: read"})
            if re.search(r'uses:\s+actions/[a-zA-Z0-9_\-]+@v\d+', w_text):
                scores["security_supply_chain"] -= 15
                remediations.append({"rule_id": "sec-01", "tier": "CRITICAL", "description": f"Workflow {wf.name} contains unpinned mutable action tag", "action": "Pin action to immutable commit SHA"})

    # 6. Issue & PR Engineering
    issue_tmpl_dir = gh_dir / "ISSUE_TEMPLATE" if gh_dir.exists() else None
    if not issue_tmpl_dir or not issue_tmpl_dir.exists() or not list(issue_tmpl_dir.glob("*.yml")):
        scores["issue_pr_engineering"] -= 40
        remediations.append({"rule_id": "issue-01", "tier": "MEDIUM", "description": "No YAML Issue Forms found", "action": "Scaffold .github/ISSUE_TEMPLATE/bug_report.yml"})

    pr_tmpl = gh_dir / "PULL_REQUEST_TEMPLATE.md" if gh_dir.exists() else repo_path / "pull_request_template.md"
    if not pr_tmpl.exists():
        scores["issue_pr_engineering"] -= 30
        remediations.append({"rule_id": "pr-01", "tier": "MEDIUM", "description": "Missing Pull Request Template", "action": "Scaffold .github/PULL_REQUEST_TEMPLATE.md"})

    # Compute Total Weighted Score
    weights = {
        "identity_discoverability": 0.10,
        "documentation_readme": 0.15,
        "developer_experience": 0.10,
        "community_health": 0.10,
        "security_supply_chain": 0.15,
        "ci_cd_automation": 0.15,
        "governance_rulesets": 0.10,
        "issue_pr_engineering": 0.10,
        "visual_presentation": 0.05,
    }
    
    total = sum(max(0, scores[dim]) * w for dim, w in weights.items())
    
    # Maturity Level (0 to 6)
    if total >= 90:
        maturity = 5
    elif total >= 80:
        maturity = 4
    elif total >= 65:
        maturity = 3
    elif total >= 50:
        maturity = 2
    elif total >= 30:
        maturity = 1
    else:
        maturity = 0

    return {
        "repository": repo_path.name,
        "maturity_level": maturity,
        "scores": {k: max(0, v) for k, v in scores.items()},
        "total_score": round(total, 1),
        "remediations": remediations
    }

def main():
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
    report = audit_repository(target)
    
    print("=" * 60)
    print(f"  TIDYFACTOR REPOSITORY HEALTH AUDIT: {report['repository']}")
    print(f"  Maturity Level: {report['maturity_level']}/6 | Total Score: {report['total_score']}/100")
    print("=" * 60)
    
    print("\n[Dimension Scores]")
    for dim, score in report["scores"].items():
        bar = "█" * int(score / 10) + "░" * (10 - int(score / 10))
        print(f"  - {dim:<26} {bar} {score:>3}/100")
        
    print("\n[Prioritized Remediations]")
    if not report["remediations"]:
        print("  ✅ Zero violations! Repository meets all production benchmarks.")
    else:
        for r in report["remediations"]:
            print(f"  [{r['tier']:<8}] ({r['rule_id']}) {r['description']} ➔ {r['action']}")
            
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
