"""Shared data, schema and page chrome for the Fernhollow Veterinary Clinic demo.

Fernhollow is a fictional dog and cat clinic in Sellwood, Portland. The places,
the emergency hospital, the poison line, Oregon's rabies rule and the county
license fees are real and were checked in October 2026. The people, the phone
number and the prices are samples.

The design is "Can It Wait": the home page is a three lane triage board (go
now, call us today, book this week), and the three lane colors carry the same
meaning on every other page. Gabarito throughout. No italics.
"""
import json
import re
from html import escape

BRAND = "Fernhollow Veterinary Clinic"
SHORT = "Fernhollow"
PHONE = "(503) 555-0146"            # 555-01xx is reserved for fiction
TEL = "+15035550146"
BASE = "https://merakislove.com/demos/fernhollow"
YEAR_FOUNDED = 2012
ER = {"name": "DoveLewis", "full": "DoveLewis Veterinary Emergency and Specialty Hospital", "addr": "1945 NW Pettygrove Street",
      "phone": "(503) 228-7281", "tel": "+15032287281"}
POISON = {"phone": "(888) 426-4435", "tel": "+18884264435"}

# A fern frond: one stem with paired leaflets.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M22 40V8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
        '<path d="M22 34c-6-1-10-4-12-9M22 34c6-1 10-4 12-9M22 27c-5-1-8-3-10-7M22 27c5-1 8-3 10-7M22 20c-4-1-6-3-7-6M22 20c4-1 6-3 7-6M22 13c-2-1-4-2-4-5M22 13c2-1 4-2 4-5" '
        'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg>')

# The three lanes of the triage board. The same key colors a tag or a panel anywhere on the site.
LANES = {"go": "Go now", "today": "Call us today", "week": "Book this week"}

SERVICES = [
    {"slug": "wellness-exams", "name": "Wellness exams", "lane": "week", "price": "$78", "reason": "Wellness exam",
     "short": "A full nose to tail exam and a written plan. Once a year for adults, twice a year from age seven."},
    {"slug": "sick-visits", "name": "Same day sick visits", "lane": "today", "price": "$95", "reason": "Sick visit",
     "short": "Call before 3 PM and we see your pet today. You get an estimate before any test or treatment."},
    {"slug": "dental-care", "name": "Dental care", "lane": "week", "price": "From $520", "reason": "Dental",
     "short": "Cleanings under anesthesia with full mouth x-rays, and a phone call before any extraction."},
    {"slug": "vaccines", "name": "Vaccines", "lane": "week", "price": "From $30", "reason": "Vaccines",
     "short": "Core vaccines for dogs and cats, puppy and kitten series, and the rabies certificate the county asks for."},
]
SVC = {s["slug"]: s for s in SERVICES}

AREAS = [
    {"slug": "westmoreland", "name": "Westmoreland"},
    {"slug": "eastmoreland", "name": "Eastmoreland"},
    {"slug": "woodstock", "name": "Woodstock"},
]
AREA_BY = {a["slug"]: a for a in AREAS}

PEOPLE = [
    ("Dr. Maren Halvorsen", "Veterinarian and owner",
     "Maren opened Fernhollow in 2012 after ten years in emergency medicine. She still takes the hard cases, and she writes down the price before any treatment starts."),
    ("Dr. Caleb Thornquist", "Veterinarian",
     "Caleb sees most of our cats and runs the dental suite. He keeps a second, quieter exam room for cats who would prefer to skip the lobby."),
    ("Junie Akana", "Certified veterinary technician",
     "Junie is the voice on the phone when you call worried. She has helped more Sellwood owners decide between tonight and tomorrow than anyone on staff."),
]
HOURS = [("Monday to Friday", "7:30 AM to 6 PM"), ("Saturday", "9 AM to 2 PM"), ("Sunday", "Closed")]


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/",
            "logo": f"{BASE}/img/og.jpg", "telephone": "+1-503-555-0146", "foundingDate": str(YEAR_FOUNDED),
            "founder": {"@type": "Person", "name": "Maren Halvorsen", "jobTitle": "Veterinarian"}}


