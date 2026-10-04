"""Single source of truth for the TWYNTRUST kit's sample organisation.

Every document and register pulls names, roles, systems, IDs and scales from here,
so the whole kit tells one consistent story. To adapt the kit to your own
organisation, change this file first and rebuild (see build/README.md).

Quillfen Studio and every person named here are fictional.
"""

KIT_VERSION = "2.0"
EFFECTIVE_DATE = "2026-11-01"
NEXT_REVIEW = "2027-11-01"
CLASSIFICATION = "Internal"

AUTHOR = "Prof. Dr. Mohamed Fawzi Elgendi (Fawzooz)"
AUTHOR_FULL = "Prof. Dr. Mohamed Fawzi Elgendi (Fawzooz), Fawzooz.ai"
LICENSE = ("CC BY 4.0 — free to share and adapt, including commercially, with credit to "
           "Prof. Dr. Mohamed Fawzi Elgendi (Fawzooz), Fawzooz.ai · creativecommons.org/licenses/by/4.0")
PUBLISHER = "Fawzooz.ai — companion to «AISEC Mastery» (ISO/IEC 42001) and «AppSec Mastery» (ISO/IEC 27001)"

# ---------------------------------------------------------------------------
# The framework
# ---------------------------------------------------------------------------
FRAMEWORK = "TWYNTRUST"
FRAMEWORK_FULL = ("TWYNTRUST Framework — one integrated management system for "
                  "ISO/IEC 27001:2022 and ISO/IEC 42001:2023")
TAGLINE = "Two standards. One system. Trust you can prove."
FRAMEWORK_IDEA = (
    "Information security (ISO/IEC 27001) and responsible AI (ISO/IEC 42001) are built on the same "
    "management-system skeleton (Clauses 4–10). TWYNTRUST twins them: one context, one leadership "
    "team, one risk process, one internal audit and one management review — with each standard's own "
    "Annex A controls attached where they belong. You run one system and earn two certificates."
)
# (number, strand name, what it covers, clauses, key documents)
STRANDS = [
    ("1", "Ground",
     "Understand your context, set one scope, appoint leaders, and publish one policy for security and AI.",
     "Clauses 4–5", ["IMS-MAN-001", "IMS-REG-001", "IMS-POL-001", "IMS-GOV-001"]),
    ("2", "Gauge",
     "Run one method for information-security and AI risks, assess AI impacts on people, choose controls, "
     "record them in the two Statements of Applicability, and set objectives.",
     "Clause 6", ["IMS-PRO-001", "IMS-REG-002", "IMS-PRO-002", "IMS-SOA-001", "IMS-SOA-002", "IMS-REG-003"]),
    ("3", "Equip",
     "Give people the skills, awareness and information they need, and keep documents under control.",
     "Clause 7", ["IMS-PRO-003", "IMS-REG-004", "IMS-PRO-004"]),
    ("4", "Operate",
     "Build security and responsibility into every stage of software and AI work: development, data, "
     "access, acceptable use, suppliers, incidents and continuity.",
     "Clause 8 + Annex A", ["IMS-POL-002", "IMS-POL-003", "IMS-POL-004", "IMS-POL-005", "IMS-POL-006",
                           "IMS-PRO-005", "IMS-PRO-006", "IMS-REG-005", "IMS-REG-006"]),
    ("5", "Prove and improve",
     "Measure, audit, review with top management, fix the causes of problems, and keep improving.",
     "Clauses 9–10", ["IMS-PRO-007", "IMS-REG-007", "IMS-PRO-008", "IMS-PRO-009", "IMS-REG-008"]),
]

