"""Build The Meraki Inn demo into public/demos/meraki-inn/.

Run from the repo root:  python3 scripts/demos/meraki-inn/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
The design is "The Day": the home page is one day at the inn, hour by hour,
set to today's sunrise and sunset, and every other page opens on its own hour.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from mi import *  # noqa: E402,F403
from content import *  # noqa: E402,F403

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "meraki-inn")
# The home page is also served at the clean URL /demos/meraki-inn (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/meraki-inn/")
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
def the_clock(spec):
    kind = spec[0]
    if kind == "live":
        return clock_live(spec[1], spec[2])
    return clock(spec[1], spec[2])


def opener(tone, crumb_items, when, clock_html, h1, lede, picture="", tall=False, rev=False, actions=True):
    """Every inner page opens the way an hour on the home page does: the hour in very
    large numerals, then the page's claim beside a photograph that hangs over the edge."""
    dark = " dark" if tone == "night" else ""
    tall_cls = ' class="tall"' if tall else ""
    fig = f"<figure{tall_cls}>{pic(picture, first=True)}</figure>" if picture else ""
    acts = gos(BOOK, CALL) if actions else ""
    layout = (" rev" if rev else "") + ("" if picture else " solo")
    return f'''<section class="hour {tone}{dark} opener{"" if picture else " nofig"}">
<div class="hour-title">{crumbs(crumb_items)}<p class="when">{when}</p>{clock_html}<hr class="hair wide"></div>
<div class="hour-g{layout}"><div class="hour-copy"><h1>{h1}</h1><p class="lede">{lede}</p>{acts}</div>
{fig}</div>
</section>
'''


def table(head, body_rows, caption):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    # With three or more columns, each cell carries its column name so the phone layout can label it.
    lab = len(head) >= 3
    body = ""
    for r in body_rows:
        cells = "".join(f'<td data-label="{head[i + 1]}">{c}</td>' if lab else f"<td>{c}</td>" for i, c in enumerate(r[1:]))
        body += f'<tr><th scope="row">{r[0]}</th>{cells}</tr>'
    return f'<div class="tw"><table class="tbl{" lab" if lab else ""}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def rows(items):
    return '<ul class="rows">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items) + "</ul>"


def steps(items):
    """A numbered sequence, for things that happen in order."""
    return '<ol class="rows steps">' + "".join(f"<li><h3>{t}</h3><p>{d}</p></li>" for t, d in items) + "</ol>"


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def bg_class(d):
    bg = d.get("bg", "")
    return "sec" + (f" {bg}" if bg else "")


def sec_lead(d, n):
    """Heading on the left, reading text on the right."""
    paras = "".join(f"<p>{p}</p>" for p in d["paras"])
    return f'''<section class="{bg_class(d)}" aria-labelledby="s{n}"><div class="lead-g">
<div><p class="label">{d["label"]}</p><h2 class="cap" id="s{n}">{d["title"]}</h2></div>
<div class="prose">{paras}</div>
</div></section>
'''


def sec_rows(d, n, ordered=False):
    items = list(d.get("items", []))
    if d.get("island"):
        items = ISLAND[:1] + d.get("extra", []) + ISLAND[1:]
    listing = steps(items) if ordered else rows(items)
    return f'''<section class="{bg_class(d)}" aria-labelledby="s{n}"><div class="lead-g">
<div><p class="label">{d["label"]}</p><h2 class="cap" id="s{n}">{d["title"]}</h2><p>{d["intro"]}</p></div>
{listing}
</div></section>
'''


def sec_table(d, n):
    return f'''<section class="{bg_class(d)} center" aria-labelledby="s{n}">
<h2 class="cap" id="s{n}">{d["title"]}</h2><hr class="hair">
{table(d["head"], d["rows"], d["caption"])}
</section>
'''


