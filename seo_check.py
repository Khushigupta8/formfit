"""
SEO audit of the built site. Run after build.py:   npm run seo

Checks every page in dist/ for the things that quietly cost rankings:
title and description length, duplicates, exactly one H1, canonical,
social tags, valid JSON-LD, images without alt, and broken internal links.
"""

import json
import os
import re
import sys
from collections import defaultdict

OUT = "dist"


def pages():
    for root, _, files in os.walk(OUT):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(root, f).replace("\\", "/")


def main():
    files = set()
    for root, _, fs in os.walk(OUT):
        for f in fs:
            files.add(os.path.join(root, f).replace("\\", "/")[len(OUT):])

    problems, titles, descs = [], defaultdict(list), defaultdict(list)
    count = 0
    for path in pages():
        h = open(path, encoding="utf-8").read()
        url = path[len(OUT):].replace("index.html", "") or "/"
        noindex = 'content="noindex' in h
        count += 1

        def bad(msg):
            problems.append("{:45} {}".format(url, msg))

        t = re.search(r"<title>(.*?)</title>", h, re.S)
        d = re.search(r'<meta name="description" content="(.*?)">', h)
        t = t.group(1).strip() if t else ""
        d = d.group(1) if d else ""
        if not t:
            bad("missing <title>")
        elif len(t) > 65:
            bad("title {} chars: {}".format(len(t), t))
        if not noindex and not 70 <= len(d) <= 165:
            bad("description {} chars".format(len(d)))
        if not noindex:
            titles[t].append(url)
            descs[d].append(url)
            if '<link rel="canonical"' not in h:
                bad("no canonical")
            for tag in ("og:title", "og:description", "og:image", "og:url", "twitter:card"):
                if tag not in h:
                    bad("missing " + tag)
        h1s = len(re.findall(r"<h1[\s>]", h))
        if h1s != 1:
            bad("{} <h1> tags".format(h1s))
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(block)
            except ValueError:
                bad("invalid JSON-LD")
        for img in re.findall(r"<img\b[^>]*>", h):
            if "alt=" not in img:
                bad("img without alt")
        for link in re.findall(r'(?:href|src)="(/[^"#?]*)', h):
            clean = link.rstrip("/")
            if not (link in files or clean + "/index.html" in files or clean == ""):
                bad("broken link " + link)

    for t, urls in titles.items():
        if len(urls) > 1:
            problems.append("duplicate title on {}: {}".format(urls, t))
    for d, urls in descs.items():
        if len(urls) > 1:
            problems.append("duplicate description on {}".format(urls))

    print("Checked {} pages.".format(count))
    for p in problems:
        print("  " + p)
    print("No problems found." if not problems else "{} problem(s).".format(len(problems)))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
