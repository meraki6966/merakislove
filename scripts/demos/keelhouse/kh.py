"""Shared layout pieces for the Keelhouse Home Services demo.

Keelhouse is a fictional contractor. Cities and neighborhoods are real; the
business, its people, phone number, prices and reviews are demo content and
the footer of every page says so.
"""
import json
from html import escape

BRAND = "Keelhouse Home Services"
SHORT = "Keelhouse"
PHONE = "(614) 555-0142"            # 555-01xx is reserved for fiction
TEL = "+16145550142"
BASE = "https://merakislove.com/demos/keelhouse"
FOUNDER = "Darnell Hayes"
YEAR_FOUNDED = 2009

# ---------------------------------------------------------------- icons
_P = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "wrench": '<path d="M14.5 5.5a4 4 0 0 0 5 5L12 18l-3 3-3-3 3-3 7.5-7.5"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "flame": '<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 0 1-10 0c0-2.5 1.5-4 2.5-5 .3 1.8 1.2 2.8 2.2 3.2C11.3 9 11.5 6 12 3z"/>',
    "snow": '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M9.5 4.5 12 6l2.5-1.5M9.5 19.5 12 18l2.5 1.5"/>',
    "bolt": '<path d="M13 3 5 13h6l-1 8 8-10h-6z"/>',
    "tank": '<rect x="7" y="3" width="10" height="16" rx="3"/><path d="M9 21h6M12 8v4"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "upload": '<path d="M12 16V4M7 9l5-5 5 5M5 20h14"/>',
    "house": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
}
# Keel mark: a house roofline over a waterline, with a keel below.
KEEL = ('<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
        'stroke-linejoin="round" aria-hidden="true"><path d="M8 18 20 8l12 10"/><path d="M11 16v8h18v-8"/>'
        '<path d="M5 24h30"/><path d="M14 24l6 10 6-10"/></svg>')


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    fill = ' fill="currentColor"' if name == "star" else ' fill="none"'
    return (f'<svg{c} viewBox="0 0 24 24"{fill} stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# ---------------------------------------------------------------- site map
SERVICES = [
    {"slug": "plumbing", "name": "Plumbing", "short": "Leaks, drains, water heaters, sump pumps", "visit": "$95", "img": "svc-plumbing"},
    {"slug": "heating-cooling", "name": "Heating &amp; Cooling", "plain": "Heating and Cooling", "short": "Furnaces, AC, heat pumps, tune ups", "visit": "$120", "img": "svc-hvac"},
    {"slug": "electrical", "name": "Electrical", "short": "Panels, lighting, EV chargers, surge protection", "visit": "$110", "img": "svc-electrical"},
]
CITIES = [
    {"slug": "columbus-oh", "name": "Columbus", "hoods": "German Village, Clintonville, Short North, Victorian Village", "drive": "Home shop and dispatch"},
    {"slug": "dublin-oh", "name": "Dublin", "hoods": "Historic Dublin, Bridge Park, Muirfield Village, Ballantrae", "drive": "About 20 min from dispatch"},
    {"slug": "westerville-oh", "name": "Westerville", "hoods": "Uptown Westerville, Alum Creek, Genoa Township", "drive": "About 25 min from dispatch"},
    {"slug": "grove-city-oh", "name": "Grove City", "hoods": "Town Center, Beulah Park, Pinnacle", "drive": "About 20 min from dispatch"},
]
PROJECTS = [
    {"slug": "panel-upgrade-dublin-oh", "trade": "Electrical", "city": "Dublin", "city_slug": "dublin-oh", "img": "proj-panel",
     "title": "200 amp panel upgrade in a 1990s Muirfield Village home"},
    {"slug": "galvanized-repipe-westerville-oh", "trade": "Plumbing", "city": "Westerville", "city_slug": "westerville-oh", "img": "proj-repipe",
     "title": "Galvanized water line replacement in an Uptown Westerville home"},
    {"slug": "heat-pump-install-grove-city-oh", "trade": "Heating &amp; Cooling", "city": "Grove City", "city_slug": "grove-city-oh", "img": "proj-heatpump",
     "title": "Dual fuel heat pump install in a Grove City ranch"},
]
NEEDS = [("leak", "drop", "Leak or clog"), ("no-heat", "flame", "No heat"), ("no-cooling", "snow", "AC not cooling"),
         ("water-heater", "tank", "Water heater"), ("electrical", "bolt", "Breaker or outlet"), ("install", "plus", "Install or upgrade")]


# ---------------------------------------------------------------- schema
def business_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["Plumber", "HVACBusiness", "Electrician"],
        "@id": f"{BASE}/#business",
        "name": BRAND,
        "url": f"{BASE}/",
        "telephone": "+1-614-555-0142",
        "image": f"{BASE}/img/og.jpg",
        "priceRange": "$$",
        "foundingDate": str(YEAR_FOUNDED),
        "address": {"@type": "PostalAddress", "addressLocality": "Columbus", "addressRegion": "OH", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": f"{c['name']}, Ohio"} for c in CITIES],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "07:00", "closes": "19:00"}],
        "founder": {"@type": "Person", "name": FOUNDER, "jobTitle": "Founder and master plumber"},
    }


def faq_schema(qa):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qa]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(n), "item": f"{BASE}/{href}" if href else f"{BASE}/"}
                                for i, (n, href) in enumerate(items)]}


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


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
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(strip(title), quote=True)}">
<meta property="og:description" content="{escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E141B">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&amp;family=Public+Sans:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def header(current=""):
    def cur(key):
        return ' aria-current="page"' if key == current else ""
    svc_dd = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    city_dd = "".join(f'<li><a href="{c["slug"]}.html">{c["name"]}</a></li>' for c in CITIES)
    return f'''<header class="site-header">
<div class="topbar"><div class="wrap"><span class="tb-left">Licensed plumbing, heating and electrical in Central Ohio</span><span class="tb-right"><span>Emergency line, 24/7</span><a href="tel:{TEL}">{PHONE}</a></span></div></div>
<div class="navbar"><div class="wrap">
<a class="brand" href="index.html" aria-label="{BRAND}, home">{KEEL}<span class="brand-name"><b>KEELHOUSE</b><span>HOME SERVICES</span></span></a>
<nav class="nav" aria-label="Main">
<ul>
<li><a class="nav-link" href="services.html"{cur("services")}>Services{ic("chev")}</a><ul class="dropdown">{svc_dd}</ul></li>
<li><a class="nav-link" href="service-areas.html"{cur("areas")}>Service Areas{ic("chev")}</a><ul class="dropdown">{city_dd}</ul></li>
<li><a class="nav-link" href="projects.html"{cur("projects")}>Projects</a></li>
<li><a class="nav-link" href="how-we-work.html"{cur("how")}>How We Work</a></li>
</ul>
<div class="nav-cta"><a class="btn btn-ghost" href="#book">Book a visit</a><a class="btn btn-copper" href="tel:{TEL}">{ic("phone")}Call now</a>
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


def page_hero(img, eyebrow, h1, lede, crumb_items, alt, extra="", even=False, btns=True):
    b = f'<div class="btn-row"><a class="btn btn-copper" href="#book">Book a visit</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}{PHONE}</a></div>' if btns else ""
    return f'''<section class="hero hero-page{" hero-even" if even else ""}">
