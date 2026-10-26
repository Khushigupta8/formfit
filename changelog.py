"""
What changed on FormFit, newest first.

One entry per real content change. Each entry drives three things:
- the "What's new" list on the home page (latest few entries),
- the "Updated" date shown on every page listed in `paths`,
- that page's sitemap <lastmod> and Article dateModified.

A page not named in any entry keeps LAUNCHED as its date. Only add an entry
when the page itself changed (new section, corrected numbers, new photos or
notes): bumping dates without changes is what Google treats as spam.

    {"date": "2026-11-02", "note": "Added my own form notes to the deadlift",
     "paths": ["/exercises/deadlift"]},
"""

LAUNCHED = "2026-10-12"

CHANGES = [
    {"date": "2026-10-18",
     "note": "BMI calculator now shows Asian / Indian cut-offs (healthy 18.5-22.9), "
             "plus six new India-focused guides on diet, protein and home workouts",
     "paths": ["/bmi-calculator", "/guides",
               "/guides/bmi-chart-for-indians",
               "/guides/high-protein-indian-vegetarian-foods",
               "/guides/indian-diet-plan-for-weight-loss",
               "/guides/high-protein-indian-breakfast",
               "/guides/indian-gym-diet-for-muscle-gain",
               "/guides/home-workout-for-beginners-no-equipment"]},
    {"date": "2026-10-17",
     "note": "Contact form added, so you can send corrections and questions straight from the site",
     "paths": ["/contact"]},
    {"date": LAUNCHED,
     "note": "FormFit launched: 18 calculators, 6 workout plans, 16 exercise guides and 15 long-form guides",
     "paths": []},
]


def updated(path):
    """Date (YYYY-MM-DD) a page last really changed."""
    return max([c["date"] for c in CHANGES if path in c["paths"]] or [LAUNCHED])
