"""Two home page previews for the Saltbrush redesign, for Adam to choose between.

Run from the repo root:  python3 scripts/demos/saltbrush/previews.py
Writes preview-a.html (The Report) and preview-b.html (The Deep End) into
public/demos/saltbrush/. Both are noindex and are not linked from the live demo.
The copy and the schema come from the same sources as the live home page.
"""
import json
import os
import re
import sys
from html import escape

sys.path.insert(0, os.path.dirname(__file__))
from sb import (BRAND, PHONE, TEL, BASE, MARK, SERVICES, AREAS, strip, org_schema, business_schema, website_schema,  # noqa: E402
                faq_schema, crumbs_schema, ld)
from content import REVIEWS, HOME_FAQ, SEASONS, WORRIES, VISIT_STEPS  # noqa: E402
from build import absolutize, PREFIX  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "saltbrush")
PROBLEMS = []
TITLE = "Pool Service in Phoenix, AZ | Saltbrush Pool Care"
DESC = ("Weekly pool service and repair in Phoenix, Arcadia, Ahwatukee and Tempe. One technician, flat monthly pricing "
        "and a water report after every visit.")
NAV = [("services.html", "Services"), ("monsoon-pool-care.html", "Monsoon care"), ("pool-safety.html", "Pool safety"),
       ("pricing.html", "Pricing"), ("about.html", "About")]
PRICES = [("weekly-pool-service.html", "Weekly pool service", "A full visit every week of the year, with all balancing chemicals.", "$155", "a month"),
          ("weekly-pool-service.html", "Chemicals only", "We test and balance every week. You handle the cleaning.", "$95", "a month"),
          ("green-pool-cleanup.html", "Green pool cleanup", "From green to swimmable, usually in three to five days.", "$295", "and up"),
          ("filter-cleaning.html", "Filter cleaning", "Taken apart, cleaned and inspected, with photos of what we found.", "$95", "per cleaning"),
          ("equipment-repair.html", "Repair diagnosis", "We find the cause and write down the price. Credited to the repair.", "$89", "per visit")]
ROUTE = [("Monday", "ahwatukee"), ("Tuesday", "arcadia"), ("Wednesday", "tempe"), ("Thursday", "ahwatukee"), ("Friday", "arcadia")]
AREA = {a["slug"]: a for a in AREAS}
CODES = [("Collected by phone", "We never ask for a gate or alarm code by text, email or web form."),
         ("Stored encrypted", "Codes sit in one system with a login for each person, and access ends the day someone leaves."),
         ("Shown on route day only", "Your technician sees the code on the morning of your visit and at no other time."),
         ("Every view is logged", "The system records who looked at a code and when.")]
TIMES = ["7:14", "7:19", "7:23", "7:31", "7:36", "7:42"]

# name, unit, scale low, scale high, target low, target high, target text
GAUGES = [("fc", "Free chlorine", "ppm", 0, 6, 2, 4, "2 to 4"), ("ph", "pH", "", 6.8, 8.4, 7.4, 7.6, "7.4 to 7.6"),
          ("ta", "Total alkalinity", "ppm", 0, 200, 80, 120, "80 to 120"), ("ch", "Calcium hardness", "ppm", 0, 600, 200, 400, "200 to 400"),
          ("cya", "Cyanuric acid", "ppm", 0, 150, 30, 50, "30 to 50"), ("salt", "Salt", "ppm", 1500, 4500, 2700, 3400, "2,700 to 3,400")]
SCENARIOS = {
    "normal": {"label": "A normal week", "status": "Balanced", "arrived": "7:14 AM", "left": "7:42 AM", "gate": "Latched at 7:42",
               "v": {"fc": 3.0, "ph": 7.5, "ta": 90, "ch": 340, "cya": 45, "salt": 3200}, "img": "brushing",
               "alt": "A technician brushing the tile line of a clear blue pool",
               "did": ["Added 1 quart of muriatic acid", "Brushed walls, steps and the tile line", "Emptied the skimmer and pump baskets", "Filter at 14 psi. Clean is 11, so no cleaning yet"]},
    "storm": {"label": "After a dust storm", "status": "Recovering", "arrived": "6:05 AM", "left": "7:10 AM", "gate": "Latched at 7:10",
              "v": {"fc": 0.5, "ph": 7.9, "ta": 70, "ch": 350, "cya": 45, "salt": 3100}, "img": "storm",
              "alt": "A leaf rake skimming palm fronds and dust from a pool the morning after a storm",
              "did": ["Netted fronds and debris, emptied baskets twice", "Brushed every surface and vacuumed the silt slowly", "Cleaned the filter: 26 psi down to 11", "Shocked the pool. Swimming again by Thursday"]},
    "green": {"label": "Green pool, day one", "status": "Day 1 of 5", "arrived": "8:30 AM", "left": "9:45 AM", "gate": "Latched at 9:45",
              "v": {"fc": 0.0, "ph": 8.2, "ta": 140, "ch": 420, "cya": 110, "salt": 2400}, "img": "green",
              "alt": "A neglected backyard pool with opaque green water",
              "did": ["Netted out debris before any chemicals went in", "Raised chlorine to shock level, and we will hold it there", "Brushed every surface to break up the algae", "Stabilizer is 110, so a partial drain is on your written quote"]},
}


