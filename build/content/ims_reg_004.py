from datetime import date

from org import who, AI_SYSTEMS, ORG, SAMPLE_AUDIT, person, title_of

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
NC = next(f for f in SAMPLE_AUDIT["findings"] if f[0] == "NC-2026-004")


def P(key):
    return who(key)


LEVELS_0_4 = ["0", "1", "2", "3", "4"]

COMPETENCES = [
    "C-01 Information-security basics and policies",
    "C-02 AI literacy (EU AI Act Art. 4)",
    "C-03 Secure development and AI application security",
    "C-04 AI/ML engineering and evaluation (incl. fairness testing)",
    "C-05 Data governance, privacy and creative rights",
    "C-06 AI risk and impact assessment",
    "C-07 Cloud and identity security",
    "C-08 Incident response (security and AI)",
    "C-09 Content safety and moderation",
    "C-10 Supplier and AI vendor management",
    "C-11 Management systems and internal audit (27001 / 42001)",
]

GAP = "=IF(AND(ISNUMBER(D{r}),ISNUMBER(E{r})),MAX(0,D{r}-E{r}),\"\")"
GAP_STATUS = "=IF(F{r}=\"\",\"\",IF(F{r}=0,\"Met\",IF(F{r}=1,\"Partial\",\"Not met\")))"

matrix_rows = [
    (P("CAIO"), "Head of AI", COMPETENCES[5], 4, 4, GAP, GAP_STATUS, "MSc ML; led 3 AIIAs; ISO/IEC 42001 LI course",
     "—", "", date(2026, 10, 1)),
    (P("CAIO"), "Head of AI", COMPETENCES[10], 3, 2, GAP, GAP_STATUS, "42001 lead implementer course",
     "TRN-09 internal auditor course", date(2027, 1, 31), date(2026, 10, 1)),
    (P("CISO"), "Security Lead", COMPETENCES[6], 4, 3, GAP, GAP_STATUS, "Cloud security certification",
     "AWS security specialty exam", date(2027, 3, 31), date(2026, 10, 1)),
    (P("CISO"), "Security Lead", COMPETENCES[1], 2, 2, GAP, GAP_STATUS, "TRN-01 + TRN-03 completed", "—", "",
     date(2026, 10, 1)),
    (P("HOD"), "Data and ML Lead", COMPETENCES[3], 4, 4, GAP, GAP_STATUS, "8 yrs ML; built ArtistMatch", "—", "",
     date(2026, 10, 1)),
    (P("HOD"), "Data and ML Lead", COMPETENCES[4], 3, 2, GAP, GAP_STATUS, "TRN-03 completed",
     "Copyright & TDM opt-out briefing with external counsel", date(2026, 12, 15), date(2026, 10, 1)),
    (P("CTO"), "CTO", COMPETENCES[2], 3, 3, GAP, GAP_STATUS, "Code review lead; TRN-02", "—", "", date(2026, 10, 1)),
    (P("CREA"), "Creative Director", COMPETENCES[8], 4, 3, GAP, GAP_STATUS, "Runs reviewer calibration",
     "Trust & safety practitioner course", date(2027, 2, 28), date(2026, 10, 1)),
    (P("DPO"), "Privacy and Legal Lead", COMPETENCES[9], 3, 3, GAP, GAP_STATUS, "Negotiated 6 AI supplier DPAs",
     "—", "", date(2026, 10, 1)),
    (P("SRE"), "Platform Engineer (SRE)", COMPETENCES[7], 3, 2, GAP, GAP_STATUS, "On-call since 2025",
     "TRN-06 tabletop + shadow incident commander twice", date(2026, 12, 31), date(2026, 10, 1)),
    (P("IMSC"), "Compliance Coordinator", COMPETENCES[10], 3, 1, GAP, GAP_STATUS, "New in role",
     "TRN-09 internal auditor course (both standards)", date(2026, 11, 30), date(2026, 10, 1)),
    ("All staff (role group)", "All employees", COMPETENCES[1], 1, 1, GAP, GAP_STATUS, "TRN-01 quiz ≥ 80%", "—", "",
     date(2026, 10, 1)),
    ("Engineers (role group)", "Software engineers", COMPETENCES[2], 2, 1, GAP, GAP_STATUS,
     "4 of 11 not yet trained on prompt-injection", "TRN-02 module 3", date(2026, 12, 31), date(2026, 10, 1)),
    ("Contractors (role group)", "Freelance contractors", COMPETENCES[0], 1, 1, GAP, GAP_STATUS,
     "TRN-01 + AUP acknowledgement", "—", "", date(2026, 10, 1)),
    ("[[name or role group]]", "[[role]]", "[[competence area]]", "[[0-4]]", "[[0-4]]", GAP, GAP_STATUS,
     "[[evidence]]", "[[action]]", "[[due date]]", "[[date]]"),
]

