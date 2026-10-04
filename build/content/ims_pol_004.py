from org import AI_SYSTEMS, ORG, TECH, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}

DOC = {
    "id": "IMS-POL-004",
    "summary": f"Who may access what at {N}, and how access is requested, granted, reviewed and removed — for "
               "staff, contractors, service accounts and AI model providers, and for the most sensitive things we "
               "hold: customer scripts, artist portfolios, training data and model weights.",
    "clauses": {"27001": "Annex A 5.3, 5.15, 5.16, 5.17, 5.18, 8.2, 8.3, 8.4, 8.5, 8.15",
                "42001": "8.1; Annex A.4.3, A.4.4, A.6.2.8, A.7.2"},
    "howto": [
        "Write down your real joiner/mover/leaver steps before editing this policy. The policy should describe "
        "what your identity provider and HR system actually do.",
        "Auditors almost always sample leavers: pick three people who left in the last 6 months and check that "
        "every account was closed on time. Do that check yourself first.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"Most breaches start with a stolen or over-powerful account. This policy keeps access to {N}'s "
              "information, systems and AI assets limited to the people and services that need it, for as long as "
              "they need it, with strong proof of identity and a record of what they did."),
        ("p", "It is one policy for both standards: the same identity system and the same reviews protect our "
              "security assets (ISO/IEC 27001) and our AI data, models and tooling (ISO/IEC 42001)."),
        ("h1", "2. Scope"),
        ("p", "All employees, contractors, interns, suppliers and automated identities (service accounts, CI/CD "
              "pipelines, API keys) that access company systems; all systems in scope of the management system — "
              "cloud accounts, GitHub, SaaS tools, the Canvas and Commons admin consoles, the model registry, datasets "
              "and logs. Customer and artist user accounts in our products follow the product security requirements in "
              f"{ref('IMS-POL-002')}; this policy covers our staff's access to their data."),
        ("std", [
            "ISO/IEC 27001 Annex A asks for rules on access control based on business and security needs (5.15), "
            "managing the full life of identities (5.16), handling authentication information safely (5.17) and "
            "granting, reviewing and removing access rights (5.18).",
            "Technical controls cover privileged access (8.2), restricting access to information (8.3), access to "
            "source code (8.4) and secure authentication (8.5); segregation of duties (5.3) and logging (8.15) "
            "support them.",
            "ISO/IEC 42001 expects you to know and manage the data, tooling and computing resources of your AI "
            "systems (A.4.3–A.4.5), to control data used for AI (A.7) and to keep event logs (A.6.2.8). Access "
            "control is how you protect those resources in practice.",
        ]),
        ("h1", "3. Roles"),
        ("table", ["Who", "Responsibility"], [
            (who("CISO"), "Owns this policy and the identity provider configuration; approves privileged access; "
                          "runs the quarterly access review."),
            (who("HOP"), "Starts every joiner, mover and leaver workflow from the HR system — the single trigger "
                         "for access changes, for employees and contractors alike."),
            ("System owners (from the asset inventory)", "Decide who needs access to their system; approve requests; "
                                                         "confirm access in reviews."),
            (who("HOD"), "Approves access to training datasets, the consent ledger and model weights."),
            (who("SRE"), "Manages cloud roles, service accounts, secrets and break-glass accounts."),
            ("Line managers", "Request the right access for their people; tell People Ops about role changes the "
                              "same day."),
            ("Everyone", "Protect their credentials; never share accounts; report lost devices or suspicious "
                         "prompts immediately."),
        ], [5.5, 11]),
        ("h1", "4. Principles"),
        ("bullets", [
            "**Least privilege.** Access is the minimum needed for the job. Default is no access.",
            "**Need-to-know.** Restricted information (customer scripts, artist portfolios and consent records, "
            "datasets, model weights, secrets) is available only to named people.",
            "**One identity per person.** Every human uses their own account through single sign-on (SSO). Shared "
            "logins are forbidden.",
            "**Role-based access.** Access is granted through groups mapped to roles, not to individuals one by one.",
            "**Segregation of duties.** Nobody approves their own access, merges their own code to production without "
            "review, or approves their own AI release.",
            "**Just-in-time for power.** Admin and production access is time-limited and requested when needed.",
        ]),
        ("h1", "5. Identity lifecycle: joiner, mover, leaver"),
        ("table", ["Event", "What happens", "Deadline"], [
            ("Joiner", "People Ops creates the person in the HR system; the identity provider creates the account "
                       "and adds role groups; laptop enrolled in device management; security key or passkey issued; "
                       "Security and Responsible AI Essentials assigned. Access to Restricted data only after "
                       "training and AUP acknowledgement.", "Account ready on day 1"),
            ("Mover", "Manager tells People Ops; old role groups removed and new ones added in the same change; "
                      "privileged access re-approved.", "Within 2 working days of the move"),
            ("Leaver (normal)", "SSO account disabled at the end of the last day; sessions and tokens revoked; "
                                "personal API keys deleted; GitHub org membership removed; laptop returned and "
                                "wiped; shared secrets the person knew are rotated.", "Same day"),
            ("Leaver (urgent / dismissal)", "Account disabled before or during the conversation.", "Immediately"),
            ("Contractor end of engagement", "As leaver. Contractor accounts also expire automatically on the "
                                             "contract end date set at creation (maximum 6 months, renewable).",
             "Contract end date"),
        ], [3.5, 10, 3]),
        ("tip", "Make the HR system the only way to start a joiner or leaver. Hiring managers who set up contractors "
                "themselves is exactly how NC-2026-004 happened — training was missed because onboarding bypassed "
                "People Ops. The same gap would leave accounts open after a contractor leaves."),
        ("h1", "6. Authentication"),
        ("bullets", [
            f"All staff and contractors use SSO with **phishing-resistant MFA** — passkeys or hardware security keys "
            f"({TECH['identity']}). SMS and one-time codes by email are not allowed for company accounts.",
            "Every SaaS tool that supports SSO must use it. Tools that do not support SSO need the Security Lead's "
            "approval, a unique strong password in the company password manager, and MFA where available.",
            "Passwords, where still used, are at least 14 characters, generated by the password manager, never "
            "reused and never shared in chat or tickets.",
            "Sessions on admin consoles expire after 12 hours; access from unmanaged devices is blocked for "
            "Confidential and Restricted systems.",
            "Lost or stolen security keys or laptops are reported within 1 hour through #trust-report.",
        ]),
        ("h1", "7. Privileged access"),
        ("bullets", [
            "Privileged roles (cloud administrator, identity-provider admin, GitHub org owner, database admin, "
            "model-registry admin) are held by named people only and listed in the access register.",
            "Day-to-day work uses normal accounts. Production admin rights are requested just-in-time for a maximum "
            "of 8 hours, with a ticket reference, and every session is logged.",
            "At most three GitHub org owners and two identity-provider super-admins at any time.",
            "Two break-glass accounts exist for emergencies, with credentials in a sealed vault entry; any use alerts "
            "the Security Lead and the CTO and is reviewed within 2 working days.",
        ]),
        ("h1", "8. Service accounts, API keys and model providers"),
        ("p", "Automated identities are as dangerous as people and easier to forget. The rules:"),
        ("bullets", [
            "Every service account and API key has a named human owner, a purpose and an entry in the asset "
            "inventory (AST-008).",
            "Keys for foundation-model and image-model providers are stored only in the secrets manager, injected at "
            "runtime, scoped per environment (development keys cannot reach production quotas), and never placed in "
            "code, notebooks, prompts or chat.",
            "Provider consoles are accessed through SSO where available, with spending limits and alerts set.",
            "Keys are rotated at least every 90 days, immediately when someone with access leaves, and immediately if "
            "secret scanning finds one exposed.",
            "CI/CD pipelines use short-lived federated credentials, not long-lived keys.",
            f"Unused service accounts (no activity for 60 days) are disabled. {SYS['AI-SYS-005']} and other vendor "
            "AI tools are licensed per named user through SSO.",
        ]),
        ("h1", "9. Access to customer data and AI assets"),
        ("table", ["Asset", "Who may access", "Conditions"], [
            ("Customer scripts, prompts and project files (AST-004)", "Support and engineering on-call, named",
             "Only with a support ticket and the customer's permission, or during an incident; access is logged and "
             "reviewed monthly."),
            ("Artist portfolios and consent records (AST-005)", "Marketplace operations; Data and ML team (read)",
             "Consent ledger is append-only; edits only through the consent workflow."),
            ("StoryFrame fine-tuning datasets and model weights (AST-006)", "Data and ML team (named)",
             "Approved by the Data and ML Lead; downloads to laptops forbidden; training runs only in the ML "
             "environment; weight exports need Head of AI approval."),
            ("ArtistMatch model, features and evaluation sets (AST-007)", "Data and ML team", "Ranking overrides "
             "require a second person and are logged."),
            ("Source code (AST-009)", "Engineering", "Branch protection; mandatory review; no direct pushes to main."),
            ("Logs and AI output logs (AST-012)", "SRE, Security, on-call", "Read-only; prompt content masked by "
             "default; unmasking is logged."),
        ], [5, 4.5, 7]),
        ("example", "Who can touch the StoryFrame weights?", [
            f"The model registry has a 'storyframe-weights' project classified Restricted. Four people are in the "
            f"'ml-restricted' group, approved by {who('HOD')}. The group is reviewed every quarter.",
            "In the Q3 review the Data and ML Lead removed a former intern who had moved to the design team — the "
            "mover workflow had removed the SSO group but a direct registry permission had been added by hand. "
            "The fix: direct grants are now blocked, and only group-based access is allowed. This links to "
            "RSK-AI-001 (consent) and RSK-IS-001 (customer data exposure) because the same pattern protects both.",
        ]),
        ("h1", "10. Contractors and suppliers"),
        ("bullets", [
            "Contractors get accounts through the same HR-driven workflow, with an automatic expiry date.",
            "Contractors receive only Internal access by default. Confidential or Restricted access needs a signed "
            f"NDA and approval by the system owner; supplier staff access follows {ref('IMS-POL-006')}.",
            "Vendor support access to our systems is time-limited, through our SSO or a supervised session, never "
            "through shared credentials.",
        ]),
        ("h1", "11. Access reviews"),
        ("steps", [
            "Every quarter (January, April, July, October) the Security Lead exports user and group lists from the "
            "identity provider, AWS, GitHub, the model registry, the consent ledger and the top SaaS tools.",
            "System owners confirm each user is still needed, at the right level, within 10 working days.",
            "Removals are made within 5 working days of the review; the export, decisions and changes are saved as "
            "the review record.",
            "Privileged accounts, service accounts and API keys are reviewed in the same cycle.",
            "Results (accounts removed, overdue reviews) go to the Trust Council.",
        ]),
        ("h1", "12. Logging and monitoring"),
        ("p", "Sign-ins, failed logins, privilege elevations, admin actions, access to Restricted stores and changes to "
              "access rights are logged centrally and kept as set out in "
              f"{ref('IMS-PRO-004')}. Alerts go to the Security Lead for: sign-in from a new country, MFA reset, "
              "break-glass use, bulk downloads from Restricted stores, and API-key use from an unknown network."),
        ("h1", "13. Records"),
        ("bullets", [
            "Access requests and approvals (tickets).",
            "Joiner/mover/leaver checklists from the HR system.",
            "Quarterly access review exports and decisions.",
            "Privileged access and break-glass logs.",
            "Service account and API-key register (in the asset inventory).",
        ]),
        ("h1", "14. Compliance and exceptions"),
        ("p", "Exceptions follow the process in " + ref("IMS-POL-001") + ": written request, risk assessment, "
              "approval by the Security Lead (and the Head of AI for AI assets), an entry in the risk register and an "
              "expiry date. Breaches are handled through the incident process and, where needed, disciplinary or "
              "contract measures."),
        ("h1", "15. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-POL-003", "IMS-POL-005", "IMS-POL-006", "IMS-REG-005",
                                      "IMS-PRO-004", "IMS-PRO-005", "IMS-REG-002")]),
        ("h1", "16. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("CISO"), title_of("CISO") + ", policy owner", "[[signature]]", "[[date]]"),
            (person("CEO"), "CEO, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
