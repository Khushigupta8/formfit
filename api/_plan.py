"""
FormFit Pro plan generator: calories, macros, a 7-day Indian meal plan and a
weekly training split, built from the person's own numbers.

It runs only on the server (api/plan.py) so the generator itself stays a Pro
feature. Food values are per listed portion and approximate; they're meant
for planning, not for medical diets.
"""

import re

ACTIVITY = {
    "sedentary": (1.2, "Desk job, little exercise"),
    "light": (1.375, "Training 1-3 days a week"),
    "moderate": (1.55, "Training 3-5 days a week"),
    "active": (1.725, "Training 6-7 days a week"),
    "very": (1.9, "Physical job plus training"),
}
GOALS = {"lose": "Lose fat", "maintain": "Maintain / recomp", "gain": "Build muscle"}
DIETS = {"veg": "Vegetarian", "egg": "Eggetarian", "nonveg": "Non-vegetarian"}

# ---------------------------------------------------------------------------
# Meals. items: (amount, unit, food). unit "" = a count (rounded to whole
# numbers when scaled), "g"/"ml" round to 10, "each"/"bowl" never scale. kcal and protein (p) are for
# the portion as written. diet: the least strict diet the meal fits.
# ---------------------------------------------------------------------------

def M(name, diet, kcal, p, items):
    return {"name": name, "diet": diet, "kcal": kcal, "p": p, "items": items}


BREAKFAST = [
    M("Moong dal chilla with curd", "veg", 340, 20, [(60, "g", "moong dal, made into chillas"), (100, "g", "curd")]),
    M("Paneer paratha with curd", "veg", 430, 20, [(1, "", "paneer paratha (40 g paneer)"), (150, "g", "curd")]),
    M("Masala oats with milk and banana", "veg", 470, 18, [(50, "g", "oats, cooked in milk"), (250, "ml", "milk"), (1, "each", "banana"), (15, "g", "almonds")]),
    M("Besan chilla stuffed with paneer", "veg", 390, 21, [(60, "g", "besan, made into chillas"), (50, "g", "paneer")]),
    M("Idli sambar", "veg", 380, 14, [(4, "", "idlis"), (200, "ml", "sambar")]),
    M("Poha with peanuts and curd", "veg", 450, 16, [(70, "g", "poha (dry)"), (20, "g", "peanuts"), (150, "g", "curd")]),
    M("Sprouts salad with a glass of milk", "veg", 330, 20, [(150, "g", "moong sprouts salad"), (250, "ml", "milk")]),
    M("Three-egg omelette with toast", "egg", 380, 24, [(3, "", "eggs, as an omelette"), (2, "", "slices wholewheat toast")]),
    M("Egg bhurji, roti and milk", "egg", 470, 28, [(3, "", "eggs, as bhurji"), (1, "", "roti"), (200, "ml", "milk")]),
]

LUNCH = [
    M("Rajma chawal with salad", "veg", 460, 16, [(150, "g", "rajma (cooked)"), (150, "g", "rice (cooked)"), (1, "bowl", "cucumber-onion salad")]),
    M("Chole with roti", "veg", 480, 18, [(150, "g", "chole (cooked)"), (2, "", "rotis")]),
    M("Dal, paneer sabzi and roti", "veg", 620, 30, [(150, "g", "dal"), (100, "g", "paneer sabzi"), (2, "", "rotis")]),
    M("Soya chunk curry with rice", "veg", 450, 28, [(40, "g", "soya chunks (dry)"), (150, "g", "rice (cooked)")]),
    M("Kadhi chawal with chana salad", "veg", 500, 19, [(200, "ml", "kadhi"), (150, "g", "rice (cooked)"), (80, "g", "boiled chana")]),
    M("Egg curry with roti", "egg", 520, 24, [(3, "", "eggs, in curry"), (2, "", "rotis")]),
    M("Chicken curry with rice and salad", "nonveg", 560, 40, [(150, "g", "chicken (cooked)"), (150, "g", "rice (cooked)"), (1, "bowl", "salad")]),
    M("Fish curry with rice", "nonveg", 480, 34, [(150, "g", "fish (cooked)"), (150, "g", "rice (cooked)")]),
]

