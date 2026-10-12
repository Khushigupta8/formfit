"""
Standalone guides, part A.

Eight long-form guides on fat loss, protein, body composition and training.
Each dict follows the shared content spec: body is a list of
(heading, blocks) tuples, faq is a list of (question, answer) tuples.
"""

G_CALORIES = {
    "slug": "how-to-calculate-calories-for-weight-loss",
    "title": "How to Calculate Calories for Weight Loss",
    "desc": ("Work out your maintenance calories, pick a sensible deficit and "
             "adjust it from real scale data. A step-by-step method with "
             "worked examples and tables."),
    "h1": "How to calculate your calories for weight loss, step by step",
    "category": "Fat Loss",
    "image": "scale",
    "intro": ("Every diet that works, works by putting you in a calorie "
              "deficit. The hard part is not the principle but the number: "
              "how many calories should you actually eat, and what do you do "
              "when the scale ignores the maths?"),
    "body": [
        ("The short version", [
            "Estimate your maintenance calories, subtract 15 to 25 percent, "
            "eat that amount consistently for two to three weeks, then "
            "adjust based on what your weekly average weight actually does. "
            "That is the whole method. Everything below explains how to do "
            "each step well.",
            "The reason it works is energy balance. When you eat less energy "
            "than you burn, your body makes up the difference from stored "
            "energy, mostly fat if you keep protein high and keep lifting. "
            "The formula gives you a starting point. Your own scale data "
            "tells you the real answer.",
        ]),
        ("Step 1: estimate your maintenance calories", [
            "Maintenance, or total daily energy expenditure (TDEE), is the "
            "number of calories you burn in a typical day. It has four parts: "
            "your basal metabolic rate (BMR), the energy you spend digesting "
            "food, deliberate exercise, and all the incidental movement you "
            "do without thinking, such as walking, standing and fidgeting.",
            "The quickest way to estimate it is our <a href=\"/tdee-calculator\">"
            "TDEE calculator</a>. It uses the Mifflin-St Jeor equation for BMR, "
            "which a 2005 review in the Journal of the American Dietetic "
            "Association (Frankenfield et al.) found to be the most accurate "
            "of the common equations for most adults, and multiplies it by an "
            "activity factor.",
            {"formula": "Men: BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age + 5"},
            {"formula": "Women: BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age - 161"},
            "Be honest with the activity level. Most people who train three "
            "or four times a week but sit at a desk all day are \"lightly "
            "active\", not \"very active\". Overestimating activity is the "
            "single most common reason a calculated deficit fails to produce "
            "weight loss.",
            {"table": {
                "head": ["Activity level", "Multiplier", "Typical person"],
                "rows": [
                    ["Sedentary", "1.2", "Desk job, little walking, no training"],
                    ["Lightly active", "1.375", "Desk job, 3 workouts a week, 5-7k steps"],
                    ["Moderately active", "1.55", "On feet part of the day or 4-5 hard sessions"],
                    ["Very active", "1.725", "Physical job or daily hard training"],
                    ["Extremely active", "1.9", "Manual labour plus training, or endurance athletes"],
                ]}},
        ]),
        ("Step 2: choose the size of your deficit", [
            "A deficit expressed as a percentage of maintenance scales "
            "sensibly with body size. A 500 calorie cut is mild for a large, "
            "active man and aggressive for a small, sedentary woman.",
            {"table": {
                "head": ["Deficit", "Expected loss per week", "Best for"],
                "rows": [
                    ["10-15%", "0.25-0.5% of bodyweight", "Lean lifters, long diets, recomposition"],
                    ["15-25%", "0.5-0.8% of bodyweight", "Most people, most of the time"],
                    ["25-30%", "0.8-1% of bodyweight", "Higher body fat, short focused phases"],
                ]}},
            "A useful guardrail from sports nutrition research is a loss rate "
            "of roughly 0.5 to 1 percent of bodyweight per week. Helms and "
            "colleagues, writing in the Journal of the International Society "
            "of Sports Nutrition in 2014, recommended this range for lifters "
            "who want to keep muscle while dieting. Slower is safer for "
            "muscle; faster is fine if you carry more fat.",
            "If you prefer a target date, our <a href=\"/weight-loss-calculator\">"
            "weight loss calculator</a> works backwards from your goal weight "
            "and tells you whether the timeline you have in mind is realistic.",
        ]),
        ("A worked example", [
            "Take a 32-year-old woman who is 165 cm (5 ft 5 in) tall, weighs "
            "75 kg (165 lb), works at a desk and lifts three times a week.",
            {"olist": [
                "BMR: 10 x 75 + 6.25 x 165 - 5 x 32 - 161 = 1,460 kcal.",
                "TDEE: 1,460 x 1.375 (lightly active) = about 2,010 kcal.",
                "Deficit of 20%: 2,010 x 0.8 = about 1,600 kcal per day.",
                "Expected loss: roughly 0.4-0.6 kg (1-1.3 lb) per week, "
                "which is 0.5-0.8% of her bodyweight. Right in the target range.",
            ]},
            "Now a 28-year-old man, 180 cm (5 ft 11 in), 95 kg (209 lb), "
            "moderately active. His BMR is about 1,940 kcal, his TDEE about "
            "3,000 kcal, and a 20% deficit puts him near 2,400 kcal. Same "
            "method, very different number, which is why copying someone "
            "else's diet rarely works.",
        ]),
        ("Step 3: set protein first, then fill in the rest", [
            "Calories decide how much weight you lose. Protein has a big say "
            "in whether that weight comes from fat or muscle. Aim for about "
            "1.6 to 2.2 g of protein per kg of bodyweight (0.7 to 1 g per lb) "
            "while dieting. If you carry a lot of body fat, base it on your "
            "goal weight instead.",
            "Once protein is set, keep fat at roughly 20 to 35 percent of "
            "calories, which supports hormones and makes meals satisfying, "
            "and give the remainder to carbohydrates to fuel training. The "
            "<a href=\"/macro-calculator\">macro calculator</a> does this split "
            "for you, and the <a href=\"/guides/how-much-protein-to-build-muscle\">"
            "protein guide</a> covers the reasoning in detail.",
        ]),
        ("Step 4: track for two weeks before changing anything", [
            "The formula is an estimate. Individual metabolic rates vary by "
            "a few hundred calories either way, and food labels are allowed "
            "to be off too. So treat your first number as a hypothesis and "
            "test it.",
            {"list": [
                "Weigh yourself every morning, after the toilet, before food or drink.",
                "Log your intake as accurately as you can. A cheap kitchen scale beats guessing.",
                "Compare <strong>weekly averages</strong>, not single days. Water, salt, "
                "carbs and digestion can swing daily weight by 1-2 kg.",
                "Ignore the first week. Initial drops are mostly water and glycogen.",
            ]},
            {"tip": "If your weekly average has not moved in two to three "
                    "weeks and you have tracked honestly, cut 150-250 kcal per "
                    "day or add 2,000-3,000 daily steps. Make one change at a time."},
        ]),
        ("Why the numbers stop working, and what to do", [
            "As you lose weight, your maintenance drops. A lighter body costs "
            "less to run and to move, and most people unconsciously move "
            "less when dieting. This is why a deficit that worked brilliantly "
            "in month one can stall in month three.",
            "The fix is simple: recalculate your maintenance every 4 to 5 kg "
            "(10 lb) lost, and keep an eye on your step count, since a drop in "
            "everyday movement can quietly erase a few hundred calories of "
            "deficit. If you have been dieting for more than 12 weeks and "
            "you feel flat, a one or two week break at maintenance often "
            "helps adherence more than it slows progress.",
        ]),
        ("Common mistakes that hide a deficit", [
            {"list": [
                "<strong>Weekend drift.</strong> A 500 kcal daily deficit "
                "Monday to Friday is 2,500 kcal. Two relaxed weekend days at "
                "+1,200 each wipe out most of it.",
                "<strong>Untracked liquids and oils.</strong> A tablespoon of "
                "oil is about 120 kcal. Lattes, juices and alcohol add up fast.",
                "<strong>Eating back exercise calories.</strong> Fitness "
                "trackers often overestimate burn. Use the "
                "<a href=\"/calories-burned-calculator\">calories burned "
                "calculator</a> as a rough guide and eat back half at most.",
                "<strong>Cutting too hard.</strong> Very large deficits raise "
                "hunger, wreck training and usually end in a rebound.",
            ]},
        ]),
        ("When to be careful", [
            "Calorie counting is a tool, not a requirement. If tracking "
            "makes you anxious or you have a history of disordered eating, "
            "work with a doctor or registered dietitian instead. The same "
            "applies if you are pregnant or breastfeeding, under 18, or "
            "managing a condition such as diabetes, where changes in intake "
            "can affect medication.",
            "As a floor, most adults should not routinely eat below their "
            "BMR without medical supervision. If your calculated target "
            "falls under it, slow down the rate of loss and move more "
            "rather than eating less.",
        ]),
    ],
    "faq": [
        ("How many calories should I eat to lose 0.5 kg a week?",
         "A common rule of thumb is a daily deficit of about 500 kcal, since "
         "a kilogram of body fat stores roughly 7,700 kcal. Real-world loss is "
         "less predictable than the arithmetic, so set the deficit, then "
         "check your weekly average after two to three weeks and adjust."),
        ("Is 1,200 calories a day enough?",
         "For some small, sedentary women it can be a reasonable short-term "
         "target, but for most adults it is too low and makes protein and "
         "micronutrient needs hard to meet. Calculate your own BMR and TDEE "
         "rather than using a generic number."),
        ("Should I count calories on rest days differently?",
         "You can keep calories the same every day for simplicity, or move "
         "some carbohydrates from rest days to training days. What matters "
         "most is your weekly average intake."),
        ("Why am I not losing weight in a calorie deficit?",
         "Usually because the deficit is smaller than you think, through "
         "overestimated activity, untracked food or weekend overeating, or "
         "because water retention is masking fat loss. Track carefully for "
         "two more weeks and compare weekly averages before changing anything."),
    ],
    "related_calcs": ["tdee-calculator", "calorie-calculator",
                      "weight-loss-calculator", "macro-calculator"],
}

