/* Sideoats preview B. The sentence builder: pick what you have and what you
   want to know, and the sentence and the answer change. The page is complete
   without this file: the first question and its answer are in the HTML. */
(function () {
  "use strict";
  var doc = document;
  var data = {};
  try { data = JSON.parse(doc.getElementById("data").textContent); } catch (e) { data = {}; }
  var form = doc.querySelector("[data-ask]");
  var qbox = doc.querySelector("[data-qs]");

  function text(sel, value) {
    var el = doc.querySelector(sel);
    if (el) el.textContent = value;
  }
  function show(thing, index) {
    var set = data[thing];
    if (!set) return;
    var item = set.qs[index] || set.qs[0];
    text('[data-s="thing"]', set.label);
    text('[data-s="q"]', item.q);
    text('[data-a="f"]', item.f);
    text('[data-a="a"]', item.a);
  }
  function questions(thing) {
    var set = data[thing];
    if (!set || !qbox) return;
    qbox.textContent = "";
    set.qs.forEach(function (item, i) {
      var label = doc.createElement("label");
      var input = doc.createElement("input");
      var span = doc.createElement("span");
      input.type = "radio"; input.name = "q"; input.value = String(i); input.checked = i === 0;
      span.textContent = item.q;
      label.appendChild(input); label.appendChild(span);
      qbox.appendChild(label);
    });
  }
  if (form) {
    form.addEventListener("change", function (ev) {
      var thing = form.elements.thing.value;
      if (ev.target.name === "thing") { questions(thing); show(thing, 0); return; }
      show(thing, Number(form.elements.q.value));
    });
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
