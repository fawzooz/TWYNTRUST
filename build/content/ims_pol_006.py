from org import (AI_SYSTEMS, COMMITTEES, KEY_RISKS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, TECH,
                 ref, who)

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
SF, SM, AM, SAFE, CA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
ARR = next(k for k in COMMITTEES if "Release" in k)
CAPA = next(c for c in SAMPLE_CAPA if c[0] == "CA-2026-004")
NC = next(f for f in SAMPLE_AUDIT["findings"] if f[0] == CAPA[1])
R5 = next(r for r in KEY_RISKS if r[0] == "RSK-AI-005")

# Shared with IMS-REG-005 (Suppliers summary sheet). Supplier IDs use the format SUP-01.
# id, supplier (generic), service, tier, supports, data shared (highest class), region,
# AI clauses status, version pinning, certifications / evidence, owner key, last review, next review, status
SUPPLIERS = [
    ("SUP-01", "Foundation-model provider (enterprise API)", f"Text model behind {SM}", "Tier 1 — Critical",
     "AI-SYS-002; AST-004, AST-008", "Restricted (customer scripts, in transit only)", "US (EU processing option)",
     "Yes — no training, zero retention, 60-day change notice", "Yes — dated model version pinned",
     "SOC 2 Type II; ISO/IEC 27001; ISO/IEC 42001; model card and system card", "CAIO", "2026-06-10", "2027-06-10",
     "Implemented"),
    ("SUP-02", "Image-model provider (licensed base model)", f"Base image model fine-tuned for {SF}",
     "Tier 1 — Critical", "AI-SYS-001; AST-006", "Restricted (fine-tuning data, model weights)", "EU",
     "Yes — training-data provenance statement, 30-day retention, change notice", "Yes — base version pinned",
     "ISO/IEC 27001; licence warranty and IP indemnity; evaluation summary", "HOD", "2026-09-05", "2027-03-05",
     "Implemented"),
    ("SUP-03", f"{SAFE} vendor (content moderation)", "Prompt and image screening for prohibited content",
     "Tier 1 — Critical", "AI-SYS-004, AI-SYS-001", "Restricted (prompts and generated images)", "EU",
     "Partial — change-notice and pinning clause being added (CA-2026-004)", "Yes — via console (since INC-2026-007)",
     "SOC 2 Type II; detection-rate report quarterly", "CREA", "2026-08-20", "2026-11-30", "In progress"),
    ("SUP-04", "AWS", "Cloud hosting, storage, compute (eu-west-1, me-central-1)", "Tier 1 — Critical",
     "AST-001, AST-004, AST-005, AST-006, AST-012", "Restricted (all production data, encrypted)", "EU and UAE",
     "Not applicable (infrastructure); AI services not used for our data", "Not applicable",
     "ISO/IEC 27001, 27017, 27018; SOC 2; shared-responsibility model reviewed", "SRE", "2026-05-15",
     "2027-05-15", "Implemented"),
    ("SUP-05", "GitHub", "Source code hosting, CI/CD, code scanning", "Tier 2 — Important", "AST-002, AST-009",
     "Confidential (source code)", "US", "Not applicable", "Not applicable",
     "SOC 2 Type II; ISO/IEC 27001", "CTO", "2026-04-02", "2027-04-02", "Implemented"),
    ("SUP-06", "Payment processor (PCI DSS Level 1)", "Card payments and artist payouts for Commons",
     "Tier 1 — Critical", "AST-003", "Confidential (payout details; card data never reaches us)", "EU and US",
     "Not applicable (fraud ML is theirs; we only receive scores)", "Not applicable",
     "PCI DSS Attestation of Compliance; SOC 2", "HOP", "2026-03-20", "2027-03-20", "Implemented"),
    ("SUP-07", f"{CA} vendor (AI coding assistant, business plan)", "Code suggestions in the IDE",
     "Tier 2 — Important", "AI-SYS-005; AST-009", "Confidential (code snippets in prompts)", "US",
     "Yes — no training on our code, no retention of prompts", "Not available — vendor updates centrally",
     "SOC 2 Type II; admin settings screenshot on file", "CTO", "2026-07-01", "2027-07-01", "Implemented"),
    ("SUP-08", "[[supplier name]]", "[[service]]", "[[tier]]", "[[systems / assets]]", "[[data class]]",
     "[[region]]", "[[Yes / Partial / No]]", "[[Yes / No / n/a]]", "[[evidence]]", "IMSC", "[[date]]", "[[date]]",
     "Planned"),
]
SUP = {s[0]: s for s in SUPPLIERS}

