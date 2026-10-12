"""
Long-form copy for the second half of the calculator pages.

Keyed by calculator slug. Each entry carries the SEO title and description,
the short intro shown above the tool, the article body in the shared block
format (see SPEC), the FAQ and a list of references. The numbers here must
match what static/js computes, so change both together.
"""

CONTENT = {
    # ------------------------------------------------------------------
    "lean-body-mass-calculator": {
        "title": "Lean Body Mass Calculator: Boer, James & Hume",
        "desc": ("Estimate your lean body mass with the Boer, James and Hume "
                 "formulas, or from your body fat %. See fat mass, implied body "
                 "fat and what the number means."),
        "intro": ("Lean body mass is everything you weigh that is not fat. "
                  "Enter your sex, height and weight to see three published "
                  "estimates, or add a body fat percentage for a direct figure."),
        "body": [
            ("What lean body mass actually is", [
                "Lean body mass (LBM) is your total weight minus your fat. It "
                "includes muscle, bone, organs, skin, blood and the water held in "
                "all of them. Muscle is the part you can change most, which is why "
                "lifters care about it, but it is only part of the total.",
                "Two people can share the same height and scale weight and carry "
                "very different amounts of lean mass. That is the gap a "
                "<a href=\"/bmi-calculator\">BMI calculator</a> cannot see and the "
                "reason lean mass is a better anchor for protein targets, some "
                "calorie formulas and tracking a "
                "<a href=\"/guides/body-recomposition-guide\">body recomposition</a>.",
                "Strictly, lean body mass and fat-free mass differ slightly: LBM "
                "counts the small amount of essential fat inside organs and nerve "
                "tissue, fat-free mass does not. For practical purposes the two "
                "terms are used interchangeably, and this calculator treats them "
                "the same way.",
            ]),
            ("How to use the calculator", [
                "Choose your sex, then enter height and weight in either metric or "
                "imperial units. The tool runs three formulas at once and shows "
                "each estimate side by side, along with the body fat percentage "
                "each one implies.",
                "If you already know your body fat percentage, from calipers, a "
                "smart scale, a DEXA scan or our "
                "<a href=\"/body-fat-calculator\">body fat calculator</a>, enter it "
                "in the optional field. The tool then calculates lean mass "
                "directly, which is usually more accurate for anyone who trains, "
                "because the height-and-weight formulas assume an average build.",
            ]),
            ("The formulas behind the numbers", [
                "All three formulas were developed in clinical settings, mostly to "
                "help dose drugs that distribute through lean tissue. They use "
                "weight in kilograms and height in centimetres.",
                {"formula": "Boer (men):   LBM = 0.407 × W + 0.267 × H − 19.2"},
                {"formula": "Boer (women): LBM = 0.252 × W + 0.473 × H − 48.3"},
                {"formula": "James (men):   LBM = 1.1 × W − 128 × (W / H)²"},
                {"formula": "James (women): LBM = 1.07 × W − 148 × (W / H)²"},
                {"formula": "Hume (men):   LBM = 0.32810 × W + 0.33929 × H − 29.5336"},
                {"formula": "Hume (women): LBM = 0.29569 × W + 0.41813 × H − 43.2933"},
                "When you supply a body fat percentage the calculation is simpler "
                "and does not depend on population averages:",
                {"formula": "LBM = weight × (1 − body fat % / 100)"},
                "The implied body fat shown next to each formula is just the "
                "reverse: (weight − LBM) / weight. It is a quick sanity check. If a "
                "formula implies you are 30% fat and you can see your abs, that "
                "formula does not fit your body.",
            ]),
            ("Reading your result", [
                "The three formulas usually land within a few kilograms of each "
                "other. Boer is the one most often recommended for general use. "
                "James tends to drift at higher body weights and can produce "
                "unrealistic numbers for people with obesity, so treat it with "
                "caution if your BMI is above about 35.",
                "To judge whether your lean mass is high or low for your height, "
                "look at the body fat it implies. Typical ranges, adapted from "
                "commonly used American Council on Exercise categories, are:",
                {"table": {
                    "head": ["Category", "Men", "Women"],
                    "rows": [
                        ["Essential fat", "2-5%", "10-13%"],
                        ["Athletes", "6-13%", "14-20%"],
                        ["Fitness", "14-17%", "21-24%"],
                        ["Average", "18-24%", "25-31%"],
                        ["Above average", "25%+", "32%+"],
                    ],
                }},
                "If you train and your direct lean mass (from a measured body fat "
                "figure) comes out well above all three formula estimates, that is "
                "normal. It means you carry more muscle than the people the "
                "formulas were built on. To put that muscle in context, run the "
                "same numbers through the <a href=\"/ffmi-calculator\">FFMI "
                "calculator</a>.",
            ]),
            ("Using lean body mass in your training and diet", [
                "Lean mass makes several other numbers more accurate:",
                {"list": [
                    "<strong>Protein.</strong> Around 2.0-2.7 g per kg of lean mass "
                    "covers most lifters, and avoids overshooting for people with "
                    "a lot of body fat. See "
                    "<a href=\"/guides/how-much-protein-to-build-muscle\">how much "
                    "protein you need</a>.",
                    "<strong>Calories.</strong> The Katch-McArdle equation, 370 + "
                    "21.6 × LBM (kg), estimates resting metabolism from lean mass "
                    "and is an option in the <a href=\"/bmr-calculator\">BMR "
                    "calculator</a>.",
                    "<strong>Progress.</strong> During a cut, the goal is to lose "
                    "weight while lean mass holds steady. During a bulk, a rising "
                    "LBM tells you the extra calories are going where you want.",
                ]},
                {"tip": "Track lean mass with the same method, at the same time "
                        "of day, every two to four weeks. Day-to-day water swings "
                        "can move it by a kilogram or more."},
            ]),
            ("Lean mass during a bulk or a cut", [
                "Lean mass is most useful when you watch how it moves "
                "alongside scale weight. A simple way to read the two "
                "together is to split each change into a lean part and a fat "
                "part, using the same measurement method each time.",
                {"table": {
                    "head": ["Scale weight", "Lean mass", "What is probably happening"],
                    "rows": [
                        ["Down", "Steady", "Ideal cut: the loss is mostly fat"],
                        ["Down", "Down sharply", "Deficit too large or protein too low"],
                        ["Up", "Up", "Productive bulk, especially if most of the gain is lean"],
                        ["Up", "Steady", "Surplus too large; the gain is mostly fat"],
                        ["Steady", "Up", "Recomposition: building muscle while losing fat"],
                    ],
                }},
                "Expect noise. On a cut, early drops in lean mass are often "
                "glycogen and the water stored with it, not muscle, and they "
                "come back when you eat more carbohydrate. On a bulk, the "
                "first kilogram or two is partly the same effect in reverse. "
                "Look at the trend over six to eight weeks before deciding "
                "whether to change anything.",
                "A reasonable target for a lean bulk is that at least half of"
                " the weight you gain shows up as lean mass. For beginners "
                "the share can be higher. For experienced lifters it is "
                "usually lower, which is why slower gains of about 0.25-0.5% "
                "of body weight per month make sense later on. The <a "
                "href=\"/guides/bulking-vs-cutting\">bulking vs cutting "
                "guide</a> goes into the trade-offs.",
            ]),
            ("Limitations worth knowing", [
                "Height-and-weight formulas cannot tell muscle from fat. A heavily "
                "muscled lifter and a sedentary person of the same size get the "
                "same estimate, so for trained people they tend to underestimate "
                "lean mass and overestimate fat.",
                "The direct method is only as good as the body fat figure you "
                "enter. Bioimpedance scales vary with hydration, calipers depend "
                "on the person pinching, and even DEXA has an error of a couple "
                "of percentage points. Lean mass also includes water, so a salty "
                "meal, creatine or a hard leg day can nudge it up without any new "
                "muscle. The formulas were not designed for children, pregnant "
                "women or people with conditions that affect fluid balance.",
            ]),
            ("What to do next", [
                "Use your lean mass to set a protein target, then plug it into "
                "the <a href=\"/macro-calculator\">macro calculator</a> to build "
                "the rest of your diet. If you want to grow it, a structured plan "
                "such as the <a href=\"/workouts/upper-lower-split\">upper/lower "
                "split</a> with steady "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload</a> is the most reliable route.",
            ]),
        ],
        "faq": [
            ("Is lean body mass the same as muscle mass?",
             "No. Lean body mass includes muscle plus bone, organs, skin and body "
             "water. Skeletal muscle is typically around half of it, so a person "
             "with 60 kg of lean mass might carry roughly 30 kg of muscle."),
            ("Which lean body mass formula is most accurate?",
             "For most adults the Boer formula is the usual choice. If you know "
             "your body fat percentage from a reliable method, the direct "
             "calculation is better, especially if you lift and carry more muscle "
             "than average."),
            ("Why do the three formulas give different answers?",
             "Each was derived from a different group of people with different "
             "measurement methods. They agree closely for average builds and "
             "spread apart for very tall, very heavy or very muscular people."),
            ("How fast can I gain lean body mass?",
             "Beginners who train well and eat enough protein can often add around "
             "0.5-1 kg of lean mass per month in the first year. The rate slows "
             "considerably after that, and part of any short-term jump is water."),
            ("Can I lose fat without losing lean mass?",
             "Mostly, yes. Keep lifting with heavy enough loads, eat high protein "
             "and avoid crash deficits. A loss rate of about 0.5-1% of body weight "
             "per week helps preserve muscle."),
        ],
        "sources": [
            "Boer P. Estimated lean body mass as an index for normalization of "
            "body fluid volumes in humans. Am J Physiol. 1984.",
            "James WPT. Research on Obesity. London: HMSO; 1976.",
            "Hume R. Prediction of lean body mass from height and weight. "
            "J Clin Pathol. 1966.",
        ],
    },

    # ------------------------------------------------------------------
    "ffmi-calculator": {
        "title": "FFMI Calculator: Fat-Free Mass Index for Lifters",
        "desc": ("Find your fat-free mass index (FFMI) and height-adjusted "
                 "FFMI from height, weight and body fat. See how much muscle you "
                 "carry and where natural limits sit."),
        "intro": ("FFMI tells you how much lean mass you carry for your height, "
                  "which makes it the BMI that actually works for lifters. Enter "
                  "height, weight and body fat percentage."),
        "body": [
            ("What FFMI measures", [
                "The fat-free mass index takes your lean mass and divides it by "
                "your height squared, the same way BMI does with total weight. "
                "Because fat is removed first, FFMI reflects how much muscle (plus "
                "bone and water) you have built rather than how heavy you are.",
                "That makes it far more useful than "
                "<a href=\"/bmi-calculator\">BMI</a> for anyone who trains. A "
                "muscular 90 kg lifter at 12% body fat and an untrained 90 kg "
                "person at 30% share a BMI. Their FFMI scores are several points "
                "apart.",
            ]),
            ("How to use the calculator", [
                "Enter your height, your current body weight and your body fat "
                "percentage. Body fat is the input that matters most, so use the "
                "best estimate you have: a DEXA scan, a skinfold measurement by "
                "someone experienced, or our "
                "<a href=\"/body-fat-calculator\">body fat calculator</a>, which "
                "uses the US Navy tape method.",
                "The calculator returns your lean mass, your raw FFMI, your "
                "height-normalised FFMI and a category. Compare the normalised "
                "figure with the table below.",
            ]),
            ("The formulas", [
                {"formula": "Lean mass (kg) = weight (kg) × (1 − body fat % / 100)"},
                {"formula": "FFMI = lean mass (kg) / height (m)²"},
                {"formula": "Normalised FFMI = FFMI + 6.1 × (1.8 − height (m))"},
                "The normalisation step comes from the original research. Taller "
                "people naturally score a little lower on a height-squared index, "
                "so the adjustment scales everyone to a reference height of 1.80 m. "
                "If you are shorter than 1.80 m your normalised score drops "
                "slightly. If you are taller it rises.",
                "Worked example: 80 kg at 15% body fat and 1.78 m tall gives 68 kg "
                "of lean mass. 68 / 1.78² = 21.5, and 21.5 + 6.1 × 0.02 = 21.6 "
                "normalised.",
            ]),
            ("Reading your FFMI", [
                "These ranges apply to men. For women, subtract roughly 3 points "
                "from each boundary as an approximate guide, since women carry "
                "less lean mass on average at the same height.",
                {"table": {
                    "head": ["Normalised FFMI (men)", "What it usually means"],
                    "rows": [
                        ["Below 18", "Below average muscle mass"],
                        ["18-20", "Average, typical of untrained men"],
                        ["20-22", "Above average, a few years of consistent training"],
                        ["22-23", "Excellent, clearly muscular"],
                        ["23-25", "Superior, advanced natural lifter"],
                        ["25-27", "Rare without performance-enhancing drugs"],
                        ["Above 27", "Very unlikely to be achieved naturally"],
                    ],
                }},
                "Most men who start lifting sit somewhere around 18-20. Gaining two "
                "or three points over the first few years is a realistic target for "
                "someone who trains hard and eats well.",
            ]),
            ("The natural limit debate", [
                "FFMI became famous because of a 1995 study by Kouri, Pope and "
                "colleagues, which compared male athletes who used anabolic steroids "
                "with those who did not. The non-users topped out around a "
                "normalised FFMI of 25, while many users exceeded it.",
                "That number is often treated as a hard ceiling. It is not. It was "
                "a single sample of American gym-goers in the early 1990s, and a "
                "small number of genetically gifted athletes exceed 25 without "
                "drugs. What it does tell you is that a score in the mid-20s or "
                "higher is exceptional, and that comparing yourself to physiques "
                "far beyond it may mean comparing against a different set of rules.",
                {"tip": "If your score jumps by more than half a point in a month, "
                        "check your body fat input first. A body fat estimate that "
                        "is 3% too low adds roughly a point of FFMI on its own."},
            ]),
            ("Realistic FFMI progress over time", [
                "Muscle gain is fastest at the start and slows every year "
                "after. That pattern shows up clearly in FFMI. A beginner can"
                " add a full point in a good first year, while an advanced "
                "lifter might take two or three years to add the same.",
                {"table": {
                    "head": ["Training age", "Typical FFMI gain per year (men)", "Notes"],
                    "rows": [
                        ["Year 1", "1-2 points", "Rapid early muscle gains"],
                        ["Year 2", "0.5-1 point", "Still steady with a good program"],
                        ["Years 3-4", "0.3-0.6 points", "Progress needs planned overload"],
                        ["Year 5+", "0.1-0.3 points", "Small, hard-won gains"],
                    ],
                }},
                "These are approximations to set expectations, not promises. "
                "Starting point, age, sleep, diet and consistency all shift "
                "them. Women typically gain at a similar relative rate from a"
                " lower starting point.",
                "Because the gains get small, measurement error starts to "
                "hide them. A one point change in body fat estimate can swamp"
                " a year of real progress for an advanced lifter. That is why"
                " it helps to track strength in a few main lifts, photos and "
                "tape measurements alongside FFMI. If all of them are moving "
                "the right way, the muscle is coming, whatever a single scan "
                "says.",
                "If you are well below 20 and have been training for a while,"
                " the usual culprits are too little food, too little protein,"
                " or a program without enough hard sets. The guide to <a "
                "href=\"/guides/how-many-sets-and-reps-for-muscle-growth\">sets"
                " and reps for muscle growth</a> and the <a href=\"/protein-"
                "calculator\">protein calculator</a> are good places to check "
                "first.",
            ]),
            ("Limitations", [
                "FFMI inherits every error in your body fat number. Bioimpedance "
                "scales are particularly noisy, and a lean, muscular person is "
                "exactly who they tend to misread. Lean mass also includes water "
                "and glycogen, so creatine supplementation or a carb load can add "
                "a fraction of a point without any new muscle.",
                "The categories describe population averages, not your potential. "
                "Frame size, limb length and age all play a role. Use FFMI to track "
                "your own trend over months rather than to rank yourself against "
                "strangers online.",
            ]),
            ("What to do next", [
                "If you want to raise your FFMI, you need two things: a training "
                "plan built on <a href=\"/guides/progressive-overload-explained\">"
                "progressive overload</a> and enough food to grow. The "
                "<a href=\"/workouts/push-pull-legs\">push/pull/legs plan</a> suits "
                "intermediate lifters, and the "
                "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting guide</a> "
                "explains how to time a surplus. Set your daily numbers with the "
                "<a href=\"/macro-calculator\">macro calculator</a>.",
            ]),
        ],
        "faq": [
            ("What is a good FFMI for a natural lifter?",
             "For men, a normalised FFMI of 22-23 is a strong result that takes "
             "several years of serious training. Scores of 23-25 are advanced. "
             "For women, roughly 3 points lower is a fair comparison."),
            ("Is an FFMI of 25 really the natural limit?",
             "It is a guideline from one 1995 study, not a law. Very few drug-free "
             "lifters exceed it, but some do, and measurement error in body fat can "
             "easily move a score by a point either way."),
            ("Why is my normalised FFMI different from my FFMI?",
             "The normalised score adjusts for height so that tall and short people "
             "can be compared fairly. It adds 6.1 times the difference between "
             "1.8 m and your height."),
            ("Can women use the FFMI calculator?",
             "Yes. The formula is the same, but the categories in the table are "
             "based on men. Subtract around 3 points from each boundary for a "
             "rough female equivalent."),
            ("How often should I check my FFMI?",
             "Every two to three months is enough. Lean mass changes slowly, and "
             "checking more often mainly picks up noise from your body fat "
             "measurement and water weight."),
        ],
        "sources": [
            "Kouri EM, Pope HG Jr, Katz DL, Oliva P. Fat-free mass index in users "
            "and nonusers of anabolic-androgenic steroids. Clin J Sport Med. 1995.",
            "Schutz Y, Kyle UU, Pichard C. Fat-free mass index and fat mass index "
            "percentiles in Caucasians aged 18-98 y. Int J Obes. 2002.",
        ],
    },

    # ------------------------------------------------------------------
    "heart-rate-zone-calculator": {
        "title": "Heart Rate Zone Calculator: Zones 1-5 by Age",
        "desc": ("Find your five heart rate training zones from your age and "
                 "resting heart rate. Uses the Tanaka or 220-age max HR and the "
                 "Karvonen method for personal zones."),
        "intro": ("Training by heart rate keeps easy days easy and hard days "
                  "hard. Enter your age, and your resting heart rate if you know "
                  "it, to get five personal training zones."),
        "body": [
            ("What heart rate zones are for", [
                "Heart rate zones split your effort range into five bands, from "
                "gentle recovery to all-out. Each band trains something slightly "
                "different: low zones build your aerobic base and help you recover, "
                "high zones raise your lactate threshold and VO2 max.",
                "The biggest practical benefit is honesty. Most people run or cycle "
                "their easy sessions too hard and their hard sessions too easy, and "
                "end up stuck in the middle. A number on a watch makes that "
                "obvious.",
            ]),
            ("How to use the calculator", [
                "Enter your age. The calculator estimates your maximum heart rate "
                "with the Tanaka formula by default, or with the classic 220 minus "
                "age if you choose it.",
                "Then, if you can, add your resting heart rate. With it, the "
                "calculator uses the Karvonen method, which builds each zone on "
                "your heart rate reserve rather than a flat percentage of maximum. "
                "Without it, zones are simple percentages of your estimated max. "
                "If you have tested your real maximum in a supervised or field test, "
                "that is always better than any age formula.",
            ]),
            ("The formulas", [
                {"formula": "Max HR (Tanaka) = 208 − 0.7 × age"},
                {"formula": "Max HR (classic) = 220 − age"},
                {"formula": "Heart rate reserve (HRR) = max HR − resting HR"},
                {"formula": "Karvonen target = resting HR + (HRR × intensity %)"},
                {"formula": "Percent-of-max target = max HR × intensity %"},
                "Tanaka's 2001 analysis of hundreds of studies found that 220 minus "
                "age underestimates max heart rate in older adults. The two agree "
                "at age 40 (180 bpm) and drift apart above and below it.",
                "Karvonen tends to give higher, more individual numbers for fit "
                "people. Someone with a resting rate of 50 bpm has more reserve "
                "than someone at 75, so their zones sit differently even at the "
                "same age.",
            ]),
            ("The five zones", [
                {"table": {
                    "head": ["Zone", "Intensity", "Feels like", "Main purpose"],
                    "rows": [
                        ["Zone 1", "50-60%", "Very easy, chatty", "Recovery and warm-ups"],
                        ["Zone 2", "60-70%", "Easy, can hold a conversation",
                         "Aerobic base, fat oxidation, endurance"],
                        ["Zone 3", "70-80%", "Moderate, short sentences",
                         "Aerobic fitness, tempo work"],
                        ["Zone 4", "80-90%", "Hard, a few words at a time",
                         "Lactate threshold, race pace"],
                        ["Zone 5", "90-100%", "Maximal, no talking",
                         "VO2 max, short intervals"],
                    ],
                }},
                "A 35-year-old with a resting rate of 60 bpm has a Tanaka max of "
                "about 184 bpm and a reserve of 124. Their zone 2 by Karvonen is "
                "60 + 124 × 0.6 to 0.7, or roughly 134-147 bpm.",
            ]),
            ("Why zone 2 is everywhere right now", [
                "Zone 2 training has become popular well beyond endurance sport, "
                "and with reason. Long, easy sessions improve the ability of your "
                "muscles to use fat and clear lactate, build mitochondria and "
                "strengthen the heart, with little recovery cost.",
                "Many endurance coaches have long used roughly an 80/20 split: "
                "around 80% of training time at low intensity and 20% hard. For "
                "lifters, two or three 30-45 minute zone 2 sessions per week "
                "improve work capacity between sets without eating into strength. "
                "The <a href=\"/guides/cardio-for-fat-loss-hiit-vs-liss\">HIIT vs "
                "LISS guide</a> covers how to fit it around a lifting plan.",
                {"tip": "A quick check for zone 2: you can breathe through your "
                        "nose and speak in full sentences, but you would not want "
                        "to sing."},
            ]),
            ("How to measure resting heart rate", [
                {"olist": [
                    "Measure first thing in the morning, before getting up or "
                    "drinking coffee.",
                    "Find your pulse at the wrist or neck, or use a chest strap.",
                    "Count beats for 60 seconds, or 30 seconds and double it.",
                    "Repeat on three to five mornings and use the average.",
                ]},
                "Most adults sit between 60 and 100 bpm, and trained endurance "
                "athletes often fall below 60. A resting rate several beats above "
                "your usual can be a sign of poor sleep, illness or "
                "under-recovery, which is covered in the "
                "<a href=\"/guides/rest-days-and-recovery\">recovery guide</a>.",
            ]),
            ("Using zones alongside lifting", [
                "Most people reading this train with weights first and do "
                "cardio second. Heart rate zones still help, but the goal "
                "shifts from racing performance to fitness, recovery and fat "
                "loss without hurting strength.",
                {"list": [
                    "<strong>Keep most cardio in zone 2.</strong> It builds "
                    "the aerobic base that speeds recovery between sets and "
                    "barely touches leg recovery.",
                    "<strong>Limit zone 4-5 work to one or two short sessions"
                    " a week.</strong> Hard intervals are effective but "
                    "taxing; stack them on the same day as upper-body "
                    "lifting, or well away from heavy squats and deadlifts.",
                    "<strong>Use zone 1 for active recovery.</strong> A "
                    "20-minute easy walk or bike ride on a rest day can "
                    "reduce stiffness without adding fatigue.",
                    "<strong>Separate cardio and lifting</strong> by at least"
                    " a few hours when you can, or do cardio after lifting so"
                    " it does not tire you before heavy sets.",
                ]},
                "Heart rate during lifting itself is a poor guide to effort. "
                "A set of heavy squats can push heart rate into zone 4 for a "
                "minute, then it falls during rest. That is normal and does "
                "not mean the session counts as cardio.",
                "Zones also shift as you get fitter. Your resting heart rate "
                "will often drop by several beats over the first few months "
                "of regular cardio, which raises your heart rate reserve. Re-"
                "measure your resting rate every couple of months and "
                "recalculate so your zones stay accurate.",
            ]),
            ("Limitations", [
                "Age formulas predict the average, and individuals can differ from "
                "them by 10-15 bpm or more. If your zones feel wrong, trust your "
                "breathing and perceived effort and adjust. Wrist-based optical "
                "sensors lag and misread during intervals and lifting, so a chest "
                "strap is more reliable for hard efforts.",
                "Beta blockers and some other medications lower heart rate and make "
                "these zones inaccurate. If you have a heart condition, are "
                "pregnant or are new to exercise after a long break, ask your "
                "doctor what intensity is appropriate before training in zones 4 "
                "and 5.",
            ]),
        ],
        "faq": [
            ("Which max heart rate formula should I use?",
             "Tanaka (208 minus 0.7 times age) is more accurate across age groups, "
             "especially for people over 40. 220 minus age is simpler and widely "
             "used. A real field test beats both."),
            ("Is the Karvonen method better?",
             "For most people, yes. It accounts for your resting heart rate, so "
             "fitter people with low resting rates get zones that match their "
             "actual reserve instead of a generic percentage."),
            ("What zone burns the most fat?",
             "Zone 2 burns the highest proportion of fat, but higher zones burn more "
             "total calories per minute. For fat loss, total weekly energy balance "
             "matters far more than the zone you train in."),
            ("Why is my heart rate higher than usual during workouts?",
             "Heat, dehydration, caffeine, stress, poor sleep and illness all raise "
             "heart rate at the same pace. If it stays elevated for days, take an "
             "easier week."),
            ("How much time should I spend in each zone?",
             "A common approach is roughly 80% of cardio time in zones 1-2 and "
             "20% in zones 3-5. Beginners can do almost everything in zone 2 for "
             "the first couple of months."),
        ],
        "sources": [
            "Tanaka H, Monahan KD, Seals DR. Age-predicted maximal heart rate "
            "revisited. J Am Coll Cardiol. 2001.",
            "Karvonen MJ, Kentala E, Mustala O. The effects of training on heart "
            "rate; a longitudinal study. Ann Med Exp Biol Fenn. 1957.",
            "Seiler S. What is best practice for training intensity and duration "
            "distribution in endurance athletes? Int J Sports Physiol Perform. 2010.",
        ],
    },

    # ------------------------------------------------------------------
    "calories-burned-calculator": {
        "title": "Calories Burned Calculator for 20 Gym Activities",
        "desc": ("Estimate calories burned lifting, running, cycling, HIIT, "
                 "swimming and more. Uses MET values from the Compendium of "
                 "Physical Activities and your body weight."),
        "intro": ("Pick an activity, enter your body weight and how long you "
                  "did it. The calculator estimates calories burned using "
                  "standard MET values."),
        "body": [
            ("How the calculator estimates calories", [
                "Every activity in the list has a MET value, short for metabolic "
                "equivalent of task. One MET is the energy you use sitting quietly, "
                "roughly 1 kcal per kilogram of body weight per hour. An activity "
                "rated 8 METs costs about eight times that.",
                "The values come from the Compendium of Physical Activities, a "
                "reference maintained by exercise scientists that pulls together "
                "measured energy costs for hundreds of activities. It is the same "
                "source behind most fitness apps and research questionnaires.",
            ]),
            ("Using the calculator", [
                "Choose the activity closest to what you did, enter your body "
                "weight and the number of minutes you were actually moving. For "
                "lifting, that is the length of the session. For intervals, use the "
                "whole session including recoveries, because the MET value for "
                "circuit training already accounts for them.",
                "Heavier people burn more for the same activity because they move "
                "more mass, so keep your weight current. If two activities are "
                "close, pick the lower one. You will rarely regret underestimating.",
            ]),
            ("The formula", [
                {"formula": "Calories (kcal) = MET × body weight (kg) × duration (hours)"},
                "Example: a 75 kg person running at 10 km/h (9.8 METs) for 30 "
                "minutes burns about 9.8 × 75 × 0.5 = 368 kcal.",
                "The same person lifting at a general pace (3.5 METs) for an hour "
                "burns about 263 kcal. That surprises a lot of people: lifting "
                "builds muscle and strength, but as a calorie burner it is modest.",
            ]),
            ("MET values used", [
                {"table": {
                    "head": ["Activity", "MET", "kcal / 30 min at 70 kg"],
                    "rows": [
                        ["Weight lifting, general", "3.5", "123"],
                        ["Weight lifting, vigorous", "6.0", "210"],
                        ["Circuit training / HIIT", "8.0", "280"],
                        ["Walking, 5 km/h", "3.5", "123"],
                        ["Brisk walking, 6.4 km/h", "5.0", "175"],
                        ["Running, 8 km/h", "8.3", "291"],
                        ["Running, 10 km/h", "9.8", "343"],
                        ["Running, 12 km/h", "11.8", "413"],
                        ["Cycling, 16-19 km/h", "6.8", "238"],
                        ["Cycling, 20-22 km/h", "8.0", "280"],
                        ["Swimming, moderate", "5.8", "203"],
                        ["Rowing machine, moderate", "7.0", "245"],
                        ["Elliptical, moderate", "5.0", "175"],
                        ["Stair climber", "9.0", "315"],
                        ["Jump rope", "12.3", "431"],
                        ["Yoga", "2.5", "88"],
                        ["Hiking", "6.0", "210"],
                        ["Dancing", "5.0", "175"],
                        ["Basketball", "6.5", "228"],
                        ["Football / soccer", "7.0", "245"],
                    ],
                }},
            ]),
            ("Everyday movement matters more than you think", [
                "Formal exercise is only one part of the calories you burn. "
                "The rest, called non-exercise activity thermogenesis (NEAT),"
                " covers walking, standing, fidgeting, housework and "
                "everything else you do outside the gym. Research by James "
                "Levine and colleagues showed that NEAT can differ by "
                "hundreds of calories a day between people of similar size.",
                "That has a practical consequence. A one-hour gym session at "
                "3.5-6 METs might burn 250-450 kcal. Adding 5,000 extra steps"
                " over the day, roughly 45-50 minutes of normal walking, "
                "burns a similar amount for most people, and costs far less "
                "recovery.",
                {"table": {
                    "head": ["Daily habit", "Approx. extra kcal (70 kg)"],
                    "rows": [
                        ["5,000 extra steps", "200-250"],
                        ["30 min brisk walk", "175"],
                        ["1 hour standing instead of sitting", "40-60"],
                        ["Taking stairs, 10 minutes total", "100-150"],
                    ],
                }},
                "NEAT also tends to drop when you diet. People move less "
                "without noticing when food is low, which is one of the main "
                "reasons weight loss slows. Tracking a daily step count is a "
                "simple way to keep it steady. Many people find 8,000-10,000 "
                "steps a realistic target that makes a calorie deficit "
                "noticeably easier to hold.",
            ]),
            ("Gross vs net calories", [
                "The formula gives gross calories: everything you burned during the "
                "session, including the roughly 1 MET you would have burned sitting "
                "on the sofa anyway. The extra calories caused by the exercise, "
                "the net figure, are about MET minus 1.",
                "For a long, easy walk that difference is a big share of the "
                "total. For a hard run it is small. If you add exercise calories "
                "back into a diet, the net figure is the more honest one, and your "
                "<a href=\"/tdee-calculator\">TDEE</a> may already include your "
                "usual training through the activity multiplier, so be careful not "
                "to count it twice.",
            ]),
            ("Why your watch says something different", [
                "Fitness trackers and gym machines often report higher numbers than "
                "this calculator. Independent tests of wrist wearables have found "
                "energy expenditure errors commonly in the 20-40% range or more, "
                "even when heart rate is measured well, and cardio machines often "
                "assume a default body weight.",
                "Neither source is exact. Individual fitness, technique, terrain and "
                "how hard you actually pushed all change the real cost. Use these "
                "numbers to compare activities and plan your week, not to justify "
                "an extra dessert.",
                {"tip": "If weight loss is the goal, do not eat back all your "
                        "exercise calories. Adding back half is a safer rule of "
                        "thumb, then adjust based on what the scale does over three "
                        "or four weeks."},
            ]),
            ("Putting the number to use", [
                "Exercise helps with fat loss, but diet sets the pace. A 30-minute "
                "run might burn 300-400 kcal, about the same as one large coffee "
                "drink and a pastry. Set your intake with the "
                "<a href=\"/calorie-calculator\">calorie calculator</a> and use "
                "training to build fitness and keep muscle.",
                "For a plan that combines both, see the "
                "<a href=\"/workouts/fat-loss-workout-plan\">fat loss workout "
                "plan</a> and the guide to "
                "<a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
                "calculating calories for weight loss</a>.",
            ]),
        ],
        "faq": [
            ("How many calories does lifting weights burn?",
             "A general lifting session is around 3.5 METs, so a 70 kg person burns "
             "about 245 kcal per hour. A fast-paced, vigorous session is closer to "
             "6 METs, or about 420 kcal per hour."),
            ("Does lifting burn calories after the workout?",
             "Yes, a little. Excess post-exercise oxygen consumption adds a modest "
             "amount, usually tens of calories rather than hundreds. The main "
             "long-term benefit is preserving and building muscle."),
            ("Are fitness tracker calorie counts accurate?",
             "Not very. Studies of wrist wearables regularly find energy errors of "
             "20% or more. They are useful for tracking trends but should not be "
             "treated as exact."),
            ("Why do heavier people burn more calories?",
             "Moving a heavier body takes more energy, so the formula multiplies "
             "by body weight. As you lose weight, the same workout burns fewer "
             "calories, which is one reason fat loss slows over time."),
            ("Should I eat back the calories I burn exercising?",
             "If your calorie target already includes an activity multiplier, no. "
             "If it is based on a sedentary level, adding back about half of the "
             "estimated exercise calories is a sensible starting point."),
        ],
        "sources": [
            "Ainsworth BE, Haskell WL, Herrmann SD, et al. 2011 Compendium of "
            "Physical Activities: a second update of codes and MET values. Med Sci "
            "Sports Exerc. 2011.",
            "Shcherbina A, Mattsson CM, Waggott D, et al. Accuracy in wrist-worn, "
            "sensor-based measurements of heart rate and energy expenditure in a "
            "diverse cohort. J Pers Med. 2017.",
        ],
    },

    # ------------------------------------------------------------------
    "water-intake-calculator": {
        "title": "Water Intake Calculator: How Much to Drink Daily",
        "desc": ("Work out how much water to drink each day from your body "
                 "weight, exercise and climate. Results in litres, glasses and "
                 "ounces, with tips for training days."),
        "intro": ("Your water needs rise with body size, sweat and heat. Enter "
                  "your weight, daily exercise and climate for a personal daily "
                  "target."),
        "body": [
            ("Why a personal number beats eight glasses", [
                "The old advice of eight glasses a day is easy to remember but has "
                "no clear scientific origin, and it ignores the obvious: a 55 kg "
                "office worker and a 100 kg lifter training in a hot gym do not "
                "need the same amount.",
                "Even mild dehydration, around 2% of body weight lost as sweat, "
                "has been linked to reduced endurance, higher perceived effort and "
                "poorer concentration. For people who train, getting this right "
                "is a cheap performance gain.",
            ]),
            ("How to use the calculator", [
                "Enter your body weight, the number of minutes you exercise on a "
                "typical day and whether you live or train in a temperate or hot "
                "climate. The result is shown in litres, 250 ml glasses and US "
                "cups and fluid ounces.",
                "Run it twice if your training varies: once for rest days and once "
                "for training days. The difference tells you how much extra to "
                "drink around your sessions.",
            ]),
            ("How the number is calculated", [
                {"formula": "Base = 35 ml × body weight (kg)"},
                {"formula": "Exercise = + 350 ml per 30 minutes of exercise"},
                {"formula": "Climate = + 500 ml if hot"},
                "Example: a 70 kg person who trains for 60 minutes in a temperate "
                "climate needs about 2,450 + 700 = 3,150 ml, or roughly 3.2 litres "
                "a day. In a hot climate that becomes about 3.7 litres.",
                "The 35 ml per kg base is a widely used clinical rule of thumb for "
                "healthy adults. The exercise allowance covers a moderate sweat "
                "rate. Heavy sweaters, long sessions and very humid gyms can need "
                "more.",
            ]),
            ("How your target compares with official guidance", [
                "The European Food Safety Authority set adequate intakes of 2.0 "
                "litres a day for women and 2.5 litres for men. Those figures are "
                "total water, including the roughly 20% that typically comes from "
                "food such as fruit, vegetables, soups and dairy.",
                "Because this calculator adds allowances for training and heat, "
                "most active people will see a number above those references. "
                "That is expected. The table gives a quick sense of typical "
                "results.",
                {"table": {
                    "head": ["Body weight", "Rest day", "60 min training", "60 min, hot"],
                    "rows": [
                        ["55 kg (121 lb)", "1.9 L", "2.6 L", "3.1 L"],
                        ["70 kg (154 lb)", "2.5 L", "3.2 L", "3.7 L"],
                        ["85 kg (187 lb)", "3.0 L", "3.7 L", "4.2 L"],
                        ["100 kg (220 lb)", "3.5 L", "4.2 L", "4.7 L"],
                    ],
                }},
            ]),
            ("Check yourself, not just the number", [
                "The simplest hydration check is urine colour. Pale straw yellow "
                "usually means you are well hydrated. Dark yellow or amber suggests "
                "you need more. Completely clear urine all day can mean you are "
                "drinking more than you need. Note that B-vitamin supplements can "
                "turn urine bright yellow regardless.",
                "For training, weigh yourself before and after a session. Each "
                "kilogram lost is roughly a litre of sweat, and replacing about "
                "1.25-1.5 times that over the next few hours restores fluid "
                "balance.",
                {"tip": "Drink around 400-600 ml in the two hours before training, "
                        "sip during long sessions, and add electrolytes when you "
                        "train over an hour or sweat heavily."},
            ]),
            ("Electrolytes, sweat and hot gyms", [
                "Sweat is not just water. It carries sodium, along with "
                "smaller amounts of potassium, magnesium and calcium. Sodium "
                "losses vary widely between people, and some heavy sweaters "
                "lose well over a gram per litre of sweat, which is why some "
                "people finish a session with white salt marks on their "
                "clothes.",
                "For most gym sessions under an hour, normal meals replace "
                "these losses and plain water is enough. Electrolytes become "
                "worth adding when:",
                {"list": [
                    "you train longer than 60-90 minutes, or do two sessions "
                    "in a day",
                    "you train in heat or high humidity",
                    "you are a heavy or salty sweater",
                    "you are cramping or feeling unusually flat despite "
                    "drinking enough",
                    "you follow a low-carbohydrate or keto diet, which "
                    "increases sodium loss",
                ]},
                "A simple approach is a pinch of salt in your bottle or an "
                "electrolyte drink that provides roughly 300-700 mg of sodium"
                " per litre. People with high blood pressure or on a sodium-"
                "restricted diet should check with a doctor first.",
                "Heat also raises your needs in ways a single number cannot "
                "fully capture. Acclimatising to a hot environment takes "
                "around one to two weeks, during which your sweat rate rises."
                " Start sessions hydrated, drink to thirst during them, and "
                "weigh yourself before and after to learn your own sweat "
                "rate.",
            ]),
            ("Can you drink too much?", [
                "Yes. Drinking very large volumes in a short time, particularly "
                "during long endurance events, can dilute blood sodium and cause "
                "hyponatremia. Early signs include nausea, headache, confusion and "
                "swelling. It is rare in normal gym training, but it is the reason "
                "not to force down far more than your thirst and this target "
                "suggest.",
                "People with kidney, heart or liver conditions, and anyone told to "
                "restrict fluids, should follow their doctor's advice instead of "
                "any calculator. Needs also rise during pregnancy and "
                "breastfeeding.",
            ]),
            ("Making it easy", [
                {"list": [
                    "Keep a marked bottle with you and know how many refills hit "
                    "your target.",
                    "Drink a glass with every meal and one when you wake up.",
                    "Count tea, coffee and milk. Moderate caffeine does not "
                    "dehydrate habitual drinkers.",
                    "Eat water-rich foods. A diet built from the "
                    "<a href=\"/macro-calculator\">macro calculator</a> with plenty "
                    "of fruit and vegetables covers a good share.",
                ]},
                "Creatine draws water into muscle, so if you take it, aim for the "
                "top end of your range. The <a href=\"/guides/creatine-guide\">"
                "creatine guide</a> explains why.",
            ]),
        ],
        "faq": [
            ("How much water should I drink a day?",
             "A reasonable starting point is about 35 ml per kg of body weight, "
             "plus around 350 ml for every 30 minutes of exercise and extra in hot "
             "weather. For a 70 kg active adult that is usually 3-3.5 litres."),
            ("Do tea and coffee count towards water intake?",
             "Yes. Research shows moderate caffeine intake does not cause net fluid "
             "loss in regular drinkers, so tea and coffee count. Alcohol is the "
             "exception and should not be counted."),
            ("Does water help with weight loss?",
             "Indirectly. Drinking water before meals can help some people feel "
             "fuller, and swapping sugary drinks for water cuts calories. Water on "
             "its own does not burn fat."),
            ("How much water should I drink during a workout?",
             "For sessions under an hour, sipping to thirst is usually enough. For "
             "longer or very sweaty sessions, around 400-800 ml per hour with "
             "electrolytes is a common range."),
            ("Is it possible to drink too much water?",
             "Yes. Very large volumes in a short time can lower blood sodium, a "
             "condition called hyponatremia. It is uncommon outside long endurance "
             "events, but there is no benefit in drinking far beyond your needs."),
        ],
        "sources": [
            "EFSA Panel on Dietetic Products, Nutrition and Allergies. Scientific "
            "Opinion on Dietary Reference Values for water. EFSA Journal. 2010.",
            "Sawka MN, Burke LM, Eichner ER, et al. American College of Sports "
            "Medicine position stand: exercise and fluid replacement. Med Sci "
            "Sports Exerc. 2007.",
            "Killer SC, Blannin AK, Jeukendrup AE. No evidence of dehydration with "
            "moderate daily coffee intake. PLoS One. 2014.",
        ],
    },

    # ------------------------------------------------------------------
    "waist-to-hip-ratio-calculator": {
        "title": "Waist-to-Hip Ratio Calculator (WHO Cut-offs)",
        "desc": ("Calculate your waist-to-hip ratio and waist-to-height ratio. "
                 "See WHO health risk cut-offs, whether you are apple or pear "
                 "shaped, and how to measure correctly."),
        "intro": ("Where you carry fat matters as much as how much you carry. "
                  "Enter your waist and hip measurements, plus height if you "
                  "want your waist-to-height ratio too."),
        "body": [
            ("What waist-to-hip ratio tells you", [
                "Waist-to-hip ratio (WHR) compares the circumference of your waist "
                "with that of your hips. A higher ratio means more of your fat sits "
                "around the abdomen, which is where visceral fat, the fat packed "
                "around internal organs, tends to accumulate.",
                "That matters because abdominal fat is more closely tied to type 2 "
                "diabetes, high blood pressure and heart disease than fat stored on "
                "the hips and thighs. Two people with the same "
                "<a href=\"/bmi-calculator\">BMI</a> can carry very different risk "
                "depending on their shape, and WHR picks up what BMI misses.",
            ]),
            ("How to use the calculator", [
                "Select your sex, then enter your waist and hip measurements in "
                "centimetres or inches. The calculator returns your ratio, a risk "
                "rating based on World Health Organization cut-offs and your body "
                "shape. Add your height and it also gives your waist-to-height "
                "ratio, a second screening measure that works the same way for "
                "everyone.",
            ]),
            ("How to measure properly", [
                "Measurement technique changes the result more than anything else, "
                "so take a minute to get it right.",
                {"olist": [
                    "Stand upright with feet together and arms relaxed at your "
                    "sides. Measure over bare skin or thin clothing.",
                    "Waist: find the midpoint between the bottom of your lowest rib "
                    "and the top of your hip bone. This is the WHO method and is "
                    "usually close to, but not always at, the navel.",
                    "Breathe out gently and measure at the end of a normal "
                    "breath. Do not suck in.",
                    "Hips: measure around the widest part of your buttocks, keeping "
                    "the tape level all the way round.",
                    "Keep the tape snug but not compressing the skin, and take each "
                    "measurement twice. Use the average.",
                ]},
            ]),
            ("The formulas", [
                {"formula": "Waist-to-hip ratio = waist circumference / hip circumference"},
                {"formula": "Waist-to-height ratio = waist circumference / height"},
                "Both measurements must use the same unit, which the calculator "
                "handles for you. Example: a waist of 84 cm and hips of 100 cm give "
                "a WHR of 0.84. With a height of 170 cm, the waist-to-height ratio "
                "is 0.49.",
            ]),
            ("Reading your result", [
                "The 2008 WHO expert consultation on waist circumference and "
                "waist-hip ratio set the following thresholds for substantially "
                "increased risk of metabolic complications:",
                {"table": {
                    "head": ["Measure", "Men", "Women", "Meaning"],
                    "rows": [
                        ["Waist-to-hip ratio", "Below 0.90", "Below 0.85",
                         "Lower risk"],
                        ["Waist-to-hip ratio", "0.90 or above", "0.85 or above",
                         "Substantially increased risk"],
                        ["Waist-to-height ratio", "Below 0.5", "Below 0.5",
                         "Lower risk"],
                        ["Waist-to-height ratio", "0.5 or above", "0.5 or above",
                         "Increased risk, worth acting on"],
                    ],
                }},
                "The waist-to-height rule, popularised by researcher Margaret "
                "Ashwell, boils down to a simple message: keep your waist to less "
                "than half your height. A 2012 meta-analysis by Ashwell and "
                "colleagues found it a better screening tool for cardiometabolic "
                "risk than either waist circumference or BMI alone.",
            ]),
            ("Apple and pear shapes", [
                "A high ratio is often called an apple shape: fat stored mainly "
                "around the middle. A low ratio is a pear shape: proportionally "
                "more fat on the hips and thighs. Men lean towards apple, and "
                "women towards pear before menopause, after which many women shift "
                "towards storing more around the waist.",
                "Shape is partly genetic, but abdominal fat responds well to "
                "overall fat loss, regular exercise, enough sleep and limiting "
                "alcohol. You cannot spot-reduce it with sit-ups. The "
                "<a href=\"/guides/how-to-lose-belly-fat\">belly fat guide</a> "
                "covers what actually works.",
                {"tip": "If you lift and are building glutes, your hip measurement "
                        "will grow and your ratio will fall even if your waist does "
                        "not change. Track waist circumference on its own as well."},
            ]),
            ("Waist size on its own", [
                "Waist circumference by itself is also a recognised screening"
                " measure, and it is the easiest one to track at home. "
                "Commonly used thresholds for adults of European descent are "
                "below.",
                {"table": {
                    "head": ["Waist circumference", "Men", "Women"],
                    "rows": [
                        ["Increased risk", "94 cm (37 in) or more", "80 cm (31.5 in) or more"],
                        ["Substantially increased risk", "102 cm (40 in) or more", "88 cm (34.5 in) or more"],
                    ],
                }},
                "Several health bodies recommend lower thresholds for people "
                "of South Asian, Chinese and Japanese descent, often 90 cm "
                "for men and 80 cm for women, because cardiometabolic risk "
                "tends to rise at smaller waist sizes in these groups. If "
                "that applies to you, the waist-to-height ratio is a useful "
                "cross-check because the same 0.5 threshold has held up "
                "across many populations.",
                "For tracking progress, waist size often responds earlier "
                "than the scale. Someone who starts lifting and eating better"
                " can lose a few centimetres from the waist while their "
                "weight barely moves, especially early on. Measure at the "
                "same point, at the same time of day, ideally in the morning "
                "before eating, and compare monthly rather than weekly so "
                "that bloating and water retention do not mislead you.",
            ]),
            ("Limitations and next steps", [
                "WHR is a screening tool, not a diagnosis. It does not account for "
                "muscle, it can be thrown off by poor technique, and the cut-offs "
                "were developed mainly in European populations. Some Asian "
                "populations show higher risk at lower waist sizes. It is also not "
                "meaningful during pregnancy. A high result is a reason to check "
                "blood pressure, blood sugar and cholesterol with your doctor.",
                "To build a fuller picture, pair it with a body fat estimate from "
                "the <a href=\"/body-fat-calculator\">body fat calculator</a>, then "
                "set a sensible deficit with the "
                "<a href=\"/weight-loss-calculator\">weight loss calculator</a>. "
                "Re-measure every four weeks.",
            ]),
        ],
        "faq": [
            ("What is a healthy waist-to-hip ratio?",
             "According to WHO, below 0.90 for men and below 0.85 for women. At or "
             "above those values, the risk of metabolic complications such as type "
             "2 diabetes and heart disease is substantially increased."),
            ("Is waist-to-hip ratio better than BMI?",
             "It captures something BMI cannot: where fat is stored. Many experts "
             "suggest using them together, along with waist-to-height ratio, which "
             "studies show is a strong single screening measure."),
            ("Where exactly should I measure my waist?",
             "The WHO method measures midway between the lowest rib and the top of "
             "the hip bone, after breathing out normally. Measure the same way each "
             "time so you can compare results."),
            ("Can exercise lower my waist-to-hip ratio?",
             "Yes. Overall fat loss reduces abdominal fat, and building the glutes "
             "increases hip size. Both lower the ratio. Spot exercises like "
             "crunches do not target belly fat directly."),
            ("What does a waist-to-height ratio above 0.5 mean?",
             "It means your waist is more than half your height, a common threshold "
             "for increased cardiometabolic risk. It is a prompt to reduce waist "
             "size and to get routine health checks."),
        ],
        "sources": [
            "World Health Organization. Waist circumference and waist-hip ratio: "
            "report of a WHO expert consultation, Geneva, 8-11 December 2008. "
            "WHO; 2011.",
            "Ashwell M, Gunn P, Gibson S. Waist-to-height ratio is a better "
            "screening tool than waist circumference and BMI for adult "
            "cardiometabolic risk factors: systematic review and meta-analysis. "
            "Obes Rev. 2012.",
        ],
    },

    # ------------------------------------------------------------------
    "weight-loss-calculator": {
        "title": "Weight Loss Calculator: Calories & Goal Date",
        "desc": ("Find the daily calories to reach your goal weight and the date "
                 "you can expect to get there. Pick a pace from 0.25 to 1 kg a "
                 "week, with safety checks."),
        "intro": ("Tell the calculator where you are, where you want to be and how "
                  "fast. It returns a daily calorie target, the weeks it should "
                  "take and an estimated goal date."),
        "body": [
            ("What this calculator does", [
                "Most people know they need a calorie deficit to lose fat. Fewer "
                "know how big it should be or how long it will take. This tool "
                "answers both: it estimates the calories you burn each day, "
                "subtracts the deficit needed for your chosen pace and projects "
                "a finish date.",
                "Seeing a realistic date up front helps. It turns a vague wish into "
                "a plan with a checkpoint, and it shows clearly why crash diets "
                "rarely save as much time as they promise.",
            ]),
            ("How to use it", [
                "Enter your sex, age, height, current weight and goal weight, then "
                "pick the activity level that best describes a normal week. Finally "
                "choose a pace: 0.25, 0.5, 0.75 or 1 kg per week (about 0.5, 1, 1.5 "
                "or 2 lb).",
                "The result shows your maintenance calories, your daily target, "
                "the number of weeks to your goal, the estimated date and the total "
                "deficit involved. If your target drops below a sensible floor, the "
                "calculator warns you.",
            ]),
            ("The maths behind it", [
                "Maintenance calories come from the Mifflin-St Jeor equation, "
                "multiplied by your activity factor, the same approach used in the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a>.",
                {"formula": "Men:   BMR = 10 × kg + 6.25 × cm − 5 × age + 5"},
                {"formula": "Women: BMR = 10 × kg + 6.25 × cm − 5 × age − 161"},
                {"formula": "Daily deficit = pace (kg/week) × 7,700 kcal / 7"},
                {"formula": "Target = BMR × activity factor − daily deficit"},
                {"formula": "Weeks to goal = (current − goal weight) / pace"},
                "The 7,700 kcal per kilogram figure (about 3,500 per pound) is the "
                "standard approximation for the energy in body fat tissue. A pace of "
                "0.5 kg per week therefore needs a deficit of about 550 kcal a day.",
            ]),
            ("Choosing a pace", [
                {"table": {
                    "head": ["Pace", "Daily deficit", "Best for"],
                    "rows": [
                        ["0.25 kg (0.5 lb) / week", "~275 kcal",
                         "Lean lifters, last few kilos, keeping strength"],
                        ["0.5 kg (1 lb) / week", "~550 kcal",
                         "Most people; sustainable and muscle-friendly"],
                        ["0.75 kg (1.5 lb) / week", "~825 kcal",
                         "Higher body fat, strong adherence"],
                        ["1 kg (2 lb) / week", "~1,100 kcal",
                         "Larger bodies only; hard to sustain"],
                    ],
                }},
                "A useful rule is to lose about 0.5-1% of your body weight per "
                "week. Faster than that, especially when already lean, increases "
                "the risk of losing muscle, feeling flat in the gym and rebounding "
                "afterwards.",
                "The calculator flags targets below 1,500 kcal for men and 1,200 "
                "kcal for women. Going lower is hard to meet nutritional needs on "
                "and should be done only with medical supervision.",
            ]),
            ("Why the estimate drifts, and what to do", [
                "The projected date assumes your maintenance stays fixed. In "
                "reality it falls as you lose weight: a smaller body burns less, "
                "and your body adapts by reducing movement and, to a lesser extent, "
                "metabolic rate. This is called metabolic or adaptive "
                "thermogenesis. Kevin Hall's modelling work at the NIH showed that "
                "the simple 3,500 kcal rule overestimates long-term loss for this "
                "reason.",
                {"list": [
                    "<strong>Recalculate every 5 kg (about 10 lb)</strong> lost, "
                    "using your new weight.",
                    "<strong>Judge progress on weekly averages</strong>, not single "
                    "weigh-ins. Water can move the scale 1-2 kg day to day.",
                    "<strong>Plateaus</strong> of one or two weeks are normal. If "
                    "the weekly average has not moved for three weeks, cut a further "
                    "100-200 kcal or add daily steps.",
                    "<strong>Diet breaks</strong> of one to two weeks at "
                    "maintenance every 8-12 weeks can make a long diet easier to "
                    "stick to.",
                ]},
                {"tip": "Keep protein high and keep lifting heavy. Those two habits "
                        "do more than anything else to make sure the weight you lose "
                        "is fat, not muscle."},
            ]),
            ("A worked example", [
                "Take a 32-year-old woman, 165 cm tall, weighing 78 kg, who "
                "wants to reach 68 kg. She trains three times a week, so she "
                "picks the lightly active level (1.375).",
                {"formula": "BMR = 10 × 78 + 6.25 × 165 − 5 × 32 − 161 ≈ 1,490 "
                        "kcal"},
                {"formula": "Maintenance = 1,490 × 1.375 ≈ 2,050 kcal"},
                "At 0.5 kg per week her deficit is about 550 kcal, giving a "
                "daily target of roughly 1,500 kcal and a timeline of 20 "
                "weeks for 10 kg. At 1 kg per week the target would drop to "
                "about 950 kcal, well below the 1,200 kcal floor, and the "
                "calculator would warn her. A pace of 0.5 kg is the sensible "
                "choice.",
                "After the first 5 kg she recalculates at 73 kg. Her "
                "maintenance has dropped to around 1,980 kcal, so her target "
                "becomes about 1,430 kcal to keep the same pace. Small "
                "adjustments like this, made on schedule, are what keep "
                "progress moving through the second half of a diet.",
                {"table": {
                    "head": ["Week", "Expected weight", "Daily target"],
                    "rows": [
                        ["0", "78 kg", "~1,500 kcal"],
                        ["10", "73 kg", "~1,430 kcal (recalculated)"],
                        ["20", "68 kg", "Move towards new maintenance (~1,910 kcal)"],
                    ],
                }},
                "Reaching the goal is not the end. Increase calories "
                "gradually over two to four weeks to the new maintenance "
                "level rather than jumping straight back to old habits. That "
                "reverse step is where many people regain the weight.",
            ]),
            ("Who should not use this alone", [
                "If you are pregnant or breastfeeding, under 18, have diabetes or "
                "another medical condition, take medication that affects appetite or "
                "blood sugar, or have a history of disordered eating, talk to a "
                "doctor or registered dietitian before starting a deficit. The "
                "calculator gives estimates for healthy adults only.",
            ]),
            ("Next steps", [
                "Turn your calorie target into daily protein, carbs and fat with the "
                "<a href=\"/macro-calculator\">macro calculator</a>, and pick a "
                "training plan such as the "
                "<a href=\"/workouts/fat-loss-workout-plan\">fat loss workout "
                "plan</a>. The full method, including tracking, is in "
                "<a href=\"/guides/how-to-calculate-calories-for-weight-loss\">how "
                "to calculate calories for weight loss</a>.",
            ]),
        ],
        "faq": [
            ("How many calories should I eat to lose 0.5 kg a week?",
             "About 550 kcal less than your maintenance each day. For many adults "
             "that lands between 1,500 and 2,200 kcal, depending on size and "
             "activity."),
            ("Is losing 1 kg a week safe?",
             "For people with a lot of weight to lose it can be, at least early on. "
             "For leaner people it usually means too much muscle loss and hunger. "
             "Around 0.5-1% of body weight per week is a safer guide."),
            ("Why am I not losing weight on my calorie target?",
             "Common reasons are underestimated portions, weekend overeating, water "
             "retention and a maintenance estimate that is too high. Track carefully "
             "for three weeks, then lower your target by 100-200 kcal if needed."),
            ("Will my goal date be accurate?",
             "Treat it as a best case. Your maintenance falls as you lose weight, so "
             "progress usually slows. Recalculate after every 5 kg to keep the "
             "estimate realistic."),
            ("What is the lowest calorie intake I should go to?",
             "As a general rule, not below about 1,500 kcal for men or 1,200 kcal "
             "for women without medical supervision. Below that it is difficult to "
             "get enough protein, vitamins and minerals."),
        ],
        "sources": [
            "Mifflin MD, St Jeor ST, Hill LA, et al. A new predictive equation for "
            "resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990.",
            "Hall KD, Sacks G, Chandramohan D, et al. Quantification of the effect "
            "of energy imbalance on bodyweight. Lancet. 2011.",
            "Helms ER, Aragon AA, Fitschen PJ. Evidence-based recommendations for "
            "natural bodybuilding contest preparation: nutrition and "
            "supplementation. J Int Soc Sports Nutr. 2014.",
        ],
    },

    # ------------------------------------------------------------------
    "plate-calculator": {
        "title": "Barbell Plate Calculator: What to Load Per Side",
        "desc": ("Enter a target weight and see exactly which plates go on each "
                 "side of the bar. Works in kg or lb, any bar weight, with collars "
                 "and a visual barbell."),
        "intro": ("Stop doing mental arithmetic between sets. Enter the weight you "
                  "want on the bar and the calculator shows exactly which plates to "
                  "load on each side."),
        "body": [
            ("What the plate calculator does", [
                "Loading a barbell is simple until it is not: a new gym with "
                "different plates, a percentage from your program that lands on an "
                "awkward number, or a switch between kilograms and pounds. This "
                "tool takes the target and works out the fewest plates per side to "
                "hit it.",
                "It draws the bar so you can check at a glance, and if the exact "
                "weight cannot be loaded with the plates you have, it tells you the "
                "closest weight you can make and how much is left over.",
            ]),
            ("How to use it", [
                {"olist": [
                    "Choose kilograms or pounds.",
                    "Pick your bar: 20 kg, 15 kg or 10 kg, or 45 lb or 35 lb.",
                    "Untick any plates your gym does not have. Kilogram sets "
                    "include 25, 20, 15, 10, 5, 2.5 and 1.25 kg; pound sets include "
                    "45, 35, 25, 10, 5 and 2.5 lb.",
                    "Tick the collars option if you use 2.5 kg competition collars, "
                    "which weigh 2.5 kg each and count towards the total.",
                    "Enter your target and read off the plates for one side.",
                ]},
                "Need a target first? Take a percentage of your max from the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a> and "
                "drop it in here.",
            ]),
            ("How the calculation works", [
                {"formula": "Per side = (target − bar − collars) / 2"},
                "The calculator then works greedily from the heaviest plate down, "
                "adding as many of each as fit into the remaining weight. With "
                "standard plate sets this always gives the fewest plates possible.",
                "Example: 142.5 kg on a 20 kg bar with no collars leaves 122.5 kg, "
                "or 61.25 kg per side. That is 25 + 25 + 10 + 1.25 kg on each side.",
            ]),
            ("Plate colours and loading order", [
                "Always load the heaviest plates first, closest to the inside "
                "sleeve, and work outwards to the lightest. This keeps the bar "
                "stable, makes plates easier to read from a distance and is "
                "required in competition.",
                "International Weightlifting Federation (IWF) and most powerlifting "
                "federations use a standard colour code for kilogram plates, which "
                "many commercial gyms copy:",
                {"table": {
                    "head": ["Plate", "Colour", "Per side for 100 kg on a 20 kg bar"],
                    "rows": [
                        ["25 kg", "Red", "1 plate (25 kg)"],
                        ["20 kg", "Blue", "-"],
                        ["15 kg", "Yellow", "1 plate (15 kg)"],
                        ["10 kg", "Green", "-"],
                        ["5 kg", "White", "-"],
                        ["2.5 kg", "Red (small)", "-"],
                        ["1.25 kg", "Silver/chrome", "-"],
                    ],
                }},
                "So 100 kg is a red and a yellow on each side. Learn the colours "
                "and you can check a training partner's bar in a second.",
            ]),
            ("Calibrated plates vs bumper plates", [
                "Calibrated steel plates are machined to within a few grams of "
                "their stated weight and are thin, so you can fit a lot on the bar. "
                "They are used in powerlifting and are what the colour code above "
                "describes.",
                "Bumper plates are thick rubber, designed to be dropped from "
                "overhead in Olympic lifting and CrossFit. Their thickness means a "
                "loaded bar runs out of sleeve space sooner, and cheap bumper and "
                "iron plates can be off by several percent. If your numbers seem "
                "to drift between gyms, plate accuracy is a likely reason.",
                {"tip": "Pound and kilogram plates are not interchangeable. A "
                        "45 lb plate is 20.4 kg, slightly more than a blue 20 kg "
                        "plate. Mixing them quietly changes your load."},
            ]),
            ("Microloading for steady progress", [
                "As you get stronger, adding 5 kg to a lift every week stops being "
                "realistic. Fractional plates of 0.5 kg, 1 kg or 1.25 kg let you add "
                "1-2.5 kg per session, which keeps "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload</a> going on pressing movements in particular.",
                "If your gym only goes down to 2.5 kg, the smallest jump is 5 kg. "
                "In that case, add reps before adding weight: move from 3 sets of 5 "
                "to 3 sets of 6 or 7, then increase the load. The "
                "<a href=\"/workouts/5x5-strength-program\">5x5 strength "
                "program</a> explains how to progress when jumps stall.",
            ]),
            ("Quick reference: common loads", [
                "These are the most common working weights on a 20 kg bar "
                "without collars. Plates listed are for one side, loaded "
                "heaviest first.",
                {"table": {
                    "head": ["Total", "Per side", "Plates per side"],
                    "rows": [
                        ["40 kg", "10 kg", "10"],
                        ["60 kg", "20 kg", "20"],
                        ["80 kg", "30 kg", "25 + 5"],
                        ["100 kg", "40 kg", "25 + 15"],
                        ["120 kg", "50 kg", "25 + 25"],
                        ["140 kg", "60 kg", "25 + 25 + 10"],
                        ["160 kg", "70 kg", "25 + 25 + 20"],
                        ["180 kg", "80 kg", "25 + 25 + 25 + 5"],
                        ["200 kg", "90 kg", "25 + 25 + 25 + 15"],
                    ],
                }},
                "In pound gyms the classic milestones are one plate (135 lb: "
                "a 45 lb plate a side), two plates (225 lb), three plates "
                "(315 lb) and four plates (405 lb), all on a 45 lb bar.",
                "Warm-ups are where a plate calculator saves the most time. A"
                " common pattern is the empty bar for 10 reps, then roughly "
                "40%, 60%, 75% and 85-90% of your working weight for fewer "
                "reps each set. Enter each of those numbers and load straight"
                " from the result instead of guessing and rounding mid-"
                "session.",
                {"tip": "When stripping a heavy bar, take one plate off each "
                        "side alternately. Unloading one side completely can "
                        "tip the bar off the rack."},
            ]),
            ("Bar weights and limitations", [
                "A men's Olympic bar weighs 20 kg and a women's 15 kg. Many gyms "
                "also have 10 kg technique bars and fixed EZ or straight bars that "
                "can weigh anything. If you are not sure, weigh it or ask. Smith "
                "machines and some trap bars have a different effective weight "
                "because of counterbalancing or their design.",
                "The calculator assumes plates are accurate to their label and "
                "that you load both sides identically. Use spring clips or collars "
                "for safety on every lift, even if they are not counted in the "
                "total.",
            ]),
        ],
        "faq": [
            ("How much does an Olympic barbell weigh?",
             "A men's Olympic barbell weighs 20 kg (about 44 lb) and a women's "
             "weighs 15 kg (about 33 lb). In pound gyms, standard bars are listed as "
             "45 lb."),
            ("Do collars count towards the total weight?",
             "Competition collars weigh 2.5 kg each and are counted in powerlifting "
             "and weightlifting. Light spring clips are usually ignored. Tick the "
             "collar option only if you use the 2.5 kg type."),
            ("Why should heavy plates go on first?",
             "Loading the heaviest plates closest to the centre keeps the bar "
             "balanced, makes the load easy to read and is standard in competition. "
             "It also stops small plates getting trapped behind big ones."),
            ("What if I cannot load the exact weight?",
             "The calculator shows the closest loadable weight and the remainder. "
             "Either round to that, add fractional plates or add a rep instead of "
             "weight."),
            ("Are 45 lb and 20 kg plates the same?",
             "No. A 45 lb plate is about 20.4 kg. The difference is small per plate "
             "but adds up on a heavy bar, so avoid mixing pound and kilogram plates."),
        ],
        "sources": [
            "International Weightlifting Federation. Technical and Competition "
            "Rules & Regulations.",
            "International Powerlifting Federation. Technical Rules Book.",
        ],
    },

    # ------------------------------------------------------------------
    "wilks-calculator": {
        "title": "Wilks & DOTS Calculator for Powerlifting Totals",
        "desc": ("Calculate your DOTS and Wilks scores from your powerlifting "
                 "total and bodyweight. Compare strength across weight classes and "
                 "see a rough strength level."),
        "intro": ("Lifting 200 kg at 60 kg bodyweight is not the same feat as at "
                  "120 kg. Enter your bodyweight and your squat, bench and "
                  "deadlift to get your DOTS and Wilks scores."),
        "body": [
            ("Why bodyweight-adjusted scores exist", [
                "Heavier lifters lift more weight in absolute terms, but not in "
                "direct proportion to bodyweight. Strength scales roughly with "
                "muscle cross-section, while bodyweight scales with volume, so a "
                "lighter lifter is usually stronger pound for pound.",
                "Powerlifting meets need a way to name a 'best lifter' across "
                "weight classes, and lifters want to compare themselves with friends "
                "of different sizes. Coefficient formulas like Wilks and DOTS solve "
                "this by converting your total into a single score that tries to "
                "remove the effect of bodyweight.",
            ]),
            ("How to use the calculator", [
                "Choose your sex, then enter your bodyweight and either your total "
                "or your best squat, bench press and deadlift separately. The "
                "calculator adds them up and returns both a DOTS score and a "
                "classic Wilks score, plus a rough strength level.",
                "Use lifts performed to a reasonable standard: squats to depth, "
                "a paused or at least controlled bench, and lockout on the "
                "deadlift. Touch-and-go benches and high squats inflate the score "
                "and make comparisons meaningless. If you only have rep maxes, "
                "estimate each lift with the "
                "<a href=\"/one-rep-max-calculator\">one rep max calculator</a> "
                "first.",
            ]),
            ("The formulas", [
                "Both scores multiply your total by a coefficient that depends on "
                "bodyweight (x, in kg). The coefficient is built from a polynomial "
                "fitted to elite lifting results, with separate constants for men "
                "and women.",
                {"formula": "DOTS = total × 500 / (A + Bx + Cx² + Dx³ + Ex⁴)"},
                {"formula": "Wilks = total × 500 / (a + bx + cx² + dx³ + ex⁴ + fx⁵)"},
                "The constants are long decimals, which is why nobody calculates "
                "these by hand. DOTS uses a fourth-degree polynomial and Wilks a "
                "fifth-degree one. Bodyweight inputs are capped at the edges of "
                "the range the formulas were fitted on, because the curves behave "
                "badly at extreme weights.",
            ]),
            ("Reading your DOTS score", [
                "There is no official classification, but the rough bands below "
                "reflect how DOTS scores tend to spread among raw (unequipped) "
                "lifters. Treat them as loose context, not a ranking.",
                {"table": {
                    "head": ["DOTS score", "Rough level"],
                    "rows": [
                        ["Below 200", "Beginner"],
                        ["200-300", "Novice to intermediate"],
                        ["300-400", "Intermediate to advanced"],
                        ["400-500", "Advanced, competitive at local meets"],
                        ["500 and above", "Elite, national level and beyond"],
                    ],
                }},
                "Example: an 83 kg man with a 600 kg total scores roughly 400 DOTS. "
                "A 63 kg woman with a 350 kg total scores around 375, close enough "
                "to compare directly, which is exactly the point of the score.",
                {"tip": "Your DOTS and Wilks numbers will be close but not "
                        "identical. Compare scores only within the same formula."},
            ]),
            ("Wilks, Wilks2, DOTS and IPF GL", [
                "The original Wilks formula was devised by Robert Wilks and was "
                "the standard best-lifter formula for decades. Over time lifters "
                "noticed it favoured some weight classes over others, particularly "
                "with modern women's totals.",
                "In 2020 an updated version, often called Wilks2, was released "
                "with refitted coefficients. Around the same time DOTS became "
                "popular in many federations as a simpler, fairer alternative. The "
                "International Powerlifting Federation now uses its own IPF GL "
                "points formula for best-lifter awards. This calculator shows DOTS "
                "and classic Wilks because they are the two most widely quoted "
                "outside the IPF.",
            ]),
            ("Scores at the same total", [
                "The easiest way to see what a bodyweight-adjusted score does"
                " is to hold the total fixed and change the bodyweight. Here "
                "is an approximate DOTS score for a 500 kg total for men at "
                "different bodyweights.",
                {"table": {
                    "head": ["Bodyweight", "Total", "Approx. DOTS"],
                    "rows": [
                        ["66 kg", "500 kg", "~390"],
                        ["74 kg", "500 kg", "~360"],
                        ["83 kg", "500 kg", "~340"],
                        ["93 kg", "500 kg", "~320"],
                        ["105 kg", "500 kg", "~300"],
                        ["120 kg", "500 kg", "~285"],
                    ],
                }},
                "The lighter lifter scores higher because lifting 500 kg is a"
                " much bigger achievement relative to their size. Notice that"
                " the drop gets smaller at higher bodyweights: the curve "
                "flattens because bigger lifters gain relatively less "
                "strength per extra kilogram.",
                "This is also why the score is useful for planning. If you "
                "are thinking about moving up a weight class, work out the "
                "total you would need at the heavier bodyweight to keep the "
                "same score. If that jump looks unrealistic within a year, "
                "the extra weight may cost you more than it gives.",
                "Remember that a coefficient cannot make up for missing "
                "standards. Compare scores only when the lifts were done to "
                "similar depth, pause and lockout rules, and preferably in "
                "the same equipment category.",
            ]),
            ("Limitations", [
                "Every coefficient formula is a compromise built from top-level "
                "results, so it is least accurate at the very light and very heavy "
                "ends. None of them account for age, height, equipment or drug "
                "testing, and a score from a gym session is not the same as one "
                "under competition judging.",
                "Use your score to track your own progress over time, or to see "
                "whether gaining weight actually made you stronger relative to "
                "your size. A rising DOTS after a bulk means the extra bodyweight "
                "paid off.",
            ]),
            ("Raising your score", [
                "The surest way to a higher score is a higher total at a stable "
                "bodyweight. A structured strength block such as the "
                "<a href=\"/workouts/5x5-strength-program\">5x5 strength "
                "program</a>, steady "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload</a> and good technique on the "
                "<a href=\"/exercises/barbell-back-squat\">squat</a>, "
                "<a href=\"/exercises/bench-press\">bench press</a> and "
                "<a href=\"/exercises/deadlift\">deadlift</a> will move it more "
                "than any diet trick. Load your bar quickly with the "
                "<a href=\"/plate-calculator\">plate calculator</a>.",
            ]),
        ],
        "faq": [
            ("What is a good DOTS score?",
             "Roughly, 300 marks a solid intermediate lifter, 400 is advanced and "
             "500 or more is elite. These are loose guides rather than official "
             "classifications."),
            ("What is the difference between Wilks and DOTS?",
             "Both convert a total into a bodyweight-adjusted score using a "
             "polynomial. DOTS uses newer data and a simpler curve, and many "
             "consider it fairer across weight classes than classic Wilks."),
            ("Which formula does the IPF use?",
             "The International Powerlifting Federation uses its own IPF GL points "
             "for best-lifter awards. Other federations use DOTS, Wilks or Wilks2."),
            ("Can I compare men's and women's scores?",
             "That is one of the aims, since each sex has its own coefficients. In "
             "practice, cross-sex comparisons are rougher than comparisons within "
             "the same sex."),
            ("Should I gain weight to increase my score?",
             "Only if your total rises faster than the coefficient falls. Gaining "
             "muscle often helps, but gaining mostly fat usually lowers your score "
             "even if your total goes up slightly."),
        ],
        "sources": [
            "Vanderburgh PM, Batterham AM. Validation of the Wilks powerlifting "
            "formula. Med Sci Sports Exerc. 1999.",
            "International Powerlifting Federation. IPF GL Points formula.",
        ],
    },
}
