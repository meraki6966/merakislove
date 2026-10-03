"""Shared data, schema and page chrome for the Sideoats Insurance Agency demo.

Sideoats is a fictional independent agency in Fort Worth, Texas. The Texas
Department of Insurance facts, the National Weather Service hail sizes and the
neighborhood history are real and were checked in October 2026. The people,
the phone number and the reviews are samples. Nothing on the site is a quote.

The design is "The Deductible": the home page works out a percentage hail
deductible in dollars, and every other page opens the same way, with one large
number circled in chalk. Chivo throughout, on a strict ruled grid. No italics.
"""
import json
import re
from html import escape

BRAND = "Sideoats Insurance Agency"
SHORT = "Sideoats"
PHONE = "(817) 555-0172"            # 555-01xx is reserved for fiction
TEL = "+18175550172"
BASE = "https://merakislove.com/demos/sideoats"
YEAR_FOUNDED = 2011
TDI = {"phone": "800-252-3439", "tel": "+18002523439"}

# Sideoats grama, the state grass of Texas: one stem with the seeds hanging down one side.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M12 41C14 28 19 15 31 4" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
        '<path d="M14.5 32l6 3.4M17.5 25.5l6 3.4M21 19.5l6 3.4M25 14l6 3.4" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" fill="none"/></svg>')

# The chalk circle an adjuster draws around a hail hit. It goes around one number per page.
RING = ('<svg class="ring" viewBox="0 0 600 240" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
        '<path d="M300 14C470 6 590 60 584 124 578 196 440 232 286 226 130 220 14 184 18 112 22 48 150 10 318 20"/></svg>')

COVERAGES = [
    {"slug": "home-insurance", "name": "Home", "need": "home",
     "short": "Hail, wind, fire and theft, with the deductible worked out in dollars before you sign."},
    {"slug": "auto-insurance", "name": "Auto", "need": "auto",
     "short": "The Texas minimum is 30/60/25. We show you what the next step up covers."},
    {"slug": "renters-insurance", "name": "Renters", "need": "home",
     "short": "Your landlord's policy covers the building. This one covers what is inside it."},
    {"slug": "flood-insurance", "name": "Flood", "need": "home",
     "short": "Home policies do not cover flooding, and most flood policies take 30 days to start."},
    {"slug": "business-insurance", "name": "Business", "need": "business",
     "short": "General liability, commercial auto and property for shops, trades and offices."},
    {"slug": "umbrella-insurance", "name": "Umbrella", "need": "both",
     "short": "Extra liability coverage that sits on top of your home and auto policies."},
]
COV = {c["slug"]: c for c in COVERAGES}

AREAS = [
    {"slug": "fairmount", "name": "Fairmount"},
    {"slug": "arlington-heights", "name": "Arlington Heights"},
    {"slug": "benbrook", "name": "Benbrook"},
]
AREA_BY = {a["slug"]: a for a in AREAS}

PEOPLE = [
    ("Rosalind Ibarra", "Principal agent",
     "Rosalind opened Sideoats in 2011 after twelve years as a claims adjuster. She has stood on a lot of Fort Worth roofs, and she reads every renewal before it goes out."),
    ("Desmond Achterberg", "Commercial lines",
     "Desmond writes coverage for contractors, restaurants and small shops. He asks how your truck is used before he quotes it."),
    ("Tova Pruitt", "Personal lines",
     "Tova handles home and auto, and she is the person most likely to pick up the phone."),
]
HOURS = [("Monday to Friday", "8:30 AM to 5:30 PM"), ("Saturday and Sunday", "By appointment")]


def money(n):
    return "${:,.0f}".format(n)


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/",
            "logo": f"{BASE}/img/og.jpg", "telephone": "+1-817-555-0172", "foundingDate": str(YEAR_FOUNDED),
            "founder": {"@type": "Person", "name": "Rosalind Ibarra", "jobTitle": "Principal agent"}}


def business_schema():
    # InsuranceAgency descends from LocalBusiness through FinancialService. LocalBusiness
    # is named as well so a scanner that only matches the exact type still finds it.
    return {
        "@context": "https://schema.org", "@type": ["InsuranceAgency", "LocalBusiness"], "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
        "telephone": "+1-817-555-0172", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Fort Worth", "addressRegion": "TX", "postalCode": "76104", "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": "Fort Worth"}, {"@type": "City", "name": "Benbrook"},
                       {"@type": "AdministrativeArea", "name": "Tarrant County, Texas"}],
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:30", "closes": "17:30"}],
        "parentOrganization": {"@id": f"{BASE}/#org"},
    }


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/",
            "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


