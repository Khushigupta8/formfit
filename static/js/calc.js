/* FormFit calculators.
 *
 * One form per page, rendered from calculators.py. Values are read and
 * converted to metric (cm, kg) before any maths, so every formula below
 * works in metric only. Nothing is sent anywhere: the only thing stored is
 * the unit preference, in localStorage.
 */
(function () {
  "use strict";

  var tool = document.querySelector(".tool");
  if (!tool) return;
  var form = tool.querySelector("form");
  var out = tool.querySelector(".tool__result");
  var id = tool.getAttribute("data-calc");
  var KEY = "formfit:units";
  var LB = 2.20462, IN = 2.54;

  /* ---------- formatting ---------- */

  function r(n, d) { var p = Math.pow(10, d || 0); return Math.round(n * p) / p; }
  function fmt(n, d) {
    return r(n, d || 0).toLocaleString("en-US", { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 });
  }
  function imperial() { return tool.classList.contains("is-imperial"); }
  function wt(kg, d) { return imperial() ? fmt(kg * LB, d || 0) + " lb" : fmt(kg, d === undefined ? 1 : d) + " kg"; }
  function len(cm) { return imperial() ? fmt(cm / IN, 1) + " in" : fmt(cm, 1) + " cm"; }
  function kcal(n) { return fmt(n) + " kcal"; }

  function big(label, value, unit) {
    return '<p class="result__label">' + label + '</p><p class="result__big">' + value +
      (unit ? "<small>" + unit + "</small>" : "") + "</p>";
  }
  function badge(text, tone) { return '<span class="badge' + (tone ? " badge--" + tone : "") + '">' + text + "</span>"; }
  function rows(list) {
    return '<dl class="rows">' + list.map(function (x) {
      return '<div' + (x[2] ? ' class="is-hl"' : "") + "><dt>" + x[0] + "</dt><dd>" + x[1] + "</dd></div>";
    }).join("") + "</dl>";
  }
  function note(t) { return '<p class="result__note">' + t + "</p>"; }
  function alert(t) { return '<p class="alert">' + t + "</p>"; }
  function gauge(value, min, max, bands, ticks) {
    var pct = Math.max(0, Math.min(100, (value - min) / (max - min) * 100));
    var segs = bands.map(function (b) {
      return '<span style="flex:' + b[0] + ";background:" + b[1] + '"></span>';
    }).join("");
    return '<div class="gauge"><div class="gauge__wrap"><div class="gauge__bar">' + segs +
      '</div><i class="gauge__pin" style="left:' + pct + '%"></i></div><div class="gauge__ticks">' +
      ticks.map(function (t) { return "<span>" + t + "</span>"; }).join("") + "</div></div>";
  }

  /* ---------- reading the form ---------- */

  function num(name) {
    var el = form.elements[name];
    if (!el || el.length) return NaN;
    var v = parseFloat(String(el.value).replace(",", "."));
    return isFinite(v) ? v : NaN;
  }

  function read() {
    var v = {};
    v.sex = (form.querySelector("input[name=sex]:checked") || {}).value || "male";
    var imp = imperial();
    Array.prototype.forEach.call(form.querySelectorAll("input[data-type], select"), function (el) {
      var t = el.getAttribute("data-type"), n = el.name;
      if (el.tagName === "SELECT") { v[n] = el.value; return; }
      if (t === "ft" || t === "in") return;
      var x = num(n);
      if (t === "height") {
        if (imp) {
          var ft = num(n + "_ft"), inch = num(n + "_in");
          x = (isNaN(ft) && isNaN(inch)) ? NaN : ((ft || 0) * 12 + (inch || 0)) * IN;
        }
      } else if (imp && (t === "weight" || t === "load")) {
        x = x / LB;
      } else if (imp && t === "length") {
        x = x * IN;
      }
      v[n] = x;
    });
    return v;
  }

  /* Write metric values back into the form in whichever unit is showing. */
  function write(v) {
    var imp = imperial();
    Array.prototype.forEach.call(form.querySelectorAll("input[data-type]"), function (el) {
      var t = el.getAttribute("data-type"), n = el.name, x = v[n];
      if (t === "ft" || t === "in") return;
      if (t === "height") {
        if (isNaN(x)) return;
        var total = x / IN, ft = Math.floor(total / 12), inch = r(total - ft * 12, 1);
        if (inch >= 12) { ft += 1; inch = 0; }
        form.elements[n + "_ft"].value = ft;
        form.elements[n + "_in"].value = inch;
        el.value = r(x, 1);
        return;
      }
      if (isNaN(x)) return;
      if (t === "weight" || t === "load") el.value = imp ? r(x * LB, 1) : r(x, 1);
      else if (t === "length") el.value = imp ? r(x / IN, 1) : r(x, 1);
    });
    Array.prototype.forEach.call(form.querySelectorAll("[data-unit]"), function (s) {
      var t = s.getAttribute("data-unit");
      if (t === "weight" || t === "load") s.textContent = imp ? "lb" : "kg";
      if (t === "length") s.textContent = imp ? "in" : "cm";
    });
  }

  /* ---------- shared formulas ---------- */

  function mifflin(v) {
    return 10 * v.weight + 6.25 * v.height - 5 * v.age + (v.sex === "male" ? 5 : -161);
  }
  function need() {
    for (var i = 0; i < arguments.length; i++) {
      var x = arguments[i];
      if (typeof x !== "number" || isNaN(x) || x <= 0) return false;
    }
    return true;
  }
  var FLOOR = { male: 1500, female: 1200 };

  /* ---------- calculators ---------- */

  var CALC = {};

  CALC.bmi = function (v) {
    if (!need(v.height, v.weight)) return;
    var m = v.height / 100, bmi = v.weight / (m * m);
    var cat = bmi < 18.5 ? ["Underweight", "mid"] : bmi < 25 ? ["Healthy weight", ""] :
      bmi < 30 ? ["Overweight", "mid"] : bmi < 35 ? ["Obese (class I)", "warn"] :
      bmi < 40 ? ["Obese (class II)", "warn"] : ["Obese (class III)", "warn"];
    var lo = 18.5 * m * m, hi = 24.9 * m * m;
    return big("Your BMI", fmt(bmi, 1), "kg/m²") + badge(cat[0], cat[1]) +
      gauge(bmi, 15, 40, [[3.5, "#7cb6f2"], [6.5, "#9ad433"], [5, "#f5c542"], [10, "#f08a4b"]],
        ["15", "18.5", "25", "30", "40"]) +
      rows([["Healthy weight for your height", wt(lo, 1) + " – " + wt(hi, 1), true],
            ["BMI Prime", fmt(bmi / 25, 2)],
            ["Category thresholds", "18.5 / 25 / 30"]]) +
      note("BMI can't tell muscle from fat. If you lift, check your <a href=\"/body-fat-calculator\">body fat</a> or <a href=\"/ffmi-calculator\">FFMI</a> too.");
  };

  CALC.bodyfat = function (v) {
    var f = v.sex === "female";
    if (!need(v.height, v.neck, v.waist) || (f && !need(v.hip))) return;
    if (!need(v.weight)) v.weight = NaN;
    var bf = f
      ? 495 / (1.29579 - 0.35004 * Math.log10(v.waist + v.hip - v.neck) + 0.22100 * Math.log10(v.height)) - 450
      : 495 / (1.0324 - 0.19077 * Math.log10(v.waist - v.neck) + 0.15456 * Math.log10(v.height)) - 450;
    if (!isFinite(bf) || bf < 2 || bf > 70) {
      return '<p class="alert">Those measurements don\'t produce a sensible result. Check that the waist is larger than the neck and the units are right.</p>';
    }
    var cuts = f ? [13, 20, 24, 31] : [5, 13, 17, 24];
    var names = ["Essential fat", "Athletic", "Fitness", "Average", "Above average"];
    var i = bf <= cuts[0] ? 0 : bf <= cuts[1] ? 1 : bf <= cuts[2] ? 2 : bf <= cuts[3] ? 3 : 4;
    var html = big("Body fat", fmt(bf, 1), "%") + badge(names[i], i === 4 ? "warn" : i === 3 ? "mid" : "") +
      gauge(bf, f ? 8 : 2, f ? 45 : 40,
        f ? [[5, "#7cb6f2"], [7, "#62c370"], [4, "#9ad433"], [7, "#f5c542"], [14, "#f08a4b"]]
          : [[3, "#7cb6f2"], [8, "#62c370"], [4, "#9ad433"], [7, "#f5c542"], [16, "#f08a4b"]],
        f ? ["8", "13", "20", "24", "31", "45"] : ["2", "5", "13", "17", "24", "40"]);
    var list = [["Category", names[i], true]];
    if (need(v.weight)) list.push(["Fat mass", wt(v.weight * bf / 100)], ["Lean mass", wt(v.weight * (1 - bf / 100))]);
    list.push(["Method", "US Navy tape (±3–4%)"]);
    return html + rows(list) + note("Put this figure into the <a href=\"/ffmi-calculator\">FFMI calculator</a> to see how much muscle you carry for your height.");
  };

  CALC.ideal = function (v) {
    if (!need(v.height)) return;
    var over = Math.max(0, v.height / IN - 60), m = v.sex === "male";
    var f = {
      "Devine (1974)": m ? 50 + 2.3 * over : 45.5 + 2.3 * over,
      "Robinson (1983)": m ? 52 + 1.9 * over : 49 + 1.7 * over,
      "Miller (1983)": m ? 56.2 + 1.41 * over : 53.1 + 1.36 * over,
      "Hamwi (1964)": m ? 48 + 2.7 * over : 45.5 + 2.2 * over
    };
    var vals = Object.keys(f).map(function (k) { return f[k]; });
    var avg = vals.reduce(function (a, b) { return a + b; }, 0) / vals.length;
    var h = v.height / 100;
    var list = Object.keys(f).map(function (k) { return [k, wt(f[k], 1)]; });
    list.push(["Healthy BMI range (18.5–24.9)", wt(18.5 * h * h, 1) + " – " + wt(24.9 * h * h, 1), true]);
    var html = big("Ideal weight (average of 4 formulas)", imperial() ? fmt(avg * LB) : fmt(avg, 1), imperial() ? "lb" : "kg") + rows(list);
    if (v.height < 152.4) html += alert("These formulas were built for people 5 ft (152 cm) and taller, so treat them loosely below that.");
    return html + note("Muscular lifters usually sit well above these numbers. That's fine: check <a href=\"/body-fat-calculator\">body fat</a> instead.");
  };

  CALC.lbm = function (v) {
    if (!need(v.height, v.weight)) return;
    var m = v.sex === "male", w = v.weight, h = v.height;
    var boer = m ? 0.407 * w + 0.267 * h - 19.2 : 0.252 * w + 0.473 * h - 48.3;
    var james = m ? 1.1 * w - 128 * Math.pow(w / h, 2) : 1.07 * w - 148 * Math.pow(w / h, 2);
    var hume = m ? 0.32810 * w + 0.33929 * h - 29.5336 : 0.29569 * w + 0.41813 * h - 43.2933;
    var direct = need(v.bf) ? w * (1 - v.bf / 100) : null;
    var main = direct || boer;
    function bf(l) { return fmt((1 - l / w) * 100, 1) + "%"; }
    var list = [["Boer (1984)", wt(boer) + " · " + bf(boer), !direct],
                ["James (1976)", wt(james) + " · " + bf(james)],
                ["Hume (1966)", wt(hume) + " · " + bf(hume)]];
    if (direct) list.unshift(["From your body fat %", wt(direct) + " · " + fmt(v.bf, 1) + "%", true]);
    return big(direct ? "Lean body mass" : "Lean body mass (Boer)", imperial() ? fmt(main * LB) : fmt(main, 1), imperial() ? "lb" : "kg") +
      badge("Fat mass ≈ " + wt(w - main)) + rows(list) +
      note("Formula estimates assume average body composition. If you know your body fat %, enter it for a direct figure.");
  };

  CALC.ffmi = function (v) {
    if (!need(v.height, v.weight, v.bf)) return;
    var h = v.height / 100, lbm = v.weight * (1 - v.bf / 100);
    var ffmi = lbm / (h * h), norm = ffmi + 6.1 * (1.8 - h);
    var off = v.sex === "female" ? 3 : 0, x = norm + off;
    var cat = x < 18 ? ["Below average", "mid"] : x < 20 ? ["Average", ""] : x < 22 ? ["Above average", ""] :
      x < 23 ? ["Excellent", ""] : x < 25 ? ["Superior", ""] : x < 27 ? ["Rare without drugs", "mid"] : ["Very unlikely naturally", "warn"];
    return big("Normalised FFMI", fmt(norm, 1), "kg/m²") + badge(cat[0], cat[1]) +
      gauge(x, 16, 28, [[2, "#7cb6f2"], [2, "#9ad433"], [2, "#62c370"], [1, "#3fa34d"], [2, "#2f7d3a"], [2, "#f5c542"], [1, "#f08a4b"]],
        v.sex === "female" ? ["13", "15", "17", "19", "21", "25"] : ["16", "18", "20", "22", "25", "28"]) +
      rows([["Raw FFMI", fmt(ffmi, 1)], ["Normalised to 1.80 m", fmt(norm, 1), true],
            ["Fat-free mass", wt(lbm)], ["Fat mass", wt(v.weight - lbm)]]) +
      note("Kouri et al. (1995) found few drug-free men above about 25. Body fat error moves FFMI too: ±3% body fat is roughly ±0.7 FFMI.");
  };

  CALC.whr = function (v) {
    if (!need(v.waist, v.hip)) return;
    var whr = v.waist / v.hip, f = v.sex === "female", cut = f ? 0.85 : 0.90;
    var html = big("Waist-to-hip ratio", fmt(whr, 2)) +
      badge(whr >= cut ? "Substantially increased risk" : whr >= cut - 0.05 ? "Moderate: close to threshold" : "Low risk",
        whr >= cut ? "warn" : whr >= cut - 0.05 ? "mid" : "") +
      gauge(whr, 0.6, 1.2, f ? [[20, "#9ad433"], [5, "#f5c542"], [35, "#f08a4b"]] : [[25, "#9ad433"], [5, "#f5c542"], [30, "#f08a4b"]],
        ["0.6", f ? "0.85" : "0.90", "1.2"]);
    var list = [["WHO threshold for " + (f ? "women" : "men"), "≥ " + cut.toFixed(2)],
                ["Body shape", whr >= cut ? "Apple (central)" : "Pear (lower body)"]];
    if (need(v.height)) {
      var whtr = v.waist / v.height;
      list.push(["Waist-to-height ratio", fmt(whtr, 2) + (whtr >= 0.5 ? " · above 0.5" : " · under 0.5"), true]);
    }
    return html + rows(list) + note("Waist-to-height under 0.5 (\"keep your waist under half your height\") is a simple target that works for most adults.");
  };

  function tdeeOf(v) { return mifflin(v) * parseFloat(v.activity); }

  CALC.tdee = function (v) {
    if (!need(v.age, v.height, v.weight)) return;
    var bmr = mifflin(v), act = parseFloat(v.activity);
    var levels = [[1.2, "Sedentary"], [1.375, "Light"], [1.55, "Moderate"], [1.725, "Very active"], [1.9, "Extra active"]];
    var t = '<table class="tbl-mini"><thead><tr><th>Activity</th><th>Calories / day</th></tr></thead><tbody>' +
      levels.map(function (l) {
        return '<tr' + (l[0] === act ? ' class="is-hl"' : "") + "><td>" + l[1] + "</td><td>" + kcal(bmr * l[0]) + "</td></tr>";
      }).join("") + "</tbody></table>";
    return big("Maintenance calories (TDEE)", fmt(bmr * act), "kcal/day") +
      rows([["BMR (Mifflin-St Jeor)", kcal(bmr)], ["Activity multiplier", "× " + act],
            ["Per week", kcal(bmr * act * 7)]]) + t +
      note("Weigh yourself for 2–3 weeks eating this much. Stable weight means it's right; adjust by 100–200 kcal if not. Next: <a href=\"/macro-calculator\">set your macros</a>.");
  };

  CALC.calorie = function (v) {
    if (!need(v.age, v.height, v.weight)) return;
    var t = tdeeOf(v), floor = FLOOR[v.sex];
    var goals = [["Extreme loss (1 kg / 2 lb a week)", -1100], ["Weight loss (0.5 kg / 1 lb a week)", -550],
                 ["Mild loss (0.25 kg / 0.5 lb a week)", -275], ["Maintain", 0],
                 ["Mild gain (0.25 kg / 0.5 lb a week)", 275], ["Gain (0.5 kg / 1 lb a week)", 550]];
    var low = false;
    var tbl = '<table class="tbl-mini"><thead><tr><th>Goal</th><th>Calories / day</th></tr></thead><tbody>' +
      goals.map(function (g) {
        var k = t + g[1], under = k < floor; if (under) low = true;
        return '<tr' + (g[1] === 0 ? ' class="is-hl"' : "") + "><td>" + g[0] + "</td><td>" + kcal(k) + (under ? " ⚠" : "") + "</td></tr>";
      }).join("") + "</tbody></table>";
    return big("Maintenance", fmt(t), "kcal/day") + badge("Fat loss target: " + kcal(Math.max(t - 550, floor))) + tbl +
      (low ? alert("⚠ Below " + floor + " kcal/day. Going this low is hard to sustain and makes it difficult to get enough protein and nutrients. Pick a slower pace, or talk to a doctor or dietitian first.") : "") +
      note("Based on about 7,700 kcal per kg of fat (3,500 per lb). Real loss slows over time, so recalculate every 4–5 kg.");
  };

  CALC.macro = function (v) {
    if (!need(v.age, v.height, v.weight)) return;
    var t = tdeeOf(v) * ({ cut: 0.8, maintain: 1, bulk: 1.1 })[v.goal];
    var p = v.weight * (v.goal === "cut" ? 2.0 : 1.8), pk = p * 4;
    var f, c;
    if (v.style === "keto") { c = t * 0.05 / 4; f = (t - pk - c * 4) / 9; }
    else {
      var fp = ({ balanced: 0.25, lowcarb: 0.40, highcarb: 0.20 })[v.style];
      f = t * fp / 9; c = (t - pk - f * 9) / 4;
    }
    var warn = "";
    if (c < 0 || f < 0) {
      f = Math.max(f, v.weight * 0.6); c = Math.max(0, (t - pk - f * 9) / 4);
      warn = alert("Protein and fat take up nearly all your calories at this target, so carbs are set to the minimum.");
    }
    var cols = [["Protein", p, "#3f6b00", 4], ["Carbs", c, "#1d5fd6", 4], ["Fat", f, "#e0821d", 9]];
    var total = cols.reduce(function (a, x) { return a + x[1] * x[3]; }, 0);
    var macros = '<div class="macros">' + cols.map(function (x) {
      return '<div class="macro"><i style="background:' + x[2] + '"></i><span>' + x[0] + "</span><b>" + fmt(x[1]) +
        "g</b><span>" + fmt(x[1] * x[3]) + " kcal · " + fmt(x[1] * x[3] / total * 100) + "%</span></div>";
    }).join("") + "</div>";
    var stack = '<div class="stack">' + cols.map(function (x) {
      return '<span style="flex:' + (x[1] * x[3]) + ";background:" + x[2] + '"></span>';
    }).join("") + "</div>";
    var meals = '<table class="tbl-mini"><thead><tr><th>Meals / day</th><th>Protein</th><th>Carbs</th><th>Fat</th></tr></thead><tbody>' +
      [3, 4, 5].map(function (n) {
        return "<tr><td>" + n + " meals</td><td>" + fmt(p / n) + "g</td><td>" + fmt(c / n) + "g</td><td>" + fmt(f / n) + "g</td></tr>";
      }).join("") + "</tbody></table>";
    return big("Daily target", fmt(t), "kcal") + macros + stack + warn + meals +
      note("Protein is set per kg of body weight (" + (v.goal === "cut" ? "2.0" : "1.8") + " g/kg), fat by diet style, and carbs fill the rest.");
  };

  CALC.protein = function (v) {
    if (!need(v.weight)) return;
    var g = { sedentary: [0.8, 0.8], active: [1.2, 1.6], muscle: [1.6, 2.2], cut: [1.8, 2.4] }[v.goal];
    var lo = v.weight * g[0], hi = v.weight * g[1], mid = (lo + hi) / 2;
    var meal = v.weight * 0.4;
    var foods = [["Chicken breast, cooked", 31, "100 g"], ["Greek yogurt, plain", 10, "100 g"], ["Eggs", 6, "1 large"],
                 ["Whey protein", 24, "1 scoop (30 g)"], ["Lentils, cooked", 9, "100 g"], ["Paneer / firm tofu", 18, "100 g"]];
    return big("Daily protein", lo === hi ? fmt(lo) : fmt(lo) + "–" + fmt(hi), "g/day") +
      badge(g[0] === g[1] ? g[0] + " g per kg" : g[0] + "–" + g[1] + " g per kg") +
      rows([["Middle of the range", fmt(mid) + " g", true], ["Per meal (4 meals)", "≈ " + fmt(meal) + " g"],
            ["Per lb of body weight", fmt(lo / (v.weight * LB), 2) + "–" + fmt(hi / (v.weight * LB), 2) + " g"]]) +
      '<table class="tbl-mini"><thead><tr><th>Food</th><th>Protein</th><th>Serving</th></tr></thead><tbody>' +
      foods.map(function (x) { return "<tr><td>" + x[0] + "</td><td>" + x[1] + " g</td><td>" + x[2] + "</td></tr>"; }).join("") +
      "</tbody></table>" + note("If you have kidney disease, check with your doctor before raising protein.");
  };

  CALC.bmr = function (v) {
    if (!need(v.age, v.height, v.weight)) return;
    var m = v.sex === "male", mif = mifflin(v);
    var hb = m ? 88.362 + 13.397 * v.weight + 4.799 * v.height - 5.677 * v.age
               : 447.593 + 9.247 * v.weight + 3.098 * v.height - 4.330 * v.age;
    var list = [["Mifflin-St Jeor", kcal(mif), true], ["Revised Harris-Benedict", kcal(hb)]];
    if (need(v.bf)) list.push(["Katch-McArdle (uses body fat)", kcal(370 + 21.6 * v.weight * (1 - v.bf / 100))]);
    else list.push(["Katch-McArdle", "add body fat %"]);
    return big("Basal metabolic rate", fmt(mif), "kcal/day") + rows(list) +
      note("This is what you'd burn resting all day. Your real daily burn is higher: get it from the <a href=\"/tdee-calculator\">TDEE calculator</a>.");
  };

  CALC.weightloss = function (v) {
    if (!need(v.age, v.height, v.weight, v.goalw)) return;
    if (v.goalw >= v.weight) return alert("Your goal weight is the same as or above your current weight. For gaining, use the <a href=\"/calorie-calculator\">calorie calculator</a>.");
    var t = tdeeOf(v), pace = parseFloat(v.pace), deficit = pace * 7700 / 7;
    var target = t - deficit, floor = FLOOR[v.sex], capped = target < floor;
    var eat = Math.max(target, floor), realDef = t - eat;
    var toLose = v.weight - v.goalw, weeks = toLose * 7700 / (realDef * 7);
    var d = new Date(); d.setDate(d.getDate() + Math.round(weeks * 7));
    var gb = 18.5 * Math.pow(v.height / 100, 2);
    return big("Eat about", fmt(eat), "kcal/day") + badge("Goal by " + d.toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" })) +
      rows([["Maintenance (TDEE)", kcal(t)], ["Daily deficit", kcal(realDef)], ["To lose", wt(toLose)],
            ["Time to goal", fmt(weeks) + " weeks", true], ["Total deficit", kcal(toLose * 7700)]]) +
      (capped ? alert("That pace would need fewer than " + floor + " kcal/day, so the target is held at " + floor + " and the timeline extended.") : "") +
      (v.goalw < gb ? alert("Your goal is below a BMI of 18.5 for your height. Please check it with a doctor.") : "") +
      note("Weight loss isn't a straight line. Expect slower weeks and recalculate every 5 kg (10 lb).");
  };

  CALC.water = function (v) {
    if (!need(v.weight)) return;
    var ml = v.weight * 35 + (v.exercise > 0 ? v.exercise / 30 * 350 : 0) + (v.climate === "hot" ? 500 : 0);
    var l = ml / 1000;
    return big("Drink about", fmt(l, 1), "litres/day") + badge("≈ " + fmt(ml / 250) + " glasses of 250 ml") +
      rows([["In US fluid ounces", fmt(ml / 29.574) + " fl oz"], ["In cups (8 oz)", fmt(ml / 236.6, 1)],
            ["Base (35 ml per kg)", fmt(v.weight * 35 / 1000, 1) + " L"],
            ["Extra for exercise", fmt((v.exercise > 0 ? v.exercise / 30 * 350 : 0) / 1000, 1) + " L"]]) +
      note("Includes water from all drinks. Pale straw-coloured urine is a good sign you're on track.");
  };

  CALC.orm = function (v) {
    if (!need(v.lift, v.reps)) return;
    var w = v.lift, n = Math.round(v.reps);
    if (n > 12) return alert("Estimates get unreliable above 12 reps. Use a heavier set of 3–10 reps.");
    var ep = n === 1 ? w : w * (1 + n / 30), br = w * 36 / (37 - n), lo = w * Math.pow(n, 0.10);
    var avg = (ep + br + lo) / 3;
    var pc = [[100, 1], [95, 2], [93, 3], [90, 4], [87, 5], [85, 6], [83, 7], [80, 8], [77, 9], [75, 10], [70, 12], [65, 15], [60, 18], [55, 20], [50, 24]];
    function load(x) { return imperial() ? fmt(x * LB) + " lb" : fmt(x, 1) + " kg"; }
    var t = '<table class="tbl-mini"><thead><tr><th>% of 1RM</th><th>Weight</th><th>≈ Reps</th></tr></thead><tbody>' +
      pc.map(function (x) { return "<tr" + (x[1] === n ? ' class="is-hl"' : "") + "><td>" + x[0] + "%</td><td>" + load(avg * x[0] / 100) + "</td><td>" + x[1] + "</td></tr>"; }).join("") +
      "</tbody></table>";
    return big("Estimated 1RM", imperial() ? fmt(avg * LB) : fmt(avg, 1), imperial() ? "lb" : "kg") +
      rows([["Epley", load(ep)], ["Brzycki", load(br)], ["Lombardi", load(lo)], ["Average", load(avg), true]]) + t;
  };

  CALC.plate = function (v) {
    if (!need(v.target)) return;
    var imp = imperial();
    var barKg = parseFloat(v.bar), bar = imp ? ({ 20: 45, 15: 35, 10: 25 })[barKg] : barKg;
    var collars = parseFloat(v.collars) * (imp ? 2.2 : 1);
    var target = imp ? v.target * LB : v.target;
    var plates = imp ? [45, 35, 25, 10, 5, 2.5] : [25, 20, 15, 10, 5, 2.5, 1.25];
    var colors = imp ? { 45: "#c62828", 35: "#1565c0", 25: "#f9a825", 10: "#2e7d32", 5: "#37474f", 2.5: "#546e7a" }
                     : { 25: "#c62828", 20: "#1565c0", 15: "#f9a825", 10: "#2e7d32", 5: "#eceff1", 2.5: "#37474f", 1.25: "#90a4ae" };
    var heights = imp ? { 45: 110, 35: 98, 25: 84, 10: 66, 5: 52, 2.5: 42 } : { 25: 112, 20: 112, 15: 100, 10: 86, 5: 60, 2.5: 48, 1.25: 40 };
    var side = (target - bar - collars * 2) / 2;
    var u = imp ? " lb" : " kg";
    if (side < 0) return alert("The bar" + (collars ? " and collars" : "") + " alone weigh " + fmt(bar + collars * 2, 1) + u + ". Enter a heavier target.");
    var left = side, used = [];
    plates.forEach(function (p) { while (left + 1e-9 >= p) { used.push(p); left -= p; } });
    var loaded = bar + collars * 2 + 2 * used.reduce(function (a, b) { return a + b; }, 0);
    var viz = '<div class="bar-viz"><span class="bar-viz__sleeve"></span>' + (collars ? '<span class="bar-viz__collar"></span>' : "") +
      used.slice().reverse().map(function (p) {
        return '<span class="bar-viz__plate" style="height:' + heights[p] + "px;background:" + colors[p] + (p === 5 && !imp ? ";color:#333" : "") + '">' + p + "</span>";
      }).join("") + '<span class="bar-viz__shaft"></span><span class="bar-viz__shaft"></span>' +
      used.map(function (p) {
        return '<span class="bar-viz__plate" style="height:' + heights[p] + "px;background:" + colors[p] + (p === 5 && !imp ? ";color:#333" : "") + '">' + p + "</span>";
      }).join("") + (collars ? '<span class="bar-viz__collar"></span>' : "") + '<span class="bar-viz__sleeve"></span></div>';
    var counts = {}; used.forEach(function (p) { counts[p] = (counts[p] || 0) + 1; });
    var list = '<div class="plates-list">' + plates.filter(function (p) { return counts[p]; }).map(function (p) {
      return "<span>" + counts[p] + " × " + p + u + "</span>"; }).join("") + "</div>";
    return big("Each side", fmt(side - left, 2).replace(/\.?0+$/, ""), u.trim()) + viz +
      (used.length ? list : note("Just the bar" + (collars ? " and collars" : "") + ".")) +
      rows([["Bar", bar + u], ["Loaded total", fmt(loaded, 2).replace(/\.?0+$/, "") + u, true]]) +
      (left > 1e-6 ? alert("Can't load exactly: " + fmt(left * 2, 2) + u + " short with standard plates. Closest is " + fmt(loaded, 2) + u + ".") : "") +
      note("Load heaviest plates first, on the inside. Plates per side are shown for one side of the bar.");
  };

  CALC.wilks = function (v) {
    if (!need(v.weight)) return;
    var total = (v.squat || 0) + (v.bench || 0) + (v.deadlift || 0);
    if (!(total > 0)) return;
    var m = v.sex === "male";
    var bw = Math.min(Math.max(v.weight, m ? 40 : 26.51), m ? 201.9 : 154.53);
    var W = m ? [-216.0475144, 16.2606339, -0.002388645, -0.00113732, 7.01863e-06, -1.291e-08]
              : [594.31747775582, -27.23842536447, 0.82112226871, -0.00930733913, 4.731582e-05, -9.054e-08];
    var poly = 0; for (var i = 0; i < 6; i++) poly += W[i] * Math.pow(bw, i);
    var wilks = total * 500 / poly;
    var db = Math.min(Math.max(v.weight, 40), m ? 210 : 150);
    var D = m ? [-307.75076, 24.0900756, -0.1918759221, 0.0007391293, -0.000001093]
              : [-57.96288, 13.6175032, -0.1126655495, 0.0005158568, -0.0000010706];
    var dp = 0; for (var j = 0; j < 5; j++) dp += D[j] * Math.pow(db, j);
    var dots = total * 500 / dp;
    var lvl = dots < 200 ? "Beginner" : dots < 300 ? "Novice" : dots < 400 ? "Intermediate" : dots < 500 ? "Advanced" : "Elite";
    return big("DOTS score", fmt(dots, 1)) + badge(lvl + " (rough guide)") +
      rows([["Total", (imperial() ? fmt(total * LB) + " lb" : fmt(total, 1) + " kg"), true],
            ["Wilks (classic)", fmt(wilks, 1)], ["DOTS", fmt(dots, 1)],
            ["Total ÷ body weight", fmt(total / v.weight, 2) + "×"]]) +
      note("Level bands are rough: <200 beginner, 300 intermediate, 400 advanced, 500+ elite.");
  };

  CALC.hr = function (v) {
    if (!need(v.age)) return;
    var max = v.formula === "fox" ? 220 - v.age : 208 - 0.7 * v.age;
    var rhr = need(v.rhr) ? v.rhr : null;
    function at(p) { return rhr ? rhr + (max - rhr) * p : max * p; }
    var zones = [[1, "Recovery", "Very easy, warm-ups", 0.5, 0.6, "#7cb6f2"],
                 [2, "Endurance", "Easy, conversational", 0.6, 0.7, "#62c370"],
                 [3, "Aerobic / tempo", "Comfortably hard", 0.7, 0.8, "#f5c542"],
                 [4, "Threshold", "Hard, few words", 0.8, 0.9, "#f08a4b"],
                 [5, "VO2 max", "All-out efforts", 0.9, 1.0, "#d64545"]];
    return big("Max heart rate", fmt(max), "bpm") + badge(rhr ? "Karvonen (heart rate reserve)" : "% of max heart rate") +
      '<div class="zones">' + zones.map(function (z) {
        return '<div class="zone"><b style="background:' + z[5] + '">Z' + z[0] + "</b><span>" + z[1] + "<small>" + z[2] + " · " +
          z[3] * 100 + "–" + z[4] * 100 + "%</small></span><code>" + fmt(at(z[3])) + "–" + fmt(at(z[4])) + "</code></div>";
      }).join("") + "</div>" +
      note(rhr ? "Using resting heart rate of " + fmt(rhr) + " bpm." : "Add your resting heart rate for zones that fit your fitness level.");
  };

  CALC.burn = function (v) {
    if (!need(v.weight, v.minutes)) return;
    var met = parseFloat(v.act), kc = met * v.weight * v.minutes / 60;
    var sel = form.elements.act, name = sel.options[sel.selectedIndex].text;
    return big("Calories burned", fmt(kc), "kcal") + badge(name + " · MET " + met) +
      rows([["Per minute", fmt(kc / v.minutes, 1) + " kcal"], ["Per hour", kcal(met * v.weight), true],
            ["Net (minus resting)", "≈ " + kcal((met - 1) * v.weight * v.minutes / 60)]]) +
      note("Gross figure includes what you'd burn at rest. Treat it as an estimate: real burn varies by ±20% or more.");
  };

  /* ---------- wiring ---------- */

  function run() {
    var v = read(), html;
    try { html = CALC[id] && CALC[id](v); } catch (e) { html = null; }
    out.innerHTML = html || '<div class="result result--empty"><p>Fill in the fields to see your result.</p></div>';
  }

  function sexFields() {
    var sex = (form.querySelector("input[name=sex]:checked") || {}).value;
    Array.prototype.forEach.call(form.querySelectorAll("[data-only]"), function (el) {
      el.hidden = el.getAttribute("data-only") !== sex;
    });
  }

  // Read in the old units, flip, write back in the new ones.
  function setUnits(u) {
    tool.classList.toggle("is-imperial", u !== "imperial");
    var before = read();
    tool.classList.toggle("is-imperial", u === "imperial");
    write(before);
    try { localStorage.setItem(KEY, u); } catch (e) {}
  }

  // Defaults in the HTML are metric. Mirror them into ft/in first.
  tool.classList.remove("is-imperial");
  var initial = read();
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === "imperial" && form.querySelector("input[name=units]")) {
    tool.classList.add("is-imperial");
    form.querySelector("input[name=units][value=imperial]").checked = true;
  }
  write(initial);
  sexFields();

  var timer;
  form.addEventListener("input", function (e) {
    if (e.target.name === "units") return;
    clearTimeout(timer); timer = setTimeout(run, 150);
  });
  form.addEventListener("change", function (e) {
    if (e.target.name === "units") setUnits(e.target.value);
    if (e.target.name === "sex") sexFields();
    run();
  });
  form.addEventListener("submit", function (e) {
    e.preventDefault(); run();
    if (window.innerWidth < 760) out.scrollIntoView({ behavior: "smooth", block: "start" });
  });
  run();
})();
