"""Shared layout pieces for the Tessel Dental demo.

Tessel Dental is a fictional practice. Charlotte, its neighborhoods, roads and
light rail stations are real; the practice, its dentists, phone number, prices
and reviews are demo content, and the footer of every page says so.
"""
import json
import re
from html import escape

BRAND = "Tessel Dental"
PHONE = "(704) 555-0137"            # 555-01xx is reserved for fiction
TEL = "+17045550137"
BASE = "https://merakislove.com/demos/tessel"
YEAR_FOUNDED = 2016

# ---------------------------------------------------------------- icons
_P = {
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "lock": '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "alert": '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17v.5"/>',
    "card": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/>',
    "train": '<rect x="6" y="3" width="12" height="13" rx="3"/><path d="M6 11h12M9 20l-2 1M15 20l2 1M9 16l-1 4M15 16l1 4"/>',
    "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M4 16h16v3H4z"/><circle cx="8" cy="13" r="1"/><circle cx="16" cy="13" r="1"/>',
}
# Mark: four rounded tiles, the way a mosaic starts.
MARK = ('<svg viewBox="0 0 40 40" aria-hidden="true" focusable="false">'
        '<rect x="4" y="4" width="15" height="15" rx="4" fill="#2B6B62"/>'
        '<rect x="21" y="4" width="15" height="15" rx="4" fill="#8CC5B8"/>'
        '<rect x="4" y="21" width="15" height="15" rx="4" fill="#8CC5B8"/>'
        '<rect x="21" y="21" width="15" height="15" rx="4" fill="#E6A788"/></svg>')
TILES = '<div class="tiles" aria-hidden="true">' + "<span></span>" * 9 + "</div>"


