"""Build the Tallybrook Tax and Accounting demo into public/demos/tallybrook/.

Run from the repo root:  python3 scripts/demos/tallybrook/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from tb import *  # noqa: E402,F403
from content import (REVIEWS, HOME_FAQ, SERVICE_PAGES, SERVICES_FAQ, GUIDE_ROWS, GUIDE_SECTIONS, GUIDE_FAQ, DEADLINE_FAQ,  # noqa: E402
                     PRICING_FAQ, UPLOAD_FAQ, ABOUT_FAQ, BIOS, AREA_PAGES, PRIVACY)

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "tallybrook")
# The home page is also served at the clean URL /demos/tallybrook (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/tallybrook/")
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
ABOUT_H1 = "A small firm that knows <span class=\"accent\">this city's taxes.</span>"
RATES_NOTE = ("Rates published by the City of Philadelphia as of October 2026. Wage Tax rates took effect July 1, 2026. "
              "BIRT, Net Profits Tax and School Income Tax rates are for tax year 2025.")


# ---------------------------------------------------------------- blocks
def head_block(folio, title, small="", hid=""):
    h = f' id="{hid}"' if hid else ""
    sm = f'<p class="small">{small}</p>' if small else "<span></span>"
    return f'<div class="section-head"><div><p class="folio">{folio}</p><h2 class="h-lg"{h}>{title}</h2></div>{sm}</div>'


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items) + "</ul>"


def ledger(exclude=None):
    rows = "".join(
        f'<li class="reveal"><a href="{s["slug"]}.html"><span class="no">No. 0{i + 1}</span><h3>{s["name"]}</h3><p>{s["short"]}</p>'
        f'<span class="from">from<b>{s["from"]}</b>{s["unit"]}</span>{ic("arrow")}</a></li>'
        for i, s in enumerate(SERVICES) if s["slug"] != exclude)
    return f'<ul class="ledger">{rows}</ul>'


def services_section(bg="", exclude=None, folio="What we do", title='Four services, <span class="accent">one set of books.</span>',
                     small="Each one has a fixed price, quoted in writing before any work starts."):
    return f'''<section class="section {bg}" aria-labelledby="svc-h"><div class="wrap">
{head_block(folio, title, small, "svc-h")}
{ledger(exclude)}
<p class="fine">Sample prices written for this demo.</p></div></section>
'''


def table(caption, cols, rows, note=""):
    head_html = "".join(f'<th scope="col">{c}</th>' for c in cols)
    body = ""
    for r in rows:
        cells = "".join(f"<td>{c}</td>" for c in r[1:])
        body += f'<tr><th scope="row">{r[0]}</th>{cells}</tr>'
    return (f'<div class="table-wrap reveal"><table class="data"><caption>{caption}</caption><thead><tr>{head_html}</tr></thead><tbody>{body}</tbody></table></div>'
            + (f'<p class="fine">{note}</p>' if note else ""))


def deadline_table(limit=None, caption="Tax deadlines, October 2026 to June 2027"):
    rows = ""
    for i, (iso, _short, tags, what) in enumerate(DEADLINES[:limit] if limit else DEADLINES):
        tag_html = " ".join(f'<span class="tag {t}">{TAG[t]}</span>' for t in tags)
        cls = ' class="next"' if i == 0 else ""
        rows += (f'<tr data-date="{iso}"{cls}>'
                 f'<th scope="row" class="num">{fmt_date(iso)}</th><td>{what}</td><td>{tag_html}</td><td class="num left-cell">Upcoming</td></tr>')
    return (f'<div class="table-wrap reveal"><table class="data dl"><caption>{caption}</caption><thead><tr><th scope="col">Date</th><th scope="col">What is due</th>'
            f'<th scope="col">Who collects it</th><th scope="col">Time left</th></tr></thead><tbody>{rows}</tbody></table></div>'
            '<p class="fine">Dates that fall on a weekend are shown moved to the next business day. The highlighted row is the next deadline, counted in Philadelphia time.</p>')


def rates_tiles():
    tiles = [("Wage Tax, residents", "3.735%", "From July 1, 2026"), ("Wage Tax, non-residents", "3.425%", "From July 1, 2026"),
             ("BIRT on net income", "5.71%", "Tax year 2025, plus 1.410 mills on receipts"), ("Pennsylvania income tax", "3.07%", "Flat rate")]
    return ('<div class="rates reveal">' + "".join(f'<div><span class="k">{k}</span><b>{v}</b><span>{n}</span></div>' for k, v, n in tiles)
            + f'</div><p class="fine">{RATES_NOTE}</p>')


def steps_section(folio, title, small, steps, bg="", hid="steps-h"):
    lis = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in steps)
    return f'''<section class="section {bg}" aria-labelledby="{hid}"><div class="wrap">
{head_block(folio, title, small, hid)}
<ol class="steps">{lis}</ol></div></section>
'''


def reviews_band(items, title='What clients <span class="accent">say.</span>', bg=""):
    return f'''<section class="section {bg}" aria-labelledby="rev-h"><div class="wrap">
{head_block("Client letters", title, "Sample reviews written for this demo. A live site would pull them from Google.", "rev-h")}
<div class="reviews">{"".join(review_card(*r) for r in items)}</div></div></section>
'''


def areas_section(bg="", exclude=None):
    cards = "".join(f'<a class="area reveal" href="{a["slug"]}.html"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1600" height="904">'
                    f'<b>{a["name"]}</b><span>{a["line"]}</span></a>' for a in AREAS if a["slug"] != exclude)
    return f'''<section class="section {bg}" aria-labelledby="areas-h"><div class="wrap">
{head_block("Where our clients are", 'Old City office, clients across <span class="accent">the region.</span>', "Three places we work most, and what tax questions come up in each.", "areas-h")}
<div class="areas">{cards}</div></div></section>
'''


def person_card(key):
    p, b = PEOPLE[key], BIOS[key]
    return (f'<article class="person reveal" id="{key}"><img src="img/{p["img"]}.webp" alt="{p["alt"]}" loading="lazy" width="1000" height="1345">'
            f'<h3>{p["name"]}</h3><p class="role">{p["role"]}</p>{"".join(f"<p>{x}</p>" for x in b["bio"])}<p class="cred">{b["cred"]}</p></article>')


def security_checks():
    return checks(["Files are encrypted on the way to us and while stored", "Every upload is checked for malware before anyone opens it",
                   "Staff sign in with a password and a code from their phone", "Only your preparer and reviewer can open your files, and every view is logged",
                   "Upload links expire after seven days and work for one client only", "A written security plan, required of tax preparers by federal rules, reviewed every January"])


# ---------------------------------------------------------------- pages
def build_home():
    hero = f'''<section class="hero"><div class="wrap hero-grid">
<div>
<p class="folio">CPA firm in Old City, Philadelphia</p>
<h1 class="h-xl">Philadelphia taxes, done on time and <span class="accent">explained.</span></h1>
<p class="lede">Tallybrook prepares tax returns, keeps books and runs payroll for households and small businesses in Philadelphia, where the city adds four taxes of its own to the federal and state list.</p>
<div class="btn-row"><a class="btn btn-ox" href="#contact">Request a call</a><a class="btn btn-line" href="pricing.html">See prices</a></div>
<ul class="hero-points"><li>{CHECK}<span>Fixed prices in writing before any work starts</span></li><li>{CHECK}<span>Wage Tax, BIRT, Net Profits and School Income Tax handled</span></li><li>{CHECK}<span>Documents sent through a secure upload page, never by email</span></li></ul>
</div>
<div class="hero-media"><img src="img/hero.webp" alt="A brick walled accounting office with an arched window, a long oak table, two laptops and a brass lamp" fetchpriority="high" width="2000" height="1129">{due_card()}</div>
</div></section>
<div class="figures"><div class="wrap">
<div><b>{YEAR_FOUNDED}</b><span>Founded in Philadelphia</span></div>
<div><b>3</b><span>Licensed preparers: two CPAs and an enrolled agent</span></div>
<div><b>10th</b><span>Day of the month your books are closed</span></div>
<div><b>1 day</b><span>To hear back from an accountant</span></div>
</div></div>
'''
    city = f'''<section class="section white" aria-labelledby="city-h"><div class="wrap">
{head_block("The Philadelphia part", 'Which taxes does Philadelphia add, and <span class="accent">at what rate?</span>', "Most accountants handle federal and state. In this city that leaves four more taxes on the table.", "city-h")}
{rates_tiles()}
<div class="two-col top" style="margin-top:44px">
<div class="prose reveal"><p>A Philadelphia household can owe tax to three governments on one paycheck. A Philadelphia freelancer files up to five returns a year. Since tax year 2025, when the city ended its $100,000 exemption, every business here files a Business Income and Receipts Tax return, including people who only freelance on the side.</p>
<p>Tallybrook was built around those rules. Every return we prepare starts with one question: which city filings apply to you? Then we price the whole set as one job.</p>
<div class="btn-row"><a class="btn btn-line" href="philadelphia-taxes.html">Philadelphia taxes explained</a></div></div>
<div class="stack reveal">
<div class="note"><h3>Working from home for a city employer?</h3><p>Non-residents can request a Wage Tax refund for days their employer required them to work outside Philadelphia.</p></div>
<div class="note green"><h3>Freelancing on the side?</h3><p>You need a Commercial Activity License, a BIRT return and a Net Profits Tax return, whatever you earned.</p></div>
</div></div>
</div></section>
'''
    deadlines = f'''<section class="section" aria-labelledby="dl-h"><div class="wrap">
{head_block("The calendar", 'What is due <span class="accent">next?</span>', "Federal, Pennsylvania and Philadelphia dates on one list, counted down from today.", "dl-h")}
{deadline_table(limit=5, caption="The next five tax deadlines")}
<div class="btn-row"><a class="btn btn-line" href="tax-deadlines.html">Full deadline calendar</a></div></div></section>
'''
    secure = f'''<section class="section dark" aria-labelledby="sec-h"><div class="wrap two-col top">
<div class="reveal"><p class="folio">How documents travel</p><h2 class="h-lg" id="sec-h">Your W-2 should never sit in <span class="accent">an inbox.</span></h2>
<p style="margin-top:18px">A tax return holds everything a thief needs: your name, address, Social Security number, income and bank account. So nothing with those details moves by email at Tallybrook, in either direction.</p>
<div class="btn-row"><a class="btn btn-paper" href="secure-upload.html">{ic("lock")}See the secure upload page</a></div></div>
<div class="reveal">{security_checks()}</div>
</div></section>
'''
    p, b = PEOPLE["odessa"], BIOS["odessa"]
    team = f'''<section class="section" aria-labelledby="team-h"><div class="wrap two-col">
<div class="reveal"><img class="photo" src="img/{p["img"]}.webp" alt="{p["alt"]}" loading="lazy" width="1000" height="1345" style="max-width:430px;aspect-ratio:4/5;object-position:top"></div>
<div class="reveal"><p class="folio">Who does the work</p><h2 class="h-lg" id="team-h">Two CPAs and an enrolled agent, <span class="accent">all in one office.</span></h2>
<p style="margin-top:18px">{b["bio"][0]}</p>
<p>Malachi Trestrail leads individual tax and answers notices. Yusra Pennington runs bookkeeping and payroll. Every return is prepared by one of them and reviewed by another, and no work is sent to outside preparers.</p>
<div class="btn-row"><a class="btn btn-ox" href="about.html">Meet the team</a><a class="btn btn-line" href="#contact">Ask a question</a></div></div>
</div></section>
'''
    body = (hero + services_section() + city + deadlines
            + steps_section("How it works", 'From first call to filed return in <span class="accent">four steps.</span>', "Most individual returns are filed within ten business days of the last document arriving.",
                            SERVICE_PAGES["individual-tax"]["steps"], "white")
            + secure + team + areas_section("white") + reviews_band(REVIEWS[:3])
            + faq_block("Before you call.", HOME_FAQ, "Short answers to what new clients ask first.", "white") + contact())
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ)]
    write("index.html", page("index.html", "Tallybrook | Philadelphia CPA, Tax and Bookkeeping",
                             "Tallybrook is a Philadelphia CPA firm for tax returns, BIRT and Wage Tax filings, bookkeeping and payroll. Fixed prices and secure document upload.",
                             schemas, "home", body))


def build_services_hub():
    body = (page_hero("Services", 'Tax, books and payroll for <span class="accent">Philadelphia.</span>',
                      "Four services, each at a fixed price, each built around the city, state and federal filings a Philadelphia household or business owes.",
                      [("Home", "index.html"), ("Services", "")], img="svc-bookkeeping", alt=SVC["bookkeeping"]["alt"],
                      points=["A CPA or enrolled agent on every return", "No work sent to outside preparers"],
                      buttons='<a class="btn btn-ox" href="#contact">Request a call</a><a class="btn btn-line" href="pricing.html">See prices</a>')
            + services_section(folio="The list", title='Pick the service that <span class="accent">fits.</span>')
            + f'''<section class="section white" aria-labelledby="which-h"><div class="wrap">
{head_block("Not sure where to start", 'Which service do <span class="accent">I need?</span>', "Find the line that sounds like you.", "which-h")}
{table("Start here", ["If this is you", "Start with", "Why"], [
    ("I have a job and a simple return", '<a href="individual-tax.html">Individual tax returns</a>', "One fixed fee covers federal, state and city filings"),
    ("I freelance or have a side business", '<a href="business-tax.html">Small business tax</a>', "You have city returns to file, even on small amounts"),
    ("My receipts are in a shoebox", '<a href="bookkeeping.html">Monthly bookkeeping</a>', "Clean books make every tax return cheaper and faster"),
    ("I am hiring my first employee", '<a href="payroll.html">Payroll</a>', "Wage Tax withholding starts with the first paycheck"),
    ("I got a letter from the IRS or the city", '<a href="secure-upload.html">Send us the letter</a>', "Most notices carry a deadline on the first page"),
])}
</div></section>
''' + steps_section("How it works", 'The same four steps for <span class="accent">every client.</span>', "", SERVICE_PAGES["individual-tax"]["steps"])
            + reviews_band(REVIEWS[3:6], bg="white")
            + faq_block('Our services, <span class="accent">answered.</span>', SERVICES_FAQ, "Who does the work and how we charge.") + contact())
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Tallybrook services",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f"{BASE}/{s['slug']}.html"} for i, s in enumerate(SERVICES)]}
    schemas = [org_schema(), business_schema(), items, faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")])]
    write("services.html", page("services.html", "Tax and Accounting Services in Philadelphia | Tallybrook",
                                "Tallybrook's services for Philadelphia households and small businesses: individual tax returns, business tax and BIRT, bookkeeping and payroll.",
                                schemas, "services", body))


def build_service(slug):
    s, c = SVC[slug], SERVICE_PAGES[slug]
    who = f'''<section class="section" aria-labelledby="who-h"><div class="wrap two-col top">
<div class="prose reveal"><p class="folio">In plain words</p><h2 class="h-lg" id="who-h">{c["who_h"]}</h2>
<div style="margin-top:18px">{"".join(f"<p>{p}</p>" for p in c["who"])}</div></div>
<div class="reveal"><h3 class="h-md" style="margin-bottom:18px">What is included</h3>{checks(c["included"])}</div>
</div></section>
'''
    price = f'''<section class="section" aria-labelledby="price-h"><div class="wrap">
{head_block("Fixed prices", 'What does it <span class="accent">cost?</span>', "You get a quote in writing before we start, and the invoice matches it.", "price-h")}
{table(f"{s['name']}: sample prices", ["Service", "What it covers", "Price"], c["prices"], "Sample prices written for this demo.")}
<div class="btn-row"><a class="btn btn-line" href="pricing.html">All prices</a><a class="btn btn-ox" href="?need={s["need"]}#contact">Get a fixed quote</a></div></div></section>
'''
    body = (page_hero(c["folio"], c["h1"], c["lede"], [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")],
                      img=s["img"], alt=s["alt"], points=c["points"],
                      buttons=f'<a class="btn btn-ox" href="?need={s["need"]}#contact">Get a fixed quote</a><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}{PHONE}</a>')
            + who + steps_section("How it works", 'Four steps, <span class="accent">no surprises.</span>', "", c["steps"], "white") + price
            + services_section("white", exclude=slug, folio="Also at Tallybrook", title='Three more <span class="accent">services.</span>', small="Most clients use two of them.")
            + faq_block(f'{s["name"]}, <span class="accent">answered.</span>', c["faq"], "What clients ask before they start.")
            + contact(need=s["need"]))
    schemas = [org_schema(), business_schema(), service_schema(s["name"], c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (s["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "services", body))


def build_guide():
    sections = ""
    for i, (h, ps) in enumerate(GUIDE_SECTIONS):
        sections += f'<h2 class="h-lg" id="g{i + 1}">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps)
    toc = "".join(f'<li>{CHECK}<a href="#g{i + 1}">{h}</a></li>' for i, (h, _) in enumerate(GUIDE_SECTIONS))
    body = (page_hero("Guide", 'Philadelphia taxes, <span class="accent">explained.</span>',
                      "The Wage Tax, the BIRT, the Net Profits Tax and the School Income Tax: who pays each one, at what rate, and when the returns are due.",
                      [("Home", "index.html"), ("Philadelphia Taxes", "")], img="area-center-city", alt=AREA["center-city"]["alt"], dims=(1600, 904),
                      points=["Rates as published by the city, October 2026", "Written by the preparers who file these returns"])
            + f'''<section class="section white" aria-labelledby="rates-h"><div class="wrap">
{head_block("The numbers", 'What are the current <span class="accent">rates?</span>', "Four figures cover most questions.", "rates-h")}
{rates_tiles()}</div></section>
<section class="section" aria-labelledby="apply-h"><div class="wrap">
{head_block("Find your line", 'Which Philadelphia taxes apply <span class="accent">to me?</span>', "Most people fit one or two of these rows.", "apply-h")}
{table("Philadelphia taxes by situation", ["Your situation", "What you pay", "What you file"], GUIDE_ROWS, RATES_NOTE)}
</div></section>
<section class="section white"><div class="wrap two-col top">
<div class="prose">{sections}</div>
<div class="stack" style="position:sticky;top:110px"><div class="note"><h3>On this page</h3><ul class="checks" style="margin-top:12px">{toc}</ul></div>
<div class="note green"><h3>General information</h3><p>This guide explains the rules in general terms. Your own situation may differ, so ask before you file. The first call is free.</p></div>
<a class="btn btn-ox" href="?need=business#contact">Ask about my situation</a></div>
</div></section>
<section class="section" aria-labelledby="dl-h"><div class="wrap">
{head_block("The calendar", 'When are these <span class="accent">due?</span>', "City returns share April 15 with the federal and state returns.", "dl-h")}
{deadline_table(limit=5, caption="The next five tax deadlines")}
<div class="btn-row"><a class="btn btn-line" href="tax-deadlines.html">Full deadline calendar</a></div></div></section>
''' + faq_block('Philadelphia taxes, <span class="accent">answered.</span>', GUIDE_FAQ, "The questions we hear every week.", "white") + contact(need="business"))
    article = {"@context": "https://schema.org", "@type": "Article", "headline": "Philadelphia taxes, explained", "dateModified": "2026-10-02", "datePublished": "2026-10-02",
               "author": {"@type": "Person", "name": "Odessa Varnum", "jobTitle": "Certified Public Accountant"}, "publisher": {"@id": f"{BASE}/#org"},
               "mainEntityOfPage": f"{BASE}/philadelphia-taxes.html", "image": f"{BASE}/img/area-center-city.webp"}
    schemas = [org_schema(), business_schema(), article, faq_schema(GUIDE_FAQ), crumbs_schema([("Home", ""), ("Philadelphia Taxes", "philadelphia-taxes.html")])]
    write("philadelphia-taxes.html", page("philadelphia-taxes.html", "Philadelphia Taxes Explained: Wage Tax, BIRT | Tallybrook",
                                          "A plain guide to Philadelphia's Wage Tax, BIRT, Net Profits Tax and School Income Tax: who pays, the 2026 rates and when each return is due.",
                                          schemas, "guide", body))


def build_deadlines():
    body = (page_hero("Calendar", 'Tax deadlines for Philadelphia, <span class="accent">counted down.</span>',
                      "Federal, Pennsylvania and city dates from now through June 2027, with the days left until each one.",
                      [("Home", "index.html"), ("Deadlines", "")],
                      buttons='<a class="btn btn-ox" href="#contact">Get help before the next one</a><a class="btn btn-line" href="philadelphia-taxes.html">Philadelphia taxes explained</a>')
            + f'''<section class="section" aria-labelledby="cal-h"><div class="wrap">
<div class="two-col" style="margin-bottom:44px">
<div><p class="folio">Next up</p><h2 class="h-lg" id="cal-h">What is due <span class="accent">next?</span></h2>
<p class="small" style="margin-top:16px;max-width:460px">The card and the table update on their own. They read today's date in Philadelphia and move to the next deadline once one has passed.</p></div>
<div>{due_card()}</div>
</div>
{deadline_table()}
</div></section>
<section class="section white" aria-labelledby="who-h"><div class="wrap">
{head_block("By type of filer", 'Which dates matter <span class="accent">to me?</span>', "Four common situations and the dates each one should circle.", "who-h")}
{table("Dates by type of filer", ["If you are", "Circle these dates", "For"], [
    ("An employee", "April 15", "Form 1040, PA-40 and, for residents with investment income, the School Income Tax return"),
    ("Self-employed", "January 15, April 15, June 15, September 15", "Quarterly estimates, plus BIRT and Net Profits Tax returns on April 15"),
    ("An employer", "The end of the month after each quarter, and February 1", "Form 941 and city Wage Tax returns each quarter, W-2s and 1099s in winter"),
    ("An S corporation or partnership", "March 15", "Form 1120-S or Form 1065, with K-1s to the owners"),
])}
</div></section>
''' + steps_section("If you are behind", 'Missed one? Here is what to do, <span class="accent">in order.</span>', "Most first time penalties can be reduced when you act quickly.",
                    [("File first", "A late return with no payment costs less than no return at all."), ("Pay what you can", "Interest stops on every dollar you send."),
                     ("Ask for relief", "A first missed deadline often qualifies for a penalty waiver."), ("Set up reminders", "We put your dates on a calendar and text you two weeks ahead.")], "")
            + faq_block('Deadlines, <span class="accent">answered.</span>', DEADLINE_FAQ, "Extensions, weekends and what happens when a date is missed.", "white") + contact())
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Tax deadlines for Philadelphia filers",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{fmt_date(d[0])}: {d[3]}"} for i, d in enumerate(DEADLINES)]}
    schemas = [org_schema(), business_schema(), items, faq_schema(DEADLINE_FAQ), crumbs_schema([("Home", ""), ("Deadlines", "tax-deadlines.html")])]
    write("tax-deadlines.html", page("tax-deadlines.html", "Philadelphia Tax Deadlines 2026 and 2027 | Tallybrook",
                                     "Federal, Pennsylvania and Philadelphia tax deadlines from October 2026 through June 2027, with a live count of the days left until each one.",
                                     schemas, "deadlines", body))


def build_pricing():
    tables = ""
    for i, s in enumerate(SERVICES):
        c = SERVICE_PAGES[s["slug"]]
        tables += (f'<div style="margin-top:{0 if i == 0 else 40}px"><h2 class="h-md" style="margin-bottom:14px"><a href="{s["slug"]}.html">{s["name"]}</a></h2>'
                   + table(f"{s['name']}: sample prices", ["Service", "What it covers", "Price"], c["prices"]) + "</div>")
    body = (page_hero("Pricing", 'Fixed prices, <span class="accent">in writing.</span>',
                      "Every Tallybrook service has a set price. You get a written quote before we start, and the invoice matches it.",
                      [("Home", "index.html"), ("Pricing", "")],
                      buttons='<a class="btn btn-ox" href="#contact">Get a fixed quote</a>')
            + f'''<section class="section" aria-labelledby="pr-h"><div class="wrap">
<h2 class="sr-only" id="pr-h">Price lists</h2>{tables}
<p class="fine">Sample prices written for this demo. A live site shows the firm's current fee schedule.</p></div></section>
<section class="section dark" aria-labelledby="inc-h"><div class="wrap two-col top">
<div class="reveal"><p class="folio">In every price</p><h2 class="h-lg" id="inc-h">What a quote <span class="accent">always includes.</span></h2>
<p style="margin-top:18px">No hourly meter and no charge for a phone call. If the facts change, we tell you the new price before doing the extra work.</p></div>
<div class="reveal">{checks(["A second preparer's review of every return", "Electronic filing with the IRS, Pennsylvania and the city", "Calls and emails with your preparer through the year",
                            "The first reply to any notice about a return we prepared", "Secure storage of your records for seven years"])}</div>
</div></section>
''' + faq_block('Pricing, <span class="accent">answered.</span>', PRICING_FAQ, "How quotes, changes and payments work.") + contact())
    offers = {"@context": "https://schema.org", "@type": "OfferCatalog", "name": "Tallybrook sample prices",
              "itemListElement": [{"@type": "Offer", "name": s["name"], "url": f"{BASE}/{s['slug']}.html", "priceCurrency": "USD",
                                   "price": s["from"].replace("$", "").replace(",", "")} for s in SERVICES]}
    schemas = [org_schema(), business_schema(), offers, faq_schema(PRICING_FAQ), crumbs_schema([("Home", ""), ("Pricing", "pricing.html")])]
    write("pricing.html", page("pricing.html", "Pricing for Tax, Bookkeeping and Payroll | Tallybrook",
                               "Tallybrook's sample price list: individual returns from $375, business returns from $850, bookkeeping from $350 a month and payroll from $95 a month.",
                               schemas, "pricing", body))


def build_upload():
    form = f'''<form class="form reveal" action="#upload-h" method="post" novalidate data-demo aria-label="Secure upload preview">
<div class="lockbar">{ic("lock")}Encrypted upload preview</div>
<div class="fields">
<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Mobile phone, for the confirmation text<input type="tel" name="phone" autocomplete="tel"></label>
</div>
<label class="field">Tax year<select name="year"><option>2026</option><option>2025</option><option>2024 or earlier</option></select></label>
<label class="drop" for="upload-files">{ic("upload")}<b>Choose files or take photos</b><span>PDFs and photos, up to 25 MB each</span>
<input class="sr-only" id="upload-files" type="file" name="files" multiple accept=".pdf,image/*"></label>
<ul class="files" aria-live="polite"></ul>
<button class="btn btn-ox" type="submit">{ic("lock")}Send securely</button>
<p class="form-note">This preview never sends a file. Anything you choose stays in your browser.</p>
<div class="form-done" role="status">This is a demo, so nothing was uploaded. On a live Tallybrook site, files go straight to encrypted storage, are checked for malware, and a text confirms what arrived.</div>
</form>'''
    body = (page_hero("Secure upload", 'Send tax documents <span class="accent">safely.</span>',
                      "W-2s, 1099s, notices and bank statements go through this page, encrypted from your phone to our files. Please never send them by email.",
                      [("Home", "index.html"), ("Send Documents", "")], img="upload", alt="A hand holding a phone above a paper document on a desk, photographing the page",
                      points=["Works from a phone camera", "A text confirms what arrived"])
            + f'''<section class="section" aria-labelledby="upload-h"><div class="wrap two-col top">
<div class="reveal"><p class="folio">Why this page exists</p><h2 class="h-lg" id="upload-h">How does Tallybrook protect <span class="accent">my documents?</span></h2>
<p style="margin-top:18px">A tax preparer holds some of the most sensitive records a business can hold. Federal rules require every preparer to keep a written information security plan, and ours starts with the simplest rule in it: tax documents do not travel by email.</p>
<div style="margin-top:24px">{security_checks()}</div></div>
{form}
</div></section>
''' + steps_section("How it works", 'Four steps from your phone to <span class="accent">our files.</span>', "The whole thing takes about three minutes.",
                    [("Open the link", "We text you a link that is tied to your client file and expires in seven days."), ("Add your files", "Choose PDFs or photograph each page. You can add more later."),
                     ("Get a text", "Within a minute, a text lists the file names we received."), ("We take it from there", "Your preparer is notified, and only your preparer and reviewer can open the files.")], "white")
            + f'''<section class="section" aria-labelledby="send-h"><div class="wrap">
{head_block("Checklist", 'What should <span class="accent">I send?</span>', "The common documents, by situation. We send a list that fits you after the first call.", "send-h")}
{table("Documents to send", ["If you have", "Send", "Arrives by"], [
    ("A job", "Form W-2 from each employer", "Early February"),
    ("Freelance or contract income", "Forms 1099-NEC and 1099-K, plus your own income and expense totals", "Early February"),
    ("Investments", "Forms 1099-INT, 1099-DIV and 1099-B", "Mid February to March"),
    ("A home", "Form 1098 for mortgage interest, and your property tax bill", "Early February"),
    ("A share of a business", "Schedule K-1", "March, sometimes later"),
    ("A letter from the IRS, Pennsylvania or the city", "Every page of the letter, the day it arrives", "Any time"),
])}
</div></section>
''' + faq_block('Sending documents, <span class="accent">answered.</span>', UPLOAD_FAQ, "What happens to a file after you send it.", "white") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(UPLOAD_FAQ), crumbs_schema([("Home", ""), ("Send Documents", "secure-upload.html")])]
    write("secure-upload.html", page("secure-upload.html", "Send Tax Documents Securely | Tallybrook",
                                     "Send W-2s, 1099s and tax notices to Tallybrook through an encrypted upload page. See how files are protected and why email is the wrong way to send them.",
                                     schemas, "", body))


def build_about():
    story = f'''<section class="section" aria-labelledby="story-h"><div class="wrap two-col top">
<div class="prose reveal"><p class="folio">Our story</p><h2 class="h-lg" id="story-h">Why did Tallybrook <span class="accent">start?</span></h2>
<p style="margin-top:18px">Odessa Varnum spent thirteen years at a regional accounting firm in Center City. The firm's large clients got a partner on the phone the same day. The corner store owner and the freelance designer waited a week, and often got a bill they could not predict.</p>
<p>She opened Tallybrook in {YEAR_FOUNDED} with two rules that still hold. Every client gets a fixed price in writing before work starts, and every call is returned within one business day.</p>
<p>The name is plain on purpose. A tally is a count you can check. That is the job.</p></div>
<div class="reveal"><img class="photo" src="img/hero.webp" alt="The Tallybrook office: a brick wall, an arched window and a long oak table with two laptops" loading="lazy" width="2000" height="1129" style="aspect-ratio:16/10">
<div class="note" style="margin-top:20px"><h3>Find us</h3><p>Old City, Philadelphia, two blocks from the 2nd Street station on the Market-Frankford Line. Monday to Friday, 9 AM to 5:30 PM, and Saturday mornings from February through April 15.</p></div></div>
</div></section>
'''
    team = f'''<section class="section white" aria-labelledby="team-h"><div class="wrap">
{head_block("The preparers", 'Three people who <span class="accent">sign the returns.</span>', "Each return is prepared by one of them and reviewed by another.", "team-h")}
<div class="team">{"".join(person_card(k) for k in PEOPLE)}</div></div></section>
'''
    who = f'''<section class="section" aria-labelledby="who-h"><div class="wrap">
{head_block("Who to ask for", 'Who should <span class="accent">I talk to?</span>', "One phone number reaches all three.", "who-h")}
{table("Who does what at Tallybrook", ["Preparer", "License", "Ask about"], [
    (f'<a href="#odessa">{PEOPLE["odessa"]["plain"]}</a>', "CPA, Pennsylvania", "Business returns, entity choices, planning"),
    (f'<a href="#malachi">{PEOPLE["malachi"]["plain"]}</a>', "Enrolled agent, IRS", "Individual returns, back filings, IRS and city letters"),
    (f'<a href="#yusra">{PEOPLE["yusra"]["plain"]}</a>', "CPA, Pennsylvania", "Bookkeeping, payroll, restaurants"),
])}
</div></section>
'''
    body = (page_hero("About", ABOUT_H1,
                      f"Tallybrook has prepared returns and kept books for Philadelphia households and small businesses since {YEAR_FOUNDED}, from one office in Old City.",
                      [("Home", "index.html"), ("About", "")], img="office", dims=(1600, 904),
                      alt="A red brick rowhouse office on a cobblestone street, with a dark green door, marble steps and lit windows",
                      buttons=f'<a class="btn btn-ox" href="#contact">Request a call</a><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}{PHONE}</a>')
            + story
            + team + who + areas_section("white") + reviews_band(REVIEWS[3:6])
            + faq_block('About the firm, <span class="accent">answered.</span>', ABOUT_FAQ, "Licenses, size and when we take new clients.", "white") + contact())
    people = [{"@context": "https://schema.org", "@type": "Person", "name": p["plain"], "jobTitle": p["role"], "image": f"{BASE}/img/{p['img']}.webp",
               "worksFor": {"@id": f"{BASE}/#org"}, "url": f"{BASE}/about.html#{k}"} for k, p in PEOPLE.items()]
    schemas = [org_schema(), business_schema()] + people + [faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("About", "about.html")])]
    write("about.html", page("about.html", "About Tallybrook | CPA Firm in Old City, Philadelphia",
                             "Meet the two CPAs and the enrolled agent at Tallybrook, a Philadelphia tax and accounting firm founded in 2011 with fixed prices and a one day reply.",
                             schemas, "about", body))


def build_area(slug):
    a, c = AREA[slug], AREA_PAGES[slug]
    pts = "".join(f'<div class="note{" green" if i % 2 else ""} reveal"><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(c["points"]))
    body = (page_hero(f'{a["name"]}, {a["zip"]}', c["h1"], c["lede"], [("Home", "index.html"), ("About", "about.html"), (a["name"], "")],
                      img=a["img"], alt=a["alt"], dims=(1600, 904),
                      buttons=f'<a class="btn btn-ox" href="#contact">Request a call</a><a class="btn btn-line" href="philadelphia-taxes.html">Philadelphia taxes explained</a>')
            + f'''<section class="section" aria-labelledby="about-h"><div class="wrap two-col top">
<div class="prose reveal"><p class="folio">The tax picture here</p><h2 class="h-lg" id="about-h">What do clients in {a["name"].replace("The ", "the ")} <span class="accent">ask us?</span></h2>
<div style="margin-top:18px">{"".join(f"<p>{p}</p>" for p in c["about"])}</div>
<div class="note green" style="margin-top:24px"><h3>Getting to the office</h3><p>{c["getting"]}</p></div></div>
<div class="stack">{pts}</div>
</div></section>
<section class="section white" aria-labelledby="rates-h"><div class="wrap">
{head_block("The numbers", 'What are the current <span class="accent">city rates?</span>', "The four figures that come up most.", "rates-h")}
{rates_tiles()}</div></section>
''' + services_section() + areas_section("white", exclude=slug)
            + faq_block(f'{a["name"]}, <span class="accent">answered.</span>', c["faq"], "What clients from this area ask most.") + contact())
    schemas = [org_schema(), business_schema(), faq_schema(c["faq"]), crumbs_schema([("Home", ""), ("About", "about.html"), (a["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "about", body))


def build_privacy():
    body_html = "".join(f'<h2 class="h-md" style="font-family:var(--serif);font-weight:700;margin:36px 0 10px">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (page_hero("Privacy and security", 'Your privacy at <span class="accent">Tallybrook.</span>',
                      "What this website collects, how tax documents are protected, and what we will never ask you for.",
                      [("Home", "index.html"), ("Privacy", "")])
            + f'''<section class="section"><div class="wrap prose" style="max-width:800px">{body_html}
<p class="fine" style="margin-top:36px">This is a demo site by Meraki is Love. Tallybrook is a fictional firm, and nothing entered on this site is sent anywhere. Read more about <a href="secure-upload.html">sending documents</a>, <a href="services.html">our services</a> or <a href="about.html">the team</a>.</p>
</div></section>
''' + contact())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy and Security | Tallybrook Tax and Accounting",
                               "How Tallybrook handles your information: what the website collects, how tax documents are encrypted and stored, and what we never ask for.",
                               schemas, "", body))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Building Tallybrook demo:")
    build_home()
    build_services_hub()
    for sv in SERVICES:
        build_service(sv["slug"])
    build_guide()
    build_deadlines()
    build_pricing()
    build_upload()
    build_about()
    for ar in AREAS:
        build_area(ar["slug"])
    build_privacy()
    if PROBLEMS:
        print("\nProblems:")
        for p in PROBLEMS:
            print("  " + p)
        sys.exit(1)
