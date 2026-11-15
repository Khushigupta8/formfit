"""POST /api/plan: generate and save a personalised plan. Pro only."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib as L  # noqa: E402
import _plan as P  # noqa: E402


def handle(method, headers, body):
    if method != "POST":
        raise L.HTTPError(405, "Use POST.")
    user = L.user_from_token(headers)
    if not L.is_pro(L.get_profile(user["id"])):
        raise L.HTTPError(402, "The plan generator is part of FormFit Pro.")
    inputs, errors = P.validate(L.json_body(body))
    if errors:
        return 400, {"ok": False, "errors": errors, "error": "Please check the highlighted fields."}
    plan = P.generate(inputs)
    row = L.db("POST", "plans", {"user_id": user["id"], "inputs": inputs, "plan": plan},
               prefer="return=representation")
    return 200, {"ok": True, "id": row[0]["id"] if row else None, "plan": plan}


class handler(L.vercel_handler(handle)):
    """Vercel only picks up files with a top-level class named `handler`."""
