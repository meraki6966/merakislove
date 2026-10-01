"""Build the Keelhouse Home Services demo into public/demos/keelhouse/.

Run from the repo root:  python3 scripts/demos/keelhouse/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kh import *  # noqa: E402,F403
from content import HOME_FAQ, SERVICE_PAGES, CITY_PAGES, PROJECT_PAGES, HOW_FAQ, AREAS_FAQ, SERVICES_FAQ, REVIEWS  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "keelhouse")


# Pages live at /demos/keelhouse/... and the home page is also served at the
# clean URL /demos/keelhouse (no trailing slash). Relative paths would resolve
# against /demos/ there, so every local href and src is written root-absolute.
# PREFIX="" (env) builds a relative copy for previewing outside the site.
PREFIX = os.environ.get("PREFIX", "/demos/keelhouse/")
OUT = os.environ.get("OUT", OUT)


def absolutize(html):
    import re
    if not PREFIX:
        return html

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|tel:|mailto:|#|/|data:)", url):
            return m.group(0)
        if url == "index.html" or url.startswith("index.html?") or url.startswith("index.html#"):
            return f'{attr}="{PREFIX.rstrip("/")}{url[len("index.html"):]}"'
        return f'{attr}="{PREFIX}{url}"'
    return re.sub(r'\b(href|src)="([^"]+)"', fix, html)


def write(name, html):
    html = absolutize(html)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {name:42s} {len(html)//1024:>4} KB")


def svc_cards():
    return "".join(f'''<a class="svc-card reveal" href="{s["slug"]}.html"><img src="img/{s["img"]}.webp" alt="" loading="lazy" width="1100" height="1480">
<span class="svc-body"><span class="svc-text"><span class="label">0{i+1}  /  Visits from {s["visit"]}</span><b>{s["name"]}</b><span>{s["short"]}</span></span><span class="circle-arrow">{ic("arrow")}</span></span></a>''' for i, s in enumerate(SERVICES))


def proj_card(p, feature=False):
    return f'''<a class="proj-card reveal{" proj-feature" if feature else ""}" href="{p["slug"]}.html">
<span class="img"><img src="img/{p["img"]}.webp" alt="" loading="lazy" width="1800" height="1338"></span>
<span class="label">{p["trade"]}  ·  {p["city"]}</span>
<b>{p["title"]}</b>
<span class="go">Read the project{ic("arrow")}</span></a>'''


def city_cells(link=True):
    out = []
    for i, c in enumerate(CITIES):
        tag = "a" if link else "div"
        href = f' href="{c["slug"]}.html"' if link else ""
        out.append(f'''<{tag} class="cell"{href}><span class="label">0{i+1}</span><b>{c["name"]}</b><span class="small">{c["hoods"]}</span><span class="meta">{ic("clock")}{c["drive"]}</span></{tag}>''')
    return "".join(out)


def reviews_band(items, title='What neighbors <em class="accent">say.</em>'):
    cards = "".join(review_card(*r) for r in items)
    return f'''{angle("var(--paper)", "var(--ink)")}<section class="section dark grid-bg" style="padding-top:72px" aria-labelledby="rev-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">What neighbors say</span><h2 class="h-lg" id="rev-h">{title}</h2></div>
<p>Reviews on a live site load from the Google Business Profile with the reviewer's name. The ones below are samples for this demo.</p></div>
<div class="grid cols-3">{cards}</div>
</div>
</section>
'''


PHASES = [("01", "Call or book", "Tell us what the house is doing. We text back with an arrival window, usually the same day."),
          ("02", "Diagnose on site", "The tech finds the cause first. No guessing, and no parts thrown at the problem."),
          ("03", "Approve the price", "You see a written price before anything starts. The visit fee comes off if you go ahead."),
          ("04", "Fixed and documented", "Photos and notes go into your home's file, so the next visit starts with the history.")]


def phases_block(dark=True, title='From the first call to the <em class="accent">final photo.</em>', link=True):
    ph = "".join(f'<div class="phase reveal"><div class="num">{n}</div><h3>{t}</h3><p>{d}</p></div>' for n, t, d in PHASES)
    more = '<div class="center" style="margin-top:64px"><a class="btn btn-ghost" href="how-we-work.html">See the full process</a></div>' if link else ""
    return f'''<section class="section {"dark grid-bg" if dark else "paper"}" aria-labelledby="how-h">
<div class="wrap">
<div class="section-head center"><div><span class="eyebrow">How we work</span><h2 class="h-lg" id="how-h">{title}</h2></div></div>
<div class="phases">{ph}</div>{more}
</div>
</section>
'''


def stats_block():
    yrs = 2026 - YEAR_FOUNDED
    items = [(f"{yrs}", "", "Years in Columbus"), ("6,000", "+", "Homes serviced"), ("3", "", "Licensed trades in house"), ("24/7", "", "Emergency line")]
    return '<section class="dark-2" style="border-top:1px solid var(--line-dark);border-bottom:1px solid var(--line-dark)"><div class="wrap stats">' + "".join(
        f'<div><b>{n}<i>{p}</i></b><span>{l}</span></div>' for n, p, l in items) + "</div></section>\n"


WORRIES = [("I can't tell if it's plumbing or electrical.", "You don't need to. One call covers all three trades, and the tech who arrives can trace a problem across them, like a water heater that keeps tripping a breaker."),
           ("I'm worried about a surprise bill.", "You approve a written price before work starts. If the job grows once a wall is open, we stop and show you before going further."),
           ("I've had techs who never showed up.", "You get a two hour window by text and a heads up when the tech is twenty minutes out. If we're running late, you hear it from us first."),
           ("I don't want my house torn up.", "Floor runners, shoe covers, and a cleanup before we leave. Every job ends with photos of the finished work.")]


def worries_block():
    acc = "".join(f'<details{" open" if i == 0 else ""}><summary>&#8220;{q}&#8221;{ic("chev")}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(WORRIES))
    return f'''<section class="split paper" aria-labelledby="worry-h">
<div class="split-media"><img src="img/founder.webp" alt="{FOUNDER}, founder of Keelhouse, in his workshop" loading="lazy" width="1100" height="1480" style="object-position:center 25%">
<div class="quote-card"><p>&#8220;I built Keelhouse so a family calls one number, and the person who shows up can fix the whole problem.&#8221;</p><span>{FOUNDER}  ·  Founder and master plumber</span></div></div>
<div class="split-body">
<span class="eyebrow">Before you call</span>
<h2 class="h-lg" id="worry-h">What usually holds people back.</h2>
<p class="lede" style="font-size:16px">Letting a stranger into your basement is a big ask. These are the four worries we hear most, and how we handle each one.</p>
<div class="acc quotes">{acc}</div>
<div><a class="btn btn-ink" href="tel:{TEL}">{ic("phone")}Ask us anything</a></div>
</div>
</section>
'''


def areas_block(title='Service areas across <em>Central Ohio.</em>'):
    return f'''<section class="section white" aria-labelledby="areas-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">Where we work</span><h2 class="h-lg" id="areas-h">{title}</h2></div>
<p>Each city has its own page with the neighborhoods we cover, the jobs we see most there, and typical arrival times.</p></div>
<div class="cells">{city_cells()}</div>
<div class="bar"><div><b>Don't see your town?</b><span class="small">We also cover Hilliard, Upper Arlington, Worthington, Gahanna and Powell.</span></div><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}Call now</a></div>
</div>
</section>
'''


# ====================================================================== HOME
def build_home():
    stats = f'''<div class="hero-stats"><div><b>{YEAR_FOUNDED}</b><span>Serving Columbus since</span></div><div><b>6,000<i>+</i></b><span>Homes serviced</span></div><div><b>3</b><span>Licensed trades in house</span></div></div>'''
    hero = f'''<section class="hero hero-home">
<img class="hero-img" src="img/hero.webp" alt="A Keelhouse technician walking up the front path of a brick colonial home at sunset" fetchpriority="high" width="2400" height="1355">
<div class="hero-inner"><div class="wrap hero-grid">
<div class="hero-copy">
<span class="eyebrow">Columbus  ·  Dublin  ·  Westerville  ·  Grove City</span>
<h1 class="h-xl">One crew for the <em class="accent">whole house.</em></h1>
<p class="lede">Plumbing, heating and electrical for Central Ohio homes, handled by licensed techs who show up when they say and leave the house the way they found it.</p>
<div class="btn-row"><a class="btn btn-copper" href="#book">Book a visit</a><a class="btn btn-ghost" href="#work">See recent work</a></div>
</div>
{stats}
</div></div>
</section>
'''
    tiles = "".join(f'<a class="tile reveal" href="index.html?need={v}#book">{ic(i)}<span>{t}</span></a>' for v, i, t in NEEDS)
    triage = f'''<section class="section paper" style="padding-bottom:96px" aria-labelledby="triage-h">
<div class="wrap">
<div class="section-head"><div><h2 class="h-md" id="triage-h">What's going on at the house?</h2></div><p>Pick the closest match. The booking form opens with it already checked.</p></div>
<div class="grid cols-6">{tiles}</div>
</div>
</section>
'''
    services = f'''<section class="section paper" style="padding-top:0" aria-labelledby="svc-h">
<div class="wrap">
<div class="section-head center"><div><span class="eyebrow">Our services</span><h2 class="h-lg" id="svc-h">Three trades. <em>One</em> number to call.</h2></div></div>
<div class="grid cols-3">{svc_cards()}</div>
</div>
</section>
'''
    work = f'''<section id="work" class="section paper" aria-labelledby="work-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">Recent work</span><h2 class="h-lg" id="work-h">Every job gets a write up.</h2></div>
<p>Photos, the problem we found, and what we did about it. Each project has its own page, named by the job and the town, so neighbors searching for the same fix can find it.</p></div>
<div class="grid cols-3 gap-32">{"".join(proj_card(p) for p in PROJECTS)}</div>
<div class="center" style="margin-top:56px"><a class="btn btn-outline" href="projects.html">View all projects</a></div>
</div>
</section>
'''
    body = (hero + triage + services + reviews_band(REVIEWS[:3]) + work + phases_block() + stats_block() + worries_block() + areas_block()
            + faq_block("Straight answers.", HOME_FAQ, "These are marked up so Google and AI search can quote them word for word.") + booking())
    schemas = [business_schema(), faq_schema(HOME_FAQ), {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/"}]
    write("index.html", page("index.html", "Keelhouse Home Services | Plumbing, Heating &amp; Electrical in Columbus, OH",
                             "Licensed plumbing, heating and cooling, and electrical for Columbus, Dublin, Westerville and Grove City homes. Same day windows, written prices, 24/7 emergency line.",
                             schemas, "home", body))


# ====================================================================== SERVICES HUB
def build_services_hub():
    rows = []
    for i, s in enumerate(SERVICES):
        sp = SERVICE_PAGES[s["slug"]]
        jobs = "".join(f'<li>{ic("check")}<span>{j}</span></li>' for j, _, _ in sp["prices"][1:5])
        rows.append(f'''<div class="alt-row{" flip" if i % 2 else ""} {"white" if i % 2 else "paper"}">
<div class="alt-media"><img src="img/{s["img"]}.webp" alt="{sp["img_alt"]}" loading="lazy" width="1100" height="1480"></div>
<div class="alt-body"><div class="num">0{i+1}</div><h2 class="h-lg">{s["name"]}</h2><p class="lede" style="font-size:17px">{sp["summary"]}</p>
<ul class="checks" style="grid-template-columns:1fr">{jobs}</ul>
<div class="btn-row"><a class="btn btn-ink" href="{s["slug"]}.html">{s.get("plain", s["name"])} in detail</a></div><p class="small">Diagnostic visits from {s["visit"]}, credited toward the repair.</p></div>
</div>''')
    cross = f'''<section class="section dark grid-bg" aria-labelledby="cross-h">
<div class="wrap split" style="gap:56px;align-items:center">
<div style="display:grid;gap:20px"><span class="eyebrow">When it's more than one trade</span><h2 class="h-lg" id="cross-h">The water heater that keeps <em class="accent">tripping a breaker.</em></h2>
<p class="lede" style="font-size:17px">Half the calls we get sit between trades. A plumber blames the wiring, an electrician blames the heater, and you pay for two visits. Our techs are cross trained to trace the whole problem, and a licensed specialist for each trade is one radio call away.</p></div>
<ul class="checks">{"".join(f"<li>{ic('check')}<span>{t}</span></li>" for t in ["Sump pump that kills a GFCI outlet", "Furnace that won't light after a power surge", "Tankless heater that needs a new circuit", "Heat pump install with a panel upgrade", "Bathroom remodel rough in, water and power", "Basement flood, then the electrical check"])}</ul>
</div>
</section>
'''
    body = (page_hero("hero", "Services", 'Plumbing, heating and electrical, <em class="accent">under one roof.</em>',
                      "Three licensed trades on one crew, with written prices and diagnostic visits credited toward the repair.",
                      [("Home", "index.html"), ("Services", "")], "A Keelhouse technician arriving at a brick colonial home")
            + "".join(rows) + cross + faq_block("Service questions.", SERVICES_FAQ, "Answers about pricing, scheduling and what each trade covers.") + booking())
    schemas = [business_schema(), faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")])]
    write("services.html", page("services.html", "Services | Plumbing, Heating &amp; Cooling, Electrical | Keelhouse Home Services",
                                "Plumbing, heating and cooling, and electrical services for Central Ohio homes. Written prices, credited diagnostic visits, 24/7 emergency line.",
                                schemas, "services", body))


# ====================================================================== SERVICE PAGES
def build_service(s):
    sp = SERVICE_PAGES[s["slug"]]
    plain = s.get("plain", s["name"])
    prices = "".join(f'<div class="price"><div><b>{n}</b><span>{d}</span></div><strong>{p}</strong></div>' for n, d, p in sp["prices"])
    signs = "".join(f'<li>{ic("check")}<span>{t}</span></li>' for t in sp["signs"])
    city_links = "".join(f'<a class="cell" href="{c["slug"]}.html"><span class="label">{plain} in</span><b>{c["name"]}</b><span class="meta">{ic("clock")}{c["drive"]}</span></a>' for c in CITIES)
    proj = next(p for p in PROJECTS if p["slug"] == sp["project"])
    others = [x for x in SERVICES if x["slug"] != s["slug"]]
    body = (page_hero(s["img"], f"Services  ·  {s['name']}", sp["h1"], sp["lede"],
                      [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")], sp["img_alt"])
            + f'''<section class="section paper" aria-labelledby="price-h">
<div class="wrap faq-layout">
<div><span class="eyebrow">What we do</span><h2 class="h-lg" id="price-h">{sp["price_title"]}</h2><p class="small">Prices shown are starting points for typical homes in Columbus and the suburbs. You approve the exact number in writing before work begins.</p>
<a class="btn btn-ink" href="#book" style="justify-self:start">Get a price</a></div>
<div class="prices">{prices}</div>
</div>
</section>
<section class="section white" aria-labelledby="signs-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">When to call</span><h2 class="h-lg" id="signs-h">Signs it's time for a visit.</h2></div><p>{sp["signs_lead"]}</p></div>
<ul class="checks">{signs}</ul>
</div>
</section>
''' + phases_block(dark=True, title="How a visit runs.", link=True)
            + f'''<section class="section paper" aria-labelledby="near-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">Near you</span><h2 class="h-lg" id="near-h">{plain} across Central Ohio.</h2></div><p>Every city page lists the neighborhoods we cover and the jobs we see most there.</p></div>
<div class="cells" style="background:var(--white)">{city_links}</div>
</div>
</section>
<section class="section white" aria-labelledby="proj-h">
<div class="wrap split" style="gap:56px;align-items:center">
<div style="display:grid;gap:20px"><span class="eyebrow">From the job file</span><h2 class="h-md" id="proj-h">{proj["title"]}</h2>
<p class="lede" style="font-size:17px">{PROJECT_PAGES[proj["slug"]]["summary"]}</p>
<div><a class="text-link" href="{proj["slug"]}.html">Read the project{ic("arrow")}</a></div>
<p class="small">Other trades: {" and ".join(f'<a href="{o["slug"]}.html">{o["name"]}</a>' for o in others)}.</p></div>
<a class="proj-card" href="{proj["slug"]}.html"><span class="img"><img src="img/{proj["img"]}.webp" alt="" loading="lazy" width="1800" height="1338" style="height:440px"></span></a>
</div>
</section>
''' + faq_block(f"{plain} questions.", sp["faq"], "Written for the searches people run when something stops working.")
            + booking(preset=sp["preset"]))
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": plain, "serviceType": plain,
                  "provider": {"@id": f"{BASE}/#business"}, "areaServed": [{"@type": "City", "name": f"{c['name']}, Ohio"} for c in CITIES],
                  "offers": [{"@type": "Offer", "name": strip(n), "description": strip(d)} for n, d, _ in sp["prices"]]}
    schemas = [business_schema(), svc_schema, faq_schema(sp["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (plain, f'{s["slug"]}.html')])]
    write(f'{s["slug"]}.html', page(f'{s["slug"]}.html', sp["title"], sp["desc"], schemas, "services", body))


# ====================================================================== AREAS HUB
def map_svg():
    import math
    pts = {"Columbus": (39.9612, -82.9988), "Dublin": (40.0992, -83.1141), "Westerville": (40.1262, -82.9291), "Grove City": (39.8815, -83.0930),
           "Hilliard": (40.0334, -83.1582), "Upper Arlington": (40.0276, -83.0624), "Worthington": (40.0931, -83.0180), "Gahanna": (40.0192, -82.8793), "Powell": (40.1578, -83.0752)}
    lat0, lon0 = 39.99, -83.01
    k = 2600
    W, H = 900, 640

    def xy(lat, lon):
        return (W / 2 + (lon - lon0) * math.cos(math.radians(lat0)) * k, H / 2 - (lat - lat0) * k)
    cx, cy = xy(*pts["Columbus"])
    mi = k / 69.0  # px per mile (1 degree of latitude is about 69 miles)
    rings = ""
    for r_mi, lab in [(6, "10 min"), (12, "20 min"), (18, "30 min")]:
        r = r_mi * mi
        rings += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r:.0f}" fill="none" stroke="#3E5163" stroke-width="1.5" stroke-dasharray="4 7"/>'
        rings += f'<text x="{cx + r * 0.71:.0f}" y="{cy + r * 0.71 + 16:.0f}" fill="#9AA6B2" font-size="13" font-family="Hanken Grotesk, sans-serif" letter-spacing="1">{lab.upper()}</text>'
    dots = ""
    for name, (la, lo) in pts.items():
        x, y = xy(la, lo)
        main = name in ("Columbus", "Dublin", "Westerville", "Grove City")
        if main:
            dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{9 if name == "Columbus" else 7}" fill="#C9733A"/>'
            dots += f'<text x="{x + 14:.0f}" y="{y + 7:.0f}" fill="#F3EEE6" font-size="24" font-family="Instrument Serif, serif">{name}</text>'
        else:
            dots += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="none" stroke="#A9B3BE" stroke-width="1.5"/>'
            dots += f'<text x="{x + 10:.0f}" y="{y + 5:.0f}" fill="#A9B3BE" font-size="13" font-family="Hanken Grotesk, sans-serif">{name}</text>'
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Map of Keelhouse service areas around Columbus, Ohio, with drive time rings from the Columbus dispatch">'
            f'{rings}<text x="{cx - 70:.0f}" y="{cy + 36:.0f}" fill="#E09A62" font-size="11" letter-spacing="2" font-family="Hanken Grotesk, sans-serif">DISPATCH</text>{dots}</svg>')


def build_areas_hub():
    body = (page_hero("city-columbus", "Service areas", 'Local to <em class="accent">Central Ohio.</em>',
                      "One dispatch in Columbus, four home bases, and techs who already know the housing stock in your neighborhood.",
                      [("Home", "index.html"), ("Service Areas", "")], "Brick Italianate homes on a brick street in Columbus")
            + f'''<section class="section dark grid-bg" aria-labelledby="map-h">
<div class="wrap split" style="gap:56px;align-items:center">
<div style="display:grid;gap:20px"><span class="eyebrow">Drive times</span><h2 class="h-lg" id="map-h">Close enough to be <em class="accent">same day.</em></h2>
<p class="lede" style="font-size:17px">Our trucks leave from one Columbus dispatch every morning. Most of the metro sits inside a thirty minute ring, which is why most weekday calls get a same day window.</p>
<p class="small">Rings are approximate drive times outside rush hour.</p></div>
<div class="map-wrap">{map_svg()}</div>
</div>
</section>
''' + areas_block("Pick your city.") + faq_block("Service area questions.", AREAS_FAQ, "Coverage, arrival windows and permits across the metro.") + booking())
    schemas = [business_schema(), faq_schema(AREAS_FAQ), crumbs_schema([("Home", ""), ("Service Areas", "service-areas.html")])]
    write("service-areas.html", page("service-areas.html", "Service Areas | Columbus, Dublin, Westerville, Grove City | Keelhouse",
                                     "Keelhouse serves Columbus, Dublin, Westerville and Grove City, plus Hilliard, Upper Arlington, Worthington, Gahanna and Powell.",
                                     schemas, "areas", body))


# ====================================================================== CITY PAGES
def build_city(c):
    cp = CITY_PAGES[c["slug"]]
    rows = [("clock", "Typical arrival", cp["arrival"]), ("pin", "Dispatched from", cp["dispatch"]), ("wrench", "Most booked here", cp["most"])]
    glance_rows = "".join(f'<div class="row">{ic(i)}<div><small>{a}</small><span>{b}</span></div></div>' for i, a, b in rows)
    zips = "".join(f'<span class="chip">{z}</span>' for z in cp["zips"])
    glance = f'<aside class="glance" aria-label="{c["name"]} at a glance"><h2>{c["name"]} at a glance</h2>{glance_rows}<div class="row" style="display:grid;gap:12px"><small style="font-size:11px;letter-spacing:2px;color:var(--muted);font-weight:700">ZIP CODES</small><div class="chips">{zips}</div></div></aside>'
    hoods = "".join(f'<div class="cell reveal"><span class="label">0{i+1}</span><h3>{n}</h3><p class="small">{d}</p></div>' for i, (n, d) in enumerate(cp["hoods"]))
    jobs = "".join(f'<div class="cell reveal" style="background:var(--white)"><span class="label">{t}</span><h3>{h}</h3><p class="small">{d}</p></div>' for t, h, d in cp["jobs"])
    proj = next((p for p in PROJECTS if p["city_slug"] == c["slug"]), None)
    proj_html = ""
    if proj:
        proj_html = f'''<section class="section white" aria-labelledby="cproj-h">
<div class="wrap split" style="gap:56px;align-items:center">
<a class="proj-card" href="{proj["slug"]}.html"><span class="img"><img src="img/{proj["img"]}.webp" alt="" loading="lazy" width="1800" height="1338" style="height:420px"></span></a>
<div style="display:grid;gap:20px"><span class="eyebrow">A {c["name"]} job</span><h2 class="h-md" id="cproj-h">{proj["title"]}</h2>
<p class="lede" style="font-size:17px">{PROJECT_PAGES[proj["slug"]]["summary"]}</p><div><a class="text-link" href="{proj["slug"]}.html">Read the project{ic("arrow")}</a></div></div>
</div>
</section>
'''
    trades = "".join(f'''<a class="cell" href="{s["slug"]}.html" style="background:var(--white)"><span class="label">Visits from {s["visit"]}</span><b>{s["name"]}</b><span class="small">{s["short"]}</span><span class="meta">{ic("arrow")}In {c["name"]}</span></a>''' for s in SERVICES)
    nearby = "".join(f'<a class="cell" href="{o["slug"]}.html"><b>{o["name"]}</b><span class="meta">{ic("clock")}{o["drive"]}</span></a>' for o in CITIES if o["slug"] != c["slug"])
    body = (page_hero(f'city-{c["slug"][:-3]}', f'Service area  ·  {c["name"]}, Ohio', cp["h1"], cp["lede"],
                      [("Home", "index.html"), ("Service Areas", "service-areas.html"), (c["name"], "")], cp["img_alt"], even=True)
            + f'''<section class="section paper" aria-labelledby="intro-h">
<div class="wrap split" style="gap:56px">
<div style="display:grid;gap:20px;align-content:start"><span class="eyebrow">Working in {c["name"]}</span><h2 class="h-lg" id="intro-h">{cp["intro_h"]}</h2>
{"".join(f'<p class="lede" style="font-size:17px">{p}</p>' for p in cp["intro"])}</div>
{glance}
</div>
</section>
<section class="section white" aria-labelledby="hood-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">Neighborhoods</span><h2 class="h-lg" id="hood-h">Where we work in {c["name"]}.</h2></div><p>{cp["hoods_lead"]}</p></div>
<div class="cells">{hoods}</div>
<div class="bar"><div><b>Don't see your neighborhood?</b><span class="small">We cover all of {c["name"]}. Call and tell us the street.</span></div><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}Call now</a></div>
</div>
</section>
<section class="section paper" aria-labelledby="jobs-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">What we see here</span><h2 class="h-lg" id="jobs-h">The jobs {c["name"]} homes call us for most.</h2></div></div>
<div class="cells" style="background:var(--white)">{jobs}</div>
</div>
</section>
<section class="section paper" style="padding-top:0" aria-labelledby="trades-h">
<div class="wrap">
<div class="section-head"><div><h2 class="h-md" id="trades-h">All three trades, in {c["name"]}.</h2></div><p>Permits, when a job needs one, are filed by us with the city. We schedule the inspection and meet the inspector.</p></div>
<div class="cells">{trades}</div>
</div>
</section>
''' + proj_html + reviews_band([cp["review"]] + [r for r in REVIEWS if r[2] != c["name"]][:2], title=f'What {c["name"]} neighbors say.')
            + faq_block(f'{c["name"]} questions, answered.', cp["faq"], f'Written around what people in {c["name"]} search for before they call.')
            + f'''<section class="section white" style="padding-top:0" aria-labelledby="near-h">
<div class="wrap" style="padding-top:var(--section)">
<div class="section-head"><div><h2 class="h-md" id="near-h">Nearby service areas</h2></div><p>Also near {c["name"]}: {cp["also"]}.</p></div>
<div class="cells">{nearby}</div>
</div>
</section>
''' + booking(title=f'Book a visit in <em class="accent">{c["name"]}.</em>'))
    lb = business_schema()
    lb["areaServed"] = {"@type": "City", "name": f'{c["name"]}, Ohio'}
    schemas = [lb, faq_schema(cp["faq"]), crumbs_schema([("Home", ""), ("Service Areas", "service-areas.html"), (c["name"], f'{c["slug"]}.html')])]
    write(f'{c["slug"]}.html', page(f'{c["slug"]}.html', cp["title"], cp["desc"], schemas, "areas", body, og_img="og.jpg"))


# ====================================================================== PROJECTS
def build_projects_hub():
    body = (page_hero("proj-heatpump", "Projects", 'Every job gets <em class="accent">a write up.</em>',
                      "The problem we found, what we did, and what it took. Each page is named by the job and the town, so a neighbor with the same problem can find it.",
                      [("Home", "index.html"), ("Projects", "")], "A new heat pump on a concrete pad beside a brick ranch home", btns=False)
            + f'''<section class="section paper" aria-label="Project write ups">
<div class="wrap" style="display:grid;gap:64px">
{proj_card(PROJECTS[0], feature=True)}
<div class="grid cols-2 gap-32">{proj_card(PROJECTS[1])}{proj_card(PROJECTS[2])}</div>
</div>
</section>
''' + stats_block() + booking(title='Have a job like <em class="accent">these?</em>'))
    schemas = [business_schema(), crumbs_schema([("Home", ""), ("Projects", "projects.html")]),
               {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f'{BASE}/{p["slug"]}.html', "name": strip(p["title"])} for i, p in enumerate(PROJECTS)]}]
    write("projects.html", page("projects.html", "Projects | Keelhouse Home Services, Columbus OH",
                                "Write ups of recent plumbing, heating and electrical jobs in Dublin, Westerville and Grove City, Ohio.", schemas, "projects", body))


def build_project(p):
    pp = PROJECT_PAGES[p["slug"]]
    meta = "".join(f'<div><small>{a}</small><span>{b}</span></div>' for a, b in pp["meta"])
    sections = "".join(f'<h2>{h}</h2>' + "".join(f"<p>{t}</p>" for t in paras) for h, paras in pp["sections"])
    others = [o for o in PROJECTS if o["slug"] != p["slug"]]
    svc_slug = {"Electrical": "electrical", "Plumbing": "plumbing", "Heating &amp; Cooling": "heating-cooling"}[p["trade"]]
    body = (page_hero(p["img"], f'{p["trade"]}  ·  {p["city"]}, Ohio', p["title"], pp["summary"],
                      [("Home", "index.html"), ("Projects", "projects.html"), (p["city"], "")], pp["img_alt"], even=True, btns=False)
            + f'''<section class="section paper">
<div class="wrap" style="display:grid;gap:56px">
<div class="meta-strip">{meta}</div>
<div class="faq-layout">
<div><span class="eyebrow">The job</span><p class="small">{pp["note"]}</p>
<a class="text-link" href="{svc_slug}.html">{p["trade"]} services{ic("arrow")}</a>
<a class="text-link" href="{p["city_slug"]}.html">Working in {p["city"]}{ic("arrow")}</a></div>
<article class="prose">{sections}</article>
</div>
<figure class="figure"><img src="img/{p["img"]}.webp" alt="{pp["img_alt"]}" loading="lazy" width="1800" height="1338"><figcaption>{pp["caption"]}</figcaption></figure>
</div>
</section>
<section class="section white" aria-labelledby="more-h">
<div class="wrap">
<div class="section-head"><div><span class="eyebrow">More from the job file</span><h2 class="h-md" id="more-h">Other recent projects</h2></div><a class="btn btn-outline" href="projects.html">All projects</a></div>
<div class="grid cols-2 gap-32">{"".join(proj_card(o) for o in others)}</div>
</div>
</section>
''' + booking(title=f'Need the same in <em class="accent">{p["city"]}?</em>', preset=pp["preset"]))
    art = {"@context": "https://schema.org", "@type": "Article", "headline": strip(p["title"]), "image": f'{BASE}/img/{p["img"]}.webp',
           "author": {"@id": f"{BASE}/#business"}, "publisher": {"@id": f"{BASE}/#business"}, "about": strip(p["trade"]),
           "contentLocation": {"@type": "Place", "name": f'{p["city"]}, Ohio'}, "datePublished": pp["date"]}
    schemas = [art, crumbs_schema([("Home", ""), ("Projects", "projects.html"), (strip(p["title"]), f'{p["slug"]}.html')])]
    write(f'{p["slug"]}.html', page(f'{p["slug"]}.html', f'{strip(p["title"])} | Keelhouse Projects', pp["desc"], schemas, "projects", body))


# ====================================================================== HOW WE WORK
def build_how():
    steps = [
        ("how-runner", "Phase one", "We protect the house first.", ["Shoe covers on at the door, a runner down from the entry to the work area, and drop cloths under anything we open. You shouldn't be able to tell we were there, apart from the thing that works now."]),
        ("svc-hvac", "Phase two", "We find the cause before we quote.", ["Every visit starts with a diagnosis. The tech tests, measures and shows you what failed and why, so the price you approve is for the real problem."]),
        ("proj-panel", "Phase three", "You approve a written price.", ["You get the price in writing on the tech's tablet before work starts. If a job grows once a wall is open, we stop, show you, and re-quote. No surprise line items."]),
        ("how-tablet", "Phase four", "Photos, notes and a file for your house.", ["When we're done, you get photos of the finished work and a short summary by text. It goes into your home's file, so the next tech starts with the history of every visit."]),
    ]
    rows = "".join(f'''<div class="alt-row{" flip" if i % 2 else ""} {"white" if i % 2 else "paper"}">
<div class="alt-media"><img src="img/{img}.webp" alt="" loading="lazy"></div>
<div class="alt-body"><div class="num">0{i+1}</div><span class="eyebrow">{eb}</span><h2 class="h-lg">{h}</h2>{"".join(f'<p class="lede" style="font-size:17px">{t}</p>' for t in ps)}</div>
</div>''' for i, (img, eb, h, ps) in enumerate(steps))
    standards = ["Licensed master plumber, master electrician and EPA 608 certified HVAC techs", "Background checked, drug tested and employed by us, never subcontracted", "Two hour arrival windows by text, with a heads up twenty minutes out",
                 "Written price before any work starts", "Shoe covers, floor runners and cleanup on every job", "One year labor warranty on repairs, longer on installs"]
    crew = f'''<section id="crew" class="split paper" aria-labelledby="crew-h">
<div class="split-media"><img src="img/founder.webp" alt="{FOUNDER}, founder of Keelhouse" loading="lazy" style="object-position:center 25%"></div>
<div class="split-body"><span class="eyebrow">The crew</span><h2 class="h-lg" id="crew-h">Started by a plumber who got tired of <em>handing jobs off.</em></h2>
<p class="lede" style="font-size:17px">{FOUNDER} started Keelhouse in {YEAR_FOUNDED} after years of finishing his half of a job and telling the homeowner to call someone else for the rest. Today the crew covers all three trades, and every tech is cross trained to spot what the others would.</p>
<p class="lede" style="font-size:17px">The name comes from the keel of a boat: the part nobody sees that keeps everything steady. That's the work we do inside the walls.</p>
<div><a class="btn btn-ink" href="#book">Book a visit</a></div></div>
</section>
'''
    body = (page_hero("how-runner", "How we work", 'Respect for the house, <em class="accent">start to finish.</em>',
                      "Four things happen on every Keelhouse visit, whether it's a dripping faucet or a whole new heating system.",
                      [("Home", "index.html"), ("How We Work", "")], "A Keelhouse technician laying a protective runner in a home's entryway", even=True)
            + rows
            + f'''<section class="section dark grid-bg" aria-labelledby="std-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Our standards</span><h2 class="h-lg" id="std-h">What you can hold us to.</h2></div></div>
<ul class="checks">{"".join(f"<li>{ic('check')}<span>{t}</span></li>" for t in standards)}</ul></div></section>
''' + crew + stats_block() + faq_block("Working with us.", HOW_FAQ, "The practical questions people ask before booking.") + booking())
    schemas = [business_schema(), faq_schema(HOW_FAQ), crumbs_schema([("Home", ""), ("How We Work", "how-we-work.html")])]
    write("how-we-work.html", page("how-we-work.html", "How We Work | Keelhouse Home Services",
                                   "How a Keelhouse visit runs: we protect the house, diagnose first, put the price in writing, and document every job with photos.",
                                   schemas, "how", body))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Building Keelhouse demo:")
    build_home()
    build_services_hub()
    for s in SERVICES:
        build_service(s)
    build_areas_hub()
    for c in CITIES:
        build_city(c)
    build_projects_hub()
    for p in PROJECTS:
        build_project(p)
    build_how()
