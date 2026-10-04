# TWYNTRUST — one management system for ISO/IEC 27001 and ISO/IEC 42001

**Two standards. One system. Trust you can prove.**

TWYNTRUST is a free, ready-to-adapt starter kit for organisations that want to build an
**information security management system (ISMS, ISO/IEC 27001:2022)** and an
**AI management system (AIMS, ISO/IEC 42001:2023)** at the same time, as **one integrated system**.

It is written for people who are doing this for the first time: founders, engineering leads,
security and compliance people at startups and SMEs. Every document is fully filled in for a
realistic sample company, so you can see what "good" looks like, then replace the sample with
your own facts.

The kit is a practical companion to two books by Prof. Dr. Mohamed Fawzi Elgendi (Fawzooz):
[**AISEC Mastery**] (ISO/IEC 42001) and **AppSec Mastery** (ISO/IEC 27001 and secure software development).

> TWYNTRUST v2 succeeds the earlier **TRACE** framework (v1, AIMS only).

---

## Why one system?

ISO/IEC 27001 and ISO/IEC 42001 share the same management-system skeleton (Clauses 4–10).
Running them separately doubles the meetings, the risk registers, the audits and the paperwork.
TWYNTRUST *twins* them:

| Shared once | Kept separate where the standards differ |
|---|---|
| Context, scope, interested parties, legal register | Two Statements of Applicability (27001 Annex A: 93 controls · 42001 Annex A: 38 controls) |
| Leadership, one policy, one governance committee | AI system impact assessments (42001 clauses 6.1.4 and 8.4) |
| One risk method and one risk register | AI-specific lifecycle, data and transparency controls |
| One competence, awareness and document-control process | |
| One internal audit, one management review, one corrective-action log | |

## The five strands

| # | Strand | What you do | Clauses | Folder |
|---|---|---|---|---|
| 1 | **Ground** | Understand context, set one scope, appoint leaders, publish one policy | 4–5 | `01 Ground - Context and Leadership` |
| 2 | **Gauge** | One risk method for security and AI, impact assessments, controls, objectives | 6 | `02 Gauge - Risk and Planning` |
| 3 | **Equip** | Competence, awareness, communication, document control | 7 | `03 Equip - Support` |
| 4 | **Operate** | Secure and responsible lifecycle, data, access, suppliers, incidents, continuity | 8 + Annex A | `04 Operate - Lifecycle Controls` |
| 5 | **Prove and improve** | Measure, audit, management review, corrective action | 9–10 | `05 Prove and Improve` |

## Start here

1. Open **`00 Start Here/IMS-GDE-001 Start Here - …docx`**. It explains the whole kit in plain language
   and gives you a 16–20 week route to certification.
2. Open **`00 Start Here/IMS-WBK-001 Starter Workbook …xlsx`**. Run the gap assessment, adapt the roadmap,
   and use the clause crosswalk and document register.
3. Work through the strands in order. Each document opens with a "How to use this document" box.

Conventions used in every document:

- **Yellow `[brackets]`** are values you must fill in or confirm.
- **Green "Worked example"** boxes show a completed answer for the sample company.
- **Blue "Starter tip"** boxes are guidance for you. Delete them in your final version.
- **Amber "What the standards expect"** boxes summarise requirements in plain words (not ISO text).

## The sample company

**Quillfen Studio** is a fictional 34-person creative-tech startup. It offers AI-assisted
storyboarding and concept art for publishers, game studios and agencies, plus a marketplace
of freelance artists. It has five AI systems with different roles: StoryFrame (image generation),
ScriptMate (writing assistant), ArtistMatch (artist ranking), SafeFrame (bought-in content moderation)
and CodeAssist (internal coding assistant). Its risks show why the two standards belong together:
artists' consent and copyright, deepfakes, fairness to artists, leaks of unreleased scripts,
phishing, and supplier model changes.

The company is fictional. People appear as role tags such as **[CEO]**, **[Security Lead]** and
**[Head of AI]**: replace them with your own names, or keep them for role-based documents.

## Kit contents