<img class="hero-img" src="img/{img}.webp" alt="{alt}" fetchpriority="high">
<div class="hero-inner"><div class="wrap hero-grid">
<div class="hero-copy">
{crumbs(crumb_items)}
<span class="eyebrow">{eyebrow}</span>
<h1 class="h-xl">{h1}</h1>
<p class="lede">{lede}</p>
{b}
</div>
{extra}
</div></div>
</section>
'''


def angle(top, bottom, down=False):
    return f'<div class="angle{" down" if down else ""}" style="background:{top}"><div style="background:{bottom}"></div></div>\n'


def faq_block(title, qa, lead, bg="paper"):
    items = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}{ic("plus")}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))
    return f'''<section class="section {bg}" aria-labelledby="faq-h">
<div class="wrap faq-layout">
<div><span class="eyebrow">Frequently asked</span><h2 class="h-lg" id="faq-h">{title}</h2><p class="small">{lead}</p></div>
<div class="acc">{items}</div>
</div>
</section>
'''


def review_card(text, who, where):
    stars = "".join(ic("star") for _ in range(5))
    return (f'<figure class="review reveal"><div class="stars" aria-label="5 out of 5 stars">{stars}</div>'
            f'<blockquote>{text}</blockquote><figcaption><span>{who}  ·  {where}</span><span class="sample">Sample review</span></figcaption></figure>')


def booking(title="Tell us what the house is <span class=\"accent\">doing.</span>", lead="A photo of the leak, the panel or the thermostat helps the tech bring the right parts the first time.", preset=None):
    needs = "".join(
        f'<label class="need"><input type="checkbox" name="need" value="{v}"{" checked" if preset == v else ""}>{t}</label>' for v, _, t in NEEDS)
    return f'''<section id="book" class="section dark grid-bg" aria-labelledby="book-h">
