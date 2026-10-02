"""Shared layout pieces for the Saltbrush Pool Care demo.

Saltbrush is a fictional company. Phoenix, its neighborhoods, the Arizona
pool barrier statute (A.R.S. 36-1681), the Registrar of Contractors R-6
classification and the monsoon season dates are real, checked in October 2026.
The company, its people, phone number, prices and reviews are demo content,
and the footer of every page says so.
"""
import json
import re
from html import escape

BRAND = "Saltbrush Pool Care"
SHORT = "Saltbrush"
PHONE = "(602) 555-0118"            # 555-01xx is reserved for fiction
TEL = "+16025550118"
BASE = "https://merakislove.com/demos/saltbrush"
YEAR_FOUNDED = 2014

# ---------------------------------------------------------------- icons
_P = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "drop": '<path d="M12 3c3.5 4.2 6 7.4 6 10.5a6 6 0 0 1-12 0C6 10.400 8.500 7.200 12 3z"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2.500M12 19.500V22M2 12h2.500M19.500 12H22M4.900 4.900l1.800 1.800M17.300 17.300l1.800 1.800M4.900 19.100l1.800-1.800M17.300 6.700l1.800-1.800"/>',
    "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    "cal": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
}
# Mark: a sun sitting on a waterline.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<rect width="44" height="44" rx="12" fill="#0B3C49"/>'
        '<circle cx="22" cy="19" r="8" fill="#F2B33D"/>'
        '<path d="M0 24c5.500-4 9.500 4 15 0s9.500 4 15 0 9.500 2 14 0v20H0z" fill="#17A0AA"/>'
        '<path d="M0 31c5.500-4 9.500 4 15 0s9.500 4 15 0 9.500 2 14 0v13H0z" fill="#0E7C86"/></svg>')
WAVE = ('<svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
        '<path d="M0 30c120-40 240 40 360 0s240 40 360 0 240 40 360 0 240 40 360 0v30H0z"/></svg>')


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    fill = ' fill="currentColor"' if name == "star" else ' fill="none"'
    return (f'<svg{c} viewBox="0 0 24 24"{fill} stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# ---------------------------------------------------------------- site data
SERVICES = [
    {"slug": "weekly-pool-service", "name": "Weekly pool service", "img": "brushing", "need": "weekly",
     "short": "The same technician every week: test, balance, brush, skim, empty baskets, check equipment, send a report.",
     "from": "$155", "unit": "a month, chemicals included",
     "alt": "A Saltbrush technician brushing the tile line of a backyard pool in late afternoon light"},
    {"slug": "green-pool-cleanup", "name": "Green pool cleanup", "img": "green", "need": "green",
     "short": "From green to swimmable, usually in three to five days, with the filter cleaned along the way.",
     "from": "$295", "unit": "and up, by pool size",
     "alt": "A neglected backyard pool with opaque green water and dry leaves floating on the surface"},
    {"slug": "equipment-repair", "name": "Equipment repair", "img": "equipment", "need": "repair",
     "short": "Pumps, filters, salt cells, automation, valves and leaks at the pad, diagnosed with a written price first.",
     "from": "$89", "unit": "diagnosis, credited to the repair",
     "alt": "A tidy pool equipment pad with a variable speed pump, a cartridge filter and white plumbing against a stucco wall"},
    {"slug": "filter-cleaning", "name": "Filter cleaning", "img": "filter", "need": "filter",
     "short": "Cartridge, D.E. and sand filters taken apart, cleaned and inspected, with photos of what we found.",
     "from": "$95", "unit": "per cleaning",
     "alt": "Gloved hands rinsing a pleated pool filter cartridge with a hose on a gravel yard"},
]
SVC = {s["slug"]: s for s in SERVICES}

AREAS = [
    {"slug": "arcadia", "name": "Arcadia", "img": "arcadia", "zip": "85018", "day": "Tuesdays and Fridays",
     "line": "Older diving pools under citrus trees, with leaves and blossoms in every basket",
     "alt": "A ranch home backyard in Arcadia with a lawn, citrus trees, a rectangular pool and a red rock mountain behind"},
    {"slug": "ahwatukee", "name": "Ahwatukee", "img": "ahwatukee", "zip": "85044, 85045, 85048", "day": "Mondays and Thursdays",
     "line": "Pebble pools and spas below South Mountain, where the dust arrives first",
     "alt": "A pebble finish pool and raised spa behind a tile roof home, with desert mountain slopes rising behind the wall"},
    {"slug": "tempe", "name": "Tempe", "img": "tempe", "zip": "85281 to 85284", "day": "Wednesdays",
     "line": "Mid century block homes, rentals near campus and pools that have seen a lot of summers",
     "alt": "A small kidney shaped pool behind a mid century block home with tall palm trees and a shade sail"},
]
AREA = {a["slug"]: a for a in AREAS}

# Balanced water ranges printed on the report card. Sample readings sit inside them.
READINGS = [
    ("Free chlorine", "3.0", "ppm", "2 to 4"),
    ("pH", "7.5", "", "7.4 to 7.6"),
    ("Total alkalinity", "90", "ppm", "80 to 120"),
    ("Calcium hardness", "340", "ppm", "200 to 400"),
    ("Cyanuric acid", "45", "ppm", "30 to 50"),
    ("Salt", "3,200", "ppm", "2,700 to 3,400"),
]

PEOPLE = [
    ("NV", "Nico Velarde", "Owner and lead technician",
     "Nico started Saltbrush in 2014 with one truck and forty pools in central Phoenix. He holds the company's Arizona R-6 pool service and repair license and still runs a Friday route."),
    ("TO", "Tamsin Ortega-Bell", "Service manager",
     "Tamsin builds the routes, reads every weekly report before it goes out, and is the person who calls when a reading looks wrong. She is a Certified Pool Operator."),
    ("WO", "Wendell Okafor", "Repair lead",
     "Wendell handles pumps, filters, salt systems and automation. He writes the price down before he picks up a wrench, and he keeps the old part so you can see it."),
]


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/",
            "logo": f"{BASE}/img/og.jpg", "telephone": "+1-602-555-0118", "foundingDate": str(YEAR_FOUNDED),
            "founder": {"@type": "Person", "name": "Nico Velarde", "jobTitle": "Owner"}}


