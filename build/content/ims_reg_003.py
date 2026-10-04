from datetime import date

from org import who, AI_SYSTEMS, COMMITTEES, OBJECTIVES, ORG, person, ref, title_of

N = ORG["name"]
SYS = {s["id"]: s for s in AI_SYSTEMS}
SF, SM, AM, SAFE = (SYS[i]["name"] for i in ("AI-SYS-001", "AI-SYS-002", "AI-SYS-003", "AI-SYS-004"))
TC, ARR = list(COMMITTEES)[:2]


def owner(key):
    return who(key)


# Plan for each shared objective: standard link, what, resources, when, how evaluated, current value, status
PLAN = {
    "OBJ-01": ("Both", "Finish Stage 1 and Stage 2 audits for both standards with one certification body; close "
               "all audit nonconformities on time", "Certification fee budget; 0.5 FTE Compliance Coordinator; "
               "external internal-audit support", "Stage 1 2027-05; Stage 2 2027-07; certificates by 2027-09-30",
               f"Milestones tracked monthly at the {TC}", "AUD-2026-02 done; 2 minor NCs open", "On track"),
    "OBJ-02": ("42001", f"Every new or significantly changed AI system gets an AIIA and a {ARR} record before "
               "release", f"{ARR} members' time (≈ 4 h per release); AIIA template", "Continuous; reported monthly",
               "Release log checked against AIIA register each month; sampled in internal audit",
               "100% (3 of 3 AI releases in 2026)", "Met"),
    "OBJ-03": ("42001", "Image-by-image consent audit of the fine-tuning set; automatic opt-out propagation",
               "2 weeks of Data/ML engineering; consent ledger tooling", "Audit 2026-09-30; automation 2026-12-15",
               "Monthly data-provenance report; opt-out age report", "100% of the current set verified (41 unverified images removed); one opt-out took 17 days (INC-2026-009)",
               "Not met"),
    "OBJ-04": ("27001", "CI blocks builds with critical vulnerabilities older than 7 days; weekly triage",
               "Dependency scanner (existing); 2 h/week engineering triage", "From 2026-10-15",
               "Vulnerability age report from the scanner, monthly", "Critical median 4 days; high median 34 days",
               "Not met"),
    "OBJ-05": ("Both", "Combined security + AI awareness module at onboarding and yearly; quarterly phishing "
               "simulation; contractor onboarding through People Ops (CA-2026-005)",
               "Training platform licence; 1 h per person per year", "Ongoing; contractor fix by 2026-10-31",
               "Training platform completion report; phishing simulation report rate", "94% trained; report rate 63%",
               "In progress"),
    "OBJ-06": ("42001", f"Exposure-boost slot for new artists; automatic alert when the {AM} ratio drops below 0.8",
               "1 sprint of ML engineering; monitoring dashboard", "Alert live by 2026-11-30",
               "Monthly fairness report reviewed by the Head of AI", "Jun 0.83, Jul 0.79, Aug 0.84, Sep 0.86 (July below target)", "Not met"),
    "OBJ-07": ("27001", "Multi-AZ everywhere; quarterly restore test; tested regional failover runbook",
               "Cloud budget +8%; SRE time", "Failover test 2026-12", "Uptime monitor, monthly",
               "Lowest month 99.6% (June); average 99.8%", "Met"),
}

OBJ_ROWS = []
for oid, obj, metric, tgt, own in OBJECTIVES:
    std, what, res, when, how, val, st = PLAN[oid]
    OBJ_ROWS.append([oid, obj, std, metric, tgt, what, res, owner(own), when, how, val, st])
OBJ_ROWS.append(["[[OBJ-0x]]", "[[what you want to achieve]]", "[[27001 / 42001 / Both]]", "[[how you measure it]]",
                 "[[target and date]]", "[[actions]]", "[[budget, people, tools]]", "[[owner]]", "[[when]]",
                 "[[how and how often you check]]", "", "Not started"])