def business_schema():
    # VeterinaryCare sits under MedicalOrganization in schema.org, so LocalBusiness is
    # named as well. That is what carries the address and the opening hours.
    return {
        "@context": "https://schema.org", "@type": ["VeterinaryCare", "LocalBusiness"], "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
        "telephone": "+1-503-555-0146", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Portland", "addressRegion": "OR", "postalCode": "97202", "addressCountry": "US"},
        "areaServed": [{"@type": "Place", "name": n} for n in ["Sellwood, Portland", "Westmoreland, Portland", "Eastmoreland, Portland", "Woodstock, Portland"]],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:30", "closes": "18:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "09:00", "closes": "14:00"}],
        "parentOrganization": {"@id": f"{BASE}/#org"},
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/",
            "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


def service_schema(name, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": f"{BASE}/{path}",
            "provider": {"@id": f"{BASE}/#business"}, "areaServed": {"@type": "City", "name": "Portland"}}


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
NAV = [("services.html", "Services", "services"), ("emergencies.html", "Emergencies", "emergencies"),
       ("portland-pet-hazards.html", "Portland hazards", "hazards"), ("pricing.html", "Prices", "pricing"),
       ("new-clients.html", "New clients", "new"), ("about.html", "About", "about")]


def head(title, desc, path, schemas):
    url = f"{BASE}/" if path == "index.html" else f"{BASE}/{path}"
    return f"""<!doctype html>
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
<meta name="theme-color" content="#13203A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;700;900&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
{"".join(ld(s) for s in schemas)}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current=""):
    links = ""
    for href, text, key in NAV:
        cur = ' aria-current="page"' if key == current else ""
        links += f'<a href="{href}"{cur}>{text}</a>'
    return f"""<div class="status" data-status><span class="dot" aria-hidden="true"></span><span data-status-text>Open Monday to Friday 7:30 AM to 6 PM, and Saturday 9 AM to 2 PM.</span><a href="tel:{TEL}">{PHONE}</a></div>
<header class="hd"><div class="w hd-in">
<a class="mark" href="index.html" aria-label="{BRAND}, home">{MARK}<span>Fernhollow Vet</span></a>
<nav aria-label="Main">{links}</nav>
<a class="btn small" href="#book">Request a visit</a>
</div></header>
"""


def crumbs(items):
    out = []
    for i, (n, href) in enumerate(items):
        if i < len(items) - 1:
            out.append(f'<a href="{href or "index.html"}">{n}</a><span aria-hidden="true">/</span>')
        else:
            out.append(f'<span aria-current="page">{n}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(out)}</nav>'


def tag(lane):
    """A small lane label. The color and the words always travel together."""
    return f'<span class="tag {lane}">{LANES[lane]}</span>'


def species_switch(label="I have a"):
    return (f'<div class="species" role="group" aria-label="{label}"><span>{label}</span>'
            '<button type="button" data-species="dog" aria-pressed="true">Dog</button>'
            '<button type="button" data-species="cat" aria-pressed="false">Cat</button></div>')


BOOK_BTN = '<a class="btn" href="#book">Request a visit</a>'
CALL_LINK = f'<a class="call" href="tel:{TEL}">or call {PHONE}</a>'


def pic(img, alt, cls=""):
    return f'<figure class="phero-img {cls}"><img src="img/{img}.webp" alt="{alt}" fetchpriority="high" width="1600" height="1200"></figure>'


def panel(lane, title, items, act=""):
    """A lane colored panel for an inner page opener: a title, a short ruled list and one action."""
    lis = "".join(f"<li>{t}</li>" for t in items)
    return f'<aside class="panel {lane}" aria-label="{strip(title)}"><h2>{title}</h2><ul>{lis}</ul>{act}</aside>'


def facts(items):
    return '<ul class="facts">' + "".join(f"<li><b>{b}</b>{t}</li>" for b, t in items) + "</ul>"


def phero(h1, lede, crumb_items, side="", strip_facts=None, buttons=True, extra=""):
    acts = f'<div class="acts">{BOOK_BTN}{CALL_LINK}</div>' if buttons else ""
    more = f'<div class="acts">{extra}</div>' if extra else ""
    copy = f'<div class="phero-copy">{crumbs(crumb_items)}<h1>{h1}</h1><p class="lede">{lede}</p>{acts}{more}</div>'
    under = f'<div class="w">{facts(strip_facts)}</div>' if strip_facts else ""
    return f'<section class="phero"><div class="w phero-g{"" if side else " solo"}">{copy}{side}</div>{under}</section>\n'


def faq_items(qa):
    return "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))


def faq_block(title, qa, bg=""):
    return f"""<section class="sec {bg}" aria-labelledby="faq-h"><div class="w faq-g">
