from org import (AI_SYSTEMS, DOCS, FRAMEWORK, FRAMEWORK_IDEA, KEY_RISKS, LEVELS, ORG, PUBLISHER, ROLES, SAMPLE_AUDIT,
                 STRANDS, TAGLINE, ID_FORMATS, person, ref, title_of, who)

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}

# One-line purpose for every document in the kit (kit map).
PURPOSE = {
    "IMS-GDE-001": "This guide: what the two standards ask for, how the kit fits together and a week-by-week path.",
    "IMS-WBK-001": "Your project tool: gap assessment against both standards, roadmap, clause crosswalk and the master document register.",
    "IMS-MAN-001": "The 'map of the system': walks through Clauses 4–10 once and shows how each one is met for both standards.",
    "IMS-REG-001": "Internal and external issues, interested parties, legal register, scope boundaries and your AI role for each system.",
    "IMS-POL-001": "The one top-level policy for information security and responsible AI, signed by the CEO.",
    "IMS-GOV-001": "Who decides what: Trust Council and AI Release Review charters, role descriptions, RACI chart, conflicts of interest.",
    "IMS-PRO-001": "One method to identify, score and treat information-security and AI risks, with the shared 5 x 5 scales.",
    "IMS-REG-002": "The live risk register and treatment plan, pre-filled with the example risks.",
    "IMS-PRO-002": "How to assess the impact of an AI system on people, groups and society — with a full worked example.",
    "IMS-SOA-001": "Statement of Applicability for the 93 ISO/IEC 27001 Annex A controls: applicable or not, why, and status.",
    "IMS-SOA-002": "Statement of Applicability for the ISO/IEC 42001 Annex A controls, same format.",
    "IMS-REG-003": "Objectives, how each is measured, targets, owners and the monitoring calendar.",
    "IMS-PRO-003": "How people become competent and aware, and how we communicate inside and outside the company.",
    "IMS-REG-004": "Competence matrix, training records and the communication plan.",
    "IMS-PRO-004": "How documents and records are created, approved, versioned, stored and retired.",
    "IMS-POL-002": "Security and responsibility built into every stage of software and AI development.",
    "IMS-POL-003": "Data governance and privacy for AI: sourcing, consent, quality, provenance and retention of data.",
    "IMS-POL-004": "Who gets access to what, how it is approved, reviewed and removed.",
    "IMS-POL-005": "Rules for everyday use of company systems, including which generative-AI tools staff may use and how.",
    "IMS-POL-006": "How suppliers — especially AI model and data suppliers — are chosen, contracted and monitored.",
    "IMS-PRO-005": "Detecting, reporting, handling and learning from security incidents and AI incidents.",
    "IMS-PRO-006": "Keeping the service running and recovering when a region, supplier or key person is lost.",
    "IMS-REG-005": "Inventory of information assets and AI systems, with owners and classification.",
    "IMS-REG-006": "Log of every reported event and incident, with severity, actions and lessons learned.",
    "IMS-PRO-007": "How to plan and run internal audits, with a report template.",
    "IMS-REG-007": "The audit programme and a combined checklist for both standards.",
    "IMS-PRO-008": "How top management reviews the system, with example minutes.",
    "IMS-PRO-009": "How to handle nonconformities, find root causes and fix them for good.",
    "IMS-REG-008": "The log of nonconformities, corrective actions and improvement ideas.",
}

FOLDERS = []
for _d in DOCS:
    if _d[3] not in FOLDERS:
        FOLDERS.append(_d[3])

KIT_MAP = []
for _folder in FOLDERS:
    for _id, _title, _owner, _f, _kind in DOCS:
        if _f == _folder:
            KIT_MAP.append((_id, f"{_title} ({_kind})", _folder, PURPOSE[_id]))

STRAND_ROWS = [(f"{n}. {name}", what, clauses, "\n".join(docs)) for n, name, what, clauses, docs in STRANDS]