def ic(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    fill = ' fill="currentColor"' if name == "star" else ' fill="none"'
    return (f'<svg{c} viewBox="0 0 24 24"{fill} stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{_P[name]}</svg>')


# ---------------------------------------------------------------- site data
SERVICES = [
    {"slug": "cleanings-exams", "name": "Cleanings &amp; Exams", "plain": "Cleanings and Exams", "short": "Checkups, x-rays and cleanings for adults and kids",
     "tag": "Most visits start here", "img": "svc-cleaning", "reason": "cleaning"},
    {"slug": "cosmetic-dentistry", "name": "Cosmetic Dentistry", "short": "Whitening, bonding, veneers and clear aligners",
     "tag": "Free consult", "img": "svc-cosmetic", "reason": "cosmetic"},
    {"slug": "dental-implants", "name": "Dental Implants", "short": "Single teeth to full arches, planned with a 3D scan",
     "tag": "From $4,300", "img": "svc-implants", "reason": "implants"},
    {"slug": "emergency-dentist", "name": "Emergency Dentist", "short": "Same day visits for pain, breaks and swelling",
     "tag": "Same day", "img": "svc-emergency", "reason": "pain"},
]

# Hours keyed by weekday, Sunday = 0, in Charlotte time.
OFFICES = [
    {"slug": "south-end", "name": "South End", "img": "office-south-end", "zip": "28203", "dentist": "Dr. Leena Sethuraman",
     "where": "On the Rail Trail in South End, a short walk from the East/West Blvd light rail station",
     "getting": "Ride the LYNX Blue Line to East/West Blvd and walk north along the Rail Trail. Driving, use the garage behind the building; the front desk validates two hours.",
     "parking": "Garage behind the building, two hours validated",
     "transit": "LYNX Blue Line, East/West Blvd station",
     "serves": "South End, Dilworth, Wilmore, Myers Park, Sedgefield",
     "hours": {"1": ["07:30", "17:00"], "2": ["07:30", "17:00"], "3": ["07:30", "17:00"], "4": ["07:30", "17:00"], "5": ["07:30", "14:00"]}},
    {"slug": "ballantyne", "name": "Ballantyne", "img": "office-ballantyne", "zip": "28277", "dentist": "Dr. Theo Marchbanks",
     "where": "Off Ballantyne Commons Parkway, a few minutes from the I-485 exit at Johnston Road",
     "getting": "From I-485, take the Johnston Road exit south and turn onto Ballantyne Commons Parkway. Parking is free and right at the door.",
     "parking": "Free lot at the front door",
     "transit": "Five minutes from I-485 at Johnston Road",
     "serves": "Ballantyne, Blakeney, Piper Glen, Marvin, Fort Mill",
     "hours": {"1": ["08:00", "18:00"], "2": ["08:00", "18:00"], "3": ["08:00", "18:00"], "4": ["08:00", "18:00"], "6": ["08:00", "13:00"]}},
]
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

REASONS = [("cleaning", "Cleaning and exam"), ("pain", "Tooth pain or emergency"), ("cosmetic", "Whitening or cosmetic"),
           ("implants", "Implant consult"), ("child", "Child's visit"), ("other", "Something else")]

CARRIERS = ["Delta Dental PPO", "Cigna DPPO", "MetLife PDP", "Aetna Dental PPO", "Guardian", "Blue Cross NC Dental Blue", "United Concordia", "Ameritas"]


def fmt_time(t):
    h, m = map(int, t.split(":"))
    ap = "PM" if h >= 12 else "AM"
    h = h % 12 or 12
    return f"{h}:{m:02d} {ap}" if m else f"{h} {ap}"


def hours_summary(o):
    """Compact human hours, e.g. 'Mon to Thu 7:30 AM to 5 PM, Fri 7:30 AM to 2 PM'."""
    groups = []
    for d in range(7):
        h = o["hours"].get(str(d))
        if not h:
            continue
        if groups and groups[-1][2] == h and groups[-1][1] == d - 1:
            groups[-1][1] = d
        else:
            groups.append([d, d, h])
    short = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    out = []
    for a, b, h in groups:
        days = short[a] if a == b else f"{short[a]} to {short[b]}"
        out.append(f"{days} {fmt_time(h[0])} to {fmt_time(h[1])}")
    return ", ".join(out)


def hours_table(o):
    rows = ""
    for d in [1, 2, 3, 4, 5, 6, 0]:
        h = o["hours"].get(str(d))
        val = f"{fmt_time(h[0])} to {fmt_time(h[1])}" if h else "Closed"
        rows += f'<tr data-day="{d}"><th scope="row">{DAYS[d]}</th><td>{val}</td></tr>'
    return f'<table class="hours"><caption class="sr-only">{o["name"]} office hours</caption>{rows}</table>'


def status_line(o):
    return (f'<span class="status" data-hours=\'{json.dumps(o["hours"])}\'><span class="dot"></span>'
            f'<span class="status-text">{hours_summary(o)}</span></span>')


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def office_schema(o):
    spec = []
    for d, (a, b) in o["hours"].items():
        spec.append({"@type": "OpeningHoursSpecification", "dayOfWeek": DAYS[int(d)], "opens": a, "closes": b})
    return {
        "@context": "https://schema.org", "@type": "Dentist", "@id": f"{BASE}/{o['slug']}.html#office",
        "name": f"{BRAND} {o['name']}", "url": f"{BASE}/{o['slug']}.html", "telephone": "+1-704-555-0137",
        "image": f"{BASE}/img/{o['img']}.webp", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Charlotte", "addressRegion": "NC", "postalCode": o["zip"], "addressCountry": "US"},
        "openingHoursSpecification": spec,
        "parentOrganization": {"@id": f"{BASE}/#org"},
        "currenciesAccepted": "USD", "paymentAccepted": "Cash, Credit Card, Dental Insurance, Financing",
    }


def org_schema():
    return {
        "@context": "https://schema.org", "@type": "MedicalOrganization", "@id": f"{BASE}/#org",
        "name": BRAND, "url": f"{BASE}/", "telephone": "+1-704-555-0137", "logo": f"{BASE}/img/og.jpg",
        "foundingDate": str(YEAR_FOUNDED), "medicalSpecialty": "Dentistry",
        "founder": {"@type": "Person", "name": "Leena Sethuraman", "honorificPrefix": "Dr.", "jobTitle": "General Dentist"},
        "subOrganization": [{"@id": f"{BASE}/{o['slug']}.html#office"} for o in OFFICES],
        "areaServed": {"@type": "City", "name": "Charlotte, North Carolina"},
    }


def faq_schema(qa):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qa]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": strip(n), "item": f"{BASE}/{href}" if href else f"{BASE}/"}
                                for i, (n, href) in enumerate(items)]}