def business_schema():
    return {
        "@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
        "telephone": "+1-602-555-0118", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Phoenix", "addressRegion": "AZ", "postalCode": "85016", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": n} for n in ["Phoenix, Arizona", "Arcadia, Phoenix", "Ahwatukee, Phoenix", "Tempe, Arizona"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "06:00", "closes": "16:00"}],
        "parentOrganization": {"@id": f"{BASE}/#org"},
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/",
            "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


def service_schema(name, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": f"{BASE}/{path}",
            "provider": {"@id": f"{BASE}/#business"}, "areaServed": {"@type": "City", "name": "Phoenix"}}


def article_schema(headline, desc, path):
    return {"@context": "https://schema.org", "@type": "Article", "headline": headline, "description": desc, "url": f"{BASE}/{path}",
            "author": {"@id": f"{BASE}/#org"}, "publisher": {"@id": f"{BASE}/#org"}, "dateModified": "2026-10-02"}


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
def head(title, desc, path, schemas):
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
<meta property="og:image" content="{BASE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B3C49">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&amp;family=Albert+Sans:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def brand_html():
    return f'<a class="brand" href="index.html" aria-label="{BRAND}, home">{MARK}<span class="brand-name"><b>Saltbrush</b><span>Pool Care</span></span></a>'


def header(current=""):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    svc_dd = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<header class="site-header">
<div class="wrap bar">
{brand_html()}
<nav class="nav" aria-label="Main">
<ul>
<li><a class="nav-link" href="services.html"{cur("services")}>Services{ic("chev")}</a><ul class="dropdown">{svc_dd}<li><a href="services.html">All services</a></li></ul></li>
<li><a class="nav-link" href="monsoon-pool-care.html"{cur("monsoon")}>Monsoon care</a></li>
<li><a class="nav-link" href="pool-safety.html"{cur("safety")}>Pool safety</a></li>
<li><a class="nav-link" href="pricing.html"{cur("pricing")}>Pricing</a></li>
<li><a class="nav-link" href="about.html"{cur("about")}>About</a></li>
</ul>
<div class="nav-cta"><a class="nav-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a><a class="btn btn-clay" href="index.html#contact">Get a quote</a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-label="Open menu">{ic("menu")}</button></div>
</nav>
</div>
</header>
'''


def crumbs(items):
    out = []
    for i, (n, href) in enumerate(items):
        if i < len(items) - 1:
            out.append(f'<a href="{href or "index.html"}">{n}</a><span aria-hidden="true">›</span>')
        else:
            out.append(f'<span aria-current="page">{n}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(out)}</nav>'


def page_hero(tag, h1, lede, crumb_items, img=None, alt="", points=None, buttons=""):
    pts = ""
    if points:
        pts = '<ul class="hero-points">' + "".join(f"<li>{ic('check')}<span>{p}</span></li>" for p in points) + "</ul>"
    copy = f'''<div class="copy">
{crumbs(crumb_items)}
<p class="tag">{tag}</p>
<h1 class="h-xl">{h1}</h1>
<p class="lede">{lede}</p>
{f'<div class="btn-row">{buttons}</div>' if buttons else ""}{pts}
</div>'''
    if img:
        inner = f'<div class="grid">{copy}<div class="frame"><img src="img/{img}.webp" alt="{alt}" fetchpriority="high" width="1600" height="1200"></div></div>'
    else:
        inner = f'<div class="solo">{copy}</div>'
    return f'<section class="hero-page"><div class="wrap">{inner}</div>{WAVE}</section>\n'


def water_card(title="This week at a sample pool", note="Sample report. Every weekly visit ends with one like it."):
    rows = "".join(
        f'<div class="read"><span class="k">{k}</span><span class="v">{v}<small>{u}</small></span><span class="r">Target {r}</span></div>'
        for k, v, u, r in READINGS)
    return (f'<aside class="water" aria-label="Sample water test report"><div class="water-top"><span>{ic("drop")}{title}</span><b>Balanced</b></div>'
            f'<div class="reads">{rows}</div><p class="water-note">{note}</p></aside>')


def faq_block(title, qa, lead, bg=""):
    items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    return f'''<section class="section {bg}" aria-labelledby="faq-h">
