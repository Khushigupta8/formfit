"""
Exercise library. One dict per exercise, rendered at /exercises/<slug>.

Each entry carries the how-to (steps, cues, mistakes), programming ranges and
a few longer sections in the shared body block format. Add a dict and the page,
its sitemap entry and the hub listing appear on the next build.
"""

EXERCISES = [
    {
        "slug": "barbell-back-squat",
        "name": "Barbell Back Squat",
        "title": "Barbell Back Squat: Form, Muscles Worked & Mistakes",
        "desc": ("How to barbell back squat with good form: setup, depth, bracing, "
                 "the muscles it trains, common mistakes and exactly how many sets "
                 "and reps to do."),
        "muscle": "Legs",
        "secondary": ["Glutes", "Adductors", "Lower back", "Core"],
        "equipment": "Barbell, squat rack",
        "level": "Intermediate",
        "image": "squat",
        "intro": ("The back squat is the most direct way to build strong legs with "
                  "a barbell. It loads the quads, glutes and adductors through a "
                  "long range of motion and teaches you to brace your whole trunk "
                  "under weight."),
        "steps": [
            "Set the bar in the rack at roughly mid-chest height, so you can "
            "unrack it with a slight knee bend rather than on your toes.",
            "Step under the bar and place it on your upper traps (high bar) or "
            "a few centimetres lower across the rear delts (low bar). Grip just "
            "outside your shoulders and pull your elbows down.",
            "Stand up to unrack, take two or three short steps back, and set "
            "your feet about shoulder width with toes turned out 15 to 30 degrees.",
            "Take a big breath into your belly, brace as if you are about to be "
            "punched, and hold that air.",
            "Break at the hips and knees together. Let your knees travel forward "
            "and out in line with your toes as you sit down between your heels.",
            "Descend until your hip crease is at or just below the top of your "
            "knee, keeping the bar over the middle of your foot.",
            "Drive up through the whole foot, pushing your knees out and leading "
            "with your chest, until you are standing tall. Breathe out at the "
            "top, re-brace, and repeat.",
        ],
        "cues": [
            "Bar over mid-foot the whole rep",
            "Knees follow the toes",
            "Brace before you descend, not during",
            "Chest and hips rise together",
        ],
        "mistakes": [
            ("Knees caving inward on the way up",
             "Drop the load, cue \"spread the floor\" with your feet, and add "
             "glute work such as hip thrusts."),
            ("Hips shooting up first so the squat becomes a good morning",
             "Lead with your upper back into the bar out of the hole and "
             "strengthen your quads with pauses or front squats."),
            ("Cutting depth as the weight gets heavier",
             "Film from the side. If your hip crease stops above the knee, the "
             "weight is too heavy for full range."),
            ("Heels lifting off the floor",
             "Widen your stance slightly, work on ankle mobility, or try "
             "weightlifting shoes with a raised heel."),
            ("Losing your breath halfway down",
             "Take the breath and brace at the top, hold it for the whole rep, "
             "and only exhale once you are standing again."),
        ],
        "variations": [
            ("Front squat", "Bar in front of the shoulders; more upright torso and "
             "more quad emphasis."),
            ("Goblet squat", "A dumbbell or kettlebell held at the chest, the best "
             "way for beginners to learn the pattern."),
            ("Box squat", "Sitting back to a box teaches depth and hip drive."),
            ("Pause squat", "A two-second pause at the bottom builds strength out "
             "of the hole."),
            ("Safety bar squat", "Easier on cranky shoulders and elbows."),
        ],
        "programming": {
            "strength": "3-5 sets of 3-6 reps, 3-5 minutes rest",
            "hypertrophy": "3-4 sets of 6-12 reps, 2-3 minutes rest",
            "beginner": "3 sets of 5 reps, adding 2.5 kg (5 lb) per session",
        },
        "body": [
            ("Muscles worked", [
                "The squat is a quad exercise first. Your quadriceps straighten "
                "the knee and do most of the work out of the bottom position, "
                "which is why deep squats build the front of the thigh so well.",
                "Your <strong>glutes</strong> and <strong>adductors</strong> "
                "(inner thigh) extend the hip, and they work hardest in the "
                "deepest part of the squat. The hamstrings act more as "
                "stabilisers than movers, because they lengthen at the hip as "
                "they shorten at the knee.",
                "Your spinal erectors and abdominals hold your torso rigid so "
                "force goes into the bar rather than leaking through a bending "
                "spine. A heavy squat is a serious core exercise even though "
                "nothing about the trunk moves.",
            ]),
            ("Why it is worth learning", [
                "Few lifts let you load the legs this heavily through this much "
                "range. That makes the squat an efficient builder of both "
                "strength and muscle, and it carries over to jumping, sprinting "
                "and getting off the floor as you age.",
                "It is also easy to measure. Adding weight to the bar is the "
                "simplest form of <a href=\"/guides/progressive-overload-explained\">"
                "progressive overload</a>, and you can track your estimated max "
                "with the <a href=\"/one-rep-max-calculator\">one rep max "
                "calculator</a>.",
            ]),
            ("Safety and who should modify it", [
                "Always squat in a rack with the safety arms set just below your "
                "bottom position, so a failed rep can be dumped onto the pins.",
                "If you have knee, hip or back pain, start with a goblet squat or "
                "a <a href=\"/exercises/leg-press\">leg press</a> to a pain-free "
                "depth and progress from there. Anyone with a diagnosed spinal "
                "condition should get clearance from a physiotherapist or doctor "
                "before loading a bar on their back.",
            ]),
        ],
        "faq": [
            ("How deep should I squat?",
             "Aim for your hip crease to reach at least the top of your knee, "
             "which is called parallel. Going deeper is fine and trains the glutes "
             "more, as long as your lower back stays neutral and your heels stay "
             "down."),
            ("Is it bad for your knees to go past your toes?",
             "No. Your knees need to travel forward for you to squat deep with an "
             "upright torso. What matters is that they track in line with your "
             "toes and do not cave inward."),
            ("Should I wear a belt?",
             "A belt is not required, but it helps many lifters brace harder on "
             "heavy sets. Learn to brace without one first, then use it for work "
             "sets near your limit."),
            ("High bar or low bar?",
             "High bar keeps you more upright and hits the quads harder. Low bar "
             "lets most people lift more weight by using more hip. Both are "
             "valid; pick the one that feels better and stick with it."),
        ],
        "related": ["leg-press", "romanian-deadlift", "walking-lunge"],
        "plans": ["5x5-strength-program", "beginner-full-body-workout"],
    },
    {
        "slug": "deadlift",
        "name": "Deadlift",
        "title": "Deadlift: How to Do It, Muscles Worked & Mistakes",
        "desc": ("Learn the conventional barbell deadlift step by step: foot "
                 "position, grip, bracing and lockout, plus the mistakes that hurt "
                 "backs and how to fix them."),
        "muscle": "Back",
        "secondary": ["Glutes", "Hamstrings", "Quads", "Forearms", "Traps"],
        "equipment": "Barbell, plates",
        "level": "Intermediate",
        "image": "deadlift",
        "intro": ("The deadlift is simply picking a loaded bar up off the floor. "
                  "It trains more muscle at once than almost any other lift, "
                  "from your grip to your hamstrings, and it lets most people "
                  "handle the heaviest weights they will ever lift."),
        "steps": [
            "Stand with your mid-foot under the bar, feet about hip width, toes "
            "pointing slightly out. The bar should be over your shoelaces.",
            "Hinge down and grip the bar just outside your legs with a "
            "double overhand grip.",
            "Bend your knees until your shins touch the bar. Do not let the bar "
            "roll forward.",
            "Lift your chest, set your back flat, and pull your shoulders down "
            "as if squeezing oranges in your armpits. This takes the slack out "
            "of the bar.",
            "Take a big breath into your belly and brace hard.",
            "Push the floor away with your legs, keeping the bar dragging up "
            "your shins and thighs. Your hips and shoulders should rise at the "
            "same rate.",
            "Once the bar passes your knees, drive your hips forward to stand "
            "tall. Do not lean back at the top.",
            "Lower the bar by pushing your hips back first, then bending your "
            "knees once it passes them. Reset your brace for each rep.",
        ],
        "cues": [
            "Push the floor away",
            "Bar stays in contact with your legs",
            "Chest up, lats tight",
            "Stand tall, do not lean back",
        ],
        "mistakes": [
            ("Rounding the lower back off the floor",
             "Reduce the weight, set your lats before you pull, and make sure "
             "your hips are not too high at the start."),
            ("The bar drifting away from the body",
             "Keep the bar over mid-foot and think about dragging it up your legs. "
             "Long socks or track pants help."),
            ("Jerking the bar off the floor",
             "Pull the slack out first so you hear the bar click against the "
             "plates, then squeeze it off the ground."),
            ("Hyperextending at lockout",
             "Finish by squeezing your glutes with your ribs down. Standing "
             "straight is the end of the rep."),
            ("Squatting the deadlift with hips too low",
             "Your hips should sit higher than your knees and lower than your "
             "shoulders. Shins only need a slight angle."),
        ],
        "variations": [
            ("Sumo deadlift", "A wide stance and narrow grip; more upright, with "
             "more quad and adductor work."),
            ("Trap bar deadlift", "Handles at your sides make it easier to learn "
             "and gentler on the lower back."),
            ("Romanian deadlift", "Starts from the top and focuses on the "
             "hamstrings and glutes."),
            ("Deficit deadlift", "Standing on a small platform builds speed off "
             "the floor."),
            ("Rack pull", "Pulling from just below the knee overloads the lockout."),
        ],
        "programming": {
            "strength": "1-3 heavy sets of 1-5 reps, 3-5 minutes rest",
            "hypertrophy": "3 sets of 6-8 reps, 3 minutes rest",
            "beginner": "1 work set of 5 reps after warm-ups, adding 5 kg (10 lb) per session",
        },
        "body": [
            ("Muscles worked", [
                "The deadlift is a hip extension exercise. Your <strong>glutes"
                "</strong> and <strong>hamstrings</strong> drive the hips "
                "forward, and your quads straighten the knees off the floor.",
                "Your spinal erectors, lats, traps and rhomboids work "
                "isometrically to keep your back flat and the bar close. Your "
                "forearms and grip hold the whole thing together, which is why "
                "grip often fails before anything else.",
            ]),
            ("Benefits", [
                "Few exercises build total body strength faster. A strong "
                "deadlift transfers directly to everyday tasks like lifting "
                "boxes, children or luggage with a safe, neutral back.",
                "Because it uses so much muscle, it is also demanding. Most "
                "people do best deadlifting heavy once or twice a week rather "
                "than every session, and pairing it with enough "
                "<a href=\"/guides/rest-days-and-recovery\">recovery</a> keeps "
                "progress moving.",
            ]),
            ("Safety and who should modify it", [
                "The deadlift is safe when the weight matches your ability to "
                "hold position. If your back rounds, the load is too heavy, not "
                "the exercise too dangerous.",
                "People with existing back injuries often do better with the trap "
                "bar version or by pulling from blocks to shorten the range. If "
                "you have a disc problem or recent back pain, get assessed by a "
                "physiotherapist before you start.",
            ]),
        ],
        "faq": [
            ("Is the deadlift a back or leg exercise?",
             "Both. The legs and hips produce the movement while the back holds "
             "position. Most programmes count it as a posterior chain or pull "
             "day lift."),
            ("Should I use mixed grip or straps?",
             "Use double overhand for as long as you can to build grip. For heavy "
             "sets, a mixed grip, a hook grip or straps are all fine. If you use "
             "mixed grip, alternate which hand faces up between sessions."),
            ("Should I touch and go or reset each rep?",
             "Resetting each rep (dead stop) builds strength off the floor and "
             "makes it easier to keep good form. Touch and go is fine for higher "
             "rep hypertrophy work if your position stays solid."),
            ("How often should I deadlift?",
             "Once a week is enough for most people, twice if the second session "
             "is lighter or a variation. It is very fatiguing, so more is rarely "
             "better."),
        ],
        "related": ["romanian-deadlift", "barbell-row", "hip-thrust"],
        "plans": ["5x5-strength-program", "upper-lower-split"],
    },
    {
        "slug": "bench-press",
        "name": "Bench Press",
        "title": "Bench Press: Proper Form, Muscles Worked & Mistakes",
        "desc": ("How to bench press safely and press more: setup, grip width, bar "
                 "path, leg drive and the common mistakes that stall progress or "
                 "hurt shoulders."),
        "muscle": "Chest",
        "secondary": ["Front delts", "Triceps", "Lats"],
        "equipment": "Barbell, flat bench, rack",
        "level": "Beginner",
        "image": "bench-press",
        "intro": ("The bench press is the classic upper body strength lift. "
                  "Lying on a bench lets you press heavy loads safely, making it "
                  "one of the best tools for building the chest, front shoulders "
                  "and triceps."),
        "steps": [
            "Lie on the bench with your eyes directly under the bar. Plant your "
            "feet flat on the floor, slightly behind your knees.",
            "Grip the bar slightly wider than shoulder width so your forearms "
            "are vertical when the bar touches your chest.",
            "Squeeze your shoulder blades together and down, and create a small "
            "natural arch in your upper back. Your glutes stay on the bench.",
            "Unrack the bar with straight arms and bring it over your shoulders.",
            "Take a breath and lower the bar under control to your lower chest, "
            "around the nipple line, with elbows tucked about 45 to 70 degrees "
            "from your torso.",
            "Touch the chest lightly without bouncing.",
            "Press up and slightly back toward your face, driving your feet into "
            "the floor, until your arms are straight over your shoulders.",
        ],
        "cues": [
            "Shoulder blades back and down",
            "Bend the bar",
            "Leg drive into the floor",
            "Wrists stacked over elbows",
        ],
        "mistakes": [
            ("Flared elbows at 90 degrees",
             "Tuck the elbows to roughly 45 to 70 degrees. This is stronger and "
             "easier on the shoulder joint."),
            ("Bouncing the bar off the chest",
             "Lower under control and touch. If you need a bounce, the weight is "
             "too heavy."),
            ("Glutes lifting off the bench",
             "Push the floor away toward your head rather than straight down, "
             "and keep your hips in contact."),
            ("Loose upper back",
             "Set your shoulder blades before unracking and keep them pinned "
             "for the whole set."),
            ("Benching heavy with no spotter or safeties",
             "Use safety arms set at chest level or ask for a spot. Never use "
             "collars when benching alone without safeties."),
        ],
        "variations": [
            ("Close grip bench press", "Hands at shoulder width to shift more "
             "work to the triceps."),
            ("Incline bench press", "A 30 degree bench emphasises the upper "
             "chest and front delts."),
            ("Dumbbell bench press", "Each arm works independently and you get "
             "a deeper stretch."),
            ("Paused bench press", "A one-second pause on the chest removes "
             "bounce and builds strength from the bottom."),
        ],
        "programming": {
            "strength": "3-5 sets of 3-6 reps, 3-4 minutes rest",
            "hypertrophy": "3-4 sets of 6-12 reps, 2 minutes rest",
            "beginner": "3 sets of 5 reps, adding 2.5 kg (5 lb) per session",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>pectoralis major</strong> is the main mover. It "
                "brings your upper arm across and toward your body, which is "
                "exactly what pressing the bar up does.",
                "Your <strong>front deltoids</strong> assist through the whole "
                "range and your <strong>triceps</strong> take over near lockout. "
                "Your lats and upper back stabilise the bar and help control "
                "the descent.",
            ]),
            ("Benefits", [
                "The bench press lets you overload the chest more than push-ups "
                "or flyes, which makes it reliable for building size and "
                "strength. It is also easy to progress in small steps, and you "
                "can track your strength with the <a href=\"/one-rep-max-calculator\">"
                "1RM calculator</a>.",
                "Pair it with a pulling movement such as the "
                "<a href=\"/exercises/barbell-row\">barbell row</a> to keep "
                "shoulder health and posture balanced.",
            ]),
            ("Safety and who should modify it", [
                "Most bench press injuries come from failing a rep with no "
                "safeties. Set the rack safety arms just below chest height, or "
                "have a spotter for heavy sets.",
                "If you have shoulder pain, try a slightly narrower grip, a "
                "neutral grip with dumbbells, or a floor press to limit the range. "
                "Persistent pain is worth checking with a physiotherapist.",
            ]),
        ],
        "faq": [
            ("Where should the bar touch my chest?",
             "Usually on the lower half of the chest, around the nipple line or "
             "slightly below. Your forearms should be close to vertical at the "
             "bottom."),
            ("Is arching in the bench press cheating?",
             "A moderate arch with your glutes on the bench is legal in "
             "powerlifting and helps keep the shoulders in a safer position. An "
             "extreme arch is optional and not needed for general training."),
            ("How much should I be able to bench?",
             "It depends on bodyweight, training age and genetics. Compare your "
             "lifts to people of the same bodyweight with the Wilks calculator "
             "rather than to general internet numbers."),
            ("Bench press or dumbbell press for chest growth?",
             "Both work well. Barbells allow heavier loads; dumbbells allow more "
             "range and fix side-to-side imbalances. Many programmes use both."),
        ],
        "related": ["incline-dumbbell-press", "push-up", "tricep-dip"],
        "plans": ["push-pull-legs", "5x5-strength-program"],
    },
    {
        "slug": "overhead-press",
        "name": "Overhead Press",
        "title": "Overhead Press: Form Guide, Muscles Worked & Tips",
        "desc": ("How to overhead press a barbell with good form: grip, bracing, "
                 "bar path and lockout. Learn the muscles it works and the "
                 "mistakes that stall your press."),
        "muscle": "Shoulders",
        "secondary": ["Triceps", "Upper chest", "Upper traps", "Core"],
        "equipment": "Barbell, rack",
        "level": "Intermediate",
        "image": "barbell-rack",
        "intro": ("The standing overhead press drives a barbell from your "
                  "shoulders to arms' length overhead. It builds strong, "
                  "rounded shoulders and tests your full body stability like no "
                  "seated press can."),
        "steps": [
            "Set the bar in a rack at upper chest height. Grip it just outside "
            "shoulder width with the bar resting low in your palms.",
            "Unrack it so it sits on your front delts, elbows slightly in front "
            "of the bar, and step back with feet about hip width.",
            "Squeeze your glutes and brace your abs hard so your ribs stay down.",
            "Move your head back slightly and press the bar straight up past "
            "your face.",
            "As soon as the bar passes your forehead, push your head forward "
            "\"through the window\" so the bar ends over your mid-foot.",
            "Lock your elbows and shrug slightly at the top so the bar sits over "
            "your shoulders and heels.",
            "Lower the bar back to your shoulders under control, moving your head "
            "back again to make room.",
        ],
        "cues": [
            "Squeeze glutes, ribs down",
            "Bar path straight, head moves around it",
            "Push your head through at the top",
            "Wrists stacked over elbows",
        ],
        "mistakes": [
            ("Leaning back to finish the rep",
             "Brace harder, squeeze your glutes, and reduce the weight so you can "
             "press with a stacked torso."),
            ("Pressing the bar forward around the face",
             "Move your head out of the way instead. The bar should travel in a "
             "near vertical line."),
            ("Bent wrists",
             "Grip the bar lower in the palm, close to the heel of your hand, so "
             "your forearm sits directly under it."),
            ("Elbows flared behind the bar at the start",
             "Bring the elbows slightly forward so they are under or in front of "
             "the bar before you press."),
        ],
        "variations": [
            ("Seated dumbbell press", "Back support lets you focus purely on the "
             "shoulders."),
            ("Push press", "A small leg dip and drive lets you handle heavier "
             "loads."),
            ("Landmine press", "An angled bar path that is friendlier for "
             "shoulders with limited mobility."),
            ("Arnold press", "Rotating dumbbells add more front delt range."),
        ],
        "programming": {
            "strength": "3-5 sets of 3-5 reps, 3 minutes rest",
            "hypertrophy": "3-4 sets of 6-10 reps, 2 minutes rest",
            "beginner": "3 sets of 5 reps, adding 1-2.5 kg (2.5-5 lb) per session",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>front and side deltoids</strong> lift the arm "
                "overhead, while the <strong>triceps</strong> straighten the "
                "elbow to finish the rep. The upper traps and serratus anterior "
                "rotate your shoulder blades upward so the joint has room to move.",
                "Standing turns the press into a trunk exercise as well. Your "
                "abs, obliques and glutes stop you from turning the lift into a "
                "standing incline press.",
            ]),
            ("Benefits", [
                "The press builds the shoulders and triceps that make every other "
                "upper body lift stronger, and it improves overhead stability "
                "for sports and daily life.",
                "It progresses slowly, so use small plates. Adding 1 kg per week "
                "is still 50 kg a year. Use the <a href=\"/plate-calculator\">"
                "plate calculator</a> to load the bar quickly.",
            ]),
            ("Safety and who should modify it", [
                "If you cannot raise your arms fully overhead without arching "
                "your lower back, work on thoracic and shoulder mobility and use "
                "landmine presses in the meantime.",
                "People with shoulder impingement or a past rotator cuff injury "
                "should start light, use a neutral grip with dumbbells, and get "
                "advice from a physiotherapist if pain persists.",
            ]),
        ],
        "faq": [
            ("Is overhead pressing bad for your shoulders?",
             "Not for healthy shoulders with good technique. Pressing overhead "
             "strengthens the muscles that support the joint. Pain is a sign to "
             "reduce load or adjust the variation, not to avoid it forever."),
            ("Standing or seated press?",
             "Standing trains more of the body and transfers better to sport. "
             "Seated lets you isolate the shoulders and is useful for "
             "hypertrophy."),
            ("Why is my overhead press so much weaker than my bench?",
             "It uses smaller muscles and you cannot use your legs or a bench for "
             "support. A press around 60 to 70 percent of your bench is typical."),
        ],
        "related": ["bench-press", "incline-dumbbell-press", "tricep-dip"],
        "plans": ["push-pull-legs", "5x5-strength-program"],
    },
    {
        "slug": "barbell-row",
        "name": "Barbell Row",
        "title": "Barbell Row: Form, Muscles Worked & Common Mistakes",
        "desc": ("How to do the bent-over barbell row for a thicker, stronger "
                 "back: torso angle, grip, where to pull the bar, and the "
                 "mistakes that turn it into a shrug."),
        "muscle": "Back",
        "secondary": ["Lats", "Rear delts", "Biceps", "Lower back"],
        "equipment": "Barbell, plates",
        "level": "Intermediate",
        "image": "barbell-rack",
        "intro": ("The bent-over barbell row is the main horizontal pull for "
                  "building back thickness. It balances out pressing work and "
                  "strengthens the hip hinge you use in deadlifts."),
        "steps": [
            "Stand with feet hip width, the bar over your mid-foot, and grip it "
            "slightly wider than shoulder width with palms facing you or down.",
            "Deadlift the bar to standing, then hinge forward by pushing your "
            "hips back with a soft knee bend.",
            "Lower your torso to about 30 to 45 degrees above horizontal. Keep "
            "your back flat and let the bar hang at arm's length below your "
            "shoulders.",
            "Brace your abs and keep your neck in line with your spine.",
            "Pull the bar toward your lower ribs or upper stomach, driving your "
            "elbows back and squeezing your shoulder blades together.",
            "Pause briefly when the bar touches your torso.",
            "Lower the bar under control until your arms are straight, keeping "
            "your torso angle fixed.",
        ],
        "cues": [
            "Elbows to your back pockets",
            "Torso stays still",
            "Squeeze the shoulder blades at the top",
            "Flat back, braced core",
        ],
        "mistakes": [
            ("Standing up more with every rep",
             "Pick a load you can row with a fixed torso angle. If you need to "
             "heave, it is too heavy."),
            ("Rounding the lower back",
             "Brace before each set, keep your chest up, and reduce the weight. "
             "Strengthen the hinge with Romanian deadlifts."),
            ("Pulling with the arms only",
             "Think about driving the elbows back rather than curling the bar. "
             "Your hands are just hooks."),
            ("Shrugging the shoulders toward the ears",
             "Keep the shoulders down and pull back and slightly down, toward "
             "the hips."),
        ],
        "variations": [
            ("Pendlay row", "Each rep starts from the floor with a flat torso, "
             "building explosive pulling power."),
            ("Chest supported row", "Lying face down on an incline bench removes "
             "lower back fatigue."),
            ("One-arm dumbbell row", "Lets you pull through a longer range and "
             "fix imbalances."),
            ("Seated cable row", "Constant tension and an easy way to learn the "
             "pull."),
        ],
        "programming": {
            "strength": "3-5 sets of 5-8 reps, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 8-12 reps, 90-120 seconds rest",
            "beginner": "3 sets of 8 reps with a weight you control fully",
        },
        "body": [
            ("Muscles worked", [
                "Rowing pulls your arms back toward your torso, which works the "
                "<strong>lats</strong>, <strong>rhomboids</strong>, middle "
                "<strong>trapezius</strong> and <strong>rear delts</strong>. "
                "Your biceps and forearms assist the elbow bend.",
                "Holding the bent-over position also makes your spinal erectors, "
                "glutes and hamstrings work hard isometrically, which is why "
                "rows feel taxing on the lower back.",
            ]),
            ("Benefits", [
                "A strong row builds a thick upper back that supports heavy "
                "squats and deadlifts and gives the bench press a stable base. "
                "It also offsets the rounded shoulder posture that comes from "
                "lots of pressing and desk work.",
                "Most balanced programmes include roughly as much rowing as "
                "pressing. The <a href=\"/workouts/upper-lower-split\">upper "
                "lower split</a> pairs them on every upper day.",
            ]),
            ("Safety and who should modify it", [
                "If your lower back gets tired before your upper back, switch to "
                "a chest supported or one-arm dumbbell row. You keep the benefit "
                "for the back muscles without loading the spine.",
                "Anyone with a history of disc problems should start with "
                "supported rows and only add the bent-over version once a "
                "neutral hinge feels comfortable under load.",
            ]),
        ],
        "faq": [
            ("Overhand or underhand grip?",
             "Overhand slightly favours the upper back and rear delts; underhand "
             "brings in more biceps and lats and lets many people lift a little "
             "more. Both are good choices."),
            ("Where should the bar touch?",
             "Around the bottom of your rib cage or upper stomach. Pulling higher "
             "toward the chest shifts work to the upper back and rear delts."),
            ("Is the barbell row better than a cable row?",
             "Not better, different. The barbell row allows heavier loads and "
             "trains the hinge; cable rows are easier to recover from and to do "
             "with strict form."),
        ],
        "related": ["pull-up", "lat-pulldown", "deadlift"],
        "plans": ["5x5-strength-program", "upper-lower-split"],
    },
    {
        "slug": "pull-up",
        "name": "Pull-Up",
        "title": "Pull-Up: How to Do Your First Rep and Get Better",
        "desc": ("How to do a pull-up with good form, the muscles it works, and a "
                 "clear progression to get your first rep and build up to sets of "
                 "ten or more."),
        "muscle": "Back",
        "secondary": ["Lats", "Biceps", "Rear delts", "Forearms", "Core"],
        "equipment": "Pull-up bar",
        "level": "Intermediate",
        "image": "pull-up",
        "intro": ("The pull-up lifts your whole bodyweight from a dead hang to "
                  "chin over the bar. It is one of the best measures of relative "
                  "upper body strength and one of the best back builders you can "
                  "do with almost no equipment."),
        "steps": [
            "Grip the bar with palms facing away, hands slightly wider than "
            "shoulder width.",
            "Hang with arms straight, legs together and slightly in front of you, "
            "and your abs braced so your body does not swing.",
            "Start by pulling your shoulder blades down and back, as if putting "
            "them in your back pockets.",
            "Pull yourself up by driving your elbows down toward your ribs.",
            "Keep pulling until your chin clears the bar and your chest moves "
            "toward it.",
            "Lower yourself under control, taking two to three seconds, until "
            "your arms are fully straight again.",
        ],
        "cues": [
            "Elbows to your ribs",
            "Chest to the bar",
            "No swinging, legs still",
            "Full hang at the bottom",
        ],
        "mistakes": [
            ("Half reps that never reach a dead hang",
             "Straighten your arms fully at the bottom of each rep. Partial range "
             "builds partial strength."),
            ("Kipping or swinging to get up",
             "Brace your core, squeeze your glutes and keep your legs still. "
             "Use bands if you need help."),
            ("Craning the neck to get the chin over",
             "Keep your neck neutral and pull your chest toward the bar instead."),
            ("Dropping quickly on the way down",
             "Control the lowering. The eccentric half builds a lot of strength."),
        ],
        "variations": [
            ("Chin-up", "Palms facing you; more biceps and usually easier."),
            ("Band-assisted pull-up", "A resistance band takes away part of your "
             "bodyweight."),
            ("Negative pull-up", "Jump to the top and lower slowly for 3 to 5 "
             "seconds to build strength for your first rep."),
            ("Weighted pull-up", "Add load with a dip belt once you can do 10 "
             "clean reps."),
            ("Neutral grip pull-up", "Palms facing each other; often the most "
             "comfortable on the shoulders."),
        ],
        "programming": {
            "strength": "4-5 sets of 3-6 reps, weighted if needed, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 6-12 reps, 2 minutes rest",
            "beginner": "3-4 sets of 3-5 slow negatives or band-assisted reps",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>latissimus dorsi</strong> does most of the work, "
                "pulling your upper arms down to your sides. The "
                "<strong>teres major</strong>, lower traps and rhomboids help "
                "control the shoulder blades.",
                "Your biceps and forearms flex the elbow and hold the grip, and "
                "your abs keep your body from swinging.",
            ]),
            ("How to get your first pull-up", [
                "Most people can get their first pull-up within a few months "
                "with consistent practice two or three times a week.",
                {"olist": [
                    "Dead hangs: build to 3 sets of 30 to 45 seconds.",
                    "Scapular pulls: from a hang, pull your shoulder blades down "
                    "without bending your arms, 3 sets of 8.",
                    "Negatives: jump up and lower over 3 to 5 seconds, 3 sets of 5.",
                    "Band-assisted reps or <a href=\"/exercises/lat-pulldown\">lat "
                    "pulldowns</a> for 3 sets of 8 to 10.",
                    "Test a strict rep every couple of weeks.",
                ]},
                "Losing some body fat makes pull-ups easier too, because you are "
                "lifting less weight. Check where you stand with the "
                "<a href=\"/body-fat-calculator\">body fat calculator</a>.",
            ]),
            ("Safety and who should modify it", [
                "If pull-ups irritate your elbows or shoulders, try a neutral "
                "grip, reduce the volume, and avoid kipping. Anyone with a recent "
                "shoulder dislocation should get cleared before hanging from a bar.",
            ]),
        ],
        "faq": [
            ("Pull-up vs chin-up: which is better?",
             "Both train the lats well. Chin-ups use more biceps and are usually "
             "easier. Doing both across a week is a good approach."),
            ("How many pull-ups should I be able to do?",
             "For general fitness, 5 to 10 strict reps is a solid target for most "
             "adults. Many beginners start at zero, which is normal."),
            ("Can I build a big back with only pull-ups?",
             "Pull-ups are excellent, but adding a horizontal row such as the "
             "barbell or dumbbell row gives more complete development."),
        ],
        "related": ["lat-pulldown", "barbell-row", "dumbbell-curl"],
        "plans": ["push-pull-legs", "upper-lower-split"],
    },
    {
        "slug": "push-up",
        "name": "Push-Up",
        "title": "Push-Up: Proper Form, Variations & Progressions",
        "desc": ("How to do a perfect push-up, the muscles it works, and a full "
                 "progression from incline push-ups to harder variations you can "
                 "do anywhere without equipment."),
        "muscle": "Chest",
        "secondary": ["Triceps", "Front delts", "Core", "Serratus anterior"],
        "equipment": "None (bodyweight)",
        "level": "Beginner",
        "image": "push-up",
        "intro": ("The push-up is the most accessible upper body strength "
                  "exercise there is. Done with good form, it trains the chest, "
                  "shoulders, triceps and core together and can be scaled for "
                  "almost anyone."),
        "steps": [
            "Place your hands on the floor slightly wider than shoulder width, "
            "fingers pointing forward.",
            "Step your feet back so your body forms a straight line from head to "
            "heels. Squeeze your glutes and brace your abs.",
            "Lower your chest toward the floor by bending your elbows, keeping "
            "them at about 45 degrees from your body.",
            "Go down until your chest is a fist's width from the floor.",
            "Push the floor away to straighten your arms, keeping your body in "
            "one rigid line.",
            "At the top, push slightly further so your shoulder blades spread "
            "apart, then start the next rep.",
        ],
        "cues": [
            "Body like a plank",
            "Elbows at 45 degrees, not flared",
            "Chest leads, hips follow",
            "Push the floor away",
        ],
        "mistakes": [
            ("Sagging hips",
             "Squeeze your glutes and brace your abs. If you still sag, elevate "
             "your hands on a bench."),
            ("Elbows flared straight out to the sides",
             "Tuck them so your arms form an arrow shape with your body, not a T."),
            ("Tiny range of motion",
             "Lower until your chest nearly touches the floor. Use an easier "
             "variation if you cannot reach full depth."),
            ("Head dropping forward",
             "Keep your neck neutral and look at the floor slightly ahead of "
             "your hands."),
        ],
        "variations": [
            ("Incline push-up", "Hands on a bench or wall to make it easier."),
            ("Knee push-up", "A shorter lever for building toward full reps."),
            ("Decline push-up", "Feet raised to emphasise the upper chest and "
             "shoulders."),
            ("Diamond push-up", "Hands close together for more triceps."),
            ("Deficit or weighted push-up", "Hands on blocks or a plate on your "
             "back to keep progressing."),
        ],
        "programming": {
            "strength": "4-5 sets of 5-10 reps of a hard variation",
            "hypertrophy": "3-4 sets of 10-25 reps, stopping 1-3 reps short of failure",
            "beginner": "3 sets of 5-10 incline or knee push-ups",
        },
        "body": [
            ("Muscles worked", [
                "Like the <a href=\"/exercises/bench-press\">bench press</a>, the "
                "push-up is driven by the <strong>pectoralis major</strong>, "
                "<strong>front delts</strong> and <strong>triceps</strong>.",
                "Unlike the bench, your shoulder blades are free to move, so the "
                "serratus anterior works too, and holding a rigid plank turns "
                "it into a core exercise.",
            ]),
            ("Benefits", [
                "Push-ups need no equipment, so they fit into "
                "<a href=\"/workouts/home-dumbbell-workout\">home workouts</a>, "
                "travel days and warm-ups. Studies comparing push-ups and bench "
                "presses at similar effort have found similar muscle gains, so "
                "they are far more than a warm-up exercise.",
                "They are also a simple fitness test. Tracking how many clean "
                "reps you can do is an easy way to see progress.",
            ]),
            ("Safety and who should modify it", [
                "If your wrists hurt, use push-up handles or dumbbells to keep "
                "your wrists straight, or do them on your fists. Shoulder pain "
                "often improves when you tuck your elbows more.",
            ]),
        ],
        "faq": [
            ("How many push-ups should I do a day?",
             "There is no magic number. Two or three hard sets a few times a week "
             "is more effective than hundreds of sloppy reps every day."),
            ("Do push-ups build muscle?",
             "Yes, especially for beginners and when taken close to failure. As "
             "you get stronger, harder variations or added weight keep them "
             "challenging."),
            ("Are knee push-ups worth doing?",
             "Yes. They train the same muscles with less load and are a good "
             "bridge to full push-ups. Keep your body straight from knees to head."),
        ],
        "related": ["bench-press", "tricep-dip", "plank"],
        "plans": ["home-dumbbell-workout", "fat-loss-workout-plan"],
    },
    {
        "slug": "romanian-deadlift",
        "name": "Romanian Deadlift",
        "title": "Romanian Deadlift (RDL): Form, Muscles & Mistakes",
        "desc": ("How to do the Romanian deadlift to build hamstrings and glutes: "
                 "the hip hinge, how low to go, bar path, and how it differs from "
                 "a regular deadlift."),
        "muscle": "Legs",
        "secondary": ["Hamstrings", "Glutes", "Lower back", "Forearms"],
        "equipment": "Barbell or dumbbells",
        "level": "Intermediate",
        "image": "deadlift",
        "intro": ("The Romanian deadlift, or RDL, is a hip hinge that starts "
                  "from the top and stretches the hamstrings under load. It is "
                  "one of the most effective exercises for the back of the "
                  "thighs and glutes."),
        "steps": [
            "Stand tall holding the bar at hip height with an overhand grip just "
            "outside your thighs, feet about hip width.",
            "Unlock your knees slightly and keep that bend fixed for the whole set.",
            "Push your hips straight back as if closing a car door with your "
            "backside. Your torso tips forward as a result.",
            "Let the bar slide down your thighs, staying in contact with your legs.",
            "Keep your back flat and lower until you feel a strong hamstring "
            "stretch, usually around mid-shin or just below the knee.",
            "Drive your hips forward to return to standing, squeezing your glutes "
            "at the top without leaning back.",
        ],
        "cues": [
            "Hips back, not down",
            "Bar close to your legs",
            "Soft knees, fixed angle",
            "Stop when the hips stop",
        ],
        "mistakes": [
            ("Squatting the movement by bending the knees more",
             "Keep the knee bend constant and think about pushing the hips back "
             "toward the wall behind you."),
            ("Rounding the back to reach lower",
             "Your range ends when your hips stop moving back. Going lower by "
             "rounding moves the load onto the spine."),
            ("Letting the bar drift forward",
             "Drag the bar down your thighs. Engaging your lats helps keep it close."),
            ("Hyperextending at the top",
             "Finish standing straight with glutes squeezed and ribs down."),
        ],
        "variations": [
            ("Dumbbell RDL", "Easier to learn and good for home training."),
            ("Single-leg RDL", "Trains balance and each side independently."),
            ("Stiff-leg deadlift", "Starts from the floor each rep with straighter "
             "legs."),
            ("Good morning", "A bar on the back instead of in the hands."),
        ],
        "programming": {
            "strength": "3-4 sets of 5-8 reps, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 8-12 reps, 2 minutes rest",
            "beginner": "3 sets of 10 with dumbbells or a light bar",
        },
        "body": [
            ("Muscles worked", [
                "The RDL trains the <strong>hamstrings</strong> at long muscle "
                "lengths, which research suggests is especially effective for "
                "growth. The <strong>glutes</strong> extend the hip alongside them.",
                "Your spinal erectors hold your back flat, and your grip and "
                "upper back keep the bar close.",
            ]),
            ("RDL vs conventional deadlift", [
                {"table": {
                    "head": ["", "Romanian deadlift", "Conventional deadlift"],
                    "rows": [
                        ["Starts from", "Standing, top position", "The floor"],
                        ["Knee bend", "Slight and fixed", "Bends and straightens"],
                        ["Main target", "Hamstrings and glutes", "Whole posterior chain and quads"],
                        ["Typical load", "Lighter", "Heavier"],
                    ],
                }},
                "Many lifters use the <a href=\"/exercises/deadlift\">deadlift</a> "
                "as a strength lift and the RDL as a muscle building accessory.",
            ]),
            ("Safety and who should modify it", [
                "Start light, because the stretch makes the hamstrings very sore "
                "for the first week or two. People with lower back problems often "
                "tolerate single-leg dumbbell versions better.",
            ]),
        ],
        "faq": [
            ("How low should I go in an RDL?",
             "As low as you can while your back stays flat and your hips keep "
             "moving back. For most people that is mid-shin to just below the knee."),
            ("Should I feel RDLs in my lower back?",
             "You will feel your back working to hold position, but the main "
             "sensation should be in the hamstrings. Sharp or growing lower back "
             "pain means stop and reduce the load."),
            ("Can I do RDLs and squats on the same day?",
             "Yes. Many leg days pair a squat with an RDL so both the front and "
             "back of the thighs are trained."),
        ],
        "related": ["deadlift", "hip-thrust", "barbell-back-squat"],
        "plans": ["push-pull-legs", "upper-lower-split"],
    },
    {
        "slug": "hip-thrust",
        "name": "Hip Thrust",
        "title": "Barbell Hip Thrust: Form, Setup & Glute Tips",
        "desc": ("How to do the barbell hip thrust for stronger glutes: bench "
                 "height, foot position, padding the bar, and the mistakes that "
                 "move the work into your lower back."),
        "muscle": "Glutes",
        "secondary": ["Hamstrings", "Quads", "Adductors", "Core"],
        "equipment": "Barbell, bench, bar pad",
        "level": "Beginner",
        "image": "woman-lifting",
        "intro": ("The hip thrust loads the glutes directly in their strongest, "
                  "most shortened position. It is easy to learn, easy to load "
                  "heavily and one of the best isolation-style exercises for "
                  "glute size and strength."),
        "steps": [
            "Sit on the floor with your upper back against the edge of a bench, "
            "roughly at the bottom of your shoulder blades.",
            "Roll a padded barbell over your legs until it sits in the crease of "
            "your hips.",
            "Plant your feet flat, about hip width, so that at the top your shins "
            "will be vertical.",
            "Tuck your chin slightly and brace your abs so your ribs stay down.",
            "Drive through your heels and squeeze your glutes to lift your hips "
            "until your torso is parallel to the floor.",
            "Pause for a second at the top with your glutes fully contracted.",
            "Lower your hips under control until they are just above the floor, "
            "then repeat.",
        ],
        "cues": [
            "Chin tucked, eyes forward",
            "Ribs down, pelvis tucked at the top",
            "Shins vertical at lockout",
            "Push through the heels",
        ],
        "mistakes": [
            ("Arching the lower back at the top",
             "Finish with a slight posterior pelvic tilt and ribs down. The "
             "movement stops when your hips are fully extended."),
            ("Feet too far forward or too close",
             "Feet too far forward shifts work to the hamstrings, too close to "
             "the quads. Adjust until your shins are vertical at the top."),
            ("Head thrown back, looking at the ceiling",
             "Keep your gaze forward and let your torso pivot around the bench."),
            ("Skipping the pause",
             "Hold the top for one to two seconds. That is where the glutes work "
             "hardest."),
        ],
        "variations": [
            ("Glute bridge", "Done from the floor with a shorter range; good for "
             "beginners and home training."),
            ("Single-leg hip thrust", "Bodyweight or light load, one side at a time."),
            ("Machine hip thrust", "Faster setup and easier to load."),
            ("Banded hip thrust", "A band around the knees adds more glute med work."),
        ],
        "programming": {
            "strength": "3-4 sets of 5-8 reps, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 8-15 reps, 90 seconds rest",
            "beginner": "3 sets of 10-12 glute bridges, then progress to the bench",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>gluteus maximus</strong> is the prime mover, "
                "extending the hip against the bar. Muscle activity studies "
                "consistently show high glute activation in the hip thrust, "
                "peaking at the top of the rep.",
                "The hamstrings, quads and adductors assist, and the abs hold "
                "your pelvis in position.",
            ]),
            ("Benefits", [
                "Because the hip thrust places little load on the spine and "
                "needs almost no technique, you can train it close to failure "
                "safely. That makes it an efficient accessory alongside "
                "<a href=\"/exercises/barbell-back-squat\">squats</a> and "
                "<a href=\"/exercises/romanian-deadlift\">RDLs</a>, which load "
                "the glutes in a stretched position.",
                "Stronger glutes support sprinting, jumping and a healthy lower "
                "back.",
            ]),
            ("Safety and who should modify it", [
                "Always use a bar pad or folded mat across your hips. If the "
                "bench slides, put it against a wall. Anyone with hip pain can "
                "start with bodyweight glute bridges and progress gradually.",
            ]),
        ],
        "faq": [
            ("Hip thrust or squat for glutes?",
             "Use both. Squats load the glutes in a deep stretch, hip thrusts in "
             "a full contraction. Together they cover the whole range."),
            ("How high should the bench be?",
             "Around 40 to 45 cm (16 to 18 in) works for most people. The edge "
             "should sit just below your shoulder blades."),
            ("Why do I feel hip thrusts in my hamstrings?",
             "Your feet are probably too far from your body. Bring them closer "
             "until your shins are vertical at the top."),
        ],
        "related": ["romanian-deadlift", "walking-lunge", "barbell-back-squat"],
        "plans": ["upper-lower-split", "fat-loss-workout-plan"],
    },
    {
        "slug": "walking-lunge",
        "name": "Walking Lunge",
        "title": "Walking Lunge: How to Do It, Muscles & Mistakes",
        "desc": ("How to do walking lunges with dumbbells or bodyweight: step "
                 "length, knee position and torso angle, plus the muscles they "
                 "train and how to program them."),
        "muscle": "Legs",
        "secondary": ["Glutes", "Adductors", "Hamstrings", "Calves", "Core"],
        "equipment": "Dumbbells or bodyweight",
        "level": "Beginner",
        "image": "home-workout",
        "intro": ("The walking lunge is a single-leg exercise that builds the "
                  "quads and glutes while challenging your balance. It exposes "
                  "and fixes left to right differences that two-legged lifts "
                  "can hide."),
        "steps": [
            "Stand tall holding a dumbbell in each hand at your sides, or with "
            "your hands on your hips for bodyweight lunges.",
            "Take a long step forward with one leg, landing heel first.",
            "Lower your back knee toward the floor until it almost touches, "
            "with your front shin roughly vertical.",
            "Keep your torso upright or leaning slightly forward and your front "
            "knee tracking over your toes.",
            "Push through your front foot to stand up and bring your back leg "
            "forward into the next step.",
            "Alternate legs as you walk, taking 8 to 12 steps per leg.",
        ],
        "cues": [
            "Long step, soft landing",
            "Back knee kisses the floor",
            "Front knee over the toes",
            "Tall chest",
        ],
        "mistakes": [
            ("Steps too short, so the front knee shoots forward",
             "Lengthen your stride so both knees bend to about 90 degrees at "
             "the bottom."),
            ("Front knee caving inward",
             "Push the knee out over your middle toes and slow down."),
            ("Walking on a tightrope",
             "Keep your feet hip width apart side to side, as if on train tracks."),
            ("Slamming the back knee into the floor",
             "Control the descent and stop just short of the floor."),
        ],
        "variations": [
            ("Reverse lunge", "Stepping backward is easier on the knees."),
            ("Bulgarian split squat", "Back foot on a bench for a deeper, harder "
             "single-leg squat."),
            ("Barbell walking lunge", "Allows heavier loading for strong lifters."),
            ("Stationary split squat", "Same pattern without walking, ideal for "
             "small spaces."),
        ],
        "programming": {
            "strength": "3-4 sets of 6-8 steps per leg, heavy dumbbells",
            "hypertrophy": "3 sets of 10-12 steps per leg, 90 seconds rest",
            "beginner": "2-3 sets of 8 bodyweight steps per leg",
        },
        "body": [
            ("Muscles worked", [
                "The front leg's <strong>quadriceps</strong> and "
                "<strong>glutes</strong> do most of the work, with the "
                "adductors and hamstrings helping to stabilise the hip.",
                "Balancing on a narrow base makes the glute medius and core work "
                "harder than in a squat, and the calves stabilise each landing.",
            ]),
            ("Benefits", [
                "Single-leg training transfers well to running and sport, and it "
                "lets you work the legs hard with lighter weights. That makes "
                "lunges ideal for <a href=\"/workouts/home-dumbbell-workout\">home "
                "workouts</a> and for people whose backs do not like heavy "
                "barbells.",
                "Walking lunges are also demanding on the heart and lungs, which "
                "is why they appear in many <a href=\"/workouts/fat-loss-workout-plan\">"
                "fat loss circuits</a>.",
            ]),
            ("Safety and who should modify it", [
                "If you have knee pain, switch to reverse lunges, shorten the "
                "range, or hold onto something for balance. Poor balance is "
                "common at first and improves quickly.",
            ]),
        ],
        "faq": [
            ("Are lunges better than squats?",
             "Neither is better. Squats allow heavier loads; lunges add balance "
             "and single-leg strength. Most programmes benefit from both."),
            ("Should I lean forward in a lunge?",
             "A slight forward lean puts more work on the glutes; a very upright "
             "torso shifts it toward the quads. Both are fine if your back stays "
             "neutral."),
            ("How long should my steps be?",
             "Long enough that both knees reach about 90 degrees at the bottom. "
             "For most adults that is roughly 60 to 90 cm (2 to 3 ft)."),
        ],
        "related": ["barbell-back-squat", "hip-thrust", "leg-press"],
        "plans": ["home-dumbbell-workout", "fat-loss-workout-plan"],
    },
    {
        "slug": "lat-pulldown",
        "name": "Lat Pulldown",
        "title": "Lat Pulldown: Proper Form, Grip & Mistakes",
        "desc": ("How to do the lat pulldown correctly for a wider back: grip "
                 "width, how far to lean, where to pull the bar, and how to use "
                 "it to work toward pull-ups."),
        "muscle": "Back",
        "secondary": ["Lats", "Biceps", "Rear delts", "Lower traps"],
        "equipment": "Cable pulldown machine",
        "level": "Beginner",
        "image": "gym-floor",
        "intro": ("The lat pulldown is a machine version of the pull-up that "
                  "lets you choose the load. It is the go-to exercise for "
                  "building the lats when you cannot yet do pull-ups or want "
                  "extra back volume."),
        "steps": [
            "Adjust the thigh pad so your legs are locked in snugly with feet "
            "flat on the floor.",
            "Grip the bar slightly wider than shoulder width with palms facing away.",
            "Sit down with arms fully extended overhead and lean back slightly, "
            "about 10 to 20 degrees.",
            "Pull your shoulder blades down first, then drive your elbows down "
            "toward your sides.",
            "Bring the bar to your upper chest, just below your collarbone.",
            "Squeeze your back briefly, then let the bar rise under control until "
            "your arms are straight and you feel a stretch in your lats.",
        ],
        "cues": [
            "Elbows down to your pockets",
            "Chest up to meet the bar",
            "Control the way up",
            "Slight lean, no swinging",
        ],
        "mistakes": [
            ("Leaning back and yanking the weight",
             "Keep a fixed, slight lean and use a weight you can pull without "
             "rocking your torso."),
            ("Pulling the bar behind the neck",
             "Pull to the front of your chest. Behind-the-neck pulldowns stress "
             "the shoulder joint for no added benefit."),
            ("Stopping short at the top",
             "Let your arms straighten fully so the lats get a full stretch."),
            ("Pulling with the biceps",
             "Think of your hands as hooks and drive with the elbows."),
        ],
        "variations": [
            ("Close neutral grip pulldown", "A V-handle; usually allows heavier "
             "loads with comfortable shoulders."),
            ("Underhand pulldown", "More biceps and lower lat involvement."),
            ("Single-arm cable pulldown", "Fixes imbalances and increases range."),
            ("Straight-arm pulldown", "Isolates the lats without elbow bending."),
        ],
        "programming": {
            "strength": "4 sets of 6-8 reps, 2 minutes rest",
            "hypertrophy": "3-4 sets of 8-15 reps, 90 seconds rest",
            "beginner": "3 sets of 10-12 reps with a controlled tempo",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>latissimus dorsi</strong> pulls the upper arm down "
                "and back, assisted by the <strong>teres major</strong>, lower "
                "traps and rhomboids. The biceps and forearms bend the elbow.",
            ]),
            ("Benefits", [
                "Because you set the load, pulldowns let beginners train the same "
                "pattern as a <a href=\"/exercises/pull-up\">pull-up</a> long "
                "before they can lift their bodyweight. They also make it easy "
                "to add back volume late in a session when you are tired.",
                "Build toward pulling roughly your bodyweight for 8 reps and a "
                "strict pull-up is usually close.",
            ]),
            ("Safety and who should modify it", [
                "The pulldown is very joint friendly. If your shoulders feel "
                "pinched, use a neutral grip and avoid pulling the bar lower than "
                "your upper chest.",
            ]),
        ],
        "faq": [
            ("Is the lat pulldown as good as pull-ups?",
             "For muscle growth it is very similar. Pull-ups add more core work "
             "and are a better test of strength relative to bodyweight."),
            ("Wide grip or close grip?",
             "A grip slightly wider than shoulders suits most people. Very wide "
             "grips shorten the range and do not build a wider back."),
            ("Should I lean back?",
             "Slightly, about 10 to 20 degrees, so the bar clears your face. "
             "Leaning far back turns it into a row."),
        ],
        "related": ["pull-up", "barbell-row", "dumbbell-curl"],
        "plans": ["push-pull-legs", "beginner-full-body-workout"],
    },
    {
        "slug": "dumbbell-curl",
        "name": "Dumbbell Curl",
        "title": "Dumbbell Curl: Form, Biceps Tips & Variations",
        "desc": ("How to do dumbbell bicep curls properly for bigger arms: elbow "
                 "position, tempo, supination, and the swinging mistake that "
                 "steals most of the work."),
        "muscle": "Arms",
        "secondary": ["Brachialis", "Brachioradialis", "Forearms"],
        "equipment": "Dumbbells",
        "level": "Beginner",
        "image": "dumbbells",
        "intro": ("The dumbbell curl is the simplest way to train the biceps "
                  "directly. Strict reps with a full range of motion build the "
                  "front of the upper arm more than any amount of heavy swinging."),
        "steps": [
            "Stand tall holding a dumbbell in each hand at your sides, palms "
            "facing your thighs.",
            "Pin your elbows lightly to your sides and brace your abs.",
            "Curl one or both dumbbells up, turning your palms to face the ceiling "
            "as they rise.",
            "Keep your upper arms still and lift until the dumbbells are near "
            "your shoulders.",
            "Squeeze the biceps for a moment at the top.",
            "Lower slowly over two to three seconds until your arms are fully "
            "straight.",
        ],
        "cues": [
            "Elbows stay by your sides",
            "Turn the pinky up",
            "Slow on the way down",
            "Full stretch at the bottom",
        ],
        "mistakes": [
            ("Swinging the torso to lift the weight",
             "Use a lighter dumbbell or brace against a wall so only your elbows move."),
            ("Elbows drifting forward",
             "Keep the upper arm close to vertical. Forward elbows let the front "
             "delts take over."),
            ("Half reps",
             "Lower until your arms are straight. The stretched part of the curl "
             "matters for growth."),
            ("Dropping the weight on the way down",
             "Control the lowering; it should take longer than the lift."),
        ],
        "variations": [
            ("Hammer curl", "Palms facing each other to target the brachialis "
             "and forearms."),
            ("Incline dumbbell curl", "Lying back on an incline bench stretches "
             "the long head of the biceps."),
            ("Preacher curl", "Arms supported on a pad prevents cheating."),
            ("Barbell curl", "Lets you load both arms more heavily."),
        ],
        "programming": {
            "strength": "3 sets of 6-8 reps, 90 seconds rest",
            "hypertrophy": "3-4 sets of 8-15 reps, 60-90 seconds rest",
            "beginner": "2-3 sets of 10-12 reps per arm",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>biceps brachii</strong> bends the elbow and turns the "
                "palm up, which is why twisting the dumbbell as you curl increases "
                "its involvement. The <strong>brachialis</strong> sits underneath "
                "and adds thickness, and the brachioradialis in the forearm assists.",
            ]),
            ("Benefits", [
                "Compound pulls like <a href=\"/exercises/pull-up\">pull-ups</a> "
                "and <a href=\"/exercises/barbell-row\">rows</a> train the biceps "
                "too, but direct curls add volume that most people need for "
                "visibly bigger arms. A few hard sets twice a week is enough.",
                "Strong biceps and elbow flexors also help protect the elbow "
                "during heavy pulling.",
            ]),
            ("Safety and who should modify it", [
                "Curls are low risk. If your wrists or elbows ache, try hammer "
                "curls or an EZ-bar, which put the joints in a more natural "
                "position.",
            ]),
        ],
        "faq": [
            ("Alternating or both arms together?",
             "Both work. Alternating lets you focus on one arm at a time; "
             "together saves time. Use whichever lets you keep strict form."),
            ("How heavy should my curls be?",
             "Heavy enough that the last two or three reps of each set are hard, "
             "but light enough that you can keep your elbows still."),
            ("How often should I train biceps?",
             "Two sessions a week with 6 to 10 total hard sets, counting rows and "
             "pull-ups partially, is plenty for most people."),
        ],
        "related": ["pull-up", "lat-pulldown", "tricep-dip"],
        "plans": ["push-pull-legs", "home-dumbbell-workout"],
    },
    {
        "slug": "tricep-dip",
        "name": "Tricep Dip",
        "title": "Tricep Dips: Form, Muscles Worked & Safe Depth",
        "desc": ("How to do parallel bar and bench dips for stronger triceps and "
                 "chest: body angle, safe depth for your shoulders, and how to "
                 "progress to weighted."),
        "muscle": "Arms",
        "secondary": ["Chest", "Front delts"],
        "equipment": "Parallel bars or dip station",
        "level": "Intermediate",
        "image": "gym-floor",
        "intro": ("Dips lower and lift your bodyweight between two bars. Kept "
                  "upright, they are one of the best compound exercises for the "
                  "triceps, and with a forward lean they hit the lower chest hard."),
        "steps": [
            "Grip the parallel bars and jump or step up to support yourself with "
            "straight arms, shoulders pushed down away from your ears.",
            "Keep your body fairly upright for triceps focus, legs straight or "
            "knees bent with ankles crossed.",
            "Lower yourself by bending your elbows, keeping them pointing back "
            "rather than flaring out.",
            "Descend until your upper arms are roughly parallel to the floor, or "
            "slightly above if your shoulders feel strained.",
            "Press back up by straightening your arms until your elbows are locked.",
            "Keep your shoulders down throughout; do not let them shrug up at "
            "the bottom.",
        ],
        "cues": [
            "Shoulders down, chest proud",
            "Elbows point back",
            "Controlled depth",
            "Lock out at the top",
        ],
        "mistakes": [
            ("Going far too deep",
             "Stop when your upper arms are about parallel to the floor. Extra "
             "depth stresses the front of the shoulder."),
            ("Shoulders rolling forward and shrugging",
             "Keep your chest up and depress your shoulder blades before each rep."),
            ("Flaring elbows wide",
             "Keep them tracking back and close to your body."),
            ("Kicking the legs to get up",
             "Use a band or assisted dip machine until you can do strict reps."),
        ],
        "variations": [
            ("Bench dip", "Hands on a bench behind you; easier, but limit depth to "
             "protect the shoulders."),
            ("Assisted dip machine", "A counterweight helps you build to bodyweight reps."),
            ("Weighted dip", "Add a dip belt once you can do 12 strict reps."),
            ("Chest dip", "Lean forward and flare the elbows slightly to shift "
             "work to the chest."),
        ],
        "programming": {
            "strength": "4 sets of 5-8 weighted reps, 2-3 minutes rest",
            "hypertrophy": "3 sets of 8-15 reps, 90 seconds rest",
            "beginner": "3 sets of 5-8 assisted or bench dips",
        },
        "body": [
            ("Muscles worked", [
                "All three heads of the <strong>triceps</strong> straighten the "
                "elbow, and dips let them work under your full bodyweight. The "
                "<strong>lower chest</strong> and <strong>front delts</strong> "
                "assist, more so the further you lean forward.",
            ]),
            ("Benefits", [
                "Dips build pressing lockout strength that carries over to the "
                "<a href=\"/exercises/bench-press\">bench press</a> and "
                "<a href=\"/exercises/overhead-press\">overhead press</a>. They "
                "need only a pair of bars and progress easily from assisted to "
                "weighted.",
            ]),
            ("Safety and who should modify it", [
                "Dips place the shoulder in an extended position that some "
                "people do not tolerate. If you feel pain at the front of the "
                "shoulder, reduce depth or swap to close grip bench presses and "
                "cable pushdowns. Bench dips in particular should be kept shallow.",
            ]),
        ],
        "faq": [
            ("Are bench dips safe?",
             "In moderation and with limited depth, yes. Going very deep with "
             "your hands behind you puts a lot of strain on the front of the "
             "shoulder, so stop at about 90 degrees of elbow bend."),
            ("How do I make dips target triceps instead of chest?",
             "Stay upright, keep your elbows close to your body and point them "
             "straight back."),
            ("How many dips should I be able to do?",
             "Ten strict bodyweight dips is a good intermediate benchmark. After "
             "that, adding weight is more useful than chasing high reps."),
        ],
        "related": ["bench-press", "push-up", "overhead-press"],
        "plans": ["push-pull-legs", "upper-lower-split"],
    },
    {
        "slug": "plank",
        "name": "Plank",
        "title": "Plank: Correct Form, Benefits & How Long to Hold",
        "desc": ("How to do a plank properly, how long you really need to hold "
                 "it, the muscles it trains, and harder variations once a basic "
                 "plank becomes too easy."),
        "muscle": "Core",
        "secondary": ["Glutes", "Shoulders", "Obliques"],
        "equipment": "None (bodyweight)",
        "level": "Beginner",
        "image": "stretching",
        "intro": ("The plank trains your core to resist movement, which is what "
                  "it does in most lifts and in daily life. It needs no "
                  "equipment and is a solid foundation for stronger squats, "
                  "deadlifts and presses."),
        "steps": [
            "Kneel and place your forearms on the floor with elbows directly "
            "under your shoulders.",
            "Step your feet back so your body forms a straight line from head to "
            "heels, feet hip width apart.",
            "Squeeze your glutes hard and tuck your pelvis slightly so your lower "
            "back is flat, not arched.",
            "Pull your ribs down toward your hips and brace your abs.",
            "Push the floor away with your forearms so your upper back does not sag.",
            "Breathe steadily and hold for the target time, stopping when your "
            "hips start to drop.",
        ],
        "cues": [
            "Squeeze glutes, tuck pelvis",
            "Ribs down",
            "Push the floor away",
            "Quality over time",
        ],
        "mistakes": [
            ("Hips sagging toward the floor",
             "Squeeze your glutes harder, and end the set once you cannot hold "
             "a straight line."),
            ("Hips piked high in the air",
             "Lower them until you are straight from shoulders to heels."),
            ("Holding your breath",
             "Breathe in short, controlled breaths while keeping your abs tight."),
            ("Chasing minutes of sloppy holding",
             "Several hard 20 to 45 second holds beat one long, relaxed one."),
        ],
        "variations": [
            ("Side plank", "Targets the obliques and the side of the hip."),
            ("RKC plank", "Maximum tension for 10 to 20 seconds; much harder."),
            ("Plank shoulder taps", "Adds anti-rotation challenge."),
            ("Ab wheel rollout", "A dynamic progression for strong cores."),
        ],
        "programming": {
            "strength": "3-4 hard holds of 10-20 seconds (RKC style)",
            "hypertrophy": "3 sets of 30-60 seconds or a harder variation",
            "beginner": "3 sets of 15-30 seconds with perfect alignment",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>rectus abdominis</strong> and "
                "<strong>transverse abdominis</strong> stop your lower back from "
                "arching, the <strong>obliques</strong> stop rotation, and the "
                "glutes hold your pelvis in place. Your shoulders and serratus "
                "work to keep your upper back from sagging.",
            ]),
            ("Benefits and limits", [
                "Planks teach the bracing that protects your spine during "
                "<a href=\"/exercises/deadlift\">deadlifts</a> and "
                "<a href=\"/exercises/barbell-back-squat\">squats</a>. They are "
                "a good starting point for beginners and people returning from "
                "time off.",
                "They will not burn belly fat directly. Fat loss comes from an "
                "overall calorie deficit; see <a href=\"/guides/how-to-lose-belly-fat\">"
                "how to lose belly fat</a> for what actually works.",
                {"tip": "Once you can hold a strict plank for 60 seconds, move to "
                        "a harder variation instead of holding longer."},
            ]),
            ("Safety and who should modify it", [
                "Planks are low risk. People with shoulder pain can do them from "
                "the hands with straight arms or against an incline. During and "
                "after pregnancy, check with your doctor or a pelvic health "
                "physiotherapist about appropriate core training.",
            ]),
        ],
        "faq": [
            ("How long should I hold a plank?",
             "For most people, 20 to 60 seconds of perfect form is enough. Beyond "
             "a minute, harder variations build more strength than longer holds."),
            ("Will planks give me abs?",
             "They strengthen the abs, but visible abs depend mainly on body fat "
             "level, which is driven by diet."),
            ("Can I do planks every day?",
             "Yes, they are low stress. Two to four sessions a week is plenty for "
             "most goals."),
        ],
        "related": ["push-up", "deadlift", "walking-lunge"],
        "plans": ["beginner-full-body-workout", "fat-loss-workout-plan"],
    },
    {
        "slug": "leg-press",
        "name": "Leg Press",
        "title": "Leg Press: Foot Position, Form & Safety Tips",
        "desc": ("How to use the leg press machine safely for bigger quads and "
                 "glutes: foot placement, how deep to go, locking the knees, and "
                 "how it compares with squats."),
        "muscle": "Legs",
        "secondary": ["Glutes", "Adductors", "Hamstrings"],
        "equipment": "Leg press machine",
        "level": "Beginner",
        "image": "gym-floor",
        "intro": ("The leg press lets you load your legs heavily without "
                  "balancing a bar or loading your spine. It is a reliable quad "
                  "and glute builder for beginners and experienced lifters alike."),
        "steps": [
            "Sit in the machine with your back and head flat against the pad.",
            "Place your feet in the middle of the platform, about shoulder width "
            "apart, toes turned out slightly.",
            "Press the platform up and release the safety handles.",
            "Lower the platform by bending your knees toward your chest, keeping "
            "knees in line with your toes.",
            "Go as deep as you can while your lower back and hips stay flat on "
            "the seat.",
            "Push through your whole foot to extend your legs, stopping just "
            "short of locking your knees.",
            "Re-engage the safety handles when the set is done.",
        ],
        "cues": [
            "Lower back glued to the pad",
            "Knees track over toes",
            "Soft knees at the top",
            "Push through the whole foot",
        ],
        "mistakes": [
            ("Lower back and hips rolling off the seat at the bottom",
             "Reduce your depth to the point just before your pelvis tucks under."),
            ("Locking the knees hard at the top",
             "Stop just short of full lockout to keep tension on the muscles and "
             "stress off the joint."),
            ("Loading the machine with more than you can control",
             "Use a weight you can lower for two to three seconds through a full range."),
            ("Pushing through the toes",
             "Keep your heels down; lifting them strains the knees."),
        ],
        "variations": [
            ("High and wide feet", "More glutes and hamstrings."),
            ("Low and narrow feet", "More quads, needs good knee comfort."),
            ("Single-leg press", "Fixes side-to-side imbalances."),
            ("Hack squat", "A machine squat pattern with a back pad."),
        ],
        "programming": {
            "strength": "3-4 sets of 6-8 reps, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 10-15 reps, 2 minutes rest",
            "beginner": "3 sets of 10-12 reps with a controlled tempo",
        },
        "body": [
            ("Muscles worked", [
                "The <strong>quadriceps</strong> do most of the work, with the "
                "<strong>glutes</strong> and <strong>adductors</strong> "
                "contributing more as you go deeper and place your feet higher.",
            ]),
            ("Leg press vs squat", [
                "The leg press removes the need to balance and stabilise, so you "
                "can push your legs closer to failure safely. The "
                "<a href=\"/exercises/barbell-back-squat\">squat</a> trains more "
                "total muscle and core strength.",
                "For muscle growth both work well. Many programmes use the squat "
                "as the main lift and the leg press for extra volume.",
                "The number on a leg press is not comparable to a squat because "
                "of the angle and sled weight, so do not use it to estimate your "
                "squat.",
            ]),
            ("Safety and who should modify it", [
                "Always use the safety stops. If you have knee issues, limit depth "
                "and use a higher foot position. People with lower back problems "
                "often find the leg press a good alternative to squats, provided "
                "the hips stay on the seat.",
            ]),
        ],
        "faq": [
            ("Is the leg press bad for your knees?",
             "No, when used through a comfortable range with knees tracking over "
             "the toes. Avoid snapping the knees into lockout under heavy load."),
            ("How deep should I go on the leg press?",
             "Until your knees reach roughly 90 degrees or deeper, as long as your "
             "lower back stays flat on the pad."),
            ("Does the leg press build glutes?",
             "Yes, especially with a higher foot position and deeper range."),
        ],
        "related": ["barbell-back-squat", "walking-lunge", "romanian-deadlift"],
        "plans": ["push-pull-legs", "upper-lower-split"],
    },
    {
        "slug": "incline-dumbbell-press",
        "name": "Incline Dumbbell Press",
        "title": "Incline Dumbbell Press: Upper Chest Form Guide",
        "desc": ("How to do the incline dumbbell press for a fuller upper chest: "
                 "the best bench angle, elbow position, range of motion, and how "
                 "to get heavy dumbbells in place."),
        "muscle": "Chest",
        "secondary": ["Front delts", "Triceps"],
        "equipment": "Dumbbells, adjustable bench",
        "level": "Beginner",
        "image": "dumbbells",
        "intro": ("The incline dumbbell press shifts pressing work toward the "
                  "upper chest and front shoulders. Dumbbells give you a deeper "
                  "stretch than a barbell and let each side work on its own."),
        "steps": [
            "Set an adjustable bench to about 30 degrees.",
            "Sit with a dumbbell standing on each thigh. Lie back and use your "
            "knees to kick the dumbbells up to your shoulders.",
            "Plant your feet, squeeze your shoulder blades together and keep your "
            "chest up.",
            "Press the dumbbells up over your upper chest until your arms are "
            "straight, bringing them slightly together at the top.",
            "Lower them under control to the sides of your upper chest, elbows "
            "about 45 to 60 degrees from your body.",
            "Feel a stretch across the chest at the bottom, then press up again.",
        ],
        "cues": [
            "Bench at 30 degrees",
            "Shoulder blades pinned",
            "Elbows under the wrists",
            "Deep stretch, smooth press",
        ],
        "mistakes": [
            ("Bench set too steep",
             "Angles of 45 degrees or more turn it into a shoulder press. Around "
             "30 degrees keeps the chest working."),
            ("Dumbbells drifting too wide",
             "Keep your forearms vertical and wrists stacked over elbows."),
            ("Shortening the range",
             "Lower until your elbows are just below the bench line for a full stretch."),
            ("Dropping dumbbells carelessly at the end",
             "Bring them back to your chest, then to your thighs as you sit up."),
        ],
        "variations": [
            ("Incline barbell press", "Allows heavier loading."),
            ("Low incline press", "15 degrees as a middle ground between flat and "
             "incline."),
            ("Incline neutral grip press", "Palms facing each other, easier on "
             "the shoulders."),
            ("Incline cable fly", "An isolation finisher for the upper chest."),
        ],
        "programming": {
            "strength": "3-4 sets of 6-8 reps, 2-3 minutes rest",
            "hypertrophy": "3-4 sets of 8-12 reps, 90-120 seconds rest",
            "beginner": "3 sets of 10 reps with moderate dumbbells",
        },
        "body": [
            ("Muscles worked", [
                "The incline angle increases the work done by the "
                "<strong>clavicular head</strong> of the pectoralis major, the "
                "upper chest. The <strong>front delts</strong> and "
                "<strong>triceps</strong> assist as in all presses.",
            ]),
            ("Benefits", [
                "Most people's upper chest lags behind because flat pressing "
                "favours the middle and lower fibres. Adding incline work "
                "creates a fuller look and balances shoulder development.",
                "Dumbbells also expose strength differences between sides. Pair "
                "it with the <a href=\"/exercises/bench-press\">bench press</a> "
                "in a <a href=\"/workouts/push-pull-legs\">push pull legs</a> "
                "routine for complete chest work.",
            ]),
            ("Safety and who should modify it", [
                "Use a spotter for heavy sets or stop a rep short of failure. If "
                "your shoulders are sensitive, use a neutral grip and do not lower "
                "the dumbbells below the point where you feel strain.",
            ]),
        ],
        "faq": [
            ("What is the best incline angle for upper chest?",
             "Around 30 degrees works well for most people. Steeper angles shift "
             "more work onto the front delts."),
            ("Dumbbell or barbell for incline press?",
             "Dumbbells give more range and balance each side; barbells allow "
             "heavier loads. Both build the upper chest."),
            ("Should the dumbbells touch at the top?",
             "No need. Bringing them close together is fine, but clanking them "
             "adds nothing and can make you lose control."),
        ],
        "related": ["bench-press", "push-up", "overhead-press"],
        "plans": ["push-pull-legs", "home-dumbbell-workout"],
    },
]

BY_SLUG = {e["slug"]: e for e in EXERCISES}

# Photo overrides: the site has a few more photos than the shared key list.
_PHOTOS = {"barbell-row": "rows", "dumbbell-curl": "curl", "tricep-dip": "arms",
           "plank": "core", "lat-pulldown": "bright-gym", "leg-press": "chalk",
           "romanian-deadlift": "plates"}
for _e in EXERCISES:
    _e["image"] = _PHOTOS.get(_e["slug"], _e["image"])

MUSCLES = [m for m in ("Legs", "Glutes", "Chest", "Back", "Shoulders", "Arms", "Core")
           if any(e["muscle"] == m for e in EXERCISES)]
