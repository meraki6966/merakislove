"""Two home page previews for the Sideoats Insurance Agency demo, for Adam to choose between.

Run from the repo root:  python3 scripts/demos/sideoats/previews.py
Writes preview-a.html (The Deductible) and preview-b.html (Plain Talk) into
public/demos/sideoats/. Both are noindex and are not linked from anywhere.

Sideoats is a fictional independent agency in Fort Worth. The Texas Department
of Insurance facts (30/60/25, PIP, the deductible example, flood and its 30 day
wait, the help line) and the National Weather Service hail sizes are real and
were checked in October 2026.
"""
import json
import os
import re
import sys
from html import escape

BRAND = "Sideoats Insurance Agency"
PHONE = "(817) 555-0172"            # 555-01xx is reserved for fiction
TEL = "+18175550172"
BASE = "https://merakislove.com/demos/sideoats"
PREFIX = "/demos/sideoats/"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "sideoats")
TDI = {"phone": "800-252-3439", "tel": "+18002523439"}
PROBLEMS = []

TITLE = "Insurance Agency in Fort Worth, TX | Sideoats Insurance"
DESC = ("Sideoats is an independent insurance agency in Fort Worth, Texas. Home, auto and business coverage, "
        "with your hail deductible worked out in dollars first.")
NAV = [("#home", "Home insurance"), ("#auto", "Auto"), ("#write", "What we write"), ("#people", "About")]

# Sideoats grama, the state grass of Texas: one stem with the seeds hanging down one side.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M12 41C14 28 19 15 31 4" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
        '<path d="M14.5 32l6 3.4M17.5 25.5l6 3.4M21 19.5l6 3.4M25 14l6 3.4" stroke="currentColor" stroke-width="3.4" stroke-linecap="round" fill="none"/></svg>')

COVERAGES = [
    ("Home", "Hail, wind, fire and theft, with the deductible worked out in dollars before you sign."),
    ("Auto", "The Texas minimum is 30/60/25. We show you what the next step up costs."),
    ("Renters", "Your landlord's policy covers the building. This one covers what is inside it."),
    ("Flood", "Home policies do not cover flooding, and most flood policies take 30 days to start."),
    ("Business", "General liability, commercial auto and property for shops, trades and offices."),
    ("Umbrella", "Extra liability coverage that sits on top of your home and auto policies."),
]

PEOPLE = [
    ("Rosalind Ibarra", "Principal agent", "Rosalind opened Sideoats in 2011 after twelve years as a claims adjuster. She has stood on a lot of Fort Worth roofs, and she reads every renewal before it goes out."),
    ("Desmond Achterberg", "Commercial lines", "Desmond writes coverage for contractors, restaurants and small shops. He asks how your truck is used before he quotes it."),
    ("Tova Pruitt", "Personal lines", "Tova handles home and auto, and she is the person most likely to pick up the phone."),
]

# NWS Fort Worth hail size guide: name, diameter in inches.
HAIL = [("Pea", 0.25), ("Penny", 0.75), ("Quarter", 1.0), ("Golf ball", 1.75), ("Baseball", 2.75)]

HOME_FAQ = [
    ("What is a percentage deductible?", "It is a deductible set as a share of what your house is insured for. On a house insured for $380,000, a 2% wind and hail deductible is $7,600. You pay that amount on each claim before the policy pays anything."),
    ("Does home insurance cover flooding in Texas?", "No. Home policies do not cover flooding. Flood insurance is a separate policy, and most flood policies have a 30 day waiting period before they start, so it has to be in place before a storm is on the forecast."),
    ("What is the minimum auto insurance in Texas?", "Texas requires liability coverage of at least $30,000 for each injured person, up to $60,000 per accident, and $25,000 for property damage. It is written as 30/60/25."),
    ("What is an independent insurance agency?", "An independent agency is not tied to one insurance company. We place your policy with the carrier that fits, and at renewal we can check it against the others we represent."),
    ("How do I check that an agent is licensed in Texas?", f'Call the Texas Department of Insurance help line at <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a>, or use the agent lookup on the department\'s website. Every Texas agent and agency has a license number you can ask for.'),
]

