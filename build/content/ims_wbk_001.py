from org import DOCS, ORG, ROLES, KIT_VERSION, NEXT_REVIEW, EFFECTIVE_DATE, person

N = ORG["name"]
B, S27, S42 = "Both", "27001 only", "42001 only"

# clause, standard, question (own words), kit document, example status, example note
GAP = [
    ("4.1", B, "Have you written down the internal and external issues that affect your ability to protect information and use AI responsibly?", "IMS-REG-001", "Done", "Issues sheet reviewed Oct 2026"),
    ("4.1", S42, "Have you decided your role for each AI system (provider, producer, user/customer, partner)?", "IMS-REG-001", "Done", "AI Roles sheet"),
    ("4.1", B, "Have you considered whether climate change is a relevant issue?", "IMS-REG-001", "Done", "Low relevance; GPU energy tracked"),
    ("4.2", B, "Do you know your interested parties and which of their requirements you will meet (incl. legal and contractual)?", "IMS-REG-001", "Done", ""),
    ("4.3", B, "Is there a written scope with boundaries, interfaces and dependencies — and are any exclusions justified?", "IMS-REG-001", "Done", "One scope for both standards"),
    ("4.4", B, "Is the management system defined as a set of processes that interact (who, what, inputs, outputs)?", "IMS-MAN-001", "Done", ""),
    ("5.1", B, "Can top management show how they lead the system (resources, reviews, communication)?", "IMS-GOV-001", "Done", "Trust Council minutes"),
    ("5.2", B, "Is there an approved policy covering information security and AI, with the required commitments?", "IMS-POL-001", "Done", ""),
    ("5.3", B, "Are roles, responsibilities and authorities assigned and communicated (incl. who reports on performance)?", "IMS-GOV-001", "Done", ""),
    ("6.1.1", B, "Have you planned how to address risks and opportunities to the management system itself?", "IMS-PRO-001", "Done", ""),
    ("6.1.2", B, "Is there a documented, repeatable risk-assessment method with acceptance criteria — covering both security and AI risks?", "IMS-PRO-001", "Done", ""),
    ("6.1.3", B, "Is there a risk treatment plan, approved by risk owners, with residual risks accepted?", "IMS-REG-002", "Partial", "RSK-AI-005 accepted with expiry"),
    ("6.1.3", S27, "Is the ISO/IEC 27001 Statement of Applicability complete for all 93 Annex A controls?", "IMS-SOA-001", "Done", ""),
    ("6.1.3", S42, "Is the ISO/IEC 42001 Statement of Applicability complete for all 38 Annex A controls?", "IMS-SOA-002", "Done", ""),
    ("6.1.4", S42, "Is there a process for AI system impact assessments on individuals, groups and society?", "IMS-PRO-002", "Done", ""),
    ("6.2", B, "Are measurable objectives set, with plans saying what, who, resources, when and how results are evaluated?", "IMS-REG-003", "Done", "OBJ-01 to OBJ-07"),
    ("6.3", B, "Are changes to the management system planned in a controlled way?", "IMS-MAN-001", "Done", ""),
    ("7.1", B, "Have you provided the resources (people, budget, tools) the system needs?", "IMS-MAN-001", "Done", ""),
    ("7.2", B, "Is competence defined per role and evidenced (incl. AI skills)?", "IMS-REG-004", "Partial", "Contractor gap NC-2026-004"),
    ("7.3", B, "Is everyone aware of the policy, their contribution and what happens if they don't comply?", "IMS-PRO-003", "Partial", "AI-literacy module rolling out"),
    ("7.4", B, "Is internal and external communication planned (what, when, with whom, how)?", "IMS-REG-004", "Done", ""),
    ("7.5", B, "Is documented information created, approved, controlled and retained properly?", "IMS-PRO-004", "Done", ""),
    ("8.1", B, "Are operational processes planned and controlled, including outsourced processes?", "IMS-POL-002", "Done", ""),
    ("8.1", S42, "Do AI lifecycle processes follow responsible-development criteria with gates?", "IMS-POL-002", "Done", "AI Release Review"),
    ("8.2", B, "Are risk assessments repeated at planned intervals and after significant change?", "IMS-PRO-001", "Done", ""),
    ("8.3", B, "Is the risk treatment plan being implemented, with evidence?", "IMS-REG-002", "Partial", "3 actions open"),
    ("8.4", S42, "Are AI system impact assessments performed and their results kept?", "IMS-PRO-002", "Done", "AIIA-2026-01, -02"),
    ("9.1", B, "Do you know what is monitored and measured, how, when, and who analyses the results?", "IMS-REG-003", "Done", ""),
    ("9.2", B, "Is there an internal audit programme and have audits been done by objective auditors?", "IMS-PRO-007", "Done", "AUD-2026-02"),
    ("9.3", B, "Has top management reviewed the system with all required inputs and recorded decisions?", "IMS-PRO-008", "Done", "Review 2026-10-21"),
    ("10.1", B, "Can you show continual improvement (improvement register, trend of metrics)?", "IMS-REG-008", "Done", ""),
    ("10.2", B, "Are nonconformities corrected, root causes found and corrective actions checked for effectiveness?", "IMS-PRO-009", "Partial", "CA-2026-004 open"),
    ("A (27001)", S27, "Are the controls you declared 'Implemented' actually working, with evidence an auditor can sample?", "IMS-SOA-001", "Partial", "5 partially implemented"),
    ("A (42001)", S42, "Are AI controls (data provenance, V&V, monitoring, user information, suppliers) evidenced per system?", "IMS-SOA-002", "Partial", "A.6.2.6 fairness alerting planned"),
]

