from org import AI_SYSTEMS, ORG, SAMPLE_AUDIT, SAMPLE_CAPA, SAMPLE_INCIDENT, person, ref, title_of, who

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
SFR, ARM, SCM = SYS["AI-SYS-004"], SYS["AI-SYS-003"], SYS["AI-SYS-002"]
A = SAMPLE_AUDIT
F = {f[0]: f for f in A["findings"]}
CA4, CA5 = SAMPLE_CAPA
NC3, NC4 = F[CA4[1]], F[CA5[1]]
INC = SAMPLE_INCIDENT

DOC = {
    "id": "IMS-PRO-009",
    "summary": f"How {N} records problems with its management system, fixes them, finds and removes their root "
               "causes, checks the fix worked, and keeps a register of improvements. One process for security and "
               "AI nonconformities.",
    "clauses": {"27001": "10.1, 10.2; links to 9.1, 9.2, 9.3; Annex A 5.27", "42001": "10.1, 10.2; links to 9.1–9.3"},
    "howto": [
        "The most common audit finding about corrective action is 'the cause was not addressed' — the team fixed "
        "the symptom and moved on. Spend most of your effort on section 5.4.",
        "Keep corrective actions small and specific. 'Improve supplier management' cannot be checked; 'add clause X "
        "to template Y by date Z' can.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", "A nonconformity is simply something that does not meet a requirement — of a standard, a law, a "
              "contract, or our own policies and procedures. Finding them is a sign the system works. This "
              "procedure makes sure each one is put right, its cause is removed so it does not come back, and the "
              "lessons make the whole system better."),
        ("h1", "2. Scope and definitions"),
        ("p", f"This procedure applies to all nonconformities in the integrated management system, whatever their "
              f"source, and to opportunities for improvement. Problems in AI systems themselves are handled first as "
              f"incidents under {ref('IMS-PRO-005')}; they become nonconformities here when they show that one of "
              "our requirements or controls was not met."),
        ("table", ["Term", "Plain meaning"], [
            ("Nonconformity (NC)", "A requirement was not met. Graded major or minor (see " + ref("IMS-PRO-007") + ")."),
            ("Correction", "The immediate fix of the problem in front of you (e.g. enrol the two contractors in "
             "training today). It does not stop it happening again."),
            ("Corrective action (CA)", "Action that removes the cause so the problem does not recur here or elsewhere."),
            ("Root cause", "The deepest cause we can act on. Fix it and the problem should not come back."),
            ("Effectiveness check", "Evidence, gathered later, that the corrective action actually worked."),
            ("Opportunity for improvement (OFI)", "Not a failure; a way to do better. Recorded in the Improvement Register."),
        ], [4.5, 12]),
        ("std", [
            "Both standards expect you, when a nonconformity happens, to react — control and correct it and deal "
            "with its consequences — and then decide whether action is needed to remove its cause, by reviewing it, "
            "finding the cause and checking whether similar problems exist or could occur (10.2).",
            "They expect you to carry out the actions needed, check whether they worked, and change the management "
            "system if necessary; actions should fit the size of the effects of the problem.",
            "You must keep records of the nature of each nonconformity, the actions taken and the results of "
            "corrective action, and you must continually improve the suitability, adequacy and effectiveness of the "
            "system (10.1).",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Who", "Responsibility"], [
            ("Register owner", who("IMSC"), "Records NCs, assigns IDs, chases due dates, reports status monthly."),
            ("NC owner", "Manager of the process where the NC occurred",
             "Correction, root-cause analysis, corrective-action plan, implementation."),
            ("Verifier", "Someone not responsible for the action — usually the auditor, the Security Lead or the "
             "Head of AI (for each other's areas)", "Checks effectiveness and agrees closure."),
            ("Trust Council", "Chair: " + who("CEO"),
             "Reviews open and overdue actions monthly; resolves resourcing; reviews trends at management review."),
            ("Everyone", "All staff and contractors", "Report suspected nonconformities in #trust-report."),
        ], [3.5, 5.5, 7.5]),
        ("h1", "4. Where nonconformities come from"),
        ("table", ["Source", f"{N} example"], [
            ("Internal and external audits", f"{NC3[0]} and {NC4[0]} from {A['id']}."),
            ("Incidents and near misses", "NC-2026-002: fairness monitoring was found missing after an artist "
             f"complaint about {ARM}."),
            ("Monitoring and objectives", "A metric misses its target two months running (e.g. high-severity "
             "vulnerabilities fixed later than 30 days)."),
            ("Management review", "The Trust Council finds a required review input was missing."),
            ("Complaints and feedback", "Customers, artists, the Artist Advisory Panel, regulators."),
            ("Self-reporting", "A team notices it skipped a step in the AI Release Review."),
            ("Supplier reports", "A supplier's assurance report shows a control failure affecting us."),
        ], [5, 11.5]),
        ("h1", "5. The process"),
        ("h2", "5.1 Record"),
        ("p", f"Log the NC in {ref('IMS-REG-008')} within 2 working days of it being found: ID (NC-YYYY-NNN), "
              "source, requirement not met (clause or control of each standard affected), description with "
              "evidence, grade, and owner. One NC can affect both standards — record both references on one row."),
        ("h2", "5.2 React and contain"),
        ("p", "The owner takes correction straight away to stop harm and deal with consequences — for example, "
              "rolling back a model, enrolling a person in overdue training, or removing an access right. Record "
              "what was done and when."),
        ("h2", "5.3 Decide whether corrective action is needed"),
        ("p", "Every major NC and every minor NC needs a root-cause analysis. For a genuinely one-off slip with low "
              "impact, the owner may record a short justification for correction only; the verifier must agree."),
        ("h2", "5.4 Find the root cause"),
        ("p", "Use the simplest method that gets to a cause you can act on:"),
        ("bullets", [
            "**5 Whys** — ask 'why?' repeatedly, each time about the answer before, until you reach a cause in a "
            "process, a rule, a design or a resource. Usually three to five steps. Stop when the next 'why' leaves "
            "our control.",
            "**Fishbone (Ishikawa) diagram** — for problems with several contributing causes. List possible causes "
            "under headings — for us: People, Process, Technology, Suppliers, Data, Model — then test which ones "
            "really contributed.",
            "Avoid 'human error' as a root cause. Ask why the system made the error easy or likely.",
        ]),
        ("h2", "5.5 Look for the same problem elsewhere"),
        ("p", "Ask whether the cause could produce the same failure in another system, team or supplier. If the "
              f"{SFR} contract lacked a clause, do other AI supplier contracts lack it too? Record the answer."),
        ("h2", "5.6 Plan and implement corrective action"),
        ("p", "Write one or more corrective actions (CA-YYYY-NNN) that remove the root cause. Each has an owner, a "
              "due date and a clear description of what will exist when it is done. Update risks, procedures, "
              "templates or the Statements of Applicability if the action changes them."),
        ("table", ["Grade", "Correction", "CA plan agreed", "CA completed", "Effectiveness check"], [
            ("Major", "Within 5 working days", "Within 10 working days", "Within 60 days", "Within 90 days of completion"),
            ("Minor", "Within 10 working days", "Within 15 working days", "Within 90 days", "At next audit or within 90 days"),
            ("From incident", "During the incident", "Within 10 working days of review", "As agreed", "As agreed"),
        ], [2.5, 3.4, 3.4, 3.2, 4]),
        ("h2", "5.7 Check effectiveness and close"),
        ("p", "Some time after the action is done, the verifier looks for evidence that the problem has not "
              "recurred and the new control operates. Define the check when you write the action — for example "
              "'all contractors joining in November and December complete training within 30 days'. Results are "
              "recorded in the Effectiveness Checks sheet. If the action was not effective, the NC stays open and "
              "the root cause is revisited."),
        ("tip", "Overdue actions are the first thing a certification auditor counts. If a date will slip, ask the "
                "Trust Council to approve a new date before it passes, and record why."),
        ("h1", "6. Continual improvement"),
        ("p", "Not every improvement starts from a failure. The Improvement Register in " + ref("IMS-REG-008") +
              " records OFIs from audits, ideas from staff, lessons from incidents and exercises, and changes "
              "suggested by monitoring results or the Artist Advisory Panel. Each entry gets an owner and a "
              "decision (adopt, defer, reject, with a reason). The Trust Council reviews the register at every "
              "management review and asks: is our system still suitable, adequate and effective, and where should "
              "we invest next?"),
        ("h1", "7. Worked examples"),
        ("example", f"{NC3[0]} — 5 Whys", [
            f"**Nonconformity ({NC3[1].lower()}, {NC3[2]}):** {NC3[3]} Found in {A['id']}; first visible as "
            f"incident {INC['id']}.",
            f"**Correction:** {SFR} pinned to the previous vendor model version on 2026-08-17; own likeness check "
            "added before image delivery.",
            "**Why 1** — Why did a model change go live unassessed? We did not know the vendor had changed the model.",
            "**Why 2** — Why did we not know? The vendor had no duty to tell us, and nobody watched their release notes.",
            "**Why 3** — Why no duty? The agreement was signed on the vendor's standard terms, which say nothing "
            "about model changes.",
            "**Why 4** — Why did we not ask for it? Our supplier onboarding checklist had no AI-model change clause; "
            "it was written for ordinary software-as-a-service.",
            "**Why 5** — Why did nothing else catch it? Supplier model updates were not on the change-management "
            "trigger list, so they were never treated as changes to our system.",
            f"**Root cause:** {CA4[2].split(' Action: ')[0].replace('Root cause: ', '')}",
            f"**Corrective action {CA4[0]}:** {CA4[2].split(' Action: ')[1]} Owner: {person(CA4[3])}. Due: {CA4[4]}.",
            f"**Same problem elsewhere?** Yes — the foundation-model contract for {SCM} had the same gap; it "
            "is included in the same action.",
            "**Effectiveness check:** by 2027-01-31 the Head of AI confirms that the clause is signed for both "
            "suppliers and that at least one vendor model change was notified and assessed before going live.",
            "**Risk link:** RSK-AI-005 stays at residual High until "
            "the check passes (Trust Council decision, " + ref("IMS-PRO-008") + ").",
        ]),
        ("table", ["Fishbone heading", f"Possible causes considered for {NC3[0]}", "Contributed?"], [
            ("People", "Supplier owner unaware AI models change frequently", "Partly"),
            ("Process", "No AI clause in onboarding checklist; supplier changes not change-managed", "Yes — root cause"),
            ("Technology", "Weekly (not daily) canary testing", "Yes — slowed detection"),
            ("Suppliers", "Vendor ships updates without notice", "Yes — trigger"),
            ("Data", "Canary set had few public-figure examples", "No — detected the drop"),
            ("Model", "Vendor model's lower likeness recall", "Yes — direct cause of the miss"),
        ], [3.5, 9, 4]),
        ("example", f"{NC4[0]} — short version", [
            f"**Nonconformity:** {NC4[3]} ({NC4[2]}).",
            "**Correction:** both contractors enrolled and completed training within a week of the audit.",
            "**Whys:** training enrolment is automatic only for people onboarded through the People Ops checklist → "
            "contractors were onboarded by hiring managers directly → there was no rule that contractors follow "
            "the same path.",
            f"**Corrective action {CA5[0]}:** {CA5[2].split(' Action: ')[1]} Owner: {person(CA5[3])}. Due: {CA5[4]}.",
            "**Effectiveness check:** all contractors joining from November to December 2026 complete training "
            "within 30 days (checked in December 2026 follow-up audit).",
        ]),
        ("h1", "8. Records"),
        ("bullets", [
            "NC & CA Log, Improvement Register and Effectiveness Checks in " + ref("IMS-REG-008") + ".",
            "Root-cause analyses (5 Whys or fishbone) attached to the NC record.",
            "Monthly status summary to the Trust Council; trends in management review minutes.",
        ]),
        ("h1", "9. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-PRO-005", "IMS-PRO-007", "IMS-REG-007", "IMS-PRO-008", "IMS-REG-008",
                                      "IMS-REG-002")]),
    ],
}
