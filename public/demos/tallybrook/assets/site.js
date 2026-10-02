// Tallybrook Tax and Accounting demo. Small, dependency free, CSP friendly (served from 'self').
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

  // Links into the form carry ?need=<key>, so the visitor lands on a form
  // already started. Only lowercase letters and hyphens are accepted.
  var need = (new URLSearchParams(window.location.search).get("need") || "").replace(/[^a-z-]/g, "");
  if (need) {
    var r = document.querySelector('.form input[name="need"][value="' + need + '"]');
    if (r) r.checked = true;
  }

  // Deadlines. Every dated row and card carries data-date="YYYY-MM-DD". The
  // page ships with the first date marked as next; this moves the mark to the
  // first date that has not passed in Philadelphia, and counts the days.
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  function todayInPhiladelphia() {
    try {
      var s = new Intl.DateTimeFormat("en-CA", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit" }).format(new Date());
      return s.slice(0, 10);
    } catch (e) {
      return new Date().toISOString().slice(0, 10);
    }
  }
  function daysBetween(a, b) {
    return Math.round((Date.parse(b + "T00:00:00Z") - Date.parse(a + "T00:00:00Z")) / 86400000);
  }
  function leftText(n) {
    return n === 0 ? "Due today" : n === 1 ? "1 day left" : n + " days left";
  }
  var today = todayInPhiladelphia();
  var rows = Array.prototype.slice.call(document.querySelectorAll("tr[data-date]"));
  var marked = false;
  rows.forEach(function (tr) {
    var d = tr.getAttribute("data-date");
    tr.classList.remove("next", "past");
    var cell = tr.querySelector(".left-cell");
    if (d < today) {
      tr.classList.add("past");
      if (cell) cell.textContent = "Passed";
    } else {
      if (!marked) { tr.classList.add("next"); marked = true; }
      if (cell) cell.textContent = leftText(daysBetween(today, d));
    }
  });
  Array.prototype.forEach.call(document.querySelectorAll(".due[data-deadlines]"), function (card) {
    var list;
    try { list = JSON.parse(card.getAttribute("data-deadlines")); } catch (e) { return; }
    var next = null;
    for (var i = 0; i < list.length; i++) { if (list[i][0] >= today) { next = list[i]; break; } }
    if (!next) return;
    var parts = next[0].split("-");
    var day = card.querySelector(".date b"), mon = card.querySelector(".date span"), what = card.querySelector(".what"), left = card.querySelector(".left .n");
    if (day) day.textContent = String(parseInt(parts[2], 10));
    if (mon) mon.textContent = MONTHS[parseInt(parts[1], 10) - 1] + " " + parts[0];
    if (what) what.textContent = next[1];
    if (left) left.textContent = leftText(daysBetween(today, next[0]));
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

  // Upload preview. File names are listed with textContent and the files
  // never leave the browser: there is no request, and nothing is read.
  var picker = document.querySelector("#upload-files");
  var listEl = document.querySelector(".files");
  if (picker && listEl) {
    picker.addEventListener("change", function () {
      listEl.textContent = "";
      Array.prototype.slice.call(picker.files, 0, 8).forEach(function (f) {
        var li = document.createElement("li");
        var name = document.createElement("b");
        name.textContent = f.name.slice(0, 80);
        var state = document.createElement("span");
        state.textContent = "Ready. Demo only, nothing sent";
        li.appendChild(name);
        li.appendChild(state);
        listEl.appendChild(li);
      });
    });
  }

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
