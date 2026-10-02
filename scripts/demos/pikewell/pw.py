"""Shared layout pieces for the Pikewell Real Estate demo.

Pikewell is a fictional brokerage. Denver, its neighborhoods, parks, streets
and transit lines are real; the brokerage, its agents, phone number, listings,
prices and reviews are demo content, and the footer of every page says so.

Neighborhood copy describes homes, parks, streets and transit only. It makes
no claims about who lives somewhere, schools or safety, which is how a real
brokerage keeps its guides inside fair housing rules.
"""
import json
import re
from html import escape

BRAND = "Pikewell Real Estate"
SHORT = "Pikewell"
PHONE = "(720) 555-0164"            # 555-01xx is reserved for fiction
TEL = "+17205550164"
BASE = "https://merakislove.com/demos/pikewell"
YEAR_FOUNDED = 2014

# ---------------------------------------------------------------- icons
_P = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
}
# Mark: a peak that is also a roofline, over a level line.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<rect width="44" height="44" fill="#122341"/>'
        '<path d="M7 31 L18 14 L24 22 L29 16 L37 31" fill="none" stroke="#E2A72B" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>'
        '<path d="M7 35h30" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/></svg>')
RIDGE = ('<svg class="ridge" viewBox="0 0 1200 34" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
         '<path d="M0 34V26L90 12l60 10 90-18 90 16 90-10 100 14 90-18 90 16 90-10 90 14 80-18 90 12 80-10 70 12v12z" fill="currentColor"/></svg>')


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    fill = ' fill="currentColor"' if name == "star" else ' fill="none"'
    return (f'<svg{c} viewBox="0 0 24 24"{fill} stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# ---------------------------------------------------------------- site data
HOODS = [
    {"slug": "washington-park", "name": "Washington Park", "short": "Wash Park", "zip": "80209", "img": "hood-wash-park", "tag": "Bungalows and Denver Squares",
     "line": "A 165 acre park, two lakes and brick homes on every block",
     "alt": "A calm lake ringed by a gravel path and cottonwood trees, with a white boathouse pavilion on the far shore",
     "homes": "1910s to 1930s bungalows, Denver Squares, newer infill", "range": "$1.1M to $2.4M", "downtown": "About 15 minutes"},
    {"slug": "highland", "name": "Highland", "short": "Highland", "zip": "80211", "img": "hood-highland", "tag": "Victorians and skyline views",
     "line": "Brick Victorians and modern townhomes above downtown",
     "alt": "Red brick Victorian homes on a hillside street with the downtown Denver skyline beyond the rooftops",
     "homes": "1890s Victorians, row homes, modern townhomes", "range": "$800K to $1.6M", "downtown": "About 8 minutes"},
    {"slug": "sloans-lake", "name": "Sloan's Lake", "short": "Sloan's Lake", "zip": "80212", "img": "hood-sloans-lake", "tag": "Lake loop and mountain sunsets",
     "line": "Denver's largest lake, with the Front Range behind it",
     "alt": "A wide city lake at sunset with a cyclist on the shore path and the Front Range mountains behind",
     "homes": "Mid-century ranches, bungalows, new townhomes and condos", "range": "$750K to $1.5M", "downtown": "About 12 minutes"},
    {"slug": "park-hill", "name": "Park Hill", "short": "Park Hill", "zip": "80207", "img": "hood-park-hill", "tag": "Parkways and Tudors",
     "line": "Tree lined parkways and brick Tudors east of City Park",
     "alt": "A broad grassy parkway under tall elm trees with brick Tudor homes set back on wide lawns",
     "homes": "1920s Tudors, Denver Squares, brick bungalows", "range": "$700K to $1.4M", "downtown": "About 15 minutes"},
    {"slug": "central-park", "name": "Central Park", "short": "Central Park", "zip": "80238", "img": "hood-central-park", "tag": "Newer homes and open space",
     "line": "Homes built since 2001 around 1,100 acres of parks",
     "alt": "Colorful two story homes with front porches facing a shared green and a winding greenway path",
     "homes": "Homes from 2001 to today: single family, row homes, condos", "range": "$650K to $1.3M", "downtown": "About 20 minutes, or the A Line"},
    {"slug": "berkeley", "name": "Berkeley", "short": "Berkeley", "zip": "80212", "img": "hood-berkeley", "tag": "Tennyson Street and bungalows",
     "line": "Brick bungalows a short walk from Tennyson Street",
     "alt": "A neighborhood main street at dusk with brick storefronts, cafe tables and string lights",
     "homes": "1920s brick bungalows, duplexes, newer infill", "range": "$700K to $1.2M", "downtown": "About 15 minutes"},
]

LISTINGS = [
    {"slug": "washington-park-denver-square", "img": "home-square", "price": "$1,485,000", "price_num": 1485000, "status": "New this week",
     "title": "Restored 1912 Denver Square near Washington Park", "where": "Washington Park, Denver 80209", "hood": "washington-park",
     "beds": 4, "baths": 3, "sqft": "2,940", "sqft_num": 2940, "year": 1912, "lot": "6,250 sq ft lot", "agent": "nia",
     "alt": "A restored red brick Denver Square home with a full width front porch, white columns and a brick walkway"},
    {"slug": "berkeley-brick-bungalow", "img": "home-bungalow", "price": "$865,000", "price_num": 865000, "status": "Open Saturday",
     "title": "1926 brick bungalow near Tennyson Street", "where": "Berkeley, Denver 80212", "hood": "berkeley",
     "beds": 3, "baths": 2, "sqft": "1,720", "sqft_num": 1720, "year": 1926, "lot": "5,100 sq ft lot", "agent": "tobias",
     "alt": "A brick craftsman bungalow with a covered front porch, a sage green door and a low water front garden"},
    {"slug": "sloans-lake-townhome", "img": "home-townhome", "price": "$1,050,000", "price_num": 1050000, "status": "Price improved",
     "title": "Modern townhome with a rooftop deck by Sloan's Lake", "where": "Sloan's Lake, Denver 80212", "hood": "sloans-lake",
     "beds": 3, "baths": 4, "sqft": "2,180", "sqft_num": 2180, "year": 2019, "lot": "End unit, attached garage", "agent": "ilsa",
     "alt": "A modern three story townhome with dark brick, cedar siding, black framed windows and a rooftop deck"},
]

AGENTS = {
    "ilsa": {"name": "Ilsa Brandvold", "role": "Managing broker and owner", "img": "agent-ilsa",
             "alt": "Ilsa Brandvold, managing broker, on the front porch of a brick home"},
    "tobias": {"name": "Tobias Hallgren", "role": "Buyer's agent", "img": "agent-tobias",
               "alt": "Tobias Hallgren, buyer's agent, on a tree lined Denver sidewalk"},
    "nia": {"name": "Nia Abernethy", "role": "Listing agent", "img": "agent-nia",
            "alt": "Nia Abernethy, listing agent, in a sunlit living room"},
}

HOOD = {h["slug"]: h for h in HOODS}


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/",
            "logo": f"{BASE}/img/og.jpg", "telephone": "+1-720-555-0164", "foundingDate": str(YEAR_FOUNDED),
            "founder": {"@type": "Person", "name": "Ilsa Brandvold", "jobTitle": "Managing broker"}}


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "RealEstateAgent", "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
        "telephone": "+1-720-555-0164", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": f"{h['name']}, Denver, Colorado"} for h in HOODS],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:30", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"], "opens": "10:00", "closes": "16:00"}],
        "parentOrganization": {"@id": f"{BASE}/#org"},
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/",
            "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


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
<meta name="theme-color" content="#122341">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hepta+Slab:wght@400..700&amp;family=Figtree:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def brand_html():
    return f'<a class="brand" href="index.html" aria-label="{BRAND}, home">{MARK}<span class="brand-name"><b>Pikewell</b><span>Real Estate</span></span></a>'


