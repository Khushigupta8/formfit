"""POST /api/verify: called by the browser right after Razorpay Checkout.

Checks the payment signature, then reads the subscription back from Razorpay
so the user is Pro straight away instead of waiting for the webhook.
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402


def handle(method, headers, body):
    if method != "POST":
        raise L.HTTPError(405, "Use POST.")
    user = L.user_from_token(headers)
    d = L.json_body(body)
    pay, sub_id, sig = (str(d.get(k) or "") for k in (
        "razorpay_payment_id", "razorpay_subscription_id", "razorpay_signature"))
    if not L.hmac_ok(L.env("RAZORPAY_KEY_SECRET"), pay + "|" + sub_id, sig):
        raise L.HTTPError(400, "We couldn't verify that payment. If you were charged, contact us.")
    profile = L.get_profile(user["id"]) or {}
    if profile.get("razorpay_subscription_id") != sub_id:
        raise L.HTTPError(400, "That subscription belongs to a different account.")

    sub = L.rzp("GET", "subscriptions/" + sub_id)
    L.sync_subscription(user["id"], sub)
    if not sub.get("current_end"):
        # Paid, but Razorpay has not set the period yet: Pro for 2 days until
        # the subscription.activated / .charged webhook fills in the real date.
        L.update_profile(user["id"], {"current_period_end": L.iso(time.time() + 2 * 86400),
                                      "status": "active"})
    return 200, dict(L.public_profile(L.get_profile(user["id"])), ok=True)


class handler(L.vercel_handler(handle)):
    """Vercel only picks up files with a top-level class named `handler`."""
