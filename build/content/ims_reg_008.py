from datetime import date

from org import AI_SYSTEMS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR = (SYS[f"AI-SYS-00{i}"] for i in range(1, 5))
A = SAMPLE_AUDIT
F = {f[0]: f for f in A["findings"]}
CA4, CA5 = SAMPLE_CAPA
d = date.fromisoformat


def rc(capa):
    return capa[2].split(" Action: ")[0].replace("Root cause: ", "")


def act(capa):
    return capa[2].split(" Action: ")[1]


# Columns: A ID, B Record, C Linked NC, D Raised, E Source, F Grade, G Requirement, H Description, I Correction,
# J Root cause, K Corrective action, L Owner, M Due, N Status, O Due status (formula), P Closed, Q Effectiveness
DUE_F = ('=IF(N{r}="Closed","Closed",IF(M{r}="","",IF(TODAY()>M{r},"Overdue",'
         'IF(M{r}-TODAY()<=14,"Due soon","On track"))))')

LOG = [
    ("NC-2026-001", "Nonconformity", "", d("2026-05-21"), "Internal audit AUD-2026-01", "Minor nonconformity",
     "27001 5.18 / 9.1", "Quarterly access review of production cloud accounts was not performed for Q1 2026.",
     "Access review completed 2026-05-28; two stale roles removed.", "Access review was a calendar reminder for one "
     "person with no backup and no tracking.", "See CA-2026-001", person("CISO"), d("2026-07-31"), "Closed", DUE_F,
     d("2026-07-24"), "EC-01"),
    ("CA-2026-001", "Corrective action", "NC-2026-001", d("2026-05-28"), "", "", "", "",
     "", "", "Access reviews scheduled as recurring tickets in the compliance tracker, assigned to the Security Lead "
     "with the Platform Engineer as backup; overdue tickets reported to the Trust Council.", person("CISO"),
     d("2026-07-31"), "Closed", DUE_F, d("2026-07-24"), "EC-01"),
    ("NC-2026-002", "Nonconformity", "", d("2026-05-12"), "Incident INC-2026-005", "Minor nonconformity",
     "42001 9.1 / A.6.2.6", f"Fairness monitoring defined in the {ARM} impact assessment was not running after release; "
     "the exposure ratio for new artists fell to 0.55 unnoticed.", "Exploration boost re-enabled; ratio back to 0.83 "
     "by 2026-06-05.", "Release sign-off did not check that the monitoring promised in the impact assessment was live.",
     "See CA-2026-002, CA-2026-003", person("CAIO"), d("2026-07-31"), "Closed", DUE_F, d("2026-07-30"),
     "EC-02, EC-03"),
    ("CA-2026-002", "Corrective action", "NC-2026-002", d("2026-05-19"), "", "", "", "", "", "",
     f"Build a monthly {ARM} fairness report (exposure ratio, new vs established, by portfolio language) reviewed by "
     "the Head of AI.", person("CAIO"), d("2026-06-30"), "Closed", DUE_F, d("2026-06-26"), "EC-02"),
    ("CA-2026-003", "Corrective action", "NC-2026-002", d("2026-05-19"), "", "", "", "", "", "",
     "Add 'monitoring from the impact assessment is live and alerting' as a mandatory item in the AI Release Review "
     "checklist.", person("CAIO"), d("2026-07-31"), "Closed", DUE_F, d("2026-07-30"), "EC-03"),
    (F[CA4[1]][0], "Nonconformity", "", d("2026-09-19"), f"Internal audit {A['id']} (also {SAMPLE_INCIDENT['id']})",
     F[CA4[1]][1], F[CA4[1]][2], F[CA4[1]][3], f"{SFR} pinned to previous model version; own likeness check added "
     "(2026-08-17/18).", rc(CA4), f"See {CA4[0]}", person(CA4[3]), d(CA4[4]), "In progress", DUE_F, None, "EC-04"),
    (CA4[0], "Corrective action", CA4[1], d("2026-10-02"), "", "", "", "", "", rc(CA4), act(CA4), person(CA4[3]),
     d(CA4[4]), "In progress", DUE_F, None, "EC-04"),
    (F[CA5[1]][0], "Nonconformity", "", d("2026-09-19"), f"Internal audit {A['id']}", F[CA5[1]][1], F[CA5[1]][2],
     F[CA5[1]][3], "Both contractors enrolled; training completed 2026-09-24.", rc(CA5), f"See {CA5[0]}",
     person(CA5[3]), d(CA5[4]), "In progress", DUE_F, None, "EC-05"),
    (CA5[0], "Corrective action", CA5[1], d("2026-10-01"), "", "", "", "", "", rc(CA5), act(CA5), person(CA5[3]),
     d(CA5[4]), "In progress", DUE_F, None, "EC-05"),
    ("[[NC-YYYY-NNN]]", "Nonconformity", "", "[[date]]", "[[source]]", "[[grade]]", "[[27001 / 42001 ref]]",
     "[[what was not met, with evidence]]", "[[immediate fix]]", "[[root cause]]", "[[CA ID]]", "[[owner]]", "",
     "Open", DUE_F, "", ""),
]

