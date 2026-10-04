from datetime import date

from org import (who, AI_SYSTEMS, ASSETS, COMMITTEES, IMPACT, KEY_RISKS, LEVELS, LIKELIHOOD, ORG, level_for, person,
                 ref, title_of)

N = ORG["name"]
SYS = {s["id"]: s for s in AI_SYSTEMS}
AST = {a[0]: a for a in ASSETS}
TC, ARR = list(COMMITTEES)[:2]


def target(code):
    if code in SYS:
        return f"{code} {SYS[code]['name']}"
    return f"{code} {AST[code][1]}"


def owner(key):
    return who(key)


def split_controls(text):
    """'42001 A.7.3, A.7.5; 27001 5.32' -> ('5.32', 'A.7.3, A.7.5')."""
    iso27, iso42 = "", ""
    for part in text.split(";"):
        part = part.strip()
        if part.startswith("27001"):
            iso27 = part[5:].strip()
        elif part.startswith("42001"):
            iso42 = part[5:].strip()
    return iso27, iso42


SCORE_IN = '=IF(OR(H{r}="",I{r}=""),"",H{r}*I{r})'
LEVEL_IN = '=IF(J{r}="","",IF(J{r}>=16,"Critical",IF(J{r}>=10,"High",IF(J{r}>=5,"Medium","Low"))))'
SCORE_RES = '=IF(OR(P{r}="",Q{r}=""),"",P{r}*Q{r})'
LEVEL_RES = '=IF(R{r}="","",IF(R{r}>=16,"Critical",IF(R{r}>=10,"High",IF(R{r}>=5,"Medium","Low"))))'

# Extra details for the shared key risks: cause, consequence, existing controls, acceptance, review, status
KEY_DETAIL = {
    "RSK-AI-001": ("Bulk-licensed image packs and early commissions without a per-image consent record; "
                   "artist opt-outs not propagated to the training set",
                   "Copyright claims, artists' trust lost, model must be retrained; breach of Artist Agreement",
                   "Licence checks on new packs; consent ledger for commissions since 2025",
                   "Risk owner", "2027-01-15", "In progress"),
    "RSK-AI-002": ("Prompts naming real people or jailbreak phrasing get past the content filter",
                   "Deceptive image harms a real person's reputation; EU AI Act deepfake duties breached; "
                   "customer trust lost",
                   f"{SYS['AI-SYS-004']['name']} screening; visible AI label; C2PA content credentials",
                   "Risk owner (reported to " + TC + ")", "2027-03-31", "In progress"),
    "RSK-AI-003": ("Ranking features weight rating history and English-language tags heavily",
                   "New and non-English-portfolio artists get fewer commissions and less income; unfair outcome",
                   "Manual monthly fairness review of exposure ratio",
                   "Risk owner", "2027-01-15", "In progress"),
    "RSK-AI-004": ("Model confabulates scenes; session context bug or shared cache mixes customers' scripts",
                   "Wrong storyboards delivered; confidential unreleased script disclosed to another customer",
                   "Zero-retention API terms; per-tenant session isolation; user can edit scene list",
                   "Risk owner", "2027-03-31", "Implemented"),
    "RSK-AI-005": ("Vendor ships model updates without notice; we did not pin versions or re-test after changes",
                   "Prohibited or deceptive content reaches customers; harm to depicted people; regulatory exposure",
                   "Weekly canary test set; vendor version pinning (since INC-2026-007)",
                   TC + " 2026-10-21, until 2027-01-31, pending CA-2026-004", "2027-01-31", "In progress"),
    "RSK-IS-001": ("Bucket policy changed by hand outside infrastructure-as-code; no public-access guard",
                   "Unreleased customer scripts exposed; notifiable breach; contract penalties",
                   "Encryption at rest; IaC for most buckets",
                   "Risk owner", "2027-03-31", "Implemented"),
    "RSK-IS-002": ("Credential phishing with relayed one-time codes against engineers",
                   "Attacker reaches production; customer data and model weights stolen; notifiable breach",
                   "SSO with app-based one-time codes; yearly awareness training",
                   "Risk owner", "2027-03-31", "Implemented"),
    "RSK-IS-003": ("Staff use free AI chatbots to debug code or summarise documents",
                   "Source code, API keys or customer data disclosed to an AI vendor and possibly used for training",
                   "Acceptable use guidance (informal); secret scanning in CI",
                   "Risk owner", "2027-01-15", "In progress"),
    "RSK-IS-004": ("Single-region deployment; restore process untested",
                   "Canvas and API down for more than 24 hours; SLA credits; customers leave",
                   "Daily snapshots; multi-AZ database",
                   "Risk owner", "2027-03-31", "Implemented"),
    "RSK-IS-005": ("Outdated npm packages; no time-bound patching rule",
                   "Remote code execution or data theft through the web app",
                   "Dependency scanning alerts in GitHub",
                   "Risk owner", "2027-01-15", "In progress"),
}