def header(current=""):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    hood_dd = "".join(f'<li><a href="{h["slug"]}.html">{h["name"]}</a></li>' for h in HOODS)
    return f'''<header class="site-header">
<div class="topbar"><div class="wrap"><span class="tb-left">Denver homes, neighborhood by neighborhood. Licensed in Colorado.</span><span>Call or text <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<div class="navbar"><div class="wrap">
{brand_html()}
<nav class="nav" aria-label="Main">
<ul>
<li><a class="nav-link" href="buy.html"{cur("buy")}>Buy</a></li>
<li><a class="nav-link" href="sell.html"{cur("sell")}>Sell</a></li>
<li><a class="nav-link" href="neighborhoods.html"{cur("hoods")}>Neighborhoods{ic("chev")}</a><ul class="dropdown">{hood_dd}<li><a href="neighborhoods.html">All neighborhoods</a></li></ul></li>
<li><a class="nav-link" href="listings.html"{cur("listings")}>Listings</a></li>
<li><a class="nav-link" href="about.html"{cur("about")}>Our Team</a></li>
</ul>
<div class="nav-cta"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-gold" href="home-value.html">Home value</a>
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


def page_hero(eyebrow, h1, lede, crumb_items, img=None, alt="", points=None, buttons="", extra=""):
    pts = ""
    if points:
        pts = '<ul class="hero-points">' + "".join(f"<li>{ic('check')}<span>{p}</span></li>" for p in points) + "</ul>"
    frame = (f'<div class="frame"><img src="img/{img}.webp" alt="{alt}" fetchpriority="high" width="1600" height="904"></div>' if img else "")
    cls = "hero hero-page" + ("" if img else " plain")
    grid = f'<div class="grid"><div class="copy">' if img else '<div class="copy" style="max-width:820px">'
    close = f'</div>{frame}</div>' if img else '</div>'
    return f'''<section class="{cls}">
