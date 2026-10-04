import datetime as dt

from org import who, AI_SYSTEMS, ASSETS, KEY_RISKS, ORG, ROLES, person, ref, title_of

from content.ims_pol_006 import SUPPLIERS

D = dt.date
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}
SF, SM, AM, SAFE, CA = (SYS[f"AI-SYS-00{i}"] for i in range(1, 6))


def owner(key):
    return who(key)


def risks_for(item_id):
    return ", ".join(r[0] for r in KEY_RISKS if r[2] == item_id) or "—"


REVIEW = '=IF({c}{{r}}="","",IF({c}{{r}}+365<TODAY(),"Overdue","On track"))'

# ---------------------------------------------------------------------------
# Information assets: org.ASSETS first, then ten more
# ---------------------------------------------------------------------------
# extra: id, name, type, owner key, class, location
EXTRA_ASSETS = [
    ("AST-013", f"{ORG['products'][2].split(' — ')[0]} and API keys issued to enterprise customers", "Software + credentials", "CTO",
     "Restricted", "AWS, secrets manager"),
    ("AST-014", "CI/CD pipelines, build runners and signing keys", "Service / infrastructure", "SRE",
     "Restricted", "GitHub, AWS"),
    ("AST-015", "Backups and snapshots (databases, S3, model registry)", "Data copy", "SRE", "Restricted",
     "AWS (separate backup account)"),
    ("AST-016", "Consent and licence ledger and opt-out log", "Records", "HOD", "Restricted", "Ledger database"),
    ("AST-017", "SafeFrame canary and red-team test sets (incl. likeness set)", "AI asset (evaluation data)",
     "CREA", "Restricted", "Model registry"),
    ("AST-018", "Prompt templates and system prompts for ScriptMate and StoryFrame", "AI asset (configuration)",
     "CAIO", "Confidential", "GitHub"),
    ("AST-019", "Customer and artist support tickets", "Customer data + personal data", "HOP", "Confidential",
     "Help-desk SaaS"),
    ("AST-020", "Company website and public documentation", "Public information", "CREA", "Public",
     "Static hosting"),
    ("AST-021", "Policies, procedures and management-system records", "Documented information", "IMSC",
     "Internal", "Company drive"),
    ("AST-022", "Brand assets and company-owned illustration library", "Intellectual property", "CREA",
     "Internal", "Company drive"),
]
EXTRA_ASSETS = [(a[0], a[1].replace("SafeFrame", SAFE).replace("ScriptMate", SM).replace("StoryFrame", SF),
                 *a[2:]) for a in EXTRA_ASSETS]