# ---------------------------------------------------------------------------
# The sample organisation (fictional)
# ---------------------------------------------------------------------------
ORG = {
    "name": "Quillfen Studio",
    "legal_name": "Quillfen Studio FZ-LLC",
    "hq": "Dubai, United Arab Emirates",
    "sites": [
        "Dubai, UAE — small head office (leadership, product, creative team)",
        "Fully remote team in Egypt, Jordan, Portugal and the UK",
        "No data centre of our own: everything runs in the cloud and on company laptops",
    ],
    "headcount": "34 employees and about 10 freelance contractors",
    "age": "Founded 2024; seed-funded; first enterprise customers in 2026",
    "mission": "Help small studios and independent creators turn ideas into finished visual stories faster — "
               "with AI that respects artists, their rights and their audiences.",
    "sector": "Creative technology — AI-assisted illustration, storyboarding and an artist marketplace",
    "products": [
        "Quillfen Canvas — web app where writers, publishers, game studios and agencies turn scripts into "
        "storyboards and concept art, then refine them with human artists",
        "Quillfen Commons — marketplace where vetted freelance artists accept paid commissions",
        "Quillfen API — enterprise API for agencies that embed storyboard generation in their own tools",
    ],
    "customers": "Indie publishers, game studios, advertising agencies (B2B) and freelance artists (marketplace) "
                 "in the UAE, Saudi Arabia, the EU, the UK and the US",
    "why_certify": "Two enterprise agencies and one publisher require ISO/IEC 27001 in their contracts; EU "
                   "customers ask for evidence of responsible AI and EU AI Act readiness; artists want proof "
                   "that their work is not used to train models without consent.",
}

# AI systems in scope. ISO/IEC 42001 asks you to know your role for each one
# (provider, producer, customer/user, partner — see ISO/IEC 22989).
AI_SYSTEMS = [
    {
        "id": "AI-SYS-001", "name": "StoryFrame",
        "what": "Generates storyboard panels and concept art from a script or prompt. Uses a licensed "
                "third-party image model, fine-tuned by us only on licensed and commissioned artwork with "
                "artist consent. Outputs carry content credentials (C2PA) and a visible 'AI-assisted' label.",
        "role": "AI provider and AI producer (we fine-tune, integrate and operate it)",
        "users": "Canvas and API customers",
        "criticality": "High — copyright and consent, harmful or deceptive imagery, likeness of real people",
    },
    {
        "id": "AI-SYS-002", "name": "ScriptMate",
        "what": "Writing assistant that breaks scripts into scenes and shot lists. Calls a third-party "
                "foundation-model API with zero data retention; customer scripts are never used for training.",
        "role": "AI provider (we integrate and offer it); the model itself is a supplier's",
        "users": "Canvas customers",
        "criticality": "Medium — confidentiality of unreleased scripts, hallucinated content",
    },
    {
        "id": "AI-SYS-003", "name": "ArtistMatch",
        "what": "In-house ranking model that recommends marketplace artists for a commission based on "
                "portfolio style, availability and ratings.",
        "role": "AI provider and AI producer",
        "users": "Customers commissioning artists; affects artists' income",
        "criticality": "High — fairness to artists (visibility and earnings), transparency of ranking",
    },
    {
        "id": "AI-SYS-004", "name": "SafeFrame",
        "what": "Vendor content-moderation service that screens prompts and generated images for prohibited "
                "content (sexual content involving minors, extremist symbols, real-person deepfakes).",
        "role": "AI customer / user (we buy it and rely on it as a control)",
        "users": "Runs automatically on all StoryFrame traffic",
        "criticality": "High — a failure lets harmful content through",
    },
    {
        "id": "AI-SYS-005", "name": "CodeAssist",
        "what": "Approved AI coding assistant used by engineers in the IDE, business plan with no training "
                "on our code.",
        "role": "AI customer / user",
        "users": "Engineering staff",
        "criticality": "Medium — source code and secrets exposure, insecure suggestions",
    },
]