G_PROTEIN = {
    "slug": "how-much-protein-to-build-muscle",
    "title": "How Much Protein Do You Need to Build Muscle?",
    "desc": ("The evidence-based protein target for muscle growth, how to "
             "split it across meals, the best food sources, and when eating "
             "more actually helps."),
    "h1": "How much protein do you really need to build muscle?",
    "category": "Nutrition",
    "image": "protein-food",
    "intro": ("Protein is the one nutrient lifters argue about most and "
              "measure least. The research is clearer than the arguments: "
              "there is a range that works, a point beyond which more does "
              "little, and a few details that matter more than the exact gram."),
    "body": [
        ("The number", [
            "For people who lift weights and want to build or keep muscle, "
            "aim for <strong>1.6 to 2.2 g of protein per kg of bodyweight per "
            "day</strong>, which is about 0.7 to 1 g per lb.",
            "The lower end comes from a 2018 meta-analysis by Morton and "
            "colleagues in the British Journal of Sports Medicine, which "
            "pooled 49 trials and found that the benefit of extra protein on "
            "lean mass gains plateaued at around 1.6 g/kg per day, with an "
            "upper confidence limit near 2.2 g/kg. Most people will capture "
            "nearly all of the benefit at 1.6 g/kg. Going higher is a cheap "
            "insurance policy, not a requirement.",
            "For comparison, the general adult recommendation (the RDA) is "
            "0.8 g/kg. That figure is set to prevent deficiency in sedentary "
            "people, not to maximise muscle growth.",
        ]),
        ("Quick reference by bodyweight", [
            {"table": {
                "head": ["Bodyweight", "1.6 g/kg (minimum)", "2.2 g/kg (upper)"],
                "rows": [
                    ["55 kg (121 lb)", "88 g", "121 g"],
                    ["65 kg (143 lb)", "104 g", "143 g"],
                    ["75 kg (165 lb)", "120 g", "165 g"],
                    ["85 kg (187 lb)", "136 g", "187 g"],
                    ["95 kg (209 lb)", "152 g", "209 g"],
                    ["105 kg (231 lb)", "168 g", "231 g"],
                ]}},
            "Want a personalised number that accounts for your goal and "
            "activity? Use the <a href=\"/protein-calculator\">protein "
            "calculator</a>.",
        ]),
        ("When to aim higher", [
            "Two situations justify sitting at the top of the range or "
            "slightly above it.",
            {"list": [
                "<strong>Dieting.</strong> In a calorie deficit your body is "
                "more willing to break down muscle for energy. Higher protein, "
                "around 2.0-2.4 g/kg of lean mass, helps protect it. Protein is "
                "also the most filling macronutrient, which makes a deficit "
                "easier to sustain.",
                "<strong>Older lifters.</strong> Muscle becomes less responsive "
                "to protein with age, so people over about 50 tend to benefit "
                "from larger servings, closer to 0.4 g/kg per meal.",
            ]},
            "If you carry a lot of body fat, calculating protein from total "
            "bodyweight gives an inflated number. Use your goal weight, or "
            "your lean body mass from the <a href=\"/lean-body-mass-calculator\">"
            "lean body mass calculator</a>, instead.",
        ]),
        ("How to split it across the day", [
            "Total daily intake matters most. Distribution is a refinement, "
            "but a sensible one. Muscle protein synthesis responds to each "
            "protein-rich meal, so three to five meals of roughly 0.3-0.4 g/kg "
            "each is a practical pattern for most people.",
            "For a 75 kg lifter targeting 140 g a day, that might look like "
            "four meals of about 35 g. You do not need to time a shake to "
            "the minute after training; having a protein-containing meal "
            "within a few hours either side of your session is plenty. The "
            "<a href=\"/guides/pre-and-post-workout-nutrition\">workout "
            "nutrition guide</a> goes deeper on timing.",
            "One meal with 100 g and the rest of the day near zero is less "
            "practical than spreading it out, and it is also harder to eat.",
        ]),
        ("Best protein sources, compared", [
            {"table": {
                "head": ["Food", "Serving", "Protein", "Calories (approx.)"],
                "rows": [
                    ["Chicken breast, cooked", "100 g", "31 g", "165"],
                    ["Greek yogurt, 0% fat", "200 g", "20 g", "115"],
                    ["Eggs", "3 large", "19 g", "215"],
                    ["Paneer", "100 g", "18 g", "265-320"],
                    ["Tinned tuna, drained", "1 can (110 g)", "26 g", "115"],
                    ["Lentils, cooked", "1 cup (200 g)", "18 g", "230"],
                    ["Firm tofu", "150 g", "20-25 g", "180"],
                    ["Whey protein", "1 scoop (30 g)", "22-25 g", "120"],
                ]}},
            "Values vary by brand and preparation, so check labels. Animal "
            "proteins and soy are complete and rich in leucine, the amino "
            "acid that most strongly switches on muscle building. Plant-based "
            "eaters can do just as well by eating a variety of sources and "
            "aiming toward the upper end of the range.",
        ]),
        ("Do you need protein powder?", [
            "No. Powder is food, just a convenient one. It is useful if you "
            "struggle to hit your target, train early, or want a cheap, "
            "low-calorie protein hit. Whey and casein are well studied; "
            "soy and pea blends work well for vegans.",
            "Look for products that carry third-party testing marks, because "
            "supplements are less tightly regulated than food in many "
            "countries.",
        ]),
        ("A day of eating at 140 g", [
            "Numbers are easier to hit when you can picture them. Here is "
            "one ordinary day for a 75 kg lifter aiming for about 140 g, "
            "using everyday foods rather than supplements at every meal.",
            {"table": {
                "head": ["Meal", "Food", "Protein"],
                "rows": [
                    ["Breakfast", "3 eggs, 2 slices wholegrain toast, 150 g Greek yogurt", "35 g"],
                    ["Lunch", "150 g cooked chicken, rice, salad", "45 g"],
                    ["Snack", "Glass of milk (300 ml) and a handful of peanuts", "17 g"],
                    ["Dinner", "Lentil and paneer curry (100 g paneer, 1 cup dal), roti", "38 g"],
                    ["Total", "", "about 135-140 g"],
                ]}},
            "Notice that carbohydrate foods such as bread, rice and roti "
            "contribute a few grams each. They are not protein sources, but "
            "across a day they add 10-20 g that people forget to count.",
            "Vegetarians can hit the same target by leaning on dairy, eggs, "
            "soy and pulses. Vegans should plan a little more deliberately: "
            "tofu, tempeh, seitan, lentils, chickpeas and a pea or soy powder "
            "make 1.6-2.0 g/kg very achievable.",
        ]),
        ("What about protein while bulking?", [
            "When you are in a calorie surplus, extra energy already protects "
            "your muscle and supports growth, so there is less benefit to "
            "pushing protein high. 1.6-2.0 g/kg is plenty. Use the calories "
            "you free up for carbohydrates, which fuel harder training. The "
            "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting guide</a> "
            "covers how to set up each phase.",
        ]),
        ("Is high protein safe?", [
            "For healthy adults, intakes up to about 2.2 g/kg are well "
            "within the range studied without harm. Concerns about kidney "
            "damage come mainly from people with existing kidney disease, "
            "for whom protein intake should be set by their doctor.",
            "The practical downside of very high protein is that it crowds "
            "out carbohydrates and fats, which fuel training and support "
            "hormones. More is not better past the plateau.",
            "Two practical cautions. If you raise protein sharply, increase "
            "your water intake too, since processing protein produces more "
            "urea for your kidneys to clear; the <a href=\"/water-intake-calculator\">"
            "water intake calculator</a> gives a sensible daily target. And "
            "keep fibre up with vegetables, fruit and whole grains, because "
            "high-protein diets built on meat and shakes alone can be low in it.",
        ]),
        ("A simple way to hit your target", [
            {"olist": [
                "Work out your number with the <a href=\"/protein-calculator\">"
                "protein calculator</a>.",
                "Divide it by the number of meals you actually eat.",
                "Build every meal around a palm-to-two-palm portion of a protein food.",
                "Track for one week to see where you fall short, then fix the weakest meal, "
                "usually breakfast.",
            ]},
            {"tip": "Breakfast is where most people lose protein. Swapping toast "
                    "for eggs, Greek yogurt or a protein smoothie often closes a "
                    "30-40 g daily gap on its own."},
        ]),
    ],
    "faq": [
        ("Can my body only absorb 30 g of protein at once?",
         "No. Your gut absorbs nearly all the protein you eat; larger servings "
         "just take longer to digest and use. Spreading protein across three to "
         "five meals is practical and sensible, but a bigger serving is not "
         "simply wasted."),
        ("Should I eat protein on rest days?",
         "Yes. Muscle repair and growth continue for a day or two after "
         "training, so keep your protein intake roughly the same every day."),
        ("Is plant protein as good for building muscle?",
         "It can be, provided you eat enough and combine sources. Plant proteins "
         "are often lower in leucine, so aiming toward the upper end of the range "
         "and including soy, lentils, beans and grains makes up the difference."),
        ("How much protein do I need if I don't lift weights?",
         "The general recommendation is 0.8 g/kg, though many experts consider "
         "1.0-1.2 g/kg a better target for active adults and older people."),
    ],
    "related_calcs": ["protein-calculator", "macro-calculator",
                      "lean-body-mass-calculator"],
}

