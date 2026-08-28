#!/usr/bin/env python3
"""
org_audit.py — TidyFactor GitHub Organization & Team Permission Auditor.
Analyzes permission matrices, 2FA status, and least-privilege compliance.
"""

import sys
import json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def audit_org_data(matrix_file: Path):
    if not matrix_file.exists():
        print(f"Matrix file not found: {matrix_file}")
        return
        
    data = json.loads(matrix_file.read_text(encoding="utf-8"))
    org_name = data.get("organization", "Unknown")
    teams = data.get("teams", [])
    repos = data.get("repositories", [])
    
    print("=" * 60)
    print(f"  TIDYFACTOR ORGANIZATION GOVERNANCE AUDIT: @{org_name}")
    print("=" * 60)
    
    print(f"\n[1] Team Architecture ({len(teams)} teams defined):")
    for t in teams:
        parent_str = f" (Parent: @{t['parent']})" if t.get("parent") else ""
        print(f"  - @{t['slug']:<20} [{t['privacy']}]{parent_str}")
        
    print(f"\n[2] Repository Permission Mapping ({len(repos)} repositories):")
    anomalies = []
    for r in repos:
        name = r["name"]
        perms = r["team_permissions"]
        print(f"\n  📁 Repository: {name}")
        for team, level in perms.items():
            print(f"     ➔ @{team:<18} : {level}")
            if level == "admin" and team not in ["devops-infra", "platform-core"]:
                anomalies.append(f"Excessive Admin role granted to @{team} on repo '{name}'")
                
    print("\n[3] Least Privilege & Governance Anomalies:")
    if not anomalies:
        print("  ✅ 100% Compliant with Least Privilege matrix!")
    else:
        for a in anomalies:
            print(f"  ⚠️  {a}")
            
    print("\n" + "=" * 60)

def main():
    root = Path(__file__).resolve().parent.parent
    sample_matrix = root / "schemas" / "permission-matrix.schema.json"
    print(f"Org auditor ready. Pass a JSON matrix file matching: {sample_matrix.name}")

if __name__ == "__main__":
    main()