<div class="wrap faq-layout">
<div><p class="tag">Questions owners ask</p><h2 class="h-lg" id="faq-h">{title}</h2><p class="small" style="margin-top:14px">{lead}</p></div>
<div class="acc">{items}</div>
</div>
</section>
'''


def review_card(text, who, where):
    stars = "".join(ic("star") for _ in range(5))
    return (f'<figure class="review reveal"><div class="stars" role="img" aria-label="5 out of 5 stars">{stars}</div>'
            f'<blockquote>{text}</blockquote><figcaption><span>{who}, {where}</span><span class="sample">Sample review</span></figcaption></figure>')


def contact(title="Tell us about <span class=\"accent\">your pool.</span>",
            lead="Four quick questions and we send a written quote the same business day. No one comes to the gate until you say so.",
            need=None):
    opts = [("weekly", "Weekly service"), ("green", "My pool is green"), ("repair", "Something is broken"), ("filter", "Filter cleaning")]
    choices = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}"{" checked" if need == v else ""}>{t}</label>' for v, t in opts)
    return f'''<section id="contact" class="section deep" aria-labelledby="contact-h">
<div class="wrap form-layout">
<div>
<p class="tag">Get a quote</p>
<h2 class="h-lg" id="contact-h">{title}</h2>
<p class="lead">{lead}</p>
<a class="band-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
<p class="small">Routes run Monday to Friday from 6 AM. The office answers 7 AM to 4 PM, Arizona time.</p>
</div>
<form class="form" action="#contact" method="post" novalidate data-demo>
<fieldset><legend class="step">1. What do you need</legend><div class="choice-grid">{choices}</div></fieldset>
<p class="step">2. About the pool</p>
<div class="fields">
<label class="field">ZIP code<input type="text" name="zip" inputmode="numeric" autocomplete="postal-code"></label>
<label class="field">Pool type<select name="type"><option>Chlorine</option><option>Salt</option><option>Not sure</option></select></label>
</div>
<p class="step">3. How to reach you</p>
<div class="fields">
<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="field full">Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn btn-clay" type="submit">Send my quote request</button>
<p class="form-note">Please leave gate codes and alarm codes out of this form. We collect those by phone after you sign up. See our <a href="privacy.html">privacy page</a>.</p>
<div class="form-done" role="status">This is a demo site, so nothing was sent. On a live Saltbrush site, this request reaches the office and a written quote comes back the same business day.</div>
</form>
</div>
</section>
'''


def footer():
    svcs = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    return f'''<footer class="site-footer">
{WAVE}
<div class="wrap">
<div class="foot-top">{brand_html()}<p class="foot-tag">Clear water every week, and a report that proves it.</p></div>
<div class="foot-cols">
<div><h2>Contact</h2><address>Phoenix, AZ 85016<br><a href="tel:{TEL}">{PHONE}</a><br>Routes Mon to Fri from 6 AM<br>Office 7 AM to 4 PM</address></div>
<div><h2>Services</h2><ul>{svcs}<li><a href="pricing.html">Pricing</a></li></ul></div>
<div><h2>Guides</h2><ul><li><a href="monsoon-pool-care.html">Monsoon and dust storm care</a></li><li><a href="pool-safety.html">Arizona pool barrier law</a></li><li><a href="service-reports.html">Your weekly report</a></li></ul></div>
<div><h2>Where we work</h2><ul>{areas}<li><a href="about.html">About Saltbrush</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
</div>
<div class="foot-base"><span>© 2026 {BRAND}. Licensed for residential pool service and repair in Arizona, ROC classification R-6.</span><span>A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Saltbrush is a fictional company, and its prices are samples.</span></div>
</div>
</footer>
<div class="mobile-bar"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-clay" href="index.html#contact">Get a quote</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, desc, schemas, current, body):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
