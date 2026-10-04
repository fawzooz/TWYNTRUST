from datetime import date, datetime

from org import AI_SYSTEMS, ORG, SAMPLE_INCIDENT, person, ref

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
INC = SAMPLE_INCIDENT
d = date.fromisoformat

SEV = ["Critical (S1)", "High (S2)", "Medium (S3)", "Low (S4)"]
TYPES = ["Security incident", "Personal-data breach", "AI incident (harmful output)", "AI incident (bias / fairness)",
         "AI incident (model failure)", "AI incident (content safety) — also a supplier issue",
         "AI incident (data leak)", "Availability / supplier", "Event / near miss"]
LEVEL_F = '=IF(G{r}="","",LEFT(G{r},FIND(" ",G{r})-1))'
DAYS_F = '=IF(C{r}="","",IF(O{r}="",TODAY()-C{r},O{r}-C{r}))'

LOG = [
    ("INC-2026-001", d("2026-01-21"), d("2026-01-21"), "Phishing email impersonating the payment processor sent to finance",
     "Event / near miss", "AST-010", "Low (S4)", LEVEL_F, "Staff report", person("CISO"), "No",
     "Two staff received a fake payout-failure email. Both reported it within 10 minutes; nobody clicked.",
     "Sender domain blocked; warning posted; used as a phishing-simulation template.", "Closed", d("2026-01-22"),
     DAYS_F, "RSK-IS-002"),
    ("INC-2026-002", d("2026-02-09"), d("2026-02-09"), "Contractor laptop stolen from a car in Lisbon",
     "Security incident", "AST-010", "Medium (S3)", LEVEL_F, "Contractor", person("CISO"), "Possible",
     "Company-managed laptop with full-disk encryption and passkey login stolen.",
     "Remote lock and wipe confirmed; sessions revoked; DPO assessed: encrypted, no notification needed.", "Closed",
     d("2026-02-11"), DAYS_F, "RSK-IS-002"),
    ("INC-2026-003", d("2026-03-04"), d("2026-03-05"), f"{SCM} invented a scene not in the customer's script",
     "AI incident (model failure)", "AI-SYS-002", "Low (S4)", LEVEL_F, "Customer support", person("CAIO"), "No",
     "Shot list included a chase scene that did not exist in the script. Customer noticed before production.",
     "Prompt template tightened to cite script line numbers; hallucination test added to the evaluation set.",
     "Closed", d("2026-03-20"), DAYS_F, "RSK-AI-004"),
    ("INC-2026-004", d("2026-04-14"), d("2026-04-14"), "Staging bucket briefly public after infrastructure change",
     "Security incident", "AST-004", "Medium (S3)", LEVEL_F, "Cloud security alert", person("SRE"), "No",
     "A staging bucket holding synthetic test scripts was made public by a template error for 38 minutes.",
     "Public access blocked; access logs show no external reads; policy-as-code rule now blocks public buckets.",
     "Closed", d("2026-04-17"), DAYS_F, "RSK-IS-001"),
    ("INC-2026-005", d("2026-05-06"), d("2026-05-06"), f"Artists report that {ARM} never shows new portfolios",
     "AI incident (bias / fairness)", "AI-SYS-003", "Medium (S3)", LEVEL_F, "Artist complaint (12 artists)",
     person("CAIO"), "No",
     "Exposure ratio for new vs established artists had fallen to 0.55. Planned fairness monitoring was not running.",
     "Exploration boost re-enabled; monthly fairness report built; NC-2026-002 raised.", "Closed", d("2026-06-12"),
     DAYS_F, "RSK-AI-003; NC-2026-002"),
    ("INC-2026-006", d("2026-06-24"), d("2026-06-24"), f"Foundation-model API outage — {SCM} unavailable 3 hours",
     "Availability / supplier", "AI-SYS-002", "Medium (S3)", LEVEL_F, "Uptime monitoring", person("SRE"), "No",
     "Supplier-wide outage. Canvas worked; writing assistant showed 'paused'.",
     f"Manual mode used; status page updated; alternative-provider switch not needed (outage < RTO). See {ref('IMS-PRO-006')}.",
     "Closed", d("2026-06-24"), DAYS_F, "RSK-IS-004"),
    (INC["id"], d(INC["date"]), d("2026-08-17"), INC["title"], INC["type"], "AI-SYS-004", INC["severity"], LEVEL_F,
     "Weekly canary test set", person("CAIO"), "Yes (likeness of a real person)", INC["summary"], INC["actions"],
     "Closed", d("2026-09-16"), DAYS_F, INC["links"]),
    ("INC-2026-008", d("2026-08-28"), d("2026-08-28"), "Image-model API key pushed to a feature branch",
     "Security incident", "AST-008", "Medium (S3)", LEVEL_F, "Secret scanning", person("CISO"), "No",
     "Push protection was bypassed by mistake; key visible in the private repository for 40 minutes.",
     "Key rotated; provider logs show no misuse; bypass now needs Security Lead approval.", "Closed",
     d("2026-08-29"), DAYS_F, "RSK-IS-003"),
    ("INC-2026-009", d("2026-09-08"), d("2026-09-22"), "Artist opt-out request not actioned within 14 days",
     "AI incident (data leak)", "AI-SYS-001", "Medium (S3)", LEVEL_F, "Artist email", person("HOD"), "Yes",
     "Opt-out email went to a shared inbox that was not monitored during leave; 17 days elapsed. Artwork was "
     "not used in any training run in that period.",
     "Request actioned; artist informed and apologised to; opt-outs now go to the consent ledger form only.",
     "Closed", d("2026-09-25"), DAYS_F, "RSK-AI-001; OBJ-03"),
    ("INC-2026-010", d("2026-09-29"), d("2026-09-29"), "Prompt-injection attempts against the API to extract system prompts",
     "Event / near miss", "AI-SYS-002", "Low (S4)", LEVEL_F, "API abuse alert", person("CISO"), "No",
     "One trial account sent 240 injection prompts in an hour. No system prompt was returned.",
     "Account suspended; pattern added to abuse rules.", "In progress", None, DAYS_F, "RSK-AI-004"),
]