# C, I, A on the 1–5 impact scale; linked AI system; handling note
CIA = {
    "AST-001": (4, 4, 5, "All", "IaC only; no console changes without ticket"),
    "AST-002": (4, 4, 4, "—", "Branch protection; SAST/SCA in CI"),
    "AST-003": (4, 4, 4, "AI-SYS-003", "PII minimised; payouts via processor"),
    "AST-004": (5, 4, 4, "AI-SYS-001, AI-SYS-002", "Encrypted; never used for training without opt-in"),
    "AST-005": (5, 4, 3, "AI-SYS-001, AI-SYS-003", "Ledger check before any training use"),
    "AST-006": (5, 5, 3, "AI-SYS-001", "Named-group access; hashes in dataset record"),
    "AST-007": (4, 5, 3, "AI-SYS-003", "Fairness evaluation sets versioned"),
    "AST-008": (5, 4, 4, "AI-SYS-001, AI-SYS-002, AI-SYS-004", "Secrets manager; rotate every 90 days"),
    "AST-009": (4, 4, 3, "AI-SYS-005", "Private repos; secret scanning with push protection"),
    "AST-010": (4, 4, 4, "—", "Passkeys; MDM; EDR"),
    "AST-011": (4, 3, 3, "—", "SaaS suite with SSO; DLP rules"),
    "AST-012": (4, 4, 3, "All", "Retention 90 days for AI output logs; tamper-evident"),
    "AST-013": (5, 4, 5, "AI-SYS-001, AI-SYS-002", "Keys scoped per customer; quotas and rate limits"),
    "AST-014": (4, 5, 4, "—", "Runners ephemeral; OIDC to AWS; no long-lived keys"),
    "AST-015": (5, 5, 5, "All", "Immutable, cross-account; restore tested quarterly"),
    "AST-016": (4, 5, 3, "AI-SYS-001, AI-SYS-003", "Append-only; daily export to backup"),
    "AST-017": (4, 5, 3, "AI-SYS-004, AI-SYS-001", "Restricted access; harmful samples hashed, not viewable"),
    "AST-018": (3, 4, 3, "AI-SYS-001, AI-SYS-002", "Changes via pull request; prompt-injection tests"),
    "AST-019": (4, 3, 3, "—", "Masking of IDs; 2-year retention"),
    "AST-020": (1, 4, 3, "—", "Change approval by Creative Director"),
    "AST-021": (2, 4, 2, "—", "Version-controlled per IMS-PRO-004"),
    "AST-022": (2, 3, 2, "—", "Licence terms recorded"),
}
REVIEWED = {"AST-004": D(2025, 9, 10), "AST-019": D(2025, 8, 1)}  # two deliberately overdue
asset_rows = []
for a in ASSETS + EXTRA_ASSETS:
    c, i, av, sysl, note = CIA[a[0]]
    asset_rows.append((
        a[0], a[1], a[2], owner(a[3]), a[4], a[5], c, i, av,
        '=IF(COUNT(G{r}:I{r})=0,"",IF(MAX(G{r}:I{r})>=5,"Critical",IF(MAX(G{r}:I{r})=4,"High",'
        'IF(MAX(G{r}:I{r})=3,"Medium","Low"))))',
        sysl, risks_for(a[0]), note, REVIEWED.get(a[0], D(2026, 9, 25)), REVIEW.format(c="N"),
    ))
asset_rows.append(("[[AST-0xx]]", "[[asset name]]", "[[type]]", "[[owner]]", "[[class]]", "[[location]]",
                   "[[1-5]]", "[[1-5]]", "[[1-5]]",
                   '=IF(COUNT(G{r}:I{r})=0,"",IF(MAX(G{r}:I{r})>=5,"Critical",IF(MAX(G{r}:I{r})=4,"High",'
                   'IF(MAX(G{r}:I{r})=3,"Medium","Low"))))', "[[AI system]]", "[[risk IDs]]",
                   "[[handling]]", "[[date]]", REVIEW.format(c="N")))

# ---------------------------------------------------------------------------
# AI system inventory
# ---------------------------------------------------------------------------
# id -> (model type, model source, data used, affected people, owner, tech lead, AIIA, release status,
#        version, monitoring, human oversight, doc link, last review)
AI_EXTRA = {
    "AI-SYS-001": ("Diffusion image model, fine-tuned (LoRA adapters)", "Licensed base model from SUP-02; "
                   "fine-tuned in-house", "Licensed and consented artwork (AST-006); customer prompts at "
                   "run time (not stored for training)", "Customers; artists whose styles are used; people who "
                   "could be depicted; audiences of published storyboards", "CAIO", "HOD", "AIIA-2026-01",
                   "Live", "v2.4 (2026-09-24)", "Daily content-safety canary; monthly quality and drift review; "
                   "C2PA label sampling", "Users edit or reject every panel; likeness check blocks real-person "
                   "outputs; kill-switch per feature flag", D(2026, 9, 22)),
    "AI-SYS-002": ("Large language model via API (no fine-tuning)", "SUP-01 foundation-model provider, pinned "
                   "dated version", "Customer scripts at run time, zero retention", "Customers and their "
                   "unreleased scripts; writers named in scripts", "CAIO", "CTO", "AIIA-2026-03", "Live",
                   "Prompt template v1.7 / model pinned 2026-05", "Weekly hallucination spot-check (50 scripts); "
                   "cross-tenant leakage probes monthly", "Suggestions only; user accepts or edits every scene; "
                   "'report a problem' button", D(2026, 7, 14)),
    "AI-SYS-003": ("Gradient-boosted ranking model", "In-house", "Artist portfolios, availability, ratings "
                   "(AST-005, AST-007)", "Artists (visibility and income); customers choosing artists",
                   "CAIO", "HOD", "AIIA-2026-02", "Live", "v1.3 (2026-06-30)",
                   "Weekly exposure-ratio metric (OBJ-06); monthly fairness review",
                   "Customers see 'why this artist'; artists can appeal ranking; manual boost for new artists",
                   D(2026, 8, 30)),
    "AI-SYS-004": ("Vendor classification models (image + text)", "SUP-03 vendor, version pinned since "
                   "INC-2026-007", "Prompts and generated images in transit", "Anyone who could be harmed by "
                   "prohibited or deceptive content; customers", "CREA", "SRE", "AIIA-2026-04", "Live",
                   "Vendor model pinned 2026-08-17", "Daily canary set (daily for 30 days after INC-2026-007, "
                   "then weekly); vendor detection-rate report", "Blocked items reviewed by Trust & Safety; "
                   "our own likeness check as second layer", D(2026, 9, 18)),
    "AI-SYS-005": ("Code-generation LLM (vendor service)", "SUP-07, business plan", "Code context from "
                   "the IDE (AST-009)", "Engineers; indirectly customers if insecure code ships", "CTO", "CISO",
                   "Screening only (low impact)", "Live (internal tool)", "Vendor-managed",
                   "Admin settings checked yearly; SAST findings tagged by origin",
                   "Every suggestion reviewed by a human; normal code review and CI apply", D(2025, 10, 1)),
}
ai_rows = []
for s in AI_SYSTEMS:
    x = AI_EXTRA[s["id"]]
    crit, _, why = s["criticality"].partition(" — ")
    ai_rows.append((
        s["id"], s["name"], s["what"], s["role"], x[0], x[1], x[2], s["users"], x[3], crit, why,
        owner(x[4]), owner(x[5]), x[6], x[7], x[8], x[9], x[10], risks_for(s["id"]),
        f"Model card + design notes: registry/{s['name'].lower()}", x[11], REVIEW.format(c="U"),
    ))
