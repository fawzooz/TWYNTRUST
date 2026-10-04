from org import AI_SYSTEMS, COMMITTEES, ORG, ROLES, SAMPLE_INCIDENT, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}

# IMS responsibilities per role key (adds to the one-line description in org.ROLES).
DUTIES = {
    "CEO": ("Accountable for the whole IMS. Approves policy, objectives, budget and risk acceptance above Medium. "
            "Chairs the Trust Council and the management review.", "CTO"),
    "CTO": ("Owns the development lifecycle and platform. Makes sure security and AI gates are built into CI/CD "
            "and that engineering has time for treatment actions. Owns AST-002, AST-003, AST-004 and AST-009.",
            "SRE"),
    "CISO": ("ISMS owner. Runs the risk method, the information-security risk register and IMS-SOA-001. Leads "
             "incident response. Advises on security in every AI Release Review.", "SRE"),
    "CAIO": ("AIMS owner. Owns AI risks, AI impact assessments and IMS-SOA-002. Chairs the AI Release Review. "
             "Accountable owner for StoryFrame, ScriptMate and ArtistMatch.", "HOD"),
    "DPO": ("Data protection officer. Keeps the legal register current, advises on privacy, AI law and contracts, "
            "handles data-subject requests and breach notifications, owns IMS-POL-006.", "LEGAL"),
    "CREA": ("Voice of artists and audiences. Signs off content-safety controls and labelling; accountable owner "
             "for SafeFrame as a control; links to the Artist Advisory Panel.", "CAIO"),
    "HOP": ("Hiring, screening, onboarding, training and offboarding for staff and contractors. Owns the "
            "competence matrix and training records.", "IMSC"),
    "IMSC": ("Coordinates the IMS day to day: document register, audit calendar, corrective-action log, Trust "
             "Council agenda and minutes, metrics dashboard. Audit coordinator, never auditor of own work.", "HOP"),
    "HOD": ("Datasets, data quality, provenance and consent records, model training and evaluation. Owns "
            "AST-005, AST-006 and AST-007.", "CAIO"),
    "SRE": ("Cloud, availability, backups, logging and continuity. Owns AST-001, AST-008 and AST-012.", "CISO"),
    "LEGAL": ("Part-time external counsel for contracts, IP and copyright questions; supports the Privacy and Legal "
              "Lead.", "DPO"),
}

RACI_COLS = ["TC", "CEO", "CTO", "CISO", "CAIO", "DPO", "CREA", "HOP", "IMSC", "HOD", "SRE"]
RACI = [
    ("Approve IMS policy and topic policies", "A", "R", "C", "R", "R", "C", "C", "I", "C", "I", "I"),
    ("Define context, scope and interested parties", "A", "C", "C", "C", "C", "C", "I", "I", "R", "I", "I"),
    ("Maintain legal and regulatory register", "I", "I", "I", "C", "C", "A/R", "I", "I", "C", "I", "I"),
    ("Run information-security risk assessment", "I", "I", "C", "A/R", "C", "C", "I", "I", "C", "C", "R"),
    ("Run AI risk assessment", "I", "I", "C", "C", "A/R", "C", "C", "I", "C", "R", "I"),
    ("AI system impact assessment", "I", "I", "C", "C", "A", "C", "R", "I", "I", "R", "I"),
    ("Accept residual risk above Medium", "A", "R", "C", "R", "R", "C", "C", "I", "I", "I", "I"),
    ("Maintain SoAs (27001 / 42001)", "A", "I", "C", "R", "R", "C", "C", "I", "C", "C", "I"),
    ("AI release go / no-go", "I", "I", "C", "C", "A/R", "C", "R", "I", "I", "C", "I"),
    ("Security and AI awareness training", "I", "I", "I", "C", "C", "C", "I", "A/R", "C", "I", "I"),
    ("Supplier due diligence (incl. AI suppliers)", "I", "I", "C", "R", "C", "A", "C", "I", "I", "C", "R"),
    ("Incident response (security and AI)", "I", "I", "R", "A", "R", "R", "R", "I", "I", "R", "R"),
    ("Access reviews", "I", "I", "R", "A", "C", "I", "I", "R", "C", "C", "R"),
    ("Internal audit programme", "I", "I", "I", "C", "C", "C", "I", "I", "A/R", "I", "I"),
    ("Management review", "A/R", "R", "C", "C", "C", "C", "C", "C", "R", "I", "I"),
    ("Corrective actions and improvement log", "I", "I", "C", "C", "C", "C", "C", "C", "A/R", "C", "C"),
]

