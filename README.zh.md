<div align="center">

# TidyFactor GitHub

**面向 AI 编码智能体的 GitHub 平台运维、治理、内容、视觉体验与智能引擎**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ 快速上手 (Quickstart)

数秒内将技能添加到您的智能体环境中：

```bash
# 全局安装或通过 NPM 直接运行
npx @alwkala/tidyfactor-github
```

或在 AI 编码助手 (*Google Antigravity, Claude Code, Cursor, Codex*) 中直接调用：
```text
/tidyfactor-github audit
```

---

## 🎯 什么是 TidyFactor GitHub？

`tidyfactor-github` 将 GitHub 从一个被动的 Git 远程仓库转变为一个**受控、安全、自动化、视觉美观且高转化率的软件工程中心**。

它贯穿整个平台层级运行：
**账户** ➔ **组织 (Org)** ➔ **仓库 (Repo)** ➔ **代码** ➔ **协作** ➔ **安全** ➔ **开发者体验 (DX)**。

---

## 📋 核心命令矩阵

| 命令 | 目标与产出 | 执行工作流 |
|---|---|---|
| `/brief` | 战略发现与项目基础架构基线制定 | `workflows/brief-discovery.md` |
| `/audit` | 9 维仓库健康度体检 (0-100分) 与缺陷诊断 | `workflows/run-repo-audit.md` |
| `/oss` | 10 轴开源成熟度与就绪度评估 | `workflows/run-oss-audit.md` |
| `/ruleset` | 配置 GitHub Rulesets 与分支保护策略 | `workflows/configure-rulesets.md` |
| `/issue` | 生成交互式 YAML Issue Forms 表单 | `workflows/setup-issue-forms.md` |
| `/pr` | 创建标准化 PR 模板与 CODEOWNERS 规则 | `workflows/setup-pr-template.md` |
| `/action` | 审计与加固 GitHub Actions 工作流 (SHA256 Pinning) | `workflows/audit-actions-ci.md` |
| `/security` | 配置安全漏洞披露政策 (`SECURITY.md`) 与 Dependabot | `workflows/harden-security.md` |
| `/readme` | 打造清晰易读、无废话的高质感技术文档 | `workflows/craft-readme.md` |

---

## 💡 典型应用场景

### 1. 快速无害仓库体检 (安全只读模式)
```bash
python tools/repo_audit.py .
```
评估安全、文档、自动化和治理得分，不修改任何文件。

### 2. 生成 Issue 表单与 PR 规范模板
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
在 `.github/ISSUE_TEMPLATE/` 和 `.github/PULL_REQUEST_TEMPLATE.md` 中生成标准文件。

### 3. 安全加固与自动化依赖更新
```text
/tidyfactor-github security
```
配置漏洞披露流程与每周自动依赖扫描。

---

## 📖 完整技术规范与文档

如需查看深层架构设计、完整 JSON Schema 契约和原生工具集，请参阅[英文权威技术文档 (README.md)](README.md)。
