# FormFit, exam form photo & signature resizer

Flask + Pillow. Resizes an image to exact pixel dimensions and lands the file
inside a KB range, which is what Indian exam portals check on upload.

## Files

    app.py              presets, page content, routes
    build.py            renders every page into dist/ for static hosting
    vercel.json         clean URLs and cache headers
    passenger_wsgi.py   cPanel entry point, don't edit
    requirements.txt    Flask + Pillow
    templates/          index.html (the tool), guide.html (size reference)
    static/css/         style.css
    static/js/          app.js, does all the resizing, in the browser
    static/img/         logo, favicons, social share image
    static/fonts/       Archivo + IBM Plex, self-hosted (172 KB)
    passenger_wsgi.py   only needed for cPanel, ignore on Vercel

## Putting it on cPanel (only if you are not using Vercel)

1. **Upload.** cPanel → File Manager. Make a folder in your home directory
   called `formfit` (not inside `public_html`). Upload the zip there and
   extract it. You should see `app.py` sitting directly inside `formfit`.

2. **Create the app.** cPanel → Setup Python App → Create Application.
   - Python version: 3.9 or higher
   - Application root: `formfit`
   - Application URL: pick your domain or a subdomain
   - Application startup file: `passenger_wsgi.py`
   - Application Entry point: `application`

   Click Create.

3. **Install the packages.** Still on the Setup Python App screen, find the
   *Configuration files* box, type `requirements.txt`, click Add, then click
   **Run Pip Install**. Wait for it to finish.

4. **Restart** with the button at the top of that screen, then open your URL.

## If something breaks

**500 error.** Open `stderr.log` in your application root, the real error is
at the bottom. Nine times out of ten it's step 3 not having run.

**Pillow won't install.** Some shared hosts lack the build tools. Ask support
to install `python3-devel`, `libjpeg-devel` and `zlib-devel`, or try a slightly
older Pillow version in `requirements.txt`.

**Text looks like Times New Roman.** The `static/fonts` folder didn't make it
through the extract. Re-upload it, the fonts are self-hosted on purpose so
the page doesn't wait on Google's servers.

**Static files 404.** Confirm the `static` folder came across in the extract
and that Application root in step 2 matches your folder name exactly.

**Changes don't show up.** Passenger caches. Hit Restart, then hard-refresh
the browser with Ctrl+Shift+R.

## SEO: what is already built in

Every preset automatically becomes its own page. Fifteen presets means
fifteen indexable pages, each with its own title, description, H1, body copy
and FAQ schema. Add a preset and its page appears with no extra work.

    /ssc-photo-size
    /ibps-signature-size
    /neet-jee-photo-size          ... and so on

Also live: `/sitemap.xml` (submit this to Google Search Console on day one),
`/robots.txt`, canonical tags, Open Graph tags for WhatsApp and Telegram
shares, FAQPage and BreadcrumbList structured data, and internal links
between related sizes.

**Set your domain first.** Open `app.py` and change the two lines at the top:

    SITE_NAME = "FormFit"
    SITE_URL  = "https://formfit.com"

Canonical tags and the sitemap are built from `SITE_URL`. Leave it wrong and
you will point Google at a domain you do not own.

**Content depth.** Each exam page carries roughly 800 words, generated from
that preset's own numbers - aspect ratio, physical size at 300 DPI, how much
compression headroom the KB ceiling leaves. Pages measure 50-76% similar to
each other, which is normal for a set of related guides. Templated pages that
differ only by a number sit above 90% and get treated as duplicates.

The tool stays at the top of every page and the article sits below it, so
someone in a hurry never has to scroll past text to reach it.

**Still missing before you can apply to an ad network:** a privacy policy that
names cookies and third-party advertising, plus About, Contact and Terms
pages. HTTPS is also mandatory - turn on the free SSL in cPanel.

**Then, in order:** verify your site in Google Search Console, submit
`/sitemap.xml`, and check the sizes on each page against the official
notification PDF before you publicise anything. Published sizes that turn out
to be wrong will cost you trust you cannot buy back.