SNACK = [
    M("Roasted chana and buttermilk", "veg", 200, 10, [(40, "g", "roasted chana"), (250, "ml", "buttermilk")]),
    M("Hung curd with fruit", "veg", 190, 14, [(150, "g", "hung curd / Greek yoghurt"), (1, "each", "seasonal fruit")]),
    M("Paneer tikka", "veg", 230, 15, [(80, "g", "paneer, grilled")]),
    M("Sprouts chaat", "veg", 160, 9, [(120, "g", "sprouts chaat")]),
    M("Fruit and almonds", "veg", 220, 6, [(1, "each", "apple or banana"), (20, "g", "almonds")]),
    M("Boiled eggs", "egg", 160, 13, [(2, "", "boiled eggs")]),
    M("Chicken tikka", "nonveg", 180, 28, [(100, "g", "chicken tikka")]),
]

DINNER = [
    M("Palak paneer with roti", "veg", 520, 24, [(150, "g", "palak paneer"), (2, "", "rotis")]),
    M("Dal, mixed veg and roti", "veg", 450, 18, [(150, "g", "dal"), (150, "g", "mixed veg sabzi"), (2, "", "rotis")]),
    M("Soya keema with roti", "veg", 430, 30, [(40, "g", "soya granules (dry)"), (2, "", "rotis")]),
    M("Moong dal khichdi with curd", "veg", 440, 20, [(80, "g", "rice + moong dal (dry)"), (150, "g", "curd")]),
    M("Paneer bhurji with roti", "veg", 560, 28, [(120, "g", "paneer, as bhurji"), (2, "", "rotis")]),
    M("Egg bhurji with roti", "egg", 440, 24, [(3, "", "eggs, as bhurji"), (2, "", "rotis")]),
    M("Grilled chicken, veg and roti", "nonveg", 520, 48, [(150, "g", "chicken breast, grilled"), (150, "g", "sauteed veg"), (2, "", "rotis")]),
    M("Fish tikka with salad and roti", "nonveg", 380, 38, [(150, "g", "fish tikka"), (1, "bowl", "salad"), (1, "", "roti")]),
]

ALLOWED = {"veg": {"veg"}, "egg": {"veg", "egg"}, "nonveg": {"veg", "egg", "nonveg"}}
SPLIT = (("Breakfast", BREAKFAST, .25), ("Lunch", LUNCH, .32),
         ("Snack", SNACK, .13), ("Dinner", DINNER, .30))
TOP_UP = {"veg": "1 scoop whey (24 g), 150 g hung curd (15 g) or 100 g paneer (18 g)",
          "egg": "1 scoop whey (24 g), 4 egg whites (14 g) or 150 g hung curd (15 g)",
          "nonveg": "1 scoop whey (24 g), 100 g chicken breast (31 g) or 4 egg whites (14 g)"}


def _pool(meals, diet):
    """Meals this diet can eat, the diet's own dishes first so they come up
    more often, then the rest, interleaved."""
    ok = [m for m in meals if m["diet"] in ALLOWED[diet]]
    own = [m for m in ok if m["diet"] == diet]
    other = [m for m in ok if m["diet"] != diet]
    out = []
    while own or other:
        if own:
            out.append(own.pop(0))
        if other:
            out.append(other.pop(0))
    return out


def _amount(a, unit, f):
    """Scaled portion: whole counts for rotis and eggs, 10 g / 10 ml steps."""
    if unit == "each":
        return str(a)
    if unit == "bowl":
        return "{} bowl".format(a)
    if unit == "":
        return str(max(1, int(round(a * f))))
    return "{} {}".format(max(10, int(round(a * f / 10)) * 10), unit)


PLURALS = re.compile(r"\b(rotis|idlis|eggs|slices)\b")


def _item(a, unit, f, food):
    n = _amount(a, unit, f)
    if n == "1":
        food = PLURALS.sub(lambda m: m.group(1)[:-1], food)
    return "{} {}".format(n, food)


def _scaled(meal, target):
    f = min(2.2, max(.6, target / meal["kcal"]))
    f = round(f * 4) / 4                  # quarter steps keep portions sane
    return {
        "name": meal["name"],
        "kcal": int(round(meal["kcal"] * f)),
        "protein": int(round(meal["p"] * f)),
        "items": [_item(a, u, f, food) for a, u, food in meal["items"]],
    }


def meal_plan(kcal, protein, diet):
    pools = [(slot, _pool(meals, diet), share) for slot, meals, share in SPLIT]
    days = []
    for d in range(7):
        meals = []
        for i, (slot, pool, share) in enumerate(pools):
            m = _scaled(pool[(d + i) % len(pool)], kcal * share)
            m["slot"] = slot
            meals.append(m)
        total_k = sum(m["kcal"] for m in meals)
        total_p = sum(m["protein"] for m in meals)
        day = {"day": "Day {}".format(d + 1), "meals": meals,
               "kcal": total_k, "protein": total_p, "top_up": None}
        short = protein - total_p
        if short >= 12:
            day["top_up"] = "Add about {} g protein, e.g. {}.".format(int(round(short / 5.0)) * 5, TOP_UP[diet])
        days.append(day)
    return days


