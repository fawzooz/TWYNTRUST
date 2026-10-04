from org import AI_SYSTEMS, ORG, TECH, person, ref, title_of, who

N = ORG["name"]
SYS = {s["id"]: s["name"] for s in AI_SYSTEMS}

DOC = {
    "id": "IMS-POL-005",
    "summary": f"The everyday rules for using {N}'s devices, information, messaging and social media — and a "
               "practical section on generative AI: which tools are approved, what must never go into them, how to "
               "label AI-assisted work and how to respect other people's creative rights.",
    "clauses": {"27001": "Annex A 5.10, 5.14, 6.2, 6.4, 6.7, 7.7, 8.1",
                "42001": "Annex A.9.2, A.9.3, A.9.4; supports A.2.2, A.8.2"},
    "howto": [
        "Keep this policy readable in 15 minutes — it is the one document every person signs. Move long technical "
        "detail to the topic policies.",
        "Update the approved AI tools list (section 9.2) whenever the Head of AI approves or withdraws a tool; it "
        "changes more often than the rest of the policy, so give it a version date.",
    ],
    "body": [
        ("h1", "1. Purpose"),
        ("p", f"This policy tells everyone at {N} what is expected when they use company devices, accounts and "
              "information, and when they use AI tools at work. Most of it is common sense written down. The "
              "generative-AI section is new for most people: AI tools are part of our product and of our daily work, "
              "and they create new ways to leak secrets, infringe someone's copyright or mislead an audience."),
        ("h1", "2. Scope"),
        ("p", "Everyone who works for or with us — employees, contractors, interns and supplier staff using our "
              "systems — on company devices, on personal devices used for work (mobile phones only, see 4.2), and "
              "anywhere they work: the Dubai office, home, a café or while travelling."),
        ("std", [
            "ISO/IEC 27001 Annex A asks for rules for the acceptable use of information and assets (5.10), "
            "secure information transfer (5.14), protection of endpoints (8.1), remote working (6.7) and a clear "
            "desk and clear screen (7.7). People must sign terms of employment that cover their security duties "
            "(6.2), and there is a disciplinary process for breaches (6.4).",
            "ISO/IEC 42001 asks you to define processes for the responsible use of AI systems, set objectives for "
            "that use, and make sure AI is used as intended (A.9.2–A.9.4). Using third-party AI tools at work is "
            "'use of AI' and is covered.",
        ]),
        ("h1", "3. Responsibilities"),
        ("table", ["Who", "Responsibility"], [
            (who("CISO"), "Owns this policy; manages device controls and data-loss alerts; investigates misuse."),
            (who("CAIO"), "Approves or withdraws AI tools; maintains the approved AI tools list."),
            (who("DPO"), "Advises on personal data and IP questions; reviews AI tool terms."),
            (who("HOP"), "Collects signed acknowledgements at onboarding and yearly."),
            ("Line managers", "Lead by example; answer questions; report concerns."),
            ("Everyone", "Read, sign and follow this policy; ask when unsure; report incidents and misuse."),
        ], [5.5, 11]),
        ("h1", "4. Devices"),
        ("h2", "4.1 Company laptops"),
        ("bullets", [
            f"Work is done on company-managed laptops ({TECH['devices']}). Do not disable or work around these "
            "controls.",
            "Install software only from the company software catalogue or with IT approval. Browser extensions that "
            "read page content (including AI extensions) need approval.",
            "Lock the screen whenever you step away (Windows+L / Ctrl+Cmd+Q); screens lock automatically after 5 "
            "minutes.",
            "Family members and friends may not use your work laptop.",
            "Report loss or theft within 1 hour via #trust-report so the device can be wiped.",
        ]),
        ("h2", "4.2 Personal phones"),
        ("p", "You may use your own phone for email, chat and the SSO authenticator if it has a screen lock, current "
              "updates and the company's device-management profile for work apps. Restricted data must never be "
              "downloaded to a personal device."),
        ("h1", "5. Handling information by classification"),
        ("table", ["Class", "You may", "You must not"], [
            ("Public", "Share freely once approved for publication.", "Publish drafts before approval."),
            ("Internal", "Share with staff and contractors in company tools.", "Send to personal email or "
                                                                              "unapproved tools."),
            ("Confidential", "Share with people who need it for their work, inside company tools; with external "
                             "parties only under NDA via approved sharing.", "Paste into unapproved AI tools; "
                                                                             "store on unmanaged devices."),
            ("Restricted", "Access only if named on the access list, in the approved system.", "Download, export, "
                                                                                             "screenshot or put into "
                                                                                             "any AI tool not "
                                                                                             "approved for "
                                                                                             "Restricted data."),
        ], [2.5, 7, 7]),
        ("p", f"Classification is explained in {ref('IMS-PRO-004')}. Customer scripts and artist portfolios are always "
              "Restricted."),
        ("h1", "6. Remote working and travel"),
        ("bullets", [
            "Use a private space for calls about customers, artists or incidents. Use headphones in public.",
            "Use a privacy screen filter in cafés, airports and co-working spaces.",
            "Public Wi-Fi is acceptable because all our tools use encryption; never turn off the laptop firewall.",
            "Do not leave devices unattended in cars or public places.",
            "Tell the Security Lead before travelling with a laptop to a country not on the approved travel list.",
        ]),
        ("h1", "7. Clear desk and clear screen"),
        ("bullets", [
            "In the Dubai office, no Confidential or Restricted printouts are left on desks; shred them after use.",
            "Hide notifications and close customer files before sharing your screen in meetings or demos.",
            "Whiteboards with customer or product details are wiped after meetings.",
        ]),
        ("h1", "8. Email, messaging and social media"),
        ("bullets", [
            "Use company email and the company chat workspace for work. Do not move work conversations to personal "
            "messaging apps.",
            "Share files by link with access controls, not as attachments, when they are Confidential or Restricted.",
            "Be alert to phishing — especially fake script shares, payout notices and model-provider billing emails. "
            "Report suspicious messages with the 'Report phish' button.",
            "On social media, you may say you work here and share public material. Do not post customer names, "
            "unreleased projects, screenshots of internal tools, or AI outputs from customer work.",
            f"Only authorised spokespeople talk to the press about security or AI ({ref('IMS-PRO-003')}).",
        ]),
        ("pagebreak",),
        ("h1", "9. Generative AI at work"),
        ("h2", "9.1 Why this section matters"),
        ("p", "AI tools are useful and we want people to use them. But a prompt is a disclosure: anything you type or "
              "upload may be stored, reviewed or used by the tool's provider unless we have a contract that says "
              "otherwise. Pasting secrets or source code into unapproved tools is one of our top risks (RSK-IS-003), "
              "and our customers and artists trust us with work that is not ours to share."),
        ("h2", "9.2 Approved AI tools"),
        ("p", "Only tools on this list may be used with company information. The list is version-dated and kept on "
              "the wiki; this table is the version at the policy's effective date."),
        ("table", ["Tool", "Approved for", "Data allowed", "Conditions"], [
            (f"{SYS['AI-SYS-005']} ({'AI-SYS-005'})", "Engineering staff — code completion and review help in the "
                                                     "IDE", "Internal and Confidential source code",
             "Business plan, no training on our code; secret scanning on all commits; suggestions reviewed like any "
             "other code."),
            ("Enterprise AI assistant (company workspace)", "All staff — drafting, summarising, analysis",
             "Up to Confidential", "Signed in through SSO only; zero data retention for training; no Restricted "
                                   "data."),
            (f"{SYS['AI-SYS-002']} and {SYS['AI-SYS-001']} (internal workspace)", "Creative and product teams — demos, "
                                                                                "testing, internal projects",
             "Up to Restricted for customer projects inside the customer's own workspace",
             "Same safeguards as for customers; outputs labelled."),
            ("Meeting transcription in the company video-call suite", "Internal meetings", "Internal",
             "Off by default for customer or artist calls unless all participants agree at the start."),
            ("[[tool name]]", "[[who / what for]]", "[[highest class]]", "[[conditions]]"),
        ], [4, 4.5, 3.5, 4.5]),
        ("p", "To propose a new tool, open a request in the ticketing system. The Head of AI and the Security Lead "
              "review the provider's data use, retention, security and IP terms (with the Privacy and Legal Lead) "
              f"under {ref('IMS-POL-006')}, normally within 10 working days. Free consumer versions of AI tools are "
              "not approved for work information of any class above Public."),
        ("h2", "9.3 What never goes into an AI tool"),
        ("p", "Unless the tool is on the approved list **and** approved for that class of data, never enter, paste or "
              "upload:"),
        ("bullets", [
            "**Customer scripts, prompts, storyboards or project files** — they are unreleased creative work.",
            "**Artist portfolios or commissioned artwork** — including to 'restyle', 'upscale' or 'analyse' them.",
            "**Secrets** — passwords, API keys (including model-provider keys), tokens, private keys, connection "
            "strings. These may not go into any AI tool, approved or not.",
            "**Personal data** — names with contact details, payout or identity documents, HR data, support tickets "
            "with customer details.",
            "**Security details** — vulnerability reports, incident details, network or cloud configuration.",
            "**Non-public company information** — financials, investor material, contracts, unannounced products.",
        ]),
        ("tip", "Give people a simple test they can remember: 'Would I paste this into a public forum? If not, is this "
                "tool on the approved list for this kind of data?' Put it on the onboarding slide and the awareness "
                "campaign for December."),
        ("h2", "9.4 Using AI outputs responsibly"),
        ("bullets", [
            "**You are responsible for the output.** Check facts, code and claims before you rely on or share them. "
            "AI tools can invent references, scenes or functions that do not exist.",
            "**Code:** review AI-suggested code as carefully as a colleague's, run the normal tests and scans, and "
            "check that suggested packages actually exist (watch for invented package names).",
            "**Labelling:** any image, storyboard or text that is mostly AI-generated and shared outside the company "
            "must be labelled 'AI-assisted' and keep its content credentials (C2PA). Never remove or hide labels or "
            "metadata from StoryFrame outputs. Internal documents drafted with AI should note it in the revision "
            "history.",
            "**People's likeness:** do not generate images of real, identifiable people without their written "
            "permission, and never for parody, advertising or anything that could deceive.",
            "**Decisions about people:** do not use AI tools to decide about hiring, performance, artist ranking or "
            "payouts outside the approved, assessed systems.",
        ]),
        ("h2", "9.5 Intellectual property and copyright"),
        ("bullets", [
            "Do not prompt AI tools to imitate a named living artist's style for customer or marketing work, and do "
            "not upload another person's work as a style reference without a licence.",
            "Check generated images for recognisable third-party characters, logos or trademarks before use.",
            "Material generated with AI may not be protected by copyright in some countries. Tell the Privacy and "
            f"Legal Lead before using AI-generated material as a company asset you want to own (logo, mascot, key art). "
            f"External counsel ({title_of('LEGAL')}) advises on difficult cases.",
            "Respect artists' opt-outs: if an artist has opted out of AI training, their work must not be used in "
            f"any AI workflow, including experiments ({ref('IMS-POL-003')}).",
        ]),
        ("example", "An afternoon with a deadline", [
            "A product designer needs to summarise feedback from 40 customer interviews before a board meeting. The "
            "notes include customer names and quotes about unreleased game projects (Restricted).",
            "Wrong: pasting the notes into a free chat assistant on a personal account.",
            "Right: removing names and project titles, then using the enterprise AI assistant through SSO (approved up "
            "to Confidential), and checking the summary against the notes before presenting it. The slide notes "
            "'Summary drafted with AI assistance'.",
        ]),
        ("h2", "9.6 Reporting misuse and mistakes"),
        ("p", "If you put something into the wrong tool, report it straight away through #trust-report — within 1 "
              "hour if it was a secret, so it can be rotated. Honest, quick reports are treated as learning, not "
              "punishment. Also report AI outputs that look harmful, biased, infringing or deceptive, and any "
              f"colleague's misuse you notice ({ref('IMS-PRO-005')})."),
        ("h1", "10. Monitoring"),
        ("p", "To protect customers, artists and staff, we monitor company systems: device security status, sign-ins, "
              "data-loss alerts for secrets and Restricted data leaving approved tools, and use of AI tool admin logs. "
              "Monitoring is proportionate, done by the Security team, and complies with privacy law; we do not read "
              "personal messages without a legitimate investigation approved by the Privacy and Legal Lead."),
        ("h1", "11. Breaches"),
        ("p", "Breaches of this policy are handled fairly and in proportion: coaching for first, honest mistakes; "
              "formal disciplinary or contract measures for deliberate, repeated or serious breaches (for example "
              "uploading customer scripts to a public AI tool or removing AI labels from published work)."),
        ("h1", "12. Related documents"),
        ("bullets", [ref(x) for x in ("IMS-POL-001", "IMS-POL-002", "IMS-POL-003", "IMS-POL-004", "IMS-POL-006",
                                      "IMS-PRO-003", "IMS-PRO-004", "IMS-PRO-005")]),
        ("h1", "13. Acknowledgement form"),
        ("p", "Signed at onboarding (before access to Confidential or Restricted data) and every year after the "
              "refresher training. Stored in the HR system."),
        ("table", ["Statement", "Agreed"], [
            ("I have read and understood the Acceptable Use Policy (including Generative AI), version "
             "[[version]].", "[[Yes / No]]"),
            ("I will use only approved AI tools for work, and never put customer scripts, artist portfolios, secrets "
             "or personal data into tools not approved for them.", "[[Yes / No]]"),
            ("I will label AI-assisted work shared outside the company and will not remove content credentials.",
             "[[Yes / No]]"),
            ("I will report incidents, lost devices and AI misuse straight away via #trust-report.", "[[Yes / No]]"),
            ("I understand that company systems are monitored as described in section 10.", "[[Yes / No]]"),
        ], [13, 3.5]),
        ("table", ["Name", "Role / team", "Employee or contractor", "Signature", "Date"], [
            ("[Contractor A]", "Front-end developer", "Contractor", "(signed electronically)", "2026-09-24"),
            ("[[name]]", "[[role]]", "[[type]]", "[[signature]]", "[[date]]"),
        ], [3.5, 3.5, 3.2, 3.3, 3]),
        ("h1", "14. Approval"),
        ("table", ["Name", "Role", "Signature", "Date"], [
            (person("CISO"), title_of("CISO") + ", policy owner", "[[signature]]", "[[date]]"),
            (person("CEO"), "CEO, for the Trust Council", "[[signature]]", "[[date]]"),
        ], [4.5, 5.5, 3.5, 3]),
    ],
}
