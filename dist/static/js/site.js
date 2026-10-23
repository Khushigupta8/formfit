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
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("/sw.js").catch(function () {});
    });
  }

  // Chrome, Edge and Android fire beforeinstallprompt when the site can be
  // installed. Offer it from a quiet footer button instead of a pop-up.
  // (iOS has no prompt: Share > Add to Home Screen.)
  var install = document.querySelector(".foot__install");
  var deferred = null;
  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    if (install) install.hidden = false;
  });
  if (install) install.addEventListener("click", function () {
    if (!deferred) return;
    deferred.prompt();
    deferred.userChoice.then(function () { deferred = null; install.hidden = true; });
  });
  window.addEventListener("appinstalled", function () {
    deferred = null;
    if (install) install.hidden = true;
  });
})();
