"""
FormFit - gym and fitness calculators, workouts, exercises and guides.

Flask is only used to render templates. build.py freezes every route into
dist/ as plain HTML, and every calculator runs in the visitor's browser.

    python app.py      local preview at http://127.0.0.1:5000 (ad slots outlined)
    python build.py    write the static site to dist/
"""

import os
import re
from datetime import date

from flask import Flask, Response, abort, render_template, request

import calculators as C
import exercises as E
import guides as G
import legal as L
import workouts as W

# ---------------------------------------------------------------------------
# Site config
# ---------------------------------------------------------------------------

SITE_NAME = "FormFit"
SITE_URL = "https://www.formfit.in"       # no trailing slash
TAGLINE = "Fitness calculators and training guides"

# Shown as "Reviewed <date>" on content pages, and used as the sitemap
# lastmod / article modified date. Bump both when you review content.
REVIEWED = "October 2026"
MODIFIED = "2026-10-12"

# Google Search Console > Add property > HTML tag: paste the content="..."
# value here. Optional if you verify by DNS instead.
GSC_VERIFICATION = ""

# AdSense publisher ID. Empty string turns every ad tag off.
ADSENSE_ID = "ca-pub-9986755295957814"

# Ad unit IDs from AdSense > Ads > By ad unit. Each placement on the site is
# tagged with one of these names. Leave a value empty and that placement
# renders nothing (Auto ads can still fill the page). Fill it in and a fixed
# responsive unit appears there on every page that has the placement.
AD_SLOTS = {
    "below_tool": "",    # under a calculator's result, above the article
    "in_article": "",    # inside long articles, between sections
    "sidebar": "",       # sticky column on desktop
    "in_feed": "",       # inside card grids on hub pages
    "end": "",           # after the article, before related links
}

# Outline every placement with a labelled box. On by default when running
# app.py locally; on the live site add ?adpreview to any URL to see them.
AD_PREVIEW = os.environ.get("FORMFIT_AD_PREVIEW") == "1"

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


app.jinja_env.filters["slugify"] = slugify

# Alt text per photo key: describes the picture, not the page it sits on.
PHOTO_ALT = {
    "hero": "Athlete gripping a loaded barbell before a deadlift",
    "gym-floor": "Industrial gym floor with benches, racks and free weights",
    "barbell-rack": "Loaded barbell in a power rack in front of a city view",
    "squat": "Woman performing a barbell back squat in a rack",
    "deadlift": "Lifter gripping a barbell on the gym floor for a deadlift",
    "bench-press": "Man bench pressing a barbell with a spotter behind him",
    "dumbbells": "Rows of dumbbells on a rack in a gym",
    "pull-up": "Woman using a cable pulldown machine",
    "kettlebell": "Man doing a kettlebell exercise in a functional gym",
    "running": "Three runners silhouetted against a blue evening sky",
    "cycling": "Athlete training on a rowing machine",
    "home-workout": "Man doing push-ups on dumbbells at home",
    "woman-lifting": "Woman holding a barbell across her shoulders in a rack",
    "stretching": "Woman stretching in a downward dog position on a mat",
    "healthy-meal": "Plate of eggs, avocado, greens and vegetables",
    "meal-prep": "Meal prep salad in a glass jar with fresh vegetables",
    "protein-food": "Bowl with salmon, eggs, edamame and vegetables",
    "water": "Bottle of water on a table",
    "scale": "Athletic woman's back in a gym",
    "measuring-tape": "Bodybuilder showing his back muscles",
    "sleep": "Man resting on a bench between sets",
    "battle-ropes": "Man training with battle ropes",
    "push-up": "Man doing a push-up on a gym floor",
    "curl": "Man doing a barbell curl",
    "arms": "Muscular man in a sleeveless top in a gym",
    "chalk": "Lifter chalking up beside a loaded barbell",
    "plates": "Barbell loaded with weight plates in a rack",
    "group-class": "Group fitness class training with resistance bands",
    "bright-gym": "Bright modern gym with cardio machines",
    "fit-food": "Bowl of vegetables, chickpeas and avocado",
    "core": "Woman doing a core exercise on a mat",
    "rows": "Woman doing a single-arm dumbbell row on a bench",
}
app.jinja_env.globals["alt"] = lambda key: PHOTO_ALT.get(key, "")