METRICS = [
    # id, type, std, metric, link, source, freq, threshold, owner, last value, measured, status
    ("M-01", "KPI", "42001", "AI releases with approved AIIA and release-review record", "OBJ-02",
     "Release log + AIIA register", "Monthly", "100%", "CAIO", "100%", "Met"),
    ("M-02", "KPI", "42001", "Fine-tuning images with verified licence or consent", "OBJ-03; RSK-AI-001",
     "Consent ledger vs dataset manifest", "Monthly", "100%", "HOD", "100%", "Met"),
    ("M-03", "KRI", "42001", "Opt-out requests unresolved after 14 days", "OBJ-03", "Commons opt-out queue",
     "Weekly", "0", "HOD", "1 (17 days, INC-2026-009)", "Not met"),
    ("M-04", "KPI", "42001", f"{AM} exposure ratio, new vs established artists (top-10)", "OBJ-06; RSK-AI-003",
     "Ranking logs, fairness notebook", "Monthly", "≥ 0.8", "CAIO", "0.86 (Sep); 0.79 in Jul", "Not met"),
    ("M-05", "KRI", "42001", f"{AM} drift — population stability index of input features", "RSK-AI-008",
     "Monitoring dashboard", "Monthly", "< 0.2", "HOD", "0.12", "Met"),
    ("M-06", "KRI", "42001", f"{SAFE} detection rate on canary test set (prohibited + real-person likeness)",
     "RSK-AI-005; RSK-AI-002", "Canary test run", "Weekly (daily after a vendor change)", "≥ 98%", "CREA",
     "99.1%", "Met"),
    ("M-07", "KRI", "42001", f"{SF} deepfake red-team bypass rate", "RSK-AI-002", "Red-team report",
     "Quarterly", "0 of 200 attempts", "CAIO", "0 / 200", "Met"),
    ("M-08", "KPI", "42001", f"{SM} scene-list accuracy on reference scripts (no invented scenes)", "RSK-AI-004",
     "Evaluation suite in CI", "Each release + monthly", "≥ 95%", "HOD", "96.4%", "Met"),
    ("M-09", "KPI", "27001", "Median days to fix critical / high vulnerabilities in production", "OBJ-04; RSK-IS-005",
     "Dependency and container scanner", "Monthly", "Critical ≤ 7; high ≤ 30", "CTO", "4 / 34", "Not met"),
    ("M-10", "KPI", "Both", "Staff and contractors trained within 30 days of joining and yearly", "OBJ-05",
     "Training platform", "Monthly", "100%", "HOP", "94%", "Not met"),
    ("M-11", "KPI", "27001", "Phishing simulation report rate", "OBJ-05; RSK-IS-002", "Phishing simulation tool",
     "Quarterly", "≥ 60%", "HOP", "63%", "Met"),
    ("M-12", "KPI", "27001", "Accounts with phishing-resistant MFA", "RSK-IS-002", "Identity provider report",
     "Monthly", "100%", "CISO", "100%", "Met"),
    ("M-13", "KPI", "27001", "Canvas and API availability", "OBJ-07; RSK-IS-004", "Uptime monitor", "Monthly",
     "≥ 99.5%", "SRE", "99.71%", "Met"),
    ("M-14", "KPI", "27001", "Successful restore tests", "RSK-IS-004", "Restore test record", "Quarterly",
     "1 per quarter, RTO ≤ 8 h", "SRE", "1, 5.5 h", "Met"),
    ("M-15", "KPI", "Both", "Access reviews completed for production, GitHub and model registry",
     "RSK-IS-006", "Access review records", "Quarterly", "100% on time", "CISO", "2 of 3", "Not met"),
    ("M-16", "KRI", "Both", "Security and AI incidents rated S1/S2", "IMS-PRO-005", "Incident log",
     "Monthly", "0 S1; ≤ 1 S2 per quarter", "CISO", "1 S2 (INC-2026-007)", "Met"),
    ("M-17", "KPI", "Both", "Corrective actions closed by due date", "IMS-PRO-009", "CAPA log", "Monthly",
     "≥ 90%", "IMSC", "2 open, 0 overdue", "On track"),
    ("M-18", "KPI", "Both", "Critical suppliers (incl. AI model suppliers) reviewed in last 12 months",
     "RSK-AI-005", "Supplier register", "Quarterly", "100%", "DPO", "80%", "Not met"),
]
MEASURED = date(2026, 9, 30)
MET_ROWS = [[i, t, s, m, link, src, f, th, owner(o), v, MEASURED, st]
            for (i, t, s, m, link, src, f, th, o, v, st) in METRICS]
MET_ROWS.append(["[[M-xx]]", "[[KPI or KRI]]", "[[27001 / 42001 / Both]]", "[[what you count]]", "[[OBJ / RSK]]",
                 "[[system or report]]", "[[how often]]", "[[target or tolerance]]", "[[owner]]", "", "",
                 "Not started"])

