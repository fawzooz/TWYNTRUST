from org import AI_SYSTEMS, DOCS, ID_FORMATS, ORG, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}

DOC = {
    "id": "IMS-PRO-004",
    "summary": f"How {N} creates, approves, publishes, protects, keeps and retires the documents and records of "
               "its integrated management system — including the technical documentation and event logs that every "
               "AI system needs.",
    "clauses": {"27001": "7.5.1, 7.5.2, 7.5.3; Annex A 5.12, 5.13, 5.33, 5.37",
                "42001": "7.5.1, 7.5.2, 7.5.3; Annex A.6.2.3, A.6.2.7, A.6.2.8, A.7.5"},
    "howto": [
        "Choose your tools first (where documents live, where records live), then write this procedure around "
        "them. A procedure that describes a tool you do not use fails at the first audit question.",
        "The retention table in section 9 is a starting point. Check every period against your own laws and "
        "contracts with your legal adviser.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", "Documented information is the management system's memory. **Documents** tell people what to do "
              "(policies, procedures, templates) and change over time. **Records** prove what was done (a completed "
              "risk assessment, an audit report, a training completion) and must not be changed afterwards."),
        ("p", f"This procedure makes sure that at {N}: people always use the current version; documents are "
              "reviewed and approved by the right person; sensitive documents are protected; records are kept long "
              "enough to prove what happened — and no longer; and every AI system has the documentation and logs "
              "needed to explain, audit and fix it."),
        ("h1", "2. Scope"),
        ("p", f"All documented information required by ISO/IEC 27001 and ISO/IEC 42001 or that we decided is "
              f"needed for the system to work: the documents listed in the master document register in "
              f"{ref('IMS-WBK-001')}, the records they produce, AI system technical documentation and logs, and "
              "external documents we rely on (standards, laws, supplier documentation)."),
        ("std", [
            "Both standards require the documented information they name, plus whatever else you decide is needed "
            "to run the system effectively. The size of your documentation can match the size of your company.",
            "When creating or updating documents you need proper identification (title, date, author or reference "
            "number), a suitable format, and review and approval (Clause 7.5.2).",
            "Documents must be available where needed and adequately protected. You must control distribution, "
            "access, storage, changes (version control), retention and disposal, including external documents "
            "(Clause 7.5.3).",
            "ISO/IEC 42001 adds AI-specific documentation: records of design and development, technical documentation "
            "for each AI system suitable for the people who need it, and deciding when event logs are recorded "
            "(A.6.2.3, A.6.2.7, A.6.2.8), plus data provenance records (A.7.5).",
        ]),
        ("h1", "3. Roles and responsibilities"),
        ("table", ["Who", "Responsibility"], [
            (who("IMSC"), "Owns this procedure and the master document register. Checks format and ID before "
                          "publishing; runs the review calendar; archives obsolete versions."),
            ("Document owner (named in the register)", "Writes and maintains the document; reviews it on schedule; "
                                                       "proposes changes; makes sure their team knows about them."),
            (who("CEO") + " / Trust Council", "Approves the Manual, top-level and topic policies, and the "
                                              "Statements of Applicability."),
            (who("CISO") + " and " + who("CAIO"), "Approve procedures and registers in their area; approve access "
                                                  "to Restricted documents."),
            (who("HOD"), "Owns dataset provenance records and model cards for models we train or fine-tune."),
            (who("SRE"), "Runs log retention and backup of the document and record stores."),
            ("Everyone", "Use only the published version; never keep private copies of Restricted documents."),
        ], [6, 10.5]),
        ("h1", "4. Document hierarchy"),
        ("table", ["Level", "What", "Examples", "Approved by"], [
            ("1", "Direction", f"{ref('IMS-MAN-001')}; {ref('IMS-POL-001')}", "Trust Council"),
            ("2", "Topic policies and governance", "IMS-POL-002 to IMS-POL-006; IMS-GOV-001; IMS-SOA-001/002",
             "Trust Council"),
            ("3", "Procedures and methods", "IMS-PRO-001 to IMS-PRO-009", "Security Lead or Head of AI"),
            ("4", "Registers, templates, work instructions, runbooks", "IMS-REG-001 to IMS-REG-008; on-call runbooks; "
                                                                    "model card template", "Document owner"),
            ("5", "Records", "Completed AIIAs, audit reports, training records, logs, tickets", "Not approved — "
                                                                                              "protected from change"),
        ], [1.5, 4, 7.5, 3.5]),
        ("h1", "5. Identification"),
        ("p", "Every controlled document has an ID of the form **IMS-TYPE-NNN**, where TYPE is one of:"),
        ("table", ["Type", "Meaning", "Example"], [
            ("GDE", "Guide", "IMS-GDE-001"), ("WBK", "Workbook", "IMS-WBK-001"),
            ("MAN", "Manual", "IMS-MAN-001"), ("POL", "Policy", "IMS-POL-004"),
            ("GOV", "Governance charter", "IMS-GOV-001"), ("PRO", "Procedure", "IMS-PRO-004"),
            ("REG", "Register (spreadsheet or database)", "IMS-REG-002"),
            ("SOA", "Statement of Applicability", "IMS-SOA-002"),
        ], [2.5, 8, 6]),
        ("p", "Records use their own ID patterns so they can be cross-referenced across tools:"),
        ("table", ["Record", "ID pattern"], [(a, b) for a, b in ID_FORMATS], [10, 6.5]),
        ("p", "Each document shows on its front page: ID, title, version, status, classification, owner, approver, "
              "effective date, next review date and the clauses it addresses. Every page carries the ID, version and "
              "classification in the footer."),
        ("tip", f"Start your register by copying the {len(DOCS)}-row document list from the kit and deleting what "
                "you do not need. Do not renumber when you delete a document — retire the ID instead, so old "
                "references still make sense."),
        ("h1", "6. Creating, reviewing and approving"),
        ("steps", [
            "**Draft.** The owner starts from the kit template (or the Git template for policies-as-code) and saves "
            "it as version 0.1 with status 'Draft'.",
            "**Review.** At least one reviewer outside the author's team reads it — for AI documents, someone from the "
            "AI Release Review; for anything customer-facing, the Privacy and Legal Lead. Comments are resolved in "
            "the tool (wiki comments or a Git pull request).",
            "**Approve.** The approver from section 4 approves. In Git, the approving review on the pull request is "
            "the approval record; on the wiki, the approver ticks the approval property and the page history keeps "
            "the date.",
            "**Publish.** The Compliance Coordinator sets the version (1.0, 1.1, 2.0…), updates the register and "
            "announces the change in #announcements within 5 working days (communication plan COM-01 in "
            f"{ref('IMS-REG-004')}). Policies that need acknowledgement are pushed to the HR system.",
            "**Review on schedule.** Policies and the Manual yearly; procedures yearly; registers at least every "
            "6 months or as their procedure says; and always after a major incident, audit finding, law change or "
            "significant AI system change.",
        ]),
        ("table", ["Change", "Version", "Re-approval?"], [
            ("Typo, broken link, formatting", "1.0 → 1.1", "No — owner approves; noted in revision history"),
            ("New or changed requirement, role or deadline", "1.1 → 2.0", "Yes — full approval"),
            ("Draft", "0.x", "Not yet in force"),
        ], [7, 3, 6.5]),
        ("h1", "7. Where documents and records live"),
        ("p", f"{N} has no file server. We use a small set of cloud tools, each with single sign-on and MFA "
              f"({ref('IMS-POL-004')}):"),
        ("table", ["Store", "What lives there", "Version control and protection"], [
            ("Company wiki (Trust space)", "Published Manual, policies, procedures, runbooks, awareness pages",
             "Page history; edit rights for owners only; everyone else read-only"),
            ("Git repository 'trust-docs' on GitHub (policies-as-code)", "Markdown source of policies and procedures; "
             "SoA and register CSV snapshots; templates", "Pull request with required approver = approval record; "
             "tags = versions; protected main branch"),
            ("Shared drive — IMS folder", "Registers (xlsx), audit reports, management review minutes",
             "Folder permissions by role; version history; Restricted subfolders"),
            ("Model registry and ML repository", "Model cards, evaluation reports, dataset manifests, training configs",
             "Immutable model versions; access limited to Data and ML team"),
            ("Consent ledger", "Artist consent and licence records linked to dataset items", "Append-only; changes "
             "logged; Restricted"),
            ("Ticketing system", "Incidents, corrective actions, access requests, AI concern reports",
             "Audit trail per ticket"),
            ("Log platform", "Application, security and AI event logs", "Write-once retention policies; "
             "access for SRE and Security only"),
            ("HR system and learning platform", "Training records, acknowledgements, CVs, certificates",
             "HR and line-manager access only"),
        ], [4.5, 6, 6]),
        ("example", "A policy change through Git", [
            f"The Security Lead wants to shorten the quarterly access review window in {ref('IMS-POL-004')}. "
            "He opens a branch in 'trust-docs', edits the Markdown, and raises a pull request.",
            "GitHub requires an approving review from a Trust Council member (CODEOWNERS file). The CTO approves; "
            "the Compliance Coordinator merges, tags the commit 'IMS-POL-004-v2.0', and the CI pipeline publishes the "
            "rendered page to the wiki and exports a PDF to the IMS folder.",
            "Evidence for the auditor: the pull request (who changed what, who approved, when), the tag, and the "
            "announcement link — no separate approval form needed.",
        ]),
        ("h1", "8. Access, classification and protection"),
        ("p", "Every document and record has one of four classifications:"),
        ("table", ["Class", "Meaning", "Examples", "Handling"], [
            ("Public", "Approved for anyone", "Trust Centre page, AI system summary pages", "No restriction once "
                                                                                          "approved"),
            ("Internal", "For staff and contractors", "Most policies and procedures in this kit", "Company tools only"),
            ("Confidential", "Need-to-know within the company", "Risk register, audit reports, source code, logs",
             "Role-based access; no external sharing without NDA"),
            ("Restricted", "Highest harm if exposed", "Customer scripts, artist portfolios and consent records, "
                                                       "training datasets and model weights, secrets, breach files",
             "Named access, approved by owner; encrypted; access logged"),
        ], [2.5, 4, 6, 4]),
        ("p", "Labels: documents show the class in the footer; repositories, folders and buckets carry the class in "
              "their name or tag. When in doubt, use the higher class. Printed copies are uncontrolled and must be "
              "shredded after use."),
        ("h1", "9. Retention and disposal"),
        ("p", "Records are kept for the period below, then deleted or anonymised. Where a law, contract or legal "
              "hold requires longer, the longer period wins. The owner of each store sets automatic deletion where the "
              "tool allows."),
        ("table", ["Record", "Standard link", "Retention", "Owner"], [
            ("Superseded versions of policies, procedures, SoAs", "27001 / 42001 7.5", "6 years after replacement",
             title_of("IMSC")),
            ("Risk register snapshots, risk acceptance decisions", "27001 6.1.3, 8.3; 42001 6.1, 8.3", "6 years",
             title_of("CISO")),
            ("AI system impact assessments (AIIA-…)", "42001 6.1.4, 8.4, A.5.3", "Life of the AI system + 6 years",
             title_of("CAIO")),
            ("Internal audit reports and evidence", "9.2 (both)", "6 years (two certification cycles)",
             title_of("IMSC")),
            ("Management review minutes", "9.3 (both)", "6 years", title_of("IMSC")),
            ("Nonconformities and corrective actions", "10.2 (both)", "6 years", title_of("IMSC")),
            ("Training and competence records", "7.2 (both)", "Employment + 2 years", title_of("HOP")),
            ("Incident records and post-incident reviews", "27001 A 5.24–5.28; 42001 A.8.4", "6 years",
             title_of("CISO")),
            ("Access requests and quarterly access reviews", "27001 A 5.18", "3 years", title_of("CISO")),
            ("Dataset provenance, licence and consent records", "42001 A.7.5, A.7.3", "Life of any model trained on "
             "the data + 6 years", title_of("HOD")),
            ("Model cards, evaluation and fairness test reports", "42001 A.6.2.3–A.6.2.7", "Life of the model + 6 years",
             title_of("HOD")),
            ("AI Release Review decisions", "42001 A.6.2.5", "Life of the AI system + 6 years", title_of("CAIO")),
            ("AI event logs — prompts and outputs (metadata)", "42001 A.6.2.8", "12 months", title_of("SRE")),
            ("AI event logs — content-safety decisions and blocked items", "42001 A.6.2.8, A.6.2.6", "24 months",
             title_of("SRE")),
            ("Security logs (authentication, admin actions)", "27001 A 8.15", "12 months online + 12 months archive",
             title_of("SRE")),
            ("Customer scripts and project files", "Contract; 27001 A 5.33, 8.10", "Contract term; deleted within "
             "30 days of account closure", title_of("CTO")),
            ("Supplier assessments and contracts", "27001 A 5.19–5.22; 42001 A.10", "Contract + 6 years",
             title_of("DPO")),
        ], [5.5, 4, 4.5, 2.5]),
        ("p", "Disposal: digital records are deleted through the tool's deletion function (cloud storage lifecycle "
              "rules, log retention policies); deletion of Restricted data is logged. Laptops are wiped through device "
              "management before reuse or recycling."),
        ("tip", "Logs of prompts can contain personal data and unreleased scripts. Keep metadata (who, when, which "
                "model version, safety verdict) longer than full content — it is enough to investigate most incidents "
                "and much safer to hold."),
        ("h1", "10. AI system documentation"),
        ("h2", "10.1 Technical documentation (A.6.2.7)"),
        ("p", "Each AI system in the inventory has a documentation pack, kept in the model registry and linked from "
              f"{ref('IMS-REG-005')}. It is written for three readers: engineers who maintain it, reviewers and "
              "auditors who check it, and (in a shortened public form) users. Minimum contents:"),
        ("bullets", [
            "Purpose, intended users and uses, and uses we do not support.",
            "Our role for the system (provider, producer, user) and the suppliers involved.",
            "Architecture overview: models and versions, data flows, guardrails, human oversight points.",
            "Data: datasets used, their provenance and consent status, and data-quality checks (link to the dataset "
            "manifest).",
            "Evaluation: accuracy, robustness, fairness and safety test results against release criteria.",
            "Known limitations and residual risks (link to risk IDs and the AIIA).",
            "Operating instructions: monitoring, thresholds, rollback, and how to switch the feature off.",
            "Change history and AI Release Review decisions.",
        ]),
        ("h2", "10.2 Event logs (A.6.2.8)"),
        ("p", "We decide per system which events are logged, and for how long, during design — not after an "
              "incident. The baseline:"),
        ("table", ["AI system", "Logged events"], [
            (SYS["AI-SYS-001"], "Request ID, user/org ID, model and filter versions, prompt hash, SafeFrame verdict, "
                                "likeness-check result, label and C2PA status of the output."),
            (SYS["AI-SYS-002"], "Request ID, user/org ID, model version, token counts, tenant isolation check, "
                                "user feedback flags."),
            (SYS["AI-SYS-003"], "Ranking request, model version, top-10 artist IDs shown, new-artist exposure "
                                "share, manual overrides."),
            (SYS["AI-SYS-004"], "Every verdict with vendor model version, category, score and reviewer override."),
            (SYS["AI-SYS-005"], "Seat assignment and admin-console audit log from the vendor (we do not log code "
                                "suggestions)."),
        ], [3.5, 13]),
        ("example", "Why the logs mattered", [
            "During INC-2026-007, the SafeFrame verdict log showed the vendor model version on every decision. The "
            "team could see exactly when the new version went live and which images it had passed, and re-screen "
            "them — in hours, not days.",
        ]),
        ("h1", "11. External documents"),
        ("p", "Standards, laws, supplier security and model documentation, and customer requirements are listed in "
              f"the document register in {ref('IMS-WBK-001')} as type 'External', with their version and the date we last checked "
              f"for updates. The {title_of('DPO')} checks laws and the owners check supplier documents every 6 months. "
              "Purchased ISO standards are stored in a Restricted folder because their licence limits sharing."),
        ("h1", "12. Obsolete documents"),
        ("bullets", [
            "When a new version is published, the old one is moved to the 'Archive' area (wiki archive space, Git "
            "history, or the shared drive's Archive folder) and marked 'SUPERSEDED'.",
            "Retired documents keep their ID; the register shows status 'Withdrawn' and the date.",
            "Nobody may work from an archived document. Links in other documents point to the register, not to a file.",
        ]),
        ("h1", "13. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-WBK-001", "IMS-MAN-001", "IMS-POL-003", "IMS-POL-004", "IMS-POL-002",
                                      "IMS-REG-005", "IMS-PRO-003")]),
        ("h1", "14. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("IMSC"), title_of("IMSC") + ", document owner", "[[signature]]", "[[date]]"),
            (person("CEO"), "CEO, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
