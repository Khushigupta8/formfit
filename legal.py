"""
Trust pages. AdSense reviewers look for these, and for a health site the
medical disclaimer matters as much as the privacy policy.

Body format is the same block format the guides use. "{email}" anywhere in
the text is replaced with CONTACT_EMAIL. Keep CONTACT_EMAIL a real inbox you
read: reviewers do check that it works.
"""

CONTACT_EMAIL = "devkhushii08@gmail.com"
UPDATED = "12 October 2026"

LEGAL = [
    {
        "slug": "about",
        "title": "About FormFit",
        "h1": "About FormFit",
        "desc": ("FormFit builds free, private fitness calculators and plain-English "
                 "training guides for people who lift, run and train."),
        "body": [
            ("What FormFit is", [
                "FormFit is a free toolkit for people who train. It started as a "
                "set of calculators we kept rebuilding in spreadsheets: how much "
                "to eat on a cut, what a set of five says about a one rep max, "
                "which plates go on the bar. Now they live in one place, work on "
                "any phone, and come with the explanation behind every number.",
                "Alongside the calculators you will find workout plans with full "
                "weekly schedules, an exercise library with step-by-step "
                "technique, and guides on nutrition, fat loss, muscle gain and "
                "recovery.",
            ]),
            ("How we write and check content", [
                "Every calculator uses a published, peer-reviewed formula, and "
                "each page names the formula and the paper it comes from, so you "
                "can check our working. Where researchers disagree we say so "
                "rather than pick a side and present it as settled.",
                "Guides are written by the FormFit editorial team from the "
                "research literature and position stands from bodies such as the "
                "International Society of Sports Nutrition, the American College "
                "of Sports Medicine and the World Health Organization. We update "
                "pages when better evidence comes along and correct mistakes as "
                "soon as they are reported.",
                {"list": [
                    "No calculator result is a diagnosis. They are estimates for "
                    "healthy adults and say so on every page.",
                    "We do not sell supplements, coaching or meal plans, so we "
                    "have nothing to push you towards.",
                    "Advertising is clearly labelled and never placed where it "
                    "could be mistaken for a button or a result.",
                ]},
            ]),
            ("Your data stays with you", [
                "Every calculator runs inside your browser. The numbers you type "
                "are not sent to us or stored on any server. The only thing the "
                "site remembers is whether you prefer metric or imperial units, "
                "and that lives in your own browser.",
            ]),
            ("Get in touch", [
                "Spotted an error, or want a calculator we don't have yet? Write "
                "to <a href=\"mailto:{email}\">{email}</a>. We read everything.",
            ]),
        ],
    },
    {
        "slug": "contact",
        "title": "Contact FormFit",
        "h1": "Contact us",
        "desc": "How to reach the FormFit team with corrections, suggestions or questions.",
        "body": [
            ("Email", [
                "The fastest way to reach us is email: "
                "<a href=\"mailto:{email}\">{email}</a>. We usually reply within "
                "two working days.",
            ]),
            ("What to write to us about", [
                {"list": [
                    "<strong>Corrections.</strong> If a formula, number or claim on "
                    "the site looks wrong, tell us the page and what you think it "
                    "should say. Corrections get priority.",
                    "<strong>Suggestions.</strong> Calculators, exercises or guides "
                    "you would like to see.",
                    "<strong>Privacy requests.</strong> Questions about the data "
                    "described in our <a href=\"/privacy\">privacy policy</a>.",
                    "<strong>Advertising and partnerships.</strong> Put "
                    "\"Partnership\" in the subject line.",
                ]},
            ]),
            ("What we can't help with", [
                "We can't give personal medical, dietary or injury advice by "
                "email. If you have a health condition, pain, or are pregnant, "
                "please speak to a doctor or a registered dietitian. Our "
                "<a href=\"/disclaimer\">medical disclaimer</a> explains why.",
            ]),
        ],
    },
    {
        "slug": "privacy",
        "title": "Privacy Policy",
        "h1": "Privacy policy",
        "desc": ("How FormFit handles your data, which cookies are used for "
                 "advertising, and the choices you have."),
        "body": [
            ("The short version", [
                "Calculators run in your browser and the numbers you enter are "
                "never sent to us. We do not have accounts, logins or a "
                "newsletter. The site is paid for by advertising from Google "
                "AdSense, which uses cookies as described below.",
            ]),
            ("What you type into calculators", [
                "Your height, weight, age, measurements and lifts are processed "
                "by JavaScript on your own device. They are not transmitted over "
                "the network, logged, or stored by us.",
                "We save one preference in your browser's local storage: whether "
                "you use metric or imperial units. It never leaves your device "
                "and you can clear it at any time by clearing site data in your "
                "browser.",
            ]),
            ("Server logs", [
                "Our hosting provider records standard request logs when a page "
                "is loaded: IP address, page requested, time, referring page and "
                "browser user agent. These are used to keep the site running and "
                "secure, and are deleted on the host's normal schedule.",
            ]),
            ("Advertising and cookies", [
                "This site shows advertising supplied by Google AdSense.",
                {"list": [
                    "Third-party vendors, including Google, use cookies to serve "
                    "ads based on a user's prior visits to this website or other "
                    "websites.",
                    "Google's use of advertising cookies enables it and its "
                    "partners to serve ads to you based on your visit to this "
                    "site and/or other sites on the internet.",
                    "You may opt out of personalised advertising by visiting "
                    "<a href=\"https://www.google.com/settings/ads\" rel=\"nofollow noopener\">"
                    "Google Ads Settings</a>. You can also opt out of some "
                    "third-party vendors' use of cookies for personalised "
                    "advertising at <a href=\"https://www.aboutads.info/choices/\" "
                    "rel=\"nofollow noopener\">aboutads.info</a>.",
                    "Other third-party vendors or ad networks may also serve ads "
                    "on this site. A list of the vendors Google works with is "
                    "available in your ad settings and in Google's published "
                    "list of ad technology providers.",
                ]},
                "Learn more about how Google uses information from sites that "
                "use its services at <a href=\"https://policies.google.com/technologies/partner-sites\" "
                "rel=\"nofollow noopener\">policies.google.com/technologies/partner-sites</a>.",
            ]),
            ("Consent in the UK, EEA and Switzerland", [
                "Visitors from the European Economic Area, the United Kingdom and "
                "Switzerland are shown a consent message, provided through "
                "Google's certified consent management platform, before any "
                "personalised advertising cookies are set. You can change your "
                "choice at any time from the privacy link that message leaves on "
                "the page. If you decline, you may still see non-personalised "
                "ads, which use cookies only for frequency capping, fraud "
                "prevention and measurement.",
            ]),
            ("US state privacy rights", [
                "If you live in a US state with a consumer privacy law, such as "
                "California, you can opt out of the sale or sharing of personal "
                "information for targeted advertising using the options Google "
                "displays on this site, or by using Google Ads Settings above. "
                "We do not sell personal information in any other way.",
            ]),
            ("Children", [
                "FormFit is written for adults. We do not knowingly collect "
                "information from children under 13 (or under 16 in the EEA and "
                "UK). Calculators such as BMI are not designed for under-18s, as "
                "each page explains.",
            ]),
            ("Links to other sites", [
                "Some pages link to research papers and other websites. We are "
                "not responsible for their privacy practices.",
            ]),
            ("Changes and contact", [
                "If this policy changes, the new version will be posted here with "
                "a new date. Questions or requests: "
                "<a href=\"mailto:{email}\">{email}</a>.",
            ]),
        ],
    },
    {
        "slug": "terms",
        "title": "Terms of Use",
        "h1": "Terms of use",
        "desc": "The terms that apply when you use FormFit's calculators, plans and guides.",
        "body": [
            ("Using the site", [
                "FormFit is free to use for personal, non-commercial purposes. By "
                "using it you agree to these terms. If you don't agree, please "
                "don't use the site.",
            ]),
            ("Not medical advice", [
                "Everything on FormFit is general information for healthy adults. "
                "It is not medical, nutritional or physiotherapy advice and does "
                "not replace a professional who knows your history. Read the full "
                "<a href=\"/disclaimer\">medical disclaimer</a>.",
            ]),
            ("Accuracy", [
                "Calculators use published formulas that produce estimates. Real "
                "people vary, sometimes by a lot. We work to keep pages accurate "
                "but make no guarantee that any result or statement is correct, "
                "complete or current.",
            ]),
            ("Exercise at your own risk", [
                "Physical training carries a risk of injury. You are responsible "
                "for choosing loads you can handle safely, using spotters and "
                "safety equipment, and stopping if something hurts. FormFit is "
                "not liable for any injury, loss or damage arising from use of "
                "the site, to the extent the law allows.",
            ]),
            ("Content and copyright", [
                "The text, calculators and design of FormFit are owned by us. "
                "Photographs are used under the Unsplash licence. You may link to "
                "any page and quote short passages with a link back; please don't "
                "republish whole pages.",
            ]),
            ("Advertising and third-party links", [
                "The site displays third-party advertising. We don't endorse "
                "advertised products, and any dealings you have with advertisers "
                "are between you and them.",
            ]),
            ("Changes", [
                "We may update these terms. The date at the top of the page shows "
                "the latest version. Questions: <a href=\"mailto:{email}\">{email}</a>.",
            ]),
        ],
    },
    {
        "slug": "disclaimer",
        "title": "Medical Disclaimer",
        "h1": "Medical disclaimer",
        "desc": ("FormFit's calculators and guides are general information, not "
                 "medical advice. Read this before acting on any result."),
        "body": [
            ("Information, not advice", [
                "The calculators, workout plans and articles on FormFit are for "
                "general educational purposes. They are not a substitute for "
                "advice from a doctor, registered dietitian, physiotherapist or "
                "other qualified professional who can assess you in person.",
            ]),
            ("Results are estimates", [
                "Every calculator is built on a population-level formula. It "
                "describes averages, and you are not an average. A BMI, body fat "
                "or calorie figure can be several percent off for an individual, "
                "and more for athletes, older adults, and people with certain "
                "medical conditions.",
            ]),
            ("Talk to a professional first if", [
                {"list": [
                    "you are pregnant or breastfeeding",
                    "you are under 18",
                    "you have heart, kidney, liver or metabolic disease, diabetes "
                    "or high blood pressure, or take medication for any of them",
                    "you have, or have had, an eating disorder",
                    "you are returning from injury or surgery, or feel pain, "
                    "dizziness or chest discomfort when exercising",
                ]},
            ]),
            ("Stop and seek help", [
                "Stop exercising and get medical help immediately if you have "
                "chest pain, severe breathlessness, fainting, or pain that is "
                "sharp or getting worse.",
            ]),
            ("No professional relationship", [
                "Using FormFit or writing to us does not create a doctor-patient "
                "or coach-client relationship. Questions: "
                "<a href=\"mailto:{email}\">{email}</a>.",
            ]),
        ],
    },
]

BY_SLUG = {p["slug"]: p for p in LEGAL}
