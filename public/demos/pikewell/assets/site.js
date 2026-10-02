// Pikewell Real Estate demo. Small, dependency free, CSP friendly (served from 'self').
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

  // Links into the form carry ?intent=<buy|sell|value> and ?area=<slug> so the
  // visitor lands on a form already started. Only lowercase letters and
  // hyphens are accepted.
  var params = new URLSearchParams(window.location.search);
  var intent = (params.get("intent") || "").replace(/[^a-z-]/g, "");
  if (intent) {
    var r = document.querySelector('.form input[name="intent"][value="' + intent + '"]');
    if (r) r.checked = true;
  }
  var area = (params.get("area") || "").replace(/[^a-z-]/g, "");
  if (area) {
    var sel = document.querySelector('.form select[name="area"]');
    if (sel && sel.querySelector('option[value="' + area + '"]')) sel.value = area;
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
