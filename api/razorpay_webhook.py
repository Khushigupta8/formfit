"""POST /api/razorpay_webhook (Razorpay > Settings > Webhooks > Add).

URL:     https://www.formfit.in/api/razorpay_webhook
Secret:  the same value as the RAZORPAY_WEBHOOK_SECRET env var
Events:  subscription.authenticated, .activated, .charged, .pending, .halted,
         .cancelled, .completed, .paused, .resumed

This is the source of truth for renewals, failed payments and cancellations.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402


def handle(method, headers, body):
    if method != "POST":
        raise L.HTTPError(405, "Use POST.")
    sig = headers.get("X-Razorpay-Signature") or headers.get("x-razorpay-signature")
    if not L.hmac_ok(L.env("RAZORPAY_WEBHOOK_SECRET"), body, sig):
        raise L.HTTPError(400, "Bad signature.")
    event = L.json_body(body)
    if not str(event.get("event", "")).startswith("subscription."):
        return 200, {"ok": True, "ignored": True}
    sub = (((event.get("payload") or {}).get("subscription") or {}).get("entity")) or {}
    user_id = (sub.get("notes") or {}).get("user_id")
    if not sub.get("id") or not user_id:
        return 200, {"ok": True, "ignored": True}
    profile = L.get_profile(user_id)
    # Only the user's current subscription may change their status, so a late
    # event for an old, abandoned checkout can't undo a newer one.
    if not profile or profile.get("razorpay_subscription_id") != sub["id"]:
        return 200, {"ok": True, "ignored": True}
    L.sync_subscription(user_id, sub)
    return 200, {"ok": True}


handler = L.vercel_handler(handle)