# People are shown as role tags such as [CEO] so the kit reads as a template.
# Replace a tag with a real name if you prefer. In a startup one person often holds two roles —
# that is fine as long as conflicts are managed (see IMS-GOV-001).
ROLES = {
    "CEO": ("[CEO]", "Chief Executive Officer and co-founder — top management, chairs the Trust Council"),
    "CTO": ("[CTO]", "Chief Technology Officer and co-founder — owns engineering, the development lifecycle and the platform"),
    "CISO": ("[Security Lead]", "Security Lead (acting CISO) — ISMS owner"),
    "CAIO": ("[Head of AI]", "Head of AI — AIMS owner, chairs the AI Release Review"),
    "DPO": ("[Privacy and Legal Lead]", "Privacy and Legal Lead — Data Protection Officer"),
    "CREA": ("[Creative Director]", "Creative Director — voice of artists and creators, content-safety sign-off"),
    "HOP": ("[People and Operations Lead]", "People and Operations Lead — hiring, onboarding, training, offboarding"),
    "IMSC": ("[Compliance Coordinator]", "Compliance Coordinator — runs the document register, audit calendar and corrective-action log"),
    "HOD": ("[Data and ML Lead]", "Data and ML Lead — datasets, data quality, model training and evaluation"),
    "SRE": ("[Platform Engineer]", "Platform Engineer (SRE) — cloud, availability, backups and continuity"),
    "LEGAL": ("[Legal Counsel]", "External Legal Counsel (part-time) — contracts, IP and copyright"),
}

COMMITTEES = {
    "Trust Council": "Top-management body for both standards. Chair: CEO. Members: CTO, Security Lead, Head of AI, "
                     "Privacy and Legal Lead, Creative Director. Meets monthly (30–45 minutes) and acts as the "
                     "management review twice a year. Approves policies, objectives and risk acceptance above Medium.",
    "AI Release Review": "Go / no-go gate for new or significantly changed AI systems. Chair: Head of AI. Members: "
                         "Creative Director, Privacy and Legal Lead, Security Lead, product owner, and one member of "
                         "the external Artist Advisory Panel. Meets when a release needs it.",
}

TECH = {
    "cloud": "AWS — eu-west-1 (Ireland) primary; me-central-1 (UAE) for UAE enterprise customers who require it",
    "foundation_model": "Third-party foundation-model and image-model APIs under enterprise terms (no training on our data, zero or 30-day retention)",
    "identity": "Single sign-on with phishing-resistant MFA (passkeys / security keys) for all staff and contractors",
    "devices": "Company-managed laptops with disk encryption, EDR and automatic patching",
    "sdlc": "GitHub, trunk-based development, CI/CD with mandatory code review, SAST, dependency and secret scanning, infrastructure as code",
    "payments": "Card payments handled entirely by a PCI DSS-certified payment processor (we never store card data)",
}

LAWS = [
    ("UAE Federal Decree-Law No. 45 of 2021 (Personal Data Protection Law)", "Personal data of UAE customers, artists and staff"),
    ("UAE Federal Decree-Law No. 38 of 2021 (Copyright and Neighbouring Rights)", "Artwork, scripts and generated outputs"),
    ("EU General Data Protection Regulation (GDPR) and UK GDPR", "EU/UK customers, artists and remote staff"),
    ("EU Artificial Intelligence Act (Regulation (EU) 2024/1689)", "Transparency duties for AI-generated content and deepfakes (Art. 50); AI literacy (Art. 4); general-purpose model downstream obligations"),
    ("EU Copyright (DSM) Directive 2019/790, Art. 4 text-and-data-mining opt-out", "Training-data sourcing and artist opt-outs"),
    ("EU Platform-to-Business Regulation (EU) 2019/1150", "Transparency of ranking parameters on the Commons marketplace (ArtistMatch)"),
    ("Consumer protection and advertising rules in target markets", "Labelling of AI-generated content used in ads"),
    ("Customer contracts, data processing agreements and the Artist Agreement", "Security, AI-use, confidentiality, IP and breach-notification terms"),
]

