/* Site-wide bits: ad slot preview and the exercise filter. */
(function () {
  "use strict";

  // ?adpreview outlines every ad placement on the live site.
  if (/[?&]adpreview\b/.test(location.search)) document.body.classList.add("adpreview");

  // Exercise library filter.
  var filter = document.querySelector(".filter");
  if (filter) {
    filter.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      var m = b.getAttribute("data-filter");
      Array.prototype.forEach.call(filter.querySelectorAll("button"), function (x) { x.classList.toggle("is-on", x === b); });
      Array.prototype.forEach.call(document.querySelectorAll("#xgrid .xcard"), function (c) {
        c.hidden = m !== "all" && c.getAttribute("data-muscle") !== m;
      });
    });
  }

  // Contact form: send with fetch and show the result in place.
  var form = document.querySelector(".cform");
  if (form) {
    form.ts.value = Date.now();
    var status = form.querySelector(".cform__status");
    var btn = form.querySelector("button[type=submit]");
    var show = function (msg) { status.textContent = msg; status.hidden = !msg; };
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      Array.prototype.forEach.call(form.querySelectorAll(".cform__err"), function (x) {
        x.textContent = "";
        var f = form[x.getAttribute("data-for")];
        if (f) f.removeAttribute("aria-invalid");
      });
      show("");
      var data = {};
      Array.prototype.forEach.call(form.elements, function (el) { if (el.name) data[el.name] = el.value; });
      btn.disabled = true;
      btn.textContent = "Sending...";
      fetch(form.action, {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(data)
      }).then(function (r) {
        return r.json().catch(function () { return { ok: false }; });
      }).then(function (res) {
        if (res.ok) {
          form.reset();
          var ok = document.getElementById("sent");
          ok.classList.add("is-on");
          ok.scrollIntoView({ block: "center" });
          return;
        }
        var errs = res.errors || {};
        Object.keys(errs).forEach(function (k) {
          var slot = form.querySelector('.cform__err[data-for="' + k + '"]');
          if (slot) slot.textContent = errs[k];
          if (form[k]) form[k].setAttribute("aria-invalid", "true");
        });
        var first = form.querySelector("[aria-invalid=true]");
        if (first) first.focus();
        show(res.error || "Something went wrong. Please try again.");
      }).catch(function () {
        show("Couldn't reach the server. Check your connection and try again.");
      }).then(function () {
        btn.disabled = false;
        btn.textContent = "Send message";
      });
    });
  }

  // Close the mobile menu after following an in-page link.
  var toggle = document.getElementById("navtoggle");
  if (toggle) document.querySelector(".nav__menu").addEventListener("click", function (e) {
    if (e.target.closest("a")) toggle.checked = false;
  });

  // Installable app: the service worker caches every calculator for offline use.
  if ("serviceWorker" in navigator && window.isSecureContext) {
    // A controller already running means this visitor had an older version,
    // so a new worker taking over is an update, not a first install.
    var hadWorker = !!navigator.serviceWorker.controller;
    navigator.serviceWorker.addEventListener("message", function (e) {
      if (hadWorker && e.data && e.data.type === "updated") showUpdate(e.data.note);
    });
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("/sw.js").catch(function () {});
    });
  }

  // "FormFit has been updated" bar, with the optional UPDATE_NOTE from app.py.
  function showUpdate(note) {
    if (document.querySelector(".update")) return;
    var bar = document.createElement("div");
    bar.className = "update";
    bar.setAttribute("role", "status");
    var text = document.createElement("p");
    var head = document.createElement("b");
    head.textContent = "FormFit has been updated";
    text.appendChild(head);
    if (note) {
      var sub = document.createElement("span");
      sub.textContent = note;
      text.appendChild(sub);
    }
    var reload = document.createElement("button");
    reload.type = "button";
    reload.className = "btn btn--volt btn--sm";
    reload.textContent = "Refresh";
    reload.addEventListener("click", function () { location.reload(); });
    var close = document.createElement("button");
    close.type = "button";
    close.className = "update__close";
    close.setAttribute("aria-label", "Dismiss");
    close.textContent = "×";
    close.addEventListener("click", function () { bar.remove(); });
    bar.appendChild(text);
    bar.appendChild(reload);
    bar.appendChild(close);
    document.body.appendChild(bar);
  }

  // Install buttons (navbar + footer). They appear only when the browser
  // fires beforeinstallprompt (Chrome, Edge, Samsung Internet...), so a tap
  // always opens the real install prompt. Elsewhere they stay hidden and
  // the browser's own menu remains the way in.
  var installs = document.querySelectorAll("[data-install]");
  var deferred = null;
  var showInstall = function (on) {
    Array.prototype.forEach.call(installs, function (b) { b.hidden = !on; });
  };
  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    showInstall(true);
  });
  Array.prototype.forEach.call(installs, function (b) {
    b.addEventListener("click", function () {
      if (!deferred) return;
      deferred.prompt();
      deferred.userChoice.then(function (r) {
        deferred = null;
        if (r.outcome === "accepted") showInstall(false);
      });
    });
  });
  window.addEventListener("appinstalled", function () {
    deferred = null;
    showInstall(false);
  });
})();
