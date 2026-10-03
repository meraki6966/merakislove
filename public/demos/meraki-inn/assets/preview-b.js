/* The Meraki Inn preview B. Two small behaviors, both optional.
   1. Today's sunrise and sunset in Galveston, worked out in the browser from
      the date and the island's position, and shown in island time.
   2. The stay form totals the nights. Rates are samples. */
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
    var rise = clock(t.rise), set = clock(t.set), golden = clock(new Date(t.set.getTime() - 3600000));
    var line = doc.querySelector("[data-sun]");
    if (line) line.textContent = "Today in Galveston the sun rises at " + rise + " and sets at " + set + ".";
    doc.querySelectorAll('[data-time="sunrise"]').forEach(function (el) { setClock(el, rise); });
    doc.querySelectorAll('[data-time="golden"]').forEach(function (el) { setClock(el, golden); });
    doc.querySelectorAll('[data-time="sunset"]').forEach(function (el) { setClock(el, set); });
  } catch (e) { /* the written words stay on the page */ }

  /* 2. the stay form */
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
    if (!form.elements.arrive.value) form.elements.arrive.value = nextFriday();
    form.addEventListener("change", update);
    update();
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) done.classList.add("show");
    });
  }
})();