# Preview B: the sentence builder. thing -> (label, article, [(question, answer, big figure)])
ASK = {
    "house": ("house", [
        ("what a hail claim would cost me",
         "It depends on your deductible, and in Texas that is often a percentage of what the house is insured for. The Texas Department of Insurance gives this example: on a $150,000 home, a 5% deductible is $7,500, so a $6,500 roof repair would be paid entirely by you.", "$7,500"),
        ("whether a flood is covered",
         "No. Home policies do not cover flooding. Flood insurance is a separate policy, and most flood policies have a 30 day waiting period, so it has to be in place before the storm is on the forecast.", "30 days"),
        ("why my premium went up",
         "Usually it is one of three things. The cost to rebuild your house rose, your roof got older, or your insurer raised its rates. Send us the renewal and we will tell you which, then check what the other carriers we represent would charge.", "3 reasons"),
    ]),
    "car": ("car", [
        ("if the state minimum is enough",
         "Texas requires 30/60/25. That is $30,000 for each injured person, up to $60,000 per accident, and $25,000 for property damage. The property number is the one that runs out first, because many new vehicles cost more than $25,000.", "30/60/25"),
        ("what happens if the other driver has no insurance",
         "That is what uninsured and underinsured motorist coverage is for. In Texas the insurer has to offer it, and you only go without it if you turned it down in writing. Check your policy for a signed rejection.", "In writing"),
        ("what PIP is",
         "Personal injury protection pays medical bills and some lost income for you and your passengers, whoever caused the wreck. Every Texas auto policy includes it unless you rejected it in writing.", "PIP"),
    ]),
    "rental": ("rental", [
        ("if I need renters insurance",
         "Your landlord's policy covers the building. It does not cover your furniture, your laptop or a guest who gets hurt in your apartment. A renters policy does. Ask us for the price before you decide.", "Your things"),
        ("what a renters policy covers",
         "Three things: your belongings, your liability if someone is hurt in your home, and a place to stay if a covered loss makes the apartment unlivable. Flooding is not covered.", "3 things"),
    ]),
    "business": ("small business", [
        ("what general liability covers",
         "It pays when a customer or a member of the public is hurt, or their property is damaged, because of your business. Your own employees are covered by a different policy, workers' compensation.", "The public"),
        ("if my truck is covered for work",
         "Probably not under a personal auto policy. A vehicle that hauls tools, makes deliveries or carries customers usually needs a commercial auto policy. Tell us how the truck is used and we will check.", "Ask first"),
    ]),
}


def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def money(n):
    return "${:,.0f}".format(n)


def schemas():
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/", "logo": f"{BASE}/img/og.jpg",
           "telephone": "+1-817-555-0172", "foundingDate": "2011", "founder": {"@type": "Person", "name": "Rosalind Ibarra", "jobTitle": "Principal agent"}}
    biz = {"@context": "https://schema.org", "@type": "InsuranceAgency", "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
           "telephone": "+1-817-555-0172", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
           "address": {"@type": "PostalAddress", "addressLocality": "Fort Worth", "addressRegion": "TX", "postalCode": "76104", "addressCountry": "US"},
           "areaServed": [{"@type": "City", "name": "Fort Worth"}, {"@type": "AdministrativeArea", "name": "Tarrant County, Texas"}],
           "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:30", "closes": "17:30"}],
           "parentOrganization": {"@id": f"{BASE}/#org"}}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/", "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in HOME_FAQ]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"}]}
    return "".join(ld(s) for s in [org, biz, site, faq, crumbs])


def head(css, fonts, theme):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE}</title>
<meta name="description" content="{escape(DESC, quote=True)}">
<meta name="author" content="{BRAND}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{BASE}/">
<meta name="theme-color" content="{theme}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&amp;display=swap">
<link rel="stylesheet" href="assets/{css}">
{schemas()}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''


def ribbon(this, other_href, other_name):
    return f'<p class="ribbon">Preview {this}. <a href="{other_href}">See {other_name}</a>.</p>\n'


def nav_links():
    return "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)


def faq_items():
    return "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(HOME_FAQ))


def people_list():
    return '<ul class="people">' + "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in PEOPLE) + "</ul>"


def form():
    return '''<form class="form" action="#quote" method="post" novalidate data-demo>
<fieldset><legend>What do you need covered?</legend><div class="choices">
<label class="choice"><input type="radio" name="need" value="home">Home</label>
<label class="choice"><input type="radio" name="need" value="auto">Auto</label>
<label class="choice"><input type="radio" name="need" value="both">Home and auto</label>
<label class="choice"><input type="radio" name="need" value="business">Business</label></div></fieldset>
<div class="fields">
<label>ZIP code<input type="text" name="zip" inputmode="numeric" autocomplete="postal-code"></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label>Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn" type="submit">Ask for a quote</button>
<p class="form-note">Leave policy numbers, driver's license numbers and birth dates out of this form. We collect those by phone, once you know who you are talking to.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live Sideoats site, an agent calls back the same business day.</p>
</form>'''


