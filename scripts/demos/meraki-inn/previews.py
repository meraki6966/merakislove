"""Two home page previews for The Meraki Inn demo, for Adam to choose between.

Run from the repo root:  python3 scripts/demos/meraki-inn/previews.py
Writes preview-a.html (The Collage) and preview-b.html (The Day) into
public/demos/meraki-inn/. Both are noindex and are not linked from anywhere.

Both follow the reference Adam sent on 10/2 (boutiqueinncollection.com): a thin
display serif in capitals, small spaced capitals over a short rule, photographs
that overlap, and text in a bordered card. They share assets/preview.css.

The Meraki Inn is a fictional seven room inn in Galveston's East End. The
district, the Seawall and grade raising, the Bolivar ferry and Dickens on The
Strand are real, checked in October 2026. Rates are samples.
"""
import json
import os
import re
import sys
from html import escape

BRAND = "The Meraki Inn"
PHONE = "(409) 555-0134"            # 555-01xx is reserved for fiction
TEL = "+14095550134"
BASE = "https://merakislove.com/demos/meraki-inn"
PREFIX = "/demos/meraki-inn/"
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "meraki-inn")
PROBLEMS = []

TITLE = "Boutique Inn in Galveston's East End | The Meraki Inn"
DESC = ("The Meraki Inn is a seven room boutique inn in Galveston's East End Historic District, with breakfast on the gallery "
        "and a short bike ride to the beach.")
NAV = [("#rooms", "Rooms"), ("#island", "The island"), ("#inn", "The inn"), ("#stay", "Stay")]

# A small sun on the horizon: the Gulf side of the island faces the sunrise.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M6 30h32M12 36h20" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
        '<path d="M12 30a10 10 0 0 1 20 0" stroke="currentColor" stroke-width="2.6" fill="none"/>'
        '<path d="M22 8v6M8.5 14.5l4 4M35.5 14.5l-4 4" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/></svg>')

# slug, name, rate, label, bed line, craft line, image, alt, second image (file, alt) or None
ROOMS = [
    ("loom", "The Loom", 249, "Second floor, corner king", "Corner king on the second floor, with a door to the gallery.",
     "Linen curtains and indigo throws from a Texas weaver. The bay window catches the Gulf breeze before the rest of the house.",
     "room-loom", "A bright corner bedroom with a black iron bed, white linen, an indigo throw and sheer curtains lifting at tall windows",
     ("porch-golden", "Two white rocking chairs on the gallery porch at golden hour, with iced tea on a small table and pink flowers beyond the railing")),
    ("kiln", "The Kiln", 219, "Second floor, queen", "Queen on the second floor, with a clawfoot tub by the window.",
     "Lamps, tiles and a washbasin thrown by a Galveston potter, against deep green walls. The quietest room in the house.",
     "room-kiln", "A guest room with deep green walls, a white clawfoot tub with brass taps under a tall window and a bed in the background", None),
    ("press", "The Press", 189, "First floor, step free queen", "Queen on the first floor, step free from the side porch.",
     "Letterpress prints of island charts over the bed, and a writing desk that gets used.",
     "room-press", "A ground floor bedroom with an oak bed in white linen, framed chart prints on the wall, a writing desk with a brass lamp and a glass door open to the side porch", None),
    ("darkroom", "The Darkroom", 289, "Carriage house, king suite", "King suite in the carriage house, with a porch of its own.",
     "Silver prints of the Gulf on every wall, a sitting room, and the only private porch at the inn.",
     "room-darkroom", "A carriage house suite with a vaulted board ceiling, a king bed with a charcoal blanket, black and white photographs of the Gulf, a leather armchair and French doors open to a porch",
     ("porch-night", "A porch at night, with a lit lantern beside a coral door and warm light in the tall windows")),
]

ISLAND = [
    ("The East End Historic District", "The inn sits inside it. The district covers about 150 acres and more than 550 buildings, and it has been a National Historic Landmark since 1976. Most of the houses are Victorian, with a few Greek Revival survivors."),
    ("The Seawall", "Built from 1902 to 1904 after the 1900 Storm, and extended ever since. It now runs for more than 10 miles along the Gulf, and the beach is a short bike ride from our porch."),
    ("The Bolivar ferry", "It is free and it runs 24 hours a day. The crossing is 2.7 miles and takes about 18 minutes each way."),
    ("Dickens on The Strand", "December 4 to 6, 2026, the 53rd year of the festival. Rooms for that weekend are the first to go."),
]

