"""
Guides, part B: supplements, training volume, workout nutrition, recovery,
cardio, body fat measurement and sleep.

Each entry follows the shared body block format: `body` is a list of
(heading, blocks) tuples, `faq` a list of (question, answer) tuples.
"""

GUIDES = [
    # -----------------------------------------------------------------------
    {
        "slug": "creatine-guide",
        "title": "Creatine Guide: Dose, Timing, Safety and Myths",
        "desc": ("How creatine monohydrate works, how much to take, whether you "
                 "need to load, and what the research says about hair loss, "
                 "kidneys and water weight."),
        "h1": "Creatine: what it does, how much to take, and what to ignore",
        "category": "Nutrition",
        "image": "protein-food",
        "intro": ("Creatine monohydrate is the most researched supplement in "
                  "sport nutrition, and one of very few with consistent evidence "
                  "behind it. It is also cheap, simple to take, and surrounded by "
                  "more myths than almost anything else on the shelf."),
        "body": [
            ("What creatine actually does", [
                "Your muscles store creatine mostly as phosphocreatine, which "
                "regenerates ATP, the molecule that powers short, hard muscle "
                "contractions. During a heavy set of five or a 10-second sprint, "
                "phosphocreatine is a major energy source.",
                "Your body makes about 1 g of creatine a day, and a diet with "
                "meat and fish supplies roughly another 1 to 2 g. That leaves "
                "muscle stores at around 60 to 80 percent of their capacity. "
                "Supplementing tops them up.",
                "Fuller stores let you squeeze out an extra rep or two at a given "
                "weight and recover slightly faster between sets. Over weeks, "
                "that extra work adds up to more strength and more muscle than "
                "the same training without it. Creatine does not build muscle "
                "on its own; it lets you train a little harder.",
            ]),
            ("What the evidence shows", [
                "The International Society of Sports Nutrition position stand "
                "(Kreider et al., Journal of the International Society of Sports "
                "Nutrition, 2017) reviewed hundreds of studies and concluded that "
                "creatine monohydrate is the most effective nutritional "
                "supplement available for increasing high-intensity exercise "
                "capacity and lean body mass.",
                {"list": [
                    "<strong>Strength:</strong> modest but reliable improvements "
                    "when combined with resistance training.",
                    "<strong>Lean mass:</strong> typically an extra 1 to 2 kg "
                    "(2 to 4 lb) over a training block of several weeks, part of "
                    "which is water held inside the muscle.",
                    "<strong>Repeated sprints:</strong> better performance in "
                    "sports with short bursts and brief rest, like football or "
                    "court sports.",
                    "<strong>Endurance:</strong> little direct benefit for steady "
                    "aerobic work.",
                ]},
                "Response varies. People with low starting stores, including "
                "many vegetarians and vegans, tend to see the largest effect. A "
                "minority of people who already eat a lot of meat notice very "
                "little.",
            ]),
            ("How much to take, and when", [
                "The standard maintenance dose is <strong>3 to 5 g per day</strong>, "
                "every day, including rest days. Larger people sit at the upper "
                "end; smaller people do fine with 3 g.",
                {"table": {
                    "head": ["Approach", "Dose", "Time to full stores"],
                    "rows": [
                        ["Daily dose only", "3-5 g/day", "About 3-4 weeks"],
                        ["Loading phase", "20 g/day split into 4 doses, 5-7 days, then 3-5 g/day", "About 1 week"],
                    ],
                }},
                "Loading is optional. It gets you to saturation faster, but you "
                "end up in the same place a few weeks later either way. Splitting "
                "a 20 g day into four 5 g servings reduces the stomach upset that "
                "one large dose can cause.",
                {"tip": "Consistency matters far more than timing. Pick a time "
                        "you will not forget, such as with breakfast, and take it "
                        "every day."},
                "A few studies hint that taking creatine close to training, "
                "especially after, is slightly better, but the differences are "
                "small and inconsistent. Because creatine works by keeping stores "
                "topped up, the daily total is what counts.",
                "Taking it with a meal containing carbohydrate and protein may "
                "improve uptake a little and is easier on the stomach. Mixing it "
                "into a protein shake, water or juice all works. Coffee does not "
                "cancel it out in normal amounts.",
            ]),
            ("Which type to buy", [
                "Buy plain <strong>creatine monohydrate</strong>. It is the form "
                "used in nearly all the research, and it is the cheapest. Micronised "
                "monohydrate dissolves more easily but works the same.",
                "Creatine HCl, buffered creatine, creatine ethyl ester and "
                "liquid creatine cost more and have not been shown to work "
                "better. Some, like liquid forms, are less stable.",
                "If you compete in a tested sport, choose a product carrying a "
                "third-party certification such as Informed Sport or NSF "
                "Certified for Sport, which screens for banned substances.",
            ]),
            ("Myth: creatine causes hair loss", [
                "This claim traces back to one small study of college rugby "
                "players (van der Merwe et al., Clinical Journal of Sport "
                "Medicine, 2009). After three weeks of creatine, levels of DHT, a "
                "hormone linked to male pattern baldness, rose compared with "
                "placebo.",
                "The study did not measure hair loss. DHT stayed within the "
                "normal range, and the finding has not been replicated in the "
                "years since. Other studies on creatine and testosterone-related "
                "hormones have not found meaningful changes.",
                "The honest summary: there is no direct evidence that creatine "
                "causes hair loss. If you have a strong family history and are "
                "worried, that is a reasonable conversation to have with a "
                "dermatologist, but the evidence does not support avoiding it on "
                "these grounds alone.",
            ]),
            ("Myth: creatine damages your kidneys", [
                "In healthy people, studies lasting up to several years at "
                "normal doses have not found harm to kidney function. The ISSN "
                "position stand describes it as safe for healthy individuals at "
                "recommended doses.",
                "The confusion comes from blood tests. Creatine breaks down into "
                "creatinine, the marker doctors use to estimate kidney function. "
                "Supplementing can nudge creatinine up, which looks like reduced "
                "kidney function on paper when it is not. Tell your doctor you "
                "take creatine before any blood test.",
                "If you already have kidney disease, diabetes affecting the "
                "kidneys, or take medications that strain them, speak to your "
                "doctor before using creatine. The same applies if you are "
                "pregnant, breastfeeding, or under 18.",
            ]),
            ("Water weight, bloating and cramping", [
                "Expect the scale to rise by about 1 to 2 kg (2 to 4 lb) in the "
                "first few weeks. That water is stored inside muscle cells, not "
                "under the skin, so it does not make you look softer. If you are "
                "tracking a fat loss diet with the "
                "<a href=\"/weight-loss-calculator\">weight loss calculator</a>, "
                "account for this jump rather than cutting calories further.",
                "Bloating is mostly a loading-phase issue and usually disappears "
                "at 3 to 5 g a day. Reviews have not found that creatine increases "
                "cramping or dehydration; if anything, some data suggest the "
                "opposite. Drinking enough water is sensible regardless, and the "
                "<a href=\"/water-intake-calculator\">water intake calculator</a> "
                "gives you a starting number.",
            ]),
            ("Who benefits most", [
                "Creatine helps most in training built on short, hard efforts. "
                "That covers most gym goers, but the size of the effect varies.",
                {"table": {
                    "head": ["Who", "Expected benefit", "Why"],
                    "rows": [
                        ["Lifters training for strength or muscle", "Clear", "Sets of 1-15 reps lean heavily on phosphocreatine"],
                        ["Vegetarians and vegans", "Often larger", "Little dietary creatine, so lower starting stores"],
                        ["Team and court sport players", "Clear", "Repeated sprints with short rests"],
                        ["Older adults who lift", "Moderate", "May help preserve muscle and strength alongside training"],
                        ["Pure endurance athletes", "Small", "Steady aerobic work relies on other energy systems"],
                    ],
                }},
                "If you do not train, creatine on its own will do very little for "
                "your body composition. It amplifies work; it does not replace it.",
            ]),
            ("Getting started: a simple checklist", [
                {"olist": [
                    "Buy plain creatine monohydrate, ideally third-party tested.",
                    "Take 3 to 5 g once a day with a meal. Use a 5 ml teaspoon as "
                    "a rough guide if your tub has no scoop; a level teaspoon is "
                    "about 4 to 5 g, but check your product's label.",
                    "Expect a 1 to 2 kg rise on the scale over the first few weeks.",
                    "Give it at least four weeks before judging whether it helps.",
                    "Tell your doctor you take it before any blood test.",
                ]},
                "Judge the effect by your training log, not by how you feel. Look "
                "for an extra rep at the same weight, or slightly better "
                "performance on the last set of an exercise, compared with the "
                "month before you started.",
                "Creatine does not need cycling, does not go off quickly when kept "
                "dry, and does not need special drinks. If a product promises "
                "dramatic results from a fancy form, you are paying for marketing.",
            ]),
            ("Do you need it?", [
                "No supplement is required to build muscle. Training with "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload</a>, eating enough protein (see "
                "<a href=\"/guides/how-much-protein-to-build-muscle\">how much "
                "protein you need</a>) and sleeping well matter far more.",
                "Once those are in place, creatine is the one supplement most "
                "worth considering. It costs very little per day, the downside "
                "for a healthy adult is a little water weight, and the upside is "
                "a small but real edge in every session.",
                "If you try it for two months and see no change in your training "
                "log, you may be one of the people who already have high stores. "
                "Stopping is perfectly reasonable; nothing bad happens when you do.",
            ]),
        ],
        "faq": [
            ("Should I cycle creatine on and off?",
             "There is no evidence that cycling is necessary. Your body does not "
             "build a tolerance, and stores drop back to baseline over about four "
             "to six weeks after you stop, so cycling mostly means losing the "
             "benefit for part of the year."),
            ("Can women take creatine?",
             "Yes. Research in women shows similar benefits for strength and "
             "lean mass, and women often have lower starting stores. The same 3 "
             "to 5 g daily dose applies; check with a doctor if pregnant or "
             "breastfeeding."),
            ("Will creatine make me fat?",
             "No. Creatine contains no calories worth counting. The early weight "
             "gain is water held inside muscle, typically 1 to 2 kg, and it "
             "levels off after the first few weeks."),
            ("Do I need to take creatine on rest days?",
             "Yes. Creatine works by keeping muscle stores saturated, so take "
             "your normal dose every day. Timing on rest days does not matter."),
            ("Is creatine a steroid?",
             "No. Creatine is a compound made naturally in your body from amino "
             "acids and found in meat and fish. It does not act like an anabolic "
             "steroid and is not banned by sports bodies."),
        ],
        "related_calcs": ["protein-calculator", "water-intake-calculator",
                          "lean-body-mass-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "how-many-sets-and-reps-for-muscle-growth",
        "title": "How Many Sets and Reps to Build Muscle",
        "desc": ("Weekly sets per muscle, the rep ranges that work, how close to "
                 "failure to train, and how to set up volume for beginners and "
                 "experienced lifters."),
        "h1": "How many sets and reps you need to build muscle",
        "category": "Muscle Building",
        "image": "dumbbells",
        "intro": ("The old rule of three sets of ten is not wrong, but it hides "
                  "the variables that actually drive growth: how many hard sets a "
                  "muscle gets each week, and how close those sets come to "
                  "failure. Get those two right and the exact rep number matters "
                  "much less than you were told."),
        "body": [
            ("Think in weekly sets, and count them properly", [
                "Muscle growth responds to the total amount of hard work a muscle "
                "does over a week. Researchers count this as <strong>hard sets "
                "per muscle per week</strong>: sets taken reasonably close to "
                "failure, counted for the muscles that do most of the work.",
                "A dose-response meta-analysis by Schoenfeld, Ogborn and Krieger "
                "(Journal of Sports Sciences, 2017) found that more weekly sets "
                "produced more growth, with 10 or more sets per muscle per week "
                "outperforming lower volumes. The gains get smaller with each "
                "extra set, and past a point, recovery suffers.",
                {"table": {
                    "head": ["Training age", "Hard sets per muscle per week"],
                    "rows": [
                        ["Beginner (under 1 year)", "6-10"],
                        ["Intermediate (1-3 years)", "10-16"],
                        ["Advanced (3+ years)", "12-20, varied by muscle"],
                    ],
                }},
                "These are starting points. Begin at the low end and add sets "
                "only when progress stalls and you are recovering well.",
                "A set counts for a muscle when that muscle is a main mover. A "
                "bench press counts for chest and triceps; a row counts for back "
                "and biceps. A practical shortcut used by many coaches is to "
                "count compound lifts as a full set for the prime mover and a "
                "half set for the assisting muscles.",
                "Warm-up sets do not count. Neither do sets you stop with six or "
                "more reps still in the tank. If you are not sure whether a set "
                "was hard, it probably was not.",
            ]),
            ("Rep ranges: wider than you think", [
                "Studies comparing heavy and light loads, including Schoenfeld et "
                "al. (Journal of Strength and Conditioning Research, 2017), show "
                "that sets of roughly 6 to 30 reps build similar muscle when they "
                "are taken close to failure. The rep count changes how the set "
                "feels, not whether it works.",
                {"table": {
                    "head": ["Reps", "Best used for", "Trade-off"],
                    "rows": [
                        ["1-5", "Maximal strength, skill on the big lifts", "Little volume per set, more joint stress"],
                        ["6-12", "Most compound and isolation work", "The efficient middle ground"],
                        ["12-20", "Isolation, machines, joint-friendly work", "Burning fatigue, harder to judge failure"],
                        ["20-30", "Small muscles, deload weeks, home training", "Long sets, cardiovascular fatigue limits you"],
                    ],
                }},
                "A sensible default is to do your main compound lifts in the 5 "
                "to 10 range and your accessories in the 8 to 15 range. Heavy "
                "sets still matter if you want to get strong; use the "
                "<a href=\"/one-rep-max-calculator\">one-rep max calculator</a> to "
                "pick loads by percentage.",
            ]),
            ("Proximity to failure and RIR", [
                "Effort is what makes a set count. Coaches measure it with "
                "<strong>reps in reserve (RIR)</strong>: how many more clean reps "
                "you could have done when you stopped.",
                {"list": [
                    "<strong>0 RIR:</strong> true failure, the next rep would not "
                    "go up.",
                    "<strong>1-2 RIR:</strong> the productive zone for most sets.",
                    "<strong>3-4 RIR:</strong> fine for heavy compound lifts and "
                    "technique work.",
                    "<strong>5+ RIR:</strong> too easy to count as a hard set.",
                ]},
                "Training to absolute failure on every set adds fatigue faster "
                "than it adds growth, especially on squats and deadlifts. Save "
                "0 RIR for the last set of an isolation exercise, where the risk "
                "is low.",
                {"tip": "Beginners nearly always underestimate how many reps they "
                        "have left. Once in a while, take a safe exercise like a "
                        "machine curl to true failure to calibrate your sense of "
                        "what 2 RIR feels like."},
            ]),
            ("How often to train each muscle", [
                "Hitting each muscle <strong>twice a week</strong> tends to produce "
                "slightly better growth than once a week at the same total volume "
                "(Schoenfeld, Ogborn and Krieger, Sports Medicine, 2016). The main "
                "benefit is practical: 14 sets of chest is far better spread over "
                "two sessions of 7 than crammed into one.",
                "Splits like the <a href=\"/workouts/upper-lower-split\">upper "
                "lower split</a> and <a href=\"/workouts/push-pull-legs\">push pull "
                "legs</a> naturally train each muscle twice weekly. A <a "
                "href=\"/workouts/beginner-full-body-workout\">full body routine</a> "
                "three days a week does the same with fewer exercises per session.",
                "Keep it to roughly 6 to 10 hard sets per muscle in any single "
                "session. Beyond that, the quality of later sets drops sharply.",
            ]),
            ("Rest between sets", [
                "Short rest periods feel productive but cut the reps you can do "
                "on the next set. For compound lifts, rest 2 to 3 minutes. For "
                "isolation exercises, 60 to 90 seconds is usually enough.",
                "A good rule: rest until your breathing has settled and you feel "
                "able to repeat the previous set's performance. Supersets of "
                "non-competing muscles, such as biceps with triceps, save time "
                "without much cost.",
            ]),
            ("A sample week", [
                "Here is how an intermediate lifter might reach about 12 weekly "
                "sets for chest across an upper/lower split:",
                {"table": {
                    "head": ["Day", "Exercise", "Sets x reps", "RIR"],
                    "rows": [
                        ["Upper A", "<a href=\"/exercises/bench-press\">Bench press</a>", "3 x 6-8", "2"],
                        ["Upper A", "<a href=\"/exercises/incline-dumbbell-press\">Incline dumbbell press</a>", "3 x 8-12", "1-2"],
                        ["Upper B", "Machine chest press", "3 x 10-12", "1"],
                        ["Upper B", "Cable fly", "3 x 12-15", "0-1"],
                    ],
                }},
                "Triceps also get indirect work from every press, which is why "
                "they need fewer direct sets than you might expect.",
            ]),
            ("Weekly volume by muscle group", [
                "Not every muscle needs the same direct work. Some get plenty of "
                "indirect volume from compound lifts; others recover quickly and "
                "tolerate more. These ranges are typical starting points for "
                "intermediates:",
                {"table": {
                    "head": ["Muscle", "Direct hard sets/week", "Notes"],
                    "rows": [
                        ["Chest", "10-16", "Presses and flies"],
                        ["Back (lats and upper back)", "12-18", "Mix vertical pulls and rows"],
                        ["Quads", "10-16", "Squats and leg presses are taxing; recover well"],
                        ["Hamstrings and glutes", "8-14", "Hinges like <a href=\"/exercises/romanian-deadlift\">Romanian deadlifts</a> plus curls"],
                        ["Shoulders (side and rear delts)", "8-16", "Front delts get lots from pressing"],
                        ["Biceps", "6-12", "Rows and pull-ups add indirect work"],
                        ["Triceps", "6-12", "Every press adds indirect work"],
                        ["Calves and abs", "6-12", "Recover quickly; can be trained often"],
                    ],
                }},
                "If you are prioritising one muscle, run it near the top of its "
                "range and pull a few sets from muscles you are happy to maintain. "
                "Maintenance needs surprisingly little: about a third of your "
                "normal volume, kept hard, is usually enough for a few months.",
            ]),
            ("Common mistakes", [
                {"list": [
                    "<strong>Junk volume:</strong> piling on sets that stop far "
                    "short of failure. Five easy sets do less than three hard ones.",
                    "<strong>Too many exercises:</strong> six chest movements for "
                    "two sets each makes it hard to track progress. Two or three "
                    "exercises done well is plenty.",
                    "<strong>Chasing soreness:</strong> soreness reflects novelty "
                    "more than growth. Rotating exercises constantly to feel sore "
                    "slows progress.",
                    "<strong>Copying advanced programs:</strong> a beginner does "
                    "not need 20 sets per muscle. Start low and earn the extra "
                    "volume.",
                    "<strong>Ignoring the log:</strong> without writing down "
                    "weights and reps you cannot tell whether your volume is "
                    "working.",
                ]},
            ]),
            ("Adjusting volume when cutting or short on time", [
                "In a calorie deficit, recovery drops. Many lifters do best cutting "
                "volume by 20 to 30 percent while keeping intensity high. Heavy, "
                "hard sets send the signal to keep muscle; extra sets mostly add "
                "fatigue you cannot recover from.",
                "If you only have 45 minutes, prioritise in this order: compound "
                "lifts for your weakest muscles, then the remaining compounds, "
                "then isolation work. Supersets and rest-pause sets can fit more "
                "hard sets into the time, at the cost of slightly less weight.",
                "A minimum effective dose for busy weeks is around 4 to 6 hard "
                "sets per muscle, spread over two sessions. That will hold most "
                "of your progress until life calms down.",
            ]),
            ("How to progress over time", [
                "Use a double progression: pick a rep range such as 8 to 12. When "
                "you hit 12 on every set at the target RIR, add weight and drop "
                "back to 8. This is <a href=\"/guides/progressive-overload-explained\">"
                "progressive overload</a> in its simplest form.",
                "If a muscle has stopped growing for six to eight weeks while "
                "your diet and sleep are in order, add one or two weekly sets "
                "for it. If you feel beaten up, performance is dropping and "
                "joints ache, cut volume back by a third for a week, then build "
                "up again.",
                "Expect progress to slow as you gain experience. A beginner can "
                "add weight almost every week; an advanced lifter may add a rep "
                "or two over a month. That is normal, not a sign the program has "
                "failed.",
                "None of this works without enough food. If you are eating in a "
                "large deficit, more sets will not save you. Check your intake "
                "with the <a href=\"/calorie-calculator\">calorie calculator</a> "
                "and <a href=\"/protein-calculator\">protein calculator</a>.",
            ]),
        ],
        "faq": [
            ("Is 3 sets of 10 enough to build muscle?",
             "It can be, as long as the sets are hard and the weekly total adds "
             "up. Three sets of 10 on two exercises for a muscle, done twice a "
             "week, gives 12 weekly sets, which is a solid amount for most "
             "people."),
            ("Are low reps or high reps better for muscle growth?",
             "Both work for growth when sets are taken close to failure, roughly "
             "anywhere from 6 to 30 reps. Low reps are better for building "
             "maximal strength, so most programs use a mix."),
            ("Can I do too many sets?",
             "Yes. Past about 20 hard sets per muscle per week, most people stop "
             "seeing extra growth and start accumulating fatigue and joint pain. "
             "If performance is falling, cut volume rather than adding more."),
            ("Do I need to train to failure?",
             "No. Stopping one to three reps short of failure gives nearly the "
             "same growth with less fatigue. Going to failure occasionally on "
             "isolation exercises is fine."),
        ],
        "related_calcs": ["one-rep-max-calculator", "protein-calculator",
                          "ffmi-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "pre-and-post-workout-nutrition",
        "title": "Pre and Post Workout Nutrition: What to Eat",
        "desc": ("What to eat before and after training, how much protein and "
                 "carbohydrate you need, whether the anabolic window is real, and "
                 "meal ideas for any schedule."),
        "h1": "What to eat before and after a workout",
        "category": "Nutrition",
        "image": "meal-prep",
        "intro": ("Workout nutrition gets more attention than it deserves, and "
                  "the basics get less. What you eat across the whole day decides "
                  "most of your results; the meals around training are about "
                  "feeling good in the session and recovering well from it."),
        "body": [
            ("Start with the daily totals", [
                "Before worrying about timing, make sure you hit three numbers "
                "most days: total calories for your goal, enough protein, and "
                "enough carbohydrate to fuel your training.",
                {"list": [
                    "<strong>Calories:</strong> set by your goal. The <a "
                    "href=\"/calorie-calculator\">calorie calculator</a> gives you "
                    "a target.",
                    "<strong>Protein:</strong> about 1.6 g per kg of bodyweight "
                    "(0.7 g per lb) covers most lifters. A meta-analysis by Morton "
                    "et al. (British Journal of Sports Medicine, 2018) found gains "
                    "in lean mass plateaued around 1.6 g/kg/day, with some "
                    "people benefiting from up to 2.2 g/kg.",
                    "<strong>Carbohydrate:</strong> 3 to 5 g per kg is a sensible "
                    "range for people lifting most days; endurance athletes need "
                    "more.",
                ]},
                "If those totals are off, perfect pre and post workout meals will "
                "not fix it. The <a href=\"/macro-calculator\">macro calculator</a> "
                "splits your calories into grams.",
            ]),
            ("Is the anabolic window real?", [
                "The idea that you must drink a shake within 30 minutes of "
                "training or lose your gains has been largely retired. A review "
                "by Aragon and Schoenfeld (Journal of the International Society "
                "of Sports Nutrition, 2013) concluded the window is much wider "
                "than once thought, at least several hours either side of the "
                "session.",
                "What matters is the gap between protein meals. If you ate a "
                "protein-rich meal two hours before training, your next meal can "
                "wait an hour or two afterwards. If you train fasted first thing "
                "in the morning, eating soon after is more useful.",
                {"tip": "Rule of thumb: get a protein-containing meal within "
                        "roughly two hours before and two hours after training. "
                        "That covers the window for almost everyone."},
            ]),
            ("What to eat before training (or not)", [
                "The pre-workout meal has two jobs: give you energy and not upset "
                "your stomach. Timing changes what you should eat.",
                {"table": {
                    "head": ["Time before training", "What to eat", "Example"],
                    "rows": [
                        ["2-3 hours", "Full balanced meal: protein, carbs, some fat and fibre", "Chicken, rice and vegetables; dal, rice and curd"],
                        ["1-2 hours", "Smaller meal, lower fat and fibre", "Greek yoghurt with banana and oats"],
                        ["30-60 minutes", "Light, mainly fast carbs plus a little protein", "Banana, toast with honey, a small protein shake"],
                        ["Under 30 minutes", "Only if needed: small, easily digested carbs", "Half a banana, a few dates, a sports drink"],
                    ],
                }},
                "Fat and fibre slow digestion, which is good most of the day but "
                "can sit heavily during squats or sprints. Keep them lower in the "
                "last hour before training.",
                "Aim for roughly 20 to 40 g of protein and 0.5 to 1 g of "
                "carbohydrate per kg of bodyweight in the meal before training. "
                "Longer or harder sessions justify the upper end.",
                "Lifting on an empty stomach is fine if you feel good doing it. "
                "Some people prefer it for early sessions. Research does not show "
                "that fasted training burns more body fat over time when total "
                "calories are equal.",
                "If you train fasted, you may lose a little performance on long or "
                "high-volume sessions. Eating protein soon afterwards matters more "
                "here, since it has been many hours since your last meal.",
            ]),
            ("Caffeine and other pre-workout ingredients", [
                "Caffeine is the active ingredient in most pre-workout products "
                "and the one with strong evidence. The ISSN position stand on "
                "caffeine (Guest et al., 2021) reports performance benefits at "
                "about 3 to 6 mg per kg of bodyweight, taken around 60 minutes "
                "before exercise.",
                "For a 70 kg person, that is roughly 200 to 400 mg, or two to "
                "four cups of brewed coffee. Start at the low end. More is not "
                "better and can wreck your sleep, which costs you more than the "
                "caffeine gains. Avoid it within six to eight hours of bed.",
                "Beta-alanine (the ingredient that causes tingling) and citrulline "
                "have some supporting evidence; most other pre-workout additives "
                "have little. Plain coffee and a banana do most of the job. "
                "Creatine works regardless of timing; see the <a "
                "href=\"/guides/creatine-guide\">creatine guide</a>.",
            ]),
            ("What to eat after training", [
                "After training, aim for a normal meal with protein and "
                "carbohydrate. Research on muscle protein synthesis suggests "
                "about 0.3 to 0.4 g of protein per kg of bodyweight per meal, "
                "which is 20 to 40 g for most people.",
                {"list": [
                    "Eggs on toast with fruit",
                    "Rice, beans or lentils with paneer, tofu or chicken",
                    "Greek yoghurt or skyr with granola and berries",
                    "A protein shake with milk and a banana if a meal is hours away",
                    "Tuna or chickpea wrap with salad",
                ]},
                "Carbohydrate after lifting refills muscle glycogen, which matters "
                "most if you train the same muscles again within 24 hours or do "
                "two sessions in a day. For one session a day, normal meals over "
                "the rest of the day refill it fully.",
                "Fat in the post-workout meal is fine. It slows digestion "
                "slightly but has not been shown to reduce muscle growth, so there "
                "is no need to strip it out of an otherwise good meal.",
            ]),
            ("Hydration", [
                "Being dehydrated by even 2 percent of bodyweight can reduce "
                "performance in longer sessions. Drink water through the day so "
                "your urine is pale, then sip during training.",
                "For long or sweaty sessions, weighing yourself before and after "
                "is a simple check: replace each kilogram lost with about 1.25 to "
                "1.5 litres of fluid over the next few hours. Use the <a "
                "href=\"/water-intake-calculator\">water intake calculator</a> "
                "for a daily baseline.",
            ]),
            ("Do you need anything during training?", [
                "For a typical 45 to 90 minute lifting session, water is all you "
                "need. Intra-workout carbohydrate drinks and amino acid powders "
                "add little when you have eaten in the hours before.",
                "Fuel during training starts to matter for sessions longer than "
                "about 90 minutes, hard endurance work, or two sessions in one "
                "day. Then, 30 to 60 g of carbohydrate per hour from a sports "
                "drink, banana or dates can help you keep performance up.",
                "Branched-chain amino acids (BCAAs) are a common add-on. If you "
                "already eat enough protein, research shows little extra benefit; "
                "the money is better spent on food.",
            ]),
            ("Workout nutrition when losing fat", [
                "In a calorie deficit, there is less food to go around, so it pays "
                "to place some of it around training. Moving a portion of your "
                "daily carbohydrate into the meals before and after your session "
                "can help you keep training quality high, which in turn helps "
                "you keep muscle.",
                {"list": [
                    "Keep protein high, around 1.8 to 2.2 g per kg, while dieting.",
                    "Put a larger share of carbs in the pre-workout meal.",
                    "Make the post-workout meal your largest protein meal.",
                    "Count drinks and pre-workout snacks; they add up quickly.",
                ]},
                "Fat loss still comes down to the weekly deficit. Use the <a "
                "href=\"/weight-loss-calculator\">weight loss calculator</a> to set "
                "a realistic rate, and read <a href=\"/guides/how-to-calculate-"
                "calories-for-weight-loss\">how to calculate calories for weight "
                "loss</a> for the details.",
            ]),
            ("Vegetarian and budget options", [
                "You do not need expensive powders or chicken breast at every "
                "meal. These foods give roughly 20 g of protein per serving and "
                "work well before or after training:",
                {"table": {
                    "head": ["Food", "Approx. serving for 20 g protein", "Notes"],
                    "rows": [
                        ["Greek yoghurt or hung curd", "200-250 g", "Easy pre-workout with fruit"],
                        ["Paneer", "100 g", "Higher fat, better 2+ hours before"],
                        ["Eggs", "3 large", "Cheap, versatile"],
                        ["Milk", "600 ml", "Good post-workout with a banana"],
                        ["Cooked lentils or chickpeas", "About 250 g", "Also high in carbs and fibre"],
                        ["Firm tofu", "About 130-150 g", "Varies by brand"],
                        ["Soya chunks (dry)", "About 40 g", "Very cheap per gram of protein"],
                        ["Whey or plant protein powder", "1 scoop (25-30 g)", "Convenient when a meal is far off"],
                    ],
                }},
                "Combining plant proteins across the day, such as grains with "
                "pulses, gives you a full range of amino acids. Vegans may want to "
                "aim slightly higher on total protein to make up for lower "
                "digestibility of some plant sources.",
            ]),
            ("Sample days by training time", [
                {"table": {
                    "head": ["Training time", "Before", "After"],
                    "rows": [
                        ["6 am", "Coffee and a banana, or nothing", "Breakfast within 1 hour: eggs, toast, fruit"],
                        ["12 pm", "Breakfast at 9: oats, milk, protein", "Lunch: rice, dal or chicken, vegetables"],
                        ["6 pm", "Snack at 4: yoghurt and fruit", "Dinner: protein, carbs, vegetables"],
                        ["9 pm", "Dinner at 6:30", "Small protein snack, e.g. milk or curd, before bed"],
                    ],
                }},
                "Late training does not need a large meal afterwards if you ate "
                "well earlier. A protein-rich snack before bed supports overnight "
                "recovery; see <a href=\"/guides/sleep-and-muscle-growth\">sleep "
                "and muscle growth</a>.",
            ]),
        ],
        "faq": [
            ("Do I need a protein shake after the gym?",
             "No. A shake is just a convenient source of protein. A normal meal "
             "with 20 to 40 g of protein within a couple of hours does the same "
             "job."),
            ("Should I eat carbs before a workout?",
             "For most sessions, yes, carbs eaten one to three hours before help "
             "you train harder, especially for longer or high-volume workouts. "
             "For short sessions, it matters less and comes down to preference."),
            ("Is it bad to work out on an empty stomach?",
             "Not for most healthy people. Some feel weaker or dizzy, in which "
             "case a small snack helps. Eat a proper meal with protein soon after "
             "a fasted session."),
            ("How long after eating should I work out?",
             "About two to three hours after a full meal, or 30 to 60 minutes "
             "after a light snack. Larger, fattier meals need more time to "
             "settle."),
        ],
        "related_calcs": ["macro-calculator", "protein-calculator",
                          "calorie-calculator", "water-intake-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "rest-days-and-recovery",
        "title": "Rest Days and Recovery: How Much Do You Need?",
        "desc": ("How many rest days you need, what to do on them, the signs you "
                 "are under-recovered, and how to plan deloads so you keep making "
                 "progress in the gym."),
        "h1": "Rest days and recovery: how much you need and what to do",
        "category": "Health & Recovery",
        "image": "stretching",
        "intro": ("Training breaks you down; recovery is when you get better. "
                  "Skip enough of it and progress stalls, motivation fades and "
                  "small aches turn into injuries. Here is how to plan rest so it "
                  "works for you."),
        "body": [
            ("Why rest is part of the program", [
                "A hard session leaves you temporarily weaker. Over the next one "
                "to three days, your body repairs muscle tissue, refills energy "
                "stores and adapts so it can handle that stress better next time. "
                "Coaches call this cycle stress, recovery, adaptation.",
                "Train the same muscles hard again before that process finishes "
                "and you dig a deeper hole instead of climbing out of it. Leave "
                "too long between sessions and the stimulus fades. Good programs "
                "sit in between.",
                "Recovery is also not only about muscle. Tendons and ligaments "
                "adapt more slowly than muscle, which is why beginners who add "
                "weight quickly often feel their elbows or knees before their "
                "muscles complain. Your nervous system, energy stores and even "
                "your motivation all need time to bounce back after hard weeks.",
            ]),
            ("How many rest days per week", [
                "Most people make their best progress training three to five "
                "days a week, with at least one or two full rest days.",
                {"table": {
                    "head": ["Training days", "Rest days", "Good fit for"],
                    "rows": [
                        ["3", "4", "Beginners, busy schedules, <a href=\"/workouts/beginner-full-body-workout\">full body plans</a>"],
                        ["4", "3", "Most intermediates, <a href=\"/workouts/upper-lower-split\">upper/lower splits</a>"],
                        ["5-6", "1-2", "Experienced lifters, <a href=\"/workouts/push-pull-legs\">push pull legs</a>"],
                        ["7", "0", "Not recommended for hard training"],
                    ],
                }},
                "Training six days a week can work if sessions are split by "
                "muscle group so each one gets around 48 to 72 hours before it is "
                "trained hard again. You still need at least one day off.",
            ]),
            ("How long muscles need between sessions", [
                "A muscle trained hard generally needs about 48 to 72 hours "
                "before being trained hard again. Several factors stretch or "
                "shrink that:",
                {"list": [
                    "<strong>Volume and effort:</strong> 12 sets to failure needs "
                    "longer than 6 sets at 2-3 reps in reserve.",
                    "<strong>Exercise:</strong> heavy squats and deadlifts cause "
                    "more systemic fatigue than curls.",
                    "<strong>New exercises:</strong> unfamiliar movements cause "
                    "much more soreness for the first week or two.",
                    "<strong>Age, sleep, stress and diet:</strong> all slow or "
                    "speed recovery.",
                ]},
                "Soreness is a poor guide on its own. You can grow without it, and "
                "mild soreness does not mean you must rest. Judge readiness by "
                "how your warm-up sets feel and whether your performance is "
                "holding up.",
            ]),
            ("Signs you are not recovering", [
                "Missing recovery for a week or two is called overreaching and "
                "clears up with rest. Ignoring it for months can lead to a longer "
                "slump. Watch for clusters of these signs:",
                {"list": [
                    "Weights that normally move well feel heavy for two or more "
                    "sessions in a row",
                    "Resting heart rate a few beats above your usual baseline for "
                    "several mornings",
                    "Poor sleep despite feeling tired",
                    "Persistent joint aches, not just muscle soreness",
                    "Low motivation, irritability, or frequent minor illnesses",
                ]},
                "One bad session means nothing. Three in a row, plus poor sleep "
                "and dread before training, means take a few easy days.",
                "Mental fatigue counts too. Work deadlines, family stress and "
                "poor sleep draw on the same recovery resources as training. In "
                "a heavy week at work, a lighter week in the gym is not a failure; "
                "it is good planning. Training through life stress at full "
                "intensity is one of the most common routes to burnout and "
                "nagging injuries.",
                {"tip": "Track your resting heart rate each morning before getting "
                        "up. A sustained rise of 5 or more beats above your normal "
                        "is a useful early warning. The <a "
                        "href=\"/heart-rate-zone-calculator\">heart rate zone "
                        "calculator</a> explains how resting rate is measured."},
            ]),
            ("Active recovery: what to do on rest days", [
                "Rest days do not have to mean the sofa. Light activity increases "
                "blood flow and can reduce stiffness without adding fatigue.",
                {"list": [
                    "A 30 to 60 minute walk",
                    "Easy cycling or swimming at a conversational pace",
                    "Mobility work or gentle yoga",
                    "Playing a sport casually, without sprinting or heavy contact",
                ]},
                "Keep effort low: you should be able to talk comfortably. If it "
                "feels like a workout, it is one. Daily steps also count toward "
                "calorie burn; the <a href=\"/calories-burned-calculator\">calories "
                "burned calculator</a> estimates how much.",
            ]),
            ("Deload weeks", [
                "Fatigue builds slowly across weeks of hard training even when "
                "individual rest days look fine. A <strong>deload</strong> is a "
                "planned easy week that clears it.",
                "Most lifters benefit from a deload every 4 to 8 weeks, or "
                "whenever progress stalls and the signs above appear. Two simple "
                "ways to run one:",
                {"olist": [
                    "Keep the same weights but cut sets roughly in half.",
                    "Keep the same sets but reduce the load by about 30 to 40 "
                    "percent and stop well short of failure.",
                ]},
                "You may feel a little restless. That is the point. Most people "
                "come back the following week stronger than before.",
                "Beginners rarely need formal deloads in their first few months, "
                "because the weights are still light relative to their potential. "
                "Once you have been training consistently for six months or more, "
                "build them into your plan rather than waiting to feel run down.",
            ]),
            ("The recovery basics that matter most", [
                "Massage guns, ice baths and supplements get attention, but their "
                "effects are small. The big levers are dull and reliable:",
                {"table": {
                    "head": ["Factor", "Target"],
                    "rows": [
                        ["Sleep", "7-9 hours a night, consistent schedule"],
                        ["Protein", "About 1.6 g per kg bodyweight daily"],
                        ["Calories", "Not too far below maintenance"],
                        ["Hydration", "Pale urine through the day"],
                        ["Stress", "Train lighter in high-stress weeks"],
                    ],
                }},
                "Sleep in particular has an outsized effect; see <a "
                "href=\"/guides/sleep-and-muscle-growth\">sleep and muscle "
                "growth</a>. Check protein needs with the <a "
                "href=\"/protein-calculator\">protein calculator</a>.",
                "Note that cold water immersion straight after lifting may blunt "
                "muscle growth slightly in some studies. Save ice baths for "
                "competition periods when fast recovery matters more than "
                "long-term gains.",
            ]),
            ("Sample weekly schedules", [
                "Where you put rest days matters as much as how many you take. "
                "Spread them so hard sessions for the same muscles never land on "
                "back-to-back days.",
                {"table": {
                    "head": ["Plan", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                    "rows": [
                        ["3-day full body", "Train", "Rest", "Train", "Rest", "Train", "Active", "Rest"],
                        ["4-day upper/lower", "Upper", "Lower", "Rest", "Upper", "Lower", "Active", "Rest"],
                        ["5-day hybrid", "Upper", "Lower", "Rest", "Push", "Pull", "Legs", "Rest"],
                        ["6-day PPL", "Push", "Pull", "Legs", "Push", "Pull", "Legs", "Rest"],
                    ],
                }},
                "If you miss a day, do not cram two sessions together. Shift the "
                "week along by a day or skip the missed session. Consistency over "
                "months matters far more than any one workout.",
            ]),
            ("Stretching, massage and recovery tools", [
                "Plenty of recovery products promise faster bounce-back. The "
                "evidence for most of them is modest: they may make you feel "
                "better, which has value, but they will not make up for poor "
                "sleep or a crash diet.",
                {"table": {
                    "head": ["Tool", "What it does well", "Limits"],
                    "rows": [
                        ["Foam rolling", "Short-term reduction in stiffness and soreness", "Effects last minutes to hours"],
                        ["Massage or massage gun", "Feels good, may ease soreness", "Small effect on actual muscle repair"],
                        ["Static stretching", "Improves flexibility over weeks", "Does not prevent soreness"],
                        ["Compression garments", "May reduce perceived soreness", "Small, inconsistent effects"],
                        ["Sauna", "Relaxation, possible heat adaptation", "Dehydrating; drink water"],
                    ],
                }},
                "If a tool helps you relax and you enjoy it, keep using it. Just "
                "spend your effort on the basics first.",
            ]),
            ("Recovery as you get older or diet", [
                "Recovery slows gradually with age, often noticeably from the "
                "40s onward. That does not mean training less hard; it means "
                "planning more carefully.",
                {"list": [
                    "Allow an extra day between hard sessions for the same muscles.",
                    "Use slightly higher reps (8 to 15) on joint-heavy lifts.",
                    "Spend longer on warm-ups, building up with three or four sets.",
                    "Keep protein at the higher end; older muscles respond less to "
                    "small doses, so 30 to 40 g per meal is a good target.",
                    "Deload more often, every 4 to 6 weeks.",
                ]},
                "Strength training remains one of the best things you can do as "
                "you age, for muscle, bone density and independence. Adjust the "
                "recovery, not the commitment.",
                "In a calorie deficit, recovery slows. You have less energy to "
                "repair tissue and sleep often suffers. Keep the deficit moderate, "
                "around 0.5 to 1 percent of bodyweight lost per week, keep protein "
                "high and consider trimming volume by 20 to 30 percent rather than "
                "adding more training.",
                "The <a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
                "guide to calculating calories for weight loss</a> shows how to "
                "set a deficit you can recover from.",
            ]),
        ],
        "faq": [
            ("Is it OK to work out every day?",
             "Light activity like walking can be done daily. Hard training every "
             "day without a rest day raises the risk of fatigue and injury, so "
             "most people should take at least one full day off each week."),
            ("Should I train if I am still sore?",
             "Mild soreness is fine; light movement often eases it. If soreness "
             "is severe, limits your range of motion, or affects your technique, "
             "train a different muscle group or rest."),
            ("How long does it take muscles to recover?",
             "Typically 48 to 72 hours after a hard session. Large compound lifts "
             "and new exercises may need longer, while lighter sessions need "
             "less."),
            ("Will I lose muscle if I take a week off?",
             "No. Meaningful muscle loss takes several weeks of complete "
             "inactivity. A week off often leaves people feeling stronger when "
             "they return."),
        ],
        "related_calcs": ["heart-rate-zone-calculator", "protein-calculator",
                          "calories-burned-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "cardio-for-fat-loss-hiit-vs-liss",
        "title": "HIIT vs LISS Cardio for Fat Loss: Which Is Better?",
        "desc": ("HIIT or steady-state cardio for fat loss? What the research "
                 "shows, calories burned, the effect on lifting, and a weekly "
                 "cardio plan to follow."),
        "h1": "HIIT vs LISS: which cardio is better for fat loss?",
        "category": "Fat Loss",
        "image": "running",
        "intro": ("High-intensity intervals are sold as the fat-burning shortcut; "
                  "steady walking and cycling are sold as the gentle, sustainable "
                  "option. Both work. The better choice depends on your time, your "
                  "recovery and how much you lift."),
        "body": [
            ("The two types, defined", [
                "<strong>HIIT (high-intensity interval training)</strong> "
                "alternates short, hard efforts with recovery. A typical session "
                "is 6 to 10 rounds of 20 to 60 seconds hard, with equal or longer "
                "easy periods, totalling 15 to 25 minutes including warm-up.",
                "<strong>LISS (low-intensity steady state)</strong> is continuous "
                "work at an easy to moderate pace: brisk walking, easy cycling, "
                "rowing or swimming for 30 to 60 minutes. You can hold a "
                "conversation throughout.",
                "Between them sits moderate-intensity continuous training, such "
                "as a steady 30-minute jog, which many studies use as the "
                "comparison.",
                {"table": {
                    "head": ["", "HIIT", "LISS"],
                    "rows": [
                        ["Heart rate", "85-95% of max in work intervals", "60-70% of max"],
                        ["Session length", "15-25 minutes", "30-60+ minutes"],
                        ["Sessions per week", "1-3", "3-7"],
                        ["Recovery cost", "High", "Low"],
                        ["Skill or fitness needed", "Moderate base fitness", "Almost none"],
                    ],
                }},
                "Use the <a href=\"/heart-rate-zone-calculator\">heart rate zone "
                "calculator</a> to find your own numbers.",
            ]),
            ("What the research says about fat loss", [
                "Head-to-head studies show that both approaches reduce body fat, "
                "and the difference between them is small. A meta-analysis by "
                "Wewege et al. (Obesity Reviews, 2017) found that interval "
                "training and moderate continuous training produced similar "
                "reductions in body fat, with intervals taking roughly 40 percent "
                "less time.",
                "Some later analyses, such as Viana et al. (British Journal of "
                "Sports Medicine, 2019), reported a modestly greater fat loss "
                "with interval training, particularly sprint intervals. Even "
                "there, the absolute differences were small compared with the "
                "effect of diet.",
                "The so-called afterburn (excess post-exercise oxygen consumption) "
                "is real but modest, usually adding only a few dozen extra "
                "calories, not the hundreds often claimed.",
                "Fat loss is also not the only reason to do cardio. The World "
                "Health Organization recommends adults get 150 to 300 minutes of "
                "moderate activity, or 75 to 150 minutes of vigorous activity, "
                "each week, alongside muscle strengthening on two or more days. "
                "Both HIIT and LISS count towards that, and both improve heart "
                "health, blood pressure and blood sugar control.",
                {"tip": "Cardio supports fat loss; your calorie deficit drives it. "
                        "Set that first with the <a "
                        "href=\"/calorie-calculator\">calorie calculator</a>, then "
                        "choose cardio you will keep doing."},
            ]),
            ("Calories burned: a realistic comparison", [
                "Per minute, HIIT burns more. Per session, longer steady cardio "
                "often matches or beats it, because you can do much more of it. "
                "Rough figures for a 75 kg (165 lb) person:",
                {"table": {
                    "head": ["Session", "Duration", "Approx. calories"],
                    "rows": [
                        ["Brisk walk, 6 km/h", "45 min", "250-300"],
                        ["Easy cycling", "45 min", "300-400"],
                        ["Steady jog, 9 km/h", "30 min", "330-380"],
                        ["Bike sprint intervals", "20 min incl. warm-up", "200-280"],
                        ["Rowing intervals", "20 min incl. warm-up", "220-300"],
                    ],
                }},
                "Estimates vary with fitness and body size. Get a figure for your "
                "own weight with the <a href=\"/calories-burned-calculator\">"
                "calories burned calculator</a>.",
            ]),
            ("How each affects your lifting", [
                "Cardio and strength training compete for recovery. This is "
                "called the interference effect, and it is strongest when cardio "
                "is high-impact, high-volume, and done close to leg training.",
                {"list": [
                    "<strong>HIIT</strong> is demanding on the legs and nervous "
                    "system. Two or three sessions a week can eat into squat and "
                    "deadlift performance if placed badly.",
                    "<strong>LISS</strong>, especially walking or cycling, has "
                    "little effect on lifting and may help recovery.",
                    "<strong>Running</strong> has more impact than cycling or "
                    "rowing, so it interferes more with leg training.",
                ]},
                "If muscle and strength are your priority, lean towards LISS and "
                "keep HIIT to one or two short sessions. Separate hard cardio from "
                "leg days by at least 24 hours, or do it after lifting rather "
                "than before.",
            ]),
            ("Don't overlook steps", [
                "Non-exercise activity, such as walking around, taking stairs and "
                "standing, often burns more calories across a week than formal "
                "cardio. It also tends to drop without you noticing when you "
                "diet, which is one reason fat loss slows.",
                "A daily step target is the simplest form of LISS. Moving from "
                "4,000 to 9,000 steps a day can add roughly 200 to 300 calories of "
                "daily burn for many people, with almost no recovery cost.",
            ]),
            ("Who should choose which", [
                {"table": {
                    "head": ["Situation", "Better choice"],
                    "rows": [
                        ["Short on time", "HIIT, 2 x 20 minutes a week"],
                        ["Beginner or very deconditioned", "LISS; build a base first"],
                        ["Heavy lifting 4+ days a week", "Mostly LISS, max 1 HIIT"],
                        ["Joint pain or high bodyweight", "LISS on bike, rower or in water"],
                        ["Want better fitness (VO2 max)", "Mix both"],
                        ["Deep in a diet, low energy", "LISS and steps"],
                    ],
                }},
                "Ask your doctor before starting HIIT if you have heart disease, "
                "high blood pressure, or have been inactive for a long time.",
                "Most people end up doing best with a mix: plenty of easy "
                "movement as the base, plus a small dose of hard intervals once "
                "fitness allows. The easy work burns calories and aids recovery; "
                "the intervals build fitness quickly and keep sessions short.",
                "Whatever you choose, judge it after six to eight weeks by your "
                "weekly average weight, waist measurement and how your lifting is "
                "going, not by how exhausted a single session leaves you.",
            ]),
            ("A weekly plan that combines both", [
                "This template works alongside three or four lifting sessions, "
                "for example the <a href=\"/workouts/fat-loss-workout-plan\">fat "
                "loss workout plan</a> or an <a href=\"/workouts/upper-lower-split\">"
                "upper lower split</a>:",
                {"table": {
                    "head": ["Day", "Lifting", "Cardio"],
                    "rows": [
                        ["Mon", "Upper", "20-30 min walk"],
                        ["Tue", "Lower", "None or easy walk"],
                        ["Wed", "Rest", "40-45 min LISS"],
                        ["Thu", "Upper", "15-20 min HIIT after lifting"],
                        ["Fri", "Lower", "20-30 min walk"],
                        ["Sat", "Rest", "45-60 min LISS"],
                        ["Sun", "Rest", "Easy walk"],
                    ],
                }},
                "Plus a daily step target of 7,000 to 10,000. Start with less if "
                "you are new and add one session every week or two.",
            ]),
            ("Choosing the best LISS for you", [
                "The best steady cardio is the one you will do three to five times "
                "a week without dreading it or getting hurt. Each option has a "
                "different trade-off:",
                {"table": {
                    "head": ["Activity", "Joint impact", "Leg fatigue", "Notes"],
                    "rows": [
                        ["Walking (incl. incline)", "Very low", "Very low", "Easiest to fit into daily life"],
                        ["Cycling (outdoor or stationary)", "Very low", "Low to moderate", "Good for heavier people"],
                        ["Swimming", "None", "Low", "Technique limits intensity for beginners"],
                        ["Rowing machine", "Low", "Moderate", "Works the whole body"],
                        ["Elliptical", "Low", "Low", "Easy to hold a steady heart rate"],
                        ["Jogging", "High", "Moderate to high", "Build up mileage slowly"],
                    ],
                }},
                "Incline treadmill walking deserves a mention: at a 10 to 12 "
                "percent incline and a moderate pace, it pushes your heart rate up "
                "without the impact of running, and it barely touches your "
                "lifting recovery.",
            ]),
            ("Common cardio mistakes", [
                {"list": [
                    "<strong>Eating it back:</strong> fitness trackers often "
                    "overestimate calories burned, and many people eat more after "
                    "cardio. Do not add cardio calories back to your diet unless "
                    "you are losing weight faster than planned.",
                    "<strong>Doing HIIT too often:</strong> intervals done four or "
                    "five times a week stop being high intensity. Quality drops and "
                    "fatigue builds.",
                    "<strong>All grey-zone effort:</strong> many people do every "
                    "session at a medium-hard pace that is neither easy enough to "
                    "recover from nor hard enough to count as intervals. Make easy "
                    "days easy and hard days hard.",
                    "<strong>Starting too big:</strong> going from zero to an hour "
                    "a day leads to sore joints and quitting. Add 10 to 15 minutes "
                    "per week.",
                    "<strong>Replacing lifting with cardio:</strong> while dieting, "
                    "lifting is what tells your body to keep muscle. Keep it in.",
                ]},
            ]),
            ("A simple HIIT session to start with", [
                {"olist": [
                    "Warm up for 5 minutes at an easy pace on a bike or rower.",
                    "Go hard for 30 seconds, at roughly 8 out of 10 effort.",
                    "Recover for 90 seconds at an easy pace.",
                    "Repeat 6 times. Add a round every week up to 10.",
                    "Cool down for 5 minutes.",
                ]},
                "Bikes and rowers are safer for intervals than sprinting, which "
                "has a higher injury risk if you have not sprinted in years. As "
                "fitness improves, shorten recovery to 60 seconds before adding "
                "rounds.",
            ]),
        ],
        "faq": [
            ("Is HIIT better than walking for fat loss?",
             "Per minute, HIIT burns more calories, but walking can be done daily "
             "for long periods with almost no fatigue. Over a week, both lead to "
             "similar fat loss when diet is the same."),
            ("Does cardio kill muscle gains?",
             "Moderate amounts do not, especially low-impact cardio like walking "
             "or cycling. Large volumes of running or hard intervals close to leg "
             "sessions can reduce strength and muscle gains."),
            ("How many times a week should I do HIIT?",
             "One to three sessions is plenty. More than that adds fatigue that "
             "can hurt your lifting and raises injury risk."),
            ("Should I do cardio before or after weights?",
             "If strength or muscle is your priority, lift first. Light cardio as "
             "a warm-up is fine, but hard cardio before lifting reduces "
             "performance."),
            ("Is fasted cardio better for burning fat?",
             "Fasted cardio burns a higher proportion of fat during the session, "
             "but studies show no extra fat loss over time when daily calories "
             "are equal. Choose whichever timing you prefer."),
        ],
        "related_calcs": ["calories-burned-calculator",
                          "heart-rate-zone-calculator", "calorie-calculator",
                          "weight-loss-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "how-to-measure-body-fat-at-home",
        "title": "How to Measure Body Fat at Home Accurately",
        "desc": ("Compare tape measure, skinfold calipers, smart scales and "
                 "progress photos for measuring body fat at home, with accuracy, "
                 "costs and step-by-step methods."),
        "h1": "How to measure body fat at home (and which method to trust)",
        "category": "Health & Recovery",
        "image": "measuring-tape",
        "intro": ("Bodyweight tells you how heavy you are, not what that weight "
                  "is made of. Tracking body fat shows whether you are losing fat, "
                  "building muscle, or both. No home method is precise, but the "
                  "right one used consistently is very useful."),
        "body": [
            ("Accuracy versus consistency", [
                "Every home method has error. A tape or caliper estimate might "
                "be 3 or 4 percentage points off your true value. That sounds "
                "bad, but if the error is roughly the same each time, the "
                "<strong>trend</strong> is still reliable.",
                "So the goal is not a perfect number. It is to pick one method, "
                "measure the same way under the same conditions, and watch the "
                "direction over weeks. Switching methods makes the numbers "
                "impossible to compare.",
            ]),
            ("The methods compared", [
                {"table": {
                    "head": ["Method", "Typical error", "Cost", "Best for"],
                    "rows": [
                        ["Tape measure (US Navy formula)", "About ±3-4%", "Very low", "Most people; simple trend tracking"],
                        ["Skinfold calipers", "About ±3-5%, less with a skilled tester", "Low", "Lean people; tracking specific sites"],
                        ["Smart scale (BIA)", "About ±4-8%, varies with hydration", "Moderate", "Convenience; long-term averages"],
                        ["Progress photos", "Not numerical", "Free", "Visual change, combined with any method"],
                        ["DEXA scan (clinic)", "About ±1-2%", "High", "A reference point once or twice a year"],
                    ],
                }},
                "Error ranges are approximate and depend heavily on technique, "
                "the device and the individual. Even DEXA, often treated as the "
                "gold standard, varies between machines and with hydration.",
            ]),
            ("Method 1: the tape measure", [
                "The US Navy method estimates body fat from height and a few "
                "circumferences. It needs only a flexible tape and two minutes, "
                "and our <a href=\"/body-fat-calculator\">body fat calculator</a> "
                "does the maths.",
                {"olist": [
                    "<strong>Neck:</strong> measure just below the Adam's apple, "
                    "tape sloping slightly down at the front.",
                    "<strong>Waist (men):</strong> horizontally at the level of the "
                    "navel.",
                    "<strong>Waist (women):</strong> at the narrowest point, "
                    "usually just above the navel.",
                    "<strong>Hips (women):</strong> at the widest point of the "
                    "buttocks.",
                    "Take each measurement three times and use the average.",
                ]},
                "Keep the tape snug but not compressing the skin, stand relaxed "
                "and measure at the end of a normal breath out. Do not suck in. "
                "Its weakness: people who carry fat mainly on the hips or legs, or "
                "who have very thick necks from training, can be misestimated.",
                {"tip": "Even if you never convert to body fat, waist measurement "
                        "alone is a strong progress marker. A shrinking waist with "
                        "stable weight usually means you are recomposing. See the "
                        "<a href=\"/waist-to-hip-ratio-calculator\">waist to hip "
                        "ratio calculator</a> for a health angle."},
            ]),
            ("Method 2: skinfold calipers", [
                "Calipers pinch a fold of skin and fat at set sites and measure "
                "its thickness. Formulas such as Jackson-Pollock then estimate "
                "total body fat. A 3-site or 7-site test is most common.",
                {"list": [
                    "Men, 3-site: chest, abdomen, thigh",
                    "Women, 3-site: triceps, suprailiac (above the hip bone), thigh",
                ]},
                "Measure on the right side of the body, pinch the fold firmly "
                "between thumb and finger, place the caliper about 1 cm away, "
                "and read after two seconds. Take two or three readings per site.",
                "Calipers work well for lean people and for tracking individual "
                "sites over time. They are harder to use on yourself, so ask the "
                "same person to measure you each time if possible. In people with "
                "higher body fat, folds can be too thick to measure reliably.",
            ]),
            ("Method 3: smart scales (bioelectrical impedance)", [
                "Smart scales send a small, harmless current through your body. "
                "Fat conducts electricity less well than water-rich lean tissue, "
                "so the resistance is used to estimate body fat.",
                "The catch is that the reading depends heavily on hydration. A "
                "large drink, a salty meal, a workout or a hot shower can shift "
                "the result by several percentage points in a day. Foot-only "
                "scales mainly read your lower body.",
                "Use them for the long-term average, not the daily number. Weigh "
                "at the same time each morning after using the bathroom and "
                "before eating or drinking, then look at the weekly average. "
                "People with pacemakers or other implanted devices should not "
                "use BIA scales, and they are generally not recommended during "
                "pregnancy.",
            ]),
            ("Method 4: progress photos", [
                "Photos cannot give you a percentage, but they are often the most "
                "motivating record of change, because day-to-day you see yourself "
                "too often to notice it.",
                {"list": [
                    "Same place, same lighting, same time of day",
                    "Front, side and back, relaxed and flexed",
                    "Phone at the same height and distance each time",
                    "Every 2 to 4 weeks is enough",
                ]},
            ]),
            ("How often to measure, and mistakes to avoid", [
                "Body fat changes slowly. Losing 0.5 kg (1 lb) of fat a week "
                "moves body fat percentage by roughly half a point per week for "
                "many people, which is inside the error of most methods. Measuring "
                "daily mostly records noise.",
                {"table": {
                    "head": ["Measure", "How often"],
                    "rows": [
                        ["Bodyweight", "Daily, use the weekly average"],
                        ["Waist and tape measurements", "Every 1-2 weeks"],
                        ["Calipers or tape body fat estimate", "Every 2-4 weeks"],
                        ["Photos", "Every 2-4 weeks"],
                        ["DEXA (optional)", "Every 6-12 months"],
                    ],
                }},
                {"list": [
                    "<strong>Changing the time of day.</strong> You are taller and "
                    "lighter in the morning, and your waist grows after meals. "
                    "Always measure first thing, before eating.",
                    "<strong>Measuring after training.</strong> Muscles are pumped "
                    "and fluid shifts for hours. Wait until the next morning.",
                    "<strong>Pulling the tape tight.</strong> Compressing the skin "
                    "shaves centimetres off. Snug, not squeezing.",
                    "<strong>Moving the landmarks.</strong> Measure the waist at "
                    "the navel every time, not wherever looks smallest.",
                    "<strong>Ignoring the menstrual cycle.</strong> Water retention "
                    "can add 1 to 2 kg and change tape and BIA readings. Compare "
                    "the same point in your cycle month to month.",
                    "<strong>Reacting to one reading.</strong> Decide only on "
                    "trends across at least three measurements.",
                ]},
            ]),
            ("Example: tracking a 12-week cut", [
                "Here is what realistic numbers look like for someone who starts "
                "at 85 kg (187 lb) and around 24 percent body fat, losing about "
                "0.5 kg a week while lifting three times weekly.",
                {"table": {
                    "head": ["Week", "Weight (avg)", "Waist", "Tape body fat", "Lean mass"],
                    "rows": [
                        ["0", "85.0 kg", "94 cm", "24%", "64.6 kg"],
                        ["4", "83.1 kg", "92 cm", "22.5%", "64.4 kg"],
                        ["8", "81.0 kg", "89.5 cm", "21%", "64.0 kg"],
                        ["12", "79.2 kg", "87 cm", "19%", "64.2 kg"],
                    ],
                }},
                "Notice that individual readings wobble: lean mass appears to dip "
                "then recover, which is measurement noise. The overall picture is "
                "clear, though: about 6 kg lost, almost all of it fat, and a 7 cm "
                "smaller waist. That is a successful cut, even if no single "
                "number was perfect.",
            ]),
            ("When the scale and tape disagree", [
                "Sometimes your weight stays flat while your waist shrinks, or the "
                "scale drops but the mirror looks the same. Here is how to read it:",
                {"table": {
                    "head": ["Scale", "Waist", "Likely meaning"],
                    "rows": [
                        ["Down", "Down", "Losing fat; on track"],
                        ["Flat", "Down", "Recomposition, or water masking fat loss"],
                        ["Up", "Flat or down", "Gaining muscle, glycogen or water (e.g. new creatine)"],
                        ["Up", "Up", "Gaining fat; check calories"],
                        ["Down fast", "Flat", "Mostly water or glycogen, common in week one of a diet"],
                    ],
                }},
                "Give any surprising reading two weeks before acting on it. If you "
                "are deliberately trying to lose fat and build muscle together, "
                "read the <a href=\"/guides/body-recomposition-guide\">body "
                "recomposition guide</a>.",
            ]),
            ("What to do with your number", [
                "A body fat estimate is more useful than <a "
                "href=\"/guides/bmi-vs-body-fat-percentage\">BMI</a> for people "
                "who lift, because BMI cannot tell muscle from fat. Use your "
                "result to:",
                {"list": [
                    "Work out lean mass with the <a href=\"/lean-body-mass-calculator\">"
                    "lean body mass calculator</a>",
                    "Check how muscular you are relative to height with the <a "
                    "href=\"/ffmi-calculator\">FFMI calculator</a>",
                    "Set a goal weight: lean mass divided by (1 minus target body "
                    "fat fraction)",
                    "Decide between a cut or a bulk; see <a "
                    "href=\"/guides/bulking-vs-cutting\">bulking vs cutting</a>",
                ]},
                "Rough healthy ranges for adults are about 10 to 22 percent for "
                "men and 20 to 32 percent for women, varying with age. Very low "
                "levels are not healthier and can disrupt hormones, especially in "
                "women.",
                "If you notice yourself measuring obsessively, or the numbers are "
                "affecting how you eat or feel about yourself, take a break from "
                "tracking and consider speaking to a doctor. Progress photos and "
                "training performance are perfectly good ways to judge progress.",
            ]),
        ],
        "faq": [
            ("What is the most accurate way to measure body fat at home?",
             "Skinfold calipers in skilled hands and the tape measure method are "
             "usually more consistent than smart scales. Whichever you choose, "
             "using it the same way every time matters more than the method."),
            ("Are smart scales accurate for body fat?",
             "They are not very accurate on any given day because hydration "
             "changes the reading. Averaged over weeks under the same conditions, "
             "they can show a useful trend."),
            ("Why did my body fat jump overnight?",
             "Real fat does not change that quickly. Overnight jumps come from "
             "hydration, food in the gut, salt intake or measurement technique. "
             "Look at the trend over several weeks."),
            ("How accurate is the US Navy body fat method?",
             "Studies usually find it within about 3 to 4 percentage points of "
             "lab methods for most people. It tends to be less accurate for very "
             "muscular or very lean people."),
        ],
        "related_calcs": ["body-fat-calculator", "lean-body-mass-calculator",
                          "ffmi-calculator", "waist-to-hip-ratio-calculator"],
    },

    # -----------------------------------------------------------------------
    {
        "slug": "sleep-and-muscle-growth",
        "title": "Sleep and Muscle Growth: How Much Sleep You Need",
        "desc": ("How sleep affects muscle growth, strength and fat loss, how "
                 "many hours you need, and practical steps to sleep better when "
                 "you train hard and diet."),
        "h1": "Sleep and muscle growth: why your gains depend on it",
        "category": "Health & Recovery",
        "image": "sleep",
        "intro": ("Lifters will track every gram of protein and then sleep six "
                  "hours a night. Sleep is when much of your recovery happens, "
                  "and cutting it short quietly undermines your strength, your "
                  "muscle gains and your fat loss."),
        "body": [
            ("How much sleep you need", [
                "The American Academy of Sleep Medicine and Sleep Research "
                "Society recommend that adults get <strong>7 or more hours</strong> "
                "a night regularly. Most people who train hard do best with 7 to "
                "9 hours; teenagers need more, about 8 to 10.",
                "Time in bed is not the same as time asleep. If you are in bed for "
                "7 hours, you might sleep only 6 to 6.5. Plan for 7.5 to 8.5 hours "
                "in bed to get 7 to 8 hours of actual sleep.",
            ]),
            ("What happens to muscle while you sleep", [
                "Several recovery processes peak at night. A large share of daily "
                "growth hormone is released during deep sleep, and testosterone "
                "levels in men are closely tied to sleep, rising through the night.",
                "Sleep loss shifts hormones the wrong way: less testosterone and "
                "more cortisol, which favours breakdown over building. In one "
                "study, a single night without sleep reduced muscle protein "
                "synthesis by about 18 percent in young adults (Lamon et al., "
                "Physiological Reports, 2021).",
                "Most research uses severe or total sleep loss, so the effect of "
                "losing an hour or two is smaller. But chronic short sleep adds "
                "up over months of training.",
            ]),
            ("Sleep, strength and performance", [
                "Short sleep tends to reduce performance on long or repeated "
                "efforts and make the same weight feel harder. Single maximal "
                "lifts often hold up after one bad night, but volume, motivation "
                "and focus suffer.",
                "Reaction time and coordination also drop, which matters for "
                "complex lifts like squats and deadlifts and raises injury risk. "
                "Several studies of athletes link sleeping under about 7 hours "
                "with higher injury rates.",
                {"tip": "After a very poor night, keep the session but drop the "
                        "top sets. Do your warm-ups, work at moderate weights, and "
                        "save heavy attempts for a day you have slept."},
            ]),
            ("Sleep and fat loss", [
                "Sleep may matter most when you are dieting. In a well-known "
                "study (Nedeltcheva et al., Annals of Internal Medicine, 2010), "
                "people on the same calorie deficit lost similar weight whether "
                "they slept 5.5 or 8.5 hours, but the short sleepers lost about "
                "55 percent less of that weight as fat and more as lean mass.",
                "Short sleep also increases hunger. Levels of ghrelin, the hunger "
                "hormone, tend to rise, while leptin, which signals fullness, "
                "drops. Most people eat more and crave higher-calorie food after "
                "a bad night, making a deficit harder to hold.",
                "If you are cutting, protecting sleep is one of the easiest ways "
                "to keep more muscle. Pair it with the targets from the <a "
                "href=\"/weight-loss-calculator\">weight loss calculator</a> and "
                "a high protein intake.",
            ]),
            ("Practical steps to sleep better", [
                {"olist": [
                    "<strong>Fix your wake time.</strong> Get up at the same time "
                    "every day, including weekends, within about an hour. It anchors "
                    "your body clock more than bedtime does.",
                    "<strong>Get daylight early.</strong> 10 to 20 minutes outside "
                    "in the morning helps set your rhythm.",
                    "<strong>Cut caffeine by mid-afternoon.</strong> Caffeine's "
                    "effects can last six hours or more. That includes pre-workout "
                    "drinks.",
                    "<strong>Keep the room cool, dark and quiet.</strong> Around "
                    "16 to 19 °C (60 to 67 °F) suits most people.",
                    "<strong>Wind down for 30 to 60 minutes.</strong> Dim lights, "
                    "put work away, and keep the phone out of bed.",
                    "<strong>Limit alcohol.</strong> It helps you fall asleep but "
                    "fragments sleep in the second half of the night.",
                    "<strong>Do not go to bed stuffed or starving.</strong> A "
                    "moderate meal two to three hours before bed works for most.",
                ]},
            ]),
            ("Training late without wrecking sleep", [
                "Evening training is fine for most people. Studies suggest "
                "exercise ending at least an hour before bed generally does not "
                "harm sleep. Very hard sessions close to bedtime can leave some "
                "people wired.",
                "If you train late, skip stimulant pre-workouts, keep the last "
                "hour of the evening calm and take a warm shower, which helps your "
                "body cool down afterwards.",
            ]),
            ("Pre-sleep protein", [
                "Eating protein before bed can support overnight muscle protein "
                "synthesis. A study by Res et al. (Medicine and Science in Sports "
                "and Exercise, 2012) found that 40 g of casein protein taken "
                "before sleep after evening training increased overnight muscle "
                "protein synthesis.",
                "This matters most if your evening meal was early or protein-light. "
                "Good options include milk, Greek yoghurt, curd, cottage cheese or "
                "paneer, all rich in slow-digesting casein. Your daily total, set "
                "with the <a href=\"/protein-calculator\">protein calculator</a>, "
                "still matters most. More on timing in <a "
                "href=\"/guides/pre-and-post-workout-nutrition\">pre and post "
                "workout nutrition</a>.",
            ]),
            ("Tracking your sleep", [
                "Wearables and phone apps estimate sleep from movement and heart "
                "rate. They are reasonably good at total sleep time and poor at "
                "telling sleep stages apart, so treat deep sleep and REM figures "
                "as rough guesses.",
                "The most useful things to track are simple: what time you went "
                "to bed, what time you got up, and how rested you felt on a scale "
                "of 1 to 5. Put a column for it next to your training log, and "
                "you will quickly see how your sessions track your sleep.",
                {"tip": "Do not let tracking itself keep you awake. If checking "
                        "your sleep score makes you anxious, take the watch off "
                        "for a week and go by how you feel."},
            ]),
            ("Early training, shift work and busy schedules", [
                "If you lift at 5 or 6 in the morning, the time has to come from "
                "somewhere. Move bedtime earlier rather than cutting sleep; "
                "training at 5:30 on five hours of sleep is often worse than "
                "training at 6:30 on seven.",
                "Shift workers face a harder problem, because the body clock "
                "resists changing. A few things help:",
                {"list": [
                    "Keep the same sleep window on work days where you can, even "
                    "if it is during the day.",
                    "Make the bedroom fully dark with blackout curtains or an eye "
                    "mask, and use earplugs.",
                    "Wear sunglasses on the way home from a night shift to limit "
                    "morning light.",
                    "Schedule hard sessions after your main sleep, not before.",
                ]},
                "When sleep is limited for a stretch, such as a newborn or exam "
                "season, cut training volume rather than skipping sleep to keep "
                "it. Shorter sessions focused on the main lifts will hold most "
                "of your strength.",
            ]),
            ("Supplements, naps and catching up", [
                "Most sleep supplements have weak evidence for healthy adults, and "
                "none fixes poor habits.",
                {"table": {
                    "head": ["Supplement", "What the evidence suggests"],
                    "rows": [
                        ["Melatonin", "Useful for jet lag and shifting your body clock; small effect on general sleep. Prescription-only in some countries"],
                        ["Magnesium", "May help if you are deficient; limited evidence otherwise"],
                        ["Glycine, L-theanine", "Small studies, modest effects"],
                        ["Antihistamine sleep aids", "Can cause next-day grogginess; not for regular use"],
                    ],
                }},
                "Check with a doctor or pharmacist before taking any sleep aid, "
                "particularly if you take other medication, are pregnant, or have "
                "a health condition. Persistent insomnia is best treated with "
                "cognitive behavioural therapy for insomnia (CBT-I), which has "
                "strong evidence.",
                "A 20 to 30 minute nap in the early afternoon can restore alertness "
                "and help performance after a short night. Longer naps or naps "
                "late in the day can make it harder to fall asleep at night.",
                "Sleeping in at weekends partly offsets a short week but shifts "
                "your body clock, making Monday harder. Steady sleep beats "
                "catching up.",
                "If you have had a run of bad nights, focus on getting back to "
                "your normal wake time rather than lying in. One or two early "
                "nights are usually enough to reset.",
                "If you regularly snore loudly, wake gasping, or feel exhausted "
                "despite enough time in bed, talk to a doctor. Sleep apnoea is "
                "common, especially in larger and heavier lifters, and very "
                "treatable. Read more about recovery in <a "
                "href=\"/guides/rest-days-and-recovery\">rest days and recovery</a>.",
            ]),
        ],
        "faq": [
            ("Can you build muscle on 6 hours of sleep?",
             "You can still build muscle, but likely more slowly, with less "
             "energy for training and more muscle loss when dieting. Most people "
             "who train hard do better with 7 to 9 hours."),
            ("Do muscles grow while you sleep?",
             "Muscle repair and growth happen around the clock, but several key "
             "processes peak during sleep, including growth hormone release. Poor "
             "sleep reduces muscle protein synthesis and recovery."),
            ("Is it better to sleep or work out if I am tired?",
             "After one poor night, a lighter session is usually fine. If you are "
             "chronically short of sleep, an extra hour of sleep will do more for "
             "your progress than an extra session."),
            ("Should I eat before bed to build muscle?",
             "A protein-rich snack before bed, such as milk, yoghurt or cottage "
             "cheese, can support overnight recovery, especially if your last "
             "meal was early. Total daily protein matters more."),
        ],
        "related_calcs": ["protein-calculator", "weight-loss-calculator",
                          "calorie-calculator"],
    },
]
