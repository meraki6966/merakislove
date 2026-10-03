/* The Meraki Inn. Six small behaviors, all optional: every page reads fine
   with this file missing.
   1. Today's sunrise, golden hour and sunset in Galveston, worked out in the
      browser from the date and the island's position, shown in island time.
      Nothing is fetched and the visitor's location is never asked for.
   2. The date request form totals the nights. Rates are samples.
   3. "Stay in this room" buttons choose that room in the form.
   4. The menu button on a phone.
   5. Ask the inn: an AI assistant that answers from these pages and can fill
      in the arrival day, the nights and the room on the form. It never asks
      for a name, an email or a card, and a message that looks like a card
      number is stopped here, before it leaves the browser.
   6. The moving hero has a pause button, and does not play at all for a
      visitor who has asked their device for less motion. */
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

  /* 6. the moving hero */
  var video = doc.querySelector(".vid video"), motionBtn = doc.querySelector("[data-motion]");
  if (video && motionBtn) {
    var setMotion = function (playing) {
      motionBtn.textContent = playing ? "Pause video" : "Play video";
      motionBtn.setAttribute("aria-pressed", playing ? "false" : "true");
    };
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      video.removeAttribute("autoplay");
      video.pause();
    } else {
      motionBtn.hidden = false;
      motionBtn.addEventListener("click", function () {
        if (video.paused) { var pr = video.play(); if (pr && pr.catch) pr.catch(function () {}); setMotion(true); }
        else { video.pause(); setMotion(false); }
      });
    }
  }

  /* 5. the assistant */
  var chat = doc.getElementById("chat");
  if (chat && window.fetch) {
    var launch = doc.querySelector("[data-chat-launch]");
    var log = doc.getElementById("chat-log"), status = doc.getElementById("chat-status");
    var cform = doc.getElementById("chat-form"), input = doc.getElementById("chat-input"), send = doc.getElementById("chat-send");
    var starters = chat.querySelector("[data-chat-starters]");
    var KEY = "meraki-inn-chat", ENDPOINT = "/api/meraki-inn-chat", KEEP = 20;
    var turns = [], busy = false;

    function save(open) {
      try { sessionStorage.setItem(KEY, JSON.stringify({ open: open, turns: turns })); } catch (e) { /* private mode: the chat still works on this page */ }
    }
    function isDay(s) { return typeof s === "string" && /^\d{4}-\d{2}-\d{2}$/.test(s) && !isNaN(new Date(s + "T00:00:00Z").getTime()); }
    function hasOption(select, value) {
      for (var i = 0; i < select.options.length; i++) if (select.options[i].value === String(value)) return true;
      return false;
    }
    /* The server has already checked these three values. They are checked again against
       this page's own form, so nothing but a listed room, a listed number of nights and a
       plain date can be written into it. */
    function applyFill(fill) {
      if (!form || !fill || !isDay(fill.arrive)) return false;
      if (!hasOption(form.elements.room, fill.room) || !hasOption(form.elements.nights, fill.nights)) return false;
      if (form.elements.arrive.min && fill.arrive < form.elements.arrive.min) return false;
      form.elements.arrive.value = fill.arrive;
      form.elements.nights.value = String(fill.nights);
      form.elements.room.value = fill.room;
      update();
      return true;
    }
    function looksLikeCard(text) {
      var runs = text.match(/\d(?:[ -]?\d){12,18}/g) || [];
      return runs.some(function (run) {
        var d = run.replace(/[ -]/g, ""), sum = 0, dbl = false;
        if (d.length < 13 || d.length > 19) return false;
        for (var i = d.length - 1; i >= 0; i--) {
          var n = d.charCodeAt(i) - 48;
          if (dbl) { n *= 2; if (n > 9) n -= 9; }
          sum += n; dbl = !dbl;
        }
        return sum % 10 === 0;
      });
    }
    function addMessage(kind, text, fill) {
      var wrap = doc.createElement("div");
      wrap.className = "chat-msg " + kind;
      var who = doc.createElement("span");
      who.className = "sr";
      who.textContent = kind === "you" ? "You said:" : kind === "error" ? "Note:" : "The inn said:";
      wrap.appendChild(who);
      /* textContent only, so a reply can never put markup on the page */
      String(text).split(/\n{2,}/).forEach(function (para) {
        var p = doc.createElement("p");
        p.textContent = para.trim();
        wrap.appendChild(p);
      });
      if (fill && form) {
        var b = doc.createElement("button");
        b.type = "button"; b.className = "go"; b.textContent = "Open the date request form";
        b.addEventListener("click", function () {
          applyFill(fill);
          closeChat(false);
          var stay = doc.getElementById("stay");
          if (stay) stay.scrollIntoView();
          form.elements.name.focus({ preventScroll: true });
        });
        wrap.appendChild(b);
      }
      log.appendChild(wrap);
      log.scrollTop = log.scrollHeight;
    }
    function openChat(focus) {
      chat.hidden = false;
      if (launch) launch.setAttribute("aria-expanded", "true");
      log.scrollTop = log.scrollHeight;
      if (focus !== false) input.focus();
      save(true);
    }
    function closeChat(focus) {
      chat.hidden = true;
      if (launch) { launch.setAttribute("aria-expanded", "false"); if (focus !== false) launch.focus(); }
      save(false);
    }
    function setBusy(state) {
      busy = state;
      input.disabled = state; send.disabled = state;
      status.textContent = state ? "Looking that up" : "";
    }
    function say(text) {
      text = String(text).trim();
      if (busy || !text) return;
      if (starters) starters.hidden = true;
      if (looksLikeCard(text)) {
        addMessage("error", "Please keep card numbers out of the chat. That message was not sent. A card is only ever taken by phone.");
        input.value = "";
        return;
      }
      addMessage("you", text);
      while (turns.length >= KEEP) turns.splice(0, 2);   /* the oldest question and its answer */
      turns.push({ role: "user", content: text });
      input.value = "";
      setBusy(true);
      fetch(ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: turns.map(function (t) { return { role: t.role, content: t.content }; }) })
      }).then(function (res) {
        return res.json().then(function (data) { return data; });
      }).then(function (data) {
        if (data && typeof data.reply === "string" && data.reply) {
          var filled = data.fill && applyFill(data.fill) ? { arrive: data.fill.arrive, nights: data.fill.nights, room: data.fill.room } : null;
          addMessage("bot", data.reply, filled);
          turns.push(filled ? { role: "assistant", content: data.reply, fill: filled } : { role: "assistant", content: data.reply });
          return;
        }
        turns.pop();   /* drop the turn that failed so it is not sent twice */
        addMessage("error", (data && data.error) || "Something went wrong. Try that again in a moment.");
      }).catch(function () {
        turns.pop();
        addMessage("error", "The assistant could not be reached. Check your connection and try again, or call the inn.");
      }).then(function () {
        setBusy(false);
        save(!chat.hidden);
        if (!chat.hidden) input.focus();
      });
    }

    /* bring the conversation along from the last page in this tab */
    var wasOpen = false;
    try {
      var kept = JSON.parse(sessionStorage.getItem(KEY) || "null");
      if (kept && Array.isArray(kept.turns)) {
        kept.turns.slice(-KEEP).forEach(function (t) {
          if (!t || typeof t.content !== "string" || (t.role !== "user" && t.role !== "assistant")) return;
          var f = t.fill && isDay(t.fill.arrive) ? t.fill : null;
          turns.push(f ? { role: t.role, content: t.content, fill: f } : { role: t.role, content: t.content });
          addMessage(t.role === "user" ? "you" : "bot", t.content, f);
        });
        while (turns.length && turns[0].role !== "user") turns.splice(0, 1);
        if (turns.length && starters) starters.hidden = true;
        wasOpen = kept.open === true;
      }
    } catch (e) { /* nothing kept */ }

    doc.querySelectorAll("[data-chat-open]").forEach(function (b) {
      b.hidden = false;
      b.addEventListener("click", function () { openChat(); });
    });
    chat.querySelector("[data-chat-close]").addEventListener("click", function () { closeChat(); });
    chat.querySelector("[data-chat-reset]").addEventListener("click", function () {
      turns = [];
      log.querySelectorAll(".chat-msg:not(:first-child)").forEach(function (el) { el.remove(); });
      if (starters) starters.hidden = false;
      save(true);
      input.focus();
    });
    chat.querySelectorAll("[data-chat-say]").forEach(function (b) {
      b.addEventListener("click", function () { say(b.getAttribute("data-chat-say")); });
    });
    cform.addEventListener("submit", function (ev) { ev.preventDefault(); say(input.value); });
    chat.addEventListener("keydown", function (ev) { if (ev.key === "Escape") closeChat(); });
    if (wasOpen && window.innerWidth >= 900) openChat(false);
  }
})();