<h2 id="faq-h">{title}</h2>
<div class="faq">{faq_items(qa)}</div>
</div></section>
"""


def hours_table():
    body = "".join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in HOURS)
    return f'<table class="hours"><caption>Clinic hours, Pacific time</caption><tbody>{body}</tbody></table>'


def form(reason=None):
    opts = ["Wellness exam", "Sick visit", "Vaccines", "Dental", "Something else"]
    options = "".join(f'<option{" selected" if o == reason else ""}>{o}</option>' for o in opts)
    return f"""<form class="form" action="#book" method="post" novalidate data-demo>
<fieldset><legend>Who is the visit for?</legend><div class="choices">
<label class="choice"><input type="radio" name="pet" value="dog">A dog</label>
<label class="choice"><input type="radio" name="pet" value="cat">A cat</label></div></fieldset>
<div class="fields">
<label>Your pet's name<input type="text" name="petname"></label>
<label>What is going on?<select name="reason">{options}</select></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="full">Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn" type="submit">Request a visit</button>
<p class="form-note">If your pet needs to be seen today, please call. Leave medical history and card numbers out of this form. See the <a href="privacy.html">privacy page</a>.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live Fernhollow site, the front desk calls back within two business hours to confirm a time.</p>
</form>"""


def book(title="Request a visit", lead="Tell us who is coming and why, and the front desk calls back within two business hours to set a time.", reason=None):
    return f"""<section class="sec book" id="book" aria-labelledby="book-h"><div class="w book-g">
<div><h2 id="book-h">{title}</h2><p>{lead}</p><p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p>
<p class="fine">Monday to Friday 7:30 AM to 6 PM, Saturday 9 AM to 2 PM. After hours, call {ER["name"]} at <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.</p></div>
{form(reason)}
</div></section>
"""


def footer(extra=""):
    svcs = "".join(f'<li><a href="{s["slug"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    data = json.dumps({"er": {"name": ER["name"], "phone": ER["phone"], "tel": ER["tel"]}}).replace("</", "<\\/")
    return f"""<footer class="ft"><div class="w">
<div class="ft-cols">
<div><h2>Fernhollow Veterinary Clinic</h2><address>Sellwood, Portland, OR 97202<br><a href="tel:{TEL}">{PHONE}</a><br>Monday to Friday, 7:30 AM to 6 PM<br>Saturday, 9 AM to 2 PM</address>
<ul><li><a href="about.html">About the clinic</a></li><li><a href="new-clients.html">New clients</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
<div><h2>Care</h2><ul>{svcs}<li><a href="services.html">All services</a></li><li><a href="pricing.html">Prices</a></li></ul></div>
<div><h2>Guides</h2><ul><li><a href="emergencies.html">What to do in an emergency</a></li><li><a href="portland-pet-hazards.html">Portland pet hazards by month</a></li><li><a href="salmon-poisoning.html">Salmon poisoning in dogs</a></li>{areas}</ul></div>
<div><h2>After hours</h2><address>{ER["full"]}<br>{ER["addr"]}, Portland<br><a href="tel:{ER["tel"]}">{ER["phone"]}</a><br>Open 24 hours, every day</address>
<address>ASPCA Animal Poison Control Center<br><a href="tel:{POISON["tel"]}">{POISON["phone"]}</a><br>Day and night. A fee may apply.</address></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Fernhollow is a fictional clinic, its people and prices are samples, and nothing here replaces an exam by your own veterinarian. DoveLewis and the ASPCA poison line are real and are not affiliated with this demo.</p>
</div></footer>
<script type="application/json" id="data">{data}</script>
{extra}<script src="assets/site.js" defer></script>
</body>
</html>
"""


def page(path, title, desc, schemas, current, body, extra=""):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer(extra)