<div class="wrap">
{grid}
{crumbs(crumb_items)}
<span class="eyebrow">{eyebrow}</span>
<h1 class="h-xl">{h1}</h1>
<p class="lede">{lede}</p>
{extra}{f'<div class="btn-row">{buttons}</div>' if buttons else ""}{pts}
{close}
</div>
</section>
{'<div class="after-hero"></div>' if img else ""}
'''


def faq_block(title, qa, lead, bg=""):
    items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    return f'''<section class="section {bg}" aria-labelledby="faq-h">
<div class="wrap faq-layout">
<div><span class="eyebrow">Questions people ask</span><h2 class="h-lg" id="faq-h">{title}</h2><p class="small" style="margin-top:14px">{lead}</p></div>
<div class="acc">{items}</div>
</div>
</section>
'''


def review_card(text, who, where):
    stars = "".join(ic("star") for _ in range(5))
    return (f'<figure class="review reveal"><div class="stars" role="img" aria-label="5 out of 5 stars">{stars}</div>'
            f'<blockquote>{text}</blockquote><figcaption><span>{who}, {where}</span><span class="sample">Sample review</span></figcaption></figure>')


def contact(title='Tell us what you are <span class="accent">planning.</span>',
            lead="A few details and one of us will call or text within one business hour. No drip emails, no auto dialer.",
            intent=None, area=None, address=False, button="Send my details"):
    choices = "".join(
        f'<label class="choice"><input type="radio" name="intent" value="{v}"{" checked" if intent == v else ""}>{t}</label>'
        for v, t in [("buy", "Buying a home"), ("sell", "Selling a home"), ("value", "What's my home worth")])
    areas = "".join(f'<option value="{h["slug"]}"{" selected" if area == h["slug"] else ""}>{h["name"]}</option>' for h in HOODS)
    return f'''<section id="contact" class="section band" aria-labelledby="contact-h">
<div class="wrap form-layout">
<div>
<span class="eyebrow">Start here</span>
<h2 class="h-lg" id="contact-h">{title}</h2>
<p class="lead">{lead}</p>
<a class="band-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
<p class="small">Office hours: Monday to Friday 8:30 AM to 6 PM, weekends 10 AM to 4 PM. Showings any day by appointment.</p>
</div>
<form class="form" action="#contact" method="post" novalidate data-demo>
<fieldset><legend class="step">1. What brings you here</legend><div class="choice-grid">{choices}</div></fieldset>
<div class="fields">
<label class="field">Neighborhood<select name="area"><option value="any">Not sure yet</option>{areas}<option value="other">Somewhere else in metro Denver</option></select></label>
<label class="field">Timing<select name="when"><option>In the next 3 months</option><option>3 to 6 months</option><option>6 to 12 months</option><option>Just looking</option></select></label>
</div>
<p class="step" style="margin-top:6px">2. How to reach you</p>
<div class="fields">
{'<label class="field full">Property address<input type="text" name="address" autocomplete="street-address"></label>' if address else ""}<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Mobile phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="field">Email<input type="email" name="email" autocomplete="email"></label>
<label class="field">Preferred contact<select name="contact"><option>Text me</option><option>Call me</option><option>Email me</option></select></label>
</div>
<button class="btn btn-blue" type="submit">{button}</button>
<p class="form-note">We use your details to answer this request and nothing else. See our <a href="privacy.html">privacy page</a>.</p>
<div class="form-done" role="status">This is a demo site, so nothing was sent. On a live Pikewell site, this request goes to the agent on duty, who calls or texts within one business hour.</div>
</form>
</div>
</section>
'''


def footer():
    hoods = "".join(f'<li><a href="{h["slug"]}.html">{h["name"]}</a></li>' for h in HOODS)
    return f'''<footer class="site-footer">
{RIDGE}
<div class="wrap inner">
<div class="foot-top">{brand_html()}<p class="foot-tag">Denver homes, neighborhood by neighborhood.</p></div>
<div class="foot-cols">
<div><h2>Contact</h2><address>Denver, Colorado<br>Call or text <a href="tel:{TEL}">{PHONE}</a><br>Mon to Fri 8:30 AM to 6 PM<br>Weekends 10 AM to 4 PM</address></div>
<div><h2>Neighborhoods</h2><ul>{hoods}</ul></div>
<div><h2>Buy and sell</h2><ul><li><a href="buy.html">Buying with Pikewell</a></li><li><a href="sell.html">Selling with Pikewell</a></li><li><a href="home-value.html">What is my home worth</a></li><li><a href="listings.html">Current listings</a></li></ul></div>
<div><h2>Pikewell</h2><ul><li><a href="about.html">Our team</a></li><li><a href="neighborhoods.html">Neighborhood guides</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="index.html?intent=buy#contact">Contact us</a></li></ul></div>
</div>
<div class="foot-base"><span>Licensed by the Colorado Division of Real Estate. Equal Housing Opportunity. © 2026 {BRAND}.</span><span>A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Pikewell is a fictional brokerage, and its listings are samples.</span></div>
</div>
</footer>
<div class="mobile-bar"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-gold" href="home-value.html">Home value</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, desc, schemas, current, body):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
