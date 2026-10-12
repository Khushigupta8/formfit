"""
Long-form copy for the first nine calculators.

Each entry is keyed by the calculator's slug and carries its SEO title, meta
description, the short intro that sits above the tool, the article body in the
shared block format, an FAQ and a short list of references. The numbers quoted
here must match what static/js does, so change both together.
"""

CONTENT = {
    # ------------------------------------------------------------------
    "bmi-calculator": {
        "title": "BMI Calculator - Body Mass Index for Adults",
        "desc": ("Work out your body mass index in metric or imperial units, "
                 "see your WHO weight category, your healthy weight range and "
                 "BMI Prime in seconds."),
        "intro": ("Enter your height and weight to get your body mass index, "
                  "the WHO category it falls in and the weight range that "
                  "counts as healthy for your height."),
        "body": [
            ("What BMI actually measures", [
                "Body mass index is a ratio of your weight to the square of "
                "your height. It does not measure fat, muscle or health "
                "directly. It is a quick screening number that tells you "
                "whether your weight is in a range that, across large "
                "populations, is linked with lower or higher health risk.",
                "That makes it useful and limited at the same time. For most "
                "adults who do not lift weights seriously, BMI tracks body "
                "fat reasonably well. For a lifter carrying a lot of muscle, "
                "it can be badly wrong, which is covered further down.",
                "This calculator is built for adults aged 18 and over. "
                "Children and teenagers are assessed with age and sex "
                "specific BMI percentiles, not the adult categories below.",
            ]),
            ("How to use the calculator", [
                "Pick metric or imperial with the unit toggle. In metric, "
                "enter height in centimetres and weight in kilograms. In "
                "imperial, enter feet and inches plus pounds. The tool "
                "converts everything internally, so the result is identical "
                "either way.",
                "Weigh yourself in the morning, after the bathroom and before "
                "eating, for the most repeatable number. Measure height "
                "barefoot against a wall. A 2 cm (about 1 in) error in height "
                "moves BMI by roughly half a point, so it is worth getting "
                "right.",
                "You get four things back: your BMI to one decimal place, "
                "your WHO category, the weight range that would put you "
                "between 18.5 and 24.9 at your height, and your BMI Prime.",
            ]),
            ("The formula", [
                "The maths is the same one Adolphe Quetelet described in the "
                "1830s. Only the unit conversion changes between systems.",
                {"formula": "BMI = weight (kg) / height (m)²"},
                {"formula": "BMI = 703 x weight (lb) / height (in)²"},
                {"formula": "BMI Prime = BMI / 25"},
                "BMI Prime expresses your BMI as a fraction of the upper "
                "healthy limit. A BMI Prime of 1.00 sits exactly on the line "
                "between healthy and overweight. 1.20 means you are 20% above "
                "that line, 0.80 means you are 20% below it. It makes "
                "progress easier to read than raw BMI points.",
                "The healthy weight range is worked out in reverse: 18.5 x "
                "height² and 24.9 x height², giving the lowest and highest "
                "weight that keep you in the healthy band.",
            ]),
            ("Reading your result", [
                "These are the World Health Organization categories for "
                "adults, which the calculator uses:",
                {"table": {
                    "head": ["BMI", "Category", "BMI Prime"],
                    "rows": [
                        ["Below 18.5", "Underweight", "Below 0.74"],
                        ["18.5 - 24.9", "Healthy weight", "0.74 - 0.99"],
                        ["25.0 - 29.9", "Overweight", "1.00 - 1.19"],
                        ["30.0 - 34.9", "Obese class I", "1.20 - 1.39"],
                        ["35.0 - 39.9", "Obese class II", "1.40 - 1.59"],
                        ["40.0 and above", "Obese class III", "1.60 and above"],
                    ]}},
                "A result near a boundary means very little on its own. "
                "Someone at 25.2 is not meaningfully less healthy than "
                "someone at 24.8. Watch the direction your number moves over "
                "months rather than reacting to a single reading.",
            ]),
            ("Asian populations use lower cut-offs", [
                "A 2004 WHO expert consultation found that many Asian "
                "populations carry more body fat and higher risk of type 2 "
                "diabetes and heart disease at the same BMI as European "
                "populations. It suggested public health action points of "
                "<strong>23</strong> for increased risk and "
                "<strong>27.5</strong> for high risk.",
                "If you are of South Asian, East Asian or Southeast Asian "
                "background, treat a BMI of 23 to 27.5 as worth acting on, "
                "even though the standard table still calls it healthy or "
                "overweight. Many national guidelines, including India's, "
                "already use these lower thresholds.",
            ]),
            ("Why lifters often get misclassified", [
                "BMI cannot tell muscle from fat. A 180 cm (5 ft 11 in) man "
                "who trains hard and weighs 90 kg (198 lb) at 13% body fat "
                "has a BMI of 27.8, which the table calls overweight. His "
                "waist and health markers may say otherwise.",
                "If you have been lifting consistently for a year or more, "
                "pair BMI with a measure that separates fat from muscle. The "
                "<a href=\"/body-fat-calculator\">body fat calculator</a> "
                "estimates fat percentage from a few tape measurements, and "
                "the <a href=\"/ffmi-calculator\">FFMI calculator</a> shows "
                "how much lean mass you carry for your height.",
                "BMI also tends to underestimate risk in older adults, who "
                "lose muscle and gain fat while their weight stays the same. "
                "Waist size is a useful second check; the "
                "<a href=\"/waist-to-hip-ratio-calculator\">waist-to-hip "
                "ratio calculator</a> covers that.",
                {"tip": "BMI is not meant for pregnancy, for under-18s, or "
                        "for diagnosing anything. If your result worries "
                        "you, a doctor can assess it alongside blood "
                        "pressure, blood sugar and waist size."},
            ]),
            ("What to do with your number", [
                "If you are above the healthy range and want to change it, "
                "start by finding your maintenance calories with the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a>, then set "
                "a modest deficit with the "
                "<a href=\"/calorie-calculator\">calorie calculator</a>. "
                "Our guide to <a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
                "calculating calories for weight loss</a> explains the "
                "process step by step.",
                "If you are underweight, the same tools work in reverse: eat "
                "above maintenance and lift to make the gain mostly muscle. "
                "The <a href=\"/workouts/beginner-full-body-workout\">beginner "
                "full body workout</a> is a sensible place to start.",
                "Either way, read <a href=\"/guides/bmi-vs-body-fat-percentage\">"
                "BMI vs body fat percentage</a> to understand when each "
                "number is the better guide.",
            ]),
        ],
        "faq": [
            ("What is a healthy BMI for adults?",
             "The WHO defines 18.5 to 24.9 as the healthy range for adults. "
             "For people of Asian background, risk starts rising from about "
             "23, so many guidelines use 23 as the upper healthy limit."),
            ("Is BMI accurate for people who lift weights?",
             "Often not. BMI only uses height and weight, so muscular people "
             "can be classed as overweight or obese while carrying little "
             "fat. A body fat estimate or FFMI gives a better picture."),
            ("Can I use this BMI calculator for children?",
             "No. Children and teenagers are assessed with BMI-for-age "
             "percentiles that account for growth. The adult categories here "
             "apply from age 18."),
            ("What is BMI Prime?",
             "BMI Prime is your BMI divided by 25, the upper limit of the "
             "healthy range. A value of 1.0 sits on that limit, and anything "
             "above it shows how far over it you are as a percentage."),
            ("How often should I check my BMI?",
             "Once a month is plenty. Day to day weight swings of 1 to 2 kg "
             "from water and food make more frequent checks noisy and "
             "unhelpful."),
        ],
        "sources": [
            "World Health Organization. Obesity: preventing and managing the global epidemic. WHO Technical Report Series 894, 2000",
            "WHO Expert Consultation. Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies. Lancet. 2004;363(9403):157-163",
            "Keys A, Fidanza F, Karvonen MJ et al. Indices of relative weight and obesity. J Chronic Dis. 1972;25(6):329-343",
        ],
    },

    # ------------------------------------------------------------------
    "bmr-calculator": {
        "title": "BMR Calculator - Basal Metabolic Rate (3 Formulas)",
        "desc": ("Calculate your basal metabolic rate with Mifflin-St Jeor, "
                 "revised Harris-Benedict and Katch-McArdle, and see how many "
                 "calories you burn at complete rest."),
        "intro": ("Find out how many calories your body burns at complete "
                  "rest, using three of the most widely used BMR equations "
                  "side by side."),
        "body": [
            ("What BMR is", [
                "Basal metabolic rate is the energy your body uses to stay "
                "alive while doing nothing: breathing, pumping blood, keeping "
                "your temperature steady, running your brain and repairing "
                "tissue. For most people it is the largest part of daily "
                "calorie burn, typically 60 to 70% of the total.",
                "BMR is not your calorie target. It is the floor that "
                "everything else sits on top of. To get your real daily burn "
                "you add the energy of movement, exercise and digestion, "
                "which is what the <a href=\"/tdee-calculator\">TDEE "
                "calculator</a> does.",
            ]),
            ("How to use the calculator", [
                "Enter your sex, age, height and weight. Those four inputs "
                "are enough for the Mifflin-St Jeor and Harris-Benedict "
                "equations, and the calculator shows both.",
                "The body fat field is optional. If you fill it in, the tool "
                "also runs Katch-McArdle, which works from lean mass instead "
                "of total weight. If you do not know your body fat, the "
                "<a href=\"/body-fat-calculator\">body fat calculator</a> "
                "can estimate it from a few tape measurements.",
                "All three results appear together so you can see how much "
                "they agree. For most people they land within about 100 kcal "
                "of each other.",
            ]),
            ("The three formulas", [
                "<strong>Mifflin-St Jeor (1990)</strong> is the default. In "
                "studies comparing predictive equations against measured "
                "metabolic rate, it has been the most accurate for the "
                "general adult population, including people with overweight.",
                {"formula": "Men: BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age + 5"},
                {"formula": "Women: BMR = 10 x weight (kg) + 6.25 x height (cm) - 5 x age - 161"},
                "<strong>Revised Harris-Benedict (Roza and Shizgal, "
                "1984)</strong> updates the original 1919 equation. It tends "
                "to give slightly higher numbers than Mifflin-St Jeor.",
                {"formula": "Men: BMR = 88.362 + 13.397 x kg + 4.799 x cm - 5.677 x age"},
                {"formula": "Women: BMR = 447.593 + 9.247 x kg + 3.098 x cm - 4.330 x age"},
                "<strong>Katch-McArdle</strong> ignores sex and age and "
                "uses only lean body mass, which is why it needs your body "
                "fat percentage.",
                {"formula": "BMR = 370 + 21.6 x lean body mass (kg)"},
                {"formula": "Lean body mass = weight x (1 - body fat % / 100)"},
            ]),
            ("Which result should you trust?", [
                {"table": {
                    "head": ["Situation", "Best formula", "Why"],
                    "rows": [
                        ["Most adults, body fat unknown", "Mifflin-St Jeor",
                         "Best validated for the general population"],
                        ["Lean, muscular lifter with a reliable body fat figure",
                         "Katch-McArdle", "Accounts for extra muscle that weight-only formulas miss"],
                        ["Higher body fat", "Mifflin-St Jeor",
                         "Katch-McArdle can underestimate if body fat is overstated"],
                        ["Comparing with older apps or charts", "Harris-Benedict",
                         "Many older tools still use it"],
                    ]}},
                "Katch-McArdle is only as good as the body fat number you "
                "feed it. A tape or smart-scale estimate can be off by 3 to "
                "5 percentage points, which moves the result by roughly 50 "
                "to 100 kcal. If you are unsure, stick with Mifflin-St Jeor.",
            ]),
            ("Why your BMR changes", [
                "Muscle burns more energy at rest than fat, so two people of "
                "the same weight can have different BMRs. Building muscle "
                "with something like the <a href=\"/workouts/upper-lower-split\">"
                "upper/lower split</a> nudges BMR up, though by less than "
                "fitness marketing suggests: roughly 13 kcal per kg of "
                "muscle per day.",
                "BMR also falls slowly with age, mostly because people lose "
                "muscle, and drops when you lose weight simply because there "
                "is less of you to run. That is why a calorie target that "
                "worked at the start of a diet needs revisiting every 4 to "
                "5 kg (about 10 lb) lost.",
            ]),
            ("Limitations", [
                "Every equation here predicts an average. Individuals can "
                "sit 10% or more above or below it because of genetics, "
                "thyroid function, medication and other factors. Lab tests "
                "such as indirect calorimetry measure BMR directly, but few "
                "people need that level of precision.",
                "The equations were developed in adults and are not meant "
                "for children, pregnancy or people with conditions that "
                "affect metabolism. If you are managing a medical condition, "
                "check targets with your doctor or a registered dietitian.",
                {"tip": "Never eat below your BMR for long stretches without "
                        "medical supervision. It makes the diet harder to "
                        "sustain and costs you muscle."},
            ]),
            ("Next steps", [
                "Take your BMR to the <a href=\"/tdee-calculator\">TDEE "
                "calculator</a> to add your activity level, then use the "
                "<a href=\"/macro-calculator\">macro calculator</a> to split "
                "those calories into protein, carbs and fat.",
                "If your goal is fat loss, our guide on "
                "<a href=\"/guides/how-to-calculate-calories-for-weight-loss\">"
                "calculating calories for weight loss</a> walks through "
                "setting a deficit you can actually stick to.",
            ]),
        ],
        "faq": [
            ("What is the difference between BMR and TDEE?",
             "BMR is what you burn at complete rest. TDEE adds everything "
             "else: walking, exercise, work and digesting food. TDEE is the "
             "number to base your eating on."),
            ("Which BMR formula is most accurate?",
             "For most adults, Mifflin-St Jeor has the best track record. "
             "Katch-McArdle can be better for lean, muscular people, but only "
             "if your body fat estimate is reliable."),
            ("Why do the three results differ?",
             "Each equation was built from a different group of people using "
             "different methods. Differences of 50 to 150 kcal are normal and "
             "smaller than the day to day error in tracking food."),
            ("Does lifting weights increase BMR?",
             "Yes, a little. Each kilogram of muscle adds roughly 13 kcal a "
             "day at rest. The bigger benefit of lifting during a diet is "
             "keeping the muscle you already have."),
            ("Should I eat my BMR to lose weight?",
             "No. Eating at BMR ignores all the energy you use moving around, "
             "so it is usually a steep and hard to sustain deficit. Base your "
             "target on TDEE minus a moderate deficit instead."),
        ],
        "sources": [
            "Mifflin MD, St Jeor ST, Hill LA et al. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990;51(2):241-247",
            "Roza AM, Shizgal HM. The Harris Benedict equation reevaluated: resting energy requirements and the body cell mass. Am J Clin Nutr. 1984;40(1):168-182",
            "Frankenfield D, Roth-Yousey L, Compher C. Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. J Am Diet Assoc. 2005;105(5):775-789",
            "McArdle WD, Katch FI, Katch VL. Exercise Physiology: Nutrition, Energy, and Human Performance. Lippincott Williams & Wilkins",
        ],
    },

    # ------------------------------------------------------------------
    "tdee-calculator": {
        "title": "TDEE Calculator - Total Daily Energy Expenditure",
        "desc": ("Estimate your total daily energy expenditure from your BMR "
                 "and activity level, compare every activity tier, and learn "
                 "to calibrate it with real weigh-ins."),
        "intro": ("Estimate how many calories you burn on a normal day, so you "
                  "know what eating at maintenance actually looks like."),
        "body": [
            ("What TDEE means", [
                "Total daily energy expenditure is every calorie you burn in "
                "24 hours. Eat that amount and your weight stays roughly "
                "level. Eat less and you lose; eat more and you gain. It is "
                "the single most useful number for planning any diet.",
                "TDEE has four parts: your basal metabolic rate, the energy "
                "used digesting food (about 10% of intake), planned exercise, "
                "and everything else you do on your feet, from walking to "
                "fidgeting. That last part, called NEAT, varies far more "
                "between people than most expect.",
            ]),
            ("How to use the calculator", [
                "Enter sex, age, height and weight, then pick the activity "
                "level that matches a typical week, not your best week. The "
                "calculator works out your BMR with the Mifflin-St Jeor "
                "equation and multiplies it by your activity factor.",
                "You get your TDEE plus a table showing what it would be at "
                "every activity level. That table is handy if your routine "
                "changes, for example on a deload week or when you start a "
                "new job with more walking.",
            ]),
            ("The formula", [
                {"formula": "TDEE = BMR (Mifflin-St Jeor) x activity multiplier"},
                {"table": {
                    "head": ["Activity level", "Multiplier", "Looks like"],
                    "rows": [
                        ["Sedentary", "1.2", "Desk job, little walking, no training"],
                        ["Lightly active", "1.375", "Training 1-3 days a week or a job with some walking"],
                        ["Moderately active", "1.55", "Training 3-5 days a week, 7,000-10,000 steps"],
                        ["Very active", "1.725", "Hard training 6-7 days a week or a physical job"],
                        ["Extra active", "1.9", "Physical labour plus training, or twice-daily sessions"],
                    ]}},
                "These multipliers come from long-standing nutrition practice "
                "rather than one precise study, which is exactly why "
                "calibrating against your own scale matters.",
            ]),
            ("Most people overestimate their activity", [
                "An hour of lifting feels like a lot, but a typical session "
                "burns 200 to 400 kcal, and much of that time is rest "
                "between sets. If you train four times a week and sit at a "
                "desk the rest of the time, you are closer to lightly active "
                "than very active.",
                "A good rule: if you are unsure between two levels, pick the "
                "lower one. Overestimating by one tier adds 250 to 350 kcal a "
                "day, which is enough to erase a whole fat-loss deficit.",
                {"tip": "Step count is a better guide than gym time. Under "
                        "5,000 steps is sedentary territory whatever you do "
                        "in the gym; 10,000 or more usually justifies "
                        "moderately active."},
            ]),
            ("Calibrate it with 2-3 weeks of weigh-ins", [
                "Treat the calculator's number as a starting estimate, then "
                "let your body correct it.",
                {"olist": [
                    "Eat close to your estimated TDEE every day for two to "
                    "three weeks. Track intake as honestly as you can.",
                    "Weigh yourself every morning under the same conditions "
                    "and write it down.",
                    "Compare the weekly average of week one with the last "
                    "week. Ignore single days; water swings can be 1-2 kg.",
                    "If the average rose, your TDEE is lower than estimated. "
                    "If it fell, it is higher.",
                    "Adjust using roughly 7,700 kcal per kg (3,500 per lb): a "
                    "0.5 kg weekly loss means you are about 550 kcal a day "
                    "under maintenance.",
                ]},
                "After this, your number is based on what you actually burn, "
                "not on a population average.",
            ]),
            ("Limitations", [
                "Prediction equations can be 10% off for an individual, and "
                "activity multipliers add more uncertainty on top. Medical "
                "conditions, some medications, and periods of heavy dieting "
                "can all lower expenditure. Pregnancy and breastfeeding raise "
                "needs and are not covered here.",
                "TDEE also moves as you change. Lose 5 kg and it drops; take "
                "up running and it rises. Recalculate after any significant "
                "change in weight or routine.",
            ]),
            ("What to do next", [
                "To turn maintenance into a goal, the "
                "<a href=\"/calorie-calculator\">calorie calculator</a> gives "
                "targets for gentle and faster loss or gain, and the "
                "<a href=\"/macro-calculator\">macro calculator</a> splits "
                "them into protein, carbs and fat.",
                "Want to raise your TDEE without eating less? More daily "
                "walking does more than most people think; our guide to "
                "<a href=\"/guides/cardio-for-fat-loss-hiit-vs-liss\">cardio "
                "for fat loss</a> compares the options, and the "
                "<a href=\"/workouts/fat-loss-workout-plan\">fat loss workout "
                "plan</a> puts them into a week.",
            ]),
        ],
        "faq": [
            ("Is TDEE the same as maintenance calories?",
             "Yes. Your TDEE is the number of calories that keeps your weight "
             "stable, which is what people mean by maintenance."),
            ("Should I count my workouts separately?",
             "No. The activity multiplier already includes exercise. Adding "
             "workout calories on top counts them twice and is a common "
             "reason diets stall."),
            ("Why is my weight not changing at my calculated TDEE?",
             "If it is stable, the estimate was right. If it is moving, use "
             "two to three weeks of average weigh-ins to adjust: roughly 550 "
             "kcal a day for every 0.5 kg per week of change."),
            ("How often should I recalculate TDEE?",
             "After every 4-5 kg (about 10 lb) of weight change, or whenever "
             "your activity changes for more than a couple of weeks."),
            ("Which activity level should a gym-goer choose?",
             "Most people who lift 3-5 times a week with a desk job fit "
             "lightly or moderately active. Your daily step count is the "
             "best tiebreaker."),
        ],
        "sources": [
            "Mifflin MD, St Jeor ST, Hill LA et al. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990;51(2):241-247",
            "Levine JA. Non-exercise activity thermogenesis (NEAT). Best Pract Res Clin Endocrinol Metab. 2002;16(4):679-702",
            "Hall KD, Sacks G, Chandramohan D et al. Quantification of the effect of energy imbalance on bodyweight. Lancet. 2011;378(9793):826-837",
        ],
    },

    # ------------------------------------------------------------------
    "calorie-calculator": {
        "title": "Calorie Calculator - Daily Calories to Lose or Gain",
        "desc": ("Find your maintenance calories and daily targets to lose or "
                 "gain 0.25 to 1 kg a week, with safety floors built in. Free, "
                 "metric or imperial."),
        "intro": ("See how many calories a day keep your weight steady, and "
                  "what to eat to lose or gain weight at a pace you choose."),
        "body": [
            ("What this calculator gives you", [
                "This tool starts from the same place as the "
                "<a href=\"/tdee-calculator\">TDEE calculator</a>: your "
                "maintenance calories, worked out from the Mifflin-St Jeor "
                "equation and your activity level. Then it adds or subtracts "
                "a fixed daily amount to give you five practical targets.",
                "It is designed for adults planning a diet phase. If you just "
                "want to know what you burn, the TDEE page is enough. If you "
                "want to know what to eat to change your weight, you are in "
                "the right place.",
            ]),
            ("How to use it", [
                "Enter sex, age, height, weight and a realistic activity "
                "level. The results table shows maintenance plus four goals. "
                "Choose the one that fits your timeline and how much hunger "
                "you can tolerate, then stick with it for at least two to "
                "three weeks before judging.",
                {"table": {
                    "head": ["Target", "Daily change", "Expected pace"],
                    "rows": [
                        ["Maintain", "0 kcal", "Weight stable"],
                        ["Mild weight loss", "-275 kcal", "About 0.25 kg (0.5 lb) a week"],
                        ["Weight loss", "-550 kcal", "About 0.5 kg (1 lb) a week"],
                        ["Extreme weight loss", "-1,100 kcal", "About 1 kg (2 lb) a week"],
                        ["Mild weight gain", "+275 kcal", "About 0.25 kg (0.5 lb) a week"],
                        ["Weight gain", "+550 kcal", "About 0.5 kg (1 lb) a week"],
                    ]}},
            ]),
            ("Where the numbers come from", [
                "The targets rely on a long-standing approximation: a "
                "kilogram of body weight change is worth about 7,700 kcal, "
                "and a pound about 3,500.",
                {"formula": "Daily change = weekly target (kg) x 7,700 / 7"},
                {"formula": "0.5 kg x 7,700 / 7 = 550 kcal per day"},
                "So a 550 kcal daily deficit should, on paper, take off half "
                "a kilogram a week.",
            ]),
            ("Why the 7,700 rule is only a starting point", [
                "Real weight loss slows over time. As you get lighter, your "
                "maintenance drops, and your body adapts by moving a little "
                "less and running a little more efficiently. Research by "
                "Kevin Hall and colleagues showed that the simple rule "
                "overstates long-term loss because it ignores this.",
                "Early on the opposite happens. The first week of a diet "
                "often shows a big drop that is mostly water and stored "
                "carbohydrate, not fat. Do not let it set your expectations "
                "for week five.",
                "The practical answer is to treat your target as a "
                "hypothesis. Weigh yourself daily, compare weekly averages, "
                "and adjust by 100 to 200 kcal if progress is clearly faster "
                "or slower than planned.",
            ]),
            ("Safety floors", [
                "The calculator flags any target that falls below "
                "<strong>1,200 kcal a day for women</strong> or "
                "<strong>1,500 kcal a day for men</strong>. Below these "
                "levels it becomes hard to get enough protein, vitamins and "
                "minerals from food, and losing muscle becomes much more "
                "likely.",
                "The extreme option is labelled that way for a reason. A "
                "1 kg weekly loss is reasonable for some people with a lot "
                "of weight to lose, but for someone already fairly lean it "
                "usually means lost strength, poor sleep and a diet that "
                "ends early. Most lifters do best losing 0.5 to 1% of body "
                "weight a week.",
                {"tip": "Pregnant or breastfeeding, under 18, or with a "
                        "history of disordered eating? Please get "
                        "personalised advice from a doctor or registered "
                        "dietitian instead of following a calculator target."},
            ]),
            ("Making the target work in the gym", [
                "Calories decide whether you lose or gain. Protein and "
                "training decide what you lose or gain. In a deficit, keep "
                "lifting heavy and keep protein high so the weight that comes "
                "off is fat rather than muscle. The "
                "<a href=\"/protein-calculator\">protein calculator</a> gives "
                "you a daily figure, and the "
                "<a href=\"/macro-calculator\">macro calculator</a> builds "
                "the full split.",
                "When gaining, a small surplus is enough. Beginners can add "
                "muscle quickly; experienced lifters gain mostly fat beyond "
                "about 0.25 kg a week. Our guide to "
                "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting</a> "
                "helps you choose, and the "
                "<a href=\"/workouts/push-pull-legs\">push pull legs</a> plan "
                "gives a surplus something to build.",
            ]),
        ],
        "faq": [
            ("How many calories should I eat to lose weight?",
             "Start about 500 kcal below your maintenance, which the "
             "calculator shows as the weight loss target. Adjust after two "
             "to three weeks based on how your average weight is moving."),
            ("Is 1,200 calories a day safe?",
             "For many women it is a sensible lower limit, not a goal. For "
             "most men and active women it is too low to meet nutrient needs "
             "or keep muscle. Going lower should be medically supervised."),
            ("Why did I lose so much weight in the first week?",
             "Early losses are mostly water and stored carbohydrate. Fat loss "
             "follows the slower, steadier pace the calculator predicts."),
            ("Does 3,500 calories always equal one pound?",
             "It is a useful approximation, not a law. Your maintenance falls "
             "as you lose weight, so long-term loss is usually slower than "
             "the simple rule predicts."),
            ("Should I eat back calories burned in workouts?",
             "No. Your activity level already includes training. Adding "
             "workout calories again is one of the most common reasons a "
             "deficit disappears."),
        ],
        "sources": [
            "Hall KD, Sacks G, Chandramohan D et al. Quantification of the effect of energy imbalance on bodyweight. Lancet. 2011;378(9793):826-837",
            "Mifflin MD, St Jeor ST, Hill LA et al. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990;51(2):241-247",
            "Helms ER, Aragon AA, Fitschen PJ. Evidence-based recommendations for natural bodybuilding contest preparation: nutrition and supplementation. J Int Soc Sports Nutr. 2014;11:20",
        ],
    },

    # ------------------------------------------------------------------
    "macro-calculator": {
        "title": "Macro Calculator - Protein, Carbs and Fat Grams",
        "desc": ("Calculate daily protein, carb and fat grams for cutting, "
                 "maintaining or lean bulking, with balanced, low carb, high "
                 "carb or keto splits and per-meal targets."),
        "intro": ("Turn your calorie target into daily grams of protein, carbs "
                  "and fat, then split them across your meals."),
        "body": [
            ("What macros are and why they matter", [
                "Macronutrients are the three nutrients that supply "
                "calories: protein and carbohydrate at 4 kcal per gram and "
                "fat at 9 kcal per gram. Your total calories decide whether "
                "your weight goes up or down. Your macros shape what that "
                "weight is made of and how you feel and train along the way.",
                "For lifters, protein is the one to get right first. It "
                "protects muscle in a deficit and supplies the raw material "
                "for growth in a surplus. Carbs and fat are more flexible and "
                "can be set to suit your preferences.",
            ]),
            ("How to use the calculator", [
                "Enter sex, age, height, weight and activity level so the "
                "tool can work out your maintenance calories. Then choose "
                "two things:",
                {"list": [
                    "<strong>Goal:</strong> cut (maintenance minus 20%), "
                    "maintain, or lean bulk (maintenance plus 10%).",
                    "<strong>Diet style:</strong> balanced, low carb, high "
                    "carb or keto, which changes how the non-protein "
                    "calories are shared between carbs and fat.",
                ]},
                "You get grams and calories for each macro, plus what that "
                "looks like split over three, four or five meals.",
            ]),
            ("How the numbers are calculated", [
                "The calculator sets the macros in a fixed order so protein "
                "is never squeezed out.",
                {"olist": [
                    "Calories: maintenance from Mifflin-St Jeor x activity, "
                    "then adjusted for your goal.",
                    "Protein: 2.0 g per kg body weight when cutting, 1.8 g/kg "
                    "when maintaining or bulking.",
                    "Fat: a share of total calories set by the diet style.",
                    "Carbs: whatever calories are left, divided by 4.",
                ]},
                {"formula": "Protein (g) = body weight (kg) x 2.0 or 1.8"},
                {"formula": "Fat (g) = calories x fat share / 9"},
                {"formula": "Carbs (g) = (calories - protein g x 4 - fat g x 9) / 4"},
                "On keto the order flips for carbs and fat: carbs are capped "
                "at about 5% of calories and fat fills the remainder.",
            ]),
            ("The four diet styles compared", [
                {"table": {
                    "head": ["Style", "Fat", "Carbs", "Best for"],
                    "rows": [
                        ["Balanced", "25% of kcal", "Remainder", "Most people, most goals"],
                        ["Low carb", "40% of kcal", "Remainder", "People who prefer fattier foods or feel fuller on them"],
                        ["High carb", "20% of kcal", "Remainder", "High training volume, endurance work, bulking"],
                        ["Keto", "Remainder", "About 5% of kcal", "People who do well with very low carbs"],
                    ]}},
                "When calories and protein are equal, controlled studies show "
                "very little difference in fat loss between high and low carb "
                "diets. The best split is the one you can follow. Lifters "
                "with heavy training volume usually perform better with more "
                "carbohydrate, since it refuels muscle glycogen.",
            ]),
            ("Worked example", [
                "An 80 kg (176 lb) man with a maintenance of 2,700 kcal "
                "chooses cut and balanced. His target is 2,160 kcal "
                "(2,700 x 0.8).",
                {"list": [
                    "Protein: 80 x 2.0 = 160 g (640 kcal)",
                    "Fat: 2,160 x 0.25 / 9 = 60 g (540 kcal)",
                    "Carbs: (2,160 - 640 - 540) / 4 = 245 g (980 kcal)",
                ]},
                "Over four meals that is about 40 g protein, 15 g fat and "
                "61 g carbs each.",
            ]),
            ("Limitations", [
                "Protein is set per kilogram of total body weight. If you "
                "carry a lot of body fat, that can produce a very high "
                "number; basing it on your goal weight is a sensible "
                "alternative. The "
                "<a href=\"/protein-calculator\">protein calculator</a> "
                "explains the ranges in more depth.",
                "Fat should rarely drop below about 0.5 g per kg for long, as "
                "very low fat intakes can affect hormone health. Keto is not "
                "suitable for everyone, including people on some diabetes "
                "medications; check with your doctor first.",
                {"tip": "Hit your calories and protein every day. Being 20 g "
                        "off on carbs or fat makes almost no difference."},
            ]),
            ("Putting it into practice", [
                "Build each meal around a protein source, then add carbs and "
                "fat to fill the plate. Our guide to "
                "<a href=\"/guides/pre-and-post-workout-nutrition\">pre and "
                "post workout nutrition</a> shows how to time carbs around "
                "training, and <a href=\"/guides/how-much-protein-to-build-muscle\">"
                "how much protein to build muscle</a> covers sources and "
                "timing.",
                "Pair your macros with a structured plan such as the "
                "<a href=\"/workouts/upper-lower-split\">upper/lower split</a> "
                "and check progress every few weeks with the "
                "<a href=\"/body-fat-calculator\">body fat calculator</a>.",
            ]),
        ],
        "faq": [
            ("What is the best macro ratio for fat loss?",
             "There is no single best ratio. Keep protein high, around 2 g "
             "per kg, stay in a calorie deficit, and split the rest between "
             "carbs and fat in whatever way you can sustain."),
            ("Do I have to hit my macros exactly?",
             "No. Aim to hit calories and protein within about 5-10%. Small "
             "daily variation in carbs and fat does not matter."),
            ("Why is my protein the same on different diet styles?",
             "Protein is set by body weight and goal, not by diet style. The "
             "style only changes how the remaining calories are split between "
             "carbs and fat."),
            ("Is keto better for building muscle?",
             "Generally not. Most lifters train harder and recover better "
             "with more carbohydrate, especially during a bulk. Keto can work "
             "for fat loss if you prefer it."),
            ("How many meals should I split my macros into?",
             "Three to five meals work for most people. Getting 25-40 g of "
             "protein in each meal is a practical target for muscle growth."),
        ],
        "sources": [
            "Jäger R, Kerksick CM, Campbell BI et al. International Society of Sports Nutrition Position Stand: protein and exercise. J Int Soc Sports Nutr. 2017;14:20",
            "Hall KD, Guo J. Obesity energetics: body weight regulation and the effects of diet composition. Gastroenterology. 2017;152(7):1718-1727",
            "Helms ER, Aragon AA, Fitschen PJ. Evidence-based recommendations for natural bodybuilding contest preparation: nutrition and supplementation. J Int Soc Sports Nutr. 2014;11:20",
        ],
    },

    # ------------------------------------------------------------------
    "protein-calculator": {
        "title": "Protein Calculator - How Much Protein Per Day",
        "desc": ("Work out how much protein you need per day for health, "
                 "fitness, muscle gain or fat loss, with per-meal targets and "
                 "real food equivalents you can plan around."),
        "intro": ("Find your daily protein target based on your weight and "
                  "goal, plus how much to eat per meal and what that looks "
                  "like as food."),
        "body": [
            ("Why protein needs vary so much", [
                "The protein figure printed on food labels and in public "
                "guidelines, 0.8 g per kg of body weight, is the amount that "
                "prevents deficiency in sedentary adults. It was never meant "
                "to be the best intake for someone lifting four days a week "
                "and trying to build muscle or hold on to it in a diet.",
                "Training increases how much protein your body uses to "
                "repair and build muscle. A calorie deficit increases it "
                "again, because your body is more willing to break muscle "
                "down for energy. That is why this calculator asks for your "
                "goal, not just your weight.",
            ]),
            ("How to use the calculator", [
                "Enter your body weight in kg or lb and choose the goal that "
                "fits you best. You get a daily range in grams, an amount to "
                "aim for at each of four meals, and food equivalents so the "
                "number feels real.",
                {"table": {
                    "head": ["Goal", "Grams per kg", "Grams per lb"],
                    "rows": [
                        ["Sedentary / general health", "0.8", "0.36"],
                        ["Active / general fitness", "1.2 - 1.6", "0.55 - 0.73"],
                        ["Build muscle", "1.6 - 2.2", "0.73 - 1.0"],
                        ["Fat loss while lifting", "1.8 - 2.4", "0.82 - 1.1"],
                    ]}},
            ]),
            ("The maths", [
                {"formula": "Daily protein (g) = body weight (kg) x grams per kg"},
                {"formula": "Per meal (g) = body weight (kg) x 0.4"},
                "For a 75 kg (165 lb) person building muscle, that is 120 to "
                "165 g a day, or about 30 g per meal across four meals.",
                "The per-meal figure comes from research suggesting that "
                "spreading roughly 0.4 g/kg over at least four meals is a "
                "practical way to maximise muscle building across the day.",
            ]),
            ("What the research says", [
                "A 2018 meta-analysis by Morton and colleagues in the "
                "<em>British Journal of Sports Medicine</em> pooled 49 "
                "studies on protein and resistance training. Gains in muscle "
                "levelled off at around <strong>1.6 g per kg</strong> a day "
                "on average, with the upper confidence limit around 2.2 g/kg. "
                "That is why the build muscle range runs from 1.6 to 2.2.",
                "The International Society of Sports Nutrition position stand "
                "(Jäger et al., 2017) recommends 1.4 to 2.0 g/kg for most "
                "exercising people, and notes that higher intakes may help "
                "preserve lean mass during a calorie deficit. Hence the "
                "higher fat loss range.",
                "More than 2.2 to 2.4 g/kg is not harmful for healthy people "
                "but offers little extra benefit and crowds out carbs and "
                "fats that fuel training.",
            ]),
            ("Turning grams into food", [
                "These are approximate protein contents for common foods:",
                {"table": {
                    "head": ["Food", "Serving", "Protein"],
                    "rows": [
                        ["Chicken breast, cooked", "100 g (3.5 oz)", "31 g"],
                        ["Eggs", "2 large", "12 g"],
                        ["Greek yogurt, plain", "200 g", "18-20 g"],
                        ["Paneer", "100 g", "18 g"],
                        ["Lentils, cooked", "1 cup (200 g)", "18 g"],
                        ["Tofu, firm", "100 g", "15 g"],
                        ["Whey protein", "1 scoop (30 g)", "22-25 g"],
                        ["Tuna, canned", "1 can (drained, ~120 g)", "28 g"],
                    ]}},
                "Plant proteins are slightly less digestible and lower in "
                "leucine on average. If you eat mostly plant foods, aim for "
                "the top half of your range and mix sources.",
            ]),
            ("Limitations and caution", [
                "If you carry a lot of body fat, calculating protein from "
                "total weight gives a figure that is higher than you need. "
                "Using your goal weight or lean body mass, from the "
                "<a href=\"/lean-body-mass-calculator\">lean body mass "
                "calculator</a>, keeps it realistic.",
                {"tip": "If you have kidney disease or reduced kidney "
                        "function, do not raise your protein intake without "
                        "talking to your doctor. High-protein diets are "
                        "considered safe for healthy kidneys, but not for "
                        "damaged ones."},
                "Pregnancy, breastfeeding and older age change protein needs "
                "too. Adults over 60 generally benefit from the higher end "
                "of each range to counter age-related muscle loss.",
            ]),
            ("Next steps", [
                "Fit your protein into a full plan with the "
                "<a href=\"/macro-calculator\">macro calculator</a>, then read "
                "<a href=\"/guides/how-much-protein-to-build-muscle\">how much "
                "protein to build muscle</a> for timing and source tips. If "
                "you are dieting, <a href=\"/guides/body-recomposition-guide\">"
                "body recomposition</a> explains how high protein lets you "
                "lose fat and gain muscle at the same time.",
            ]),
        ],
        "faq": [
            ("How much protein do I need to build muscle?",
             "Most lifters do well on 1.6 to 2.2 g per kg of body weight a "
             "day (about 0.7 to 1 g per lb). Research shows gains levelling "
             "off around 1.6 g/kg on average."),
            ("Can I eat too much protein?",
             "For healthy adults, intakes up to around 2.5 g/kg appear safe, "
             "but there is little extra benefit beyond 2.2 g/kg. People with "
             "kidney disease should follow medical advice."),
            ("How much protein can I absorb in one meal?",
             "Your body absorbs nearly all the protein you eat. For muscle "
             "building, about 0.4 g/kg per meal over four meals is a "
             "practical target, but larger meals are not wasted."),
            ("Do I need protein shakes?",
             "No. Shakes are a convenient way to top up, but whole foods can "
             "cover your target just as well."),
            ("Should I base protein on my current or goal weight?",
             "If you are lean or near your goal, use current weight. If you "
             "have a lot of fat to lose, goal weight gives a more sensible "
             "number."),
        ],
        "sources": [
            "Morton RW, Murphy KT, McKellar SR et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. Br J Sports Med. 2018;52(6):376-384",
            "Jäger R, Kerksick CM, Campbell BI et al. International Society of Sports Nutrition Position Stand: protein and exercise. J Int Soc Sports Nutr. 2017;14:20",
            "Schoenfeld BJ, Aragon AA. How much protein can the body use in a single meal for muscle-building? J Int Soc Sports Nutr. 2018;15:10",
        ],
    },

    # ------------------------------------------------------------------
    "body-fat-calculator": {
        "title": "Body Fat Calculator - US Navy Tape Method",
        "desc": ("Estimate your body fat percentage with the US Navy tape "
                 "method using height, neck, waist and hip. See your ACE "
                 "category, fat mass and lean mass."),
        "intro": ("Estimate your body fat percentage with nothing more than a "
                  "tape measure, and see how much of your weight is fat and "
                  "how much is lean mass."),
        "body": [
            ("Why body fat beats the scale", [
                "Two people can weigh the same and look completely different "
                "because one carries more muscle and the other more fat. "
                "Body fat percentage separates the two, which makes it far "
                "more useful than weight or BMI for anyone who trains.",
                "It also tells you whether a diet is working properly. If "
                "your weight drops but your body fat percentage barely "
                "moves, you may be losing muscle along with fat.",
            ]),
            ("How the US Navy method works", [
                "The US Navy developed this method in the 1980s to assess "
                "personnel quickly without lab equipment. Researchers "
                "Hodgdon and Beckett compared circumference measurements "
                "against underwater weighing and built equations that "
                "predict body fat from them. It is still used by the US "
                "military today.",
                {"formula": "Men: BF% = 495 / (1.0324 - 0.19077 x log10(waist - neck) + 0.15456 x log10(height)) - 450"},
                {"formula": "Women: BF% = 495 / (1.29579 - 0.35004 x log10(waist + hip - neck) + 0.22100 x log10(height)) - 450"},
                "All measurements are in centimetres. The calculator "
                "converts inches for you. From your body fat percentage it "
                "also works out fat mass (weight x BF%) and lean mass "
                "(weight minus fat mass).",
            ]),
            ("How to measure correctly", [
                "The equations are very sensitive to waist size, so a "
                "sloppy measurement can move your result by several points. "
                "Use a flexible, non-stretch tape and measure in the morning "
                "before eating.",
                {"olist": [
                    "<strong>Height:</strong> barefoot, back against a wall.",
                    "<strong>Neck:</strong> just below the Adam's apple, tape "
                    "angled slightly down toward the front.",
                    "<strong>Waist (men):</strong> horizontally at the level "
                    "of the navel, relaxed, at the end of a normal breath out.",
                    "<strong>Waist (women):</strong> at the narrowest point, "
                    "usually just above the navel.",
                    "<strong>Hip (women):</strong> around the widest part of "
                    "the buttocks, feet together.",
                ]},
                "Keep the tape snug but not pressing into the skin, and do "
                "not suck in. Take each measurement twice and use the "
                "average.",
            ]),
            ("Reading your result", [
                "The calculator places you in one of the American Council "
                "on Exercise (ACE) categories:",
                {"table": {
                    "head": ["Category", "Men", "Women"],
                    "rows": [
                        ["Essential fat", "2 - 5%", "10 - 13%"],
                        ["Athletes", "6 - 13%", "14 - 20%"],
                        ["Fitness", "14 - 17%", "21 - 24%"],
                        ["Average", "18 - 24%", "25 - 31%"],
                        ["Obese", "25% and above", "32% and above"],
                    ]}},
                "Women naturally carry more essential fat, linked to "
                "hormonal and reproductive health, so their ranges sit "
                "higher. Staying near essential levels is not healthy long "
                "term for anyone; it is a stage-day condition for "
                "bodybuilders, not a goal.",
            ]),
            ("How accurate is it?", [
                "Compared with lab methods, the Navy method typically lands "
                "within about <strong>3 to 4 percentage points</strong> of "
                "the true value for most people. It tends to be less "
                "accurate for very lean, very muscular, or very heavy "
                "people, and for anyone whose fat is stored unusually.",
                "Precision matters more than accuracy for tracking. If you "
                "measure the same way every time, the change over weeks is "
                "much more reliable than any single reading. Smart scales "
                "and bioimpedance devices are not clearly better, and they "
                "swing with hydration. Our guide to "
                "<a href=\"/guides/how-to-measure-body-fat-at-home\">measuring "
                "body fat at home</a> compares the options.",
                {"tip": "Measure every two to four weeks, not daily. Body "
                        "fat changes slowly, and frequent checks mostly "
                        "pick up measurement noise."},
            ]),
            ("What to do with your number", [
                "Use your lean mass to sharpen other calculations. The "
                "<a href=\"/bmr-calculator\">BMR calculator</a> can use your "
                "body fat for the Katch-McArdle formula, and the "
                "<a href=\"/ffmi-calculator\">FFMI calculator</a> shows how "
                "muscular you are for your height.",
                "If you want to lower body fat, set a modest deficit with the "
                "<a href=\"/calorie-calculator\">calorie calculator</a> and "
                "read <a href=\"/guides/how-to-lose-belly-fat\">how to lose "
                "belly fat</a>. If you are already lean and want to build, "
                "<a href=\"/guides/bulking-vs-cutting\">bulking vs cutting</a> "
                "helps you plan the next phase.",
            ]),
        ],
        "faq": [
            ("How accurate is the US Navy body fat method?",
             "For most people it is within about 3-4 percentage points of lab "
             "methods. It is best used to track changes over time with "
             "consistent measurements."),
            ("Where should men measure their waist?",
             "Horizontally at the navel, standing relaxed, at the end of a "
             "normal breath out. Do not pull the stomach in."),
            ("Why do women need a hip measurement?",
             "Women tend to store more fat around the hips and thighs, so the "
             "women's equation includes hip size to account for it."),
            ("What is a good body fat percentage?",
             "For general health and fitness, roughly 14-24% for men and "
             "21-31% for women is common. Athletes often sit lower."),
            ("Is body fat percentage better than BMI?",
             "For people who train, yes. BMI cannot tell muscle from fat, "
             "while body fat percentage shows your body composition directly."),
        ],
        "sources": [
            "Hodgdon JA, Beckett MB. Prediction of percent body fat for U.S. Navy men and women from body circumferences and height. Naval Health Research Center, Reports 84-11 and 84-29, 1984",
            "American Council on Exercise. ACE Personal Trainer Manual. American Council on Exercise",
            "Heyward VH, Wagner DR. Applied Body Composition Assessment. 2nd ed. Human Kinetics; 2004",
        ],
    },

    # ------------------------------------------------------------------
    "one-rep-max-calculator": {
        "title": "One Rep Max Calculator - Estimate Your 1RM",
        "desc": ("Estimate your one rep max from any set of 1 to 12 reps using "
                 "Epley, Brzycki and Lombardi, then get a full training "
                 "percentage chart for your program."),
        "intro": ("Estimate the most you could lift for one rep from a set you "
                  "have already done, then get your training weights by "
                  "percentage."),
        "body": [
            ("What a one rep max is", [
                "Your one rep max, or 1RM, is the heaviest weight you can "
                "lift once with good technique. Most strength programs, "
                "including the <a href=\"/workouts/5x5-strength-program\">5x5 "
                "strength program</a>, prescribe training loads as a "
                "percentage of it, so knowing roughly where it sits makes "
                "programming much easier.",
                "You do not need to test it to find it. A hard set of a few "
                "reps carries enough information to estimate it closely, "
                "without the injury risk and fatigue of a true max attempt.",
            ]),
            ("How to use the calculator", [
                "Enter the weight you lifted and how many clean reps you "
                "managed, from 1 to 12. Use a set taken close to failure, "
                "with one rep or less left in the tank, for the best "
                "estimate. A comfortable set of 5 with plenty left will "
                "underestimate your max.",
                "The calculator shows the estimate from three formulas, "
                "their average, and a chart of percentages from 100% down "
                "to 50% with the approximate reps you could do at each.",
            ]),
            ("The three formulas", [
                "Each formula was derived from a different set of lifters "
                "and fits slightly differently across rep ranges.",
                {"formula": "Epley: 1RM = weight x (1 + reps / 30)"},
                {"formula": "Brzycki: 1RM = weight x 36 / (37 - reps)"},
                {"formula": "Lombardi: 1RM = weight x reps^0.10"},
                "Epley and Brzycki agree closely in the 2 to 10 rep range. "
                "Lombardi tends to give lower numbers at higher reps. The "
                "average smooths out those quirks, which is why it is shown "
                "as the headline figure.",
                "Example: 100 kg (220 lb) for 5 reps gives Epley 116.7 kg, "
                "Brzycki 112.5 kg and Lombardi 117.5 kg, averaging about "
                "115.6 kg.",
            ]),
            ("Using the percentage chart", [
                {"table": {
                    "head": ["% of 1RM", "Approx. reps", "Typical use"],
                    "rows": [
                        ["100%", "1", "Max testing, competition"],
                        ["95%", "2", "Heavy singles and doubles"],
                        ["90%", "3-4", "Strength peaking"],
                        ["85%", "5-6", "Strength work, 5x5 style"],
                        ["80%", "7-8", "Strength and size"],
                        ["75%", "9-10", "Hypertrophy"],
                        ["70%", "11-12", "Hypertrophy, technique"],
                        ["65%", "13-15", "Volume work"],
                        ["60%", "16-20", "Warm-ups, speed work"],
                        ["50%", "20+", "Warm-ups, deloads"],
                    ]}},
                "Rep numbers are averages. Some people can do more reps at a "
                "given percentage, especially on lower body lifts, and "
                "everyone gets fewer reps when tired. Our guide to "
                "<a href=\"/guides/how-many-sets-and-reps-for-muscle-growth\">"
                "sets and reps for muscle growth</a> explains how to use "
                "these zones.",
            ]),
            ("Accuracy and its limits", [
                "Estimates are most accurate from sets of 1 to 6 reps and "
                "become noticeably less reliable beyond about 10. At high "
                "reps, endurance and pain tolerance start to matter as much "
                "as strength, and the formulas cannot see that.",
                "Results also vary by lift. Estimates for the "
                "<a href=\"/exercises/deadlift\">deadlift</a> and "
                "<a href=\"/exercises/barbell-back-squat\">squat</a> often "
                "differ from the bench press for the same rep count. Use the "
                "numbers to plan training, not as a substitute for a "
                "properly run test if you compete.",
            ]),
            ("Safety", [
                "Testing a true one rep max is a skill. If you are new to "
                "lifting, have not used a lift for long, or train alone, "
                "use this calculator instead of testing.",
                {"tip": "Never attempt a max bench press without a spotter or "
                        "safety arms set at the right height. For squats, "
                        "use a rack with safety pins and learn how to bail "
                        "out before you need to."},
                "If you do test, warm up gradually, take three to five "
                "minutes between heavy attempts, and stop when technique "
                "breaks down rather than when the bar stops moving.",
            ]),
            ("Next steps", [
                "Track your estimate every few weeks to see whether your "
                "program is working, and read "
                "<a href=\"/guides/progressive-overload-explained\">progressive "
                "overload explained</a> to keep the number climbing. If you "
                "compete in powerlifting, the "
                "<a href=\"/wilks-calculator\">Wilks and DOTS calculator</a> "
                "compares your total across body weights, and the "
                "<a href=\"/plate-calculator\">plate calculator</a> tells you "
                "exactly what to load.",
            ]),
        ],
        "faq": [
            ("How accurate are one rep max calculators?",
             "From sets of 1 to 6 reps they are usually within a few percent "
             "of a true max. Accuracy drops with higher rep sets, especially "
             "above about 10 reps."),
            ("Which 1RM formula is best?",
             "Epley and Brzycki are the most widely used and agree closely in "
             "the low to mid rep range. The average of several formulas is a "
             "sensible middle ground."),
            ("How often should I test my 1RM?",
             "Most lifters do not need to test true maxes at all. Estimating "
             "from a hard set every four to eight weeks is safer and gives "
             "similar information."),
            ("Should I use reps to failure?",
             "Use a set where you had about one rep left. Grinding to absolute "
             "failure adds risk without improving the estimate much."),
            ("Can beginners use this calculator?",
             "Yes, and it is safer than testing. Beginners' numbers change "
             "quickly, so re-estimate every few weeks."),
        ],
        "sources": [
            "Epley B. Poundage chart. Boyd Epley Workout. Lincoln, NE: Body Enterprises; 1985",
            "Brzycki M. Strength testing: predicting a one-rep max from reps-to-fatigue. J Phys Educ Recreat Dance. 1993;64(1):88-90",
            "LeSuer DA, McCormick JH, Mayhew JL et al. The accuracy of prediction equations for estimating 1-RM performance in the bench press, squat, and deadlift. J Strength Cond Res. 1997;11(4):211-213",
        ],
    },

    # ------------------------------------------------------------------
    "ideal-weight-calculator": {
        "title": "Ideal Weight Calculator - 4 Formulas and BMI Range",
        "desc": ("Calculate your ideal body weight with the Devine, Robinson, "
                 "Miller and Hamwi formulas, plus the healthy BMI weight range "
                 "for your height and sex."),
        "intro": ("Compare four classic ideal body weight formulas with the "
                  "healthy BMI range for your height, and see why the answer "
                  "is a range, not a single number."),
        "body": [
            ("What ideal weight formulas actually are", [
                "There is no single ideal weight for a given height. The "
                "formulas on this page were created by doctors to estimate "
                "a reference weight for calculating drug doses and kidney "
                "function, not to tell anyone how they should look.",
                "They are still a useful sense check, especially when shown "
                "together and next to the healthy BMI range. Where they "
                "cluster gives you a reasonable picture of a typical healthy "
                "weight for an average build at your height.",
            ]),
            ("How to use the calculator", [
                "Choose your sex and enter your height in centimetres or "
                "feet and inches. The calculator returns the result from "
                "each of the four formulas and the weight range that keeps "
                "your BMI between 18.5 and 24.9.",
                "Weight is not an input, because none of the formulas use "
                "it. That is part of their limitation: they ignore your "
                "frame and how much muscle you carry.",
            ]),
            ("The four formulas", [
                "All four start from a base weight at 5 feet (152.4 cm) and "
                "add a fixed amount for every inch above that.",
                {"table": {
                    "head": ["Formula", "Men", "Women"],
                    "rows": [
                        ["Devine (1974)", "50 kg + 2.3 kg per inch", "45.5 kg + 2.3 kg per inch"],
                        ["Robinson (1983)", "52 kg + 1.9 kg per inch", "49 kg + 1.7 kg per inch"],
                        ["Miller (1983)", "56.2 kg + 1.41 kg per inch", "53.1 kg + 1.36 kg per inch"],
                        ["Hamwi (1964)", "48 kg + 2.7 kg per inch", "45.5 kg + 2.2 kg per inch"],
                    ]}},
                {"formula": "Inches over 5 ft = (height in cm / 2.54) - 60"},
                {"formula": "Healthy BMI range = 18.5 x height(m)² to 24.9 x height(m)²"},
                "Example: a man 178 cm (5 ft 10 in) tall gets Devine 73.2 kg, "
                "Robinson 71.2 kg, Miller 70.4 kg and Hamwi 75.2 kg. His "
                "healthy BMI range is 58.6 to 78.9 kg.",
            ]),
            ("Why the formulas disagree", [
                "Each formula came from different data and was tuned for a "
                "different purpose. Devine's was a dosing shortcut that "
                "spread through medicine without much testing. Robinson and "
                "Miller were later attempts to fit it better to actual "
                "population data. Hamwi's dates from life insurance tables "
                "of the era.",
                "Miller's formula rises slowest with height, so it gives "
                "lower numbers for tall people. Hamwi's rises fastest. For "
                "very short or very tall people the spread between them can "
                "be 10 kg or more, which shows how rough these estimates are.",
            ]),
            ("Who these numbers do not suit", [
                {"list": [
                    "<strong>People who lift.</strong> Muscle is dense. A "
                    "well-trained lifter can be 10-15 kg over every formula "
                    "here and still be lean and healthy.",
                    "<strong>Larger or smaller frames.</strong> None of the "
                    "formulas adjust for bone structure.",
                    "<strong>Very short or very tall people.</strong> The "
                    "linear per-inch method breaks down at the extremes, and "
                    "the formulas are not meant for anyone under 5 ft.",
                    "<strong>Children, older adults and pregnancy.</strong> "
                    "Different references apply.",
                ]},
                {"tip": "If your weight is above these numbers but your waist "
                        "is under half your height and your body fat is in "
                        "a healthy range, the formulas are not telling you "
                        "anything useful."},
            ]),
            ("A better target for lifters", [
                "If you train, build your goal from body composition instead. "
                "Estimate your body fat with the "
                "<a href=\"/body-fat-calculator\">body fat calculator</a>, "
                "find your lean mass with the "
                "<a href=\"/lean-body-mass-calculator\">lean body mass "
                "calculator</a>, and decide what body fat you want to reach. "
                "Then divide lean mass by (1 minus your target body fat as a "
                "decimal).",
                {"formula": "Goal weight = lean mass / (1 - target BF% / 100)"},
                "Someone with 65 kg of lean mass aiming for 15% body fat "
                "would land at about 76.5 kg. Check your muscularity with "
                "the <a href=\"/ffmi-calculator\">FFMI calculator</a>.",
            ]),
            ("Next steps", [
                "To move toward your chosen weight, find your maintenance "
                "with the <a href=\"/tdee-calculator\">TDEE calculator</a> "
                "and read <a href=\"/guides/bmi-vs-body-fat-percentage\">BMI "
                "vs body fat percentage</a> to understand which number to "
                "watch. Beginners should pair any weight goal with the "
                "<a href=\"/guides/beginner-gym-guide\">beginner gym guide</a>.",
            ]),
        ],
        "faq": [
            ("Which ideal weight formula is most accurate?",
             "None is accurate for individuals. Robinson and Miller tend to "
             "fit modern populations a little better than Devine, but the "
             "healthy BMI range is a more practical guide."),
            ("Why is my ideal weight lower than my current weight even though "
             "I am lean?",
             "The formulas ignore muscle and frame size. Lifters routinely "
             "weigh more than them while carrying little fat."),
            ("What were these formulas designed for?",
             "Mostly for doctors estimating drug doses and kidney function. "
             "They were never intended as aesthetic or fitness targets."),
            ("Does ideal weight change with age?",
             "The formulas do not include age. In practice, keeping muscle as "
             "you age matters more than hitting a specific number."),
            ("Can I use these formulas if I am under 5 feet tall?",
             "They are not designed for heights under 5 ft. Use the healthy "
             "BMI range shown by the calculator instead."),
        ],
        "sources": [
            "Devine BJ. Gentamicin therapy. Drug Intell Clin Pharm. 1974;8:650-655",
            "Robinson JD, Lupkiewicz SM, Palenik L et al. Determination of ideal body weight for drug dosage calculations. Am J Hosp Pharm. 1983;40(6):1016-1019",
            "Miller DR, Carlson JD, Loyd BJ, Day BJ. Determining ideal body weight (and mass). Am J Hosp Pharm. 1983;40(10):1622-1625",
            "Pai MP, Paloucek FP. The origin of the 'ideal' body weight equations. Ann Pharmacother. 2000;34(9):1066-1069",
        ],
    },
}