<div class="wrap book-layout">
<div>
<span class="eyebrow">Book a visit</span>
<h2 class="h-lg" id="book-h">{title}</h2>
<p class="small" style="font-size:16px;max-width:400px">{lead}</p>
<a class="book-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
<p class="small">Office Mon to Sat, 7 AM to 7 PM. Emergency line 24/7.</p>
</div>
<form class="book-form" action="#book" method="post" novalidate>
<fieldset><legend class="step">1  ·  What's happening</legend><div class="need-grid">{needs}</div></fieldset>
<div class="fields">
<label class="field">Property type<select name="property"><option>Single family home</option><option>Townhome or condo</option><option>Rental property</option><option>Small business</option></select></label>
<label class="field">How soon<select name="when"><option>Today, it's urgent</option><option>This week</option><option>Planning ahead</option></select></label>
</div>
<label class="field">Describe it<textarea name="details" rows="3"></textarea></label>
<label class="upload">{ic("upload")}Add photos (optional)<input type="file" name="photos" accept="image/*" multiple></label>
<p class="step">2  ·  Where and who</p>
<div class="fields">
<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="field">ZIP code<input type="text" name="zip" inputmode="numeric" autocomplete="postal-code"></label>
<label class="field">Email (optional)<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn btn-copper" type="submit">Request a visit</button>
<p class="form-note">We text to confirm a window. Your number is only used for this visit.</p>
<div class="form-done" role="status">This is a demo site, so nothing was sent. On a live Keelhouse site, this request lands in the office inbox and the customer gets a text with an arrival window.</div>
</form>
</div>
</section>
'''


def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    cty = "".join(f'<li><a href="{c["slug"]}.html">{c["name"]}</a></li>' for c in CITIES)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-top"><a class="brand" href="index.html" aria-label="{BRAND}, home">{KEEL}<span class="brand-name"><b>KEELHOUSE</b><span>HOME SERVICES</span></span></a><p class="foot-tag">Kept running. Kept safe.</p></div>
<div class="foot-cols">
<div><h2>Contact</h2><address>Columbus, Ohio<br><a href="tel:{TEL}">{PHONE}</a><br>Mon to Sat, 7 AM to 7 PM<br>Emergency line 24/7</address></div>
<div><h2>Services</h2><ul>{svc}<li><a href="services.html">All services</a></li></ul></div>
<div><h2>Service areas</h2><ul>{cty}<li><a href="service-areas.html">All areas</a></li></ul></div>
<div><h2>Company</h2><ul><li><a href="how-we-work.html">How we work</a></li><li><a href="projects.html">Projects</a></li><li><a href="how-we-work.html#crew">The crew</a></li><li><a href="#book">Book a visit</a></li></ul></div>
</div>
<div class="foot-base"><span>Ohio contractor license on file. Insured. © 2026 {BRAND}.</span><span>A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Keelhouse is a fictional business.</span></div>
</div>
</footer>
<a class="float-call" href="tel:{TEL}" aria-label="Call {SHORT}">{ic("phone")}</a>
<div class="mobile-bar"><a class="btn btn-outline" href="tel:{TEL}">{ic("phone")}Call now</a><a class="btn btn-copper" href="#book">Book a visit</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, desc, schemas, current, body, og_img="og.jpg"):
    return head(title, desc, path, schemas, og_img) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
