"""
Trust pages. AdSense will not approve a site without these, and the privacy
policy has to actually describe what happens - cookies, third party ad
vendors, and what you do with uploads.

CONTACT_EMAIL below is a placeholder. Put a real, working address in before
you apply, because reviewers check that it is reachable.
"""

CONTACT_EMAIL = "devkhushii08@gmail.com"

LEGAL = [
    {
        "slug": "privacy",
        "title": "Privacy Policy",
        "h1": "Privacy policy",
        "desc": ("How FormFit handles your images, what cookies are used for "
                 "advertising, and the choices you have."),
        "body": [
            ("Your images never leave your device", [
                "This is the part that matters most, so it comes first. When you "
                "resize a photo or signature here, the work happens inside your "
                "own web browser using your device's processor. The image file is "
                "not uploaded to us. It is not transmitted over the network at "
                "all.",
                "Because nothing is sent, there is nothing for us to store, "
                "nothing to delete on a schedule, and nothing that could be "
                "exposed if our hosting were ever compromised. When you close the "
                "tab, the image is gone from memory along with the page.",
                "We therefore hold no photographs, no signatures, and no "
                "thumbprints belonging to anyone.",
            ]),
            ("What we do collect", [
                "Our host records standard server logs when a page is requested. "
                "These typically include an IP address, the page requested, a "
                "timestamp, and the browser's user agent string. They are used to "
                "keep the site running and to detect abuse.",
                "We do not ask you to create an account, and we do not collect "
                "names, email addresses or phone numbers unless you choose to "
                "write to us.",
            ]),
            ("Advertising and cookies", [
                "This site displays advertising supplied by Google AdSense.",
                "Third party vendors, including Google, use cookies to serve ads "
                "based on your prior visits to this and other websites. Google's "
                "use of advertising cookies enables it and its partners to serve "
                "ads to you based on your visit to this site and other sites on "
                "the internet.",
                "You can opt out of personalised advertising by visiting Google's "
                "Ads Settings at https://www.google.com/settings/ads. You may also "
                "opt out of a third party vendor's use of cookies for personalised "
                "advertising at https://www.aboutads.info/choices/.",
                "Third party vendors and ad networks other than Google may also "
                "serve ads on this site. You can visit "
                "https://optout.networkadvertising.org/ to opt out of some of "
                "these vendors' use of cookies.",
                "If you are in the European Economic Area, the United Kingdom or "
                "Switzerland, you will be shown a consent notice before "
                "personalised advertising cookies are set, and you can change your "
                "choice at any time.",
            ]),
            ("Analytics", [
                "We may use privacy-respecting analytics to count page views and "
                "understand which guides are useful. This does not identify you "
                "personally and is not combined with the advertising data "
                "described above.",
            ]),
            ("Children", [
                "This site is a utility aimed at people filling in examination "
                "forms and is not directed at children under 13. We do not "
                "knowingly collect personal information from children.",
            ]),
            ("Your choices", [
                "You can block or delete cookies through your browser settings. "
                "Doing so will not affect the resizer, because it does not depend "
                "on cookies to function. It may affect which advertisements you "
                "see.",
            ]),
            ("Changes and contact", [
                "If this policy changes we will update the date shown at the "
                "bottom of this page. For any question about privacy, write to "
                "{email} and we will respond.",
            ]),
        ],
    },
    {
        "slug": "terms",
        "title": "Terms of Use",
        "h1": "Terms of use",
        "desc": "The terms under which FormFit is provided, and its limits.",
        "body": [
            ("Using this site", [
                "FormFit is provided free of charge for personal use. You may use "
                "it to prepare images for examination and application forms. You "
                "may not attempt to disrupt the service, run automated bulk "
                "requests against it, or republish its content as your own.",
            ]),
            ("Accuracy of the sizes we list", [
                "The dimensions and file size limits shown on this site are "
                "compiled from published examination notifications and are offered "
                "as a convenience. Examination bodies revise their requirements "
                "between cycles and occasionally between papers in the same cycle.",
                "The official notification for your examination is the only "
                "authoritative source. Always check the numbers there before you "
                "upload. We accept no responsibility for an application rejected "
                "because a specification changed after we published it.",
            ]),
            ("No warranty", [
                "The tool is provided as is. We do not guarantee that a file "
                "produced here will be accepted by any particular portal, because "
                "acceptance depends on that portal's own rules and behaviour, "
                "which are outside our control.",
                "To the extent permitted by law, we are not liable for any loss "
                "arising from use of this site, including a missed application "
                "deadline.",
            ]),
            ("Advertising", [
                "This site is supported by advertising. Advertisements are "
                "supplied by third parties and their presence does not constitute "
                "an endorsement by us of the advertiser, its products, or its "
                "services. Any dealing you have with an advertiser is between you "
                "and them.",
            ]),
            ("Intellectual property", [
                "The text, design and code of this site belong to us. Images you "
                "process remain entirely yours, and since they never reach our "
                "servers we could make no claim over them even if we wished to.",
            ]),
            ("Contact", [
                "Questions about these terms can be sent to {email}.",
            ]),
        ],
    },
    {
        "slug": "about",
        "title": "About FormFit",
        "h1": "About FormFit",
        "desc": ("Why FormFit exists, how it works, and who maintains it."),
        "body": [
            ("Why this exists", [
                "Every examination season, a large number of candidates get as far "
                "as the photograph upload and stop. The form wants an exact pixel "
                "size and a file weight inside a narrow band, the error message "
                "explains nothing, and the existing tools are either slow, "
                "smothered in advertising, or ask you to hand your photograph to "
                "an unknown server.",
                "FormFit does one job. You pick your examination, it fills in the "
                "correct numbers, and it hands back a file that matches. There is "
                "no sign up and no charge.",
            ]),
            ("How it works", [
                "All the image processing runs in your browser. When you choose a "
                "file, your device reads it, resizes it, and searches for the "
                "highest JPEG quality that still lands inside the required "
                "kilobyte range. If the result falls below the minimum, it adds "
                "JPEG comment padding, which changes the file size without "
                "altering a single pixel.",
                "It also reads the orientation tag that phone cameras write, which "
                "is why photographs that arrive sideways at other portals come out "
                "the right way up here.",
                "Nothing is uploaded. That is a deliberate design decision rather "
                "than a limitation, because the safest way to handle somebody's "
                "photograph and signature is never to receive it.",
            ]),
            ("Where the sizes come from", [
                "The presets are compiled from published examination "
                "notifications. We check them against official documents, but "
                "requirements change and mistakes are possible, so every page "
                "tells you to verify against your own notice. If you find a "
                "number that is wrong, please tell us and we will correct it.",
            ]),
            ("How it is funded", [
                "The site carries advertising, which covers hosting and the time "
                "spent keeping the presets current. There is no paid tier and no "
                "feature held back behind one.",
            ]),
            ("Contact", [
                "Corrections, requests for an examination we have not covered, and "
                "anything else: {email}.",
            ]),
        ],
    },
    {
        "slug": "contact",
        "title": "Contact",
        "h1": "Contact us",
        "desc": "How to reach FormFit for corrections, requests or any question.",
        "body": [
            ("Write to us", [
                "Email {email} and we read everything that arrives. We usually "
                "reply within two or three working days.",
            ]),
            ("Reporting a wrong size", [
                "This is the most useful thing you can send us. If a page lists a "
                "specification that does not match your notification, tell us the "
                "examination, the page you were looking at, and what your notice "
                "actually says. A link to the notification PDF helps enormously. "
                "We correct these quickly because a wrong number here can cost "
                "somebody an application.",
            ]),
            ("Requesting an examination", [
                "If we do not cover your examination, send us its name and the "
                "photograph and signature requirements from the notification and "
                "we will add a preset for it.",
            ]),
            ("Something not working", [
                "Tell us which browser and device you were using and what you "
                "expected to happen. If a particular image fails, please describe "
                "it rather than attaching it. We would rather not receive your "
                "photograph, and we do not need it to diagnose most problems.",
            ]),
            ("Advertising and other enquiries", [
                "Advertising on this site is handled through Google AdSense, so we "
                "do not sell placements directly. For anything else, the same "
                "address reaches us.",
            ]),
        ],
    },
]

BY_SLUG = {p["slug"]: p for p in LEGAL}
