"""Shared data, schema and page chrome for The Meraki Inn demo.

The Meraki Inn is a fictional five room inn in Galveston's East End Historic
District. The district, the 1900 Storm, the Seawall and grade raising, the
Bolivar ferry, Dickens on The Strand, Mardi Gras! Galveston, the cruise
terminals, the hotel occupancy tax and the hurricane advisory times are real
and were checked on October 2, 2026. The house, the people, the rooms, the
rates and the policies are samples.

The design is "The Day", Adam's pick, in the style of the reference he sent
(boutiqueinncollection.com): a thin display serif in capitals, small spaced
capitals over a short rule, photographs that overlap the edge of each ground,
and text in a bordered card. The home page is one day at the inn, hour by hour,
set to today's sunrise and sunset. Every other page opens on its own hour.
Noto Serif Display, Source Serif 4 and Jost. No italics.
"""
import json
import re
from html import escape

BRAND = "The Meraki Inn"
PHONE = "(409) 555-0134"            # 555-01xx is reserved for fiction
TEL = "+14095550134"
BASE = "https://merakislove.com/demos/meraki-inn"
FONTS = "family=Noto+Serif+Display:wght@200;300&amp;family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&amp;family=Jost:wght@500"

# A small sun on the horizon: the Gulf side of the island faces the sunrise.
MARK = ('<svg viewBox="0 0 44 44" aria-hidden="true" focusable="false">'
        '<path d="M6 30h32M12 36h20" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/>'
        '<path d="M12 30a10 10 0 0 1 20 0" stroke="currentColor" stroke-width="2.6" fill="none"/>'
        '<path d="M22 8v6M8.5 14.5l4 4M35.5 14.5l-4 4" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" fill="none"/></svg>')

# Image name -> (width, height, alt text)
PICS = {
    "exterior": (1920, 1084, "A two story Victorian house painted pale sea green with white double gallery porches, a coral front door, palm trees and pink flowers in the garden"),
    "beach-sunrise": (1920, 1084, "A wide Gulf beach at sunrise, with a pink and orange sky reflected in wet sand and shorebirds at the water line"),
    "breakfast": (1600, 1189, "Breakfast set on the upstairs gallery porch: a coffee pot, pastries, fruit and preserves, with palms and Victorian houses beyond the railing"),
    "porch-golden": (1600, 1189, "Two white rocking chairs on the gallery porch at golden hour, with iced tea on a small table and pink flowers beyond the railing"),
    "porch-night": (1600, 1189, "A porch at night, with a lit lantern beside a coral door and warm light in the tall windows"),
    "innkeeper": (1600, 1189, "The innkeeper, a woman with silver curly hair in a linen apron, arranging flowers at the kitchen island beside a tray of coffee cups"),
    "entry-hall": (1200, 1614, "The entry hall of the inn, with a wooden staircase, heart pine floors and flowers on a console table by the open front door"),
    "bikes": (1600, 1189, "Three cream colored cruiser bicycles with wicker baskets leaning on a white picket fence in front of a green Victorian cottage, with pink oleander in bloom"),
    "room-loom": (1600, 1189, "A bright corner bedroom with a black iron bed, white linen, an indigo throw and sheer curtains lifting at tall windows"),
    "room-kiln": (1200, 1614, "A guest room with deep green walls, a white clawfoot tub with brass taps under a tall window and a bed in the background"),
    "room-press": (1600, 1189, "A ground floor bedroom with an oak bed in white linen, framed chart prints on the wall, a writing desk with a brass lamp and a glass door open to the side porch"),
    "room-bindery": (1600, 1189, "A bedroom in evening lamplight with a carved walnut bed, a wall of shelves filled with old books, and a shuttered window at dusk"),
    "room-darkroom": (1200, 1614, "A carriage house suite with a vaulted board ceiling, a king bed with a charcoal blanket, black and white photographs on the wall, a leather armchair and French doors open to a porch"),
}

ROOMS = [
    {"slug": "the-loom", "key": "loom", "name": "The Loom", "rate": 249, "label": "Second floor, corner king", "bed": "King", "where": "Second floor of the house",
     "line": "Corner king on the second floor, with a door to the gallery.",
     "craft": "Linen curtains and indigo throws from a Texas weaver. The bay window catches the Gulf breeze before the rest of the house.",
     "pic": "room-loom", "second": "porch-golden"},
    {"slug": "the-kiln", "key": "kiln", "name": "The Kiln", "rate": 219, "label": "Second floor, queen", "bed": "Queen", "where": "Second floor of the house",
     "line": "Queen on the second floor, with a clawfoot tub by the window.",
     "craft": "Lamps, tiles and a washbasin thrown by a Galveston potter, against deep green walls. The quietest room in the house.",
     "pic": "room-kiln", "second": None},
    {"slug": "the-press", "key": "press", "name": "The Press", "rate": 189, "label": "First floor, step free queen", "bed": "Queen", "where": "First floor of the house",
     "line": "Queen on the first floor, step free from the side porch.",
     "craft": "Letterpress prints of island charts over the bed, and a writing desk that gets used.",
     "pic": "room-press", "second": None},
    {"slug": "the-bindery", "key": "bindery", "name": "The Bindery", "rate": 209, "label": "Second floor, queen", "bed": "Queen", "where": "Second floor of the house",
     "line": "Queen on the second floor, with a wall of books and a chair to read them in.",
     "craft": "A hand bound journal waits on the nightstand for guests to write in, and the shutters close the room down to one lamp.",
     "pic": "room-bindery", "second": None},
    {"slug": "the-darkroom", "key": "darkroom", "name": "The Darkroom", "rate": 289, "label": "Carriage house, king suite", "bed": "King", "where": "Carriage house",
     "line": "King suite in the carriage house, with a porch of its own.",
     "craft": "Silver prints of the Gulf on every wall, a sitting corner, and the only private porch at the inn.",
     "pic": "room-darkroom", "second": "porch-night"},
]
ROOM = {r["slug"]: r for r in ROOMS}

