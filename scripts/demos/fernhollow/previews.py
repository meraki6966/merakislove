"""Two home page previews for the Fernhollow Veterinary Clinic demo, for Adam to choose between.

Run from the repo root:  python3 scripts/demos/fernhollow/previews.py
Writes preview-a.html (The Field Guide) and preview-b.html (Can It Wait) into
public/demos/fernhollow/. Both are noindex and are not linked from anywhere.

Fernhollow is a fictional clinic. Portland, Sellwood, DoveLewis, the ASPCA
poison line, Oregon's rabies rule and the Multnomah County license fees are
real, checked in October 2026.
"""
import json
import os
import re
import sys
from html import escape

BRAND = "Fernhollow Veterinary Clinic"
PHONE = "(503) 555-0146"            # 555-01xx is reserved for fiction
TEL = "+15035550146"
BASE = "https://merakislove.com/demos/fernhollow"
PREFIX = "/demos/fernhollow/"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "fernhollow")
ER = {"name": "DoveLewis", "full": "DoveLewis Veterinary Emergency and Specialty Hospital", "addr": "1945 NW Pettygrove Street", "phone": "(503) 228-7281", "tel": "+15032287281"}
POISON = {"phone": "(888) 426-4435", "tel": "+18884264435"}
PROBLEMS = []

TITLE = "Veterinarian in Sellwood, Portland | Fernhollow Vet"
DESC = ("Fernhollow is a dog and cat veterinary clinic in Sellwood, Portland. Same day sick visits, prices on the page, "
        "and a plain guide to what can wait until morning.")
NAV = [("#watch", "What to watch for"), ("#prices", "Prices"), ("#team", "Our team"), ("#visit", "Visit")]

# A fern frond: one stem with paired leaflets.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M22 40V8" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" fill="none"/>'
        '<path d="M22 34c-6-1-10-4-12-9M22 34c6-1 10-4 12-9M22 27c-5-1-8-3-10-7M22 27c5-1 8-3 10-7M22 20c-4-1-6-3-7-6M22 20c4-1 6-3 7-6M22 13c-2-1-4-2-4-5M22 13c2-1 4-2 4-5" '
        'stroke="currentColor" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg>')

TRIAGE = {
    "dog": {
        "go": ["Trouble breathing, or gums that look pale, white or blue", "Collapse, or a seizure that lasts more than a few minutes",
               "A swollen belly with retching and nothing coming up", "Hit by a car, even if they seem fine",
               "Ate rat bait, antifreeze, xylitol gum, grapes or a lot of chocolate", "Bleeding that will not stop"],
        "today": ["Vomiting or diarrhea more than twice in a day", "Ate raw salmon or trout, even with no symptoms yet",
                  "Squinting, or a red or cloudy eye", "Sudden head shaking or sneezing fits after a walk in tall grass",
                  "Limping that has not improved after a day of rest", "Not eating for a full day"],
        "week": ["Itchy skin, ear scratching or licking paws", "Bad breath or a broken tooth", "Stiffness getting up or on stairs",
                 "A new lump", "Weight gain or loss you can see", "Vaccines, a nail trim or a refill"],
    },
    "cat": {
        "go": ["Trouble breathing, or breathing with the mouth open", "A male cat straining in the litter box with little or no urine",
               "Chewed or licked any part of a lily, even the pollen", "Collapse, or a seizure that lasts more than a few minutes",
               "A fall from a window or balcony, even if they seem fine", "Licked antifreeze or ate rat bait"],
        "today": ["Not eating for a full day", "Vomiting more than twice in a day", "Hiding and not coming out for meals",
                  "Squinting, or a red or cloudy eye", "Urinating outside the box, or going much more often", "A bite wound or swelling after a fight"],
        "week": ["Bad breath or drooling", "Drinking more water than usual", "Weight loss you can feel along the spine",
                 "A new lump", "Matted fur or dandruff", "Vaccines, a nail trim or a refill"],
    },
}