catalogue_rows = [
    ("TRN-01", "Security and Responsible AI Essentials", "Everyone incl. contractors", "C-01, C-02",
     "E-learning (internal, 45 min) + quiz", "Within 30 days of joining", 12, "Quiz ≥ 80%; AUP signed",
     P("HOP"), "27001 7.2, 7.3, A 6.3; 42001 7.2, 7.3, A.4.6; EU AI Act Art. 4"),
    ("TRN-02", "Secure Coding and AI Application Security", "Engineers, ML engineers", "C-03",
     "Workshop (3 h) + hands-on lab (OWASP Top 10, LLM Top 10, prompt injection)", "Within 60 days", 12,
     "Lab exercise reviewed", P("CTO"), "27001 8.25, 8.28; 42001 A.6.2.4"),
    ("TRN-03", "Responsible AI in Practice: impact, fairness, consent", "Data and ML, product, AI Release Review",
     "C-02, C-04, C-05, C-06", "Workshop (2 h) + sample AIIA walkthrough", "Before first release decision", 12,
     "Walkthrough completed", P("CAIO"), "42001 A.4.6, A.5.2–A.5.4, A.7.3"),
    ("TRN-04", "Content-safety reviewer training", "Creative team, moderation reviewers", "C-09",
     "Live session (1.5 h) + calibration test", "Before first review shift", 6, "≥ 90% agreement",
     P("CREA"), "42001 A.6.2.6, A.9.3"),
    ("TRN-05", "Privacy and personal data essentials", "Support, People Ops, marketplace team", "C-05",
     "E-learning (30 min)", "Within 30 days", 24, "Quiz ≥ 80%", P("DPO"), "27001 5.34"),
    ("TRN-06", "Incident response tabletop", "Incident team, on-call engineers", "C-08",
     "Tabletop exercise (90 min) using a past incident", "On joining the rota", 6, "Attendance + actions",
     P("CISO"), "27001 5.24–5.27; 42001 A.8.4"),
    ("TRN-07", "Phishing simulation", "Everyone", "C-01", "Simulated emails (quarterly)", "From first month", 3,
     "Report rate tracked", P("CISO"), "27001 6.3"),
    ("TRN-08", "Supplier and AI vendor due diligence", "Privacy and Legal, procurement, product owners", "C-10",
     "Briefing (1 h) + checklist", "Before first supplier review", 24, "Checklist used once with review",
     P("DPO"), "27001 5.19–5.22; 42001 A.10.2–A.10.4"),
    ("TRN-09", "Internal auditor course (27001 + 42001)", "Compliance Coordinator, rotating peer auditors",
     "C-11", "External 2-day course", "Before first audit", 36, "Certificate", P("IMSC"), "27001 9.2; 42001 9.2"),
    ("[[TRN-xx]]", "[[course]]", "[[audience]]", "[[competences]]", "[[format / provider]]", "[[when]]",
     "[[months]]", "[[pass rule]]", "[[owner]]", "[[standard link]]"),
]

DUE = "=IF(NOT(ISNUMBER(D{r})),\"\",TEXT(D{r}+F{r},\"yyyy-mm-dd\"))"
REC_STATUS = ("=IF(NOT(ISNUMBER(D{r})),\"\",IF(ISNUMBER(H{r}),IF(H{r}<=D{r}+F{r},\"Done\",\"Done late\"),"
              "IF(TODAY()>D{r}+F{r},\"Overdue\",\"Open\")))")

