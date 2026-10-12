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

  // Close the mobile menu after following an in-page link.
  var toggle = document.getElementById("navtoggle");
  if (toggle) document.querySelector(".nav__menu").addEventListener("click", function (e) {
    if (e.target.closest("a")) toggle.checked = false;
  });
})();