Expect nothing for three to four months. New domains sit in a trust sandbox.

## Deploying to Vercel

The site builds to plain HTML. All image work happens in the visitor's
browser, so there is no server at runtime.

**Deploy from the project root, not from `dist/`.** Vercel keeps a hidden
`.vercel` folder in whichever directory you deploy from, and that folder is
what ties the deploy to your project and your domain. `build.py` clears
`dist/` every run, so deploying from inside it used to destroy that link and
Vercel would create a fresh project and ask you to connect the domain again.
Deploying from the root keeps the link somewhere the build never touches.

### If you first deployed with Vercel Drop

Drag and drop cannot update an existing project. Every drop creates a new
one, and your domain stays attached to the old project. Use one of the two
routes below instead.

### Route 1: command line, deploy the built folder

    npm i -g vercel
    vercel login
    python build.py
    cd dist
    vercel link

Choose the existing project when it asks. Then, now and every time after:

    vercel --prod

`build.py` writes a `vercel.json` into `dist/` with the routing rules, and it
preserves `dist/.vercel` between builds, so the link survives.

### Route 2: Git, and never touch a terminal again

You do not need Git installed. GitHub's website accepts dragged files.

1. github.com, New repository, name it, Create.
2. On the empty repo page click "uploading an existing file".
3. Unzip the project and drag everything from *inside* the folder, so that
   `app.py` and `vercel.json` land at the top level of the repo, not nested
   one folder down. Commit.
4. On your existing Vercel project press Connect Git and pick the repo.

Connect Git on the project you already have rather than importing as a new
one, so the domain stays where it is.

Vercel then runs `python3 -m pip install -r requirements.txt && python3
build.py` on its own machines and publishes `dist/`. Nothing needs installing
on yours. After this you can edit `app.py`, `articles.py` or `legal.py`
straight in GitHub's web editor and the site rebuilds on save.

Pillow is deliberately not in `requirements.txt`. The build only renders
templates, and the live site resizes in the browser, so Flask is all it needs.
`requirements-server.txt` has the full set if you ever want the unused
server-side route to work.


Push the repo to GitHub, then press Connect Git on your Vercel project. Leave
the build settings alone, `vercel.json` already has them. After that, every
`git push` publishes.

If Vercel's build step fails on Python, set `"buildCommand": ""` in
`vercel.json`, delete the `dist/` line from `.gitignore`, and commit the built
folder. Vercel then serves your locally built files, which always works.

### Fresh project from scratch

    npm i -g vercel
    vercel --prod

Vercel reads `vercel.json`, runs the build itself, and publishes `dist/`.
Add your domain afterwards under Project, Settings, Domains.

### Every time after that

    vercel --prod

That is the whole thing. Same project, same domain, updated files. You never
reconnect anything.

### Better: deploy on git push

Push the repo to GitHub and import it at vercel.com. Everything is already
configured in `vercel.json`, so leave the build settings alone. From then on:

    git add -A
    git commit -m "what changed"
    git push

The site rebuilds and goes live in well under a minute. No terminal, no
uploads, and you get a rollback button in the Vercel dashboard if a change
turns out badly.

### Do not delete and recreate the project

Deploy updates to the project you already have. Deleting it releases the
domain, drops your Vercel analytics history, and leaves the site unreachable
while you set it up again, which is exactly the wrong thing to happen while
Google is crawling you.

If `vercel --prod` offers to create a new project, the folder has lost its
link. Relink it instead of accepting:

    vercel link

Choose the existing project when prompted, then deploy as normal. Your domain
and Search Console verification are untouched by any of this.

### Redirects for merged pages

When two exams turn out to share a specification their pages get merged, and
the slug that loses out would start returning 404. `vercel.json` carries a
permanent redirect for each one, and `build.py` prints a warning if a preset
slug has no page and no redirect. Keep them: an old link that redirects passes
its ranking to the surviving page, an old link that 404s throws it away.

