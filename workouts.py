"""
Workout plans. Each dict becomes a page at /workouts/<slug>.

The schedule is rendered as a table per training day. Each exercise row is
[name, sets, reps, rest, exercise_slug_or_None]; a slug links the row to its
page in the exercise library. Body sections use the shared block format
described in the content spec (paragraphs, lists, tables, tips, formulas).
"""

WORKOUTS = [
    # -----------------------------------------------------------------------
    {
        "slug": "beginner-full-body-workout",
        "name": "Beginner Full Body Workout",
        "title": "Beginner Full Body Workout: 3-Day Gym Plan",
        "desc": ("A 3-day full body gym plan for beginners. Learn the big lifts, "
                 "add weight every week and build a solid base of strength and "
                 "muscle in 12 weeks."),
        "level": "Beginner",
        "days": 3,
        "weeks": 12,
        "goal": "General fitness",
        "equipment": "Full gym",
        "session": "45-60 min",
        "image": "gym-floor",
        "intro": ("Three sessions a week, every major muscle trained each time, "
                  "and a simple rule for adding weight. This is the plan to run "
                  "for your first three months in the gym, before you need "
                  "anything more complicated."),
        "schedule": [
            {"day": "Day 1 - Full body A", "focus": "Squat, push, pull",
             "exercises": [
                 ["Barbell back squat", "3", "8", "2-3 min", "barbell-back-squat"],
                 ["Bench press", "3", "8", "2-3 min", "bench-press"],
                 ["Lat pulldown", "3", "10", "90 sec", "lat-pulldown"],
                 ["Romanian deadlift", "2", "10", "2 min", "romanian-deadlift"],
                 ["Dumbbell curl", "2", "12", "60 sec", "dumbbell-curl"],
                 ["Plank", "3", "30 sec", "60 sec", "plank"],
             ]},
            {"day": "Day 2 - Rest", "focus": "Rest or light walking", "exercises": []},
            {"day": "Day 3 - Full body B", "focus": "Hinge, press, row",
             "exercises": [
                 ["Deadlift", "3", "5", "3 min", "deadlift"],
                 ["Overhead press", "3", "8", "2 min", "overhead-press"],
                 ["Barbell row", "3", "8", "2 min", "barbell-row"],
                 ["Walking lunge", "2", "10 per leg", "90 sec", "walking-lunge"],
                 ["Push-up", "2", "As many as possible", "90 sec", "push-up"],
             ]},
            {"day": "Day 4 - Rest", "focus": "Rest or light walking", "exercises": []},
            {"day": "Day 5 - Full body C", "focus": "Legs, upper chest, back",
             "exercises": [
                 ["Leg press", "3", "10", "2 min", "leg-press"],
                 ["Incline dumbbell press", "3", "10", "90 sec", "incline-dumbbell-press"],
                 ["Pull-up (or assisted)", "3", "5-8", "2 min", "pull-up"],
                 ["Hip thrust", "3", "10", "90 sec", "hip-thrust"],
                 ["Tricep dip (or bench dip)", "2", "8-12", "60 sec", "tricep-dip"],
             ]},
            {"day": "Days 6-7 - Rest", "focus": "Rest, walk, stretch", "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This plan is for anyone with less than about six months of "
                "consistent lifting. That includes complete beginners, people "
                "coming back after a long break, and anyone who has trained for "
                "years without a plan and never really learned the barbell lifts.",
                "Full body training suits beginners for a simple reason: you get "
                "better at a movement by practising it often. Squatting, pressing "
                "and pulling three times a week gives you three chances to "
                "groove the technique, and each muscle gets a growth signal "
                "every 48 hours or so instead of once a week.",
                "Three sessions also fits into real life. Monday, Wednesday and "
                "Friday is the classic layout, but any three non-consecutive "
                "days work. If you miss a session, do it the next day and carry "
                "on. Do not try to cram two sessions into one.",
            ]),
            ("How to progress week to week", [
                "Progress is the whole point of a plan. The method here is "
                "called double progression, and it is the simplest system that "
                "actually works.",
                {"olist": [
                    "Each exercise has a target number of reps, for example 3 sets of 8.",
                    "Start with a weight you can lift for all sets with two or three "
                    "reps left in the tank.",
                    "When you hit every rep of every set with good form, add weight "
                    "next session: 2.5 kg (5 lb) on upper body lifts, 5 kg (10 lb) "
                    "on squats and deadlifts.",
                    "If you miss reps, keep the same weight and try again next time.",
                    "If you fail the same weight three sessions in a row, drop it "
                    "by 10% and build back up.",
                ]},
                "On small exercises such as curls, lunges and dips, add reps "
                "before weight. Work from the bottom of the rep range to the top "
                "(for example 10 up to 15), then add the smallest weight jump "
                "available and start again at 10.",
                "Expect to add weight to most lifts most weeks for the first two "
                "months. That pace slows naturally. When jumps stall even after "
                "a reset, you have earned an intermediate plan such as the "
                "<a href=\"/workouts/upper-lower-split\">upper/lower split</a>.",
                {"tip": "Write every set down. A notebook or phone note with the "
                        "date, weight and reps is the single best predictor of "
                        "whether a beginner keeps progressing."},
            ]),
            ("Warm-up", [
                "Spend 8 to 10 minutes warming up. You are not trying to get "
                "tired, only warm and practised.",
                {"list": [
                    "3 to 5 minutes of easy cardio: bike, rower or brisk incline walk.",
                    "A few bodyweight squats, lunges and arm circles.",
                    "Ramp-up sets on the first lift: the empty bar for 10 reps, then "
                    "about 50% of your work weight for 5, then about 75% for 3, "
                    "then start your work sets.",
                ]},
                "Later exercises in the session need only one light set, since "
                "your body is already warm by then.",
            ]),
            ("How to pick your starting weights", [
                "Start lighter than your ego wants. A first week that feels too "
                "easy is perfect, because it leaves room to add weight for "
                "weeks before you stall.",
                "If you have never lifted, begin with the empty barbell (usually "
                "20 kg / 45 lb) on squats, bench and overhead press, and a light "
                "dumbbell or machine weight elsewhere. Your first few sessions "
                "are for learning the movement patterns on the "
                "<a href=\"/exercises/barbell-back-squat\">squat</a> and "
                "<a href=\"/exercises/deadlift\">deadlift</a>.",
                "If you have some experience, do a set of 5 to 8 with a "
                "challenging weight, plug it into the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a>, "
                "and start your work sets at around 65 to 70% of the estimate. "
                "Loading a bar to an exact weight is easy with the "
                "<a href=\"/plate-calculator\">plate calculator</a>.",
            ]),
            ("Eating to support the plan", [
                "Beginners can build muscle and lose some fat at the same time, "
                "but only if they eat enough protein. Aim for roughly 1.6 to "
                "2.2 g of protein per kg of bodyweight (0.7 to 1 g per lb). The "
                "<a href=\"/protein-calculator\">protein calculator</a> gives "
                "you a daily target.",
                "Calories depend on your goal. To gain muscle as fast as "
                "possible, eat a small surplus of 200 to 300 kcal above "
                "maintenance. To lose fat while learning to lift, eat 300 to "
                "500 kcal below. Find your maintenance number with the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a>.",
                "Sleep matters as much as food. Seven to nine hours is where "
                "recovery and strength gains happen; see "
                "<a href=\"/guides/sleep-and-muscle-growth\">sleep and muscle growth</a>.",
            ]),
            ("When to take a deload", [
                "Most beginners do not need a planned deload in the first eight "
                "weeks. The weights are light enough that recovery keeps up.",
                "From week 8 onward, take an easier week if your joints ache, "
                "your sleep gets worse or several lifts stall at once. Keep the "
                "same exercises, use about 60% of your normal weights and cut "
                "the sets in half. Then pick up where you left off.",
            ]),
            ("Exercise swaps", [
                "If equipment is busy or a movement does not suit you, swap it "
                "for something that trains the same pattern:",
                {"table": {"head": ["Planned exercise", "Good swap"], "rows": [
                    ["Barbell back squat", "Goblet squat or leg press"],
                    ["Bench press", "Dumbbell bench press or push-ups"],
                    ["Deadlift", "Trap bar deadlift or Romanian deadlift"],
                    ["Pull-up", "Lat pulldown or assisted pull-up machine"],
                    ["Barbell row", "Seated cable row or one-arm dumbbell row"],
                    ["Overhead press", "Seated dumbbell shoulder press"],
                ]}},
                "Keep the swap for at least four weeks so you can track progress "
                "on it. New to the gym in general? Read the "
                "<a href=\"/guides/beginner-gym-guide\">beginner gym guide</a> first.",
            ]),
            ("Common beginner mistakes", [
                "Most beginners who stall in the first three months make one of "
                "a handful of predictable errors. Avoid these and the plan will "
                "carry you a long way.",
                {"list": [
                    "<strong>Program hopping.</strong> Switching plans every two "
                    "weeks resets progress. Give this one at least 12 weeks.",
                    "<strong>Adding weight with worse form.</strong> A rep only "
                    "counts if it looks like the last one. Shorter range of "
                    "motion is not progress.",
                    "<strong>Skipping the legs.</strong> Squats, deadlifts and "
                    "lunges train the largest muscles you have and drive most of "
                    "your strength gains.",
                    "<strong>Resting too little.</strong> Two to three minutes "
                    "between heavy sets is normal. Rushing makes later sets weaker.",
                    "<strong>Undereating protein.</strong> Training without "
                    "enough protein leaves muscle on the table.",
                ]},
                "Film a set from the side every couple of weeks. Comparing "
                "videos with the technique notes on each exercise page, such as "
                "the <a href=\"/exercises/bench-press\">bench press</a>, is the "
                "fastest way to fix form without a coach.",
            ]),
        ],
        "faq": [
            ("How long should I run a beginner full body plan?",
             "Run it for as long as you can keep adding weight, which for most "
             "people is three to six months. Move to a split when progress "
             "stalls even after resetting the weights."),
            ("Can I add extra exercises?",
             "You can add a couple of sets of arm or calf work at the end, but "
             "resist adding more. Beginners progress fastest on a short list of "
             "big lifts done well, and extra volume mostly adds fatigue."),
            ("Is 3 days a week enough to build muscle?",
             "Yes. Training each muscle three times a week with a few hard sets "
             "is plenty for a beginner. Consistency over months matters far more "
             "than the number of days."),
            ("What if I cannot do a pull-up yet?",
             "Use an assisted pull-up machine, a resistance band or the lat "
             "pulldown. Add slow negatives, lowering yourself from the top for "
             "three to five seconds, to build toward your first full rep."),
        ],
        "related_calcs": ["one-rep-max-calculator", "protein-calculator", "tdee-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "push-pull-legs",
        "name": "Push Pull Legs Split",
        "title": "Push Pull Legs Workout: 6-Day PPL Routine",
        "desc": ("A 6-day push pull legs routine for building muscle. Full "
                 "schedule with sets, reps and rest times, plus how to progress, "
                 "deload and adjust it."),
        "level": "Intermediate",
        "days": 6,
        "weeks": 8,
        "goal": "Muscle gain",
        "equipment": "Full gym",
        "session": "60-75 min",
        "image": "dumbbells",
        "intro": ("Push pull legs splits your training by movement: pressing "
                  "muscles one day, pulling muscles the next, then legs. Run it "
                  "twice a week and every muscle gets hit twice with plenty of "
                  "volume, which makes it one of the most popular hypertrophy "
                  "routines for good reason."),
        "schedule": [
            {"day": "Day 1 - Push (heavy)", "focus": "Chest, shoulders, triceps",
             "exercises": [
                 ["Bench press", "4", "5-8", "2-3 min", "bench-press"],
                 ["Overhead press", "3", "6-10", "2 min", "overhead-press"],
                 ["Incline dumbbell press", "3", "8-12", "90 sec", "incline-dumbbell-press"],
                 ["Cable lateral raise", "3", "12-15", "60 sec", None],
                 ["Tricep dip", "3", "8-12", "90 sec", "tricep-dip"],
                 ["Overhead cable tricep extension", "2", "10-15", "60 sec", None],
             ]},
            {"day": "Day 2 - Pull (heavy)", "focus": "Back, rear delts, biceps",
             "exercises": [
                 ["Deadlift", "3", "4-6", "3 min", "deadlift"],
                 ["Pull-up", "3", "6-10", "2 min", "pull-up"],
                 ["Barbell row", "3", "8-10", "2 min", "barbell-row"],
                 ["Face pull", "3", "12-15", "60 sec", None],
                 ["Dumbbell curl", "3", "8-12", "60 sec", "dumbbell-curl"],
                 ["Hammer curl", "2", "10-15", "60 sec", None],
             ]},
            {"day": "Day 3 - Legs (heavy)", "focus": "Quads, hamstrings, glutes, calves",
             "exercises": [
                 ["Barbell back squat", "4", "5-8", "2-3 min", "barbell-back-squat"],
                 ["Romanian deadlift", "3", "8-10", "2 min", "romanian-deadlift"],
                 ["Leg press", "3", "10-12", "2 min", "leg-press"],
                 ["Lying leg curl", "3", "10-15", "60 sec", None],
                 ["Standing calf raise", "4", "8-12", "60 sec", None],
             ]},
            {"day": "Day 4 - Push (volume)", "focus": "Chest, shoulders, triceps",
             "exercises": [
                 ["Incline dumbbell press", "4", "8-12", "90 sec", "incline-dumbbell-press"],
                 ["Seated dumbbell shoulder press", "3", "8-12", "90 sec", None],
                 ["Cable fly", "3", "12-15", "60 sec", None],
                 ["Dumbbell lateral raise", "4", "12-20", "60 sec", None],
                 ["Push-up", "2", "As many as possible", "60 sec", "push-up"],
                 ["Tricep rope pushdown", "3", "10-15", "60 sec", None],
             ]},
            {"day": "Day 5 - Pull (volume)", "focus": "Back, rear delts, biceps",
             "exercises": [
                 ["Lat pulldown", "4", "8-12", "90 sec", "lat-pulldown"],
                 ["Seated cable row", "3", "10-12", "90 sec", None],
                 ["One-arm dumbbell row", "3", "10-12", "60 sec", None],
                 ["Reverse pec deck", "3", "12-20", "60 sec", None],
                 ["Incline dumbbell curl", "3", "10-15", "60 sec", None],
             ]},
            {"day": "Day 6 - Legs (volume)", "focus": "Glutes, quads, hamstrings",
             "exercises": [
                 ["Hip thrust", "4", "8-12", "90 sec", "hip-thrust"],
                 ["Walking lunge", "3", "10-12 per leg", "90 sec", "walking-lunge"],
                 ["Leg extension", "3", "12-15", "60 sec", None],
                 ["Seated leg curl", "3", "10-15", "60 sec", None],
                 ["Seated calf raise", "3", "12-20", "60 sec", None],
                 ["Plank", "3", "45 sec", "60 sec", "plank"],
             ]},
            {"day": "Day 7 - Rest", "focus": "Full rest", "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This routine is for lifters with at least six months of "
                "consistent training who can perform the main barbell lifts "
                "with solid technique. If you are still adding weight every "
                "session on a beginner plan, stay there; this split trades fast "
                "linear progress for more volume per muscle.",
                "It also demands time. Six sessions of an hour or more is a "
                "serious commitment. If you can reliably train only four days, "
                "the <a href=\"/workouts/upper-lower-split\">upper/lower split</a> "
                "will give you better results than a PPL you keep skipping.",
                "A useful middle ground is running the six days as a rolling "
                "cycle: push, pull, legs, rest, repeat. That gives you roughly "
                "five sessions a week and an extra recovery day.",
            ]),
            ("How the heavy and volume days work", [
                "Days 1 to 3 are built around compound lifts in lower rep ranges, "
                "where the goal is to push strength. Days 4 to 6 use more "
                "dumbbell, cable and machine work in higher rep ranges, where the "
                "goal is to accumulate quality volume without beating up joints.",
                "Both styles build muscle. Research reviews, such as Schoenfeld "
                "and colleagues' work on loading ranges, consistently find similar "
                "hypertrophy across a wide rep range as long as sets are taken "
                "close to failure. Mixing them gives you strength and size, and "
                "keeps training from getting stale. More on this in "
                "<a href=\"/guides/how-many-sets-and-reps-for-muscle-growth\">"
                "how many sets and reps for muscle growth</a>.",
            ]),
            ("How to progress week to week", [
                "Use double progression on every exercise. Each one has a rep "
                "range, for example 8 to 12.",
                {"olist": [
                    "Pick a weight you can lift for the bottom of the range on all sets.",
                    "Each session, try to add a rep or two to at least one set.",
                    "Once every set hits the top of the range, increase the weight "
                    "by the smallest available jump and drop back to the bottom.",
                ]},
                "Most sets should finish with one to three reps in reserve, "
                "meaning you could have done one to three more with good form. "
                "Take the last set of isolation exercises such as lateral raises "
                "and curls to technical failure if you like, but avoid true "
                "failure on squats and deadlifts, where form breaks down first.",
                "Over an 8-week block, you should see your logbook numbers creep "
                "up across most lifts. If a lift has not moved in three weeks, "
                "swap it for a close variation for the next block.",
                {"tip": "Progress in total reps counts too. Going from 3 sets of "
                        "8 to 3 sets of 10 at the same weight is a real gain."},
            ]),
            ("Warm-up", [
                "Warm up for 5 to 10 minutes before each session:",
                {"list": [
                    "Light cardio until you break a mild sweat.",
                    "Push days: band pull-aparts, arm circles and a few push-ups.",
                    "Pull days: dead hangs, scapular pull-ups and light rows.",
                    "Leg days: bodyweight squats, hip swings and glute bridges.",
                    "Two to four ramp-up sets on the first compound lift, building "
                    "from the empty bar to your first working weight.",
                ]},
            ]),
            ("How to pick weights", [
                "For the heavy compound lifts, start with a load around 75 to 80% "
                "of your one rep max. If you do not know your max, take a recent "
                "hard set and run it through the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a>; "
                "it estimates your max and prints a percentage table you can work "
                "from.",
                "For accessories, choose by feel. The right weight lets you hit "
                "the bottom of the rep range with clean form and leaves you "
                "unable to do more than two or three extra reps.",
            ]),
            ("Nutrition to support the split", [
                "Six days of high-volume training burns a lot of energy, so it "
                "pairs best with a small calorie surplus if muscle gain is the "
                "goal. Estimate maintenance with the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a> and add 200 to "
                "400 kcal. A gain of about 0.25 to 0.5% of bodyweight per week is "
                "a good pace for most intermediates.",
                "Set protein at around 1.6 to 2.2 g per kg of bodyweight with the "
                "<a href=\"/protein-calculator\">protein calculator</a>, and use "
                "the <a href=\"/macro-calculator\">macro calculator</a> to split "
                "the rest between carbs and fat. Carbohydrates fuel high-volume "
                "sessions, so do not cut them too low. If you are deciding "
                "between gaining and leaning out first, read "
                "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting</a>.",
            ]),
            ("Deloads and swaps", [
                "After every 6 to 8 weeks, take a deload week: same exercises, "
                "half the sets, and stop each set four or more reps short of "
                "failure. Take one sooner if joints ache or performance drops two "
                "sessions in a row. See "
                "<a href=\"/guides/rest-days-and-recovery\">rest days and recovery</a> "
                "for the signs.",
                "Swap freely within a movement pattern: dumbbell bench for "
                "barbell bench, hack squat for back squat, chest-supported row "
                "for barbell row. Keep a swap for a full block so your progress "
                "stays measurable.",
            ]),
            ("Common mistakes on a PPL split", [
                "Push pull legs is easy to run badly. The usual problems are "
                "too much volume and too little effort, in that order.",
                {"list": [
                    "<strong>Adding exercises.</strong> Six sessions already "
                    "give each muscle 10 to 20 hard sets a week. More is rarely "
                    "better and often worse.",
                    "<strong>Junk sets.</strong> Sets that stop five or more reps "
                    "short of failure do little. Make each listed set count.",
                    "<strong>Skipping leg days.</strong> Two leg sessions a week "
                    "are what make this a complete program.",
                    "<strong>Ignoring sleep.</strong> Six training days demand "
                    "seven to nine hours a night; see "
                    "<a href=\"/guides/sleep-and-muscle-growth\">sleep and muscle growth</a>.",
                ]},
                "If you find yourself dreading sessions or missing lifts across "
                "the board, drop to the rolling five-day version for a few weeks "
                "rather than pushing through.",
            ]),
        ],
        "faq": [
            ("Is push pull legs good for beginners?",
             "It can work, but it is usually not the best choice. Beginners "
             "progress faster on a three-day full body plan that practises the "
             "main lifts more often and leaves more time to recover."),
            ("Can I run push pull legs 3 days a week?",
             "Yes, but each muscle is then trained only once a week. That works "
             "for maintenance, but most people build muscle faster with twice-weekly "
             "frequency, so four to six days is better for growth."),
            ("Where does ab training fit?",
             "Add two or three sets of planks, hanging leg raises or cable "
             "crunches at the end of any two sessions. Heavy squats and "
             "deadlifts already train your trunk hard."),
            ("Should I train to failure on every set?",
             "No. Leave one to three reps in reserve on most sets, especially "
             "compound lifts. Occasional failure on isolation exercises is fine, "
             "but constant failure adds fatigue faster than it adds muscle."),
            ("How long should a PPL session take?",
             "Most sessions take 60 to 75 minutes including the warm-up. If you "
             "are regularly going past 90 minutes, shorten rest on isolation "
             "exercises or drop a set from the last movement."),
        ],
        "related_calcs": ["one-rep-max-calculator", "macro-calculator", "tdee-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "upper-lower-split",
        "name": "Upper Lower Split",
        "title": "Upper Lower Split: 4-Day Workout Plan",
        "desc": ("A 4-day upper lower split that trains every muscle twice a "
                 "week. Strength and hypertrophy days, full sets and reps, and a "
                 "clear way to progress."),
        "level": "Intermediate",
        "days": 4,
        "weeks": 10,
        "goal": "Strength and muscle",
        "equipment": "Full gym",
        "session": "60-70 min",
        "image": "barbell-rack",
        "intro": ("Four sessions a week, two for the upper body and two for the "
                  "lower body. Each half gets one heavy day for strength and one "
                  "lighter day for muscle-building volume, which makes this the "
                  "natural next step after a beginner full body plan."),
        "schedule": [
            {"day": "Day 1 - Upper (strength)", "focus": "Chest, back, shoulders, arms",
             "exercises": [
                 ["Bench press", "4", "4-6", "3 min", "bench-press"],
                 ["Barbell row", "4", "6-8", "2 min", "barbell-row"],
                 ["Overhead press", "3", "6-8", "2 min", "overhead-press"],
                 ["Pull-up", "3", "6-8", "2 min", "pull-up"],
                 ["Dumbbell curl", "2", "8-12", "60 sec", "dumbbell-curl"],
                 ["Tricep dip", "2", "8-12", "60 sec", "tricep-dip"],
             ]},
            {"day": "Day 2 - Lower (strength)", "focus": "Quads, hamstrings, glutes",
             "exercises": [
                 ["Barbell back squat", "4", "4-6", "3 min", "barbell-back-squat"],
                 ["Romanian deadlift", "3", "6-8", "2 min", "romanian-deadlift"],
                 ["Walking lunge", "3", "8 per leg", "90 sec", "walking-lunge"],
                 ["Standing calf raise", "3", "8-12", "60 sec", None],
                 ["Plank", "3", "45 sec", "60 sec", "plank"],
             ]},
            {"day": "Day 3 - Rest", "focus": "Rest or light cardio", "exercises": []},
            {"day": "Day 4 - Upper (hypertrophy)", "focus": "Chest, back, shoulders, arms",
             "exercises": [
                 ["Incline dumbbell press", "4", "8-12", "90 sec", "incline-dumbbell-press"],
                 ["Lat pulldown", "4", "10-12", "90 sec", "lat-pulldown"],
                 ["Seated cable row", "3", "10-12", "90 sec", None],
                 ["Dumbbell lateral raise", "3", "12-20", "60 sec", None],
                 ["Incline dumbbell curl", "3", "10-15", "60 sec", None],
                 ["Tricep rope pushdown", "3", "10-15", "60 sec", None],
             ]},
            {"day": "Day 5 - Lower (hypertrophy)", "focus": "Glutes, quads, hamstrings",
             "exercises": [
                 ["Deadlift", "3", "5", "3 min", "deadlift"],
                 ["Leg press", "3", "10-15", "2 min", "leg-press"],
                 ["Hip thrust", "3", "8-12", "90 sec", "hip-thrust"],
                 ["Lying leg curl", "3", "10-15", "60 sec", None],
                 ["Seated calf raise", "3", "12-20", "60 sec", None],
             ]},
            {"day": "Days 6-7 - Rest", "focus": "Rest, walk, mobility", "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This plan suits lifters who have finished a beginner program and "
                "can no longer add weight every session. It also suits busy "
                "people of any level who want results from four sessions a week "
                "rather than five or six.",
                "The classic schedule is Monday, Tuesday, Thursday, Friday, with "
                "Wednesday and the weekend off. Any layout works as long as you "
                "avoid training the same half of the body on back-to-back days.",
                "Twice-weekly frequency per muscle is the main draw. Training "
                "each muscle two times a week tends to produce more growth than "
                "once a week at the same total volume, and the split keeps each "
                "session focused enough to finish in about an hour.",
            ]),
            ("How to progress week to week", [
                "The two day types progress differently.",
                {"list": [
                    "<strong>Strength days (4-6 reps):</strong> when you complete "
                    "all sets at the top of the range, add 2.5 kg (5 lb) to upper "
                    "body lifts and 2.5 to 5 kg (5 to 10 lb) to squats and "
                    "deadlifts. Expect a jump every one to three weeks.",
                    "<strong>Hypertrophy days (8-15 reps):</strong> add reps "
                    "first. Once every set reaches the top of the range, move up "
                    "the smallest weight increment and start again at the bottom.",
                ]},
                "A realistic target over a 10-week block is 5 to 10% more weight "
                "on your main lifts, or the same weight for noticeably more reps. "
                "Gains are slower than in your first months, and that is normal. "
                "The mechanics are explained in "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload explained</a>.",
                {"tip": "Keep one or two reps in reserve on strength days. Grinding "
                        "out ugly reps on squats and bench builds fatigue, not "
                        "strength."},
            ]),
            ("Warm-up", [
                "Spend 5 minutes on light cardio, then do movement prep for the "
                "day: band pull-aparts and shoulder circles on upper days, hip "
                "openers and bodyweight squats on lower days.",
                "Before the first lift, ramp up in three or four sets: the empty "
                "bar for 8 to 10 reps, then roughly 40%, 60% and 80% of your top "
                "weight for 5, 3 and 1 to 2 reps.",
            ]),
            ("How to pick weights", [
                "For the strength days, start at around 80 to 85% of your one "
                "rep max for sets of 4 to 6. Use a recent hard set with the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a> "
                "to get an estimate and a full percentage chart, then use the "
                "<a href=\"/plate-calculator\">plate calculator</a> to load the bar.",
                "Run week one slightly conservative, ending each set with two "
                "reps left. You will move faster over 10 weeks from a "
                "slightly-too-easy start than a too-hard one.",
            ]),
            ("Nutrition to support the plan", [
                "For muscle gain, eat a modest surplus of 200 to 300 kcal above "
                "maintenance. For fat loss while keeping strength, eat 300 to "
                "500 kcal below. The <a href=\"/calorie-calculator\">calorie "
                "calculator</a> gives you a target for either goal.",
                "Protein stays high regardless of goal: around 1.6 to 2.2 g per "
                "kg of bodyweight. Use the "
                "<a href=\"/macro-calculator\">macro calculator</a> to turn that "
                "into a full daily split. A carb-containing meal 1 to 3 hours "
                "before training helps on heavy days; see "
                "<a href=\"/guides/pre-and-post-workout-nutrition\">pre and "
                "post workout nutrition</a>.",
            ]),
            ("Deload", [
                "Deload in week 6 or whenever several lifts stall at once. Keep "
                "all exercises, cut sets roughly in half and reduce the strength "
                "day loads by about 10 to 15%. After the deload, restart the "
                "strength days a little below your previous best and build past it.",
            ]),
            ("Exercise swaps", [
                {"table": {"head": ["Planned exercise", "Good swap"], "rows": [
                    ["Barbell back squat", "Front squat, hack squat or safety bar squat"],
                    ["Bench press", "Dumbbell bench press or machine chest press"],
                    ["Deadlift", "Trap bar deadlift or rack pull"],
                    ["Barbell row", "Chest-supported dumbbell row"],
                    ["Pull-up", "Lat pulldown or assisted pull-up"],
                    ["Hip thrust", "Glute bridge or cable pull-through"],
                ]}},
                "If lower back fatigue builds up from doing both deadlifts and "
                "Romanian deadlifts, replace the RDL on the strength day with a "
                "leg curl variation for the block.",
            ]),
            ("Common mistakes", [
                "The upper/lower split is forgiving, but a few habits will slow "
                "you down.",
                {"list": [
                    "<strong>Treating both days the same.</strong> Strength days "
                    "should be heavy with long rests; hypertrophy days should be "
                    "lighter with shorter rests. Blurring them loses the benefit of each.",
                    "<strong>Skimping on the back.</strong> Every upper day pairs "
                    "a press with a pull. Keep pulling volume at least equal to "
                    "pressing volume for healthy shoulders.",
                    "<strong>Letting sessions sprawl.</strong> If sessions run "
                    "past 80 minutes, trim rest on accessories rather than "
                    "dropping the big lifts.",
                    "<strong>Never testing progress.</strong> Re-estimate your "
                    "max every block with the "
                    "<a href=\"/one-rep-max-calculator\">one rep max calculator</a> "
                    "so your percentages stay accurate.",
                ]},
                "After two or three blocks, rotate some exercises, for example "
                "front squats for back squats or a close-grip bench for the "
                "regular bench, to keep progress moving while still training the "
                "same patterns.",
            ]),
        ],
        "faq": [
            ("Is an upper lower split better than push pull legs?",
             "Neither is better in general. Upper/lower fits four days and is "
             "easier to recover from, while push pull legs fits five or six days "
             "and allows more volume per session. Choose the one you can do "
             "consistently."),
            ("Can beginners do an upper lower split?",
             "Yes, especially beginners who prefer four shorter sessions. Keep "
             "the weights conservative and focus on adding weight to the main "
             "lifts every week."),
            ("Can I do upper lower three days a week?",
             "You can alternate upper, lower, upper one week and lower, upper, "
             "lower the next. Progress is a little slower than four days but "
             "still solid."),
            ("Where do I add cardio?",
             "Do 20 to 30 minutes of easy cardio after upper sessions or on rest "
             "days. Avoid hard intervals right before a lower body strength day."),
        ],
        "related_calcs": ["one-rep-max-calculator", "calorie-calculator", "macro-calculator"],
    },
    # -----------------------------------------------------------------------
    {
        "slug": "5x5-strength-program",
        "name": "5x5 Strength Program",
        "title": "5x5 Workout: 3-Day Barbell Strength Program",
        "desc": ("A 3-day 5x5 barbell program built on squats, presses, rows and "
                 "deadlifts. A and B workouts, linear progression rules, and how "
                 "to handle stalls."),
        "level": "Beginner",
        "days": 3,
        "weeks": 12,
        "goal": "Strength",
        "equipment": "Barbell, rack, bench",
        "session": "45-60 min",
        "image": "squat",
        "intro": ("Five sets of five on a handful of barbell lifts, three days a "
                  "week, with a little more weight every session. It is one of "
                  "the oldest and most reliable ways to get strong, and it needs "
                  "nothing more than a barbell, a rack and a bench."),
        "schedule": [
            {"day": "Day 1 - Workout A", "focus": "Squat, bench, row",
             "exercises": [
                 ["Barbell back squat", "5", "5", "3-5 min", "barbell-back-squat"],
                 ["Bench press", "5", "5", "3 min", "bench-press"],
                 ["Barbell row", "5", "5", "2-3 min", "barbell-row"],
                 ["Plank (optional)", "2", "30-45 sec", "60 sec", "plank"],
             ]},
            {"day": "Day 2 - Rest", "focus": "Rest or light walking", "exercises": []},
            {"day": "Day 3 - Workout B", "focus": "Squat, press, deadlift",
             "exercises": [
                 ["Barbell back squat", "5", "5", "3-5 min", "barbell-back-squat"],
                 ["Overhead press", "5", "5", "3 min", "overhead-press"],
                 ["Deadlift", "1", "5", "-", "deadlift"],
                 ["Pull-up (optional)", "3", "As many as possible", "2 min", "pull-up"],
             ]},
            {"day": "Day 4 - Rest", "focus": "Rest or light walking", "exercises": []},
            {"day": "Day 5 - Workout A", "focus": "Squat, bench, row",
             "exercises": [
                 ["Barbell back squat", "5", "5", "3-5 min", "barbell-back-squat"],
                 ["Bench press", "5", "5", "3 min", "bench-press"],
                 ["Barbell row", "5", "5", "2-3 min", "barbell-row"],
                 ["Plank (optional)", "2", "30-45 sec", "60 sec", "plank"],
             ]},
            {"day": "Days 6-7 - Rest", "focus": "Rest. Next week starts with Workout B",
             "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This is for beginners and early intermediates whose main goal "
                "is getting stronger on the big barbell lifts. It also works "
                "well for people returning to lifting after a long break, since "
                "the simple structure lets strength come back quickly.",
                "It is a strength-first plan. You will build muscle too, "
                "especially in your first months, but if your priority is how "
                "your arms and shoulders look, the "
                "<a href=\"/workouts/beginner-full-body-workout\">beginner full "
                "body workout</a> includes more accessory work.",
            ]),
            ("How the A/B rotation works", [
                "There are two workouts, A and B, and you alternate them on "
                "three non-consecutive days. Week one is A, B, A; week two is "
                "B, A, B; and so on. Over two weeks, each workout is done three "
                "times.",
                "You squat every session, which is why the squat climbs so fast "
                "on this kind of program. Bench press and overhead press "
                "alternate, as do rows and deadlifts. The deadlift gets a "
                "single heavy set of five because it is the most taxing lift and "
                "it also benefits from all the squatting.",
            ]),
            ("How to progress week to week", [
                "Progression is linear, which means you add weight every time "
                "you successfully complete a lift:",
                {"list": [
                    "Squat: add 2.5 kg (5 lb) each session.",
                    "Bench press, overhead press and row: add 2.5 kg (5 lb) "
                    "each time that workout comes round. Once jumps get hard, "
                    "switch to 1.25 kg (2.5 lb) with fractional plates.",
                    "Deadlift: add 5 kg (10 lb) each session for the first few "
                    "weeks, then 2.5 kg (5 lb).",
                ]},
                "A successful session means all 25 reps (5 sets of 5) completed "
                "with good form. If you miss reps, repeat the same weight next "
                "time. If you fail the same weight three sessions in a row, "
                "deload that lift by 10% and work back up. You will usually pass "
                "your old sticking point within two or three weeks.",
                "After two or three resets on the same lift, linear progress is "
                "done. Switch that lift to 3 sets of 5, then later move to a "
                "weekly-progression plan like the "
                "<a href=\"/workouts/upper-lower-split\">upper/lower split</a>.",
                {"tip": "Rest fully between heavy sets. Three to five minutes "
                        "on squats is normal and productive, not lazy."},
            ]),
            ("Warm-up", [
                "Warm up with 5 minutes of light cardio and a few bodyweight "
                "squats. Then ramp up on the bar for each main lift. For a 100 kg "
                "squat, a typical ramp is:",
                {"table": {"head": ["Set", "Weight", "Reps"], "rows": [
                    ["1-2", "Empty bar (20 kg / 45 lb)", "5"],
                    ["3", "40 kg / 90 lb", "5"],
                    ["4", "60 kg / 135 lb", "3"],
                    ["5", "80 kg / 175 lb", "2"],
                    ["Work sets", "100 kg / 225 lb", "5 x 5"],
                ]}},
                "Keep warm-up reps crisp and do not let them tire you. The "
                "<a href=\"/plate-calculator\">plate calculator</a> makes "
                "loading each jump quicker.",
            ]),
            ("How to pick starting weights", [
                "Start light. If you have never lifted, begin every lift except "
                "the deadlift with the empty bar, and the deadlift at about "
                "40 kg (95 lb). The fast weekly jumps mean you will be lifting "
                "challenging weights within a month.",
                "If you have lifted before, take a recent set of 5 and enter it "
                "into the <a href=\"/one-rep-max-calculator\">one rep max "
                "calculator</a>. Start your 5x5 at about 70% of the estimated "
                "max, which should feel like you could do 8 or 9 reps. That "
                "runway keeps progression going for months.",
            ]),
            ("Nutrition to support the plan", [
                "Linear strength gains need fuel. If you are underweight or at "
                "a healthy weight, eat in a surplus of around 300 kcal over your "
                "maintenance number from the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a>. Trying to "
                "add weight to the bar every session while dieting hard usually "
                "ends in early stalls.",
                "Get 1.6 to 2.2 g of protein per kg of bodyweight daily; the "
                "<a href=\"/protein-calculator\">protein calculator</a> works it "
                "out. Creatine monohydrate is one of the few supplements with "
                "strong evidence for strength gains; see the "
                "<a href=\"/guides/creatine-guide\">creatine guide</a>. Your "
                "strength-to-bodyweight progress can be compared over time with "
                "the <a href=\"/wilks-calculator\">Wilks calculator</a>.",
            ]),
            ("Swaps and adjustments", [
                "This plan has few exercises, so swaps should stay close to the "
                "original movement:",
                {"list": [
                    "Barbell row aggravates your lower back: use a chest-supported row.",
                    "No pull-up bar: do lat pulldowns for 3 sets of 8 to 10.",
                    "Overhead press stalls very early: use smaller 1 kg (2.5 lb) jumps.",
                    "Squats feel too frequent after week 8: make Workout B's squat "
                    "a lighter day at 80% of your Workout A weight.",
                ]},
            ]),
            ("Technique and safety", [
                "Adding weight every session only works if technique holds. "
                "Before each work set, set up the same way every time: feet "
                "planted, deep breath held into the belly, and the bar path "
                "planned.",
                {"list": [
                    "Squat in a rack with the safety pins set just below the "
                    "bottom of your squat. Read the "
                    "<a href=\"/exercises/barbell-back-squat\">squat technique "
                    "notes</a> before your first session.",
                    "Bench with safety arms or a spotter once the weight gets "
                    "challenging.",
                    "Pull every deadlift from a dead stop with a neutral back; see "
                    "the <a href=\"/exercises/deadlift\">deadlift guide</a>.",
                    "Keep the row strict. If your torso rises to vertical, the "
                    "weight is too heavy.",
                ]},
                "A weightlifting belt is optional and can help on heavy squats "
                "and deadlifts once you have learned to brace without one. It is "
                "not needed in the first months.",
            ]),
        ],
        "faq": [
            ("Is 5x5 good for building muscle?",
             "Yes, especially for beginners, who build muscle quickly from any "
             "well-run strength program. Intermediates focused purely on size "
             "usually do better with more volume and higher rep ranges."),
            ("Why only one set of deadlifts?",
             "Deadlifts are very fatiguing, and you are already squatting every "
             "session. One heavy set of five is enough to drive progress without "
             "wrecking recovery."),
            ("Can I add arm or ab work?",
             "Yes. Two or three sets of curls, tricep work or planks at the end "
             "of a session will not hurt progress. Keep it short so it does not "
             "eat into recovery for the main lifts."),
            ("How long can I run a 5x5 program?",
             "Most people get three to six months of steady progress. Once you "
             "have reset the same lifts two or three times, move to a program "
             "with weekly rather than per-session progression."),
        ],
        "related_calcs": ["one-rep-max-calculator", "plate-calculator", "wilks-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "home-dumbbell-workout",
        "name": "Home Dumbbell Workout",
        "title": "Home Dumbbell Workout Plan: 4 Days, No Gym",
        "desc": ("A 4-day home workout plan using only dumbbells and bodyweight. "
                 "Upper and lower sessions, sets and reps, and how to keep "
                 "progressing with limited weights."),
        "level": "Beginner",
        "days": 4,
        "weeks": 8,
        "goal": "General fitness",
        "equipment": "Dumbbells, bench or sturdy chair",
        "session": "35-50 min",
        "image": "home-workout",
        "intro": ("A pair of dumbbells and your own bodyweight are enough to "
                  "build real strength and muscle. This four-day plan alternates "
                  "upper and lower body sessions and shows you how to keep making "
                  "progress even when your heaviest dumbbell starts to feel light."),
        "schedule": [
            {"day": "Day 1 - Upper A", "focus": "Chest, back, shoulders",
             "exercises": [
                 ["Dumbbell floor or bench press", "4", "8-12", "90 sec", None],
                 ["One-arm dumbbell row", "4", "10-12 per side", "60 sec", None],
                 ["Push-up", "3", "As many as possible", "90 sec", "push-up"],
                 ["Seated dumbbell shoulder press", "3", "10-12", "90 sec", None],
                 ["Dumbbell curl", "3", "10-15", "60 sec", "dumbbell-curl"],
             ]},
            {"day": "Day 2 - Lower A", "focus": "Quads, glutes, core",
             "exercises": [
                 ["Goblet squat", "4", "10-15", "90 sec", None],
                 ["Dumbbell Romanian deadlift", "3", "10-12", "90 sec", "romanian-deadlift"],
                 ["Walking lunge", "3", "10 per leg", "90 sec", "walking-lunge"],
                 ["Single-leg calf raise", "3", "12-20 per leg", "45 sec", None],
                 ["Plank", "3", "30-60 sec", "45 sec", "plank"],
             ]},
            {"day": "Day 3 - Rest", "focus": "Rest or a 30-minute walk", "exercises": []},
            {"day": "Day 4 - Upper B", "focus": "Shoulders, back, arms",
             "exercises": [
                 ["Incline dumbbell press (bench or floor)", "4", "8-12", "90 sec", "incline-dumbbell-press"],
                 ["Chest-supported dumbbell row", "3", "10-12", "60 sec", None],
                 ["Pike push-up", "3", "6-12", "90 sec", None],
                 ["Dumbbell lateral raise", "3", "12-20", "45 sec", None],
                 ["Chair tricep dip", "3", "10-15", "60 sec", "tricep-dip"],
             ]},
            {"day": "Day 5 - Lower B", "focus": "Glutes, hamstrings, legs",
             "exercises": [
                 ["Bulgarian split squat", "3", "8-12 per leg", "90 sec", None],
                 ["Dumbbell hip thrust", "4", "12-15", "60 sec", "hip-thrust"],
                 ["Dumbbell step-up", "3", "10 per leg", "60 sec", None],
                 ["Single-leg Romanian deadlift", "3", "10 per leg", "60 sec", None],
                 ["Dead bug", "3", "10 per side", "45 sec", None],
             ]},
            {"day": "Days 6-7 - Rest", "focus": "Rest, walk, stretch", "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This is for anyone training at home with a set of dumbbells, "
                "ideally adjustable ones, and either a flat bench or a sturdy "
                "chair. It suits beginners, people who cannot get to a gym "
                "regularly, and gym-goers who want a plan for weeks away.",
                "If you can only manage three days, drop Lower B and add its "
                "split squat to Lower A in place of the walking lunge. The plan "
                "still trains everything.",
            ]),
            ("How to progress with limited weights", [
                "The challenge at home is that your dumbbells eventually feel "
                "light. Progress still works, you just need more tools than "
                "adding weight:",
                {"olist": [
                    "<strong>Add reps.</strong> Work up to the top of each rep "
                    "range on all sets before anything else.",
                    "<strong>Add weight</strong> if you have heavier dumbbells or "
                    "an adjustable set.",
                    "<strong>Slow the tempo.</strong> Take three to four seconds "
                    "to lower each rep. The same weight becomes much harder.",
                    "<strong>Add a pause.</strong> Hold for two seconds at the "
                    "bottom of squats, split squats and presses.",
                    "<strong>Go single-limb.</strong> Swap goblet squats for "
                    "Bulgarian split squats, or hip thrusts for single-leg hip "
                    "thrusts, to double the load on each side.",
                    "<strong>Add a set</strong>, up to five per exercise.",
                ]},
                "Change only one variable at a time, and keep notes so you know "
                "what to beat next session. This is "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload</a> without a barbell.",
                {"tip": "Leg exercises outgrow light dumbbells first. Move to "
                        "single-leg versions as soon as you can do 20 clean reps "
                        "of the two-leg exercise."},
            ]),
            ("Warm-up", [
                "Five to eight minutes is plenty: march or jog on the spot, then "
                "do arm circles, hip circles, 10 bodyweight squats, 10 glute "
                "bridges and a few slow push-ups. Do one light set of the first "
                "exercise before your working sets.",
            ]),
            ("How to pick weights", [
                "Pick a weight that brings you within two or three reps of "
                "failure at the top of the listed range. If you hit the top of "
                "the range with ease, the weight is too light; if you cannot "
                "reach the bottom, it is too heavy.",
                "If you are buying dumbbells, adjustable sets that reach at least "
                "20 to 25 kg (45 to 55 lb) per hand are the most useful long-term "
                "investment for most adults. You can estimate how hard a "
                "set is by putting it into the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a>.",
            ]),
            ("Nutrition to support the plan", [
                "Muscle is built from training plus food. Eat enough protein, "
                "around 1.6 to 2.2 g per kg of bodyweight, which the "
                "<a href=\"/protein-calculator\">protein calculator</a> works out "
                "for you.",
                "For fat loss, aim for a 300 to 500 kcal daily deficit from the "
                "number given by the <a href=\"/calorie-calculator\">calorie "
                "calculator</a>. Training at home makes it easy to add daily "
                "walking, which raises your total energy burn without hurting "
                "recovery. Track your trend with the "
                "<a href=\"/bmi-calculator\">BMI calculator</a> or, better, "
                "waist measurements.",
            ]),
            ("Deload", [
                "Every sixth or seventh week, or whenever your joints feel "
                "beaten up, do one week with half the sets and no sets close to "
                "failure. Home training is often lower in load but higher in "
                "reps, which can still build fatigue.",
            ]),
            ("Swaps", [
                {"table": {"head": ["Planned exercise", "Swap"], "rows": [
                    ["Dumbbell bench press", "Floor press or push-up with feet raised"],
                    ["One-arm dumbbell row", "Backpack row or towel row on a door"],
                    ["Goblet squat", "Tempo bodyweight squat or split squat"],
                    ["Dumbbell hip thrust", "Single-leg glute bridge"],
                    ["Pike push-up", "Dumbbell shoulder press"],
                ]}},
                "If you can fit a doorway pull-up bar, add 3 sets of "
                "<a href=\"/exercises/pull-up\">pull-ups</a> to each upper day. "
                "It is the single best upgrade to a home setup.",
            ]),
            ("Setting up your space", [
                "A home workout plan only works if starting it takes no effort. "
                "Keep your dumbbells somewhere visible and leave enough floor "
                "space to lie down with arms stretched out, about 2 by 2 metres "
                "(6 by 6 feet).",
                {"list": [
                    "Train on a non-slip surface. A cheap exercise mat or rubber "
                    "floor tiles protect both you and the floor.",
                    "Check that any chair or bench you use is stable before "
                    "loading it; place it against a wall if it can slide.",
                    "Set a fixed time for training. Home workouts get skipped far "
                    "more often than gym sessions because nothing forces a start.",
                    "Keep a log on your phone. Without a gym's bigger weights, "
                    "your notes are what tell you you are progressing.",
                ]},
                "If you are short on time, you can split any session into two "
                "20-minute blocks, morning and evening. Total weekly work matters "
                "more than doing it all at once.",
            ]),
        ],
        "faq": [
            ("Can you build muscle with only dumbbells?",
             "Yes. As long as you take sets close to failure and keep making "
             "them harder over time, dumbbells and bodyweight are enough to "
             "build muscle for most people, especially in the first year or two."),
            ("What weight dumbbells should I buy?",
             "Adjustable dumbbells are the best value. Most beginners do well "
             "with a set that goes up to 20 to 25 kg (45 to 55 lb) per hand, "
             "which covers both upper and lower body exercises."),
            ("I have no bench. What can I use?",
             "Do floor presses instead of bench presses, and use a sturdy chair, "
             "step or sofa edge for split squats, hip thrusts and dips. Make "
             "sure anything you use cannot slide or tip."),
            ("How long until I see results?",
             "Most people feel stronger within two to three weeks and notice "
             "visible changes in 8 to 12 weeks, provided they train consistently "
             "and eat enough protein."),
        ],
        "related_calcs": ["protein-calculator", "calorie-calculator", "bmi-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "fat-loss-workout-plan",
        "name": "Fat Loss Workout Plan",
        "title": "Fat Loss Workout Plan: 4 Days of Lifting and Cardio",
        "desc": ("A 4-day fat loss workout plan that combines strength training "
                 "with conditioning. Keep your muscle, burn more calories and "
                 "know exactly what to do each day."),
        "level": "Beginner",
        "days": 4,
        "weeks": 8,
        "goal": "Fat loss",
        "equipment": "Gym or dumbbells plus cardio machine",
        "session": "45-60 min",
        "image": "battle-ropes",
        "intro": ("Fat loss happens in the kitchen, but what you do in the gym "
                  "decides whether the weight you lose is fat or muscle. This "
                  "plan pairs four strength sessions with short conditioning "
                  "finishers so you keep your strength while the scale moves down."),
        "schedule": [
            {"day": "Day 1 - Lower strength + intervals", "focus": "Legs, glutes, conditioning",
             "exercises": [
                 ["Barbell back squat", "4", "6-8", "2 min", "barbell-back-squat"],
                 ["Romanian deadlift", "3", "8-10", "2 min", "romanian-deadlift"],
                 ["Walking lunge", "3", "10 per leg", "90 sec", "walking-lunge"],
                 ["Plank", "3", "30-45 sec", "45 sec", "plank"],
                 ["Bike intervals: 30 sec hard / 90 sec easy", "6-8 rounds", "-", "-", None],
             ]},
            {"day": "Day 2 - Upper strength + circuit", "focus": "Chest, back, shoulders",
             "exercises": [
                 ["Bench press", "4", "6-8", "2 min", "bench-press"],
                 ["Barbell row", "4", "8-10", "90 sec", "barbell-row"],
                 ["Overhead press", "3", "8-10", "90 sec", "overhead-press"],
                 ["Lat pulldown", "3", "10-12", "60 sec", "lat-pulldown"],
                 ["Finisher: 10 push-ups + 15 kettlebell swings, 4 rounds", "4", "-", "60 sec", None],
             ]},
            {"day": "Day 3 - Rest", "focus": "Rest. Aim for 8,000+ steps", "exercises": []},
            {"day": "Day 4 - Full body strength", "focus": "Hinge, push, pull",
             "exercises": [
                 ["Deadlift", "3", "5", "3 min", "deadlift"],
                 ["Incline dumbbell press", "3", "8-12", "90 sec", "incline-dumbbell-press"],
                 ["Pull-up (or assisted)", "3", "6-10", "2 min", "pull-up"],
                 ["Hip thrust", "3", "10-12", "90 sec", "hip-thrust"],
                 ["Dumbbell curl", "2", "12-15", "45 sec", "dumbbell-curl"],
             ]},
            {"day": "Day 5 - Metabolic circuit + steady cardio", "focus": "Full body conditioning",
             "exercises": [
                 ["Circuit: goblet squat x12", "4 rounds", "12", "-", None],
                 ["Circuit: push-up x10", "4 rounds", "10", "-", "push-up"],
                 ["Circuit: dumbbell row x10 per arm", "4 rounds", "10", "-", None],
                 ["Circuit: reverse lunge x8 per leg", "4 rounds", "8", "90 sec after round", None],
                 ["Incline walk or easy bike", "1", "25-30 min", "-", None],
             ]},
            {"day": "Days 6-7 - Rest", "focus": "Active rest, long walk", "exercises": []},
        ],
        "body": [
            ("Who this plan is for", [
                "This plan is for anyone whose main goal is losing body fat, "
                "from complete beginners to people who have lifted on and off. "
                "It assumes you are also eating in a calorie deficit, because "
                "no workout plan can out-train a diet that is in surplus.",
                "The structure is deliberate. The heavy strength work tells your "
                "body to keep its muscle while you eat less. The conditioning "
                "burns extra calories and improves fitness without the "
                "recovery cost of hours of cardio. If you are new to lifting, "
                "spend the first two weeks learning technique with lighter "
                "weights; the <a href=\"/guides/beginner-gym-guide\">beginner "
                "gym guide</a> covers the basics.",
            ]),
            ("Your diet does the heavy lifting", [
                "Fat loss requires a calorie deficit. Work out your maintenance "
                "with the <a href=\"/tdee-calculator\">TDEE calculator</a>, then "
                "eat 300 to 500 kcal below it, or use the "
                "<a href=\"/weight-loss-calculator\">weight loss calculator</a> "
                "to set a target date. A loss of about 0.5 to 1% of bodyweight "
                "per week is fast enough to stay motivated and slow enough to "
                "keep muscle.",
                "Protein is the most important number in a diet. Higher intakes, "
                "around 1.8 to 2.2 g per kg of bodyweight, help preserve muscle "
                "during a deficit and keep hunger down. Use the "
                "<a href=\"/protein-calculator\">protein calculator</a>, and see "
                "<a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
                "how to calculate calories for weight loss</a> for the full method.",
            ]),
            ("How to progress week to week", [
                "In a deficit, the goal on the strength lifts is to <em>maintain "
                "or slowly improve</em>, not to set personal records every week.",
                {"list": [
                    "<strong>Strength exercises:</strong> keep the weight the same "
                    "and aim to add a rep. When you hit the top of the range on "
                    "all sets, add the smallest increment.",
                    "<strong>Intervals:</strong> start with 6 rounds. Add one round "
                    "per week up to 10, then make the hard 30 seconds harder.",
                    "<strong>Circuits:</strong> keep the reps fixed and try to cut "
                    "the rest between rounds, or add a fifth round.",
                    "<strong>Steps:</strong> raise your daily average by about "
                    "1,000 steps every two weeks up to a level you can sustain.",
                ]},
                "If your strength drops noticeably over two or three weeks, your "
                "deficit may be too aggressive. Add 100 to 200 kcal, mostly "
                "from carbohydrates around training.",
                {"tip": "Track your waist measurement weekly alongside your "
                        "weight. Waist going down while lifts hold steady means "
                        "you are losing fat, not muscle."},
            ]),
            ("Warm-up", [
                "Five minutes of easy cardio, followed by dynamic movements for "
                "the day's lifts: leg swings and bodyweight squats on lower "
                "days, arm circles and band pull-aparts on upper days. Do two or "
                "three ramp-up sets before the first heavy lift.",
            ]),
            ("How to pick weights", [
                "Use weights that leave two reps in reserve on the strength work. "
                "If you already know your numbers, start at about 70 to 75% of "
                "your one rep max; estimate it with the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a>.",
                "For circuits and finishers, choose weights that let you move "
                "steadily without long pauses. They should feel hard because of "
                "the pace, not because the load is near your limit.",
            ]),
            ("HIIT, steady cardio and walking", [
                "This plan uses both short intervals and steady cardio, and each "
                "has a role. Intervals are time-efficient for fitness. Steady "
                "cardio and walking burn calories with very little recovery "
                "cost. Daily walking is the most underrated fat loss tool there "
                "is. The trade-offs are covered in "
                "<a href=\"/guides/cardio-for-fat-loss-hiit-vs-liss\">HIIT vs "
                "LISS for fat loss</a>, and the "
                "<a href=\"/calories-burned-calculator\">calories burned "
                "calculator</a> estimates what each session adds.",
            ]),
            ("Deload and swaps", [
                "Take an easier week after week 6, or sooner if you feel run "
                "down: halve the strength sets, skip the intervals and keep "
                "walking. Dieting lowers your recovery capacity, so listen to "
                "the warning signs in "
                "<a href=\"/guides/rest-days-and-recovery\">rest days and recovery</a>.",
                "Swaps: use a rower, ski erg or hill sprints for bike intervals; "
                "a leg press for squats if your back is tired; dumbbell bench for "
                "barbell bench; and a trap bar for deadlifts. Training at home? "
                "The <a href=\"/workouts/home-dumbbell-workout\">home dumbbell "
                "workout</a> plus daily walks works well with the same diet.",
            ]),
            ("Common fat loss mistakes", [
                "Most stalled diets come down to the same handful of problems:",
                {"list": [
                    "<strong>Switching to light weights and high reps.</strong> "
                    "Heavy lifting is what tells your body to keep its muscle. "
                    "Keep the strength work heavy.",
                    "<strong>Too much cardio, too soon.</strong> Hours of extra "
                    "cardio raise hunger and fatigue. Add steps first.",
                    "<strong>Chasing the scale daily.</strong> Water shifts can "
                    "hide fat loss for a week or more. Compare weekly averages.",
                    "<strong>Not adjusting.</strong> As you lose weight, your "
                    "maintenance drops. Recalculate every 4 to 5 kg (10 lb).",
                ]},
                "Expect plateaus. When the weekly average has not moved for two "
                "to three weeks, cut 100 to 150 kcal or add 2,000 daily steps, "
                "not both at once. The <a href=\"/body-fat-calculator\">body fat "
                "calculator</a> is a better progress check than weight alone.",
            ]),
        ],
        "faq": [
            ("Should I do cardio or weights to lose fat?",
             "Both, but weights are the priority. Strength training preserves "
             "muscle while you diet, and cardio adds calorie burn. The calorie "
             "deficit from your diet is what actually drives fat loss."),
            ("How fast will I lose weight on this plan?",
             "That depends on your calorie deficit, not the workouts alone. A "
             "steady target is 0.5 to 1% of bodyweight per week; faster than "
             "that tends to cost muscle and is harder to sustain."),
            ("Can I spot-reduce belly fat with ab exercises?",
             "No. You cannot choose where fat comes off. Ab exercises strengthen "
             "your core, but belly fat drops as your overall body fat goes down."),
            ("Why am I not losing weight even though I train hard?",
             "Most often the calorie deficit is smaller than you think. Track "
             "your food carefully for two weeks, check portion sizes, and "
             "recalculate your targets as your weight drops."),
            ("Is it safe to do this plan while dieting?",
             "For most healthy adults, yes, with a moderate deficit. If you have "
             "a medical condition, are pregnant or have a history of disordered "
             "eating, speak to a doctor before starting a diet and new program."),
        ],
        "related_calcs": ["weight-loss-calculator", "calorie-calculator", "calories-burned-calculator"],
    },
]

BY_SLUG = {w["slug"]: w for w in WORKOUTS}
