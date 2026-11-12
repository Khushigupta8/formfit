"""POST /api/subscribe {"plan": "monthly" | "yearly"}

Creates a Razorpay subscription for the signed-in user and returns what the
browser needs to open Razorpay Checkout. The user only becomes Pro once the
payment is verified (api/verify.py) or the webhook says so.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402

# How many billing cycles Razorpay may charge before the mandate ends.
# UPI AutoPay mandates are capped, so keep these moderate.
CYCLES = {"monthly": 60, "yearly": 5}


def handle(method, headers, body):
    if method != "POST":
        raise L.HTTPError(405, "Use POST.")
    user = L.user_from_token(headers)
    plan = L.json_body(body).get("plan")
    if plan not in CYCLES:
        raise L.HTTPError(400, "Choose monthly or yearly.")
    profile = L.get_profile(user["id"]) or {}
    if L.is_pro(profile):
        # Razorpay can't undo a cancellation, and a new subscription would
        # charge again straight away, so wait until the paid period is over.
        raise L.HTTPError(409, "Your Pro access runs until the end of the period you've paid for. "
                               "You can subscribe again after that."
                          if profile.get("cancel_at_period_end") else "You already have FormFit Pro.")

    sub = L.rzp("POST", "subscriptions", {
        "plan_id": L.env("RAZORPAY_PLAN_" + plan.upper()),
        "total_count": CYCLES[plan],
        "customer_notify": 1,
        "notes": {"user_id": user["id"], "plan": plan},
    })
    L.update_profile(user["id"], {"razorpay_subscription_id": sub["id"], "plan": plan,
                                  "status": "created", "cancel_at_period_end": False})
    return 200, {"ok": True, "subscription_id": sub["id"],
                 "key_id": L.env("RAZORPAY_KEY_ID"), "email": user.get("email")}


handler = L.vercel_handler(handle)