def service_schema(name, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": strip(name), "description": desc, "url": f"{BASE}/{path}",
            "serviceType": strip(name), "provider": {"@id": f"{BASE}/#org"},
            "areaServed": {"@type": "City", "name": "Charlotte, North Carolina"}}


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
<meta name="robots" content="noindex">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{escape(strip(title), quote=True)}">
<meta property="og:description" content="{escape(desc, quote=True)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14302A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;600;700&amp;family=Red+Hat+Text:wght@400;500;600&amp;display=swap">
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
    off_dd = "".join(f'<li><a href="{o["slug"]}.html">{o["name"]} office</a></li>' for o in OFFICES) + '<li><a href="myers-park.html">Myers Park patients</a></li>'
    return f'''<header class="site-header">
<div class="notice"><div class="wrap"><span class="tb-left">New patients welcome at both Charlotte offices. Same day emergency visits.</span><span>Call or text <a href="tel:{TEL}">{PHONE}</a></span></div></div>
<div class="navbar"><div class="wrap">
<a class="brand" href="index.html" aria-label="{BRAND}, home">{MARK}<span class="brand-name">Tessel <span>Dental</span></span></a>
<nav class="nav" aria-label="Main">
<ul>
<li><a class="nav-link" href="services.html"{cur("services")}>Services{ic("chev")}</a><ul class="dropdown">{svc_dd}<li><a href="services.html">All services</a></li></ul></li>
<li><a class="nav-link" href="offices.html"{cur("offices")}>Offices{ic("chev")}</a><ul class="dropdown">{off_dd}</ul></li>
<li><a class="nav-link" href="our-dentists.html"{cur("dentists")}>Our Dentists</a></li>
<li><a class="nav-link" href="insurance-financing.html"{cur("insurance")}>Insurance</a></li>
<li><a class="nav-link" href="new-patients.html"{cur("new")}>New Patients</a></li>
</ul>
<div class="nav-cta"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-sea" href="#book">Book online</a>
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


def page_hero(img, eyebrow, h1, lede, crumb_items, alt, points=None, reason=None, portrait=False, btns=True):
    q = f"?reason={reason}" if reason else ""
    b = (f'<div class="btn-row"><a class="btn btn-sea" href="{q}#book">Book online</a>'
         f'<a class="btn btn-line" href="tel:{TEL}">{ic("phone")}{PHONE}</a></div>') if btns else ""
    pts = ""
    if points:
        pts = '<ul class="hero-points">' + "".join(f"<li>{ic('check')}<span>{p}</span></li>" for p in points) + "</ul>"
    return f'''<section class="hero hero-page">
<div class="wrap hero-grid">
<div class="hero-copy">
{crumbs(crumb_items)}
<span class="eyebrow">{eyebrow}</span>
<h1 class="h-xl">{h1}</h1>
<p class="lede">{lede}</p>
{b}{pts}
</div>
<div class="hero-media{" portrait" if portrait else ""}"><div class="frame"><img src="img/{img}.webp" alt="{alt}" fetchpriority="high" width="1400" height="1041"></div>{TILES}</div>
</div>
</section>
'''


def faq_block(title, qa, lead, bg="white"):
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


def booking(title='Pick a time that <span class="accent">works for you.</span>',
            lead="Tell us what you need and which office is easier. We call or text within one business hour to confirm a time.",
            preset=None, office=None):
    reasons = "".join(
        f'<label class="reason"><input type="radio" name="reason" value="{v}"{" checked" if preset == v else ""}>{t}</label>' for v, t in REASONS)
    offs = "".join(f'<option value="{o["slug"]}"{" selected" if office == o["slug"] else ""}>{o["name"]}</option>' for o in OFFICES)
    carriers = "".join(f"<option>{c}</option>" for c in CARRIERS)
    return f'''<section id="book" class="section book" aria-labelledby="book-h">