def sec_checks(d, n):
    picture = f'<figure>{pic(d["pic"])}</figure>' if d.get("pic") else ""
    return f'''<section class="{bg_class(d)}" aria-labelledby="s{n}"><div class="split">
<div><p class="label">{d["label"]}</p><h2 class="cap" id="s{n}">{d["title"]}</h2><p>{d["intro"]}</p>{checks(d["items"])}</div>
{picture}
</div></section>
'''


def people_list():
    return '<ul class="people">' + "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in PEOPLE) + "</ul>"


def sec_people(d, n, with_pic=False):
    picture = f'<figure>{pic("innkeeper")}</figure>' if with_pic else f'<figure>{pic("porch-golden")}</figure>'
    return f'''<section class="{bg_class(d)}" aria-labelledby="people-h"><div class="split">
{picture}
<div><p class="label">The people</p><h2 class="cap" id="people-h">Who keeps the inn?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>
'''


def rates_table(caption="Sample rates for this demo, before tax. Every rate includes breakfast for two."):
    body = [(f'<a href="{r["slug"]}.html">{r["name"]}</a>', r["bed"], r["where"], f'${r["rate"]}') for r in ROOMS]
    return table(["Room", "Bed", "Where", "A night"], body, caption)


def sec_rates(d, n):
    return f'''<section class="sec center" aria-labelledby="s{n}">
<h2 class="cap" id="s{n}">What does a night cost?</h2><hr class="hair">
{rates_table()}
</section>
'''


def room_block(r, i):
    cls = "block" + (" flip" if i % 2 else "") + ("" if r["second"] else " solo")
    small = f'<figure class="small">{pic(r["second"])}</figure>\n' if r["second"] else ""
    return f'''<article class="{cls}" id="{r["key"]}">
{small}<div class="card"><p class="label">{r["label"]}</p><h3>{r["name"]}</h3>
<p><b>{r["line"]}</b> {r["craft"]}</p>
<p class="rate">${r["rate"]} a night, breakfast included</p>
<p class="gos">{go(r["slug"] + ".html", "See " + r["name"])}<button class="go" type="button" data-pick="{r["key"]}">Stay in {r["name"]}</button></p></div>
<figure class="big">{pic(r["pic"])}</figure>
</article>
'''


def more_links(links, title="Keep reading"):
    return f'''<section class="sec more" aria-label="{title}"><div class="w">
<p class="label">{title}</p>
<p class="gos wide">{"".join(go(h, t) for h, t in links)}</p>
</div></section>
'''


DRAW = {"lead": sec_lead, "rows": sec_rows, "table": sec_table, "checks": sec_checks, "rates": sec_rates}


def draw(sections):
    out = ""
    for n, (kind, d) in enumerate(sections, 1):
        if kind == "steps":
            out += sec_rows(d, n, ordered=True)
        elif kind == "people":
            out += sec_people(d, n)
        else:
            out += DRAW[kind](d, n)
    return out


# ---------------------------------------------------------------- pages
def hour(cls, hid, name, clock_html, copy, figure, layout="", attrs=""):
    return f'''<section class="hour {cls}"{attrs} aria-labelledby="{hid}">
<div class="hour-title"><h2 id="{hid}">{name}</h2>{clock_html}<hr class="hair wide"></div>
<div class="hour-g{layout}"><div class="hour-copy">{copy}</div>
{figure}</div>
</section>
'''


