/* The Meraki Inn preview A. The booking bar and the stay form share one set of
   dates: change either and both update, with the total. The page is complete
   without this file. Rates are samples. */
(function () {
  "use strict";
  var doc = document;

  function nextFriday() {
    var d = new Date();
    var add = (5 - d.getDay() + 7) % 7 || 7;
    d.setDate(d.getDate() + add);
    var m = String(d.getMonth() + 1), day = String(d.getDate());
    return d.getFullYear() + "-" + (m.length < 2 ? "0" + m : m) + "-" + (day.length < 2 ? "0" + day : day);
  }
  function fields(key) { return doc.querySelectorAll('[data-sync="' + key + '"]'); }
  function value(key) { var f = fields(key)[0]; return f ? f.value : ""; }
  function setAll(key, val) { fields(key).forEach(function (el) { el.value = val; }); }

  function update() {
    var room = fields("room")[0];
    if (!room) return;
    var opt = room.options[room.selectedIndex];
    var rate = Number(opt.getAttribute("data-rate"));
    var nights = Number(value("nights")) || 1;
    var name = opt.textContent.split(",")[0];
    var line = nights + (nights === 1 ? " night in " : " nights in ") + name;
    doc.querySelectorAll("[data-total]").forEach(function (el) { el.textContent = line; });
    doc.querySelectorAll("[data-sum]").forEach(function (el) { el.textContent = "$" + (rate * nights).toLocaleString("en-US"); });
  }

  ["arrive", "nights", "room"].forEach(function (key) {
    fields(key).forEach(function (el) {
      el.addEventListener("change", function () { setAll(key, el.value); update(); });
    });
  });
  var start = nextFriday();
  fields("arrive").forEach(function (el) { el.min = new Date().toISOString().slice(0, 10); if (!el.value) el.value = start; });
  update();

  doc.querySelectorAll("[data-pick]").forEach(function (b) {
    b.addEventListener("click", function () {
      setAll("room", b.getAttribute("data-pick"));
      update();
      var stay = doc.getElementById("stay");
      if (stay) stay.scrollIntoView();
    });
  });

  /* the header is cream while the big name is on screen, dark after */
  var hd = doc.querySelector("[data-hd]"), lock = doc.querySelector("[data-lockup]");
  if (hd && lock && "IntersectionObserver" in window) {
    new IntersectionObserver(function (e) { hd.classList.toggle("at-top", e[0].isIntersecting); }, { rootMargin: "-80px 0px 0px 0px" }).observe(lock);
  }

  var bar = doc.querySelector("[data-bar]");
  if (bar) bar.addEventListener("submit", function (ev) { ev.preventDefault(); });
  doc.querySelectorAll("form[data-demo]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var done = f.querySelector(".form-done");
      if (done) done.classList.add("show");
    });
  });
})();