def fmt(k, v):
    if k in ("fc", "ph"):
        return f"{v:.1f}"
    return f"{int(v):,}"


def pct(v, lo, hi):
    return max(2.0, min(98.0, (v - lo) / (hi - lo) * 100))


def state(v, tlo, thi):
    return "In range" if tlo <= v <= thi else ("Low" if v < tlo else "High")


def scenario_json():
    out = {}
    for key, s in SCENARIOS.items():
        rows = {}
        for k, _, _, lo, hi, tlo, thi, _ in GAUGES:
            v = s["v"][k]
            rows[k] = {"t": fmt(k, v), "p": round(pct(v, lo, hi), 1), "s": state(v, tlo, thi)}
        out[key] = {"status": s["status"], "arrived": s["arrived"], "left": s["left"], "gate": s["gate"], "rows": rows,
                    "img": f'{PREFIX}img/{s["img"]}.webp', "alt": s["alt"], "did": s["did"]}
    return json.dumps(out).replace("</", "<\\/")


def head(css, fonts, theme):
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{escape(DESC, quote=True)}">
<meta name="author" content="{BRAND}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{BASE}/">
<meta name="theme-color" content="{theme}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&amp;display=swap">
<link rel="stylesheet" href="assets/{css}">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def ribbon(this, other_href, other_name):
    return (f'<p class="ribbon">Preview {this}. <a href="{other_href}">See {other_name}</a> or '
            f'<a href="index.html">the version that is live now</a>.</p>\n')


def nav_links():
    return "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)


def season_note():
    return '<p class="season" data-monsoon><span class="txt">Monsoon season runs June 15 to September 30.</span> <a href="monsoon-pool-care.html">Read the storm care guide</a></p>'


def faq_items():
    return "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(HOME_FAQ))


def form(btn_class="btn"):
    opts = [("weekly", "Weekly service"), ("green", "My pool is green"), ("repair", "Something is broken"), ("filter", "Filter cleaning")]
    choices = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}">{t}</label>' for v, t in opts)
    return f'''<form class="form" action="#quote" method="post" novalidate data-demo>
<fieldset><legend>What do you need?</legend><div class="choices">{choices}</div></fieldset>
<div class="fields">
<label>ZIP code<input type="text" name="zip" inputmode="numeric" autocomplete="postal-code"></label>
<label>Pool type<select name="type"><option>Chlorine</option><option>Salt</option><option>Not sure</option></select></label>
<label>Full name<input type="text" name="name" autocomplete="name"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="full">Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="{btn_class}" type="submit">Request my quote</button>
<p class="form-note">Leave gate codes and alarm codes out of this form. We collect those by phone after you sign up. See the <a href="privacy.html">privacy page</a>.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live Saltbrush site, a written quote comes back the same business day.</p>
</form>'''


def footer(cls="ft"):
    svcs = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    return f'''<footer class="{cls}"><div class="w">
<div class="ft-cols">
<div><h2>Contact</h2><address>Phoenix, AZ 85016<br><a href="tel:{TEL}">{PHONE}</a><br>Routes Monday to Friday from 6 AM<br>Office 7 AM to 4 PM</address></div>
<div><h2>Services</h2><ul>{svcs}<li><a href="pricing.html">Pricing</a></li></ul></div>
<div><h2>Guides</h2><ul><li><a href="monsoon-pool-care.html">Monsoon and dust storm care</a></li><li><a href="pool-safety.html">Arizona pool barrier law</a></li><li><a href="service-reports.html">Your weekly report</a></li></ul></div>
<div><h2>Where we work</h2><ul>{areas}<li><a href="about.html">About Saltbrush</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
</div>
<p class="ft-base">© 2026 {BRAND}. Licensed for residential pool service and repair in Arizona, ROC classification R-6. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Saltbrush is a fictional company, and its prices are samples.</p>
</div></footer>
<script type="application/json" id="scn">{scenario_json()}</script>
<script src="assets/preview.js" defer></script>
</body>
</html>
'''