PEOPLE = [
    ("Celeste Arceneaux", "Innkeeper and owner", "Celeste bought the house in 2014 and spent two years bringing it back. She answers the phone, and she will know which room you would like."),
    ("Isadora Fontenot", "Breakfast cook", "Isadora bakes before sunrise and cooks to order from 8 to 9:30. The fig preserves are hers."),
]

HOME_FAQ = [
    ("Where is The Meraki Inn?", "In Galveston's East End Historic District, between Broadway and Market Street. The Strand and the beach are both a short bike ride away, and we keep six bikes by the side gate."),
    ("What does meraki mean?", "It is a Greek word for doing something with soul, creativity and love, so that a piece of you ends up in the work. Each room is furnished around one craft, made by hand in Texas."),
    ("Is breakfast included?", "Yes. Coffee is out at 6:30, and breakfast is cooked to order on the gallery from 8 to 9:30."),
    ("Can I park at the inn while I am on a cruise?", "Yes. Guests who stay the night before a cruise can leave a car in our gated lot for $12 a day. That is a sample rate for this demo."),
    ("What happens if a hurricane is forecast?", "Hurricane season runs from June 1 to November 30. If a hurricane warning is issued for Galveston during your dates, we refund the stay in full."),
]


def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>"


def schemas():
    org = {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/", "logo": f"{BASE}/img/og.jpg",
           "telephone": "+1-409-555-0134", "foundingDate": "2016", "founder": {"@type": "Person", "name": "Celeste Arceneaux", "jobTitle": "Innkeeper"}}
    biz = {"@context": "https://schema.org", "@type": ["BedAndBreakfast", "LocalBusiness"], "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
           "telephone": "+1-409-555-0134", "image": f"{BASE}/img/og.jpg", "priceRange": "$189 to $289",
           "address": {"@type": "PostalAddress", "addressLocality": "Galveston", "addressRegion": "TX", "postalCode": "77550", "addressCountry": "US"},
           "numberOfRooms": 7, "checkinTime": "15:00", "checkoutTime": "11:00",
           "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["Breakfast included", "Off street parking", "Bicycles"]],
           "parentOrganization": {"@id": f"{BASE}/#org"}}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/", "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in HOME_FAQ]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"}]}
    return "".join(ld(s) for s in [org, biz, site, faq, crumbs])


FONTS = "family=Noto+Serif+Display:wght@200;300&amp;family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&amp;family=Jost:wght@500"


def head(theme, body_class):
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS}&amp;display=swap">
<link rel="stylesheet" href="assets/preview.css">
{schemas()}
</head>
<body class="{body_class}">
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


def island_rows():
    return '<ul class="island">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in ISLAND) + "</ul>"


def room_options(selected="loom"):
    return "".join(f'<option value="{r[0]}" data-rate="{r[2]}"{" selected" if r[0] == selected else ""}>{r[1]}, ${r[2]}</option>' for r in ROOMS)


def nights_options(selected=2):
    return "".join(f'<option value="{n}"{" selected" if n == selected else ""}>{n} night{"" if n == 1 else "s"}</option>' for n in range(1, 8))


def stay_form():
    return f'''<form class="form" action="#stay" method="post" novalidate data-demo data-stay>
<div class="fields">
<label>Arrive<input type="date" name="arrive" data-sync="arrive"></label>
<label>Nights<select name="nights" data-sync="nights">{nights_options()}</select></label>
<label class="full">Room<select name="room" data-sync="room">{room_options()}</select></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Email<input type="email" name="email" autocomplete="email"></label>
</div>
<p class="total" aria-live="polite"><span data-total>2 nights in The Loom</span><b data-sum>$498</b><small>before tax</small></p>
<button class="btn" type="submit">Ask for these dates</button>
<p class="form-note">We reply the same day to confirm the room. A card is taken by phone once the dates are held, never through this form.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live site, the innkeeper replies the same day to confirm your room.</p>
</form>'''


