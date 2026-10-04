from org import AI_SYSTEMS, KEY_RISKS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref, title_of, who

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
INC = SAMPLE_INCIDENT
R5 = {r[0]: r for r in KEY_RISKS}["RSK-AI-005"]
NC3 = SAMPLE_AUDIT["findings"][0]
CA4 = SAMPLE_CAPA[0]

DOC = {
    "id": "IMS-PRO-005",
    "summary": f"One procedure for every kind of incident at {N}: security events, personal-data breaches and AI "
               "incidents such as harmful output, a bias complaint, a model failure or a content-safety miss. "
               "It sets severity levels, response times, who does what, how to keep evidence and when to tell "
               "customers and regulators.",
    "clauses": {"27001": "Annex A 5.5, 5.24, 5.25, 5.26, 5.27, 5.28, 6.8, 8.15, 8.16; Clause 10.2",
                "42001": "Annex A.3.3, A.6.2.6, A.8.3, A.8.4, A.10.3; Clauses 8.1, 10.2"},
    "howto": [
        "Print the severity matrix (section 4) and the first-hour checklist (section 5.1) and pin them in your "
        "incident channel. Nobody reads a ten-page procedure in the middle of an incident.",
        "Check every legal deadline in section 7 against your own contracts and the laws where you operate. "
        "The deadlines shown are a sensible starting point, not legal advice.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"Things go wrong. A laptop is stolen, an API key ends up in a public repository, or {STF} produces "
              "an image it never should have. This procedure makes sure that when something goes wrong we notice "
              "quickly, limit the harm, tell the right people on time, and learn so that it does not happen again."),
        ("p", "We run **one** incident process for security and for AI. The same people, the same channel, the same "
              f"log ({ref('IMS-REG-006')}) and the same severity scale. AI incidents simply have a few extra steps "
              "(section 6), such as rolling back a model and preserving prompts and outputs."),
        ("h1", "2. Scope and definitions"),
        ("p", f"This procedure covers all information, systems and AI systems inside the scope in {ref('IMS-REG-001')}, "
              "including incidents that start at a supplier (for example our cloud provider, the foundation-model "
              f"API or the {SFR} vendor) but affect us, our customers or our artists."),
        ("table", ["Term", "Plain meaning", f"{N} example"], [
            ("Event", "Something observed that might matter for security or AI behaviour. Most events are harmless.",
             "A failed login burst from one IP address; a single odd output reported by a user."),
            ("Security incident", "An event that harms, or is likely to harm, the confidentiality, integrity or "
             "availability of information.", "Customer scripts exposed through a public storage link."),
            ("AI incident", "An AI system behaves in a way that harms, or could harm, people, rights, customers or "
             "us — whether or not anyone attacked it.",
             f"{STF} produces a deceptive image of a real person; {ARM} hides new artists; {SCM} mixes up two "
             "customers' scripts."),
            ("Personal-data breach", "A security incident that affects personal data. It may start legal clocks "
             "(section 7).", "An artist's payout details visible to another artist."),
            ("Near miss", "Something that would have been an incident if a control had not stopped it. Logged and "
             "learned from, like an incident.", "Secret scanning blocks a commit containing an API key."),
        ], [3.2, 6.3, 7]),
        ("std", [
            "ISO/IEC 27001 Annex A expects you to plan how you handle incidents, decide which events are incidents, "
            "respond to them, learn from them and keep evidence properly (5.24–5.28), and to give everyone an easy "
            "way to report what they notice (6.8).",
            "ISO/IEC 42001 expects you to tell users and other affected parties about AI incidents (A.8.4), to meet "
            "any duty to report externally (A.8.3), to let people raise concerns about AI (A.3.3) and to monitor AI "
            "systems in operation so problems are found (A.6.2.6).",
            "Both standards expect incidents that reveal a failure of your own rules to go into nonconformity and "
            "corrective action (Clause 10.2).",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Who", "What they do"], [
            ("Reporter", "Anyone — staff, contractors, customers, artists, suppliers",
             "Report anything suspicious within 1 hour of noticing. Do not investigate alone or delete anything."),
            ("Incident Lead (security)", who("CISO"),
             "Default lead for security incidents and breaches. Decides severity, runs the response, keeps the record."),
            ("Incident Lead (AI)", who("CAIO"),
             "Default lead for AI incidents. Decides on model rollback or kill switch with the system owner."),
            ("Platform responder", who("SRE"), "Containment and recovery in the cloud; preserves logs and snapshots."),
            ("Data and ML responder", who("HOD"),
             "Investigates model, dataset and evaluation evidence; runs canary and regression tests."),
            ("Privacy and legal", who("DPO") + "; " + who("LEGAL") + " as needed",
             "Decides whether a notification duty exists, drafts regulator and data-subject notices, legal hold."),
            ("Content-safety sign-off", who("CREA"),
             "Judges harmful or deceptive content; signs off before content-safety controls are restored."),
            ("Incident Commander (S1 only)", who("CEO"),
             "Takes overall command of a critical incident, approves external statements and spending."),
            ("Scribe", "Anyone the Incident Lead names", "Keeps the timeline in the incident channel in real time."),
        ], [3.6, 4.5, 8.4]),
        ("p", "If the default Incident Lead is unavailable, the other lead takes over; if both are away, the CTO "
              f"leads. Out of hours, the on-call engineer in the platform rota pages the lead. Full role descriptions "
              f"are in {ref('IMS-GOV-001')}."),
        ("h1", "4. Severity matrix"),
        ("p", "Severity is set at triage and can go up or down as facts emerge. When unsure, pick the higher level — "
              "it is cheap to downgrade and expensive to be late."),
        ("table", ["Level", "Typical criteria (any one is enough)", "Acknowledge", "Contain by", "Updates", "Who is told"], [
            ("S1 Critical", "Confirmed breach of Restricted data (customer scripts, artist portfolios, consent records) "
             "affecting many people; prohibited content (e.g. sexual content involving minors) generated or delivered; "
             "Canvas or the API down for everyone; attacker in production.",
             "15 min", "4 hours", "Every hour", "CEO immediately; Trust Council same day"),
            ("S2 High", "Limited personal-data breach; harmful or deceptive AI output reached a customer; a safety "
             "control (e.g. " + SFR + ") materially weakened; one enterprise customer seriously affected; "
             "outage over 2 hours.", "1 hour", "24 hours", "Every 4 hours", "CEO and both leads within 1 hour"),
            ("S3 Medium", "Contained security issue with no confirmed data exposure; credible bias or fairness "
             "complaint; AI quality failure without serious harm; lost encrypted device.",
             "1 working day", "5 working days", "Daily", "Incident Lead and system owner"),
            ("S4 Low", "Event or near miss; blocked attack; single low-impact output issue.",
             "3 working days", "30 days", "On closure", "Logged; reviewed monthly"),
        ], [2.2, 6.3, 1.8, 1.8, 1.9, 2.5]),
        ("tip", "Keep severity separate from blame. A high severity says how much is at stake, not that someone "
                "did something wrong. People who report early must never be punished for it."),
        ("h1", "5. The process"),
        ("p", "Every incident goes through the seven phases below. Small incidents move through them in an hour; "
              "big ones take weeks. The Incident Lead records each phase in the incident log."),
        ("h2", "5.1 Report"),
        ("bullets", [
            "Staff and contractors: post in **#trust-report** or email trust@quillfen.example. Mark it urgent if "
            "customer data or harmful content is involved. Phone the on-call number if nobody answers in 15 minutes.",
            "Customers and artists: the in-app 'Report a problem with this output' button, the support form or "
            "security@quillfen.example. Support staff forward these to #trust-report within 1 hour.",
            "Automated alerts: cloud security findings, secret scanning, endpoint protection, uptime monitoring and "
            "AI monitoring (canary test sets, fairness dashboards, moderation-rate alarms) post to #trust-report.",
            "Suppliers: notices from suppliers go to the Incident Lead, even when they say 'no action needed'.",
        ]),
        ("p", "**First-hour checklist for the person who receives a report:** (1) open a record in the incident log; "
              "(2) open a private incident channel named inc-YYYY-NNN; (3) page the Incident Lead; (4) write down "
              "what you know and what you do not know; (5) do not delete, restart or 'clean up' anything yet."),
        ("h2", "5.2 Triage"),
        ("steps", [
            "Confirm it is real and not a duplicate. If it is only an event, log it as S4 and close it with a note.",
            "Classify the type: security, personal-data breach, AI incident (harmful output, bias, model failure, "
            "content-safety miss, data leak through AI), availability, or supplier.",
            "Set the severity using section 4 and name the Incident Lead.",
            "Ask the privacy question: is personal data involved? If yes, the Privacy and Legal Lead joins now and "
            "records the time we became aware — this starts the legal clocks in section 7.",
            "Link the incident to existing risks in " + ref("IMS-REG-002") + " and to the affected assets or AI "
            "systems in " + ref("IMS-REG-005") + ".",
        ]),
        ("h2", "5.3 Contain"),
        ("p", "Stop the harm spreading before trying to understand everything. Typical containment moves:"),
        ("table", ["Situation", "Containment options"], [
            ("Compromised account", "Revoke sessions, reset passkeys, disable the account in single sign-on, review "
             "recent actions."),
            ("Leaked secret or API key", "Rotate the key immediately; check provider logs for use since the leak."),
            ("Exposed storage", "Remove public access; rotate any pre-signed links; snapshot access logs first."),
            ("Malware on a laptop", "Isolate it through endpoint protection; do not wipe until evidence is captured."),
            ("Harmful or wrong AI output", "Use the kill switch or roll back the model (section 6); quarantine the "
             "output; block the prompt pattern if needed."),
            ("Supplier failure", "Switch to fallback mode in " + ref("IMS-PRO-006") + "; pin the supplier version "
             "if they offer it."),
        ], [4.5, 12]),
        ("h2", "5.4 Investigate"),
        ("p", "Work out what happened, when, how, and who or what was affected. Build a timeline from logs, "
              "tickets, chat and model records. Collect evidence as described in section 8. For AI incidents, "
              "reproduce the behaviour on a copy of the model version that was live at the time — never on "
              "production with real customer data."),
        ("h2", "5.5 Eradicate and recover"),
        ("bullets", [
            "Remove the cause: patch the flaw, fix the configuration, retrain or re-filter the dataset, or replace "
            "the supplier component.",
            "Restore service from known-good state (clean images, verified backups, approved model versions).",
            "For AI systems, run the release evaluation again — accuracy, fairness and content-safety tests — and "
            f"get sign-off from the system owner (and the {title_of('CREA')} for content-safety controls) before "
            "returning to normal operation. A significant fix goes through the AI Release Review.",
            "Watch more closely for a set period after recovery (for example daily checks for 30 days).",
        ]),
        ("h2", "5.6 Notify"),
        ("p", "The Privacy and Legal Lead decides, and records in the Notification Tracker in "
              f"{ref('IMS-REG-006')}, whether anyone outside {N} must be told, by when, and by whom. Section 7 lists "
              "the usual duties. A decision **not** to notify is recorded with its reasons."),
        ("h2", "5.7 Learn"),
        ("bullets", [
            "Hold a blameless post-incident review within 10 working days for S1 and S2 incidents, and for any S3 "
            "that reveals a weak control. S4 events are reviewed in bulk once a month.",
            "Ask: what happened, why, what went well, what did not, and what will we change?",
            "Record lessons in the Lessons Learned sheet of " + ref("IMS-REG-006") + ". Where a rule or control "
            "was not followed or did not work, raise a nonconformity in " + ref("IMS-REG-008") + " under "
            + ref("IMS-PRO-009") + ".",
            "Update the risk register, impact assessments and this procedure where needed. Incident trends go to "
            "the management review (" + ref("IMS-PRO-008") + ").",
        ]),
        ("h1", "6. AI-specific steps"),
        ("h2", "6.1 Kill switches and rollback"),
        ("p", "Every AI system in production must have a documented way to switch it off or roll it back that the "
              "on-call engineer can use in under 15 minutes without a code change. These are tested twice a year."),
        ("table", ["AI system", "Kill switch / safe fallback", "Rollback"], [
            (STF, "Feature flag pauses generation; Canvas shows 'temporarily unavailable' and human artists can "
             "still be commissioned.", "Model registry: redeploy the previous approved model version."),
            (SCM, "Feature flag disables assistant; users can still write and break down scripts by hand.",
             "Pin the previous foundation-model version or prompt template."),
            (ARM, "Switch to a simple, transparent ordering (availability, then random) with a banner.",
             "Redeploy the previous ranking model and feature set."),
            (SFR, "If moderation is unavailable or unreliable, generation stops (fail closed).",
             "Pin the vendor's previous model version through their version-pinning option."),
            (CDA, "Disable the IDE extension through device management.", "Not applicable (supplier tool)."),
        ], [3, 7.5, 6]),
        ("h2", "6.2 Preserve prompts and outputs"),
        ("bullets", [
            "Before changing anything, export the relevant prompts, inputs, outputs, moderation scores, model and "
            "prompt-template versions and configuration for the affected time window.",
            "Store them in the restricted incident evidence bucket with access limited to the incident team.",
            "Quarantine harmful outputs rather than deleting them, so they can be analysed — **except** suspected "
            "child sexual abuse material: never download, view, copy or forward it. Restrict access, call the "
            "Privacy and Legal Lead and external counsel, who decide on reporting to the competent authority.",
            "Keep AI incident evidence for at least 3 years, or longer if a legal hold applies.",
        ]),
        ("h2", "6.3 Bias and fairness complaints"),
        ("p", f"A fairness complaint (for example an artist saying {ARM} never shows their work) is an AI incident "
              "even if we think the model is fine. The Head of AI checks the fairness metrics for the affected "
              "group, replies to the person within 10 working days with what we found, and records the outcome. "
              "Several similar complaints in a quarter trigger a review of the impact assessment "
              f"({ref('IMS-PRO-002')})."),
        ("h1", "7. Notification duties"),
        ("table", ["Who must be told", "When it applies", "Deadline we work to", "Owner"], [
            ("EU / UK supervisory authority (GDPR, UK GDPR)", "Personal-data breach where we are controller, unless "
             "unlikely to result in risk to people", "Within 72 hours of becoming aware", person("DPO")),
            ("UAE Data Office (PDPL)", "Breach affecting the privacy, confidentiality or security of personal data "
             "of UAE data subjects", "As set in the executive regulations; internal target 72 hours", person("DPO")),
            ("Affected individuals", "Breach likely to result in high risk to them; or AI output that directly "
             "affected them", "Without undue delay", person("DPO")),
            ("Business customers (we are their processor)", "Any breach of their data; AI incident affecting their "
             "projects", "Contract terms; default within 48 hours, sooner for S1", "Account owner + Incident Lead"),
            ("EU AI Act market surveillance authority", "Serious incident with a high-risk AI system (Art. 73). None "
             "of our systems is currently classed high-risk — record this check every time", "15 days, shorter "
             "for the most serious cases", person("CAIO")),
            ("Suppliers involved", "Incident caused by, or affecting, a supplier service", "Same day for S1/S2",
             "Incident Lead"),
            ("Insurer, payment processor, police", "As required by policy or law", "[[per policy]]", person("CEO")),
        ], [4, 5.5, 4, 3]),
        ("tip", "The 72-hour clock starts when we become reasonably sure personal data was affected — not when the "
                "investigation ends. If you do not have all the facts, notify with what you know and send updates."),
        ("h1", "8. Evidence collection"),
        ("bullets", [
            "Capture first, fix second: take disk and memory snapshots, export logs and copy configuration before "
            "remediation where this does not prolong serious harm.",
            "Record for each item: what it is, where it came from, who collected it, when (UTC), and its SHA-256 "
            "hash. Keep this chain-of-custody list in the incident record.",
            "Store evidence in the write-once incident evidence bucket; access is logged.",
            "Rely on synchronised clocks (all systems use the cloud time service) so timelines line up.",
            "If legal action or a regulator inquiry is possible, the Privacy and Legal Lead places a legal hold and "
            "suspends normal log deletion for the affected sources.",
        ]),
        ("h1", "9. Communication templates"),
        ("p", "**Internal alert (incident channel):** INC-[[YYYY-NNN]] · Severity [[S1–S4]] · Lead [[name]]. What we "
              "know: [[facts]]. What we don't know yet: [[open questions]]. Do not discuss outside this channel. "
              "Next update at [[time UTC]]."),
        ("p", "**Customer notice:** We are writing to tell you about an issue that affected [[service]] between "
              "[[start]] and [[end]]. What happened: [[plain description]]. What it means for you: [[impact]]. "
              "What we have done: [[containment and fix]]. What you may want to do: [[recommended steps]]. "
              "Contact: [[name, email]]. We will update you by [[date]]."),
        ("p", "**Regulator notification outline:** nature of the breach; categories and approximate number of "
              "people and records; likely consequences; measures taken or proposed; contact point; what is still "
              "under investigation and when we will follow up."),
        ("p", "**Artist or user notice (AI incident):** Thank you for telling us about [[issue]]. We looked into it "
              "and found [[finding]]. We have [[action]]. If you would like to talk to a person about this, reply "
              "to this email or contact [[name]]."),
        ("h1", "10. Worked example"),
        ("example", f"{INC['id']} — {INC['title']}", [
            f"**Type and severity:** {INC['type']}; {INC['severity']}.",
            f"**What happened:** {INC['summary']}",
            f"**Timeline (UTC):** 2026-08-12 vendor ships an update to {SFR} without notice. {INC['date']} the "
            "customer's prompt produces the panel; it is delivered with the 'AI-assisted' label and content "
            "credentials. 2026-08-17 09:10 the weekly canary run shows likeness detection down from 97% to 81%; "
            f"09:40 triaged as S2, {person('CAIO')} is Incident Lead, {person('CREA')} joins for content safety. "
            f"10:30 {SFR} pinned to the previous model version; canary back to 97%. 14:00 our own likeness check "
            "scans all outputs since 08-12: three candidates, one confirmed. 15:00 the customer is told and "
            "confirms the image was not published.",
            f"**Containment and recovery:** {INC['actions']}",
            "**Evidence kept:** prompts, outputs and moderation scores for 08-12 to 08-17; vendor version history; "
            "canary results; chat timeline — hashed and stored in the evidence bucket.",
            "**Notification decision:** the Privacy and Legal Lead recorded that no regulator notification was "
            "required: no breach of data we hold, the image was labelled and unpublished, and the customer agreed "
            f"to delete it. {STF} is not a high-risk system under the EU AI Act, so Art. 73 does not apply. The "
            "vendor was asked for a written explanation.",
            f"**Lessons:** we had no contract right to be told about vendor model changes and no change check for "
            f"supplier AI updates. Risk {R5[0]} was re-assessed (likelihood unchanged at {R5[6]}, severity "
            f"{R5[7]}). The internal audit {SAMPLE_AUDIT['id']} later confirmed this as {NC3[0]} ({NC3[1].lower()}), "
            f"fixed by {CA4[0]} (owner {person(CA4[3])}, due {CA4[4]}). Links: {INC['links']}.",
        ]),
        ("h1", "11. Testing and training"),
        ("bullets", [
            "Tabletop exercise twice a year, alternating a security scenario and an AI scenario; one may be "
            "combined with the continuity test in " + ref("IMS-PRO-006") + ".",
            "Kill switches and rollbacks for each production AI system tested twice a year.",
            "Every new joiner learns how to report in their first week (" + ref("IMS-PRO-003") + ").",
            "Contact lists and on-call rota checked every quarter by the " + title_of("IMSC") + ".",
        ]),
        ("h1", "12. Records"),
        ("bullets", [
            "Incident record and timeline (Incident Log in " + ref("IMS-REG-006") + ").",
            "Notification decisions and copies of notices (Notification Tracker).",
            "Evidence inventory with hashes; post-incident review notes (Lessons Learned sheet).",
            "Nonconformities and corrective actions raised (" + ref("IMS-REG-008") + ").",
        ]),
        ("h1", "13. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-PRO-001", "IMS-PRO-002", "IMS-POL-006", "IMS-PRO-006",
                                      "IMS-REG-006", "IMS-PRO-009")]),
    ],
}
