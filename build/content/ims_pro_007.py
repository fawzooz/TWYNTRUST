from org import AI_SYSTEMS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref, title_of, who

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
A = SAMPLE_AUDIT
F = A["findings"]
CA = {c[1]: c for c in SAMPLE_CAPA}

DOC = {
    "id": "IMS-PRO-007",
    "summary": f"How {N} plans and runs internal audits of its integrated management system — one audit programme "
               "covering ISO/IEC 27001 and ISO/IEC 42001 — including auditor independence in a small company, "
               f"sampling, grading of findings and follow-up. Contains the full report of {A['id']} and a blank "
               "report template.",
    "clauses": {"27001": "9.2.1, 9.2.2; 10.2; Annex A 5.35", "42001": "9.2.1, 9.2.2; 10.2"},
    "howto": [
        "If this is your first audit, hire an experienced auditor for a few days rather than auditing yourself. "
        "Shadow them, then use their checklist (IMS-REG-007) to run smaller cross-audits in between.",
        "Section 11 is a real-looking example; section 12 is the empty template to copy for your own reports.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", "An internal audit is a planned, honest check of whether we do what our management system says, "
              "whether that meets both standards, and whether it actually works. It is how we find problems before "
              "a certification auditor — or an incident — finds them for us."),
        ("h1", "2. Scope"),
        ("p", f"The audit programme covers the whole integrated management system defined in {ref('IMS-REG-001')}: "
              "Clauses 4 to 10 of both standards, the applicable controls in both Statements of Applicability "
              f"({ref('IMS-SOA-001')} and {ref('IMS-SOA-002')}), all in-scope AI systems, and the processes of "
              "suppliers we rely on, to the extent our contracts allow."),
        ("std", [
            "Both standards ask for internal audits at planned intervals that tell you whether the management "
            "system meets your own requirements and the standard's, and whether it is effectively implemented and "
            "maintained (9.2.1).",
            "Both ask you to plan an audit programme — frequency, methods, responsibilities, reporting — that takes "
            "into account how important processes are and the results of earlier audits; to define the criteria "
            "and scope of each audit; to choose auditors who are objective and impartial; to report results to "
            "relevant management; and to keep evidence of the programme and results (9.2.2).",
            "ISO/IEC 27001 Annex A 5.35 adds independent review of information security at planned intervals or "
            "after significant change.",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Who", "Responsibility"], [
            ("Audit programme owner", who("IMSC"),
             "Maintains the programme in " + ref("IMS-REG-007") + ", books auditors, coordinates audits, tracks "
             "findings to closure."),
            ("Lead auditor", "Contracted independent auditor (qualified ISO/IEC 27001 and ISO/IEC 42001 lead auditor)",
             "Plans and leads full-system audits, grades findings, writes the report."),
            ("Cross-auditors", f"{title_of('CISO')} and {title_of('CAIO')}, trained in auditing",
             "Run smaller audits of each other's areas between full audits."),
            ("Auditees", "Process and control owners",
             "Provide evidence on time, agree facts, propose corrective actions."),
            ("Trust Council", "Chair: " + who("CEO"),
             "Approves the programme, receives reports, ensures resources for corrective action."),
        ], [3.5, 5.5, 7.5]),
        ("h1", "4. Auditor independence in a startup"),
        ("p", f"At {N} almost everyone owns some part of the management system, so nobody is fully independent. "
              "The standards do not require an outside auditor; they require that auditors are objective and do not "
              "audit their own work. We meet this as follows:"),
        ("table", ["Option", "When we use it", "How independence is kept"], [
            ("Contracted auditor", "At least one full-system audit a year, and before certification",
             "No other consulting work for us on the areas audited in the same year; signs a confidentiality and "
             "conflict-of-interest statement."),
            ("Cross-audit", "Smaller, focused audits between full audits",
             f"The {title_of('CISO')} audits AI processes; the {title_of('CAIO')} audits security processes. Nobody "
             "audits a process they own or wrote the procedure for."),
            ("Audit coordinator", "Every audit", f"The {title_of('IMSC')} schedules and supports but does not grade "
             "findings in areas they administer (document control, corrective-action log)."),
        ], [3.5, 5, 8]),
        ("tip", "Budget roughly 3–4 auditor days for a full remote audit of a 30–50 person company with five AI "
                "systems. Pairing a contracted auditor with your coordinator also trains your own people."),
        ("h1", "5. The audit programme"),
        ("bullets", [
            "Runs on a rolling 12-month cycle, recorded in the Audit Programme sheet of " + ref("IMS-REG-007") + ".",
            "Every clause of both standards and every applicable Annex A control is audited at least once per cycle.",
            "Higher-risk areas are audited more often: AI release decisions, training-data consent, content safety, "
            "supplier AI changes, access to production, and anything linked to recent incidents or nonconformities.",
            "The programme is approved by the Trust Council each October and changed when risks, incidents or "
            "the organisation change significantly.",
        ]),
        ("h1", "6. Planning an audit"),
        ("steps", [
            "At least 2 weeks before: the lead auditor and coordinator agree the audit plan — objectives, scope, "
            "criteria (standards, our procedures, contracts, laws), sample areas, interview timetable.",
            "Send the plan to auditees and ask for a short evidence pack (registers, recent records).",
            "Prepare a checklist from the Audit Checklist sheet, focused on the areas in scope and recent issues.",
            "Confirm access: read-only access to tools, screen-share sessions, and redacted samples where data is "
            "Restricted.",
        ]),
        ("h1", "7. Conducting the audit"),
        ("h2", "7.1 Methods"),
        ("bullets", [
            "**Interview** the people who do the work, not just the owners of documents.",
            "**Inspect records**: tickets, logs, release-gate records, training records, contracts.",
            "**Observe** live: ask an engineer to show the kill switch, the secret-scanning alert, the canary dashboard.",
            "**Trace** one item end to end — for example one AI release from impact assessment to monitoring.",
        ]),
        ("h2", "7.2 Sampling"),
        ("p", "Auditors cannot check everything. Pick samples at random or by risk, write down how they were chosen, "
              "and look at enough items to draw a fair conclusion:"),
        ("table", ["Population in the period", "Minimum sample", "Example"], [
            ("1–5", "All", "AI Release Review decisions this half-year"),
            ("6–50", "5, or 25% if higher", "New joiners and contractors"),
            ("51–250", "10–15", "Access requests; pull requests to production"),
            ("More than 250", "20–25, including some chosen by risk", "Generated images checked by moderation"),
        ], [4.5, 4.5, 7.5]),
        ("h2", "7.3 Evidence"),
        ("p", "Each finding must rest on objective evidence that someone else could check: document ID and version, "
              "record ID, screenshot with date, or a named interview. Opinions and 'we usually' are not evidence. "
              "Keep the audit working papers with the report for at least 3 years."),
        ("h1", "8. Grading findings"),
        ("table", ["Grade", "Meaning", "Response expected"], [
            ("Major nonconformity", "A requirement is not met at all, or a failure is systemic or puts the system's "
             "ability to achieve its results in doubt (e.g. no risk assessment of a new AI system).",
             "Containment within 5 working days; corrective-action plan within 10; verification within 90 days."),
            ("Minor nonconformity", "A single or occasional failure to meet a requirement that does not undermine "
             "the system as a whole.", "Corrective-action plan within 15 working days; closure normally within 90 days."),
            ("Opportunity for improvement (OFI)", "Requirement is met, but there is a better or more reliable way.",
             "Owner decides and records whether to act, in the Improvement Register."),
            ("Positive observation", "Practice worth keeping or spreading.", "Shared in the report."),
        ], [3.8, 7.5, 5.2]),
        ("h1", "9. Reporting"),
        ("bullets", [
            "Closing meeting on the last day: findings read out and facts agreed. Disagreements are recorded, not hidden.",
            "Written report within 10 working days to the auditees and the Trust Council, using section 12.",
            "Every nonconformity is entered in " + ref("IMS-REG-008") + " with the next NC number; OFIs go to the "
            "Improvement Register.",
            "Audit results are an input to management review (" + ref("IMS-PRO-008") + ").",
        ]),
        ("h1", "10. Follow-up"),
        ("p", f"The auditee proposes correction and corrective action under {ref('IMS-PRO-009')}. The coordinator "
              "tracks due dates. A nonconformity is closed only after someone independent of the action checks it "
              "worked — usually at the next audit or a short follow-up review."),
        ("pagebreak",),
        ("h1", f"11. Example report — {A['id']}"),
        ("table", ["Field", "Detail"], [
            ("Audit ID", A["id"]),
            ("Dates", A["dates"]),
            ("Auditor(s)", A["auditor"]),
            ("Scope", A["scope"]),
            ("Criteria", "ISO/IEC 27001:2022 Clauses 4–10 and applicable Annex A controls; ISO/IEC 42001:2023 "
             "Clauses 4–10 and applicable Annex A controls; our own policies and procedures; customer and supplier "
             "contracts sampled."),
            ("Method", "Remote interviews with 11 people, screen-share walkthroughs, record sampling, one end-to-end "
             f"trace of a {STF} release and one of incident {SAMPLE_INCIDENT['id']}."),
            ("Previous audit", "AUD-2026-01 (May 2026, cross-audit of Clauses 4–6, risk and access control). "
             "NC-2026-001 verified closed during this audit."),
        ], [4, 12.5]),
        ("h2", "11.1 Summary and conclusion"),
        ("p", "The integrated management system is established and largely effective. Leadership is visibly engaged "
              "through the Trust Council; risk and impact assessment are done before AI releases; incidents are "
              "handled well. Two minor nonconformities and one opportunity for improvement were found. No major "
              "nonconformities. Subject to closing the minor findings, the system is on track for a certification "
              "stage 1 audit in 2027."),
        ("h2", "11.2 Positive observations"),
        ("bullets", [
            "All AI releases in the period (3 of 3) had an approved impact assessment and AI Release Review record.",
            f"Incident {SAMPLE_INCIDENT['id']} was detected by our own canary testing, contained the same morning and "
            "documented with a clear notification decision.",
            "Quarterly backup restore tests completed on time with checksum evidence.",
        ]),
        ("h2", "11.3 Findings"),
        ("table", ["ID", "Grade", "Requirement", "Finding"], [f for f in F], [2.7, 3.2, 3.6, 7]),
        ("h3", f"{F[0][0]} — {F[0][1]}"),
        ("p", f"**Requirement:** {F[0][2]} — manage AI suppliers and changes in supplier services so that "
              "responsible-AI and security requirements stay met."),
        ("p", f"**Evidence:** {SFR} vendor agreement (signed 2025-11) has no clause on notice of model changes. "
              "Change log shows the vendor's 2026-08-12 model update went live without any assessment. This led to "
              f"{SAMPLE_INCIDENT['id']}. The supplier policy ({ref('IMS-POL-006')}) requires change assessment, but "
              "the change-management trigger list does not include supplier model updates."),
        ("p", f"**Finding:** {F[0][3]}"),
        ("h3", f"{F[1][0]} — {F[1][1]}"),
        ("p", f"**Requirement:** {F[1][2]} — people must be competent and aware, and our own rule is awareness "
              "training within 30 days of joining (OBJ-05)."),
        ("p", "**Evidence:** sampled 6 of 9 people who joined June–August. Two contractors who started on 2026-07-07 "
              "and 2026-07-14 had not completed training by day 30; one completed on day 53, one had not completed "
              "by the audit date. Both were onboarded by their hiring managers outside the People Ops checklist."),
        ("p", f"**Finding:** {F[1][3]}"),
        ("h3", f"{F[2][0]} — {F[2][1]}"),
        ("p", f"**Area:** {F[2][2]}. **Observation:** {F[2][3]} In July the exposure ratio dipped to 0.76 for nine "
              "days before the monthly review spotted it. An automatic alert below 0.8 would shorten detection."),
        ("h2", "11.4 Follow-up"),
        ("table", ["Finding", "Corrective action", "Owner", "Due"], [
            (CA[F[0][0]][1], CA[F[0][0]][0], person(CA[F[0][0]][3]), CA[F[0][0]][4]),
            (CA[F[1][0]][1], CA[F[1][0]][0], person(CA[F[1][0]][3]), CA[F[1][0]][4]),
            (F[2][0], "Improvement Register entry; owner decision", person("CAIO"), "2026-12-15"),
        ], [3.5, 5.5, 4, 3.5]),
        ("p", f"Distribution: Trust Council; auditees. Verification of closure is planned in the next cross-audit "
              f"(February 2027). Report issued 2026-09-30 by the contracted auditor; coordinated by {person('IMSC')}."),
        ("pagebreak",),
        ("h1", "12. Blank report template"),
        ("table", ["Field", "Detail"], [
            ("Audit ID", "[[AUD-YYYY-NN]]"), ("Dates", "[[start]] to [[end]]"),
            ("Auditor(s) and independence statement", "[[names; confirm no audit of own work]]"),
            ("Scope", "[[clauses, controls, processes, AI systems, sites]]"),
            ("Criteria", "[[standards, procedures, contracts, laws]]"),
            ("Method and sample", "[[interviews, records sampled and how chosen]]"),
            ("Previous findings checked", "[[NC IDs and status]]"),
        ], [5, 11.5]),
        ("p", "**Summary and conclusion:** [[is the system conforming and effective? major risks?]]"),
        ("p", "**Positive observations:** [[practices worth keeping]]"),
        ("table", ["ID", "Grade", "Requirement (27001 / 42001)", "Evidence", "Finding"], [
            ("[[NC-YYYY-NNN]]", "[[Major / Minor / OFI]]", "[[clause or control]]", "[[objective evidence]]",
             "[[what is not met]]"),
        ], [2.7, 2.5, 3.3, 4, 4]),
        ("table", ["Finding", "Corrective action ID", "Owner", "Due", "Verified by / date"], [
            ("[[NC ID]]", "[[CA-YYYY-NNN]]", "[[owner]]", "[[date]]", "[[name, date]]"),
        ], [3, 3.5, 3.5, 3, 3.5]),
        ("p", "**Signed:** [[lead auditor]], [[date]]. **Received for the Trust Council:** [[name]], [[date]]."),
        ("h1", "13. Records"),
        ("bullets", ["Audit programme and checklists (" + ref("IMS-REG-007") + ").",
                     "Audit plans, working papers, evidence and reports — kept at least 3 years.",
                     "Nonconformities and corrective actions (" + ref("IMS-REG-008") + ")."]),
        ("h1", "14. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-MAN-001", "IMS-REG-007", "IMS-PRO-008", "IMS-PRO-009", "IMS-REG-008")]),
    ],
}
