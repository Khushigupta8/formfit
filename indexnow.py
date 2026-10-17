"""
Tell Bing (and so DuckDuckGo and Yahoo), Yandex, Seznam and Naver that
pages changed, so they recrawl in hours instead of weeks. Google does not
use IndexNow; for Google, submit sitemap.xml in Search Console.

Run after a deploy is live:   npm run indexnow
Only submit URLs that changed:   python indexnow.py /bmi-calculator /guides/creatine-guide
"""

import json
import sys
import urllib.error
import urllib.request

from app import INDEXNOW_KEY, SITE_URL, all_urls


def main(paths):
    urls = [SITE_URL + p for p in (paths or [p for p, _ in all_urls()])]
    body = json.dumps({
        "host": SITE_URL.split("//", 1)[1],
        "key": INDEXNOW_KEY,
        "keyLocation": "{}/{}.txt".format(SITE_URL, INDEXNOW_KEY),
        "urlList": urls,
    }).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", body,
                                 {"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print("IndexNow accepted {} URLs (HTTP {}).".format(len(urls), r.status))
            return 0
    except urllib.error.HTTPError as e:
        # 403 means the key file isn't live yet: deploy first, then run this.
        print("IndexNow refused: HTTP {} {}".format(e.code, e.read().decode()[:200]))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