PEOPLE = [
    ("Celeste Arceneaux", "Innkeeper and owner", "Celeste bought the house in 2014 and spent two years bringing it back. She answers the phone, and she will know which room you would like."),
    ("Isadora Fontenot", "Breakfast cook", "Isadora bakes before sunrise and cooks to order from 8 to 9:30. The fig preserves are hers."),
]

ISLAND = [
    ("The East End Historic District", "The inn sits inside it. The district covers about 150 acres and more than 550 buildings, and it has been a National Historic Landmark since 1976. Most of the houses are Victorian, with a few Greek Revival survivors."),
    ("The Seawall", "Built from 1902 to 1904 after the 1900 Storm, and extended ever since. It now runs for more than 10 miles along the Gulf, and the beach is a short bike ride from our porch."),
    ("The Bolivar ferry", "It is free and it runs 24 hours a day. The crossing is 2.7 miles and takes about 18 minutes each way."),
    ("Dickens on The Strand", 'December 4 to 6, 2026, the 53rd year of the festival. Rooms for that weekend are the first to go. <a href="dickens-on-the-strand.html">See the weekend</a>.'),
]

NAV = [("rooms.html", "Rooms", "rooms"), ("breakfast.html", "Breakfast", "breakfast"), ("the-island.html", "The island", "island"),
       ("the-house.html", "The house", "house"), ("stay.html", "Rates", "stay")]


# ---------------------------------------------------------------- schema
def strip(s):
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&").replace("&#39;", "'")


def org_schema():
    return {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE}/#org", "name": BRAND, "url": f"{BASE}/", "logo": f"{BASE}/img/og.jpg",
            "telephone": "+1-409-555-0134", "foundingDate": "2016", "founder": {"@type": "Person", "name": "Celeste Arceneaux", "jobTitle": "Innkeeper"}}


def business_schema():
    # BedAndBreakfast descends from LocalBusiness through LodgingBusiness. LocalBusiness is
    # named as well so a scanner that only matches the exact type still finds it.
    return {"@context": "https://schema.org", "@type": ["BedAndBreakfast", "LocalBusiness"], "@id": f"{BASE}/#business", "name": BRAND, "url": f"{BASE}/",
            "telephone": "+1-409-555-0134", "image": f"{BASE}/img/og.jpg", "priceRange": "$189 to $289",
            "address": {"@type": "PostalAddress", "addressLocality": "Galveston", "addressRegion": "TX", "postalCode": "77550", "addressCountry": "US"},
            "numberOfRooms": 5, "checkinTime": "15:00", "checkoutTime": "11:00", "petsAllowed": False,
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in ["Breakfast included", "Off street parking", "Bicycles"]],
            "parentOrganization": {"@id": f"{BASE}/#org"}}


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": f"{BASE}/", "publisher": {"@id": f"{BASE}/#org"}, "author": {"@id": f"{BASE}/#org"}}


def room_schema(r, desc):
    return {"@context": "https://schema.org", "@type": "HotelRoom", "name": r["name"], "description": desc, "url": f'{BASE}/{r["slug"]}.html',
            "image": f'{BASE}/img/{r["pic"]}.webp', "bed": {"@type": "BedDetails", "typeOfBed": r["bed"], "numberOfBeds": 1},
            "occupancy": {"@type": "QuantitativeValue", "maxValue": 2}, "containedInPlace": {"@id": f"{BASE}/#business"}}


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
def head(title, desc, path, schemas, theme="#12231D"):
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
<meta name="theme-color" content="{theme}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS}&amp;display=swap">
<script>document.documentElement.className="js"</script>
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
    return f"""<header class="hd"><div class="hd-in">
<a class="mark" href="index.html" aria-label="{BRAND}, home">{MARK}<span>The Meraki Inn</span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" data-menu hidden>Menu</button>
<nav id="nav" aria-label="Main">{links}<a class="book" href="#stay">Book a stay</a></nav>
</div></header>
"""


def pic(name, lazy=True, first=False, alt=None):
    w, h, a = PICS[name]
    extra = ' fetchpriority="high"' if first else (' loading="lazy"' if lazy else "")
    return f'<img src="img/{name}.webp" alt="{alt or a}"{extra} width="{w}" height="{h}">'