DOC = {
    "id": "IMS-GDE-001",
    "summary": f"Read this first. A plain-English guide to building one integrated management system for "
               f"information security (ISO/IEC 27001) and responsible AI (ISO/IEC 42001) with the {FRAMEWORK} kit, "
               f"using {N} as the worked example.",
    "clauses": {"27001": "Overview of Clauses 4–10 and Annex A (orientation only — this guide is not a control document)",
                "42001": "Overview of Clauses 4–10 and Annexes A–D (orientation only)"},
    "howto": [
        "Read sections 1–4 before you open any other document. They take about 30 minutes.",
        "Use section 7 (the 16-week path) as your project plan, and track it in "
        "IMS-WBK-001, the Starter Workbook.",
        "You do not need to keep this guide in your final management system. It is a teaching document.",
    ],
    "body": [
        # ------------------------------------------------------------------
        ("h1", "1. Welcome"),
        ("p", f"This kit helps you build a management system that can be certified against two international "
              f"standards at once: **ISO/IEC 27001:2022** for information security and **ISO/IEC 42001:2023** for "
              f"artificial intelligence. It is written for people who have never done this before — a founder, a "
              f"first security hire, a head of AI or an operations lead who has been told 'we need ISO'."),
        ("p", f"Every document in the kit is filled in for a fictional company, **{N}**. You will see realistic "
              f"systems, risks and dates. People appear as role tags such as {who('CEO')} or {who('CISO')} — put your "
              f"own names in their place, or keep the tags if you prefer role-based documents. That is on purpose: a blank template tells you what headings to "
              f"write, but a worked example shows you what a good answer looks like. Your job is to replace "
              f"{N}'s facts with your own."),
        ("p", f"The kit is a companion to the books by {PUBLISHER}. The books explain the standards and the "
              f"thinking behind them in depth; this kit gives you the ready-to-adapt documents."),
        ("tip", "You will feel tempted to read the standards first, cover to cover. Buy them (you need your own "
                "licensed copies for an audit), but read them alongside this guide, one clause at a time. The "
                "standards are short, dense and written for experts; this guide translates them into tasks."),

        # ------------------------------------------------------------------
        ("h1", "2. What are an ISMS and an AIMS?"),
        ("h2", "2.1 A management system, in one paragraph"),
        ("p", "A **management system** is simply the way an organisation makes sure something important is done "
              "well, every time, and keeps getting better. It has a few fixed parts: you understand your situation, "
              "leaders set direction, you plan around your risks, you give people what they need, you do the work in "
              "a controlled way, you check how it went, and you fix what went wrong. That is the "
              "plan–do–check–act cycle, written down so that it does not depend on one heroic person."),
        ("h2", "2.2 ISMS — information security management system (ISO/IEC 27001)"),
        ("p", "An **ISMS** protects the confidentiality, integrity and availability of information: your customers' "
              "data, your source code, your staff records, your systems. ISO/IEC 27001 sets the requirements for the "
              "management system (Clauses 4–10) and lists 93 security controls in its Annex A — things like access "
              "control, secure development, backups, supplier security and incident handling. You do not have to "
              "use every control, but you must consider every one and explain your choice."),
        ("h2", "2.3 AIMS — AI management system (ISO/IEC 42001)"),
        ("p", "An **AIMS** makes sure that the AI systems you build, provide or use are developed and run "
              "responsibly: they are fair, transparent, safe, secure, respect privacy and stay under human "
              "control. ISO/IEC 42001 uses the same Clauses 4–10 skeleton as ISO/IEC 27001 and adds AI-specific "
              "requirements — most importantly the **AI system impact assessment**, which looks at the effect of an "
              "AI system on people and society, not only on your company. Its Annex A lists 38 AI controls in nine "
              "groups, from AI policy and data for AI to the use of AI systems and third-party relationships."),
        ("h2", "2.4 What the certificate means"),
        ("p", "An accredited certification body (an independent auditing company) checks that your system meets "
              "the standard and that it actually runs. If it does, you get a certificate valid for three years, "
              "checked every year. Customers trust it because someone independent has looked at your evidence."),
        ("std", "Both standards use the same harmonised structure. Clauses 4 to 10 are mandatory and cannot be "
                "excluded. Annex A in each standard is a list of reference controls: you compare your risk "
                "treatment against it, and record in a Statement of Applicability which controls you use, which "
                "you do not, and why."),

        # ------------------------------------------------------------------
        ("h1", "3. Why build one integrated system?"),
        ("p", "Because about 70% of the work is the same. Both standards ask you to understand your context, "
              "appoint leaders, write a policy, assess risks, set objectives, train people, control documents, "
              "audit yourself, hold management reviews and fix nonconformities. If you build two systems you do "
              "all of that twice, and the two systems slowly drift apart. Worse, real risks do not respect the "
              "boundary: a leaked API key is a security problem **and** an AI problem."),
        ("table", ["Clause", "What ISO/IEC 27001 asks", "What ISO/IEC 42001 adds", f"What {FRAMEWORK} does once"], [
            ("4 Context", "Issues, interested parties, scope", "Your role for each AI system; intended purpose of AI",
             f"One register: {ref('IMS-REG-001')}"),
            ("5 Leadership", "Policy, roles, top-management commitment", "AI policy; AI-specific responsibilities",
             f"One policy ({'IMS-POL-001'}), one Trust Council ({'IMS-GOV-001'})"),
            ("6 Planning", "Risk assessment and treatment; SoA; objectives", "AI risk + AI system impact assessment; AI SoA",
             "One risk method and register; two SoAs side by side; one objectives plan"),
            ("7 Support", "Resources, competence, awareness, communication, documents",
             "AI resources (data, tools, compute, people)", "One training programme; one document control procedure"),
            ("8 Operation", "Run the risk treatment; control changes and suppliers",
             "Run AI impact assessments; lifecycle controls", "One development lifecycle with security and AI gates"),
            ("9 Evaluation", "Monitoring, internal audit, management review", "Same, for AI",
             "One audit programme, one management review"),
            ("10 Improvement", "Nonconformity, corrective action, continual improvement", "Same, for AI",
             "One corrective-action log"),
        ], [2.4, 4.2, 4.6, 5.3]),
        ("p", "Integration also helps you in the audit room. Many certification bodies can audit both standards "
              "in one combined visit, with one audit team, which saves days of your time and their fees."),

        # ------------------------------------------------------------------
        ("h1", f"4. The {FRAMEWORK} idea"),
        ("p", FRAMEWORK_IDEA),
        ("p", f"**{TAGLINE}**"),
        ("p", f"To make the work easy to follow, {FRAMEWORK} groups everything into five strands. Each strand "
              "is a folder in the kit. You work through them roughly in order, but strand 4 (Operate) runs all "
              "the time once it starts, and strand 5 (Prove and improve) loops back to the beginning every year."),
        ("table", ["Strand", "What it covers", "Clauses", "Key documents"], STRAND_ROWS, [2.8, 7, 2.2, 4.5]),
        ("tip", "When someone asks 'is this an ISMS thing or an AIMS thing?', the usual answer is 'both'. "
                "Default to one process with an AI-specific step inside it, rather than a separate AI process."),

        # ------------------------------------------------------------------
        ("h1", f"5. Meet {N}, the example company"),
        ("p", f"{N} ({ORG['legal_name']}) is based in {ORG['hq']}. It has {ORG['headcount']}. "
              f"{ORG['age']}. Its sector is {ORG['sector'].lower()}."),
        ("bullets", ORG["products"]),
        ("p", f"**Why it wants certification:** {ORG['why_certify']}"),
        ("p", f"{N} has five AI systems in scope. It builds some itself and buys others, which means its "
              "**role** under ISO/IEC 42001 is different for each one — a key idea we return to below."),
        ("table", ["ID", "System", "What it does (short)", "Our role"],
         [(s["id"], s["name"], s["what"].split(". ")[0] + ".", s["role"]) for s in AI_SYSTEMS], [2.4, 2.4, 7, 4.6]),
        ("p", f"The roles you will meet throughout the kit are {who('CEO')}, {who('CTO')}, {who('CISO')} (owner of "
              f"the ISMS), {who('CAIO')} (owner of the AIMS) and {who('IMSC')}, who coordinates the whole system day "
              f"to day. In a small company one person often holds more than one of these roles."),

        # ------------------------------------------------------------------
        ("h1", "6. The kit map"),
        ("p", "The kit has five working folders plus this 'Start Here' folder. Every document has a fixed ID. "
              "Documents refer to each other by ID, so keep the IDs even if you rename the titles. **POL** = "
              "policy (what we commit to), **PRO** = procedure (how we do it), **REG** = register (the records), "
              "**SOA** = Statement of Applicability, **MAN** = manual, **GOV** = governance."),
        ("table", ["ID", "Document", "Folder", "What it is for"], KIT_MAP, [2.3, 5.4, 3.3, 5.5]),
        ("p", "Records produced while you run the system use the ID formats below, so that a risk, an incident and "
              "a corrective action can always be traced to each other."),
        ("table", ["Record type", "ID format"], [(a, b) for a, b in ID_FORMATS], [8, 5]),

        # ------------------------------------------------------------------
        ("h1", "7. Your 16-week path"),
        ("p", "A small company with committed leaders can build a working, auditable system in 12 to 16 weeks. "
              "The plan below assumes one coordinator spending about half their time on it, and a few hours a "
              "week from each leader. If you are larger, or your AI systems are more complex, stretch it — but "
              "keep the order."),
        ("table", ["Weeks", "Phase", "What you do", "Documents", "You are done when"], [
            ("1", "Kick-off and gap check",
             "Name a coordinator. Get the CEO to sponsor the project. Score yourself against every clause of both "
             "standards. Agree the target certification date.",
             "IMS-WBK-001", "Gap assessment complete; roadmap agreed by the CEO"),
            ("2", "Context and scope",
             "List internal and external issues, interested parties and legal obligations. Draw the scope "
             "boundary. Decide your AI role for each AI system.",
             "IMS-REG-001", "Scope statement drafted and agreed"),
            ("3", "Leadership",
             "Set up the Trust Council. Agree roles and the RACI chart. Approve the top-level policy. Draft "
             "the manual.",
             "IMS-GOV-001, IMS-POL-001, IMS-MAN-001", "Policy signed; first Trust Council meeting minuted"),
            ("4", "Inventory",
             "List information assets and AI systems with owners and classification.",
             "IMS-REG-005", "Every asset and AI system has an owner"),
            ("5–6", "Risk assessment",
             "Agree the risk method and scales. Run risk workshops with each team. Fill the risk register.",
             "IMS-PRO-001, IMS-REG-002", "Risks scored; treatment options chosen"),
            ("6–7", "AI impact assessment",
             "Assess the impact of each AI system on artists, customers, depicted people and society. Start "
             "with the highest-criticality system.",
             "IMS-PRO-002", "Impact assessment approved for each in-scope AI system"),
            ("7–8", "Controls and objectives",
             "Compare your treatments with both Annex A lists. Fill both SoAs. Set measurable objectives. "
             "The Trust Council approves the treatment plan and accepts residual risks.",
             "IMS-SOA-001, IMS-SOA-002, IMS-REG-003", "Both SoAs approved; objectives have owners and targets"),
            ("8–9", "Equip",
             "Run awareness training (security + responsible AI). Fill the competence matrix. Put document "
             "control in place.",
             "IMS-PRO-003, IMS-REG-004, IMS-PRO-004", "Training records for all staff and contractors"),
            ("9–12", "Operate",
             "Publish the topic policies. Run the processes for real: an AI Release Review, a supplier review, an "
             "access review, an incident tabletop exercise, a backup restore test. Log events.",
             "IMS-POL-002 to IMS-POL-006, IMS-PRO-005, IMS-PRO-006, IMS-REG-006",
             "At least one record of each key process"),
            ("12–13", "Internal audit",
             "Audit the whole system against both standards with someone who did not build it.",
             "IMS-PRO-007, IMS-REG-007", "Audit report issued"),
            ("14", "Fix",
             "Record nonconformities, find root causes and start corrective actions.",
             "IMS-PRO-009, IMS-REG-008", "Every finding has an owner and a due date"),
            ("15", "Management review",
             "Top management reviews performance, audit results, risks and objectives, and makes decisions.",
             "IMS-PRO-008", "Minutes with decisions and actions"),
            ("16", "Ready for Stage 1",
             "Check the gap assessment again. Choose an accredited certification body and book Stage 1.",
             "IMS-WBK-001", "Stage 1 date booked"),
        ], [1.4, 2.5, 6, 3.4, 3.4]),
        ("example", f"How {N} used the path", [
            f"{person('IMSC')} ran the project from week 1, with {person('CISO')} leading the security work and "
            f"{person('CAIO')} leading the AI work. The Trust Council met every month and the CEO opened each "
            "meeting by asking 'what is blocking you?'.",
            f"In weeks 5–6 the risk workshops produced ten key risks, for example {KEY_RISKS[0][0]} "
            f"('{KEY_RISKS[0][1]}') and {KEY_RISKS[6][0]} ('{KEY_RISKS[6][1]}').",
            f"The independent internal audit {SAMPLE_AUDIT['id']} ran {SAMPLE_AUDIT['dates']} and found two minor "
            f"nonconformities and one opportunity for improvement — a normal, healthy result for a first audit.",
        ]),
        ("tip", "Most certification bodies want to see the system **running**, not just written: usually a few "
                "months of records, at least one full internal audit and one management review before Stage 2. "
                "Start creating evidence (meeting minutes, training records, review tickets) from week 3."),

        # ------------------------------------------------------------------
        ("h1", "8. How to adapt the kit to your organisation"),
        ("p", f"Do not edit 30 documents one by one. Start with your **facts**. The kit was generated from a "
              f"single fact sheet about {N}; if you collect your own facts first, every document becomes a "
              "find-and-replace exercise plus some thinking."),
        ("steps", [
            "**Write your fact sheet.** Company name and legal entity, locations, headcount, products, customers, "
            "why you want certification. Keep it to one page.",
            "**List your people and roles.** Who is top management? Who owns security? Who owns AI? Who "
            "coordinates? In a small company one person often holds two roles — write that down.",
            "**List your AI systems.** For each: what it does, whether you build, fine-tune, integrate or just use "
            "it, who uses it, who could be harmed and how critical it is. Your AI role follows from this.",
            "**Agree your risk scales.** Adjust the money amounts in the impact scale to your size. A USD 100k "
            "loss is 'moderate' for a 34-person startup; it may be 'minor' for a bank.",
            "**List your laws and contracts.** Data protection, AI, copyright, consumer and sector laws in every "
            "market where you operate, plus the security and AI terms in your customer contracts.",
            "**Replace names, systems and numbers** throughout the documents. Search for the example "
            f"company name, the example people and the system names ({', '.join(SYS.values())}).",
            "**Cut what you do not need, add what you do.** A company with no marketplace does not need artist "
            "fairness controls; a company that trains large models needs more on data provenance and compute.",
            "**Read every document aloud with its owner.** If the owner says 'we don't actually do that', change "
            "the document or change the practice — never leave it untrue.",
        ]),
        ("table", ["Fact to collect", f"{N}'s answer (example)", "Your answer"], [
            ("Organisation name", N, "[[your organisation]]"),
            ("Headquarters", ORG["hq"], "[[city, country]]"),
            ("Size", ORG["headcount"], "[[employees and contractors]]"),
            ("Top management", f"{person('CEO')}, {title_of('CEO')}", "[[name, title]]"),
            ("ISMS owner", f"{person('CISO')}, {title_of('CISO')}", "[[name, title]]"),
            ("AIMS owner", f"{person('CAIO')}, {title_of('CAIO')}", "[[name, title]]"),
            ("AI systems in scope", ", ".join(SYS.values()), "[[list]]"),
            ("Risk acceptance rule", f"{LEVELS[2][0]}: {LEVELS[2][3]}", "[[your rule]]"),
        ], [4, 7, 5.5]),
        ("tip", "If you are comfortable with a little Python, the kit's build folder lets you change the fact "
                "sheet once and regenerate every document. If not, a careful find-and-replace in your word "
                "processor works too."),

        # ------------------------------------------------------------------
        ("h1", "9. What a certification audit looks like"),
        ("p", "Certification is done by an **accredited certification body** — check that its accreditation "
              "covers ISO/IEC 27001 and ISO/IEC 42001 (accreditation for ISO/IEC 42001 is newer, so ask). Ask "
              "for a combined or integrated audit of both standards. The cycle has four parts."),
        ("table", ["Step", "When", "What happens", "What you need ready"], [
            ("Stage 1", "Usually 4–8 weeks before Stage 2; often remote, 1–2 days",
             "The auditor reads your documents and checks you are ready: scope, policy, risk method, SoAs, "
             "impact assessments, internal audit and management review done.",
             "The core documents, an audit report, management review minutes, both SoAs."),
            ("Stage 2", "The main audit; several days for a company of this size",
             "The auditor interviews people, samples records and checks that controls work in practice. "
             "Findings are graded as major nonconformity, minor nonconformity or opportunity for improvement.",
             "People available; evidence easy to find; a guide to walk the auditor through."),
            ("Certificate", "After any major findings are closed",
             "Minor findings need an accepted corrective-action plan; majors must be fixed and verified before "
             "the certificate is issued. The certificate is valid for three years.",
             "Corrective-action plans with root causes and dates."),
            ("Surveillance and recertification", "Years 1 and 2; full re-audit in year 3",
             "Shorter audits that sample part of the system and check that previous findings are closed and "
             "that internal audits, management reviews and improvements continue.",
             "A system that kept running between audits."),
        ], [2.6, 3.4, 6, 4.5]),
        ("p", "A **major nonconformity** means a requirement is not met at all, or there is a breakdown that "
              "puts the system's purpose at risk (for example, no management review has ever been held). A "
              "**minor nonconformity** is a single lapse (for example, two contractors missed training). An "
              "**opportunity for improvement** is advice — you decide what to do with it."),
        ("tip", "Auditors love traceability. Pick one risk and be ready to show its whole journey: risk register "
                "entry, treatment, SoA control, evidence the control works, objective it supports, and where it "
                "was discussed in management review."),

        # ------------------------------------------------------------------
        ("h1", "10. Common beginner mistakes"),
        ("bullets", [
            "**Writing documents nobody follows.** The auditor will ask staff, not read your prose. A short "
            "true policy beats a long aspirational one.",
            "**Copying a template without changing it.** Auditors spot foreign company names, systems you do "
            "not have and processes nobody recognises.",
            "**Making the scope too big or too small.** Too big and you cannot finish; too small and customers "
            "find the certificate does not cover the service they buy.",
            "**Treating AI as an IT risk only.** ISO/IEC 42001 cares about harm to people outside your company — "
            "artists, users, people depicted in images. That is what the impact assessment is for.",
            "**Forgetting the AI you buy.** Vendor AI services and AI coding assistants are in scope as AI "
            "systems you use, with supplier controls.",
            "**Two of everything.** Two risk registers, two audit programmes, two review meetings. Run one.",
            "**Leaving top management out.** Both standards expect leaders to be visibly involved. Minutes "
            "with the CEO's decisions are evidence.",
            "**No records.** If it is not recorded, for an auditor it did not happen. Keep tickets, minutes and "
            "logs from the start.",
            "**Auditing your own work.** The internal auditor must be independent of what they audit — use a "
            "contractor or a colleague from another team.",
            "**Starting with tools.** A compliance platform helps later. First decide how you work; then choose "
            "a tool that fits.",
            "**Stopping after the certificate.** Surveillance audits check that the system kept running.",
        ]),

        # ------------------------------------------------------------------
        ("h1", "11. Short glossary"),
        ("table", ["Term", "Plain meaning"], [
            ("ISMS", "Information security management system — the policies, processes, people and controls that "
                     "protect information (ISO/IEC 27001)."),
            ("AIMS", "AI management system — the same idea for developing, providing and using AI responsibly "
                     "(ISO/IEC 42001)."),
            ("Integrated management system (IMS)", "One management system that meets more than one standard."),
            ("Scope", "The parts of the organisation, locations, services and systems the management system covers."),
            ("Interested party", "Anyone who can affect, or is affected by, what you do: customers, artists, "
                                 "staff, regulators, investors, suppliers."),
            ("Risk owner", "The person accountable for a risk and allowed to decide how it is treated or accepted."),
            ("Risk treatment", "What you do about a risk: modify it (add controls), avoid it, share it (for example "
                               "insurance or contract) or accept it."),
            ("Residual risk", "The risk that remains after treatment."),
            ("Annex A", "The list of reference controls at the back of each standard."),
            ("SoA (Statement of Applicability)", "A list of every Annex A control saying whether you apply it, "
                                                 "why or why not, and whether it is implemented."),
            ("AI system", "A system that generates outputs such as content, predictions, recommendations or "
                          "decisions from the inputs it receives, using machine learning or other AI techniques."),
            ("AI provider", "An organisation that makes an AI system or service available to others."),
            ("AI producer", "An organisation that designs, develops, trains or fine-tunes an AI system."),
            ("AI customer / user", "An organisation that uses an AI system someone else provides."),
            ("AI system impact assessment", "A structured look at how an AI system could affect individuals, "
                                            "groups and society, done before release and when it changes."),
            ("Nonconformity", "Not meeting a requirement — of the standard, the law, a contract or your own "
                              "documents."),
            ("Corrective action", "Action to remove the cause of a nonconformity so that it does not happen again."),
            ("Internal audit", "Your own independent check that the system meets the standards and works."),
            ("Management review", "A planned meeting where top management reviews the system and makes decisions."),
            ("Documented information", "The standards' term for documents (what you plan to do) and records "
                                       "(evidence of what you did)."),
            ("Stage 1 / Stage 2", "The two parts of the initial certification audit: readiness review, then the "
                                  "full audit of implementation."),
        ], [4.5, 12]),

        # ------------------------------------------------------------------
        ("h1", "12. Where to go next"),
        ("steps", [
            f"Open {ref('IMS-WBK-001')} and complete the gap assessment.",
            f"Read {ref('IMS-MAN-001')} to see the whole system on a few pages.",
            f"Fill in {ref('IMS-REG-001')} — everything else depends on your context and scope.",
            f"Set up your governance with {ref('IMS-GOV-001')} and sign {ref('IMS-POL-001')}.",
        ]),
        ("p", f"For the reasoning behind each clause and more examples, see the companion books by {PUBLISHER}."),
    ],
}