# ---------------------------------------------------------------------------
# Training. Each row: [name, sets, reps, rest, exercise slug or None]
# ---------------------------------------------------------------------------

GYM = {
    "squat": ["Barbell back squat", "8", "2-3 min", "barbell-back-squat"],
    "hinge": ["Romanian deadlift", "10", "2 min", "romanian-deadlift"],
    "deadlift": ["Deadlift", "5", "3 min", "deadlift"],
    "legpress": ["Leg press", "12", "90 sec", "leg-press"],
    "lunge": ["Walking lunge", "10 per leg", "90 sec", "walking-lunge"],
    "glute": ["Hip thrust", "10", "90 sec", "hip-thrust"],
    "hpush": ["Bench press", "8", "2-3 min", "bench-press"],
    "ipush": ["Incline dumbbell press", "10", "90 sec", "incline-dumbbell-press"],
    "vpush": ["Overhead press", "8", "2 min", "overhead-press"],
    "hpull": ["Barbell row", "8", "2 min", "barbell-row"],
    "vpull": ["Lat pulldown", "10", "90 sec", "lat-pulldown"],
    "chin": ["Pull-up (or assisted)", "6-8", "2 min", "pull-up"],
    "bi": ["Dumbbell curl", "12", "60 sec", "dumbbell-curl"],
    "tri": ["Tricep dip (or bench dip)", "10", "60 sec", "tricep-dip"],
    "core": ["Plank", "40 sec", "60 sec", "plank"],
}
HOME = {
    "squat": ["Goblet squat (backpack or dumbbell)", "12-15", "90 sec", None],
    "hinge": ["Single-leg Romanian deadlift", "10 per leg", "60 sec", None],
    "deadlift": ["Backpack deadlift", "12", "90 sec", None],
    "legpress": ["Bulgarian split squat", "10 per leg", "90 sec", None],
    "lunge": ["Walking lunge", "12 per leg", "60 sec", "walking-lunge"],
    "glute": ["Glute bridge (single-leg when easy)", "15", "60 sec", "hip-thrust"],
    "hpush": ["Push-up", "As many as possible", "90 sec", "push-up"],
    "ipush": ["Feet-elevated push-up", "8-12", "90 sec", "push-up"],
    "vpush": ["Pike push-up", "8-10", "90 sec", None],
    "hpull": ["Table or towel row", "10-12", "90 sec", None],
    "vpull": ["Doorway or towel row", "12", "60 sec", None],
    "chin": ["Pull-up (bar) or backpack row", "6-10", "2 min", "pull-up"],
    "bi": ["Backpack curl", "15", "60 sec", None],
    "tri": ["Chair dip", "10-15", "60 sec", "tricep-dip"],
    "core": ["Plank", "40 sec", "60 sec", "plank"],
}

DAYS = {
    3: [("Full body A", ["squat", "hpush", "vpull", "hinge", "bi", "core"]),
        ("Full body B", ["deadlift", "vpush", "hpull", "lunge", "tri"]),
        ("Full body C", ["legpress", "ipush", "chin", "glute", "core"])],
    4: [("Upper A", ["hpush", "hpull", "vpush", "vpull", "bi", "tri"]),
        ("Lower A", ["squat", "hinge", "lunge", "core"]),
        ("Upper B", ["vpush", "chin", "ipush", "hpull", "tri"]),
        ("Lower B", ["deadlift", "legpress", "glute", "core"])],
    5: [("Upper", ["hpush", "hpull", "vpush", "vpull", "bi"]),
        ("Lower", ["squat", "hinge", "lunge", "core"]),
        ("Push", ["vpush", "ipush", "hpush", "tri"]),
        ("Pull", ["chin", "hpull", "vpull", "bi"]),
        ("Legs", ["deadlift", "legpress", "glute", "core"])],
    6: [("Push A", ["hpush", "vpush", "ipush", "tri"]),
        ("Pull A", ["deadlift", "vpull", "hpull", "bi"]),
        ("Legs A", ["squat", "hinge", "lunge", "core"]),
        ("Push B", ["vpush", "ipush", "hpush", "tri"]),
        ("Pull B", ["chin", "hpull", "vpull", "bi"]),
        ("Legs B", ["legpress", "glute", "lunge", "core"])],
}
WEEK = {3: [1, 0, 1, 0, 1, 0, 0], 4: [1, 1, 0, 1, 1, 0, 0],
        5: [1, 1, 0, 1, 1, 1, 0], 6: [1, 1, 1, 1, 1, 1, 0]}
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def training(days, place, level, goal):
    lib = HOME if place == "home" else GYM
    sets = "3" if level == "beginner" else "4"
    sessions = iter(DAYS[days])
    week = []
    for name, on in zip(WEEKDAYS, WEEK[days]):
        if on:
            title, moves = next(sessions)
            rows = []
            for k in moves:
                n, reps, rest, slug = lib[k]
                s = "2" if k in ("bi", "tri") and level == "beginner" else sets
                rows.append([n, "3" if k == "core" else s, reps, rest, slug])
            focus = title
            if goal == "lose":
                focus += " + 10 min incline walk to finish"
            week.append({"day": name, "title": title, "focus": focus, "exercises": rows})
        else:
            rest = "Rest: 8,000-10,000 steps" if goal == "lose" else "Rest or an easy walk"
            week.append({"day": name, "title": "Rest", "focus": rest, "exercises": []})
    return week


