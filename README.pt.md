<div align="center">

# TidyFactor GitHub

**Motor de Operações, Governança, Conteúdo, Experiência e Inteligência do GitHub para Agentes de IA**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ Início Rápido (Quickstart)

Adicione a habilidade ao seu ambiente de agente em segundos:

```bash
# Instalação global ou direta via NPM
npx @alwkala/tidyfactor-github
```

Ou execute diretamente dentro do seu assistente de IA (*Google Antigravity, Claude Code, Cursor, Codex*):
```text
/tidyfactor-github audit
```

---

## 🎯 O que é o TidyFactor GitHub?

O `tidyfactor-github` transforma o GitHub de um simples repositório remoto em um **centro de engenharia de software governado, seguro, automatizado e de alto padrão visual**.

Opera em todos os níveis da plataforma:
**Conta** ➔ **Organização** ➔ **Repositório** ➔ **Código** ➔ **Colaboração** ➔ **Segurança** ➔ **Experiência do Desenvolvedor (DX)**.

---

## 📋 Matriz de Comandos Principais

| Comando | Objetivo e Resultado | Fluxo de Trabalho |
|---|---|---|
| `/brief` | Descoberta estratégica e arquitetura base do repositório | `workflows/brief-discovery.md` |
| `/audit` | Auditoria de saúde em 9 dimensões (0-100) com plano de ação | `workflows/run-repo-audit.md` |
| `/oss` | Avaliação de maturidade Open Source em 10 eixos | `workflows/run-oss-audit.md` |
| `/ruleset` | Configuração de GitHub Rulesets e proteção estrita de branches | `workflows/configure-rulesets.md` |
| `/issue` | Geração de formulários interativos YAML Issue Forms | `workflows/setup-issue-forms.md` |
| `/pr` | Criação de templates de PR padronizados e regras CODEOWNERS | `workflows/setup-pr-template.md` |
| `/action` | Auditoria e proteção de GitHub Actions com pinning SHA256 | `workflows/audit-actions-ci.md` |
| `/security` | Configuração de políticas de segurança (`SECURITY.md`) e Dependabot | `workflows/harden-security.md` |
| `/readme` | Criação de README técnico, escaneável e livre de conteúdo genérico | `workflows/craft-readme.md` |

---

## 💡 Casos de Uso Práticos

### 1. Auditoria Imediata de Repositório (Modo Seguro)
```bash
python tools/repo_audit.py .
```
Gera um diagnóstico de 0 a 100 avaliando segurança, documentação e governança sem alterar arquivos.

### 2. Criação de Issue Forms e Template de PR
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
Cria formulários estruturados `.github/ISSUE_TEMPLATE/` e `.github/PULL_REQUEST_TEMPLATE.md`.

### 3. Fortalecimento de Segurança e Dependabot
```text
/tidyfactor-github security
```
Configura política de divulgação de vulnerabilidades e atualizações semanais automáticas de dependências.

---

## 📖 Especificação Técnica Canônica

Para a arquitetura detalhada, esquemas JSON completos, ferramentas nativas e documentação profunda, consulte a [Documentação Técnica Canônica em Inglês (README.md)](README.md).