IMPROVE = [
    ("OFI-2026-01", d("2026-05-21"), "Audit AUD-2026-01", "Link risks to assets automatically by asset ID instead "
     "of free text.", "Faster risk review after asset changes", "27001 6.1.2 / 42001 6.1.2", person("CISO"),
     "Adopt", d("2026-08-31"), "Done", "Asset ID column with drop-down added to the risk register."),
    ("OFI-2026-02", d("2026-05-21"), "Audit AUD-2026-01", "Collect policy acknowledgements in the HR system rather "
     "than a spreadsheet.", "Reliable evidence for awareness", "27001 7.3 / 42001 7.3", person("HOP"), "Adopt",
     d("2026-09-30"), "Done", "Live since September onboarding."),
    ("OFI-2026-03", d("2026-05-21"), "Audit AUD-2026-01", "Give the AI Release Review template a fixed fairness and "
     "content-safety section.", "Consistent release decisions", "42001 A.6.2.4, A.6.2.5", person("CAIO"), "Adopt",
     d("2026-07-31"), "Done", "Merged with CA-2026-003."),
    ("OFI-2026-04", d("2026-05-21"), "Audit AUD-2026-01", "Reuse a standard supplier security questionnaire.",
     "Less effort per supplier", "27001 5.19–5.21", person("DPO"), "Defer", d("2027-03-31"), "Not started",
     "Deferred until supplier contract template is updated (CA-2026-004)."),
    (F["OFI-2026-05"][0], d("2026-09-19"), f"Audit {A['id']}", F["OFI-2026-05"][3],
     "Detect fairness drift within days, not weeks", F["OFI-2026-05"][2], person("CAIO"), "Adopt", d("2026-12-15"),
     "In progress", "Daily metric with alert below 0.8 to #trust-report; also supports OBJ-06."),
    ("IMP-2026-01", d("2026-06-18"), "Tabletop BC-TT-2026-02", "Two-person rule for DNS failover written into the "
     "runbook.", "Avoid false or missed failover", "27001 5.30", person("SRE"), "Adopt", d("2026-07-15"), "Done", ""),
    ("IMP-2026-02", d("2026-06-18"), "Tabletop BC-TT-2026-02", "Status page reachable through a break-glass account "
     "when single sign-on is down.", "Customer communication during outage", "27001 5.29, 5.30", person("SRE"),
     "Adopt", d("2026-07-15"), "Done", ""),
    ("IMP-2026-03", d("2026-06-18"), "Tabletop BC-TT-2026-02", f"Test the {SCM} alternative model provider twice a "
     "year.", "Proven AI fallback", "27001 5.30 / 42001 A.4.5", person("CAIO"), "Adopt", d("2026-08-31"), "Done",
     "First switch test 2026-08-20: 40 minutes, evaluation set passed."),
    ("IMP-2026-04", d("2026-09-25"), "Incident INC-2026-009", "Single opt-out form feeding the consent ledger with an "
     "ageing alert at day 7.", "Meets OBJ-03 14-day target reliably", "42001 A.7.3, A.7.5", person("HOD"), "Adopt",
     d("2026-10-31"), "In progress", ""),
    ("IMP-2026-05", d("2026-08-26"), f"Incident {SAMPLE_INCIDENT['id']} review", f"Evaluate a second moderation vendor "
     f"to run in parallel with {SFR} on a sample of traffic.", "Independent check on a critical AI supplier",
     "42001 A.10.3 / 27001 5.22", person("CREA"), "Adopt", d("2027-01-31"), "In progress", "Linked to RSK-AI-005."),
    ("[[IMP-YYYY-NN]]", "[[date]]", "[[source]]", "[[idea]]", "[[benefit]]", "[[clause / control]]", "[[owner]]",
     "[[decision]]", "[[due]]", "Not started", ""),
]

