"""Shared layout pieces for the Tallybrook Tax and Accounting demo.

Tallybrook is a fictional firm. Philadelphia, its neighborhoods, transit lines,
tax types, tax rates and filing dates are real, taken from phila.gov and the
IRS calendar in October 2026. The firm, its people, phone number, prices and
reviews are demo content, and the footer of every page says so.
"""
import json
import re
from html import escape

BRAND = "Tallybrook Tax and Accounting"
SHORT = "Tallybrook"
PHONE = "(215) 555-0137"            # 555-01xx is reserved for fiction
TEL = "+12155550137"
BASE = "https://merakislove.com/demos/tallybrook"
YEAR_FOUNDED = 2011

# ---------------------------------------------------------------- icons
_P = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "lock": '<rect x="5" y="11" width="14" height="9" rx="1"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "upload": '<path d="M12 16V4M7 9l5-5 5 5M5 20h14"/>',
}
# Mark: four tally strokes and the fifth across them.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<rect x="1" y="1" width="42" height="42" fill="#7B2D26"/>'
        '<path d="M12 11v22M18.5 11v22M25 11v22M31.5 11v22" stroke="#F6F1E6" stroke-width="2.6" stroke-linecap="round"/>'
        '<path d="M7 29L37 14" stroke="#E9C27A" stroke-width="2.6" stroke-linecap="round"/></svg>')


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    fill = ' fill="currentColor"' if name == "star" else ' fill="none"'
    return (f'<svg{c} viewBox="0 0 24 24"{fill} stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# ---------------------------------------------------------------- site data
SERVICES = [
    {"slug": "individual-tax", "name": "Individual tax returns", "nav": "Individual tax", "img": "svc-individual", "need": "individual",
     "short": "Federal, Pennsylvania and Philadelphia returns for employees, freelancers and landlords.", "from": "$375", "unit": "per return",
     "alt": "A couple at a kitchen table with a laptop and a few neat folders, smiling at each other"},
    {"slug": "business-tax", "name": "Small business tax", "nav": "Business tax", "img": "svc-business", "need": "business",
     "short": "BIRT, Net Profits Tax and federal returns for sole proprietors, LLCs, partnerships and S corporations.", "from": "$1,150", "unit": "per year",
     "alt": "A coffee shop owner in a canvas apron checking figures on a tablet behind the counter"},
    {"slug": "bookkeeping", "name": "Monthly bookkeeping", "nav": "Bookkeeping", "img": "svc-bookkeeping", "need": "bookkeeping",
     "short": "Books closed by the 10th of each month, with a one page report you can read in five minutes.", "from": "$350", "unit": "per month",
     "alt": "Hands sorting receipts into piles on an oak desk beside a laptop, a calculator and a cup of coffee"},
    {"slug": "payroll", "name": "Payroll", "nav": "Payroll", "img": "svc-payroll", "need": "payroll",
     "short": "Paychecks, Philadelphia Wage Tax withholding, quarterly filings and W-2s for teams of 1 to 50.", "from": "$95", "unit": "per month",
     "alt": "Three bakery employees in aprons shaping dough together and laughing in a small bakery kitchen"},
]
SVC = {s["slug"]: s for s in SERVICES}

AREAS = [
    {"slug": "center-city", "name": "Center City", "img": "area-center-city", "zip": "19102, 19103, 19107",
     "line": "Professionals, commuters and firms with an office downtown",
     "alt": "A wide downtown Philadelphia avenue lined with stone office buildings, with the City Hall clock tower at the end"},
    {"slug": "fishtown", "name": "Fishtown", "img": "area-fishtown", "zip": "19125",
     "line": "Freelancers, restaurants, bars and makers along Frankford Avenue",
     "alt": "A street of red brick rowhouses with marble steps and a corner storefront with cafe tables"},
    {"slug": "main-line", "name": "The Main Line", "img": "area-main-line", "zip": "Ardmore, Bryn Mawr, Wayne",
     "line": "Suburban households and owners who work or do business in the city",
     "alt": "A tree lined suburban main street with gray stone shopfronts and striped awnings"},
]
AREA = {a["slug"]: a for a in AREAS}

# (ISO date, short label for the card, tags, what is due). Weekend dates are
# already moved to the next business day.
DEADLINES = [
    ("2026-10-15", "Extended 2025 returns", ["fed", "pa"], "Extended 2025 individual returns: Form 1040 and PA-40, for anyone who filed an extension in April"),
    ("2026-11-02", "Third quarter Form 941", ["fed"], "Third quarter payroll return, Form 941. October 31 falls on a Saturday, so it moves to Monday"),
    ("2027-01-15", "Fourth quarter estimates", ["fed", "pa"], "Fourth quarter 2026 estimated tax payments, federal and Pennsylvania"),
    ("2027-02-01", "W-2s and 1099s", ["fed", "phl"], "W-2 and 1099-NEC forms to recipients and filed, fourth quarter Form 941, and the Philadelphia Wage Tax fourth quarter return"),
    ("2027-03-15", "S corp and partnership returns", ["fed"], "2026 S corporation and partnership returns: Forms 1120-S and 1065, with K-1s to owners"),
    ("2027-04-15", "Individual returns", ["fed", "pa"], "2026 individual returns, Form 1040 and PA-40, and first quarter 2027 estimated payments"),
    ("2027-04-15", "Philadelphia business returns", ["phl"], "2026 Philadelphia BIRT, Net Profits Tax and School Income Tax returns, with BIRT and Net Profits estimated payments"),
    ("2027-06-15", "Second quarter estimates", ["fed", "pa", "phl"], "Second quarter 2027 estimated payments, federal and Pennsylvania, and the second Net Profits Tax installment"),
]
TAG = {"fed": "Federal", "pa": "Pennsylvania", "phl": "Philadelphia"}
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

PEOPLE = {
    "odessa": {"name": "Odessa Varnum, CPA", "plain": "Odessa Varnum", "role": "Founder and managing partner", "img": "agent-odessa",
               "alt": "Odessa Varnum, CPA, founder of Tallybrook, in front of a brick wall in the office"},
    "malachi": {"name": "Malachi Trestrail, EA", "plain": "Malachi Trestrail", "role": "Tax director", "img": "agent-malachi",
                "alt": "Malachi Trestrail, enrolled agent, beside a tall office window"},
    "yusra": {"name": "Yusra Pennington, CPA", "plain": "Yusra Pennington", "role": "Bookkeeping and payroll lead", "img": "agent-yusra",
              "alt": "Yusra Pennington, CPA, at her desk with shelves of binders behind her"},
}


def fmt_date(iso, year=True):
    y, m, d = iso.split("-")
    return f"{MONTHS[int(m) - 1]} {int(d)}" + (f", {y}" if year else "")


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/",
            "logo": f"{BASE}/img/og.jpg", "telephone": "+1-215-555-0137", "foundingDate": str(YEAR_FOUNDED),
            "founder": {"@type": "Person", "name": "Odessa Varnum", "jobTitle": "Certified Public Accountant"}}


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "AccountingService", "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
        "telephone": "+1-215-555-0137", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Philadelphia", "addressRegion": "PA", "postalCode": "19106", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": n} for n in ["Old City, Philadelphia", "Center City, Philadelphia", "Fishtown, Philadelphia", "Ardmore, Pennsylvania", "Bryn Mawr, Pennsylvania", "Wayne, Pennsylvania"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "17:30"}],
        "parentOrganization": {"@id": f"{BASE}/#org"},
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/",
            "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