def footer_html(js):
    return f'''<footer class="ft dark">
<p class="lock">{MARK}<span>The Meraki Inn</span></p>
<div class="ft-cols">
<div><h2>Find us</h2><address>East End Historic District<br>Galveston, TX 77550<br><a href="tel:{TEL}">{PHONE}</a></address></div>
<div><h2>Arriving</h2><p>Check in from 3 PM. Check out by 11 AM. Off street parking behind the house.</p></div>
<div><h2>The season</h2><p>Open all year. Hurricane season runs from June 1 to November 30, and a warning for the island means a full refund.</p></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. The Meraki Inn is a fictional inn, and its people, rooms and rates are samples. The district, the Seawall, the ferry and the festival are real and are not affiliated with this demo.</p>
</footer>
<script src="assets/{js}" defer></script>
</body>
</html>
'''


EXTERIOR_ALT = "A two story Victorian house painted pale sea green with white double gallery porches, a coral front door, palm trees and pink flowers in the garden"
BREAKFAST_ALT = "Breakfast set on the upstairs gallery porch: a coffee pot, pastries, fruit and preserves, with palms and Victorian houses beyond the railing"
BEACH_ALT = "A wide Gulf beach at sunrise, with a pink and orange sky reflected in wet sand and shorebirds at the water line"
KEEPER_ALT = "The innkeeper, a woman with silver curly hair in a linen apron, arranging flowers at the kitchen island beside a tray of coffee cups"
SIZES = {"exterior": (1920, 1084), "beach-sunrise": (1920, 1084), "room-loom": (1600, 1189), "breakfast": (1600, 1189), "porch-golden": (1600, 1189),
         "porch-night": (1600, 1189), "innkeeper": (1600, 1189), "room-press": (1600, 1189), "entry-hall": (1200, 1614), "room-kiln": (1200, 1614),
         "room-darkroom": (1200, 1614)}


def img(name, alt, lazy=True, first=False):
    w, h = SIZES[name]
    extra = ' fetchpriority="high"' if first else (' loading="lazy"' if lazy else "")
    return f'<img src="img/{name}.webp" alt="{alt}"{extra} width="{w}" height="{h}">'


def header(home, last):
    return f'''<header class="hd" data-hd><div class="hd-in">
<a class="mark" href="{home}" aria-label="{BRAND}, home">{MARK}<span>The Meraki Inn</span></a>
<nav aria-label="Main">{nav_links()}</nav>
{last}
</div></header>
'''


def people_section(dark):
    return f'''<section class="{"dark" if dark else "plain"}" aria-labelledby="people-h"><div class="split">
<figure>{img("innkeeper", KEEPER_ALT)}</figure>
<div><p class="label">The people</p><h2 class="cap" id="people-h">Who keeps the inn?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>
'''


def faq_section():
    return f'''<section class="faqs" aria-labelledby="faq-h">
<h2 class="cap" id="faq-h">Before you book</h2><hr class="hair">
<div class="faq">{faq_items()}</div>
</section>
'''


def stay_section():
    return f'''<section id="stay" aria-labelledby="stay-h"><div class="split top">
<div><p class="label">Your dates</p><h2 class="cap" id="stay-h">Ask for your dates</h2>
<p>Pick an arrival day, the number of nights and a room. The innkeeper replies the same day.</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p></div>
{stay_form()}
</div></section>
'''