CAL = [
    ("Weekly", "Canary safety test, opt-out queue, vulnerability triage", "M-03, M-06, M-09",
     "CREA", "Dashboards; triage notes", "Head of AI / CTO if threshold breached"),
    ("Monthly", "All monthly metrics collected and compared with thresholds", "Metrics sheet",
     "IMSC", "Updated Metrics sheet", TC),
    ("Monthly", f"{TC} meeting: top risks, metrics off target, incidents, actions", "Risk register; metrics",
     "CEO", "Minutes", TC),
    ("Monthly", f"{AM} fairness and drift review", "M-04, M-05", "CAIO", "Fairness report", ARR),
    ("Quarterly", "Risk register review by risk owners; treatment plan progress", "IMS-REG-002",
     "CISO", "Dated register copy", TC),
    ("Quarterly", "Access reviews; restore test; phishing simulation; red-team", "M-07, M-11, M-14, M-15",
     "CISO", "Review records; test reports", TC),
    ("Quarterly", "Supplier and AI model-supplier check (model changes, certificates, incidents)", "M-18",
     "DPO", "Supplier register", TC),
    ("Twice a year", "Management review (both standards)", "All of the above", "CEO", "Management review minutes",
     TC),
    ("Yearly", "Internal audit of the whole system", "Audit programme", "IMSC", "Audit report", TC),
    ("Yearly", "AIIA review of High-criticality AI systems", "IMS-PRO-002", "CAIO", "Updated AIIAs", ARR),
    ("Yearly", "Objectives reset; policy and scope review; SoA review", "Objectives sheet; SoAs", "IMSC",
     "Approved objectives and SoAs", TC),
    ("Yearly", "Awareness training refresh for all staff and contractors", "M-10", "HOP", "Training records", TC),
    ("Yearly", "Penetration test of Canvas, Commons and API", "RSK-IS-005, RSK-IS-009", "CTO", "Pentest report",
     TC),
]
CAL_ROWS = [[f, what, inp, owner(o), out, to, "", ""] for (f, what, inp, o, out, to) in CAL]
CAL_ROWS[0][6], CAL_ROWS[0][7] = "Weekly (Mondays)", "Planned"
CAL_ROWS[2][6], CAL_ROWS[2][7] = "2026-10-21", "Planned"
CAL_ROWS[7][6], CAL_ROWS[7][7] = "2026-11-18", "Planned"
CAL_ROWS[8][6], CAL_ROWS[8][7] = "AUD-2026-02 done 2026-09-19", "Done"
for row in CAL_ROWS:
    if not row[6]:
        row[6], row[7] = "[[next date]]", "Planned"

WB = {
    "id": "IMS-REG-003",
    "summary": f"{N}'s information-security and AI objectives with the plan to achieve them, the metrics used to "
               "monitor both management systems, and the calendar for measuring and reviewing them.",
    "clauses": {"27001": "6.2, 9.1; supports 9.3 inputs", "42001": "6.2, 9.1; Annex A.6.2.6 (operation and monitoring)"},
    "howto": [
        "Keep objectives few (5–8) and measurable. Each one needs a plan: what, resources, who, when, how evaluated.",
        "KPI = how well we are doing; KRI = an early warning that a risk is growing. Every High risk should have "
        "at least one KRI.",
        f"Update the 'Last value' column before each {TC} meeting.",
    ],
    "sheets": [
        {
            "name": "Objectives",
            "title": "Objectives and plans to achieve them",
            "intro": "Objectives set by the Trust Council for both standards, with the planning details both "
                     "standards ask for (what, resources, who, when, how results are evaluated).",
            "headers": ["ID", "Objective", "Standard", "Metric", "Target", "What will be done", "Resources",
                        "Owner", "When", "How evaluated", "Current value", "Status"],
            "rows": OBJ_ROWS,
            "widths": [8, 28, 9, 32, 26, 40, 28, 24, 24, 30, 22, 12],
            "lists": {"Standard": ["27001", "42001", "Both"],
                      "Status": ["Not started", "In progress", "On track", "Met", "Not met"]},
            "status": ["Status"],
            "freeze_cols": 2,
        },
        {
            "name": "Metrics",
            "title": "Metrics — KPIs and KRIs",
            "intro": "What we measure to know whether the integrated system and our AI systems work as intended, "
                     f"including AI performance, drift and fairness. Results feed the management review ({ref('IMS-PRO-008')}).",
            "headers": ["ID", "Type", "Standard", "Metric", "Linked objective / risk", "Source", "Frequency",
                        "Threshold / target", "Owner", "Last value", "Last measured", "Status"],
            "rows": MET_ROWS,
            "widths": [7, 7, 9, 40, 20, 26, 16, 20, 24, 16, 12, 11],
            "lists": {"Type": ["KPI", "KRI"], "Standard": ["27001", "42001", "Both"],
                      "Status": ["Not started", "On track", "Met", "Not met"]},
            "status": ["Status"],
            "freeze_cols": 1,
        },
        {
            "name": "Monitoring Calendar",
            "title": "Monitoring, measurement and review calendar",
            "intro": "When each thing is measured or reviewed, by whom, what record it produces and where the "
                     "result goes.",
            "headers": ["Frequency", "What is measured or reviewed", "Inputs", "Owner", "Output / record",
                        "Reported to", "Next due", "Status"],
            "rows": CAL_ROWS,
            "widths": [13, 48, 24, 24, 28, 18, 22, 11],
            "lists": {"Frequency": ["Weekly", "Monthly", "Quarterly", "Twice a year", "Yearly"],
                      "Status": ["Planned", "Done", "Overdue"]},
            "status": ["Status"],
        },
    ],
}
