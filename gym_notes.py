"""
First-hand notes from the gym, keyed by exercise slug.

These are what make an exercise page more than a rewrite of every other
how-to: what *you* noticed doing the lift. Write them yourself, from real
sessions. An exercise with no entry simply shows no "From the gym" block.

Each entry:
    "notes":  2-5 short paragraphs or points in your own words: what clicked,
              what you got wrong at first, the cue that fixed it, the weights
              and reps you actually use.
    "photo":  optional, a photo of you doing this exercise, saved under
              static/img/team/ (WebP, about 900px wide), e.g. "khushi-squat.webp".
    "alt":    describes the photo, required when there is a photo.
    "date":   the day you wrote or last changed the notes (YYYY-MM-DD).

When you add or change notes, also add an entry to changelog.py for
/exercises/<slug>, so the page's Updated date moves with it.

Example:
    "hip-thrust": {
        "notes": [
            "For my first month I pushed through my toes and felt it in my quads. "
            "Moving my feet closer and driving through the heels fixed it.",
            "I pause one second at the top on every rep. Right now that is "
            "3 x 10 at 60 kg.",
        ],
        "photo": "khushi-hip-thrust.webp",
        "alt": "Khushi Gupta at the top of a barbell hip thrust",
        "date": "2026-11-02",
    },
"""

GYM_NOTES = {
}
