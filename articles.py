"""
Standalone guide articles.

These are not exam pages. They answer the questions people type before they
know which tool they need, which is where most search traffic starts.

Each entry: slug, title (the <title> tag), h1, desc (meta description),
and body as a list of (heading, [paragraphs]).
"""

ARTICLES = [
    {
        "slug": "how-to-reduce-photo-size-to-20-kb",
        "title": "How to Reduce Photo Size to 20 KB Without Ruining It",
        "h1": "How to reduce a photo to 20 KB",
        "desc": ("Get a photo down to 20 KB for an exam form without turning it "
                 "into a blurry mess, and avoid the mistake that makes portals "
                 "reject it anyway."),
        "body": [
            ("What actually controls file size", [
                "Three things decide how many kilobytes a JPG takes up: how many "
                "pixels it contains, how much detail sits in those pixels, and how "
                "hard the JPEG encoder is told to squeeze. Most people only ever "
                "touch the first one, shrinking the image until the number falls, "
                "and end up with something too small to be accepted.",
                "The second factor is the one nobody thinks about. A photograph "
                "taken against a plain white wall compresses far smaller than the "
                "same photograph taken in front of a bookshelf, at identical "
                "dimensions and identical quality. JPEG stores difference between "
                "neighbouring pixels, and a flat background has almost none to "
                "store. If you are struggling to hit a tight limit, reshooting "
                "against a blank wall will do more than any slider.",
            ]),
            ("The mistake that gets photos rejected", [
                "Almost every form asks for a range rather than a ceiling. Twenty "
                "to fifty kilobytes. Ten to twenty. Four to thirty. People read "
                "the upper number, compress as hard as their tool allows, and "
                "submit a 6 KB file against a 20 KB minimum.",
                "That file is rejected exactly as firmly as one that came in at "
                "200 KB, and the error message usually says nothing more helpful "
                "than that the upload failed. If your photo keeps bouncing and "
                "you have been making it smaller each time, you are very likely "
                "walking further away from the answer with every attempt.",
                "Check the minimum in your notification before you compress "
                "anything. If it says 20 to 50 KB, aim for the middle, around 35 "
                "KB, so small variations do not push you outside the range.",
            ]),
            ("Doing it without losing quality", [
                "Set the pixel dimensions first, exactly as the form specifies. "
                "Only then adjust compression. Doing it the other way round means "
                "compressing twice, and JPEG loses a little detail every single "
                "time it is re-encoded, which is why a photo forwarded through "
                "three WhatsApp chats looks soft.",
                "Always work from the original file out of your camera roll, not "
                "from a copy that has already been sent somewhere. Messaging apps "
                "compress on send. The version your friend sent back to you has "
                "already lost detail you cannot recover.",
                "If you must lose something, lose it from the background rather "
                "than the face. Cropping tighter reduces pixel count and file "
                "size at once, without touching the quality of what remains.",
            ]),
            ("When 20 KB is genuinely hard", [
                "The trouble is not the target, it is the target combined with "
                "the dimensions. Twenty kilobytes is comfortable for a 140 by 60 "
                "signature and cramped for a 400 by 500 photograph, because the "
                "second one has to spread the same budget across twenty times as "
                "many pixels.",
                "If your form asks for large dimensions and a small file, expect "
                "some quality loss and plan around it. Shoot in good light, "
                "against a plain background, with the subject filling the frame. "
                "A sharp, well lit photo survives heavy compression. A dim one "
                "taken in a hurry falls apart.",
            ]),
            ("Padding, and why it is not cheating", [
                "Sometimes an image compresses well below the minimum even at the "
                "highest quality setting, particularly small signatures on white "
                "paper where there is almost nothing to encode. You cannot make "
                "the file bigger by adding quality that is not there.",
                "The standard fix is a JPEG comment segment. The format allows "
                "blocks of arbitrary data that every decoder skips over, so the "
                "file gets heavier while the image stays pixel for pixel "
                "identical. The portal reads a file inside its accepted range and "
                "displays exactly the image you saw. Our resizer does this "
                "automatically when it needs to, and tells you when it has.",
            ]),
        ],
    },
    {
        "slug": "photo-rejected-in-online-form",
        "title": "Photo Rejected in an Online Form? Here Is Why",
        "h1": "Why your photo keeps getting rejected",
        "desc": ("The real reasons exam portals reject a photo upload, in the "
                 "order they actually happen, and how to fix each one."),
        "body": [
            ("The error message is rarely honest", [
                "Portals test several conditions and report one generic failure. "
                "You get told the upload was unsuccessful, or that the file is "
                "invalid, with no indication of which check tripped. That is why "
                "people try the same fix five times.",
                "Work through the causes below in order. They are arranged by how "
                "often they turn out to be the culprit, not by how obvious they "
                "seem.",
            ]),
            ("One: the file is under the minimum", [
                "This is the single most common cause and the most "
                "counter-intuitive, because the person has been actively trying "
                "to make the file smaller. Re-read the notification. If it "
                "specifies a range, you have a floor as well as a ceiling.",
            ]),
            ("Two: the photo is sideways", [
                "Phone cameras do not rotate the image when you turn the handset. "
                "They record the orientation in a small tag inside the file and "
                "leave the pixels where they are. Your gallery app reads that tag "
                "and shows the photo the right way up, so everything looks fine.",
                "Plenty of upload systems ignore the tag. The portal receives what "
                "the sensor actually captured, which is rotated ninety degrees, "
                "and either rejects it or accepts a sideways photo onto your "
                "admit card. Any tool that reads orientation properly fixes this "
                "silently, ours included.",
            ]),
            ("Three: the dimensions are close but not exact", [
                "Some portals accept a range of dimensions and some demand an "
                "exact match. If yours wants exactly 200 by 230 pixels, then 201 "
                "by 230 fails. Resizing by dragging a corner in a phone gallery "
                "app almost never lands on an exact number, because it preserves "
                "the aspect ratio and rounds.",
            ]),
            ("Four: wrong format, or a format pretending to be another", [
                "Most forms want JPG. Renaming a PNG to end in .jpg does not "
                "convert it. The bytes inside still identify it as a PNG and any "
                "competent server checks those bytes rather than trusting the "
                "extension. You need a genuine re-encode, which is what a resizer "
                "does when it hands you a JPG.",
                "Watch for HEIC as well. Newer iPhones save in HEIC by default, "
                "and almost no Indian exam portal accepts it. In iOS, Settings, "
                "Camera, Formats, choose Most Compatible to shoot JPG instead.",
            ]),
            ("Five: the file name", [
                "Some older portals choke on spaces, apostrophes, brackets or "
                "non-English characters in a file name. If everything else looks "
                "right, rename the file to something plain like photo.jpg and try "
                "again. It costs nothing to rule out.",
            ]),
            ("Six: the background is too dark or too busy", [
                "A few portals run an automated contrast check, especially on "
                "signatures. Paper photographed in room light reads as grey rather "
                "than white and can fail. Shoot in daylight, avoid casting a "
                "shadow across the page, and use a whitening option if your tool "
                "offers one.",
            ]),
            ("If none of that works", [
                "Try a different browser. Portals under heavy load during the "
                "final days of an application window sometimes fail in ways that "
                "have nothing to do with your file. Trying at a quieter hour "
                "solves more problems than it should.",
                "Do not leave it until the last day. The servers are at their "
                "worst exactly when everyone is trying to submit, and a genuine "
                "portal fault at that point leaves you no time to work around it.",
            ]),
        ],
    },
    {
        "slug": "how-to-scan-signature-with-phone",
        "title": "How to Scan a Signature With Your Phone for a Form",
        "h1": "Scanning a signature with your phone",
        "desc": ("Get a clean signature image for an exam form using only a "
                 "phone, with a white background and no scanner needed."),
        "body": [
            ("Sign it properly first", [
                "Use plain white unlined paper. Ruled or graph paper leaves lines "
                "in the image that no amount of processing removes cleanly. A "
                "black or dark blue pen with a reasonably thick nib works best. "
                "Gel and ballpoint are both fine. Pencil and light coloured ink "
                "disappear once the image is compressed.",
                "Sign larger than you normally would, filling perhaps a third of "
                "an A4 sheet. The image gets scaled down to something like 140 by "
                "60 pixels, and a small signature turns to mush at that size while "
                "a large one stays legible.",
                "Use your ordinary signature. Whatever you upload has to match "
                "what you write on the OMR sheet and attendance register on exam "
                "day, and a mismatch can cost you your candidature. This is not "
                "the moment to invent a neater version of yourself.",
            ]),
            ("Photographing it", [
                "Put the paper on a flat surface in daylight, near a window but "
                "not in direct sun, which creates harsh shadows and blown out "
                "highlights. Turn the flash off. Flash flattens the ink and "
                "creates a bright hotspot in the middle of the page.",
                "Hold the phone directly above the paper, parallel to it. Shooting "
                "at an angle makes the signature look skewed and no crop fixes "
                "the distortion. Watch your own shadow. Standing between the "
                "window and the paper puts you in the picture whether you like it "
                "or not.",
                "Tap the screen on the signature before you shoot, which locks "
                "focus and exposure onto the ink rather than the bright paper.",
            ]),
            ("Getting the paper to read as white", [
                "This is where most phone captures fall down. Your eye sees white "
                "paper. The camera records light grey, because it exposes for the "
                "overall scene and paper reflects less light than you assume. Some "
                "portals run a contrast check and bounce the result.",
                "The fix is to push everything above a brightness threshold to "
                "pure white while leaving the dark ink untouched. Our resizer has "
                "a checkbox for exactly this, and it is switched on by default on "
                "signature presets. If you prefer to do it elsewhere, most photo "
                "editors achieve the same thing with a strong levels or curves "
                "adjustment.",
            ]),
            ("Cropping and sizing", [
                "Crop reasonably tight around the signature, leaving a small "
                "margin. Do not crop so close that the ink touches the edge, "
                "because some portals treat that as a truncated image.",
                "Then set the exact pixel dimensions your form asks for. "
                "Signatures are usually wide and short, something like 140 by 60, "
                "which is a very different shape from anything your phone camera "
                "produces. Choose the option that keeps the whole signature and "
                "pads with white rather than the one that crops to fill, or you "
                "will lose the ends of your own name.",
            ]),
            ("A note on scanner apps", [
                "Document scanner apps often apply aggressive sharpening and "
                "contrast that can break thin pen strokes into dotted lines. If "
                "you use one, check the result at full zoom before you commit. A "
                "plain camera photo processed properly is usually cleaner than an "
                "over-enhanced scan.",
            ]),
        ],
    },
    {
        "slug": "why-phone-photos-upload-sideways",
        "title": "Why Phone Photos Upload Sideways, and How to Fix It",
        "h1": "Why your photo uploads sideways",
        "desc": ("Phone photos look upright in the gallery and arrive rotated at "
                 "the portal. Here is the reason and the fix."),
        "body": [
            ("The photo was never upright", [
                "When you turn your phone sideways, the camera sensor does not "
                "turn with it. It captures the scene in whatever orientation it "
                "is physically mounted, then writes a small note inside the file "
                "saying which way up the result should be displayed. That note is "
                "called the EXIF orientation tag.",
                "Your gallery app reads the tag and rotates the picture for you on "
                "screen. Nothing was changed on disk. The pixels are still stored "
                "the way the sensor saw them, and the tag is a request rather "
                "than a fact.",
            ]),
            ("Where it breaks", [
                "Any software that reads the pixels without checking the tag gets "
                "the raw, unrotated image. Plenty of upload handlers, especially "
                "older government portals, do exactly that. So a photo that has "
                "looked upright on every screen you have seen arrives at the "
                "portal lying on its side.",
                "This is also why the problem seems random. Photos taken with the "
                "phone held upright often have no rotation to apply and pass "
                "through fine, while one taken in landscape fails. It looks like "
                "the portal is being inconsistent when it is behaving the same way "
                "every time.",
            ]),
            ("How to fix it", [
                "The reliable fix is to bake the rotation into the pixels, so the "
                "file no longer depends on a tag anyone might ignore. Any tool "
                "that reads the orientation tag and applies it before saving does "
                "this. Our resizer does it on every image that passes through, "
                "which is why a sideways photo comes out the right way up without "
                "you asking.",
                "If you would rather do it manually, open the photo in your "
                "phone's editor, rotate it a full turn, and save. Most editors "
                "rewrite the pixels and clear the tag in the process. Simply "
                "viewing the photo rotated does not help, because nothing is "
                "written back to the file.",
            ]),
            ("How to check before you upload", [
                "Email the photo to yourself and open it in a browser rather than "
                "a gallery app. Browsers are stricter about orientation than "
                "phone galleries, so if it looks wrong there it will very likely "
                "look wrong to the portal. Alternatively, drop it into any web "
                "based resizer and look at the preview.",
            ]),
        ],
    },
    {
        "slug": "passport-size-photo-at-home",
        "title": "How to Take a Passport Size Photo at Home",
        "h1": "Taking a passport size photo at home",
        "desc": ("Shoot an acceptable passport style photograph with a phone, "
                 "including background, lighting and the rules that get photos "
                 "rejected."),
        "body": [
            ("What a studio actually gives you", [
                "A photo studio provides three things: a plain evenly lit "
                "background, diffuse light with no harsh shadow, and a camera far "
                "enough away that your face is not distorted. You can reproduce "
                "all three at home. What you cannot reproduce is their willingness "
                "to reshoot until it works, so plan on taking twenty pictures.",
            ]),
            ("The background", [
                "Find a plain wall in white, off white or very light grey. Stand "
                "at least a foot away from it, further if you can. Standing "
                "against the wall throws a hard shadow directly behind your head, "
                "which is one of the most common reasons a photo is rejected.",
                "A plain bedsheet pinned flat works if you have no clear wall, but "
                "iron it first. Creases show up clearly and read as a patterned "
                "background.",
            ]),
            ("The light", [
                "Face a window during the day. Do not stand with the window behind "
                "you, or the camera exposes for the bright background and turns "
                "your face into a silhouette. Overcast days are better than bright "
                "sun, which creates deep shadows under the eyes and nose.",
                "Avoid overhead ceiling lights on their own. They cast shadows "
                "downward across the eye sockets, which is exactly where clarity "
                "matters most. Turn them off and use the window.",
            ]),
            ("The camera", [
                "Use the rear camera, not the selfie camera. The front lens is "
                "wide angle and at arm's length it visibly enlarges your nose and "
                "narrows the sides of your face. Automated face matching systems "
                "are sensitive to that distortion.",
                "Ask someone to hold the phone about five to six feet away and "
                "zoom in slightly, or prop the phone up and use the timer. "
                "Distance plus zoom gives a flatter, more accurate rendering of "
                "your face.",
            ]),
            ("How to stand and what to wear", [
                "Face the camera squarely with your shoulders level. Keep a "
                "neutral expression with your mouth closed. Eyes open, looking "
                "straight at the lens. No cap and no sunglasses. Prescription "
                "glasses are usually acceptable as long as there is no glare and "
                "the frames do not cover your eyes.",
                "Wear something that contrasts with the background. A white shirt "
                "against a white wall merges into one shape and looks poor once "
                "cropped. Darker clothing is safer.",
                "Leave space above your head when you frame the shot. Cropping to "
                "a tall ratio later will eat into the top of the frame, and if "
                "you started tight your forehead gets cut off.",
            ]),
            ("Sizing it afterwards", [
                "A passport photograph is conventionally 35 by 45 mm, which is 413 "
                "by 531 pixels at 300 DPI. Exam forms vary widely from that and "
                "usually specify their own dimensions, so always follow your "
                "notification rather than the passport standard.",
                "Several exams now require the date to be printed on the "
                "photograph, or that it was taken within the last few months. "
                "Check before you shoot, because it is easier to include a date "
                "card in the frame than to add one convincingly afterwards.",
            ]),
        ],
    },
    {
        "slug": "jpg-png-heic-which-format-for-forms",
        "title": "JPG, PNG or HEIC: Which Format Do Exam Forms Want?",
        "h1": "Which image format do exam forms accept?",
        "desc": ("Why exam portals ask for JPG, what goes wrong with PNG and "
                 "HEIC, and how to convert without losing quality."),
        "body": [
            ("Almost every form wants JPG", [
                "JPG, also written JPEG, is what Indian exam portals overwhelmingly "
                "ask for. It is old, universally supported, and crucially it lets "
                "the file size be tuned smoothly, which is how a portal can demand "
                "a photo between 20 and 50 KB and expect people to comply.",
                "That last point explains the preference. You cannot ask for a PNG "
                "of a specific kilobyte size in any meaningful way, because PNG "
                "compression is lossless and the size is whatever the image "
                "content happens to produce.",
            ]),
            ("Why PNG causes trouble", [
                "PNG is excellent for screenshots, logos and anything with sharp "
                "edges or transparency. For photographs it produces much larger "
                "files, often five to ten times the size of an equivalent JPG, "
                "which puts you over the ceiling immediately.",
                "Renaming a PNG to end in .jpg does not convert it. The file "
                "begins with bytes that identify the format, and any server "
                "checking properly will see a PNG regardless of what the name "
                "says. You need a real re-encode, which any resizer performs when "
                "it outputs a JPG.",
                "Transparency is a second trap. A PNG with a transparent "
                "background converts to JPG with that area filled, and if the "
                "converter fills it with black you get a photo with a black "
                "background. Good converters fill with white.",
            ]),
            ("HEIC, the iPhone problem", [
                "Recent iPhones save photos as HEIC by default. It is a genuinely "
                "better format, roughly half the size of JPG at similar quality, "
                "and almost no Indian exam portal accepts it. Many will not even "
                "recognise the file enough to give you a sensible error.",
                "You can switch the camera itself. Open Settings, then Camera, "
                "then Formats, and choose Most Compatible. New photos will be JPG. "
                "Existing HEIC photos need converting, which any resizer that "
                "reads HEIC will do as part of its normal output.",
                "Sharing a HEIC photo through WhatsApp converts it to JPG as a "
                "side effect, which is a common workaround. Be aware it also "
                "compresses the image heavily, so you lose quality you may need "
                "for a large photograph.",
            ]),
            ("WEBP and the others", [
                "WEBP turns up when you save an image from a website. Support in "
                "exam portals is close to zero. Convert it to JPG before you try.",
                "PDF is occasionally requested for documents like a handwritten "
                "declaration, but almost never for a photograph. Read the "
                "notification carefully, since sending a PDF where a JPG was "
                "wanted fails silently on some portals.",
            ]),
            ("Converting without losing quality", [
                "Every JPG save discards a little detail. Converting once, from "
                "your original file, is fine. Converting a file that has already "
                "been through WhatsApp, then through a compressor, then through a "
                "resizer, stacks the losses and shows.",
                "Start from the original in your camera roll every time, and do "
                "the resize and the format conversion in one step rather than "
                "several. That single habit produces noticeably better results "
                "than any amount of fiddling afterwards.",
            ]),
        ],
    },
    {
        "slug": "what-is-dpi-in-exam-form-photo",
        "title": "What DPI Means for an Exam Form Photo",
        "h1": "DPI, pixels, and what your form actually needs",
        "desc": ("Understand DPI versus pixel dimensions so you stop guessing "
                 "when a form asks for 200 DPI or a size in centimetres."),
        "body": [
            ("Pixels are real, DPI is a label", [
                "An image file contains a grid of pixels. That grid is the only "
                "thing that exists. A photo that is 350 pixels wide and 450 tall "
                "contains 157,500 pixels and that number does not change no matter "
                "what else you do to the file.",
                "DPI, dots per inch, is a separate number stored alongside the "
                "pixels that says how densely they should be printed. Changing it "
                "does not add or remove a single pixel. It only changes how large "
                "the image comes out on paper.",
                "This is why changing DPI in an editor sometimes appears to do "
                "nothing. On screen it genuinely does nothing. It matters when "
                "something gets printed, and an admit card is printed.",
            ]),
            ("Converting between the two", [
                "The arithmetic is simple. Pixels divided by DPI gives inches. "
                "Multiply by 2.54 for centimetres.",
                "So 350 pixels at 300 DPI is 350 divided by 300, which is 1.17 "
                "inches, or about 2.96 cm. The same 350 pixels at 200 DPI covers "
                "1.75 inches, or 4.45 cm, because each pixel is being printed "
                "larger.",
                "Run it backwards when a form specifies centimetres. A 3.5 by 4.5 "
                "cm photograph at 300 DPI needs 3.5 divided by 2.54 times 300, "
                "which comes to 413 pixels wide and 531 tall.",
            ]),
            ("When your form gives you both", [
                "Some notifications state dimensions in centimetres and a DPI, "
                "leaving you to work out the pixels. Others give pixels directly. "
                "A few give both, and occasionally they disagree because whoever "
                "wrote the notice made an arithmetic slip.",
                "When they conflict, the pixel figure is the one to follow. The "
                "upload validator checks pixels, because that is what it can "
                "measure reliably. DPI is metadata that many validators do not "
                "read at all.",
            ]),
            ("Does DPI affect file size?", [
                "Barely. The DPI value is a handful of bytes in the file header. "
                "Changing it from 72 to 300 does not meaningfully change the "
                "kilobytes, because the pixel data is untouched.",
                "If changing DPI in some tool did change your file size, that tool "
                "resampled the image, meaning it actually added or removed pixels. "
                "That is a different operation and it does affect quality. Be "
                "careful with editors that combine the two settings in one dialog.",
            ]),
            ("What to set", [
                "If your notification specifies a DPI, use it. If it says nothing, "
                "300 is a safe default for anything that might be printed, and it "
                "is what our resizer uses unless you change it.",
                "The important thing is to get the pixel dimensions exactly right. "
                "Get those correct and DPI almost never causes a rejection on its "
                "own.",
            ]),
        ],
    },
]

BY_SLUG = {a["slug"]: a for a in ARTICLES}
