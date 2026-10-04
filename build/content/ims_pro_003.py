from org import AI_SYSTEMS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
NC_TRAIN = next(f for f in SAMPLE_AUDIT["findings"] if f[0] == "NC-2026-004")
CA_TRAIN = next(c for c in SAMPLE_CAPA if c[0] == "CA-2026-005")

DOC = {
    "id": "IMS-PRO-003",
    "summary": f"How {N} makes sure every person has the skills their role needs, knows what the management "
               "system expects of them, and how we decide what to say about security and AI — to whom, when, "
               "how and by whom — inside the company and outside it.",
    "clauses": {"27001": "7.2, 7.3, 7.4; Annex A 5.4, 5.5, 5.6, 6.3",
                "42001": "7.2, 7.3, 7.4; Annex A.4.6, A.8.2, A.8.3, A.8.4, A.8.5"},
    "howto": [
        f"Use this procedure together with the workbook {ref('IMS-REG-004')} — the procedure says what we do, "
        "the workbook holds the evidence (matrix, training records, campaign plan, communication plan).",
        "Auditors sample people, not paperwork: they pick two or three names and ask for proof of competence. "
        "Make sure every person in scope has a line in the training records.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"Controls only work when people understand them. A phishing-resistant key is useless if an engineer "
              "pastes an API key into a chat tool; a fairness test is useless if nobody knows how to read its result. "
              f"This procedure describes how {N} plans, builds, checks and records **competence** (can you do the "
              "job safely?), **awareness** (do you know the rules and why they matter?) and **communication** "
              "(do the right people hear the right thing at the right time?)."),
        ("p", "One process serves both standards. ISO/IEC 27001 and ISO/IEC 42001 have the same three support "
              "clauses (7.2, 7.3, 7.4); we run one competence matrix, one training programme and one communication "
              "plan, with AI-specific content added where it belongs."),
        ("h1", "2. Scope"),
        ("p", f"This procedure covers all employees, freelance contractors and interns of {N}, members of the "
              "Trust Council and the AI Release Review (including the external Artist Advisory Panel member), and "
              "suppliers' staff who work inside our systems. It covers all communication about information security "
              "and AI — internal messages, customer and artist notices, regulator contact and public statements."),
        ("std", [
            "Both standards ask you to decide what competence each role affecting performance needs, make sure "
            "people have it (through education, training or experience), act to close gaps, check whether those "
            "actions worked, and keep records as evidence (Clause 7.2 in each).",
            "Everyone working under your control must know the policy, how they contribute, and what happens if "
            "they do not follow it (Clause 7.3). ISO/IEC 27001 Annex A 6.3 adds a planned awareness and training "
            "programme.",
            "You must decide what to communicate, when, with whom and how (Clause 7.4); ISO/IEC 27001:2022 also "
            "asks who communicates.",
            "ISO/IEC 42001 adds AI-specific needs: competence for people working on AI (A.4.6), and information "
            "for users and other interested parties — system documentation, a way to report adverse impacts, "
            "incident communication and obligations to share information (A.8.2–A.8.5).",
            "The EU AI Act (Art. 4) separately expects providers and deployers of AI to take measures so that "
            "staff dealing with AI have a sufficient level of AI literacy.",
        ]),
        ("h1", "3. Roles and responsibilities"),
        ("table", ["Who", "Responsibility"], [
            (who("HOP"), "Owns this procedure and the workbook. Runs onboarding, enrols people in training, "
                         "chases overdue items, keeps training records, reports completion to the Trust Council."),
            (who("CISO"), "Defines security competences and content; runs phishing simulations; approves "
                          "security-related external statements."),
            (who("CAIO"), "Defines AI competences and AI literacy content; owns AI system documentation for users "
                          "(A.8.2) and approves AI-related external statements."),
            (who("DPO"), "Owns regulator communication (data protection authorities) and breach notifications; "
                         "reviews customer-facing privacy and AI transparency text."),
            (who("CREA"), "Owns communication with the artist community and the Artist Advisory Panel."),
            (who("CEO"), "Approves public statements about serious incidents; sets the tone in all-hands."),
            (who("IMSC"), "Keeps the communication plan current; files records; checks evidence before audits."),
            ("Line managers", "Confirm the competence of their people at onboarding, role changes and the yearly "
                              "check-in; release time for training."),
            ("Everyone", "Complete assigned training on time; report incidents, AI concerns and suspicious messages."),
        ], [5.5, 11]),
        ("h1", "4. Competence"),
        ("h2", "4.1 Defining what each role needs"),
        ("p", f"The **Competence Matrix** sheet in {ref('IMS-REG-004')} lists each role against a short set of "
              "competence areas, with a required level from 0 to 4:"),
        ("table", ["Level", "Meaning", "Typical evidence"], [
            ("0 — Not needed", "The role does not need this competence.", "—"),
            ("1 — Aware", "Knows the rules and when to ask for help.", "Onboarding course completed, quiz ≥ 80%"),
            ("2 — Practitioner", "Applies it independently in routine work.", "Role training, peer-reviewed work samples"),
            ("3 — Advanced", "Handles non-routine cases, reviews others' work.", "Certification, track record, "
                                                                                "led a review or assessment"),
            ("4 — Expert", "Sets direction and teaches others.", "Recognised qualification and years of experience"),
        ], [3.5, 7, 6]),
        ("p", "The competence areas are: information-security basics; **AI literacy**; secure development; AI/ML "
              "engineering and evaluation; data governance, privacy and creative rights; AI risk and impact "
              "assessment; cloud and identity security; incident response; content safety; supplier management; "
              "and management-system and audit skills."),
        ("h2", "4.2 AI-specific competence and AI literacy"),
        ("p", "Everybody at the company needs a baseline of AI literacy (level 1), because everybody uses AI tools "
              "or talks to customers about AI features. That baseline means a person can explain, in their own "
              "words:"),
        ("bullets", [
            "what our AI systems do and do not do, and their known limitations (for example, that "
            f"{SYS['AI-SYS-002']} can invent scenes that are not in the script);",
            "why outputs are labelled 'AI-assisted' and carry content credentials, and why that must never be "
            "removed;",
            "which AI tools are approved and what may never be put into them "
            f"({ref('IMS-POL-005')});",
            "how bias and unfairness can arise (for example in artist rankings) and how to raise a concern;",
            "how to report an AI incident or an adverse impact on a person.",
        ]),
        ("p", f"People who build, evaluate or oversee AI systems (Data and ML, engineering, the AI Release Review) "
              "need level 2–3 in AI/ML engineering and evaluation, AI risk and impact assessment, and data governance. "
              "Members of the AI Release Review must complete the impact-assessment walkthrough "
              f"({ref('IMS-PRO-002')}) before they vote on a release. People who supervise "
              f"{SYS['AI-SYS-004']} decisions (content-safety reviewers) need level 2 in content safety, "
              "including how to recognise a likeness of a real person."),
        ("tip", "Do not invent 30 competence areas. Ten to twelve, each with a one-line description, is plenty for a "
                "startup. If a gap matters, it shows up quickly; if it does not, you did not need the row."),
        ("h2", "4.3 Checking competence"),
        ("steps", [
            "**Hiring.** The hiring manager writes the competence needs of the role into the job description, using "
            "the matrix. Interviews include at least one security or AI-responsibility question for technical roles.",
            "**Onboarding (day 1–30).** People Ops records the person's current level against the matrix, based on "
            "CV, certificates and the manager's view. Any gap of 2 or more becomes a training action with a due date.",
            "**Role change.** A mover gets a new matrix line within 10 working days of the change.",
            "**Yearly check-in.** Each manager confirms current levels once a year (in October, before the "
            "management review). The Gap column in the workbook calculates automatically.",
            "**Closing gaps.** Options are training, mentoring, pairing with an expert, hiring, or using an "
            "external specialist (for example the part-time legal counsel for copyright). The action and its due "
            "date go into the Training Records sheet.",
        ]),
        ("h1", "5. Training and awareness"),
        ("h2", "5.1 The training programme"),
        ("table", ["Course", "Who", "When", "Pass rule"], [
            ("Security and Responsible AI Essentials (45 min, includes AI literacy and the AUP)", "Everyone "
             "including contractors", "Within 30 days of joining (access to Restricted data only after completion), "
             "then yearly", "Quiz ≥ 80%; signed AUP acknowledgement"),
            ("Secure Coding and AI Application Security (3 h)", "Engineers, ML engineers", "Within 60 days, then "
             "yearly", "Practical exercise reviewed"),
            ("Responsible AI in Practice: impact, fairness, consent (2 h)", "Data and ML, product, AI Release "
             "Review members", "Before first release decision, then yearly", "Walkthrough of a sample AIIA"),
            ("Content-safety reviewer training (1.5 h)", "Creative team, moderation reviewers", "Before first "
             "review shift, then every 6 months", "Calibration test ≥ 90% agreement"),
            ("Incident response tabletop (90 min)", "Incident team and on-call engineers", "Twice a year", "Attendance"),
            ("Phishing simulation", "Everyone", "Every quarter", "Report rate tracked (target ≥ 60%)"),
        ], [6, 3.5, 4, 3]),
        ("p", f"The full catalogue, with providers and refresh intervals, is in {ref('IMS-REG-004')}."),
        ("h2", "5.2 Awareness campaign"),
        ("p", "Training happens once or twice a year; awareness happens every month. The People and Operations Lead "
              "runs a light campaign: one topic per month, a short post in #general, a 5-minute slot at the all-hands, "
              "and a one-page 'what good looks like' note on the wiki. Topics follow our real risks — for example "
              "phishing and passkeys (RSK-IS-002), pasting secrets into AI tools (RSK-IS-003), labelling AI-generated "
              "work, and honouring artist opt-outs (RSK-AI-001)."),
        ("p", "Every person must know four things (the Clause 7.3 test): where the policy is and what it says about "
              "them; how their work contributes to security and responsible AI; what happens if they ignore the rules; "
              "and how to report a problem (#trust-report or trust@quillfen.example)."),
        ("h2", "5.3 Phishing simulations"),
        ("bullets", [
            "Quarterly, run by the Security Lead with the approved simulation tool. Templates mimic real threats "
            "to us: fake customer script shares, fake payout notices to artists, fake model-provider billing alerts.",
            "We measure the **report rate** (people who reported the message) as the headline number, and the click "
            "rate as a secondary one. A click is a learning moment, never a disciplinary matter on its own.",
            "Anyone who clicks twice in a row gets a 10-minute one-to-one with the Security Lead, not a public list.",
        ]),
        ("h2", "5.4 Evaluating effectiveness"),
        ("p", "Both standards ask whether training actually worked, not just whether it happened. We look at:"),
        ("table", ["Measure", "Source", "Target"], [
            ("Completion within 30 days of joining, and yearly", "Training Records", "100% (OBJ-05)"),
            ("Quiz pass rate at first attempt", "Learning platform", "≥ 85%"),
            ("Phishing report rate", "Simulation tool", "≥ 60% (OBJ-05)"),
            ("Secrets or code pasted into unapproved AI tools", "Data-loss alerts, incident log", "Falling quarter on quarter"),
            ("Competence gaps of 2+ levels open for > 90 days", "Competence Matrix", "Zero"),
            ("Staff who can name how to report an AI concern", "Audit interviews, pulse survey", "≥ 90%"),
        ], [6.5, 5, 5]),
        ("p", f"Results go to the Trust Council monthly and into the management review ({ref('IMS-PRO-008')}). "
              f"Metrics are tracked in {ref('IMS-REG-003')}."),
        ("example", f"{NC_TRAIN[0]} — late contractor training", [
            f"In internal audit {SAMPLE_AUDIT['id']} ({SAMPLE_AUDIT['dates']}) the auditor found: "
            f"\"{NC_TRAIN[3]}\" ({NC_TRAIN[1]}, {NC_TRAIN[2]}).",
            f"Corrective action {CA_TRAIN[0]}, owned by {who(CA_TRAIN[3])}, due {CA_TRAIN[4]}: {CA_TRAIN[2]}",
            "Both contractors completed the course the week after the audit. Their lines in the Training Records "
            "sheet show the late completion and the NC reference — we do not delete or back-date the evidence.",
            "Effectiveness check: the next three contractor onboardings will be sampled in the following audit.",
        ]),
        ("h1", "6. Communication"),
        ("h2", "6.1 How we decide what to communicate"),
        ("p", f"The **Communication Plan** sheet in {ref('IMS-REG-004')} answers, for each recurring message: "
              "what, why, to whom, when (or what triggers it), how (channel), who sends it and who approves it, and "
              "what record we keep. The table below is the summary."),
        ("table", ["What", "With whom", "When", "How", "Who"], [
            ("Policy changes and new procedures", "All staff and contractors", "Within 5 working days of approval",
             "#announcements + wiki change log; acknowledgement for policies", title_of("IMSC")),
            ("Risk, objective and audit status", "Trust Council", "Monthly", "Trust Council pack", title_of("IMSC")),
            ("Security and AI awareness topic", "All staff", "Monthly", "All-hands slot, #general, wiki", title_of("HOP")),
            ("AI system documentation and limitations", "Canvas and API customers", "Each release; kept current",
             "Help centre, API docs, model summary pages", title_of("CAIO")),
            ("How ArtistMatch ranks artists", "Artists and commissioning customers", "Kept current; 15 days' notice "
             "of material changes", "Commons help centre, artist newsletter", title_of("CREA")),
            ("Incident affecting customers or artists", "Affected parties", "Within 48 hours by default; sooner "
             "for S1 or where the contract says so", "Email, in-app banner, status page", title_of("CISO")),
            ("Personal-data breach", "Data protection authorities; data subjects", "Within legal deadlines "
             "(e.g. 72 hours under GDPR)", "Regulator portal; email", title_of("DPO")),
            ("Trust and certification status", "Prospects and customers", "On request; updated quarterly",
             "Trust Centre page, security questionnaire responses", title_of("CISO")),
            ("Supplier security and AI requirements", "Suppliers", "At onboarding and contract renewal",
             "Contract schedules, supplier questionnaire", title_of("DPO")),
        ], [3.8, 3.2, 3.5, 3.5, 2.5]),
        ("h2", "6.2 AI-specific information for interested parties"),
        ("p", "ISO/IEC 42001 asks for four extra kinds of communication about AI. This is how we meet each one:"),
        ("table", ["Need (42001)", "What we do"], [
            ("System documentation and information for users (A.8.2)",
             f"Each customer-facing AI system has a public summary page: purpose, how to use it well, known "
             f"limitations, the data it uses, and how outputs are labelled. {SYS['AI-SYS-001']} and "
             f"{SYS['AI-SYS-002']} pages live in the Canvas help centre; {SYS['AI-SYS-003']}'s ranking explanation "
             "lives in the Commons help centre. Updated before any release the AI Release Review approves."),
            ("External reporting of adverse impacts (A.8.3)",
             "A 'Report an AI concern' form in Canvas and Commons, plus trust@quillfen.example, lets anyone report "
             "harmful output, unfair ranking, a missing label or use of their work without consent. Reports reach the "
             f"incident queue within one working day and are acknowledged within 2 working days ({ref('IMS-PRO-005')})."),
            ("Communication of incidents (A.8.4)",
             "The incident procedure decides who must be told about an AI incident: affected customers, artists, "
             "the AI supplier, and regulators where the law requires it. Messages are factual, avoid blame and say "
             "what the person should do."),
            ("Information for interested parties (A.8.5)",
             "We keep a list of what we have promised or are obliged to share — for example contract clauses on AI use, "
             "EU AI Act transparency duties for AI-generated content, and artist consent terms — and who sends it. "
             f"The list is the 'Obligation' column of the communication plan and links to {ref('IMS-REG-001')}."),
        ], [5, 11.5]),
        ("example", f"Communicating {SAMPLE_INCIDENT['id']}", [
            f"{SAMPLE_INCIDENT['title']} ({SAMPLE_INCIDENT['date']}). {SAMPLE_INCIDENT['summary']}",
            f"Internal: incident channel opened the same day; the Trust Council was briefed at its next meeting.",
            f"Customer: {title_of('CISO')} and {title_of('CAIO')} called the customer within 24 hours of confirming "
            "the cause, followed by a written summary of what happened and what we changed.",
            f"Supplier: {title_of('DPO')} wrote to the {SYS['AI-SYS-004']} vendor asking for advance notice of model "
            "changes — later made a contract clause through CA-2026-004.",
            "Regulator: no personal data was disclosed and the image was not published, so no notification was "
            "required; the decision and reasoning were recorded in the incident log.",
        ]),
        ("h2", "6.3 Rules for external communication"),
        ("bullets", [
            "Only the people named in the communication plan speak for the company on security or AI topics. "
            "Everyone else forwards press, regulator or researcher contacts to trust@quillfen.example.",
            "Statements about a serious incident (S1 or S2) are approved by the CEO, with the Privacy and Legal Lead "
            "checking legal wording.",
            "We never overstate: no 'unhackable', 'bias-free' or 'fully compliant' claims. We say what we do and how we "
            "check it.",
            "Contact with authorities and special interest groups (ISO/IEC 27001 Annex A 5.5 and 5.6) is listed in "
            "the communication plan, with named owners and contact details kept on the wiki.",
            "Security researchers may report vulnerabilities through our published security.txt and disclosure page.",
        ]),
        ("tip", "If you are short of time, start with three external messages that customers ask about most: the "
                "Trust Centre page, the AI system summary pages, and the incident notification template. Everything "
                "else can grow from there."),
        ("h1", "7. Records and evidence"),
        ("table", ["Record", "Where", "Kept for"], [
            ("Competence matrix and yearly check-ins", "IMS-REG-004, Competence Matrix sheet", "Employment + 2 years"),
            ("Training and awareness completion, quiz scores", "Learning platform export + Training Records sheet",
             "Employment + 2 years"),
            ("Signed AUP acknowledgements", "HR system", "Employment + 2 years"),
            ("Phishing simulation results (aggregated)", "Security drive", "3 years"),
            ("Certificates and CVs used as evidence", "HR system (Restricted)", "Employment + 2 years"),
            ("Communication plan and key messages sent", "IMS-REG-004; email / ticket archive", "3 years"),
            ("Regulator and breach notifications", "Legal drive (Restricted)", "6 years"),
        ], [6.5, 6.5, 3.5]),
        ("p", f"Retention follows {ref('IMS-PRO-004')}."),
        ("h1", "8. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-GOV-001", "IMS-REG-004", "IMS-POL-005", "IMS-PRO-002",
                                      "IMS-PRO-005", "IMS-REG-003", "IMS-PRO-008", "IMS-PRO-009")]),
        ("h1", "9. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("HOP"), title_of("HOP") + ", document owner", "[[signature]]", "[[date]]"),
            (person("CEO"), "CEO, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