# ------------------------------------------------------------------ Preview A
def build_a():
    blocks = ""
    for i, (slug, name, rate, label, bed, craft, pic, alt, second) in enumerate(ROOMS):
        cls = "block" + (" flip" if i % 2 else "") + ("" if second else " solo")
        small = f'<figure class="small">{img(second[0], second[1])}</figure>\n' if second else ""
        blocks += f'''<article class="{cls}" id="room-{slug}">
{small}<div class="card"><p class="label">{label}</p><h3>{name}</h3>
<p><b>{bed}</b> {craft}</p>
<p class="rate">${rate} a night, breakfast included</p>
<p class="gos"><button class="go" type="button" data-pick="{slug}">Stay in {name}</button></p></div>
<figure class="big">{img(pic, alt)}</figure>
</article>
'''
    roomnav = "".join(f'<li><a href="#room-{r[0]}"><b>{r[1]}</b><span>${r[2]} a night</span></a></li>' for r in ROOMS)
    body = f'''{ribbon("A, The Collage", "preview-b.html", "preview B, The Day")}{header("preview-a.html", f'<a class="tel" href="tel:{TEL}">{PHONE}</a>')}<main id="main">
<section class="collage" aria-label="The Meraki Inn in photographs">
<div class="lockup" data-lockup>{MARK}<p class="name">The Meraki Inn</p><p class="place">Galveston, Texas</p></div>
<figure class="c1">{img("porch-golden", ROOMS[0][8][1], lazy=False)}</figure>
<figure class="c2">{img("exterior", EXTERIOR_ALT, first=True)}</figure>
<figure class="c3">{img("entry-hall", "The entry hall of the inn, with a wooden staircase, heart pine floors and flowers on a console table by the open front door", lazy=False)}</figure>
<figure class="c4">{img("beach-sunrise", BEACH_ALT)}</figure>
<figure class="c5">{img("porch-night", ROOMS[3][8][1])}</figure>
<figure class="c6">{img("room-loom", ROOMS[0][7])}</figure>
</section>

<section class="statement">
<h1>A seven room inn on Galveston's East End.</h1>
<hr class="hair">
<p>Built in 1894, raised after the 1900 Storm, and kept with meraki: soul, creativity and love put into the work.</p>
</section>

<section class="dark" id="inn" aria-labelledby="inn-h"><div class="split">
<div><p class="label">The name</p><h2 class="cap" id="inn-h">What does meraki mean?</h2>
<p><b>It is a Greek word for doing something with soul, creativity and love,</b> so that a piece of you ends up in the work.</p>
<p>We took it as a rule for the house. Each of the seven rooms is furnished around one craft, made by hand in Texas: a loom, a kiln, a press, a darkroom. Breakfast is cooked to order and eaten on the gallery. The floors are the heart pine the house was built with.</p>
<p>After the 1900 Storm, Galveston lifted about 2,000 buildings on jackscrews and pumped sand underneath. This house was one of them.</p></div>
<figure>{img("breakfast", BREAKFAST_ALT)}</figure>
</div></section>

<section class="title" id="rooms" aria-labelledby="rooms-h">
<h2 id="rooms-h"><span class="the">The</span> <span class="big">Rooms</span></h2>
<hr class="hair wide">
<p>Seven rooms, each named for the craft it is furnished around. Four are shown here. Sample rates for this demo.</p>
<ul class="roomnav">{roomnav}</ul>
</section>
<div class="blocks">
{blocks}</div>

<section id="island" aria-labelledby="island-h"><div class="island-g">
<div><p class="label">The island</p><h2 class="cap" id="island-h">What is outside the door?</h2>
<p>An island with a long memory. Everything here is close enough for a bicycle.</p>
<figure>{img("beach-sunrise", BEACH_ALT)}</figure></div>
{island_rows()}
</div></section>

{people_section(True)}
{faq_section()}
{stay_section()}</main>
<form class="bookbar" aria-label="Check dates" data-bar>
<label>Arrive<input type="date" name="arrive" data-sync="arrive"></label>
<label>Nights<select name="nights" data-sync="nights">{nights_options()}</select></label>
<label>Room<select name="room" data-sync="room">{room_options()}</select></label>
<p class="bar-total" aria-live="polite"><span data-total>2 nights in The Loom</span><b data-sum>$498</b></p>
<a class="btn" href="#stay">Ask for these dates</a>
</form>
'''
    return head("#FBF5E6", "pa") + body + footer_html("preview-a.js")


# ------------------------------------------------------------------ Preview B
def hour(cls, hid, name, clock, copy, figure, layout="", attrs=""):
    return f'''<section class="hour {cls}"{attrs} aria-labelledby="{hid}">
<div class="hour-title"><h2 id="{hid}">{name}</h2>{clock}<hr class="hair wide"></div>
<div class="hour-g{layout}"><div class="hour-copy">{copy}</div>
{figure}</div>
</section>
'''