GAP_SCORE = '=IF(E{r}="Done",2,IF(E{r}="Partial",1,IF(E{r}="","",0)))'

# week, strand, task, owner key, output
ROADMAP = [
    ("1", "Start", "Get leadership commitment: agree why (contracts, trust), budget, and target certification date", "CEO", "Trust Council kick-off note"),
    ("1", "Start", "Appoint the Compliance Coordinator, ISMS owner and AIMS owner; set up a shared folder or wiki", "CEO", "IMS-GOV-001 draft"),
    ("1–2", "Start", "Run the gap assessment in this workbook; agree priorities", "IMSC", "Gap Assessment sheet"),
    ("2–3", "1 Ground", "Write context, interested parties, legal register and one scope for both standards", "IMSC", "IMS-REG-001"),
    ("3", "1 Ground", "Agree governance: Trust Council, AI Release Review, RACI", "CEO", "IMS-GOV-001"),
    ("3–4", "1 Ground", "Write and approve the top-level policy", "CEO", "IMS-POL-001"),
    ("4", "4 Operate", "Build the asset and AI system inventory; name an owner for every AI system", "CISO", "IMS-REG-005"),
    ("4–5", "2 Gauge", "Agree the risk method and scales; train risk owners for one hour", "CISO", "IMS-PRO-001"),
    ("5–6", "2 Gauge", "Run risk workshops (security, then AI) and fill in the risk register", "CISO", "IMS-REG-002"),
    ("6–7", "2 Gauge", "Do impact assessments for High-criticality AI systems", "CAIO", "IMS-PRO-002"),
    ("7–8", "2 Gauge", "Choose controls; complete both Statements of Applicability; approve treatment plan", "CISO", "IMS-SOA-001, IMS-SOA-002"),
    ("8", "2 Gauge", "Set objectives and metrics", "IMSC", "IMS-REG-003"),
    ("6–10", "4 Operate", "Write or adapt the topic policies and procedures; close the biggest control gaps first", "CTO", "IMS-POL-002 to 006, IMS-PRO-005, 006"),
    ("8–10", "3 Equip", "Competence matrix, awareness and AI-literacy training for everyone", "HOP", "IMS-REG-004"),
    ("8–9", "3 Equip", "Set up document control and the document register", "IMSC", "IMS-PRO-004"),
    ("10–12", "4 Operate", "Operate the system: run the processes and keep records (minimum 6–8 weeks of evidence before audit)", "IMSC", "Records in all registers"),
    ("12–13", "5 Prove and improve", "Full internal audit of both standards", "IMSC", "IMS-PRO-007, IMS-REG-007"),
    ("13", "5 Prove and improve", "Management review with all required inputs", "CEO", "IMS-PRO-008"),
    ("13–14", "5 Prove and improve", "Corrective actions for audit findings", "IMSC", "IMS-REG-008"),
    ("14", "Certify", "Choose an accredited certification body that can audit both standards together; book stage 1", "CEO", "Contract"),
    ("15–16", "Certify", "Stage 1 audit (documents and readiness); fix any stage 1 concerns", "IMSC", "Stage 1 report"),
    ("18–20", "Certify", "Stage 2 audit (implementation and effectiveness)", "IMSC", "Certificates"),
]

