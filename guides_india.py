"""
Standalone guides, India edition.

Six guides written for Indian readers: Indian foods, kg and cm, and the
Asian BMI cut-offs. Same content spec as guides_a.py: body is a list of
(heading, blocks) tuples, faq is a list of (question, answer) tuples.

Food values are rounded from the Indian Food Composition Tables (NIN, 2017)
and USDA FoodData Central. Home recipes vary, so treat them as estimates.
"""

G_BMI_CHART = {
    "slug": "bmi-chart-for-indians",
    "title": "BMI Chart for Indians: Healthy Weight by Height",
    "desc": ("Healthy weight for your height on the Indian BMI cut-offs "
             "(18.5-22.9), in kg and feet, for men and women, with the "
             "waist limits doctors in India use."),
    "h1": "BMI chart for Indians: healthy weight for your height",
    "category": "Health & Recovery",
    "image": "scale",
    "intro": ("Most BMI charts online use the international cut-offs, where "
              "healthy runs up to 24.9. Indian guidelines draw the line "
              "lower, at 22.9. Here is what that means in kilograms for "
              "your height."),
    "body": [
        ("Why Indians use a different BMI chart", [
            "BMI is weight in kilograms divided by height in metres squared. "
            "The formula is the same everywhere. What changes is where the "
            "categories start.",
            "At the same BMI, South Asian adults tend to carry more body "
            "fat, and more of it around the stomach, than white Europeans. "
            "That is why type 2 diabetes and high blood pressure appear at "
            "lower weights in India. A 2004 WHO expert consultation "
            "recognised this, and India's 2009 consensus guidelines (Misra "
            "et al.) set lower cut-offs for Indian adults.",
            {"table": {"head": ["BMI", "Category for Indian adults"],
                       "rows": [["Below 18.5", "Underweight"],
                                ["18.5 - 22.9", "Normal"],
                                ["23.0 - 24.9", "Overweight"],
                                ["25.0 and above", "Obese"]]}},
            "So a BMI of 24, which an international chart calls healthy, "
            "already counts as overweight for an Indian adult.",
        ]),
        ("Healthy weight chart by height", [
            "The normal range below is BMI 18.5 to 22.9. The same chart "
            "applies to men and women: BMI does not change with sex, "
            "although women naturally carry more body fat at any given BMI.",
            {"table": {"head": ["Height", "Normal weight", "Overweight from",
                                "Obese from"],
                       "rows": [["150 cm (4 ft 11 in)", "41.6 - 51.5 kg", "51.8 kg", "56.2 kg"],
                                ["155 cm (5 ft 1 in)", "44.4 - 55.0 kg", "55.3 kg", "60.1 kg"],
                                ["160 cm (5 ft 3 in)", "47.4 - 58.6 kg", "58.9 kg", "64.0 kg"],
                                ["165 cm (5 ft 5 in)", "50.4 - 62.3 kg", "62.6 kg", "68.1 kg"],
                                ["170 cm (5 ft 7 in)", "53.5 - 66.2 kg", "66.5 kg", "72.2 kg"],
                                ["175 cm (5 ft 9 in)", "56.7 - 70.1 kg", "70.4 kg", "76.6 kg"],
                                ["180 cm (5 ft 11 in)", "59.9 - 74.2 kg", "74.5 kg", "81.0 kg"],
                                ["185 cm (6 ft 1 in)", "63.3 - 78.4 kg", "78.7 kg", "85.6 kg"]]}},
            "For your exact height, use the <a href=\"/bmi-calculator\">BMI "
            "calculator</a> and choose <strong>Asian / Indian</strong> "
            "cut-offs. It shows your category on both the Indian and the "
            "international scale, and your healthy weight range.",
        ]),
        ("Check your waist too", [
            "Two people with the same BMI can carry very different amounts "
            "of belly fat, and belly fat is the riskier kind. Indian "
            "guidelines use lower waist limits than Western ones:",
            {"table": {"head": ["", "Waist limit (India)", "Common Western limit"],
                       "rows": [["Men", "90 cm (35.4 in)", "94-102 cm"],
                                ["Women", "80 cm (31.5 in)", "80-88 cm"]]}},
            "Measure around your bare stomach at the level of the navel, "
            "after breathing out normally. If your BMI is normal but your "
            "waist is over the limit, the waist is the number to act on. The "
            "<a href=\"/waist-to-hip-ratio-calculator\">waist-to-hip ratio "
            "calculator</a> gives a second view.",
        ]),
        ("When the chart is wrong for you", [
            "BMI cannot tell muscle from fat. If you have lifted weights "
            "seriously for a year or more, you may sit in the overweight "
            "band while being lean. A <a href=\"/body-fat-calculator\">body "
            "fat estimate</a> or your <a href=\"/ffmi-calculator\">FFMI</a> "
            "tells you more.",
            "The chart is also not meant for children and teenagers, who "
            "are measured against growth charts for their age, or for "
            "pregnancy.",
            {"tip": "If you are above the normal range, you do not need to "
                    "reach the bottom of the chart. Losing 5 to 10 percent "
                    "of your body weight already improves blood sugar and "
                    "blood pressure noticeably."},
        ]),
    ],
    "faq": [
        ("What is the ideal weight for a 5 ft 5 in Indian woman?",
         "At 165 cm, the normal range on Indian cut-offs is about 50 to 62 "
         "kg. Within that range, a weight you can hold comfortably while "
         "eating well and training is a better target than one exact number."),
        ("What is the ideal weight for a 5 ft 9 in Indian man?",
         "At 175 cm, the normal range on Indian cut-offs is about 57 to 70 "
         "kg. A man who lifts regularly may sit a few kilograms above that "
         "while still being lean."),
        ("Is a BMI of 24 overweight for Indians?",
         "Yes. Under India's guidelines, 23 to 24.9 counts as overweight. "
         "On the international WHO chart, 24 is still in the healthy range."),
        ("Is the BMI chart different for men and women?",
         "No, the same cut-offs apply to both. Women carry more body fat "
         "than men at the same BMI, which is why waist limits are set "
         "separately for each."),
    ],
    "related_calcs": ["bmi-calculator", "ideal-weight-calculator",
                      "waist-to-hip-ratio-calculator", "body-fat-calculator"],
}

