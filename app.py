"""
FormFit - exam form photo & signature resizer
Flask + Pillow. Designed to run on cPanel via Passenger.
"""

import base64
import io
import os
from datetime import date
from math import gcd

import articles as ARTICLES_MOD
import legal as LEGAL_MOD
from flask import Flask, Response, abort, jsonify, render_template, request

try:
    from PIL import Image, ImageOps
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# ---------------------------------------------------------------------------
# Site config - change these two lines when you pick a domain
# ---------------------------------------------------------------------------

SITE_NAME = "FormFit"
SITE_URL = "https://www.formfit.in"       # no trailing slash

# Your AdSense publisher ID. Leave it as an empty string to turn ads off
# (useful while testing locally). This ID is public - it appears in the page
# source of every site running ads - so there is nothing to hide here.
ADSENSE_ID = "ca-pub-9986755295957814"

app = Flask(__name__)

# Reject uploads larger than 12 MB before they hit memory.
app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024

ALLOWED_MIME = {"image/jpeg", "image/png", "image/webp", "image/bmp"}

# Hard ceilings so nobody can ask for a 20000px canvas and eat the server.
MAX_DIMENSION = 2000
MIN_DIMENSION = 20


# ---------------------------------------------------------------------------
# Exam presets
# ---------------------------------------------------------------------------
# These are starting points based on commonly published requirements.
# Exam bodies change them between notifications, so the UI tells users to
# check their own notice. Edit this dict to add exams - nothing else changes.

PRESETS = [
    {
        "id": "ssc-photo",
        "slug": "ssc-photo-size",
        "exam": "SSC",
        "kind": "Photograph",
        "w": 350, "h": 450, "min_kb": 20, "max_kb": 50,
        "note": "CGL, CHSL, MTS, GD",
    },
    {
        "id": "ssc-sign",
        "slug": "ssc-signature-size",
        "exam": "SSC",
        "kind": "Signature",
        "w": 400, "h": 200, "min_kb": 10, "max_kb": 20,
        "note": "Black ink on white paper",
    },
    {
        "id": "ibps-photo",
        "slug": "ibps-photo-size",
        "exam": "IBPS / Bank",
        "kind": "Photograph",
        "w": 200, "h": 230, "min_kb": 20, "max_kb": 50,
        "note": "PO, Clerk, SO, RRB",
    },
    {
        "id": "ibps-sign",
        "slug": "ibps-signature-size",
        "exam": "IBPS / Bank",
        "kind": "Signature",
        "w": 140, "h": 60, "min_kb": 10, "max_kb": 20,
        "note": "PO, Clerk, SO, RRB",
    },
    {
        "id": "ibps-thumb",
        "slug": "ibps-thumb-impression-size",
        "exam": "IBPS / Bank",
        "kind": "Left thumb",
        "w": 240, "h": 240, "min_kb": 20, "max_kb": 50,
        "note": "Thumb impression",
    },
    {
        "id": "ibps-declaration",
        "slug": "ibps-handwritten-declaration-size",
        "exam": "IBPS / Bank",
        "kind": "Declaration",
        "w": 800, "h": 400, "min_kb": 50, "max_kb": 100,
        "note": "Handwritten declaration",
    },
    {
        "id": "upsc-photo",
        "slug": "upsc-photo-size",
        "exam": "UPSC",
        "kind": "Photograph",
        "w": 350, "h": 350, "min_kb": 20, "max_kb": 300,
        "note": "Civil Services, CDS, NDA",
    },
    {
        "id": "upsc-sign",
        "slug": "upsc-signature-size",
        "exam": "UPSC",
        "kind": "Signature",
        "w": 350, "h": 350, "min_kb": 20, "max_kb": 300,
        "note": "Civil Services, CDS, NDA",
    },
    {
        "id": "nta-photo",
        "slug": "neet-jee-photo-size",
        "exam": "NTA",
        "kind": "Photograph",
        "w": 400, "h": 500, "min_kb": 10, "max_kb": 200,
        "note": "NEET, JEE, CUET, UGC NET",
    },
    {
        "id": "nta-sign",
        "slug": "neet-jee-signature-size",
        "exam": "NTA",
        "kind": "Signature",
        "w": 400, "h": 200, "min_kb": 4, "max_kb": 30,
        "note": "NEET, JEE, CUET, UGC NET",
    },
    {
        "id": "rrb-photo",
        "slug": "rrb-railway-photo-size",
        "exam": "RRB / Railway",
        "kind": "Photograph",
        "w": 320, "h": 240, "min_kb": 15, "max_kb": 40,
        "note": "NTPC, Group D, ALP",
    },
    {
        "id": "rrb-sign",
        "slug": "rrb-railway-signature-size",
        "exam": "RRB / Railway",
        "kind": "Signature",
        "w": 320, "h": 240, "min_kb": 10, "max_kb": 30,
        "note": "NTPC, Group D, ALP",
    },
    {
        "id": "uppsc-photo",
        "slug": "uppsc-photo-size",
        "exam": "UPPSC / UPSSSC",
        "kind": "Photograph",
        "w": 200, "h": 230, "min_kb": 20, "max_kb": 50,
        "note": "UP state exams",
    },
    {
        "id": "uppsc-sign",
        "slug": "uppsc-signature-size",
        "exam": "UPPSC / UPSSSC",
        "kind": "Signature",
        "w": 140, "h": 60, "min_kb": 10, "max_kb": 20,
        "note": "UP state exams",
    },
    {
        "id": "passport",
        "slug": "passport-photo-size",
        "exam": "Passport",
        "kind": "Photograph",
        "w": 413, "h": 531, "min_kb": 20, "max_kb": 300,
        "note": "35 x 45 mm at 300 DPI",
    },
]