def words(item):
    """Rough word count of everything readable on a page, for read times."""
    n = len(item.get("intro", "").split())
    for _, blocks in item.get("body", []):
        for b in blocks:
            if isinstance(b, str):
                n += len(b.split())
            elif "list" in b or "olist" in b:
                n += sum(len(x.split()) for x in b.get("list", b.get("olist", [])))
            elif "tip" in b:
                n += len(b["tip"].split())
    return n


def minutes(item):
    return max(3, round(words(item) / 220))


def crumbs(*pairs):
    """BreadcrumbList schema plus the visible trail."""
    items = [("Home", SITE_URL + "/")] + list(pairs)
    return items


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ],
    }


def faq_schema(faq):
    if not faq:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }


def article_schema(title, desc, url, image):
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "mainEntityOfPage": url,
        "image": "{}/static/img/photos/{}.webp".format(SITE_URL, image),
        "author": {"@type": "Organization", "name": SITE_NAME + " Editorial Team",
                   "url": SITE_URL + "/about"},
        "publisher": {"@type": "Organization", "name": SITE_NAME,
                      "logo": {"@type": "ImageObject",
                               "url": SITE_URL + "/static/img/logo.png"}},
        "dateModified": MODIFIED,
        "datePublished": "2026-10-12",
    }


def render(template, **kw):
    """render_template with everything every page needs."""
    kw.setdefault("show_ads", True)
    kw.setdefault("image", "hero")
    kw.setdefault("schema", [])
    kw["schema"] = [s for s in kw["schema"] if s]
    trail = kw.get("breadcrumb")
    if trail:
        kw["schema"].append(breadcrumb_schema(trail))
    # Keep the <title> under ~60 characters: drop the brand suffix when the
    # page title is already long enough to be truncated with it.
    t = kw["page_title"]
    full = "{} | {}".format(t, SITE_NAME)
    kw["title_tag"] = t if kw.get("full_title") or len(full) > 60 else full
    article = any(k in kw for k in ("g", "w", "x"))
    kw["og_type"] = "article" if article else "website"
    kw["section"] = (kw.get("g") or {}).get("category") or ("Workouts" if "w" in kw else "Exercises")
    kw["og_image"] = SITE_URL + (
        "/static/img/og/{}.jpg".format(kw["image"]) if kw["image"] != "hero"
        else "/static/img/og-image.png")
    return render_template(
        template,
        site_name=SITE_NAME, site_url=SITE_URL, tagline=TAGLINE, reviewed=REVIEWED,
        modified=MODIFIED, gsc_verification=GSC_VERIFICATION,
        adsense=ADSENSE_ID, ad_slots=AD_SLOTS,
        ad_preview=AD_PREVIEW or app.debug,
        categories=C.CATEGORIES, calcs=C.CALCS, by_cat=C.by_cat,
        popular=[c for c in C.CALCS if c.get("popular")],
        guide_topics=G.TOPICS,
        year=date.today().year,
        **kw)


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render(
        "home.html",
        page_title="FormFit - Free Gym & Fitness Calculators",
        page_desc=("Free fitness calculators for people who train: BMI, TDEE, "
                   "macros, body fat, one rep max and FFMI, plus workout plans "
                   "and evidence-based guides."),
        canonical=SITE_URL + "/",
        full_title=True,
        workouts=W.WORKOUTS, exercises=E.EXERCISES[:8],
        guides=G.GUIDES[:6],
        schema=[{
            "@context": "https://schema.org", "@type": "WebSite",
            "name": SITE_NAME, "url": SITE_URL + "/",
        }, {
            "@context": "https://schema.org", "@type": "Organization",
            "name": SITE_NAME, "url": SITE_URL + "/",
            "logo": SITE_URL + "/static/img/logo.png",
        }])


@app.route("/calculators")
def calculators_hub():
    return render(
        "calculators.html",
        page_title="Fitness Calculators: BMI, TDEE, Macros, 1RM and More",
        page_desc=("Every FormFit calculator in one place: body composition, "
                   "calories and macros, strength training and cardio. Free, "
                   "private, metric and imperial."),
        canonical=SITE_URL + "/calculators",
        h1="Fitness calculators",
        breadcrumb=crumbs(("Calculators", SITE_URL + "/calculators")),
        image="bright-gym")