G_VEG_PROTEIN = {
    "slug": "high-protein-indian-vegetarian-foods",
    "title": "High-Protein Indian Vegetarian Foods for the Gym",
    "desc": ("How much protein paneer, dal, soya, curd and chana really give "
             "you, how much a vegetarian lifter needs, and a full day that "
             "hits 100 g without supplements."),
    "h1": "High-protein Indian vegetarian foods, and how to eat enough",
    "category": "Nutrition",
    "image": "protein-food",
    "intro": ("A typical Indian vegetarian plate is built on roti, rice and "
              "a katori of dal, which adds up to far less protein than most "
              "people think. Here is how much the common foods actually give "
              "you, and how to build a day that is enough for the gym."),
    "body": [
        ("How much protein do you need?", [
            "The ICMR-NIN recommended allowance for Indian adults is 0.83 g "
            "of protein per kg of body weight a day. That is the minimum to "
            "stay healthy, not the amount that builds muscle best.",
            "For people who lift weights, a 2018 meta-analysis (Morton et "
            "al., British Journal of Sports Medicine) found muscle gain "
            "levelled off at about <strong>1.6 g per kg</strong> a day, with "
            "some people benefiting from up to 2.2 g.",
            {"table": {"head": ["Body weight", "Minimum (0.83 g/kg)",
                                "Lifting (1.6 g/kg)"],
                       "rows": [["50 kg", "42 g", "80 g"],
                                ["60 kg", "50 g", "96 g"],
                                ["70 kg", "58 g", "112 g"],
                                ["80 kg", "66 g", "128 g"]]}},
            "Your own number is one click away in the <a "
            "href=\"/protein-calculator\">protein calculator</a>.",
        ]),
        ("Protein in common vegetarian foods", [
            "Values are approximate. Dal and rajma are given cooked, per "
            "katori made from about 30 g of dry dal, because that is how "
            "they are eaten.",
            {"table": {"head": ["Food", "Serving", "Protein", "Calories"],
                       "rows": [["Soya chunks (dry)", "50 g", "26 g", "175 kcal"],
                                ["Paneer (full fat)", "100 g", "18 g", "265 kcal"],
                                ["Tofu (firm)", "100 g", "12-15 g", "120-145 kcal"],
                                ["Hung curd / Greek yogurt", "150 g", "12-15 g", "130-150 kcal"],
                                ["Whey protein", "1 scoop (30 g)", "24 g", "120 kcal"],
                                ["Milk (toned)", "250 ml", "8 g", "145 kcal"],
                                ["Dal, rajma or chole (cooked)", "1 katori", "7 g", "120-160 kcal"],
                                ["Besan", "50 g", "11 g", "195 kcal"],
                                ["Roasted chana", "30 g", "6 g", "110 kcal"],
                                ["Peanuts", "30 g", "7.5 g", "170 kcal"],
                                ["Sattu", "40 g", "8 g", "160 kcal"],
                                ["Curd (dahi)", "1 katori (150 g)", "5 g", "90 kcal"],
                                ["Roti (medium)", "1", "3 g", "110 kcal"],
                                ["Cooked rice", "1 cup (150 g)", "4 g", "195 kcal"]]}},
            "Two things stand out. Soya chunks, paneer, hung curd and tofu "
            "carry most of the load. Dal is a good food, but one katori "
            "gives about 7 g: you would need more than ten katoris to reach "
            "80 g from dal alone.",
        ]),
        ("A 100 g vegetarian day, without supplements", [
            "This day is roughly 1,900 kcal, which suits a lightly active "
            "60 to 70 kg person. Scale the portions up or down with the <a "
            "href=\"/calorie-calculator\">calorie calculator</a>.",
            {"table": {"head": ["Meal", "What to eat", "Protein"],
                       "rows": [["Breakfast", "2 besan chillas (60 g besan) with 150 g hung curd", "26 g"],
                                ["Lunch", "2 roti, 1 katori rajma, soya chunk sabzi (30 g dry), salad", "28 g"],
                                ["Snack", "30 g roasted chana, 1 glass toned milk", "14 g"],
                                ["Dinner", "100 g paneer bhurji, 1 roti, 1 katori dal", "28 g"],
                                ["Total", "", "about 96-100 g"]]}},
            "Add a scoop of whey or another 50 g of soya and you are "
            "comfortably at 120 g, enough for a 75 kg lifter.",
        ]),
        ("Tips that make it easier", [
            {"list": [
                "Put a protein food in every meal, not just at dinner. Three "
                "or four servings of 25 to 30 g work better than one big one.",
                "Swap regular curd for hung curd. Straining it overnight "
                "roughly doubles the protein per spoon.",
                "Use soya chunks in pulao, sabzi or keema-style dishes. 50 g "
                "dry gives as much protein as 140 g of paneer, for fewer "
                "calories.",
                "Watch the paneer calories. It is high in fat, so on a fat "
                "loss diet, low-fat paneer or tofu goes further.",
                "Mix dal with rice or roti. Grains and pulses together give "
                "a complete set of amino acids.",
            ]},
            {"tip": "If you eat eggs, two eggs add about 12 g of protein for "
                    "140 kcal, one of the cheapest ways to close the gap."},
        ]),
    ],
    "faq": [
        ("Can vegetarians build muscle without eggs or meat?",
         "Yes. Muscle growth depends on total protein, training and "
         "calories, not on where the protein comes from. Vegetarians just "
         "have to plan more, leaning on soya, paneer, hung curd, tofu and, "
         "if they like, whey."),
        ("Which Indian vegetarian food has the most protein?",
         "Dry soya chunks, at about 52 g per 100 g. Among everyday foods, "
         "paneer, tofu, hung curd and besan are the next best."),
        ("Is soya safe for men?",
         "Yes, in normal food amounts. Studies have not found that eating "
         "soya foods lowers testosterone in men. One or two servings a day "
         "is a sensible amount."),
        ("Do I need whey protein as a vegetarian?",
         "No, but it helps. One scoop gives about 24 g of protein for very "
         "few calories, which makes a high target much easier to reach on a "
         "budget or a busy day."),
    ],
    "related_calcs": ["protein-calculator", "macro-calculator",
                      "calorie-calculator"],
}

