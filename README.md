# FormFit: gym & fitness calculators

Flask templates frozen to static HTML. Every calculator runs in the visitor's
browser, so there is no server at runtime.

    npm run dev        live preview at http://127.0.0.1:5000 (ad slots outlined)
    npm run build      write the static site to dist/
    npm run preview    build, then serve dist/ at http://localhost:5001
    npm run seo        audit every built page (titles, descriptions, H1s,
                       canonicals, social tags, JSON-LD, breadcrumbs, alt text,
                       WebP, lazy loading, links, sitemap coverage)
    npm run indexnow   after a deploy is live: ping Bing/Yandex to recrawl

The npm scripts just call Python (3.9+ with Flask: pip install -r requirements.txt).

## SEO built in

- Unique title (brand suffix dropped when it would push past 60 chars) and
  meta description per page; one H1; canonical URL; robots meta with
  max-image-preview:large; noindex on the 404.
- Open Graph + Twitter cards. Each page shares its own photo
  (static/img/og/*.jpg, 1200x630); the home page uses og-image.png.
- JSON-LD: Organization + WebSite (home), WebApplication (calculators),
  Article (guides, workouts, exercises), FAQPage and BreadcrumbList.
- sitemap.xml with lastmod and image entries; robots.txt; ads.txt.
- Descriptive alt text per photo (PHOTO_ALT in app.py).
- Search Console: paste your HTML-tag token into GSC_VERIFICATION in app.py,
  or verify by DNS. Then submit https://www.formfit.in/sitemap.xml.
- Bing Webmaster Tools: import from Search Console, or paste the msvalidate.01
  token into BING_VERIFICATION. IndexNow (indexnow.py, key in INDEXNOW_KEY,
  key file built to /<key>.txt) pings Bing, Yandex, Seznam and Naver.
- Old URLs redirect with a real 301 (statusCode in vercel.json; Vercel's
  "permanent" would send a 308).
- MODIFIED / REVIEWED in app.py drive the dates; bump them when you update content.

## Installable app (PWA)

- `/manifest.webmanifest` (route in app.py): name, icons incl. maskable,
  shortcuts to the TDEE, macro, 1RM and plate calculators.
- `/sw.js` (templates/sw.js): on install it precaches every calculator page,
  the hubs, CSS/JS and fonts, so all 18 calculators work offline. Pages are
  network-first with a cache fallback, then `/offline`. Its version is a hash
  of the source, so each build that changes anything replaces the old caches.
- Footer "Install the app" button appears when the browser allows installing
  (Chrome, Edge, Android). On iPhone: Share > Add to Home Screen.

## Files

    app.py              site config (domain, AdSense, ad slot IDs) and routes
    calculators.py      the 18 calculators: names, fields, categories
    calc_content_a.py   article, FAQ and references for calculators 1-9
    calc_content_b.py   ... and 10-18
    guides.py           merges guides_a.py + guides_b.py + guides_india.py, defines guide topics
    exercises.py        16 exercises
    workouts.py         6 workout plans
    legal.py            about, contact, privacy, terms, medical disclaimer
    api/contact.py      contact form endpoint (Vercel function)
    indexnow.py         submit URLs to IndexNow after a deploy
    templates/          Jinja templates; _macros.html holds icons, ads, cards
    static/js/calc.js   all calculator maths (metric internally)
    static/js/site.js   ad preview, exercise filter, mobile menu
    static/img/photos/  Unsplash photos (free commercial licence), WebP, 2 sizes
    static/img/mark.svg the logo mark; PNG icons and og-image are made from it

## Site structure (76 indexable pages)

    /                               home
    /calculators                    hub
    /<name>-calculator              18 calculators, each with a ~1,000 word article
    /workouts, /workouts/<slug>     6 plans with full weekly schedules
    /exercises, /exercises/<slug>   16 exercises: steps, cues, mistakes
    /guides, /guides/<slug>         21 long-form guides (6 India-focused)
    /guides/topic/<topic>           5 topic pages
    /about /contact /privacy /terms /disclaimer

Old exam-resizer URLs 301-redirect to the home page (see `vercel.json`).

## Contact form

`/contact` posts to `api/contact.py`, a Vercel serverless function that emails
the message over SMTP (standard library only). app.py serves the same code at
`/api/contact` for local preview. It has a honeypot and a 3-second minimum fill
time against bots; nothing is stored.

Until these are set in Vercel > Settings > Environment Variables (then
redeploy), the form answers "not set up yet, please email us":

| Variable     | Example                                   |
|--------------|-------------------------------------------|
| `SMTP_HOST`  | `smtp.gmail.com`                          |
| `SMTP_PORT`  | `465` (SSL) or `587` (STARTTLS)           |
| `SMTP_USER`  | the sending mailbox                       |
| `SMTP_PASS`  | Gmail: an App Password (needs 2-step verification) |
| `CONTACT_TO` | inbox for messages (defaults to SMTP_USER) |

After deploying, send yourself a test message from the live /contact page.

## Ads

`ADSENSE_ID` in `app.py` loads the AdSense script on every page except the
legal pages and the 404, and builds `/ads.txt`.

Fixed placements are already in the templates. They stay empty until you
create a display ad unit in AdSense and paste its slot ID into `AD_SLOTS`:

| Name         | Where                                                   |
|--------------|---------------------------------------------------------|
| `below_tool` | under a calculator / workout schedule, above the article |
| `in_article` | between sections 2-3 and 5-6 of long articles            |
| `sidebar`    | sticky right column on desktop (300x600)                 |
| `in_feed`    | inside card grids on hub pages                           |
| `end`        | after the article, before related links                 |

To see every placement, add `?adpreview` to any URL on the live site, or run
`python app.py` locally.

Policy choices already made, and why: nothing above the calculator, every
unit labelled "Advertisement", no units next to buttons or results, none on
privacy/terms/disclaimer, and no limit on Auto ads. If you switch Auto ads on,
check a few pages; Auto ads plus five fixed units can feel heavy on mobile.

## Adding content

- **Calculator:** add an entry to `CALCS` in `calculators.py`, a function with
  the same `id` to `CALC` in `calc.js`, and copy to a content file.
- **Guide / exercise / workout:** add a dict to the relevant file. Pages,
  sitemap entries and links appear on the next build.
- When you review content, bump `REVIEWED` in `app.py`.

## Deploying

Same as before: `python build.py`, commit, push. Vercel serves `dist/` as-is
(`buildCommand` is empty, so commit the built `dist/` folder).