def service_schema(name, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": f"{BASE}/{path}",
            "provider": {"@id": f"{BASE}/#business"}, "areaServed": {"@type": "City", "name": "Philadelphia"}}


def faq_schema(qa):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qa]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(n), "item": f"{BASE}/{href}" if href else f"{BASE}/"}
                                for i, (n, href) in enumerate(items)]}


def ld(obj):
    # Escape "</" so a value can never close the script element early.
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


# ---------------------------------------------------------------- chrome
def head(title, desc, path, schemas, og_img="og.jpg"):
    url = f"{BASE}/" if path == "index.html" else f"{BASE}/{path}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{escape(desc, quote=True)}">
<meta name="author" content="{BRAND}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(strip(title), quote=True)}">
<meta property="og:description" content="{escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#173A2F">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&amp;family=Libre+Caslon+Text:wght@400;700&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def brand_html():
    return f'<a class="brand" href="index.html" aria-label="{BRAND}, home">{MARK}<span class="brand-name"><b>Tallybrook</b><span>Tax and Accounting</span></span></a>'


def header(current=""):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    svc_dd = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<header class="site-header">
<div class="navbar"><div class="wrap">
{brand_html()}
<nav class="nav" aria-label="Main">
<ul>
<li><a class="nav-link" href="services.html"{cur("services")}>Services{ic("chev")}</a><ul class="dropdown">{svc_dd}<li><a href="services.html">All services</a></li></ul></li>
<li><a class="nav-link" href="philadelphia-taxes.html"{cur("guide")}>Philadelphia taxes</a></li>
<li><a class="nav-link" href="tax-deadlines.html"{cur("deadlines")}>Deadlines</a></li>
<li><a class="nav-link" href="pricing.html"{cur("pricing")}>Pricing</a></li>
<li><a class="nav-link" href="about.html"{cur("about")}>About</a></li>
</ul>
<div class="nav-cta"><a class="nav-phone" href="tel:{TEL}">{PHONE}</a><a class="btn btn-ox" href="secure-upload.html">{ic("lock")}Send documents</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-label="Open menu">{ic("menu")}</button></div>
</nav>
</div></div>
</header>
'''


def crumbs(items):
    out = []
    for i, (n, href) in enumerate(items):
        if i < len(items) - 1:
            out.append(f'<a href="{href or "index.html"}">{n}</a><span aria-hidden="true">/</span>')
        else:
            out.append(f'<span aria-current="page">{n}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(out)}</nav>'


def page_hero(folio, h1, lede, crumb_items, img=None, alt="", points=None, buttons="", dims=(1500, 1115)):
    pts = ""
    if points:
        pts = '<ul class="hero-points">' + "".join(f"<li>{ic('check')}<span>{p}</span></li>" for p in points) + "</ul>"
    copy = f'''<div class="copy">
{crumbs(crumb_items)}
<p class="folio">{folio}</p>
<h1 class="h-xl">{h1}</h1>
<p class="lede">{lede}</p>
{f'<div class="btn-row">{buttons}</div>' if buttons else ""}{pts}
</div>'''
    if img:
        inner = f'<div class="grid">{copy}<div class="frame"><img src="img/{img}.webp" alt="{alt}" fetchpriority="high" width="{dims[0]}" height="{dims[1]}"></div></div>'
    else:
        inner = f'<div style="max-width:820px">{copy}</div>'
    return f'<section class="hero-page"><div class="wrap">{inner}</div></section>\n<hr class="double">\n'


def due_card():
    """The next deadline. Rendered with the first date; site.js moves it forward."""
    first = DEADLINES[0]
    y, m, d = first[0].split("-")
    data = escape(json.dumps([[x[0], x[1]] for x in DEADLINES]), quote=True)
    return (f'<div class="due" data-deadlines="{data}"><span class="lbl">Next tax deadline</span>'
            f'<div class="date"><b>{int(d)}</b><span>{MONTHS[int(m) - 1]} {y}</span></div>'
            f'<span class="what">{first[1]}</span><span class="left"><span class="n">Coming up</span>. <a href="tax-deadlines.html">See the calendar</a></span></div>')


def faq_block(title, qa, lead, bg=""):
    items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    return f'''<section class="section {bg}" aria-labelledby="faq-h">
