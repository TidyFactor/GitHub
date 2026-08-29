<div align="center">

# TidyFactor GitHub

**Motor de Operaciones, Gobernanza, Contenido, Experiencia e Inteligencia de GitHub para Agentes de IA**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ Inicio Rápido (Quickstart)

Añade la habilidad a tu entorno de agente en segundos:

```bash
# Instalación global o directa vía NPM
npx @tidyfactor/cli-github
```

O actívala directamente dentro de tu asistente de codificación con IA (*Google Antigravity, Claude Code, Cursor, Codex*):
```text
/tidyfactor-github audit
```

---

## 🎯 ¿Qué es TidyFactor GitHub?

`tidyfactor-github` transforma GitHub de un simple repositorio remoto en un **centro de software gobernado, seguro, automatizado y visualmente optimizado**.

Funciona en toda la jerarquía de la plataforma:
**Cuenta** ➔ **Organización** ➔ **Repositorio** ➔ **Código** ➔ **Colaboración** ➔ **Seguridad** ➔ **Experiencia de Desarrollador (DX)**.

---

## 📋 Matriz de Comandos Principales

| Comando | Propósito y Resultado | Flujo de Trabajo |
|---|---|---|
| `/brief` | Descubrimiento estratégico y arquitectura base del proyecto | `workflows/brief-discovery.md` |
| `/audit` | Auditoría de salud de 9 dimensiones (0-100) con diagnóstico de brechas | `workflows/run-repo-audit.md` |
| `/oss` | Evaluación de preparación Open Source en 10 ejes | `workflows/run-oss-audit.md` |
| `/ruleset` | Configuración de GitHub Rulesets y políticas de ramas seguras | `workflows/configure-rulesets.md` |
| `/issue` | Generación de plantillas interactivas YAML Issue Forms | `workflows/setup-issue-forms.md` |
| `/pr` | Creación de plantillas PR estandarizadas y asignación CODEOWNERS | `workflows/setup-pr-template.md` |
| `/action` | Auditoría y endurecimiento de GitHub Actions con pinning SHA256 | `workflows/audit-actions-ci.md` |
| `/security` | Configuración de políticas de seguridad (`SECURITY.md`) y Dependabot | `workflows/harden-security.md` |
| `/readme` | Diseño de documentación técnica scannable y libre de texto genérico | `workflows/craft-readme.md` |

---

## 💡 Casos de Uso Prácticos

### 1. Auditoría Inmediata de Repositorio (Modo Seguro)
```bash
python tools/repo_audit.py .
```
Calcula una puntuación de salud de 0 a 100 evaluando seguridad, documentación, automatización y gobernanza sin modificar ningún archivo.

### 2. Generación de Formularios de Issues y Plantilla PR
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
Crea formularios estructurados `.github/ISSUE_TEMPLATE/` y `.github/PULL_REQUEST_TEMPLATE.md` adaptados a tu stack.

### 3. Endurecimiento de Seguridad y Dependabot
```text
/tidyfactor-github security
```
Configura la política de divulgación coordinada de vulnerabilidades y la actualización semanal automática de dependencias.

---

## 📖 Especificación Técnica Completa

Para la arquitectura profunda, esquemas JSON completos, herramientas nativas y especificaciones de gobernanza, consulta la [Documentación Técnica Canónica en Inglés (README.md)](README.md).