DEADLINE_F = '=IF(OR(F{r}="",H{r}=""),"",TEXT(F{r}+H{r}/24,"yyyy-mm-dd hh:mm"))'
NSTAT_F = ('=IF(E{r}="No","Not required",IF(I{r}<>"","Done",IF(F{r}="","",'
           'IF(NOW()>F{r}+H{r}/24,"Overdue","Open"))))')
dt = datetime.fromisoformat

NOTIFY = [
    ("NOT-001", "INC-2026-002", "EU supervisory authority (GDPR)", "GDPR Art. 33", "No",
     dt("2026-02-09T16:00"), DEADLINE_F, 72, "", NSTAT_F, person("DPO"),
     "Encrypted, wiped remotely; no risk to individuals. Decision recorded."),
    ("NOT-002", "INC-2026-004", "Affected enterprise customers", "DPA clause 9 (48 h)", "No",
     dt("2026-04-14T11:20"), DEADLINE_F, 48, "", NSTAT_F, person("DPO"),
     "Synthetic test data only; no customer data involved."),
    ("NOT-003", "INC-2026-006", "All Canvas customers (status page)", "Service terms", "Yes",
     dt("2026-06-24T08:05"), DEADLINE_F, 1, dt("2026-06-24T08:30"), NSTAT_F, person("CREA"), "Status page + email."),
    ("NOT-004", INC["id"], "Affected customer", "Customer agreement; IMS-PRO-005 s.7", "Yes",
     dt("2026-08-17T09:40"), DEADLINE_F, 48, dt("2026-08-17T15:00"), NSTAT_F, person("CREA"),
     "Customer confirmed image not published; agreed to delete it."),
    ("NOT-005", INC["id"], f"{SFR} vendor", "Supplier agreement", "Yes", dt("2026-08-17T09:40"), DEADLINE_F, 24,
     dt("2026-08-17T11:00"), NSTAT_F, person("DPO"), "Requested written root-cause explanation (received 2026-08-25)."),
    ("NOT-006", INC["id"], "EU / UAE data-protection authorities", "GDPR Art. 33; UAE PDPL", "No",
     dt("2026-08-17T09:40"), DEADLINE_F, 72, "", NSTAT_F, person("DPO"),
     "No breach of data we hold; image labelled and unpublished. Reasoning recorded."),
    ("NOT-007", INC["id"], "EU AI Act market surveillance authority", "EU AI Act Art. 73", "No",
     dt("2026-08-17T09:40"), DEADLINE_F, 360, "", NSTAT_F, person("CAIO"),
     f"{STF} is not a high-risk AI system; Art. 73 does not apply."),
    ("NOT-008", "INC-2026-009", "Artist (data subject)", "GDPR Art. 21 objection; Artist Agreement", "Yes",
     dt("2026-09-22T10:00"), DEADLINE_F, 72, dt("2026-09-23T09:00"), NSTAT_F, person("HOD"),
     "Confirmation of opt-out and apology sent."),
    ("NOT-009", "[[INC-YYYY-NNN]]", "[[recipient]]", "[[law or contract]]", "[[Yes/No]]", "", DEADLINE_F, "",
     "", NSTAT_F, "[[owner]]", "[[notes]]"),
]