def calc_page(calc):
    url = "{}/{}".format(SITE_URL, calc["slug"])
    related = [c for c in C.by_cat(calc["cat"]) if c is not calc]
    related += [c for c in C.CALCS if c.get("popular") and c is not calc
                and c not in related]
    return render(
        "calculator.html",
        calc=calc,
        page_title=calc["title"], page_desc=calc["desc"],
        canonical=url, h1=calc["name"], image=calc["image"],
        related=related[:6],
        guides=G.for_calc(calc["slug"])[:3],
        read_min=minutes(calc),
        breadcrumb=crumbs(("Calculators", SITE_URL + "/calculators"),
                          (calc["name"], url)),
        schema=[{
            "@context": "https://schema.org", "@type": "WebApplication",
            "name": calc["name"], "url": url,
            "applicationCategory": "HealthApplication",
            "operatingSystem": "Any", "description": calc["desc"],
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        }, faq_schema(calc["faq"])])


@app.route("/workouts")
def workouts_hub():
    return render(
        "workouts.html",
        workouts=W.WORKOUTS,
        page_title="Free Workout Plans for Every Goal and Level",
        page_desc=("Free gym and home workout plans with full weekly schedules: "
                   "beginner full body, push pull legs, upper lower, 5x5 strength, "
                   "dumbbell-only and fat loss."),
        canonical=SITE_URL + "/workouts",
        h1="Workout plans",
        breadcrumb=crumbs(("Workouts", SITE_URL + "/workouts")),
        image="gym-floor")


@app.route("/workouts/<slug>")
def workout_page(slug):
    w = W.BY_SLUG.get(slug) or abort(404)
    url = "{}/workouts/{}".format(SITE_URL, slug)
    return render(
        "workout.html",
        w=w, page_title=w["title"], page_desc=w["desc"], canonical=url,
        h1=w["name"], image=w["image"], read_min=minutes(w),
        others=[x for x in W.WORKOUTS if x is not w][:3],
        ex=E.BY_SLUG, calc_by_slug=C.BY_SLUG,
        breadcrumb=crumbs(("Workouts", SITE_URL + "/workouts"), (w["name"], url)),
        schema=[article_schema(w["title"], w["desc"], url, w["image"]),
                faq_schema(w["faq"])])


@app.route("/exercises")
def exercises_hub():
    return render(
        "exercises.html",
        exercises=E.EXERCISES, muscles=E.MUSCLES,
        page_title="Exercise Library: How to Do Every Major Lift",
        page_desc=("Step-by-step technique for the lifts that matter: squat, "
                   "deadlift, bench, overhead press, rows, pull-ups and more, "
                   "with muscles worked, cues and common mistakes."),
        canonical=SITE_URL + "/exercises",
        h1="Exercise library",
        breadcrumb=crumbs(("Exercises", SITE_URL + "/exercises")),
        image="dumbbells")


@app.route("/exercises/<slug>")
def exercise_page(slug):
    x = E.BY_SLUG.get(slug) or abort(404)
    url = "{}/exercises/{}".format(SITE_URL, slug)
    return render(
        "exercise.html",
        x=x, page_title=x["title"], page_desc=x["desc"], canonical=url,
        h1=x["name"], image=x["image"],
        related=[E.BY_SLUG[s] for s in x.get("related", []) if s in E.BY_SLUG],
        plans=[W.BY_SLUG[s] for s in x.get("plans", []) if s in W.BY_SLUG],
        same_muscle=[e for e in E.EXERCISES if e["muscle"] == x["muscle"] and e is not x][:4],
        breadcrumb=crumbs(("Exercises", SITE_URL + "/exercises"), (x["name"], url)),
        schema=[article_schema(x["title"], x["desc"], url, x["image"]),
                faq_schema(x["faq"])])


@app.route("/guides")
def guides_hub():
    return render(
        "guides.html",
        guides=G.GUIDES, topic=None,
        page_title="Fitness Guides: Training, Nutrition and Fat Loss",
        page_desc=("Evidence-based guides on building muscle, losing fat, protein, "
                   "progressive overload, recovery and sleep, written in plain "
                   "English with numbers you can use."),
        canonical=SITE_URL + "/guides",
        h1="Guides",
        breadcrumb=crumbs(("Guides", SITE_URL + "/guides")),
        image="healthy-meal")


@app.route("/guides/topic/<topic>")
def guides_topic(topic):
    t = G.TOPIC_BY_SLUG.get(topic) or abort(404)
    url = "{}/guides/topic/{}".format(SITE_URL, topic)
    return render(
        "guides.html",
        guides=[g for g in G.GUIDES if g["category"] == t["name"]], topic=t,
        page_title="{} Guides".format(t["name"]),
        page_desc=t["desc"], canonical=url, h1=t["name"],
        breadcrumb=crumbs(("Guides", SITE_URL + "/guides"), (t["name"], url)),
        image=t["image"])