DOC = {
    "id": "IMS-GOV-001",
    "summary": f"Who decides what in {N}'s integrated management system: the Trust Council and AI Release Review "
               "charters, role descriptions, the RACI chart, how a small team manages combined roles and conflicts, "
               "how concerns are raised, and who keeps contact with authorities and specialist groups.",
    "clauses": {"27001": "5.1, 5.3; Annex A 5.2, 5.3, 5.4, 5.5, 5.6, 6.8",
                "42001": "5.1, 5.3; Annex A.3.2, A.3.3, A.10.2"},
    "howto": [
        "Fill in your own people first (section 4), then the RACI chart. Each activity must have exactly one 'A'.",
        "In a startup it is normal for one person to hold several roles. Section 6 shows how to make that "
        "acceptable to an auditor: name the conflict and add a check by someone else.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"This charter sets out how {N} governs its integrated management system for information security "
              "and responsible AI: which bodies make decisions, who holds which role, who is responsible, "
              "accountable, consulted and informed for key activities, and how we keep decisions honest in a "
              "small company where people wear several hats."),
        ("h1", "2. Scope"),
        ("p", f"It applies to all staff, contractors and committee members within the scope in "
              f"{ref('IMS-REG-001')}, and to members of the external Artist Advisory Panel when they take part in "
              "the AI Release Review."),
        ("std", "Top management must show leadership of both systems, make sure roles and authorities are "
                "assigned and communicated, and name who reports on system performance. The Annex A controls add "
                "that responsibilities are defined and allocated, conflicting duties are separated where "
                "possible, people can report concerns about AI systems, responsibilities are shared clearly with "
                "partners and suppliers across the AI lifecycle, and contacts with authorities and specialist "
                "groups are kept."),

        ("h1", "3. Governance structure"),
        ("table", ["Body or role", "Reports to", "Main authority"], [
            ("Trust Council", "Board of directors (quarterly update)",
             "Approves policies, objectives, the two SoAs and residual risk above Medium; acts as management review."),
            ("AI Release Review", "Trust Council (monthly summary)",
             "Go / no-go for new or significantly changed AI systems; can impose conditions or block a release."),
            (who("CISO"), person("CEO"), "Owns the ISMS; can stop a deployment for a Critical security risk."),
            (who("CAIO"), person("CEO"), "Owns the AIMS; can suspend an AI feature for a Critical AI risk or harm."),
            (who("IMSC"), person("CEO"), "Coordinates the IMS; escalates overdue actions to the Trust Council."),
        ], [4.5, 4, 8]),

        ("h2", "3.1 Trust Council charter"),
        ("p", COMMITTEES["Trust Council"]),
        ("table", ["Item", "Rule"], [
            ("Purpose", "Top-management body for both standards; sets direction and makes the decisions the "
                        "standards reserve for top management."),
            ("Quorum", "The CEO (or the CTO as named deputy) plus at least one of the two system owners (Security "
                       "Lead or Head of AI)."),
            ("Standing agenda", "Metrics dashboard; open High and Critical risks; incidents since last meeting; "
                                "AI Release Review decisions; overdue corrective actions; decisions needed."),
            ("Management review", "Twice a year (April and October) the meeting runs the full agenda in "
                                  f"{ref('IMS-PRO-008')}."),
            ("Decisions", "By consensus; if none, the CEO decides and the dissent is minuted."),
            ("Records", "Minutes with decisions and actions within 3 working days, stored in the IMS workspace "
                        "by the Compliance Coordinator."),
        ], [3.5, 13]),

        ("h2", "3.2 AI Release Review charter"),
        ("p", COMMITTEES["AI Release Review"]),
        ("table", ["Item", "Rule"], [
            ("When it meets", "Before any new AI system goes live; on a significant change (new model or model "
                              "version, new training data, new use or user group, a supplier model update); and "
                              "when monitoring shows a fairness or safety threshold breached."),
            ("Inputs", f"Approved impact assessment ({ref('IMS-PRO-002')}), risk register entries, test and "
                       "evaluation results, security review, labelling and transparency check."),
            ("Possible decisions", "Go; go with conditions (owner and due date); no-go."),
            ("Veto", "The Creative Director and the Artist Advisory Panel member can each require a no-go on "
                     "artist-rights or content-safety grounds; the Trust Council can only overrule it in writing."),
            ("Records", "Gate record linked to the pull request or release ticket; summary to the Trust Council."),
        ], [3.5, 13]),
        ("example", "An AI Release Review decision", [
            f"After incident {SAMPLE_INCIDENT['id']} ({SAMPLE_INCIDENT['title']}), the review met to approve "
            f"re-enabling the vendor's newer model in {SYS['AI-SYS-004']}.",
            "Decision: go with conditions — keep version pinning, run the canary test set daily for 30 days and "
            "keep our own likeness check before image delivery. Owner: the Creative Director.",
        ]),

        ("h1", "4. Roles and responsibilities"),
        ("table", ["Role", "Person", "Responsibilities in the IMS", "Deputy"],
         [(title_of(k), person(k), DUTIES[k][0], person(DUTIES[k][1])) for k in ROLES],
         [3.5, 2.8, 7.7, 2.5]),
        ("bullets", [
            "**All managers** make sure their teams follow the policies, attend training and have time for "
            "treatment actions.",
            "**Everyone** (staff and contractors) follows the policies and reports incidents, weaknesses and AI "
            "concerns straight away.",
            "**Artist Advisory Panel** (three external artists, rotating yearly) gives an independent view on "
            "artist rights and fairness and sends one member to each AI Release Review.",
            "**AI system owners**: every AI system in the inventory has one accountable owner, named in "
            f"{ref('IMS-REG-005')}.",
        ]),
        ("p", "Role descriptions are part of each job description and contractor statement of work. People "
              "confirm in writing that they have read their IMS responsibilities when they join and when "
              "their role changes."),

        ("h1", "5. RACI chart"),
        ("p", "**R** = responsible (does the work), **A** = accountable (one person who answers for it), "
              "**C** = consulted, **I** = informed. **TC** = Trust Council. Column keys:"),
        ("table", ["Key", "Role"], [("TC", "Trust Council")] + [(k, who(k)) for k in RACI_COLS[1:]], [2, 14.5]),
        ("table", ["Activity"] + RACI_COLS, RACI, [4.5] + [1.1] * len(RACI_COLS)),

        ("h1", "6. Combined roles and conflicts of interest"),
        ("p", f"{N} has 34 people. We cannot give every role to a different person, and the standards do not "
              "require that. They require us to know where conflicts exist and to manage them. These are ours:"),
        ("table", ["Combined role or conflict", "Why it is a risk", "How we manage it"], [
            ("Head of AI owns the AIMS **and** is accountable owner of three AI systems",
             "Could approve her own systems' releases and impact assessments.",
             "Creative Director and Artist Advisory Panel hold a veto at the AI Release Review; the Trust Council "
             "sees every go decision."),
            ("CTO builds the platform **and** approves production changes",
             "Could bypass review under deadline pressure.",
             "Branch protection requires another engineer's review; emergency changes are reviewed within 2 "
             "working days by the Security Lead."),
            ("Security Lead is also a hands-on engineer with admin rights",
             "Could change logs or controls that monitor their own actions.",
             "Admin actions logged to a log store the Security Lead cannot delete; the Platform Engineer reviews "
             "admin activity monthly."),
            ("Compliance Coordinator coordinates the IMS **and** the internal audit",
             "Cannot audit their own work.",
             "Audits are done by an independent contracted auditor; the coordinator only schedules and supports."),
            ("CEO is top management **and** the commercial lead",
             "Revenue pressure may push risk acceptance.",
             "Risk acceptance above Medium needs the relevant system owner's written recommendation; disagreements "
             "are minuted."),
            ("Data and ML Lead trains models **and** checks consent records",
             "Could under-report consent gaps in training data.",
             "Monthly sample check of consent records by the Privacy and Legal Lead (OBJ-03 evidence)."),
        ], [4.5, 4.5, 7.5]),
        ("p", "Personal conflicts (for example a family link to a supplier, or a committee member's own artwork "
              "being affected by a decision) are declared to the chair at the start of a meeting and minuted; "
              "the person does not vote on that item."),
        ("tip", "Auditors do not expect perfect separation in a startup. They expect you to have **noticed** each "
                "conflict and to show a compensating check — a second reviewer, a log, a veto."),

        ("h1", "7. Segregation of duties"),
        ("table", ["Duty that must not be held alone", "Separated from", "Control"], [
            ("Writing code", "Approving its merge to main", "Branch protection; mandatory review by a different person"),
            ("Requesting access", "Approving that access", "Access requests approved by the system owner in the "
                                                          "identity provider"),
            ("Training or fine-tuning a model", "Approving its release", "AI Release Review gate"),
            ("Raising a supplier payment", "Approving it", "Two-person approval in the finance tool"),
            ("Running a control", "Auditing it", "Independent internal auditor"),
            ("Creating a user in production", "Reviewing user lists", "Quarterly access review by the Security Lead"),
        ], [5, 4.5, 7]),

        ("h1", "8. Raising concerns about security and AI"),
        ("p", "Anyone — staff, contractors, artists, customers or members of the public — can report a security "
              "event, a weakness or a concern about how one of our AI systems behaves or affects people."),
        ("table", ["Channel", "Who uses it", "Response time"], [
            ("#trust-report Slack channel", "Staff and contractors", "Acknowledged within 4 working hours"),
            ("trust@quillfen.example", "Anyone, including artists and customers", "Acknowledged within 1 working day"),
            ("Anonymous form (no login, no IP logging)", "Anyone who prefers not to be named",
             "Triaged within 2 working days"),
            ("Direct to the CEO or any Trust Council member", "If the concern is about a system owner",
             "Same day where possible"),
        ], [5.5, 5.5, 5.5]),
        ("steps", [
            "The Security Lead (security events) or the Head of AI (AI concerns) triages the report. If in "
            f"doubt, both look at it. Incidents follow {ref('IMS-PRO-005')}.",
            "Concerns about a system owner's own decisions go to the CEO, who assigns another Trust Council member.",
            "The reporter is told the outcome, unless they reported anonymously.",
            "Every report is logged in the incident and event log, including those that turn out to be nothing.",
            "We never retaliate against anyone who reports in good faith. Retaliation is a disciplinary matter.",
        ]),

        ("h1", "9. Contact with authorities and special interest groups"),
        ("p", "We keep a short list of who we contact, when and who owns the relationship, so that nobody "
              "searches for phone numbers during an incident. The list is checked every six months."),
        ("table", ["Organisation", "Why we would contact them", "Owner"], [
            ("UAE Data Office (UAE PDPL regulator)", "Personal-data breach affecting UAE data subjects",
             person("DPO")),
            ("EU / UK data protection authorities (via our GDPR representative); UK ICO",
             "Notifiable breach involving EU or UK personal data (72-hour rule)", person("DPO")),
            ("UAE Cyber Security Council / national CERT", "Serious cyber attack; threat intelligence",
             person("CISO")),
            ("Dubai Police (e-crime)", "Fraud, extortion or criminal misuse of our platform", person("CISO")),
            ("Child-protection reporting hotline in the relevant country",
             "Any detection of sexual content involving minors", person("CREA")),
            ("Cloud provider and model-API suppliers' security teams", "Incidents in their services",
             person("SRE")),
            ("[[your other authority]]", "[[trigger]]", "[[owner]]"),
        ], [6, 7, 3.5]),
        ("table", ["Special interest group", "What we get from it", "Owner"], [
            ("OWASP (incl. Top 10 for LLM Applications)", "Secure-development and AI-security guidance",
             person("CTO")),
            ("Content authenticity / C2PA community", "Content-credential standards for labelling outputs",
             person("CREA")),
            ("Local ISACA / ISC2 chapter", "Peer contacts, training, audit practice", person("CISO")),
            ("Responsible-AI and ISO/IEC 42001 practitioner groups", "Interpretation and good practice",
             person("CAIO")),
            ("Illustrators' and artists' associations", "Artist expectations on consent and fair pay",
             person("CREA")),
        ], [6, 7, 3.5]),

        ("h1", "10. Records"),
        ("bullets", [
            "Trust Council and AI Release Review minutes and gate records.",
            "Signed role acknowledgements and conflict-of-interest declarations.",
            "The concerns and event log.",
            "Contact list for authorities and special interest groups, with review date.",
        ]),
        ("p", f"Related documents: {ref('IMS-MAN-001')}; {ref('IMS-POL-001')}; {ref('IMS-PRO-008')}; "
              f"{ref('IMS-REG-004')}."),
        ("h1", "11. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("CEO"), f"{title_of('CEO')}, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
