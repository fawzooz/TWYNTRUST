from org import (AI_SYSTEMS, COMMITTEES, FRAMEWORK, KEY_RISKS, LEVELS, OBJECTIVES, ORG, STRANDS, TECH,
                 person, ref, title_of, who)

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
R5 = next(r for r in KEY_RISKS if r[0] == "RSK-AI-005")


def clause_table(rows):
    return ("table", ["Topic", "ISO/IEC 27001", "ISO/IEC 42001", f"How {N} meets both", "Where to find it"],
            rows, [2.6, 1.6, 1.6, 7.2, 3.5])


DOC = {
    "id": "IMS-MAN-001",
    "summary": f"The map of {N}'s integrated management system. It walks through Clauses 4 to 10 once and shows, "
               "for each clause, how a single process meets both ISO/IEC 27001 and ISO/IEC 42001, and where the "
               "evidence lives.",
    "clauses": {"27001": "4.1–4.4, 5.1–5.3, 6.1–6.3, 7.1–7.5, 8.1–8.3, 9.1–9.3, 10.1–10.2; Annex A via IMS-SOA-001",
                "42001": "4.1–4.4, 5.1–5.3, 6.1–6.3, 7.1–7.5, 8.1–8.4, 9.1–9.3, 10.1–10.2; Annex A via IMS-SOA-002"},
    "howto": [
        "The manual is not a mandatory document in either standard, but it is the fastest way to show an auditor "
        "how the system hangs together. Keep it as a map: point to other documents rather than repeating them.",
        "Section 2 (scope statement) and section 3 (AI roles) must match the register IMS-REG-001 exactly. "
        "Change them together.",
        "Rewrite the 'How we meet both' column in your own words. An auditor will test whether it is true.",
    ],
    "body": [
        # ------------------------------------------------------------------
        ("h1", "1. Purpose and how to read this manual"),
        ("p", f"This manual describes the integrated management system (IMS) of {N}. The IMS is our information "
              "security management system (ISMS) under ISO/IEC 27001:2022 and our AI management system (AIMS) under "
              f"ISO/IEC 42001:2023, run as one system under the {FRAMEWORK} framework. We have one context, one "
              "leadership team, one risk process, one internal audit and one management review. Each standard's "
              "Annex A controls are attached where they belong."),
        ("p", "For every clause the manual gives a short explanation, a table showing how we meet both standards "
              "and the documents that hold the detail and the evidence. It is written for three readers: new staff "
              "who want the big picture, leaders who are accountable for the system, and auditors."),
        ("std", "Both standards share the same ten-clause structure. Clauses 4 to 10 contain the requirements and "
                "none of them can be excluded. Each standard also has an Annex A of reference controls; an "
                "organisation decides which controls it needs through risk treatment and justifies the decision in a "
                "Statement of Applicability."),

        # ------------------------------------------------------------------
        ("h1", f"2. About {N} and the scope of the IMS"),
        ("p", f"{N} ({ORG['legal_name']}) is a {ORG['sector'].lower()} company headquartered in {ORG['hq']}, with "
              f"{ORG['headcount']}. {ORG['age']}. Our mission: {ORG['mission']}"),
        ("bullets", ORG["products"]),
        ("p", "Where we work:"),
        ("bullets", ORG["sites"]),
        ("h2", "2.1 Scope statement"),
        ("example", "Scope statement (as it will appear on both certificates)", [
            f"The integrated information security and AI management system of {ORG['legal_name']} covering the "
            "design, development, operation and support of the Quillfen Canvas web application, the Quillfen "
            "Commons artist marketplace and the Quillfen API, including the AI systems "
            f"{', '.join(SYS.values())}, in the roles of AI provider, AI producer and AI user as defined per system, "
            "delivered from the Dubai head office and by remote staff, on cloud infrastructure, in accordance with "
            f"the Statements of Applicability {'IMS-SOA-001'} and {'IMS-SOA-002'} (current versions).",
        ]),
        ("p", f"**Boundaries.** In scope: all staff and contractors, company laptops, our AWS accounts, GitHub, "
              "the identity provider and the SaaS tools that hold in-scope information. Out of scope: the "
              "physical security of supplier data centres and the internal operation of our suppliers' AI models, "
              "which we manage as supplier relationships rather than run ourselves. The full in/out list, with "
              f"justifications, interfaces and dependencies, is in {ref('IMS-REG-001')} (sheet 'Scope & Boundaries')."),
        ("p", f"**Technology at a glance.** Cloud: {TECH['cloud']}. Identity: {TECH['identity']}. Devices: "
              f"{TECH['devices']}. Development: {TECH['sdlc']}. Payments: {TECH['payments']}."),

        # ------------------------------------------------------------------
        ("h1", "3. Our role for each AI system"),
        ("p", "ISO/IEC 42001 asks us to know our role for each AI system, because the role decides which "
              "requirements and controls matter most. We use the role terms of ISO/IEC 22989: an **AI provider** "
              "makes an AI system available to others; an **AI producer** designs, develops or trains it; an "
              "**AI customer / user** uses a system someone else provides. One organisation can hold several roles "
              "for the same system."),
        ("table", ["ID", "System", "Our role", "Who uses it / who is affected", "Criticality"],
         [(s["id"], s["name"], s["role"], s["users"], s["criticality"]) for s in AI_SYSTEMS],
         [2.2, 2.2, 4.4, 3.8, 4]),
        ("tip", "If you only use an AI system (like a vendor moderation service), you still have AIMS duties: you "
                "must assess its impact in your context, control the supplier and monitor it. Being a 'user' "
                "does not take a system out of scope."),

        # ------------------------------------------------------------------
        ("h1", "4. Structure of the integrated management system"),
        ("p", f"The IMS is organised in five strands. Each strand is a folder of documents and a set of "
              "recurring activities. The table is our structure diagram: read it top to bottom as the "
              "plan–do–check–act cycle."),
        ("table", ["Strand", "PDCA", "Clauses", "What happens", "Documents"],
         [(f"{n}. {name}", pdca, cl, what, ", ".join(docs)) for (n, name, what, cl, docs), pdca in
          zip(STRANDS, ["Plan", "Plan", "Do", "Do", "Check / Act"])],
         [2.4, 1.6, 2.2, 6, 4.3]),
        ("p", "Governance sits across all strands:"),
        ("table", ["Body", "Charter (summary)"], [(k, v) for k, v in COMMITTEES.items()], [3.5, 13]),
        ("p", f"Full charters, role descriptions and the RACI chart are in {ref('IMS-GOV-001')}."),

        # ------------------------------------------------------------------
        ("h1", "5. Clause 4 — Context of the organisation"),
        ("p", "We start by understanding what affects our ability to protect information and to use AI "
              "responsibly. The same analysis feeds both standards; AI-specific points are tagged in the register."),
        clause_table([
            ("Internal and external issues", "4.1", "4.1",
             "Twice a year the Compliance Coordinator updates the issues list with the Trust Council, using "
             "PESTLE prompts. AI-specific issues (model supply, copyright debate, EU AI Act timelines) sit in the "
             "same list. We also record whether climate change is a relevant issue.",
             "IMS-REG-001 'Internal & External Issues', 'Climate-change consideration'"),
            ("Our AI roles and intended purpose", "—", "4.1",
             "Role and intended purpose recorded for each AI system and reviewed at every AI Release Review.",
             "IMS-REG-001 'AI Roles per system'; section 3 above"),
            ("Interested parties and their requirements", "4.2", "4.2",
             "One list of interested parties (customers, artists, staff, regulators, investors, suppliers, "
             "people depicted in images). We decide which requirements we will address; the binding ones go to "
             "the legal register.",
             "IMS-REG-001 'Interested Parties', 'Legal & Regulatory'"),
            ("Scope", "4.3", "4.3",
             "One scope covering both standards, with the same boundaries (section 2).",
             "IMS-REG-001 'Scope & Boundaries'; this manual"),
            ("The management system itself", "4.4", "4.4",
             "This manual and the document register describe the processes and how they interact.",
             "IMS-MAN-001; IMS-WBK-001 document register"),
        ]),
        ("p", "ISO/IEC 27001:2022/Amd 1:2024 added climate-change consideration to clauses 4.1 and 4.2. We apply "
              "the same consideration to the AIMS as good practice (and AI compute energy use is relevant to "
              "ISO/IEC 42001 Annex C 'environmental impact')."),

        # ------------------------------------------------------------------
        ("h1", "6. Clause 5 — Leadership"),
        ("p", f"Top management at {N} is the CEO together with the Trust Council. Leadership is shown in "
              "practice: the CEO chairs the Trust Council, approves the policy, signs off risk acceptance above "
              "Medium and opens each management review."),
        clause_table([
            ("Leadership and commitment", "5.1", "5.1",
             "The Trust Council meets monthly; budget and people for the IMS are agreed in the annual plan; "
             "IMS requirements are built into product and engineering processes rather than added on top.",
             "Trust Council minutes; IMS-GOV-001"),
            ("Policy", "5.2", "5.2",
             "One Information Security and Responsible AI Policy, signed by the CEO, published on the intranet "
             "and shared with artists and customers on request.",
             "IMS-POL-001"),
            ("Roles, responsibilities and authorities", "5.3", "5.3",
             f"The ISMS is owned by {who('CISO')}; the AIMS by {who('CAIO')}; both report on performance to the "
             f"Trust Council. {who('IMSC')} coordinates the IMS day to day.",
             "IMS-GOV-001"),
        ]),

        # ------------------------------------------------------------------
        ("h1", "7. Clause 6 — Planning"),
        ("h2", "7.1 One risk process for information security and AI"),
        ("p", "We use one method, one set of 5 x 5 scales and one register for both kinds of risk. An "
              "information-security risk is anything that threatens confidentiality, integrity or availability. "
              "An AI risk is anything that could stop an AI system meeting its objectives or harm people through "
              "the AI system. Risk level is likelihood x impact:"),
        ("table", ["Level", "Score", "What we do"], [(n, f"{lo}–{hi}", act) for n, lo, hi, act in LEVELS],
         [2.5, 2, 12]),
        clause_table([
            ("Risks and opportunities (general)", "6.1.1", "6.1.1",
             "Issues and interested-party requirements from Clause 4 are turned into risks and opportunities "
             "during the twice-yearly context review.",
             "IMS-REG-001; IMS-REG-002"),
            ("Risk assessment", "6.1.2", "6.1.2",
             "Workshops with each team at least yearly and whenever a trigger occurs (new AI system, new "
             "supplier, major change, incident). AI risks consider the AI system's whole lifecycle.",
             "IMS-PRO-001; IMS-REG-002"),
            ("Risk treatment and SoA", "6.1.3", "6.1.3",
             "Risk owners choose treatment; controls are compared with both Annex A lists; decisions are recorded "
             "in two Statements of Applicability. The Trust Council approves the treatment plan and residual risk.",
             "IMS-REG-002; IMS-SOA-001; IMS-SOA-002"),
            ("AI system impact assessment", "—", "6.1.4",
             "Before release and on significant change, the Head of AI leads an impact assessment of each AI "
             "system on individuals, groups and society. Results feed the risk assessment.",
             "IMS-PRO-002"),
            ("Objectives", "6.2", "6.2",
             "One set of objectives with metrics, targets, owners and monitoring dates, approved yearly.",
             "IMS-REG-003"),
            ("Planning of changes", "6.3", "6.3",
             "Changes to the IMS itself (new scope, new committee, new standard) are planned, risk-assessed and "
             "approved by the Trust Council.",
             "Trust Council minutes; IMS-PRO-004"),
        ]),
        ("p", "Current objectives:"),
        ("table", ["ID", "Objective", "Target", "Owner"],
         [(o[0], o[1], o[3], person(o[4])) for o in OBJECTIVES], [1.6, 6.5, 5.4, 3]),

        # ------------------------------------------------------------------
        ("h1", "8. Clause 7 — Support"),
        clause_table([
            ("Resources", "7.1", "7.1",
             "People, budget and tools are agreed in the annual plan. For AI we also track the resources the "
             "standard highlights: data, tooling, compute, system components and human expertise.",
             "IMS-REG-005; IMS-SOA-002 (A.4)"),
            ("Competence", "7.2", "7.2",
             "Each IMS role has required competences; gaps are closed by training, mentoring or hiring; evidence "
             "is kept.",
             "IMS-PRO-003; IMS-REG-004"),
            ("Awareness", "7.3", "7.3",
             "Combined security and responsible-AI awareness training within 30 days of joining and every year "
             "after; monthly phishing simulation.",
             "IMS-PRO-003; IMS-REG-004"),
            ("Communication", "7.4", "7.4",
             "One communication plan: what, when, with whom, by whom — internal and external (customers, "
             "artists, regulators).",
             "IMS-REG-004 communication plan"),
            ("Documented information", "7.5", "7.5",
             "Documents have an ID, owner, version and approval; records are kept in defined systems for defined "
             "periods.",
             "IMS-PRO-004; IMS-WBK-001 register"),
        ]),

        # ------------------------------------------------------------------
        ("h1", "9. Clause 8 — Operation"),
        ("p", "Operation is where the plans become daily practice. Most of the Annex A controls of both "
              "standards live here, inside our topic policies and procedures."),
        clause_table([
            ("Operational planning and control", "8.1", "8.1",
             "Processes run as described in the topic policies; changes are controlled through pull requests and "
             "the change triggers; outsourced processes (cloud, model APIs, moderation) are controlled through "
             "supplier management.",
             "IMS-POL-002 to IMS-POL-006"),
            ("Risk assessment at planned intervals", "8.2", "8.2",
             "Yearly full review plus trigger-based reviews; results recorded in the register.",
             "IMS-REG-002"),
            ("Risk treatment", "8.3", "8.3",
             "Treatment actions tracked to completion; owners report progress to the Trust Council monthly.",
             "IMS-REG-002"),
            ("AI system impact assessment (performing it)", "—", "8.4",
             "Done at planned intervals and on significant change; approval is a condition of the AI Release "
             "Review go decision.",
             "IMS-PRO-002"),
        ]),
        ("p", "How the operational controls are organised:"),
        ("table", ["Area", "Main documents", "Typical controls (27001 / 42001)"], [
            ("Secure and responsible development", "IMS-POL-002",
             "8.25–8.29, 8.31, 8.32 / A.6.1.2–A.6.2.8"),
            ("Data governance and privacy for AI", "IMS-POL-003", "5.12, 5.34, 8.10–8.12 / A.7.2–A.7.6"),
            ("Access control", "IMS-POL-004", "5.15–5.18, 8.2–8.5"),
            ("Acceptable use incl. generative AI", "IMS-POL-005", "5.10, 6.7, 8.1 / A.9.2–A.9.4"),
            ("Suppliers and third-party AI", "IMS-POL-006", "5.19–5.23 / A.10.2–A.10.4"),
            ("Incidents", "IMS-PRO-005, IMS-REG-006", "5.24–5.28, 6.8 / A.8.4"),
            ("Continuity", "IMS-PRO-006", "5.29, 5.30, 8.13, 8.14"),
            ("Assets and AI system inventory", "IMS-REG-005", "5.9–5.12 / A.4.2–A.4.6"),
        ], [5, 4, 7.5]),

        # ------------------------------------------------------------------
        ("h1", "10. Clause 9 — Performance evaluation"),
        clause_table([
            ("Monitoring, measurement, analysis", "9.1", "9.1",
             "Each objective and key control has a metric, an owner and a frequency. The Compliance Coordinator "
             "prepares a one-page dashboard for every Trust Council meeting.",
             "IMS-REG-003"),
            ("Internal audit", "9.2", "9.2",
             "One audit programme covering both standards over 12 months, run by an independent contracted "
             "auditor with the Compliance Coordinator as audit coordinator.",
             "IMS-PRO-007; IMS-REG-007"),
            ("Management review", "9.3", "9.3",
             "The Trust Council acts as the management review twice a year, with a fixed agenda covering every "
             "input both standards require.",
             "IMS-PRO-008"),
        ]),

        # ------------------------------------------------------------------
        ("h1", "11. Clause 10 — Improvement"),
        clause_table([
            ("Continual improvement", "10.1", "10.1",
             "Improvement ideas from staff, audits, incidents and customers are logged and prioritised by the "
             "Trust Council.",
             "IMS-REG-008"),
            ("Nonconformity and corrective action", "10.2", "10.2",
             "Every nonconformity is recorded, contained, root-caused and corrected; effectiveness is checked "
             "before closure.",
             "IMS-PRO-009; IMS-REG-008"),
        ]),

        # ------------------------------------------------------------------
        ("h1", "12. How Annex A controls are selected — the two SoAs"),
        ("p", "We do not start from the control lists. We start from our risks and then use the lists as a "
              "checklist to make sure nothing important is missing:"),
        ("steps", [
            "Assess risks and AI impacts (Clause 6.1.2 and, for AI, 6.1.4).",
            "For each risk the owner chooses a treatment and the controls needed — from anywhere, including "
            "contracts, technical settings and training.",
            "Compare the chosen controls with ISO/IEC 27001 Annex A and ISO/IEC 42001 Annex A, control by control. "
            "Add any control we missed.",
            "Record every Annex A control in the right SoA: applicable or not, the justification, the risks or "
            "requirements it addresses, its implementation status and the evidence.",
            "The Trust Council approves both SoAs together with the risk treatment plan and the residual risks.",
            "Review the SoAs whenever risks change, and at least yearly before the management review.",
        ]),
        ("example", f"From one risk to two SoAs — {R5[0]}", [
            f"Risk: {R5[1]} ({SYS[R5[2]]}). Owner: {who(R5[3])}. Inherent score {R5[4]} x {R5[5]} = "
            f"{R5[4] * R5[5]}; residual {R5[6]} x {R5[7]} = {R5[6] * R5[7]}.",
            f"Controls chosen: {R5[9]}.",
            "In IMS-SOA-002 the AI supplier control (A.10.3) and the AI system deployment and verification "
            "controls point to this risk. In IMS-SOA-001 the supplier-change monitoring control (5.22) points to "
            "the same risk. One risk, one treatment plan, two SoA entries.",
            "When incident INC-2026-007 showed the supplier control was weak, the SoA entries, the risk and the "
            "supplier contract were updated together through corrective action CA-2026-004.",
        ]),
        ("tip", "A control is only 'not applicable' when there is a real reason — for example the activity does not "
                "exist in your scope. 'Too expensive' is not a reason to exclude; it is a reason to accept a risk, "
                "which needs a risk owner's signature."),

        # ------------------------------------------------------------------
        ("h1", "13. Documented-information map"),
        ("p", "Both standards require certain information to be documented. This map shows where we keep each "
              "item. Other documents and records we decided we need are listed in the document register."),
        ("table", ["Documented information", "27001", "42001", "Where it is held"], [
            ("Scope of the management system", "4.3", "4.3", "IMS-REG-001; section 2 of this manual"),
            ("Policy", "5.2", "5.2", "IMS-POL-001"),
            ("Risk assessment process", "6.1.2", "6.1.2", "IMS-PRO-001"),
            ("Risk treatment process", "6.1.3", "6.1.3", "IMS-PRO-001"),
            ("Statements of Applicability", "6.1.3", "6.1.3", "IMS-SOA-001; IMS-SOA-002"),
            ("Risk treatment plan", "6.1.3", "6.1.3", "IMS-REG-002"),
            ("AI system impact assessment process", "—", "6.1.4", "IMS-PRO-002"),
            ("Objectives", "6.2", "6.2", "IMS-REG-003"),
            ("Evidence of competence", "7.2", "7.2", "IMS-REG-004"),
            ("Documents the organisation decides it needs", "7.5.1", "7.5.1", "IMS-WBK-001 document register"),
            ("Operational planning and control records", "8.1", "8.1", "Pull requests, AI Release Review records, "
                                                                          "supplier reviews"),
            ("Risk assessment results", "8.2", "8.2", "IMS-REG-002"),
            ("Risk treatment results", "8.3", "8.3", "IMS-REG-002"),
            ("AI system impact assessment results", "—", "8.4", "Completed assessments filed per IMS-PRO-002"),
            ("Monitoring and measurement results", "9.1", "9.1", "IMS-REG-003 and dashboards"),
            ("Audit programme and audit results", "9.2.2", "9.2.2", "IMS-REG-007; audit reports per IMS-PRO-007"),
            ("Management review results", "9.3.3", "9.3.3", "Minutes per IMS-PRO-008"),
            ("Nonconformities and corrective actions", "10.2", "10.2", "IMS-REG-008"),
        ], [5.5, 1.6, 1.6, 7.8]),

        # ------------------------------------------------------------------
        ("h1", "14. Review and approval"),
        ("p", f"The Compliance Coordinator, {person('IMSC')}, keeps this manual current. It is reviewed at "
              "least yearly and after any change to scope, AI systems, structure or roles, and approved by "
              f"the CEO on behalf of the Trust Council. Related documents: {ref('IMS-REG-001')}; "
              f"{ref('IMS-GOV-001')}; {ref('IMS-POL-001')}; {ref('IMS-GDE-001')}."),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("CEO"), f"{title_of('CEO')}, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
