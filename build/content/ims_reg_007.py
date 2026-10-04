from org import AI_SYSTEMS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref, title_of

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
A = SAMPLE_AUDIT
F = A["findings"]
CA = {c[1]: c for c in SAMPLE_CAPA}
EXT = "Contracted auditor"
X_AI = f"{title_of('CAIO')} (cross-audit)"
X_IS = f"{title_of('CISO')} (cross-audit)"

PROGRAMME = [
    ("2026-05", "AUD-2026-01", "Cross-audit", "Context, leadership, risk method, access control", "4, 5, 6.1; A 5.15–5.18",
     "4, 5, 6.1", f"{X_AI} + {X_IS}", "All leads", "High", "Done", "NC-2026-001; OFI-2026-01 to OFI-2026-04"),
    ("2026-09", A["id"], "Full system audit", A["scope"], "4–10; Annex A sample", "4–10; Annex A sample", EXT,
     "All leads", "High", "Done", "; ".join(f[0] for f in F)),
    ("2026-10", "—", "Programme review", "Approve this programme; report AUD-2026-02 to the Trust Council", "9.2, 9.3",
     "9.2, 9.3", person("IMSC"), "Trust Council", "—", "Planned", ""),
    ("2026-11", "AUD-2026-03", "Cross-audit", "Supplier and cloud management incl. supplier AI changes",
     "5.19–5.23, 8.32", "A.10.2–A.10.4, 8.1", X_IS, title_of("DPO"), "High", "Planned", "Follows NC-2026-003"),
    ("2026-12", "AUD-2026-04", "Follow-up", "Verify effectiveness of CA-2026-004 and CA-2026-005", "10.2, 7.2, 5.22",
     "10.2, 7.2, A.10.3", EXT, f"{title_of('DPO')}, {title_of('HOP')}", "High", "Planned", ""),
    ("2027-01", "AUD-2027-01", "Cross-audit", "Identity, privileged access, endpoints", "5.15–5.18, 8.2–8.5, 8.1, 6.7",
     "—", X_AI, title_of("CISO"), "High", "Planned", ""),
    ("2027-02", "AUD-2027-02", "Cross-audit", f"AI data and consent ({STF} fine-tuning, {ARM} features)",
     "5.12, 5.33, 5.34", "A.7.2–A.7.6, A.4.3", X_IS, title_of("HOD"), "High", "Planned", "RSK-AI-001; OBJ-03"),
    ("2027-03", "AUD-2027-03", "Process audit", "Secure and responsible development lifecycle; AI Release Review",
     "8.8, 8.25–8.29, 8.31, 8.32", "8.2–8.4, A.6.1.2–A.6.2.8", EXT, f"{title_of('CTO')}, {title_of('CAIO')}",
     "High", "Planned", "OBJ-02; OBJ-04"),
    ("2027-04", "AUD-2027-04", "Cross-audit", "Incident management, continuity, backups, AI fallback",
     "5.24–5.30, 6.8, 8.13, 8.14", "A.3.3, A.4.5, A.8.3, A.8.4", X_AI, f"{title_of('CISO')}, {title_of('SRE')}",
     "Medium", "Planned", "INC-2026-007 lessons"),
    ("2027-05", "AUD-2027-05", "Process audit", "Monitoring, fairness and content-safety metrics; objectives",
     "9.1, 6.2, 8.16", "9.1, 6.2, A.6.2.6, A.5.2–A.5.5", EXT, f"{title_of('CAIO')}, {title_of('CREA')}", "High",
     "Planned", "OFI-2026-05; OBJ-06"),
    ("2027-06", "AUD-2027-06", "Full system audit", "Pre-certification audit of the whole system", "4–10; all applicable Annex A",
     "4–10; all applicable Annex A", EXT, "All leads", "High", "Planned", "Before stage 1"),
    ("2027-08", "AUD-2027-07", "Cross-audit", "Competence, awareness, documented information", "7.1–7.5, 6.3, 5.37",
     "7.1–7.5, A.4.6", X_AI, f"{title_of('HOP')}, {title_of('IMSC')}", "Medium", "Planned", "NC-2026-004 recurrence"),
    ("2027-09", "AUD-2027-08", "Follow-up", "Close-out of pre-certification findings; programme for next cycle",
     "9.2, 10.1, 10.2", "9.2, 10.1, 10.2", EXT, person("IMSC"), "Medium", "Planned", "OBJ-01"),
]

