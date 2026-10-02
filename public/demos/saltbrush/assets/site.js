// Saltbrush Pool Care demo. Small, dependency free, CSP friendly (served from 'self').
(function () {
  // Monsoon season note. The National Weather Service season runs June 15
  // through September 30. The date is read in Phoenix time.
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
  if (today >= start && today <= end) {
    var left = days(today, end);
    text = "Monsoon season is on. " + (left === 0 ? "Today is the last day." : left === 1 ? "1 day left." : left + " days left.");
  } else {
    var next = today < start ? start : (year + 1) + "-06-15";
    var until = days(today, next);
    text = "Monsoon season starts June 15, " + (until === 1 ? "1 day from now." : until + " days from now.");
  }
  Array.prototype.forEach.call(document.querySelectorAll("[data-monsoon] .txt"), function (el) { el.textContent = text; });

  // The "Today" marker on the year strip.
  var marker = document.querySelector("[data-today]");
  if (marker) {
    var dayOfYear = days(year + "-01-01", today);
    var total = days(year + "-01-01", (year + 1) + "-01-01");
    marker.style.left = (dayOfYear / total * 100).toFixed(2) + "%";
    marker.style.display = "block";
  }

  // Switch the sample report between three weeks. Values come from
  // a JSON block written at build time and are set with textContent.
  var sheet = document.querySelector(".sheet");
  var dataEl = document.getElementById("scn");
  if (sheet && dataEl) {
    var data;
    try { data = JSON.parse(dataEl.textContent); } catch (e) { data = null; }
    var tabs = Array.prototype.slice.call(sheet.querySelectorAll('[role="tab"]'));
    var show = function (key) {
      var s = data && data[key];
      if (!s) return;
      sheet.setAttribute("data-s", key);
      tabs.forEach(function (t) { t.setAttribute("aria-selected", t.getAttribute("data-s") === key ? "true" : "false"); });
      ["status", "arrived", "left", "gate"].forEach(function (f) {
        var el = sheet.querySelector('[data-f="' + f + '"]');
        if (el) el.textContent = s[f];
      });
      Object.keys(s.rows).forEach(function (k) {
        var row = sheet.querySelector('.g[data-k="' + k + '"]');
        if (!row) return;
        row.setAttribute("data-state", s.rows[k].s);
        row.querySelector(".g-v b").textContent = s.rows[k].t;
        row.querySelector(".dot").style.left = s.rows[k].p + "%";
        row.querySelector(".g-s").textContent = s.rows[k].s;
      });
      var list = sheet.querySelector('[data-f="did"]');
      if (list) {
        list.textContent = "";
        s.did.forEach(function (d) { var li = document.createElement("li"); li.textContent = d; list.appendChild(li); });
      }
      var img = sheet.querySelector('[data-f="img"]');
      if (img) { img.src = s.img; img.alt = s.alt; }
    };
    tabs.forEach(function (t) { t.addEventListener("click", function () { show(t.getAttribute("data-s")); }); });
  }

  // Hero video: a pause control, and no motion at all for visitors who have
  // asked their device to reduce it.
  var video = document.querySelector(".hero-media video");
  var motionBtn = document.querySelector("[data-motion]");
  if (video && motionBtn) {
    var setState = function (playing) {
      motionBtn.textContent = playing ? "Pause video" : "Play video";
      motionBtn.setAttribute("aria-pressed", playing ? "false" : "true");
    };
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      video.removeAttribute("autoplay");
      video.pause();
      setState(false);
    }
    motionBtn.addEventListener("click", function () {
      if (video.paused) { var p = video.play(); if (p && p.catch) p.catch(function () {}); setState(true); }
      else { video.pause(); setState(false); }
    });
  }

  // Demo forms: nothing is sent anywhere. Show a clear note instead.
  Array.prototype.forEach.call(document.querySelectorAll("form[data-demo]"), function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) { done.classList.add("show"); done.setAttribute("tabindex", "-1"); done.focus(); }
    });
  });
})();
