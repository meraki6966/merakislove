/* The Meraki Inn. Four small behaviors, all optional: every page reads fine
   with this file missing.
   1. Today's sunrise, golden hour and sunset in Galveston, worked out in the
      browser from the date and the island's position, shown in island time.
      Nothing is fetched and the visitor's location is never asked for.
   2. The date request form totals the nights. Rates are samples.
   3. "Stay in this room" buttons choose that room in the form.
   4. The menu button on a phone. */
(function () {
  "use strict";
  var doc = document;

  /* 1. the sun over Galveston: 29.30 north, 94.80 west */
  var LAT = 29.3013, LNG = -94.7977, rad = Math.PI / 180;
  function sunTimes(date) {
    var lw = rad * -LNG, phi = rad * LAT;
    var d = date.valueOf() / 86400000 - 0.5 + 2440588 - 2451545;
    var n = Math.round(d - 0.0009 - lw / (2 * Math.PI));
    function transit(ht) { return 0.0009 + (ht + lw) / (2 * Math.PI) + n; }
    var ds = transit(0);
    var M = rad * (357.5291 + 0.98560028 * ds);
    var C = rad * (1.9148 * Math.sin(M) + 0.02 * Math.sin(2 * M) + 0.0003 * Math.sin(3 * M));
    var L = M + C + rad * 102.9372 + Math.PI;
    var dec = Math.asin(Math.sin(L) * Math.sin(rad * 23.4397));
    function solarJ(base) { return 2451545 + base + 0.0053 * Math.sin(M) - 0.0069 * Math.sin(2 * L); }
    var noon = solarJ(ds);
    var w = Math.acos((Math.sin(rad * -0.833) - Math.sin(phi) * Math.sin(dec)) / (Math.cos(phi) * Math.cos(dec)));
    var set = solarJ(transit(w));
    var rise = noon - (set - noon);
    function toDate(j) { return new Date((j + 0.5 - 2440588) * 86400000); }
    return { rise: toDate(rise), set: toDate(set) };
  }
  function clock(date) {
    return new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", hour: "numeric", minute: "2-digit" }).format(date);
  }
  function setClock(el, text) {
    var parts = text.split(" ");
    el.textContent = parts[0] + " ";
    var small = doc.createElement("small");
    small.textContent = parts[1] || "";
    el.appendChild(small);
  }
  try {
    var t = sunTimes(new Date());
    var times = { sunrise: clock(t.rise), golden: clock(new Date(t.set.getTime() - 3600000)), sunset: clock(t.set) };
    var line = doc.querySelector("[data-sun]");
    if (line) line.textContent = "Today in Galveston the sun rises at " + times.sunrise + " and sets at " + times.sunset + ".";
    doc.querySelectorAll("[data-time]").forEach(function (el) {
      var v = times[el.getAttribute("data-time")];
      if (v) setClock(el, v);
    });
  } catch (e) { /* the written words stay on the page */ }

  /* 2. the date request form */
  function nextFriday() {
    var d = new Date();
    var add = (5 - d.getDay() + 7) % 7 || 7;
    d.setDate(d.getDate() + add);
    var m = String(d.getMonth() + 1), day = String(d.getDate());
    return d.getFullYear() + "-" + (m.length < 2 ? "0" + m : m) + "-" + (day.length < 2 ? "0" + day : day);
  }
  var form = doc.querySelector("[data-stay]");
  function update() {
    var room = form.elements.room, opt = room.options[room.selectedIndex];
    var rate = Number(opt.getAttribute("data-rate")), nights = Number(form.elements.nights.value) || 1;
    var name = opt.textContent.split(",")[0];
    form.querySelector("[data-total]").textContent = nights + (nights === 1 ? " night in " : " nights in ") + name;
    form.querySelector("[data-sum]").textContent = "$" + (rate * nights).toLocaleString("en-US");
  }
  if (form) {
    var arrive = form.elements.arrive;
    arrive.min = new Date().toISOString().slice(0, 10);
    if (!arrive.value) arrive.value = nextFriday();
    form.addEventListener("change", update);
    update();
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) done.classList.add("show");
    });
  }

  /* 3. choose a room from anywhere on the page */
  doc.querySelectorAll("[data-pick]").forEach(function (b) {
    b.addEventListener("click", function () {
      if (!form) return;
      form.elements.room.value = b.getAttribute("data-pick");
      update();
      var stay = doc.getElementById("stay");
      if (stay) stay.scrollIntoView();
      form.elements.arrive.focus({ preventScroll: true });
    });
  });

  /* 4. the menu on a phone */
  var btn = doc.querySelector("[data-menu]"), nav = doc.getElementById("nav");
  if (btn && nav) {
    btn.hidden = false;
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.textContent = open ? "Close" : "Menu";
    });
    nav.addEventListener("click", function (ev) {
      if (ev.target.tagName === "A") { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.textContent = "Menu"; }
    });
    doc.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); btn.textContent = "Menu"; btn.focus(); }
    });
  }
})();
