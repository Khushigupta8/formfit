"""
Calculator definitions.

Each entry describes the form; the maths lives in static/js/calc.js under the
same id. Page copy (article, FAQ, sources) lives in calc_content_a.py and
calc_content_b.py, keyed by slug, and is merged in at the bottom of this file.

Field types understood by templates/_fields.html and calc.js:
    sex      male / female toggle
    age      years
    height   cm, or ft + in in imperial mode
    weight   body weight, kg or lb
    load     a weight on a bar, kg or lb
    length   a tape measurement, cm or in
    number   plain number, "unit" is shown as a suffix
    select   "options" is a list of (value, label)
"""

import calc_content_a
import calc_content_b

CATEGORIES = [
    ("body", "Body composition", "Where you stand today: BMI, body fat, lean mass and frame."),
    ("nutrition", "Nutrition & calories", "How much to eat, and what, for the goal you have."),
    ("strength", "Strength training", "Numbers for the barbell: maxes, loading, scoring."),
    ("cardio", "Cardio & health", "Heart rate, calories burned and the markers that matter."),
]

ACTIVITY = [
    ("1.2", "Sedentary: desk job, little exercise"),
    ("1.375", "Light: exercise 1-3 days a week"),
    ("1.55", "Moderate: exercise 3-5 days a week"),
    ("1.725", "Very active: hard exercise 6-7 days"),
    ("1.9", "Extra active: physical job plus training"),
]

SEX = {"name": "sex", "type": "sex", "label": "Sex"}
AGE = {"name": "age", "type": "age", "label": "Age", "default": 28}
HEIGHT = {"name": "height", "type": "height", "label": "Height", "default": 175}
WEIGHT = {"name": "weight", "type": "weight", "label": "Weight", "default": 75}
ACT = {"name": "activity", "type": "select", "label": "Activity level",
       "options": ACTIVITY, "default": "1.55"}