# clause, title (short), 27001, 42001, what is different for AI
CROSSWALK = [
    ("4.1", "Organisation and its context", "Yes", "Yes", "42001 also asks you to decide your AI role(s) and the intended purpose of your AI systems."),
    ("4.2", "Interested parties", "Yes", "Yes", "Add people affected by AI outputs (e.g. depicted people, artists) even if they are not customers."),
    ("4.3", "Scope", "Yes", "Yes", "Write one scope; list the AI systems in scope by name."),
    ("4.4", "Management system", "Yes", "Yes", "Same."),
    ("5.1", "Leadership and commitment", "Yes", "Yes", "Same; leaders also commit to responsible AI."),
    ("5.2", "Policy", "Yes", "Yes", "AI policy must fit the purpose of AI use and give a framework for AI objectives — one combined policy works."),
    ("5.3", "Roles, responsibilities, authorities", "Yes", "Yes", "Same."),
    ("6.1.1", "Actions to address risks and opportunities", "Yes", "Yes", "42001 asks you to separate tasks for AI risk assessment, treatment and impact assessment."),
    ("6.1.2", "Risk assessment", "Yes (information security risk)", "Yes (AI risk)", "AI risks include consequences for individuals, groups and society, not only the organisation."),
    ("6.1.3", "Risk treatment and SoA", "Yes — Annex A 93 controls", "Yes — Annex A 38 controls", "Two SoAs; one treatment plan."),
    ("6.1.4", "AI system impact assessment", "—", "Yes", "New for AI: assess impacts on people and society; results feed risk assessment."),
    ("6.2", "Objectives and planning", "Yes", "Yes", "Same structure; add AI objectives (e.g. fairness, transparency)."),
    ("6.3", "Planning of changes", "Yes", "Yes", "Same."),
    ("7.1", "Resources", "Yes", "Yes", "Same."),
    ("7.2", "Competence", "Yes", "Yes", "Add AI-specific competences."),
    ("7.3", "Awareness", "Yes", "Yes", "Awareness of the AI policy as well."),
    ("7.4", "Communication", "Yes", "Yes", "Same."),
    ("7.5", "Documented information", "Yes", "Yes", "Same; AI documentation (model cards, data provenance) is added."),
    ("8.1", "Operational planning and control", "Yes", "Yes", "Same; AI lifecycle processes included."),
    ("8.2", "Risk assessment (operation)", "Yes", "Yes", "Same."),
    ("8.3", "Risk treatment (operation)", "Yes", "Yes", "Same."),
    ("8.4", "AI system impact assessment (operation)", "—", "Yes", "Perform impact assessments at planned intervals and on change."),
    ("9.1", "Monitoring, measurement, analysis, evaluation", "Yes", "Yes", "Add AI system performance metrics."),
    ("9.2", "Internal audit", "Yes", "Yes", "One programme, auditors competent in both."),
    ("9.3", "Management review", "Yes", "Yes", "One review; include AI-specific inputs."),
    ("10.1", "Continual improvement", "Yes", "Yes", "Same."),
    ("10.2", "Nonconformity and corrective action", "Yes", "Yes", "Same."),
]

DOC_REG = [(d[0], d[1], d[3], d[4], f"{person(d[2])}", KIT_VERSION, "Approved", EFFECTIVE_DATE, NEXT_REVIEW,
            f"=IF(I{{r}}=\"\",\"\",IF(DATEVALUE(I{{r}})<TODAY(),\"Overdue\",\"On track\"))") for d in DOCS]