RISK_ROWS = []
for rid, title, tgt, own, l, i, rl, ri, treat, ctl in KEY_RISKS:
    cause, cons, existing, acc_by, review, status = KEY_DETAIL[rid]
    c27, c42 = split_controls(ctl)
    if acc_by == "Risk owner":
        acc_by = person(own) + " (risk owner)"
    elif acc_by.startswith("Risk owner"):
        acc_by = person(own) + acc_by[len("Risk owner"):]
    RISK_ROWS.append([rid, "AI" if "-AI-" in rid else "IS", title, cause, cons, target(tgt), owner(own),
                      l, i, SCORE_IN, LEVEL_IN, existing, treat, c27 or "—", c42 or "—",
                      rl, ri, SCORE_RES, LEVEL_RES, acc_by, review, status])

EXTRA = [
    ("RSK-IS-006", "IS", "Former contractor keeps access to GitHub or AWS after the contract ends",
     "Contractor offboarding run by hiring managers; no automatic deprovisioning",
     "Source code or customer data accessed by someone with no business need", "AST-010", "CISO",
     3, 3, "Enterprise SSO for most tools", "Modify", "5.11, 5.18, 6.5", "—", 1, 3,
     "Risk owner", "2027-03-31", "In progress"),
    ("RSK-IS-007", "IS", "Ransomware on a company laptop encrypts synced business records",
     "Malicious attachment; sync client propagates encrypted files",
     "Finance and HR records unavailable for days; possible personal-data breach", "AST-011", "CISO",
     2, 3, "EDR on all laptops; SaaS version history", "Modify", "8.1, 8.7, 8.13", "—", 1, 3,
     "Risk owner", "2027-03-31", "Implemented"),
    ("RSK-IS-008", "IS", "Foundation-model API key leaked and abused",
     "Key committed to a repository or pasted into a ticket; no spend limit",
     "Five-figure bill overnight; prompts and outputs exposed; service suspended by provider", "AST-008", "SRE",
     3, 4, "Secrets manager for production; secret scanning in CI", "Modify", "5.17, 8.12, 8.16, 8.24",
     "A.4.4", 2, 3, "Risk owner", "2027-01-15", "In progress"),
    ("RSK-IS-009", "IS", "Broken access control in Commons exposes artists' payout and identity details",
     "Object IDs in the API not checked against the logged-in user",
     "Personal data of artists exposed; notifiable breach; artists leave the marketplace", "AST-003", "CTO",
     3, 4, "Code review; annual pentest", "Modify", "8.3, 8.26, 8.28, 8.29", "—", 1, 4,
     "Risk owner", "2027-03-31", "Implemented"),
    ("RSK-AI-006", "AI", "Prompt injection hidden in an uploaded script makes ScriptMate ignore its instructions",
     "Untrusted script text passed to the model in the same context as system instructions",
     "Misleading scene lists; system prompt disclosed; customer loses trust", "AI-SYS-002", "CAIO",
     3, 3, "Output limited to scene lists; no tool access", "Modify", "8.28", "A.6.2.4, A.6.2.6", 2, 2,
     "Risk owner", "2027-03-31", "In progress"),
    ("RSK-AI-007", "AI", "StoryFrame outputs closely imitate a living artist's signature style or a protected character",
     "Base model memorised popular works; prompts name living artists",
     "Infringement claim; harm to the artist's income and reputation; marketplace trust lost", "AI-SYS-001", "CREA",
     3, 4, "Artist-name prompt warnings", "Modify", "5.32", "A.6.2.4, A.7.5, A.8.2, A.9.4", 2, 3,
     "Risk owner", "2027-01-15", "In progress"),
    ("RSK-AI-008", "AI", "ArtistMatch relevance drifts as the marketplace grows and nobody notices",
     "Model trained on 2025 data; no drift metric or alert",
     "Poor matches, fewer completed commissions, unfair exposure creeping back", "AI-SYS-003", "HOD",
     3, 2, "Quarterly manual retrain", "Modify", "—", "A.6.2.6, A.6.2.8", 2, 2,
     "Risk owner", "2027-03-31", "Planned"),
    ("RSK-AI-009", "AI", "Engineers accept insecure CodeAssist suggestions without proper review",
     "Over-trust in AI suggestions; time pressure; reviewers assume code was checked",
     "Vulnerabilities shipped to production", "AI-SYS-005", "CTO",
     4, 3, "Mandatory code review; SAST in CI", "Modify", "8.25, 8.28, 8.29", "A.9.2, A.9.3", 2, 3,
     "Risk owner", "2027-03-31", "In progress"),
    ("RSK-AI-010", "AI", "Customers publish StoryFrame images in adverts without the required AI disclosure",
     "Customers strip labels or credentials; terms do not explain their duties",
     "Audiences deceived; customer and our brand exposed under EU AI Act and advertising rules", "AI-SYS-001", "DPO",
     3, 3, "Visible label and C2PA credentials on export", "Share", "5.31", "A.8.2, A.9.4, A.10.4", 2, 3,
     "Risk owner", "2027-03-31", "Planned"),
]