C = "Conforms"
Q = [
    # 27001, 42001, area, question, evidence, result, notes
    ("4.1", "4.1", "Context", "Have internal and external issues affecting security and AI been identified and "
     "reviewed in the last 12 months?", "Context register with review date; Trust Council minutes", C, ""),
    ("—", "4.1", "Context", "Is our role (provider, producer, user) recorded for each AI system?",
     "AI system inventory, role column", C, "Roles recorded for all five systems"),
    ("4.2", "4.2", "Context", "Are interested parties, their needs and which of them we treat as obligations "
     "recorded?", "Interested-party register; legal and contractual register", C, ""),
    ("4.3", "4.3", "Context", "Is one scope documented, with boundaries and interfaces to suppliers?",
     "Scope statement; network/data-flow diagram", C, ""),
    ("4.4", "4.4", "Context", "Are the system's processes and how they interact defined?",
     "Manual process map", C, ""),
    ("5.1", "5.1", "Leadership", "Can top management show how they direct and resource the system?",
     "Trust Council minutes; budget lines; CEO interview", C, ""),
    ("5.2", "5.2", "Leadership", "Is the policy approved, available and understood by staff?",
     "Signed policy; intranet; 3 staff interviews", C, ""),
    ("5.3", "5.3", "Leadership", "Are roles and authorities for security and AI assigned and known?",
     "Governance charter; RACI; interviews", C, ""),
    ("A 5.1", "A.2.2–A.2.4", "Policies", "Are topic policies aligned with the top policy and reviewed on schedule?",
     "Policy set with review dates", C, ""),
    ("6.8", "A.3.3", "Leadership", "Can staff and others raise AI concerns easily and without fear of reprisal?",
     "Reporting channel; examples of concerns raised", C, "Two concerns raised this year, both answered"),
    ("6.1.1", "6.1.1", "Planning", "Were risks and opportunities for the management system itself considered?",
     "Risk register entries for the system", C, ""),
    ("6.1.2", "6.1.2", "Planning", "Is the risk method defined so results are consistent and comparable?",
     ref("IMS-PRO-001"), C, ""),
    ("6.1.2", "6.1.2", "Planning", "Is the risk register current, with owners and scores for a sample of risks?",
     "Sample 5 risks in the register", C, "Sampled RSK-AI-001..005"),
    ("6.1.3", "6.1.3", "Planning", "Do risk owners approve treatment plans and residual risk, with Trust Council "
     "approval above Medium?", "Approval records; minutes", C, ""),
    ("6.1.3 d", "6.1.3", "Planning", "Do both Statements of Applicability justify inclusions and exclusions and show "
     "implementation status?", "Both SoAs", C, ""),
    ("—", "6.1.4", "Planning", "Has an impact assessment been done for each AI system, covering individuals, groups "
     "and society?", "Impact assessment records", C, ""),
    ("6.2", "6.2", "Planning", "Are objectives measurable, monitored and supported by plans?", ref("IMS-REG-003"), C, ""),
    ("6.3", "6.3", "Planning", "Are changes to the management system planned and controlled?", "Change records", C, ""),
    ("7.1", "7.1", "Support", "Are enough people, time and tools provided?", "Budget; interviews", C, ""),
    ("7.2", "7.2", "Support", "Are competence needs defined and is competence evidenced for key roles?",
     "Competence matrix; certificates", C, ""),
    ("7.2, 7.3", "7.2, 7.3", "Support", "Do new joiners, including contractors, finish awareness training within "
     "30 days?", "Sample of joiners vs training records", "Minor NC", F[1][0]),
    ("7.3", "7.3", "Support", "Do staff know the policy, their part, and what happens if rules are not followed?",
     "Interviews with 5 staff", C, ""),
    ("7.4", "7.4", "Support", "Is there a plan for internal and external communication on security and AI?",
     "Communication plan", C, ""),
    ("7.5", "7.5", "Support", "Are documents versioned, approved, reviewed and access-controlled?",
     "Document register; 3 sampled documents", C, ""),
    ("—", "A.4.2–A.4.6", "AI resources", "Are data, tools, computing and human resources for each AI system "
     "documented?", "AI system inventory; resource records", C, ""),
    ("6.1, 6.2, 6.6", "—", "People", "Are screening, employment terms and confidentiality agreements in place for "
     "staff and contractors?", "Sample of contracts and NDAs", C, ""),
    ("8.1", "8.1", "Operation", "Are processes, including outsourced ones, planned and controlled?",
     "Procedures; supplier controls", C, ""),
    ("8.2", "8.2", "Operation", "Is risk re-assessed after significant changes and incidents?",
     f"Risk register history after {SAMPLE_INCIDENT['id']}", C, "RSK-AI-005 reassessed 2026-08-26"),
    ("8.3", "8.3", "Operation", "Are risk treatment actions done on time?", "Sample of treatment actions", C, ""),
    ("—", "8.4", "Operation", "Are AI impact assessments repeated when systems change significantly?",
     "Impact assessment versions", C, ""),
    ("—", "A.6.1.2, A.6.1.3", "AI lifecycle", "Are objectives and a defined process for responsible AI design and "
     "development in place?", ref("IMS-POL-002"), C, ""),
    ("8.25–8.28", "A.6.2.2, A.6.2.3", "AI lifecycle", "Are requirements and design for AI systems documented, "
     "including security?", "Design docs for one release", C, ""),
    ("8.29", "A.6.2.4", "AI lifecycle", "Is each AI release verified and validated (security, accuracy, fairness, "
     "content safety) before go-live?", "Evaluation reports for sampled releases", C, ""),
    ("8.32", "A.6.2.5", "AI lifecycle", "Does every AI deployment go through the AI Release Review with a recorded "
     "decision?", "Release Review records (all in period)", C, "3 of 3 releases"),
    ("8.16", "A.6.2.6", "AI lifecycle", "Are AI systems monitored in operation (drift, fairness, content-safety "
     "canaries) with alerts?", "Dashboards; alert rules", "OFI", F[2][0]),
    ("8.15", "A.6.2.7, A.6.2.8", "AI lifecycle", "Is technical documentation kept and are AI event logs recorded "
     "and retained?", "Model cards; log retention settings", C, ""),
    ("5.33, 5.34", "A.7.2–A.7.6", "AI data", "Can we prove licence or consent for training data and its "
     "provenance and quality?", "Sample 20 images in consent ledger", C, "20 of 20 traced"),
    ("—", "A.8.2–A.8.5", "Information for users", "Are AI outputs labelled, documented for users, and is there a "
     "way to report problems?", "Product walkthrough; help pages", C, ""),
    ("—", "A.9.2–A.9.4", "Use of AI", "Are intended uses defined and responsible-use processes in place?",
     "Terms of service; acceptable use policy", C, ""),
    ("5.10", "A.9.2, A.9.4", "Use of AI", "Do staff use only approved AI tools and follow the rules on sensitive data?",
     f"{CDA} settings; data-loss alerts", C, ""),
    ("5.9", "A.4.2", "Assets", "Is the asset and AI system inventory complete with owners?", ref("IMS-REG-005"), C, ""),
    ("5.12, 5.13", "—", "Assets", "Is information classified and labelled?", "Sample of files and buckets", C, ""),
    ("5.15–5.18", "—", "Access", "Are joiners, movers and leavers handled and access reviewed quarterly?",
     "Leaver sample; access review records", C, "NC-2026-001 verified closed"),
    ("5.19–5.22", "A.10.2–A.10.4", "Suppliers", "Do supplier contracts include security and AI requirements, and are "
     "supplier changes monitored and assessed?", f"{SFR} agreement; change log", "Minor NC", F[0][0]),
    ("5.23", "A.10.3", "Suppliers", "Are cloud services selected, managed and exited securely?", "Cloud policy; "
     "provider reports", C, ""),
    ("5.24–5.28, 6.8", "A.8.3, A.8.4", "Incidents", "Are incidents reported, classified, handled, notified and "
     "learned from?", f"Sample of 3 incidents incl. {SAMPLE_INCIDENT['id']}", C, ""),
    ("5.29, 5.30, 8.13, 8.14", "A.4.5", "Continuity", "Is there a BIA, are backups and AI fallbacks tested?",
     ref("IMS-PRO-006") + "; test reports", C, ""),
    ("5.31, 5.34", "—", "Compliance", "Are legal requirements (GDPR, UAE PDPL, EU AI Act, copyright) identified and "
     "met?", "Legal register; privacy records", C, ""),
    ("5.37", "—", "Operations", "Are operating procedures (runbooks) documented and available?", "Runbooks", C, ""),
    ("6.7, 7.9, 8.1", "—", "Endpoints", "Are laptops encrypted, managed and protected for remote work?",
     "Device management report", C, ""),
    ("8.2–8.5", "—", "Technology", "Is privileged access limited, with phishing-resistant MFA?",
     "Admin list; SSO settings", C, ""),
    ("8.7, 8.8", "—", "Technology", "Are malware protection and vulnerability fixing within target times?",
     "Vulnerability dashboard; OBJ-04", C, ""),
    ("8.9", "—", "Technology", "Is configuration managed as code with drift detection?", "IaC repo; config alerts", C, ""),
    ("8.11, 8.12", "—", "Technology", "Are data masking and leakage prevention applied where needed?",
     "DLP rules; test data policy", C, ""),
    ("8.15–8.17", "A.6.2.8", "Technology", "Are logs collected, protected, monitored and time-synchronised?",
     "Log platform; alert examples", C, ""),
    ("8.20–8.23", "—", "Technology", "Are networks segmented and web access filtered?", "Network config", C, ""),
    ("8.24", "—", "Technology", "Are encryption keys managed?", "Key management settings", C, ""),
    ("8.32", "—", "Technology", "Do changes, including supplier model changes, go through change management?",
     "Change tickets", C, f"Supplier model changes covered by {F[0][0]}"),
    ("9.1", "9.1", "Performance", "Is it defined what is measured, how, when and who analyses it?",
     ref("IMS-REG-003"), C, ""),
    ("9.2", "9.2", "Performance", "Is there an audit programme with objective auditors and reported results?",
     "This workbook; reports", C, ""),
    ("9.3", "9.3", "Performance", "Did management review cover all required inputs and record decisions?",
     "Minutes of last review", C, ""),
    ("10.1, 10.2", "10.1, 10.2", "Improvement", "Are nonconformities corrected, root causes found and effectiveness "
     "checked?", ref("IMS-REG-008"), C, ""),
]

