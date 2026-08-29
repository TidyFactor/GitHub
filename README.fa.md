<div align="center" dir="rtl">

# تایدی‌فاکتور گیت‌هاب (TidyFactor GitHub)

**موتور عملیات، حاکمیت، محتوا، تجربه بصری و هوشمندی پلتفرم GitHub برای ایجنت‌های هوش مصنوعی**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[ English ](README.md) • [ العربية ](README.ar.md) • [ فارسی ](README.fa.md) • [ Español ](README.es.md) • [ Português ](README.pt.md) • [ 简体中文 ](README.zh.md) • [ Deutsch ](README.de.md) • [ Français ](README.fr.md)

</div>

---

## ⚡ راه‌اندازی سریع (Quickstart)

افزودن این مهارت به محیط ایجنت شما در چند ثانیه:

```bash
# نصب سراسری یا مستقیم از طریق NPM
npx @tidyfactor/cli-github
```

یا فراخوانی مستقیم درون دستیار برنامه‌نویسی هوش مصنوعی (*Google Antigravity, Claude Code, Cursor, Codex*):
```text
/tidyfactor-github audit
```

---

## 🎯 تایدی‌فاکتور گیت‌هاب چیست؟

مهارت `tidyfactor-github` پلتفرم GitHub را از یک مخزن ساده و غیرفعال Git به یک **مرکز مهندسی نرم‌افزار ایمن، خودکار، با ساختار استاندارد و حاکمیت دقیق** تبدیل می‌کند.

این سیستم در تمامی لایه‌های پلتفرم عمل می‌کند:
**حساب کاربری** ➔ **سازمان** ➔ **مخزن (Repository)** ➔ **کد** ➔ **همکاری تیمی** ➔ **امنیت** ➔ **تجربه توسعه‌دهنده (DX)**.

---

## 📋 ماتریس دستورات اصلی

| دستور | هدف و خروجی | جریان کاری (Workflow) |
|---|---|---|
| `/brief` | کشف استراتژیک و پایه‌ریزی معماری اولیه پروژه | `workflows/brief-discovery.md` |
| `/audit` | ممیزی سلامت ۹ بعدی مخزن (امتیاز ۰ تا ۱۰۰) و شناسایی نقایص | `workflows/run-repo-audit.md` |
| `/oss` | سنجش آمادگی و بلوغ متن‌باز در ۱۰ محور کلیدی | `workflows/run-oss-audit.md` |
| `/ruleset` | پیکربندی GitHub Rulesets و قوانین امنیتی برنچ‌ها | `workflows/configure-rulesets.md` |
| `/issue` | ساخت فرم‌های تعاملی گزارش باگر و درخواست ویژگی (YAML Issue Forms) | `workflows/setup-issue-forms.md` |
| `/pr` | ایجاد قالب استاندارد Pull Request و قوانین CODEOWNERS | `workflows/setup-pr-template.md` |
| `/action` | ممیزی و امن‌سازی خطوط لوله CI/CD با پین کردن SHA256 اکشن‌ها | `workflows/audit-actions-ci.md` |
| `/security` | تنظیم خط‌مشی افشای آسیب‌پذیری (`SECURITY.md`) و پیکربندی Dependabot | `workflows/harden-security.md` |
| `/readme` | طراحی README فنی، خوانا، ساختاریافته و فاقد محتوای عمومی زائد | `workflows/craft-readme.md` |

---

## 💡 سناریوهای کاربردی

### ۱. ممیزی سریع و ایمن مخزن (Safe Mode)
```bash
python tools/repo_audit.py .
```
محاسبه امتیاز سلامت از ۰ تا ۱۰۰ بدون اعمال هیچ‌گونه تغییر ناخواسته در فایل‌ها.

### ۲. ایجاد فرم‌های Issue و قالب PR
```text
/tidyfactor-github issue
/tidyfactor-github pr
```
تولید ساختار استاندارد در مسیرهای `.github/ISSUE_TEMPLATE/` و `.github/PULL_REQUEST_TEMPLATE.md`.

### ۳. امن‌سازی و پیکربندی Dependabot
```text
/tidyfactor-github security
```
پیکربندی امنیت و اسکن هفتگی خودکار وابستگی‌ها.

---

## 📖 مستندات فنی کامل و رسمی

برای دسترسی به معماری عمیق، اسکیماهای کامل JSON، ابزارهای بومی و جزئیات دقیق، به [مستندات فنی کامل به زبان انگلیسی (README.md)](README.md) مراجعه کنید.
