/* Sideoats preview A. The deductible example recalculates as the dials move.
   The page is complete without this file: the starting numbers are in the HTML. */
(function () {
  "use strict";
  var doc = document;
  var form = doc.querySelector("[data-calc]");
  function money(n) { return "$" + Math.round(n).toLocaleString("en-US"); }
  function set(key, text) {
    doc.querySelectorAll('[data-o="' + key + '"]').forEach(function (el) { el.textContent = text; });
  }
  function run() {
    var house = Number(form.elements.house.value);
    var roof = Number(form.elements.roof.value);
    var pct = Number(form.elements.pct.value);
    var ded = Math.round(house * pct / 100);
    var you = Math.min(roof, ded);
    var pays = Math.max(0, roof - ded);
    set("house", money(house));
    set("roof", money(roof));
    set("ded", money(ded));
    set("you", money(you));
    set("pays", money(pays));
    var bar = doc.querySelector("[data-bar]");
    if (bar) bar.style.width = (you / roof * 100).toFixed(2) + "%";
    var say = pays > 0
      ? "On a " + money(roof) + " roof, a " + pct + "% deductible leaves you with " + money(you) + " and the policy with " + money(pays) + "."
      : "A " + money(roof) + " roof costs less than your " + money(ded) + " deductible, so the policy pays nothing and the whole roof is yours.";
    set("say", say);
  }
  if (form) {
    form.addEventListener("input", run);
    form.addEventListener("change", run);
    form.addEventListener("submit", function (ev) { ev.preventDefault(); });
  }

  doc.querySelectorAll("form[data-demo]").forEach(function (f) {
    f.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var done = f.querySelector(".form-done");
      if (done) done.classList.add("show");
    });
  });
})();
