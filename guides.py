"""
Guides. The articles themselves live in guides_a.py and guides_b.py; this
module merges them and adds the topic pages.
"""

import guides_a
import guides_b

GUIDES = guides_a.GUIDES + guides_b.GUIDES
BY_SLUG = {g["slug"]: g for g in GUIDES}


def topic_slug(name):
    return name.lower().replace(" & ", "-").replace(" ", "-")


TOPICS = [
    {"name": "Training", "image": "squat",
     "desc": "How to train: picking exercises, sets and reps, progressive overload "
             "and building a routine that keeps working."},
    {"name": "Muscle Building", "image": "arms",
     "desc": "Guides to gaining muscle: volume, bulking, cutting and body "
             "recomposition, with the numbers that matter."},
    {"name": "Nutrition", "image": "protein-food",
     "desc": "Protein, meal timing, supplements and eating for performance, "
             "explained without the hype."},
    {"name": "Fat Loss", "image": "running",
     "desc": "Losing fat without losing your mind or your muscle: calories, "
             "cardio and what actually moves the scale."},
    {"name": "Health & Recovery", "image": "stretching",
     "desc": "Sleep, rest days and measuring your progress properly, so the "
             "training you do actually pays off."},
]
for _t in TOPICS:
    _t["slug"] = topic_slug(_t["name"])
TOPIC_BY_SLUG = {t["slug"]: t for t in TOPICS}


def for_calc(slug):
    return [g for g in GUIDES if slug in g.get("related_calcs", [])]
