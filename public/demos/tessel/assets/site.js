// Tessel Dental demo. Small, dependency free, CSP friendly (served from 'self').
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

  // Service pages link to the form with ?reason=<value>#book so the visit
  // type is already picked. Only lowercase letters and hyphens are accepted.
  var params = new URLSearchParams(window.location.search);
  var reason = (params.get("reason") || "").replace(/[^a-z-]/g, "");
  if (reason) {
    var r = document.querySelector('.book-form input[name="reason"][value="' + reason + '"]');
    if (r) r.checked = true;
  }
  var office = (params.get("office") || "").replace(/[^a-z-]/g, "");
  if (office) {
    var sel = document.querySelector('.book-form select[name="office"]');
    if (sel && sel.querySelector('option[value="' + office + '"]')) sel.value = office;
  }

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

  // Open now / closed, computed in Charlotte time (America/New_York) from
  // each office's data-hours, e.g. {"1":["07:30","17:00"], ...} keyed by
  // weekday with Sunday as 0. If the browser can't resolve the time zone,
  // the static text already in the page stays as it is.
  function charlotteNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-US", {
        timeZone: "America/New_York", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false
      }).formatToParts(new Date());
      var map = {};
      parts.forEach(function (p) { map[p.type] = p.value; });
      var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      var h = parseInt(map.hour, 10) % 24;
      return { day: days[map.weekday], mins: h * 60 + parseInt(map.minute, 10) };
    } catch (err) { return null; }
  }
  function toMins(t) { var a = t.split(":"); return parseInt(a[0], 10) * 60 + parseInt(a[1], 10); }
  function fmt(t) {
    var m = toMins(t), h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? "PM" : "AM";
    h = h % 12 || 12;
    return h + (mm ? ":" + (mm < 10 ? "0" : "") + mm : "") + " " + ap;
  }
  var now = charlotteNow();
  if (now) {
    Array.prototype.forEach.call(document.querySelectorAll("[data-hours]"), function (el) {
      var hours;
      try { hours = JSON.parse(el.getAttribute("data-hours")); } catch (err) { return; }
      var today = hours[String(now.day)];
      var dot = el.querySelector(".dot");
      var label = el.querySelector(".status-text");
      var open = today && now.mins >= toMins(today[0]) && now.mins < toMins(today[1]);
      if (dot) dot.classList.toggle("open", !!open);
      if (label) {
        if (open) label.textContent = "Open now until " + fmt(today[1]);
        else if (today && now.mins < toMins(today[0])) label.textContent = "Opens today at " + fmt(today[0]);
        else {
          for (var i = 1; i <= 7; i++) {
            var d = (now.day + i) % 7, next = hours[String(d)];
            if (next) {
              var names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
              label.textContent = "Closed now. Opens " + (i === 1 ? "tomorrow" : names[d]) + " at " + fmt(next[0]);
              break;
            }
          }
        }
      }
    });
    Array.prototype.forEach.call(document.querySelectorAll(".hours tr[data-day]"), function (tr) {
      if (tr.getAttribute("data-day") === String(now.day)) tr.classList.add("today-row");
    });
  }

  // Gentle reveal as sections come into view. A scroll check (not only an
  // IntersectionObserver) so a fast jump past an element still reveals it.
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