for (rid, typ, title, cause, cons, tgt, own, l, i, existing, treat, c27, c42, rl, ri, acc, review,
     status) in EXTRA:
    RISK_ROWS.append([rid, typ, title, cause, cons, target(tgt), owner(own), l, i, SCORE_IN, LEVEL_IN, existing,
                      treat, c27, c42, rl, ri, SCORE_RES, LEVEL_RES,
                      person(own) + " (risk owner)" if acc == "Risk owner" else acc, review, status])

RISK_ROWS.append(["[[RSK-IS-0xx]]", "[[IS or AI]]", "[[cause → event → consequence in one line]]", "[[cause]]",
                  "[[who or what is harmed]]", "[[AST-0xx or AI-SYS-00x]]", "[[one named owner]]", "", "",
                  SCORE_IN, LEVEL_IN, "[[controls that work today]]", "", "[[e.g. 8.8]]", "[[e.g. A.6.2.4]]",
                  "", "", SCORE_RES, LEVEL_RES, "[[name, date]]", "[[yyyy-mm-dd]]", "Open"])

HEADERS = ["Risk ID", "Type", "Risk title", "Cause (threat / vulnerability / source)", "Consequence",
           "Affected system / asset", "Risk owner", "Inherent L", "Inherent I", "Inherent score",
           "Inherent level", "Existing controls", "Treatment option", "Planned controls — 27001 Annex A",
           "Planned controls — 42001 Annex A", "Residual L", "Residual I", "Residual score", "Residual level",
           "Accepted by", "Next review", "Status"]