STANDARDS = [
    "ISO/IEC 27001:2022 (+ Amd 1:2024) — Information security management systems — Requirements",
    "ISO/IEC 42001:2023 — Artificial intelligence — Management system",
    "ISO/IEC 27002:2022 — Information security controls (guidance)",
    "ISO/IEC 23894:2023 — AI risk management (guidance)",
    "ISO/IEC 42005:2025 — AI system impact assessment (guidance)",
    "ISO/IEC 22989:2022 — AI concepts and terminology",
    "ISO 31000:2018 — Risk management guidelines",
    "NIST AI Risk Management Framework 1.0 and OWASP Top 10 for LLM Applications (optional references)",
]

# Risk scales used everywhere (methodology, register, impact assessment). Sized for a startup.
LIKELIHOOD = [
    (1, "Rare", "Not expected in the next 3 years"),
    (2, "Unlikely", "Could happen once in 2–3 years"),
    (3, "Possible", "Could happen about once a year"),
    (4, "Likely", "Expected several times a year"),
    (5, "Almost certain", "Expected monthly or already happening"),
]
IMPACT = [
    (1, "Negligible", "No harm to people; cost < USD 5k; nobody outside notices"),
    (2, "Minor", "Short inconvenience for a few users or artists; < USD 25k; one customer complaint"),
    (3, "Moderate", "Noticeable harm, unfair outcome or data exposure for a limited group; < USD 100k; a customer escalates or a regulator asks questions"),
    (4, "Major", "Serious harm to people or rights, notifiable data breach, IP infringement claim; < USD 500k; loss of a key customer"),
    (5, "Severe", "Harm to a vulnerable person, widespread unfair or deceptive outcomes, or > USD 500k; threatens the company's survival or market access"),
]
LEVELS = [
    ("Low", 1, 4, "Accept; risk owner monitors"),
    ("Medium", 5, 9, "Treat, or accept by the risk owner; review every 6 months"),
    ("High", 10, 15, "Must treat; residual acceptance only by the Security Lead or Head of AI plus the Trust Council"),
    ("Critical", 16, 25, "Not acceptable; stop, redesign or withdraw; tell the CEO within 24 hours"),
]


def level_for(score: int) -> str:
    for name, lo, hi, _ in LEVELS:
        if lo <= score <= hi:
            return name
    raise ValueError(score)


ID_FORMATS = [
    ("Information-security risk", "RSK-IS-001"),
    ("AI risk", "RSK-AI-001"),
    ("AI system", "AI-SYS-001"),
    ("Information asset", "AST-001"),
    ("AI system impact assessment", "AIIA-2026-01"),
    ("Incident", "INC-2026-001"),
    ("Nonconformity", "NC-2026-001"),
    ("Corrective action", "CA-2026-001"),
    ("Internal audit", "AUD-2026-01"),
    ("Objective", "OBJ-01"),
    ("Supplier", "SUP-01"),
]

