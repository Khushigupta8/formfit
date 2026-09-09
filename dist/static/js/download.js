/* FormFit - the download page.
 *
 * The resizer hands the finished file over in sessionStorage and sends the
 * visitor here. Nothing is uploaded and nothing is fetched; this page only
 * reads what the previous page put down, verifies it, and hands it over.
 *
 * The checks below are real. They are computed on the tool page from the
 * actual output pixels and only displayed here. They are revealed one at a
 * time because a list that appears all at once does not get read.
 */

(function () {
  "use strict";

  var KEY = "formfit:result";
  var $ = function (id) { return document.getElementById(id); };

  var PRESETS = JSON.parse(document.getElementById("presetData").textContent);
  var SLUGS = JSON.parse(document.getElementById("slugMap").textContent);

  var data = null;
  try {
    var raw = sessionStorage.getItem(KEY);
    if (raw) data = JSON.parse(raw);
  } catch (e) { data = null; }

  if (!data || !data.dataUrl) {
    $("dlEmpty").hidden = false;
    return;
  }
  $("dlReady").hidden = false;

  var isSign = /sign|thumb|declaration/i.test(data.kind || "");
  var noun = isSign ? (/thumb/i.test(data.kind || "") ? "thumb impression" : "signature") : "photo";

  /* ---------- header ---------- */

  // The preset label already names the document ("SSC photo"), so the noun
  // is only there for the custom sizes that have no label at all.
  var what = data.examLabel || noun;

  document.title = what.charAt(0).toUpperCase() + what.slice(1) +
    " ready to download | FormFit";

  $("dlTitle").textContent = "Your " + what + " is ready";

  $("dlSub").textContent = "Resized to " + data.width + " x " + data.height +
    " pixels and " + data.kb + " KB, which is what the form asks for. " +
    "It never left your device - the work happened in this browser.";

  $("dlImg").src = data.dataUrl;
  $("dlImg").style.width = Math.min(data.width, 340) + "px";

  if (data.slug) $("dlAgain").href = "/" + data.slug;

  /* ---------- the download itself ----------
     A blob URL rather than the data URL: some mobile browsers refuse to
     download a data: href, and a 60 KB base64 string in an attribute is
     wasteful when the bytes are right here. */

  var btn = $("dlBtn");
  var objectUrl = null;
  try {
    var parts = data.dataUrl.split(",");
    var bin = atob(parts[1]);
    var buf = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) buf[i] = bin.charCodeAt(i);
    objectUrl = URL.createObjectURL(new Blob([buf], { type: "image/jpeg" }));
  } catch (e) {
    objectUrl = data.dataUrl;
  }
  btn.href = objectUrl;
  btn.download = data.filename || "image.jpg";

  /* ---------- checks, revealed one at a time ---------- */

  function row(label, state, value) {
    var li = document.createElement("li");
    li.className = "is-new";
    var t = document.createElement("span");
    t.className = "tick" + (state === "no" ? " tick--no" : state === "warn" ? " tick--warn" : "");
    t.textContent = state === "no" ? "!" : state === "warn" ? "~" : "OK";
    var x = document.createElement("span"); x.textContent = label;
    var v = document.createElement("span"); v.className = "val"; v.textContent = value;
    li.appendChild(t); li.appendChild(x); li.appendChild(v);
    return li;
  }

  var checks = [
    ["Pixel size", "ok", data.width + " x " + data.height],
    ["File size", data.size_ok ? "ok" : "no",
      data.kb + " KB  (need " + data.min_kb + "-" + data.max_kb + ")"],
    ["Format", "ok", "JPG, baseline"],
    ["Orientation", "ok", "upright"],
    ["Colour", "ok", data.grayscale ? "black and white" : "colour"],
    ["Source resolution",
      (data.original_w >= data.width && data.original_h >= data.height) ? "ok" : "warn",
      data.original_w + " x " + data.original_h]
  ];

  var list = $("dlChecks");
  var idx = 0;

  function step() {
    if (idx >= checks.length) { finish(); return; }
    var c = checks[idx++];
    list.appendChild(row(c[0], c[1], c[2]));
    setTimeout(step, 320);
  }
  setTimeout(step, 260);

  function finish() {
    var failed = checks.some(function (c) { return c[1] === "no"; });
    $("dlChecksTitle").textContent = failed ? "One thing to look at" : "All checks passed";
    $("dlEyebrow").textContent = failed ? "Check before you upload" : "Checked and ready";

    btn.classList.remove("is-waiting");
    btn.removeAttribute("aria-disabled");
    // The name goes on its own line rather than into the button. Filenames
    // run to thirty characters and a button is the one place on a 320 px
    // screen that cannot afford to grow.
    btn.textContent = "Download JPG";
    $("dlFilename").textContent = data.filename || "image.jpg";

    if (data.over_limit) {
      $("dlMeta").textContent = "This canvas could not be squeezed under " +
        data.max_kb + " KB without wrecking it. Try smaller pixel dimensions.";
    } else if (data.padded) {
      $("dlMeta").textContent = "The image compressed below the minimum, so invisible " +
        "filler bytes were added to lift it into range. The pixels are untouched and " +
        "every portal reads it as a normal JPG.";
    } else {
      $("dlMeta").textContent = "Came from " + data.original_w + " x " + data.original_h +
        " at " + data.original_kb + " KB.";
    }

    showQuality();
    showKit();
  }

  /* ---------- quality report ----------
     Measured on the tool page from the output canvas. Thresholds are
     deliberately forgiving: a false alarm on a fine photo costs more trust
     than a missed warning. */

  function showQuality() {
    var q = data.q;
    if (!q) return;

    var score = 100;
    var items = [];

    function add(label, state, text, href, linkText) {
      items.push({ label: label, state: state, text: text, href: href, linkText: linkText });
    }

    // Sharpness. Variance of the Laplacian, the standard cheap blur measure.
    if (q.sharpness < 18) {
      score -= 30;
      add("Sharpness", "no",
        "This looks blurred. At " + data.width + " x " + data.height + " pixels a soft " +
        "image is what verification staff notice first.",
        "/guides/photo-rejected-in-online-form", "Why photos get rejected");
    } else if (q.sharpness < 55) {
      score -= 12;
      add("Sharpness", "warn",
        "Slightly soft. Usually fine, but if you have a steadier shot use that one.");
    } else {
      add("Sharpness", "ok", "Crisp at this size.");
    }

    // Exposure.
    if (q.mean < 78) {
      score -= 18;
      add("Brightness", "no",
        "Underexposed. Faces go muddy at this level once the portal compresses it again.",
        "/guides/passport-size-photo-at-home", "Lighting at home");
    } else if (q.mean > 214) {
      score -= 14;
      add("Brightness", "warn",
        "Very bright. Detail may be washing out in the light areas.");
    } else {
      add("Brightness", "ok", "Well exposed.");
    }

    // Contrast.
    if (q.contrast < 22) {
      score -= 10;
      add("Contrast", "warn", "Flat. A little more light on the subject would help.");
    } else {
      add("Contrast", "ok", "Good separation between subject and background.");
    }

    // Background, judged from the border pixels.
    if (isSign) {
      if (q.border < 205) {
        score -= 16;
        add("Paper", "warn",
          "The paper behind the " + noun + " is not reading as white. Tick " +
          "“Clean the paper to white” on the resizer and run it again.",
          "/guides/how-to-scan-signature-with-phone", "Scanning a signature properly");
      } else {
        add("Paper", "ok", "Reads as clean white.");
      }
    } else {
      if (q.border < 150) {
        score -= 16;
        add("Background", "warn",
          "The background is dark. Most exam bodies ask for a plain white or light " +
          "coloured background and reject busy ones.",
          "/guides/photo-rejected-in-online-form", "What gets a photo rejected");
      } else {
        add("Background", "ok", "Plain and light.");
      }
    }

    // Upscaling. Enlarging a small source invents detail that is not there.
    if (data.original_w < data.width || data.original_h < data.height) {
      score -= 20;
      add("Source", "no",
        "The original was smaller than " + data.width + " x " + data.height +
        ", so it had to be enlarged. Use the full-size original from your camera roll.",
        "/guides/how-to-reduce-photo-size-to-20-kb", "Working from the original");
    } else if (data.original_w > data.width * 6) {
      add("Source", "ok", "Plenty of resolution to work from.");
    } else {
      add("Source", "ok", "Enough resolution to work from.");
    }

    if (!data.size_ok) score -= 25;

    score = Math.max(5, Math.min(100, Math.round(score)));

    $("qualityScore").textContent = score;
    $("qualityRing").style.setProperty("--pct", score);
    $("qualityRing").classList.add(score >= 80 ? "ring--good" : score >= 55 ? "ring--warn" : "ring--bad");

    $("qualityVerdict").textContent =
      score >= 88 ? "Nothing to fix. Upload it." :
      score >= 70 ? "Fine to upload. One or two things below could be better." :
      score >= 50 ? "Usable, but the points below are the ones that get files sent back." :
                    "Worth redoing before you upload. Here is what is wrong.";

    var ul = $("qualityList");
    ul.innerHTML = "";
    items.forEach(function (it) {
      var li = document.createElement("li");
      li.className = "quality__item quality__item--" + it.state;

      var head = document.createElement("span");
      head.className = "quality__label";
      head.textContent = it.label;

      var body = document.createElement("span");
      body.className = "quality__text";
      body.textContent = it.text;

      li.appendChild(head);
      li.appendChild(body);

      if (it.href) {
        var a = document.createElement("a");
        a.className = "quality__link";
        a.href = it.href;
        a.textContent = it.linkText + " →";
        li.appendChild(a);
      }
      ul.appendChild(li);
    });

    $("qualityCard").hidden = false;
  }

  /* ---------- the rest of the kit ---------- */

  function showKit() {
    if (!window.FormFitKit || !data.exam) return;
    window.FormFitKit.render({
      card: $("kitCard"), exam: $("kitExam"), sub: $("kitSub"),
      fill: $("kitFill"), list: $("kitList"), actions: $("kitActions")
    }, { presets: PRESETS, slugMap: SLUGS, exam: data.exam, currentId: data.presetId });
  }
})();