@app.route("/guides/<slug>")
def guide_page(slug):
    g = G.BY_SLUG.get(slug) or abort(404)
    url = "{}/guides/{}".format(SITE_URL, slug)
    i = G.GUIDES.index(g)
    return render(
        "guide.html",
        g=g, page_title=g["title"], page_desc=g["desc"], canonical=url,
        h1=g["h1"], image=g["image"], read_min=minutes(g),
        next_guide=G.GUIDES[(i + 1) % len(G.GUIDES)],
        others=[x for x in G.GUIDES if x["category"] == g["category"] and x is not g][:3]
        or G.GUIDES[:3],
        tools=[C.BY_SLUG[s] for s in g.get("related_calcs", []) if s in C.BY_SLUG],
        breadcrumb=crumbs(("Guides", SITE_URL + "/guides"),
                          (g["category"], "{}/guides/topic/{}".format(
                              SITE_URL, G.topic_slug(g["category"]))),
                          (g["h1"], url)),
        schema=[article_schema(g["title"], g["desc"], url, g["image"]),
                faq_schema(g["faq"])])


@app.route("/<slug>")
def top_level(slug):
    if slug in C.BY_SLUG:
        return calc_page(C.BY_SLUG[slug])
    if slug in L.BY_SLUG:
        doc = L.BY_SLUG[slug]
        return render(
            "legal.html", doc=doc,
            page_title=doc["title"], page_desc=doc["desc"],
            canonical="{}/{}".format(SITE_URL, slug), h1=doc["h1"],
            email=L.CONTACT_EMAIL,
            updated=L.UPDATED,
            show_ads=False)     # policy: no ads on utility and legal pages
    abort(404)


# ---------------------------------------------------------------------------
# Machine files
# ---------------------------------------------------------------------------

def all_urls():
    u = [("/", "1.0"), ("/calculators", "0.9"), ("/workouts", "0.8"),
         ("/exercises", "0.8"), ("/guides", "0.8")]
    u += [("/" + c["slug"], "0.9") for c in C.CALCS]
    u += [("/workouts/" + w["slug"], "0.8") for w in W.WORKOUTS]
    u += [("/exercises/" + x["slug"], "0.7") for x in E.EXERCISES]
    u += [("/guides/topic/" + t["slug"], "0.5") for t in G.TOPICS]
    u += [("/guides/" + g["slug"], "0.8") for g in G.GUIDES]
    u += [("/" + p["slug"], "0.3") for p in L.LEGAL]
    return u


def page_images():
    """Photo key for each URL, so the sitemap can list images for image search."""
    m = {"/": "hero", "/calculators": "bright-gym", "/workouts": "gym-floor",
         "/exercises": "dumbbells", "/guides": "healthy-meal"}
    m.update({"/" + c["slug"]: c["image"] for c in C.CALCS})
    m.update({"/workouts/" + w["slug"]: w["image"] for w in W.WORKOUTS})
    m.update({"/exercises/" + x["slug"]: x["image"] for x in E.EXERCISES})
    m.update({"/guides/" + g["slug"]: g["image"] for g in G.GUIDES})
    m.update({"/guides/topic/" + t["slug"]: t["image"] for t in G.TOPICS})
    return m


@app.route("/sitemap.xml")
def sitemap():
    imgs = page_images()
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for path, pri in all_urls():
        entry = "  <url><loc>{}{}</loc><lastmod>{}</lastmod><priority>{}</priority>".format(
            SITE_URL, path, MODIFIED, pri)
        if path in imgs:
            entry += "<image:image><image:loc>{}/static/img/photos/{}.webp</image:loc></image:image>".format(
                SITE_URL, imgs[path])
        xml.append(entry + "</url>")
    xml.append("</urlset>")
    return Response("\n".join(xml), mimetype="application/xml")


@app.route("/ads.txt")
def ads_txt():
    if not ADSENSE_ID:
        abort(404)
    pub = ADSENSE_ID.replace("ca-", "")
    return Response("google.com, {}, DIRECT, f08c47fec0942fa0\n".format(pub),
                    mimetype="text/plain")


@app.route("/robots.txt")
def robots():
    return Response("User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE_URL),
                    mimetype="text/plain")


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file("img/favicon.ico")


@app.errorhandler(404)
def not_found(_):
    return render("404.html", page_title="Page not found",
                  page_desc="This page does not exist.",
                  canonical=SITE_URL + request.path, noindex=True,
                  show_ads=False, h1="Page not found"), 404


if __name__ == "__main__":
    app.run(debug=True)