# ---------------------------------------------------------------------------

def validate(d):
    def num(k, lo, hi):
        try:
            v = float(d.get(k))
        except (TypeError, ValueError):
            raise ValueError(k)
        if not lo <= v <= hi:
            raise ValueError(k)
        return v

    errors = {}
    out = {}
    for k, lo, hi in (("age", 16, 80), ("height", 130, 220), ("weight", 35, 200)):
        try:
            out[k] = num(k, lo, hi)
        except ValueError:
            errors[k] = "Enter a value between {} and {}.".format(lo, hi)
    out["sex"] = "f" if d.get("sex") == "f" else "m"
    out["activity"] = d.get("activity") if d.get("activity") in ACTIVITY else "moderate"
    out["goal"] = d.get("goal") if d.get("goal") in GOALS else "maintain"
    out["diet"] = d.get("diet") if d.get("diet") in DIETS else "veg"
    out["place"] = "home" if d.get("place") == "home" else "gym"
    out["level"] = "intermediate" if d.get("level") == "intermediate" else "beginner"
    try:
        out["days"] = int(d.get("days"))
    except (TypeError, ValueError):
        out["days"] = 3
    out["days"] = min(6, max(3, out["days"]))
    return out, errors


def generate(x):
    w, h, a = x["weight"], x["height"], x["age"]
    bmr = 10 * w + 6.25 * h - 5 * a + (5 if x["sex"] == "m" else -161)
    tdee = bmr * ACTIVITY[x["activity"]][0]
    floor = 1500 if x["sex"] == "m" else 1200
    target = {"lose": tdee * .8, "maintain": tdee, "gain": tdee * 1.1}[x["goal"]]
    target = int(round(max(target, floor) / 10) * 10)

    # Protein on a reference weight (BMI 25 at most) so it stays sensible
    # for heavier people.
    ref = min(w, 25 * (h / 100) ** 2)
    per_kg = {"lose": 1.8, "maintain": 1.6, "gain": 1.7}[x["goal"]]
    protein = int(round(ref * per_kg))
    fat = int(round(target * .25 / 9))
    carbs = max(0, int(round((target - protein * 4 - fat * 9) / 4)))
    weekly = {"lose": "about 0.5-0.8% of body weight a week",
              "maintain": "steady weight; waist and strength tell you it's working",
              "gain": "about 0.25-0.5% of body weight a week"}[x["goal"]]

    return {
        "inputs": x,
        "summary": {
            "goal": GOALS[x["goal"]], "diet": DIETS[x["diet"]],
            "bmr": int(round(bmr)), "tdee": int(round(tdee)),
            "calories": target, "protein": protein, "carbs": carbs, "fat": fat,
            "water_l": round(w * .035, 1), "expect": weekly,
        },
        "meals": meal_plan(target, protein, x["diet"]),
        "training": training(x["days"], x["place"], x["level"], x["goal"]),
        "rules": [
            "Weigh yourself 3-4 mornings a week and compare weekly averages, not single days.",
            "Add a rep each session; when you hit the top of the rep range on every set, add 2.5 kg (or a harder variation at home).",
            "If the weekly average hasn't moved in 2-3 weeks, change calories by about 150 kcal a day.",
            "Sleep 7-9 hours. It matters as much as the plan.",
        ],
    }
