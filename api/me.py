"""GET /api/me: the signed-in user's Pro status (Authorization: Bearer <jwt>)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402


def handle(method, headers, body):
    user = L.user_from_token(headers)
    profile = L.get_profile(user["id"])
    if not profile:     # the signup trigger normally creates it; be safe
        L.db("POST", "profiles", {"id": user["id"], "email": user.get("email")},
             prefer="resolution=ignore-duplicates,return=minimal")
        profile = L.get_profile(user["id"])
    return 200, dict(L.public_profile(profile), ok=True, email=user.get("email"))


handler = L.vercel_handler(handle)