G_WEIGHT_LOSS = {
    "slug": "indian-diet-plan-for-weight-loss",
    "title": "Indian Diet Plan for Weight Loss (Veg, 1,500 kcal)",
    "desc": ("A simple Indian diet plan for weight loss built on a calorie "
             "deficit: how many calories to eat, a full 1,500 kcal veg day "
             "and the hidden calories in Indian cooking."),
    "h1": "Indian diet plan for weight loss that you can actually follow",
    "category": "Fat Loss",
    "image": "healthy-meal",
    "intro": ("You do not need to give up roti, rice or dal to lose weight. "
              "You need to eat a little less energy than you burn, every "
              "day, for months. This plan shows you how to do that with "
              "normal Indian food."),
    "body": [
        ("Step 1: find your calorie target", [
            "Weight loss comes from a calorie deficit. Start with your "
            "maintenance calories from the <a href=\"/tdee-calculator\">TDEE "
            "calculator</a>, then eat 15 to 25 percent less. For most "
            "people that means losing about 0.5 kg a week.",
            {"table": {"head": ["Maintenance", "Weight loss target"],
                       "rows": [["1,800 kcal", "1,350 - 1,550 kcal"],
                                ["2,000 kcal", "1,500 - 1,700 kcal"],
                                ["2,200 kcal", "1,650 - 1,850 kcal"],
                                ["2,500 kcal", "1,900 - 2,100 kcal"]]}},
            "Do not go below about 1,200 kcal (women) or 1,500 kcal (men) "
            "without medical advice. Very low intakes make you lose muscle "
            "and are hard to stick to.",
        ]),
        ("Step 2: watch the hidden calories", [
            "Indian home food is not usually the problem. The problem is "
            "the oil and ghee that go into it, and the snacks around it.",
            {"table": {"head": ["Item", "Calories"],
                       "rows": [["1 teaspoon oil or ghee", "45 kcal"],
                                ["1 tablespoon oil (a normal tadka)", "120 kcal"],
                                ["1 samosa", "250 - 300 kcal"],
                                ["1 plate chole bhature", "about 700 kcal"],
                                ["1 cup tea with milk and 2 tsp sugar", "about 80 kcal"],
                                ["1 medium roti with ghee", "150 kcal (vs 110 plain)"],
                                ["30 g namkeen / bhujia", "about 165 kcal"]]}},
            "Three cups of sweet tea and a handful of namkeen add up to "
            "around 400 kcal, often the whole deficit. Measuring oil with a "
            "spoon instead of pouring it is the single easiest change.",
        ]),
        ("A 1,500 kcal vegetarian day", [
            "This day gives about 1,500 kcal and 70 g of protein. Keep oil "
            "to 3 to 4 teaspoons for the whole day.",
            {"table": {"head": ["Meal", "What to eat", "Calories", "Protein"],
                       "rows": [["Breakfast", "2 besan chillas (60 g besan), 100 g hung curd", "330 kcal", "20 g"],
                                ["Lunch", "2 roti, 1 katori dal, 1 katori sabzi, salad", "510 kcal", "15 g"],
                                ["Evening", "30 g roasted chana, tea with less sugar", "170 kcal", "8 g"],
                                ["Dinner", "100 g paneer bhurji, 1 roti, 1 katori sabzi", "520 kcal", "25 g"],
                                ["Total", "", "about 1,530 kcal", "about 68 g"]]}},
            "To eat rice instead of roti, one cup of cooked rice (150 g) "
            "replaces about two medium rotis. If you eat eggs, chicken or "
            "fish, swap them for the paneer to cut calories and add protein.",
        ]),
        ("Step 3: keep protein high and keep moving", [
            "Protein keeps you fuller and protects muscle while you lose "
            "fat. Aim for about 1.2 to 1.6 g per kg of body weight. The <a "
            "href=\"/guides/high-protein-indian-vegetarian-foods\">vegetarian "
            "protein guide</a> lists the best Indian sources.",
            "Strength training two or three times a week makes sure the "
            "weight you lose is mostly fat. Walking 7,000 to 10,000 steps a "
            "day adds 200 to 400 kcal of burn without making you hungrier.",
        ]),
        ("Step 4: check progress the right way", [
            "Weigh yourself in the morning, a few times a week, and compare "
            "the weekly average. Daily weight swings by 1 to 2 kg from water "
            "and salt, especially after a heavy dinner or during your period.",
            "If the weekly average has not moved after three weeks, cut "
            "another 150 to 200 kcal, usually from oil or snacks. The <a "
            "href=\"/weight-loss-calculator\">weight loss calculator</a> "
            "shows how long your goal will take at your pace.",
        ]),
    ],
    "faq": [
        ("Can I eat rice and still lose weight?",
         "Yes. Rice does not cause weight gain on its own; total calories do. "
         "Keep the portion to about one cup of cooked rice and pair it with "
         "dal, curd or a protein food."),
        ("How fast can I lose weight on an Indian diet?",
         "About 0.5 kg a week is realistic and sustainable for most people. "
         "You may lose 1 to 2 kg in the first week, mostly water, before it "
         "settles."),
        ("Is jaggery better than sugar for weight loss?",
         "Not really. Jaggery has about the same calories as sugar. It has "
         "small amounts of minerals, but for weight loss it counts the same."),
        ("Do I need to stop eating after 7 pm?",
         "No. What matters is how much you eat across the day, not the "
         "clock. Eating dinner earlier can help if late-night snacking is "
         "where your extra calories come from."),
    ],
    "related_calcs": ["calorie-calculator", "tdee-calculator",
                      "weight-loss-calculator", "protein-calculator"],
}