<div class="wrap book-layout">
<div>
<span class="eyebrow">Book online</span>
<h2 class="h-lg" id="book-h">{title}</h2>
<p class="lead" style="margin-top:14px">{lead}</p>
<a class="book-phone" href="tel:{TEL}">{ic("phone")}{PHONE}</a>
<p class="small">South End: {hours_summary(OFFICES[0])}.<br>Ballantyne: {hours_summary(OFFICES[1])}.</p>
<p class="small">In pain right now? Call. Same day emergency slots open at both offices every weekday morning.</p>
</div>
<form class="book-form" action="#book" method="post" novalidate data-demo>
<fieldset><legend class="step">1. What's the visit for</legend><div class="reason-grid">{reasons}</div></fieldset>
<div class="fields">
<label class="field">Office<select name="office">{offs}<option value="either">Either is fine</option></select></label>
<label class="field">Best time<select name="when"><option>As soon as possible</option><option>Mornings</option><option>Afternoons</option><option>Fridays or Saturdays</option></select></label>
<label class="field">New or returning<select name="patient"><option>New patient</option><option>Returning patient</option></select></label>
<label class="field">Insurance<select name="insurance"><option>Not sure yet</option>{carriers}<option>Other plan</option><option>No insurance</option></select></label>
</div>
<p class="step" style="margin-top:6px">2. How to reach you</p>
<div class="fields">
<label class="field">Full name<input type="text" name="name" autocomplete="name"></label>
<label class="field">Mobile phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="field">Email<input type="email" name="email" autocomplete="email"></label>
<label class="field">Preferred contact<select name="contact"><option>Text me</option><option>Call me</option><option>Email me</option></select></label>
</div>
<p class="privacy-note">{ic("lock")}<span>Please leave health details out of this form. Once your visit is set, we send a secure link for your health history.</span></p>
<button class="btn btn-sea" type="submit">Request my visit</button>
<div class="form-done" role="status">This is a demo site, so nothing was sent. On a live Tessel site, this request lands in the front desk queue and you get a text within one business hour to confirm a time.</div>
</form>
</div>
</section>
'''


def cta_band(title, text, reason=None):
    q = f"?reason={reason}" if reason else ""
    return f'''<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band reveal">{TILES}
<div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-light" href="{q}#book">Book online</a></div>
</div></div></section>
'''


def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    offs = "".join(f'<li><a href="{o["slug"]}.html">{o["name"]}</a><br><span>{hours_summary(o)}</span></li>' for o in OFFICES)
    return f'''<footer class="site-footer">
<div class="wrap">
<div class="foot-top"><a class="brand" href="index.html" aria-label="{BRAND}, home">{MARK}<span class="brand-name">Tessel <span>Dental</span></span></a><p class="foot-tag">Calm, unhurried dentistry in Charlotte.</p></div>
<div class="foot-cols">
<div><h2>Contact</h2><address>Charlotte, North Carolina<br>Call or text <a href="tel:{TEL}">{PHONE}</a><br>Same day emergency visits</address></div>
<div><h2>Offices</h2><ul>{offs}</ul></div>
<div><h2>Services</h2><ul>{svc}<li><a href="services.html">All services</a></li></ul></div>
<div><h2>Patients</h2><ul><li><a href="new-patients.html">New patients</a></li><li><a href="insurance-financing.html">Insurance and financing</a></li><li><a href="our-dentists.html">Our dentists</a></li><li><a href="myers-park.html">Myers Park patients</a></li></ul></div>
</div>
<div class="foot-base"><span>Licensed by the North Carolina State Board of Dental Examiners. © 2026 {BRAND}.</span><span>A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Tessel Dental is a fictional practice.</span></div>
</div>
</footer>
<div class="mobile-bar"><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}Call</a><a class="btn btn-sea" href="#book">Book online</a></div>
<script src="assets/site.js" defer></script>
</body>
</html>
'''


def page(path, title, desc, schemas, current, body):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