def build_home():
    hours = hour("dawn", "h-first", "First light", clock_live("sunrise", "Sunrise"),
                 "<p><b>The Gulf side of the island faces southeast,</b> so the sun comes up over the water. The beach is a ten minute bike ride from the porch, and we keep six bikes by the side gate.</p>"
                 "<p>Coffee is out in the hall from 6:30 for anyone who wants to carry a cup down there.</p>"
                 + gos(go("the-island.html", "What is near the inn")),
                 f'<figure>{pic("beach-sunrise")}</figure>')
    hours += hour("morning over", "h-break", "Breakfast on the gallery", clock("8:00", "AM"),
                  "<p><b>Isadora bakes before sunrise and cooks to order from 8 to 9:30.</b> Eat upstairs on the gallery, where the palms are at eye level.</p>"
                  "<p>The word meraki is Greek. It means doing something with soul, creativity and love, so that a piece of you ends up in the work. Breakfast is where most guests first see what we mean by it.</p>"
                  + gos(go("breakfast.html", "See this week's breakfast")),
                  f'<figure>{pic("breakfast")}</figure>', " rev")
    hours += hour("noon over", "h-island", "The island", clock("11:00", "AM"),
                  "<p><b>Everything here is close enough for a bicycle.</b> The inn sits in the East End, about half a mile from The Strand on one side and a short ride from the Seawall on the other.</p>"
                  + gos(go("the-island.html", "The island, by bicycle"), go("cruise-parking.html", "The night before a cruise")),
                  rows(ISLAND), " flat", ' id="island"')
    hours += hour("golden", "h-porch", "Porch hour", clock_live("golden", "Golden hour"),
                  "<p><b>An hour before sunset the light comes in low under the porch ceiling.</b> There is iced tea on the table and a rocking chair for everyone who wants one.</p>"
                  "<p>After the 1900 Storm, Galveston lifted about 2,000 buildings on jackscrews and pumped sand underneath. This house was one of them, porch and all.</p>"
                  + gos(go("the-house.html", "The house and the 1900 Storm")),
                  f'<figure>{pic("porch-golden")}</figure>', " rev")
    night = f'''<section class="hour night dark over" id="rooms" aria-labelledby="h-night">
<div class="hour-title"><h2 id="h-night">Lamplight</h2>{clock_live("sunset", "Sunset")}<hr class="hair wide"></div>
<div class="hour-g flat"><div class="hour-copy"><p><b>The lantern by the door goes on at sunset.</b> There are five rooms, four in the house and a suite in the carriage house, each furnished around one craft made by hand in Texas.</p>
{gos(go("rooms.html", "See the five rooms"))}</div>
<figure>{pic("room-darkroom")}</figure></div>
<div class="hour-table">{rates_table("Sample rates for this demo, before tax. Every rate includes breakfast for two.")}</div>
</section>
'''
    body = f'''<section class="block solo hero" id="inn">
<div class="card"><p class="label">Galveston, Texas</p>
<h1>A day at The Meraki Inn, hour by hour.</h1>
<p>Five rooms in an 1894 house on Galveston's East End. Here is what a day looks like, set to today's sun.</p>
<p class="sun" data-sun>Today in Galveston the sun rises over the Gulf and sets behind the bay.</p>
{gos(BOOK, CALL)}</div>
<figure class="big">{pic("exterior", first=True)}</figure>
</section>

{hours}{night}
<section class="sec" aria-labelledby="people-h"><div class="split">
<figure>{pic("innkeeper")}</figure>
<div><p class="label">The people</p><h2 class="cap" id="people-h">Who keeps the inn?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p>
{gos(go("about.html", "What meraki means here"))}</div>
</div></section>
{faq_section("Before you book", HOME_FAQ)}{stay_section()}'''
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    write("index.html", page("index.html", HOME_TITLE, HOME_DESC, schemas, "", body))


def build_rooms():
    p = ROOMS_HUB
    blocks = "".join(room_block(r, i) for i, r in enumerate(ROOMS))
    body = (opener(p["tone"], p["crumbs"], p["when"], the_clock(p["clock"]), p["h1"], p["lede"], p["pic"])
            + f'''<section class="sec mist center" aria-labelledby="s1">
<h2 class="cap" id="s1">Which room is which?</h2><hr class="hair">
{rates_table()}
</section>
<div class="blocks">
{blocks}</div>
'''
            + sec_rows({"label": "Choosing", "title": "How do I choose a room?", "intro": "Tell Celeste what the trip is for and she will know. Until then, this is how most guests choose.", "items": p["choose"]}, 2)
            + faq_section("The rooms, answered", p["faq"]) + stay_section())
    schemas = [org_schema(), business_schema(), faq_schema(p["faq"]), crumbs_schema([("Home", ""), ("Rooms", "rooms.html")])]
    write("rooms.html", page("rooms.html", p["title"], p["desc"], schemas, "rooms", body))