G_BMI_BF = {
    "slug": "bmi-vs-body-fat-percentage",
    "title": "BMI vs Body Fat Percentage: Which Should You Use?",
    "desc": ("BMI is quick, body fat percentage is more telling. Learn what "
             "each measures, where BMI misleads lifters, and how to track "
             "body composition properly."),
    "h1": "BMI vs body fat percentage: what each number really tells you",
    "category": "Health & Recovery",
    "image": "measuring-tape",
    "intro": ("BMI says a muscular lifter is overweight and can call a "
              "sedentary person with little muscle healthy. Body fat "
              "percentage fixes that, but it is harder to measure. Here is "
              "when each one is useful and how to use them together."),
    "body": [
        ("What BMI measures", [
            "Body mass index is your weight divided by your height squared. "
            "It was devised in the 1830s by the Belgian statistician Adolphe "
            "Quetelet to describe populations, not to diagnose individuals.",
            {"formula": "BMI = weight (kg) / height (m)²"},
            {"formula": "BMI = 703 x weight (lb) / height (in)²"},
            {"table": {
                "head": ["BMI", "WHO category"],
                "rows": [
                    ["Below 18.5", "Underweight"],
                    ["18.5-24.9", "Healthy weight"],
                    ["25.0-29.9", "Overweight"],
                    ["30.0 and above", "Obesity"],
                ]}},
            "Some health bodies use lower cut-offs for people of South Asian, "
            "Chinese and other Asian backgrounds, because cardiometabolic risk "
            "tends to rise at lower BMIs. India's guidelines, for example, "
            "treat 23 as the start of overweight. You can check your own "
            "figure with the <a href=\"/bmi-calculator\">BMI calculator</a>.",
        ]),
        ("Why BMI works for most people", [
            "BMI gets criticised a lot, but it earns its place. It needs only "
            "a tape measure and a scale, it is free, and across large groups "
            "of people it tracks reasonably well with body fat and with the "
            "risk of type 2 diabetes, heart disease and early death.",
            "For the average sedentary adult, a BMI of 32 almost always "
            "means excess body fat. In that situation, the extra precision "
            "of a body fat test rarely changes the advice.",
        ]),
        ("Where BMI gets it wrong", [
            "BMI cannot tell muscle from fat. It also says nothing about where "
            "fat is stored, which matters more for health than how much there is.",
            {"list": [
                "<strong>Muscular lifters.</strong> A 180 cm man at 90 kg and "
                "12% body fat has a BMI of 27.8, labelled overweight, despite "
                "being lean.",
                "<strong>\"Normal weight\" with high body fat.</strong> Someone "
                "with little muscle can sit at a BMI of 23 while carrying 30%+ "
                "body fat, sometimes called normal-weight obesity.",
                "<strong>Older adults.</strong> Muscle loss with age can keep "
                "BMI stable while body fat quietly rises.",
                "<strong>Fat distribution.</strong> Two people with identical "
                "BMIs can have very different amounts of visceral (abdominal) fat.",
            ]},
        ]),
        ("What body fat percentage measures", [
            "Body fat percentage is the share of your total weight that is "
            "fat. The rest is lean mass: muscle, bone, organs and water. It "
            "describes what your body is made of, which is exactly what a "
            "lifter cares about.",
            {"table": {
                "head": ["Category", "Men", "Women"],
                "rows": [
                    ["Essential fat", "2-5%", "10-13%"],
                    ["Athletic", "6-13%", "14-20%"],
                    ["Fitness", "14-17%", "21-24%"],
                    ["Average", "18-24%", "25-31%"],
                    ["Above average", "25%+", "32%+"],
                ]}},
            "These bands are widely used reference ranges from the American "
            "Council on Exercise, not medical cut-offs. Women naturally carry "
            "more essential fat, so their numbers run about 8-10 points higher.",
        ]),
        ("How to estimate body fat", [
            "No home method is perfectly accurate, and even lab methods "
            "disagree by a few percent. Pick one, use it consistently, and "
            "watch the trend.",
            {"table": {
                "head": ["Method", "Cost", "Typical error", "Notes"],
                "rows": [
                    ["Tape measure (US Navy formula)", "Free", "3-4%", "Good for tracking trends"],
                    ["Skinfold calipers", "Low", "3-5%", "Depends heavily on technique"],
                    ["Bioimpedance scales", "Low-medium", "4-8%", "Swings with hydration"],
                    ["DEXA scan", "High", "1-3%", "Best accessible reference"],
                ]}},
            "The <a href=\"/body-fat-calculator\">body fat calculator</a> uses "
            "the US Navy tape method, which needs only your neck, waist and "
            "(for women) hip measurements. Our "
            "<a href=\"/guides/how-to-measure-body-fat-at-home\">home "
            "measurement guide</a> explains how to take them properly.",
        ]),
        ("Two people, same BMI", [
            "A worked example makes the difference concrete. Both of these "
            "people are 175 cm (5 ft 9 in) tall and weigh 85 kg (187 lb), so "
            "both have a BMI of 27.8, which falls in the overweight band.",
            {"table": {
                "head": ["", "Person A", "Person B"],
                "rows": [
                    ["Training history", "5 years lifting", "Sedentary"],
                    ["Body fat", "14%", "29%"],
                    ["Fat mass", "11.9 kg", "24.7 kg"],
                    ["Lean mass", "73.1 kg", "60.3 kg"],
                    ["Waist", "82 cm", "100 cm"],
                    ["Waist-to-height ratio", "0.47", "0.57"],
                ]}},
            "BMI treats them identically. Body fat and waist measurements show "
            "that person A is lean and muscular while person B carries twice as "
            "much fat, much of it around the middle. The useful advice for each "
            "is completely different: person A needs nothing, person B would "
            "benefit from a moderate calorie deficit and strength training.",
            "This is the core reason lifters should not judge themselves by BMI "
            "alone, and also why non-lifters should not dismiss a high BMI as "
            "\"just muscle\" without checking.",
        ]),
        ("Tracking change over time", [
            "The bigger value of body composition is not a single reading but "
            "what it tells you about change. When you diet, you want to know "
            "whether the weight you lose is fat or muscle. When you bulk, you "
            "want to know whether the weight you gain is mostly muscle.",
            "Multiply your weight by your body fat percentage to get fat mass, "
            "and subtract that from your weight to get lean mass. Compare both "
            "every month. If lean mass is holding steady or rising while fat "
            "mass falls, your training and nutrition are doing their job. The "
            "<a href=\"/lean-body-mass-calculator\">lean body mass calculator</a> "
            "gives you a second estimate from height and weight alone.",
        ]),
        ("The underrated third number: your waist", [
            "If you want one extra measurement that predicts health risk, "
            "make it your waist. Abdominal fat is the type most closely linked "
            "to metabolic disease, and waist size captures it in a way BMI cannot.",
            "A simple guideline used by the UK's NICE is to keep your waist "
            "below half your height. A 170 cm person should aim for a waist "
            "under 85 cm. You can also check your <a href=\"/waist-to-hip-ratio-calculator\">"
            "waist-to-hip ratio</a>, which the WHO flags as raised above 0.90 "
            "for men and 0.85 for women.",
        ]),
        ("Which should you use?", [
            {"list": [
                "<strong>Use BMI</strong> as a quick screening number, especially "
                "if you do not lift and are not very muscular.",
                "<strong>Use body fat percentage</strong> if you strength train, "
                "are recomposing, or want to know whether weight changes are "
                "fat or muscle.",
                "<strong>Use waist measurements</strong> alongside either, as a "
                "simple health check.",
            ]},
            "Lifters who want one more step can calculate their "
            "<a href=\"/ffmi-calculator\">FFMI</a>, which is essentially BMI "
            "for lean mass only. It tells you how muscular you are relative "
            "to your height, independent of fat.",
            "For most people a sensible routine is: check BMI once to see where "
            "you stand, measure your waist monthly, and if you train, add a "
            "body fat estimate every month or two using the same method each "
            "time. If any of these numbers are high, or have been rising, it "
            "is worth discussing with a doctor, who may also check blood "
            "pressure, blood sugar and cholesterol, the markers that matter "
            "most for long-term health.",
            {"tip": "Track monthly, under the same conditions: same time of day, "
                    "same method, same person measuring. Trends over three months "
                    "tell you far more than any single reading."},
        ]),
    ],
    "faq": [
        ("Is BMI accurate for bodybuilders?",
         "No. Because BMI cannot separate muscle from fat, muscular people are "
         "often classified as overweight or even obese. Body fat percentage, "
         "waist measurements or FFMI give a much better picture for lifters."),
        ("What is a healthy body fat percentage?",
         "For general health, roughly 10-20% for men and 20-30% for women is a "
         "reasonable range. Athletes are often leaner, but going below about "
         "5% for men or 13% for women is not healthy to sustain."),
        ("Why do smart scales give different body fat readings each day?",
         "They send a small electrical current through your body, and the "
         "result depends heavily on hydration, recent meals and exercise. Weigh "
         "at the same time each morning and use the trend, not the daily figure."),
        ("Can I have a normal BMI and still be unhealthy?",
         "Yes. A normal BMI with high body fat, a large waist or low muscle mass "
         "can still carry raised metabolic risk. Regular strength training and "
         "a waist check help close that gap."),
    ],
    "related_calcs": ["bmi-calculator", "body-fat-calculator",
                      "ffmi-calculator", "waist-to-hip-ratio-calculator"],
}