def footer_html(js, data=None):
    blob = f'<script type="application/json" id="data">{json.dumps(data).replace("</", "<" + chr(92) + "/")}</script>\n' if data else ""
    return f'''<footer class="ft"><div class="w">
<div class="ft-cols">
<div><h2>Sideoats Insurance Agency</h2><address>Magnolia Avenue, Near Southside<br>Fort Worth, TX 76104<br><a href="tel:{TEL}">{PHONE}</a><br>Monday to Friday, 8:30 AM to 5:30 PM</address></div>
<div><h2>Licensing</h2><p>Licensed by the Texas Department of Insurance. On a live site, the agency license number goes here.</p></div>
<div><h2>Texas Department of Insurance</h2><address>Help line <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a><br>For complaints, license checks and the Consumer Bill of Rights.</address></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Sideoats is a fictional agency, and its people are samples. The numbers on this page are illustrations and are not a quote or an offer of coverage. The Texas Department of Insurance is real and is not affiliated with this demo.</p>
</div></footer>
{blob}<script src="assets/{js}" defer></script>
</body>
</html>
'''


def coverage_rows():
    return "".join(f"<li><h3>{n}</h3><p>{d}</p></li>" for n, d in COVERAGES)


# ------------------------------------------------------------------ Preview A
def build_a():
    house, pct, roof = 380000, 2, 18500
    ded = house * pct // 100
    pays = max(0, roof - ded)
    you = min(roof, ded)
    share = round(you / roof * 100, 2)
    hail = ""
    for n, d in HAIL:
        cls = ' class="sev"' if d == 1.0 else ""
        hail += f'<li{cls} style="--d:{d}"><i aria-hidden="true"></i><b>{n}</b><span>{d:g} in</span></li>'
    pct_opts = "".join(f'<label><input type="radio" name="pct" value="{p}"{" checked" if p == pct else ""}><span>{p}%</span></label>' for p in (1, 2, 3, 5))
    body = f'''{ribbon("A, The Deductible", "preview-b.html", "preview B, Plain Talk")}<header class="hd"><div class="w hd-in">
<a class="mark" href="preview-a.html" aria-label="{BRAND}, home">{MARK}<span>Sideoats<small>Insurance Agency</small></span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a>
<a class="btn small" href="#quote">Get a quote</a>
</div></header>
<main id="main">
<section class="hero" id="home"><div class="w">
<div class="calc">
<div class="calc-in">
<h1>Your hail deductible, in dollars.</h1>
<p class="lede">Many Texas home policies set the wind and hail deductible as a percentage of what the house is insured for. Move the numbers and see what a roof claim would cost you.</p>
<form class="dials" data-calc aria-label="Deductible calculator">
<label class="dial"><span>Your house is insured for <output data-o="house">{money(house)}</output></span>
<input type="range" name="house" min="150000" max="900000" step="10000" value="{house}"></label>
<fieldset class="dial"><legend>Wind and hail deductible</legend><div class="seg">{pct_opts}</div></fieldset>
<label class="dial"><span>A new roof costs <output data-o="roof">{money(roof)}</output></span>
<input type="range" name="roof" min="6000" max="40000" step="500" value="{roof}"></label>
</form>
</div>
<div class="calc-out" aria-live="polite">
<p class="k">You pay</p>
<p class="big"><svg class="ring" viewBox="0 0 600 240" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M300 14C470 6 590 60 584 124 578 196 440 232 286 226 130 220 14 184 18 112 22 48 150 10 318 20"/></svg><span data-o="ded">{money(ded)}</span></p>
<div class="bar" aria-hidden="true"><span class="you" data-bar style="width:{share}%"></span></div>
<dl class="split"><div><dt>You pay</dt><dd data-o="you">{money(you)}</dd></div><div><dt>The policy pays</dt><dd data-o="pays">{money(pays)}</dd></div></dl>
<p class="say" data-o="say">On a {money(roof)} roof, a {pct}% deductible leaves you with {money(you)} and the policy with {money(pays)}.</p>
</div>
</div>
<p class="fine">An illustration with round numbers. It is not a quote, and your policy may work differently. The percentage is applied to your dwelling coverage, the amount the house is insured for. <a href="#quote">Have us read your policy</a>.</p>
</div></section>

<section class="sec" aria-labelledby="hail-h"><div class="w hail-g">
<div><h2 id="hail-h">How big was the hail?</h2>
<p>The National Weather Service office in Fort Worth sizes hail against things you already own. A storm counts as severe once the stones reach one inch across, the size of a quarter.</p>
<ol class="hail" aria-label="Hail sizes from the National Weather Service">{hail}</ol>
<p class="fine">Drawn to scale against each other.</p></div>
<div><figure><img src="img/shingles-chalk.webp" alt="Dark asphalt shingles seen from above, with hail bruises circled in white chalk and a stick of chalk resting on the roof" loading="lazy" width="1200" height="900"><figcaption>An adjuster circles each hail hit in chalk before counting them.</figcaption></figure>
<h3>After a storm, in this order</h3>
<ol class="steps"><li>Take photos of the roof, the gutters and the car before anything is cleaned up.</li><li>Call us before a roofer asks you to sign anything.</li><li>We compare the repair estimate with your deductible, so you know whether a claim pays before you file one.</li></ol></div>
</div></section>

<section class="sec dark" id="auto" aria-labelledby="auto-h"><div class="w">
<h2 id="auto-h">What does 30/60/25 mean?</h2>
<p class="intro">It is the least auto liability coverage Texas lets you drive with. Each number is in thousands of dollars.</p>
<ul class="trio">
<li><b>30</b><h3>$30,000 for each injured person</h3><p>What your policy pays toward one person's injuries when a wreck is your fault.</p></li>
<li><b>60</b><h3>$60,000 for each accident</h3><p>The most it pays for everyone's injuries in one wreck, however many people are hurt.</p></li>
<li><b>25</b><h3>$25,000 for property damage</h3><p>What it pays to fix the other driver's vehicle. Many new trucks cost more than this.</p></li>
</ul>
<p class="fine">Every Texas auto policy also includes personal injury protection unless you turned it down in writing, and your insurer has to offer uninsured motorist coverage.</p>
</div></section>

<section class="sec" id="write" aria-labelledby="write-h"><div class="w write-g">
<div><h2 id="write-h">What does Sideoats write?</h2><p>We are an independent agency, so your policy can be placed with the carrier that fits and checked against the others at renewal.</p></div>
<ul class="cov">{coverage_rows()}</ul>
</div></section>

<section class="sec tint" id="people" aria-labelledby="people-h"><div class="w people-g">
<figure><img src="img/kitchen.webp" alt="An insurance agent in a denim shirt at a kitchen table with a homeowner couple, going over a printed page with a pen" loading="lazy" width="1600" height="1200"></figure>
<div><h2 id="people-h">Who reads your policy?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>

<section class="sec" aria-labelledby="faq-h"><div class="w faq-g">
<h2 id="faq-h">Questions we answer every week</h2>
<div class="faq">{faq_items()}</div>
</div></section>

<section class="sec quote" id="quote" aria-labelledby="quote-h"><div class="w quote-g">
<div><h2 id="quote-h">Have us read your policy</h2><p>Send four details and an agent calls back the same business day. Bring your current policy to the call and we will find the deductible together.</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p>
<figure class="office"><img src="img/office.webp" alt="A single story red brick office building in Fort Worth under a wide blue sky, with a pickup truck parked at the curb" loading="lazy" width="1600" height="1200"></figure></div>
{form()}
</div></section>
</main>
'''
    return head("preview-a.css", "family=Chivo:wght@400;500;700;900", "#F4F4F1") + body + footer_html("preview-a.js")