def build_room(slug):
    r, p = ROOM[slug], ROOM_PAGES[slug]
    others = [(o["slug"] + ".html", f'{o["name"]}, ${o["rate"]}') for o in ROOMS if o["slug"] != slug]
    details = [("Bed", r["bed"]), ("Where", r["where"]), ("Bath", p["bath"]), ("Sleeps", "Two"),
               ("Rate", f'${r["rate"]} a night with breakfast, before tax'), ("Good to know", p["know"])]
    second = r["second"] or "entry-hall"
    body = (opener(p["tone"], [("Home", "index.html"), ("Rooms", "rooms.html"), (r["name"], "")], p["when"], the_clock(p["clock"]), p["h1"], p["lede"], r["pic"], tall=p.get("tall", False))
            + f'''<section class="sec" aria-labelledby="s1"><div class="split">
<div><p class="label">{r["label"]}</p><h2 class="cap" id="s1">What is in the room?</h2>{checks(p["checks"])}
<p class="gos"><button class="go" type="button" data-pick="{r["key"]}">Stay in {r["name"]}</button></p></div>
<figure>{pic(second)}</figure>
</div></section>
'''
            + sec_lead({"bg": "dark", "label": "The craft", "title": p["story_title"], "paras": p["story"]}, 2)
            + sec_table({"bg": "mist", "title": f'{r["name"]} at a glance', "head": ["Detail", r["name"]], "rows": details,
                         "caption": "The rate is a sample for this demo."}, 3)
            + faq_section(f'{r["name"]}, answered', p["faq"])
            + more_links(others + [("rooms.html", "All five rooms")], "The other rooms")
            + stay_section(slug, title=f'Ask for {r["name"]}', lead=f'{r["name"]} is already chosen below. Pick an arrival day and the number of nights, and the innkeeper replies the same day.'))
    schemas = [org_schema(), room_schema(r, p["desc"]), faq_schema(p["faq"]),
               crumbs_schema([("Home", ""), ("Rooms", "rooms.html"), (r["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", p["title"], p["desc"], schemas, "rooms", body))


def build_page(p):
    body = (opener(p["tone"], p["crumbs"], p["when"], the_clock(p["clock"]), p["h1"], p["lede"], p["pic"], tall=p.get("tall", False))
            + draw(p["sections"]) + faq_section(p["faq_title"], p["faq"]) + more_links(p["more"]) + stay_section())
    trail = [(n, "" if n == "Home" else (h or f'{p["slug"]}.html')) for n, h in p["crumbs"]]
    schemas = [org_schema(), business_schema(), faq_schema(p["faq"]), crumbs_schema(trail)]
    if p.get("article"):
        schemas.insert(2, article_schema(p["h1"], p["desc"], f'{p["slug"]}.html'))
    write(f'{p["slug"]}.html', page(f'{p["slug"]}.html', p["title"], p["desc"], schemas, p["nav"], body))


def build_privacy():
    body_html = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{x}</p>" for x in ps) for h, ps in PRIVACY)
    body = (opener("noon", [("Home", "index.html"), ("Privacy", "")], "What the form asks for", clock("5", "things"),
                   "Your privacy at The Meraki Inn", "What this website collects, how a card is taken, and what we will never ask you for.", actions=False)
            + f'''<section class="sec mist"><div class="w narrow"><div class="prose legal">{body_html}
<p class="fine">This is a demo site by Meraki is Love. The Meraki Inn is a fictional inn, and nothing entered on this site is sent anywhere. Read more about <a href="about.html">who keeps the inn</a>, <a href="stay.html">rates and policies</a> or <a href="rooms.html">the rooms</a>.</p>
</div></div></section>
''' + stay_section())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy | The Meraki Inn, Galveston",
                               "How The Meraki Inn handles your details: the five things the date request form asks for, how a card is taken, and what we never ask for.",
                               schemas, "", body))


# ---------------------------------------------------------------- the assistant's knowledge
def plain(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", str(text)).replace("&amp;", "&")).strip()


def knowledge_text():
    """Everything the chat assistant may say, drawn from the same content the pages are
    built from. If a rate or a policy changes in content.py, the assistant changes with it."""
    out = ["THE INN IN SHORT",
           f"The Meraki Inn is a five room inn in an 1894 house in Galveston's East End Historic District, Galveston, TX 77550. Phone {PHONE}.",
           "Four rooms are in the house and one is a suite in the carriage house. Every rate includes breakfast for two.",
           "Check in is from 3 PM to 8 PM. Check out is by 11 AM. Parking is free for guests in the gated lot behind the house. Six bicycles are free for guests.",
           "The innkeeper and owner is Celeste Arceneaux. The breakfast cook is Isadora Fontenot.", ""]
    out.append("THE ROOMS")
    for r in ROOMS:
        p = ROOM_PAGES[r["slug"]]
        out += [f'{r["name"]} (form value: {r["key"]}). ${r["rate"]} a night with breakfast, before tax. {r["bed"]} bed. {r["where"]}. Bath: {p["bath"]}. Sleeps two.',
                plain(r["line"] + " " + r["craft"]), "In the room: " + "; ".join(plain(c) for c in p["checks"]) + ".",
                "Good to know: " + plain(p["know"]) + ".", " ".join(plain(x) for x in p["story"])]
        out += [f"Q: {plain(q)} A: {plain(a)}" for q, a in p["faq"]]
        out.append("")
    out.append("CHOOSING A ROOM")
    out += [f"{plain(t)}: {plain(d)}" for t, d in ROOMS_HUB["choose"]]
    out += [f"Q: {plain(q)} A: {plain(a)}" for q, a in ROOMS_HUB["faq"]]
    out.append("")
    for p in PAGES:
        out += [f'PAGE: {plain(p["h1"])}', plain(p["lede"])]
        for kind, d in p["sections"]:
            if kind == "rates":
                continue
            if d.get("title"):
                out.append(plain(d["title"]))
            if d.get("intro"):
                out.append(plain(d["intro"]))
            out += [plain(x) for x in d.get("paras", [])]
            items = list(d.get("items", []))
            if d.get("island"):
                items = ISLAND[:1] + d.get("extra", []) + ISLAND[1:]
            for it in items:
                out.append(f"{plain(it[0])}: {plain(it[1])}" if isinstance(it, tuple) else plain(it))
            if d.get("rows"):
                out.append(" | ".join(d["head"]))
                out += [" | ".join(plain(c) for c in row) for row in d["rows"]]
                out.append(plain(d["caption"]))
        out += [f"Q: {plain(q)} A: {plain(a)}" for q, a in p["faq"]]
        out.append("")
    out.append("MORE QUESTIONS")
    out += [f"Q: {plain(q)} A: {plain(a)}" for q, a in HOME_FAQ]
    out += ["", "PRIVACY"]
    for h, ps in PRIVACY:
        out.append(plain(h) + " " + " ".join(plain(x) for x in ps))
    return "\n".join(out).strip() + "\n"


def write_knowledge():
    import json
    path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "lib", "meraki-inn-knowledge.json")
    data = {"note": "Generated by scripts/demos/meraki-inn/build.py. Do not edit by hand.",
            "phone": PHONE,
            "rooms": [{"key": r["key"], "name": r["name"], "rate": r["rate"]} for r in ROOMS],
            "knowledge": knowledge_text()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f'  lib/meraki-inn-knowledge.json  {len(data["knowledge"].split())} words')


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    print("Building The Meraki Inn demo:")
    build_home()
    build_rooms()
    for room in ROOMS:
        build_room(room["slug"])
    for pg in PAGES:
        build_page(pg)
    build_privacy()
    write_knowledge()
    if PROBLEMS:
        print("\nProblems:")
        for prob in PROBLEMS:
            print("  " + prob)
        sys.exit(1)