# ---------------------------------------------------------------------------
# SEO copy
# ---------------------------------------------------------------------------
# Each exam page needs its own title, description and body text. Fifteen
# pages with the same words on them is "thin content" and Google buries
# the lot, so the copy below varies by document type as well as by exam.

def build_pages():
    """One page per unique specification.

    Some exam bodies publish the same requirement - IBPS and UPPSC both want
    200x230 at 20-50 KB, for instance. Giving each its own page would create
    duplicates that compete with one another in search. A single page naming
    both ranks for both queries and reads better.
    """
    groups = {}
    for p in PRESETS:
        key = (p["kind"], p["w"], p["h"], p["min_kb"], p["max_kb"])
        groups.setdefault(key, []).append(p)

    pages = []
    for members in groups.values():
        first = members[0]
        exams = [SEARCH_NAME.get(m["exam"], m["exam"]) for m in members]
        pages.append({
            "slug": first["slug"],
            "primary": first,
            "members": members,
            "exams": exams,
            "exam_label": " and ".join(exams) if len(exams) < 3
                          else ", ".join(exams[:-1]) + " and " + exams[-1],
            "notes": [m["note"] for m in members],
        })
    return pages


def slug_for(preset):
    """Which page covers this preset - several presets can share one."""
    for page in PAGES:
        if preset in page["members"]:
            return page["slug"]
    return preset["slug"]


def _add_labels():
    """Attach the search-friendly label to each preset, once, at startup."""
    for p in PRESETS:
        p["label"] = "{} {}".format(
            SEARCH_NAME.get(p["exam"], p["exam"]),
            SEARCH_KIND.get(p["kind"], p["kind"]).lower())


def by_slug(slug):
    for page in PAGES:
        if page["slug"] == slug:
            return page
    return None


# People search for the exam they are sitting, not the body that runs it.
# Nobody types "NTA photograph size"; they type "NEET photo size".
SEARCH_NAME = {
    "NTA": "NEET JEE",
    "IBPS / Bank": "IBPS Bank",
    "RRB / Railway": "RRB Railway",
    "UPPSC / UPSSSC": "UPPSC UPSSSC",
}
SEARCH_KIND = {"Photograph": "Photo", "Left thumb": "Thumb Impression"}


def seo_meta(page):
    """The title and description Google actually shows in results."""
    p = page["primary"]
    exam = page["exam_label"]
    kind = SEARCH_KIND.get(p["kind"], p["kind"])
    title = "{exam} {kind} Size - {w}x{h} px, {lo}-{hi} KB".format(
        exam=exam, kind=kind, w=p["w"], h=p["h"],
        lo=p["min_kb"], hi=p["max_kb"])
    desc = ("The exact {kind} size for the {exam} form: {w}x{h} pixels and "
            "{lo} to {hi} KB. Free online resizer that works on mobile."
            ).format(exam=exam, kind=kind.lower(), w=p["w"], h=p["h"],
                     lo=p["min_kb"], hi=p["max_kb"])
    return title, desc