# Master document register. Every cross-reference in the kit uses these IDs.
# (id, title, owner role key, folder, kind)
DOCS = [
    ("IMS-GDE-001", "Start Here — Build Your ISMS and AIMS with TWYNTRUST", "IMSC", "00 Start Here", "docx"),
    ("IMS-WBK-001", "Starter Workbook — Gap Assessment, Roadmap, Crosswalk and Document Register", "IMSC", "00 Start Here", "xlsx"),
    ("IMS-MAN-001", "Integrated Management System Manual (ISMS + AIMS)", "CEO", "01 Ground - Context and Leadership", "docx"),
    ("IMS-REG-001", "Context, Interested Parties and Scope Register", "IMSC", "01 Ground - Context and Leadership", "xlsx"),
    ("IMS-POL-001", "Information Security and Responsible AI Policy", "CEO", "01 Ground - Context and Leadership", "docx"),
    ("IMS-GOV-001", "Governance Charter, Roles and Responsibilities", "CEO", "01 Ground - Context and Leadership", "docx"),
    ("IMS-PRO-001", "Risk Management Methodology (Information Security and AI)", "CISO", "02 Gauge - Risk and Planning", "docx"),
    ("IMS-REG-002", "Integrated Risk Register and Treatment Plan", "CISO", "02 Gauge - Risk and Planning", "xlsx"),
    ("IMS-PRO-002", "AI System Impact Assessment Procedure and Worked Example", "CAIO", "02 Gauge - Risk and Planning", "docx"),
    ("IMS-SOA-001", "Statement of Applicability — ISO/IEC 27001:2022 Annex A", "CISO", "02 Gauge - Risk and Planning", "xlsx"),
    ("IMS-SOA-002", "Statement of Applicability — ISO/IEC 42001:2023 Annex A", "CAIO", "02 Gauge - Risk and Planning", "xlsx"),
    ("IMS-REG-003", "Objectives, Metrics and Monitoring Plan", "IMSC", "02 Gauge - Risk and Planning", "xlsx"),
    ("IMS-PRO-003", "Competence, Awareness and Communication Procedure", "HOP", "03 Equip - Support", "docx"),
    ("IMS-REG-004", "Competence Matrix, Training Records and Communication Plan", "HOP", "03 Equip - Support", "xlsx"),
    ("IMS-PRO-004", "Documented Information Control Procedure", "IMSC", "03 Equip - Support", "docx"),
    ("IMS-POL-002", "Secure and Responsible Development Lifecycle Policy (AppSec + AI)", "CTO", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-POL-003", "Data Governance and Privacy Policy for AI", "HOD", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-POL-004", "Access Control Policy", "CISO", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-POL-005", "Acceptable Use Policy (including Generative AI)", "CISO", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-POL-006", "Supplier and Third-Party AI Policy", "DPO", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-PRO-005", "Incident Management Procedure (Security and AI Incidents)", "CISO", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-PRO-006", "Business Continuity and ICT Readiness Plan", "SRE", "04 Operate - Lifecycle Controls", "docx"),
    ("IMS-REG-005", "Asset and AI System Inventory", "CISO", "04 Operate - Lifecycle Controls", "xlsx"),
    ("IMS-REG-006", "Incident and Event Log", "CISO", "04 Operate - Lifecycle Controls", "xlsx"),
    ("IMS-PRO-007", "Internal Audit Procedure, Programme and Report Template", "IMSC", "05 Prove and Improve", "docx"),
    ("IMS-REG-007", "Internal Audit Programme and Checklist", "IMSC", "05 Prove and Improve", "xlsx"),
    ("IMS-PRO-008", "Management Review Procedure and Example Minutes", "CEO", "05 Prove and Improve", "docx"),
    ("IMS-PRO-009", "Nonconformity, Corrective Action and Improvement Procedure", "IMSC", "05 Prove and Improve", "docx"),
    ("IMS-REG-008", "Nonconformity, Corrective Action and Improvement Log", "IMSC", "05 Prove and Improve", "xlsx"),
]

DOC_INDEX = {d[0]: d for d in DOCS}


def ref(doc_id: str) -> str:
    """Cross-reference text, e.g. 'IMS-PRO-001 Risk Management Methodology (...)'."""
    return f"{doc_id} {DOC_INDEX[doc_id][1]}"


def person(key: str) -> str:
    return ROLES[key][0]


def title_of(key: str) -> str:
    return ROLES[key][1].split(" — ")[0]


def who(key: str) -> str:
    """Label for a role holder. With role tags this is just the tag, e.g. '[Security Lead]'.
    If you replace a tag with a real name, it becomes 'Name (Title)'."""
    if person(key).startswith("["):
        return person(key)
    return f"{person(key)} ({title_of(key)})"