G_BEGINNER = {
    "slug": "beginner-gym-guide",
    "title": "Beginner Gym Guide: Your First Month, Step by Step",
    "desc": ("Nervous about starting at the gym? A practical plan for your "
             "first four weeks: what to do, how much to lift, gym etiquette, "
             "and how to keep progressing."),
    "h1": "The beginner's gym guide: your first month, step by step",
    "category": "Training",
    "image": "gym-floor",
    "intro": ("Walking into a gym for the first time is mostly a confidence "
              "problem, not a fitness problem. With a short plan, a handful of "
              "exercises and a few unwritten rules, your first month can set "
              "up years of progress."),
    "body": [
        ("What actually matters in month one", [
            "Beginners overthink programme choice and underthink consistency. "
            "In your first months almost any sensible plan works, because your "
            "body is reacting to a brand new stimulus. What does not work is "
            "turning up twice, getting sore, and disappearing for three weeks.",
            "So the goals for month one are simple: train two or three times "
            "a week, learn six to eight basic movements, leave each session "
            "feeling you could have done a bit more, and write everything down.",
        ]),
        ("Before your first session", [
            {"list": [
                "<strong>Get a check-up if needed.</strong> If you have a heart "
                "condition, high blood pressure, are pregnant, or have been "
                "inactive for years with health concerns, speak to a doctor first.",
                "<strong>Take the induction.</strong> Most gyms offer a free "
                "tour. Use it to learn where things are and how the machines adjust.",
                "<strong>Pack light.</strong> Comfortable clothes, flat-soled "
                "shoes, a water bottle, a towel, and your phone or a notebook "
                "for logging.",
                "<strong>Go at a quiet time.</strong> Mid-morning, early "
                "afternoon and late evening are usually calmer than 6 pm.",
            ]},
        ]),
        ("The eight movements to learn", [
            "Nearly every strength programme is built from a few movement "
            "patterns. Learn these and you can follow almost any plan.",
            {"table": {
                "head": ["Pattern", "Start with", "Progress to"],
                "rows": [
                    ["Squat", "Goblet squat or <a href=\"/exercises/leg-press\">leg press</a>",
                     "<a href=\"/exercises/barbell-back-squat\">Barbell back squat</a>"],
                    ["Hinge", "Dumbbell <a href=\"/exercises/romanian-deadlift\">Romanian deadlift</a>",
                     "<a href=\"/exercises/deadlift\">Deadlift</a>"],
                    ["Horizontal push", "<a href=\"/exercises/push-up\">Push-up</a>",
                     "<a href=\"/exercises/bench-press\">Bench press</a>"],
                    ["Vertical push", "Dumbbell shoulder press",
                     "<a href=\"/exercises/overhead-press\">Overhead press</a>"],
                    ["Horizontal pull", "Seated cable row",
                     "<a href=\"/exercises/barbell-row\">Barbell row</a>"],
                    ["Vertical pull", "<a href=\"/exercises/lat-pulldown\">Lat pulldown</a>",
                     "<a href=\"/exercises/pull-up\">Pull-up</a>"],
                    ["Single leg", "Split squat", "<a href=\"/exercises/walking-lunge\">Walking lunge</a>"],
                    ["Core", "<a href=\"/exercises/plank\">Plank</a>", "Longer planks, carries"],
                ]}},
            "Machines and dumbbells are not \"cheating\". They are a sensible "
            "way to learn a movement and build strength before adding the "
            "skill demands of a barbell.",
        ]),
        ("A simple first-month plan", [
            "Train three non-consecutive days a week, for example Monday, "
            "Wednesday and Friday. Alternate two full-body sessions.",
            {"table": {
                "head": ["Workout A", "Sets x reps", "Workout B", "Sets x reps"],
                "rows": [
                    ["Goblet squat", "3 x 10", "Romanian deadlift (DB)", "3 x 10"],
                    ["Dumbbell bench press", "3 x 10", "Dumbbell shoulder press", "3 x 10"],
                    ["Lat pulldown", "3 x 10", "Seated cable row", "3 x 10"],
                    ["Walking lunge", "2 x 10 each leg", "Leg press", "2 x 12"],
                    ["Plank", "3 x 20-30 s", "Dumbbell curl", "2 x 12"],
                ]}},
            "Rest 60 to 120 seconds between sets. A session should take 45 to "
            "60 minutes including a warm-up. When you are ready for something "
            "more structured, move on to our <a href=\"/workouts/beginner-full-body-workout\">"
            "beginner full-body workout</a>.",
        ]),
        ("How heavy should you lift?", [
            "Choose a weight you can lift for the target reps with good form "
            "and about two or three reps left in the tank. The last couple of "
            "reps should feel challenging, but your technique should not "
            "change. If it breaks down, the weight is too heavy.",
            "In week one, deliberately start light. You are learning, and "
            "very new lifters get sore easily. Each session, add a little: "
            "one more rep, or the next dumbbell up once you hit the top of "
            "the rep range on every set. That is "
            "<a href=\"/guides/progressive-overload-explained\">progressive "
            "overload</a>, and it is the engine of all progress.",
            "Before your working sets, warm up properly:",
            {"olist": [
                "Five minutes on a bike, rower or brisk incline walk.",
                "A few dynamic moves: leg swings, arm circles, bodyweight squats, hip hinges.",
                "One or two light sets of your first exercise, at about 50% of your working weight.",
            ]},
            "That is enough. Long static stretching before lifting is not "
            "needed; save it for after training if you enjoy it.",
            "Once you know your working weights, a quick estimate of your "
            "maximum can help you plan. Enter a recent set into the "
            "<a href=\"/one-rep-max-calculator\">one-rep max calculator</a>, "
            "but do not test true one-rep maxes in your first months; there "
            "is nothing to gain from it yet.",
        ]),
        ("Gym etiquette nobody tells you", [
            {"list": [
                "Re-rack your weights and unload plates from bars when you finish.",
                "Wipe down benches and handles after use.",
                "Do not curl in the squat rack when it is busy.",
                "Ask \"how many sets have you got left?\" if you want to share equipment. "
                "Most people are happy to let you work in.",
                "Give people space in front of the mirror and do not walk "
                "directly in front of someone mid-set.",
                "Headphones in usually means \"busy\". Wait until they finish a set "
                "to ask a question.",
            ]},
            "And remember: almost nobody is watching you. Everyone else is "
            "thinking about their own workout.",
        ]),
        ("Soreness, rest and food", [
            "Expect some muscle soreness (DOMS) a day or two after your first "
            "sessions. It fades as you adapt and is not a measure of a good "
            "workout. Sharp or joint pain is different: stop and get it "
            "checked if it persists.",
            "Sleep seven to nine hours, and eat enough protein, roughly "
            "1.6 g per kg of bodyweight, to recover. The "
            "<a href=\"/protein-calculator\">protein calculator</a> and "
            "<a href=\"/tdee-calculator\">TDEE calculator</a> give you a "
            "starting point whether your goal is to lose fat or build muscle.",
        ]),
        ("Week by week: what the month looks like", [
            {"table": {
                "head": ["Week", "Focus", "What to do"],
                "rows": [
                    ["1", "Learn", "Light weights, 2 sets per exercise, practise every movement"],
                    ["2", "Settle", "3 sets, find a weight that leaves 3 reps in reserve"],
                    ["3", "Build", "Add a rep or a small weight jump each session"],
                    ["4", "Review", "Compare your log with week 1, then pick your next programme"],
                ]}},
            "Keep the same exercises all month. Switching every week feels "
            "fresh but stops you getting better at anything. Repetition is "
            "how a movement becomes skilful, and skill is what lets you load "
            "it safely later.",
        ]),
        ("Five beginner mistakes to skip", [
            {"list": [
                "<strong>Copying an advanced routine.</strong> A six-day "
                "bodybuilding split built for someone with ten years of training "
                "is the wrong tool for week one.",
                "<strong>Ego lifting.</strong> Adding weight before your "
                "technique is stable is the fastest route to a tweaked back or shoulder.",
                "<strong>Skipping legs.</strong> Lower body exercises train your "
                "largest muscles and make everyday life easier. Do them.",
                "<strong>Doing only cardio for fat loss.</strong> Lifting "
                "protects muscle while you diet. Do both if fat loss is your goal.",
                "<strong>Changing everything after a bad week.</strong> One "
                "low-energy session means nothing. Look at a month of data.",
            ]},
        ]),
        ("Track it", [
            "Write down every exercise, weight, set and rep. A notes app is "
            "fine. Your log tells you what to beat next time, and after a "
            "month it becomes the best motivation you have: proof you are "
            "stronger than when you started.",
            {"tip": "Set a target of 12 sessions in your first month. Hitting "
                    "that number matters more than anything you do inside them."},
        ]),
    ],
    "faq": [
        ("How many days a week should a beginner go to the gym?",
         "Two to three full-body sessions a week is ideal. It gives each muscle "
         "enough practice and enough recovery, and it is easy to sustain "
         "alongside work and family life."),
        ("Should beginners do cardio or weights first?",
         "If your main goal is strength or muscle, lift first and do cardio "
         "afterwards or on separate days. A short cardio warm-up before lifting "
         "is fine."),
        ("How long until I see results from the gym?",
         "Strength usually rises noticeably within two to four weeks as your "
         "nervous system learns the movements. Visible changes in muscle and "
         "body shape typically take eight to twelve weeks of consistent training "
         "and sensible eating."),
        ("Do I need a personal trainer as a beginner?",
         "No, but a few sessions can be worth it to learn technique on the main "
         "lifts. Otherwise, start with machines and dumbbells, film your sets, "
         "and compare them to good demonstrations."),
        ("What should I eat before my first gym session?",
         "A normal meal two to three hours before, or a light snack such as a "
         "banana or yogurt an hour before, is plenty. Avoid training on a "
         "completely empty stomach if it makes you feel light-headed."),
    ],
    "related_calcs": ["tdee-calculator", "protein-calculator",
                      "one-rep-max-calculator"],
}