CHECK = [(f"Q{i:02d}",) + q[:5] + q[5:] for i, q in enumerate(Q, 1)]
CHECK.append((f"Q{len(Q) + 1:02d}", "[[ref]]", "[[ref]]", "[[area]]", "[[your question]]", "[[evidence]]",
              "Not audited", ""))

def chk(fid):
    return next(c[0] for c in CHECK if c[7] == fid)

FINDINGS = [
    (F[0][0], A["id"], F[0][1], F[0][2], F[0][3], f"{SFR} agreement has no model-change clause; vendor update of "
     f"2026-08-12 went live unassessed ({SAMPLE_INCIDENT['id']}).", chk(F[0][0]), person(CA[F[0][0]][3]),
     CA[F[0][0]][0], CA[F[0][0]][4], "Open"),
    (F[1][0], A["id"], F[1][1], F[1][2], F[1][3], "6 of 9 joiners sampled; 2 contractors (start 2026-07-07 and "
     "2026-07-14) missed the 30-day deadline.", chk(F[1][0]), person(CA[F[1][0]][3]), CA[F[1][0]][0],
     CA[F[1][0]][4], "Open"),
    (F[2][0], A["id"], F[2][1], F[2][2], F[2][3], "July dip to 0.76 found only at monthly review.", chk(F[2][0]),
     person("CAIO"), "Improvement Register", "2026-12-15", "Open"),
    ("[[ID]]", "[[AUD-YYYY-NN]]", "[[grade]]", "[[requirement]]", "[[finding]]", "[[evidence]]", "[[Q no.]]",
     "[[owner]]", "[[CA ID]]", "[[due]]", "Open"),
]