def season_table():
    rows = "".join(f'<tr><th scope="row">{s}</th><td>{m}</td><td>{c}</td><td>{d}</td></tr>' for s, m, c, d in SEASONS)
    return ('<div class="tw"><table class="seasons"><caption>The five pool seasons in Phoenix and what weekly service does in each</caption>'
            '<thead><tr><th scope="col">Season</th><th scope="col">Months</th><th scope="col">What changes in the water</th><th scope="col">What we do about it</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')


# ------------------------------------------------------------------ Preview A
def build_a():
    s0 = SCENARIOS["normal"]
    tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if k == "normal" else "false"}" data-s="{k}">{s["label"]}</button>' for k, s in SCENARIOS.items())
    gauges = ""
    for k, name, unit, lo, hi, tlo, thi, ttxt in GAUGES:
        v = s0["v"][k]
        st = state(v, tlo, thi)
        gauges += (f'<div class="g" data-k="{k}" data-state="{st}"><span class="g-k">{name}<small>Target {ttxt}</small></span>'
                   f'<span class="g-v"><b>{fmt(k, v)}</b>{(" " + unit) if unit else ""}</span>'
                   f'<span class="g-t" aria-hidden="true"><span class="band" style="left:{pct(tlo, lo, hi):.1f}%;width:{pct(thi, lo, hi) - pct(tlo, lo, hi):.1f}%"></span>'
                   f'<span class="dot" style="left:{pct(v, lo, hi):.1f}%"></span></span><span class="g-s">{st}</span></div>')
    did = "".join(f"<li>{d}</li>" for d in s0["did"])
    log = "".join(f'<li><time>{t} AM</time><div><h3>{h}</h3><p>{p}</p></div></li>' for t, (h, p) in zip(TIMES, VISIT_STEPS))
    stmt = "".join(f'<tr><th scope="row"><a href="{h}">{n}</a></th><td>{d}</td><td class="amt"><b>{p}</b> {u}</td></tr>' for h, n, d, p, u in PRICES)
    months = "".join(f'<span><abbr title="{full}">{full[:3]}</abbr></span>' for full in
                     ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    route = "".join(
        f'<tr><th scope="row">{day}</th><td><a href="{slug}.html"><img src="img/{AREA[slug]["img"]}.webp" alt="{AREA[slug]["alt"]}" loading="lazy" width="1600" height="1200">{AREA[slug]["name"]}</a></td>'
        f'<td>{AREA[slug]["zip"]}</td><td>{AREA[slug]["line"]}</td></tr>' for day, slug in ROUTE)
    worries = "".join(f'<div><h3>“{q}”</h3><p>{a}</p></div>' for q, a in WORRIES)
    codes = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in CODES)
    reviews = "".join(f'<figure><blockquote>{t}</blockquote><figcaption>{w}, {p} <span>Sample review</span></figcaption></figure>' for t, w, p in REVIEWS)
    body = f'''{ribbon("A, The Report", "preview-b.html", "preview B, The Deep End")}<header class="hd"><div class="w hd-in">
<a class="mark" href="index.html" aria-label="{BRAND}, home">{MARK}<span>Saltbrush Pool Care</span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a><a class="btn" href="#quote">Get a quote</a>
</div></header>
<main id="main">
<section class="hero"><div class="w hero-g">
<div class="hero-copy">
<h1>We service your pool every week, and send you the proof.</h1>
<p class="lede">Saltbrush is a pool service and repair company for central Phoenix, Arcadia, Ahwatukee and Tempe. One technician looks after your pool. Before the truck leaves your street, a report like this one is on your phone.</p>
<div class="acts"><a class="btn" href="#quote">Get a written quote</a><a class="call" href="tel:{TEL}">or call {PHONE}</a></div>
{season_note()}
</div>
<article class="sheet" aria-labelledby="rep-h">
<header class="sheet-hd"><div><h2 id="rep-h">Visit report</h2><p>Sample pool, Arcadia 85018</p></div><p class="status" data-f="status">{s0["status"]}</p></header>
<div class="tabs" role="tablist" aria-label="Choose a sample week">{tabs}</div>
<dl class="meta"><div><dt>Arrived</dt><dd data-f="arrived">{s0["arrived"]}</dd></div><div><dt>Left</dt><dd data-f="left">{s0["left"]}</dd></div><div><dt>Technician</dt><dd>Tamsin O.</dd></div><div><dt>Gate</dt><dd data-f="gate">{s0["gate"]}</dd></div></dl>
<div class="gauges">{gauges}</div>
<div class="did"><img data-f="img" src="img/{s0["img"]}.webp" alt="{s0["alt"]}" width="1600" height="1200"><div><h3>What we did</h3><ul data-f="did">{did}</ul></div></div>
<p class="sheet-ft">Sample data written for this demo. Pick a week above to see how the report changes.</p>
</article>
</div></section>

<section class="sec" aria-labelledby="log-h"><div class="w log-g">
<div class="log-copy"><h2 id="log-h">What happens on a weekly visit?</h2>
<p>The visit follows the same six steps at every pool, every week. It takes 25 to 35 minutes, and nothing is skipped because the route is running late.</p>
<p>Testing comes first because the readings decide everything else. We use a drop test kit at the pool, which is slower than a strip and far more accurate, and the numbers go into your report as they are read.</p>
<img src="img/testing.webp" alt="A Saltbrush technician in a sun hat holding a water test vial up to the light beside an open test kit" loading="lazy" width="1600" height="1200">
<p><a href="weekly-pool-service.html">Everything included in weekly service</a></p></div>
<ol class="log">{log}</ol>
</div></section>

<section class="sec white" aria-labelledby="cost-h"><div class="w">
<div class="sec-hd"><h2 id="cost-h">How much does pool service cost?</h2><p>Every price we charge is on this site. Weekly service is one flat monthly number, the same in July as in January.</p></div>
<div class="tw"><table class="stmt"><caption>Saltbrush sample prices</caption><thead><tr><th scope="col">Service</th><th scope="col">What it covers</th><th scope="col" class="amt">Price</th></tr></thead><tbody>{stmt}</tbody></table></div>
<p class="fine">Repairs and cleanups get a written price before any work starts, and you approve it from your phone. See the <a href="pricing.html">full price list</a>.</p>
</div></section>

<section class="sec" aria-labelledby="year-h"><div class="w">
<div class="sec-hd"><h2 id="year-h">What does a Phoenix year do to a pool?</h2><p>The desert has five pool seasons, and each one asks for something different. The marker shows today.</p></div>
<div class="year" aria-hidden="true"><div class="months">{months}</div>
<div class="bands"><span class="b winter" style="grid-column:1/3">Winter</span><span class="b spring" style="grid-column:3/6">Spring</span><span class="b summer" style="grid-column:6/10">Summer</span><span class="b fall" style="grid-column:10/12">Fall</span><span class="b winter" style="grid-column:12/13">Winter</span></div>
<div class="mon"><span style="left:45.6%;width:29.4%">Monsoon, June 15 to September 30</span></div>
<span class="today" data-today></span></div>
{season_table()}
<p class="fine">Monsoon dates are the National Weather Service definition for Arizona. Read the guide to <a href="monsoon-pool-care.html">monsoon and dust storm pool care</a>.</p>
</div></section>

<section class="sec white" aria-labelledby="route-h"><div class="w">
<div class="sec-hd"><h2 id="route-h">Which neighborhoods are on our routes?</h2><p>Each neighborhood has its own route days. Tight routes mean more time at each pool and less time on the 51.</p></div>
<div class="tw"><table class="route"><caption>Saltbrush route days by neighborhood</caption><thead><tr><th scope="col">Day</th><th scope="col">Neighborhood</th><th scope="col">ZIP</th><th scope="col">What we see there</th></tr></thead><tbody>{route}</tbody></table></div>
</div></section>

<section class="sec" aria-labelledby="worry-h"><div class="w">
<div class="sec-hd"><h2 id="worry-h">What worries pool owners most?</h2><p>Three things we hear on almost every first call, and what we do about each.</p></div>
<div class="worries">{worries}</div>
</div></section>

<section class="sec deep" aria-labelledby="code-h"><div class="w code-g">
<div><h2 id="code-h">How is my gate code protected?</h2><p>A pool company knows when you are away and how to open your gate. We treat your code like a house key.</p><p><a href="service-reports.html">How reports and codes are protected</a></p>
<p class="kid">Small children at home? Arizona law sets rules for pool fences and gates, and we check your gate on every visit. <a href="pool-safety.html">Read the pool barrier guide</a>.</p></div>
<ul class="codes">{codes}</ul>
</div></section>

<section class="sec white" aria-labelledby="rev-h"><div class="w">
<div class="sec-hd"><h2 id="rev-h">What do customers say?</h2><p>Sample reviews written for this demo.</p></div>
<div class="reviews">{reviews}</div>
</div></section>

<section class="sec" aria-labelledby="faq-h"><div class="w faq-g">
<div><h2 id="faq-h">Pool service in Phoenix, answered</h2><p>Still have a question? Call <a href="tel:{TEL}">{PHONE}</a> and a person answers.</p></div>
<div class="faq">{faq_items()}</div>
</div></section>

<section class="sec white" id="quote" aria-labelledby="quote-h"><div class="w quote-g">
<div><h2 id="quote-h">Tell us about your pool</h2><p>Five details and we send a written quote the same business day. No one comes to the gate until you say so.</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p><p class="fine">Routes run Monday to Friday from 6 AM. The office answers 7 AM to 4 PM, Arizona time.</p></div>
{form()}
</div></section>
</main>
'''
    return head("preview-a.css", "family=Geologica:wght@300..800", "#07303A") + body + footer()


