// Saltbrush Pool Care demo. Small, dependency free, CSP friendly (served from 'self').
(function () {
  document.documentElement.classList.add("js");

  // Phone and tablet menu.
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
  }

  // Monsoon season status. The National Weather Service season runs June 15
  // through September 30. The date is read in Phoenix time, which has no
  // daylight saving change.
  function phoenixToday() {
    try {
      return new Intl.DateTimeFormat("en-CA", { timeZone: "America/Phoenix", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date()).slice(0, 10);
    } catch (e) {
      return new Date().toISOString().slice(0, 10);
    }
  }
  function days(a, b) {
    return Math.round((Date.parse(b + "T00:00:00Z") - Date.parse(a + "T00:00:00Z")) / 86400000);
  }
  var today = phoenixToday();
  var year = parseInt(today.slice(0, 4), 10);
  var start = year + "-06-15", end = year + "-09-30";
  var text;
  var inSeason = today >= start && today <= end;
  if (inSeason) {
    var left = days(today, end);
    text = "Monsoon season is on. " + (left === 0 ? "Today is the last day." : left === 1 ? "1 day left." : left + " days left.");
  } else {
    var next = today < start ? start : (year + 1) + "-06-15";
    var until = days(today, next);
    text = "Monsoon season starts June 15, " + (until === 1 ? "1 day from now." : until + " days from now.");
  }
  Array.prototype.forEach.call(document.querySelectorAll("[data-monsoon]"), function (el) {
    var t = el.querySelector(".txt");
    if (t) t.textContent = text;
    if (inSeason) el.classList.add("on");
  });

  // Demo forms: nothing is sent anywhere. Show a clear note instead.
  Array.prototype.forEach.call(document.querySelectorAll("form[data-demo]"), function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) {
        done.classList.add("show");
        done.setAttribute("tabindex", "-1");
        done.focus();
      }
    });
  });

  // Gentle reveal as sections come into view.
  var pending = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    pending.forEach(function (el) { el.classList.add("in"); });
    pending = [];
  }
  var ticking = false;
  function check() {
    ticking = false;
    var limit = window.innerHeight * 0.92;
    pending = pending.filter(function (el) {
      if (el.getBoundingClientRect().top < limit) { el.classList.add("in"); return false; }
      return true;
    });
    if (!pending.length) window.removeEventListener("scroll", onScroll);
  }
  function onScroll() { if (!ticking) { ticking = true; window.requestAnimationFrame(check); } }
  if (pending.length) { window.addEventListener("scroll", onScroll, { passive: true }); check(); }
})();