G_OVERLOAD = {
    "slug": "progressive-overload-explained",
    "title": "Progressive Overload Explained: How to Keep Progressing",
    "desc": ("Progressive overload is how you get stronger and build muscle. "
             "Learn six ways to apply it, a simple double progression system, "
             "and how to beat a stall."),
    "h1": "Progressive overload explained: the principle behind every gain",
    "category": "Training",
    "image": "barbell-rack",
    "intro": ("Your body adapts to exactly the demand you place on it, then "
              "stops. Progressive overload means nudging that demand upward "
              "over time, and it is the difference between training for a year "
              "and improving for a year."),
    "body": [
        ("The principle in one paragraph", [
            "Muscles and nerves adapt to stress. Lift a weight that challenges "
            "you, recover, and next time that weight is a little easier. If you "
            "keep lifting the same weight for the same reps forever, the "
            "challenge disappears and so does the reason to adapt. Progressive "
            "overload is simply the habit of making training slightly harder "
            "over weeks and months, in a way you can recover from.",
            "It is not the same as adding weight every session forever. That "
            "works for a few months as a beginner, then it stops. Overload "
            "comes in several forms, and knowing them all is what keeps you "
            "progressing for years.",
        ]),
        ("Six ways to overload", [
            {"table": {
                "head": ["Method", "Example", "Best used when"],
                "rows": [
                    ["Add weight", "Squat 60 kg x 8 becomes 62.5 kg x 8", "Main lifts, beginners"],
                    ["Add reps", "3 x 8 becomes 3 x 10 at the same weight", "Dumbbells and machines"],
                    ["Add sets", "3 sets becomes 4 sets", "Muscle growth phases, short term"],
                    ["Improve technique", "Same load, deeper squat, controlled tempo", "Always"],
                    ["Reduce rest", "Same work in less time", "Conditioning, time-limited sessions"],
                    ["Increase frequency", "Train a muscle twice a week instead of once", "Lagging muscle groups"],
                ]}},
            "Weight and reps are the main levers. Sets are useful but should "
            "rise slowly, since adding volume without limit eventually outruns "
            "your recovery. Better technique is a quiet form of overload that "
            "many lifters overlook: a full-range rep is harder than a half rep, "
            "so cleaning up your form often makes the same weight more productive.",
        ]),
        ("Double progression: the simplest system that works", [
            "If you only learn one method, learn this. Pick a rep range, such "
            "as 8 to 12, and a weight you can lift for 8 good reps.",
            {"olist": [
                "Each session, try to add a rep or two on each set.",
                "When you hit the top of the range (12 reps) on every set, increase the weight.",
                "With the heavier weight you will drop back to around 8 reps. Repeat.",
            ]},
            {"table": {
                "head": ["Week", "Weight", "Set 1", "Set 2", "Set 3"],
                "rows": [
                    ["1", "20 kg", "10", "9", "8"],
                    ["2", "20 kg", "11", "10", "9"],
                    ["3", "20 kg", "12", "11", "10"],
                    ["4", "20 kg", "12", "12", "12"],
                    ["5", "22.5 kg", "9", "8", "8"],
                ]}},
            "Double progression works for almost every exercise and every "
            "level. It also stops you from jumping weight too early, which is "
            "how most technique breaks down.",
        ]),
        ("How fast should you progress?", [
            "It depends on your training age, and it slows down over time. "
            "That is normal, not failure.",
            {"list": [
                "<strong>Beginners (first 6-12 months):</strong> add weight to "
                "main lifts most sessions, e.g. 2.5 kg on squats and deadlifts, "
                "1-2.5 kg on presses.",
                "<strong>Intermediates:</strong> progress weekly or every couple "
                "of weeks. Programmes such as the "
                "<a href=\"/workouts/5x5-strength-program\">5x5 strength programme</a> "
                "or <a href=\"/workouts/upper-lower-split\">upper/lower split</a> "
                "build this in.",
                "<strong>Advanced lifters:</strong> progress over months, through "
                "planned cycles of volume and intensity.",
            ]},
            "Small plates help. Moving from 60 to 62.5 kg is a 4% jump; moving "
            "a 12 kg dumbbell press to 14 kg is a 17% jump. When jumps are big, "
            "lean on reps instead. The <a href=\"/plate-calculator\">plate "
            "calculator</a> helps you load exact targets quickly.",
        ]),
        ("Use effort to guide the load", [
            "A practical way to keep overload productive is reps in reserve "
            "(RIR): how many more reps you could have done. Most working sets "
            "for muscle growth should end 0 to 3 reps short of failure. If "
            "your planned sets start ending at 4-5 RIR, the weight is too light "
            "and it is time to add load.",
            "Knowing your estimated max helps too. Plug a recent hard set into "
            "the <a href=\"/one-rep-max-calculator\">one-rep max calculator</a> "
            "and track that estimate over time. It can rise even on weeks when "
            "your top weight does not.",
        ]),
        ("What to do when you stall", [
            "Every lifter plateaus. Before changing your whole programme, run "
            "through this checklist, roughly in order.",
            {"olist": [
                "<strong>Sleep and food.</strong> Are you sleeping seven hours or "
                "more and eating enough? A calorie deficit slows strength gains, "
                "especially for lean lifters.",
                "<strong>Consistency.</strong> Count your sessions over the last "
                "month. Missed workouts are the most common cause of a stall.",
                "<strong>Rep range.</strong> Switch a stuck lift from 5s to 8s, or "
                "8s to 12s, for a few weeks.",
                "<strong>Deload.</strong> Cut volume by about half for a week, then "
                "resume. Fatigue often masks strength you have already built.",
                "<strong>Variation.</strong> Swap to a close variation, such as a "
                "pause squat or incline press, for a 4-6 week block.",
            ]},
        ]),
        ("A worked example on the bench press", [
            "Here is how an early intermediate lifter might run eight weeks of "
            "bench press with linear weight jumps on a top set and double "
            "progression on back-off sets.",
            {"table": {
                "head": ["Week", "Top set", "Back-off sets", "Note"],
                "rows": [
                    ["1", "70 kg x 5", "3 x 8 at 60 kg", "Starting point"],
                    ["2", "72.5 kg x 5", "3 x 9 at 60 kg", ""],
                    ["3", "75 kg x 5", "3 x 10 at 60 kg", ""],
                    ["4", "77.5 kg x 4", "3 x 10 at 62.5 kg", "First missed rep"],
                    ["5", "77.5 kg x 5", "3 x 8 at 62.5 kg", "Repeat the weight"],
                    ["6", "80 kg x 4", "3 x 9 at 62.5 kg", ""],
                    ["7", "60 kg x 5", "2 x 8 at 50 kg", "Deload"],
                    ["8", "80 kg x 5", "3 x 10 at 62.5 kg", "New best"],
                ]}},
            "Notice what happened in week 4. The lifter missed a rep, did not "
            "panic, repeated the weight, and moved on. A planned light week "
            "in week 7 cleared fatigue, and week 8 delivered a personal best. "
            "This is what sustainable progress actually looks like: mostly "
            "upward, with small stalls built in.",
        ]),
        ("Mistakes that look like progress", [
            {"list": [
                "<strong>Shortening the range of motion</strong> to lift more. "
                "A half squat with 100 kg is not progress over a full squat with 90 kg.",
                "<strong>Adding volume every week</strong> without limit. "
                "Fatigue builds until performance drops.",
                "<strong>Chasing a new max every session.</strong> Testing your "
                "limit constantly costs recovery and rarely builds strength.",
                "<strong>Changing programmes too often.</strong> You need several "
                "weeks on the same exercises to see whether you are actually progressing.",
            ]},
        ]),
        ("Track it or it did not happen", [
            "You cannot overload what you do not record. Log the exercise, "
            "weight, sets, reps and how hard it felt. Before every session, "
            "look at what you did last time and choose one thing to beat.",
            {"tip": "Progress is not linear week to week, but it should be "
                    "obvious month to month. Compare your log to four weeks ago, "
                    "not to last Tuesday."},
        ]),
        ("Overload and muscle growth", [
            "For hypertrophy, the evidence suggests total weekly sets per "
            "muscle and effort close to failure matter a lot, across a wide "
            "range of rep counts. Progressive overload is how you keep those "
            "sets challenging as you get stronger. Our guide to "
            "<a href=\"/guides/how-many-sets-and-reps-for-muscle-growth\">sets "
            "and reps for muscle growth</a> covers the volume side in detail.",
        ]),
    ],
    "faq": [
        ("How often should I increase the weight?",
         "Beginners can often add weight to the main lifts every session. "
         "Intermediate lifters usually progress weekly or every few weeks. Use "
         "double progression: increase weight once you hit the top of your rep "
         "range on all sets."),
        ("Is it progressive overload if I add reps but not weight?",
         "Yes. More reps with the same weight is more total work and a valid "
         "form of overload. It is often the better choice for dumbbells and "
         "machines where weight jumps are large."),
        ("Can you do progressive overload with bodyweight exercises?",
         "Yes. Add reps, slow the tempo, pause at the hardest point, reduce "
         "rest, or move to a harder variation, for example from incline "
         "push-ups to regular push-ups to deficit push-ups."),
        ("What is a deload and do I need one?",
         "A deload is a planned lighter week, typically with half the volume, "
         "used to shed fatigue. Beginners rarely need them; intermediates often "
         "benefit from one every 4-8 weeks or whenever performance stalls."),
    ],
    "related_calcs": ["one-rep-max-calculator", "plate-calculator",
                      "wilks-calculator"],
}