records_rows = [
    ("TR-2026-001", P("CEO"), "Employee", date(2026, 1, 12), "TRN-01", 365, DUE, date(2026, 1, 20), 95, REC_STATUS,
     "LMS export Q1", ""),
    ("TR-2026-014", P("CAIO"), "Employee", date(2026, 2, 2), "TRN-03", 60, DUE, date(2026, 2, 18), "", REC_STATUS,
     "Attendance sheet", "Co-presented the session"),
    ("TR-2026-021", P("HOD"), "Employee", date(2026, 3, 2), "TRN-02", 60, DUE, date(2026, 3, 30), "", REC_STATUS,
     "Lab review in GitHub", ""),
    ("TR-2026-033", P("CREA"), "Employee", date(2026, 4, 6), "TRN-04", 30, DUE, date(2026, 4, 9), 96, REC_STATUS,
     "Calibration sheet", ""),
    ("TR-2026-040", "[Backend Engineer 1]", "Employee", date(2026, 5, 4), "TRN-01", 30, DUE,
     date(2026, 5, 19), 88, REC_STATUS, "LMS export", "New joiner"),
    ("TR-2026-041", "[Backend Engineer 1]", "Employee", date(2026, 5, 4), "TRN-02", 60, DUE,
     date(2026, 6, 25), "", REC_STATUS, "Lab review", ""),
    ("TR-2026-052", "[Contractor A] (Front-end developer)", "Contractor", date(2026, 7, 6), "TRN-01", 30, DUE,
     date(2026, 9, 24), 84, REC_STATUS, "LMS export",
     f"Late — {NC[0]} ({SAMPLE_AUDIT['id']}); onboarded by hiring manager, not People Ops. CA-2026-005"),
    ("TR-2026-053", "[Contractor B] (Illustrator, content reviewer)", "Contractor", date(2026, 7, 13), "TRN-01", 30, DUE,
     date(2026, 9, 25), 90, REC_STATUS, "LMS export",
     f"Late — {NC[0]} ({SAMPLE_AUDIT['id']}); CA-2026-005"),
    ("TR-2026-054", "[Contractor B] (Illustrator, content reviewer)", "Contractor", date(2026, 7, 13), "TRN-04", 30,
     DUE, date(2026, 9, 26), 92, REC_STATUS, "Calibration sheet", "No review shifts allowed before completion"),
    ("TR-2026-060", P("SRE"), "Employee", date(2026, 8, 20), "TRN-06", 30, DUE, date(2026, 8, 27), "", REC_STATUS,
     "Tabletop notes (INC-2026-007 scenario)", ""),
    ("TR-2026-071", "[Support Agent 1]", "Employee", date(2026, 9, 14), "TRN-01", 30, DUE, "", "",
     REC_STATUS, "", "Day-25 reminder sent (CA-2026-005)"),
    ("TR-2026-072", P("IMSC"), "Employee", date(2026, 9, 1), "TRN-09", 90, DUE, "", "", REC_STATUS, "",
     "Booked on external course"),
    ("[[TR-yyyy-nnn]]", "[[name (role)]]", "Employee", "[[start date]]", "[[TRN-xx]]", 30, DUE, "[[completed]]",
     "[[score]]", REC_STATUS, "[[evidence]]", "[[notes]]"),
]

campaign_rows = [
    ("2026-11", "Passkeys and phishing: why we report, not just ignore", "RSK-IS-002; OBJ-05",
     "A reported phish protects everyone. Use #trust-report.", "All-hands, #general, Q4 simulation", P("CISO"),
     "Report rate in Q4 simulation", "Planned"),
    ("2026-12", "What never goes into an AI tool", "RSK-IS-003",
     "Customer scripts, artist portfolios, secrets and personal data stay out of unapproved AI tools.",
     "Wiki one-pager, #general quiz", P("CISO"), "Data-loss alerts per month", "Planned"),
    ("2027-01", "AI literacy refresher: limits of " + SYS["AI-SYS-002"] + " and " + SYS["AI-SYS-001"],
     "RSK-AI-004; EU AI Act Art. 4", "AI drafts, people decide. Check outputs before sharing.",
     "Lunch-and-learn (recorded)", P("CAIO"), "Attendance; pulse survey", "Planned"),
    ("2027-02", "Labels and content credentials stay on", "RSK-AI-002",
     "Never strip the 'AI-assisted' label or C2PA data.", "All-hands, Canvas release notes", P("CREA"),
     "Label-removal tickets", "Planned"),
    ("2027-03", "Artist consent and opt-outs", "RSK-AI-001; OBJ-03",
     "No consent record, no training data.", "Data team stand-up, #general", P("HOD"),
     "Opt-out requests > 14 days", "Planned"),
    ("2027-04", "Reporting AI concerns and adverse impacts", "OBJ-02",
     "If an output looks harmful or unfair, report it — you will not be blamed.", "All-hands story", P("CAIO"),
     "AI concern reports per month", "Planned"),
    ("2027-05", "Clean desk, clean screen, safe travel", "Remote working",
     "Lock your screen; no customer work on shared screens in cafés.", "#general, wiki", P("HOP"),
     "Spot checks (Dubai office)", "Planned"),
    ("2027-06", "Fairness in ArtistMatch", "RSK-AI-003; OBJ-06",
     "How we measure fair exposure and why it matters to artists' income.", "Product all-hands", P("CAIO"),
     "Exposure ratio trend", "Planned"),
    ("2026-09", "Contractor onboarding reminder (after audit)", NC[0],
     "All contractors go through People Ops; training within 30 days.", "Manager email", P("HOP"),
     "Contractors trained on time", "Done"),
    ("[[yyyy-mm]]", "[[topic]]", "[[risk / objective]]", "[[key message]]", "[[channels]]", "[[owner]]",
     "[[measure]]", "Planned"),
]