CALCS = [
    # ---- body composition -------------------------------------------------
    {"id": "bmi", "slug": "bmi-calculator", "name": "BMI Calculator", "cat": "body",
     "icon": "scale", "image": "scale", "popular": True,
     "blurb": "Body mass index with WHO or Asian/Indian cut-offs, and a healthy weight range for your height.",
     "fields": [HEIGHT, WEIGHT,
                {"name": "standard", "type": "select", "label": "BMI cut-offs",
                 "options": [("who", "WHO international"),
                             ("asian", "Asian / Indian (lower cut-offs)")],
                 "default": "who"}]},
    {"id": "bodyfat", "slug": "body-fat-calculator", "name": "Body Fat Calculator", "cat": "body",
     "icon": "ruler", "image": "measuring-tape", "popular": True,
     "blurb": "US Navy tape method: body fat %, fat mass and lean mass from four measurements.",
     "fields": [SEX, HEIGHT,
                {"name": "neck", "type": "length", "label": "Neck", "default": 38,
                 "hint": "Just below the Adam's apple"},
                {"name": "waist", "type": "length", "label": "Waist", "default": 85,
                 "hint": "Men: at the navel. Women: narrowest point"},
                {"name": "hip", "type": "length", "label": "Hips", "default": 98,
                 "hint": "Widest point of the buttocks", "only": "female"},
                dict(WEIGHT, label="Weight (optional, for fat and lean mass)")]},
    {"id": "ideal", "slug": "ideal-weight-calculator", "name": "Ideal Weight Calculator", "cat": "body",
     "icon": "target", "image": "woman-lifting",
     "blurb": "Four classic ideal body weight formulas side by side, plus the healthy BMI range.",
     "fields": [SEX, HEIGHT]},
    {"id": "lbm", "slug": "lean-body-mass-calculator", "name": "Lean Body Mass Calculator", "cat": "body",
     "icon": "body", "image": "measuring-tape",
     "blurb": "Everything you weigh that isn't fat, estimated three ways or from your body fat %.",
     "fields": [SEX, HEIGHT, WEIGHT,
                {"name": "bf", "type": "number", "label": "Body fat (optional)", "unit": "%",
                 "optional": True, "min": 3, "max": 60}]},
    {"id": "ffmi", "slug": "ffmi-calculator", "name": "FFMI Calculator", "cat": "body",
     "icon": "bicep", "image": "arms", "popular": True,
     "blurb": "Fat-free mass index: how much muscle you carry for your height, normalised.",
     "fields": [SEX, HEIGHT, WEIGHT,
                {"name": "bf", "type": "number", "label": "Body fat", "unit": "%",
                 "default": 15, "min": 3, "max": 60}]},
    {"id": "whr", "slug": "waist-to-hip-ratio-calculator", "name": "Waist-to-Hip Ratio Calculator",
     "cat": "body", "icon": "ruler", "image": "core",
     "blurb": "Waist-to-hip and waist-to-height ratio, with the WHO risk thresholds.",
     "fields": [SEX,
                {"name": "waist", "type": "length", "label": "Waist", "default": 84},
                {"name": "hip", "type": "length", "label": "Hips", "default": 98},
                dict(HEIGHT, label="Height (optional)", optional=True)]},

    # ---- nutrition --------------------------------------------------------
    {"id": "tdee", "slug": "tdee-calculator", "name": "TDEE Calculator", "cat": "nutrition",
     "icon": "flame", "image": "healthy-meal", "popular": True,
     "blurb": "Total daily energy expenditure: the calories you burn on a normal day.",
     "fields": [SEX, AGE, HEIGHT, WEIGHT, ACT]},
    {"id": "calorie", "slug": "calorie-calculator", "name": "Calorie Calculator", "cat": "nutrition",
     "icon": "apple", "image": "fit-food", "popular": True,
     "blurb": "Daily calories to maintain, lose or gain weight at a pace you choose.",
     "fields": [SEX, AGE, HEIGHT, WEIGHT, ACT]},
    {"id": "macro", "slug": "macro-calculator", "name": "Macro Calculator", "cat": "nutrition",
     "icon": "pie", "image": "meal-prep", "popular": True,
     "blurb": "Protein, carbs and fat in grams for cutting, maintaining or lean bulking.",
     "fields": [SEX, AGE, HEIGHT, WEIGHT, ACT,
                {"name": "goal", "type": "select", "label": "Goal", "default": "cut",
                 "options": [("cut", "Cut: lose fat (-20%)"), ("maintain", "Maintain"),
                             ("bulk", "Lean bulk (+10%)")]},
                {"name": "style", "type": "select", "label": "Diet style", "default": "balanced",
                 "options": [("balanced", "Balanced"), ("lowcarb", "Lower carb"),
                             ("highcarb", "Higher carb (endurance)"), ("keto", "Keto")]}]},
    {"id": "protein", "slug": "protein-calculator", "name": "Protein Calculator", "cat": "nutrition",
     "icon": "egg", "image": "protein-food", "popular": True,
     "blurb": "How many grams of protein a day for your weight and training goal.",
     "fields": [WEIGHT,
                {"name": "goal", "type": "select", "label": "Goal", "default": "muscle",
                 "options": [("sedentary", "General health, not training"),
                             ("active", "Active / general fitness"),
                             ("muscle", "Build muscle"),
                             ("cut", "Lose fat while lifting")]}]},
    {"id": "bmr", "slug": "bmr-calculator", "name": "BMR Calculator", "cat": "nutrition",
     "icon": "bolt", "image": "sleep",
     "blurb": "Basal metabolic rate by Mifflin-St Jeor, Harris-Benedict and Katch-McArdle.",
     "fields": [SEX, AGE, HEIGHT, WEIGHT,
                {"name": "bf", "type": "number", "label": "Body fat (optional)", "unit": "%",
                 "optional": True, "min": 3, "max": 60}]},
    {"id": "weightloss", "slug": "weight-loss-calculator", "name": "Weight Loss Calculator",
     "cat": "nutrition", "icon": "trend", "image": "running",
     "blurb": "Daily calories and a realistic finish date for your goal weight.",
     "fields": [SEX, AGE, HEIGHT, WEIGHT,
                {"name": "goalw", "type": "weight", "label": "Goal weight", "default": 68},
                ACT,
                {"name": "pace", "type": "select", "label": "Pace", "default": "0.5",
                 "options": [("0.25", "Slow: 0.25 kg / 0.5 lb a week"),
                             ("0.5", "Steady: 0.5 kg / 1 lb a week"),
                             ("0.75", "Fast: 0.75 kg / 1.5 lb a week"),
                             ("1", "Aggressive: 1 kg / 2 lb a week")]}]},
    {"id": "water", "slug": "water-intake-calculator", "name": "Water Intake Calculator",
     "cat": "nutrition", "icon": "drop", "image": "water",
     "blurb": "Daily water for your body weight, training and climate.",
     "fields": [WEIGHT,
                {"name": "exercise", "type": "number", "label": "Exercise per day",
                 "unit": "min", "default": 45, "min": 0, "max": 600},
                {"name": "climate", "type": "select", "label": "Climate", "default": "temperate",
                 "options": [("temperate", "Temperate"), ("hot", "Hot or humid")]}]},

    # ---- strength ---------------------------------------------------------
    {"id": "orm", "slug": "one-rep-max-calculator", "name": "One Rep Max Calculator",
     "cat": "strength", "icon": "dumbbell", "image": "deadlift", "popular": True,
     "blurb": "Estimate your 1RM from any set, with a full training percentage chart.",
     "fields": [{"name": "lift", "type": "load", "label": "Weight lifted", "default": 100},
                {"name": "reps", "type": "number", "label": "Reps completed", "default": 5,
                 "min": 1, "max": 12}]},
    {"id": "plate", "slug": "plate-calculator", "name": "Barbell Plate Calculator",
     "cat": "strength", "icon": "plate", "image": "plates",
     "blurb": "Exactly which plates go on each side of the bar, drawn for you.",
     "fields": [{"name": "target", "type": "load", "label": "Target weight", "default": 100},
                {"name": "bar", "type": "select", "label": "Bar", "default": "20",
                 "options": [("20", "20 kg / 45 lb Olympic bar"), ("15", "15 kg / 35 lb women's bar"),
                             ("10", "10 kg / 25 lb technique bar")]},
                {"name": "collars", "type": "select", "label": "Collars", "default": "0",
                 "options": [("0", "Spring clips (no weight)"), ("2.5", "2.5 kg competition collars")]}]},
    {"id": "wilks", "slug": "wilks-calculator", "name": "Wilks & DOTS Calculator",
     "cat": "strength", "icon": "trophy", "image": "chalk",
     "blurb": "Score your powerlifting total against lifters of any body weight.",
     "fields": [SEX, dict(WEIGHT, label="Body weight", default=83),
                {"name": "squat", "type": "load", "label": "Squat", "default": 180},
                {"name": "bench", "type": "load", "label": "Bench press", "default": 120},
                {"name": "deadlift", "type": "load", "label": "Deadlift", "default": 220}]},

    # ---- cardio -----------------------------------------------------------
    {"id": "hr", "slug": "heart-rate-zone-calculator", "name": "Heart Rate Zone Calculator",
     "cat": "cardio", "icon": "heart", "image": "running",
     "blurb": "Your five training zones in beats per minute, by age and resting heart rate.",
     "fields": [AGE,
                {"name": "rhr", "type": "number", "label": "Resting heart rate (optional)",
                 "unit": "bpm", "optional": True, "min": 30, "max": 110},
                {"name": "formula", "type": "select", "label": "Max HR formula", "default": "tanaka",
                 "options": [("tanaka", "Tanaka: 208 - 0.7 x age"), ("fox", "Classic: 220 - age")]}]},
    {"id": "burn", "slug": "calories-burned-calculator", "name": "Calories Burned Calculator",
     "cat": "cardio", "icon": "flame", "image": "battle-ropes",
     "blurb": "Calories burned in 20 gym and cardio activities, from MET values.",
     "fields": [{"name": "act", "type": "select", "label": "Activity", "default": "6.0",
                 "options": [
                     ("3.5", "Weight lifting, general"), ("6.0", "Weight lifting, vigorous"),
                     ("8.0", "Circuit training / HIIT"), ("3.5|w", "Walking, 5 km/h"),
                     ("5.0", "Brisk walking, 6.4 km/h"), ("8.3", "Running, 8 km/h"),
                     ("9.8", "Running, 10 km/h"), ("11.8", "Running, 12 km/h"),
                     ("6.8", "Cycling, 16-19 km/h"), ("8.0|c", "Cycling, 20-22 km/h"),
                     ("5.8", "Swimming, moderate"), ("7.0", "Rowing machine, moderate"),
                     ("5.0|e", "Elliptical, moderate"), ("9.0", "Stair climber"),
                     ("12.3", "Jump rope"), ("2.5", "Yoga"), ("6.0|h", "Hiking"),
                     ("5.0|d", "Dancing"), ("6.5", "Basketball"), ("7.0|f", "Football / soccer")]},
                WEIGHT,
                {"name": "minutes", "type": "number", "label": "Duration", "unit": "min",
                 "default": 45, "min": 1, "max": 600}]},
]

BY_SLUG = {c["slug"]: c for c in CALCS}
BY_ID = {c["id"]: c for c in CALCS}

_CONTENT = dict(calc_content_a.CONTENT, **calc_content_b.CONTENT)
for _c in CALCS:
    _c.update(_CONTENT.get(_c["slug"], {}))
    _c.setdefault("title", _c["name"])
    _c.setdefault("desc", _c["blurb"])
    _c.setdefault("intro", _c["blurb"])
    _c.setdefault("body", [])
    _c.setdefault("faq", [])
    _c.setdefault("sources", [])
    _c["units"] = any(f["type"] in ("height", "weight", "load", "length") for f in _c["fields"])


def by_cat(cat):
    return [c for c in CALCS if c["cat"] == cat]