D = date
ACTIONS = [
    ("TP-01", "RSK-AI-001", "Audit every image in the fine-tuning set against the consent ledger; remove unverified "
     "images and retrain", "HOD", D(2026, 9, 30), "In progress", "Audit report; dataset hash before/after"),
    ("TP-02", "RSK-AI-001", "Automate opt-out propagation from Commons profile to the training-data exclusion list",
     "HOD", D(2026, 12, 15), "In progress", "Pipeline run log; test opt-out record"),
    ("TP-03", "RSK-AI-002", "Add named-person likeness check before image delivery", "CAIO", D(2026, 8, 31),
     "Done", "Release record; red-team rerun 0/200 bypasses"),
    ("TP-04", "RSK-AI-002", "Quarterly red-team of deepfake prompts with Artist Advisory Panel member",
     "CAIO", D(2026, 12, 31), "In progress", "Red-team reports"),
    ("TP-05", "RSK-AI-003", "Add exposure-boost slot for new artists and automatic alert when ratio < 0.8",
     "CAIO", D(2026, 11, 30), "In progress", "Model card update; alert config (OFI-2026-05)"),
    ("TP-06", "RSK-AI-005", "CA-2026-004: model-change notice and version-pinning clause in SafeFrame agreement "
     "and AI supplier template", "DPO", D(2026, 11, 30), "In progress", "Signed contract amendment"),
    ("TP-07", "RSK-AI-005", "Run canary test set daily for 30 days after INC-2026-007, then weekly with alerting",
     "CREA", D(2026, 9, 15), "Done", "Canary dashboard export"),
    ("TP-08", "RSK-IS-001", "Account-level public-access block and IaC drift detection on all buckets",
     "SRE", D(2026, 6, 30), "Done", "Cloud config screenshot; CI policy check"),
    ("TP-09", "RSK-IS-002", "Roll out passkeys / security keys to all staff and contractors", "CISO",
     D(2026, 7, 31), "Done", "Identity provider MFA report: 100% phishing-resistant"),
    ("TP-10", "RSK-IS-002", "Just-in-time production access with approval and 4-hour expiry", "CISO",
     D(2026, 8, 31), "Done", "Access request log"),
    ("TP-11", "RSK-IS-003", "Publish generative-AI rules in the Acceptable Use Policy and block unapproved AI "
     "tools on managed laptops", "CISO", D(2026, 10, 31), "In progress", "IMS-POL-005 v2; web-filter rule"),
    ("TP-12", "RSK-IS-005", "Patch SLA in CI: build fails on critical vulnerabilities older than 7 days",
     "CTO", D(2026, 10, 15), "In progress", "CI policy; vulnerability age report"),
    ("TP-13", "RSK-IS-006", "Route all contractor onboarding/offboarding through People Ops with automatic "
     "deprovisioning (see CA-2026-005)", "HOP", D(2026, 10, 31), "In progress", "Checklist; SSO deprovision log"),
    ("TP-14", "RSK-IS-008", "Set spend limits and anomaly alerts on all model-provider accounts", "SRE",
     D(2026, 9, 30), "In progress", "Provider console settings"),
    ("TP-15", "RSK-AI-008", "Add drift metric (population stability index) to monthly ArtistMatch report",
     "HOD", D(2027, 1, 31), "Not started", "Monitoring dashboard"),
    ("TP-16", "RSK-AI-010", "Update customer terms with AI-disclosure duties and in-app reminder at export",
     "DPO", D(2026, 12, 31), "Not started", "Terms v4; UI release note"),
]
DUE = '=IF(F{r}="","",IF(G{r}="Done","Done",IF(F{r}<TODAY(),"Overdue","On track")))'
# 'Control refs' column comes from the risk rows
CTRL = {row[0]: "; ".join(p for p in (row[13], row[14]) if p and p != "—") for row in RISK_ROWS}
PLAN_ROWS = [[a, r, act, owner(o), CTRL.get(r, ""), due, st, DUE, ev] for (a, r, act, o, due, st, ev) in ACTIONS]
PLAN_ROWS.append(["[[TP-xx]]", "[[RSK-..]]", "[[what will be done]]", "[[owner]]", "[[Annex A refs]]",
                  "[[due date]]", "Not started", DUE, "[[where the proof will be]]"])

# Scales sheet
SCALE_ROWS = [["Likelihood (L)", "", "", ""]]
SCALE_ROWS += [["Likelihood", n, name, text] for n, name, text in LIKELIHOOD]
SCALE_ROWS += [["Impact (I)", "", "", ""]]
SCALE_ROWS += [["Impact", n, name, text] for n, name, text in IMPACT]
SCALE_ROWS += [["Risk level (score = L × I)", "", "", ""]]
SCALE_ROWS += [["Level", f"{lo}–{hi}", name, rule] for name, lo, hi, rule in LEVELS]
SCALE_ROWS += [["Treatment options", "", "", ""],
               ["Treatment", "", "Modify", "Add or improve controls to reduce likelihood or impact"],
               ["Treatment", "", "Avoid", "Stop or change the activity that creates the risk"],
               ["Treatment", "", "Share", "Transfer part of the impact by contract, insurance or supplier"],
               ["Treatment", "", "Retain", "Accept as it is, within the acceptance rules in IMS-PRO-001"]]

# Heat map (rows start at 5)
RNG = "'Risk Register'!${c}$5:${c}$600"
IMP_HEAD = [f"{n} {name}" for n, name, _ in IMPACT]


def block(lcol, icol, start):
    rows = []
    for k, (l, lname, _) in enumerate(reversed(LIKELIHOOD)):
        r = start + k
        rows.append([f"{l} {lname}"] + [f"=COUNTIFS({RNG.format(c=lcol)},{l},{RNG.format(c=icol)},{i})"
                                         for i, _, _ in IMPACT] + [f"=SUM(B{r}:F{r})"])
    s, e = start, start + 4
    rows.append(["Total"] + [f"=SUM({c}{s}:{c}{e})" for c in "BCDEFG"])
    return rows