# name, who it affects, first month, last month (1 to 12, may wrap), what you see, what to do, image
HAZARDS = [
    ("Raw salmon and trout", "dog", 9, 12, "Vomiting, fever and swollen glands within six days of eating raw fish from a river or a cooler.",
     "Call us the day it happens. Treated early with an antibiotic and a wormer, most dogs improve within two days. Without treatment, nine in ten sick dogs die.", "salmon"),
    ("Foxtails and grass seeds", "dog", 6, 9, "Sudden head shaking, sneezing fits, or licking at one paw after a walk through dry grass.",
     "Call the same day. The barbed seed only travels one way, and it has to be found and removed.", "foxtail"),
    ("Wild mushrooms", "dog", 10, 12, "Drooling, vomiting or wobbling after time in the yard or on a trail once the fall rains start.",
     "Go to the emergency hospital and bring a photo of the mushroom. Some kinds that grow here damage the liver.", "mushroom"),
    ("River algae", "dog", 7, 9, "Green scum or paint like streaks on slow water. The Willamette around Ross Island gets advisories in late summer.",
     "Keep dogs out of the water during an advisory. If your dog swam or drank and seems weak or is vomiting, go to the emergency hospital.", None),
    ("Lilies", "cat", 3, 5, "A bouquet or a potted Easter lily in the house. Every part is toxic to cats, including the pollen and the vase water.",
     "Go to the emergency hospital right away, even if your cat seems fine. Treatment in the first hours protects the kidneys.", "lily"),
    ("Antifreeze", "both", 11, 2, "A sweet tasting puddle under a car in the driveway or garage during the cold months.",
     "Go to the emergency hospital right away. A very small amount is dangerous to a cat or a dog.", None),
    ("Fleas", "both", 1, 12, "Scratching, scabs along the back, or black specks in the coat. Portland winters are mild enough for fleas to live all year.",
     "Keep prevention going every month, including for indoor cats. Ask us which product fits your pet.", None),
]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
FULL = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

PRICES = [("Wellness exam", "A full nose to tail exam and a written plan", "$78"),
          ("Puppy or kitten first visit", "Forty minutes, with time for every question", "$65"),
          ("Same day sick visit", "Call before 3 PM and we see your pet today", "$95"),
          ("Rabies vaccine", "With the certificate Multnomah County asks for", "$32"),
          ("Dental cleaning", "With anesthesia, monitoring and full mouth x-rays", "From $520"),
          ("Nail trim", "No appointment needed on weekdays", "$24")]

TEAM = [("Dr. Maren Halvorsen", "Veterinarian and owner", "Maren opened Fernhollow in 2012 after ten years in emergency medicine. She still takes the hard cases, and she writes down the price before any treatment starts."),
        ("Dr. Caleb Thornquist", "Veterinarian", "Caleb sees most of our cats and runs the dental suite. He keeps a second, quieter exam room for cats who would prefer to skip the lobby."),
        ("Junie Akana", "Certified veterinary technician", "Junie is the voice on the phone when you call worried. She has helped more Sellwood owners decide between tonight and tomorrow than anyone on staff.")]

HOME_FAQ = [
    ("Are you taking new patients?", "Yes. We see dogs and cats, and most first visits are booked within the week. A puppy or kitten first visit is forty minutes, so there is time for every question."),
    ("What should I do if my pet has an emergency after hours?",
     f'Go to {ER["full"]} at {ER["addr"]} in Northwest Portland. It is open 24 hours every day, and the number is <a href="tel:{ER["tel"]}">{ER["phone"]}</a>. '
     f'If you think your pet ate something toxic, the ASPCA Animal Poison Control Center answers at <a href="tel:{POISON["tel"]}">{POISON["phone"]}</a> day and night. A consultation fee may apply.'),
    ("How much does an exam cost?", "A wellness exam is $78 and a same day sick visit is $95. Anything beyond the exam gets a written estimate first, and you approve it before we start."),
    ("Does my dog need a rabies vaccine in Oregon?", "Yes. Oregon requires dogs to be vaccinated against rabies by six months of age. Multnomah County also licenses dogs and cats, and asks for a current rabies certificate. We hand you the certificate at the visit."),
    ("What is salmon poisoning?", "It is an infection dogs get from a parasite in raw salmon, trout and other fish that run upstream, and it is most common west of the Cascades. Signs show up within six days. It is treatable when caught early, so call us the day your dog eats raw fish."),
    ("Is the clinic calm for cats?", "We try to make it so. Cats have their own waiting nook away from the dogs and a quiet exam room at the back, and we book cat visits at the slower times of day when we can."),
]


