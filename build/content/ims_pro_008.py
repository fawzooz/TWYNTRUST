from org import (AI_SYSTEMS, KEY_RISKS, OBJECTIVES, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, level_for,
                 person, ref, title_of, who)

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
RISK = {r[0]: r for r in KEY_RISKS}
OBJ = {o[0]: o for o in OBJECTIVES}
A = SAMPLE_AUDIT
F = A["findings"]
CA4, CA5 = SAMPLE_CAPA
INC = SAMPLE_INCIDENT
R5 = RISK["RSK-AI-005"]
R5_RES = R5[6] * R5[7]
MR_DATE = "2026-10-21"


def risk_line(rid):
    r = RISK[rid]
    return (r[0], r[1], person(r[3]), f"{r[4] * r[5]} {level_for(r[4] * r[5])}", f"{r[6] * r[7]} {level_for(r[6] * r[7])}")


# objective id -> (result to end September 2026, status)
OBJ_RESULT = {
    "OBJ-01": ("Pre-certification audit planned June 2027; certification body selected", "On track"),
    "OBJ-02": ("3 of 3 AI releases with approved impact assessment and gate record (100%)", "Met"),
    "OBJ-03": ("100% of fine-tuning images verified; one opt-out took 17 days (INC-2026-009)", "Not met"),
    "OBJ-04": ("Critical median 4 days; high median 34 days", "Not met (high)"),
    "OBJ-05": ("Training 94% on time (two contractors late, NC-2026-004); phishing report rate 63%", "Partial"),
    "OBJ-06": ("Jun 0.83, Jul 0.79, Aug 0.84, Sep 0.86", "Not met (July)"),
    "OBJ-07": ("Lowest month 99.6% (June); average 99.8%", "Met"),
}