G_BELLY = {
    "slug": "how-to-lose-belly-fat",
    "title": "How to Lose Belly Fat: What Actually Works",
    "desc": ("You can't spot-reduce belly fat, but you can lose it. An honest, "
             "evidence-based plan covering calories, training, sleep, alcohol "
             "and how to measure progress."),
    "h1": "How to lose belly fat: an honest plan that works",
    "category": "Fat Loss",
    "image": "measuring-tape",
    "intro": ("No exercise burns fat from your stomach specifically. That is "
              "the bad news. The good news is that belly fat, especially the "
              "deeper visceral kind, often responds well to overall fat loss, "
              "and the plan to get there is simple."),
    "body": [
        ("The spot reduction myth", [
            "Crunches strengthen your abdominal muscles, but they do not burn "
            "the fat on top of them. Studies that have tested this directly, "
            "such as a 2011 trial by Vispute and colleagues in the Journal of "
            "Strength and Conditioning Research, found six weeks of abdominal "
            "exercise did not reduce belly fat compared with no ab training.",
            "Your body draws fat from stores all over, in a pattern largely "
            "set by genetics, sex and hormones. Many men store fat first and "
            "lose it last around the belly; many women do the same on the hips "
            "and thighs. You cannot choose the order, but you can keep the "
            "process going long enough to reach the stubborn areas.",
        ]),
        ("Two kinds of belly fat", [
            "<strong>Subcutaneous fat</strong> sits under the skin; it is the "
            "part you can pinch. <strong>Visceral fat</strong> sits deeper, "
            "around your organs, and is the type most strongly linked to type "
            "2 diabetes, high blood pressure and heart disease.",
            "Visceral fat is metabolically active and tends to respond well "
            "to a calorie deficit and regular exercise, often falling faster "
            "in proportion than subcutaneous fat. So the health benefits of "
            "losing belly fat often start well before your stomach looks "
            "different in the mirror.",
        ]),
        ("Step 1: create a calorie deficit", [
            "This is the non-negotiable part. Work out your maintenance with "
            "the <a href=\"/tdee-calculator\">TDEE calculator</a>, then eat "
            "about 15-25% below it. Our <a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
            "calorie guide</a> walks you through setting and adjusting the number.",
            "Aim to lose 0.5-1% of bodyweight a week. Faster than that "
            "and you risk losing muscle and rebounding; slower is fine if "
            "it keeps you consistent.",
        ]),
        ("Step 2: eat in a way that makes the deficit easy", [
            {"list": [
                "<strong>Prioritise protein.</strong> About 1.6-2.2 g per kg "
                "of bodyweight. It is the most filling macronutrient and protects "
                "muscle. The <a href=\"/protein-calculator\">protein calculator</a> "
                "gives you a target.",
                "<strong>Fill half your plate with vegetables and fruit.</strong> "
                "Lots of volume, fibre and few calories.",
                "<strong>Cut liquid calories.</strong> Sugary drinks, juices and "
                "large milky coffees are an easy place to save 200-500 kcal a day.",
                "<strong>Limit ultra-processed snacks.</strong> They are easy to "
                "overeat and rarely filling.",
            ]},
            "No single food or diet style is required. Low-carb, "
            "intermittent fasting and balanced diets all produce similar fat "
            "loss when calories and protein are matched. Pick the pattern you "
            "can stick to.",
        ]),
        ("Step 3: lift weights", [
            "Strength training two to four times a week helps you keep, or "
            "even build, muscle while you lose fat. That changes your shape "
            "more than the scale suggests and stops you ending up smaller but "
            "softer.",
            "Focus on big compound lifts: <a href=\"/exercises/barbell-back-squat\">"
            "squats</a>, <a href=\"/exercises/deadlift\">deadlifts</a>, "
            "<a href=\"/exercises/bench-press\">presses</a> and "
            "<a href=\"/exercises/barbell-row\">rows</a>. Core work such as "
            "the <a href=\"/exercises/plank\">plank</a> is still worth doing "
            "for strength and posture, just not for burning fat. Our "
            "<a href=\"/workouts/fat-loss-workout-plan\">fat loss workout plan</a> "
            "combines lifting and conditioning in one schedule.",
        ]),
        ("Step 4: move more, every day", [
            "Cardio helps, and research suggests aerobic exercise is "
            "particularly effective at reducing visceral fat. But for most "
            "people, the bigger lever is everyday movement: walking, taking "
            "stairs, standing more. Going from 4,000 to 9,000 steps a day can "
            "burn an extra 200-300 kcal without adding much hunger.",
            "Both steady cardio and intervals work. Our "
            "<a href=\"/guides/cardio-for-fat-loss-hiit-vs-liss\">HIIT vs LISS "
            "guide</a> explains how to choose.",
        ]),
        ("Step 5: sleep, stress and alcohol", [
            "Short sleep is consistently associated with higher waist size "
            "and makes dieting harder by increasing hunger and cravings. Aim "
            "for seven to nine hours.",
            "Chronic stress and alcohol both make abdominal fat gain more "
            "likely and fat loss harder. Alcohol also adds calories that are "
            "easy to forget: two pints of beer or two large glasses of wine "
            "can be 400-500 kcal. If you drink, cutting back is one of the "
            "highest-return changes you can make.",
        ]),
        ("A sample week", [
            "Putting it together, a realistic week for someone working a desk "
            "job might look like this.",
            {"table": {
                "head": ["Day", "Training", "Daily target"],
                "rows": [
                    ["Mon", "Full-body strength, 45-60 min", "8,000+ steps"],
                    ["Tue", "30 min brisk walk or easy cycle", "8,000+ steps"],
                    ["Wed", "Full-body strength", "8,000+ steps"],
                    ["Thu", "20 min intervals or a sport", "8,000+ steps"],
                    ["Fri", "Full-body strength", "8,000+ steps"],
                    ["Sat", "Long walk, hike or active hobby", "10,000+ steps"],
                    ["Sun", "Rest", "Easy movement"],
                ]}},
            "Every day: protein at each meal, vegetables at two meals or more, "
            "a calorie target you actually track, and a consistent bedtime. "
            "None of it is exotic. The results come from repeating it for "
            "months, not from any single clever trick.",
        ]),
        ("Things that do not work", [
            {"list": [
                "<strong>Waist trainers and sweat belts.</strong> They make you "
                "sweat and compress tissue temporarily. No fat is lost.",
                "<strong>Fat-burner supplements.</strong> Most rely on caffeine "
                "and produce, at best, a tiny increase in energy use.",
                "<strong>Detox teas and cleanses.</strong> Weight lost is "
                "water and gut contents, and it returns within days.",
                "<strong>Hundreds of crunches a day.</strong> Good for endurance, "
                "useless for fat loss on their own.",
            ]},
        ]),
        ("How to measure progress", [
            "The scale is useful but blunt. Track your waist too.",
            {"olist": [
                "Measure at the level of your belly button, standing relaxed, after breathing out.",
                "Measure on the same morning each week, before eating.",
                "Take photos every four weeks in the same light and pose.",
            ]},
            {"table": {
                "head": ["Measure", "Healthy target", "Tool"],
                "rows": [
                    ["Waist-to-height ratio", "Below 0.5", "Tape measure"],
                    ["Waist-to-hip ratio", "Below 0.90 men, 0.85 women",
                     "<a href=\"/waist-to-hip-ratio-calculator\">WHR calculator</a>"],
                    ["Body fat percentage", "Trending down",
                     "<a href=\"/body-fat-calculator\">Body fat calculator</a>"],
                ]}},
            {"tip": "A waist that drops 1 cm a fortnight is excellent progress, "
                    "even if the scale barely moves because you are building muscle."},
            "How long will it take? It depends on how much there is to lose. As a rough guide, losing "
            "5-10% of bodyweight over three to six months produces noticeable "
            "changes in waist size for most people. The last layer of lower "
            "belly fat is usually the slowest to go, which is exactly why "
            "patience and consistency beat any quick fix.",
            "Expect plateaus along the way. Two or three weeks without change "
            "on the scale or tape is normal, especially for women around the "
            "menstrual cycle, when water retention can mask fat loss. Judge "
            "your progress over months and recalculate your calories every "
            "4-5 kg (10 lb) lost, because your maintenance falls as you get lighter.",
        ]),
    ],
    "faq": [
        ("Can I lose belly fat in a week?",
         "Not meaningfully. You might lose some water and bloating, which can "
         "make your stomach look flatter, but real fat loss takes weeks to months "
         "of a consistent calorie deficit."),
        ("Do ab exercises burn belly fat?",
         "No. Ab exercises strengthen the muscles underneath, which helps posture "
         "and performance, but they do not burn the fat on top. Fat loss comes "
         "from an overall calorie deficit."),
        ("Why is belly fat the last to go?",
         "Fat storage and loss patterns are largely set by genetics and hormones. "
         "For many people, especially men, the abdomen is where fat goes first and "
         "leaves last. Keep going and it does come off."),
        ("Is belly fat more dangerous than other fat?",
         "Visceral fat, the deeper fat around your organs, is linked to higher "
         "risk of type 2 diabetes and heart disease. A large waist is a useful "
         "warning sign worth discussing with a doctor."),
    ],
    "related_calcs": ["tdee-calculator", "waist-to-hip-ratio-calculator",
                      "body-fat-calculator", "calorie-calculator"],
}