HEAT = [["INHERENT RISK — number of risks in each cell"] + [""] * 6]
HEAT += block("H", "I", 6)                       # rows 6–11
HEAT += [["RESIDUAL RISK — number of risks in each cell"] + [""] * 6]   # row 12
HEAT += block("P", "Q", 13)                      # rows 13–18
HEAT += [["RISK LEVEL OF EACH CELL (key)"] + [""] * 6]                  # row 19
HEAT += [[f"{l} {lname}"] + [level_for(l * i) for i, _, _ in IMPACT] + [""] for l, lname, _ in reversed(LIKELIHOOD)]

WB = {
    "id": "IMS-REG-002",
    "summary": f"{N}'s single register for information-security and AI risks, with the treatment plan, the "
               "scales and a live heat map. Built with the method in IMS-PRO-001.",
    "clauses": {"27001": "6.1.2, 6.1.3, 8.2, 8.3; Annex A referenced per risk",
                "42001": "6.1.2, 6.1.3, 8.2, 8.3; Annex A referenced per risk; inputs from 6.1.4 / 8.4"},
    "howto": [
        "Enter likelihood and impact as numbers 1–5. Score and level columns calculate themselves.",
        f"Every risk needs one named owner. Residual High risks need {TC} acceptance (see IMS-PRO-001 section 9).",
        "Write Annex A references in both control columns when a risk needs controls from both standards — "
        "then copy them into the two Statements of Applicability (IMS-SOA-001, IMS-SOA-002).",
        "Save a dated copy every quarter so auditors can see how risks changed over time.",
    ],
    "sheets": [
        {
            "name": "Risk Register",
            "title": "Integrated Risk Register (Information Security + AI)",
            "intro": f"One row per risk. Scales are on the 'Scales' sheet; method in {ref('IMS-PRO-001')}. "
                     "IS = information-security risk, AI = AI risk. Inherent = with today's controls; residual = "
                     "after planned controls work.",
            "headers": HEADERS,
            "rows": RISK_ROWS,
            "widths": [12, 6, 36, 34, 34, 26, 22, 8, 8, 8, 10, 30, 11, 18, 20, 8, 8, 8, 10, 26, 12, 13],
            "formulas": {"Inherent score": SCORE_IN, "Inherent level": LEVEL_IN,
                         "Residual score": SCORE_RES, "Residual level": LEVEL_RES},
            "lists": {"Type": ["IS", "AI"], "Inherent L": ["1", "2", "3", "4", "5"],
                      "Inherent I": ["1", "2", "3", "4", "5"], "Residual L": ["1", "2", "3", "4", "5"],
                      "Residual I": ["1", "2", "3", "4", "5"],
                      "Treatment option": ["Modify", "Avoid", "Share", "Retain"],
                      "Status": ["Open", "Planned", "In progress", "Implemented", "Closed"]},
            "levels": ["Inherent level", "Residual level"],
            "status": ["Status"],
            "freeze_cols": 3,
        },
        {
            "name": "Treatment Plan",
            "title": "Risk Treatment Plan",
            "intro": "Actions that put the planned controls in place. Each action belongs to a risk. 'Due status' "
                     "calculates itself from the due date and status.",
            "headers": ["Action ID", "Risk ID", "Action", "Owner", "Control refs (27001; 42001)", "Due date",
                        "Status", "Due status", "Evidence"],
            "rows": PLAN_ROWS,
            "widths": [10, 12, 50, 24, 24, 12, 13, 12, 34],
            "formulas": {"Due status": DUE},
            "lists": {"Status": ["Not started", "Planned", "In progress", "Done"]},
            "status": ["Status", "Due status"],
            "freeze_cols": 2,
        },
        {
            "name": "Scales",
            "title": "Risk scales and treatment options",
            "intro": f"The same scales are used in {ref('IMS-PRO-001')} and {ref('IMS-PRO-002')}. Change them "
                     "only by Trust Council decision, and everywhere at once.",
            "headers": ["Scale", "Value", "Name", "Meaning"],
            "rows": SCALE_ROWS,
            "widths": [26, 10, 18, 90],
            "levels": ["Name"],
            "section_rows": True,
            "blank_rows": 0,
        },
        {
            "name": "Heat map",
            "title": "Risk heat map (calculated)",
            "intro": "Counts of risks per likelihood × impact cell, calculated from the Risk Register with COUNTIFS. "
                     "Compare the inherent and residual grids to show the effect of treatment.",
            "headers": ["Likelihood ↓ / Impact →"] + IMP_HEAD + ["Total"],
            "rows": HEAT,
            "widths": [44, 14, 14, 14, 14, 14, 10],
            "levels": IMP_HEAD,
            "section_rows": True,
            "blank_rows": 0,
        },
    ],
}
