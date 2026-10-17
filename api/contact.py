"""
Contact form endpoint: POST /api/contact.

Vercel runs this file as a serverless function (the rest of the site stays
static). app.py imports the same functions so the form also works under
`python app.py`. Standard library only, so it needs no extra packages.

The message is emailed over SMTP. Set these in Vercel > Project > Settings >
Environment Variables (and redeploy):

    SMTP_HOST    smtp.gmail.com            (or your provider's host)
    SMTP_PORT    465                       465 = SSL, 587 = STARTTLS
    SMTP_USER    the mailbox that sends     e.g. devkhushii08@gmail.com
    SMTP_PASS    its password               Gmail: a 16-character App Password
    CONTACT_TO   where messages arrive      defaults to SMTP_USER

Nothing is stored: the message goes straight into the email.
"""

import json
import os
import re
import smtplib
import ssl
import time
from email.message import EmailMessage
from email.utils import formataddr
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

TOPICS = ("Correction", "Suggestion", "Privacy request", "Partnership", "Other")
LIMITS = {"name": 100, "email": 254, "message": 5000}
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class NotConfigured(Exception):
    pass


def validate(data):
    """Return (clean fields, {field: error}). An empty dict means it's valid."""
    def one(k):
        v = data.get(k, "")
        v = v[0] if isinstance(v, list) else v
        return str(v or "").strip()

    # Header-bound fields must be a single line.
    f = {k: re.sub(r"[\r\n]+", " ", one(k)) for k in ("name", "email", "topic")}
    f["message"] = one("message")
    errors = {}
    if not f["name"]:
        errors["name"] = "Please tell us your name."
    if not EMAIL_RE.match(f["email"]):
        errors["email"] = "Please enter a valid email address so we can reply."
    if f["topic"] not in TOPICS:
        f["topic"] = "Other"
    if len(f["message"]) < 10:
        errors["message"] = "Please write a little more (at least 10 characters)."
    for k, n in LIMITS.items():
        if len(f[k]) > n:
            errors[k] = "That's too long (max {} characters).".format(n)
    return f, errors


def is_spam(data):
    """Honeypot field filled in, or the form submitted inhumanly fast."""
    def one(k):
        v = data.get(k, "")
        return (v[0] if isinstance(v, list) else v) or ""
    if one("website"):
        return True
    try:
        started = int(one("ts")) / 1000
    except ValueError:
        return False            # no JS, no timestamp: let it through
    return 0 < time.time() - started < 3


def send(f):
    host, user, pw = (os.environ.get(k, "") for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASS"))
    if not host:
        raise NotConfigured("SMTP_HOST is not set")
    port = int(os.environ.get("SMTP_PORT") or 465)
    to = os.environ.get("CONTACT_TO") or user

    msg = EmailMessage()
    msg["Subject"] = "[FormFit] {}: {}".format(f["topic"], f["name"])
    msg["From"] = formataddr(("FormFit contact form", os.environ.get("CONTACT_FROM") or user))
    msg["To"] = to
    msg["Reply-To"] = formataddr((f["name"], f["email"]))
    msg.set_content("{}\n\n--\nFrom: {} <{}>\nTopic: {}\nSent via formfit.in/contact\n".format(
        f["message"], f["name"], f["email"], f["topic"]))

    ctx = ssl.create_default_context()
    if port == 465:
        s = smtplib.SMTP_SSL(host, port, context=ctx, timeout=15)
    else:
        s = smtplib.SMTP(host, port, timeout=15)
        if os.environ.get("SMTP_STARTTLS", "1") != "0":
            s.starttls(context=ctx)
    with s:
        if user and pw:
            s.login(user, pw)
        s.send_message(msg)


def handle(data):
    """(status, json body) for a parsed form submission."""
    if is_spam(data):
        return 200, {"ok": True}        # don't tell bots they were caught
    f, errors = validate(data)
    if errors:
        return 400, {"ok": False, "errors": errors,
                     "error": "Please fix the highlighted fields."}
    try:
        send(f)
    except NotConfigured:
        return 503, {"ok": False, "error": "The form isn't set up yet. Please email us instead."}
    except (smtplib.SMTPException, OSError) as e:
        print("contact form send failed:", repr(e))
        return 502, {"ok": False, "error": "We couldn't send that just now. Please try again or email us."}
    return 200, {"ok": True}


def parse(body, content_type):
    if "application/json" in (content_type or ""):
        try:
            d = json.loads(body or b"{}")
            return d if isinstance(d, dict) else {}
        except ValueError:
            return {}
    return parse_qs((body or b"").decode("utf-8", "replace"))


FALLBACK = """<!DOCTYPE html><meta charset="utf-8"><meta name="robots" content="noindex">
<title>Message not sent</title><p>{}</p><p><a href="/contact">Back to the contact page</a></p>"""


class handler(BaseHTTPRequestHandler):
    """Vercel's Python runtime looks for a class named `handler`."""

    def do_POST(self):
        n = min(int(self.headers.get("Content-Length") or 0), 64 * 1024)
        ctype = self.headers.get("Content-Type", "")
        status, out = handle(parse(self.rfile.read(n), ctype))
        if "application/json" in self.headers.get("Accept", "") or "application/json" in ctype:
            self._reply(status, "application/json", json.dumps(out))
        elif out["ok"]:
            # No-JS submit: back to the page, where #sent shows the thank-you.
            self.send_response(303)
            self.send_header("Location", "/contact#sent")
            self.end_headers()
        else:
            msg = " ".join(out.get("errors", {}).values()) or out["error"]
            self._reply(status, "text/html; charset=utf-8", FALLBACK.format(msg))

    def do_GET(self):
        self.send_response(303)
        self.send_header("Location", "/contact")
        self.end_headers()

    def _reply(self, status, ctype, body):
        b = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)
