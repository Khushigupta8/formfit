/* FormFit - all image work happens in the visitor's browser.
   Nothing is uploaded, so there is no request size limit to hit and no
   server cost per resize. Also means the site can be hosted as plain
   static files. */

(function () {
  "use strict";

  var PRESETS = JSON.parse(document.getElementById("presetData").textContent);
  var $ = function (id) { return document.getElementById(id); };

  // preset id -> the page that covers it. Merged pages mean a preset's own
  // slug is not always a URL that exists.
  var SLUGS = {};
  var slugNode = document.getElementById("slugMap");
  if (slugNode) { try { SLUGS = JSON.parse(slugNode.textContent); } catch (e) { SLUGS = {}; } }

  // Exam pages tell us which preset to open with, so the visitor lands on
  // exactly the size they searched for.
  var PRESELECT = null;
  var pre = document.getElementById("preselect");
  if (pre) { try { PRESELECT = JSON.parse(pre.textContent); } catch (e) { PRESELECT = null; } }

  var dropzone = $("dropzone"), fileInput = $("fileInput"), preview = $("preview"),
      emptyState = $("emptyState"), fileCaption = $("fileCaption"),
      examSelect = $("examSelect"), kindChips = $("kindChips"), presetNote = $("presetNote"),
      goBtn = $("goBtn"), result = $("result"), resultImg = $("resultImg"),
      checklist = $("checklist"), downloadBtn = $("downloadBtn"), againBtn = $("againBtn"),
      resultMeta = $("resultMeta"), alertBox = $("alert");

  var chosenFile = null, activePreset = null, leaving = false;

  /* ---------- presets ---------- */

  var exams = [];
  PRESETS.forEach(function (p) { if (exams.indexOf(p.exam) === -1) exams.push(p.exam); });
  exams.forEach(function (n) {
    var o = document.createElement("option"); o.value = n; o.textContent = n;
    examSelect.appendChild(o);
  });
  var co = document.createElement("option");
  co.value = "__custom"; co.textContent = "Something else, I'll type the sizes";
  examSelect.appendChild(co);

  function renderKinds() {
    kindChips.innerHTML = "";
    if (examSelect.value === "__custom") {
      activePreset = null;
      presetNote.textContent = "Enter the width, height and KB range printed in your notification.";
      return;
    }
    PRESETS.filter(function (p) { return p.exam === examSelect.value; })
      .forEach(function (p, i) {
        var b = document.createElement("button");
        b.type = "button"; b.className = "chip"; b.textContent = p.kind;
        b.addEventListener("click", function () { applyPreset(p); });
        kindChips.appendChild(b);
        if (i === 0) applyPreset(p);
      });
  }

  function applyPreset(p) {
    activePreset = p;
    $("width").value = p.w; $("height").value = p.h;
    $("minKb").value = p.min_kb; $("maxKb").value = p.max_kb;
    var isSign = /sign|thumb|declaration/i.test(p.kind);
    $("mode").value = isSign ? "contain" : "cover";
    $("whiten").checked = /sign|declaration/i.test(p.kind);
    presetNote.textContent = p.note + ", " + p.w + " x " + p.h +
      " px, " + p.min_kb + " to " + p.max_kb + " KB";
    Array.prototype.forEach.call(kindChips.children, function (c) {
      c.classList.toggle("is-on", c.textContent === p.kind);
    });
    paintKit();
  }

  examSelect.addEventListener("change", renderKinds);

  /* The kit card under the tool. It only appears once the visitor has
     actually finished one file for this exam - before that there is nothing
     to report and an empty progress bar is just noise. */
  function paintKit() {
    if (!window.FormFitKit || !$("formKit") || !activePreset) return;
    var done = window.FormFitKit.doneFor(activePreset.exam);
    if (!Object.keys(done).length) { $("formKit").hidden = true; return; }
    window.FormFitKit.render({
      card: $("formKit"), exam: $("kitExam"), sub: $("kitSub"),
      fill: $("kitFill"), list: $("kitList"), actions: $("kitActions")
    }, { presets: PRESETS, slugMap: SLUGS, exam: activePreset.exam,
         currentId: activePreset.id });
  }

  if (PRESELECT) {
    var wanted = PRESETS.filter(function (p) { return p.id === PRESELECT; })[0];
    if (wanted) {
      examSelect.value = wanted.exam;
      renderKinds();
      applyPreset(wanted);
    } else { renderKinds(); }
  } else {
    renderKinds();
  }

  /* ---------- file intake ---------- */

  function acceptFile(f) {
    if (!f) return;
    if (!/^image\//.test(f.type)) { showAlert("That's not an image. Use a JPG, PNG or WEBP file."); return; }
    if (f.size > 12 * 1024 * 1024) { showAlert("That file is over 12 MB. Use a smaller one."); return; }
    hideAlert();
    chosenFile = f;
    var r = new FileReader();
    r.onload = function (e) { preview.src = e.target.result; preview.hidden = false; emptyState.hidden = true; };
    r.readAsDataURL(f);
    fileCaption.textContent = f.name + "  ·  " + (f.size / 1024).toFixed(0) + " KB";
    goBtn.disabled = false;
  }

  dropzone.addEventListener("click", function () { fileInput.click(); });
  dropzone.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); fileInput.click(); }
  });
  fileInput.addEventListener("change", function () { acceptFile(fileInput.files[0]); });
  ["dragenter", "dragover"].forEach(function (ev) {
    dropzone.addEventListener(ev, function (e) { e.preventDefault(); dropzone.classList.add("is-dragging"); });
  });
  ["dragleave", "drop"].forEach(function (ev) {
    dropzone.addEventListener(ev, function (e) { e.preventDefault(); dropzone.classList.remove("is-dragging"); });
  });
  dropzone.addEventListener("drop", function (e) {
    if (e.dataTransfer.files.length) acceptFile(e.dataTransfer.files[0]);
  });

  function showAlert(m) { alertBox.textContent = m; alertBox.hidden = false; }
  function hideAlert() { alertBox.hidden = true; }

  /* ---------- image processing ---------- */

  function loadBitmap(file) {
    // imageOrientation:'from-image' applies the EXIF rotation tag, which is
    // what stops phone photos arriving sideways.
    if (window.createImageBitmap) {
      return createImageBitmap(file, { imageOrientation: "from-image" })
        .catch(function () { return loadViaImg(file); });
    }
    return loadViaImg(file);
  }

  function loadViaImg(file) {
    return new Promise(function (res, rej) {
      var img = new Image();
      img.onload = function () { res(img); };
      img.onerror = function () { rej(new Error("That file isn't a readable image.")); };
      img.src = URL.createObjectURL(file);
    });
  }

  function drawCanvas(src, w, h, mode) {
    var c = document.createElement("canvas");
    c.width = w; c.height = h;
    var g = c.getContext("2d");
    g.fillStyle = "#ffffff";
    g.fillRect(0, 0, w, h);
    g.imageSmoothingQuality = "high";

    var sw = src.width, sh = src.height;

    if (mode === "stretch") {
      g.drawImage(src, 0, 0, w, h);
    } else if (mode === "contain") {
      var s = Math.min(w / sw, h / sh);
      var dw = sw * s, dh = sh * s;
      g.drawImage(src, (w - dw) / 2, (h - dh) / 2, dw, dh);
    } else {
      // cover: crop to fill, biased slightly above centre so faces sit right
      var sc = Math.max(w / sw, h / sh);
      var cw = w / sc, ch = h / sc;
      g.drawImage(src, (sw - cw) / 2, (sh - ch) * 0.4, cw, ch, 0, 0, w, h);
    }
    return c;
  }

  function whiten(canvas, threshold) {
    var g = canvas.getContext("2d");
    var d = g.getImageData(0, 0, canvas.width, canvas.height);
    var p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var lum = 0.299 * p[i] + 0.587 * p[i + 1] + 0.114 * p[i + 2];
      if (lum > threshold) { p[i] = 255; p[i + 1] = 255; p[i + 2] = 255; }
    }
    g.putImageData(d, 0, 0);
    return canvas;
  }

  function greyscale(canvas) {
    var g = canvas.getContext("2d");
    var d = g.getImageData(0, 0, canvas.width, canvas.height);
    var p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var v = 0.299 * p[i] + 0.587 * p[i + 1] + 0.114 * p[i + 2];
      p[i] = p[i + 1] = p[i + 2] = v;
    }
    g.putImageData(d, 0, 0);
    return canvas;
  }

  function encode(canvas, q) {
    return new Promise(function (res) {
      canvas.toBlob(function (b) { res(b); }, "image/jpeg", q / 100);
    });
  }

  // Grow a JPEG to a minimum size with comment segments. Decoders skip
  // them, so file size moves and pixels don't.
  function padJpeg(bytes, target) {
    var need = target - bytes.length;
    if (need <= 0) return bytes;
    var segs = [], remaining = need;
    while (remaining > 4) {
      var payload = Math.min(remaining - 4, 65531);
      var s = new Uint8Array(payload + 4);
      s[0] = 0xFF; s[1] = 0xFE;
      s[2] = ((payload + 2) >> 8) & 0xFF;
      s[3] = (payload + 2) & 0xFF;
      s.fill(0x20, 4);
      segs.push(s);
      remaining -= payload + 4;
    }
    var extra = segs.reduce(function (a, s) { return a + s.length; }, 0);
    var out = new Uint8Array(bytes.length + extra);
    out.set(bytes.subarray(0, 2), 0);
    var off = 2;
    segs.forEach(function (s) { out.set(s, off); off += s.length; });
    out.set(bytes.subarray(2), off);
    return out;
  }

  /* Cheap image statistics, read straight off the output canvas. The
     download page turns these into the quality report. All of it is
     arithmetic on pixels already in memory, so it costs a few milliseconds
     and nothing leaves the browser.

       mean      average luminance, i.e. exposure
       contrast  standard deviation of luminance
       sharpness variance of the Laplacian, the usual cheap blur measure
       border    average luminance of the outermost ring of pixels, which is
                 the background behind a face or the paper behind a signature
  */
  function analyse(canvas) {
    var w = canvas.width, h = canvas.height;
    var d = canvas.getContext("2d").getImageData(0, 0, w, h).data;
    var lum = new Float32Array(w * h);
    var sum = 0, i, p;

    for (i = 0, p = 0; p < d.length; p += 4, i++) {
      var v = 0.299 * d[p] + 0.587 * d[p + 1] + 0.114 * d[p + 2];
      lum[i] = v; sum += v;
    }
    var mean = sum / lum.length;

    var acc = 0;
    for (i = 0; i < lum.length; i++) { var dv = lum[i] - mean; acc += dv * dv; }
    var contrast = Math.sqrt(acc / lum.length);

    var lSum = 0, lSq = 0, n = 0;
    for (var y = 1; y < h - 1; y++) {
      for (var x = 1; x < w - 1; x++) {
        var k = y * w + x;
        var L = 4 * lum[k] - lum[k - 1] - lum[k + 1] - lum[k - w] - lum[k + w];
        lSum += L; lSq += L * L; n++;
      }
    }
    var sharpness = n ? (lSq / n) - Math.pow(lSum / n, 2) : 0;

    var bSum = 0, bN = 0;
    for (x = 0; x < w; x++) { bSum += lum[x] + lum[(h - 1) * w + x]; bN += 2; }
    for (y = 0; y < h; y++) { bSum += lum[y * w] + lum[y * w + w - 1]; bN += 2; }

    return {
      mean: +mean.toFixed(1),
      contrast: +contrast.toFixed(1),
      sharpness: +sharpness.toFixed(1),
      border: +(bSum / bN).toFixed(1)
    };
  }

  async function process(file, o) {
    var src = await loadBitmap(file);
    var originalW = src.width, originalH = src.height;

    var canvas = drawCanvas(src, o.width, o.height, o.mode);
    if (o.whiten) whiten(canvas, 200);
    if (o.grayscale) greyscale(canvas);

    var maxBytes = o.maxKb * 1024, minBytes = o.minKb * 1024;

    // highest quality that still fits under the ceiling
    var lo = 5, hi = 95, best = null;
    while (lo <= hi) {
      var mid = (lo + hi) >> 1;
      var blob = await encode(canvas, mid);
      if (blob.size <= maxBytes) { best = blob; lo = mid + 1; } else { hi = mid - 1; }
    }
    var overLimit = false;
    if (!best) { best = await encode(canvas, 5); overLimit = best.size > maxBytes; }

    var bytes = new Uint8Array(await best.arrayBuffer());
    var padded = false;

    if (bytes.length < minBytes) {
      var grown = null;
      for (var q of [96, 98, 100]) {
        var b2 = await encode(canvas, q);
        if (b2.size >= minBytes && b2.size <= maxBytes) { grown = b2; break; }
      }
      if (grown) {
        bytes = new Uint8Array(await grown.arrayBuffer());
      } else {
        bytes = padJpeg(bytes, minBytes);
        padded = true;
      }
    }

    return {
      bytes: bytes,
      q: analyse(canvas),
      grayscale: !!o.grayscale,
      original_w: originalW, original_h: originalH,
      original_kb: +(file.size / 1024).toFixed(1),
      width: o.width, height: o.height,
      kb: +(bytes.length / 1024).toFixed(1),
      min_kb: o.minKb, max_kb: o.maxKb,
      padded: padded, over_limit: overLimit,
      size_ok: bytes.length >= minBytes && bytes.length <= maxBytes
    };
  }

  /* ---------- run ---------- */

  goBtn.addEventListener("click", async function () {
    if (!chosenFile) return;
    var minKb = parseInt($("minKb").value, 10), maxKb = parseInt($("maxKb").value, 10);
    if (!(minKb < maxKb)) { showAlert("The smallest size has to be lower than the largest size."); return; }

    hideAlert();
    goBtn.disabled = true;
    goBtn.textContent = "Resizing…";

    try {
      var d = await process(chosenFile, {
        width: Math.max(20, Math.min(2000, parseInt($("width").value, 10) || 200)),
        height: Math.max(20, Math.min(2000, parseInt($("height").value, 10) || 230)),
        minKb: minKb, maxKb: maxKb,
        mode: $("mode").value,
        whiten: $("whiten").checked,
        grayscale: $("grayscale").checked
      });
      await handoff(d);
    } catch (err) {
      showAlert(err.message || "Something broke while processing. Try another file.");
    } finally {
      // Not when we are on our way to /download: putting the button back
      // invites a second click during the moment the next page is loading.
      if (!leaving) {
        goBtn.disabled = false;
        goBtn.textContent = "Resize photo";
      }
    }
  });

  function row(label, ok, value) {
    var li = document.createElement("li");
    var t = document.createElement("span");
    t.className = "tick" + (ok ? "" : " tick--no");
    t.textContent = ok ? "OK" : "!";
    var x = document.createElement("span"); x.textContent = label;
    var v = document.createElement("span"); v.className = "val"; v.textContent = value;
    li.appendChild(t); li.appendChild(x); li.appendChild(v);
    return li;
  }

  function toDataUrl(bytes) {
    return new Promise(function (res, rej) {
      var fr = new FileReader();
      fr.onload = function () { res(fr.result); };
      fr.onerror = function () { rej(new Error("Couldn't build the download.")); };
      fr.readAsDataURL(new Blob([bytes], { type: "image/jpeg" }));
    });
  }

  function fileNameFor(d) {
    var kind = activePreset ? activePreset.kind.toLowerCase().replace(/\s+/g, "-") : "image";
    var exam = activePreset ? activePreset.exam.toLowerCase().replace(/[^a-z]+/g, "-") : "custom";
    return exam + "-" + kind + "-" + d.width + "x" + d.height + ".jpg";
  }

  /* The finished file goes to /download rather than appearing under the tool.

     It travels in sessionStorage, which means it is still only ever in this
     browser - the download page fetches nothing. If storage refuses (private
     mode on some browsers, or a file large enough to blow the quota) the old
     in-page result panel is used instead, so nobody ends up unable to get
     their image. */
  async function handoff(d) {
    var url = await toDataUrl(d.bytes);
    var payload = {
      dataUrl: url,
      filename: fileNameFor(d),
      width: d.width, height: d.height, kb: d.kb,
      min_kb: d.min_kb, max_kb: d.max_kb,
      size_ok: d.size_ok, padded: d.padded, over_limit: d.over_limit,
      grayscale: d.grayscale,
      original_w: d.original_w, original_h: d.original_h, original_kb: d.original_kb,
      q: d.q,
      presetId: activePreset ? activePreset.id : null,
      exam: activePreset ? activePreset.exam : null,
      kind: activePreset ? activePreset.kind : null,
      examLabel: activePreset ? (activePreset.label || activePreset.exam) : null,
      slug: activePreset ? (SLUGS[activePreset.id] || activePreset.slug) : null,
      at: Date.now()
    };

    try {
      sessionStorage.setItem("formfit:result", JSON.stringify(payload));
    } catch (e) {
      await render(d, url);
      return;
    }

    if (window.FormFitKit && activePreset) {
      window.FormFitKit.record(activePreset);
      window.FormFitKit.store(activePreset, payload.filename, url);
    }

    leaving = true;
    goBtn.textContent = "Opening your file…";
    window.location.href = "/download";
  }

  async function render(d, prebuilt) {
    var url = prebuilt || await toDataUrl(d.bytes);
    resultImg.onerror = function () {
      showAlert("The image was built correctly but your browser won't preview it. " +
                "Download JPG still works.");
    };
    resultImg.src = url;
    resultImg.style.width = Math.min(d.width, 340) + "px";
    downloadBtn.href = url;

    downloadBtn.download = fileNameFor(d);

    checklist.innerHTML = "";
    checklist.appendChild(row("Pixel size", true, d.width + " x " + d.height));
    checklist.appendChild(row("File size", d.size_ok, d.kb + " KB  (need " + d.min_kb + "-" + d.max_kb + ")"));
    checklist.appendChild(row("Format", true, "JPG"));

    if (d.over_limit) {
      resultMeta.textContent = "This canvas can't be squeezed under " + d.max_kb +
        " KB without wrecking it. Try smaller pixel dimensions.";
    } else if (d.padded) {
      resultMeta.textContent = "The image compressed below the minimum, so invisible filler " +
        "was added to lift it into range. Pixels are untouched.";
    } else {
      resultMeta.textContent = "Came from " + d.original_w + " x " + d.original_h +
        " at " + d.original_kb + " KB.";
    }

    result.hidden = false;
    result.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  againBtn.addEventListener("click", function () {
    chosenFile = null; fileInput.value = "";
    preview.hidden = true; preview.src = "";
    emptyState.hidden = false;
    fileCaption.textContent = "No file chosen yet";
    goBtn.disabled = true; result.hidden = true; hideAlert();
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
})();
