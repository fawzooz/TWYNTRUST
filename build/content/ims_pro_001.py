from org import (AI_SYSTEMS, ASSETS, COMMITTEES, IMPACT, KEY_RISKS, LEVELS, LIKELIHOOD, ORG, level_for, person,
                 ref, title_of, who)

N = ORG["name"]
SYS = {s["id"]: s for s in AI_SYSTEMS}
AST = {a[0]: a for a in ASSETS}
RISK = {r[0]: r for r in KEY_RISKS}
TC, ARR = list(COMMITTEES)[:2]


def nm(sys_id):
    return SYS[sys_id]["name"]


def rk(risk_id):
    """'RSK-AI-002 (title)' style label taken from org.KEY_RISKS."""
    return f"{risk_id} ({RISK[risk_id][1]})"


def score_text(l, i):
    s = l * i
    return f"{l} × {i} = {s} ({level_for(s)})"


SF, SM, AM, SAFE, CA = nm("AI-SYS-001"), nm("AI-SYS-002"), nm("AI-SYS-003"), nm("AI-SYS-004"), nm("AI-SYS-005")

AI2 = RISK["RSK-AI-002"]
IS2 = RISK["RSK-IS-002"]

MATRIX_ROWS = []
for l, lname, _ in reversed(LIKELIHOOD):
    MATRIX_ROWS.append([f"**{l} {lname}**"] + [f"{l * i} {level_for(l * i)}" for i, _, _ in IMPACT])

