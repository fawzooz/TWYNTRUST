"""Statement of Applicability — ISO/IEC 42001:2023 Annex A (38 controls).

Control names are short paraphrases for orientation only; use your licensed copy of
ISO/IEC 42001 (Annex A and the Annex B implementation guidance) for the authoritative wording.
"""
from org import AI_SYSTEMS, ORG, who

N = ORG["name"]
I, P, PL = "Implemented", "Partially implemented", "Planned"
ALL = "All"

# id, short name (paraphrased), area, applicable, reasons, systems, linked risks, status, how / evidence, owner, related 27001
C = [
    ("A.2.2", "AI policy", "Policies related to AI", "Yes", "R,C,B", ALL, "All", I,
     "IMS-POL-001 section 3.2 sets responsible-AI principles; approved by the Trust Council.", "CEO", "5.1"),
    ("A.2.3", "Alignment with other organisational policies", "Policies related to AI", "Yes", "B", ALL, "—", I,
     "One integrated policy set; AI rules embedded in POL-002 to POL-006 rather than a separate silo.", "IMSC", "5.1"),
    ("A.2.4", "Review of the AI policy", "Policies related to AI", "Yes", "B", ALL, "—", I,
     "Yearly review and after major change (new model, new law) — IMS-PRO-008 input.", "CAIO", "5.1"),
    ("A.3.2", "AI roles and responsibilities", "Internal organisation", "Yes", "B", ALL, "All", I,
     "Head of AI as AIMS owner; named owner per AI system in IMS-REG-005; RACI in IMS-GOV-001.", "CEO", "5.2"),
    ("A.3.3", "Reporting of concerns", "Internal organisation", "Yes", "R,L", ALL, "RSK-AI-002, RSK-AI-003", I,
     "#trust-report, anonymous form, and an external address for artists and the public; no-retaliation rule.", "CAIO", "6.8"),
    ("A.4.2", "Resource documentation", "Resources for AI systems", "Yes", "B", ALL, "—", I,
     "'AI Resources' sheet in IMS-REG-005 lists data, tools, compute and people per system.", "HOD", "5.9"),
    ("A.4.3", "Data resources", "Resources for AI systems", "Yes", "R,L", "AI-SYS-001, AI-SYS-003", "RSK-AI-001", I,
     "Dataset register with provenance, licence/consent status and intended use.", "HOD", "5.9, 5.32"),
    ("A.4.4", "Tooling resources", "Resources for AI systems", "Yes", "B", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "—", I,
     "Training, evaluation and MLOps tools listed with versions in IMS-REG-005.", "HOD", "5.9"),
    ("A.4.5", "System and computing resources", "Resources for AI systems", "Yes", "B", "AI-SYS-001, AI-SYS-003", "RSK-IS-004", I,
     "GPU and API quotas, regions and capacity limits documented; energy use estimated per training run.", "SRE", "8.6"),
    ("A.4.6", "Human resources", "Resources for AI systems", "Yes", "R,L", ALL, "—", P,
     "AI competence matrix in IMS-REG-004; AI-literacy training (EU AI Act Art. 4) rolling out to all staff.", "HOP", "6.3"),
    ("A.5.2", "AI system impact assessment process", "Assessing impacts", "Yes", "R,L", ALL, "RSK-AI-002, RSK-AI-003", I,
     "IMS-PRO-002 defines when and how impact assessments are done.", "CAIO", "—"),
    ("A.5.3", "Documentation of AI system impact assessments", "Assessing impacts", "Yes", "L", ALL, "—", I,
     "AIIA records kept for system life + 5 years; AIIA-2026-01 (StoryFrame) and AIIA-2026-02 (ArtistMatch).", "CAIO", "5.33"),
    ("A.5.4", "Impact on individuals or groups of individuals", "Assessing impacts", "Yes", "R,L", ALL, "RSK-AI-002, RSK-AI-003", I,
     "AIIA covers artists, customers, depicted people and audiences; fairness tests for ArtistMatch.", "CAIO", "—"),
    ("A.5.5", "Societal impacts of AI systems", "Assessing impacts", "Yes", "R,B", "AI-SYS-001, AI-SYS-003", "RSK-AI-002", I,
     "AIIA covers misinformation, creative-labour market effects and environmental footprint.", "CAIO", "—"),
    ("A.6.1.2", "Objectives for responsible development", "AI system life cycle", "Yes", "B", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "All", I,
     "Responsible-development objectives in IMS-POL-002 and OBJ-02, OBJ-03, OBJ-06.", "CAIO", "—"),
    ("A.6.1.3", "Processes for responsible design and development", "AI system life cycle", "Yes", "R", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "All", I,
     "Integrated lifecycle with gates and the AI Release Review (IMS-POL-002).", "CTO", "8.25"),
    ("A.6.2.2", "AI system requirements and specification", "AI system life cycle", "Yes", "R", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-004", I,
     "Requirements template includes intended use, misuse cases, performance, fairness and safety criteria.", "CTO", "8.26"),
    ("A.6.2.3", "Documentation of design and development", "AI system life cycle", "Yes", "B", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "—", I,
     "Design docs and model cards in the repository; decisions logged.", "HOD", "8.27"),
    ("A.6.2.4", "Verification and validation", "AI system life cycle", "Yes", "R", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-002, RSK-AI-003, RSK-AI-004", I,
     "Evaluation suites (quality, fairness, safety red-teaming) with release thresholds.", "HOD", "8.29"),
    ("A.6.2.5", "Deployment", "AI system life cycle", "Yes", "R", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-005", I,
     "Staged roll-out, feature flags and rollback plan approved at the AI Release Review.", "CTO", "8.32"),
    ("A.6.2.6", "Operation and monitoring", "AI system life cycle", "Yes", "R", ALL, "RSK-AI-002, RSK-AI-003, RSK-AI-005", P,
     "Drift, abuse and content-safety canaries monitored; automatic fairness alerting planned (OFI-2026-05).", "CAIO", "8.16"),
    ("A.6.2.7", "Technical documentation", "AI system life cycle", "Yes", "C,L", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "—", I,
     "Model cards and system documentation for customers and auditors (IMS-PRO-004).", "HOD", "5.37"),
    ("A.6.2.8", "Recording of event logs", "AI system life cycle", "Yes", "R,L", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-002", I,
     "Prompt, output, moderation decision and model version logged with retention limits.", "SRE", "8.15"),
    ("A.7.2", "Data for development and enhancement", "Data for AI systems", "Yes", "R,L", "AI-SYS-001, AI-SYS-003", "RSK-AI-001", I,
     "IMS-POL-003 data-for-AI rules; customer data never used for training without opt-in.", "HOD", "5.34"),
    ("A.7.3", "Acquisition of data", "Data for AI systems", "Yes", "R,L", "AI-SYS-001, AI-SYS-003", "RSK-AI-001", I,
     "Licence or consent required before acquisition; EU text-and-data-mining opt-outs honoured.", "HOD", "5.32"),
    ("A.7.4", "Quality of data", "Data for AI systems", "Yes", "R", "AI-SYS-001, AI-SYS-003", "RSK-AI-003", I,
     "Quality checks (duplicates, labels, representativeness) recorded per dataset version.", "HOD", "—"),
    ("A.7.5", "Data provenance", "Data for AI systems", "Yes", "R,L", "AI-SYS-001, AI-SYS-003", "RSK-AI-001", I,
     "Consent and licence ledger links every training image to its source; 41 images without a verified record were removed in 2026.", "HOD", "5.32"),
    ("A.7.6", "Data preparation", "Data for AI systems", "Yes", "R", "AI-SYS-001, AI-SYS-003", "RSK-AI-003", I,
     "Documented, versioned preparation pipelines; personal data removed or masked.", "HOD", "8.11"),
    ("A.8.2", "System documentation and information for users", "Information for interested parties", "Yes", "L,C", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-002", I,
     "In-product AI notices, 'AI-assisted' labels, C2PA credentials, and a public 'How ArtistMatch works' page.", "CAIO", "—"),
    ("A.8.3", "External reporting", "Information for interested parties", "Yes", "L,B", ALL, "RSK-AI-002", I,
     "Public form for reporting harmful outputs or rights concerns; reviewed within 2 working days.", "CREA", "6.8"),
    ("A.8.4", "Communication of incidents", "Information for interested parties", "Yes", "L,C", ALL, "All", I,
     "Incident communication steps and templates in IMS-PRO-005.", "CISO", "5.26"),
    ("A.8.5", "Information for interested parties", "Information for interested parties", "Yes", "L,C", ALL, "—", I,
     "Obligations to customers, artists and regulators listed in IMS-REG-001 and the communication plan (IMS-REG-004).", "DPO", "5.31"),
    ("A.9.2", "Processes for responsible use of AI systems", "Use of AI systems", "Yes", "R", "AI-SYS-004, AI-SYS-005", "RSK-IS-003", I,
     "Generative-AI rules in IMS-POL-005; approved-tools list.", "CISO", "5.10"),
    ("A.9.3", "Objectives for responsible use", "Use of AI systems", "Yes", "B", "AI-SYS-004, AI-SYS-005", "RSK-IS-003", I,
     "Use objectives: no confidential data in unapproved tools; human review of AI-assisted code and support replies.", "CISO", "—"),
    ("A.9.4", "Intended use of the AI system", "Use of AI systems", "Yes", "R", ALL, "RSK-AI-004", I,
     "Intended and prohibited uses stated per system in IMS-REG-005 and in customer terms.", "CAIO", "—"),
    ("A.10.2", "Allocating responsibilities", "Third-party and customer relationships", "Yes", "C", ALL, "RSK-AI-005", I,
     "Responsibility split with model providers, SafeFrame vendor and customers set out in contracts.", "DPO", "5.19, 5.20"),
    ("A.10.3", "Suppliers", "Third-party and customer relationships", "Yes", "R,C", "AI-SYS-001, AI-SYS-002, AI-SYS-004, AI-SYS-005", "RSK-AI-005", P,
     "AI supplier due diligence in IMS-POL-006; model-change notice and version pinning being added (CA-2026-004).", "DPO", "5.19–5.22"),
    ("A.10.4", "Customers", "Third-party and customer relationships", "Yes", "C,L", "AI-SYS-001, AI-SYS-002, AI-SYS-003", "RSK-AI-002", I,
     "Customer terms set acceptable use, labelling duties and how we use (and do not use) their data.", "DPO", "5.20"),
]