ai_rows.append(("[[AI-SYS-0xx]]", "[[name]]", "[[purpose]]", "[[role]]", "[[model type]]", "[[source]]",
                "[[data]]", "[[users]]", "[[affected people]]", "[[level]]", "[[why]]", "[[owner]]",
                "[[technical lead]]", "[[AIIA ref]]", "[[status]]", "[[version]]", "[[monitoring]]",
                "[[oversight]]", "[[risk IDs]]", "[[link]]", "[[date]]", REVIEW.format(c="U")))

# ---------------------------------------------------------------------------
# AI resources (42001 A.4.2–A.4.6)
# ---------------------------------------------------------------------------
res_rows = [
    ("AI-SYS-001", "Data", "StoryFrame fine-tuning dataset DS-SF-2026-Q3 (3,159 images after quarantine)",
     "Internal, from licensed and consented artwork", "AST-006, AST-016", "HOD",
     "Ledger check in pipeline; dataset record; Restricted storage", "A.4.3"),
    ("AI-SYS-001", "Data", "Evaluation and red-team sets (prohibited content, likeness, style fidelity)",
     "Internal", "AST-017", "CREA", "Versioned; access limited to Trust & Safety", "A.4.3"),
    ("AI-SYS-001", "Tooling", "Training framework, model registry, experiment tracking, C2PA signing library",
     "Open source + internal", "AST-006", "HOD", "Pinned versions; SCA scanning; registry access by group", "A.4.4"),
    ("AI-SYS-001", "System and computing", "GPU training jobs (on demand) and inference endpoints, eu-west-1",
     "SUP-04 AWS", "AST-001", "SRE", "Budgets and quotas; IaC; separate training account", "A.4.5"),
    ("AI-SYS-001", "Human", "ML engineers (2), Trust & Safety reviewer (1), Artist Advisory Panel member",
     "Internal + panel", "—", "CAIO", "Competence per IMS-REG-004; red-team training", "A.4.6"),
    ("AI-SYS-002", "Data", "Customer scripts at run time; 120 synthetic test scripts", "Customers; internal",
     "AST-004", "CTO", "Zero-retention endpoint; synthetic data for tests", "A.4.3"),
    ("AI-SYS-002", "Tooling", "Prompt templates, evaluation harness, leakage probe set", "Internal", "AST-018",
     "CAIO", "Templates changed by pull request only", "A.4.4"),
    ("AI-SYS-002", "System and computing", "Foundation-model API (pinned version)", "SUP-01", "AST-008",
     "SRE", "Keys in secrets manager; per-tenant quotas", "A.4.5"),
    ("AI-SYS-003", "Data", "Artist features (style embeddings, availability, ratings) and fairness eval set",
     "Internal (Commons data)", "AST-005, AST-007", "HOD", "Pseudonymised artist IDs; bias note per version",
     "A.4.3"),
    ("AI-SYS-003", "Tooling", "Ranking library, fairness metrics toolkit, monitoring dashboard",
     "Open source + internal", "AST-007", "HOD", "Weekly exposure-ratio job; alert planned (OFI-2026-05)", "A.4.4"),
    ("AI-SYS-003", "Human", "Data scientist (1), Commons product owner, artist appeals handler",
     "Internal", "—", "CAIO", "Appeals reviewed within 10 working days", "A.4.6"),
    ("AI-SYS-004", "System and computing", "Vendor moderation API; our likeness-check service on AWS",
     "SUP-03; SUP-04", "AST-001, AST-008", "SRE", "Version pinned; fail-closed if vendor unavailable", "A.4.5"),
    ("AI-SYS-005", "Tooling", "IDE plug-in, business plan admin console", "SUP-07", "AST-009", "CTO",
     "Training on our code disabled; telemetry minimised", "A.4.4"),
    ("[[AI-SYS-0xx]]", "[[type]]", "[[resource]]", "[[provided by]]", "[[asset IDs]]", "[[owner]]",
     "[[controls]]", "[[A.4.x]]"),
]
res_rows = [(r[0], SYS.get(r[0], "[[name]]"), r[1], r[2].replace("StoryFrame", SF), r[3], r[4],
             owner(r[5]) if r[5] in ROLES else r[5], r[6], r[7]) for r in res_rows]

