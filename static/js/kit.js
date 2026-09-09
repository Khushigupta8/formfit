/* FormFit - the upload kit tracker.
 *
 * An exam form almost never wants one image. SSC wants a photo and a
 * signature, IBPS adds a thumb impression and a handwritten declaration.
 * People do them one at a time, on different days, and turn up at the portal
 * missing one. This remembers which ones are done, per exam, in localStorage,
 * and is the thing that turns a single visit into four.
 *
 * It also keeps the finished files themselves, so someone who resized their
 * photo yesterday and their signature today can take both away in one go.
 * They live in this browser's own storage and nowhere else - the same place
 * the rest of the site keeps things, never a server.
 */

window.FormFitKit = (function () {
  "use strict";

  var KEY = "formfit:kit:v1";
  var FILES = "formfit:files:v1";
  // localStorage is a few megabytes at most and shared with everything else
  // on the origin. A form image is 20-100 KB, so this ceiling is generous
  // and still leaves no way for the kit to fill the quota.
  var MAX_FILE = 400 * 1024;

  function read() {
    try {
      var raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  function write(state) {
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
  }

  function record(preset) {
    if (!preset || !preset.exam || !preset.id) return;
    var s = read();
    if (!s.exams) s.exams = {};
    if (!s.exams[preset.exam]) s.exams[preset.exam] = {};
    s.exams[preset.exam][preset.id] = Date.now();
    s.last = preset.exam;
    write(s);
  }

  function doneFor(exam) {
    var s = read();
    return (s.exams && s.exams[exam]) || {};
  }

  function lastExam() { return read().last || null; }

  function forget() {
    try { localStorage.removeItem(KEY); localStorage.removeItem(FILES); } catch (e) {}
  }

  /* ---------- the files themselves ---------- */

  function readFiles() {
    try {
      var raw = localStorage.getItem(FILES);
      return raw ? JSON.parse(raw) : {};
    } catch (e) { return {}; }
  }

  /* Kept separate from the progress record on purpose: if the quota refuses
     the image, the tick against that document must still stand. */
  function store(preset, filename, dataUrl) {
    if (!preset || !dataUrl || dataUrl.length > MAX_FILE) return false;
    var all = readFiles();
    if (!all[preset.exam]) all[preset.exam] = {};
    all[preset.exam][preset.id] = { name: filename, url: dataUrl, at: Date.now() };
    try {
      localStorage.setItem(FILES, JSON.stringify(all));
      return true;
    } catch (e) {
      // Out of room. Drop everything but what was just made and try once more.
      var only = {};
      only[preset.exam] = {};
      only[preset.exam][preset.id] = all[preset.exam][preset.id];
      try { localStorage.setItem(FILES, JSON.stringify(only)); return true; }
      catch (e2) { return false; }
    }
  }

  function fileFor(exam, id) {
    var all = readFiles();
    return (all[exam] && all[exam][id]) || null;
  }

  function bytesOf(dataUrl) {
    var bin = atob(dataUrl.split(",")[1]);
    var out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  function saveAs(blob, name) {
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url; a.download = name;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
  }

  /* ---------- zip ----------
     Stored, not deflated. JPEGs are already compressed, so deflating them
     saves nothing and would mean shipping a compression library to every
     visitor for no gain. This is about eighty lines and no dependency. */

  var CRC_TABLE = (function () {
    var t = new Uint32Array(256);
    for (var n = 0; n < 256; n++) {
      var c = n;
      for (var k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1);
      t[n] = c >>> 0;
    }
    return t;
  })();

  function crc32(buf) {
    var c = 0xFFFFFFFF;
    for (var i = 0; i < buf.length; i++) c = CRC_TABLE[(c ^ buf[i]) & 0xFF] ^ (c >>> 8);
    return (c ^ 0xFFFFFFFF) >>> 0;
  }

  function dosTime(d) {
    return ((d.getHours() << 11) | (d.getMinutes() << 5) | (d.getSeconds() / 2)) & 0xFFFF;
  }
  function dosDate(d) {
    return (((d.getFullYear() - 1980) << 9) | ((d.getMonth() + 1) << 5) | d.getDate()) & 0xFFFF;
  }

  function zip(entries) {
    var now = new Date(), time = dosTime(now), date = dosDate(now);
    var parts = [], central = [], offset = 0;

    entries.forEach(function (e) {
      var name = new TextEncoder().encode(e.name);
      var crc = crc32(e.bytes), size = e.bytes.length;

      var local = new DataView(new ArrayBuffer(30));
      local.setUint32(0, 0x04034b50, true);
      local.setUint16(4, 20, true);      // version needed
      local.setUint16(6, 0, true);       // flags
      local.setUint16(8, 0, true);       // method: stored
      local.setUint16(10, time, true);
      local.setUint16(12, date, true);
      local.setUint32(14, crc, true);
      local.setUint32(18, size, true);
      local.setUint32(22, size, true);
      local.setUint16(26, name.length, true);
      local.setUint16(28, 0, true);

      parts.push(new Uint8Array(local.buffer), name, e.bytes);

      var cd = new DataView(new ArrayBuffer(46));
      cd.setUint32(0, 0x02014b50, true);
      cd.setUint16(4, 20, true);         // version made by
      cd.setUint16(6, 20, true);         // version needed
      cd.setUint16(8, 0, true);
      cd.setUint16(10, 0, true);
      cd.setUint16(12, time, true);
      cd.setUint16(14, date, true);
      cd.setUint32(16, crc, true);
      cd.setUint32(20, size, true);
      cd.setUint32(24, size, true);
      cd.setUint16(28, name.length, true);
      cd.setUint32(42, offset, true);
      central.push(new Uint8Array(cd.buffer), name);

      offset += 30 + name.length + size;
    });

    var cdSize = central.reduce(function (a, p) { return a + p.length; }, 0);
    var end = new DataView(new ArrayBuffer(22));
    end.setUint32(0, 0x06054b50, true);
    end.setUint16(8, entries.length, true);
    end.setUint16(10, entries.length, true);
    end.setUint32(12, cdSize, true);
    end.setUint32(16, offset, true);

    return new Blob(parts.concat(central, [new Uint8Array(end.buffer)]),
                    { type: "application/zip" });
  }

  function downloadAll(exam, items) {
    var have = items
      .map(function (p) { return fileFor(exam, p.id); })
      .filter(Boolean)
      .map(function (f) { return { name: f.name, bytes: bytesOf(f.url) }; });

    if (!have.length) return 0;
    if (have.length === 1) {
      saveAs(new Blob([have[0].bytes], { type: "image/jpeg" }), have[0].name);
      return 1;
    }
    saveAs(zip(have), exam.toLowerCase().replace(/[^a-z0-9]+/g, "-") + "-form-files.zip");
    return have.length;
  }

  /* ---------- rendering ---------- */

  function ago(ts) {
    var mins = Math.round((Date.now() - ts) / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + " min ago";
    var hrs = Math.round(mins / 60);
    if (hrs < 24) return hrs === 1 ? "an hour ago" : hrs + " hours ago";
    var days = Math.round(hrs / 24);
    return days === 1 ? "yesterday" : days + " days ago";
  }

  /* Every preset that belongs to the same exam, in the order they were
     defined, which is the order the form asks for them. */
  function itemsFor(presets, exam) {
    return presets.filter(function (p) { return p.exam === exam; });
  }

  /**
   * Draw the kit into a card.
   *
   * els   - { card, exam, sub, fill, list }
   * opts  - { presets, slugMap, exam, currentId }
   * Returns the number still outstanding, so the caller can decide whether
   * the card is worth showing at all.
   */
  function render(els, opts) {
    var exam = opts.exam || lastExam();
    if (!exam || !els.card) return 0;

    var items = itemsFor(opts.presets, exam);
    if (items.length < 2) { return 0; }   // nothing to track, one file is the whole job

    var done = doneFor(exam);
    var pending = items.filter(function (p) { return !done[p.id]; });
    var doneCount = items.length - pending.length;

    if (els.exam) els.exam.textContent = exam;

    if (els.sub) {
      els.sub.textContent = pending.length === 0
        ? "All " + items.length + " files done. Keep them together in one folder so you are not hunting for them at the portal."
        : doneCount + " of " + items.length + " done. The " + exam +
          " form also wants " + listWords(pending.map(function (p) { return p.kind.toLowerCase(); })) + ".";
    }

    if (els.fill) {
      els.fill.style.width = Math.round((doneCount / items.length) * 100) + "%";
    }

    if (els.list) {
      els.list.innerHTML = "";
      items.forEach(function (p) {
        var slug = (opts.slugMap && opts.slugMap[p.id]) || p.slug;
        var isDone = !!done[p.id];
        var li = document.createElement("li");
        li.className = "kit__item" + (isDone ? " is-done" : "");

        var mark = document.createElement("span");
        mark.className = "kit__mark";
        mark.textContent = isDone ? "✓" : String(items.indexOf(p) + 1);

        var body = document.createElement("span");
        body.className = "kit__body";

        var a = document.createElement("a");
        a.className = "kit__name";
        a.href = "/" + slug;
        a.textContent = p.kind;
        body.appendChild(a);

        var meta = document.createElement("span");
        meta.className = "kit__meta";
        meta.textContent = p.w + " x " + p.h + " px, " + p.min_kb + "-" + p.max_kb + " KB" +
          (isDone ? "  ·  done " + ago(done[p.id]) : "");
        body.appendChild(meta);

        var actions = document.createElement("span");
        actions.className = "kit__row-actions";

        // The file itself, if this browser still has it. Someone who did the
        // photo yesterday should not have to make it again to get a copy.
        var saved = isDone ? fileFor(exam, p.id) : null;
        if (saved) {
          var dl = document.createElement("button");
          dl.type = "button";
          dl.className = "kit__cta";
          dl.textContent = "Download";
          dl.addEventListener("click", function (f) {
            return function () { saveAs(new Blob([bytesOf(f.url)], { type: "image/jpeg" }), f.name); };
          }(saved));
          actions.appendChild(dl);
        }

        var cta = document.createElement("a");
        cta.className = (isDone || saved) ? "kit__cta kit__cta--redo" : "kit__cta";
        cta.href = "/" + slug;
        cta.textContent = isDone ? "Redo" : "Do this next";
        actions.appendChild(cta);

        li.appendChild(mark);
        li.appendChild(body);
        li.appendChild(actions);
        els.list.appendChild(li);
      });
    }

    // One button for the lot. Two or more files zip; a single one comes
    // down as the JPG itself, because a zip holding one image is a nuisance.
    if (els.actions) {
      els.actions.innerHTML = "";
      var stored = items.filter(function (p) { return !!fileFor(exam, p.id); });
      if (stored.length > 1) {
        var all = document.createElement("button");
        all.type = "button";
        all.className = "go go--download kit__all";
        all.textContent = "Download all " + stored.length + " files (.zip)";
        all.addEventListener("click", function () { downloadAll(exam, items); });
        els.actions.appendChild(all);

        var note = document.createElement("p");
        note.className = "kit__note";
        note.textContent = "Kept in this browser only, on this device. Clearing your " +
          "browsing data removes them.";
        els.actions.appendChild(note);
      }
      els.actions.hidden = !els.actions.children.length;
    }

    els.card.hidden = false;
    return pending.length;
  }

  function listWords(words) {
    if (words.length === 1) return "a " + words[0];
    return "a " + words.slice(0, -1).join(", a ") + " and a " + words[words.length - 1];
  }

  return {
    record: record,
    store: store,
    fileFor: fileFor,
    downloadAll: downloadAll,
    render: render,
    doneFor: doneFor,
    lastExam: lastExam,
    itemsFor: itemsFor,
    forget: forget
  };
})();
