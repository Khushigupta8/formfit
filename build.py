"""
Build every page to plain HTML in dist/.

Run this, then deploy dist/. The site needs no server at runtime because
all image work happens in the browser, which means no cold starts, no
upload size limit, and nothing to pay for.

    python build.py
"""

import os
import shutil
import stat
import sys

from app import INDEXNOW_KEY, all_urls, app

OUT = "dist"


def _unlock(func, path, _exc):
    """Retry a delete after clearing the read-only bit.

    OneDrive marks synced folders read-only, and Windows then refuses to
    remove them, so a rebuild inside a synced folder fails on the second run.
    """
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(path):
    shutil.rmtree(path, onexc=_unlock) if sys.version_info >= (3, 12) \
        else shutil.rmtree(path, onerror=lambda f, p, e: _unlock(f, p, e))


def write(client, route, path):
    res = client.get(route)
    if res.status_code not in (200, 404):
        print("  FAILED {} -> {}".format(route, res.status_code))
        return False
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "wb") as f:
        f.write(res.data)
    return True


def main():
    # .vercel is what links this folder to your existing Vercel project and
    # therefore to your domain. Wiping it makes the next deploy create a
    # brand new project and ask you to connect the domain all over again.
    keep = os.path.join(OUT, ".vercel")
    stash = None
    if os.path.isdir(keep):
        stash = OUT + ".vercel.bak"
        if os.path.isdir(stash):
            rmtree(stash)
        shutil.move(keep, stash)

    if os.path.isdir(OUT):
        rmtree(OUT)
    os.makedirs(OUT)

    if stash:
        shutil.move(stash, keep)

    ok = 0
    with app.test_client() as c:
        # Folder-per-page gives clean URLs (/bmi-calculator) on any static host.
        for path, _ in all_urls():
            ok += write(c, path, "index.html" if path == "/" else path.strip("/") + "/index.html")
        ok += write(c, "/offline", "offline/index.html")
        for f in ("sitemap.xml", "robots.txt", "ads.txt", INDEXNOW_KEY + ".txt",
                  "manifest.webmanifest", "sw.js"):
            ok += write(c, "/" + f, f)
        ok += write(c, "/this-page-does-not-exist", "404.html")

    shutil.copytree("static", os.path.join(OUT, "static"))

    # dist/ is already the built output, so it needs the routing rules but not
    # the build instructions. This lets you deploy dist/ directly.
    import json
    cfg = json.load(open("vercel.json"))
    json.dump({k: cfg[k] for k in ("cleanUrls", "trailingSlash", "redirects", "headers")
               if k in cfg}, open(os.path.join(OUT, "vercel.json"), "w"), indent=2)
    # browsers request /favicon.ico from the root regardless of the link tags
    shutil.copy("static/img/favicon.ico", os.path.join(OUT, "favicon.ico"))

    total = sum(
        os.path.getsize(os.path.join(r, f))
        for r, _, fs in os.walk(OUT) for f in fs
    )
    print("Built {} pages into {}/  ({:.0f} KB total)".format(ok, OUT, total / 1024))
    print("Deploy that folder. Nothing else needed.")


if __name__ == "__main__":
    if "SITE_URL" in os.environ:
        print("note: SITE_URL comes from app.py, not the environment")
    sys.exit(main())
