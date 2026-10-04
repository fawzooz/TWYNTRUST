from org import AI_SYSTEMS, COMMITTEES, KEY_RISKS, ORG, SAMPLE_INCIDENT, TECH, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
SF, SM, AM, SAFE, CA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
ARR = next(k for k in COMMITTEES if "Release" in k)
TC = next(k for k in COMMITTEES if "Council" in k)
RISK = {r[0]: r for r in KEY_RISKS}

DOC = {
    "id": "IMS-POL-002",
    "summary": f"One lifecycle for all software and AI work at {N}: from idea to retirement, with security, "
               "privacy and responsible-AI checks built into the same gates, the same tools and the same "
               "definition of done.",
    "clauses": {"27001": "8.1, 6.3; Annex A 5.8, 8.4, 8.8, 8.9, 8.25–8.34",
                "42001": "8.1, 6.3; Annex A.6.1.2–A.6.1.3, A.6.2.2–A.6.2.8 (data stages via A.7.2–A.7.6)"},
    "howto": [
        "Start from what your engineers already do (pull requests, CI, releases). Add gates to that flow — "
        "do not invent a parallel paper process that nobody follows.",
        "The gate checklist (section 5) and the definition of done (section 6) are the parts auditors test "
        "most. Make sure your tools can show evidence for every 'must' line.",
        "If you do not train or fine-tune models yourself, keep the G3 'data and model' stage but shrink it to "
        f"supplier-model evaluation (see the {SM} and {SAFE} rows in section 4.2).",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"Most security and AI failures are designed in, not bolted on. A storage bucket left public, a "
              "dependency nobody patched, a training set nobody checked for consent, a content filter updated "
              f"without a test — each one starts as a small decision during development. This policy makes sure "
              f"those decisions are made deliberately, by the right people, with evidence, at {N}."),
        ("p", "It defines **one secure and responsible development lifecycle** (we call it the SDLC) that every "
              "change to our software and AI systems follows. Application security (AppSec) and responsible-AI "
              "controls live in the same stages and the same gates, so engineers learn one way of working and "
              "auditors for both ISO/IEC 27001 and ISO/IEC 42001 see one set of records."),
        ("h1", "2. Scope"),
        ("bullets", [
            f"All code, infrastructure-as-code and configuration for {', '.join(p.split(' — ')[0] for p in ORG['products'])}.",
            f"All AI systems in the inventory ({ref('IMS-REG-005')}), whatever our role: systems we build and "
            f"fine-tune ({SF}, {AM}), systems we integrate from a supplier model ({SM}), and AI services we "
            f"rely on as a control or a tool ({SAFE}, {CA}).",
            "Work by employees, freelance contractors and outsourced developers (27001 Annex A 8.30).",
            "Changes that come from suppliers — for example a new version of a foundation model or of the "
            f"{SAFE} classifier — are treated as changes to our system and enter the lifecycle at G0.",
        ]),
        ("std", [
            "ISO/IEC 27001 asks for rules for secure development, security requirements defined up front, secure "
            "architecture principles, secure coding, security testing before acceptance, separated environments, "
            "controlled changes, protected test data, and timely handling of technical vulnerabilities "
            "(Annex A 8.25–8.34 and 8.8), with security considered in every project (5.8).",
            "ISO/IEC 42001 asks you to set objectives for responsible AI development, define the processes for it, "
            "and then control each lifecycle step: requirements, design documentation, verification and validation, "
            "deployment, operation and monitoring, technical documentation and event logs (Annex A.6.1.2–A.6.2.8).",
            "Both standards (Clause 8.1) want operations planned and controlled, including planned changes, and "
            "outsourced processes kept under control. One gated lifecycle satisfies both.",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Responsibility in the lifecycle"], [
            (who("CTO"), "Owns this policy and the engineering toolchain. Approves G1, G2 and G6 for "
                         "non-AI changes. Owns OBJ-04 (vulnerability fix times)."),
            (who("CAIO"), f"Chairs the {ARR} (gate G5). Owns AI impact assessments and approves AI design (G1) "
                          "and evaluation plans."),
            (who("CISO"), "Sets secure coding and testing standards, maintains the threat-model templates, "
                          "triages scanner findings, signs off penetration tests, member of the release review."),
            (who("HOD"), "Owns the data and model stage (G3): datasets, training runs, evaluation and the model "
                         f"registry. Follows {ref('IMS-POL-003')}."),
            (who("CREA"), "Signs off content-safety and red-team results for image-generating systems."),
            (who("DPO"), "Advises on privacy by design and on the need for a DPIA; reviews new data uses."),
            (who("SRE"), "Owns environments, CI/CD hardening, deployment, monitoring, rollback and backups."),
            ("Security Champion (one per squad)", "An engineer with 2–4 hours a week to run threat-model sessions, "
             "review risky pull requests and be the first contact for scanner questions."),
            ("Product owner", "Writes the requirements, including security and responsible-AI acceptance "
             "criteria; owns the change ticket from G0 to G6."),
            ("Every engineer", "Follows the secure coding standard, never merges their own code without review, "
             "and reports weaknesses through #trust-report."),
        ], [5.5, 11]),
        ("h1", "4. The lifecycle"),
        ("p", "The lifecycle has nine stages. Seven of them end in a **gate**: a short, recorded check that the "
              "stage's evidence exists. Gates are light for small changes and heavy for risky ones (see 4.1). "
              "A gate is a pull-request checklist, a ticket field or a meeting — whatever leaves a record."),
        ("table", ["Stage", "What happens", "Gate / evidence"], [
            ("**G0 Idea and requirements**", "Classify the change (4.1). Write functional, security, privacy and "
             "responsible-AI requirements as acceptance criteria. Check legal duties (e.g. EU AI Act Art. 50 "
             "labelling). Decide if an AI impact assessment or DPIA is needed.",
             "Change ticket with class, requirements and AIIA/DPIA decision"),
            ("**G1 Design**", "Data-flow diagram, threat model (STRIDE plus the AI threats in 4.3), secure design "
             "principles, human-oversight design, model and supplier choice.",
             "Threat model; design note; AIIA started or updated"),
            ("**G2 Build**", "Secure coding standard, peer review, SAST, SCA, secret scanning, IaC scanning, "
             "dependency policy, separated environments.", "Green CI pipeline; approved pull requests"),
            ("**G3 Data and model development**", "Data acquisition with licence/consent checks, provenance, "
             "preparation, training or fine-tuning, model card, evaluation plan.",
             "Dataset record; training log; model card draft"),
            ("**G4 Verification and validation**", "Functional, security (DAST, pen test where needed) and AI "
             "evaluation: accuracy, fairness, robustness, safety red-teaming, privacy leakage tests.",
             "Test report; evaluation report against thresholds"),
            ("**G5 AI Release Review**", f"Go / no-go by the {ARR} for new or significantly changed AI systems.",
             "Signed release record; updated risk register and AIIA"),
            ("**G6 Deployment**", "Automated deploy from CI, canary or staged rollout, rollback plan tested, "
             "user information and labels in place.", "Deployment record; release notes"),
            ("Operation and monitoring", "Security monitoring, vulnerability management, AI drift, abuse and "
             "content-safety canaries, user feedback, event logs.", "Dashboards; monthly monitoring review"),
            ("Change and retirement", "Every change re-enters at G0. Retirement removes access, data and models "
             "safely and tells affected users.", "Change ticket; retirement checklist"),
        ], [3.6, 8.4, 4.5]),
        ("h2", "4.1 Change classes — how heavy are the gates?"),
        ("table", ["Class", "Examples", "Gates required"], [
            ("Standard", "Copy fix, UI tweak, dependency patch with no breaking change",
             "G2 (automated) + peer review; G6 automated"),
            ("Normal", "New feature in Canvas, new API endpoint, new data field",
             "G0–G2, G4 (security tests), G6; threat model if it touches auth, payments, personal or customer data"),
            ("Significant AI change", "New AI system; new or retrained model; new training data source; new "
             "supplier model version; change of intended use; change to a safety filter or threshold",
             f"All gates G0–G6, including G3 and the {ARR} (G5)"),
            ("Emergency", "Fix for an actively exploited vulnerability or an AI incident",
             "Fix first with two-person approval; complete the missing gate records within 5 working days"),
        ], [3.2, 7.3, 6]),
        ("tip", "Put the change class as a required field in your pull-request template or ticket. When it says "
                "'Significant AI change', your CI can automatically block the release until the release-review "
                "record is linked. That single automation produces most of your audit evidence for A.6.2."),
        ("h2", "4.2 Our AI systems in the lifecycle"),
        ("table", ["System", "Our role", "How the lifecycle applies"], [
            (SF, "Provider and producer", "Full lifecycle. Every fine-tune or base-model upgrade is a "
             f"Significant AI change. Content-safety red-team by the {title_of('CREA')}."),
            (SM, "Provider (supplier model)", "No training. G3 becomes supplier-model evaluation: hallucination "
             "and cross-session leakage tests before any model version change."),
            (AM, "Provider and producer", "Full lifecycle; fairness evaluation against OBJ-06 is a release "
             "blocker."),
            (SAFE, "Customer / user", "Vendor model updates are changes to our control. Canary test set must "
             f"pass before a new version is accepted (lesson from {SAMPLE_INCIDENT['id']})."),
            (CA, "Customer / user", "Tool, not product. Suggestions are treated like any untrusted code: "
             "reviewed and scanned in G2. Settings checked yearly."),
        ], [3, 3.6, 9.9]),
        ("h2", "4.3 Threat modelling, including AI threats"),
        ("p", "Threat modelling means sitting down before you build and asking 'what could go wrong, and what will "
              "we do about it?'. We use a 45–60 minute session run by the Security Champion, with the developer, "
              "the product owner and, for AI systems, someone from the data and ML team."),
        ("steps", [
            "Draw the data-flow diagram: users, services, data stores, suppliers, trust boundaries.",
            "Mark entry points (UI, API, prompts, uploaded files, training-data feeds, supplier model calls).",
            "Walk STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation "
            "of privilege) across each element.",
            "For AI components, add the AI threat list below and the OWASP Top 10 for LLM Applications.",
            f"Score each credible threat with the scales in {ref('IMS-PRO-001')}; record High and Critical "
            f"ones in {ref('IMS-REG-002')}.",
            "Agree mitigations, write them as acceptance criteria, and re-visit the model when the design changes.",
        ]),
        ("table", ["AI threat", "What it looks like at " + N, "Typical mitigations"], [
            ("Prompt injection (direct and indirect)", f"A script uploaded to {SM} contains hidden text telling "
             "the model to reveal other projects or ignore rules", "Separate system and user content; output "
             "filtering; no tool access beyond the session; tenant isolation tested in G4"),
            ("Data and model poisoning", f"Mislabelled or malicious images slipped into the {SF} fine-tuning set",
             "Licensed sources only; provenance and hash checks; review of new batches; held-out canary images"),
            ("Model theft and extraction", "Bulk API calls used to copy fine-tuned weights or behaviour",
             "Weights in Restricted storage; rate limits and quotas per key; anomaly alerts on API usage"),
            ("Sensitive information disclosure", "Model outputs fragments of another customer's script or an "
             "artist's private portfolio", "Zero-retention supplier terms; no customer data in training without "
             "opt-in; leakage tests"),
            ("Filter evasion / jailbreak", "Prompt wording that gets a real-person deepfake past filters",
             f"Layered filters ({SAFE} + our likeness check); red-team set; canaries (see {RISK['RSK-AI-002'][0]})"),
            ("Supply-chain change", "Supplier silently updates a model", "Version pinning and change notice "
             f"({ref('IMS-POL-006')}); evaluation before switch"),
            ("Improper output handling / excessive agency", "Generated text inserted into HTML without encoding; "
             "model allowed to call internal tools", "Treat model output as untrusted input; least-privilege "
             "tools; human approval for actions"),
            ("Unbounded consumption", "Abuse that runs up GPU or API costs", "Quotas, budgets and alerts per "
             "customer"),
        ], [3.6, 6.4, 6.5]),
        ("h2", "4.4 Build: secure coding and the pipeline"),
        ("p", f"Our toolchain: {TECH['sdlc']}. The rules below apply to every repository."),
        ("bullets", [
            "**Secure coding standard** — we follow the OWASP Top 10 and OWASP ASVS level 2 for web and API code. "
            "Key habits: validate input with allow-lists, encode output, use parameterised queries, use the "
            "framework's authentication and session handling, never roll our own crypto, give generic error "
            "messages and log the details securely, and never log secrets or personal data.",
            "**Peer review** — every pull request needs one approving reviewer who is not the author; two for "
            "changes to authentication, payments, infrastructure or AI safety filters. Branch protection enforces "
            "this, including for administrators.",
            "**SAST** (static analysis) runs on every pull request; new High or Critical findings block the merge.",
            "**SCA** (software composition analysis) checks dependencies for known vulnerabilities and licences; "
            "automated update pull requests are opened weekly.",
            "**Secret scanning** with push protection on GitHub, plus a pre-commit hook. A leaked secret is "
            "revoked and rotated within 4 hours, even if the commit was never pushed.",
            "**IaC scanning** checks infrastructure templates for public buckets, open security groups and "
            "missing encryption before they are applied.",
            "**Dependency policy** — prefer well-maintained libraries; pin versions with lock files; no new "
            "dependency with fewer than two maintainers or no release in 18 months without Security Lead approval; "
            "model files and datasets from public hubs are scanned and pinned by hash like code.",
            "**AI-generated code** from the approved assistant is reviewed exactly like human code. Engineers stay "
            f"responsible for what they merge ({ref('IMS-POL-005')}).",
            "**Environments** — development, staging and production are separate AWS accounts. Engineers have no "
            "standing write access to production; deploys run from CI only. Production customer data is never "
            "copied to development or test; we use synthetic or masked data (27001 8.31, 8.33).",
            f"**Source code access** — repositories are private, access is by SSO group and reviewed quarterly "
            f"({ref('IMS-POL-004')}).",
        ]),
        ("h2", "4.5 Data and model development"),
        ("p", f"Data stages follow {ref('IMS-POL-003')}. In the lifecycle this means: every training or "
              "evaluation dataset has a dataset record (source, licence or consent basis, version, hash, "
              "known limitations); every training run is reproducible from versioned code, data and parameters; "
              "every model in the registry has a model card describing intended use, limitations, evaluation "
              "results and the human-oversight measures. Evaluation thresholds are agreed at G1, before anyone "
              "sees the results."),
        ("h2", "4.6 Verification and validation"),
        ("table", ["Test", "When", "Pass criteria (examples)"], [
            ("Unit, integration and regression", "Every pull request", "All tests green"),
            ("DAST (dynamic scan of running app)", "Weekly on staging; before each Normal release",
             "No new High or Critical"),
            ("External penetration test", "Yearly and before a major new product",
             "Criticals fixed before go-live; Highs within 30 days"),
            ("Quality / accuracy", "Every model change", "Agreed metric no worse than current version"),
            ("Fairness", f"Every {AM} change; {SF} depiction tests", f"{AM} exposure ratio ≥ 0.8 (OBJ-06)"),
            ("Robustness and safety red-team", f"Every {SF}/{SM} model change", "Zero passes on the prohibited-"
             "content set; deepfake likeness set blocked ≥ 99%"),
            ("Privacy leakage", "Model or prompt-template change", "No cross-tenant content in 500 probe prompts"),
            ("Content credentials and labels", f"Every {SF} release", "C2PA manifest and 'AI-assisted' label "
             "present on 100% of sampled outputs"),
        ], [4.5, 5.3, 6.7]),
        ("h2", "4.7 AI Release Review (G5)"),
        ("p", f"The {ARR} decides go, go-with-conditions or no-go for every Significant AI change. Its members "
              f"and quorum are set in {ref('IMS-GOV-001')}. It reviews the AI impact assessment "
              f"({ref('IMS-PRO-002')}), the evaluation report, open risks, red-team results and the monitoring "
              "plan. A no-go is normal and healthy; the record says what must change. Conditions have an owner "
              "and a date and are tracked to closure."),
        ("h2", "4.8 Deployment, operation and monitoring"),
        ("bullets", [
            "Deploys run only from CI, are signed and logged, and can be rolled back in under 15 minutes. "
            "AI models are deployed by registry version, so rollback means pointing back to the previous version.",
            "Significant AI changes go to 5% of traffic (or internal users) for at least 48 hours before full rollout.",
            "**Vulnerability management** (27001 8.8) — fix production vulnerabilities by severity: Critical "
            "within 7 days, High within 30 days, Medium within 90 days (OBJ-04). Exceptions go to the risk register.",
            "**AI monitoring** (42001 A.6.2.6) — monthly review of quality metrics and input drift; daily automated "
            f"content-safety canary set through {SF} and {SAFE}; weekly {AM} fairness metric; alerts on abuse "
            "patterns such as mass prompt variations or quota spikes.",
            "**Event logs** (42001 A.6.2.8, 27001 8.15) — we keep prompts, model version, filter decisions and "
            "output IDs for 90 days (customer content is stored encrypted and accessed only for incidents).",
            f"Anything odd is reported and handled through {ref('IMS-PRO-005')}.",
        ]),
        ("h2", "4.9 Change management and retirement"),
        ("p", "All changes — ours or a supplier's — go through a ticket and the right class of gates (27001 8.32; "
              "both standards' Clause 6.3 and 8.1). Supplier model changes are on the change trigger list. When a "
              "system or model is retired we: tell affected customers at least 30 days ahead (unless retiring for "
              "safety), revoke keys and service accounts, delete or archive data and weights according to the "
              f"retention schedule in {ref('IMS-POL-003')}, archive the model card and last evaluation for 3 years, "
              f"and update {ref('IMS-REG-005')}."),
        ("h1", "5. Gate checklist"),
        ("p", "Copy this table into your pull-request or ticket template. 'Must' items block the gate; 'Should' "
              "items need a reason if skipped."),
        ("table", ["Gate", "Checklist item", "Level", "Evidence", "Approver"], [
            ("G0", "Change class set; requirements include security, privacy and responsible-AI criteria", "Must",
             "Ticket", "Product owner"),
            ("G0", "AIIA / DPIA needed? Decision recorded", "Must", "Ticket field", title_of("CAIO")),
            ("G1", "Threat model done (STRIDE + AI threats) for Normal/Significant changes", "Must",
             "Threat model file", "Security Champion"),
            ("G1", "Human-oversight and fallback design described", "Must (AI)", "Design note", title_of("CAIO")),
            ("G1", "Evaluation metrics and thresholds agreed before testing", "Must (AI)", "Evaluation plan",
             title_of("HOD")),
            ("G2", "Peer review, SAST, SCA, secret and IaC scans green", "Must", "CI run", "Automated"),
            ("G2", "No new dependency outside the dependency policy", "Must", "SCA report", "Security Champion"),
            ("G3", "Every dataset has licence/consent and provenance record", "Must (AI)", "Dataset record",
             title_of("HOD")),
            ("G3", "Training reproducible; model card drafted", "Must (AI)", "Registry entry", title_of("HOD")),
            ("G4", "Security tests passed (DAST; pen test where required)", "Must", "Test report", title_of("CISO")),
            ("G4", "Quality, fairness, robustness, safety and leakage tests meet thresholds", "Must (AI)",
             "Evaluation report", title_of("HOD")),
            ("G5", "Release review decision recorded; risk register and AIIA updated", "Must (Significant AI)",
             "Release record", title_of("CAIO")),
            ("G6", "Rollback tested; monitoring and alerts live; labels and user information updated", "Must",
             "Deployment record", title_of("SRE")),
            ("G6", "Customer or artist communication sent where behaviour changes", "Should", "Release notes",
             "Product owner"),
        ], [1.2, 6.8, 2.3, 2.8, 3.4]),
        ("h1", "6. Definition of done"),
        ("p", "A piece of work is 'done' only when every line that applies is true. This is the same list for "
              "ordinary features and AI features; AI work simply has more lines."),
        ("table", ["Area", "Done means…", "Applies to"], [
            ("Code", "Reviewed by someone else, merged to main, all CI checks green", "All"),
            ("Security", "No new High/Critical findings; secrets in the secrets manager; least-privilege IAM", "All"),
            ("Tests", "Automated tests cover the new behaviour, including one abuse case", "All"),
            ("Documentation", "README / runbook updated; design note and threat model linked", "Normal +"),
            ("Logging", "Security-relevant and AI events logged without secrets or personal data", "Normal +"),
            ("Data", "Dataset records complete; no data without a licence or consent basis", "AI"),
            ("Model", "Model card complete; registry version tagged; previous version kept for rollback", "AI"),
            ("Evaluation", "All thresholds met, or a documented exception accepted by the risk owner", "AI"),
            ("Transparency", "Outputs labelled; user-facing help explains limits and how to report problems", "AI"),
            ("Oversight", "Named owner; kill-switch or feature flag tested", "AI"),
            ("Records", "Inventory, risk register and AIIA updated", "Significant AI"),
        ], [3, 10.5, 3]),
        ("pagebreak",),
        ("h1", f"7. Worked example — a {SF} model update"),
        ("example", f"{SF} v2.4: new fine-tune plus base-model upgrade", [
            f"**G0 (2 Sept 2026).** The product owner opens a ticket: fine-tune {SF} on 3,200 newly licensed "
            "images from the Q3 artist intake, and move to the image-model supplier's new base version. Class: "
            f"Significant AI change. {person('CAIO')} decides the AIIA for AI-SYS-001 needs updating; "
            f"{person('DPO')} confirms no new personal data, so no new DPIA.",
            f"**G1 (5 Sept).** The threat-model session adds one new threat: the new base version accepts longer "
            f"prompts, which could make filter evasion easier ({RISK['RSK-AI-002'][0]}). Mitigation: cap prompt "
            "length and add 40 new jailbreak prompts to the red-team set. Thresholds are agreed in advance.",
            "**G2 (8–12 Sept).** Integration code changes pass review, SAST and SCA. SCA flags a High vulnerability "
            "in an image-processing library; it is upgraded before merge.",
            f"**G3 (9–16 Sept).** {person('HOD')}'s team checks every new image against the consent and licence "
            f"ledger. 41 images from one agency have a licence that does not cover AI training; they are "
            f"quarantined ({RISK['RSK-AI-001'][0]}). The training run is logged with data hash, code commit and "
            "parameters; the model card is drafted.",
            f"**G4 (17–19 Sept).** Quality improves. Red-team: 2 of 240 deepfake prompts pass the filters — "
            f"above the threshold. {person('CREA')} records a fail. The team adds the prompts to the likeness "
            "check and re-tests: 0 of 240 pass. C2PA labels present on 100% of 200 sampled images.",
            f"**G5 (22 Sept).** The {ARR} approves 'go with conditions': daily canary for 30 days, and the "
            "base-model version is pinned in the supplier console. Risk register and AIIA updated.",
            f"**G6 (24 Sept).** {person('SRE')} deploys v2.4 to internal users and 5% of customers for 48 hours, "
            "then 100%. Rollback to v2.3 tested in staging. Release notes tell customers about the quality change.",
            "**Operation.** Canary results stay green; the 30-day condition is closed on 24 Oct and the record is "
            "linked from the inventory.",
        ]),
        ("h1", "8. Records produced"),
        ("bullets", [
            "Change tickets and pull requests with gate checklists (GitHub).",
            "Threat models and design notes (repository /docs folder).",
            "CI scan results, SAST/SCA/secret-scanning reports, DAST and penetration-test reports.",
            "Dataset records, training logs, model cards and evaluation reports (model registry).",
            f"{ARR} records and conditions; updated AIIA and risk register entries.",
            "Deployment records, monitoring dashboards and monthly monitoring review notes.",
            "Retirement checklists.",
        ]),
        ("h1", "9. Exceptions and compliance"),
        ("p", "Gates can be skipped only with an exception approved by the Security Lead (security items) or the "
              f"Head of AI (AI items), recorded in {ref('IMS-REG-002')} with an expiry date. Repeated bypasses "
              f"are nonconformities and go to {ref('IMS-PRO-009')}. The {TC} reviews gate metrics (releases with "
              "complete records — OBJ-02; vulnerability fix times — OBJ-04) every quarter."),
        ("tip", "Measure, do not police. A simple monthly count of 'releases with all gate records' versus 'all "
                "releases' tells you where the process is too heavy. If a gate is skipped often, fix the gate."),
        ("h1", "10. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-POL-003", "IMS-POL-004", "IMS-POL-005", "IMS-POL-006",
                                      "IMS-PRO-001", "IMS-PRO-002", "IMS-PRO-005", "IMS-REG-002", "IMS-REG-005")]),
    ],
}