DOC = {
    "id": "IMS-POL-006",
    "summary": f"How {N} chooses, contracts, monitors and leaves suppliers — with extra rules for suppliers whose "
               "AI models, data or services become part of our own AI systems.",
    "clauses": {"27001": "8.1 (externally provided processes); Annex A 5.19, 5.20, 5.21, 5.22, 5.23",
                "42001": "8.1 (externally provided processes); Annex A.10.2, A.10.3, A.10.4"},
    "howto": [
        "Most startups' biggest AI risks sit with suppliers: you rent the model, so you inherit its changes. "
        "Section 7 (model change and version pinning) is the part to copy first.",
        "Use the supplier register (section 9) as the single list; the same list feeds the Suppliers sheet in "
        f"{ref('IMS-REG-005')}.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"{N} has no data centre and trains no model from scratch. Our product runs on cloud infrastructure, "
              "third-party foundation and image models, a content-moderation service and many SaaS tools. Each of "
              "them can protect or expose our customers' scripts, our artists' work and the people shown in "
              "generated images. This policy makes sure suppliers are chosen with care, bound by clear contracts, "
              "watched while we use them and left safely."),
        ("h1", "2. Scope"),
        ("p", "All suppliers that access, store, process or transmit our information, or that provide a "
              "component, model, dataset or service used in an AI system in scope. It also covers what we promise "
              "our own customers about the AI we supply to them (42001 A.10.4)."),
        ("std", [
            "ISO/IEC 27001 expects you to manage security risks from suppliers, agree security requirements in "
            "contracts, manage risks in the technology supply chain, monitor and review supplier services and "
            "their changes, and have rules for acquiring, using, managing and exiting cloud services "
            "(Annex A 5.19–5.23).",
            "ISO/IEC 42001 expects responsibilities across the AI life cycle to be shared out clearly between you, "
            "your suppliers, partners and customers; a process so that suppliers' services, products and materials "
            "fit your approach to responsible AI; and attention to your customers' needs and expectations "
            "(Annex A.10.2–A.10.4).",
            "Both standards' Clause 8.1 also ask that externally provided processes, products and services that "
            "matter to the management system are controlled.",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Responsibility"], [
            (who("DPO"), "Owns this policy and the contract templates; signs data processing agreements; owns "
                         f"{CAPA[0]}."),
            ("Supplier owner (named per supplier)", "Business owner who requests the supplier, completes due "
             "diligence with help, monitors performance and runs the yearly review."),
            (who("CISO"), "Reviews security due diligence for Tier 1 and Tier 2 suppliers; approves cloud services."),
            (who("CAIO"), f"Reviews AI-specific due diligence; decides when a supplier model change needs the {ARR}."),
            (who("LEGAL"), "Negotiates IP, licence, indemnity and liability terms."),
            (who("IMSC"), "Keeps the supplier register and the review calendar."),
            ("Everyone", "Does not sign up for a new tool that handles company data without this process "
                         f"({ref('IMS-POL-005')})."),
        ], [5.5, 11]),
        ("h1", "4. Supplier tiers"),
        ("table", ["Tier", "Definition", "Due diligence", "Review"], [
            ("Tier 1 — Critical", "Handles Restricted data, runs production, or is part of an AI system or "
             "control (a model, a safety filter)", "Full questionnaire incl. AI section; certificates; "
             "contract with all clauses in section 6; Security Lead and Head of AI sign-off", "Every 6–12 months "
             "and on any major change"),
            ("Tier 2 — Important", "Handles Confidential data or supports engineering", "Short questionnaire; "
             "certificate or SOC 2 report; standard DPA", "Yearly"),
            ("Tier 3 — Low", "Internal or Public data only; easy to replace", "Check terms, SSO support and data "
             "location", "Every 2 years or at renewal"),
        ], [3, 5, 5.5, 3]),
        ("tip", "Do not try to assess 80 SaaS tools in depth. Tier them in an afternoon; spend 80% of your effort "
                "on the five to eight Tier 1 suppliers. That is exactly what auditors expect to see."),
        ("h1", "5. Due diligence before we sign"),
        ("p", "The supplier owner sends the questionnaire, collects evidence and records the outcome in the register. "
              "Gaps become contract clauses, compensating controls or a documented risk acceptance "
              f"in {ref('IMS-REG-002')}."),
        ("h2", "5.1 Security and privacy questions (all tiers, scaled)"),
        ("bullets", [
            "Certifications and reports (ISO/IEC 27001, SOC 2, PCI DSS, ISO/IEC 42001) and their scope.",
            "Where data is stored and processed; sub-processors and their countries.",
            "Encryption in transit and at rest; key management; SSO and MFA support for our users.",
            "Vulnerability management, penetration testing, secure development practices.",
            "Incident notification time; business continuity and recovery objectives.",
            "Data deletion at contract end, with confirmation.",
        ]),
        ("h2", "5.2 AI-specific questions (any supplier providing a model, dataset or AI service)"),
        ("table", ["#", "Question", "What a good answer looks like"], [
            ("AI-1", "Do you use our inputs, outputs or files to train or improve any model?",
             "No, by contract, for all our data — not just an opt-out setting"),
            ("AI-2", "How long do you retain prompts, outputs and files? Who can see them?",
             "Zero retention, or ≤ 30 days for abuse monitoring, with restricted staff access"),
            ("AI-3", "How will you tell us about model changes? Can we pin a version?",
             "Written notice ≥ 30 days before material changes; dated versions available ≥ 90 days"),
            ("AI-4", "What evaluations do you run (quality, safety, bias, robustness) and can we see results?",
             "Model or system card; evaluation summary; red-team approach described"),
            ("AI-5", "What content-safety and misuse protections are built in?",
             "Documented filters, abuse monitoring, and how false negatives are handled"),
            ("AI-6", "Where did the training data come from? Do you warrant you have the rights?",
             "Provenance statement; respect for TDM opt-outs; IP indemnity"),
            ("AI-7", "Which sub-processors or other model providers sit behind your service?",
             "Named list with notice of changes"),
            ("AI-8", "What logs and explanations can you give us when something goes wrong?",
             "Request IDs, model version per call, incident support within 24 hours"),
            ("AI-9", "Are you prepared for EU AI Act duties that apply to you (e.g. general-purpose model "
                     "documentation for downstream providers)?", "Named contact; documentation available"),
        ], [1.2, 7.3, 8]),
        ("h1", "6. Contract clauses"),
        ("p", f"The DPO keeps two templates: the standard supplier agreement + DPA, and the **AI supplier contract "
              "template** that adds the AI clauses. Tier 1 contracts must include every applicable clause below."),
        ("table", ["Clause", "Requirement", "Tier"], [
            ("Security requirements", "Controls at least equal to ours; encryption; MFA; vulnerability fixes", "1, 2"),
            ("Data processing agreement", "Purpose, data types, sub-processors, transfers safeguards, deletion", "All with personal data"),
            ("Breach notification", "Tell us within 24 hours of a confirmed incident affecting our data", "1, 2"),
            ("Right to audit / reports", "Annual certificates or SOC 2 report; questionnaire on request", "1"),
            ("No training on our data", "Inputs, outputs and files not used to train or improve models", "AI"),
            ("Retention limits", "Zero or ≤ 30 days; deletion on request and at exit", "AI"),
            ("**Model change notification**", "Written notice ≥ 30 days before a material model change "
             "(≥ 5 working days for urgent safety fixes), with release notes and evaluation summary", "AI"),
            ("**Version pinning**", "Our right to stay on a named model version for ≥ 90 days after notice, "
             "and to roll back if a new version fails our tests", "AI"),
            ("Evaluation and safety information", "Model/system card; material safety findings shared", "AI"),
            ("IP warranty and indemnity", "Rights to training data; indemnity for infringement claims", "AI (models)"),
            ("Sub-processor changes", "30 days' notice with right to object", "1"),
            ("Continuity and exit", "Data export in standard format; deletion certificate; transition support", "1"),
        ], [4.2, 9.8, 2.5]),
        ("h1", "7. Model change and version pinning"),
        ("p", f"A supplier changing its model changes our AI system. Therefore, under {ref('IMS-POL-002')}, "
              "supplier model changes are on the change-management trigger list:"),
        ("steps", [
            "We pin every supplier model to a dated version in configuration. 'Latest' aliases are not allowed in "
            "production.",
            "When notice arrives, the supplier owner opens a change ticket (class: Significant AI change).",
            "The new version is tested in staging against our evaluation and canary sets "
            "(quality, safety, leakage, likeness detection).",
            f"The {ARR} approves the switch, or we stay pinned and ask the supplier to fix the issue.",
            "If a supplier changes a model without notice, we treat it as an incident "
            f"({ref('IMS-PRO-005')}) and as a contract breach to raise with them.",
        ]),
        ("example", f"{SAMPLE_INCIDENT['id']} → {NC[0]} → {CAPA[0]}", [
            f"**Incident.** {SAMPLE_INCIDENT['summary']}",
            f"**Audit finding.** {SAMPLE_AUDIT['id']} raised {NC[0]} ({NC[1].lower()}, {NC[2]}): {NC[3]}",
            f"**Corrective action {CAPA[0]}** (owner: {who(CAPA[3])}, due {CAPA[4]}). {CAPA[2]}",
            "**What changed in this policy.** The AI supplier contract template now requires model change "
            f"notification and version pinning (section 6); the {SAFE} agreement is being amended; supplier model "
            f"changes are now a change trigger (section 7). Linked risk: {R5[0]} — {R5[1]}.",
        ]),
        ("h1", "8. Cloud services, ICT supply chain and monitoring"),
        ("h2", "8.1 Cloud services (27001 5.23)"),
        ("bullets", [
            f"Approved platform: {TECH['cloud']}. New cloud services need Security Lead approval and a register entry.",
            "We document the shared-responsibility split for each Tier 1 cloud service: what the provider secures "
            "and what we must configure (IAM, encryption, logging, backups, public access).",
            "Accounts are managed as code with guardrails (no public buckets, logging always on, region limits).",
            "Exit: we keep infrastructure as code and data export scripts so we could move within 90 days.",
        ]),
        ("h2", "8.2 ICT and AI supply chain (27001 5.21, 42001 A.10.3)"),
        ("bullets", [
            "Open-source libraries, container images, model files and datasets are supply-chain components: they "
            f"follow the dependency policy in {ref('IMS-POL-002')} (pinned, scanned, from trusted sources).",
            "We ask Tier 1 suppliers to name the models and sub-processors behind their service (question AI-7).",
        ]),
        ("h2", "8.3 Monitoring and review (27001 5.22)"),
        ("bullets", [
            f"Daily: our own canary tests watch {SAFE} and model behaviour; alerts go to the supplier owner.",
            "Monthly: availability and incident check for Tier 1 suppliers in the Trust Council pack.",
            "Yearly (6-monthly for AI Tier 1): review certificates, questionnaire updates, incidents, change notices "
            "received and whether the supplier is still the right choice. Record the result in the register.",
        ]),
        ("h2", "8.4 Our duties to customers (42001 A.10.4)"),
        ("p", f"We tell our customers which AI systems they are using, their intended use and limits, that their "
              "data is not used for training without opt-in, how outputs are labelled, and how to report problems. "
              "API customers receive our own model change notices 30 days ahead — we offer them what we ask of "
              "our suppliers."),
        ("h1", "9. Supplier register (example)"),
        ("table", ["ID", "Supplier", "Tier", "Supports", "AI clauses", "Pinning", "Next review"],
         [(s[0], s[1], s[3].split(" — ")[0], s[4], s[7], s[8], s[12]) for s in SUPPLIERS], [1.3, 3.2, 1.4, 2.6, 3.6, 2.4, 2]),
        ("p", f"The full register, with data, regions, evidence and owners, is the Suppliers sheet in "
              f"{ref('IMS-REG-005')}."),
        ("h1", "10. Exit"),
        ("bullets", [
            "Each Tier 1 supplier has a short exit note: alternative supplier, data export method, time needed.",
            "At exit we revoke keys and accounts within 24 hours, get data returned or deleted with written "
            "confirmation, and update the register and inventory.",
            "For a model supplier we re-run the full AI evaluation on the replacement before switching.",
        ]),
        ("h1", "11. Records produced"),
        ("bullets", ["Supplier register and tiering", "Completed questionnaires and evidence (certificates, reports)",
                     "Signed contracts and DPAs", "Change notices received and related change tickets",
                     "Review records and exit notes"]),
        ("h1", "12. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-POL-002", "IMS-POL-003", "IMS-POL-005", "IMS-PRO-005",
                                      "IMS-PRO-006", "IMS-PRO-009", "IMS-REG-002", "IMS-REG-005", "IMS-REG-008")]),
    ],
}