comm_rows = [
    ("COM-01", "Policy and procedure changes", "All staff and contractors", "Internal", "Outbound",
     "Within 5 working days of approval", "#announcements, wiki change log, acknowledgement in HR system",
     P("IMSC"), "Document owner", "27001 / 42001 7.3, 7.5", "Message link; acknowledgements", "Implemented"),
    ("COM-02", "Monthly Trust Council pack (risks, objectives, incidents, audits)", "Trust Council", "Internal",
     "Two-way", "Monthly", "Shared doc + meeting", P("IMSC"), P("CEO"), "27001 / 42001 9.3",
     "Minutes", "Implemented"),
    ("COM-03", "Awareness topic of the month", "All staff", "Internal", "Outbound", "Monthly",
     "All-hands slot, #general, wiki", P("HOP"), P("CISO"), "27001 7.3, A 6.3; 42001 7.3",
     "Campaign sheet", "Implemented"),
    ("COM-04", "Reporting events, weaknesses and AI concerns", "All staff and contractors", "Internal", "Inbound",
     "Any time", "#trust-report, trust@quillfen.example", "Everyone", "—", "27001 A 6.8; 42001 A.8.3",
     "Incident log", "Implemented"),
    ("COM-05", "AI system summary pages (purpose, limits, data, labels)", "Canvas and API customers", "External",
     "Outbound", "Before each approved AI release; reviewed quarterly", "Help centre, API docs", P("CAIO"),
     "AI Release Review", "42001 A.8.2; EU AI Act Art. 50", "Page version history", "Implemented"),
    ("COM-06", "How " + SYS["AI-SYS-003"] + " ranks artists", "Artists, commissioning customers", "External",
     "Outbound", "Kept current; 15 days' notice of material changes", "Commons help centre, artist newsletter",
     P("CREA"), P("CAIO"), "42001 A.8.2, A.8.5; EU P2B ranking transparency", "Page history, newsletter archive",
     "Partially implemented"),
    ("COM-07", "Report an AI concern / adverse impact", "Customers, artists, public", "External", "Inbound",
     "Any time; acknowledge within 2 working days", "In-app form, trust@quillfen.example", P("CAIO"), "—",
     "42001 A.8.3", "Ticket queue", "Implemented"),
    ("COM-08", "Incident notification to affected customers / artists", "Affected parties", "External",
     "Outbound", "Default within 48 hours; sooner for S1 or if the contract says so",
     "Email, in-app banner, status page", P("CISO"), P("CEO") + " for S1/S2", "27001 A 5.24, 5.26; 42001 A.8.4",
     "Incident record", "Implemented"),
    ("COM-09", "Personal-data breach notification", "Data protection authorities; data subjects", "External",
     "Outbound", "Within legal deadlines (GDPR: 72 hours to authority)", "Regulator portal, email", P("DPO"),
     P("CEO"), "27001 A 5.5, 5.34; GDPR Art. 33–34; UAE PDPL", "Legal file", "Implemented"),
    ("COM-10", "Trust Centre: certifications, policies summary, sub-processors", "Prospects and customers",
     "External", "Outbound", "Quarterly and after changes", "Trust Centre web page", P("CISO"), P("CEO"),
     "42001 A.8.5; customer contracts", "Page history", "In progress"),
    ("COM-11", "Security and AI requirements for suppliers; model-change notices", "AI and cloud suppliers",
     "External", "Two-way", "Onboarding, renewal, and on any supplier model change", "Contract schedules, email",
     P("DPO"), P("CAIO"), "27001 A 5.20, 5.22; 42001 A.10.3", "Supplier file", "In progress"),
    ("COM-12", "Contact with authorities and special interest groups", "UAE and EU/UK authorities; CERTs; "
     "industry groups", "External", "Two-way", "As needed; contact list checked every 6 months", "Wiki contact list",
     P("CISO"), "—", "27001 A 5.5, 5.6", "Contact list", "Implemented"),
    ("COM-13", "Vulnerability disclosure", "Security researchers", "External", "Inbound",
     "Acknowledge within 3 working days", "security.txt, disclosure page", P("CISO"), "—", "27001 A 8.8",
     "Ticket queue", "Implemented"),
    ("[[COM-xx]]", "[[what]]", "[[with whom]]", "Internal", "Outbound", "[[when / trigger]]", "[[how]]",
     "[[who]]", "[[approver]]", "[[obligation]]", "[[record]]", "Planned"),
]

