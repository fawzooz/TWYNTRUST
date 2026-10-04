from org import AI_SYSTEMS, KEY_RISKS, LAWS, ORG, TECH, person, ref, title_of, who, level_for

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
SF, SM, AM, SAFE, CA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))
R1 = next(r for r in KEY_RISKS if r[0] == "RSK-AI-001")
R1_IN, R1_RES = R1[4] * R1[5], R1[6] * R1[7]

DOC = {
    "id": "IMS-POL-003",
    "summary": f"How {N} classifies, protects and uses data — especially the data that trains, tests and "
               "feeds our AI systems — so that artists' rights, customers' confidentiality and people's privacy "
               "are respected from acquisition to deletion.",
    "clauses": {"27001": "Annex A 5.12, 5.13, 5.14, 5.31, 5.32, 5.33, 5.34, 8.10, 8.11, 8.12, 8.33",
                "42001": "Annex A.7.2–A.7.6; also A.4.3, A.5.2–A.5.4, A.8.2"},
    "howto": [
        "The consent and licence ledger (section 6) is the heart of this policy for any company that trains or "
        "fine-tunes on other people's work. If you have nothing else, build that first — a spreadsheet is fine.",
        "Check the retention periods in section 10 against your own laws and contracts before approval.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"Data is what our AI systems learn from and what our customers trust us with. At {N} it includes "
              "unreleased scripts, artists' portfolios, licensed artwork, marketplace payouts and staff records. "
              "If we take data we have no right to, keep it longer than needed or let it leak, we harm real "
              "people and break the promise in our mission."),
        ("p", "This policy sets the rules for classifying and protecting all information (the ISO/IEC 27001 "
              "side) and for acquiring, preparing and using data for AI (the ISO/IEC 42001 side). It is one "
              "policy because the same dataset — for example artist portfolios — raises security, privacy, "
              "copyright and AI-quality questions at the same time."),
        ("h1", "2. Scope"),
        ("p", f"All information created, received or processed by {N}, in any form, and all data used to "
              f"develop, evaluate, fine-tune or operate the AI systems in {ref('IMS-REG-005')}. It applies to "
              "employees, contractors and suppliers who handle our data."),
        ("std", [
            "ISO/IEC 27001 expects information to be classified by its sensitivity and labelled, protected when "
            "transferred, kept as records where needed, handled in line with privacy law, deleted when no longer "
            "required, masked where appropriate and protected against leakage (Annex A 5.12–5.14, 5.33, 5.34, "
            "8.10–8.12).",
            "ISO/IEC 42001 expects you to define and document how data for AI is managed: where it comes from and "
            "how it was acquired, what quality it must have, its provenance over its life, and how it is "
            "prepared (Annex A.7.2–A.7.6).",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Role", "Responsibility"], [
            (who("HOD"), "Owns this policy. Data steward for all AI datasets; runs the consent and licence ledger, "
                         "dataset records and data-quality checks."),
            (who("DPO"), "Privacy lead: lawful basis, DPIAs, data-subject requests, transfers, breach notification "
                         "decisions. Approves any new use of personal data."),
            (who("CISO"), "Classification scheme, encryption, DLP and access controls."),
            (who("LEGAL"), "Licence terms for artwork and datasets; copyright questions."),
            (who("CREA"), "Represents artists; reviews opt-out handling and the Artist Agreement wording."),
            ("Data owners (asset owners)", f"Classify their assets in {ref('IMS-REG-005')} and approve access."),
            ("Everyone", "Handle data according to its class; report suspected leaks within 1 hour to #trust-report."),
        ], [5.5, 11]),
        ("h1", "4. Data classification"),
        ("p", "Every information asset gets one of four classes. When in doubt, choose the higher class. The "
              "asset owner sets the class; the Security Lead can change it."),
        ("table", ["Class", "Meaning", f"Examples at {N}", "Minimum handling"], [
            ("Public", "Approved for anyone", "Website, published help pages, marketing art with credit",
             "Approval before publishing"),
            ("Internal", "For staff and contractors; low harm if leaked", "Policies, roadmaps, internal wiki",
             "Company accounts only; no public links"),
            ("Confidential", "Harm to us, customers or artists if leaked", "Source code, model evaluation sets, "
             "contracts, logs, marketplace data", "Need-to-know access; encrypted at rest and in transit; no "
             "personal devices; DLP rules apply"),
            ("Restricted", "Serious harm; legal or contractual duties", "Customer scripts and prompts, artist "
             "consent records, fine-tuning datasets and weights, API keys", "Named-group access with MFA; "
             "access logged and reviewed monthly; never pasted into AI tools other than the product systems "
             "themselves; masked or synthetic in test"),
        ], [2.4, 3.6, 5.5, 5]),
        ("p", "**Labelling (5.13).** Documents carry the class in the footer; storage buckets, datasets and "
              "registry entries carry a 'classification' tag. Unlabelled data in S3 is treated as Restricted until "
              "tagged. **Transfer (5.14).** Confidential and Restricted data is shared only through approved "
              "channels (company drive with named sharing, encrypted API, signed customer portal) — never by "
              "personal email or chat apps."),
        ("h1", "5. Data for AI — lifecycle rules"),
        ("p", "The table shows the stages every AI dataset passes through. The dataset record (one per dataset "
              "version, kept in the model registry) captures the evidence for each stage."),
        ("table", ["Stage", "Rule", "Evidence in the dataset record"], [
            ("Need (A.7.2)", "State what the data is for, which system, and why less data would not do",
             "Purpose, system ID, minimisation note"),
            ("Acquisition (A.7.3)", "Only from sources we own, licensed for AI training, or with explicit "
             "consent. No web scraping of artwork. Supplier datasets need a written licence that allows training",
             "Source, licence/consent IDs from the ledger"),
            ("Quality (A.7.4)", "Check completeness, duplicates, corrupted files, label accuracy (sample 5%) "
             "and representativeness against the intended users",
             "Quality report with pass/fail against thresholds"),
            ("Provenance (A.7.5)", "Record origin, every transformation and every version; files hashed",
             "Lineage log; hashes; parent dataset version"),
            ("Preparation (A.7.6)", "Document cleaning, filtering, augmentation, labelling instructions and "
             "who labelled", "Preparation script commit; labelling guide version"),
            ("Bias check", "Compare distribution of styles, regions, languages and depicted groups with the "
             "intended use; record gaps and mitigations", "Bias note reviewed by the Head of AI"),
            ("Use and storage", "Restricted class; stored in the eu-west-1 data account; access by named group",
             "Access list; bucket policy"),
            ("Retention and deletion", "Keep only as long as section 10 allows; delete on opt-out or licence end",
             "Deletion log"),
        ], [3, 8, 5.5]),
        ("h2", "5.1 Labelling and annotation"),
        ("p", "Labels (for example 'style: ink wash', 'contains a recognisable person') are written by trained "
              "staff or vetted contractors using a versioned labelling guide. Contractors label only within our "
              "tools — data never leaves our environment. Two people label a 5% sample independently; if they "
              "agree on less than 90% of items, the guide is clarified and the batch is relabelled."),
        ("h2", "5.2 Customer data and training"),
        ("p", f"**Customer scripts, prompts and project files are never used to train or fine-tune any model — "
              "ours or a supplier's — unless the customer has opted in in writing.** Opt-in is off by default, "
              f"can be withdrawn at any time, and is recorded against the customer account. Our supplier "
              f"contracts require no training on our data and zero or 30-day retention "
              f"({ref('IMS-POL-006')}). {SM} runs on a zero-retention endpoint."),
        ("h1", "6. Consent and licence ledger for artwork"),
        ("p", f"The ledger is the single record of our right to use each piece of artwork for AI. It covers every "
              f"image in the {SF} fine-tuning sets and every portfolio image used by {AM}."),
        ("table", ["Field", "Example entry"], [
            ("Ledger ID", "LIC-2026-0418"),
            ("Artist or rights holder", "Commons artist #A-0932 (pseudonymised in the ledger)"),
            ("Basis", "Consent under Artist Agreement v3, clause 7 (AI fine-tuning, paid at USD 4 per image per year)"),
            ("Scope", "Fine-tuning of the StoryFrame style model; not for any other model or third party".replace(
                "StoryFrame", SF)),
            ("Assets covered", "126 images, hashes in dataset DS-SF-2026-Q3"),
            ("Valid from / until", "2026-07-01 / 2027-06-30 (renews unless withdrawn)"),
            ("Opt-out status", "None"),
            ("Verified by / date", f"{person('HOD')}, 2026-07-03"),
            ("Your entry", "[[ledger ID]] · [[rights holder]] · [[basis]] · [[scope]] · [[dates]]"),
        ], [4.5, 12]),
        ("h2", "6.1 Opt-outs and the EU text-and-data-mining reservation"),
        ("bullets", [
            "We do not scrape the web for training data. Where we license a third-party collection, the licensor "
            "must confirm that rights holders who reserved their works from text-and-data mining (EU DSM Directive "
            "Art. 4, for example through machine-readable metadata or site terms) are excluded.",
            "Any artist can opt out at any time by account setting or by email. Within **14 days** we mark the "
            "ledger, remove the images from all training datasets and stop any new training on them (OBJ-03).",
            "Models already trained on opted-out work are retired at the next scheduled fine-tune and in any case "
            "within 90 days. We tell the artist when this is done.",
            "Opt-out requests and their closure dates are reported monthly to the Head of AI.",
        ]),
        ("tip", "Start the ledger as a spreadsheet with one row per agreement and a separate tab of image hashes. "
                "The test an auditor will run is simple: pick five images from your training set and ask you to "
                "show the consent or licence for each within a few minutes."),
        ("h1", "7. Privacy by design and assessments"),
        ("p", "Personal data is used only when needed, for a stated purpose, with a lawful basis, and is "
              "pseudonymised where possible (artist IDs instead of names in training metadata, for example). "
              "Every new feature answers the privacy questions in G0 of the lifecycle "
              f"({ref('IMS-POL-002')})."),
        ("table", ["", "DPIA (data protection impact assessment)", "AIIA (AI system impact assessment)"], [
            ("Required by", "GDPR / UK GDPR Art. 35, UAE PDPL", "ISO/IEC 42001 (6.1.4, 8.4, A.5)"),
            ("Focus", "Risks to individuals from processing their personal data",
             "Impacts of an AI system on individuals, groups and society — fairness, safety, rights, "
             "even with no personal data"),
            ("Trigger", "High-risk processing: large-scale, new technology, profiling, sensitive data",
             "New AI system or significant change"),
            ("Owner", title_of("DPO"), title_of("CAIO")),
            ("How we combine them", "One workshop; the AIIA form has a privacy section that becomes the DPIA when "
             "the screening says one is needed", f"See {ref('IMS-PRO-002')}"),
        ], [3, 6.8, 6.7]),
        ("h2", "7.1 Data-subject rights"),
        ("p", "Customers, artists and staff can ask to access, correct, delete, restrict or port their personal "
              "data, or object to its use. Requests go to privacy@quillfen.example and are logged by the Privacy "
              "and Legal Lead. We confirm receipt within 3 working days and answer within **30 days** "
              "(the shortest common deadline across our laws). Deleting an artist's account also triggers an "
              "opt-out in the ledger."),
        ("h2", "7.2 Cross-border transfers"),
        ("p", f"Primary storage is in the EU; UAE enterprise customers can choose the UAE region "
              f"({TECH['cloud']}). Transfers to suppliers outside the EU/UK or UAE use the safeguards their laws "
              "require (for example EU Standard Contractual Clauses, the UK addendum, and UAE PDPL transfer "
              f"conditions) and are listed in the supplier register ({ref('IMS-POL-006')})."),
        ("h1", "8. Data masking, test data and leakage prevention"),
        ("bullets", [
            "**Masking (8.11).** Logs and support tools show only the last 4 characters of IDs and email "
            "addresses; customer script text is hidden from support staff unless the customer grants access for a "
            "ticket.",
            "**Test data (8.33).** Production customer data is never used in development or testing. We use "
            "synthetic scripts and a public-domain image set for tests.",
            "**DLP (8.12).** Rules on the email and file-sharing suite block external sharing of files tagged "
            "Restricted; S3 Block Public Access is enforced on every account; secret scanning runs on all code; "
            f"staff may use only approved AI tools ({ref('IMS-POL-005')}); alerts go to the Security Lead.",
        ]),
        ("h1", "9. Records and privacy (5.33, 5.34)"),
        ("p", f"We keep the records needed to prove compliance — consent and licence ledger, dataset records, "
              "DPIAs and AIIAs, data-subject request log, records of processing — protected from change and loss. "
              "The applicable laws are listed in the context register; the main ones are:"),
        ("bullets", [law for law, _ in LAWS[:5]]),
        ("h1", "10. Retention and deletion"),
        ("table", ["Data", "Keep for", "Then"], [
            ("Customer scripts and project files", "Life of the account + 30 days", "Delete, including backups "
             "within 35 days"),
            ("Prompts and AI output logs", "90 days", "Delete; keep aggregated metrics only"),
            ("Fine-tuning datasets", "While a model trained on them is in use + 12 months", "Delete; keep "
             "hashes and ledger IDs"),
            ("Consent and licence ledger", "Licence end + 6 years", "Archive, then delete"),
            ("Model weights (retired)", "3 years after retirement", "Delete"),
            ("Marketplace payout records", "As required by tax law (typically 5–7 years)", "Delete"),
            ("Your data type", "[[period]]", "[[action]]"),
        ], [5.5, 5.5, 5.5]),
        ("p", "**Deletion (8.10)** uses the cloud provider's secure delete; laptops are wiped through device "
              "management before reuse. Every deletion of a dataset is logged with the hashes removed."),
        ("pagebreak",),
        ("h1", f"11. Worked example — {R1[0]}"),
        ("example", f"{R1[0]}: {R1[1]}", [
            f"**The risk.** Owner: {who(R1[3])}. Inherent score {R1[4]} × {R1[5]} = {R1_IN} "
            f"({level_for(R1_IN)}). Treatment: {R1[8]}. Main controls: {R1[9]}.",
            "**What happened.** During the Q3 2026 intake, an agency delivered 1,200 images under a licence. The "
            "preparation script compared each image hash with the ledger and found 41 images whose licence covered "
            "'editorial use' only, not AI training.",
            "**Response under this policy.** The 41 images were quarantined in a separate bucket (section 5 "
            "acquisition rule), excluded from dataset DS-SF-2026-Q3, and the agency was asked for an amended licence. "
            "The agency declined for 12 images; they were deleted and the deletion logged (section 10).",
            "**Improvement.** The ledger check now runs automatically in the data pipeline and blocks a dataset "
            "version if any image has no valid ledger ID.",
            f"**Residual risk.** {R1[6]} × {R1[7]} = {R1_RES} ({level_for(R1_RES)}), accepted by the risk owner and "
            "tracked against OBJ-03 (100% of fine-tuning images with a verified licence or consent).",
        ]),
        ("h1", "12. Records produced"),
        ("bullets", [
            "Consent and licence ledger; opt-out log.",
            "Dataset records (purpose, source, quality, provenance, preparation, bias note).",
            "DPIAs, AIIAs and the record of processing activities.",
            "Data-subject request log; transfer register; deletion log; DLP alert log.",
        ]),
        ("h1", "13. Compliance and review"),
        ("p", "Breaches are handled through the disciplinary process or contract terms. Suspected data breaches "
              f"are incidents under {ref('IMS-PRO-005')}; the Privacy and Legal Lead decides on regulator "
              "notification (72 hours under GDPR). This policy is reviewed yearly and whenever a new data source "
              "or AI system is added."),
        ("h1", "14. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-POL-002", "IMS-POL-004", "IMS-POL-005", "IMS-POL-006",
                                      "IMS-PRO-002", "IMS-PRO-005", "IMS-REG-002", "IMS-REG-005")]),
    ],
}