| ID | Document | Type |
|---|---|---|
| IMS-GDE-001 | Start Here — Build Your ISMS and AIMS with TWYNTRUST | Guide |
| IMS-WBK-001 | Starter Workbook — Gap Assessment, Roadmap, Crosswalk and Document Register | Workbook |
| IMS-MAN-001 | Integrated Management System Manual (ISMS + AIMS) | Manual |
| IMS-REG-001 | Context, Interested Parties and Scope Register | Register |
| IMS-POL-001 | Information Security and Responsible AI Policy | Policy |
| IMS-GOV-001 | Governance Charter, Roles and Responsibilities | Charter |
| IMS-PRO-001 | Risk Management Methodology (Information Security and AI) | Procedure |
| IMS-REG-002 | Integrated Risk Register and Treatment Plan | Register |
| IMS-PRO-002 | AI System Impact Assessment Procedure and Worked Example | Procedure |
| IMS-SOA-001 | Statement of Applicability — ISO/IEC 27001:2022 Annex A | Register |
| IMS-SOA-002 | Statement of Applicability — ISO/IEC 42001:2023 Annex A | Register |
| IMS-REG-003 | Objectives, Metrics and Monitoring Plan | Register |
| IMS-PRO-003 | Competence, Awareness and Communication Procedure | Procedure |
| IMS-REG-004 | Competence Matrix, Training Records and Communication Plan | Register |
| IMS-PRO-004 | Documented Information Control Procedure | Procedure |
| IMS-POL-002 | Secure and Responsible Development Lifecycle Policy (AppSec + AI) | Policy |
| IMS-POL-003 | Data Governance and Privacy Policy for AI | Policy |
| IMS-POL-004 | Access Control Policy | Policy |
| IMS-POL-005 | Acceptable Use Policy (including Generative AI) | Policy |
| IMS-POL-006 | Supplier and Third-Party AI Policy | Policy |
| IMS-PRO-005 | Incident Management Procedure (Security and AI Incidents) | Procedure |
| IMS-PRO-006 | Business Continuity and ICT Readiness Plan | Plan |
| IMS-REG-005 | Asset and AI System Inventory | Register |
| IMS-REG-006 | Incident and Event Log | Register |
| IMS-PRO-007 | Internal Audit Procedure, Programme and Report Template | Procedure |
| IMS-REG-007 | Internal Audit Programme and Checklist | Register |
| IMS-PRO-008 | Management Review Procedure and Example Minutes | Procedure |
| IMS-PRO-009 | Nonconformity, Corrective Action and Improvement Procedure | Procedure |
| IMS-REG-008 | Nonconformity, Corrective Action and Improvement Log | Register |

## Adapting the kit to your organisation

You can edit the Word and Excel files directly. If you are comfortable with Python, there is a faster way.
The whole kit is generated from plain-text sources in [`build/`](build/README.md), and all organisation facts
(company name, people, AI systems, risk scales, document owners) live in one file,
[`build/org.py`](build/org.py). Change that file, run one command, and every document is regenerated with
your names and systems.

```bash
pip install python-docx openpyxl
python build/build.py
```

## Important notes

- **This kit does not contain ISO text.** Clause and control numbers are referenced, and requirements are
  described in our own words. To implement and certify you need licensed copies of ISO/IEC 27001:2022
  (with Amd 1:2024) and ISO/IEC 42001:2023, available from ISO or your national standards body.
  ISO/IEC 27002, 23894, 42005 and 22989 are useful guidance.
- **A template is not a management system.** Certification auditors look for evidence that you *operate*
  the processes: records, decisions, measurements and improvements over time.
- **Not legal advice.** Laws named in the sample (UAE PDPL, GDPR, EU AI Act and others) are examples.
  Confirm your own obligations with qualified advisers.

## Contributing

Issues and pull requests are welcome: clearer wording, sector adaptations, translations,
and corrections. Please edit the sources in `build/content/` rather than the generated files.

## License

- **Documents and written content** (everything in the kit folders, plus the text in `build/content/`):
  [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
  You may use, adapt and share the kit for any purpose, commercial use included, as long as you give credit:

  > Based on the TWYNTRUST Framework by Prof. Dr. Mohamed Fawzi Elgendi (Fawzooz), Fawzooz.ai —
  > licensed under CC BY 4.0. Changes were made.

- **Generator code** (`build/build.py`, `build/lib.py`, `build/check.py`): [MIT License](LICENSE-CODE).

Your own completed documents, made from the templates, are yours. The credit line is needed when you
share or publish the kit, or a version adapted from it.

---

Developed by **Fawzooz.ai** · Version 2.0 · ISO/IEC 27001:2022 + ISO/IEC 42001:2023
