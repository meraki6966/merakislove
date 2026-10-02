"""Build the Saltbrush Pool Care demo into public/demos/saltbrush/.

Run from the repo root:  python3 scripts/demos/saltbrush/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
The design is "The Report": the home page is a visit report under a moving
pool, and every other page is set like the paperwork that goes with it.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sb import *  # noqa: E402,F403
from content import *  # noqa: E402,F403

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "saltbrush")
# The home page is also served at the clean URL /demos/saltbrush (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href, src and poster is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/saltbrush/")
OUT = os.environ.get("OUT", OUT)
PROBLEMS = []


def absolutize(html):
    if not PREFIX:
        return html

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|tel:|mailto:|#|/|data:)", url):
            return m.group(0)
        if url.startswith("?"):
            return m.group(0)
        if url == "index.html" or url.startswith("index.html?") or url.startswith("index.html#"):
            return f'{attr}="{PREFIX.rstrip("/")}{url[len("index.html"):]}"'
        return f'{attr}="{PREFIX}{url}"'
    return re.sub(r'\b(href|src|poster)="([^"]+)"', fix, html)


def write(name, html):
    # Guard the limits a scanner checks, so a long title never ships unnoticed.
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1).replace("&#x27;", "'")
    if len(title) > 60 or "&" in title:
        PROBLEMS.append(f"{name}: title is {len(title)} chars or has an ampersand: {title}")
    if not 120 <= len(desc) <= 160:
        PROBLEMS.append(f"{name}: description is {len(desc)} chars")
    if html.count("<h1") != 1:
        PROBLEMS.append(f"{name}: {html.count('<h1')} h1 elements")
    if 'alt=""' in html:
        PROBLEMS.append(f"{name}: empty alt text")
    html = absolutize(html)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    words = len(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S).split())
    print(f"  {name:28s} {len(html)//1024:>3} KB  {words:>5} words")


QUOTE_BTN = '<a class="btn" href="#quote">Get a written quote</a>'
CALL_BTN = f'<a class="call" href="tel:{TEL}">or call {PHONE}</a>'
AREA_BY = {a["slug"]: a for a in AREAS}
ROUTE = [("Monday", "ahwatukee"), ("Tuesday", "arcadia"), ("Wednesday", "tempe"), ("Thursday", "ahwatukee"), ("Friday", "arcadia")]
PRICES = [("weekly-pool-service.html", "Weekly pool service", "A full visit every week of the year, with all balancing chemicals.", "$155", "a month"),
          ("weekly-pool-service.html", "Chemicals only", "We test and balance every week. You handle the cleaning.", "$95", "a month"),
          ("green-pool-cleanup.html", "Green pool cleanup", "From green to swimmable, usually in three to five days.", "$295", "and up"),
          ("filter-cleaning.html", "Filter cleaning", "Taken apart, cleaned and inspected, with photos of what we found.", "$95", "per cleaning"),
          ("equipment-repair.html", "Repair diagnosis", "We find the cause and write down the price. Credited to the repair.", "$89", "per visit")]
CODES = [("Collected by phone", "We never ask for a gate or alarm code by text, email or web form."),
         ("Stored encrypted", "Codes sit in one system with a login for each person, and access ends the day someone leaves."),
         ("Shown on route day only", "Your technician sees the code on the morning of your visit and at no other time."),
         ("Every view is logged", "The system records who looked at a code and when.")]
TIMES = ["7:14", "7:19", "7:23", "7:31", "7:36", "7:42"]
SCENARIOS = {
    "normal": {"label": "A normal week", "status": "Balanced", "arrived": "7:14 AM", "left": "7:42 AM", "gate": "Latched at 7:42",
               "v": NORMAL, "img": "brushing", "alt": "A technician brushing the tile line of a clear blue pool",
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


# ---------------------------------------------------------------- blocks
def head_block(title, small="", hid=""):
    h = f' id="{hid}"' if hid else ""
    sm = f"<p>{small}</p>" if small else ""
    return f'<div class="sec-hd"><h2{h}>{title}</h2>{sm}</div>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def table(head, rows, caption, cls="tbl"):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = ""
    for r in rows:
        cells = f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:])
        body += f"<tr>{cells}</tr>"
    return f'<div class="tw"><table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def steps(items):
    """A numbered sequence, for things that happen in order."""
    return '<ol class="steps">' + "".join(f"<li><div><h3>{t}</h3><p>{d}</p></div></li>" for t, d in items) + "</ol>"


def rows(items):
    """Titled rows with no order implied."""
    return '<ul class="rows">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items) + "</ul>"


def price_table(exclude=None):
    body = "".join(f'<tr><th scope="row"><a href="{h}">{n}</a></th><td>{d}</td><td class="amt"><b>{p}</b> {u}</td></tr>'
                   for h, n, d, p, u in PRICES if h != exclude or n == "Chemicals only")
    return ('<div class="tw"><table class="stmt"><caption>Saltbrush sample prices</caption><thead><tr><th scope="col">Service</th>'
            f'<th scope="col">What it covers</th><th scope="col" class="amt">Price</th></tr></thead><tbody>{body}</tbody></table></div>')


def services_section(bg="", exclude=None, title="What does Saltbrush do?"):
    return f'''<section class="sec {bg}" aria-labelledby="svc-h"><div class="w">
{head_block(title, 'Every service has its price on the page. <a href="pricing.html">See the full price list</a>.', "svc-h")}
{price_table(f"{exclude}.html" if exclude else None)}
</div></section>
'''


def route_table(exclude=None):
    body = ""
    for day, slug in ROUTE:
        if slug == exclude:
            continue
        a = AREA_BY[slug]
        body += (f'<tr><th scope="row">{day}</th><td><a href="{slug}.html"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1600" height="1200">{a["name"]}</a></td>'
                 f'<td>{a["zip"]}</td><td>{a["line"]}</td></tr>')
    return ('<div class="tw"><table class="route"><caption>Saltbrush route days by neighborhood</caption><thead><tr><th scope="col">Day</th>'
            f'<th scope="col">Neighborhood</th><th scope="col">ZIP</th><th scope="col">What we see there</th></tr></thead><tbody>{body}</tbody></table></div>')


def areas_section(bg="", exclude=None, title="Which neighborhoods are on our routes?"):
    return f'''<section class="sec {bg}" aria-labelledby="area-h"><div class="w">
{head_block(title, "Each neighborhood has its own route days. Tight routes mean more time at each pool and less time on the 51.", "area-h")}
{route_table(exclude)}
</div></section>
'''


def reviews_section(bg="white"):
    return f'''<section class="sec {bg}" aria-labelledby="rev-h"><div class="w">
{head_block("What do customers say?", "Sample reviews written for this demo.", "rev-h")}
<div class="reviews">{"".join(review_card(*r) for r in REVIEWS)}</div>
</div></section>
'''


def season_table():
    body = "".join(f'<tr><th scope="row">{s}</th><td>{m}</td><td>{c}</td><td>{d}</td></tr>' for s, m, c, d in SEASONS)
    return ('<div class="tw"><table class="seasons"><caption>The five pool seasons in Phoenix and what weekly service does in each</caption>'
            '<thead><tr><th scope="col">Season</th><th scope="col">Months</th><th scope="col">What changes in the water</th><th scope="col">What we do about it</th></tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def split(title, paras, img, alt, hid, extra=""):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<div class="log-g">
<div class="log-copy"><h2 id="{hid}">{title}</h2>{body}{extra}</div>
<figure class="fig"><img src="img/{img}.webp" alt="{alt}" loading="lazy" width="1600" height="1200"></figure>
</div>'''


# ---------------------------------------------------------------- pages
def build_home():
    s0 = SCENARIOS["normal"]
    tabs = ""
    for k, s in SCENARIOS.items():
        sel = "true" if k == "normal" else "false"
        tabs += f'<button type="button" role="tab" aria-selected="{sel}" data-s="{k}">{s["label"]}</button>'
    did = "".join(f"<li>{d}</li>" for d in s0["did"])
    log = "".join(f'<li><time>{t} AM</time><div><h3>{h}</h3><p>{p}</p></div></li>' for t, (h, p) in zip(TIMES, VISIT_STEPS))
    months = "".join(f'<span><abbr title="{full}">{full[:3]}</abbr></span>' for full in
                     ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    worries = "".join(f'<div><h3>“{q}”</h3><p>{a}</p></div>' for q, a in WORRIES)
    codes = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in CODES)
    body = f'''<section class="hero">
<div class="hero-media"><video autoplay muted loop playsinline preload="metadata" poster="img/hero-wide.webp" aria-hidden="true" tabindex="-1" width="1600" height="900"><source src="img/hero-loop.webm" type="video/webm"><source src="img/hero-loop.mp4" type="video/mp4"></video></div>
<div class="w hero-in">
<div class="hero-copy">
<h1>We service your pool every week, and send you the proof.</h1>
<p class="lede">Saltbrush is a pool service and repair company for central Phoenix, Arcadia, Ahwatukee and Tempe. One technician looks after your pool. Before the truck leaves your street, a report like the one below is on your phone.</p>
<div class="acts">{QUOTE_BTN}{CALL_BTN}</div>
{season_note()}
</div>
<button class="motion" type="button" aria-pressed="false" data-motion>Pause video</button>
</div>
</section>
<section class="report"><div class="w">
<article class="sheet" aria-labelledby="rep-h">
<header class="sheet-hd"><div><h2 id="rep-h">Visit report</h2><p>Sample pool, Arcadia 85018</p></div><p class="status" data-f="status">{s0["status"]}</p></header>
<div class="tabs" role="tablist" aria-label="Choose a sample week">{tabs}</div>
<dl class="meta"><div><dt>Arrived</dt><dd data-f="arrived">{s0["arrived"]}</dd></div><div><dt>Left</dt><dd data-f="left">{s0["left"]}</dd></div><div><dt>Technician</dt><dd>Tamsin O.</dd></div><div><dt>Gate</dt><dd data-f="gate">{s0["gate"]}</dd></div></dl>
<div class="sheet-body">
<div class="gauges">{gauges_html(s0["v"])}</div>
<div class="did"><img data-f="img" src="img/{s0["img"]}.webp" alt="{s0["alt"]}" width="1600" height="1200"><div><h3>What we did</h3><ul data-f="did">{did}</ul></div></div>
</div>
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
{head_block("How much does pool service cost?", "Every price we charge is on this site. Weekly service is one flat monthly number, the same in July as in January.", "cost-h")}
{price_table()}
<p class="fine">Repairs and cleanups get a written price before any work starts, and you approve it from your phone. See the <a href="pricing.html">full price list</a> and <a href="services.html">all services</a>.</p>
</div></section>

<section class="sec" aria-labelledby="year-h"><div class="w">
{head_block("What does a Phoenix year do to a pool?", "The desert has five pool seasons, and each one asks for something different. The marker shows today.", "year-h")}
<div class="year" aria-hidden="true"><div class="months">{months}</div>
<div class="bands"><span class="b winter" style="grid-column:1/3">Winter</span><span class="b spring" style="grid-column:3/6">Spring</span><span class="b summer" style="grid-column:6/10">Summer</span><span class="b fall" style="grid-column:10/12">Fall</span><span class="b winter" style="grid-column:12/13">Winter</span></div>
<div class="mon"><span style="left:45.6%;width:29.4%">Monsoon, June 15 to September 30</span></div>
<span class="today" data-today></span></div>
{season_table()}
<p class="fine">Monsoon dates are the National Weather Service definition for Arizona. Read the guide to <a href="monsoon-pool-care.html">monsoon and dust storm pool care</a>.</p>
</div></section>
''' + areas_section("white") + f'''<section class="sec" aria-labelledby="worry-h"><div class="w">
{head_block("What worries pool owners most?", "Three things we hear on almost every first call, and what we do about each.", "worry-h")}
<div class="worries">{worries}</div>
</div></section>

<section class="sec deep" aria-labelledby="code-h"><div class="w code-g">
<div><h2 id="code-h">How is my gate code protected?</h2><p>A pool company knows when you are away and how to open your gate. We treat your code like a house key.</p><p><a href="service-reports.html">How reports and codes are protected</a></p>
<p class="kid">Small children at home? Arizona law sets rules for pool fences and gates, and we check your gate on every visit. <a href="pool-safety.html">Read the pool barrier guide</a>.</p></div>
<ul class="codes">{codes}</ul>
</div></section>
''' + reviews_section() + faq_block("Pool service in Phoenix, answered", HOME_FAQ, f'Still have a question? Call <a href="tel:{TEL}">{PHONE}</a> and a person answers. You can also read <a href="about.html">about the team</a>.') + contact()
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    extra = f'<script type="application/json" id="scn">{scenario_json()}</script>\n'
    write("index.html", page("index.html", "Pool Service in Phoenix, AZ | Saltbrush Pool Care",
                             "Weekly pool service and repair in Phoenix, Arcadia, Ahwatukee and Tempe. One technician, flat monthly pricing and a water report after every visit.",
                             schemas, "", body, extra))


def build_services_hub():
    cmp_rows = [(f'<a href="{s["slug"]}.html">{s["name"]}</a>', s["short"], f'{s["from"]} {s["unit"]}') for s in SERVICES]
    body = (page_hero("", "Pool services for Phoenix homes",
                      "Weekly care, cleanups, repairs and filter cleaning for residential pools. Each service has its own page with what is included and what it costs.",
                      [("Home", "index.html"), ("Services", "")], "truck",
                      "A white service pickup with pool poles, a leaf net and a chemical caddy on a palm lined Phoenix street",
                      ["Residential pools only", "Written prices before work", "Arizona ROC R-6 licensed"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="sec white" aria-labelledby="cmp-h"><div class="w">
{head_block("Which service do you need?", "Starting prices for a standard residential pool.", "cmp-h")}
{table(("Service", "What it is", "Starting price"), cmp_rows, "Saltbrush services compared", "tbl last-strong")}
<p class="fine">Not sure which one fits? <a href="index.html#quote">Send five details</a> and we will tell you. Seasonal help is covered in the <a href="monsoon-pool-care.html">monsoon guide</a>, and every price is on the <a href="pricing.html">pricing page</a>.</p>
</div></section>
''' + areas_section("") + faq_block("Choosing a service, answered", SERVICES_FAQ, "What new customers ask before they pick.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")]),
               {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f'{BASE}/{s["slug"]}.html'} for i, s in enumerate(SERVICES)]}]
    write("services.html", page("services.html", "Pool Services in Phoenix, AZ | Saltbrush Pool Care",
                                "Pool services for Phoenix homes: weekly service, green pool cleanup, equipment repair and filter cleaning, each with its price on the page.",
                                schemas, "services", body))


def build_service(slug):
    s, c = SVC[slug], SERVICE_PAGES[slug]
    body = (page_hero("", strip(c["h1"]), c["lede"], [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")],
                      s["img"], s["alt"], c["points"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="sec" aria-labelledby="inc-h"><div class="w two-col">
<div><h2 id="inc-h">{strip(c["included_title"])}</h2>{checks(c["included"])}</div>
<div class="prose"><h2>{strip(c["body_title"])}</h2>{"".join(f"<p>{p}</p>" for p in c["body"])}</div>
</div></section>
<section class="sec white" aria-labelledby="rows-h"><div class="w">
{head_block("What does it cost?", "Sample prices for this demo. A live site would show your own.", "rows-h")}
{table(c["rows_head"], c["rows"], c["rows_title"], "tbl last-strong")}
<p class="fine">Every job gets a written price before work starts. See the <a href="pricing.html">full price list</a> or how the <a href="service-reports.html">weekly report</a> works.</p>
</div></section>
''' + services_section("", exclude=slug, title="What else does Saltbrush do?")
            + faq_block(f'{s["name"]}, answered', c["faq"], "The questions we hear most about this service.", "white") + contact(need=s["need"]))
    schemas = [org_schema(), business_schema(), service_schema(s["name"], c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (s["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "services", body))


def build_monsoon():
    body = (page_hero("", "What should you do with a pool when a haboob is coming?",
                      "Arizona's monsoon runs from June 15 to September 30. Here is what to do before a dust storm, how to clean up after one, and what Saltbrush does for weekly customers.",
                      [("Home", "index.html"), ("Monsoon care", "")], "haboob",
                      "A towering wall of dust rolling toward a Phoenix neighborhood at dusk, with a calm backyard pool in the foreground",
                      ["Season dates: June 15 to September 30", "Cleanup visit on your next route day", "Storm rate on filter cleanings"], QUOTE_BTN)
            + f'''<section class="sec" aria-labelledby="before-h"><div class="w two-col">
<div><h2 id="before-h">What should I do before a dust storm?</h2>{checks(STORM_BEFORE)}{season_note()}</div>
<div class="prose"><h2>What does a dust storm do to pool water?</h2>
<p>A haboob drops fine desert silt into the pool, and that silt carries phosphates, which are food for algae. The dust also loads the filter, so the pump moves less water at the moment the pool needs it most.</p>
<p>Rain that follows is slightly acidic and dilutes the water, so pH, alkalinity and chlorine can all fall overnight. A pool that is left alone after a big storm often turns cloudy within a day and green within a week.</p>
<p>The fix is simple, and the order matters. Debris comes out first, then the dust, then the filter is cleaned, and only then is the water tested and corrected.</p></div>
</div></section>
<section class="sec white" aria-labelledby="after-h"><div class="w">
{split("How do you clean a pool after a haboob?",
       ["These are the eight steps our technicians follow on a storm cleanup visit. You can do the first three yourself the morning after, and they make the biggest difference.",
        "If the water is still brown after a full day of filtering, the filter needs cleaning again. That is normal after a large storm."],
       "storm", "A leaf rake on a long pole skimming palm fronds and dust from a pool the morning after a storm", "after-h")}
{steps(STORM_AFTER)}
</div></section>
<section class="sec" aria-labelledby="tbl-h"><div class="w">
{head_block("What is wrong with my pool after the storm?", "Match what you see to the likely cause.", "tbl-h")}
{table(("What you see", "What is happening", "What fixes it"), STORM_TABLE, "Common pool problems after a monsoon storm and how to fix them")}
<p class="fine">Storm cleanup visits are $85 for weekly customers, and an after storm <a href="filter-cleaning.html">filter cleaning</a> is $75. If the pool has already turned, see <a href="green-pool-cleanup.html">green pool cleanup</a>.</p>
</div></section>
''' + faq_block("Monsoon pool care, answered", MONSOON_FAQ, "Season dates are from the National Weather Service.", "white") + contact())
    desc = "What to do with a Phoenix pool before and after a monsoon dust storm: season dates, eight cleanup steps, a troubleshooting table and storm visit prices."
    schemas = [org_schema(), business_schema(), article_schema("Monsoon and dust storm pool care in Phoenix", desc, "monsoon-pool-care.html"),
               faq_schema(MONSOON_FAQ), crumbs_schema([("Home", ""), ("Monsoon care", "monsoon-pool-care.html")])]
    write("monsoon-pool-care.html", page("monsoon-pool-care.html", "Monsoon Pool Care in Phoenix | Saltbrush Pool Care", desc, schemas, "monsoon", body))


def build_safety():
    abc = [("Adult supervision", "An adult watching the water with no phone in hand is the first layer, every time a child is near the pool."),
           ("Barriers", "A fence and a self latching gate slow a child down when supervision slips. They only work if the gate is closed."),
           ("Classes", "Swim lessons for children and CPR training for adults are the third layer that Valley fire departments teach.")]
    body = (page_hero("", "What does Arizona law require around a backyard pool?",
                      "A plain summary of the state pool barrier rule, A.R.S. 36-1681, for homes where a child under six lives, with the numbers in one table.",
                      [("Home", "index.html"), ("Pool safety", "")], "fence",
                      "A black wrought iron pool fence with a closed self latching gate around a backyard pool",
                      ["State rule: A.R.S. 36-1681", "5 foot barrier, 54 inch latch", "We check your gate on every visit"])
            + f'''<section class="sec white" aria-labelledby="law-h"><div class="w">
{head_block("What are the pool barrier requirements in Arizona?", "From the Arizona Department of Health Services residential pool safety notice.", "law-h")}
{table(("Requirement", "What the state rule says"), BARRIER_TABLE, "Arizona residential pool barrier requirements under A.R.S. 36-1681")}
<p class="fine">This is general information, checked in October 2026, and it is not legal advice. Many Valley cities have their own pool barrier codes that add to the state rule. Your city's building department has the final word for your address.</p>
</div></section>
<section class="sec" aria-labelledby="abc-h"><div class="w">
{head_block("What keeps children safe around water?", "No single layer is enough on its own.", "abc-h")}
{rows(abc)}
</div></section>
<section class="sec white" aria-labelledby="gate-h"><div class="w two-col">
<div class="prose"><h2 id="gate-h">How does Saltbrush help with pool safety?</h2>
<p>We are in your yard every week, so we see the gate more often than anyone except you. On every visit the technician pulls the gate shut behind them and checks that it closed and latched without help.</p>
<p>If the closer is weak, the latch is sticking or something has been propped against the fence that a child could climb, it goes on your report the same day with a photo.</p>
<p>We do not install or repair pool barriers. That work belongs to a fence contractor or a pool builder, and we will tell you which one to call.</p></div>
<div><h2>What do we check at the gate?</h2>{checks(["Gate swings closed without a push", "Latch catches on its own", "Latch is out of a small child's reach", "Nothing climbable is stacked against the fence", "Pool toys are out of the water when we leave", "Any problem is on your report with a photo"])}</div>
</div></section>
''' + faq_block("Arizona pool fence rules, answered", SAFETY_FAQ, 'Short answers for homeowners. See also <a href="service-reports.html">the weekly report</a>.') + contact())
    desc = "Arizona pool barrier law A.R.S. 36-1681 in plain words: who it applies to, fence height, gate and latch rules, and the gate check on every Saltbrush visit."
    schemas = [org_schema(), business_schema(), article_schema("Arizona pool barrier requirements for homeowners", desc, "pool-safety.html"),
               faq_schema(SAFETY_FAQ), crumbs_schema([("Home", ""), ("Pool safety", "pool-safety.html")])]
    write("pool-safety.html", page("pool-safety.html", "Arizona Pool Fence Law Explained | Saltbrush Pool Care", desc, schemas, "safety", body))


def build_pricing():
    groups = ""
    for slug, bg in zip(SVC, ["white", "", "white", ""]):
        c = SERVICE_PAGES[slug]
        groups += (f'<section class="sec {bg}" aria-labelledby="p-{slug}"><div class="w">'
                   + head_block(c["rows_title"], f'<a href="{slug}.html">How {SVC[slug]["name"].lower()} works</a>', f"p-{slug}")
                   + table(c["rows_head"], c["rows"], c["rows_title"], "tbl last-strong") + "</div></section>\n")
    extras = [("Storm cleanup visit", "Weekly customers, after a dust storm", "$85"), ("Phosphate treatment", "After a storm or an algae bloom", "$45"),
              ("Tile line cleaning", "Scale removed at the waterline", "From $220"), ("One time vacation service", "A single full visit", "$75")]
    body = (page_hero("", "Every price, on one page",
                      "Sample prices for a fictional company, laid out the way a pool owner wants to read them: what it is, what it covers and what it costs.",
                      [("Home", "index.html"), ("Pricing", "")], None, "", ["Flat monthly price all year", "Chemicals included in weekly service", "Written price before any repair"], QUOTE_BTN)
            + groups + f'''<section class="sec white" aria-labelledby="p-extra"><div class="w">
{head_block("Storm visits and extras", 'See the <a href="monsoon-pool-care.html">monsoon guide</a> for when these apply.', "p-extra")}
{table(("Service", "When it applies", "Price"), extras, "Storm visits and extra services", "tbl last-strong")}
<p class="fine">Prices are samples written for this demo site. Saltbrush is a fictional company.</p>
</div></section>
''' + faq_block("Pool service pricing, answered", PRICING_FAQ, "How billing works.") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(PRICING_FAQ), crumbs_schema([("Home", ""), ("Pricing", "pricing.html")]),
               {"@context": "https://schema.org", "@type": "OfferCatalog", "name": "Saltbrush Pool Care sample prices",
                "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}, "description": f'{s["from"]} {s["unit"]}'} for s in SERVICES]}]
    write("pricing.html", page("pricing.html", "Pool Service Prices in Phoenix | Saltbrush Pool Care",
                               "Pool service prices in Phoenix on one page: weekly service at $155 a month, green pool cleanup, filter cleaning, repairs and storm visits.",
                               schemas, "pricing", body))


def build_reports():
    body = (page_hero("", "A report after every visit, and your gate code kept safe",
                      "What the report shows, why it exists, and how Saltbrush protects the two most sensitive things a pool company holds: your gate code and your schedule.",
                      [("Home", "index.html"), ("Your weekly report", "")], None, "",
                      ["Sent by text and email within minutes", "Six readings beside their targets", "Codes stored encrypted, views logged"], QUOTE_BTN)
            + f'''<section class="sec" aria-labelledby="rep-h"><div class="w two-col">
<div><h2 id="rep-h">What is on the weekly report?</h2>
<p>The report answers the question every pool owner has when they come home: did someone come, and what did they do? It is short enough to read at a stoplight and complete enough to hand to the next owner of the house.</p>
{rows(REPORT_ITEMS)}</div>
{water_card("Visit report, Tuesday 7:42 AM", "Arrived 7:14 AM, left 7:42 AM. Added 1 quart of acid. Filter at 14 psi. Gate latched.")}
</div></section>
<section class="sec deep" aria-labelledby="sec-h"><div class="w">
{head_block("How are gate codes and reports protected?", "A pool company knows when you are away and how to open your gate. We treat that as the responsibility it is.", "sec-h")}
{rows(REPORT_SECURITY)}
</div></section>
<section class="sec white" aria-labelledby="why-h"><div class="w prose narrow">
<h2 id="why-h">Why does a pool company need to think about security?</h2>
<p>Most pool routes still run on a clipboard or a group text. Somewhere in that thread is a list of addresses, the day nobody is home, and the code that opens the side gate. If a phone is lost or a former employee keeps the thread, that list goes with them.</p>
<p>Saltbrush keeps codes in one system with a login for each person, and removes access the day someone leaves. Technicians see a code on the morning of your route day and at no other time. Every view is logged.</p>
<p>The same care applies to this website. It loads no trackers, sets no advertising cookies, and its forms ask only for what a quote needs. Read the <a href="privacy.html">privacy page</a> for the full list.</p>
</div></section>
''' + faq_block("Reports and privacy, answered", REPORT_FAQ, 'How the report and the portal work. Weekly service is described on <a href="weekly-pool-service.html">its own page</a>.') + contact())
    schemas = [org_schema(), business_schema(), faq_schema(REPORT_FAQ), crumbs_schema([("Home", ""), ("Your weekly report", "service-reports.html")])]
    write("service-reports.html", page("service-reports.html", "Weekly Pool Service Reports | Saltbrush Pool Care",
                                       "What the Saltbrush weekly pool report shows, and how gate codes, photos and schedules are protected with encryption, logging and two step login.",
                                       schemas, "", body))


def build_about():
    people = "".join(f'<div class="person"><span class="avatar" aria-hidden="true">{i}</span><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></div>' for i, n, r, b in PEOPLE)
    scope = [("Covered by our R-6 license", "Service and minor repair of residential pools and accessories: pumps, filters, salt systems, automation, valves and equipment plumbing."),
             ("Outside it", "Connections to a drinking water line, gas lines, gas chlorine systems, electrical work beyond the first disconnect, and full replacement of plaster, pebble or decks."),
             ("What we do then", "We tell you which licensed trade to call, what to ask for, and we coordinate our part of the job around theirs.")]
    body = (page_hero("", "A small pool company that shows its work",
                      "Saltbrush started in 2014 with one truck and forty pools in central Phoenix. It is still owner run, and every technician is an employee.",
                      [("Home", "index.html"), ("About", "")], "truck",
                      "A white service pickup with pool poles, a leaf net and a chemical caddy on a Phoenix street at sunrise",
                      ["Owner on a route every Friday", "Employees, never subcontractors", "Arizona ROC R-6 licensed"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="sec white" aria-labelledby="story-h"><div class="w prose narrow">
<h2 id="story-h">Why did Saltbrush start?</h2>
<p>Nico Velarde spent six summers on another company's routes, servicing more pools a day than anyone could do well. Customers rarely knew his name, and he rarely had time to brush. He left to build a company around two rules: fewer pools per route, and a report after every visit.</p>
<p>Those two rules still run the business. A technician has about half an hour at each pool. The report goes out before the truck leaves your street. Everything else, from the flat monthly price to the way gate codes are stored, follows from wanting customers to be able to check our work.</p>
<p>We stay inside a small part of the Valley on purpose. Tight routes through <a href="arcadia.html">Arcadia</a>, <a href="ahwatukee.html">Ahwatukee</a> and <a href="tempe.html">Tempe</a> mean less time on the freeway and more time with a brush in the water.</p>
</div></section>
<section class="sec" aria-labelledby="team-h"><div class="w">
{head_block("Who looks after your pool?", "Fictional people, written for this demo.", "team-h")}
<div class="people">{people}</div>
</div></section>
<section class="sec white" aria-labelledby="lic-h"><div class="w">
{head_block("What is Saltbrush licensed to do?", "The scope of Arizona's R-6 classification, in plain words.", "lic-h")}
{rows(scope)}
<p class="fine">Scope summarized from the Arizona Registrar of Contractors residential classification R-6, Swimming Pool Service and Repair. See <a href="equipment-repair.html">equipment repair</a> for what that looks like on a job.</p>
</div></section>
''' + reviews_section("") + faq_block("About Saltbrush, answered", ABOUT_FAQ, "A few things people ask before they hire us.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("About", "about.html")]),
               {"@context": "https://schema.org", "@type": "Person", "name": "Nico Velarde", "jobTitle": "Owner and lead technician", "worksFor": {"@id": f"{BASE}/#org"}}]
    write("about.html", page("about.html", "About Saltbrush Pool Care | Phoenix Pool Service",
                             "Saltbrush Pool Care is an owner run Phoenix pool service founded in 2014, with employee technicians, capped routes and an Arizona R-6 license.",
                             schemas, "about", body))


def build_area(slug):
    a, c = AREA_BY[slug], AREA_PAGES[slug]
    notes = table(("What we see here", "What we do about it"), c["notes"], f'Pool care notes for {a["name"]}')
    body = (page_hero("", strip(c["h1"]), c["lede"], [("Home", "index.html"), ("About", "about.html"), (a["name"], "")],
                      a["img"], a["alt"], c["points"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="sec" aria-labelledby="loc-h"><div class="w two-col">
<div class="prose"><h2 id="loc-h">{strip(c["body_title"])}</h2>{"".join(f"<p>{p}</p>" for p in c["body"])}</div>
<div><h2>What do we plan for here?</h2>{notes}{season_note()}</div>
</div></section>
''' + services_section("white", title=f'What do we do for pools in {a["name"]}?') + areas_section("", exclude=slug, title="Where else do we work?")
            + faq_block(f'{a["name"]} pool service, answered', c["faq"], "What neighbors here ask us.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(c["faq"]), crumbs_schema([("Home", ""), ("About", "about.html"), (a["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "about", body))


def build_privacy():
    body_html = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (page_hero("", "Your privacy at Saltbrush",
                      "What this website collects, how gate codes and photos are handled, and what we will never ask you for.",
                      [("Home", "index.html"), ("Privacy", "")])
            + f'''<section class="sec white"><div class="w prose narrow legal">{body_html}
<p class="fine">This is a demo site by Meraki is Love. Saltbrush is a fictional company, and nothing entered on this site is sent anywhere. Read more about <a href="service-reports.html">weekly reports</a>, <a href="services.html">our services</a> or <a href="about.html">the team</a>.</p>
</div></section>
''' + contact())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy | Saltbrush Pool Care",
                               "How Saltbrush Pool Care handles your information: what the website collects, how gate codes and photos are protected, and what we never ask for.",
                               schemas, "", body))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Building Saltbrush demo:")
    build_home()
    build_services_hub()
    for sv in SERVICES:
        build_service(sv["slug"])
    build_monsoon()
    build_safety()
    build_pricing()
    build_reports()
    build_about()
    for ar in AREAS:
        build_area(ar["slug"])
    build_privacy()
    if PROBLEMS:
        print("\nProblems:")
        for p in PROBLEMS:
            print("  " + p)
        sys.exit(1)