REASONS = "R = treats a risk in IMS-REG-002 · L = legal/regulatory · C = contractual · B = business need / good practice"

ANNEX_C_OBJ = [
    ("Accountability", "Yes", "Named owner per AI system; AI Release Review records", "OBJ-02"),
    ("AI expertise", "Yes", "AI competence matrix and hiring plan", "OBJ-05"),
    ("Availability and quality of training data", "Yes", "Dataset register, quality checks, licensed sources only", "OBJ-03"),
    ("Environmental impact", "Yes", "Training runs sized and logged; prefer fine-tuning over training from scratch", "—"),
    ("Fairness", "Yes", "ArtistMatch exposure-ratio monitoring; depiction tests for StoryFrame", "OBJ-06"),
    ("Maintainability", "Yes", "Versioned models and pipelines; documented retraining", "—"),
    ("Privacy", "Yes", "No training on customer data without opt-in; masking", "—"),
    ("Robustness", "Yes", "Red-teaming, prompt-injection tests, canary sets", "OBJ-02"),
    ("Safety", "Yes", "SafeFrame plus own likeness check; prohibited-content rules", "—"),
    ("Security", "Yes", "Integrated with the ISMS (IMS-SOA-001)", "OBJ-04"),
    ("Transparency and explainability", "Yes", "Labels, C2PA credentials, public ArtistMatch explanation", "—"),
]
ANNEX_C_SRC = [
    ("Complexity of the environment", "Medium", "Open-ended creative prompts from many cultures and languages"),
    ("Lack of transparency and explainability", "High", "Image model behaviour is hard to explain; mitigated by documentation and labels"),
    ("Level of automation", "Medium", "Outputs are drafts refined by humans; ArtistMatch ranks automatically"),
    ("Risks related to machine learning", "High", "Training-data rights, bias, drift after supplier updates"),
    ("System hardware issues", "Low", "Cloud GPUs; capacity limits handled by quotas and fallbacks"),
    ("System life cycle issues", "Medium", "Frequent model updates; covered by gates and change management"),
    ("Technology readiness", "Medium", "Generative image models are new and fast-changing"),
]

