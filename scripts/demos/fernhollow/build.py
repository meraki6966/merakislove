"""Build the Fernhollow Veterinary Clinic demo into public/demos/fernhollow/.

Run from the repo root:  python3 scripts/demos/fernhollow/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
The design is "Can It Wait": the home page is a three lane triage board, and
the lane colors (red, yellow, green) mean the same thing on every page.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from fh import *  # noqa: E402,F403
from content import *  # noqa: E402,F403

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "fernhollow")
# The home page is also served at the clean URL /demos/fernhollow (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/fernhollow/")
OUT = os.environ.get("OUT", OUT)
PROBLEMS = []


def absolutize(html):
    if not PREFIX:
        return html

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"(https?:|tel:|mailto:|#|/|data:)", url):
            return m.group(0)
        if url == "index.html" or url.startswith("index.html#"):
            return f'{attr}="{PREFIX.rstrip("/")}{url[len("index.html"):]}"'
        return f'{attr}="{PREFIX}{url}"'
    return re.sub(r'\b(href|src|poster)="([^"]+)"', fix, html)


def write(name, html):
    # Guard the limits a scanner checks, so a long title never ships unnoticed.
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1).replace("&#x27;", "'")
    if len(title) > 60 or "&" in title:
        PROBLEMS.append(f"{name}: title is {len(title)} chars or has an ampersand: {title}")
    if not 120 <= len(desc) <= 160:
        PROBLEMS.append(f"{name}: description is {len(desc)} chars")
    if html.count("<h1") != 1:
        PROBLEMS.append(f"{name}: {html.count('<h1')} h1 elements")
    if 'alt=""' in html:
        PROBLEMS.append(f"{name}: empty alt text")
    html = absolutize(html)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    words = len(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S).split())
    print(f"  {name:28s} {len(html)//1024:>3} KB  {words:>5} words")


# ---------------------------------------------------------------- blocks
def in_months(first, last):
    """Month numbers a hazard covers, allowing a range that wraps past December."""
    if first <= last:
        return list(range(first, last + 1))
    return list(range(first, 13)) + list(range(1, last + 1))


def season_text(first, last):
    if (first, last) == (1, 12):
        return "All year"
    return f"{FULL[first - 1]} to {FULL[last - 1]}"


def who_text(who):
    return {"dog": "Dogs", "cat": "Cats", "both": "Dogs and cats"}[who]


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def steps(items):
    """A numbered sequence, for things that happen in order."""
    return '<ol class="steps">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items) + "</ol>"


def rows(items):
    """Titled rows with no order implied."""
    return '<ul class="rows">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items) + "</ul>"


def table(head, body_rows, caption, cls="tbl"):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = ""
    for r in body_rows:
        body += f'<tr><th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>"
    return f'<div class="tw"><table class="{cls}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def prose(title, paras, hid=""):
    h = f' id="{hid}"' if hid else ""
    return f'<div class="prose"><h2{h}>{title}</h2>' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def svc_list(exclude=None):
    out = ""
    for s in SERVICES:
        if s["slug"] == exclude:
            continue
        out += (f'<li>{tag(s["lane"])}<div><h3><a href="{s["slug"]}.html">{s["name"]}</a></h3><p>{s["short"]}</p></div>'
                f'<b>{s["price"]}</b></li>')
    return f'<ul class="svc">{out}</ul>'


def services_section(bg="", exclude=None, title="What does Fernhollow do?"):
    return f'''<section class="sec {bg}" aria-labelledby="svc-h"><div class="w">
<h2 id="svc-h">{title}</h2>
{svc_list(exclude)}
<p class="fine">The colored label shows how soon each kind of visit usually happens. Every price is on the <a href="pricing.html">prices page</a>.</p>
</div></section>
'''


def areas_section(bg="", exclude=None, title="Which neighborhoods do you serve?"):
    links = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS if a["slug"] != exclude)
    return f'''<section class="sec {bg}" aria-labelledby="areas-h"><div class="w areas-g">
<div><h2 id="areas-h">{title}</h2><p>The clinic is in Sellwood, a few blocks from the bridge. Most of our clients live within a short drive, and each neighborhood has its own page with what we see there.</p></div>
<ul class="areas"><li><a href="about.html">Sellwood</a></li>{links}</ul>
</div></section>
'''


def reviews_section(bg=""):
    figs = "".join(f'<figure><blockquote>{t}</blockquote><figcaption>{w}, {where}<span>Sample review</span></figcaption></figure>' for t, w, where in REVIEWS)
    return f'''<section class="sec {bg}" aria-labelledby="rev-h"><div class="w">
<h2 id="rev-h">What do clients say?</h2>
<div class="reviews">{figs}</div>
</div></section>
'''


def year_table():
    body = ""
    for slug, name, who, first, last, lane, see, do, more, img in HAZARDS:
        months = in_months(first, last)
        cells = "".join(f'<td class="{"on" if m in months else ""}"><span class="sr">{FULL[m - 1] if m in months else ""}</span></td>' for m in range(1, 13))
        body += f'<tr><th scope="row"><a href="portland-pet-hazards.html#{slug}">{name}</a><small>{who_text(who)}</small></th>{cells}</tr>'
    heads = "".join(f'<th scope="col"><abbr title="{FULL[i]}">{m}</abbr></th>' for i, m in enumerate(MONTHS))
    return (f'<div class="tw"><table class="yeartbl"><caption>Seasonal hazards for Portland dogs and cats, by month</caption>'
            f'<thead><tr><th scope="col">Hazard</th>{heads}</tr></thead><tbody>{body}</tbody></table></div>')


def board():
    lanes = ""
    for key, sub in LANE_COPY:
        lists = "".join(f'<ul data-for="{sp}"{"" if sp == "dog" else " hidden"}>' + "".join(f"<li>{t}</li>" for t in TRIAGE[sp][key]) + "</ul>" for sp in TRIAGE)
        if key == "go":
            act = (f'<a class="lane-act" href="tel:{ER["tel"]}"><b>Call {ER["name"]}</b>{ER["phone"]}, open 24 hours</a>'
                   f'<p class="lane-note">{ER["addr"]}, Northwest Portland. <a href="emergencies.html">What to do on the way</a></p>')
        elif key == "today":
            act = (f'<a class="lane-act" href="tel:{TEL}" data-callus><b>Call {PHONE}</b><span data-callus-note>Call before 3 PM for a same day visit</span></a>'
                   '<p class="lane-note"><a href="sick-visits.html">How a same day visit works</a></p>')
        else:
            act = ('<a class="lane-act" href="#book"><b>Request a visit</b>We call back within two business hours</a>'
                   '<p class="lane-note"><a href="services.html">See what we do and what it costs</a></p>')
        lanes += f'<section class="lane {key}" aria-labelledby="lane-{key}"><h2 id="lane-{key}">{LANES[key]}</h2><p class="lane-sub">{sub}</p>{lists}{act}</section>'
    return f'<div class="board">{lanes}</div>'


def plate(sp):
    img, alt, cap = PLATE[sp]
    marks = "".join(f'<li style="--x:{x}%;--y:{y}%"><span aria-hidden="true">{i + 1}</span></li>' for i, (_, _, x, y) in enumerate(CALLOUTS[sp]))
    notes = "".join(f"<li><h3>{name}</h3><p>{note}</p></li>" for name, note, _, _ in CALLOUTS[sp])
    hidden = "" if sp == "dog" else " hidden"
    load = ' fetchpriority="high"' if sp == "dog" else ' loading="lazy"'
    return (f'<figure class="plate" data-for="{sp}"{hidden}><div class="plate-img"><img src="img/{img}.webp" alt="{alt}" width="1600" height="1200"{load}>'
            f'<ol class="marks" aria-hidden="true">{marks}</ol></div><figcaption>{cap}</figcaption><ol class="notes">{notes}</ol></figure>')


def team_list():
    return '<ul class="team">' + "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in PEOPLE) + "</ul>"


EXAM_ALT = "A veterinarian in navy scrubs kneeling on an exam room floor, looking into the ear of a calm golden retriever mix"
EXTERIOR_ALT = "A green craftsman bungalow clinic on a rainy Sellwood street, with a person in a yellow rain jacket walking a dog toward the porch"


# ---------------------------------------------------------------- pages
def build_home():
    prices = "".join(f'<li><div><h3><a href="{h}">{n}</a></h3><p>{d}</p></div><b>{p}</b></li>' for n, d, p, h in PRICES)
    body = f'''<section class="hero"><div class="w">
<div class="hero-top">
<h1>Can it wait until morning?</h1>
<div class="hero-side"><p class="lede">Find what you are seeing on the board. If it is not there, or you are not sure which column you are in, call us.</p>
{species_switch()}</div>
</div>
{board()}
<p class="fine">This board is general guidance from a neighborhood clinic and cannot examine your pet. When in doubt, call.</p>
</div></section>

<section class="who"><div class="w who-g">
<div class="portrait"><img data-for="dog" src="img/dog-yellow.webp" alt="A scruffy terrier mix sitting against a bright yellow background, head tilted at the camera" width="1600" height="1200"><img data-for="cat" hidden src="img/cat-green.webp" alt="A grey tabby cat sitting upright against a green background, looking at the camera" loading="lazy" width="1600" height="1200"></div>
<div><h2>A neighborhood clinic for Sellwood dogs and cats</h2>
<p>Fernhollow has been on the same corner since 2012. Three people will know your pet by name, the phone is answered by a technician, and every price on this site is the price on your invoice.</p>
{facts([("Same day", "sick visits when you call before 3 PM"), ("Forty minutes", "for a first puppy or kitten visit"), ("In writing", "an estimate before any treatment")])}
<p class="more"><a href="about.html">Meet the clinic</a> or see <a href="new-clients.html">how a first visit works</a>.</p></div>
</div></section>

{services_section("")}
<section class="sec tint" id="watch" aria-labelledby="watch-h"><div class="w">
<h2 id="watch-h">What should a Portland pet owner watch for?</h2>
<p class="intro">Seven things we see every year in this city, and the months they show up.</p>
{year_table()}
<p class="fine">Raw salmon and trout are the one to know if you are new to the Northwest. A dog that eats raw fish can be very sick within six days, and treatment works when it starts early. Read the <a href="portland-pet-hazards.html">full hazards guide</a> or the page on <a href="salmon-poisoning.html">salmon poisoning in dogs</a>.</p>
</div></section>

<section class="sec" id="prices" aria-labelledby="price-h"><div class="w price-g">
<div><h2 id="price-h">How much does a visit cost?</h2><p>Sample prices for this demo. Anything beyond the exam gets a written estimate first, and you approve it before we start.</p><p><a href="pricing.html">See the full price list</a></p></div>
<ul class="pricelist">{prices}</ul>
</div></section>

<section class="sec tint" id="team" aria-labelledby="team-h"><div class="w team-g">
<img src="img/exam.webp" alt="{EXAM_ALT}" loading="lazy" width="1600" height="1200">
<div><h2 id="team-h">Who will see your pet?</h2>{team_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>

{reviews_section("")}
<section class="sec tint" id="visit" aria-labelledby="visit-h"><div class="w visit-g">
<div><h2 id="visit-h">Where is the clinic?</h2>
<p>We are in a green bungalow in Sellwood, a few blocks from the bridge and a short walk from the off leash area at Sellwood Riverfront Park. There is parking behind the building and a covered porch for rainy day waits.</p>
<p>We also see pets from <a href="westmoreland.html">Westmoreland</a>, <a href="eastmoreland.html">Eastmoreland</a> and <a href="woodstock.html">Woodstock</a>.</p>
{hours_table()}</div>
<img src="img/exterior.webp" alt="{EXTERIOR_ALT}" loading="lazy" width="1600" height="1200">
</div></section>
''' + faq_block("Questions new clients ask", HOME_FAQ) + book()
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    write("index.html", page("index.html", "Veterinarian in Sellwood, Portland | Fernhollow Vet",
                             "Fernhollow is a dog and cat veterinary clinic in Sellwood, Portland. Same day sick visits, prices on the page, and a plain guide to what can wait until morning.",
                             schemas, "", body))


def build_services_hub():
    mini = (f'<a class="lane go" href="emergencies.html"><h3>{LANES["go"]}</h3><p>Trouble breathing, collapse, poisoning, a cat that cannot urinate. The emergency page tells you where to go and what to do on the way.</p></a>'
            f'<a class="lane today" href="sick-visits.html"><h3>{LANES["today"]}</h3><p>Vomiting, a sore eye, a limp, a pet that will not eat. Call before 3 PM and we see your pet the same day.</p></a>'
            f'<a class="lane week" href="#book"><h3>{LANES["week"]}</h3><p>Exams, vaccines, teeth, skin, lumps and refills. Most visits are booked within the week.</p></a>')
    body = (phero("Veterinary care for Sellwood dogs and cats",
                  "Four kinds of visit cover most of what a dog or cat needs in a year. Each has its own page with what is included and what it costs.",
                  [("Home", "index.html"), ("Services", "")],
                  pic("cat-green", "A grey tabby cat sitting upright against a green background, looking at the camera"),
                  [("Dogs and cats", "and only dogs and cats"), ("Posted prices", "for every exam and vaccine"), ("Since 2012", "on the same corner in Sellwood")])
            + f'''<section class="sec white" aria-labelledby="svc-h"><div class="w">
<h2 id="svc-h">Which visit do you need?</h2>
{svc_list()}
<p class="fine">Surgery days are Tuesday and Thursday. For anything not listed, call <a href="tel:{TEL}">{PHONE}</a> and ask.</p>
</div></section>
<section class="sec" aria-labelledby="soon-h"><div class="w">
<h2 id="soon-h">How soon does my pet need to be seen?</h2>
<p class="intro">Every visit falls into one of three speeds. The colors mean the same thing on every page of this site.</p>
<div class="minilanes">{mini}</div>
</div></section>
''' + areas_section("white") + faq_block("Choosing a visit, answered", SERVICES_FAQ) + book())
    schemas = [org_schema(), business_schema(), faq_schema(SERVICES_FAQ), crumbs_schema([("Home", ""), ("Services", "services.html")]),
               {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["name"], "url": f'{BASE}/{s["slug"]}.html'} for i, s in enumerate(SERVICES)]}]
    write("services.html", page("services.html", "Veterinary Services in Sellwood, Portland | Fernhollow",
                                "Veterinary services for dogs and cats in Sellwood, Portland: wellness exams, same day sick visits, dental care and vaccines, each with its price.",
                                schemas, "services", body))


def build_service(slug):
    s, c = SVC[slug], SERVICE_PAGES[slug]
    trail = [("Home", "index.html"), ("Services", "services.html"), (s["name"], "")]
    if slug == "wellness-exams":
        side = f'<div class="plates">{species_switch("Show the checklist for a")}{plate("dog")}{plate("cat")}</div>'
    elif slug == "sick-visits":
        side = panel("today", LANES["today"], ["Vomiting or diarrhea more than twice in a day", "Squinting, or a red or cloudy eye", "Limping that has not improved after a day of rest",
                                               "Not eating for a full day", "A cat hiding and not coming out for meals", "Urinating outside the box, or going much more often"],
                     f'<a class="lane-act" href="tel:{TEL}" data-callus><b>Call {PHONE}</b><span data-callus-note>Call before 3 PM for a same day visit</span></a>')
    elif slug == "dental-care":
        side = pic("teeth-navy", "A brown and white dog sitting against a navy blue background with its mouth open, showing clean white teeth")
    else:
        side = pic("pair-red", "A grey and white kitten sitting beside a golden retriever puppy against a red background")
    if c["kind"] == "checks":
        main = checks(c["main"])
    elif c["kind"] == "steps":
        main = steps(c["main"])
    else:
        main = table(c["main_head"], c["main"], "Vaccines for dogs and cats at Fernhollow")
    if c["kind"] == "table":
        first = f'''<section class="sec white" aria-labelledby="main-h"><div class="w">
<h2 id="main-h">{c["main_title"]}</h2>
{main}
</div></section>
<section class="sec" aria-labelledby="body-h"><div class="w article-g">{prose(c["body_title"], c["body"], "body-h")}
{panel("week", "Puppies and kittens", ["First vaccines at six to eight weeks", "A booster every three to four weeks", "The last booster at 16 weeks or older", "Rabies for dogs by six months of age"],
       '<a class="lane-act" href="#book"><b>Book the first visit</b>Forty minutes, $65</a>')}
</div></section>
'''
    else:
        first = f'''<section class="sec white" aria-labelledby="main-h"><div class="w two-col">
<div><h2 id="main-h">{c["main_title"]}</h2>{main}</div>
{prose(c["body_title"], c["body"])}
</div></section>
'''
    body = (phero(c["h1"], c["lede"], trail, side, c["facts"]) + first
            + f'''<section class="sec{" white" if c["kind"] == "table" else ""}" aria-labelledby="cost-h"><div class="w">
<h2 id="cost-h">What does it cost?</h2>
<p class="intro">Sample prices for this demo. A live site would show your own.</p>
{table(c["rows_head"], c["rows"], c["rows_title"], "tbl price")}
<p class="fine">Anything beyond these gets a written estimate first. See the <a href="pricing.html">full price list</a> or <a href="new-clients.html">how a first visit works</a>.</p>
</div></section>
''' + services_section("" if c["kind"] == "table" else "white", exclude=slug, title="What else does Fernhollow do?")
            + faq_block(f'{s["name"]}, answered', c["faq"], "white" if c["kind"] == "table" else "") + book(reason=s["reason"]))
    schemas = [org_schema(), business_schema(), service_schema(s["name"], c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Services", "services.html"), (s["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "services", body))


def build_emergencies():
    side = panel("go", LANES["go"], [f'{ER["full"]}', f'{ER["addr"]}, Northwest Portland', "Open 24 hours, every day",
                                     f'Poison questions: ASPCA at <a href="tel:{POISON["tel"]}">{POISON["phone"]}</a>'],
                 f'<a class="lane-act" href="tel:{ER["tel"]}"><b>Call {ER["name"]}</b>{ER["phone"]}</a>')
    golists = "".join(f'<section class="lane go" aria-label="{name}"><h3>{name}</h3><ul>' + "".join(f"<li>{t}</li>" for t in TRIAGE[sp]["go"]) + "</ul></section>"
                      for sp, name in [("dog", "Dogs"), ("cat", "Cats")])
    body = (phero("What to do in a pet emergency in Portland",
                  "If what you are seeing is on the red list, do not wait for us. Go to the emergency hospital, and call them from the car.",
                  [("Home", "index.html"), ("Emergencies", "")], side, buttons=False)
            + f'''<section class="sec white" aria-labelledby="signs-h"><div class="w">
<h2 id="signs-h">Which signs mean go now?</h2>
<p class="intro">Any one of these is enough. You do not need to be sure.</p>
<div class="golists">{golists}</div>
<p class="fine">This list is general guidance and cannot examine your pet. If something frightens you and it is not here, treat it as an emergency.</p>
</div></section>
<section class="sec" aria-labelledby="way-h"><div class="w two-col">
<div><h2 id="way-h">What should I do on the way?</h2>{steps(EMERGENCY_STEPS)}</div>
<div><h2>Is it poison?</h2>
<p>The ASPCA Animal Poison Control Center answers day and night. A consultation fee may apply. They give you a case number, and the emergency veterinarian can call them with it.</p>
<p class="bignum"><a href="tel:{POISON["tel"]}">{POISON["phone"]}</a></p>
<h3 class="sub">Have this ready when you call</h3>{checks(POISON_READY)}</div>
</div></section>
<section class="sec white" aria-labelledby="hours-h"><div class="w two-col">
{prose("What if it happens while Fernhollow is open?", [f'Call us at <a href="tel:{TEL}">{PHONE}</a>. A technician answers, asks a few questions, and tells you whether to come to us or go straight to the emergency hospital. We would rather take ten of those calls than miss one.',
                                                        'For problems on the yellow list, we keep <a href="sick-visits.html">same day visits</a> open every weekday and Saturday morning.'], "hours-h")}
{prose("What happens after the emergency visit?", ["Ask the emergency hospital to send us the record. We read it the next business day, call you, and book any recheck here.",
                                                    'Many emergencies are seasonal in this city. The <a href="portland-pet-hazards.html">Portland hazards guide</a> shows which months to watch.'])}
</div></section>
''' + faq_block("Pet emergencies in Portland, answered", EMERGENCY_FAQ) + book("Not an emergency?", "If it can wait for an appointment, tell us who is coming and why. The front desk calls back within two business hours."))
    schemas = [org_schema(), business_schema(), faq_schema(EMERGENCY_FAQ), crumbs_schema([("Home", ""), ("Emergencies", "emergencies.html")]),
               article_schema("What to do in a pet emergency in Portland", "Signs that mean go now for dogs and cats, what to do on the way, and where to go after hours in Portland.", "emergencies.html")]
    write("emergencies.html", page("emergencies.html", "Pet Emergency in Portland: What to Do | Fernhollow Vet",
                                   "What to do in a pet emergency in Portland: the signs that mean go now for dogs and cats, what to do on the way, and the 24 hour hospital to call.",
                                   schemas, "emergencies", body))


def build_hazards():
    entries = ""
    for slug, name, who, first, last, lane, see, do, more, img in HAZARDS:
        pic_html = f'<img src="img/{img}.webp" alt="An illustration of {name.lower()}" loading="lazy" width="1200" height="1200">' if img else ""
        entries += (f'<article class="hz{"" if img else " plain"}" id="{slug}">{pic_html}<div><h3>{name}</h3>'
                    f'<p class="hz-meta">{tag(lane)}<span>{season_text(first, last)}</span><span>{who_text(who)}</span></p>'
                    f'<dl><dt>What you see</dt><dd>{see}</dd><dt>What to do</dt><dd>{do}</dd></dl><p class="hz-more">{more}</p></div></article>')
    body = (phero("Portland pet hazards, month by month",
                  "Seven things send Portland dogs and cats to a veterinarian every year, and most of them keep a calendar. Here is what to watch for and when.",
                  [("Home", "index.html"), ("Portland hazards", "")], buttons=False)
            + f'''<section class="sec white" aria-labelledby="year-h"><div class="w">
<h2 id="year-h">When does each hazard show up?</h2>
<p class="intro">The highlighted column is this month.</p>
{year_table()}
</div></section>
<section class="sec" aria-labelledby="each-h"><div class="w">
<h2 id="each-h">What does each one look like?</h2>
<p class="intro">The colored label is the speed: go to the emergency hospital, call us today, or book a visit this week.</p>
<div class="hzs">{entries}</div>
<p class="fine">General guidance from a neighborhood clinic. It cannot examine your pet. For a possible poisoning, the ASPCA Animal Poison Control Center answers at <a href="tel:{POISON["tel"]}">{POISON["phone"]}</a>, and a fee may apply.</p>
</div></section>
''' + faq_block("Portland pet hazards, answered", HAZARDS_FAQ, "white") + book())
    desc = "A month by month guide to Portland pet hazards: raw salmon, foxtails, wild mushrooms, river algae, lilies, antifreeze and fleas, with what to do for each."
    schemas = [org_schema(), business_schema(), faq_schema(HAZARDS_FAQ), crumbs_schema([("Home", ""), ("Portland hazards", "portland-pet-hazards.html")]),
               article_schema("Portland pet hazards, month by month", desc, "portland-pet-hazards.html")]
    write("portland-pet-hazards.html", page("portland-pet-hazards.html", "Portland Pet Hazards by Month | Fernhollow Vet", desc, schemas, "hazards", body))


def build_salmon():
    side = pic("salmon", "An illustration of a salmon in side profile", "illus")
    act = (f'<a class="lane-act" href="tel:{TEL}" data-callus><b>Call {PHONE}</b><span data-callus-note>Call before 3 PM for a same day visit</span></a>')
    aside = panel("today", "If your dog ate raw fish", ["Call us the day it happens, even with no symptoms", "Tell us what kind of fish and when",
                                                         "Watch for vomiting, fever and low energy for a week", "Do not wait for it to pass on its own"], act)
    signs = checks(["Vomiting", "Lack of appetite", "Fever", "Diarrhea", "Weakness", "Swollen lymph nodes", "Dehydration"])
    body = (phero("Salmon poisoning in dogs",
                  "Salmon poisoning is an infection dogs get from eating raw salmon, trout and other fish that swim upstream to breed. It is most common west of the Cascades, and it is treatable when it is caught early.",
                  [("Home", "index.html"), ("Portland hazards", "portland-pet-hazards.html"), ("Salmon poisoning", "")], side,
                  [("Within six days", "is when signs generally appear"), ("Nine in ten", "dogs with symptoms die without treatment"), ("Two days", "is how fast most treated dogs improve")], buttons=False)
            + f'''<section class="sec white"><div class="w article-g">
<div class="prose">
<h2>What causes salmon poisoning?</h2>
<p>The fish can carry a parasite, a fluke called Nanophyetus salmincola. The fluke can carry a bacteria like organism called Neorickettsia helminthoeca, and that organism is what makes a dog sick. The illness is seen only in dogs.</p>
<h2>Which dogs are at risk?</h2>
<p>Any dog that eats raw salmon, trout or another fish that runs upstream. In Portland that usually means a carcass on a riverbank in the fall, scraps from cleaning a catch, or a raw fillet taken off a counter.</p>
<h2>What are the signs?</h2>
<p>Signs generally appear within six days of eating an infected fish.</p>
{signs}
<h2>How serious is it?</h2>
<p>Ninety percent of dogs that show symptoms die without treatment, usually within two weeks of eating the fish. With treatment, the outlook is good.</p>
<h2>How is it diagnosed and treated?</h2>
<p>We look for the fluke's eggs in a stool sample, or take a needle sample from a swollen lymph node. Treatment is an antibiotic to kill the organism and a wormer to clear the fluke. Most dogs show dramatic improvement within two days.</p>
<h2>How do I prevent it?</h2>
<p>Keep your dog leashed along rivers when the fish are running, from September through December. Bag heads, skin and scraps when you clean a catch, and put the bag where a dog cannot reach it. Cook any fish you plan to share.</p>
<p class="fine">The medical facts on this page come from the <a href="https://hospital.vetmed.wsu.edu/2021/10/29/salmon-poisoning/">Washington State University Veterinary Teaching Hospital</a>. This page is general guidance and cannot examine your dog.</p>
</div>
{aside}
</div></section>
''' + faq_block("Salmon poisoning, answered", SALMON_FAQ) + book(reason="Sick visit"))
    desc = "Salmon poisoning in dogs comes from raw salmon and trout. Signs appear within six days, and treatment works when it starts early. Here is what to watch for."
    schemas = [org_schema(), business_schema(), faq_schema(SALMON_FAQ),
               crumbs_schema([("Home", ""), ("Portland hazards", "portland-pet-hazards.html"), ("Salmon poisoning", "salmon-poisoning.html")]),
               article_schema("Salmon poisoning in dogs", desc, "salmon-poisoning.html")]
    write("salmon-poisoning.html", page("salmon-poisoning.html", "Salmon Poisoning in Dogs: Signs and Treatment | Fernhollow", desc, schemas, "hazards", body))


def build_pricing():
    groups = ""
    for name, items in PRICE_GROUPS:
        groups += f'<h3 class="grp">{name}</h3>' + table(("Item", "What it covers", "Price"), items, f"Fernhollow sample prices: {name.lower()}", "tbl price")
    how = [("The exam price is fixed", "A wellness exam is $78 and a same day sick visit is $95, whoever you see and however long it takes."),
           ("Everything else is estimated in writing", "The estimate has a low and a high number. You approve it before any test or treatment starts."),
           ("We call before going over", "If something changes during a procedure, the veterinarian calls you with the reason and the new number before continuing."),
           ("The invoice matches the estimate", "Line for line. If an item was not needed, it comes off.")]
    body = (phero("What a vet visit costs at Fernhollow",
                  "Every exam and vaccine price is on this page. Anything beyond the exam gets a written estimate first, and you approve it before we start.",
                  [("Home", "index.html"), ("Prices", "")], "",
                  [("$78", "for a wellness exam"), ("$95", "for a same day sick visit"), ("In writing", "an estimate before anything else")])
            + f'''<section class="sec white" aria-labelledby="list-h"><div class="w">
<h2 id="list-h">The price list</h2>
<p class="intro">Sample prices for this demo. A live site would show your own.</p>
{groups}
</div></section>
<section class="sec" aria-labelledby="how-h"><div class="w two-col">
<div><h2 id="how-h">How do estimates work?</h2><p>Most surprise bills come from work that was never priced out loud. Four habits keep that from happening here.</p></div>
{rows(how)}
</div></section>
''' + services_section("white", title="What is each visit for?") + faq_block("Vet prices, answered", PRICING_FAQ) + book())
    schemas = [org_schema(), business_schema(), faq_schema(PRICING_FAQ), crumbs_schema([("Home", ""), ("Prices", "pricing.html")])]
    write("pricing.html", page("pricing.html", "Vet Prices in Sellwood, Portland | Fernhollow Vet",
                               "Vet prices at Fernhollow in Sellwood, Portland: wellness exam $78, same day sick visit $95, vaccines from $30, and a written estimate before anything else.",
                               schemas, "pricing", body))


def build_new_clients():
    body = (phero("How a first visit works",
                  "New clients are welcome, and most first visits are booked within the week. Here is what to expect and what to bring.",
                  [("Home", "index.html"), ("New clients", "")],
                  pic("carrier-fog", "An orange tabby cat looking out of an open grey pet carrier against a pale blue background"),
                  [("Within the week", "for most first visits"), ("Forty minutes", "for a puppy or kitten first visit"), ("Ten minutes early", "is the right time to arrive")])
            + f'''<section class="sec white" aria-labelledby="first-h"><div class="w two-col">
<div><h2 id="first-h">What happens at a first visit?</h2>{steps(NEW_STEPS)}</div>
<div><h2>What should I bring?</h2>{checks(NEW_BRING)}
<p class="note">Sick today? Skip the form and call <a href="tel:{TEL}">{PHONE}</a> before 3 PM. We see new clients the same day too.</p></div>
</div></section>
<section class="sec" aria-labelledby="info-h"><div class="w two-col">
<div><h2 id="info-h">How do you handle my information?</h2><p>A clinic holds names, addresses, phone numbers and medical records. We keep the website out of most of it, and we are careful with the rest.</p><p><a href="privacy.html">Read the privacy page</a></p></div>
{rows(NEW_INFO)}
</div></section>
''' + services_section("white", title="What can I book?") + faq_block("New clients, answered", NEW_FAQ) + book())
    schemas = [org_schema(), business_schema(), faq_schema(NEW_FAQ), crumbs_schema([("Home", ""), ("New clients", "new-clients.html")])]
    write("new-clients.html", page("new-clients.html", "New Clients | Fernhollow Veterinary Clinic, Portland",
                                   "New to Fernhollow Veterinary Clinic in Sellwood, Portland? Here is how a first visit works, what to bring, and how we handle your information.",
                                   schemas, "new", body))


def build_about():
    story = ["Maren Halvorsen spent ten years in emergency medicine before she opened Fernhollow in 2012. Most of what she saw on those nights had started days earlier as something small, with an owner who was not sure whether to call.",
             "So the clinic was built around that question. A technician answers the phone. The site sorts the common signs into three speeds. Sick pets are seen the day you call.",
             "Fernhollow is independent, and it sees dogs and cats only. Three people will know your pet by name."]
    body = (phero("A neighborhood veterinary clinic in Sellwood since 2012",
                  "Fernhollow is an independent dog and cat clinic in a green bungalow a few blocks from the Sellwood Bridge.",
                  [("Home", "index.html"), ("About", "")], pic("exterior", EXTERIOR_ALT),
                  [("2012", "the year the clinic opened"), ("Two species", "dogs and cats, and only those"), ("Independent", "owned by the veterinarian who works here")])
            + f'''<section class="sec white" aria-labelledby="story-h"><div class="w two-col">
{prose("Why does Fernhollow exist?", story, "story-h")}
<div><h2>How do you work?</h2>{rows(ABOUT_ROWS)}</div>
</div></section>
<section class="sec" id="team" aria-labelledby="team-h"><div class="w team-g">
<img src="img/exam.webp" alt="{EXAM_ALT}" loading="lazy" width="1600" height="1200">
<div><h2 id="team-h">Who will see your pet?</h2>{team_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>
<section class="sec white" aria-labelledby="visit-h"><div class="w two-col">
<div><h2 id="visit-h">Where is the clinic and when is it open?</h2>
<p>We are in Sellwood, a short walk from the off leash area at Sellwood Riverfront Park, which sits at SE Spokane Street and Oaks Parkway. There is parking behind the building and a covered porch for rainy day waits.</p></div>
<div>{hours_table()}</div>
</div></section>
''' + areas_section("") + faq_block("About the clinic, answered", ABOUT_FAQ, "white") + book())
    people = [{"@context": "https://schema.org", "@type": "Person", "name": n.replace("Dr. ", ""), "jobTitle": r, "worksFor": {"@id": f"{BASE}/#org"}} for n, r, _ in PEOPLE]
    schemas = [org_schema(), business_schema(), faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("About", "about.html")])] + people
    write("about.html", page("about.html", "About Fernhollow Veterinary Clinic | Sellwood, Portland",
                             "Fernhollow Veterinary Clinic is an independent dog and cat clinic in Sellwood, Portland, opened in 2012 by a veterinarian with ten years in emergency care.",
                             schemas, "about", body))


def build_area(slug):
    a, c = AREA_BY[slug], AREA_PAGES[slug]
    side = panel("ink", "The clinic", ["Sellwood, Portland, OR 97202", "Monday to Friday, 7:30 AM to 6 PM", "Saturday, 9 AM to 2 PM", "Parking behind the building"],
                 f'<a class="lane-act" href="tel:{TEL}"><b>Call {PHONE}</b>A technician answers</a>')
    notes = table(("What we see here", "What we do about it"), c["notes"], f'Pet care notes for {a["name"]}')
    body = (phero(c["h1"], c["lede"], [("Home", "index.html"), ("About", "about.html"), (a["name"], "")], side)
            + f'''<section class="sec white" aria-labelledby="loc-h"><div class="w two-col">
{prose(c["body_title"], c["body"], "loc-h")}
<div><h2>What do we plan for here?</h2>{notes}<p class="fine">Seasonal risks for the whole city are in the <a href="portland-pet-hazards.html">Portland hazards guide</a>.</p></div>
</div></section>
''' + services_section("", title=f'What do you do for pets from {a["name"]}?') + areas_section("white", exclude=slug, title="Where else do your clients come from?")
            + faq_block(f'{a["name"]} pet owners ask', c["faq"]) + book())
    schemas = [org_schema(), business_schema(), faq_schema(c["faq"]), crumbs_schema([("Home", ""), ("About", "about.html"), (a["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "about", body))


def build_privacy():
    body_html = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (phero("Your privacy at Fernhollow",
                  "What this website collects, how your pet's records are handled, and what we will never ask you for.",
                  [("Home", "index.html"), ("Privacy", "")], buttons=False)
            + f'''<section class="sec white"><div class="w narrow"><div class="prose legal">{body_html}
<p class="fine">This is a demo site by Meraki is Love. Fernhollow is a fictional clinic, and nothing entered on this site is sent anywhere. Read more about <a href="new-clients.html">a first visit</a>, <a href="services.html">our services</a> or <a href="about.html">the clinic</a>.</p>
</div></div></section>
''' + book())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy | Fernhollow Veterinary Clinic",
                               "How Fernhollow Veterinary Clinic handles your information: what the website collects, how pet records are released, and what we never ask for.",
                               schemas, "", body))


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    print("Building Fernhollow demo:")
    build_home()
    build_services_hub()
    for sv in SERVICES:
        build_service(sv["slug"])
    build_emergencies()
    build_hazards()
    build_salmon()
    build_pricing()
    build_new_clients()
    build_about()
    for ar in AREAS:
        build_area(ar["slug"])
    build_privacy()
    if PROBLEMS:
        print("\nProblems:")
        for p in PROBLEMS:
            print("  " + p)
        sys.exit(1)