# ---------------------------------------------------------------------------
# Shared worked-example records. Documents that mention these must use the
# same IDs and facts so that the kit reads as one consistent story.
# ---------------------------------------------------------------------------
KEY_RISKS = [
    # id, title, system/asset, owner key, inherent L, I, residual L, I, treatment, main controls (27001 / 42001)
    ("RSK-AI-001", "StoryFrame fine-tuning set contains artwork without valid consent or licence", "AI-SYS-001", "HOD",
     4, 4, 2, 4, "Modify", "42001 A.7.3, A.7.5, A.4.3; 27001 5.32"),
    ("RSK-AI-002", "Prompt or filter bypass lets StoryFrame produce a deceptive deepfake of a real person", "AI-SYS-001", "CAIO",
     3, 5, 2, 4, "Modify", "42001 A.6.2.4, A.6.2.6, A.10.3; 27001 8.16"),
    ("RSK-AI-003", "ArtistMatch ranking systematically under-exposes new or non-English-portfolio artists", "AI-SYS-003", "CAIO",
     4, 3, 2, 3, "Modify", "42001 A.5.2–A.5.4, A.6.2.4, A.8.2"),
    ("RSK-AI-004", "ScriptMate hallucinates scenes or leaks one customer's script into another's session", "AI-SYS-002", "CAIO",
     3, 4, 1, 4, "Modify", "42001 A.6.2.4, A.9.3; 27001 8.11, 8.26"),
    ("RSK-AI-005", "SafeFrame vendor model update silently lowers detection of prohibited content", "AI-SYS-004", "CREA",
     3, 5, 2, 5, "Modify", "42001 A.10.3, A.6.2.6; 27001 5.22"),
    ("RSK-IS-001", "Unreleased customer scripts exposed through a misconfigured storage bucket", "AST-004", "SRE",
     3, 4, 1, 4, "Modify", "27001 8.9, 8.12, 8.15, 5.23"),
    ("RSK-IS-002", "Account takeover of an engineer through phishing leads to production access", "AST-010", "CISO",
     3, 5, 1, 5, "Modify", "27001 5.17, 8.2, 8.5, 6.3"),
    ("RSK-IS-003", "Secrets or source code pasted into unapproved AI tools by staff", "AST-009", "CISO",
     4, 3, 2, 3, "Modify", "27001 5.10, 6.3, 8.12; 42001 A.9.2, A.9.4"),
    ("RSK-IS-004", "Loss of the primary cloud region stops Canvas and the API for more than a day", "AST-001", "SRE",
     2, 4, 2, 2, "Modify", "27001 5.29, 5.30, 8.13, 8.14"),
    ("RSK-IS-005", "Vulnerable open-source dependency exploited in the Canvas web app", "AST-002", "CTO",
     3, 4, 2, 3, "Modify", "27001 8.8, 8.25, 8.28, 8.29"),
]

OBJECTIVES = [
    # id, objective, metric, target, owner key
    ("OBJ-01", "Certify the integrated system", "ISO/IEC 27001 and ISO/IEC 42001 certificates issued", "Both by 2027-09-30", "CEO"),
    ("OBJ-02", "Every AI release passes the AI Release Review", "% of AI releases with an approved impact assessment and gate record", "100%", "CAIO"),
    ("OBJ-03", "Respect artists' rights in training data", "% of fine-tuning images with a verified licence or consent record", "100%; zero unresolved opt-out requests older than 14 days", "HOD"),
    ("OBJ-04", "Keep critical vulnerabilities short-lived", "Median days to fix critical/high vulnerabilities in production", "Critical ≤ 7 days, high ≤ 30 days", "CTO"),
    ("OBJ-05", "Make people the strongest control", "Staff completing security + AI awareness training; phishing-simulation report rate", "100% within 30 days of joining and yearly; report rate ≥ 60%", "HOP"),
    ("OBJ-06", "Fair exposure for artists", "ArtistMatch exposure ratio for new vs established artists (top-10 results)", "≥ 0.8 every month", "CAIO"),
    ("OBJ-07", "Stay available", "Canvas and API monthly availability", "≥ 99.5%", "SRE"),
]