def _ratio(w, h):
    g = gcd(w, h)
    return w // g, h // g


def _shape_note(p):
    """What the target ratio means for someone holding a phone photo."""
    ratio = p["w"] / p["h"]
    if ratio > 1.6:
        return ("a wide strip",
                "A photo taken on a phone is 3:4 and taller than it is wide. It "
                "cannot fill a strip this wide without losing a large part of "
                "the top and bottom, which is why this page opens with the "
                "option that keeps the whole image and pads the sides in white.")
    if ratio > 1.05:
        return ("wider than it is tall",
                "The target is wider than it is tall while a phone photo is the "
                "other way round. Cropping to fill will take a fair amount off "
                "the top and bottom, so check the important part sits inside "
                "the frame before you download.")
    if ratio > 0.95:
        return ("close to square",
                "The target is close to square. A portrait photo loses a little "
                "from each side, which is usually fine for a head and shoulders "
                "shot.")
    if ratio > 0.85:
        return ("slightly taller than it is wide",
                "This is only a little taller than it is wide, so a portrait "
                "photo has to give up some height. Frame yourself with a bit of "
                "room below the shoulders and the crop will sit naturally.")
    if ratio > 0.72:
        return ("clearly taller than it is wide",
                "This works in your favour, because a phone photo is also "
                "taller than it is wide and in similar proportion. Very little "
                "gets cropped away, usually just a sliver from the sides.")
    return ("a tall narrow rectangle",
            "This is narrower than a phone photo, so the sides come in "
            "noticeably while the height stays. Keep your shoulders towards the "
            "middle of the frame rather than filling it edge to edge.")


def _budget(p):
    """How much room the KB ceiling actually leaves per pixel."""
    per_px = (p["max_kb"] * 1024) / (p["w"] * p["h"])
    if per_px < 0.12:
        return ("This is a tight ceiling for an image this size, so quality has "
                "to drop a little to fit. Start with a sharp, well lit photo, "
                "otherwise it will look muddy once compressed.")
    if per_px < 0.3:
        return ("The ceiling is a little tight but a good photo fits without "
                "trouble. The plainer your background, the less space it needs.")
    if per_px < 0.8:
        return ("There is plenty of room at this size, so quality barely has to "
                "drop at all.")
    return ("The ceiling is generous for an image this small. Files here tend "
            "to come out under the minimum rather than over the maximum, and "
            "the tool lifts them back into range when that happens.")


def _cm(px, dpi):
    return round(px / dpi * 2.54, 1)


PHOTO_TIPS = [
    ("What the photograph should look like",
     "Face the camera straight on with your eyes open and your whole face "
     "visible. Keep the background plain and light. White, pale blue or light "
     "grey are the safest choices. No cap and no sunglasses. Prescription "
     "glasses are usually fine as long as there is no glare on the lenses. "
     "Leave a little space above your head, because a tight frame means the "
     "crop will cut into your forehead. Many exams now ask for the date to be "
     "printed on the photograph and for it to have been taken recently, often "
     "within the last three or six months, so check your notification."),
    ("Photos that will not work",
     "A selfie is often rejected because the lens stretches the edges of the "
     "face. A picture cropped out of a group photo comes through soft and "
     "blurred. Anything sent over WhatsApp has already been compressed once, "
     "so use the original file from your gallery instead. A screenshot of a "
     "photo loses a great deal of quality and rarely passes."),
]

SIGN_TIPS = [
    ("How to produce the signature",
     "Sign on plain white paper with a black or dark blue pen. Avoid pencil "
     "and light coloured ink, which barely register once the image is "
     "compressed. Sign larger than you normally would, because a small "
     "signature looks smaller still after it has been scaled down. Photograph "
     "it in daylight and make sure no shadow from your hand or phone falls "
     "across the paper. Keep the paper straight rather than at an angle."),
    ("Use the same signature everywhere",
     "The signature you upload has to match the one you put on the OMR sheet "
     "and the attendance sheet on exam day. If they do not match, your "
     "candidature can be cancelled. Use your ordinary everyday signature "
     "rather than inventing a neater one for the form."),
]

