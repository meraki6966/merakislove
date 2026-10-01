"""Build the Tessel Dental demo into public/demos/tessel/.

Run from the repo root:  python3 scripts/demos/tessel/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from td import *  # noqa: E402,F403
from content import (REVIEWS, HOME_FAQ, SERVICES_FAQ, SERVICE_PAGES, DENTISTS, INSURANCE_FAQ,  # noqa: E402
                     NEW_FAQ, AREA_FAQ, AREA_PAGES)

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "tessel")
# The home page is also served at the clean URL /demos/tessel (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/tessel/")
OUT = os.environ.get("OUT", OUT)


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


def keep_together(html):
    """Stop "I-485" breaking at its hyphen. Body text only, never the head."""
    head_part, sep, body_part = html.partition("<body>")
    body_part = re.sub(r">([^<]*)<", lambda m: ">" + m.group(1).replace("I-485", '<span class="nw">I-485</span>') + "<", body_part)
    return head_part + sep + body_part


def write(name, html):
    html = keep_together(absolutize(html))
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {name:32s} {len(html)//1024:>4} KB")


SVC = {s["slug"]: s for s in SERVICES}
CHECK = ic("check")
OFF = {o["slug"]: o for o in OFFICES}


# ---------------------------------------------------------------- blocks
def svc_cards(exclude=None):
    return "".join(f'''<a class="svc-card reveal" href="{s["slug"]}.html"><span class="ph"><img src="img/{s["img"]}.webp" alt="{IMG_ALT[s["img"]]}" loading="lazy" width="1400" height="1041"></span>
<span class="body"><span class="tag">{s["tag"]}</span><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Learn more{ic("arrow")}</span></span></a>'''
                   for s in SERVICES if s["slug"] != exclude)


def first_visit_steps(bg=""):
    steps = [("Book online or text us", "Pick an office and a time. We confirm by text within one business hour."),
             ("Fill out forms securely", "A private link lets you finish your health history at home in about ten minutes."),
             ("Meet your dentist", "X-rays, a full exam and a cleaning, with time to ask whatever you want."),
             ("Leave with a plan", "If anything needs work, you get a written plan with your cost before you decide.")]
    lis = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in steps)
    return f'''<section class="section {bg}" aria-labelledby="steps-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Your first visit</span><h2 class="h-lg" id="steps-h">Four steps, <span class="accent">no surprises.</span></h2></div>
<p class="small">New patients usually get in within a week. Emergencies are seen the same day.</p></div>
<ol class="steps">{lis}</ol></div></section>
'''


def worries_block():
    items = [
        ("“It's been years, and I'm embarrassed.”", "Most new patients tell us something like this. We start where you are, skip the lecture, and fix the most important thing first."),
        ("“I'm worried about a surprise bill.”", "You get a written estimate with your insurance share and your share before any treatment. The bill matches the estimate."),
        ("“Needles and drills make me tense.”", "Raise a hand and we stop. We numb the gum before the injection, play what you like in the room, and offer nitrous oxide for longer visits."),
        ("“I can't take a morning off work.”", "South End opens at 7:30 AM on weekdays and Ballantyne is open Saturday mornings. A checkup takes under an hour."),
    ]
    cards = "".join(f'<div class="worry reveal"><blockquote>{q}</blockquote><p>{a}</p></div>' for q, a in items)
    return f'''<section class="section dark" aria-labelledby="worry-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">What people tell us</span><h2 class="h-lg" id="worry-h">The worries we hear, <span class="accent">answered.</span></h2></div>
<p class="small">If any of these sound like you, mention it when you book. It changes how we plan your visit.</p></div>
<div class="worries">{cards}</div></div></section>
'''


def office_cards(heading=True):
    cards = ""
    for o in OFFICES:
        cards += f'''<article class="office reveal"><div class="ph"><img src="img/{o["img"]}.webp" alt="{IMG_ALT[o["img"]]}" loading="lazy" width="1800" height="1016"></div>
<div class="body"><h3>{o["name"]}</h3>{status_line(o)}
<dl><dt>Where</dt><dd>{o["where"]}</dd><dt>Parking</dt><dd>{o["parking"]}</dd><dt>Dentist</dt><dd>{o["dentist"]}</dd><dt>Close to</dt><dd>{o["serves"]}</dd></dl>
<div class="btn-row"><a class="btn btn-sea" href="?office={o["slug"]}#book">Book at {o["name"]}</a><a class="btn btn-line" href="{o["slug"]}.html">Office details</a></div></div></article>'''
    head_html = ('<div class="section-head"><div><span class="eyebrow">Two Charlotte offices</span><h2 class="h-lg" id="off-h">South End and <span class="accent">Ballantyne.</span></h2></div>'
                 '<p class="small">Your records are shared, so you can book at whichever office is easier that week.</p></div>') if heading else '<h2 class="sr-only" id="off-h">Our offices</h2>'
    return f'<section class="section" aria-labelledby="off-h"><div class="wrap">{head_html}<div class="offices">{cards}</div></div></section>\n'


def reviews_band(items, title='What patients <span class="accent">say.</span>', bg="white"):
    cards = "".join(review_card(*r) for r in items)
    return f'''<section class="section {bg}" aria-labelledby="rev-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Patient stories</span><h2 class="h-lg" id="rev-h">{title}</h2></div>
<p class="small">Sample reviews written for this demo. A live site would pull real ones from Google.</p></div>
<div class="reviews">{cards}</div></div></section>
'''


def doc_card(d, flip=False, h="h2"):
    bio = "".join(f"<p>{p}</p>" for p in d["bio"])
    creds = "".join(f"<li><b>{a}</b>{b}</li>" for a, b in d["creds"])
    img = f'<div class="media-wrap reveal"><div class="rounded" style="aspect-ratio:4/5"><img src="img/{d["img"]}.webp" alt="{d["name"]}, smiling in the office" loading="lazy" width="1100" height="1480"></div>{TILES}</div>'
    text = f'<div class="reveal"><span class="eyebrow">{d["role"]}</span><{h} class="h-lg" id="doc-{d["slug"]}">{d["name"]}</{h}><div style="margin-top:18px">{bio}</div><ul class="creds">{creds}</ul></div>'
    inner = text + img if flip else img + text
    return f'<div class="doc-card" id="{d["slug"]}">{inner}</div>'


def prices_list(rows, note="Self pay prices for this demo. With insurance, your share is usually lower."):
    lis = "".join(f"<li><b>{a}</b><span>{b}</span><strong>{c}</strong></li>" for a, b, c in rows)
    return f'<ul class="prices reveal">{lis}</ul><p class="fine">{note}</p>'


def carriers_strip():
    chips = "".join(f'<li class="chip">{c}</li>' for c in CARRIERS)
    return f'<section class="carriers" aria-label="Insurance accepted"><div class="wrap"><p>In network with most PPO plans</p><ul class="chips">{chips}</ul></div></section>\n'


# ---------------------------------------------------------------- pages
def build_home():
    today = "".join(f'<span><b style="display:inline;font-size:14px;margin-right:6px">{o["name"]}</b>{status_line(o)}</span>' for o in OFFICES)
    hero = f'''<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<span class="eyebrow">Dentist in Charlotte, NC</span>
<h1 class="h-xl">Calm, unhurried dentistry in <span class="accent">Charlotte.</span></h1>
<p class="lede" style="margin-top:20px">Cleanings, cosmetic work, implants and same day emergencies at two offices, South End and Ballantyne. Most PPO plans accepted, and a membership plan if you don't have insurance.</p>
<div class="btn-row"><a class="btn btn-sea" href="#book">Book online</a><a class="btn btn-line" href="tel:{TEL}">{ic("phone")}{PHONE}</a></div>
<ul class="hero-points"><li>{ic("check")}<span>New patients seen within a week</span></li><li>{ic("check")}<span>Written cost before any treatment</span></li><li>{ic("check")}<span>Open 7:30 AM weekdays and Saturday mornings</span></li></ul>
</div>
<div class="hero-media"><div class="frame"><img src="img/hero.webp" alt="A bright treatment room with a sage dental chair, white oak cabinets and a wall of soft green tile" fetchpriority="high" width="2000" height="1129"></div>
<div class="today"><b>Today at Tessel</b>{today}</div>{TILES}</div>
</div></section>
'''
    svc = f'''<section class="section white" aria-labelledby="svc-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">What we do</span><h2 class="h-lg" id="svc-h">Care for the whole family, <span class="accent">under one roof.</span></h2></div>
<p class="small">From a child's first checkup to a full implant, planned and done by the same small team.</p></div>
<div class="svc-grid">{svc_cards()}</div></div></section>
'''
    d = DENTISTS[0]
    doc = f'''<section class="section white" aria-labelledby="doc-sethuraman"><div class="wrap">{doc_card(d)}
<div style="margin-top:36px" class="btn-row"><a class="btn btn-line" href="our-dentists.html">Meet both dentists</a></div></div></section>
'''
    member = cta_band("No insurance? The membership plan covers the basics.",
                      "Two cleanings and exams, all routine x-rays and one emergency exam a year for $32 a month, plus 15% off everything else.")
    body = (hero + carriers_strip() + first_visit_steps() + svc + worries_block() + doc + office_cards()
            + reviews_band(REVIEWS[:3]) + member + faq_block("Before you book.", HOME_FAQ, "Quick answers to what new patients ask most.") + booking())
    schemas = [org_schema()] + [office_schema(o) for o in OFFICES] + [faq_schema(HOME_FAQ)]
    write("index.html", page("index.html", "Tessel Dental | Charlotte Dentist, South End and Ballantyne",
                             "Calm, unhurried dentistry at two Charlotte offices. Cleanings, cosmetic work, implants and same day emergencies. Most PPO plans accepted.",
                             schemas, "home", body))


def build_services_hub():
    family = f'''<section class="section" aria-labelledby="fam-h"><div class="wrap two-col">
<div class="media-wrap reveal"><div class="rounded" style="aspect-ratio:4/3"><img src="img/family.webp" alt="A young girl laughing in a dental chair while her father holds her hand and the dentist smiles" loading="lazy" width="1400" height="1041"></div>{TILES}</div>
<div class="reveal"><span class="eyebrow">Kids and families</span><h2 class="h-lg" id="fam-h">Back to back visits for <span class="accent">the whole family.</span></h2>
<p style="margin-top:18px">Book parents and kids in the same hour and you're done in one trip. Children's visits are short, start with a tour of the chair, and end with a prize from the tile box at the front desk.</p>
<ul class="checks" style="margin-top:20px"><li>{ic("check")}<span>First visit by age one or six months after the first tooth</span></li><li>{ic("check")}<span>Sealants and fluoride varnish to prevent cavities</span></li><li>{ic("check")}<span>Child cleaning and exam $149, or $24 a month on the membership plan</span></li></ul>
<div class="btn-row"><a class="btn btn-sea" href="?reason=child#book">Book a child's visit</a></div></div>
</div></section>
'''
    grid = f'''<section class="section white" aria-labelledby="all-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Our services</span><h2 class="h-lg" id="all-h">Four ways we <span class="accent">help.</span></h2></div>
<p class="small">Every visit starts with an exam, and every plan comes with a written cost.</p></div>
<div class="svc-grid">{svc_cards()}</div></div></section>
'''
    body = (page_hero("lobby", "Services", 'General, cosmetic and <span class="accent">emergency dentistry.</span>',
                      "Everything most families need from a dentist, at two Charlotte offices with the same team, the same prices and shared records.",
                      [("Home", "index.html"), ("Services", "")], "The Tessel waiting room with an oak bench, green tile wall and plants",
                      points=["Most PPO plans accepted", "Membership plan for patients without insurance"])
            + grid + family + first_visit_steps("white") + faq_block("About our services.", SERVICES_FAQ, "What people ask before their first appointment.", "") + booking())
    schemas = [org_schema(), faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")])]
    write("services.html", page("services.html", "Dental Services in Charlotte, NC | Tessel Dental",
                                "Cleanings, exams, cosmetic dentistry, dental implants and same day emergency care at Tessel Dental in South End and Ballantyne, Charlotte.",
                                schemas, "services", body))


def build_service(slug):
    s, c = SVC[slug], SERVICE_PAGES[slug]
    hero = page_hero(s["img"], c["eyebrow"], c["h1"], c["lede"], [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")],
                     c["alt"], points=c["points"], reason=s["reason"])
    if "steps" in c:
        lis = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in c["steps"])
        detail = f'<ol class="steps">{lis}</ol>'
    elif "timeline" in c:
        lis = "".join(f'<li class="reveal"><span class="when">{w}</span><b>{t}</b><p>{d}</p></li>' for t, w, d in c["timeline"])
        detail = f'<ol class="timeline" style="max-width:720px">{lis}</ol>'
    else:
        lis = "".join(f'<div class="callout{" sea" if i % 2 else ""} reveal">{ic("alert") if i == 3 else ic("check")}<div><h3>{t}</h3><p>{d}</p></div></div>' for i, (t, d) in enumerate(c["now"]))
        detail = f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px">{lis}</div>'
    how = f'''<section class="section white" aria-labelledby="how-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">{c["eyebrow"]}</span><h2 class="h-lg" id="how-h">{c["intro_h"]}</h2></div></div>
{detail}</div></section>
'''
    price = f'''<section class="section" aria-labelledby="price-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Clear prices</span><h2 class="h-lg" id="price-h">What it costs, <span class="accent">up front.</span></h2>
<p style="margin-top:18px">These are self pay prices. If you have insurance, we check your benefits first and give you your exact share in writing before treatment.</p>
<div class="callout sea" style="margin-top:24px">{ic("card")}<div><h3>No insurance?</h3><p>The membership plan takes 15% off this list and covers your cleanings and x-rays. <a href="insurance-financing.html">See the plan</a>.</p></div></div></div>
<div>{prices_list(c["prices"])}</div></div></section>
'''
    others = f'''<section class="section white" aria-labelledby="more-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Also at Tessel</span><h2 class="h-lg" id="more-h">Other services</h2></div></div>
<div class="svc-grid" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">{svc_cards(exclude=slug)}</div></div></section>
'''
    body = (hero + how + price + reviews_band([r for r in REVIEWS][:3], bg="") + others
            + faq_block(f'{s.get("plain", s["name"])}, <span class="accent">answered.</span>', c["faq"], "Straight answers to what patients ask us most.", "")
            + booking(preset=s["reason"]))
    schemas = [org_schema(), service_schema(s["name"], c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (s["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "services", body))


def build_dentists():
    docs = "".join(f'<section class="section{" white" if i == 0 else ""}" aria-labelledby="doc-{d["slug"]}"><div class="wrap">{doc_card(d, flip=bool(i))}</div></section>' for i, d in enumerate(DENTISTS))
    team = f'''<section class="section dark" aria-labelledby="team-h"><div class="wrap two-col top">
<div><span class="eyebrow">The rest of the team</span><h2 class="h-lg" id="team-h">Hygienists who <span class="accent">stay.</span></h2>
<p style="margin-top:18px">Our four hygienists have been with Tessel an average of six years, so most patients see the same person every visit. Two of them speak Spanish.</p></div>
<ul class="checks">{"".join(f"<li>{ic('check')}<span>{t}</span></li>" for t in ["Registered dental hygienists licensed in North Carolina", "CPR and medical emergency training every year", "Continuing education in gum disease and patient comfort", "Spanish spoken at both offices"])}</ul>
</div></section>
'''
    body = (page_hero("lobby", "Our dentists", 'Two dentists who <span class="accent">take their time.</span>',
                      "Dr. Sethuraman leads South End and Dr. Marchbanks leads Ballantyne. Both keep fewer patients a day so every visit has room for questions.",
                      [("Home", "index.html"), ("Our Dentists", "")], "The Tessel waiting room with an oak bench, green tile wall and plants")
            + docs + team + reviews_band(REVIEWS[3:6]) + booking())
    people = [{"@context": "https://schema.org", "@type": "Person", "name": d["name"].replace("Dr. ", ""), "honorificPrefix": "Dr.",
               "jobTitle": "General Dentist", "image": f"{BASE}/img/{d['img']}.webp", "worksFor": {"@id": f"{BASE}/#org"},
               "url": f"{BASE}/our-dentists.html#{d['slug']}"} for d in DENTISTS]
    schemas = [org_schema()] + people + [crumbs_schema([("Home", ""), ("Our Dentists", "our-dentists.html")])]
    write("our-dentists.html", page("our-dentists.html", "Our Dentists | Tessel Dental, Charlotte NC",
                                    "Meet Dr. Leena Sethuraman and Dr. Theo Marchbanks, the general dentists at Tessel Dental's South End and Ballantyne offices in Charlotte.",
                                    schemas, "dentists", body))


def build_insurance():
    chips = "".join(f'<li class="chip">{c}</li>' for c in CARRIERS)
    plans = [("Adult plan", "$32", "a month, or $349 a year", ["Two cleanings and exams", "All routine x-rays", "One emergency exam", "15% off all other treatment"]),
             ("Child plan", "$24", "a month, or $259 a year", ["Two cleanings and exams with fluoride", "All routine x-rays", "Sealants at 15% off", "One emergency exam"])]
    pl = "".join(f'<div class="plan reveal"><h3>{n}</h3><p class="price">{p} <small>{t}</small></p><ul>{"".join(f"<li>{CHECK}<span>{x}</span></li>" for x in li)}</ul></div>' for n, p, t, li in plans)
    body = (page_hero("svc-cleaning", "Insurance and financing", 'Know your cost <span class="accent">before you sit down.</span>',
                      "We check your benefits before your first visit and put your share in writing before any treatment. No insurance? There's a plan for that too.",
                      [("Home", "index.html"), ("Insurance", "")], "A hygienist cleaning a relaxed patient's teeth in a bright treatment room")
            + f'''<section class="section white" aria-labelledby="ins-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Insurance</span><h2 class="h-lg" id="ins-h">In network with <span class="accent">most PPO plans.</span></h2>
<p style="margin-top:18px">Being in network means you pay your plan's negotiated price, and your share is usually lower. If your plan isn't listed, we can still file the claim for you as an out of network provider.</p>
<ul class="chips" style="margin-top:20px">{chips}</ul></div>
<div class="reveal"><ol class="timeline">
<li><span class="when">When you book</span><b>Send your plan details</b><p>Your member ID and the employer or plan name are enough.</p></li>
<li><span class="when">Before your visit</span><b>We check your benefits</b><p>Coverage levels, deductible left and yearly maximum used so far.</p></li>
<li><span class="when">Before treatment</span><b>You get a written estimate</b><p>Your plan's share and your share, line by line.</p></li>
<li><span class="when">After your visit</span><b>We file the claim</b><p>You pay your share at the desk. We handle the paperwork.</p></li>
</ol></div></div></section>
<section class="section dark" aria-labelledby="mem-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">No insurance</span><h2 class="h-lg" id="mem-h">The Tessel <span class="accent">membership plan.</span></h2></div>
<p class="small">One yearly fee, no deductibles, no waiting periods, and no claim forms. Cancel any time after the first year.</p></div>
<div class="plans">{pl}</div></div></section>
<section class="section" aria-labelledby="self-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Self pay and financing</span><h2 class="h-lg" id="self-h">Prices you can <span class="accent">plan around.</span></h2>
<p style="margin-top:18px">We accept cash, all major cards, and HSA and FSA cards. For larger treatment, monthly payment plans are available on approved credit, including 0% options for 6 to 12 months.</p>
<div class="callout" style="margin-top:24px">{ic("card")}<div><h3>Splitting a big plan</h3><p>We can stage treatment across two benefit years so your insurance pays its maximum twice. Ask about it at your consult.</p></div></div></div>
<div>{prices_list([("New patient visit", "Exam, full x-rays and cleaning", "$289"), ("Emergency exam with x-ray", "Diagnosis and a written plan", "$119"), ("Tooth colored filling", "Per tooth", "From $185"), ("Porcelain crown", "Per tooth", "From $1,250"), ("In office whitening", "One 90 minute visit", "$495"), ("Single implant with crown", "Post, abutment and crown", "From $4,300")])}</div>
</div></section>
''' + faq_block("Insurance and payment.", INSURANCE_FAQ, "Common questions about plans, bills and payment.") + booking())
    schemas = [org_schema(), faq_schema(INSURANCE_FAQ), crumbs_schema([("Home", ""), ("Insurance and Financing", "insurance-financing.html")])]
    write("insurance-financing.html", page("insurance-financing.html", "Dental Insurance and Membership Plan | Tessel Dental",
                                           "Tessel Dental is in network with most PPO dental plans in Charlotte. No insurance? Our membership plan starts at $32 a month. Self pay prices and financing.",
                                           schemas, "insurance", body))


def build_new_patients():
    protect = ["The whole site runs on HTTPS, with strict transport security so browsers never fall back to an unencrypted connection.",
               "Health history goes through an encrypted intake service covered by a business associate agreement, never by email.",
               "No ad trackers or tracking pixels on any page that asks about your health.",
               "The patient portal requires a second sign in step, a code sent to your phone.",
               "Staff accounts are limited by role, and every view of a patient record is logged.",
               "We check the site's security headers and forms on a schedule, and fix what we find."]
    intake = f'''<section class="section white" aria-labelledby="intake-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Secure intake</span><h2 class="h-lg" id="intake-h">Your health history <span class="accent">stays private.</span></h2>
<p style="margin-top:18px">A dental website collects some of the most personal information a business can hold: medications, conditions, allergies, insurance IDs. So the forms on this site are built around one rule. Health details never travel by email and never sit in a website inbox.</p>
<ul class="checks" style="margin-top:22px">{"".join(f"<li>{ic('shield')}<span>{t}</span></li>" for t in protect)}</ul></div>
<form class="intake reveal" action="#intake-h" method="post" novalidate data-demo aria-label="Secure intake preview">
<div class="lockbar">{ic("lock")}Encrypted form preview</div>
<p class="step" style="margin:0">Health history, step 1 of 4</p>
<div class="fields">
<label class="field">Legal name<input type="text" name="legal_name" autocomplete="name"></label>
<label class="field">Date of birth<input type="text" name="dob" inputmode="numeric" placeholder="MM/DD/YYYY" autocomplete="bday"></label>
</div>
<label class="field">Current medications<textarea name="meds" rows="3"></textarea></label>
<label class="field">Allergies<input type="text" name="allergies"></label>
<button class="btn btn-sea" type="submit">Save and continue</button>
<div class="form-done" role="status">This is a demo, so nothing was saved. On a live Tessel site, this form posts to an encrypted, HIPAA compliant intake service, and the link expires after one use.</div>
</form>
</div></section>
'''
    timeline = f'''<section class="section" aria-labelledby="prep-h"><div class="wrap two-col top">
<div class="media-wrap reveal"><div class="rounded" style="aspect-ratio:4/3"><img src="img/lobby.webp" alt="The Tessel waiting room with an oak bench, green tile wall and plants" loading="lazy" width="1400" height="1041"></div>{TILES}</div>
<div class="reveal"><span class="eyebrow">Before you come in</span><h2 class="h-lg" id="prep-h">What to expect, <span class="accent">step by step.</span></h2>
<ol class="timeline" style="margin-top:28px">
<li><span class="when">After you book</span><b>A text to confirm</b><p>Within one business hour, with the office address and parking details.</p></li>
<li><span class="when">Two days before</span><b>Your secure forms link</b><p>About ten minutes on your phone. The link works once and expires after seven days.</p></li>
<li><span class="when">The day of</span><b>Bring your ID and insurance card</b><p>Plus a list of medications if you didn't add them to the form.</p></li>
<li><span class="when">At the visit</span><b>About an hour</b><p>X-rays, exam, cleaning and a conversation about anything we find.</p></li>
</ol></div></div></section>
'''
    body = (page_hero("intake", "New patients", 'Welcome. Here’s how your <span class="accent">first visit works.</span>',
                      "Book online, finish your forms securely at home, and walk in ready. Most new patients are seen within a week.",
                      [("Home", "index.html"), ("New Patients", "")], "A tablet, reading glasses and a cup of tea on an oak desk in soft morning light",
                      points=["Forms done from your phone in ten minutes", "Benefits checked before you arrive"], reason="cleaning")
            + timeline + intake + faq_block("New patient questions.", NEW_FAQ, "Everything people ask before their first appointment.", "") + booking(preset="cleaning"))
    schemas = [org_schema(), faq_schema(NEW_FAQ), crumbs_schema([("Home", ""), ("New Patients", "new-patients.html")])]
    write("new-patients.html", page("new-patients.html", "New Patients | Tessel Dental, Charlotte NC",
                                    "New to Tessel Dental? Book online, complete secure health forms from home, and see what happens at your first visit in South End or Ballantyne.",
                                    schemas, "new", body))


def build_offices_hub():
    compare = f'''<section class="section white" aria-labelledby="pick-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Choosing an office</span><h2 class="h-lg" id="pick-h">Which one <span class="accent">fits your week?</span></h2></div></div>
<div class="two-col top">
<div class="callout sea reveal">{ic("train")}<div><h3>Pick South End if</h3><p>you live or work in Dilworth, Myers Park, Wilmore or uptown, ride the light rail, or want a 7:30 AM appointment before work.</p></div></div>
<div class="callout reveal">{ic("car")}<div><h3>Pick Ballantyne if</h3><p>you're in south Charlotte, Marvin or Fort Mill, want parking at the door, need a Saturday morning, or are planning an implant.</p></div></div>
</div></div></section>
'''
    body = (page_hero("office-south-end", "Our offices", 'Two offices, <span class="accent">one team.</span>',
                      "South End on the Rail Trail and Ballantyne off I-485. Same dentists, same prices, shared records.",
                      [("Home", "index.html"), ("Offices", "")], "The Tessel South End office, a red brick building beside the Rail Trail")
            + office_cards(heading=False) + compare + faq_block("About our offices.", HOME_FAQ[4:5] + AREA_FAQ["south-end"][:2] + AREA_FAQ["ballantyne"][:1], "Parking, transit and hours.", "") + booking())
    qa = HOME_FAQ[4:5] + AREA_FAQ["south-end"][:2] + AREA_FAQ["ballantyne"][:1]
    schemas = [org_schema()] + [office_schema(o) for o in OFFICES] + [faq_schema(qa), crumbs_schema([("Home", ""), ("Offices", "offices.html")])]
    write("offices.html", page("offices.html", "Dentist Offices in South End and Ballantyne | Tessel",
                               "Tessel Dental has two Charlotte offices: South End on the Rail Trail near the East/West Blvd light rail station, and Ballantyne off I-485 with Saturday hours.",
                               schemas, "offices", body))


def office_detail(o):
    return f'''<section class="section white" aria-labelledby="visit-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Visit us</span><h2 class="h-lg" id="visit-h">Hours and <span class="accent">getting here.</span></h2>
<p style="margin-top:18px">{o["getting"]}</p>
<ul class="checks" style="margin-top:20px"><li>{ic("pin")}<span>{o["where"]}</span></li><li>{ic("car")}<span>{o["parking"]}</span></li><li>{ic("train") if o["slug"] == "south-end" else ic("clock")}<span>{o["transit"]}</span></li></ul>
<p style="margin-top:20px">{status_line(o)}</p></div>
<div class="reveal">{hours_table(o)}<p class="fine">Emergency slots open every weekday morning. After hours, call {PHONE} and choose option 2.</p></div>
</div></section>
'''


def hoods_block(hoods, title):
    cells = "".join(f'<div class="hood reveal"><b>{n}</b><span>{t}</span></div>' for n, t in hoods)
    return f'''<section class="section" aria-labelledby="hood-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Neighborhoods</span><h2 class="h-lg" id="hood-h">{title}</h2></div></div>
<div class="hoods">{cells}</div></div></section>
'''


def build_office(slug):
    o, c = OFF[slug], AREA_PAGES[slug]
    d = DENTISTS[0] if slug == "south-end" else DENTISTS[1]
    about = "".join(f"<p>{p}</p>" for p in c["about"])
    story = f'''<section class="section" aria-labelledby="about-h"><div class="wrap two-col">
<div class="reveal"><span class="eyebrow">About this office</span><h2 class="h-lg" id="about-h">The {o["name"]} <span class="accent">office.</span></h2><div style="margin-top:18px">{about}</div>
<div class="btn-row"><a class="btn btn-line" href="our-dentists.html#{d["slug"]}">Meet {d["name"]}</a></div></div>
<div class="media-wrap reveal"><div class="rounded" style="aspect-ratio:4/5;max-width:420px;margin-left:auto"><img src="img/{d["img"]}.webp" alt="{d["name"]}, smiling in the office" loading="lazy" width="1100" height="1480"></div>{TILES}</div>
</div></section>
'''
    revs = [r for r in REVIEWS if (r[2] in ("South End", "Dilworth", "Wilmore", "Myers Park")) == (slug == "south-end")][:3]
    body = (page_hero(o["img"], f"{o['name']} office", c["h1"], c["lede"], [("Home", "index.html"), ("Offices", "offices.html"), (o["name"], "")],
                      c["alt"], points=[hours_summary(o)])
            + office_detail(o) + story + hoods_block(c["hoods"], f'Close to <span class="accent">{o["name"]}.</span>')
            + reviews_band(revs, title=f'From {o["name"]} <span class="accent">patients.</span>')
            + faq_block(f'The {o["name"]} office, <span class="accent">answered.</span>', AREA_FAQ[slug], "Parking, hours and getting here.", "")
            + booking(office=slug, title=f'Book at <span class="accent">{o["name"]}.</span>'))
    schemas = [office_schema(o), org_schema(), faq_schema(AREA_FAQ[slug]),
               crumbs_schema([("Home", ""), ("Offices", "offices.html"), (o["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "offices", body))


def build_myers_park():
    o = OFF["south-end"]
    route = f'''<section class="section white" aria-labelledby="route-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">From Myers Park</span><h2 class="h-lg" id="route-h">About ten minutes to <span class="accent">South End.</span></h2>
<p style="margin-top:18px">Myers Park doesn't have a Tessel office of its own, but our South End office is a short drive away. Most patients come down Queens Road or Kings Drive past Freedom Park and are parked in about ten minutes.</p>
<p>Students and staff at Queens University often book the 7:30 AM slots and are back on campus before a 9 AM class.</p>
<ul class="checks" style="margin-top:20px"><li>{ic("car")}<span>Garage behind the building, two hours validated</span></li><li>{ic("clock")}<span>{hours_summary(o)}</span></li><li>{ic("pin")}<span>Serving Myers Park in 28207 and 28209</span></li></ul></div>
<div class="reveal">{hours_table(o)}<p style="margin-top:16px">{status_line(o)}</p></div>
</div></section>
'''
    why = f'''<section class="section" aria-labelledby="why-h"><div class="wrap">
<div class="section-head"><div><span class="eyebrow">Why Myers Park patients come to us</span><h2 class="h-lg" id="why-h">Close, early and <span class="accent">in network.</span></h2></div></div>
<div class="steps" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
<div class="reveal" style="background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px"><h3 class="h-md">Early starts</h3><p class="small" style="margin-top:8px">Checkups from 7:30 AM, so the visit fits before work or school drop off.</p></div>
<div class="reveal" style="background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px"><h3 class="h-md">Most PPO plans</h3><p class="small" style="margin-top:8px">Delta Dental, Cigna, MetLife, Aetna, Blue Cross NC and more, with benefits checked ahead of time.</p></div>
<div class="reveal" style="background:#fff;border:1px solid var(--line);border-radius:20px;padding:28px"><h3 class="h-md">Family visits</h3><p class="small" style="margin-top:8px">Back to back appointments for parents and kids, done in one trip.</p></div>
</div></div></section>
'''
    body = (page_hero("office-south-end", "Myers Park patients", 'A dentist close to <span class="accent">Myers Park.</span>',
                      "Our South End office is about ten minutes from Myers Park, with early weekday hours, validated parking and most PPO plans accepted.",
                      [("Home", "index.html"), ("Offices", "offices.html"), ("Myers Park", "")],
                      "The Tessel South End office, a red brick building beside the Rail Trail")
            + route + why + reviews_band([REVIEWS[5], REVIEWS[0], REVIEWS[1]], title='From our <span class="accent">neighbors.</span>')
            + faq_block('Myers Park patients, <span class="accent">answered.</span>', AREA_FAQ["myers-park"], "Directions, parking and hours.", "")
            + booking(office="south-end", title='Book at <span class="accent">South End.</span>'))
    schemas = [office_schema(o), org_schema(), faq_schema(AREA_FAQ["myers-park"]),
               crumbs_schema([("Home", ""), ("Offices", "offices.html"), ("Myers Park", "myers-park.html")])]
    write("myers-park.html", page("myers-park.html", "Dentist near Myers Park, Charlotte NC | Tessel Dental",
                                  "Tessel Dental's South End office is about ten minutes from Myers Park, with 7:30 AM weekday appointments, validated parking and most PPO plans accepted.",
                                  schemas, "offices", body))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Building Tessel demo:")
    build_home()
    build_services_hub()
    for s in SERVICES:
        build_service(s["slug"])
    build_dentists()
    build_insurance()
    build_new_patients()
    build_offices_hub()
    for o in OFFICES:
        build_office(o["slug"])
    build_myers_park()