WB = {
    "id": "IMS-WBK-001",
    "summary": f"The first file to open. Check where you stand against both standards, plan your route to "
               f"certification, see how ISO/IEC 27001 and ISO/IEC 42001 line up clause by clause, and keep the list "
               f"of every controlled document. Filled in for the sample company {N}.",
    "clauses": {"27001": "Clauses 4–10 (gap assessment); 7.5 (document register)",
                "42001": "Clauses 4–10 (gap assessment); 7.5 (document register)"},
    "howto": [
        "Start with 'Gap Assessment': clear the Status column and answer each question honestly for your organisation.",
        "Then adapt 'Roadmap' — the 16–20 week plan suits a startup of 20–100 people with one part-time coordinator.",
        "'Crosswalk' shows why one system can serve both standards: only 6.1.4 and 8.4 are AI-only clauses.",
    ],
    "sheets": [
        {
            "name": "Gap Assessment",
            "title": "Readiness and gap assessment — both standards",
            "intro": "Status: Done (2 points) · Partial (1) · Not started (0). The score and summary update automatically. "
                     "'Kit document' tells you which template helps close the gap.",
            "headers": ["Clause", "Applies to", "Question", "Kit document", "Status", "Score", "Notes / evidence", "Action owner"],
            "rows": [(c, s, q, d, st, GAP_SCORE, n, "") for c, s, q, d, st, n in GAP],
            "formulas": {"Score": GAP_SCORE},
            "widths": [10, 12, 80, 22, 13, 8, 34, 16],
            "lists": {"Status": ["Done", "Partial", "Not started"], "Applies to": [B, S27, S42]},
            "status": ["Status"],
            "freeze_cols": 1,
            "blank_rows": 10,
        },
        {
            "name": "Gap Summary",
            "title": "Readiness by clause group",
            "intro": "Percentage of maximum score per clause group.",
            "headers": ["Clause group", "Questions", "Score", "Max", "Readiness"],
            "rows": [
                (g, f"=COUNTIFS('Gap Assessment'!A:A,\"{p}*\",'Gap Assessment'!E:E,\"<>\")",
                 f"=SUMIF('Gap Assessment'!A:A,\"{p}*\",'Gap Assessment'!F:F)", "=B{r}*2",
                 "=IF(D{r}=0,\"\",ROUND(C{r}/D{r}*100,0)&\"%\")")
                for g, p in (("4 Context", "4"), ("5 Leadership", "5"), ("6 Planning", "6"), ("7 Support", "7"),
                             ("8 Operation", "8"), ("9 Performance evaluation", "9"), ("10 Improvement", "10"),
                             ("Annex A controls", "A"))
            ] + [("Overall", "=SUM(B5:B12)", "=SUM(C5:C12)", "=SUM(D5:D12)", "=IF(D13=0,\"\",ROUND(C13/D13*100,0)&\"%\")")],
            "widths": [28, 11, 9, 9, 12],
            "blank_rows": 0,
        },
        {
            "name": "Roadmap",
            "title": "Implementation roadmap — startup route to two certificates",
            "intro": "Weeks are counted from kick-off. Strands follow the TWYNTRUST framework: 1 Ground, 2 Gauge, 3 Equip, "
                     "4 Operate, 5 Prove and improve.",
            "headers": ["Week", "Strand", "Task", "Owner", "Output", "Status", "Done date"],
            "rows": [(w, s, t, person(o), out, "Done" if i < 16 else ("In progress" if i < 19 else "Planned"), "")
                     for i, (w, s, t, o, out) in enumerate(ROADMAP)],
            "widths": [8, 18, 80, 18, 32, 13, 12],
            "lists": {"Status": ["Not started", "In progress", "Done", "Planned"]},
            "status": ["Status"],
            "blank_rows": 10,
        },
        {
            "name": "Crosswalk",
            "title": "Clause crosswalk — ISO/IEC 27001:2022 and ISO/IEC 42001:2023",
            "intro": "Both standards use the same harmonised structure, so one process can meet the same clause in both. "
                     "Clause titles are short descriptions, not ISO text.",
            "headers": ["Clause", "Topic", "ISO/IEC 27001", "ISO/IEC 42001", "What changes when AI is added"],
            "rows": CROSSWALK,
            "widths": [9, 38, 24, 24, 80],
            "blank_rows": 0,
        },
        {
            "name": "Document Register",
            "title": "Master list of controlled documents",
            "intro": "Every controlled document and register in the system. Review status turns 'Overdue' after the next-review date.",
            "headers": ["ID", "Title", "Folder", "Type", "Owner", "Version", "Status", "Effective", "Next review", "Review status"],
            "rows": DOC_REG,
            "formulas": {"Review status": "=IF(I{r}=\"\",\"\",IF(DATEVALUE(I{r})<TODAY(),\"Overdue\",\"On track\"))"},
            "widths": [13, 66, 32, 7, 18, 8, 10, 12, 12, 13],
            "lists": {"Status": ["Draft", "In review", "Approved", "Obsolete"]},
            "status": ["Review status"],
            "freeze_cols": 1,
            "blank_rows": 15,
        },
    ],
}