def service_schema(name, desc, path):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "description": desc, "url": f"{BASE}/{path}",
            "provider": {"@id": f"{BASE}/#business"}, "areaServed": {"@type": "City", "name": "Fort Worth"}}


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
NAV = [("coverage.html", "Coverage", "coverage"), ("hail-deductible.html", "Hail deductible", "deductible"),
       ("after-a-hail-storm.html", "After a storm", "storm"), ("switching.html", "Switching", "switching"),
       ("about.html", "About", "about")]


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
<meta name="theme-color" content="#F4F4F1">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chivo:wght@400;500;700;900&amp;display=swap">
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
    return f"""<header class="hd"><div class="w hd-in">
<a class="mark" href="index.html" aria-label="{BRAND}, home">{MARK}<span>Sideoats<small>Insurance Agency</small></span></a>
<nav aria-label="Main">{links}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a>
<a class="btn small" href="#quote">Get a quote</a>
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


QUOTE_BTN = '<a class="btn" href="#quote">Get a quote</a>'
CALL_LINK = f'<a class="call" href="tel:{TEL}">or call {PHONE}</a>'


def big(number):
    return f'<p class="big">{RING}<span>{number}</span></p>'


def opener(h1, lede, crumb_items, label, number, caption, buttons=True):
    """Every inner page opens like the home page: the claim on the left, one circled number on the right."""
    acts = f'<div class="acts">{QUOTE_BTN}{CALL_LINK}</div>' if buttons else ""
    return f'''<section class="hero"><div class="w">
<div class="calc">
<div class="calc-in">{crumbs(crumb_items)}<h1>{h1}</h1><p class="lede">{lede}</p>{acts}</div>
<div class="calc-out"><p class="k">{label}</p>{big(number)}<p class="say">{caption}</p></div>
</div>
</div></section>
'''


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
    return f'<table class="hours"><caption>Office hours, Central time</caption><tbody>{body}</tbody></table>'


def form(need=None):
    opts = [("home", "Home"), ("auto", "Auto"), ("both", "Home and auto"), ("business", "Business")]
    choices = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}"{" checked" if v == need else ""}>{t}</label>' for v, t in opts)
    return f"""<form class="form" action="#quote" method="post" novalidate data-demo>
<fieldset><legend>What do you need covered?</legend><div class="choices">{choices}</div></fieldset>
<div class="fields">
<label>ZIP code<input type="text" name="zip" inputmode="numeric" autocomplete="postal-code"></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label>Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn" type="submit">Ask for a quote</button>
<p class="form-note">Leave policy numbers, driver's license numbers and birth dates out of this form. We collect those by phone, once you know who you are talking to. See the <a href="privacy.html">privacy page</a>.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live Sideoats site, an agent calls back the same business day.</p>
</form>"""


def quote(title="Have us read your policy",
          lead="Send four details and an agent calls back the same business day. Bring your current policy to the call and we will find the deductible together.", need=None):
    return f"""<section class="sec quote" id="quote" aria-labelledby="quote-h"><div class="w quote-g">
<div><h2 id="quote-h">{title}</h2><p>{lead}</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p>
<p class="fine">Monday to Friday, 8:30 AM to 5:30 PM Central. Magnolia Avenue, Near Southside, Fort Worth.</p></div>
{form(need)}
</div></section>
"""


def footer(extra=""):
    covs = "".join(f'<li><a href="{c["slug"]}.html">{c["name"]} insurance</a></li>' for c in COVERAGES)
    areas = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS)
    return f"""<footer class="ft"><div class="w">
<div class="ft-cols">
<div><h2>Sideoats Insurance Agency</h2><address>Magnolia Avenue, Near Southside<br>Fort Worth, TX 76104<br><a href="tel:{TEL}">{PHONE}</a><br>Monday to Friday, 8:30 AM to 5:30 PM</address>
<ul><li><a href="about.html">About the agency</a></li><li><a href="switching.html">Switching to Sideoats</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
<div><h2>Coverage</h2><ul>{covs}<li><a href="coverage.html">All coverage</a></li></ul></div>
<div><h2>Guides and places</h2><ul><li><a href="hail-deductible.html">Your hail deductible in dollars</a></li><li><a href="after-a-hail-storm.html">What to do after a hail storm</a></li>{areas}</ul></div>
<div><h2>Texas Department of Insurance</h2><address>Help line <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a><br>For complaints, license checks and the Consumer Bill of Rights.</address>
<p>Licensed by the Texas Department of Insurance. On a live site, the agency license number goes here.</p></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Sideoats is a fictional agency, and its people and reviews are samples. The numbers on this site are illustrations and are not a quote or an offer of coverage. The Texas Department of Insurance is real and is not affiliated with this demo.</p>
</div></footer>
{extra}<script src="assets/site.js" defer></script>
</body>
</html>
"""


def page(path, title, desc, schemas, current, body, extra=""):
    return head(title, desc, path, schemas) + header(current) + f'<main id="main">\n{body}</main>\n' + footer(extra)