EFFECT = [
    ("EC-01", "CA-2026-001", "NC-2026-001", "Q2 access review done on time with evidence; Q3 review raised on schedule",
     d("2026-09-17"), d("2026-09-17"), f"Contracted auditor ({A['id']})", "Effective",
     "Q2 ticket closed 2026-07-08 with export of reviewed roles; Q3 ticket opened automatically 2026-09-15.", "Close NC-2026-001"),
    ("EC-02", "CA-2026-002", "NC-2026-002", "Monthly fairness report produced June–September and acted on",
     d("2026-09-17"), d("2026-09-17"), f"Contracted auditor ({A['id']})", "Partially effective",
     "Reports produced every month, but the July dip to 0.76 lasted 9 days before review.",
     "Raised OFI-2026-05 (automatic alert)"),
    ("EC-03", "CA-2026-003", "NC-2026-002", "Release checklist item used for every AI release since July",
     d("2026-09-17"), d("2026-09-17"), f"Contracted auditor ({A['id']})", "Effective",
     "2 of 2 releases since July show the monitoring item ticked with dashboard link.", "Close NC-2026-002"),
    ("EC-04", CA4[0], CA4[1], f"Clause signed with {SFR} and foundation-model supplier; at least one vendor model "
     "change notified and assessed before going live", d("2027-01-31"), None, person("CAIO"), "Pending", "",
     "Trust Council review of RSK-AI-005 acceptance on result"),
    ("EC-05", CA5[0], CA5[1], "All contractors joining Nov–Dec 2026 complete training within 30 days",
     d("2026-12-15"), None, "Contracted auditor (AUD-2026-04)", "Pending", "", ""),
    ("[[EC-NN]]", "[[CA ID]]", "[[NC ID]]", "[[what evidence will show it worked]]", "[[date]]", "", "[[verifier]]",
     "Pending", "", ""),
]

WB = {
    "id": "IMS-REG-008",
    "summary": f"{N}'s single log of nonconformities and corrective actions for both standards, the continual "
               f"improvement register, and the record of effectiveness checks. Used with {ref('IMS-PRO-009')}.",
    "clauses": {"27001": "10.1, 10.2", "42001": "10.1, 10.2"},
    "howto": [
        "Put each nonconformity on its own row and each corrective action on a row below it, linked by 'Linked NC'. "
        "One NC can have several actions.",
        "'Due status' is a formula using TODAY(): it shows On track, Due soon (14 days or less), Overdue or Closed. "
        "Only change the 'Status' column by hand.",
    ],
    "sheets": [
        {"name": "NC & CA Log", "title": "Nonconformity and corrective action log",
         "intro": "Sources: audits, incidents, monitoring, management review, complaints, self-reporting. Status is "
                  "set by hand; Due status calculates automatically.",
         "headers": ["ID", "Record type", "Linked NC", "Date raised", "Source", "Grade", "Requirement (27001 / 42001)",
                     "Description and evidence", "Correction (immediate fix)", "Root cause", "Corrective action",
                     "Owner", "Due date", "Status", "Due status", "Date closed", "Effectiveness check"],
         "rows": LOG,
         "formulas": {"Due status": DUE_F},
         "widths": [13, 15, 12, 11, 22, 18, 18, 42, 32, 38, 48, 15, 11, 11, 11, 11, 12],
         "lists": {"Record type": ["Nonconformity", "Corrective action"],
                   "Grade": ["Major nonconformity", "Minor nonconformity"],
                   "Status": ["Open", "In progress", "Closed"]},
         "status": ["Status", "Due status"]},
        {"name": "Improvement Register", "title": "Continual improvement register",
         "intro": "Opportunities for improvement (OFI) from audits and other improvement ideas (IMP) from incidents, "
                  "exercises, staff and interested parties. Reviewed at every management review.",
         "headers": ["ID", "Date raised", "Source", "Improvement", "Expected benefit", "Clause / control",
                     "Owner", "Decision", "Due", "Status", "Outcome / notes"],
         "rows": IMPROVE,
         "widths": [13, 11, 22, 48, 30, 20, 15, 10, 11, 12, 40],
         "lists": {"Decision": ["Adopt", "Defer", "Reject"],
                   "Status": ["Not started", "In progress", "Done"]},
         "status": ["Status"]},
        {"name": "Effectiveness Checks", "title": "Effectiveness checks of corrective actions",
         "intro": "Defined when the action is planned; done by someone not responsible for the action. A result other "
                  "than 'Effective' keeps the NC open or raises a follow-up.",
         "headers": ["Check ID", "CA ID", "NC ID", "Success criterion", "Planned date", "Date done", "Checked by",
                     "Result", "Evidence", "Follow-up"],
         "rows": EFFECT,
         "widths": [9, 13, 13, 45, 12, 11, 26, 16, 45, 30],
         "lists": {"Result": ["Effective", "Partially effective", "Not effective", "Pending"]}},
    ],
}
