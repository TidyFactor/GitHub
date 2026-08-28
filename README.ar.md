<div align="center" dir="rtl">

# تايدي فاكتور جيت هب (TidyFactor GitHub)

**محرك تشغيل، حوكمة، محتوى، تجربة بصرية، وذكاء منصة GitHub للوكلاء البرمجيين**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)](package.json)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg?style=flat-square)](LICENSE)
[![Ecosystem](https://img.shields.io/badge/TidyFactor-Skills--LAB-purple.svg?style=flat-square)](https://github.com/TidyFactor)
[![Compatibility](https://img.shields.io/badge/Agents-Antigravity%20|%20Claude%20|%20Cursor%20|%20Codex-orange.svg?style=flat-square)](SKILL.md)

[English](README.md) • [العربية](README.ar.md)

</div>

---

## 📌 نظرة عامة

مهارة **`tidyfactor-github`** هي مهارة ذكاء اصطناعي متقدمة مخصصة لبيئات التطوير بالوكلاء (*Google Antigravity, Claude Code, Cursor, Codex*) لتحويل منصة GitHub من مجرد خادم بعيد لتخزين ملفات Git إلى بيئة عمل متكاملة تخضع لأعلى معايير الحوكمة، الأمان، الأتمتة، الجودة البصرية، وتجربة المطور الفائقة.

تعمل المهارة عبر كافة مستويات المنصة:
**الحساب** ➔ **المنظمة** ➔ **المستودع** ➔ **الكود** ➔ **التعاون** ➔ **الأمان** ➔ **تجربة المطور**.

---

## 🏛️ المحرك الخماسي والقدرات الأساسية

```text
                               ┌─────────────────────────────────────────┐
                               │            TIDYFACTOR GITHUB            │
                               │  محرك تشغيل وحوكمة وذكاء منصة جيت هب    │
                               └────────────────────┬────────────────────┘
                                                    │
        ┌───────────────────┬───────────────────────┼───────────────────────┬───────────────────┐
        │                   │                       │                       │                   │
  ┌─────▼───────┐     ┌─────▼─────────┐       ┌─────▼─────────┐       ┌─────▼─────────┐   ┌─────▼─────────┐
  │  العمليات   │     │    الحوكمة    │       │    المحتوى    │       │ الهوية والتنسيق│   │  طبقة الذكاء  │
  ├─────────────┤     ├───────────────┤       ├───────────────┤       ├───────────────┤   ├───────────────┤
  │• المستودعات │     │• قواعد Ruleset│       │• تجربة README │       │• التنسيق البصري│   │• ذاكرة السياق │
  │• المنظمات   │     │• تعيين الملاك │       │• نماذج Issues │       │• مصفوفة الشارات│   │• قرارات ADRs  │
  │• إدارة الفرق│     │• حماية الفروع │       │• قوالب الـ PR │       │• التايبوغرافي │   │• فحص الانحراف │
  │• سلاسل CI/CD│     │• الصلاحيات    │       │• التوثيق الفني│       │• بطاقات المعاينة│  │• مواصفة Blueprint│
  │• الإصدارات  │     │• السياسات     │       │• سجل التغييرات│       │• سهولة المسح  │   │• وضع الطوارئ  │
  └─────────────┘     └───────────────┘       └───────────────┘       └───────────────┘   └───────────────┘
```

1. **طبقة العمليات (Operations)**: دورة حياة المستودعات، إدارة المنظمات والفرق، الفروع، الإصدارات، وتوزيع الحزم.
2. **طبقة الحوكمة (Governance)**: قواعد GitHub Rulesets، حماية الفروع، ملفات CODEOWNERS، مصفوفة الصلاحيات، وتطبيق مبدأ Least Privilege.
3. **طبقة المحتوى (Content)**: محرك هندسة README ومكافحة الحشو والتسويق الأجوف، نماذج Issue Forms التفاعلية (`.yml`)، وقوالب مراجعة الكود المتخصصة.
4. **طبقة التنسيق والهوية (Styling)**: التسلسل الهرمي البصري، ضبط كثافة الشارات ($\le 5$)، وبطاقات المعاينة الاجتماعية (Social Preview Cards).
5. **طبقة الذكاء والذاكرة (Intelligence)**: ذاكرة سياق المستودعات، تتبع سجلات القرارات المعمارية (ADRs)، رصد الانحراف عن المخطط المعياري (Drift Detection)، وتحليل حوادث الإنتاج وتوليد تقارير ما بعد الحادث (Postmortems).

---

## 🛡️ أنماط التشغيل الثلاثية وبوابات السلامة

| النمط | السلوك والوظيفة | بوابة الأمان |
|---|---|---|
| **`AUDIT`** *(الافتراضي)* | فحص المستودعات والمنظمات، وحساب درجات الصحة التساعية (Scorecards 0-100) دون أي كتابة أو تعديل. | للقراءة فقط |
| **`PLAN`** *(محاكاة Dry-Run)* | قياس الفجوات بين الوضع الحالي والمخطط المعياري `repository.blueprint.yml` وتوليد فوارق الملفات (Diffs) وأوامر `gh` المقترحة. | محاكاة وتخطيط |
| **`APPLY`** *(تنفيذ محكوم)* | تطبيق التكوينات والأتمتة المعتمدة. العمليات الحساسة (حذف المستودعات، الدمج القسري، ترقية صلاحيات Admin، وتغيير نوع المستودع إلى Public) تتطلب موافقة صريحة من المستخدم. | تنفيذ مشروط |

---

## 🧭 طبقة القرارات السياقية (CDL) ومصفوفة الأوامر

| الأمر | الهدف والوظيفة | الملفات المحملة |
|---|---|---|
| `/brief` | الاستكشاف الاستراتيجي وتثبيت خط الأساس التقني | `brief-discovery.md` + `decision-points.md` |
| `/audit` | تقرير تدقيق الصحة التساعي للمستودع والمنظمة | `run-repo-audit.md` + `maturity-model.md` |
| `/org` | هندسة المنظمة، هيكل الفرق، ومصفوفة الصلاحيات | `setup-org-hierarchy.md` + `permission-matrix.md` |
| `/repo` | مصنع المستودعات الجديدة وإدارة محفظة المشاريع | `scaffold-repository.md` + `maturity-model.md` |
| `/branch` | استراتيجيات الفروع (Trunk, GitFlow, GitHub Flow) | `configure-rulesets.md` + `branch-strategies.md` |
| `/ruleset` | قواعد الحماية المتقدمة على مستوى الفروع والمنظمة | `configure-rulesets.md` + `gov-rules.md` |
| `/issue` | نماذج الـ Issues المنظمة وتصنيف المشاكل | `setup-issue-forms.md` + `issue-taxonomy.md` |
| `/pr` | قوالب طلبات السحب ومراجعة الكود والمالكين | `setup-pr-template.md` + `permission-matrix.md` |
| `/action` | سلاسل CI/CD، تثبيت الـ SHA، وأمان سلاسل التوريد | `audit-actions-ci.md` + `ci-rules.md` + `sec-rules.md` |
| `/security` | تعزيز الأمان، Dependabot، وحماية الأسرار و 2FA | `harden-security.md` + `sec-rules.md` |
| `/community` | ملفات صحة المجتمع (`CONTRIBUTING`, `SECURITY`) | `setup-community-health.md` + `maturity-model.md` |
| `/readme` | محرك صياغة الـ README ومكافحة الحشو والتسويق الزائف | `craft-readme.md` + `content-rules.md` |
| `/style` | الهوية البصرية، الشارات المعتمدة، وبطاقات المعاينة | `design-social-preview.md` + `content-rules.md` |
| `/release` | أتمتة الإصدارات والوسوم ومزامنة CHANGELOG | `automate-release.md` + `maturity-model.md` |
| `/project` | إدارة مشاريع GitHub Projects والخرائط الزمنية | `manage-projects.md` + `maturity-model.md` |
| `/discover` | تحسين الظهور والـ SEO والمواضيع (RDO) | `optimize-discoverability.md` + `rdo-matrix.md` |
| `/incident` | التعامل مع طوارئ الإنتاج، التراجع، والتقارير الفنية | `handle-incident.md` + `security-baseline.md` |
| `/blueprint` | تحليل الفجوات وتطبيق المخططات المعيارية | `apply-blueprint.md` + `decision-points.md` |

---

## 📚 كتالوجات القواعد المصنفة حسب التأثير

تفرض المهارة 4 كتالوجات قواعد صارمة تبدأ من `CRITICAL` نزولاً إلى `LOW`:
- **قواعد الأمان (`sec-rules.md`)**: تثبيت الـ SHA للإجراءات، تقييد صلاحيات الوظائف، حماية الأسرار وتفعيل Dependabot.
- **قواعد الحوكمة (`gov-rules.md`)**: حماية الفرع الرئيسي، فرض التاريخ الخطي، تغطية `CODEOWNERS`، واشتراط حل المحادثات.
- **قواعد المحتوى (`content-rules.md`)**: حظر العبارات التسويقية الجوفاء، وضوح البداية السريعة، وتحديد سقف الشارات ($\le 5$).
- **قواعد الأتمتة CI/CD (`ci-rules.md`)**: إلغاء التشغيل المتزامن القديم، فرض Timeouts صريحة، وتفعيل الكاش للحزم.

---

## 💻 التثبيت والتشغيل

### التضمين السريع في مشروعك
```bash
npx @alwkala/tidyfactor-github
```

### التضمين اليدوي في بيئة الوكيل
انسخ مجلد المهارة إلى:
```bash
.agents/skills/tidyfactor-github/
```

---

## 📄 الترخيص

Apache-2.0 © [TidyFactor](https://github.com/TidyFactor) & [وكالة الوكالة الرقمية](https://alwkala.com)