THUMB_TIPS = [
    ("Taking the thumb impression",
     "Use a blue or black stamp pad rather than ink from a ballpoint pen. "
     "Press your thumb straight down onto plain white paper and do not roll "
     "it, or the ridges will smudge. Press gently. Too much pressure spreads "
     "the ink and the ridge pattern disappears entirely. Let it dry fully "
     "before you photograph it."),
    ("Which thumb",
     "Most forms ask for the left thumb. Confirm this in your notification, "
     "because the wrong thumb can cause problems at document verification. "
     "The impression needs to be clear. A smudged or partial print will not "
     "be accepted."),
]

DECL_TIPS = [
    ("Writing the declaration",
     "Copy the exact text given in the notification, in your own handwriting, "
     "on plain white paper, using a black or blue pen. Do not write in capital "
     "letters unless the notification specifically asks for them. Having "
     "someone else write it for you is not allowed and will void the form if "
     "it is noticed."),
    ("Photographing it",
     "Keep the whole sheet inside the frame and square to the camera rather "
     "than at an angle. Light it from the front so no shadow falls across the "
     "writing. The handwriting has to be legible, because a person reads it, "
     "so text scrawled in a hurry can cause problems."),
]

TIPS_BY_KIND = {
    "Photograph": PHOTO_TIPS,
    "Signature": SIGN_TIPS,
    "Left thumb": THUMB_TIPS,
    "Declaration": DECL_TIPS,
}


def _phone_block(p):
    """Phone advice differs a lot depending on what is being photographed."""
    if p["kind"] == "Photograph":
        return ("Doing it on a phone",
                "Tap the box, pick the shot from your gallery, and the finished "
                "file lands in Downloads ready to upload. Use the rear camera "
                "rather than the front one, since the selfie lens distorts a "
                "face at close range. Worth knowing: phone cameras do not "
                "rotate the picture, they store the rotation in a hidden tag. "
                "That is why a photo looks upright in your gallery and arrives "
                "sideways at the portal. This tool reads the tag and "
                "straightens it on the way through.")
    if p["kind"] == "Signature":
        return ("Doing it on a phone",
                "Put the signed paper on a flat surface and hold the phone "
                "directly above it rather than at an angle, or the signature "
                "comes out skewed. Turn the flash off. It blows out the paper "
                "and flattens the ink. Natural light near a window works best. "
                "Once you have the shot, tap the box above, pick it from your "
                "gallery, and the resized file goes straight to Downloads.")
    if p["kind"] == "Left thumb":
        return ("Doing it on a phone",
                "Hold the phone straight above the paper and get close enough "
                "that the impression fills a good part of the frame, but not so "
                "close that the camera cannot focus. Tap the screen on the "
                "print to lock focus before you shoot, because an out of focus "
                "thumb impression loses the ridge detail that makes it usable.")
    return ("Doing it on a phone",
            "Lay the sheet flat and shoot from directly above so the lines stay "
            "straight. Fill the frame with the paper and nothing else. Check "
            "the writing is readable when you zoom in on your phone first, "
            "because whatever you can barely read now will be worse after it "
            "has been scaled to {} pixels wide.".format(p["w"]))


def _source_block(p):
    """What the visitor's original photo needs to be, computed per preset."""
    long_edge = max(p["w"], p["h"])
    comfortable = long_edge * 2
    return ("What your original needs to be",
            "The target here has a long edge of {} pixels. Anything from a "
            "phone camera in the last decade is far bigger than that, so you "
            "have room to spare. Aim for an original with a long edge of at "
            "least {} pixels and the result stays sharp. What you must avoid is "
            "feeding in something already smaller than {} by {}, because "
            "scaling an image up cannot invent detail that was never captured. "
            "That is why a crop from a group photo, or a screenshot, tends to "
            "look soft no matter what you do to it afterwards."
            .format(long_edge, comfortable, p["w"], p["h"]))


def _scope_block(page):
    p = page["primary"]
    kind = SEARCH_KIND.get(p["kind"], p["kind"]).lower()
    scope = "; ".join(page["notes"])
    return ("Which exams this covers",
            "These dimensions apply across {}. The bodies running them keep the "
            "{} specification consistent between its papers, so one correctly "
            "sized file usually serves every form you fill under it that "
            "season. Save the {} by {} version you download here and you can "
            "reuse it, but check each notification anyway, because a single "
            "paper occasionally departs from the standard."
            .format(scope, kind, p["w"], p["h"]))