G_BREAKFAST = {
    "slug": "high-protein-indian-breakfast",
    "title": "High-Protein Indian Breakfast: 10 Easy Ideas",
    "desc": ("Ten Indian breakfasts with 15-30 g of protein each, from besan "
             "chilla and paneer paratha to egg bhurji and sattu, with "
             "protein and calories for every one."),
    "h1": "10 high-protein Indian breakfasts, with protein counts",
    "category": "Nutrition",
    "image": "fit-food",
    "intro": ("Poha, upma and paratha are quick and filling, but most give "
              "you only 5 to 8 g of protein. These ten breakfasts keep the "
              "same flavours and give you 15 to 30 g, which keeps you full "
              "until lunch and helps you build muscle."),
    "body": [
        ("Why protein at breakfast matters", [
            "Studies on protein timing suggest muscle grows best when "
            "protein is spread over three or four meals of about 0.4 g per "
            "kg each, rather than packed into dinner. For a 65 kg person "
            "that is about 25 g per meal.",
            "A protein-rich breakfast also keeps you full longer, which "
            "makes it easier to avoid mid-morning biscuits and chai.",
        ]),
        ("The ten breakfasts", [
            "Protein and calories are approximate, for one person.",
            {"table": {"head": ["Breakfast", "Protein", "Calories"],
                       "rows": [["2 besan chillas (60 g besan) + 100 g hung curd", "20 g", "330 kcal"],
                                ["2 moong dal chillas (60 g dal) with paneer filling (40 g)", "22 g", "340 kcal"],
                                ["1 paneer paratha (60 g paneer) + 1 katori curd", "20 g", "450 kcal"],
                                ["3-egg bhurji + 1 roti", "21 g", "360 kcal"],
                                ["Soya chunk upma (30 g soya, 30 g suji)", "20 g", "300 kcal"],
                                ["Oats cooked in 250 ml milk + 1 tbsp peanut butter", "18 g", "390 kcal"],
                                ["Sprouts chaat (1 cup) + 100 g paneer cubes", "20 g", "300 kcal"],
                                ["Sattu drink (40 g) + 2 boiled eggs", "20 g", "300 kcal"],
                                ["Poha with 20 g peanuts + 150 g hung curd", "22 g", "500 kcal"],
                                ["3 idli + sambar + 1 glass milk", "18 g", "450 kcal"]]}},
        ]),
        ("How to raise the protein in what you already eat", [
            {"list": [
                "Add 50 g of crumbled paneer or tofu to poha, upma or a "
                "paratha filling: about 6 to 9 g more protein.",
                "Mix a spoon of besan or sattu into atta for parathas.",
                "Serve hung curd instead of regular curd on the side.",
                "Cook oats or daliya in milk instead of water.",
                "Keep boiled eggs or roasted chana ready for rushed days.",
            ]},
            {"tip": "Running late? A glass of milk with a scoop of whey and "
                    "a banana takes two minutes and gives about 32 g of "
                    "protein."},
        ]),
    ],
    "faq": [
        ("Which Indian breakfast has the most protein?",
         "Among everyday options, egg bhurji, besan or moong dal chilla, "
         "paneer paratha and soya chunk upma lead, each at roughly 20 g per "
         "serving. Adding hung curd to any of them adds another 8 to 12 g."),
        ("Is poha a good breakfast for weight loss?",
         "Poha is light and fine in moderation, but low in protein at about "
         "5 g a plate. Add peanuts, sprouts or paneer, or have it with hung "
         "curd, so it keeps you full."),
        ("How much protein should breakfast have?",
         "About 20 to 30 g suits most adults who train, or roughly 0.4 g per "
         "kg of body weight."),
    ],
    "related_calcs": ["protein-calculator", "macro-calculator",
                      "calorie-calculator"],
}

