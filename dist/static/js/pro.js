/* FormFit Pro: sign-in (Supabase), checkout (Razorpay), plan generator and
   progress tracking. Loaded only on /account and /dashboard.

   - Supabase keeps the session in localStorage, so it's shared by both pages.
   - Anything that decides who is Pro happens on the server (api/*.py) or in
     the database (row level security in supabase/schema.sql).
   - localStorage "ff_pro" holds the time Pro runs out; base.html reads it to
     skip loading ads. It's only a display hint, never a permission. */
(function () {
  "use strict";

  var cfg = window.FF_PRO || {};
  var root = document.querySelector("[data-pro-root]");
  if (!root) return;
  var isDash = !!document.querySelector("[data-plan-form]");

  function $(sel, el) { return (el || document).querySelector(sel); }
  function $$(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function view(name) {
    $$("[data-view]").forEach(function (el) { el.hidden = el.getAttribute("data-view") !== name; });
    var out = $("[data-signout-wrap]");
    if (out) out.hidden = name === "signin" || name === "loading";
  }
  function status(el, msg, ok) {
    if (!el) return;
    el.textContent = msg || "";
    el.hidden = !msg;
    el.classList.toggle("is-ok", !!ok);
  }
  function fmtDate(iso) {
    if (!iso) return "";
    return new Date(iso).toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" });
  }
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2);
  }
  function rememberPro(me) {
    try {
      if (me && me.is_pro && me.current_period_end) {
        localStorage.setItem("ff_pro", String(Date.parse(me.current_period_end) + 864e5));
      } else {
        localStorage.removeItem("ff_pro");
      }
    } catch (e) { /* private mode: ads just stay on */ }
  }

  if (!cfg.supabaseUrl || !cfg.supabaseKey || !window.supabase) {
    view("none");
    $("[data-setup]").hidden = false;
    return;
  }

  var sb = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseKey);

  function api(name, body) {
    return sb.auth.getSession().then(function (r) {
      var s = r.data && r.data.session;
      if (!s) throw new Error("Please sign in again.");
      return fetch("/api/" + name, {
        method: body ? "POST" : "GET",
        headers: { "Authorization": "Bearer " + s.access_token, "Content-Type": "application/json" },
        body: body ? JSON.stringify(body) : undefined
      });
    }).then(function (res) {
      return res.json().catch(function () { return {}; }).then(function (j) {
        if (!res.ok || !j.ok) {
          var err = new Error(j.error || "Something went wrong. Please try again.");
          err.fields = j.errors;
          throw err;
        }
        return j;
      });
    });
  }

  var me = null;

  function load() {
    return sb.auth.getSession().then(function (r) {
      var s = r.data && r.data.session;
      if (!s) { rememberPro(null); view("signin"); return; }
      return api("me").then(function (m) {
        me = m;
        rememberPro(m);
        $$("[data-email]").forEach(function (el) { el.textContent = m.email || ""; });
        if (m.is_pro) {
          view("pro");
          if (isDash) startDashboard(); else showPro(m);
        } else {
          view("free");
        }
      });
    }).catch(function (e) {
      view("signin");
      status($(".cform__status", $("[data-view=signin]")), e.message);
    });
  }

  sb.auth.onAuthStateChange(function (event) {
    if (event === "SIGNED_IN" && !me) load();
  });

  // --------------------------------------------------------------- sign in
  var signin = $("[data-signin]");
  if (signin) {
    var redirect = location.origin + location.pathname + location.search;
    signin.addEventListener("submit", function (e) {
      e.preventDefault();
      var st = $(".cform__status", signin);
      var email = signin.email.value.trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { status(st, "Please enter a valid email address."); return; }
      var btn = $("button", signin);
      btn.disabled = true;
      sb.auth.signInWithOtp({ email: email, options: { emailRedirectTo: redirect } }).then(function (r) {
        if (r.error) throw r.error;
        status(st, "Check your inbox: we've sent a sign-in link to " + email + ".", true);
      }).catch(function (err) {
        status(st, err.message || "Couldn't send the link. Please try again.");
      }).then(function () { btn.disabled = false; });
    });
    var g = $("[data-google]");
    if (g) g.addEventListener("click", function () {
      sb.auth.signInWithOAuth({ provider: "google", options: { redirectTo: redirect } });
    });
  }

  var out = $("[data-signout]");
  if (out) out.addEventListener("click", function () {
    sb.auth.signOut().then(function () { rememberPro(null); location.href = "/"; });
  });

  // --------------------------------------------------------------- account
  var wanted = (location.search.match(/[?&]plan=(monthly|yearly)/) || [])[1];
  if (wanted) $$("input[name=plan]").forEach(function (r) { r.checked = r.value === wanted; });

  function showPro(m) {
    var line = $("[data-pro-line]");
    var end = fmtDate(m.current_period_end);
    var plan = m.plan === "yearly" ? "yearly" : "monthly";
    $$("[data-end]").forEach(function (el) { el.textContent = end; });
    if (m.cancel_at_period_end || m.status === "cancelled") {
      line.textContent = "Your subscription is cancelled. Pro stays on until " + end + ".";
      $("[data-cancel-box]").hidden = true;
    } else if (m.status === "pending") {
      line.textContent = "Your last renewal payment didn't go through. Razorpay will try again; " +
        "please check your UPI app or card. Pro is on until " + end + ".";
    } else {
      line.textContent = "Your " + plan + " plan renews on " + end + ".";
    }
  }

  var subBtn = $("[data-subscribe]");
  if (subBtn) subBtn.addEventListener("click", function () {
    var st = $("[data-status]", $("[data-view=free]"));
    var plan = ($("input[name=plan]:checked") || {}).value || "monthly";
    if (!window.Razorpay) { status(st, "The payment window didn't load. Check your connection and try again."); return; }
    subBtn.disabled = true;
    status(st, "");
    api("subscribe", { plan: plan }).then(function (r) {
      var rzp = new window.Razorpay({
        key: r.key_id,
        subscription_id: r.subscription_id,
        name: "FormFit Pro",
        description: plan === "yearly" ? "Yearly subscription" : "Monthly subscription",
        prefill: { email: r.email || "" },
        theme: { color: "#0c0e11" },
        handler: function (resp) {
          status(st, "Payment received, switching on Pro...", true);
          api("verify", resp).then(function () {
            return load();
          }).catch(function (e) { status(st, e.message); });
        },
        modal: { ondismiss: function () { subBtn.disabled = false; } }
      });
      rzp.on("payment.failed", function (resp) {
        status(st, (resp.error && resp.error.description) || "The payment failed. Please try again.");
        subBtn.disabled = false;
      });
      rzp.open();
    }).catch(function (e) {
      status(st, e.message);
      subBtn.disabled = false;
    });
  });

  var cancel = $("[data-cancel]");
  if (cancel) {
    var confirmBox = $("[data-cancel-confirm]");
    cancel.addEventListener("click", function () { confirmBox.hidden = false; cancel.hidden = true; });
    $("[data-cancel-no]").addEventListener("click", function () { confirmBox.hidden = true; cancel.hidden = false; });
    $("[data-cancel-yes]").addEventListener("click", function (e) {
      var st = $("[data-status]", $("[data-view=pro]"));
      e.target.disabled = true;
      api("cancel", {}).then(function (m) {
        me = m; rememberPro(m); showPro(Object.assign({ email: me.email }, m));
        status(st, "Cancelled. You won't be charged again.", true);
      }).catch(function (err) { status(st, err.message); e.target.disabled = false; });
    });
  }

  // ------------------------------------------------------------- dashboard
  var started = false;

  function startDashboard() {
    if (started) return;
    started = true;
    initPlan();
    initProgress();
  }

  // Plan generator
  var saved = [];

  function initPlan() {
    var form = $("[data-plan-form]");
    var st = $("[data-plan-status]");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      $$(".cform__err", form).forEach(function (x) { x.textContent = ""; });
      var data = {};
      $$("input, select", form).forEach(function (el) {
        if (el.type === "radio" && !el.checked) return;
        data[el.name] = el.value;
      });
      var btn = $("button[type=submit]", form);
      btn.disabled = true;
      btn.textContent = "Building...";
      status(st, "");
      api("plan", data).then(function (r) {
        renderPlan(r.plan);
        loadSaved();
        $("[data-plan-out]").scrollIntoView({ behavior: "smooth", block: "start" });
      }).catch(function (err) {
        Object.keys(err.fields || {}).forEach(function (k) {
          var slot = $('.cform__err[data-for="' + k + '"]', form);
          if (slot) slot.textContent = err.fields[k];
        });
        status(st, err.message);
      }).then(function () {
        btn.disabled = false;
        btn.textContent = "Build my plan";
      });
    });
    loadSaved(true);
  }

  function fillForm(inputs) {
    var form = $("[data-plan-form]");
    Object.keys(inputs || {}).forEach(function (k) {
      $$('[name="' + k + '"]', form).forEach(function (el) {
        if (el.type === "radio") el.checked = el.value === String(inputs[k]);
        else el.value = inputs[k];
      });
    });
  }

  function loadSaved(first) {
    sb.from("plans").select("id, created_at, inputs, plan").order("created_at", { ascending: false }).limit(8)
      .then(function (r) {
        if (r.error) return;
        saved = r.data || [];
        var box = $("[data-saved]");
        box.hidden = !saved.length;
        $("[data-saved-list]").innerHTML = saved.map(function (p, i) {
          return '<button type="button" class="chipbtn" data-open="' + i + '">' +
            esc(fmtDate(p.created_at)) + " &middot; " + esc(p.plan.summary.goal) + "</button>";
        }).join(" ");
        if (first && saved.length) {
          fillForm(saved[0].inputs);
          renderPlan(saved[0].plan);
        }
      });
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-open]");
    if (b) {
      var p = saved[+b.getAttribute("data-open")];
      if (p) { fillForm(p.inputs); renderPlan(p.plan); }
    }
    var d = e.target.closest("[data-day]");
    if (d) {
      var out = $("[data-plan-out]");
      var n = d.getAttribute("data-day");
      $$("[data-day]", out).forEach(function (x) { x.setAttribute("aria-pressed", x === d); });
      $$(".planday", out).forEach(function (x) { x.classList.toggle("is-on", x.getAttribute("data-dayn") === n); });
    }
    if (e.target.closest("[data-print]")) window.print();
  });

  function tile(label, value, unit) {
    return '<div class="ptile"><p class="result__label">' + esc(label) + '</p><p class="ptile__v">' +
      esc(value) + "<small>" + esc(unit) + "</small></p></div>";
  }

  function renderPlan(p) {
    var s = p.summary;
    var h = '<div class="planout__head"><div><p class="eyebrow eyebrow--dark">Your plan</p><h2>' + esc(s.goal) +
      " &middot; " + esc(s.diet) + '</h2><p class="result__note">Maintenance is about <strong>' + esc(s.tdee) +
      " kcal</strong> a day. Expect " + esc(s.expect) + '.</p></div>' +
      '<button type="button" class="btn btn--sm noprint" data-print>Print or save as PDF</button></div>';
    h += '<div class="ptiles">' + tile("Calories", s.calories, " kcal") + tile("Protein", s.protein, " g") +
      tile("Carbs", s.carbs, " g") + tile("Fat", s.fat, " g") + tile("Water", s.water_l, " L") + "</div>";

    h += '<h3 class="planout__sub">Meals</h3><div class="daytabs noprint" role="group" aria-label="Day">';
    p.meals.forEach(function (d, i) {
      h += '<button type="button" class="chipbtn" data-day="' + i + '" aria-pressed="' + (i === 0) + '">' + esc(d.day) + "</button>";
    });
    h += "</div>";
    p.meals.forEach(function (d, i) {
      h += '<div class="planday' + (i === 0 ? " is-on" : "") + '" data-dayn="' + i + '"><h4 class="planday__t">' +
        esc(d.day) + ' <span>' + esc(d.kcal) + " kcal &middot; " + esc(d.protein) + " g protein</span></h4><div class=\"meals\">";
      d.meals.forEach(function (m) {
        h += '<div class="meal"><p class="result__label">' + esc(m.slot) + "</p><p class=\"meal__n\">" + esc(m.name) +
          "</p><ul>" + m.items.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") +
          '</ul><p class="meal__k">' + esc(m.kcal) + " kcal &middot; " + esc(m.protein) + " g protein</p></div>";
      });
      h += "</div>" + (d.top_up ? '<p class="tip tip--sm">' + esc(d.top_up) + "</p>" : "") + "</div>";
    });

    h += '<h3 class="planout__sub">Training week</h3><div class="weekgrid">';
    p.training.forEach(function (d) {
      h += '<div class="wday' + (d.exercises.length ? "" : " wday--rest") + '"><p class="result__label">' + esc(d.day) +
        '</p><p class="wday__t">' + esc(d.title) + '</p><p class="wday__f">' + esc(d.focus) + "</p>";
      if (d.exercises.length) {
        h += '<table class="wtable"><thead><tr><th>Exercise</th><th>Sets</th><th>Reps</th><th>Rest</th></tr></thead><tbody>';
        d.exercises.forEach(function (x) {
          var name = x[4] ? '<a href="/exercises/' + esc(x[4]) + '">' + esc(x[0]) + "</a>" : esc(x[0]);
          h += "<tr><td>" + name + "</td><td>" + esc(x[1]) + "</td><td>" + esc(x[2]) + "</td><td>" + esc(x[3]) + "</td></tr>";
        });
        h += "</tbody></table>";
      }
      h += "</div>";
    });
    h += '</div><h3 class="planout__sub">How to run it</h3><ul class="rules">' +
      p.rules.map(function (r) { return "<li>" + esc(r) + "</li>"; }).join("") + "</ul>" +
      '<p class="field__hint">Food values are approximate. This is general guidance, not medical advice; see our <a href="/disclaimer">medical disclaimer</a>.</p>';

    var out = $("[data-plan-out]");
    out.innerHTML = h;
    out.hidden = false;
  }

  // Progress tracking
  var logs = [];
  var UNITS = { weight: ["Weight", "kg"], waist: ["Waist", "cm"], lift: ["Weight lifted", "kg"] };

  function initProgress() {
    var form = $("[data-log-form]");
    form.logged_on.value = today();
    form.addEventListener("change", function (e) {
      if (e.target.name !== "kind") return;
      var k = e.target.value;
      $$("[data-lift-only]", form).forEach(function (el) { el.hidden = k !== "lift"; });
      $("[data-value-label]", form).textContent = UNITS[k][0];
      $("[data-value-unit]", form).textContent = UNITS[k][1];
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var st = $("[data-log-status]");
      var kind = $("input[name=kind]:checked", form).value;
      var row = { kind: kind, value: parseFloat(form.value.value), logged_on: form.logged_on.value || today() };
      if (!(row.value > 0 && row.value < 1000)) { status(st, "Enter a number."); return; }
      if (kind === "lift") {
        row.exercise = form.exercise.value.trim().slice(0, 60);
        row.reps = parseInt(form.reps.value, 10) || 1;
        if (!row.exercise) { status(st, "Which exercise?"); return; }
      }
      var btn = $("button[type=submit]", form);
      btn.disabled = true;
      sb.from("logs").insert(row).then(function (r) {
        if (r.error) throw r.error;
        status(st, "Saved.", true);
        form.value.value = "";
        if (form.reps) form.reps.value = "";
        loadLogs();
      }).catch(function (err) {
        status(st, /row-level security/i.test(err.message || "")
          ? "Your Pro subscription isn't active, so new entries can't be saved."
          : (err.message || "Couldn't save that. Please try again."));
      }).then(function () { btn.disabled = false; });
    });
    $$("input[name=chart]").forEach(function (r) { r.addEventListener("change", drawChart); });
    document.addEventListener("click", function (e) {
      var del = e.target.closest("[data-del]");
      if (!del) return;
      del.disabled = true;
      sb.from("logs").delete().eq("id", del.getAttribute("data-del")).then(loadLogs);
    });
    loadLogs();
  }

  function loadLogs() {
    sb.from("logs").select("id, kind, logged_on, value, reps, exercise").order("logged_on", { ascending: true })
      .order("id", { ascending: true }).limit(2000).then(function (r) {
        if (r.error) return;
        logs = r.data || [];
        drawChart();
        drawBest();
        drawRecent();
      });
  }

  function drawChart() {
    var kind = ($("input[name=chart]:checked") || {}).value || "weight";
    var pts = logs.filter(function (l) { return l.kind === kind; })
      .map(function (l) { return { t: Date.parse(l.logged_on), v: +l.value }; });
    var box = $("[data-chart]");
    var note = $("[data-chart-note]");
    if (pts.length < 2) {
      box.innerHTML = '<div class="result--empty chart__empty"><p>Log at least two ' + (kind === "weight" ? "weigh-ins" : "waist measurements") + " to see your trend.</p></div>";
      note.textContent = "";
      return;
    }
    var avg = pts.map(function (p, i) {
      var w = pts.slice(Math.max(0, i - 6), i + 1);
      return { t: p.t, v: w.reduce(function (a, b) { return a + b.v; }, 0) / w.length };
    });
    var W = 600, H = 220, P = 34;
    var t0 = pts[0].t, t1 = pts[pts.length - 1].t || t0 + 1;
    var vs = pts.map(function (p) { return p.v; });
    var lo = Math.min.apply(null, vs), hi = Math.max.apply(null, vs);
    if (hi - lo < 1) { lo -= .5; hi += .5; }
    var x = function (t) { return P + (t1 === t0 ? .5 : (t - t0) / (t1 - t0)) * (W - P * 2); };
    var y = function (v) { return H - P - (v - lo) / (hi - lo) * (H - P * 2); };
    var unit = UNITS[kind][1];
    var svg = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="' + esc(UNITS[kind][0]) + ' over time">' +
      '<line class="chart__axis" x1="' + P + '" x2="' + (W - P) + '" y1="' + (H - P) + '" y2="' + (H - P) + '"/>' +
      '<text class="chart__lbl" x="' + P + '" y="' + (y(hi) - 8) + '">' + hi.toFixed(1) + " " + unit + "</text>" +
      '<text class="chart__lbl" x="' + P + '" y="' + (y(lo) + 18) + '">' + lo.toFixed(1) + " " + unit + "</text>" +
      '<text class="chart__lbl" x="' + P + '" y="' + (H - 8) + '">' + esc(fmtDate(t0)) + "</text>" +
      '<text class="chart__lbl" text-anchor="end" x="' + (W - P) + '" y="' + (H - 8) + '">' + esc(fmtDate(t1)) + "</text>";
    pts.forEach(function (p) { svg += '<circle class="chart__dot" cx="' + x(p.t).toFixed(1) + '" cy="' + y(p.v).toFixed(1) + '" r="3"/>'; });
    svg += '<polyline class="chart__line" points="' + avg.map(function (p) { return x(p.t).toFixed(1) + "," + y(p.v).toFixed(1); }).join(" ") + '"/></svg>';
    box.innerHTML = svg;

    // Change in the trend over the last 28 days of entries.
    var last = avg[avg.length - 1];
    var past = avg.filter(function (p) { return p.t <= last.t - 28 * 864e5; }).pop() || avg[0];
    var diff = last.v - past.v;
    var days = Math.max(1, Math.round((last.t - past.t) / 864e5));
    note.innerHTML = "Trend now <strong>" + last.v.toFixed(1) + " " + unit + "</strong>, " +
      (diff === 0 ? "no change" : (diff > 0 ? "up " : "down ") + Math.abs(diff).toFixed(1) + " " + unit) +
      " over " + days + " day" + (days === 1 ? "" : "s") + ".";
  }

  function drawBest() {
    var best = {};
    logs.forEach(function (l) {
      if (l.kind !== "lift" || !l.exercise) return;
      var reps = l.reps || 1;
      var e1rm = reps === 1 ? +l.value : l.value * (1 + reps / 30);
      var k = l.exercise.toLowerCase();
      if (!best[k] || e1rm > best[k].e) best[k] = { name: l.exercise, e: e1rm, set: l.value + " kg x " + reps, on: l.logged_on };
    });
    var rows = Object.keys(best).map(function (k) { return best[k]; }).sort(function (a, b) { return b.e - a.e; });
    $("[data-best]").innerHTML = rows.length
      ? '<table class="wtable"><thead><tr><th>Lift</th><th>Est. 1RM</th><th>Best set</th></tr></thead><tbody>' +
        rows.map(function (r) {
          return "<tr><td>" + esc(r.name) + "</td><td><strong>" + r.e.toFixed(1) + " kg</strong></td><td>" + esc(r.set) + "</td></tr>";
        }).join("") + "</tbody></table>"
      : '<p class="field__hint">Log a lift to see it here.</p>';
  }

  function drawRecent() {
    var rows = logs.slice(-12).reverse();
    $("[data-recent]").innerHTML = rows.length
      ? '<table class="wtable"><tbody>' + rows.map(function (l) {
          var what = l.kind === "lift" ? esc(l.exercise) + " " + esc(l.value) + " kg x " + esc(l.reps || 1)
            : esc(UNITS[l.kind][0]) + " " + esc(l.value) + " " + UNITS[l.kind][1];
          return "<tr><td>" + esc(fmtDate(l.logged_on)) + "</td><td>" + what +
            '</td><td class="wtable__x"><button type="button" class="linkbtn" data-del="' + esc(l.id) + '" aria-label="Delete entry">&times;</button></td></tr>';
        }).join("") + "</tbody></table>"
      : '<p class="field__hint">Nothing logged yet.</p>';
  }

  load();
})();