def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def schemas():
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/", "logo": f"{BASE}/img/og.jpg",
           "telephone": "+1-503-555-0146", "foundingDate": "2012", "founder": {"@type": "Person", "name": "Maren Halvorsen", "jobTitle": "Veterinarian"}}
    biz = {"@context": "https://schema.org", "@type": "VeterinaryCare", "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
           "telephone": "+1-503-555-0146", "image": f"{BASE}/img/og.jpg", "priceRange": "$$",
           "address": {"@type": "PostalAddress", "addressLocality": "Portland", "addressRegion": "OR", "postalCode": "97202", "addressCountry": "US"},
           "areaServed": [{"@type": "Place", "name": n} for n in ["Sellwood, Portland", "Westmoreland, Portland", "Eastmoreland, Portland", "Woodstock, Portland"]],
           "openingHoursSpecification": [
               {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "07:30", "closes": "18:00"},
               {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "09:00", "closes": "14:00"}],
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


def species_switch(label="Show the guide for"):
    return (f'<div class="species" role="group" aria-label="{label}"><span>{label}</span>'
            '<button type="button" data-species="dog" aria-pressed="true">Dogs</button>'
            '<button type="button" data-species="cat" aria-pressed="false">Cats</button></div>')


def faq_items():
    return "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(HOME_FAQ))


def hours_table():
    rows = [("Monday to Friday", "7:30 AM to 6 PM"), ("Saturday", "9 AM to 2 PM"), ("Sunday", "Closed")]
    body = "".join(f'<tr><th scope="row">{d}</th><td>{h}</td></tr>' for d, h in rows)
    return f'<table class="hours"><caption>Clinic hours, Pacific time</caption><tbody>{body}</tbody></table>'


def form():
    return f'''<form class="form" action="#book" method="post" novalidate data-demo>
<fieldset><legend>Who is the visit for?</legend><div class="choices">
<label class="choice"><input type="radio" name="pet" value="dog">A dog</label>
<label class="choice"><input type="radio" name="pet" value="cat">A cat</label></div></fieldset>
<div class="fields">
<label>Your pet's name<input type="text" name="petname"></label>
<label>What is going on?<select name="reason"><option>Wellness exam</option><option>Sick visit</option><option>Vaccines</option><option>Dental</option><option>Something else</option></select></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Phone<input type="tel" name="phone" autocomplete="tel"></label>
<label class="full">Email<input type="email" name="email" autocomplete="email"></label>
</div>
<button class="btn" type="submit">Request a visit</button>
<p class="form-note">If your pet needs to be seen today, please call instead. We answer the phone faster than we answer forms.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live Fernhollow site, the front desk calls back within two business hours to confirm a time.</p>
</form>'''


def footer_html():
    data = json.dumps({"er": {"name": ER["name"], "phone": ER["phone"], "tel": ER["tel"]}}).replace("</", "<\\/")
    return f'''<footer class="ft"><div class="w">
<div class="ft-cols">
<div><h2>Fernhollow Veterinary Clinic</h2><address>Sellwood, Portland, OR 97202<br><a href="tel:{TEL}">{PHONE}</a><br>Monday to Friday, 7:30 AM to 6 PM<br>Saturday, 9 AM to 2 PM</address></div>
<div><h2>After hours</h2><address>{ER["full"]}<br>{ER["addr"]}, Portland<br><a href="tel:{ER["tel"]}">{ER["phone"]}</a><br>Open 24 hours, every day</address></div>
<div><h2>Poison questions</h2><address>ASPCA Animal Poison Control Center<br><a href="tel:{POISON["tel"]}">{POISON["phone"]}</a><br>Day and night. A fee may apply.</address></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. Fernhollow is a fictional clinic, its people and prices are samples, and nothing here replaces an exam by your own veterinarian. DoveLewis and the ASPCA poison line are real and are not affiliated with this demo.</p>
</div></footer>
<script type="application/json" id="data">{data}</script>
<script src="assets/preview.js" defer></script>
</body>
</html>
'''


def in_months(first, last):
    """Month numbers a hazard covers, allowing a range that wraps past December."""
    if first <= last:
        return list(range(first, last + 1))
    return list(range(first, 13)) + list(range(1, last + 1))


def season_text(first, last):
    if (first, last) == (1, 12):
        return "All year"
    return f"{FULL[first - 1]} to {FULL[last - 1]}"


# ------------------------------------------------------------------ Preview A
# Callouts on the specimen plates: label, note, x and y of the point on the
# animal (percent of the image), and which side the label sits on.
CALLOUTS = {
    "dog": [("Ears", "Checked at every visit. Foxtails hide here from June to September.", 30, 17, "l"),
            ("Teeth", "Looked at yearly and cleaned when they need it.", 15, 29, "l"),
            ("Heart and lungs", "Listened to before any vaccine or anesthesia.", 36, 48, "r"),
            ("Weight", "Recorded on every chart, so a slow change gets noticed.", 64, 34, "r"),
            ("Paws", "Checked between the toes for grass seeds and cracked pads.", 36, 86, "l")],
    "cat": [("Ears and eyes", "Clean ears and clear, even eyes. Squinting in a cat is a same day call.", 24.3, 34.3, "l"),
            ("Teeth and gums", "Dental disease is common in adult cats, and it hides well.", 18, 46.8, "l"),
            ("Heart", "Listened to at every visit. Murmurs are common and worth tracking.", 33.3, 56.5, "r"),
            ("Kidneys", "Bloodwork from age seven catches changes early.", 59, 48.2, "r"),
            ("Weight", "A pound lost on a cat is a lot. We weigh every time.", 47.2, 62.6, "r")],
}
PLATE = {"dog": ("plate-dog", "A gouache illustration of a scruffy tan and white mixed breed dog in side profile",
                 "Plate 1. The Portland dog, with five things we check at every visit."),
         "cat": ("plate-cat", "A gouache illustration of a grey tabby cat walking in side profile",
                 "Plate 1. The Portland cat, with five things we check at every visit.")}


def plate(sp):
    img, alt, cap = PLATE[sp]
    marks = ""
    for i, (name, note, x, y, side) in enumerate(CALLOUTS[sp]):
        marks += f'<li class="co {side}" style="--x:{x}%;--y:{y}%"><span class="pt" aria-hidden="true">{i + 1}</span></li>'
    notes = "".join(f'<li><span class="n" aria-hidden="true">{i + 1}</span><div><h3>{name}</h3><p>{note}</p></div></li>' for i, (name, note, _, _, _) in enumerate(CALLOUTS[sp]))
    hidden = "" if sp == "dog" else " hidden"
    load = ' fetchpriority="high"' if sp == "dog" else ' loading="lazy"'
    return (f'<figure class="plate" data-for="{sp}"{hidden}><div class="plate-img"><img src="img/{img}.webp" alt="{alt}" width="1600" height="1200"{load}>'
            f'<ol class="marks">{marks}</ol></div>'
            f'<figcaption>{cap}</figcaption><ol class="notes">{notes}</ol></figure>')


def entry(i, h):
    name, who, first, last, see, do, img = h
    pic = f'<img src="img/{img}.webp" alt="A field guide illustration of {name.lower()}" loading="lazy" width="1200" height="1200">' if img else ""
    cls = "entry" if img else "entry plain"
    cells = "".join(f'<span class="{"on" if m in in_months(first, last) else ""}">{MONTHS[m - 1][0]}</span>' for m in range(1, 13))
    return (f'<article class="{cls}" data-who="{who}">{pic}<div><h3>{name}</h3>'
            f'<p class="when"><span class="yr" role="img" aria-label="{season_text(first, last)}">{cells}</span>{season_text(first, last)}</p>'
            f'<dl><dt>What you see</dt><dd>{see}</dd><dt>What to do</dt><dd>{do}</dd></dl></div></article>')


def build_a():
    entries = "".join(entry(i, h) for i, h in enumerate(HAZARDS) if h[6])
    plain = "".join(entry(i, h) for i, h in enumerate(HAZARDS) if not h[6])
    prices = "".join(f'<tr><th scope="row">{n}</th><td>{d}</td><td class="amt">{p}</td></tr>' for n, d, p in PRICES)
    team = "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in TEAM)
    go = {sp: "".join(f"<li>{t}</li>" for t in TRIAGE[sp]["go"]) for sp in TRIAGE}
    body = f'''{ribbon("A, The Field Guide", "preview-b.html", "preview B, Can It Wait")}<header class="hd"><div class="w hd-in">
<a class="mark" href="preview-a.html" aria-label="{BRAND}, home">{MARK}<span>Fernhollow <small>Veterinary Clinic</small></span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="tel" href="tel:{TEL}">{PHONE}</a>
</div></header>
<main id="main">
<section class="hero"><div class="w hero-g">
<div class="hero-copy">
<h1>A field guide to keeping a Portland pet well.</h1>
<p class="lede">Fernhollow is a veterinary clinic for dogs and cats in Sellwood. This page is the short version of what we tell every new client: what we check, what to watch for in this city, and when to call.</p>
{species_switch()}
<div class="acts"><a class="btn" href="#book">Book a visit</a><a class="call" href="tel:{TEL}">or call {PHONE}</a></div>
<p class="open" data-open>Open Monday to Friday 7:30 AM to 6 PM, and Saturday 9 AM to 2 PM.</p>
</div>
{plate("dog")}{plate("cat")}
</div></section>

<section class="sec" id="watch" aria-labelledby="watch-h"><div class="w">
<div class="sec-hd"><h2 id="watch-h">What should a Portland pet owner watch for?</h2>
<p>Seven things we see every year in this city, with the months they show up. The bar beside each one runs January to December.</p></div>
<div class="entries">{entries}</div>
<div class="entries three">{plain}</div>
</div></section>

<section class="sec alt" aria-labelledby="wait-h"><div class="w wait-g">
<div><h2 id="wait-h">Which signs cannot wait?</h2>
<p>If you see any of these, skip the appointment line and go straight to an emergency hospital. After hours, that is {ER["name"]} in Northwest Portland, open 24 hours every day.</p>
<p class="er"><a href="tel:{ER["tel"]}">{ER["phone"]}</a><span>{ER["full"]}, {ER["addr"]}</span></p>
<p class="fine">This list is general guidance and cannot examine your pet. If you are unsure, call us during the day or {ER["name"]} at night.</p></div>
<div><ul class="cannot" data-for="dog">{go["dog"]}</ul><ul class="cannot" data-for="cat" hidden>{go["cat"]}</ul></div>
</div></section>

<section class="sec" id="prices" aria-labelledby="price-h"><div class="w">
<div class="sec-hd"><h2 id="price-h">How much does a visit cost?</h2><p>Sample prices for this demo. Anything beyond the exam gets a written estimate first.</p></div>
<div class="tw"><table class="prices"><caption>Fernhollow sample prices</caption><thead><tr><th scope="col">Visit</th><th scope="col">What it covers</th><th scope="col" class="amt">Price</th></tr></thead><tbody>{prices}</tbody></table></div>
</div></section>

<section class="sec alt" id="team" aria-labelledby="team-h"><div class="w team-g">
<figure><img src="img/exam.webp" alt="A veterinarian in navy scrubs kneeling on an exam room floor, looking into the ear of a calm golden retriever mix" loading="lazy" width="1600" height="1200"><figcaption>Most of our exams happen on the floor, where the dog already is.</figcaption></figure>
<div><h2 id="team-h">Who will see your pet?</h2><ul class="team">{team}</ul><p class="fine">Fictional people, written for this demo.</p></div>
</div></section>

<section class="sec" id="visit" aria-labelledby="visit-h"><div class="w visit-g">
<div><h2 id="visit-h">Where is the clinic?</h2>
<p>We are in a green bungalow in Sellwood, a few blocks from the bridge and a short walk from the off leash area at Sellwood Riverfront Park. There is parking behind the building and a covered porch for rainy day waits.</p>
{hours_table()}</div>
<figure><img src="img/exterior.webp" alt="A green craftsman bungalow clinic on a rainy Sellwood street, with a person in a yellow rain jacket walking a dog toward the porch" loading="lazy" width="1600" height="1200"></figure>
</div></section>

<section class="sec alt" aria-labelledby="faq-h"><div class="w faq-g">
<div><h2 id="faq-h">Questions new clients ask</h2><p>Call <a href="tel:{TEL}">{PHONE}</a> if yours is not here.</p></div>
<div class="faq">{faq_items()}</div>
</div></section>

<section class="sec" id="book" aria-labelledby="book-h"><div class="w book-g">
<div><h2 id="book-h">Book a visit</h2><p>Tell us who is coming and why, and the front desk calls back within two business hours to set a time.</p><p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p></div>
{form()}
</div></section>
</main>
'''
    return head("preview-a.css", "family=Alegreya:wght@500;700;800&amp;family=Alegreya+Sans:wght@400;500;700", "#1F3A2E") + body + footer_html()


# ------------------------------------------------------------------ Preview B
LANES = [("go", "Go now", "Do not wait for us. Go to the emergency hospital."),
         ("today", "Call us today", "We keep same day visits open for exactly this."),
         ("week", "Book this week", "Worth a visit, and it can wait for an appointment.")]


def build_b():
    lanes = ""
    for key, title, sub in LANES:
        lists = "".join(f'<ul data-for="{sp}"{"" if sp == "dog" else " hidden"}>' + "".join(f"<li>{t}</li>" for t in TRIAGE[sp][key]) + "</ul>" for sp in TRIAGE)
        if key == "go":
            act = f'<a class="lane-act" href="tel:{ER["tel"]}"><b>Call {ER["name"]}</b>{ER["phone"]}, open 24 hours</a><p class="lane-note">{ER["addr"]}, Northwest Portland</p>'
        elif key == "today":
            act = f'<a class="lane-act" href="tel:{TEL}" data-callus><b>Call {PHONE}</b><span data-callus-note>Call before 3 PM for a same day visit</span></a>'
        else:
            act = '<a class="lane-act" href="#book"><b>Request a visit</b>We call back within two business hours</a>'
        lanes += f'<section class="lane {key}" aria-labelledby="lane-{key}"><h2 id="lane-{key}">{title}</h2><p class="lane-sub">{sub}</p>{lists}{act}</section>'
    year = ""
    for name, who, first, last, see, do, img in HAZARDS:
        cells = "".join(f'<td class="{"on" if m in in_months(first, last) else ""}"><span class="sr">{FULL[m - 1] if m in in_months(first, last) else ""}</span></td>' for m in range(1, 13))
        tag = {"dog": "Dogs", "cat": "Cats", "both": "Dogs and cats"}[who]
        year += f'<tr data-who="{who}"><th scope="row">{name}<small>{tag}</small></th>{cells}</tr>'
    heads = "".join(f'<th scope="col"><abbr title="{FULL[i]}">{m}</abbr></th>' for i, m in enumerate(MONTHS))
    prices = "".join(f'<li><div><h3>{n}</h3><p>{d}</p></div><b>{p}</b></li>' for n, d, p in PRICES)
    team = "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in TEAM)
    body = f'''{ribbon("B, Can It Wait", "preview-a.html", "preview A, The Field Guide")}<div class="status" data-status><span class="dot" aria-hidden="true"></span><span data-status-text>Open Monday to Friday 7:30 AM to 6 PM, and Saturday 9 AM to 2 PM.</span><a href="tel:{TEL}">{PHONE}</a></div>
<header class="hd"><div class="w hd-in">
<a class="mark" href="preview-b.html" aria-label="{BRAND}, home">{MARK}<span>Fernhollow Vet</span></a>
<nav aria-label="Main">{nav_links()}</nav>
<a class="btn small" href="#book">Request a visit</a>
</div></header>
<main id="main">
<section class="hero"><div class="w">
<div class="hero-top">
<h1>Can it wait until morning?</h1>
<div class="hero-side"><p class="lede">Find what you are seeing on the board. If it is not there, or you are not sure which column you are in, call us.</p>
{species_switch("I have a")}</div>
</div>
<div class="board">{lanes}</div>
<p class="fine">This board is general guidance from a neighborhood clinic and cannot examine your pet. When in doubt, call.</p>
</div></section>

<section class="who"><div class="w who-g">
<div class="portrait"><img data-for="dog" src="img/dog-yellow.webp" alt="A scruffy terrier mix sitting against a bright yellow background, head tilted at the camera" width="1600" height="1200"><img data-for="cat" hidden src="img/cat-green.webp" alt="A grey tabby cat sitting upright against a green background, looking at the camera" loading="lazy" width="1600" height="1200"></div>
<div><h2>A neighborhood clinic for Sellwood dogs and cats</h2>
<p>Fernhollow has been on the same corner since 2012. Three people will know your pet by name, the phone is answered by a technician, and every price on this page is the price on your invoice.</p>
<ul class="facts"><li><b>Same day</b>sick visits when you call before 3 PM</li><li><b>Forty minutes</b>for a first puppy or kitten visit</li><li><b>In writing</b>an estimate before any treatment</li></ul></div>
</div></section>

<section class="sec" id="watch" aria-labelledby="watch-h"><div class="w">
<h2 id="watch-h">What should a Portland pet owner watch for?</h2>
<p class="intro">Seven things we see every year in this city, and the months they show up.</p>
<div class="tw"><table class="yeartbl"><caption>Seasonal hazards for Portland dogs and cats, by month</caption><thead><tr><th scope="col">Hazard</th>{heads}</tr></thead><tbody>{year}</tbody></table></div>
<p class="fine">Raw salmon and trout are the one to know if you are new to the Northwest. A dog that eats raw fish can be very sick within six days, and treatment works when it starts early.</p>
</div></section>

<section class="sec tint" id="prices" aria-labelledby="price-h"><div class="w price-g">
<div><h2 id="price-h">How much does a visit cost?</h2><p>Sample prices for this demo. Anything beyond the exam gets a written estimate first, and you approve it before we start.</p></div>
<ul class="pricelist">{prices}</ul>
</div></section>

<section class="sec" id="team" aria-labelledby="team-h"><div class="w team-g">
<img src="img/exam.webp" alt="A veterinarian in navy scrubs kneeling on an exam room floor, looking into the ear of a calm golden retriever mix" loading="lazy" width="1600" height="1200">
<div><h2 id="team-h">Who will see your pet?</h2><ul class="team">{team}</ul><p class="fine">Fictional people, written for this demo.</p></div>
</div></section>

<section class="sec tint" id="visit" aria-labelledby="visit-h"><div class="w visit-g">
<div><h2 id="visit-h">Where is the clinic?</h2>
<p>We are in a green bungalow in Sellwood, a few blocks from the bridge and a short walk from the off leash area at Sellwood Riverfront Park. There is parking behind the building and a covered porch for rainy day waits.</p>
{hours_table()}</div>
<img src="img/exterior.webp" alt="A green craftsman bungalow clinic on a rainy Sellwood street, with a person in a yellow rain jacket walking a dog toward the porch" loading="lazy" width="1600" height="1200">
</div></section>

<section class="sec" aria-labelledby="faq-h"><div class="w faq-g">
<h2 id="faq-h">Questions new clients ask</h2>
<div class="faq">{faq_items()}</div>
</div></section>

<section class="sec book" id="book" aria-labelledby="book-h"><div class="w book-g">
<div><h2 id="book-h">Request a visit</h2><p>Tell us who is coming and why, and the front desk calls back within two business hours to set a time.</p><p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p></div>
{form()}
</div></section>
</main>
'''
    return head("preview-b.css", "family=Gabarito:wght@400;500;700;900", "#13203A") + body + footer_html()


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
    print("Building Fernhollow previews:")
    write("preview-a.html", build_a())
    write("preview-b.html", build_b())
    if PROBLEMS:
        print("\n".join(PROBLEMS))
        sys.exit(1)