def page_body(page):
    """Full article for one exam page.

    Most of this is computed from the preset's own numbers - aspect ratio,
    physical size, compression headroom - so no two pages carry the same
    text. Templated pages that differ only by a number get treated as thin
    content, which is what gets a site rejected from ad programmes.
    """
    p = page["primary"]
    label = page["exam_label"]
    kind = SEARCH_KIND.get(p["kind"], p["kind"]).lower()
    rw, rh = _ratio(p["w"], p["h"])
    shape, shape_text = _shape_note(p)
    budget_text = _budget(p)

    blocks = []

    blocks.append((
        "What size does the {} {} need to be".format(label, kind),
        "The {} {} the {} at {} by {} pixels, saved as a JPG, with the "
        "file somewhere between {} and {} KB. At 300 DPI that works out to "
        "roughly {} by {} cm on paper. All three conditions have to hold at "
        "once. Getting the pixels right will not help if the file is the wrong "
        "weight, and a file of the right weight fails if the dimensions are "
        "off. The portal checks each one separately and the error message it "
        "shows rarely tells you which one failed."
        .format(label, "forms want" if len(page["members"]) > 1 else "form wants",
                kind, p["w"], p["h"], p["min_kb"], p["max_kb"],
                _cm(p["w"], 300), _cm(p["h"], 300))))

    blocks.append((
        "What the shape means for cropping",
        "{} by {} pixels is a ratio of {}:{}, which is {}. {} Open More "
        "controls above if you want to switch between cropping the edges to "
        "fill the frame and keeping the whole image with white space around it."
        .format(p["w"], p["h"], rw, rh, shape, shape_text)))

    blocks.append((
        "Why the range is {} to {} KB".format(p["min_kb"], p["max_kb"]),
        "People tend to read only the upper limit and compress the file as "
        "small as it will go. That is the single most common mistake. A file "
        "under {lo} KB is rejected exactly as firmly as one over {hi} KB, "
        "because the portal tests both ends. This tool searches for the best "
        "quality that still fits under {hi} KB, and if the result lands below "
        "{lo} KB it lifts the file back into range without altering a single "
        "pixel. {budget}"
        .format(lo=p["min_kb"], hi=p["max_kb"], budget=budget_text)))

    blocks.append((
        "How to do it",
        "Tap the box above and pick your image. The preset is already set to "
        "{} {}, so the width, height and KB range are filled in and you do not "
        "need to type anything. Press Resize. The result appears below with a "
        "three line checklist covering pixel size, file size and format. Green "
        "against all three means the portal will accept it. Then press "
        "Download JPG and upload that file to the form."
        .format(label, kind)))

    blocks.append(_phone_block(p))

    blocks.append(_source_block(p))
    blocks.append(_scope_block(page))

    for h, t in TIPS_BY_KIND.get(p["kind"], PHOTO_TIPS):
        blocks.append((h, t))

    blocks.append((
        "If the upload is still rejected",
        "Read your notification again and check the numbers against this page. "
        "Exam bodies revise them between cycles, and the {} by {} px and {} to "
        "{} KB shown here reflect a previous notification. If your notice says "
        "something different, type those numbers straight into the width, "
        "height and KB boxes above, which are all editable. If it still fails "
        "after that, try a different browser, and try renaming the file. Some "
        "portals quietly reject file names containing spaces or special "
        "characters."
        .format(p["w"], p["h"], p["min_kb"], p["max_kb"])))

    return blocks


_add_labels()
PAGES = build_pages()


def page_faq(page):
    """Marked up as FAQPage schema so answers can show directly in results."""
    p = page["primary"]
    label = page["exam_label"]
    kind = SEARCH_KIND.get(p["kind"], p["kind"]).lower()
    return [
        ("What is the {} {} size?".format(label, kind),
         "The {} {} the {} at {} by {} pixels with the file between "
         "{} and {} KB, in JPG format.".format(
             label, "forms need" if len(page["members"]) > 1 else "form needs",
             kind, p["w"], p["h"], p["min_kb"], p["max_kb"])),
        ("How do I get the file under {} KB?".format(p["max_kb"]),
         "Put your image into the tool above. It adjusts the quality until the "
         "file sits between {} and {} KB, leaving the dimensions exactly as the "
         "form requires.".format(p["min_kb"], p["max_kb"])),
        ("Does this work on a phone?",
         "Yes. The tool runs in a phone browser. Choose a photo from your "
         "gallery and download the resized file when it is ready."),
        ("Is my photo stored anywhere?",
         "No. The whole thing happens inside your browser and the image is "
         "never sent anywhere. Nothing is uploaded and nothing is kept."),
    ]


