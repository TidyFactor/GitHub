#!/usr/bin/env python3
"""
readme_linter.py — TidyFactor README Experience & Anti-Slop Linter.
Checks:
1. Banned marketing buzzwords and AI slop phrases.
2. Badge density (max 5 badges).
3. Above-the-fold value clarity & quick-start code placement.
4. Bilingual RTL structure verification when README.ar.md is present.
"""

import sys
import re
from pathlib import Path

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BANNED_SLOP_PHRASES = [
    r"revolutionary\s+next-generation",
    r"blazing\s+fast",
    r"game-changing",
    r"seamlessly\s+leverages",
    r"cutting-edge\s+ai\s+power",
    r"ultimate\s+all-in-one\s+solution",
    r"state\s+of\s+the\s+art\s+magic",
    r"effortlessly\s+empowers",
    r"unparalleled\s+performance",
]

def lint_readme(file_path: Path):
    if not file_path.exists():
        return [f"File not found: {file_path}"]
    
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    violations = []
    
    # 1. Anti-Slop check
    for pattern in BANNED_SLOP_PHRASES:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            violations.append(f"Anti-slop violation: Found banned phrase '{match.group(0)}' in {file_path.name}")
            
    # 2. Badge density check
    badge_matches = re.findall(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', text)
    badge_count = len(badge_matches)
    if badge_count > 5:
        violations.append(f"Badge density violation: Found {badge_count} badges (Maximum allowed is 5).")
        
    # 3. Above-the-fold Quick Start check
    first_code_line = -1
    for idx, line in enumerate(lines[:50]):
        if line.strip().startswith("```"):
            first_code_line = idx + 1
            break
    if first_code_line == -1 or first_code_line > 35:
        violations.append("Above-the-fold clarity violation: No quick start code block found within first 35 lines.")
        
    # 4. RTL check for Arabic files
    if file_path.name.endswith(".ar.md"):
        if 'dir="rtl"' not in text and "dir='rtl'" not in text:
            violations.append("RTL violation: README.ar.md must include dir=\"rtl\" container wrapper.")
            
    return violations

def main():
    root = Path(__file__).resolve().parent.parent
    target_files = [root / "README.md"]
    if (root / "README.ar.md").exists():
        target_files.append(root / "README.ar.md")
        
    all_violations = []
    print("=" * 60)
    print("  RUNNING TIDYFACTOR README LINTER & ANTI-SLOP AUDIT")
    print("=" * 60)
    
    for f in target_files:
        print(f"\nScanning: {f.name}")
        v = lint_readme(f)
        if v:
            for item in v:
                print(f"  ❌ {item}")
                all_violations.append(item)
        else:
            print("  ✅ 100% Clean! Zero slop, optimal density and scannable.")
            
    print("\n" + "=" * 60)
    if all_violations:
        print(f"[FAIL] {len(all_violations)} README lint violations found.")
        sys.exit(1)
    else:
        print("[SUCCESS] README PASSED ALL EXPERIENCE & ANTI-SLOP CRITERIA!")
        sys.exit(0)

if __name__ == "__main__":
    main()
