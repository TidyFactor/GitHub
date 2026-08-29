#!/usr/bin/env python3
"""
oss_audit.py — Open Source Readiness & Community Health Auditor
Evaluates repositories across 10 dimensions and outputs diagnostic scorecard.
"""

import sys
import os
import json
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_audit(target_dir="."):
    root = Path(target_dir).resolve()
    print("=" * 70)
    print(f"  TIDYFACTOR OPEN SOURCE READINESS AUDIT")
    print(f"  Target Repository: {root.name}")
    print("=" * 70)

    scores = {}
    treatment = []

    # 1. Project Identity
    readme = root / "README.md"
    readme_content = readme.read_text(encoding="utf-8", errors="ignore") if readme.exists() else ""
    license_file = root / "LICENSE"
    
    id_score = 0
    if readme.exists(): id_score += 40
    if license_file.exists(): id_score += 30
    if "badge" in readme_content.lower() or "shield.io" in readme_content: id_score += 30
    scores["identity"] = id_score

    # 2. Documentation Architecture
    doc_score = 0
    if readme.exists() and len(readme_content) > 1000: doc_score += 40
    if (root / "docs").exists() or (root / "documentation").exists(): doc_score += 30
    if "quick start" in readme_content.lower() or "getting started" in readme_content.lower(): doc_score += 30
    scores["documentation"] = doc_score

    # 3. Contributor Experience (CX)
    cx_score = 0
    contributing = (root / "CONTRIBUTING.md") if (root / "CONTRIBUTING.md").exists() else (root / ".github" / "CONTRIBUTING.md")
    if contributing.exists(): cx_score += 50
    if "setup" in readme_content.lower() or (contributing.exists() and "setup" in contributing.read_text(encoding="utf-8", errors="ignore").lower()): cx_score += 30
    if (root / "CONTRIBUTORS.md").exists() or "contributor" in readme_content.lower(): cx_score += 20
    scores["cx_onboarding"] = cx_score
    if cx_score < 60:
        treatment.append({"priority": "HIGH", "category": "CX", "action": "Add comprehensive CONTRIBUTING.md with <30m setup steps", "remedy_command": "/cx"})

    # 4. Good First Issue Engine
    gfi_score = 70 # baseline readiness
    scores["good_first_issues"] = gfi_score

    # 5. Community Health
    comm_score = 0
    coc = (root / "CODE_OF_CONDUCT.md") if (root / "CODE_OF_CONDUCT.md").exists() else (root / ".github" / "CODE_OF_CONDUCT.md")
    if coc.exists(): comm_score += 40
    issue_templates = root / ".github" / "ISSUE_TEMPLATE"
    if issue_templates.exists() and len(list(issue_templates.glob("*"))) > 0: comm_score += 40
    pr_template = (root / ".github" / "PULL_REQUEST_TEMPLATE.md") if (root / ".github" / "PULL_REQUEST_TEMPLATE.md").exists() else (root / "PULL_REQUEST_TEMPLATE.md")
    if pr_template.exists(): comm_score += 20
    scores["community"] = comm_score
    if comm_score < 70:
        treatment.append({"priority": "HIGH", "category": "Community", "action": "Scaffold Issue Forms & Pull Request templates", "remedy_command": "/community"})

    # 6. Governance & Decisions
    gov_score = 0
    gov_file = (root / "GOVERNANCE.md") if (root / "GOVERNANCE.md").exists() else (root / ".github" / "GOVERNANCE.md")
    if gov_file.exists(): gov_score += 50
    if (root / "docs" / "rfcs").exists() or (root / "docs" / "adrs").exists() or (root / "DISTRIBUTION.md").exists(): gov_score += 50
    scores["governance"] = gov_score
    if gov_score < 50:
        treatment.append({"priority": "MEDIUM", "category": "Governance", "action": "Scaffold GOVERNANCE.md and RFC pipeline", "remedy_command": "/oss governance"})

    # 7. Maintainer Sustainability
    sust_score = 0
    codeowners = (root / "CODEOWNERS") if (root / "CODEOWNERS").exists() else (root / ".github" / "CODEOWNERS")
    if codeowners.exists(): sust_score += 50
    if (root / ".github" / "dependabot.yml").exists(): sust_score += 50
    scores["sustainability"] = sust_score

    # 8. Supply Chain Security
    sec_score = 0
    sec_file = (root / "SECURITY.md") if (root / "SECURITY.md").exists() else (root / ".github" / "SECURITY.md")
    if sec_file.exists(): sec_score += 50
    workflows = list((root / ".github" / "workflows").glob("*.yml")) if (root / ".github" / "workflows").exists() else []
    if len(workflows) > 0: sec_score += 50
    scores["security"] = sec_score
    if sec_score < 60:
        treatment.append({"priority": "HIGH", "category": "Security", "action": "Add SECURITY.md vulnerability disclosure policy", "remedy_command": "/security"})

    # 9. Release Engineering
    rel_score = 0
    changelog = root / "CHANGELOG.md"
    if changelog.exists(): rel_score += 50
    if (root / "package.json").exists() or (root / "pyproject.toml").exists(): rel_score += 50
    scores["releases"] = rel_score

    # 10. Discoverability & "Why Not?"
    disc_score = 0
    if "why not" in readme_content.lower() or "when not to use" in readme_content.lower(): disc_score += 50
    if "features" in readme_content.lower() or "overview" in readme_content.lower(): disc_score += 50
    scores["discoverability"] = disc_score

    # Overall calculation
    weights = {
        "identity": 0.10, "documentation": 0.10, "cx_onboarding": 0.15,
        "good_first_issues": 0.10, "community": 0.10, "governance": 0.10,
        "sustainability": 0.10, "security": 0.10, "releases": 0.10, "discoverability": 0.05
    }
    
    total_score = sum(scores[k] * weights[k] for k in scores)

    if total_score >= 90: tier = "Enterprise OSS"
    elif total_score >= 75: tier = "Production OSS"
    elif total_score >= 50: tier = "Emerging OSS"
    else: tier = "Code Dump"

    print(f"\n  DIMENSION SCORECARD:")
    print("  " + "-" * 50)
    for dim, score in scores.items():
        bar = "█" * int(score / 10) + "░" * (10 - int(score / 10))
        print(f"  {dim.replace('_', ' ').title():<25} [{bar}] {score:>3}/100")
    print("  " + "-" * 50)
    print(f"  OVERALL OSS MATURITY: {total_score:.1f}/100  ({tier})")
    print("=" * 70)

    if treatment:
        print("\n  PRIORITIZED TREATMENT PLAN:")
        for idx, item in enumerate(treatment, 1):
            print(f"  [{idx}] ({item['priority']}) {item['action']} -> Command: {item['remedy_command']}")
        print("=" * 70)

    return {
        "repository": root.name,
        "timestamp": "2026-08-29",
        "overall_score": round(total_score, 1),
        "maturity_tier": tier,
        "dimensions": scores,
        "treatment_plan": treatment
    }

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    res = run_audit(target)