DOC = {
    "id": "IMS-PRO-008",
    "summary": f"How top management at {N} reviews the integrated management system twice a year through the Trust "
               "Council: the inputs both standards require, the decisions it must produce, how to prepare, and full "
               f"example minutes of the October 2026 review.",
    "clauses": {"27001": "9.3.1, 9.3.2, 9.3.3; 5.1; 10.1", "42001": "9.3.1, 9.3.2, 9.3.3; 5.1; 10.1"},
    "howto": [
        "Do not hold a separate management review for each standard. One meeting, one pack, one set of minutes — "
        "with the AI-specific inputs added as their own agenda items.",
        "Auditors read the minutes to see that each required input was discussed and that decisions were made. "
        "Write decisions as decisions ('approved', 'accepted until', 'rejected'), not as 'discussed'.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", "Management review is when the people who run the company step back and ask: is our system for "
              "security and responsible AI still right for us, is it enough, and is it working? They look at the "
              "evidence, decide what to change, and commit the resources to do it."),
        ("h1", "2. Scope and cadence"),
        ("bullets", [
            "Covers the whole integrated management system — both standards — in one review.",
            "Held **twice a year**, in April and October, as an extended meeting (about 90 minutes) of the Trust "
            "Council. The monthly Trust Council meetings handle day-to-day decisions in between.",
            "An extra review is called after a critical (S1) incident, a major audit nonconformity, a significant "
            "change of scope, or a new AI system with high impact.",
        ]),
        ("std", [
            "Both standards expect top management to review the management system at planned intervals to make sure "
            "it remains suitable, adequate and effective (9.3.1).",
            "They list inputs that must be considered (9.3.2): status of actions from earlier reviews; changes in "
            "external and internal issues; changes in the needs and expectations of interested parties; feedback on "
            "performance — nonconformities and corrective actions, monitoring and measurement results, audit "
            "results and (for ISO/IEC 27001) fulfilment of objectives; and opportunities for continual "
            "improvement. ISO/IEC 27001 also asks for risk assessment results and the risk treatment plan, and "
            "feedback from interested parties.",
            "ISO/IEC 42001 adds AI-specific matters that management needs to see in practice: how AI systems perform, "
            "the results of AI system impact assessments, risks, and information from interested parties about AI. "
            "We include all of these.",
            "Outputs must include decisions on improvement opportunities and any need to change the system, and the "
            "results must be kept as documented information (9.3.3).",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Who", "Responsibility"], [
            ("Chair", who("CEO"), "Chairs the review; ensures decisions and resources."),
            ("Members", f"{title_of('CTO')}, {title_of('CISO')}, {title_of('CAIO')}, {title_of('DPO')}, "
             f"{title_of('CREA')}", "Present their inputs; take decisions; own actions."),
            ("Secretary", who("IMSC"), "Prepares the pack, takes minutes, tracks actions."),
            ("Invited as needed", "Process owners; Artist Advisory Panel representative",
             "Present specific topics; bring outside perspective on AI impacts."),
        ], [3, 6, 7.5]),
        ("h1", "4. Inputs"),
        ("table", ["Input", "Source", "Presented by"], [
            ("Status of actions from previous reviews", "Previous minutes; action tracker", title_of("IMSC")),
            ("Changes in external and internal issues", ref("IMS-REG-001"), title_of("CEO")),
            ("Changes in interested parties' needs and expectations, incl. about AI", ref("IMS-REG-001") +
             "; customer, artist and regulator feedback", title_of("DPO")),
            ("Nonconformities and corrective actions", ref("IMS-REG-008"), title_of("IMSC")),
            ("Monitoring and measurement results; fulfilment of objectives", ref("IMS-REG-003"), title_of("IMSC")),
            ("Audit results", ref("IMS-REG-007") + "; audit reports", title_of("IMSC")),
            ("Risk assessment results and treatment plan status", ref("IMS-REG-002"), title_of("CISO")),
            ("AI system performance (accuracy, fairness, content safety, drift)", "Monitoring dashboards",
             title_of("CAIO")),
            ("AI system impact assessment results", ref("IMS-PRO-002") + " records", title_of("CAIO")),
            ("Incidents and lessons learned", ref("IMS-REG-006"), title_of("CISO")),
            ("Opportunities for continual improvement", "Improvement Register in " + ref("IMS-REG-008"),
             title_of("IMSC")),
            ("Adequacy of resources", "Budget, hiring plan", title_of("CEO")),
        ], [6.5, 6, 4]),
        ("h1", "5. Outputs"),
        ("bullets", [
            "A conclusion on whether the system is suitable, adequate and effective.",
            "Decisions on improvement opportunities and on changes to the system (policy, scope, objectives, "
            "controls, risk acceptance, Statements of Applicability).",
            "Resource decisions — people, budget, tools.",
            "Actions with owners and due dates, tracked by the secretary until closed.",
        ]),
        ("h1", "6. Preparing and running the review"),
        ("steps", [
            "Four weeks before: the secretary asks each input owner for a one-page update using the input table.",
            "Five working days before: the pack (no more than 15 pages, dashboard first) goes to members.",
            "In the meeting: walk the agenda in the order of section 4; record a short discussion and an explicit "
            "decision under each item.",
            "Within 5 working days: minutes approved by the chair and filed; actions entered in the tracker.",
            "Next monthly Trust Council: first check of action progress.",
        ]),
        ("tip", "Lead with a one-page dashboard: objectives (red/amber/green), open NCs, incident count by severity, "
                "top risks. Busy founders engage with a picture of the system before the detail."),
        ("pagebreak",),
        ("h1", "7. Example minutes — management review October 2026"),
        ("table", ["Field", "Detail"], [
            ("Meeting", f"Trust Council — management review MR-2026-02 (ISO/IEC 27001 and ISO/IEC 42001)"),
            ("Date and time", f"{MR_DATE}, 14:00–15:40 (Dubai time), video call"),
            ("Chair", who("CEO")),
            ("Members present", ", ".join(who(k) for k in ("CTO", "CISO", "CAIO", "DPO", "CREA"))),
            ("In attendance", f"{who('IMSC')} (secretary); {who('SRE')} (item 4); {who('HOP')} (item 3)"),
            ("Apologies", "None. Quorum met."),
            ("Pack", f"Circulated 2026-10-14: dashboard, {A['id']} report, objectives status, risk register extract, "
             "incident summary, draft Statements of Applicability."),
        ], [3.5, 13]),
        ("h2", "Item 1 — Actions from the previous review (MR-2026-01, April 2026)"),
        ("table", ["Action", "Owner", "Status"], [
            (f"Implement fairness monitoring for {ARM}", person("CAIO"), "Closed (CA-2026-002)"),
            ("Contract an independent auditor for a full-system audit", person("IMSC"), f"Closed ({A['id']} held)"),
            ("Risk-assess the UAE region launch", person("SRE"), "Closed"),
            ("Run quarterly phishing simulations", person("HOP"), "Closed; continuing"),
        ], [9, 4, 3.5]),
        ("h2", "Item 2 — Changes in issues and interested parties"),
        ("bullets", [
            "**External:** EU AI Act transparency duties for AI-generated content and deepfakes apply from August "
            "2026; our labelling and content credentials already meet them. Two new enterprise agencies in Saudi "
            "Arabia require ISO/IEC 27001 in contracts.",
            "**Internal:** headcount grew from 28 to 34; five contractors added. Dependence on AI suppliers is now a "
            "top issue after " + INC["id"] + ".",
            "**Interested parties about AI:** one enterprise customer now asks for notice of any model change "
            "affecting their outputs; the Artist Advisory Panel asked for a public explanation of how " + ARM +
            " ranks artists; 12 artists complained in May about low visibility (INC-2026-005).",
        ]),
        ("p", f"**Decision:** context and interested-party register to be updated with these changes ({person('IMSC')}, "
              "by 2026-11-15). Publish a plain-language " + ARM + " ranking explanation (see actions)."),
        ("h2", "Item 3 — Performance: objectives and monitoring"),
        ("table", ["Objective", "Target", "Result to end Sept 2026", "Status"],
         [(f"{o[0]} {o[1]}", o[3], OBJ_RESULT[o[0]][0], OBJ_RESULT[o[0]][1]) for o in OBJECTIVES],
         [4.5, 4, 5.8, 2.2]),
        ("p", "**Discussion:** OBJ-05 and OBJ-03 misses share a cause — processes that depend on one person's inbox "
              "or on hiring managers rather than a system. OBJ-04: high-severity fixes are slowed by one legacy "
              "image-processing library."),
        ("p", "**Decision:** targets unchanged. CTO to replace the legacy library by Q1 2027. The October phishing "
              "report rate counts towards OBJ-05 from now on as a quarterly measure."),
        ("h2", "Item 4 — Audit results, nonconformities and corrective actions"),
        ("p", f"{A['id']} ({A['dates']}; {A['auditor']}) found no major nonconformities. Findings:"),
        ("table", ["ID", "Grade", "Requirement", "Finding"], list(F), [2.7, 3.2, 3.6, 7]),
        ("table", ["NC", "Corrective action", "Owner", "Due", "Status"], [
            ("NC-2026-001", "CA-2026-001", person("CISO"), "2026-07-31", "Closed, effective"),
            ("NC-2026-002", "CA-2026-002, CA-2026-003", person("CAIO"), "2026-07-31",
             "Closed; CA-2026-002 partially effective → OFI-2026-05"),
            (CA4[1], CA4[0], person(CA4[3]), CA4[4], "In progress — clause agreed with vendor, signature pending"),
            (CA5[1], CA5[0], person(CA5[3]), CA5[4], "In progress — checklist live, reminder automation in test"),
        ], [2.7, 4, 3.3, 2.3, 4.2]),
        ("p", "**Decision:** corrective-action plans accepted. Audit programme for November 2026 to September 2027 "
              f"({ref('IMS-REG-007')}) approved."),
        ("h2", "Item 5 — AI system performance and impact assessments"),
        ("table", ["AI system", "Performance summary", "Impact assessment"], [
            (STF, "Content-safety canary pass rate 97–99% since August; 0 prohibited outputs delivered; label and "
             "credential coverage 100%.", "Re-assessed after " + INC["id"] + "; likeness harm rated Major; new "
             "likeness check added."),
            (SCM, "Hallucination rate on evaluation set 1.8% (target ≤ 3%); no cross-customer leakage found in "
             "quarterly test.", "No change; next review March 2027."),
            (ARM, "Exposure ratio new vs established 0.79–0.86; non-English portfolios at parity.",
             "Updated June 2026 after INC-2026-005; transparency notice to be published."),
            (SFR, "Pinned to previous version; vendor notice clause pending (CA-2026-004).",
             "Supplier-side risk remains the main driver of " + R5[0] + "."),
            (CDA, "Business plan, no training on our code; secret-leak alerts 1 (INC-2026-008 was not from this tool).",
             "Not required (internal use, low impact)."),
        ], [2.8, 7.4, 6.3]),
        ("h2", "Item 6 — Incidents"),
        ("p", "Ten incidents and events logged in 2026 to date: one S2, six S3, three S4; no S1; no regulator "
              f"notification required. {INC['id']} ({INC['title']}) was discussed in detail: detected by our own "
              "canary, contained the same morning, customer informed the same day. Lessons are being implemented "
              f"through {CA4[0]} and IMP-2026-05 (second moderation vendor evaluation)."),
        ("h2", "Item 7 — Risks, risk treatment and Statements of Applicability"),
        ("table", ["Risk", "Title", "Owner", "Inherent", "Residual"],
         [risk_line(r) for r in ("RSK-AI-005", "RSK-AI-001", "RSK-AI-002", "RSK-IS-002", "RSK-IS-004")],
         [2.4, 7.4, 2.8, 2, 2]),
        ("p", f"**{R5[0]}:** residual score {R5[6]}×{R5[7]} = {R5_RES} ({level_for(R5_RES)}) remains above our "
              f"Medium threshold because impact stays at {R5[7]} until the vendor is contractually bound to notify "
              f"model changes. {person(R5[3])} (risk owner) and {person('CAIO')} proposed time-limited acceptance."),
        ("p", f"**Decision:** the Trust Council **accepts the residual High risk {R5[0]} until 2027-01-31**, pending "
              f"completion and effectiveness check of {CA4[0]}, on three conditions: daily canary testing continues; "
              f"our own likeness check stays in front of image delivery; any canary drop greater than 3 points "
              f"triggers the {SFR} fail-closed switch. If {CA4[0]} is not effective by 2027-01-31, the acceptance "
              "lapses and the Council will decide on a second-vendor architecture."),
        ("p", f"**Decision:** the Statements of Applicability ({ref('IMS-SOA-001')} and {ref('IMS-SOA-002')}) are "
              f"**approved** as presented on {MR_DATE}, including the added supplier model-change control "
              "description."),
        ("h2", "Item 8 — Opportunities for improvement and resources"),
        ("bullets", [
            "OFI-2026-05 (automatic fairness alerting) adopted; due 2026-12-15.",
            "IMP-2026-05: budget of [[USD amount]] approved to evaluate a second moderation vendor in parallel.",
            "OFI-2026-04 (standard supplier questionnaire) deferred to Q1 2027.",
            "Resources: approve 0.5 FTE compliance support from January 2027 for certification preparation.",
        ]),
        ("h2", "Conclusion"),
        ("p", "The Trust Council concluded that the integrated management system is **suitable** for our business "
              "and AI activities, **adequate** with the corrective actions above, and **effective**: incidents were "
              "detected and handled well, the first full audit found no major nonconformities, and most objectives "
              "are met or on track. Supplier AI governance is the main area to strengthen."),
        ("h2", "Actions"),
        ("table", ["Ref", "Action", "Owner", "Due"], [
            ("MR-2026-02-A1", "Update context and interested-party register with item 2 changes", person("IMSC"),
             "2026-11-15"),
            ("MR-2026-02-A2", f"Publish plain-language explanation of how {ARM} ranks artists", person("CAIO"),
             "2026-12-31"),
            ("MR-2026-02-A3", f"Complete {CA4[0]} and report effectiveness to the Trust Council", person(CA4[3]),
             "2027-01-31"),
            ("MR-2026-02-A4", f"Re-decide acceptance of {R5[0]} at the January Trust Council", person("CEO"),
             "2027-01-31"),
            ("MR-2026-02-A5", "Replace legacy image-processing library (OBJ-04)", person("CTO"), "2027-03-31"),
            ("MR-2026-02-A6", "Run second-vendor moderation evaluation (IMP-2026-05)", person("CREA"), "2027-01-31"),
            ("MR-2026-02-A7", "Recruit 0.5 FTE compliance support", person("HOP"), "2027-01-15"),
        ], [3.2, 8.3, 3, 2]),
        ("p", f"Next management review: April 2027. Minutes approved by {person('CEO')}, [[date]]."),
        ("h1", "8. Records"),
        ("bullets", ["Review pack and approved minutes, kept for at least 3 years.",
                     "Action tracker; risk acceptance decisions copied to " + ref("IMS-REG-002") + "."]),
        ("h1", "9. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-GOV-001", "IMS-REG-003", "IMS-REG-002", "IMS-PRO-007", "IMS-PRO-009",
                                      "IMS-REG-006", "IMS-REG-008")]),
    ],
}
