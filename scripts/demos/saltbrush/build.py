"""Build the Saltbrush Pool Care demo into public/demos/saltbrush/.

Run from the repo root:  python3 scripts/demos/saltbrush/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sb import *  # noqa: E402,F403
from content import *  # noqa: E402,F403

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "saltbrush")
# The home page is also served at the clean URL /demos/saltbrush (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
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
    return re.sub(r'\b(href|src)="([^"]+)"', fix, html)


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


CHECK = ic("check")
ARROW = ic("arrow")
QUOTE_BTN = f'<a class="btn btn-clay" href="#contact">Get a written quote{ARROW}</a>'
CALL_BTN = f'<a class="btn btn-line" href="tel:{TEL}">{ic("phone")}{PHONE}</a>'


# ---------------------------------------------------------------- blocks
def head_block(tag, title, small="", hid=""):
    h = f' id="{hid}"' if hid else ""
    sm = f'<p class="small">{small}</p>' if small else "<span></span>"
    return f'<div class="section-head"><div><p class="tag">{tag}</p><h2 class="h-lg"{h}>{title}</h2></div>{sm}</div>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items) + "</ul>"


def table(head, rows, caption, cls="data"):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = "".join("<tr>" + "".join(f'<td data-label="{head[i]}">{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def steps(items, cls="steps"):
    return f'<ol class="{cls}">' + "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in items) + "</ol>"


def services_section(bg="", exclude=None, title='What does Saltbrush <span class="accent">do?</span>'):
    cards = "".join(
        f'<a class="svc reveal" href="{s["slug"]}.html"><img src="img/{s["img"]}.webp" alt="{s["alt"]}" loading="lazy" width="1600" height="1200">'
        f'<div class="svc-body"><h3>{s["name"]}</h3><p>{s["short"]}</p><p class="price"><b>{s["from"]}</b> {s["unit"]}</p><span class="more">See how it works{ARROW}</span></div></a>'
        for s in SERVICES if s["slug"] != exclude)
    return f'''<section class="section {bg}" aria-labelledby="svc-h"><div class="wrap">
{head_block("Services", title, 'Four services, each with its price on the page. <a href="pricing.html">See all prices</a>.', "svc-h")}
<div class="svc-grid">{cards}</div>
</div></section>
'''


def areas_section(bg="", exclude=None):
    cards = "".join(
        f'<a class="area reveal" href="{a["slug"]}.html"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1600" height="1200">'
        f'<div><h3>{a["name"]}</h3><p>{a["line"]}.</p><p class="meta">{a["day"]} · {a["zip"]}</p></div></a>'
        for a in AREAS if a["slug"] != exclude)
    return f'''<section class="section {bg}" aria-labelledby="area-h"><div class="wrap">
{head_block("Where we work", 'Which neighborhoods are <span class="accent">on our routes?</span>', "Tight routes mean more time at each pool and less time on the 51.", "area-h")}
<div class="area-grid">{cards}</div>
</div></section>
'''


def reviews_section(bg="white"):
    return f'''<section class="section {bg}" aria-labelledby="rev-h"><div class="wrap">
{head_block("Reviews", 'What do customers <span class="accent">say?</span>', "Sample reviews written for this demo.", "rev-h")}
<div class="review-grid">{"".join(review_card(*r) for r in REVIEWS)}</div>
</div></section>
'''


def season_status():
    return ('<p class="season" data-monsoon><span class="dot"></span><span class="txt">Monsoon season runs June 15 to September 30.</span> '
            '<a href="monsoon-pool-care.html">Storm care guide</a></p>')


def split(tag, title, paras, img, alt, hid, extra="", flip=False):
    body = "".join(f"<p>{p}</p>" for p in paras)
    return f'''<div class="split{" flip" if flip else ""}">
<div class="frame reveal"><img src="img/{img}.webp" alt="{alt}" loading="lazy" width="1600" height="1200"></div>
<div class="prose"><p class="tag">{tag}</p><h2 class="h-lg" id="{hid}">{title}</h2>{body}{extra}</div>
</div>'''


# ---------------------------------------------------------------- pages
def build_home():
    stats = [("2014", "Serving Phoenix pools since"), ("1", "Technician assigned to your pool"), ("6", "Readings on every weekly report"), ("R-6", "Arizona license for service and repair")]
    worries = "".join(f'<div class="worry reveal"><p class="q">“{q}”</p><p>{a}</p></div>' for q, a in WORRIES)
    season_rows = [(f"<b>{s}</b>", m, c, d) for s, m, c, d in SEASONS]
    price_rows = [("Weekly service", "$155 a month, chemicals included"), ("Green pool cleanup", "From $295"), ("Filter cleaning", "From $95"), ("Repair diagnosis", "$89, credited to the repair")]
    body = f'''<section class="hero"><div class="wrap hero-grid">
<div class="copy">
<p class="tag">Phoenix pool service since 2014</p>
<h1 class="h-xxl">Clear water every week, <span class="accent">through a Phoenix summer.</span></h1>
<p class="lede">Saltbrush is a pool service and repair company for central Phoenix, Arcadia, Ahwatukee and Tempe. One technician looks after your pool, and a report with six readings and a photo reaches your phone after every visit.</p>
<div class="btn-row">{QUOTE_BTN}{CALL_BTN}</div>
{season_status()}
</div>
<div class="hero-art"><img src="img/hero.webp" alt="A clear turquoise backyard pool behind a white stucco desert home, with a palo verde tree and a mountain in the distance" fetchpriority="high" width="1600" height="1200">
{water_card()}</div>
</div>{WAVE}</section>
<section class="strip" aria-label="Saltbrush at a glance"><div class="wrap stats">{"".join(f'<div><b>{n}</b><span>{t}</span></div>' for n, t in stats)}</div></section>
''' + services_section() + f'''<section class="section white" aria-labelledby="visit-h"><div class="wrap">
{split("The weekly visit", 'What happens on <span class="accent">a weekly visit?</span>',
       ["The visit follows the same six steps at every pool, every week. It takes 25 to 35 minutes, and nothing is skipped because the route is running late.",
        "Testing comes first because the readings decide everything else. We use a drop test kit at the pool, which is slower than a strip and far more accurate, and the numbers go straight into your report."],
       "testing", "A Saltbrush technician in a sun hat at the pool edge, holding a water test vial up to the light beside an open test kit", "visit-h",
       f'<p><a class="link" href="weekly-pool-service.html">Everything included in weekly service{ARROW}</a></p>')}
{steps(VISIT_STEPS)}
</div></section>
<section class="section tint" aria-labelledby="year-h"><div class="wrap">
{head_block("A Phoenix year", 'What does a Phoenix year <span class="accent">do to a pool?</span>', "The desert has five pool seasons, and each one asks for something different.", "year-h")}
{table(("Season", "Months", "What changes in the water", "What we do about it"), season_rows, "The five pool seasons in Phoenix and how weekly service changes with each")}
<p class="fine">Monsoon dates are the National Weather Service definition for Arizona. Read the full guide to <a href="monsoon-pool-care.html">monsoon and dust storm pool care</a>.</p>
</div></section>
<section class="section" aria-labelledby="why-h"><div class="wrap">
{head_block("Why Saltbrush", 'What worries pool owners <span class="accent">most?</span>', "Three things we hear on almost every first call, and what we do about each.", "why-h")}
<div class="worry-grid">{worries}</div>
<div class="note-row reveal"><div>{ic("lock")}<p><b>Your gate code is treated like a house key.</b> It is collected by phone, stored encrypted and shown to your technician on route day only. <a href="service-reports.html">How reports and codes are protected</a>.</p></div>
<div>{ic("sun")}<p><b>Small children at home?</b> Arizona law sets rules for pool fences and gates. We check your gate on every visit. <a href="pool-safety.html">Read the pool barrier guide</a>.</p></div></div>
</div></section>
''' + areas_section("white") + f'''<section class="section tint" aria-labelledby="price-h"><div class="wrap price-teaser">
<div><p class="tag">Pricing</p><h2 class="h-lg" id="price-h">How much does pool service <span class="accent">cost?</span></h2>
<p>Every price we charge is on this site. Weekly service is one flat monthly number with chemicals included, the same in July as in January. Repairs and cleanups are quoted in writing before any work starts.</p>
<p><a class="btn btn-deep" href="pricing.html">See the full price list{ARROW}</a></p></div>
{table(("Service", "Price"), price_rows, "Saltbrush starting prices", "data compact")}
</div></section>
''' + reviews_section() + faq_block('Pool service in Phoenix, <span class="accent">answered.</span>', HOME_FAQ, f'Still have a question? Call <a href="tel:{TEL}">{PHONE}</a> and a person answers.') + contact()
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    write("index.html", page("index.html", "Pool Service in Phoenix, AZ | Saltbrush Pool Care",
                             "Weekly pool service and repair in Phoenix, Arcadia, Ahwatukee and Tempe. One technician, flat monthly pricing and a water report after every visit.",
                             schemas, "", body))


def build_services_hub():
    rows = [(f'<a href="{s["slug"]}.html">{s["name"]}</a>', s["short"], f'{s["from"]} {s["unit"]}') for s in SERVICES]
    body = (page_hero("Services", 'Pool services for <span class="accent">Phoenix homes.</span>',
                      "Weekly care, cleanups, repairs and filter cleaning for residential pools. Each service has its own page with what is included and what it costs.",
                      [("Home", "index.html"), ("Services", "")], "truck",
                      "A white service pickup with pool poles and a chemical caddy parked on a palm lined Phoenix street",
                      ["Residential pools only", "Written prices before work", "Arizona ROC R-6 licensed"], QUOTE_BTN + CALL_BTN)
            + services_section(title='Which service <span class="accent">do you need?</span>')
            + f'''<section class="section white" aria-labelledby="cmp-h"><div class="wrap">
{head_block("Side by side", 'How do the services <span class="accent">compare?</span>', "Starting prices for a standard residential pool.", "cmp-h")}
{table(("Service", "What it is", "Starting price"), rows, "Saltbrush services compared")}
<p class="fine">Not sure which one fits? <a href="index.html#contact">Send four details</a> and we will tell you. Seasonal help is covered in the <a href="monsoon-pool-care.html">monsoon guide</a>.</p>
</div></section>
''' + faq_block('Choosing a service, <span class="accent">answered.</span>', SERVICES_FAQ, "What new customers ask before they pick.", "tint") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")]),
               {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f'{BASE}/{s["slug"]}.html'} for i, s in enumerate(SERVICES)]}]
    write("services.html", page("services.html", "Pool Services in Phoenix, AZ | Saltbrush Pool Care",
                                "Pool services for Phoenix homes: weekly service, green pool cleanup, equipment repair and filter cleaning, each with its price on the page.",
                                schemas, "services", body))


def build_service(slug):
    s, c = SVC[slug], SERVICE_PAGES[slug]
    body = (page_hero(c["tag"], c["h1"], c["lede"], [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")],
                      s["img"], s["alt"], c["points"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="section" aria-labelledby="inc-h"><div class="wrap two-col">
<div><p class="tag">Included</p><h2 class="h-lg" id="inc-h">{c["included_title"]}</h2>{checks(c["included"])}</div>
<div class="prose"><p class="tag">Good to know</p><h2 class="h-lg">{c["body_title"]}</h2>{"".join(f"<p>{p}</p>" for p in c["body"])}</div>
</div></section>
<section class="section white" aria-labelledby="rows-h"><div class="wrap">
{head_block("Prices", f'What does it <span class="accent">cost?</span>', "Sample prices for this demo. A live site would show your own.", "rows-h")}
{table(c["rows_head"], c["rows"], c["rows_title"])}
<p class="fine">Every job gets a written price before work starts. See the <a href="pricing.html">full price list</a> or how the <a href="service-reports.html">weekly report</a> works.</p>
</div></section>
''' + services_section("tint", exclude=slug, title='What else does Saltbrush <span class="accent">do?</span>')
            + faq_block(f'{s["name"]}, <span class="accent">answered.</span>', c["faq"], "The questions we hear most about this service.") + contact(need=s["need"]))
    schemas = [org_schema(), business_schema(), service_schema(s["name"], c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (s["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "services", body))


def build_monsoon():
    before = checks(STORM_BEFORE)
    body = (page_hero("Monsoon and dust storm care", 'What should you do with a pool <span class="accent">when a haboob is coming?</span>',
                      "Arizona's monsoon runs from June 15 to September 30. Here is what to do before a dust storm, how to clean up after one, and what Saltbrush does for weekly customers.",
                      [("Home", "index.html"), ("Monsoon care", "")], "haboob",
                      "A towering wall of dust rolling toward a Phoenix neighborhood at dusk, with a calm backyard pool in the foreground",
                      ["Season dates: June 15 to September 30", "Cleanup visit on your next route day", "Storm rate on filter cleanings"], QUOTE_BTN)
            + f'''<section class="section" aria-labelledby="before-h"><div class="wrap two-col">
<div><p class="tag">Before the storm</p><h2 class="h-lg" id="before-h">What should I do <span class="accent">before a dust storm?</span></h2>{before}{season_status()}</div>
<div class="prose"><p class="tag">Why it matters</p><h2 class="h-lg">What does a dust storm <span class="accent">do to pool water?</span></h2>
<p>A haboob drops fine desert silt into the pool, and that silt carries phosphates, which are food for algae. The dust also loads the filter, so the pump moves less water at the moment the pool needs it most.</p>
<p>Rain that follows is slightly acidic and dilutes the water, so pH, alkalinity and chlorine can all fall overnight. A pool that is left alone after a big storm often turns cloudy within a day and green within a week.</p>
<p>The fix is simple, and the order matters. Debris comes out first, then the dust, then the filter is cleaned, and only then is the water tested and corrected.</p></div>
</div></section>
<section class="section white" aria-labelledby="after-h"><div class="wrap">
{split("After the storm", 'How do you clean a pool <span class="accent">after a haboob?</span>',
       ["These are the eight steps our technicians follow on a storm cleanup visit. You can do the first three yourself the morning after, and they make the biggest difference.",
        "If the water is still brown after a full day of filtering, the filter needs cleaning again. That is normal after a large storm."],
       "storm", "A leaf rake on a long pole skimming palm fronds and dust from a pool the morning after a storm", "after-h")}
{steps(STORM_AFTER, "steps eight")}
</div></section>
<section class="section tint" aria-labelledby="tbl-h"><div class="wrap">
{head_block("Troubleshooting", 'What is wrong with my pool <span class="accent">after the storm?</span>', "Match what you see to the likely cause.", "tbl-h")}
{table(("What you see", "What is happening", "What fixes it"), STORM_TABLE, "Common pool problems after a monsoon storm and how to fix them")}
<p class="fine">Storm cleanup visits are $85 for weekly customers, and an after storm <a href="filter-cleaning.html">filter cleaning</a> is $75. If the pool has already turned, see <a href="green-pool-cleanup.html">green pool cleanup</a>.</p>
</div></section>
''' + faq_block('Monsoon pool care, <span class="accent">answered.</span>', MONSOON_FAQ, "Season dates are from the National Weather Service.") + contact())
    desc = "What to do with a Phoenix pool before and after a monsoon dust storm: season dates, eight cleanup steps, a troubleshooting table and storm visit prices."
    schemas = [org_schema(), business_schema(), article_schema("Monsoon and dust storm pool care in Phoenix", desc, "monsoon-pool-care.html"),
               faq_schema(MONSOON_FAQ), crumbs_schema([("Home", ""), ("Monsoon care", "monsoon-pool-care.html")])]
    write("monsoon-pool-care.html", page("monsoon-pool-care.html", "Monsoon Pool Care in Phoenix | Saltbrush Pool Care", desc, schemas, "monsoon", body))


def build_safety():
    abc = [("Adult supervision", "An adult watching the water with no phone in hand is the first layer, every time a child is near the pool."),
           ("Barriers", "A fence and a self latching gate slow a child down when supervision slips. They only work if the gate is closed."),
           ("Classes", "Swim lessons for children and CPR training for adults are the third layer that Valley fire departments teach.")]
    body = (page_hero("Pool safety", 'What does Arizona law require <span class="accent">around a backyard pool?</span>',
                      "A plain summary of the state pool barrier rule, A.R.S. 36-1681, for homes where a child under six lives, with the numbers in one table.",
                      [("Home", "index.html"), ("Pool safety", "")], "fence",
                      "A black wrought iron pool fence with a closed self latching gate around a backyard pool",
                      ["State rule: A.R.S. 36-1681", "5 foot barrier, 54 inch latch", "We check your gate on every visit"])
            + f'''<section class="section" aria-labelledby="law-h"><div class="wrap">
{head_block("The state rule", 'What are the pool barrier <span class="accent">requirements in Arizona?</span>', "From the Arizona Department of Health Services residential pool safety notice.", "law-h")}
{table(("Requirement", "What the state rule says"), BARRIER_TABLE, "Arizona residential pool barrier requirements under A.R.S. 36-1681")}
<p class="fine">This is general information, checked in October 2026, and it is not legal advice. Many Valley cities have their own pool barrier codes that add to the state rule. Your city's building department has the final word for your address.</p>
</div></section>
<section class="section white" aria-labelledby="abc-h"><div class="wrap">
{head_block("Layers of protection", 'What keeps children safe <span class="accent">around water?</span>', "No single layer is enough on its own.", "abc-h")}
{steps(abc, "steps three")}
</div></section>
<section class="section tint" aria-labelledby="gate-h"><div class="wrap two-col">
<div class="prose"><p class="tag">What we do</p><h2 class="h-lg" id="gate-h">How does Saltbrush <span class="accent">help with pool safety?</span></h2>
<p>We are in your yard every week, so we see the gate more often than anyone except you. On every visit the technician pulls the gate shut behind them and checks that it closed and latched without help.</p>
<p>If the closer is weak, the latch is sticking or something has been propped against the fence that a child could climb, it goes on your report the same day with a photo.</p>
<p>We do not install or repair pool barriers. That work belongs to a fence contractor or a pool builder, and we will tell you which one to call.</p></div>
<div><p class="tag">Checked every visit</p><h2 class="h-lg">The gate check</h2>{checks(["Gate swings closed without a push", "Latch catches on its own", "Latch is out of a small child's reach", "Nothing climbable is stacked against the fence", "Pool toys are out of the water when we leave", "Any problem is on your report with a photo"])}</div>
</div></section>
''' + faq_block('Arizona pool fence rules, <span class="accent">answered.</span>', SAFETY_FAQ, "Short answers for homeowners.") + contact())
    desc = "Arizona pool barrier law A.R.S. 36-1681 in plain words: who it applies to, fence height, gate and latch rules, and the gate check on every Saltbrush visit."
    schemas = [org_schema(), business_schema(), article_schema("Arizona pool barrier requirements for homeowners", desc, "pool-safety.html"),
               faq_schema(SAFETY_FAQ), crumbs_schema([("Home", ""), ("Pool safety", "pool-safety.html")])]
    write("pool-safety.html", page("pool-safety.html", "Arizona Pool Fence Law Explained | Saltbrush Pool Care", desc, schemas, "safety", body))


def build_pricing():
    groups = "".join(
        f'<section class="section {bg}" aria-labelledby="p-{slug}"><div class="wrap">'
        + head_block(SVC[slug]["name"], f'{SERVICE_PAGES[slug]["rows_title"]}', f'<a href="{slug}.html">How {SVC[slug]["name"].lower()} works</a>', f"p-{slug}")
        + table(SERVICE_PAGES[slug]["rows_head"], SERVICE_PAGES[slug]["rows"], SERVICE_PAGES[slug]["rows_title"]) + "</div></section>\n"
        for slug, bg in zip(SVC, ["", "white", "", "white"]))
    extras = [("Storm cleanup visit", "Weekly customers, after a dust storm", "$85"), ("Phosphate treatment", "After a storm or an algae bloom", "$45"), ("Tile line cleaning", "Scale removed at the waterline", "From $220"), ("One time vacation service", "A single full visit", "$75")]
    body = (page_hero("Pricing", 'Every price, <span class="accent">on one page.</span>',
                      "Sample prices for a fictional company, laid out the way a pool owner wants to read them: what it is, what it covers and what it costs.",
                      [("Home", "index.html"), ("Pricing", "")], None, "", ["Flat monthly price all year", "Chemicals included in weekly service", "Written price before any repair"], QUOTE_BTN)
            + groups + f'''<section class="section tint" aria-labelledby="p-extra"><div class="wrap">
{head_block("Other work", "Storm visits and extras", 'See the <a href="monsoon-pool-care.html">monsoon guide</a> for when these apply.', "p-extra")}
{table(("Service", "When it applies", "Price"), extras, "Storm visits and extra services")}
<p class="fine">Prices are samples written for this demo site. Saltbrush is a fictional company.</p>
</div></section>
''' + faq_block('Pool service pricing, <span class="accent">answered.</span>', PRICING_FAQ, "How billing works.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(PRICING_FAQ), crumbs_schema([("Home", ""), ("Pricing", "pricing.html")]),
               {"@context": "https://schema.org", "@type": "OfferCatalog", "name": "Saltbrush Pool Care sample prices",
                "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}, "description": f'{s["from"]} {s["unit"]}'} for s in SERVICES]}]
    write("pricing.html", page("pricing.html", "Pool Service Prices in Phoenix | Saltbrush Pool Care",
                               "Pool service prices in Phoenix on one page: weekly service at $155 a month, green pool cleanup, filter cleaning, repairs and storm visits.",
                               schemas, "pricing", body))


def build_reports():
    items = "".join(f'<div class="item reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in REPORT_ITEMS)
    sec = "".join(f'<div class="item reveal">{ic("lock")}<h3>{t}</h3><p>{d}</p></div>' for t, d in REPORT_SECURITY)
    body = (page_hero("Your weekly report", 'A report after every visit, <span class="accent">and your gate code kept safe.</span>',
                      "What the report shows, why it exists, and how Saltbrush protects the two most sensitive things a pool company holds: your gate code and your schedule.",
                      [("Home", "index.html"), ("Your weekly report", "")], None, "",
                      ["Sent by text and email within minutes", "Six readings beside their targets", "Codes stored encrypted, views logged"], QUOTE_BTN)
            + f'''<section class="section" aria-labelledby="rep-h"><div class="wrap two-col report">
<div><p class="tag">What you receive</p><h2 class="h-lg" id="rep-h">What is on <span class="accent">the weekly report?</span></h2>
<p>The report answers the question every pool owner has when they come home: did someone come, and what did they do? It is short enough to read at a stoplight and complete enough to hand to the next owner of the house.</p>
<div class="items">{items}</div></div>
{water_card("Visit report, Tuesday 7:42 AM", "Arrived 7:14 AM, left 7:42 AM. Added 1 quart of acid. Filter at 14 psi. Gate latched.")}
</div></section>
<section class="section deep" aria-labelledby="sec-h"><div class="wrap">
{head_block("Security", 'How are gate codes and reports <span class="accent">protected?</span>', "A pool company knows when you are away and how to open your gate. We treat that as the responsibility it is.", "sec-h")}
<div class="items four">{sec}</div>
</div></section>
<section class="section white" aria-labelledby="why-h"><div class="wrap prose narrow">
<p class="tag">Why it matters</p><h2 class="h-lg" id="why-h">Why does a pool company need <span class="accent">to think about security?</span></h2>
<p>Most pool routes still run on a clipboard or a group text. Somewhere in that thread is a list of addresses, the day nobody is home, and the code that opens the side gate. If a phone is lost or a former employee keeps the thread, that list goes with them.</p>
<p>Saltbrush keeps codes in one system with a login for each person, and removes access the day someone leaves. Technicians see a code on the morning of your route day and at no other time. Every view is logged.</p>
<p>The same care applies to this website. It loads no trackers, sets no advertising cookies, and its forms ask only for what a quote needs. Read the <a href="privacy.html">privacy page</a> for the full list.</p>
</div></section>
''' + faq_block('Reports and privacy, <span class="accent">answered.</span>', REPORT_FAQ, "How the report and the portal work.", "tint") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(REPORT_FAQ), crumbs_schema([("Home", ""), ("Your weekly report", "service-reports.html")])]
    write("service-reports.html", page("service-reports.html", "Weekly Pool Service Reports | Saltbrush Pool Care",
                                       "What the Saltbrush weekly pool report shows, and how gate codes, photos and schedules are protected with encryption, logging and two step login.",
                                       schemas, "", body))


def build_about():
    people = "".join(f'<div class="person reveal"><span class="avatar" aria-hidden="true">{i}</span><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></div>' for i, n, r, b in PEOPLE)
    scope = [("Covered by our R-6 license", "Service and minor repair of residential pools and accessories: pumps, filters, salt systems, automation, valves and equipment plumbing."),
             ("Outside it", "Connections to a drinking water line, gas lines, gas chlorine systems, electrical work beyond the first disconnect, and full replacement of plaster, pebble or decks."),
             ("What we do then", "We tell you which licensed trade to call, what to ask for, and we coordinate our part of the job around theirs.")]
    body = (page_hero("About Saltbrush", 'A small pool company that <span class="accent">shows its work.</span>',
                      "Saltbrush started in 2014 with one truck and forty pools in central Phoenix. It is still owner run, and every technician is an employee.",
                      [("Home", "index.html"), ("About", "")], "truck",
                      "A white service pickup with pool poles, a leaf net and a chemical caddy on a Phoenix street at sunrise",
                      ["Owner on a route every Friday", "Employees, never subcontractors", "Arizona ROC R-6 licensed"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="section" aria-labelledby="story-h"><div class="wrap prose narrow">
<p class="tag">Our story</p><h2 class="h-lg" id="story-h">Why did Saltbrush <span class="accent">start?</span></h2>
<p>Nico Velarde spent six summers on another company's routes, servicing more pools a day than anyone could do well. Customers rarely knew his name, and he rarely had time to brush. He left to build a company around two rules: fewer pools per route, and a report after every visit.</p>
<p>Those two rules still run the business. A technician has about half an hour at each pool. The report goes out before the truck leaves your street. Everything else, from the flat monthly price to the way gate codes are stored, follows from wanting customers to be able to check our work.</p>
<p>We stay inside a small part of the Valley on purpose. Tight routes through <a href="arcadia.html">Arcadia</a>, <a href="ahwatukee.html">Ahwatukee</a> and <a href="tempe.html">Tempe</a> mean less time on the freeway and more time with a brush in the water.</p>
</div></section>
<section class="section white" aria-labelledby="team-h"><div class="wrap">
{head_block("The team", 'Who looks after <span class="accent">your pool?</span>', "Fictional people, written for this demo.", "team-h")}
<div class="people">{people}</div>
</div></section>
<section class="section tint" aria-labelledby="lic-h"><div class="wrap">
{head_block("Licensing", 'What is Saltbrush <span class="accent">licensed to do?</span>', "The scope of Arizona's R-6 classification, in plain words.", "lic-h")}
{steps(scope, "steps three")}
<p class="fine">Scope summarized from the Arizona Registrar of Contractors residential classification R-6, Swimming Pool Service and Repair. See <a href="equipment-repair.html">equipment repair</a> for what that looks like on a job.</p>
</div></section>
''' + reviews_section("") + faq_block('About Saltbrush, <span class="accent">answered.</span>', ABOUT_FAQ, "A few things people ask before they hire us.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("About", "about.html")]),
               {"@context": "https://schema.org", "@type": "Person", "name": "Nico Velarde", "jobTitle": "Owner and lead technician", "worksFor": {"@id": f"{BASE}/#org"}}]
    write("about.html", page("about.html", "About Saltbrush Pool Care | Phoenix Pool Service",
                             "Saltbrush Pool Care is an owner run Phoenix pool service founded in 2014, with employee technicians, capped routes and an Arizona R-6 license.",
                             schemas, "about", body))


def build_area(slug):
    a, c = AREA[slug], AREA_PAGES[slug]
    notes = table(("What we see here", "What we do about it"), c["notes"], f'Pool care notes for {a["name"]}')
    body = (page_hero(f'{a["name"]} · {a["zip"]}', c["h1"], c["lede"], [("Home", "index.html"), ("About", "about.html"), (a["name"], "")],
                      a["img"], a["alt"], c["points"], QUOTE_BTN + CALL_BTN)
            + f'''<section class="section" aria-labelledby="loc-h"><div class="wrap two-col">
<div class="prose"><p class="tag">Local notes</p><h2 class="h-lg" id="loc-h">{c["body_title"]}</h2>{"".join(f"<p>{p}</p>" for p in c["body"])}</div>
<div><p class="tag">On the route</p><h2 class="h-lg">What we plan for</h2>{notes}{season_status()}</div>
</div></section>
''' + services_section("white", title=f'What do we do for pools <span class="accent">in {a["name"]}?</span>') + areas_section("tint", exclude=slug)
            + faq_block(f'{a["name"]} pool service, <span class="accent">answered.</span>', c["faq"], "What neighbors here ask us.") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(c["faq"]), crumbs_schema([("Home", ""), ("About", "about.html"), (a["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "about", body))


def build_privacy():
    body_html = "".join(f'<h2 class="h-md">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (page_hero("Privacy", 'Your privacy at <span class="accent">Saltbrush.</span>',
                      "What this website collects, how gate codes and photos are handled, and what we will never ask you for.",
                      [("Home", "index.html"), ("Privacy", "")])
            + f'''<section class="section"><div class="wrap prose narrow">{body_html}
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