def build_b():
    rooms = "".join(f'<li><div><h3>{r[1]}</h3><p>{r[4]}</p></div><b>${r[2]}</b></li>' for r in ROOMS)
    hours = hour("dawn", "h-first", "First light", '<p class="clock" data-time="sunrise">Sunrise</p>',
                 "<p><b>The Gulf side of the island faces southeast,</b> so the sun comes up over the water. The beach is a ten minute bike ride from the porch, and we keep six bikes by the side gate.</p>"
                 "<p>Coffee is out in the hall from 6:30 for anyone who wants to carry a cup down there.</p>",
                 f'<figure>{img("beach-sunrise", BEACH_ALT)}</figure>')
    hours += hour("morning over", "h-break", "Breakfast on the gallery", '<p class="clock">8:00 <small>AM</small></p>',
                  "<p><b>Isadora bakes before sunrise and cooks to order from 8 to 9:30.</b> Eat upstairs on the gallery, where the palms are at eye level.</p>"
                  "<p>The word meraki is Greek. It means doing something with soul, creativity and love, so that a piece of you ends up in the work. Breakfast is where most guests first see what we mean by it.</p>",
                  f'<figure>{img("breakfast", BREAKFAST_ALT)}</figure>', " rev")
    hours += hour("noon over", "h-island", "The island", '<p class="clock">11:00 <small>AM</small></p>',
                  "<p><b>Everything here is close enough for a bicycle.</b> The inn sits in the East End, a few blocks from The Strand on one side and the Seawall on the other.</p>"
                  f'<p class="gos"><a class="go" href="#stay">Ask for your dates</a></p>',
                  island_rows(), " flat", ' id="island"')
    hours += hour("golden", "h-porch", "Porch hour", '<p class="clock" data-time="golden">Golden hour</p>',
                  "<p><b>An hour before sunset the light comes in low under the porch ceiling.</b> There is iced tea on the table and a rocking chair for everyone who wants one.</p>"
                  "<p>After the 1900 Storm, Galveston lifted about 2,000 buildings on jackscrews and pumped sand underneath. This house was one of them, porch and all.</p>",
                  f'<figure>{img("porch-golden", ROOMS[0][8][1])}</figure>', " rev")
    hours += hour("night over", "h-night", "Lamplight", '<p class="clock" data-time="sunset">Sunset</p>',
                  "<p><b>The lantern by the door goes on at sunset.</b> Upstairs there are seven rooms, each furnished around one craft made by hand in Texas. Four are listed here, with sample rates for this demo.</p>"
                  f'<ul class="roomlist">{rooms}</ul>',
                  f'<figure>{img("room-darkroom", ROOMS[3][7])}</figure>', " flat", ' id="rooms"')
    body = f'''{ribbon("B, The Day", "preview-a.html", "preview A, The Collage")}{header("preview-b.html", '<a class="tel" href="#stay">Book a stay</a>')}<main id="main">
<section class="block solo hero" id="inn">
<div class="card"><p class="label">Galveston, Texas</p>
<h1>A day at The Meraki Inn, hour by hour.</h1>
<p>Seven rooms in an 1894 house on Galveston's East End. Here is what a day looks like, set to today's sun.</p>
<p class="sun" data-sun>Today in Galveston the sun rises over the Gulf and sets behind the bay.</p>
<p class="gos"><a class="go" href="#stay">Book a stay</a><a class="go" href="tel:{TEL}">Call {PHONE}</a></p></div>
<figure class="big">{img("exterior", EXTERIOR_ALT, first=True)}</figure>
</section>

{hours}
{people_section(False)}
{faq_section()}
{stay_section()}</main>
'''
    return head("#12231D", "pb") + body + footer_html("preview-b.js")


def absolutize(html):
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|tel:|mailto:|#|/|data:)", url):
            return m.group(0)
        return f'{attr}="{PREFIX}{url}"'
    return re.sub(r'\b(href|src|poster)="([^"]+)"', fix, html)


def write(name, html):
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1).replace("&#x27;", "'")
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
    print("Building The Meraki Inn previews:")
    write("preview-a.html", build_a())
    write("preview-b.html", build_b())
    if PROBLEMS:
        print("\n".join(PROBLEMS))
        sys.exit(1)
