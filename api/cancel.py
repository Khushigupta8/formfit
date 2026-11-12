"""POST /api/cancel: stop renewals. Pro stays on until the paid period ends."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402


def handle(method, headers, body):
    if method != "POST":
        raise L.HTTPError(405, "Use POST.")
    user = L.user_from_token(headers)
    profile = L.get_profile(user["id"]) or {}
    sub_id = profile.get("razorpay_subscription_id")
    if not sub_id or profile.get("cancel_at_period_end") \
            or profile.get("status") in ("cancelled", "completed", "expired"):
        raise L.HTTPError(400, "There's no active subscription to cancel.")
    # A checkout that was never paid can't wait for a cycle end.
    at_end = 0 if profile.get("status") == "created" else 1
    sub = L.rzp("POST", "subscriptions/{}/cancel".format(sub_id), {"cancel_at_cycle_end": at_end})
    L.sync_subscription(user["id"], sub)
    L.update_profile(user["id"], {"cancel_at_period_end": True})
    return 200, dict(L.public_profile(L.get_profile(user["id"])), ok=True)


handler = L.vercel_handler(handle)