G_BULK_CUT = {
    "slug": "bulking-vs-cutting",
    "title": "Bulking vs Cutting: Which Should You Do First?",
    "desc": ("Should you bulk or cut? Use your body fat, training age and "
             "goals to decide, then set the right calorie surplus or deficit "
             "and rate of change."),
    "h1": "Bulking vs cutting: how to decide which comes first",
    "category": "Muscle Building",
    "image": "meal-prep",
    "intro": ("Bulking means eating more to build muscle; cutting means eating "
              "less to lose fat. Most lifters spend years switching between "
              "them. Choosing the right phase, and running it at the right "
              "speed, saves a lot of wasted months."),
    "body": [
        ("The definitions", [
            "<strong>A bulk</strong> is a planned period in a calorie surplus "
            "with hard training, designed to maximise muscle gain. Some fat "
            "gain comes with it; the goal is to keep that small.",
            "<strong>A cut</strong> is a planned period in a calorie deficit, "
            "designed to lose fat while keeping as much muscle as possible.",
            "<strong>Maintenance</strong> and <strong>recomposition</strong> "
            "sit between the two. Eating around maintenance while training "
            "hard can slowly build muscle and lose fat at the same time, "
            "particularly for beginners. See our "
            "<a href=\"/guides/body-recomposition-guide\">body recomposition guide</a>.",
        ]),
        ("A simple decision rule", [
            {"table": {
                "head": ["Your situation", "Men (body fat)", "Women (body fat)", "Start with"],
                "rows": [
                    ["Higher body fat", "Above ~20%", "Above ~30%", "Cut"],
                    ["Moderate", "~13-20%", "~23-30%", "Recomp or your preference"],
                    ["Lean", "Below ~13%", "Below ~23%", "Lean bulk"],
                ]}},
            "These are practical rules of thumb, not hard thresholds. Not sure "
            "where you are? Estimate it with the <a href=\"/body-fat-calculator\">"
            "body fat calculator</a>.",
            "Beyond body fat, ask yourself what would make you happiest in six "
            "months. If carrying more fat would make you miserable or less "
            "consistent, cutting first is the right call even at moderate body "
            "fat. Adherence beats optimisation.",
        ]),
        ("Why lean bulks beat dirty bulks", [
            "Muscle can only be built so fast. Eating far beyond what you need "
            "does not speed it up much; it just adds fat that you later have to "
            "diet off. Studies comparing larger and smaller surpluses in trained "
            "lifters have generally found that the bigger surplus mainly adds "
            "more fat, with little or no extra muscle to show for it.",
            "That is why most coaches now favour a lean bulk: a small surplus "
            "and a slow, steady rate of gain.",
        ]),
        ("How to set up a bulk", [
            {"olist": [
                "Find maintenance with the <a href=\"/tdee-calculator\">TDEE calculator</a>.",
                "Add a surplus of about 5-10%, roughly 150-300 kcal per day for most people.",
                "Set protein at 1.6-2.2 g/kg, fat at 20-35% of calories, carbs for the rest. "
                "The <a href=\"/macro-calculator\">macro calculator</a> does this for you.",
                "Weigh daily, compare weekly averages, and adjust by 100-150 kcal if you "
                "are outside your target rate.",
            ]},
            {"table": {
                "head": ["Training age", "Target gain per month", "Example (75 kg lifter)"],
                "rows": [
                    ["Beginner (year 1)", "1-1.5% of bodyweight", "0.75-1.1 kg (1.7-2.5 lb)"],
                    ["Intermediate", "0.5-1%", "0.4-0.75 kg (0.8-1.7 lb)"],
                    ["Advanced", "0.25-0.5%", "0.2-0.4 kg (0.4-0.8 lb)"],
                ]}},
            "Train with a programme that drives "
            "<a href=\"/guides/progressive-overload-explained\">progressive "
            "overload</a>, such as <a href=\"/workouts/push-pull-legs\">push "
            "pull legs</a> or an <a href=\"/workouts/upper-lower-split\">"
            "upper/lower split</a>. A surplus without hard training simply "
            "makes you fatter.",
        ]),
        ("How to set up a cut", [
            {"olist": [
                "Start from your maintenance and subtract 15-25%.",
                "Raise protein toward the top of the range, around 2.0-2.2 g/kg.",
                "Keep lifting heavy. Your training is the signal that tells your body "
                "to keep its muscle; do not switch to light, high-rep \"toning\" work.",
                "Aim to lose 0.5-1% of bodyweight per week.",
            ]},
            "Our <a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
            "calorie guide</a> covers adjusting the deficit as you go, and the "
            "<a href=\"/weight-loss-calculator\">weight loss calculator</a> will "
            "estimate how long the cut will take.",
        ]),
        ("How long should each phase last?", [
            "Bulks tend to work best when they are long, often four to six "
            "months or more, because muscle gain is slow and you want enough "
            "time for it to accumulate. Cuts are often shorter, typically 8 to "
            "16 weeks, because longer deficits get harder to sustain and "
            "start to bite into training quality.",
            "End a bulk when your body fat climbs to a level you are no longer "
            "comfortable with, or when your waist has grown noticeably faster "
            "than your strength. End a cut when you reach your goal or when "
            "you have been dieting long enough that a break at maintenance "
            "would help.",
            "A useful sanity check is the ratio of time spent bulking to "
            "cutting. If you find yourself cutting for longer than you bulked, "
            "the surplus was probably too large. Over a year, most successful "
            "lifters spend more time building or maintaining than dieting.",
        ]),
        ("The transition matters", [
            "After a cut, raise calories back to maintenance over a week or "
            "two and hold there for a few weeks before starting a surplus. "
            "Expect the scale to rise 1-2 kg as food volume, water and "
            "glycogen return. That is not fat.",
            "After a bulk, there is no need for a dramatic drop. Reduce "
            "calories to your new deficit target and keep training the same way.",
            "One more point: your maintenance changes during each phase. "
            "After a bulk you are heavier, so your maintenance is higher than "
            "when you started; after a cut it is lower. Recalculate with the "
            "<a href=\"/tdee-calculator\">TDEE calculator</a> at every "
            "transition, then confirm the new number with two weeks of scale "
            "data before you commit to it.",
        ]),
        ("A year planned out", [
            "Here is how a lean-ish intermediate lifter at around 15% body "
            "fat might arrange a year. The exact lengths are flexible; the "
            "pattern is what matters.",
            {"table": {
                "head": ["Months", "Phase", "Calories", "Expected result"],
                "rows": [
                    ["1-5", "Lean bulk", "+5-10%", "+2-3.5 kg, mostly muscle with some fat"],
                    ["6", "Maintenance", "Maintenance", "Weight stabilises, recovery improves"],
                    ["7-9", "Cut", "-20%", "-4-5 kg, body fat back near starting point"],
                    ["10", "Maintenance", "Maintenance", "Diet break, rebuild training"],
                    ["11-12", "Start next bulk", "+5-10%", "Gains resume from a leaner base"],
                ]}},
            "The net result over a year is a modest, real gain in muscle at a "
            "similar body fat level. That might not sound dramatic, but repeated "
            "over three or four years it transforms a physique, which is "
            "exactly why patience beats extreme surpluses and crash diets.",
        ]),
        ("Food choices for each phase", [
            "During a bulk, the challenge for many people is simply eating "
            "enough. Calorie-dense but nutritious foods help: oats, rice, "
            "whole milk, nuts, nut butters, olive oil, dried fruit and larger "
            "portions of your usual meals. A homemade shake of milk, oats, "
            "banana and peanut butter can easily add 600-700 kcal.",
            "During a cut, the challenge flips to managing hunger. Lean "
            "proteins, vegetables, potatoes, fruit, soups and high-fibre foods "
            "deliver plenty of volume for few calories. Keeping a couple of "
            "favourite treats in planned portions often helps you stay on track "
            "more than banning them outright.",
        ]),
        ("Signs your phase is going wrong", [
            {"list": [
                "<strong>Bulk:</strong> your waist grows more than about 1 cm for "
                "every kilogram you gain, or your lifts are not improving.",
                "<strong>Cut:</strong> strength is dropping quickly on most lifts, "
                "or you are losing more than 1% of bodyweight per week consistently.",
                "<strong>Both:</strong> sleep, mood or recovery are tanking. "
                "Pull calories back toward maintenance for a week.",
            ]},
            {"tip": "Track three things through any phase: weekly average "
                    "bodyweight, waist measurement and your main lifts. Together "
                    "they tell you whether you are gaining muscle or just weight."},
        ]),
    ],
    "faq": [
        ("Should a skinny-fat beginner bulk or cut?",
         "Usually neither. A beginner with low muscle and moderate body fat "
         "tends to do best with recomposition: eating around maintenance with "
         "high protein and progressive strength training for the first few months."),
        ("How big should a calorie surplus be for bulking?",
         "For most lifters, about 5-10% above maintenance, roughly 150-300 kcal "
         "per day. Beginners can use the upper end; advanced lifters the lower end."),
        ("Will I lose muscle when cutting?",
         "Not if you keep protein high, keep lifting heavy and avoid very "
         "aggressive deficits. Many lifters maintain or even slightly gain "
         "strength in a moderate cut."),
        ("How long should I bulk before cutting?",
         "Typically four to six months or longer. Short bulks do not give muscle "
         "gain enough time to add up, which leads to endless cycling with little "
         "progress."),
    ],
    "related_calcs": ["tdee-calculator", "calorie-calculator",
                      "macro-calculator", "body-fat-calculator"],
}

