"""
Trust pages. AdSense reviewers look for these, and for a health site the
medical disclaimer matters as much as the privacy policy.

Body format is the same block format the guides use. "{email}" anywhere in
the text is replaced with CONTACT_EMAIL. Keep CONTACT_EMAIL a real inbox you
read: reviewers do check that it works.
"""

CONTACT_EMAIL = "devkhushii08@gmail.com"
UPDATED = "17 October 2026"

LEGAL = [
    {
        "slug": "about",
        "title": "About FormFit",
        "h1": "About FormFit",
        "desc": ("Who runs FormFit, why it exists, how the calculators and guides "
                 "are made and checked, and how to report a mistake."),
        "body": [
            ("What FormFit is", [
                "FormFit is a free set of fitness calculators, workout plans, "
                "exercise guides and articles for people who train. It is an "
                "independent site, run from India, with no gym, supplement brand "
                "or coaching business behind it.",
                "Everything here is free to use without an account. The site is "
                "paid for by advertising, which is labelled and kept away from "
                "the calculators themselves.",
            ]),
            ("Who runs FormFit", [
                "FormFit is built and run by <strong>Khushi Gupta</strong>. I "
                "train in the gym myself, and I edit everything published here: "
                "the calculators, the workout plans, the exercise pages and the "
                "guides.",
                "The aim is simple. When you put your numbers into a fitness "
                "calculator, you should get the formula behind the answer, an "
                "honest note on how far to trust it, and a clear idea of what to "
                "do next, without anyone trying to sell you something.",
                {"photos": [
                    ("/static/img/team/khushi-2.webp", "Khushi Gupta in the gym, mirror photo beside a plate-loaded machine"),
                    ("/static/img/team/khushi-3.webp", "Khushi Gupta sitting on a plate-loaded chest press machine"),
                    ("/static/img/team/khushi-1.webp", "Khushi Gupta in the gym, mirror photo beside a loaded barbell"),
                ]},
                "If you have a question, a correction or an idea for the site, "
                "you can reach me at <a href=\"mailto:{email}\">{email}</a>.",
            ]),
            ("How the site started", [
                "FormFit began in September 2026 as a small tool for resizing photos and "
                "signatures for Indian exam application forms. It was useful, but "
                "narrow, and most visitors used it once and never came back.",
                "A month later, in October 2026, we rebuilt the site around something people use "
                "every week: training and nutrition. The questions people ask in "
                "the gym are mostly maths problems (how much to eat, what a set "
                "of five says about a max, which plates go on the bar), and most "
                "online calculators answer them without showing their working. "
                "FormFit is our attempt to do that properly.",
                "If you followed an old link to an exam-photo page, it now "
                "redirects to the home page. Those tools are no longer offered.",
            ]),
            ("What you'll find here", [
                {"list": [
                    "<a href=\"/calculators\">18 calculators</a> for body "
                    "composition, calories and macros, strength training and "
                    "cardio, in metric or imperial units.",
                    "<a href=\"/workouts\">Workout plans</a> with every exercise, "
                    "set, rep and rest period written out, and how to progress.",
                    "An <a href=\"/exercises\">exercise library</a> covering setup, "
                    "coaching cues and the most common mistakes.",
                    "<a href=\"/guides\">Guides</a> on nutrition, fat loss, muscle "
                    "gain and recovery that explain the evidence in plain English.",
                ]},
            ]),
            ("How we make and check content", [
                "<strong>Calculators use published formulas.</strong> Every "
                "calculator is built on a peer-reviewed or widely used formula "
                "(Mifflin-St Jeor, the US Navy tape method, Epley, DOTS and so "
                "on). Each page names the formula, shows it, and explains where "
                "it is weak. The maths is tested in code, and the worked examples "
                "on each page are checked against what the calculator returns.",
                "<strong>Guides lean on research and position stands.</strong> "
                "We draw on published research and on statements from bodies "
                "such as the International Society of Sports Nutrition, the "
                "American College of Sports Medicine and the World Health "
                "Organization. Where the evidence is mixed we say so.",
                "<strong>We use AI tools in drafting.</strong> AI writing tools "
                "help us draft and structure some articles. We decide what goes "
                "on the site, check formulas and figures, and correct anything "
                "that turns out to be wrong. We would rather tell you this than "
                "have you wonder.",
                "<strong>Pages carry a review date.</strong> Each calculator, "
                "guide, plan and exercise page shows when it was last reviewed, "
                "and we update pages when better evidence or a reader's "
                "correction comes in.",
            ]),
            ("What FormFit is not", [
                "FormFit is not a medical service, and nothing here is a "
                "diagnosis or a personal prescription. The calculators give "
                "estimates for healthy adults. If you are pregnant, under 18, "
                "managing a medical condition or recovering from injury, please "
                "talk to a doctor or registered dietitian first. Our "
                "<a href=\"/disclaimer\">medical disclaimer</a> explains more.",
            ]),
            ("Independence and advertising", [
                {"list": [
                    "We don't sell supplements, coaching, programmes or meal "
                    "plans, and no brand pays to be mentioned in our content.",
                    "Ads are supplied by Google AdSense, are labelled "
                    "\"Advertisements\", and never sit inside a calculator or "
                    "next to a result.",
                    "There are no ads on our privacy, terms or disclaimer pages.",
                    "Calculators run in your browser, so the numbers you type are "
                    "never sent to us. See the <a href=\"/privacy\">privacy policy</a>.",
                ]},
            ]),
            ("Corrections and contact", [
                "If you spot a wrong number, a broken calculator or a claim that "
                "doesn't match the research, email "
                "<a href=\"mailto:{email}\">{email}</a> with the page and what you "
                "think it should say. Corrections are our first priority, and we "
                "update the page and its review date when we fix something.",
                "Suggestions for new calculators, exercises or guides are welcome "
                "too. More ways to reach us are on the "
                "<a href=\"/contact\">contact page</a>.",
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
                "Prefer email? Write to "
                "<a href=\"mailto:{email}\">{email}</a>. The form above lands in "
                "the same inbox, and we usually reply within two working days.",
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
                "newsletter. If you use the contact form, we receive what you "
                "write in it, and nothing else. The site is paid for by advertising from Google "
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
            ("The contact form", [
                "When you send a message through the <a href=\"/contact\">contact "
                "form</a>, the name, email address, topic and message you enter are "
                "emailed to our inbox so we can reply. They are not stored in a "
                "database, added to a mailing list, or shared with anyone else. "
                "The email is delivered through our email provider and kept in our "
                "inbox for as long as we need it to handle your message. To have a "
                "message deleted, email <a href=\"mailto:{email}\">{email}</a>.",
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