# ---------------------------------------------------------------------------
# Suppliers summary (same records as IMS-POL-006 section 9)
# ---------------------------------------------------------------------------
sup_rows = []
for s in SUPPLIERS:
    last = s[11] if s[11].startswith("[[") else D.fromisoformat(s[11])
    nxt = s[12] if s[12].startswith("[[") else D.fromisoformat(s[12])
    sup_rows.append((s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9],
                     owner(s[10]) if not s[1].startswith("[[") else "[[owner]]", last, nxt,
                     '=IF(M{r}="","",IF(M{r}<TODAY(),"Overdue","On track"))', s[13]))

WB = {
    "id": "IMS-REG-005",
    "summary": "One inventory of the information assets, AI systems, AI resources and suppliers inside the "
               "scope of the integrated management system — the starting point for risk assessment, the "
               "Statements of Applicability and every audit trail.",
    "clauses": {"27001": "Annex A 5.9, 5.10, 5.11, 5.12, 5.19–5.23 (supplier summary)",
                "42001": "4.1 (AI roles); Annex A.4.2–A.4.6, A.6.2.7; supports 6.1.4 and 8.4"},
    "howto": [
        "Start with the AI System Inventory: one row per AI system you build, integrate or use, including "
        "AI tools staff use (like a coding assistant). Then list the assets those systems depend on.",
        "Every risk in the risk register should point to an asset or AI system ID in this workbook "
        f"({ref('IMS-REG-002')}).",
        "Review owners and classifications every 12 months and after any significant change. The 'Review "
        "status' columns turn red when the last review is more than a year old.",
        f"The Suppliers sheet mirrors the register in {ref('IMS-POL-006')}; keep them in step.",
    ],
    "sheets": [
        {
            "name": "Information Assets",
            "title": "Information asset inventory (27001 Annex A 5.9, 5.12)",
            "intro": "One row per information asset or group of similar assets. Score confidentiality (C), "
                     "integrity (I) and availability (A) on the 1–5 impact scale from IMS-PRO-001; the "
                     "criticality column calculates from the highest score. Classification follows IMS-POL-003.",
            "headers": ["Asset ID", "Asset", "Type", "Owner", "Classification", "Location", "C (1-5)",
                        "I (1-5)", "A (1-5)", "Criticality", "Linked AI system(s)", "Linked risks",
                        "Handling notes", "Last reviewed", "Review status"],
            "rows": asset_rows,
            "widths": [10, 42, 22, 30, 14, 24, 8, 8, 8, 12, 24, 16, 38, 13, 13],
            "lists": {"Classification": ["Public", "Internal", "Confidential", "Restricted"],
                      "C (1-5)": ["1", "2", "3", "4", "5"], "I (1-5)": ["1", "2", "3", "4", "5"],
                      "A (1-5)": ["1", "2", "3", "4", "5"]},
            "levels": ["Criticality"],
            "status": ["Review status"],
            "formulas": {"Criticality": '=IF(COUNT(G{r}:I{r})=0,"",IF(MAX(G{r}:I{r})>=5,"Critical",'
                                        'IF(MAX(G{r}:I{r})=4,"High",IF(MAX(G{r}:I{r})=3,"Medium","Low"))))',
                         "Review status": REVIEW.format(c="N")},
            "freeze_cols": 2,
        },
        {
            "name": "AI System Inventory",
            "title": "AI system inventory (42001 4.1, A.4.2, A.6.2.7)",
            "intro": "One row per AI system in scope, whatever our role (provider, producer, customer/user). "
                     "Register a system at gate G0 of IMS-POL-002 and update it at every release. Release status "
                     "and the AIIA reference are checked by the AI Release Review.",
            "headers": ["AI system ID", "Name", "Purpose", "Our role", "Model type", "Model source", "Data used",
                        "Users", "Affected people", "Criticality", "Why", "System owner", "Technical lead",
                        "AIIA ref", "Release status", "Current version", "Monitoring",
                        "Human oversight measure", "Linked risks", "Documentation", "Last review",
                        "Review status"],
            "rows": ai_rows,
            "widths": [11, 13, 42, 26, 24, 26, 30, 18, 30, 11, 30, 26, 26, 14, 14, 18, 34, 36, 16, 26, 12, 12],
            "lists": {"Criticality": ["Low", "Medium", "High", "Critical"],
                      "Release status": ["Idea", "In development", "Pilot", "Live", "Live (internal tool)",
                                         "Suspended", "Retired"]},
            "levels": ["Criticality"],
            "status": ["Review status"],
            "formulas": {"Review status": REVIEW.format(c="U")},
            "freeze_cols": 2,
            "blank_rows": 15,
        },
        {
            "name": "AI Resources",
            "title": "Resources for AI systems (42001 A.4.2–A.4.6)",
            "intro": "For each AI system, document the data, tooling, system and computing, and human resources "
                     "it depends on (A.4.3–A.4.6). Together with the inventory this is the resource documentation "
                     "asked for in A.4.2.",
            "headers": ["AI system ID", "AI system", "Resource type", "Resource", "Provided by",
                        "Linked assets", "Owner", "Controls in place", "42001 control"],
            "rows": res_rows,
            "widths": [11, 13, 18, 48, 22, 18, 30, 44, 10],
            "lists": {"Resource type": ["Data", "Tooling", "System and computing", "Human"],
                      "42001 control": ["A.4.2", "A.4.3", "A.4.4", "A.4.5", "A.4.6"]},
            "freeze_cols": 2,
        },
        {
            "name": "Suppliers",
            "title": "Supplier summary (27001 5.19–5.23; 42001 A.10.2–A.10.3)",
            "intro": "Same records as the supplier register in IMS-POL-006. Tier 1 suppliers are reviewed every "
                     "6–12 months; 'Review status' turns red when the next review date has passed.",
            "headers": ["Supplier ID", "Supplier", "Service", "Tier", "Supports (systems / assets)",
                        "Data shared (highest class)", "Region", "AI clauses", "Version pinning",
                        "Evidence", "Supplier owner", "Last review", "Next review", "Review status",
                        "Contract status"],
            "rows": sup_rows,
            "widths": [10, 30, 30, 16, 26, 30, 16, 34, 26, 34, 28, 12, 12, 12, 14],
            "lists": {"Tier": ["Tier 1 — Critical", "Tier 2 — Important", "Tier 3 — Low"],
                      "Contract status": ["Implemented", "In progress", "Planned", "Not implemented"]},
            "status": ["Review status", "Contract status"],
            "formulas": {"Review status": '=IF(M{r}="","",IF(M{r}<TODAY(),"Overdue","On track"))'},
            "freeze_cols": 2,
        },
    ],
}