WB = {
    "id": "IMS-REG-004",
    "summary": f"The evidence behind {N}'s competence, awareness and communication process: who needs which skills, "
               "what training exists, who completed it and when, the monthly awareness campaign, and the plan for "
               "what we tell whom about security and AI.",
    "clauses": {"27001": "7.2, 7.3, 7.4; Annex A 5.5, 5.6, 6.3",
                "42001": "7.2, 7.3, 7.4; Annex A.4.6, A.8.2–A.8.5"},
    "howto": [
        "Procedure: IMS-PRO-003 Competence, Awareness and Communication Procedure.",
        "Competence Matrix: Gap and Status calculate from Required and Current level (0–4). Any 'Not met' row "
        "needs an action and a due date.",
        "Training Records: enter the start date and the number of days allowed; Due and Status calculate. "
        "'Overdue' rows go to the Trust Council every month. Never back-date or delete a late record.",
    ],
    "sheets": [
        {
            "name": "Competence Matrix",
            "title": "Competence matrix — required vs current level",
            "intro": "One row per person (or role group) and competence area. Levels: 0 not needed, 1 aware, "
                     "2 practitioner, 3 advanced, 4 expert. Areas: " + "; ".join(COMPETENCES) + ".",
            "headers": ["Person / role group", "Role", "Competence area", "Required level", "Current level", "Gap",
                        "Status", "Evidence", "Action to close gap", "Due", "Last reviewed"],
            "rows": matrix_rows,
            "widths": [30, 22, 38, 10, 10, 7, 11, 34, 34, 12, 13],
            "lists": {"Required level": LEVELS_0_4, "Current level": LEVELS_0_4},
            "status": ["Status"],
            "formulas": {"Gap": GAP, "Status": GAP_STATUS},
        },
        {
            "name": "Training Catalogue",
            "title": "Training catalogue",
            "intro": "Every course we run or buy, who must take it, and how often it must be refreshed.",
            "headers": ["Course ID", "Course", "Audience", "Competences", "Format / provider", "First due",
                        "Refresh (months)", "Pass rule", "Owner", "Standards / law"],
            "rows": catalogue_rows,
            "widths": [10, 34, 28, 16, 36, 22, 10, 22, 30, 32],
        },
        {
            "name": "Training Records",
            "title": "Training records",
            "intro": "One row per person per course. Days allowed: 30 for onboarding essentials, 60 for role "
                     "training, 365 for yearly refreshers. Status: Done, Done late, Open or Overdue.",
            "headers": ["Record ID", "Person", "Type", "Start / assigned date", "Course ID", "Days allowed", "Due",
                        "Completed on", "Score %", "Status", "Evidence", "Notes"],
            "rows": records_rows,
            "widths": [13, 36, 11, 13, 9, 9, 12, 13, 8, 11, 24, 46],
            "lists": {"Type": ["Employee", "Contractor", "Intern", "Supplier staff"],
                      "Course ID": [r[0] for r in catalogue_rows[:-1]]},
            "status": ["Status"],
            "formulas": {"Due": DUE, "Status": REC_STATUS},
        },
        {
            "name": "Awareness Campaign",
            "title": "Awareness campaign plan — one topic a month",
            "intro": "Topics follow real risks and objectives. Keep each message to one sentence people can repeat.",
            "headers": ["Month", "Topic", "Linked risk / objective", "Key message", "Channels", "Owner", "Measure",
                        "Status"],
            "rows": campaign_rows,
            "widths": [10, 40, 22, 48, 30, 30, 26, 12],
            "lists": {"Status": ["Planned", "In progress", "Done"]},
            "status": ["Status"],
        },
        {
            "name": "Communication Plan",
            "title": "Communication plan — what, with whom, when, how, who",
            "intro": "Internal and external communication for both standards, including AI-specific information "
                     "for users and interested parties (ISO/IEC 42001 A.8.2–A.8.5).",
            "headers": ["ID", "What", "With whom", "Internal / External", "Direction", "When / trigger", "How",
                        "Who communicates", "Approver", "Obligation / standard", "Record kept", "Status"],
            "rows": comm_rows,
            "widths": [8, 36, 28, 11, 11, 30, 32, 30, 26, 30, 22, 14],
            "lists": {"Internal / External": ["Internal", "External"],
                      "Direction": ["Outbound", "Inbound", "Two-way"],
                      "Status": ["Planned", "In progress", "Partially implemented", "Implemented"]},
            "status": ["Status"],
        },
    ],
}