def crumbs(items):
    out = []
    for i, (n, href) in enumerate(items):
        if i < len(items) - 1:
            out.append(f'<a href="{href or "index.html"}">{n}</a><span aria-hidden="true">/</span>')
        else:
            out.append(f'<span aria-current="page">{n}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(out)}</nav>'


def clock(text, small=""):
    """A fixed hour, or any short figure that should stand as tall as one."""
    s = f" <small>{small}</small>" if small else ""
    return f'<p class="clock">{text}{s}</p>'


def clock_live(kind, fallback):
    """Sunrise, golden hour or sunset. The word stays if the script does not run."""
    return f'<p class="clock" data-time="{kind}">{fallback}</p>'


def go(href, text):
    return f'<a class="go" href="{href}">{text}</a>'


def gos(*links):
    return '<p class="gos">' + "".join(links) + "</p>"


BOOK = go("#stay", "Book a stay")
CALL = go(f"tel:{TEL}", f"Call {PHONE}")


def faq_items(qa):
    return "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(qa))


def faq_section(title, qa):
    return f'''<section class="faqs" aria-labelledby="faq-h">
<h2 class="cap" id="faq-h">{title}</h2><hr class="hair">
<div class="faq">{faq_items(qa)}</div>
</section>
'''


def room_options(selected="the-loom"):
    return "".join(f'<option value="{r["key"]}" data-rate="{r["rate"]}"{" selected" if r["slug"] == selected else ""}>{r["name"]}, ${r["rate"]}</option>' for r in ROOMS)


def nights_options(selected=2):
    return "".join(f'<option value="{n}"{" selected" if n == selected else ""}>{n} night{"" if n == 1 else "s"}</option>' for n in range(1, 8))


def stay_form(selected="the-loom"):
    r = ROOM[selected]
    return f'''<form class="form" action="#stay" method="post" novalidate data-demo data-stay>
<div class="fields">
<label>Arrive<input type="date" name="arrive"></label>
<label>Nights<select name="nights">{nights_options()}</select></label>
<label class="full">Room<select name="room">{room_options(selected)}</select></label>
<label>Your name<input type="text" name="name" autocomplete="name"></label>
<label>Email<input type="email" name="email" autocomplete="email"></label>
</div>
<p class="total" aria-live="polite"><span data-total>2 nights in {r["name"]}</span><b data-sum>${r["rate"] * 2}</b><small>before tax</small></p>
<button class="btn" type="submit">Ask for these dates</button>
<p class="form-note">We reply the same day to confirm the room. A card is taken by phone once the dates are held, never through this form. See <a href="privacy.html">how we handle your details</a>.</p>
<p class="form-done" role="status">This is a demo site, so nothing was sent. On a live site, the innkeeper replies the same day to confirm your room.</p>
</form>'''


def stay_section(selected="the-loom", title="Ask for your dates",
                 lead="Pick an arrival day, the number of nights and a room. The innkeeper replies the same day."):
    return f'''<section class="sec" id="stay" aria-labelledby="stay-h"><div class="split top">
<div><p class="label">Your dates</p><h2 class="cap" id="stay-h">{title}</h2>
<p>{lead}</p>
<p class="bigtel"><a href="tel:{TEL}">{PHONE}</a></p>
<p class="fine">Rates are samples for this demo and are before tax. See <a href="stay.html">rates and policies</a>.</p></div>
{stay_form(selected)}
</div></section>
'''


def footer():
    rooms = "".join(f'<li><a href="{r["slug"]}.html">{r["name"]}</a></li>' for r in ROOMS)
    return f"""<footer class="ft dark">
<p class="lock">{MARK}<span>The Meraki Inn</span></p>
<div class="ft-cols">
<div><h2>Find us</h2><address>East End Historic District<br>Galveston, TX 77550<br><a href="tel:{TEL}">{PHONE}</a></address>
<p>Check in from 3 PM. Check out by 11 AM.</p></div>
<div><h2>Rooms</h2><ul>{rooms}<li><a href="rooms.html">All five rooms</a></li></ul></div>
<div><h2>The inn</h2><ul><li><a href="breakfast.html">Breakfast</a></li><li><a href="the-house.html">The house</a></li><li><a href="about.html">Who keeps the inn</a></li><li><a href="stay.html">Rates and policies</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
<div><h2>The island</h2><ul><li><a href="the-island.html">What is near the inn</a></li><li><a href="cruise-parking.html">The night before a cruise</a></li><li><a href="dickens-on-the-strand.html">Dickens on The Strand</a></li><li><a href="hurricane-season.html">Hurricane season</a></li></ul></div>
</div>
<p class="ft-base">© 2026 {BRAND}. A demo site by <a href="https://merakislove.com/packages/presence-first-web-design">Meraki is Love</a>. The Meraki Inn is a fictional inn, and its house, people, rooms, rates and policies are samples. The district, the Seawall, the ferry, the festivals, the port and the weather service are real and are not affiliated with this demo.</p>
</footer>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def page(path, title, desc, schemas, current, body, theme="#12231D"):
    return head(title, desc, path, schemas, theme) + header(current) + f'<main id="main">\n{body}</main>\n' + footer()