SAMPLE_INCIDENT = {
    "id": "INC-2026-007",
    "title": "SafeFrame missed a real-person deepfake after a vendor model update",
    "date": "2026-08-14",
    "type": "AI incident (content safety) — also a supplier issue",
    "summary": "A customer generated a storyboard panel showing a recognisable public figure in a fabricated scene. "
               "SafeFrame's vendor had shipped a model update two days earlier that lowered its likeness-detection "
               "rate. Our weekly canary test set caught the drop 3 days later; the customer had not published the image.",
    "severity": "High (S2)",
    "actions": "Rolled SafeFrame back to the previous model version via the vendor's pinning option; added our own "
               "likeness check before image delivery; re-ran the canary set daily for 30 days; informed the customer.",
    "links": "RSK-AI-005; NC-2026-003; CA-2026-004",
}

SAMPLE_AUDIT = {
    "id": "AUD-2026-02",
    "dates": "2026-09-15 to 2026-09-19",
    "auditor": "Independent auditor (contracted) plus the [Compliance Coordinator] as audit coordinator",
    "scope": "Whole integrated management system, both standards, remote audit",
    "findings": [
        ("NC-2026-003", "Minor nonconformity", "42001 A.10.3 / 27001 5.22",
         "Supplier changes to SafeFrame were not assessed before going live; the supplier agreement does not "
         "require notice of model changes."),
        ("NC-2026-004", "Minor nonconformity", "27001 7.2 / 42001 7.2",
         "Two contractors who joined in July had not completed awareness training within 30 days."),
        ("OFI-2026-05", "Opportunity for improvement", "42001 A.6.2.6",
         "ArtistMatch fairness metric is reviewed monthly but not automatically alerted."),
    ],
}

SAMPLE_CAPA = [
    ("CA-2026-004", "NC-2026-003", "Root cause: supplier onboarding checklist had no AI-model change clause. Action: add a "
     "'model change notification and version pinning' clause to the AI supplier contract template and to the SafeFrame "
     "agreement; add supplier model changes to the change-management trigger list.", "DPO", "2026-11-30"),
    ("CA-2026-005", "NC-2026-004", "Root cause: contractor onboarding handled by hiring managers, not People Ops. Action: route "
     "all contractor onboarding through the People Ops checklist with automatic training enrolment and a day-25 reminder.",
     "HOP", "2026-10-31"),
]

# Key information assets (the inventory IMS-REG-005 lists these first; risks refer to them).
ASSETS = [
    # id, name, type, owner key, classification, location
    ("AST-001", "Production cloud environment (AWS accounts, eu-west-1 and me-central-1)", "Service / infrastructure", "SRE", "Confidential", "AWS"),
    ("AST-002", "Quillfen Canvas web application and its source code", "Software", "CTO", "Confidential", "GitHub, AWS"),
    ("AST-003", "Quillfen Commons marketplace (artist profiles, commissions, payouts data)", "Software + personal data", "CTO", "Confidential", "AWS, payment processor"),
    ("AST-004", "Customer scripts, prompts and project files", "Customer data", "CTO", "Restricted", "AWS S3 (encrypted)"),
    ("AST-005", "Artist portfolios and consent / licence records", "Personal data + IP", "HOD", "Restricted", "AWS S3, consent ledger"),
    ("AST-006", "StoryFrame fine-tuning datasets and model weights", "AI asset (data + model)", "HOD", "Restricted", "AWS S3, model registry"),
    ("AST-007", "ArtistMatch model, features and evaluation sets", "AI asset", "HOD", "Confidential", "Model registry"),
    ("AST-008", "Foundation-model and image-model API keys and service accounts", "Credentials", "SRE", "Restricted", "Secrets manager"),
    ("AST-009", "Company source code repositories", "Software", "CTO", "Confidential", "GitHub"),
    ("AST-010", "Staff identities, SSO and company laptops", "Identity / endpoints", "CISO", "Confidential", "Identity provider, MDM"),
    ("AST-011", "Business records (finance, HR, contracts)", "Business data", "HOP", "Confidential", "SaaS suite"),
    ("AST-012", "Logs and monitoring data (application, security, AI output logs)", "Operational data", "SRE", "Confidential", "Log platform"),
]
