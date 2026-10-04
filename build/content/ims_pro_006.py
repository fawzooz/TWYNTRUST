from org import AI_SYSTEMS, KEY_RISKS, OBJECTIVES, ORG, TECH, level_for, person, ref, title_of, who

N = ORG["name"]
SYS = {a["id"]: a["name"] for a in AI_SYSTEMS}
STF, SCM, ARM, SFR, CDA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
R4 = {r[0]: r for r in KEY_RISKS}["RSK-IS-004"]
OBJ7 = {o[0]: o for o in OBJECTIVES}["OBJ-07"]

DOC = {
    "id": "IMS-PRO-006",
    "summary": f"How {N} keeps Canvas, the API, Commons and its AI features running — or degrades them safely — "
               "when a cloud region, a model supplier or a key person is unavailable, and how we recover data. "
               "Includes the business impact analysis, backup strategy, invocation steps and test plan.",
    "clauses": {"27001": "Annex A 5.29, 5.30, 8.13, 8.14, 5.23; Clause 8.1",
                "42001": "Annex A.4.5, A.6.2.6, A.10.3; Clauses 6.1, 8.1"},
    "howto": [
        "Start with the business impact analysis (section 4). Ask each product owner: 'How long can this be down "
        "before customers leave or artists cannot get paid?' The answer is your maximum tolerable outage.",
        "RTO and RPO numbers only mean something once tested. Put the test dates in your audit evidence folder.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"{N} has no data centre of its own. Everything runs in the cloud, on supplier APIs and on staff "
              "laptops. That makes us resilient to many local problems, but dependent on a few suppliers. This plan "
              "says what we do when one of them, or something of ours, fails: how fast each service must come back, "
              "how much data we can afford to lose, and how AI features fall back safely instead of failing in "
              "harmful ways."),
        ("p", "It is one plan for both standards. For information security it covers continuity of security during "
              "disruption and ICT readiness. For AI it makes sure that, when AI resources fail, systems stop or "
              "degrade in a controlled way — and that safety controls are never the part that is skipped to keep "
              "the lights on."),
        ("h1", "2. Scope"),
        ("bullets", [
            "Customer services: Canvas, the API and Commons, and the AI systems inside them (" +
            ", ".join(SYS[k] for k in ("AI-SYS-001", "AI-SYS-002", "AI-SYS-003", "AI-SYS-004")) + ").",
            "Supporting platforms: production cloud (" + TECH["cloud"] + "), identity and single sign-on, source "
            "code and CI/CD, secrets manager, log platform.",
            "Critical suppliers: the cloud provider, foundation-model and image-model APIs, the content-moderation "
            "vendor, the payment processor.",
            "People: key-person dependencies in a 34-person company.",
        ]),
        ("p", "Out of scope: total loss of the company or its funding. Those are business risks handled by the "
              "Trust Council outside this plan."),
        ("std", [
            "ISO/IEC 27001 Annex A expects you to keep information secure during a disruption (5.29), to plan, "
            "implement and test ICT readiness based on continuity objectives (5.30), to keep and test backups "
            "(8.13) and to build in enough redundancy to meet availability needs (8.14).",
            "ISO/IEC 42001 has no continuity clause of its own, but expects you to document and provide the "
            "computing resources your AI systems depend on (A.4.5), monitor AI systems in operation (A.6.2.6) and "
            "manage suppliers so their failures do not compromise responsible AI (A.10.3).",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Who", "Responsibility"], [
            ("Plan owner and Recovery Lead", who("SRE"),
             "Maintains this plan, runs backups and failover tests, leads technical recovery."),
            ("Continuity Decision-maker", who("CEO") + "; deputy " + who("CTO"),
             "Formally invokes the plan, approves spending and customer messaging."),
            ("Security during disruption", who("CISO"),
             "Makes sure emergency changes keep access control, logging and encryption in place."),
            ("AI fallback owner", who("CAIO"),
             "Decides when AI features degrade or switch provider; confirms safety controls before restart."),
            ("Customer and artist communication", who("CREA") + " with account owners",
             "Status page, customer emails, artist notices."),
            ("Supplier liaison", who("DPO"), "Contract terms, supplier escalation, alternative-provider terms."),
            ("Plan administration", who("IMSC"), "Contact lists, test calendar, evidence of tests."),
        ], [4, 5, 7.5]),
        ("h1", "4. Business impact analysis"),
        ("p", "The table below is our business impact analysis (BIA). **MTPD** is the maximum tolerable period of "
              "disruption — after that, serious damage is done. **RTO** (recovery time objective) is how quickly we "
              "aim to restore. **RPO** (recovery point objective) is the most data we accept losing, measured in "
              f"time. Targets support objective {OBJ7[0]} ({OBJ7[1].lower()}: {OBJ7[3]} monthly)."),
        ("table", ["Service / resource", "Impact if down", "MTPD", "RTO", "RPO", "Fallback"], [
            ("Canvas web app", "Customers cannot work on projects; enterprise SLA credits after 4 hours",
             "24 h", "8 h", "15 min", "Region failover (section 6)"),
            ("API", "Agency integrations fail; contractual SLA", "24 h", "8 h", "15 min", "Region failover"),
            ("Customer scripts and project files", "Loss would breach contracts and destroy trust", "—",
             "8 h", "≈ 0 (versioned, replicated)", "Restore from cross-region replica"),
            ("Commons marketplace", "Artists cannot accept commissions; payouts delayed", "72 h", "24 h", "1 h",
             "Read-only mode; payments stay with processor"),
            (STF, "No new panels; human artists still available", "72 h", "24 h", "24 h (model registry)",
             "Queue jobs; offer human commission"),
            (SCM, "Writing assistant unavailable", "5 days", "24 h", "n/a", "Manual mode; alternative model"),
            (ARM, "Recommendations unavailable", "5 days", "72 h", "24 h",
             "Transparent simple ordering"),
            (SFR, "Generation must stop — safety control", "n/a", "4 h", "n/a",
             "Fail closed; backup moderation vendor"),
            ("Artist consent and licence ledger", "Fine-tuning must pause", "10 days", "48 h", "1 h",
             "Freeze all training until restored"),
            ("Single sign-on and identity", "Nobody can log in to admin tools", "8 h", "4 h", "n/a",
             "Two sealed break-glass accounts"),
            ("Source code and CI/CD", "Cannot ship fixes", "5 days", "48 h", "0 (distributed git)",
             "Local clones; manual deploy runbook"),
            ("Business SaaS (finance, HR)", "Admin delays", "10 days", "5 days", "24 h", "Supplier recovery"),
        ], [3.3, 4.5, 1.5, 1.4, 2.6, 3.2]),
        ("tip", "Do not set every RTO to 'one hour'. Each hour you shave off costs money (standby capacity, "
                "engineering time). Set targets the business truly needs, then prove you can meet them."),
        ("h1", "5. External model APIs and AI fallback"),
        ("p", f"Three of our AI systems depend on suppliers ({TECH['foundation_model']}). Their outages, sudden "
              "model changes or withdrawn versions are our most likely continuity events. Rules:"),
        ("steps", [
            "**Degrade gracefully.** Each AI feature has a kill switch and a non-AI fallback "
            f"(see {ref('IMS-PRO-005')} section 6). The product tells users plainly that the feature is paused.",
            f"**Never fail open on safety.** If {SFR} is unavailable, slow or unreliable, image generation stops. We "
            "never deliver unscreened images to keep the service up.",
            f"**Alternative provider.** For {SCM} we keep a second foundation-model provider under contract with the "
            "same no-training and retention terms. Switching is a configuration change, tested twice a year. A "
            "switch counts as a significant change: the Head of AI confirms the quick evaluation set passes first.",
            f"**Backup moderation.** For {SFR} a second moderation vendor is contracted in standby; it can screen "
            "traffic within 4 hours at a lower throughput.",
            "**Version pinning.** We pin supplier model versions where the supplier allows it, so that a supplier "
            "update cannot silently change behaviour during a disruption.",
            "**Model weights we own** (fine-tuned models, ranking models) are stored in the model registry with "
            "cross-region replication, so we can redeploy them anywhere we run.",
        ]),
        ("h1", "6. Region failover"),
        ("p", f"This section treats risk {R4[0]} ({R4[1].lower()}). Inherent score {R4[4]}×{R4[5]} = "
              f"{R4[4] * R4[5]} ({level_for(R4[4] * R4[5])}); after the measures below, residual "
              f"{R4[6]}×{R4[7]} = {R4[6] * R4[7]} ({level_for(R4[6] * R4[7])})."),
        ("bullets", [
            "Production runs in the primary EU region across three availability zones, so the loss of one data "
            "centre is handled automatically.",
            "A **pilot-light** copy runs in a second EU region ([[recovery region, e.g. eu-central-1]]): databases "
            "replicate continuously, storage buckets replicate, infrastructure is defined as code and can be "
            "scaled up in about 2 hours. EU data stays in the EU.",
            "UAE enterprise tenants run in the UAE region across availability zones. Their contracts require data "
            "to stay in the UAE, so they do not fail over abroad; their agreed RTO is 24 hours, restoring from "
            "in-country backups.",
            "DNS failover is manual and needs two people (Recovery Lead plus CTO or Security Lead) to avoid a "
            "false failover.",
        ]),
        ("h1", "7. Backup strategy"),
        ("table", ["What", "How", "Frequency", "Retention", "Restore test"], [
            ("Production databases", "Point-in-time recovery + cross-region replica; encrypted with our keys",
             "Continuous", "35 days PITR; monthly snapshot kept 12 months", "Quarterly"),
            ("Customer files and artist portfolios", "Versioned storage, cross-region replication, delete protection",
             "Continuous", "Versions 90 days", "Quarterly sample"),
            ("Consent and licence ledger", "Append-only store + daily export to separate backup account",
             "Hourly / daily", "7 years", "Twice a year"),
            ("Model registry and datasets", "Replicated registry; datasets in versioned storage", "On each release",
             "All approved versions", "Twice a year (redeploy previous version)"),
            ("Infrastructure as code, source", "Git (hosted) + nightly mirror to backup account", "Nightly",
             "90 days", "Twice a year"),
            ("Secrets", "Secrets manager with multi-region replication", "Continuous", "n/a",
             "Yearly (break-glass drill)"),
        ], [3.3, 5.3, 2.2, 3, 2.7]),
        ("p", "Backups are stored in a separate cloud account that production engineers cannot delete from, to "
              "survive ransomware or a compromised admin account. Backup failures alert the Recovery Lead."),
        ("h1", "8. Invocation"),
        ("steps", [
            "An incident (" + ref("IMS-PRO-005") + ") is expected to exceed an RTO in section 4, or a supplier "
            "declares a major outage.",
            "The Recovery Lead recommends invocation in #trust-report, with the expected impact and options.",
            "The Continuity Decision-maker (or deputy) invokes the plan and records the time.",
            "The Security Lead confirms emergency access is through break-glass or approved roles only and is "
            "logged.",
            "Recovery Lead executes the relevant runbook (region failover, AI fallback, restore from backup).",
            "Head of AI confirms AI safety checks pass before AI features return.",
            "Stand down when services meet normal targets for 24 hours; hold a review within 10 working days.",
        ]),
        ("h1", "9. Communication during disruption"),
        ("table", ["Audience", "Channel", "When", "Owner"], [
            ("Staff", "#trust-report, then all-hands message; SMS if chat is down", "Within 30 min of invocation",
             title_of("SRE")),
            ("Customers", "Status page; email to enterprise contacts", "Within 1 hour; updates every 2 hours",
             title_of("CREA")),
            ("Artists", "Commons banner and email if payouts or commissions affected", "Within 4 hours",
             title_of("CREA")),
            ("Suppliers", "Support escalation and account manager", "Immediately", title_of("DPO")),
            ("Trust Council", "Summary at end of event; full review at next meeting", "End of event",
             title_of("CEO")),
        ], [3, 6, 4, 3.5]),
        ("h1", "10. Testing schedule"),
        ("table", ["Test", "Frequency", "Pass criterion", "Owner"], [
            ("Database and file restore", "Quarterly", "Restore within RTO; data matches checksums", person("SRE")),
            ("Region failover (pilot light scale-up)", "Yearly", "Canvas and API serve traffic from recovery region "
             "within 8 h", person("SRE")),
            (f"{SCM} alternative-provider switch", "Twice a year", "Evaluation set passes; switch < 1 h",
             person("CAIO")),
            (f"{SFR} backup moderation", "Twice a year", "Backup screens test set at agreed detection rate",
             person("CREA")),
            ("AI kill switches and model rollback", "Twice a year", "Each works in < 15 min", person("HOD")),
            ("Tabletop exercise", "Twice a year", "Actions recorded and tracked", person("IMSC")),
            ("Break-glass accounts", "Yearly", "Log-in works; alert fires", person("CISO")),
        ], [5, 2.5, 6, 3]),
        ("example", "Tabletop exercise BC-TT-2026-02 (2026-06-18, 90 minutes)", [
            f"**Scenario:** the primary EU region suffers a major outage at 10:00 on a Tuesday. At 11:30 the "
            f"foundation-model provider used by {SCM} also reports degraded service. An agency customer is "
            "mid-campaign and calls the CEO.",
            f"**Participants:** {person('SRE')} (facilitator), {person('CTO')}, {person('CISO')}, {person('CAIO')}, "
            f"{person('CREA')}, {person('IMSC')} (scribe).",
            "**What went well:** the team knew the RTO for Canvas and the decision to invoke was taken in 20 minutes; "
            f"everyone agreed immediately that {STF} must stay off until {SFR} was confirmed in the recovery region.",
            "**Gaps found:** (1) the runbook did not say who changes DNS — fixed with the two-person rule; (2) the "
            "status-page login used single sign-on, which would also be down — moved to a break-glass account; (3) "
            f"the alternative provider for {SCM} had not been tested since signing — test added to the schedule.",
            "**Follow-up:** three actions logged in the Improvement Register of " + ref("IMS-REG-008") +
            "; all closed by 2026-08-31. The real foundation-model API outage of June 2026 (INC-2026-006 in "
            + ref("IMS-REG-006") + ") later confirmed that manual mode worked.",
        ]),
        ("h1", "11. Records"),
        ("bullets", [
            "This plan and its BIA, reviewed yearly and after any invocation or major architecture change.",
            "Backup job reports and restore-test results; failover and switch test reports.",
            "Tabletop exercise notes and actions; invocation logs and post-event reviews.",
        ]),
        ("h1", "12. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-PRO-005", "IMS-REG-002", "IMS-REG-005", "IMS-POL-006", "IMS-REG-003",
                                      "IMS-REG-006")]),
    ],
}