WB = {
    "id": "IMS-REG-007",
    "summary": f"The 12-month internal audit programme for {N}'s integrated management system, a reusable checklist "
               f"covering Clauses 4–10 of both standards and key Annex A areas, and the findings of {A['id']}. "
               f"Used with {ref('IMS-PRO-007')}.",
    "clauses": {"27001": "9.2.1, 9.2.2", "42001": "9.2.1, 9.2.2"},
    "howto": [
        "Copy the checklist for each audit and keep only the questions in scope. Write evidence you actually saw in "
        "Notes (document ID, record ID, who you interviewed).",
        "The checklist questions are written in our own words. Always check the requirement against your licensed "
        "copy of each standard.",
    ],
    "sheets": [
        {"name": "Audit Programme", "title": "Integrated audit programme (rolling 12 months)",
         "intro": "One row per audit or programme activity. Every clause of both standards and every applicable "
                  "Annex A control is covered at least once per cycle; high-risk areas more often.",
         "headers": ["Month", "Audit ID", "Type", "Area / process", "ISO/IEC 27001 refs", "ISO/IEC 42001 refs",
                     "Auditor", "Auditees", "Risk priority", "Status", "Notes / links"],
         "rows": PROGRAMME,
         "widths": [10, 13, 16, 40, 22, 22, 26, 24, 10, 11, 28],
         "lists": {"Type": ["Full system audit", "Process audit", "Cross-audit", "Follow-up", "Programme review"],
                   "Risk priority": ["High", "Medium", "Low", "—"],
                   "Status": ["Planned", "In progress", "Done", "Overdue"]},
         "levels": ["Risk priority"], "status": ["Status"]},
        {"name": "Audit Checklist", "title": f"Audit checklist — results shown for {A['id']}",
         "intro": "Questions in our own words, mapped to both standards. Result: Conforms / Minor NC / Major NC / OFI / "
                  "Not audited.",
         "headers": ["No.", "Ref ISO/IEC 27001", "Ref ISO/IEC 42001", "Area", "Question", "Evidence to look for",
                     "Result", "Notes"],
         "rows": CHECK,
         "widths": [6, 16, 16, 16, 55, 36, 12, 30],
         "lists": {"Result": ["Conforms", "Minor NC", "Major NC", "OFI", "Not audited"]}},
        {"name": "Findings", "title": f"Findings — {A['id']} ({A['dates']})",
         "intro": f"Copied into {ref('IMS-REG-008')} for corrective action. Grades as defined in "
                  f"{ref('IMS-PRO-007')} section 8.",
         "headers": ["Finding ID", "Audit ID", "Grade", "Requirement", "Finding", "Evidence", "Checklist no.",
                     "Owner", "Action / register", "Due", "Status"],
         "rows": FINDINGS,
         "widths": [13, 12, 18, 22, 45, 40, 10, 16, 18, 11, 11],
         "lists": {"Grade": ["Major nonconformity", "Minor nonconformity", "Opportunity for improvement"],
                   "Status": ["Open", "In progress", "Closed"]},
         "status": ["Status"]},
    ],
}