# Worked examples and practical sections, slotted in before each page's
# closing "next steps" section.
_EXTRA = {
    "bmi-calculator": ("Waist size: the check BMI misses", [
        "Where you carry fat matters as much as how much you carry. Fat "
        "stored deep around the organs, which shows up as a larger waist, is "
        "more strongly linked with type 2 diabetes and heart disease than fat "
        "on the hips and thighs. Two people with the same BMI can have very "
        "different risk because of this.",
        "A simple rule used by the UK's NICE guidance is to keep your waist "
        "below half your height. A 170 cm (5 ft 7 in) person would aim for a "
        "waist under 85 cm (33.5 in). Measure at the midpoint between the "
        "bottom of your ribs and the top of your hip bone, relaxed, after "
        "breathing out.",
        "If your BMI is in the healthy range but your waist is above that "
        "line, it is worth paying attention to. If your BMI says overweight "
        "but your waist is comfortably under it and you train regularly, "
        "your extra weight is probably muscle.",
    ]),
    "bmr-calculator": ("Worked example", [
        "Take a 30-year-old woman who is 165 cm (5 ft 5 in) tall, weighs "
        "62 kg (137 lb) and estimates her body fat at 26%.",
        {"list": [
            "Mifflin-St Jeor: 10 x 62 + 6.25 x 165 - 5 x 30 - 161 = 1,340 kcal",
            "Revised Harris-Benedict: 447.593 + 9.247 x 62 + 3.098 x 165 - "
            "4.330 x 30 = 1,402 kcal",
            "Katch-McArdle: lean mass 62 x 0.74 = 45.9 kg, so 370 + 21.6 x "
            "45.9 = 1,361 kcal",
        ]},
        "The three answers sit within about 60 kcal of each other, which "
        "is typical. That gap is smaller than the error in most people's "
        "food tracking, so there is no point agonising over which one is "
        "right. Pick Mifflin-St Jeor unless you have a solid reason not to, "
        "and let your weigh-ins tell you whether the final calorie target "
        "needs nudging.",
        "Notice how small the age term is: five extra years lowers the "
        "Mifflin-St Jeor result by only 25 kcal. Changes in muscle and body "
        "weight move BMR far more than birthdays do.",
    ]),
    "tdee-calculator": ("Worked example", [
        "A 28-year-old man, 180 cm (5 ft 11 in) and 82 kg (181 lb), lifts "
        "four times a week and averages about 8,000 steps a day.",
        {"list": [
            "BMR (Mifflin-St Jeor): 10 x 82 + 6.25 x 180 - 5 x 28 + 5 = 1,810 kcal",
            "Lightly active (1.375): 2,489 kcal",
            "Moderately active (1.55): 2,806 kcal",
        ]},
        "He is somewhere between the two tiers, so a sensible starting "
        "point is the lower figure of about 2,500 kcal. After three weeks of "
        "eating close to that, his weekly average weight has dropped by "
        "0.3 kg (0.7 lb) in total, or about 0.1 kg a week. That works out "
        "to a daily deficit of roughly 110 kcal, so his real maintenance is "
        "close to 2,600 kcal.",
        "That is the whole point of calibration. The calculator got him "
        "within about 4%, and two to three weeks of honest data closed the "
        "gap. From here he can set a cut or a lean bulk using a number that "
        "reflects his own body, not an average one.",
    ]),
    "calorie-calculator": ("Worked example", [
        "A 35-year-old woman, 163 cm (5 ft 4 in), 74 kg (163 lb), lightly "
        "active. Her BMR is 10 x 74 + 6.25 x 163 - 5 x 35 - 161 = 1,423 kcal, "
        "and her maintenance is 1,423 x 1.375 = 1,956 kcal.",
        {"table": {
            "head": ["Target", "Calories a day"],
            "rows": [
                ["Maintain", "1,956"],
                ["Mild weight loss", "1,681"],
                ["Weight loss", "1,406"],
                ["Extreme weight loss", "856 (flagged: below 1,200)"],
                ["Mild weight gain", "2,231"],
                ["Weight gain", "2,506"],
            ]}},
        "The extreme target is flagged because it falls well below the "
        "1,200 kcal floor. For her, the weight loss option at around "
        "1,400 kcal is the realistic choice, and it should take off roughly "
        "2 kg (4.4 lb) a month at first.",
        "This shows why smaller and less active people have less room for "
        "aggressive deficits. A fixed 1,100 kcal cut is a big share of a "
        "small maintenance. Increasing daily steps is often a better way to "
        "widen the gap than eating less still.",
    ]),
    "macro-calculator": ("Adjusting macros as you go", [
        "Your first set of macros is a starting point. Review it every two "
        "to four weeks using three signals: the trend in your weekly average "
        "weight, how your training is going, and how hungry you are.",
        {"list": [
            "<strong>Weight not moving as planned:</strong> change calories "
            "first, by 100 to 200 kcal, taking it from or adding it to carbs "
            "or fat. Leave protein alone.",
            "<strong>Training feels flat in a cut:</strong> move some calories "
            "from fat to carbs, especially around sessions.",
            "<strong>Constantly hungry:</strong> keep protein high, add more "
            "high-volume foods like vegetables and potatoes, and consider a "
            "slightly smaller deficit.",
            "<strong>After losing 4-5 kg (about 10 lb):</strong> recalculate, "
            "because your maintenance and protein target have both dropped.",
        ]},
        "Tracking does not need to be perfect to work. Weighing foods for a "
        "few weeks teaches you what portions look like, and many people can "
        "then estimate well enough to keep progressing without logging "
        "every meal.",
    ]),
    "protein-calculator": ("Timing and distribution", [
        "Total daily protein matters most. Once that is covered, spreading "
        "it fairly evenly gives a small additional benefit. A study by "
        "Areta and colleagues found that four meals of about 20 g each "
        "stimulated muscle protein synthesis more over 12 hours than two "
        "large meals or eight small ones.",
        "In practice that means building three to five meals around a "
        "decent protein source rather than eating most of it at dinner. "
        "Breakfast is where most people fall short; eggs, yogurt or a shake "
        "fix that quickly.",
        "The window after training is less urgent than once believed. If "
        "you ate a protein-rich meal a few hours before lifting, there is no "
        "need to rush a shake afterwards. If you train fasted first thing in "
        "the morning, eating protein reasonably soon after makes more sense.",
        "A serving of protein before bed, such as cottage cheese or a casein "
        "shake, is a convenient way to add another feeding for people who "
        "struggle to hit their total during the day.",
    ]),
    "body-fat-calculator": ("Worked example", [
        "A man 178 cm tall with a 38 cm neck and an 86 cm waist at the navel "
        "(70 in, 15 in and 33.9 in) weighs 80 kg (176 lb).",
        {"list": [
            "Waist minus neck: 48 cm. log10(48) = 1.681",
            "log10(178) = 2.250",
            "Body fat: 495 / (1.0324 - 0.19077 x 1.681 + 0.15456 x 2.250) - "
            "450 = about 17%",
            "Fat mass: 80 x 0.17 = 13.6 kg. Lean mass: 66.4 kg",
        ]},
        "That puts him at the top of the fitness category. If his waist "
        "drops by 4 cm over a cut while his neck stays the same, his "
        "estimate falls to about 14%, which shows how strongly the method "
        "responds to waist size.",
        "That sensitivity is both its weakness and its strength. A careless "
        "measurement throws the result off, but a consistent one tracks "
        "real fat loss from the place most people store it.",
    ]),
    "one-rep-max-calculator": ("Planning training from your 1RM", [
        "Once you have an estimate, use it to set working weights rather "
        "than guessing each session. A common approach for a strength block "
        "is to start at about 75% for sets of 5 and add 2.5% each week until "
        "sets feel very hard, then reset slightly higher.",
        "Many lifters now combine percentages with RPE, a 1 to 10 rating of "
        "effort where 10 means no reps left. A set of 5 at RPE 8 means you "
        "could have done 2 more. If 80% feels like RPE 9 on a bad day, drop "
        "the weight a little; if it feels like RPE 6, your max has probably "
        "gone up.",
        "Base percentages on a training max of about 90% of your estimated "
        "1RM if you are unsure. It leaves room for bad days and makes it "
        "easier to keep adding weight for longer before stalling, which is "
        "the approach behind several popular programs.",
        "Re-estimate every four to eight weeks from a hard set of 3 to 5. "
        "If the number keeps rising, the program is working. If it stalls "
        "for two cycles, look at sleep, food and total volume before "
        "changing everything.",
    ]),
    "ideal-weight-calculator": ("How to use these numbers sensibly", [
        "Think of the results as a band rather than a target. The lowest and "
        "highest of the four formulas, together with the healthy BMI range, "
        "frame where most people of average build and your height feel and "
        "function well.",
        "If you are well above that band and do not lift, it is a fair sign "
        "that some fat loss would benefit your health. Losing even 5 to 10% "
        "of your body weight improves blood pressure, blood sugar and "
        "cholesterol for many people, long before you reach any formula's "
        "number.",
        "If you are below the band, especially below the BMI range, and "
        "have lost weight without trying, speak to a doctor. Unintended "
        "weight loss can have medical causes worth ruling out.",
        "For most people, the more useful goals are behaviours rather than "
        "a number: training three or four times a week, eating enough "
        "protein, walking daily and sleeping seven or more hours. Weight "
        "tends to settle somewhere healthy when those are in place.",
    ]),
}

for _slug, _section in _EXTRA.items():
    CONTENT[_slug]["body"].insert(-1, _section)