# ------------------------------------------------------------------ Preview B
def build_b():
    things = "".join(f'<label><input type="radio" name="thing" value="{k}"{" checked" if k == "house" else ""}><span>{v[0]}</span></label>' for k, v in ASK.items())
    first = ASK["house"][1]
    qs = "".join(f'<label><input type="radio" name="q" value="{i}"{" checked" if i == 0 else ""}><span>{q}</span></label>' for i, (q, a, f) in enumerate(first))
    said = "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in [
        ("Your hail deductible is probably a percentage.", "On a house insured for $380,000, a 2% wind and hail deductible is $7,600. That comes out of your pocket on each claim, before the policy pays."),
        ("Your home policy does not cover a flood.", "Flood insurance is a separate policy. Most flood policies take 30 days to start, so the day before the storm is too late."),
        ("30/60/25 is the legal minimum, and it is small.", "$25,000 is all the state minimum pays to fix the other driver's vehicle. Many new trucks cost more than that."),
    ])
    cov = "".join(f"<li><h3>{n}</h3><p>{d}</p></li>" for n, d in COVERAGES)
    data = {k: {"label": v[0], "qs": [{"q": q, "a": a, "f": f} for q, a, f in v[1]]} for k, v in ASK.items()}
    body = f'''{ribbon("B, Plain Talk", "preview-a.html", "preview A, The Deductible")}<header class="hd field"><div class="w hd-in">
<a class="mark" href="preview-b.html" aria-label="{BRAND}, home">{MARK}<span>Sideoats</span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a>
</div></header>
<main id="main">
<section class="hero field" id="home"><div class="w hero-g">
<div class="ask">
<h1>Texas insurance, answered in plain talk.</h1>
<p class="sentence" aria-hidden="true">I have a <span data-s="thing">house</span> in Fort Worth, and I want to know <span data-s="q">{first[0][0]}</span>.</p>
<form class="pick" data-ask aria-label="Build your question">
<fieldset><legend>I have a</legend><div class="chips">{things}</div></fieldset>
<fieldset><legend>I want to know</legend><div class="chips" data-qs>{qs}</div></fieldset>
</form>
</div>
<div class="answer" aria-live="polite">
<p class="fig" data-a="f">{first[0][2]}</p>
<p class="txt" data-a="a">{first[0][1]}</p>
<p class="acts"><a class="btn" href="#quote">Have us check yours</a><a class="call" href="tel:{TEL}">or call {PHONE}</a></p>
</div>
</div></section>

<section class="sec" id="auto" aria-labelledby="said-h"><div class="w said-g">
<h2 id="said-h">Three things we explain every week</h2>
<ul class="said">{said}</ul>
</div></section>

<section class="sec oat" id="people" aria-labelledby="people-h"><div class="w people-g">
<figure><img src="img/kitchen.webp" alt="An insurance agent in a denim shirt at a kitchen table with a homeowner couple, going over a printed page with a pen" loading="lazy" width="1600" height="1200"><figcaption>Most of our reviews happen at a kitchen table, with the policy open.</figcaption></figure>
<div><h2 id="people-h">Who answers when you call?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>

<section class="sec" id="write" aria-labelledby="write-h"><div class="w">
<h2 id="write-h">What does Sideoats write?</h2>
<p class="intro">We are an independent agency, so your policy can be placed with the carrier that fits and checked against the others at renewal.</p>
<ul class="cov">{cov}</ul>
</div></section>

<section class="sec oat" aria-labelledby="where-h"><div class="w where-g">
<div><h2 id="where-h">Where is the office?</h2>
<p>We are on Magnolia Avenue in the Near Southside of Fort Worth, in a brick building with parking at the curb. Walk in with your policy, or we will come to your kitchen table.</p>
<table class="hours"><caption>Office hours, Central time</caption><tbody><tr><th scope="row">Monday to Friday</th><td>8:30 AM to 5:30 PM</td></tr><tr><th scope="row">Saturday and Sunday</th><td>By appointment</td></tr></tbody></table></div>
<figure><img src="img/office.webp" alt="A single story red brick office building in Fort Worth under a wide blue sky, with a pickup truck parked at the curb" loading="lazy" width="1600" height="1200"></figure>
</div></section>

<section class="sec" aria-labelledby="faq-h"><div class="w faq-g">
<h2 id="faq-h">Questions we answer every week</h2>
<div class="faq">{faq_items()}</div>
</div></section>

<section class="sec quote" id="quote" aria-labelledby="quote-h"><div class="w quote-g">
<div><h2 id="quote-h">Ask for a quote</h2><p>Send four details and an agent calls back the same business day. Bring your current policy to the call and we will read it with you.</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p></div>
{form()}
</div></section>
</main>
'''
    return head("preview-b.css", "family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&amp;family=Hanken+Grotesk:wght@400;500;700", "#A8124A") + body + footer_html("preview-b.js", data)


def absolutize(html):
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|tel:|mailto:|#|/|data:)", url):
            return m.group(0)
        return f'{attr}="{PREFIX}{url}"'
    return re.sub(r'\b(href|src|poster)="([^"]+)"', fix, html)


def write(name, html):
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1)
    if len(title) > 60 or "&" in title:
        PROBLEMS.append(f"{name}: title is {len(title)} chars")
    if not 120 <= len(desc) <= 160:
        PROBLEMS.append(f"{name}: description is {len(desc)} chars")
    if html.count("<h1") != 1:
        PROBLEMS.append(f"{name}: {html.count('<h1')} h1 elements")
    if 'alt=""' in html:
        PROBLEMS.append(f"{name}: empty alt text")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(absolutize(html))
    words = len(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S).split())
    print(f"  {name:20s} {len(html)//1024:>3} KB  {words:>5} words")


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    print("Building Sideoats previews:")
    write("preview-a.html", build_a())
    write("preview-b.html", build_b())
    if PROBLEMS:
        print("\n".join(PROBLEMS))
        sys.exit(1)
