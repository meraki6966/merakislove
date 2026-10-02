/* Fernhollow. Three small behaviors, all optional: every page reads fine with
   this file missing.
   1. Dog or Cat switch: swaps anything marked data-for.
      The choice is kept for the browser session so it follows you between pages.
   2. Open or closed, worked out in Portland time, never the visitor's clock.
   3. The demo form says plainly that nothing was sent. */
(function () {
  "use strict";
  var doc = document;
  var data = {};
  try { data = JSON.parse(doc.getElementById("data").textContent); } catch (e) { data = {}; }
  var er = data.er || {};

  /* 1. species */
  var buttons = doc.querySelectorAll("[data-species]");
  function setSpecies(sp, keep) {
    buttons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.getAttribute("data-species") === sp)); });
    doc.querySelectorAll("[data-for]").forEach(function (el) { el.hidden = el.getAttribute("data-for") !== sp; });
    if (keep) { try { sessionStorage.setItem("fh-species", sp); } catch (e) { /* private mode */ } }
  }
  buttons.forEach(function (b) {
    b.addEventListener("click", function () { setSpecies(b.getAttribute("data-species"), true); });
  });
  if (buttons.length) {
    try { if (sessionStorage.getItem("fh-species") === "cat") setSpecies("cat", false); } catch (e) { /* private mode */ }
  }

  /* 2. open or closed in Portland */
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var HOURS = { 1: [450, 1080], 2: [450, 1080], 3: [450, 1080], 4: [450, 1080], 5: [450, 1080], 6: [540, 840] };
  function clock(mins) {
    var h = Math.floor(mins / 60), m = mins % 60, half = h >= 12 ? "PM" : "AM";
    h = h % 12 || 12;
    return h + (m ? ":" + (m < 10 ? "0" : "") + m : "") + " " + half;
  }
  function portland() {
    var parts = new Intl.DateTimeFormat("en-US", { timeZone: "America/Los_Angeles", weekday: "long", month: "numeric", hour: "numeric", minute: "numeric", hourCycle: "h23" }).formatToParts(new Date());
    var get = function (t) { var p = parts.filter(function (x) { return x.type === t; })[0]; return p ? p.value : ""; };
    return { day: DAYS.indexOf(get("weekday")), mins: Number(get("hour")) * 60 + Number(get("minute")), month: Number(get("month")) };
  }
  function nextOpen(now) {
    for (var i = 0; i < 8; i++) {
      var d = (now.day + i) % 7, h = HOURS[d];
      if (!h) continue;
      if (i === 0 && now.mins >= h[0]) continue;
      var when = i === 0 ? "today" : i === 1 ? "tomorrow" : DAYS[d];
      return when + " at " + clock(h[0]);
    }
    return "Monday at 7:30 AM";
  }
  function setText(el, strong, rest) {
    el.textContent = "";
    var b = doc.createElement("b");
    b.textContent = strong;
    el.appendChild(b);
    el.appendChild(doc.createTextNode(rest));
  }
  try {
    var now = portland();
    var today = HOURS[now.day];
    var open = !!today && now.mins >= today[0] && now.mins < today[1];
    var reopen = open ? "" : nextOpen(now);

    var line = doc.querySelector("[data-open]");
    if (line) {
      if (open) setText(line, "Open now", " until " + clock(today[1]) + " Portland time.");
      else setText(line, "Closed now", ". We open " + reopen + ". For an emergency, call " + er.name + " at " + er.phone + ".");
    }

    var bar = doc.querySelector("[data-status]");
    if (bar) {
      bar.setAttribute("data-status", open ? "open" : "closed");
      var txt = bar.querySelector("[data-status-text]"), link = bar.querySelector("a");
      if (open) {
        txt.textContent = "Open now until " + clock(today[1]) + ".";
      } else {
        txt.textContent = "Closed now. We open " + reopen + ". For an emergency, call " + er.name + ":";
        if (link && er.tel) { link.setAttribute("href", "tel:" + er.tel); link.textContent = er.phone; }
      }
    }

    doc.querySelectorAll("[data-callus]").forEach(function (call) {
      var note = call.querySelector("[data-callus-note]"), head = call.querySelector("b");
      if (open && now.mins < 900) {
        note.textContent = "Call before 3 PM for a same day visit";
      } else if (open) {
        note.textContent = "Today's sick visits are booked by 3 PM. Call and we will find the first one tomorrow.";
      } else if (er.tel) {
        call.setAttribute("href", "tel:" + er.tel);
        head.textContent = "Closed now. Call " + er.name;
        note.textContent = er.phone + ". We open " + reopen + ".";
      }
    });

    /* mark this month on the year table and the entry bars */
    doc.querySelectorAll(".yeartbl tr").forEach(function (tr) {
      var cell = tr.children[now.month];
      if (cell) cell.classList.add("now");
    });
  } catch (e) { /* the written hours stay on the page */ }

  /* 3. demo form */
  doc.querySelectorAll("form[data-demo]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var done = f.querySelector(".form-done");
      if (done) done.classList.add("show");
    });
  });
})();