def related(page, n=6):
    """Internal links. Same exam body first, then the same document type."""
    p = page["primary"]
    mine = {m["exam"] for m in page["members"]}
    out = [g for g in PAGES
           if g["slug"] != page["slug"] and mine & {m["exam"] for m in g["members"]}]
    out += [g for g in PAGES
            if g["slug"] != page["slug"] and g not in out
            and g["primary"]["kind"] == p["kind"]]
    return [{"slug": g["slug"],
             "label": "{} {}".format(g["exam_label"],
                                     SEARCH_KIND.get(g["primary"]["kind"],
                                                     g["primary"]["kind"]).lower()),
             "w": g["primary"]["w"], "h": g["primary"]["h"],
             "min_kb": g["primary"]["min_kb"], "max_kb": g["primary"]["max_kb"]}
            for g in out[:n]]


# ---------------------------------------------------------------------------
# Image processing
# ---------------------------------------------------------------------------

def encode_jpeg(img, quality, dpi, subsampling=2):
    """Encode a PIL image to JPEG bytes at a given quality."""
    buf = io.BytesIO()
    img.save(
        buf,
        format="JPEG",
        quality=quality,
        optimize=True,
        subsampling=subsampling,
        dpi=(dpi, dpi),
    )
    return buf.getvalue()


def pad_jpeg(data, target_bytes):
    """
    Grow a JPEG to a minimum file size by inserting comment segments.

    Some portals reject files under a minimum KB. A JPEG COM segment is
    ignored by every decoder, so this changes file size without touching
    a single pixel. Segments go right after the SOI marker.
    """
    need = target_bytes - len(data)
    if need <= 0:
        return data

    out = bytearray(data[:2])  # SOI marker
    remaining = need
    while remaining > 4:
        # marker (2 bytes) + length field (2 bytes) + payload
        payload = min(remaining - 4, 65531)
        out += b"\xFF\xFE"
        out += (payload + 2).to_bytes(2, "big")
        out += b" " * payload
        remaining -= payload + 4
    out += data[2:]
    return bytes(out)


def whiten_background(img, threshold=200):
    """
    Push light pixels to pure white. Cleans up a signature photographed
    on paper, where the paper reads as grey rather than white.
    """
    grey = img.convert("L")
    mask = grey.point(lambda p: 255 if p > threshold else 0)
    white = Image.new("RGB", img.size, (255, 255, 255))
    white.paste(img, mask=ImageOps.invert(mask))
    return white