G_MUSCLE_DIET = {
    "slug": "indian-gym-diet-for-muscle-gain",
    "title": "Indian Gym Diet for Muscle Gain (Veg & Non-Veg)",
    "desc": ("How many calories and how much protein you need to build "
             "muscle, with full Indian gym diet plans for vegetarians and "
             "non-vegetarians at about 2,500-2,600 kcal."),
    "h1": "Indian gym diet for muscle gain: veg and non-veg plans",
    "category": "Muscle Building",
    "image": "meal-prep",
    "intro": ("Building muscle takes three things: hard training, enough "
              "protein and a small calorie surplus. This guide turns those "
              "into a day of normal Indian food you can cook at home or in "
              "a hostel mess."),
    "body": [
        ("Your targets", [
            {"list": [
                "<strong>Calories:</strong> maintenance plus 250 to 400 kcal. "
                "Get maintenance from the <a href=\"/tdee-calculator\">TDEE "
                "calculator</a>.",
                "<strong>Protein:</strong> 1.6 to 2.2 g per kg of body "
                "weight. A 65 kg lifter needs about 105 to 140 g.",
                "<strong>Pace:</strong> gain about 0.25 to 0.5 kg a month as "
                "a beginner. Faster than that is mostly fat.",
            ]},
            "The <a href=\"/macro-calculator\">macro calculator</a> works out "
            "protein, carbs and fat for a lean bulk in one step.",
        ]),
        ("Non-vegetarian plan, about 2,600 kcal and 150 g protein", [
            {"table": {"head": ["Meal", "What to eat", "Protein"],
                       "rows": [["Breakfast", "4-egg omelette, 2 slices bread, 1 banana", "30 g"],
                                ["Lunch", "150 g cooked chicken curry, 1.5 cups rice, 1 katori dal, salad", "50 g"],
                                ["Pre-workout", "1 cup curd with 30 g oats and a banana", "10 g"],
                                ["Post-workout", "1 scoop whey in 300 ml milk", "34 g"],
                                ["Dinner", "150 g fish curry or a 3-egg curry, 3 roti, sabzi", "30-40 g"],
                                ["Total", "", "about 150-160 g"]]}},
        ]),
        ("Vegetarian plan, about 2,500 kcal and 135 g protein", [
            {"table": {"head": ["Meal", "What to eat", "Protein"],
                       "rows": [["Breakfast", "2 moong dal chillas with paneer, 150 g hung curd", "32 g"],
                                ["Lunch", "3 roti, 1 katori rajma, 50 g soya chunk sabzi, salad", "42 g"],
                                ["Pre-workout", "1 banana, 30 g peanuts", "8 g"],
                                ["Post-workout", "1 scoop whey in 300 ml milk", "34 g"],
                                ["Dinner", "1.5 cups rice, 1 katori dal, 1 katori curd, sabzi", "18 g"],
                                ["Total", "", "about 135 g"]]}},
            "Without whey, replace it with 100 g paneer and a glass of milk, "
            "or with another 50 g of soya chunks. More ideas are in the <a "
            "href=\"/guides/high-protein-indian-vegetarian-foods\">vegetarian "
            "protein guide</a>.",
        ]),
        ("Training matters more than the diet", [
            "Food only builds muscle if your training asks for it. Follow a "
            "structured plan such as <a href=\"/workouts/push-pull-legs\">push "
            "pull legs</a> or a <a href=\"/workouts/beginner-full-body-workout\">"
            "beginner full-body plan</a>, and add weight or reps over time, "
            "as explained in <a href=\"/guides/progressive-overload-explained\">"
            "progressive overload</a>.",
            {"tip": "Creatine monohydrate, 3 to 5 g a day, is the one "
                    "supplement with strong evidence for muscle and "
                    "strength. See the <a href=\"/guides/creatine-guide\">"
                    "creatine guide</a>."},
        ]),
    ],
    "faq": [
        ("Can I gain muscle on a budget Indian diet?",
         "Yes. Eggs, soya chunks, dal, milk, curd, peanuts and chicken are "
         "among the cheapest protein sources in India. Whey is convenient "
         "but optional."),
        ("How many eggs a day for muscle gain?",
         "Three to six whole eggs a day is a common, safe amount for healthy "
         "adults and gives 18 to 36 g of protein. Combine them with other "
         "protein foods rather than relying on eggs alone."),
        ("Should I eat ghee to gain weight?",
         "A little ghee is fine and an easy way to add calories, at about "
         "45 kcal per teaspoon. But extra calories from protein and carbs "
         "help you train harder, so do not use ghee to fill the whole "
         "surplus."),
        ("How long before I see muscle gain?",
         "Most beginners see visible changes in 8 to 12 weeks of consistent "
         "training and eating. Strength usually goes up within the first "
         "few weeks."),
    ],
    "related_calcs": ["macro-calculator", "tdee-calculator",
                      "protein-calculator", "ffmi-calculator"],
}