LESSONS = [
    ("INC-2026-002", "Phishing-resistant MFA and full-disk encryption turned a theft into a non-event.",
     "Keep device baseline; add 'stolen device' card to staff handbook.", person("CISO"), d("2026-03-15"), "Done", ""),
    ("INC-2026-003", "Evaluation set did not test for invented content.", "Add hallucination cases to the release "
     "evaluation for every prompt-template change.", person("CAIO"), d("2026-03-31"), "Done", ""),
    ("INC-2026-004", "Manual review of infrastructure changes missed a public-access flag.",
     "Policy-as-code blocks public buckets in CI.", person("SRE"), d("2026-05-15"), "Done", ""),
    ("INC-2026-005", "Fairness monitoring in the impact assessment was never built.", "Monthly fairness report; "
     "release gate checks monitoring is live.", person("CAIO"), d("2026-06-30"), "Done", "NC-2026-002"),
    (INC["id"], "A supplier model change can weaken a safety control without notice; weekly canary was too slow.",
     "Contract clause for model-change notice and version pinning; supplier AI changes added to change management; "
     "own likeness check before delivery; daily canary for 30 days.", person("DPO"), d("2026-11-30"), "In progress",
     "NC-2026-003; CA-2026-004"),
    ("INC-2026-008", "Push-protection bypass was too easy.", "Bypass requires Security Lead approval.",
     person("CISO"), d("2026-09-15"), "Done", ""),
    ("INC-2026-009", "Opt-outs arriving by email depend on one person's inbox.", "Single opt-out form feeding the "
     "consent ledger; auto-reply points to it; ageing alert at day 7.", person("HOD"), d("2026-10-31"),
     "In progress", "OBJ-03"),
    ("[[INC-YYYY-NNN]]", "[[what we learned]]", "[[action]]", "[[owner]]", "[[due]]", "Not started", ""),
]