# ------------------------------------------------------------------ Preview B
VIAL_COLORS = {"fc": "#F28DB6", "ph": "#F0603F", "ta": "#E0483E", "ch": "#3F74D8", "cya": "#DCE6E8", "salt": "#F3C96B"}


def tile(depth):
    return f'<span class="tile" aria-hidden="true">{depth} FT</span>'


def build_b():
    s0 = SCENARIOS["normal"]
    vials = ""
    for k, name, unit, lo, hi, tlo, thi, ttxt in GAUGES:
        vials += (f'<li><span class="vial" style="--c:{VIAL_COLORS[k]}" aria-hidden="true"></span><b>{fmt(k, s0["v"][k])}</b>'
                  f'<span>{name}</span><small>Target {ttxt}{(" " + unit) if unit else ""}</small></li>')
    lanes = "".join(
        f'<li><a href="{s["slug"]}.html"><h3>{s["name"]}</h3><p>{s["short"]}</p><p class="amt"><b>{s["from"]}</b> {s["unit"]}</p></a></li>'
        for s in SERVICES)
    lap = "".join(f'<li><h3>{h}</h3><p>{p}</p></li>' for h, p in VISIT_STEPS)
    hoods = "".join(
        f'<a class="hood" href="{a["slug"]}.html"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1600" height="1200">'
        f'<h3>{a["name"]}</h3><p>{a["line"]}.</p><p class="when">{a["day"]}, ZIP {a["zip"]}</p></a>' for a in AREAS)
    worries = "".join(f'<div><h3>“{q}”</h3><p>{a}</p></div>' for q, a in WORRIES)
    reviews = "".join(f'<figure><blockquote>{t}</blockquote><figcaption>{w}, {p} <span>Sample review</span></figcaption></figure>' for t, w, p in REVIEWS)
    body = f'''{ribbon("B, The Deep End", "preview-a.html", "preview A, The Report")}<div class="rail" aria-hidden="true"><span class="rail-mark" data-depth>0 FT</span></div>
<main id="main">
<section class="surface">
<div class="sky"><div class="sun"></div>
<header class="hd"><div class="w hd-in">
<a class="mark" href="index.html" aria-label="{BRAND}, home">{MARK}<span>Saltbrush Pool Care</span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a>
</div></header>
<div class="w hero">
<h1>Clear to the bottom, every week of the year.</h1>
<p class="lede">Saltbrush is a pool service and repair company for central Phoenix, Arcadia, Ahwatukee and Tempe. One technician looks after your pool, and a report with six readings and a photo reaches your phone after every visit.</p>
<div class="acts"><a class="btn" href="#quote">Get a written quote</a><a class="call" href="tel:{TEL}">or call {PHONE}</a></div>
{season_note()}
</div></div>
<svg class="waterline" viewBox="0 0 2880 80" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 40c120-36 240 36 360 0s240 36 360 0 240 36 360 0 240 36 360 0 240 36 360 0 240 36 360 0 240 36 360 0 240 36 360 0v40H0z"/></svg>
</section>

<section class="d d3" aria-labelledby="test-h"><div class="w test-g">
<div><div class="hd2">{tile(3)}<h2 id="test-h">What do we test every week?</h2></div>
<p>Six readings, every visit, with a drop test kit at the edge of your pool. A kit is slower than a strip and far more accurate, and the numbers decide everything else we do that day.</p>
<p>Each reading goes on your report beside its target, with what we added to correct it. <a href="service-reports.html">See what the weekly report shows</a>.</p>
<ul class="vials">{vials}</ul>
<p class="fine">Sample readings from a balanced pool.</p></div>
<img src="img/testing.webp" alt="A Saltbrush technician in a sun hat holding a water test vial up to the light beside an open test kit" width="1600" height="1200">
</div></section>

<section class="d d4" aria-labelledby="svc-h"><div class="w">
<div class="hd2">{tile(4)}<h2 id="svc-h">What does Saltbrush do?</h2></div>
<p class="intro">Four services, each with its price on the page. Weekly service is one flat monthly number with chemicals included. <a href="pricing.html">See every price</a>.</p>
<ul class="lanes">{lanes}</ul>
</div></section>

<section class="d d5" aria-labelledby="lap-h"><div class="w">
<div class="hd2">{tile(5)}<h2 id="lap-h">What happens on a weekly visit?</h2></div>
<p class="intro">The same six steps at every pool, every week. The visit takes 25 to 35 minutes, and nothing is skipped because the route is running late.</p>
<ol class="lap">{lap}</ol>
</div></section>

<section class="d d6" aria-labelledby="year-h"><div class="w">
<div class="hd2">{tile(6)}<h2 id="year-h">What does a Phoenix year do to a pool?</h2></div>
<p class="intro">The desert has five pool seasons, and each one asks for something different. Monsoon dates are the National Weather Service definition for Arizona.</p>
{season_table()}
<div class="storm"><img src="img/haboob.webp" alt="A towering wall of dust rolling toward a Phoenix neighborhood at dusk, with a calm backyard pool in the foreground" loading="lazy" width="1600" height="1200">
<div><h3>When a dust storm hits</h3><p>Weekly customers get a cleanup visit on their next route day, or sooner when we add a storm day. We net the debris, vacuum the silt, clean the filter and test the water again.</p><p><a href="monsoon-pool-care.html">Read the monsoon and dust storm guide</a></p></div></div>
</div></section>

<section class="d d7" aria-labelledby="hood-h"><div class="w">
<div class="hd2">{tile(7)}<h2 id="hood-h">Which neighborhoods are on our routes?</h2></div>
<p class="intro">Tight routes mean more time at each pool and less time on the 51.</p>
<div class="hoods">{hoods}</div>
</div></section>

<section class="d d8" aria-labelledby="worry-h"><div class="w">
<div class="hd2">{tile(8)}<h2 id="worry-h">What worries pool owners most?</h2></div>
<div class="worries">{worries}</div>
<div class="reviews">{reviews}</div>
<p class="keys"><b>Your gate code is treated like a house key.</b> It is collected by phone, stored encrypted and shown to your technician on route day only. <a href="service-reports.html">How reports and codes are protected</a>. Small children at home? <a href="pool-safety.html">Read the Arizona pool barrier guide</a>.</p>
</div></section>

<section class="d d9" id="quote" aria-labelledby="quote-h"><div class="w deep-g">
<div><div class="hd2">{tile(9)}<h2 id="quote-h">Tell us about your pool</h2></div>
<p>Five details and we send a written quote the same business day. No one comes to the gate until you say so.</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p>
<h3 class="faq-h" id="faq-h">Pool service in Phoenix, answered</h3>
<div class="faq">{faq_items()}</div></div>
{form()}
</div><div class="drain" aria-hidden="true"></div></section>
</main>
'''
    return (head("preview-b.css", "family=Big+Shoulders+Display:wght@600;800;900&amp;family=Atkinson+Hyperlegible:wght@400;700", "#052B3D")
            + body + footer())


def write(name, html):
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1)
    if len(title) > 60 or "&" in title:
        PROBLEMS.append(f"{name}: title")
    if not 120 <= len(desc) <= 160:
        PROBLEMS.append(f"{name}: description is {len(desc)} chars")
    if html.count("<h1") != 1:
        PROBLEMS.append(f"{name}: {html.count('<h1')} h1 elements")
    if 'alt=""' in html:
        PROBLEMS.append(f"{name}: empty alt text")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(absolutize(html))
    words = len(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S).split())
    print(f"  {name:20s} {len(html)//1024:>3} KB  {words:>5} words")


if __name__ == "__main__":
    print("Building Saltbrush previews:")
    write("preview-a.html", build_a())
    write("preview-b.html", build_b())
    if PROBLEMS:
        print("\n".join(PROBLEMS))
        sys.exit(1)
