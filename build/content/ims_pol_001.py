from org import ORG, person, ref, who

N = ORG["name"]

DOC = {
    "id": "IMS-POL-001",
    "summary": f"The one top-level policy that commits {N} to protecting information and to developing, "
               "providing and using AI responsibly. Every other policy and procedure in the kit hangs from it.",
    "clauses": {"27001": "5.2 Information security policy; Annex A 5.1",
                "42001": "5.2 AI policy; Annex A.2.2–A.2.4"},
    "howto": [
        "Keep this policy short (2–3 pages of body text). Detail belongs in the topic policies it points to.",
        "Both standards require the policy to include a commitment to meet requirements and a commitment "
        "to continual improvement — keep sections 4 and 7 even if you rewrite everything else.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"{N} turns writers' ideas into visual stories with the help of AI and of human artists. "
              "Our customers trust us with unreleased scripts and brand material; our artists trust us with "
              "their portfolios, their income and their creative rights; the public trusts that what we help "
              "produce is honest about how it was made. This policy states how we protect that trust."),
        ("p", "It sets the direction for our integrated management system — the information security "
              "management system (ISMS) under ISO/IEC 27001:2022 and the AI management system (AIMS) under "
              "ISO/IEC 42001:2023 — which we run as **one system** under the TWYNTRUST framework."),
        ("h1", "2. Scope"),
        ("p", f"This policy applies to everyone who works for or with {N} — employees, freelance contractors, "
              "and suppliers who handle our information — and to all information, systems and AI systems inside "
              f"the scope defined in {ref('IMS-REG-001')}."),
        ("h1", "3. Our principles"),
        ("h2", "3.1 Information security"),
        ("bullets", [
            "**Confidentiality** — customer scripts, artwork, personal data and our own source code are seen "
            "only by people and systems that need them.",
            "**Integrity** — information, models and generated outputs are accurate and are not changed "
            "without authorisation.",
            "**Availability** — Canvas, Commons and the API are available when customers and artists need them, "
            "and we can recover quickly when they are not.",
        ]),
        ("h2", "3.2 Responsible AI"),
        ("table", ["Principle", "What it means at " + N], [
            ("Respect for creators", "We train or fine-tune only on work we own, have licensed, or have explicit "
             "artist consent for. We honour opt-outs. Artists are paid fairly for commissions."),
            ("Transparency", "AI-generated and AI-assisted outputs are labelled and carry content credentials. "
             "Customers and artists can find out how ArtistMatch ranks people."),
            ("Fairness", "Our AI does not systematically disadvantage artists or depicted groups; we test for it "
             "before release and monitor it after."),
            ("Safety and integrity of content", "We block prohibited content, including sexual content involving "
             "minors and deceptive deepfakes of real people, and we do not help anyone mislead the public."),
            ("Human oversight", "A named person is accountable for every AI system, and people can override, "
             "correct or switch off AI features."),
            ("Privacy", "We use the minimum personal data we need and never use customer scripts or artwork to "
             "train models unless the customer has opted in."),
            ("Security by design", "AI systems get the same security engineering as the rest of our software, "
             "plus protection against AI-specific attacks such as prompt injection and data poisoning."),
            ("Accountability", "We record our decisions about AI, we can explain them, and we learn from mistakes."),
        ], [4.5, 12]),
        ("h1", "4. Commitments"),
        ("p", "Top management commits to:"),
        ("steps", [
            "Meet applicable legal, regulatory and contractual requirements, including those listed in "
            f"{ref('IMS-REG-001')}.",
            "Set and review information-security and AI objectives each year "
            f"({ref('IMS-REG-003')}).",
            "Identify, assess and treat risks to information and from AI systems, and assess the impact of our AI "
            "systems on individuals, groups and society, before release and when they change.",
            "Provide the people, budget, tools and time needed to run the management system.",
            "Make sure everyone understands this policy and their part in it.",
            "Continually improve the suitability, adequacy and effectiveness of the management system.",
        ]),
        ("h1", "5. Responsibilities"),
        ("table", ["Who", "Responsibility"], [
            (who("CEO"), "Owns this policy; chairs the Trust Council; is accountable for the management system."),
            (who("CISO"), "Runs the ISMS; maintains the information-security risk register and Annex A controls."),
            (who("CAIO"), "Runs the AIMS; chairs the AI Release Review; owns AI impact assessments."),
            (who("CREA"), "Represents artists and audiences; signs off content-safety controls."),
            (who("DPO"), "Advises on privacy and legal requirements; handles data-subject requests."),
            ("All managers", "Make sure their teams follow this policy and have time for training."),
            ("Everyone", "Follow this policy and the policies under it; report incidents, weaknesses and AI "
                         "concerns straight away through #trust-report or trust@quillfen.example."),
        ], [5.5, 11]),
        ("p", f"Full roles and the RACI chart are in {ref('IMS-GOV-001')}."),
        ("h1", "6. Supporting policies"),
        ("p", "This policy is supported by the topic-specific policies below. Together they form the policy set "
              "required by ISO/IEC 27001 Annex A 5.1 and ISO/IEC 42001 Annex A.2."),
        ("bullets", [ref(x) for x in ("IMS-POL-002", "IMS-POL-003", "IMS-POL-004", "IMS-POL-005", "IMS-POL-006")]),
        ("h1", "7. Compliance, exceptions and review"),
        ("bullets", [
            "Breaches of this policy are handled through the disciplinary process or contract terms, in "
            "proportion to their seriousness.",
            "Exceptions must be requested in writing, risk-assessed, approved by the Security Lead or the Head "
            "of AI, recorded in the risk register and given an expiry date (maximum 12 months).",
            "The Trust Council reviews this policy at least once a year, and after major changes in law, "
            "technology (for example a new AI model), business or risk.",
        ]),
        ("tip", "Auditors will ask staff 'What does the policy say about you?'. Pick two or three sentences from "
                "sections 3 and 5 and use them in onboarding and in the awareness campaign "
                f"({ref('IMS-REG-004')})."),
        ("h1", "8. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("CEO"), "CEO, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