WB = {
    "id": "IMS-REG-006",
    "summary": f"The single log of security events, security incidents, personal-data breaches and AI incidents at "
               f"{N}, with the severity matrix, a tracker for legal and contractual notifications, and lessons "
               f"learned. Used with {ref('IMS-PRO-005')}.",
    "clauses": {"27001": "Annex A 5.24–5.28, 6.8; Clause 10.2",
                "42001": "Annex A.3.3, A.8.3, A.8.4; Clause 10.2"},
    "howto": [
        "Log every report, even ones you close in five minutes as 'Event / near miss'. Auditors look for a living log, "
        "and trends in small events are your early warning.",
        "Dates must be real dates (YYYY-MM-DD) for the 'Days open' and deadline formulas to work.",
    ],
    "sheets": [
        {"name": "Incident Log", "title": "Incident and event log",
         "intro": "One row per event or incident. Severity uses the Severity Matrix sheet. Level and Days open "
                  "calculate automatically.",
         "headers": ["Incident ID", "Date occurred", "Date detected", "Title", "Type", "Asset / AI system",
                     "Severity", "Level", "Reported by / source", "Incident Lead", "Personal data?", "Summary",
                     "Containment and actions", "Status", "Date closed", "Days open", "Links (risks, NCs, CAs)"],
         "rows": LOG,
         "formulas": {"Level": LEVEL_F, "Days open": DAYS_F},
         "widths": [14, 12, 12, 34, 24, 14, 14, 10, 18, 16, 14, 48, 48, 12, 12, 9, 22],
         "lists": {"Severity": SEV, "Type": TYPES, "Status": ["Open", "In progress", "Closed"],
                   "Personal data?": ["Yes", "No", "Possible"]},
         "levels": ["Level"], "status": ["Status"]},
        {"name": "Severity Matrix", "title": "Severity matrix and response times",
         "intro": f"Same scale for security and AI incidents. Full guidance in {ref('IMS-PRO-005')} section 4.",
         "headers": ["Severity", "Level", "Typical criteria", "Security example", "AI example", "Acknowledge within",
                     "Contain within", "Update cadence", "Who is told"],
         "rows": [
             ("Critical (S1)", "Critical", "Large breach of Restricted data; prohibited content delivered; full outage; "
              "attacker in production", "Customer scripts bucket exfiltrated",
              f"{SFR} fails and prohibited content reaches users", "15 minutes", "4 hours", "Hourly",
              "CEO at once; Trust Council same day"),
             ("High (S2)", "High", "Limited breach; harmful AI output reached a customer; safety control weakened; "
              "outage > 2 h", "Artist payout details exposed to another artist", INC["title"], "1 hour", "24 hours",
              "Every 4 hours", "CEO and both leads within 1 hour"),
             ("Medium (S3)", "Medium", "Contained issue, no confirmed exposure; credible bias complaint; AI quality "
              "failure without serious harm", "Lost encrypted laptop", f"{ARM} fairness complaint", "1 working day",
              "5 working days", "Daily", "Incident Lead and system owner"),
             ("Low (S4)", "Low", "Event or near miss; blocked attack; single low-impact output issue",
              "Phishing email reported, nobody clicked", "Single odd shot list corrected by user", "3 working days",
              "30 days", "On closure", "Logged; monthly review"),
         ],
         "widths": [14, 10, 40, 30, 34, 13, 13, 13, 26], "levels": ["Level"], "blank_rows": 0},
        {"name": "Notification Tracker", "title": "Regulator, customer and other notifications",
         "intro": "Record every notification decision — including decisions NOT to notify, with the reason. Enter "
                  "'Awareness' as a date-time; the deadline and status calculate from 'Hours allowed'.",
         "headers": ["Notification ID", "Incident ID", "Recipient", "Basis (law / contract)", "Required?",
                     "Awareness (date-time)", "Deadline", "Hours allowed", "Sent at", "Status", "Owner", "Notes"],
         "rows": NOTIFY,
         "formulas": {"Deadline": DEADLINE_F, "Status": NSTAT_F},
         "widths": [14, 14, 30, 26, 11, 18, 18, 10, 18, 13, 16, 46],
         "lists": {"Required?": ["Yes", "No"]}, "status": ["Status"]},
        {"name": "Lessons Learned", "title": "Lessons learned and follow-up actions",
         "intro": f"From post-incident reviews. Actions that fix a nonconformity go to {ref('IMS-REG-008')}; this "
                  "sheet keeps the link.",
         "headers": ["Incident ID", "What we learned", "Action", "Owner", "Due", "Status", "NC / CA link"],
         "rows": LESSONS,
         "widths": [16, 50, 55, 16, 12, 13, 22],
         "lists": {"Status": ["Not started", "In progress", "Done"]}, "status": ["Status"]},
    ],
}
