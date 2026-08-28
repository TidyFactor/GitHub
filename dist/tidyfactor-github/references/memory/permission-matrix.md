# Permission Matrix & Team Architecture (Least Privilege)

<!-- last-verified: 2026-08-29 -->

Standard organization team hierarchies, repository permission models, and CODEOWNERS routing.

---

## 1. Organization Team Hierarchy

```text
@org-root
├── @engineering
│   ├── @frontend
│   ├── @backend
│   └── @platform-core
├── @devops-infra
├── @security-leads
├── @documentation
└── @maintainers-triage
```

---

## 2. Standard Repository Permission Matrix

| Role Tier | `@devops-infra` | `@engineering` | `@maintainers` | `@documentation` | Outside Collabs |
|---|---|---|---|---|---|
| **Core Architecture Repos** | `Admin` | `Write` | `Maintain` | `Read` | `Read` |
| **Frontend / Web Apps** | `Admin` | `Write` | `Write` | `Write` (docs only) | `Triage` |
| **Public Open-Source Libs** | `Admin` | `Maintain` | `Maintain` | `Write` | `Read` |
| **Docs Portals / Specs** | `Maintain` | `Write` | `Write` | `Maintain` | `Read` |

---

## 3. CODEOWNERS Architecture Pattern

```text
# Default organization fallback
*                           @org/engineering

# Core architecture and kernel boundaries
/src/core/                  @org/platform-core
/app/Core/                  @org/platform-core

# Workflows and infrastructure
/.github/workflows/         @org/devops-infra @org/security-leads
/infra/                     @org/devops-infra
/Dockerfile                 @org/devops-infra

# Security Policies
/SECURITY.md                @org/security-leads

# Documentation
/docs/                      @org/documentation
/README.md                  @org/documentation
/README.ar.md               @org/documentation
```

---

## 4. Least Privilege Auditing Criteria

- ❌ **Direct Member Grants**: Flag any individual user with direct repository admin or write permissions. Move them into a defined team.
- ❌ **Excessive Admins**: Repositories must not have more than 3 direct admins.
- ❌ **Unrestricted Repo Creation**: Disable member repository creation in organizations; restrict creation to Maintainers and Admins.