WB = {
    "id": "IMS-SOA-002",
    "summary": f"Which of the 38 ISO/IEC 42001:2023 Annex A controls {N} applies, to which AI systems, why, and how far "
               "each is implemented. Required by ISO/IEC 42001 clause 6.1.3. Also records how the Annex C objectives "
               "and risk sources were considered.",
    "clauses": {"27001": "— (see IMS-SOA-001; related controls shown per row)",
                "42001": "6.1.3 AI risk treatment / Statement of Applicability; Annex A; Annex C"},
    "howto": [
        "All 38 controls must be listed. If you exclude one, say why (for example, you do no AI development at all).",
        "The 'AI systems' column shows where a control matters — useful when you have many systems with different roles.",
        "The 'Related 27001' column shows where one piece of evidence can serve both standards.",
        "Control names here are short paraphrases. Use your licensed copy of ISO/IEC 42001 (Annex A and the Annex B "
        "guidance) for the exact wording.",
    ],
    "sheets": [
        {
            "name": "SoA 42001",
            "title": "Statement of Applicability — ISO/IEC 42001:2023 Annex A",
            "intro": "Status values: Implemented · Partially implemented · Planned · Not implemented · Excluded. " + REASONS +
                     ". AI systems: " + "; ".join(f"{s['id']} {s['name']}" for s in AI_SYSTEMS) + ".",
            "headers": ["Control", "Control (short name)", "Control area", "Applicable?", "Reason", "AI systems",
                        "Linked risks", "Status", "How we do it / evidence", "Owner", "Related 27001"],
            "rows": [c for c in C],
            "widths": [9, 38, 26, 12, 9, 26, 24, 20, 66, 9, 12],
            "lists": {"Applicable?": ["Yes", "No"],
                      "Status": ["Implemented", "Partially implemented", "Planned", "Not implemented", "Excluded"]},
            "status": ["Status", "Applicable?"],
            "freeze_cols": 2,
            "blank_rows": 0,
        },
        {
            "name": "Annex C objectives",
            "title": "Organisational objectives for AI considered (ISO/IEC 42001 Annex C)",
            "intro": "Annex C lists objectives an organisation may pursue for AI. Record which ones you adopt and how — they feed IMS-REG-003.",
            "headers": ["Objective", "Relevant?", "How we pursue it", "Linked objective"],
            "rows": ANNEX_C_OBJ,
            "widths": [36, 11, 70, 15],
            "lists": {"Relevant?": ["Yes", "No"]},
            "status": ["Relevant?"],
            "blank_rows": 5,
        },
        {
            "name": "Annex C risk sources",
            "title": "AI risk sources considered (ISO/IEC 42001 Annex C)",
            "intro": "Annex C lists typical sources of AI risk. Rate how much each applies to you; high ones must appear in IMS-REG-002.",
            "headers": ["Risk source", "Relevance", "Why / where it shows up"],
            "rows": ANNEX_C_SRC,
            "widths": [40, 12, 80],
            "lists": {"Relevance": ["Low", "Medium", "High"]},
            "levels": ["Relevance"],
            "blank_rows": 5,
        },
        {
            "name": "Summary",
            "title": "Implementation summary",
            "intro": "Counts update automatically from the SoA sheet.",
            "headers": ["Control area", "Controls", "Implemented", "Partially implemented", "Planned", "Excluded"],
            "rows": [(a, f"=COUNTIF('SoA 42001'!C:C,A{{r}})",
                      f"=COUNTIFS('SoA 42001'!C:C,A{{r}},'SoA 42001'!H:H,\"Implemented\")",
                      f"=COUNTIFS('SoA 42001'!C:C,A{{r}},'SoA 42001'!H:H,\"Partially implemented\")",
                      f"=COUNTIFS('SoA 42001'!C:C,A{{r}},'SoA 42001'!H:H,\"Planned\")",
                      f"=COUNTIFS('SoA 42001'!C:C,A{{r}},'SoA 42001'!H:H,\"Excluded\")")
                     for a in dict.fromkeys(c[2] for c in C)]
                    + [("Total", "=SUM(B5:B13)", "=SUM(C5:C13)", "=SUM(D5:D13)", "=SUM(E5:E13)", "=SUM(F5:F13)")],
            "widths": [40, 11, 13, 13, 10, 10],
            "blank_rows": 0,
        },
        {
            "name": "Approval",
            "title": "SoA approval",
            "intro": "Approved by top management with the AI risk treatment plan and residual risks.",
            "headers": ["Version", "Date", "Approved by", "Decision", "Signature"],
            "rows": [("2.0", "2026-10-21", who("CEO") + " for the Trust Council",
                      "Approved together with residual AI risks in IMS-REG-002 (RSK-AI-005 residual High accepted until 2027-01-31)",
                      "[[signature]]")],
            "widths": [10, 12, 40, 60, 20],
            "blank_rows": 5,
        },
    ],
}

assert len(C) == 38, len(C)
assert len({c[2] for c in C}) == 9
