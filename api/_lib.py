"""
Shared helpers for the FormFit Pro serverless functions.

Files in api/ that start with "_" are not turned into endpoints by Vercel,
so this module is only ever imported. Standard library only.

Environment variables (Vercel > Project > Settings > Environment Variables):

    SUPABASE_URL               https://<project>.supabase.co
    SUPABASE_SERVICE_ROLE_KEY  Supabase > Project settings > API > service_role
                               (secret: server only, never put it in app.py)
    RAZORPAY_KEY_ID            Razorpay > Settings > API keys (rzp_test_... first)
    RAZORPAY_KEY_SECRET        the matching secret
    RAZORPAY_WEBHOOK_SECRET    the secret you type when adding the webhook
    RAZORPAY_PLAN_MONTHLY      plan_... id of the monthly plan
    RAZORPAY_PLAN_YEARLY       plan_... id of the yearly plan
"""

import base64
import hashlib
import hmac
import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler


class HTTPError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def env(name):
    v = os.environ.get(name, "")
    if not v:
        raise HTTPError(503, "Pro isn't set up yet ({} is missing).".format(name))
    return v


def _request(method, url, headers, body=None):
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()
            return r.status, json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        raw = e.read()
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, {"error": raw.decode("utf-8", "replace")}


# ---------------------------------------------------------------------------
# Supabase
# ---------------------------------------------------------------------------

def _sb_headers(extra=None):
    key = env("SUPABASE_SERVICE_ROLE_KEY")
    h = {"apikey": key, "Authorization": "Bearer " + key}
    h.update(extra or {})
    return h


def user_from_token(headers):
    """The signed-in Supabase user for an `Authorization: Bearer <jwt>` header.

    Supabase checks the token itself, so an expired or forged one fails here.
    """
    auth = headers.get("Authorization") or headers.get("authorization") or ""
    if not auth.lower().startswith("bearer "):
        raise HTTPError(401, "Please sign in.")
    status, user = _request("GET", env("SUPABASE_URL") + "/auth/v1/user", {
        "apikey": env("SUPABASE_SERVICE_ROLE_KEY"), "Authorization": auth})
    if status != 200 or not user or not user.get("id"):
        raise HTTPError(401, "Your session has expired. Please sign in again.")
    return user


def db(method, path, body=None, prefer=None):
    """PostgREST call with the service role (bypasses row level security)."""
    extra = {"Prefer": prefer} if prefer else None
    status, out = _request(method, env("SUPABASE_URL") + "/rest/v1/" + path,
                           _sb_headers(extra), body)
    if status >= 300:
        print("supabase", method, path, status, out)
        raise HTTPError(502, "Database error. Please try again.")
    return out


def get_profile(user_id):
    rows = db("GET", "profiles?id=eq.{}&select=*".format(user_id))
    return rows[0] if rows else None


def update_profile(user_id, fields):
    fields = dict(fields, updated_at=iso(time.time()))
    db("PATCH", "profiles?id=eq.{}".format(user_id), fields, prefer="return=minimal")


def iso(ts):
    return datetime.fromtimestamp(int(ts), timezone.utc).isoformat()


GRACE = 24 * 3600   # Razorpay charges on the renewal date; allow a day for it.


def is_pro(profile):
    """Paid up: inside the current billing period and not halted for failed
    payments. A subscription cancelled at period end stays Pro until then."""
    if not profile or not profile.get("current_period_end"):
        return False
    if profile.get("status") == "halted":
        return False
    end = datetime.fromisoformat(profile["current_period_end"].replace("Z", "+00:00"))
    return end.timestamp() + GRACE > time.time()


def public_profile(p):
    p = p or {}
    return {"plan": p.get("plan"), "status": p.get("status"),
            "current_period_end": p.get("current_period_end"),
            "cancel_at_period_end": bool(p.get("cancel_at_period_end")),
            "is_pro": is_pro(p)}


# ---------------------------------------------------------------------------
# Razorpay
# ---------------------------------------------------------------------------

def rzp(method, path, body=None):
    token = base64.b64encode("{}:{}".format(env("RAZORPAY_KEY_ID"),
                                            env("RAZORPAY_KEY_SECRET")).encode()).decode()
    status, out = _request(method, "https://api.razorpay.com/v1/" + path,
                           {"Authorization": "Basic " + token}, body)
    if status >= 300:
        print("razorpay", method, path, status, out)
        msg = ((out or {}).get("error") or {}).get("description") if isinstance(out, dict) else None
        raise HTTPError(502, msg or "Payment provider error. Please try again.")
    return out


def hmac_ok(secret, message, signature):
    if isinstance(message, str):
        message = message.encode("utf-8")
    want = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(want, signature or "")


def sync_subscription(user_id, sub):
    """Copy a Razorpay subscription entity onto the user's profile."""
    fields = {"razorpay_subscription_id": sub["id"], "status": sub.get("status")}
    if sub.get("current_end"):
        fields["current_period_end"] = iso(sub["current_end"])
    plan = (sub.get("notes") or {}).get("plan")
    if plan:
        fields["plan"] = plan
    update_profile(user_id, fields)


# ---------------------------------------------------------------------------
# Running a function on Vercel and under Flask
# ---------------------------------------------------------------------------

def run(fn, method, headers, body):
    """Call fn(method, headers, body_bytes) -> (status, dict), turning
    HTTPError and crashes into JSON errors."""
    try:
        return fn(method, headers, body)
    except HTTPError as e:
        return e.status, {"ok": False, "error": e.message}
    except Exception as e:      # never leak a stack trace to the browser
        print("pro api error:", repr(e))
        return 500, {"ok": False, "error": "Something went wrong. Please try again."}


def json_body(body):
    try:
        d = json.loads(body or b"{}")
        return d if isinstance(d, dict) else {}
    except ValueError:
        return {}


def vercel_handler(fn):
    """A BaseHTTPRequestHandler class for Vercel's Python runtime."""

    class handler(BaseHTTPRequestHandler):
        def _go(self):
            n = min(int(self.headers.get("Content-Length") or 0), 256 * 1024)
            body = self.rfile.read(n) if n else b""
            status, out = run(fn, self.command, self.headers, body)
            b = json.dumps(out).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(b)

        do_GET = do_POST = _go

    return handler
