// Keelhouse Home Services demo. Small, dependency free, CSP friendly (served from 'self').
(function () {
  document.documentElement.classList.add("js");

  // Phone and tablet menu.
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // "What's going on at the house?" tiles link here with ?need=<value>#book.
  // Pre-check the matching box so the visitor lands on a form already started.
  var need = new URLSearchParams(window.location.search).get("need");
  if (need) {
    var box = document.querySelector('.book-form input[name="need"][value="' + need.replace(/[^a-z-]/g, "") + '"]');
    if (box) box.checked = true;
  }

  // Demo form: nothing is sent anywhere. Show a clear note instead.
  var form = document.querySelector(".book-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var done = form.querySelector(".form-done");
      if (done) {
        done.classList.add("show");
        done.setAttribute("tabindex", "-1");
        done.focus();
      }
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
