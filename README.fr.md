<div align="center">

# TidyFactor GitHub

**Moteur d'Opérations, Gouvernance, Contenu, Expérience Visuelle & Intelligence GitHub pour Agents d'IA**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ Démarrage Rapide (Quickstart)

Ajoutez cette compétence à votre environnement d'agent en quelques secondes :

```bash
# Installation globale ou directe via NPM
npx @tidyfactor/cli-github
```

Ou appelez-la directement depuis votre assistant IA (*Google Antigravity, Claude Code, Cursor, Codex*) :
```text
/tidyfactor-github audit
```

---

## 🎯 Qu'est-ce que TidyFactor GitHub ?

`tidyfactor-github` transforme GitHub d'un simple dépôt distant en un **centre d'ingénierie logicielle gouverné, sécurisé, automatisé et au design soigné**.

Il intervient à tous les niveaux de la plateforme :
**Compte** ➔ **Organisation** ➔ **Dépôt (Repo)** ➔ **Code** ➔ **Collaboration** ➔ **Sécurité** ➔ **Expérience Développeur (DX)**.

---

## 📋 Matrice des Commandes Principales

| Commande | Objectif & Résultat | Référence de Workflow |
|---|---|---|
| `/brief` | Découverte stratégique et définition de l'architecture de base | `workflows/brief-discovery.md` |
| `/audit` | Audit de santé du dépôt en 9 dimensions (score de 0 à 100) | `workflows/run-repo-audit.md` |
| `/oss` | Diagnostic de préparation Open Source en 10 axes | `workflows/run-oss-audit.md` |
| `/ruleset` | Configuration des GitHub Rulesets et protection des branches | `workflows/configure-rulesets.md` |
| `/issue` | Génération de formulaires interactifs YAML Issue Forms | `workflows/setup-issue-forms.md` |
| `/pr` | Modèles de Pull Request standardisés et règles CODEOWNERS | `workflows/setup-pr-template.md` |
| `/action` | Audit et sécurisation des flux CI/CD (Pinning SHA256) | `workflows/audit-actions-ci.md` |
| `/security` | Politique de divulgation des vulnérabilités (`SECURITY.md`) & Dependabot | `workflows/harden-security.md` |
| `/readme` | Rédaction de README techniques, clairs et structurés | `workflows/craft-readme.md` |

---

## 💡 Cas d'Usage Pratiques

### 1. Audit Rapide de Dépôt (Mode Lecture Seule)
```bash
python tools/repo_audit.py .
```
Évalue le score de sécurité, de documentation et de gouvernance sans modifier vos fichiers.

### 2. Génération de Formulaires d'Issues et Modèle de PR
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
Génère l'arborescence standard `.github/ISSUE_TEMPLATE/` et `.github/PULL_REQUEST_TEMPLATE.md`.

### 3. Renforcement de la Sécurité et Dependabot
```text
/tidyfactor-github security
```
Active la détection automatisée et les mises à jour hebdomadaires des dépendances.

---

## 📖 Spécification Technique Complète

Pour l'architecture détaillée, les schémas JSON complets et la documentation des outils natifs, veuillez consulter la [Documentation Technique Officielle en Anglais (README.md)](README.md).