<div class="wrap faq-layout">
<div><p class="folio">Questions people ask</p><h2 class="h-lg" id="faq-h">{title}</h2><p class="small" style="margin-top:14px">{lead}</p></div>
<div class="acc">{items}</div>
</div>
</section>
'''


def review_card(text, who, where):
    stars = "".join(ic("star") for _ in range(5))
    return (f'<figure class="review reveal"><div class="stars" role="img" aria-label="5 out of 5 stars">{stars}</div>'
            f'<blockquote>{text}</blockquote><figcaption><span>{who}, {where}</span><span class="sample">Sample review</span></figcaption></figure>')


def contact(title='Tell us what you <span class="accent">need.</span>',
            lead="A few details and a real accountant calls you back within one business day. The first call is free and takes about twenty minutes.",
            need=None):
    opts = [("individual", "My own tax return"), ("business", "Taxes for my business"), ("bookkeeping", "Bookkeeping"), ("payroll", "Payroll")]
    choices = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}"{" checked" if need == v else ""}>{t}</label>' for v, t in opts)
    return f'''<section id="contact" class="section band" aria-labelledby="contact-h">
<div class="wrap form-layout">
<div>
<p class="folio">Start here</p>
<h2 class="h-lg" id="contact-h">{title}</h2>
<p class="lead">{lead}</p>
<a class="band-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
<p class="small">Old City, Philadelphia. Monday to Friday, 9 AM to 5:30 PM. Saturday mornings from February through April 15.</p>
</div>
<form class="form" action="#contact" method="post" novalidate data-demo>
<fieldset><legend class="step">1. What can we help with</legend><div class="choice-grid">{choices}</div></fieldset>
<p class="step" style="margin-top:6px">2. How to reach you</p>
<div class="fields">
<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="field">Email<input type="email" name="email" autocomplete="email"></label>
<label class="field">Best time to call<select name="when"><option>Morning</option><option>Afternoon</option><option>After 5 PM</option></select></label>
<label class="field full">Anything we should know<textarea name="note" rows="3"></textarea></label>
</div>
<button class="btn btn-ox" type="submit">Request a call</button>
<p class="form-note">Please leave Social Security numbers and tax documents out of this form. Those go through the <a href="secure-upload.html">secure upload page</a>. See our <a href="privacy.html">privacy page</a>.</p>
<div class="form-done" role="status">This is a demo site, so nothing was sent. On a live Tallybrook site, this request goes to the accountant on intake, who calls within one business day.</div>
</form>
</div>
</section>
'''


def footer():
    svcs = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-top">{brand_html()}<p class="foot-tag">Philadelphia taxes, done on time and explained.</p></div>
<div class="foot-cols">
<div><h2>Contact</h2><address>Old City, Philadelphia, PA 19106<br><a href="tel:{TEL}">{PHONE}</a><br>Mon to Fri, 9 AM to 5:30 PM<br>Saturdays in tax season</address></div>
<div><h2>Services</h2><ul>{svcs}<li><a href="pricing.html">Pricing</a></li></ul></div>
<div><h2>Guides</h2><ul><li><a href="philadelphia-taxes.html">Philadelphia taxes explained</a></li><li><a href="tax-deadlines.html">Tax deadline calendar</a></li>{areas}</ul></div>
<div><h2>Tallybrook</h2><ul><li><a href="about.html">Our team</a></li><li><a href="secure-upload.html">Send documents securely</a></li><li><a href="privacy.html">Privacy and security</a></li><li><a href="index.html#contact">Request a call</a></li></ul></div>
</div>
<div class="foot-base"><span>© 2026 {BRAND}. General information on this site is not tax advice for your situation.</span><span>A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Tallybrook is a fictional firm, and its prices are samples.</span></div>
</div>
</footer>
<div class="mobile-bar"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-ox" href="secure-upload.html">{ic("lock")}Send documents</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, desc, schemas, current, body):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