G_HOME_WORKOUT = {
    "slug": "home-workout-for-beginners-no-equipment",
    "title": "Home Workout for Beginners, No Equipment",
    "desc": ("A 3-day beginner home workout with no equipment that fits in a "
             "small room: squats, push-ups, lunges and planks, with sets, "
             "reps and how to progress each week."),
    "h1": "Home workout for beginners with no equipment",
    "category": "Training",
    "image": "home-workout",
    "intro": ("You do not need a gym membership to get stronger and lose "
              "fat. This plan needs a floor, a wall and a sturdy chair, fits "
              "in a two-metre square and takes about 30 minutes, three days "
              "a week."),
    "body": [
        ("How the plan works", [
            "Do the workout three days a week with a rest day between, for "
            "example Monday, Wednesday and Friday. Each session trains the "
            "whole body. Rest 60 to 90 seconds between sets.",
            "Early morning or late evening avoids the worst of the summer "
            "heat. Keep a fan on and water nearby: you will sweat more than "
            "you expect.",
        ]),
        ("The workout", [
            {"table": {"head": ["Exercise", "Sets x reps", "Easier version"],
                       "rows": [["Bodyweight squat", "3 x 12-15", "Squat to a chair"],
                                ["<a href=\"/exercises/push-up\">Push-up</a>", "3 x 6-12", "Hands on a wall or table"],
                                ["Reverse lunge", "3 x 8 each leg", "Hold a wall for balance"],
                                ["Glute bridge", "3 x 12-15", "Smaller range"],
                                ["Chair dip", "2 x 6-10", "Bend knees, feet closer"],
                                ["<a href=\"/exercises/plank\">Plank</a>", "3 x 20-40 s", "Knees down"],
                                ["Superman hold", "2 x 20 s", "Lift arms only"]]}},
            "Start with a 5-minute warm-up: marching on the spot, arm "
            "circles and 10 slow squats. Finish with a few minutes of "
            "stretching.",
        ]),
        ("How to progress", [
            "The body adapts to what you do, so the workout has to get "
            "slightly harder every week or two. This is <a "
            "href=\"/guides/progressive-overload-explained\">progressive "
            "overload</a>, and it is what makes a home workout keep working.",
            {"list": [
                "Add 1 or 2 reps per set until you reach the top of the range.",
                "Then move to a harder version: wall push-ups to table "
                "push-ups to floor push-ups.",
                "Slow the lowering part to 3 seconds to make a set harder.",
                "After 6 to 8 weeks, add a fourth set or a fourth day.",
                "When bodyweight gets easy, a pair of adjustable dumbbells "
                "opens up the <a href=\"/workouts/home-dumbbell-workout\">"
                "home dumbbell workout</a>.",
            ]},
        ]),
        ("Add walking for fat loss", [
            "If fat loss is your goal, the workout keeps your muscle while "
            "your diet does most of the work. A 30 to 45 minute walk on the "
            "other days burns an extra 150 to 250 kcal. The <a "
            "href=\"/calories-burned-calculator\">calories burned "
            "calculator</a> shows what each activity burns at your weight, "
            "and the <a href=\"/guides/indian-diet-plan-for-weight-loss\">"
            "Indian diet plan for weight loss</a> covers the food side.",
        ]),
    ],
    "faq": [
        ("Can I build muscle with home workouts?",
         "Yes, especially as a beginner. As long as each set is taken close "
         "to failure and you progress to harder versions, bodyweight "
         "training builds muscle. Progress slows after a year or so without "
         "added weight."),
        ("How long before I see results from home workouts?",
         "Most people feel stronger in 2 to 3 weeks and see visible changes "
         "in 6 to 10 weeks, if they train three times a week and eat to "
         "match their goal."),
        ("Is 30 minutes of exercise a day enough?",
         "Yes. Three 30-minute strength sessions a week plus daily walking "
         "meets the WHO activity guidelines for adults."),
        ("Should I work out every day?",
         "Not with this plan. Muscles need a day to recover between full-"
         "body sessions. Walk, stretch or play a sport on the rest days."),
    ],
    "related_calcs": ["calories-burned-calculator", "tdee-calculator",
                      "bmi-calculator"],
}

GUIDES = [G_BMI_CHART, G_VEG_PROTEIN, G_WEIGHT_LOSS, G_BREAKFAST,
          G_MUSCLE_DIET, G_HOME_WORKOUT]