G_RECOMP = {
    "slug": "body-recomposition-guide",
    "title": "Body Recomposition: Lose Fat and Build Muscle",
    "desc": ("Body recomposition means losing fat and gaining muscle at the "
             "same time. Who it works for, how to set calories and protein, "
             "how to train, and how to track it."),
    "h1": "Body recomposition: how to lose fat and build muscle at once",
    "category": "Muscle Building",
    "image": "woman-lifting",
    "intro": ("The old rule said you had to bulk to build muscle and cut to "
              "lose fat. For many people, that is not true. With the right "
              "setup you can do both at once, as long as you know who "
              "recomposition suits and how slowly it shows on the scale."),
    "body": [
        ("What recomposition is", [
            "Body recomposition, or recomp, is gaining muscle and losing fat "
            "over the same period. Because the two changes partly cancel out "
            "on the scale, your weight may barely move while your waist "
            "shrinks, your clothes fit differently and your lifts go up.",
            "It works because your body does not run a single energy budget "
            "for every tissue. With enough protein and a strong training "
            "signal, muscle can be built from incoming nutrients while stored "
            "fat covers part of the energy gap. A 2020 review by Barakat and "
            "colleagues in Strength and Conditioning Journal concluded that "
            "recomposition is well supported in the research, including in "
            "trained lifters.",
            "The catch is speed. Because your body is splitting its resources "
            "between two goals, each happens more slowly than it would in a "
            "dedicated phase. That makes recomp a great default for people who "
            "want steady, sustainable progress without the extremes of bulking "
            "and cutting, and a weaker choice for someone with a deadline.",
        ]),
        ("Who it works best for", [
            {"table": {
                "head": ["Profile", "How well recomp works"],
                "rows": [
                    ["Complete beginners", "Very well"],
                    ["Returning after a long break", "Very well (muscle memory)"],
                    ["Moderate to higher body fat", "Well"],
                    ["Intermediate lifters with sloppy training or diet", "Well, once those are fixed"],
                    ["Lean, advanced lifters", "Slowly; dedicated bulks and cuts are usually faster"],
                ]}},
            "If you are a beginner who is neither very lean nor carrying a lot "
            "of fat, the \"skinny-fat\" position many people start from, "
            "recomp is often the best first move. Our "
            "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting guide</a> "
            "helps if you are unsure which camp you are in.",
        ]),
        ("Set calories: maintenance or a small deficit", [
            "Find your maintenance with the <a href=\"/tdee-calculator\">TDEE "
            "calculator</a>. Then choose:",
            {"list": [
                "<strong>Maintenance</strong> if you are fairly lean and want to "
                "prioritise muscle.",
                "<strong>A small deficit, 10-20% below maintenance,</strong> if you "
                "have more fat to lose. This is the most common recomp setup.",
            ]},
            "Avoid big deficits. A deficit above about 25% makes it hard to "
            "build muscle, and you are back to a plain cut.",
        ]),
        ("Set protein high", [
            "Protein is the engine of recomposition. Aim for 1.8-2.2 g per kg "
            "of bodyweight, or about 2.0-2.4 g per kg of lean body mass if you "
            "carry more fat. Spread it across three to five meals.",
            "Use the <a href=\"/protein-calculator\">protein calculator</a> for "
            "your target, and see the <a href=\"/guides/how-much-protein-to-build-muscle\">"
            "protein guide</a> for food ideas.",
        ]),
        ("Train for muscle, with progression", [
            "Recomposition only happens if your training gives your body a "
            "reason to build muscle. That means lifting weights three to five "
            "times a week, with most sets taken close to failure and a clear "
            "plan to add reps or weight over time.",
            {"list": [
                "Train each muscle group at least twice a week.",
                "Aim for roughly 10-20 hard sets per muscle per week.",
                "Base sessions on compound lifts such as the "
                "<a href=\"/exercises/barbell-back-squat\">squat</a>, "
                "<a href=\"/exercises/romanian-deadlift\">Romanian deadlift</a>, "
                "<a href=\"/exercises/bench-press\">bench press</a> and "
                "<a href=\"/exercises/pull-up\">pull-up</a>.",
                "Keep cardio moderate. Walking is ideal; it adds to the deficit "
                "without eating into recovery.",
            ]},
            "Good starting programmes include the <a href=\"/workouts/upper-lower-split\">"
            "upper/lower split</a> and the <a href=\"/workouts/beginner-full-body-workout\">"
            "beginner full-body workout</a>.",
        ]),
        ("A sample recomp day", [
            "For a 70 kg lifter at maintenance of 2,300 kcal, a 15% deficit "
            "gives a target of about 1,950 kcal, with 140-150 g of protein.",
            {"table": {
                "head": ["Meal", "Example", "Protein", "Calories"],
                "rows": [
                    ["Breakfast", "Overnight oats with whey, berries", "35 g", "420"],
                    ["Lunch", "Chicken or tofu rice bowl with vegetables", "40 g", "550"],
                    ["Pre-workout", "Greek yogurt and a banana", "20 g", "250"],
                    ["Dinner", "Fish or lentil curry, roti, salad", "40 g", "600"],
                    ["Evening", "Glass of milk", "10 g", "130"],
                    ["Total", "", "about 145 g", "about 1,950"],
                ]}},
            "On training days, place more of your carbohydrates around your "
            "session. On rest days you can keep the same totals; the weekly "
            "average is what counts.",
        ]),
        ("Common recomp mistakes", [
            {"list": [
                "<strong>Eating too little.</strong> A big deficit turns a recomp "
                "into a cut, and muscle gain stops.",
                "<strong>Not training hard enough.</strong> Comfortable sets with "
                "five reps left in the tank do not give muscle a reason to grow.",
                "<strong>Judging by the scale.</strong> A flat scale is expected. "
                "Use the waist, photos and strength.",
                "<strong>Impatience.</strong> Recomposition is slow. Most people who "
                "quit after four weeks were making progress they could not yet see.",
            ]},
        ]),
        ("Sleep is part of the plan", [
            "Recomposition is a fine balance, and poor sleep tips it the "
            "wrong way. In a 2010 study by Nedeltcheva and colleagues in the "
            "Annals of Internal Medicine, dieters who slept 5.5 hours instead "
            "of 8.5 lost a much smaller share of their weight as fat and more "
            "as lean mass. Seven to nine hours is part of the programme, not "
            "an extra.",
        ]),
        ("How to track a recomp", [
            "Because the scale can stay flat, you need better measures.",
            {"table": {
                "head": ["Measure", "How often", "What you want to see"],
                "rows": [
                    ["Bodyweight (weekly average)", "Daily weigh-in", "Flat or slowly falling"],
                    ["Waist", "Weekly", "Slowly falling"],
                    ["Main lifts", "Every session", "Rising"],
                    ["Photos", "Every 4 weeks", "Visible change in shape"],
                    ["Body fat %", "Monthly", "Falling"],
                ]}},
            "The <a href=\"/body-fat-calculator\">body fat calculator</a> and "
            "<a href=\"/ffmi-calculator\">FFMI calculator</a> are useful "
            "monthly checks: if body fat falls while FFMI rises, you are "
            "recomposing.",
            {"tip": "If the scale is flat, your waist is unchanged and your lifts "
                    "have stalled for a month, you are not recomposing, you are "
                    "maintaining. Drop calories by 10% or tighten your training."},
        ]),
        ("How long does it take?", [
            "Recomposition is slower than a dedicated cut for fat loss and "
            "slower than a bulk for muscle gain, but it makes steady progress "
            "on both. Beginners often see clear changes in 8-12 weeks. Give it "
            "at least three months before judging, and expect it to slow as "
            "you get leaner and more experienced. At that point, switching to "
            "dedicated bulk and cut phases usually makes sense.",
            "A rough guide for a beginner over 12 weeks: a waist reduction "
            "of 3-6 cm, a body fat drop of 2-4 percentage points, clear "
            "strength gains on the main lifts, and a bodyweight change of "
            "anywhere from a few kilograms down to roughly flat. People returning "
            "after a break often see faster changes thanks to muscle memory. "
            "Individual results vary widely, so compare yourself only with your "
            "own starting point.",
        ]),
    ],
    "faq": [
        ("Can you build muscle in a calorie deficit?",
         "Yes, especially if you are a beginner, returning after a break or "
         "carrying higher body fat. High protein, hard training and a moderate "
         "deficit make it possible."),
        ("Why is my weight not changing during a recomp?",
         "Because fat loss and muscle gain can roughly cancel out on the scale. "
         "Track your waist, photos and strength instead; if those are improving, "
         "the recomp is working."),
        ("How much protein do I need for body recomposition?",
         "About 1.8-2.2 g per kg of bodyweight per day, spread across three to "
         "five meals. If you have a lot of body fat, base it on goal weight or "
         "lean mass."),
        ("Is recomp good for women?",
         "Yes. The principles are the same for everyone: enough protein, a "
         "small deficit or maintenance calories, and progressive strength training."),
    ],
    "related_calcs": ["tdee-calculator", "protein-calculator",
                      "body-fat-calculator", "ffmi-calculator"],
}

GUIDES = [G_CALORIES, G_PROTEIN, G_BMI_BF, G_BEGINNER, G_OVERLOAD,
          G_BELLY, G_BULK_CUT, G_RECOMP]