### If the build fails on Vercel

Some accounts have trouble running Python in the build step. If that happens,
open `vercel.json` and set `"buildCommand": ""`, then remove the `dist/` line
from `.gitignore` and commit the folder. Vercel will then serve the files you
built on your own machine, which always works. Run `python build.py` before
each commit in that case.

## Local preview

    python app.py

Opens at http://127.0.0.1:5000 with the same pages. Handy while editing.
Changes only reach the live site after `python build.py` plus a deploy.

## Site structure

    /                          the resizer
    /guide                     every exam size in one table
    /<exam-slug>               13 exam pages, tool preset + ~1000 word article
    /guides                    guide index
    /guides/<slug>             7 standalone guides
    /privacy /terms
    /about /contact            trust pages, required for ad approval
    /sitemap.xml /robots.txt /ads.txt

Content lives in three files. `app.py` holds the presets and the exam page
copy, `articles.py` holds the standalone guides, `legal.py` holds the trust
pages. Add a dict to any of them and the page, its sitemap entry and its
navigation links appear on the next build.

## AdSense

The publisher ID lives in one place, at the top of `app.py`:

    ADSENSE_ID = "ca-pub-XXXXXXXXXXXXXXXX"

Set it to an empty string to turn ads off, which is what you want while
working locally so you are not loading ad scripts on every reload.

Two things get generated from it. The script tag goes into the `<head>` of
every page, and `/ads.txt` is written at the site root. That second file is
the one people forget. It is how Google confirms you actually authorised that
publisher ID, and without it AdSense flags the account and some advertisers
will not bid on your inventory. Check it resolves at `yourdomain.com/ads.txt`
after you deploy.

Changes only reach the live site after `python build.py` and a redeploy.

### Where the ads sit, and why

Slots are placed below the tool, never above it. Two reasons: AdSense
penalises layouts with heavy advertising above the fold, and an ad sitting
between a visitor and the thing they came for is the fastest way to lose
them. Exam pages carry two slots, guides one or two, the home page one.

The trust pages carry none. Ads on privacy and terms pages look bad to a
reviewer and earn nothing anyway.

Each slot is separated by a rule and labelled "Advertisement", which is what
keeps it from being mistaken for site content - a specific policy
requirement, not decoration.

If you turn on Auto ads in the AdSense dashboard, Google will start injecting
its own placements on top of these, including above the tool. Use Excluded
Areas in the Auto ads settings to protect the top of the page, or leave Auto
ads off and rely on the fixed slots.

## Replacing the logo

Everything is generated from two files in `static/img/`:

    mark.png    the F icon on its own, transparent background
    logo.png    the full lockup with wordmark and tagline

Swap those, then regenerate the icon set. `og-image.png` is the card that
shows when someone shares a link on WhatsApp or Telegram, which is how most
of this traffic will travel, so it is worth keeping current.

Sizes in use: 16, 32, 48 and 96 px for browser tabs, 180 px for the iOS home
screen, 192 and 512 px for Android, and 1200x630 for social. `favicon.ico`
bundles 16, 32 and 48 for older browsers and is copied to the site root at
build time, because browsers ask for `/favicon.ico` whatever the link tags say.

## Adding an exam

Everything lives in the `PRESETS` list near the top of `app.py`. Copy an
entry, change the numbers, restart the app. The dropdown, the chips, the guide
table, the sitemap and a whole new SEO page all build themselves from it.

    {
        "id": "mppsc-photo",
        "slug": "mppsc-photo-size",
        "exam": "MPPSC",
        "kind": "Photograph",
        "w": 200, "h": 230, "min_kb": 20, "max_kb": 50,
        "note": "State service exam",
    },

## Before you launch

- Set `debug=False`, it already is outside local development.
- Put your privacy policy and contact page up. AdSense checks for them.
- The guide page exists because AdSense rejects sites that are only tools
  with no readable content. Add more of it, one page per exam, and that's
  also how you'll rank.
