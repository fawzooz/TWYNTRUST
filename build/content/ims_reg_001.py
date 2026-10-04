from datetime import date

from org import AI_SYSTEMS, LAWS, ORG, person, title_of

N = ORG["name"]
YES_NO = ["Yes", "No", "Partly"]

ISSUE_ROWS = [
    ("ISS-01", "External", "Legal", "EU AI Act transparency duties (labelling AI-generated content and deepfakes) "
     "apply to StoryFrame outputs used by EU customers.", "Both", "Risk", "High", person("DPO"),
     "RSK-AI-002; labelling controls in IMS-POL-002", '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-02", "External", "Social", "Artists and the public are sceptical of generative AI trained on scraped art; "
     "trust in our consent model is a market differentiator.", "AIMS", "Opportunity", "High", person("CREA"),
     "OBJ-03; Artist Advisory Panel", '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-03", "External", "Technological", "We depend on third-party foundation and image models that can change "
     "behaviour with little notice.", "Both", "Risk", "High", person("CAIO"),
     "RSK-AI-005; IMS-POL-006", '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-04", "External", "Economic", "Enterprise customers require ISO/IEC 27001 in contracts; certification "
     "unlocks revenue.", "ISMS", "Opportunity", "High", person("CEO"), "OBJ-01",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-05", "External", "Technological", "Phishing and credential theft targeting SaaS and cloud admins is "
     "increasing, including AI-generated lures.", "ISMS", "Risk", "High", person("CISO"), "RSK-IS-002",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-06", "External", "Legal", "Copyright law on AI training and outputs is unsettled and differs between the "
     "UAE, EU, UK and US.", "AIMS", "Risk", "Medium", person("LEGAL"), "RSK-AI-001",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-07", "External", "Political", "Data-residency expectations from UAE enterprise customers.", "ISMS",
     "Risk", "Medium", person("SRE"), "me-central-1 region option",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-08", "Internal", "Organisational", "Small team: several people hold two roles; key-person dependency in "
     "security and ML.", "Both", "Risk", "Medium", person("CEO"), "IMS-GOV-001 section 6; IMS-PRO-006",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-09", "Internal", "Cultural", "Strong engineering culture of automation; CI/CD makes controls cheap to "
     "enforce.", "Both", "Opportunity", "Medium", person("CTO"), "IMS-POL-002",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-10", "Internal", "Organisational", "Fully remote staff in four countries; contractors onboarded by "
     "different managers.", "Both", "Risk", "Medium", person("HOP"), "NC-2026-004; CA-2026-005",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-11", "Internal", "Technological", "ArtistMatch ranking directly affects artists' income.", "AIMS", "Risk",
     "High", person("CAIO"), "RSK-AI-003; OBJ-06",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
    ("ISS-12", "[[Internal/External]]", "[[category]]", "[[your issue]]", "[[ISMS/AIMS/Both]]", "[[Risk/Opportunity]]",
     "[[Low/Medium/High]]", "[[owner]]", "[[link]]",
     '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk","Monitor")'),
]

PRIORITY = ('=IFERROR(IF(OR(F{r}="",G{r}=""),"",IF(F{r}*G{r}>=15,"Manage closely",'
            'IF(F{r}*G{r}>=8,"Keep satisfied / informed","Monitor"))),"Score 1-5")')

PARTY_ROWS = [
    ("IP-01", "Enterprise customers (agencies, publishers, game studios)",
     "Confidentiality of unreleased scripts; ISO/IEC 27001 certificate; breach notification within contract times; "
     "evidence of responsible AI.", "Contract + DPA", "Yes", 5, 5, PRIORITY, person("CEO")),
    ("IP-02", "Marketplace artists", "Their work is not used for training without consent; fair ranking and pay; "
     "protection of portfolio and payout data.", "Artist Agreement; policy commitment", "Yes", 4, 5, PRIORITY,
     person("CREA")),
    ("IP-03", "End users of Canvas (writers, designers)", "Service available; outputs labelled; no leakage between "
     "customers.", "Terms of service", "Yes", 3, 4, PRIORITY, person("CTO")),
    ("IP-04", "People depicted or referenced in generated images", "No deceptive deepfakes; respect for likeness "
     "and reputation.", "Law (EU AI Act Art. 50); policy commitment", "Yes", 2, 5, PRIORITY, person("CAIO")),
    ("IP-05", "Data protection regulators (UAE, EU, UK)", "Lawful processing; notification of breaches; records of "
     "processing.", "Law", "Yes", 5, 3, PRIORITY, person("DPO")),
    ("IP-06", "Staff and contractors", "Clear rules, training, safe channels to raise concerns, privacy of HR data.",
     "Employment law; policy", "Yes", 3, 4, PRIORITY, person("HOP")),
    ("IP-07", "Investors and board", "Certification on plan; no reputation-damaging incident.", "Shareholder "
     "agreement (reporting)", "Partly", 5, 4, PRIORITY, person("CEO")),
    ("IP-08", "AI model and API suppliers", "Use within their acceptable-use policy; secure API key handling.",
     "Contract", "Yes", 3, 3, PRIORITY, person("DPO")),
    ("IP-09", "Content-moderation vendor (SafeFrame)", "Feedback on missed detections; agreed change notice.",
     "Contract (CA-2026-004)", "Yes", 3, 3, PRIORITY, person("CREA")),
    ("IP-10", "Certification body", "Access to evidence and people; timely closure of findings.", "Certification "
     "agreement", "Yes", 4, 3, PRIORITY, person("IMSC")),
    ("IP-11", "Wider public and media", "Honest labelling of AI content; no harmful imagery.", "Not binding — "
     "policy commitment only", "Partly", 3, 2, PRIORITY, person("CEO")),
    ("IP-12", "[[interested party]]", "[[their needs and expectations]]", "[[source]]", "[[Yes/No/Partly]]", "[[1-5]]",
     "[[1-5]]", PRIORITY, "[[owner]]"),
]

REVIEW_FORMULA = '=IF(H{r}="","",TEXT(H{r}+365,"yyyy-mm-dd"))'
LAW_EXTRA = {
    "45 of 2021": ("UAE", person("DPO"), "Partial", "Records of processing complete; cross-border transfer review in progress."),
    "38 of 2021": ("UAE", person("LEGAL"), "Met", "Artist Agreement grants licence; outputs policy in place."),
    "GDPR": ("EU / UK", person("DPO"), "Met", "DPAs, records of processing, EU representative appointed."),
    "Artificial Intelligence Act": ("EU", person("CAIO"), "In progress", "C2PA credentials and visible label live; AI literacy training in "
                                              "IMS-REG-004; GPAI downstream info requested from suppliers."),
    "2019/790": ("EU", person("HOD"), "Met", "Fine-tuning only on licensed or consented work; opt-out register."),
    "Consumer protection": ("All markets", person("LEGAL"), "Partial", "Ad-use guidance for customers drafted."),
    "Customer contracts": ("All", person("DPO"), "Met", "Security and AI clauses tracked in contract tool."),
    "2019/1150": ("EU", person("CAIO"), "Partial", "Public 'How ArtistMatch works' page lists the main ranking "
                                                   "parameters; artist-facing explanation in the Commons help centre."),
}


def _extra(law):
    for key, val in LAW_EXTRA.items():
        if key in law:
            return val
    raise KeyError(f"No LAW_EXTRA entry for {law!r}")

LAW_ROWS = []
for i, (law, applies) in enumerate(LAWS):
    jur, owner, status, note = _extra(law)
    LAW_ROWS.append((f"LEG-{i + 1:02d}", law, jur, applies, "Contract" if "contract" in law.lower() else "Law / regulation",
                     owner, status, date(2026, 9, 1), REVIEW_FORMULA, note))
LAW_ROWS += [
    ("LEG-08", "PCI DSS (through our payment processor)", "Global", "Card payments — we never store card data",
     "Contract", person("CTO"), "Met", date(2026, 9, 1), REVIEW_FORMULA, "Processor's attestation on file; SAQ A."),
    ("LEG-09", "UAE Federal Decree-Law No. 34 of 2021 (Combating Rumours and Cybercrimes)", "UAE",
     "Misuse of the platform for fabricated content or impersonation", "Law / regulation", person("LEGAL"), "Met",
     date(2026, 9, 1), REVIEW_FORMULA, "Prohibited-use terms and moderation; police contact in IMS-GOV-001."),
    ("LEG-10", "UK Online Safety Act 2023 (assess applicability)", "UK", "User-generated imagery on Commons",
     "Law / regulation", person("DPO"), "In progress", date(2026, 9, 1), REVIEW_FORMULA,
     "Legal opinion requested on whether Commons is in scope."),
    ("LEG-11", "Employment and data protection law in Egypt, Jordan and Portugal", "EG / JO / PT",
     "Remote staff records and monitoring", "Law / regulation", person("HOP"), "Partial", date(2026, 9, 1),
     REVIEW_FORMULA, "Employer-of-record contracts reviewed; Egypt PDPL executive regulations awaited."),
    ("LEG-12", "[[law, regulation or contract]]", "[[jurisdiction]]", "[[what it applies to]]",
     "[[type]]", "[[owner]]", "[[status]]", "", REVIEW_FORMULA, "[[evidence]]"),
]

SCOPE_ROWS = [
    ("Organisation", "All staff and contractors of " + ORG["legal_name"], "In", "Everyone handles in-scope information.",
     "HR and contractor onboarding", "IMS-PRO-003"),
    ("Location", "Dubai head office", "In", "Leadership, product and creative work happen here.",
     "Shared building services (landlord)", "Office access control; clear-desk rule"),
    ("Location", "Remote work in Egypt, Jordan, Portugal and the UK", "In", "Most engineering is remote.",
     "Home networks; employer-of-record providers", "Managed laptops, SSO, MFA"),
    ("Service", "Quillfen Canvas, Commons and API", "In", "Products customers buy and certificates must cover.",
     "Customers' own tools via API", "API terms; rate limits; IMS-POL-002"),
    ("AI system", "StoryFrame, ScriptMate, ArtistMatch, SafeFrame, CodeAssist", "In",
     "All AI systems we provide, produce or use.", "Model and moderation suppliers", "IMS-POL-006; AI Release Review"),
    ("Technology", "AWS accounts (eu-west-1, me-central-1), GitHub, identity provider, SaaS suite", "In",
     "Hold or process in-scope information.", "AWS shared-responsibility model", "Cloud supplier review"),
    ("Technology", "Physical data centres of AWS and model suppliers", "Out",
     "Run by suppliers; covered by their certifications and our contracts.", "Supplier attestations",
     "Annual review of SOC 2 / ISO reports"),
    ("AI system", "Internal operation of third-party foundation and image models", "Out",
     "We cannot control their training; we control how we select, contract, test and monitor them.",
     "Model API", "Supplier AI questionnaire; canary tests"),
    ("Process", "Card payment processing", "Out", "Fully outsourced to a PCI DSS-certified processor.",
     "Checkout redirect", "Processor attestation (LEG-08)"),
    ("Process", "Payroll for remote staff", "Out", "Handled by employer-of-record providers.",
     "HR data transfer", "DPA with provider"),
    ("[[category]]", "[[item]]", "[[In/Out]]", "[[justification]]", "[[interface]]", "[[control at boundary]]"),
]

AI_ROWS = []
OWNERS = {"AI-SYS-001": "CAIO", "AI-SYS-002": "CAIO", "AI-SYS-003": "CAIO", "AI-SYS-004": "CREA",
          "AI-SYS-005": "CTO"}
DUTIES = {
    "AI-SYS-001": ("Licensed third-party image model", "Impact assessment; data provenance and consent; labelling "
                   "and content credentials; release gate; output monitoring"),
    "AI-SYS-002": ("Foundation-model API supplier", "Supplier controls (no training, zero retention); tenant "
                   "isolation; transparency to users; hallucination warnings"),
    "AI-SYS-003": ("None (in-house)", "Impact assessment; fairness testing and monthly monitoring; explanation of "
                   "ranking to artists and customers"),
    "AI-SYS-004": ("Moderation vendor", "Assess fitness for our use; contract change notice and version pinning; "
                   "canary testing"),
    "AI-SYS-005": ("Coding-assistant vendor", "Acceptable-use rules; secret scanning; code review of suggestions"),
}
for s in AI_SYSTEMS:
    sup, duties = DUTIES[s["id"]]
    AI_ROWS.append((s["id"], s["name"], s["role"], sup, s["users"], s["criticality"].split(" — ")[0], duties,
                    f"{person(OWNERS[s['id']])}, {title_of(OWNERS[s['id']])}", "IMS-PRO-002"))
AI_ROWS.append(("[[AI-SYS-00x]]", "[[name]]", "[[AI provider / AI producer / AI customer / user / AI partner]]",
                "[[supplier]]", "[[users / affected]]", "[[High/Medium/Low]]", "[[obligations]]", "[[owner]]",
                "[[assessment ref]]"))

CLIMATE_ROWS = [
    ("CC-01", "Does climate change affect our ability to protect information?",
     "Extreme heat or flooding could disrupt cloud regions or staff in the Gulf region; mitigated by multi-region "
     "AWS and remote work.", "Partly", "Covered by RSK-IS-004 and IMS-PRO-006.", person("SRE")),
    ("CC-02", "Do interested parties have climate-related requirements for us?",
     "Two EU agency customers ask for supplier sustainability statements; none make it a security or AI "
     "requirement yet.", "Partly", "Track in Interested Parties; review at each context review.", person("CEO")),
    ("CC-03", "Is the energy use of our AI systems significant?",
     "StoryFrame inference and occasional fine-tuning use GPU compute; small in absolute terms but our largest "
     "controllable footprint.", "Yes", "Report GPU hours per month in IMS-REG-003; prefer efficient model sizes.",
     person("HOD")),
    ("CC-04", "Do AI outputs create climate-related harms (e.g. misinformation)?",
     "Not a known use of our product; covered by prohibited-content rules.", "No", "None beyond existing controls.",
     person("CREA")),
    ("CC-05", "Do climate risks affect key suppliers?",
     "Cloud and model suppliers publish resilience and sustainability reports.", "Partly",
     "Include in annual supplier review (IMS-POL-006).", person("DPO")),
    ("CC-06", "Conclusion",
     "Climate change is a relevant but low-priority issue for the IMS. It is recorded as issue context, not as a "
     "separate risk, apart from AI compute energy use, which we measure.", "Partly",
     "Review at each context review.", person("IMSC")),
    ("CC-07", "[[question]]", "[[assessment]]", "[[Yes/No/Partly]]", "[[action]]", "[[owner]]"),
]

WB = {
    "id": "IMS-REG-001",
    "summary": f"The register that captures {N}'s context for both standards: issues, interested parties and "
               "their requirements, legal and contractual obligations, the scope boundary, our role for each AI "
               "system, and whether climate change is relevant.",
    "clauses": {"27001": "4.1, 4.2, 4.3 (incl. Amd 1:2024 climate change); Annex A 5.31",
                "42001": "4.1 (incl. AI roles), 4.2, 4.3; Annex A.10.2"},
    "howto": [
        "Review the whole register twice a year with the Trust Council and after any major change "
        "(new market, new AI system, new law).",
        "Issues marked High automatically say 'Yes — raise or link a risk'. Make sure each one is linked to a risk "
        "in IMS-REG-002 or explained.",
        "Interested-party requirements that are binding (law or contract) must also appear in the Legal & "
        "Regulatory sheet.",
    ],
    "sheets": [
        {
            "name": "Internal & External Issues",
            "title": "Internal and external issues (PESTLE + internal)",
            "intro": "Things inside and outside the company that affect our ability to protect information and use "
                     "AI responsibly. 'Affects' shows whether the issue matters to the ISMS, the AIMS or both. "
                     "'Risk register?' is calculated.",
            "headers": ["ID", "Internal / External", "Category", "Issue", "Affects", "Risk or opportunity",
                        "Significance", "Owner", "Linked to", "Risk register?"],
            "rows": ISSUE_ROWS,
            "widths": [8, 12, 15, 55, 10, 14, 13, 18, 30, 26],
            "lists": {"Internal / External": ["Internal", "External"],
                      "Category": ["Political", "Economic", "Social", "Technological", "Legal", "Environmental",
                                   "Organisational", "Cultural"],
                      "Affects": ["ISMS", "AIMS", "Both"],
                      "Risk or opportunity": ["Risk", "Opportunity", "Both"],
                      "Significance": ["Low", "Medium", "High", "Critical"]},
            "levels": ["Significance"],
            "formulas": {"Risk register?": '=IF(OR(G{r}="High",G{r}="Critical"),"Yes — raise or link a risk",'
                                           'IF(G{r}="","","Monitor"))'},
        },
        {
            "name": "Interested Parties",
            "title": "Interested parties and their requirements",
            "intro": "Who can affect or is affected by our IMS, what they need, and whether we address it. Influence "
                     "and interest are scored 1–5; priority is calculated. Binding requirements become entries in "
                     "the Legal & Regulatory sheet.",
            "headers": ["ID", "Interested party", "Needs and expectations (security and AI)", "Source of requirement",
                        "Addressed in IMS?", "Influence (1-5)", "Interest (1-5)", "Priority", "Relationship owner"],
            "rows": PARTY_ROWS,
            "widths": [8, 32, 55, 26, 12, 11, 11, 22, 18],
            "lists": {"Addressed in IMS?": YES_NO, "Influence (1-5)": ["1", "2", "3", "4", "5"],
                      "Interest (1-5)": ["1", "2", "3", "4", "5"]},
            "status": ["Addressed in IMS?"],
            "formulas": {"Priority": PRIORITY},
        },
        {
            "name": "Legal & Regulatory",
            "title": "Legal, regulatory and contractual requirements register",
            "intro": "Every law, regulation and contract term we must meet. Owners review each entry at least "
                     "yearly; 'Next review' is calculated from 'Last reviewed'.",
            "headers": ["ID", "Requirement", "Jurisdiction", "What it applies to", "Type", "Owner",
                        "Compliance status", "Last reviewed", "Next review", "Evidence / notes"],
            "rows": LAW_ROWS,
            "widths": [8, 45, 12, 40, 16, 18, 15, 13, 13, 45],
            "lists": {"Type": ["Law / regulation", "Contract", "Standard / scheme", "Voluntary commitment"],
                      "Compliance status": ["Met", "Partial", "In progress", "Not met"]},
            "status": ["Compliance status"],
            "formulas": {"Next review": REVIEW_FORMULA},
        },
        {
            "name": "Scope & Boundaries",
            "title": "Scope, boundaries, interfaces and dependencies",
            "intro": "What is inside and outside the IMS and why. Interfaces and dependencies show where our "
                     "responsibility meets someone else's, and the control we use at that boundary.",
            "headers": ["Category", "Item", "In / Out", "Justification", "Interface or dependency",
                        "Control at the boundary"],
            "rows": SCOPE_ROWS,
            "widths": [14, 45, 9, 48, 32, 36],
            "lists": {"Category": ["Organisation", "Location", "Service", "Process", "Technology", "AI system",
                                   "Data"],
                      "In / Out": ["In", "Out"]},
        },
        {
            "name": "AI Roles",
            "title": "Our role for each AI system",
            "intro": "ISO/IEC 42001 asks us to determine our role for each AI system (terms from ISO/IEC 22989). "
                     "The role shapes which controls matter most. Keep in line with IMS-REG-005 and IMS-MAN-001.",
            "headers": ["AI system ID", "Name", "Our role(s)", "Supplier / partner", "Users and affected people",
                        "Criticality", "Main obligations that follow from the role", "Accountable owner",
                        "Impact assessment"],
            "rows": AI_ROWS,
            "widths": [12, 14, 36, 24, 30, 11, 50, 28, 16],
            "lists": {"Criticality": ["Low", "Medium", "High", "Critical"]},
            "levels": ["Criticality"],
        },
        {
            "name": "Climate Change",
            "title": "Climate-change consideration",
            "intro": "ISO/IEC 27001:2022/Amd 1:2024 added climate-change consideration to clauses 4.1 and 4.2. We "
                     "apply the same consideration to the AIMS as good practice (and AI compute energy use is "
                     "relevant to ISO/IEC 42001 Annex C 'environmental impact').",
            "headers": ["ID", "Question", "Our assessment", "Relevant?", "Action / link", "Owner"],
            "rows": CLIMATE_ROWS,
            "widths": [8, 40, 60, 11, 40, 18],
            "lists": {"Relevant?": YES_NO},
        },
    ],
}