def fit_canvas(img, width, height, mode):
    """Bring the image to exactly width x height."""
    if mode == "contain":
        # Whole image kept, white bars fill the gap. Safer for signatures.
        copy = img.copy()
        copy.thumbnail((width, height), Image.LANCZOS)
        canvas = Image.new("RGB", (width, height), (255, 255, 255))
        canvas.paste(copy, ((width - copy.width) // 2, (height - copy.height) // 2))
        return canvas

    if mode == "stretch":
        return img.resize((width, height), Image.LANCZOS)

    # Default: crop to fill. Bias slightly above centre so faces sit right.
    return ImageOps.fit(img, (width, height), method=Image.LANCZOS,
                        centering=(0.5, 0.4))


def process(file_storage, opts):
    """Run the full pipeline. Returns (jpeg_bytes, report_dict)."""
    raw = file_storage.read()

    try:
        img = Image.open(io.BytesIO(raw))
        img.verify()               # cheap structural check
        img = Image.open(io.BytesIO(raw))   # verify() exhausts the file
    except Exception:
        raise ValueError("That file isn't a readable image. Try a JPG or PNG.")

    original_size = img.size

    # Phones write orientation into EXIF instead of rotating pixels.
    # Skip this and half your users get a sideways photo.
    img = ImageOps.exif_transpose(img)

    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        flat = Image.new("RGB", img.size, (255, 255, 255))
        flat.paste(img, mask=img.split()[-1])
        img = flat
    else:
        img = img.convert("RGB")

    if opts["whiten"]:
        img = whiten_background(img)

    if opts["grayscale"]:
        img = ImageOps.grayscale(img).convert("RGB")

    img = fit_canvas(img, opts["width"], opts["height"], opts["mode"])

    max_bytes = int(opts["max_kb"] * 1024)
    min_bytes = int(opts["min_kb"] * 1024)
    dpi = opts["dpi"]

    # Highest quality that still fits under the ceiling.
    low, high, best = 5, 95, None
    while low <= high:
        mid = (low + high) // 2
        data = encode_jpeg(img, mid, dpi)
        if len(data) <= max_bytes:
            best = data
            low = mid + 1
        else:
            high = mid - 1

    over_limit = False
    if best is None:
        # Even the worst quality overshoots. Only happens on huge canvases
        # with a tiny KB ceiling.
        best = encode_jpeg(img, 5, dpi, subsampling=2)
        over_limit = len(best) > max_bytes

    padded = False
    if len(best) < min_bytes:
        # Try earning the bytes honestly first, with better quality.
        for q in (96, 98, 100):
            richer = encode_jpeg(img, q, dpi, subsampling=0)
            if min_bytes <= len(richer) <= max_bytes:
                best = richer
                break
        else:
            if len(best) < min_bytes:
                best = pad_jpeg(best, min_bytes)
                padded = True

    report = {
        "original_w": original_size[0],
        "original_h": original_size[1],
        "original_kb": round(len(raw) / 1024, 1),
        "width": opts["width"],
        "height": opts["height"],
        "kb": round(len(best) / 1024, 1),
        "min_kb": opts["min_kb"],
        "max_kb": opts["max_kb"],
        "padded": padded,
        "over_limit": over_limit,
        "size_ok": min_bytes <= len(best) <= max_bytes,
    }
    return best, report


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template(
        "tool.html",
        presets=PRESETS,
        preset=None,
        page_title="Exam Form Photo and Signature Resizer - Exact px and KB",
        page_desc=("Resize a photo or signature to the exact pixel size and KB "
                   "range your exam form asks for. SSC, IBPS, UPSC, NEET and "
                   "Railway presets. Free and works on mobile."),
        canonical=SITE_URL + "/",
        show_ads=True,
        h1="Your form wants an exact size. Hand over the photo and take back exactly that.",
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


@app.route("/<slug>")
def exam_page(slug):
    if slug in LEGAL_MOD.BY_SLUG:
        return legal_page(slug)
    page = by_slug(slug)
    if page is None:
        abort(404)
    p = page["primary"]
    title, desc = seo_meta(page)
    return render_template(
        "tool.html",
        presets=PRESETS,
        preset=p,
        exam_label=page["exam_label"],
        plural=len(page["members"]) > 1,
        page_title=title,
        page_desc=desc,
        canonical="{}/{}".format(SITE_URL, slug),
        show_ads=True,
        h1="{} {} size".format(
            page["exam_label"], SEARCH_KIND.get(p["kind"], p["kind"]).lower()),
        body=page_body(page),
        faq=page_faq(page),
        related=related(page),
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


@app.route("/sitemap.xml")
def sitemap():
    today = date.today().isoformat()
    urls = [(SITE_URL + "/", "1.0"),
            (SITE_URL + "/guide", "0.7"),
            (SITE_URL + "/guides", "0.7")]
    urls += [("{}/{}".format(SITE_URL, g["slug"]), "0.9") for g in PAGES]
    urls += [("{}/guides/{}".format(SITE_URL, a["slug"]), "0.8")
             for a in ARTICLES_MOD.ARTICLES]
    urls += [("{}/{}".format(SITE_URL, p["slug"]), "0.3") for p in LEGAL_MOD.LEGAL]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, pri in urls:
        xml.append("  <url><loc>{}</loc><lastmod>{}</lastmod>"
                   "<priority>{}</priority></url>".format(loc, today, pri))
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="application/xml")


@app.route("/guides")
def guides_index():
    return render_template(
        "guides.html",
        articles=ARTICLES_MOD.ARTICLES,
        pages=PAGES,
        page_title="Guides for Exam Form Photos and Signatures",
        page_desc=("Plain guides to getting a photo or signature accepted by an "
                   "exam portal: file size, formats, orientation and rejections."),
        canonical=SITE_URL + "/guides",
        show_ads=True,
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


@app.route("/guides/<slug>")
def article_page(slug):
    art = ARTICLES_MOD.BY_SLUG.get(slug)
    if art is None:
        abort(404)
    others = [a for a in ARTICLES_MOD.ARTICLES if a["slug"] != slug][:4]
    return render_template(
        "article.html",
        article=art,
        h1=art["h1"],
        body=art["body"],
        others=others,
        pages=PAGES[:6],
        page_title=art["title"],
        page_desc=art["desc"],
        canonical="{}/guides/{}".format(SITE_URL, slug),
        show_ads=True,
        breadcrumb=[("Guides", SITE_URL + "/guides")],
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


def legal_page(slug):
    doc = LEGAL_MOD.BY_SLUG[slug]
    body = [(h, [t.format(email=LEGAL_MOD.CONTACT_EMAIL) for t in paras])
            for h, paras in doc["body"]]
    return render_template(
        "article.html",
        article=doc,
        h1=doc["h1"],
        body=body,
        others=[],
        pages=[],
        page_title=doc["title"],
        page_desc=doc["desc"],
        canonical="{}/{}".format(SITE_URL, slug),
        show_ads=False,          # policy: keep ads off utility pages
        updated=date.today().strftime("%d %B %Y"),
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("img/favicon.ico")


@app.route("/ads.txt")
def ads_txt():
    if not ADSENSE_ID:
        abort(404)
    pub = ADSENSE_ID.replace("ca-", "")
    return Response(
        "google.com, {}, DIRECT, f08c47fec0942fa0\n".format(pub),
        mimetype="text/plain")


@app.route("/robots.txt")
def robots():
    body = "User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE_URL)
    return Response(body, mimetype="text/plain")


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html", presets=PAGES,
                           site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID), 404


@app.route("/api/resize", methods=["POST"])
def api_resize():
    if not HAS_PIL:
        return jsonify(error="Server-side resizing needs Pillow installed. "
                             "The site does this in the browser instead."), 501
    upload = request.files.get("image")
    if upload is None or upload.filename == "":
        return jsonify(error="Choose a photo or signature first."), 400

    if upload.mimetype not in ALLOWED_MIME:
        return jsonify(error="Use a JPG, PNG, WEBP or BMP file."), 400

    def clamp_int(name, default, lo, hi):
        try:
            return max(lo, min(hi, int(float(request.form.get(name, default)))))
        except (TypeError, ValueError):
            return default

    width = clamp_int("width", 200, MIN_DIMENSION, MAX_DIMENSION)
    height = clamp_int("height", 230, MIN_DIMENSION, MAX_DIMENSION)
    min_kb = clamp_int("min_kb", 20, 1, 5000)
    max_kb = clamp_int("max_kb", 50, 2, 5000)
    dpi = clamp_int("dpi", 300, 72, 600)

    if min_kb >= max_kb:
        return jsonify(error="Minimum size must be lower than maximum size."), 400

    mode = request.form.get("mode", "cover")
    if mode not in ("cover", "contain", "stretch"):
        mode = "cover"

    opts = {
        "width": width,
        "height": height,
        "min_kb": min_kb,
        "max_kb": max_kb,
        "dpi": dpi,
        "mode": mode,
        "grayscale": request.form.get("grayscale") == "1",
        "whiten": request.form.get("whiten") == "1",
    }

    try:
        data, report = process(upload, opts)
    except ValueError as exc:
        return jsonify(error=str(exc)), 400
    except Exception:
        app.logger.exception("resize failed")
        return jsonify(error="Something broke while processing. Try another file."), 500

    report["image"] = "data:image/jpeg;base64," + base64.b64encode(data).decode()
    return jsonify(report)


@app.errorhandler(413)
def too_large(_):
    return jsonify(error="That file is over 12 MB. Use a smaller one."), 413


@app.route("/guide")
def guide():
    return render_template(
        "guide.html", presets=PRESETS,
        slug_for=slug_for,
        page_title="Photo and Signature Sizes for Every Exam Form",
        page_desc=("Pixel dimensions and KB limits for photos and signatures on "
                   "SSC, IBPS, UPSC, NEET, JEE and Railway application forms."),
        canonical=SITE_URL + "/guide",
        show_ads=True,
        site_name=SITE_NAME, site_url=SITE_URL, adsense=ADSENSE_ID)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
