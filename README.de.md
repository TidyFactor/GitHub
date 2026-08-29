<div align="center">

# TidyFactor GitHub

**GitHub Plattformbetrieb, Governance, Content, UI-Design & Intelligence Engine für KI-Coding-Agenten**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ Schnellstart (Quickstart)

In Sekundenschnelle in Ihre KI-Agentenumgebung einbinden:

```bash
# Globale Installation oder Direktstart via NPM
npx @tidyfactor/cli-github
```

Oder direkt in Ihrem KI-Coding-Assistenten aufrufen (*Google Antigravity, Claude Code, Cursor, Codex*):
```text
/tidyfactor-github audit
```

---

## 🎯 Was ist TidyFactor GitHub?

`tidyfactor-github` verwandelt GitHub von einem passiven Remote-Speicher in ein **sicheres, automatisiertes, professionell strukturiertes und nach Enterprise-Standards geführtes Software-Hub**.

Es steuert die gesamte Plattformhierarchie:
**Account** ➔ **Organisation** ➔ **Repository** ➔ **Code** ➔ **Zusammenarbeit** ➔ **Sicherheit** ➔ **Developer Experience (DX)**.

---

## 📋 Befehls- & Workflow-Matrix

| Befehl | Ziel & Ergebnis | Workflow-Referenz |
|---|---|---|
| `/brief` | Strategische Erkennung und Erstellung der Baseline-Architektur | `workflows/brief-discovery.md` |
| `/audit` | 9-Dimensionen Repository-Gesundheitsprüfung (0-100 Score) | `workflows/run-repo-audit.md` |
| `/oss` | 10-Achsen Open-Source-Reifegradanalyse & Doctor | `workflows/run-oss-audit.md` |
| `/ruleset` | Konfiguration von GitHub Rulesets & Branch-Schutzregeln | `workflows/configure-rulesets.md` |
| `/issue` | Erstellung interaktiver YAML Issue Forms | `workflows/setup-issue-forms.md` |
| `/pr` | Standardisierte PR-Templates & CODEOWNERS-Zuweisung | `workflows/setup-pr-template.md` |
| `/action` | Auditierung und Absicherung von GitHub Actions (SHA256-Pinning) | `workflows/audit-actions-ci.md` |
| `/security` | Einrichtung von Sicherheitsrichtlinien (`SECURITY.md`) & Dependabot | `workflows/harden-security.md` |
| `/readme` | Erstellung scanbarer, entwicklerorientierter Dokumentationen | `workflows/craft-readme.md` |

---

## 💡 Praktische Anwendungsbeispiele

### 1. Schnelles Repository-Audit (Sicherer Lesemodus)
```bash
python tools/repo_audit.py .
```
Ermittelt eine Reifegradbewertung von 0 bis 100 für Sicherheit, CI/CD und Governance ohne Schreibzugriffe.

### 2. Generierung von Issue- & PR-Vorlagen
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
Erzeugt standardisierte Dateien unter `.github/ISSUE_TEMPLATE/` und `.github/PULL_REQUEST_TEMPLATE.md`.

### 3. Sicherheits-Hardening & Dependabot
```text
/tidyfactor-github security
```
Konfiguriert automatisierte wöchentliche Abhängigkeits- und Actions-Sicherheitsscans.

---

## 📖 Vollständige Technische Spezifikation

Für detaillierte Architekturpläne, vollständige JSON-Schemas und interne Tool-Dokumentation konsultieren Sie bitte die [Offizielle Technische Dokumentation auf Englisch (README.md)](README.md).