DOC = {
    "id": "IMS-PRO-001",
    "summary": f"How {N} finds, scores, treats and accepts risks — one method for information-security risks "
               "and AI risks, one register, one set of scales, feeding both Statements of Applicability.",
    "clauses": {"27001": "6.1.1, 6.1.2, 6.1.3, 8.2, 8.3; Annex A selected through 6.1.3",
                "42001": "6.1.1–6.1.3, 8.2, 8.3; links to 6.1.4 / 8.4 (impact assessment); Annex A selected through 6.1.3"},
    "howto": [
        "Change the scales only if they do not fit your size. If you do, change them everywhere at once — this "
        f"document, {ref('IMS-REG-002')} and {ref('IMS-PRO-002')} must use the same numbers.",
        "Do not try to list every possible risk on day one. Start with 15–25 real ones, treat the worst, and add "
        "more each quarter.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"This methodology tells everyone at {N} how to identify, analyse, evaluate and treat risks in a "
              "consistent way, so that two people scoring the same risk get roughly the same answer. It covers "
              "**two kinds of risk in one process**:"),
        ("bullets", [
            "**Information-security risks (IS)** — things that could harm the confidentiality, integrity or "
            "availability of our information: customer scripts, artwork, personal data, source code, cloud "
            "services.",
            "**AI risks (AI)** — things that could go wrong because we develop, provide or use AI systems, "
            "including harm to people who never touch our product, such as an artist whose style is copied or a "
            "public figure who is depicted in a fake image.",
        ]),
        ("p", "Both kinds of risk use the same scales, the same register, the same acceptance rules and the same "
              "review cycle. The only difference is the questions we ask to find them."),
        ("std", [
            "Both standards ask you to define a risk assessment process that gives consistent, valid and "
            "comparable results, with criteria for accepting risk and for performing assessments (27001 6.1.2; "
            "42001 6.1.2).",
            "Both ask you to choose treatment options, decide which controls you need, compare them with Annex A "
            "so nothing important is missed, write a Statement of Applicability, make a treatment plan, and get "
            "risk owners to approve the plan and the remaining risk (27001 6.1.3; 42001 6.1.3).",
            "ISO/IEC 42001 adds that AI risk assessment must consider consequences for individuals, groups and "
            "society — which is why it uses the results of AI system impact assessments (42001 6.1.4, 8.4).",
            "Both expect assessments to be repeated at planned intervals and when significant changes happen, "
            "with results kept as documented information (27001 8.2, 8.3; 42001 8.2, 8.3).",
        ]),
        ("h1", "2. Scope"),
        ("p", f"This method applies to all information, assets, processes, suppliers and AI systems inside the "
              f"scope in {ref('IMS-REG-001')}. That includes all five AI systems in the inventory "
              f"({', '.join(s['name'] for s in AI_SYSTEMS)}) — whether we build them, integrate a supplier's "
              "model or simply use a vendor tool."),
        ("h1", "3. Key terms"),
        ("table", ["Term", "Plain meaning"], [
            ("Risk", "Something uncertain that could happen and would affect our objectives — usually for the "
                     "worse. Written as 'cause → event → consequence'."),
            ("Likelihood (L)", "How probable the event is in the next 12 months, scored 1–5."),
            ("Impact (I)", "How bad the consequence would be for people, customers, artists or the company, "
                           "scored 1–5. For AI risks, harm to people outside the company counts fully."),
            ("Inherent risk", "The score with only the controls that already exist today."),
            ("Residual risk", "The score we expect once the planned controls are working."),
            ("Risk owner", "The one person with the authority and budget to manage the risk. Not a committee."),
            ("Treatment", "What we decide to do about the risk: modify, avoid, share or retain."),
            ("Statement of Applicability (SoA)", "The list of every Annex A control with 'applicable or not', "
                                                 "why, and whether it is in place. We keep one per standard."),
        ], [4.5, 12]),
        ("h1", "4. Roles"),
        ("table", ["Who", "What they do in this process"], [
            (who("CISO"), "Owns this methodology and the register; facilitates IS risk workshops; reviews every "
                          "new risk for consistent scoring; reports the risk picture to the " + TC + "."),
            (who("CAIO"), "Co-owns the register for AI risks; makes sure AI risks and impact-assessment results "
                          "enter the register; chairs the " + ARR + "."),
            ("Risk owners", "Agree the score, choose the treatment, own the actions, accept the residual risk "
                            "when the rules allow it, and review their risks on schedule."),
            (who("HOD"), "Brings data-quality, bias, drift and training-data risks; runs model evaluations used "
                         "as evidence for likelihood scores."),
            (who("CREA"), "Represents artists and audiences when scoring harm to people and content safety."),
            (who("DPO"), "Advises on legal, privacy and copyright consequences; checks impact scores for "
                         "notifiable breaches."),
            (TC, "Approves the scales and acceptance criteria; accepts High residual risks; reviews the top "
                 "risks every month."),
            (who("IMSC"), "Keeps the register tidy, chases overdue reviews and actions, and archives versions."),
        ], [5.5, 11]),
        ("h1", "5. The process at a glance"),
        ("steps", [
            "**Set the context** — know your scope, assets, AI systems, interested parties and legal duties "
            f"({ref('IMS-REG-001')}, {ref('IMS-REG-005')}).",
            "**Identify** risks with the prompts in section 7, and record each one in "
            f"{ref('IMS-REG-002')} with an ID, cause, consequence and owner.",
            "**Analyse** — score likelihood and impact with today's controls (inherent risk).",
            "**Evaluate** — compare the score with the risk levels and decide whether treatment is needed.",
            "**Treat** — choose an option, choose controls, check them against Annex A of both standards, plan "
            "the actions and estimate the residual risk.",
            "**Accept** — the right person signs off the residual risk (section 9).",
            "**Update the SoAs** — record each control and the risks that need it in "
            f"{ref('IMS-SOA-001')} and {ref('IMS-SOA-002')}.",
            "**Monitor and reassess** on schedule and whenever a trigger in section 11 happens.",
        ]),
        ("tip", "A good risk workshop takes 90 minutes, has 4–6 people, and uses the live register on a shared "
                "screen. Score each risk in under five minutes — if people disagree by more than one point, write "
                "down the assumption that divides them and move on. You can come back to it."),
        ("h1", "6. Risk criteria — the scales"),
        ("p", "All risks — IS and AI — are scored with these scales. Score likelihood over the next 12 months. "
              "Score impact as the **realistic worst case**, not the theoretical worst case. When a risk has "
              "several kinds of impact (money, people, rights), use the highest one."),
        ("h2", "6.1 Likelihood"),
        ("table", ["Score", "Name", "Meaning"], [(str(n), name, text) for n, name, text in LIKELIHOOD],
         [2, 3.5, 11]),
        ("h2", "6.2 Impact"),
        ("table", ["Score", "Name", "Meaning (use the highest that applies)"],
         [(str(n), name, text) for n, name, text in IMPACT], [2, 3.5, 11]),
        ("p", "For AI risks, read 'people' broadly: users, artists, people depicted in images, audiences who see "
              "generated content, and society. A risk that causes no financial loss but treats a group of artists "
              "unfairly can still be Moderate or Major."),
        ("h2", "6.3 Risk score and level"),
        ("p", "**Risk score = Likelihood × Impact** (1–25). The score gives the level:"),
        ("table", ["Level", "Score range", "What it means"],
         [(name, f"{lo}–{hi}", rule) for name, lo, hi, rule in LEVELS], [2.5, 3, 11]),
        ("h2", "6.4 Risk matrix"),
        ("table", ["Likelihood ↓ / Impact →"] + [f"{n} {name}" for n, name, _ in IMPACT], MATRIX_ROWS,
         [3.4, 2.6, 2.6, 2.6, 2.6, 2.6]),
        ("h1", "7. Identifying risks"),
        ("p", "Use whichever of the two approaches fits the situation. Both are allowed by ISO/IEC 27001, and "
              "auditors care that you are consistent, not which one you pick."),
        ("h2", "7.1 Information-security risks"),
        ("bullets", [
            f"**Asset-based** — walk through the asset inventory ({ref('IMS-REG-005')}). For each important "
            "asset ask: what threat could exploit which weakness to harm its confidentiality, integrity or "
            "availability? Example: AST-004 customer scripts + threat 'attacker scanning for open storage' + "
            "weakness 'bucket policy not checked in CI' → " + rk("RSK-IS-001") + ".",
            "**Scenario-based** — start from realistic events: phishing, ransomware, a leaked API key, a "
            "cloud-region outage, an insider copying data, a supplier breach. Then ask which assets would be "
            "hit. This is often faster for a small team.",
            "**Other sources** — pentest and scan results, incidents and near-misses in "
            f"{ref('IMS-REG-006')}, audit findings, threat intelligence, customer security questionnaires.",
        ]),
        ("h2", "7.2 AI risks"),
        ("p", "For each AI system, think about the whole life cycle — data, training or fine-tuning, testing, "
              "release, operation, change and retirement — and use these risk sources as prompts:"),
        ("table", ["Risk source", "Question to ask", f"{N} example"], [
            ("Data quality and provenance", "Is the data accurate, complete, representative — and do we have the "
                                            "right to use it?", "RSK-AI-001 — artwork without valid consent in "
                                                                "the " + SF + " fine-tuning set"),
            ("Bias and fairness", "Could outputs or decisions systematically disadvantage a group?",
             "RSK-AI-003 — " + AM + " under-exposes new or non-English-portfolio artists"),
            ("Misuse and abuse", "How could someone use the system for something we never intended?",
             "RSK-AI-002 — deceptive deepfake of a real person through " + SF),
            ("Transparency and explainability", "Do people know they are dealing with AI, and can they understand "
                                                "or challenge a result?", AM + " ranking that artists cannot "
                                                                          "understand; unlabelled AI images"),
            ("Robustness and reliability", "Does it still work on unusual inputs, under attack, or after drift?",
             "RSK-AI-004 — " + SM + " hallucinations; prompt injection in uploaded scripts"),
            ("Security of the AI system", "Could the model, prompts or data be stolen, poisoned or manipulated?",
             "Poisoned training images; leaked model weights (AST-006)"),
            ("Supplier and third-party models", "What if a supplier changes, degrades or withdraws its model?",
             "RSK-AI-005 — " + SAFE + " vendor update lowers detection"),
            ("Human oversight and use", "Will people over-trust the output or be unable to step in?",
             "Engineers accepting insecure " + CA + " suggestions without review"),
            ("Legal and societal", "Could the system break the law, infringe rights or damage public trust?",
             "Style mimicry of living artists; EU AI Act labelling duties"),
        ], [3.6, 5.6, 7.3]),
        ("p", f"The richest source of AI risks is the AI system impact assessment ({ref('IMS-PRO-002')}). Every "
              "significant negative impact found there becomes a risk in the register, linked by the AIIA ID."),
        ("h2", "7.3 Writing a good risk"),
        ("p", "Write each risk as **cause → event → consequence**, name the system or asset, and give it one "
              "owner. 'AI bias' is not a risk; 'ranking features favour artists with long rating histories, so "
              "new artists get fewer commissions and less income' is."),
        ("h1", "8. Analysing risks"),
        ("bullets", [
            "Score likelihood and impact **with the controls that exist and work today**. Planned controls do "
            "not count yet.",
            "Use evidence where you have it: red-team results, incident history, scan results, evaluation metrics. "
            "Note the evidence in the 'existing controls' column so the next reviewer can see why.",
            "For AI risks, score impact on the people affected first (from the impact assessment), then on the "
            "company, and take the higher.",
            "If you cannot agree, take the higher score and add a review date — it is cheaper to lower a score "
            "later than to explain a missed risk.",
        ]),
        ("h1", "9. Evaluating risks and acceptance criteria"),
        ("p", "The level decides what must happen and who may accept the remaining (residual) risk:"),
        ("table", ["Residual level", "Can it be accepted?", "Who may accept", "Review"], [
            ("Low (1–4)", "Yes", "Risk owner", "Yearly"),
            ("Medium (5–9)", "Yes, after treatment is considered", "Risk owner; reported to the " + TC,
             "Every 6 months"),
            ("High (10–15)", "Only with a documented reason and a plan to reduce it",
             f"{title_of('CISO')} (IS) or {title_of('CAIO')} (AI) **plus** the {TC}", "Every 3 months"),
            ("Critical (16–25)", "No", f"Nobody — stop, redesign or withdraw; tell the {title_of('CEO')} "
                                       "within 24 hours", "Weekly until resolved"),
        ], [3, 4, 6, 3.5]),
        ("bullets", [
            "Acceptance is recorded in the register: who accepted, when, and until when (maximum 12 months).",
            "Nobody may accept a risk they caused alone or a risk that breaks a law or a contract. Those must be "
            "treated or the activity stopped.",
            "AI risks with residual impact 4 or 5 on people outside the company are always reported to the "
            f"{TC}, whatever the score.",
        ]),
        ("h1", "10. Treating risks"),
        ("h2", "10.1 Treatment options"),
        ("table", ["Option", "Meaning", "Example"], [
            ("Modify", "Add or improve controls to lower likelihood or impact. The usual choice.",
             "Phishing-resistant MFA for " + rk("RSK-IS-002")),
            ("Avoid", "Stop or change the activity so the risk disappears.",
             "Not offering photorealistic face generation at all"),
            ("Share", "Move part of the impact to someone else — contract, insurance, supplier.",
             "Cyber insurance; supplier liability and notice clauses for " + SAFE),
            ("Retain", "Consciously accept the risk as it is, within the acceptance rules.",
             "Low risk of a short outage of an internal wiki"),
        ], [2.5, 6.5, 7.5]),
        ("h2", "10.2 Choosing controls and linking them to Annex A"),
        ("steps", [
            "Design the controls you actually need — start from the risk, not from the Annex A list.",
            "For each control, find the matching ISO/IEC 27001 Annex A control (5.x organisational, 6.x people, "
            "7.x physical, 8.x technological) and/or ISO/IEC 42001 Annex A control (A.2–A.10). Many AI risks "
            "need controls from both, for example a supplier model change needs 27001 5.22 and 42001 A.10.3.",
            "Write those references in the 'planned controls' columns of the register.",
            "Then go the other way: read through Annex A of both standards and ask 'have we missed anything?'. "
            "Annex A is a checklist against omission, not a shopping list.",
            "Record every Annex A control in the right SoA — applicable or not, why, the risks it treats, and "
            "whether it is implemented. Controls can also be included for legal or contract reasons, not only "
            "for risks.",
        ]),
        ("h2", "10.3 Treatment plan"),
        ("p", f"Each treated risk has at least one action in the Treatment Plan sheet of {ref('IMS-REG-002')}: "
              "what, who, due date, status and evidence. The risk owner approves the plan. Actions for High "
              "risks are due within 90 days; for Medium risks within 6 months."),
        ("h1", "11. When to reassess"),
        ("p", "The whole register is reviewed **every quarter** by the risk owners with the "
              f"{title_of('CISO')} and the {title_of('CAIO')}, and the top risks go to the {TC} every month. "
              "In addition, reassess the affected risks within **10 working days** when any of these triggers "
              "happen:"),
        ("bullets", [
            "A new AI system, a new model version, a new fine-tuning dataset, or a significant change in "
            "intended use (this also triggers an impact assessment).",
            "A supplier changes its model, terms, data location or retention (lesson from INC-2026-007).",
            "A security or AI incident, a near-miss, or a monitoring alert such as fairness or drift thresholds "
            "being breached.",
            "New infrastructure, a new cloud region, or a major architecture change.",
            "New laws, regulator guidance or customer contract terms.",
            "Audit findings, pentest results or a red-team exercise.",
            "Changes to the business: new product, new market, acquisition, big headcount change.",
        ]),
        ("pagebreak",),
        ("h1", "12. Worked example — two risks end to end"),
        ("p", "These two risks show that one method handles an AI risk and an information-security risk in "
              f"exactly the same way. Both are in {ref('IMS-REG-002')}."),
        ("h2", "12.1 " + AI2[0] + " — " + AI2[1]),
        ("table", ["Step", "What we did"], [
            ("Identify", f"Found during AIIA-2026-01 for {SF} ({AI2[2]}). Cause: users write prompts naming real "
                         f"people or use jailbreak phrasing; {SAFE} does not catch every case. Event: a "
                         "realistic, fabricated image of a real person is generated and delivered. Consequence: "
                         "damage to that person's reputation, deception of the public, breach of EU AI Act "
                         "deepfake transparency duties, loss of customer trust."),
            ("Owner", who(AI2[3])),
            ("Analyse", f"Existing controls: {SAFE} screening, visible 'AI-assisted' label, C2PA content "
                        "credentials. Evidence: an internal red-team of 200 attempts found 2 bypasses. "
                        f"Likelihood {AI2[4]} (Possible). Impact {AI2[5]} (Severe — harm to a real person and "
                        "widespread deception)."),
            ("Evaluate", f"Inherent score {score_text(AI2[4], AI2[5])}. Must be treated."),
            ("Treat", "Option: Modify. Planned controls: red-team and likeness testing before every release "
                      "(42001 A.6.2.4); daily canary test set and output monitoring in operation (42001 A.6.2.6); "
                      f"{SAFE} supplier agreement with model-change notice and version pinning (42001 A.10.3); "
                      "abuse alerting and account suspension rules (27001 8.16); our own named-person check "
                      "before image delivery."),
            ("Residual", f"Likelihood {AI2[6]} (Unlikely) because two independent filters must fail. Impact "
                         f"{AI2[7]} (Major) because labels, credentials and fast takedown limit the spread. "
                         f"Residual score {score_text(AI2[6], AI2[7])}."),
            ("Accept", f"Medium — accepted by the risk owner, {person(AI2[3])}, until the next 6-monthly review; "
                       f"reported to the {TC} because residual impact on people is 4."),
            ("SoA", f"{ref('IMS-SOA-002')}: A.6.2.4, A.6.2.6 and A.10.3 marked applicable with 'RSK-AI-002' as "
                    f"justification. {ref('IMS-SOA-001')}: 8.16 lists RSK-AI-002 alongside security risks."),
            ("Reassess", "Triggered again by INC-2026-007 in August 2026 (vendor update): scores confirmed, "
                         "daily canary runs extended for 30 days."),
        ], [2.5, 14]),
        ("h2", "12.2 " + IS2[0] + " — " + IS2[1]),
        ("table", ["Step", "What we did"], [
            ("Identify", f"Scenario-based workshop on {AST[IS2[2]][1]} ({IS2[2]}). Cause: targeted phishing "
                         "with a fake login page; one-time codes can be relayed by the attacker. Event: an "
                         "engineer's account is taken over. Consequence: production access, possible theft of "
                         "customer scripts and model weights, notifiable breach."),
            ("Owner", who(IS2[3])),
            ("Analyse", "Existing controls: SSO with app-based one-time codes, yearly awareness training. "
                        f"Evidence: two credential-phishing attempts against staff last quarter. Likelihood "
                        f"{IS2[4]} (Possible). Impact {IS2[5]} (Severe)."),
            ("Evaluate", f"Inherent score {score_text(IS2[4], IS2[5])}. Must be treated."),
            ("Treat", "Option: Modify. Planned controls: passkeys or security keys for everyone (27001 5.17 and "
                      "8.5); just-in-time, approved production access for engineers (8.2); quarterly phishing "
                      "simulations and a one-click report button (6.3)."),
            ("Residual", f"Likelihood {IS2[6]} (Rare) because phishing-resistant MFA defeats relayed codes. "
                         f"Impact stays {IS2[7]} — if it did happen, the damage would be the same. Residual score "
                         f"{score_text(IS2[6], IS2[7])}."),
            ("Accept", f"Medium — accepted by {person(IS2[3])} as risk owner; review every 6 months."),
            ("SoA", f"{ref('IMS-SOA-001')}: 5.17, 6.3, 8.2 and 8.5 applicable, justification 'RSK-IS-002'."),
        ], [2.5, 14]),
        ("example", "What the two examples teach", [
            "Controls usually reduce likelihood more than impact. That is normal — do not lower impact unless a "
            "control really limits the damage.",
            "One risk can need controls from both Annex A lists. Record both; it is a sign the integration works.",
            "Write the evidence for each score. Next quarter you will not remember why you chose a 3.",
        ]),
        ("h1", "13. Records"),
        ("bullets", [
            f"{ref('IMS-REG-002')} — risk register, treatment plan, heat map (versioned each quarter).",
            f"{ref('IMS-SOA-001')} and {ref('IMS-SOA-002')}.",
            "Workshop notes, red-team and test results used as evidence for scores.",
            f"Risk acceptance records and {TC} minutes ({ref('IMS-PRO-008')}).",
            f"Keep risk records for at least 3 years, in line with {ref('IMS-PRO-004')}.",
        ]),
        ("h1", "14. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-REG-002", "IMS-PRO-002", "IMS-SOA-001", "IMS-SOA-002",
                                      "IMS-REG-003", "IMS-REG-005", "IMS-PRO-005", "IMS-PRO-008")]),
    ],
}
