# Use Cases & User Interaction Playbook (GitHub Operations)

<!-- last-verified: 2026-08-29 -->

Structured routing and conversational interaction patterns for `tidyfactor-github` based on real-world developer lifecycle scenarios.

---

## 🎯 The 6 Core Use Case Tracks

```text
                                 ┌─────────────────────────────────────────┐
                                 │       GITHUB LIFECYCLE USE CASES        │
                                 └────────────────────┬────────────────────┘
                                                      │
         ┌───────────────────┬────────────────────────┼────────────────────────┬───────────────────┐
         │                   │                        │                        │                   │
   ┌─────▼───────┐     ┌─────▼─────────┐        ┌─────▼─────────┐        ┌─────▼─────────┐   ┌─────▼─────────┐
   │ 1. SCAFFOLD │     │ 2. GOVERNANCE │        │ 3. OSS LAUNCH │        │ 4. CI/CD SEC  │   │ 5. REBRAND UX │
   ├─────────────┤     ├───────────────┤        ├───────────────┤        ├───────────────┤   ├───────────────┤
   │ New Repo /  │     │ Rulesets / PR │        │ Community /   │        │ Hardening /   │   │ README / OG / │
   │ Org Setup   │     │ Protection    │        │ CX / GFI      │        │ SHA Pinning   │   │ Badges / RTL  │
   └─────────────┘     └───────────────┘        └───────────────┘        └───────────────┘   └───────────────┘
```

---

## 🧭 Use Case Routing & Interactive Protocols

### Use Case 1: "أريد تجهيز مستودع جديد أو حوكمة منظمة" (Repository Factory & Org Setup)
- **User Triggers**: `أنشئ مستودع جديد`, `جهز ريبو من الصفر`, `حوكمة المنظمة`, `scaffold repo`, `setup org`.
- **Command Sequence**:
  1. `/brief` ➔ تحديد اسم المستودع، نوع الترخيص، ولغات البرمجة المستهدفة.
  2. `/repo` ➔ توليد الهيكل المعماري، `.gitignore` الموحد، ملفات الترخيص و`README.md`.
  3. `/ruleset` ➔ تفعيل حماية الفروع الرسمية `Main Branch Protection` عبر API.
- **Interactive Checkpoint**:
  > ❓ هل المستودع عام (Public OSS) أم خاص (Private Enterprise)؟ وهل هناك فريق عمل يحتاج لصلاحيات مخصصة؟

---

### Use Case 2: "أريد حماية الفرع الرئيسي ومنع الـ Force Push" (Branch Protection & Rulesets)
- **User Triggers**: `احمي الماين`, `منع الـ force push`, `إلزام pull request`, `protect branch`, `ruleset`.
- **Command Sequence**:
  1. `/ruleset` ➔ فحص الـ Rulesets النشطة حالياً عبر `gh api repos/{owner}/{repo}/rulesets`.
  2. استدعاء ملف `memory/ruleset-profiles.md` وتطبيق ملف الحماية المعياري `ruleset_payload.json`.
  3. التحقق الفوري من زوال تنبيهات الحماية.
- **Interactive Checkpoint**:
  > 🔒 تم تجهيز قواعد الحماية (منع الحذف + منع Force-Push + إلزام PR). هل تريد تطبيقها مباشرة على المستودع؟

---

### Use Case 3: "أريد إطلاق مشروع مفتوح المصدر واستقبال مساهمات" (OSS Readiness & Community CX)
- **User Triggers**: `إطلاق أوبن سورس`, `استقبال مساهمات`, `good first issue`, `open source readiness`, `community health`.
- **Command Sequence**:
  1. `/oss` ➔ فحص المستودع عبر مصفوفة المحاور العشرة (Readiness Rubric).
  2. `/community` ➔ توليد ملفات المجتمع (`CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `PULL_REQUEST_TEMPLATE.md`).
  3. `/issue` ➔ تجهيز قوالب الـ Issue Forms التفاعلية (`bug_report.yml`, `feature_request.yml`).
  4. `/gfi` ➔ تحديد وتصنيف مشكلات المبتدئين وتسهيل الـ Onboarding للمطورين.
- **Interactive Checkpoint**:
  > 🚀 هل تريد توجيه المساهمين الجدد لمسار معين (مثل تحسين التوثيق، إصلاح الأخطاء، أو إضافة لغات جديدة)؟

---

### Use Case 4: "أريد تأمين خطوط الـ CI/CD والاعتماديات" (Actions Security & Supply Chain)
- **User Triggers**: `تأمين الإجراءات`, `فحص الأمان`, `dependabot`, `actions security`, `audit ci`.
- **Command Sequence**:
  1. `/action` ➔ تدقيق ملفات `.github/workflows/*.yml`، تثبيت الـ Full Commit SHAs وتقييد الـ Permissions إلى `contents: read`.
  2. `/security` ➔ تفعيل `dependabot.yml` لفحص الثغرات، وتفعيل سياسة الإبلاغ الآمن عن الثغرات `SECURITY.md`.
- **Interactive Checkpoint**:
  > 🛡️ تم رصد إجراءات تعتمد على `@v1` غير المثبتة بـ SHA. هل تريد ترقيتها وتثبيتها بالـ Full SHA256؟

---

### Use Case 5: "أريد تحسين المظهر البصري لصفحة المستودع والبادجات" (Visual Styling & README UX)
- **User Triggers**: `حسن الريدمي`, `أضف بادجات`, `صورة المعاينة`, `style readme`, `badges`, `social preview`.
- **Command Sequence**:
  1. `/readme` ➔ إعادة هيكلة ملف التوثيق وفق الـ 8-Stage Progression ومكافحة الحشو التسويقي (Anti-Slop).
  2. `/style` ➔ إضافة طقم البادجات الفاخر `style=for-the-badge` وشريط التنقل اللغوي الثماني.
  3. إضافة أقسام التواصل والمنظمة والترخيص الرسمي.
- **Interactive Checkpoint**:
  > ✨ هل تفضل إبراز شارات معينة في الترويسة (مثل NPM، التوافق مع الوكلاء، ودعم العربية)؟

---

### Use Case 6: "أريد أتمتة الإصدارات والـ Release مع CHANGELOG" (Automated Releases & SemVer)
- **User Triggers**: `أطلق إصدار جديد`, `نشر ريليز`, `سجل التغييرات`, `release`, `semver`, `changelog`.
- **Command Sequence**:
  1. `/release` ➔ تدقيق التغييرات، اقتراح رقم الإصدار الدلالي (`MAJOR`/`MINOR`/`PATCH`).
  2. تحديث `CHANGELOG.md` والميتاداتا الذرية.
  3. إنشاء فرع الإصدار `release/vX.Y.Z`، دمج الـ PR، وإنشاء GitHub Release رسمي مع إرفاق حزم الأرشيفات.
- **Interactive Checkpoint**:
  > 🏷️ تم إعداد الإصدار `vX.Y.Z` وتحديث ملفات الميتاداتا. هل تريد إنشاء الـ Release على GitHub الآن؟
