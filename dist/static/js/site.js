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

  // Install buttons (navbar + footer). Chrome, Edge and Samsung Internet
  // fire beforeinstallprompt, and the button opens that native prompt.
  // Safari, Firefox, Brave and others don't, but can still install from
  // their own menus, so there the button explains how for that browser.
  var installs = document.querySelectorAll("[data-install]");
  var help = document.querySelector(".install-help");
  var deferred = null;
  var installed = window.matchMedia("(display-mode: standalone)").matches ||
    window.matchMedia("(display-mode: window-controls-overlay)").matches ||
    navigator.standalone === true;
  var showInstall = function (on) {
    Array.prototype.forEach.call(installs, function (b) { b.hidden = !on; });
  };
  var steps = function () {
    var ua = navigator.userAgent;
    var ios = /iPad|iPhone|iPod/.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
    var android = /Android/.test(ua);
    var firefox = /Firefox|FxiOS/.test(ua);
    var safari = /Safari/.test(ua) && !/Chrome|Chromium|CriOS|Edg|OPR|Firefox|FxiOS/.test(ua);
    var name = navigator.brave ? "Brave" : /OPR\//.test(ua) ? "Opera" : /SamsungBrowser/.test(ua) ? "Samsung Internet" : "your browser";
    if (ios) return "Tap the <b>Share</b> button (the square with an arrow), scroll down and tap <b>Add to Home Screen</b>, then <b>Add</b>.";
    if (android && firefox) return "Tap the <b>menu</b> (&#8942;), then <b>Add to Home screen</b> (or <b>Install</b>).";
    if (android) return "In " + name + ", tap the <b>menu</b> (&#8942; or &#9776;), then <b>Install app</b> or <b>Add to Home screen</b>.";
    if (safari) return "In the Safari menu bar, choose <b>File &rarr; Add to Dock</b>. (Needs macOS Sonoma or later.)";
    if (firefox) return "Firefox on a computer may not offer installing websites. If you see an install option in the address bar or menu, use it; otherwise open formfit.in in Chrome, Edge or Brave to install it.";
    return "In " + name + ", click the <b>install icon</b> at the right end of the address bar (a screen with a down arrow), or open the <b>menu</b> and choose <b>Install FormFit</b> (it can sit under <i>Save and share</i> or <i>Apps</i>).";
  };
  if (!installed) showInstall(true);
  window.addEventListener("beforeinstallprompt", function (e) {
    e.preventDefault();
    deferred = e;
    if (!installed) showInstall(true);
  });
  Array.prototype.forEach.call(installs, function (b) {
    b.addEventListener("click", function () {
      if (deferred) {
        deferred.prompt();
        deferred.userChoice.then(function (r) {
          deferred = null;
          if (r.outcome === "accepted") showInstall(false);
        });
        return;
      }
      if (!help || !help.showModal) return;
      help.querySelector(".install-help__steps").innerHTML = steps();
      if (toggle) toggle.checked = false;
      help.showModal();
    });
  });
  if (help) help.addEventListener("click", function (e) {
    if (e.target === help) help.close();     // tap outside the box closes it
  });
  window.addEventListener("appinstalled", function () {
    deferred = null;
    showInstall(false);
  });
})();
