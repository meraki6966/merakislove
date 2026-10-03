"""Build the Sideoats Insurance Agency demo into public/demos/sideoats/.

Run from the repo root:  python3 scripts/demos/sideoats/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
The design is "The Deductible": the home page works out a percentage hail
deductible in dollars, and every other page opens with one circled number.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from so import *  # noqa: E402,F403
from content import *  # noqa: E402,F403

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "sideoats")
# The home page is also served at the clean URL /demos/sideoats (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/sideoats/")
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
    # With three or more columns, each cell carries its column name so the phone layout can label it.
    lab = len(head) >= 3
    body = ""
    for r in body_rows:
        cells = "".join(f'<td data-label="{head[i + 1]}">{c}</td>' if lab else f"<td>{c}</td>" for i, c in enumerate(r[1:]))
        body += f'<tr><th scope="row">{r[0]}</th>{cells}</tr>'
    return f'<div class="tw"><table class="{cls}{" lab" if lab else ""}"><caption>{caption}</caption><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def prose(title, paras, hid=""):
    h = f' id="{hid}"' if hid else ""
    return f'<div class="prose"><h2{h}>{title}</h2>' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def figure(img, alt, caption=""):
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    return f'<figure class="pic"><img src="img/{img}.webp" alt="{alt}" loading="lazy" width="1600" height="1200">{cap}</figure>'


def cov_grid(exclude=None):
    """All six, always, so the grid stays whole. The page you are on is marked and is not a link."""
    out = ""
    for c in COVERAGES:
        if c["slug"] == exclude:
            out += f'<li class="here" aria-current="page"><h3>{c["name"]}</h3><p>You are on this page.</p></li>'
        else:
            out += f'<li><h3><a href="{c["slug"]}.html">{c["name"]}</a></h3><p>{c["short"]}</p></li>'
    return f'<ul class="cov">{out}</ul>'


def coverage_section(bg="", exclude=None, title="What does Sideoats write?"):
    return f'''<section class="sec {bg}" id="write" aria-labelledby="write-h"><div class="w write-g">
<div><h2 id="write-h">{title}</h2><p>We are an independent agency, so your policy can be placed with the carrier that fits and checked against the others at renewal.</p>
<p><a href="coverage.html">See all coverage</a></p></div>
{cov_grid(exclude)}
</div></section>
'''


def areas_section(bg="", exclude=None, title="Where do you write policies?"):
    links = "".join(f'<li><a href="{a["slug"]}.html">{a["name"]}</a></li>' for a in AREAS if a["slug"] != exclude)
    return f'''<section class="sec {bg}" aria-labelledby="areas-h"><div class="w write-g">
<div><h2 id="areas-h">{title}</h2><p>All of Tarrant County. The office is on Magnolia Avenue in the Near Southside, and each of these places has a page on what we see there.</p></div>
<ul class="areas"><li><a href="about.html">Near Southside</a></li>{links}</ul>
</div></section>
'''


def reviews_section(bg=""):
    figs = "".join(f'<figure><blockquote>{t}</blockquote><figcaption>{w}, {where}<span>Sample review</span></figcaption></figure>' for t, w, where in REVIEWS)
    return f'''<section class="sec {bg}" aria-labelledby="rev-h"><div class="w">
<h2 id="rev-h">What do clients say?</h2>
<div class="reviews">{figs}</div>
</div></section>
'''


def people_list():
    return '<ul class="people">' + "".join(f'<li><h3>{n}</h3><p class="role">{r}</p><p>{b}</p></li>' for n, r, b in PEOPLE) + "</ul>"


def hail_scale():
    out = ""
    for n, d in HAIL:
        cls = ' class="sev"' if d == 1.0 else ""
        out += f'<li{cls} style="--d:{d}"><i aria-hidden="true"></i><b>{n}</b><span>{d:g} in</span></li>'
    return f'<ol class="hail" aria-label="Hail sizes from the National Weather Service">{out}</ol><p class="fine">Drawn to scale against each other. Sizes from the National Weather Service office in Fort Worth.</p>'


def trio():
    return '''<ul class="trio">
<li><b>30</b><h3>$30,000 for each injured person</h3><p>What your policy pays toward one person's injuries when a wreck is your fault.</p></li>
<li><b>60</b><h3>$60,000 for each accident</h3><p>The most it pays for everyone's injuries in one wreck, however many people are hurt.</p></li>
<li><b>25</b><h3>$25,000 for property damage</h3><p>What it pays to fix the other driver's vehicle. Many new trucks cost more than this.</p></li>
</ul>'''


def calc_hero(h1, lede, crumb_items=None):
    house, pct, roof = 380000, 2, 18500
    ded = house * pct // 100
    pays = max(0, roof - ded)
    you = min(roof, ded)
    share = round(you / roof * 100, 2)
    pct_opts = "".join(f'<label><input type="radio" name="pct" value="{p}"{" checked" if p == pct else ""}><span>{p}%</span></label>' for p in (1, 2, 3, 5))
    trail = crumbs(crumb_items) if crumb_items else ""
    return f'''<section class="hero" id="home"><div class="w">
<div class="calc">
<div class="calc-in">
{trail}<h1>{h1}</h1>
<p class="lede">{lede}</p>
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
<p class="big">{RING}<span data-o="ded">{money(ded)}</span></p>
<div class="bar" aria-hidden="true"><span class="you" data-bar style="width:{share}%"></span></div>
<dl class="split"><div><dt>You pay</dt><dd data-o="you">{money(you)}</dd></div><div><dt>The policy pays</dt><dd data-o="pays">{money(pays)}</dd></div></dl>
<p class="say" data-o="say">On a {money(roof)} roof, a {pct}% deductible leaves you with {money(you)} and the policy with {money(pays)}.</p>
</div>
</div>
<p class="fine">An illustration with round numbers. It is not a quote, and your policy may work differently. The percentage is applied to your dwelling coverage, the amount the house is insured for. <a href="#quote">Have us read your policy</a>.</p>
</div></section>
'''


SHINGLES_ALT = "Dark asphalt shingles seen from above, with hail bruises circled in white chalk and a stick of chalk resting on the roof"
KITCHEN_ALT = "An insurance agent in a denim shirt at a kitchen table with a homeowner couple, going over a printed page with a pen"
OFFICE_ALT = "A single story red brick office building in Fort Worth under a wide blue sky, with a pickup truck parked at the curb"


# ---------------------------------------------------------------- pages
def build_home():
    body = (calc_hero("Your hail deductible, in dollars.",
                      "Many Texas home policies set the wind and hail deductible as a percentage of what the house is insured for. Move the numbers and see what a roof claim would cost you.")
            + f'''<section class="sec" aria-labelledby="hail-h"><div class="w hail-g">
<div><h2 id="hail-h">How big was the hail?</h2>
<p>The National Weather Service office in Fort Worth sizes hail against things you already own. A storm counts as severe once the stones reach one inch across, the size of a quarter.</p>
{hail_scale()}</div>
<div><figure class="pic wide"><img src="img/shingles-chalk.webp" alt="{SHINGLES_ALT}" loading="lazy" width="1200" height="900"><figcaption>An adjuster circles each hail hit in chalk before counting them.</figcaption></figure>
<h3>After a storm, in this order</h3>
<ol class="steps plain"><li>Take photos of the roof, the gutters and the car before anything is cleaned up.</li><li>Call us before a roofer asks you to sign anything.</li><li>We compare the repair estimate with your deductible, so you know whether a claim pays before you file one.</li></ol>
<p class="more"><a href="after-a-hail-storm.html">The full list for the day after a storm</a></p></div>
</div></section>

<section class="sec dark" id="auto" aria-labelledby="auto-h"><div class="w">
<h2 id="auto-h">What does 30/60/25 mean?</h2>
<p class="intro">It is the least auto liability coverage Texas lets you drive with. Each number is in thousands of dollars.</p>
{trio()}
<p class="fine">Every Texas auto policy also includes personal injury protection unless you turned it down in writing, and your insurer has to offer uninsured motorist coverage. <a href="auto-insurance.html">Read the auto page</a>.</p>
</div></section>

{coverage_section("")}
<section class="sec tint" id="people" aria-labelledby="people-h"><div class="w people-g">
{figure("kitchen", KITCHEN_ALT)}
<div><h2 id="people-h">Who reads your policy?</h2>{people_list()}<p class="fine">Fictional people, written for this demo. <a href="about.html">About the agency</a>.</p></div>
</div></section>
''' + reviews_section("") + areas_section("tint") + faq_block("Questions we answer every week", HOME_FAQ) + quote())
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ), crumbs_schema([("Home", "")])]
    write("index.html", page("index.html", "Insurance Agency in Fort Worth, TX | Sideoats Insurance",
                             "Sideoats is an independent insurance agency in Fort Worth, Texas. Home, auto and business coverage, with your hail deductible worked out in dollars first.",
                             schemas, "", body))


def build_coverage_hub():
    body = (opener("Insurance for Fort Worth homes, cars and small businesses",
                   "Six kinds of policy cover most of what a household or a small business needs. Each has its own page, and each starts with the one number worth knowing.",
                   [("Home", "index.html"), ("Coverage", "")], "Kinds of policy we write", "6",
                   "Home, auto, renters, flood, business and umbrella. We place each one with the carrier that fits it.")
            + f'''<section class="sec tint" aria-labelledby="all-h"><div class="w">
<h2 id="all-h">Which policy are you looking for?</h2>
{cov_grid()}
</div></section>
<section class="sec" aria-labelledby="how-h"><div class="w two-col">
<div><h2 id="how-h">How does Sideoats work?</h2><p>The same four habits apply to every policy we write. They come from twelve years Rosalind spent on the claims side.</p><p><a href="switching.html">How switching to us works</a></p></div>
{rows(ABOUT_ROWS)}
</div></section>
''' + areas_section("tint") + faq_block("Choosing coverage, answered", COVERAGE_FAQ) + quote())
    schemas = [org_schema(), business_schema(), faq_schema(COVERAGE_FAQ), crumbs_schema([("Home", ""), ("Coverage", "coverage.html")]),
               {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": c["name"] + " insurance", "url": f'{BASE}/{c["slug"]}.html'} for i, c in enumerate(COVERAGES)]}]
    write("coverage.html", page("coverage.html", "Insurance Coverage in Fort Worth, TX | Sideoats Insurance",
                                "Home, auto, renters, flood, business and umbrella insurance in Fort Worth from an independent agency. Each page starts with the number worth knowing.",
                                schemas, "coverage", body))


def build_coverage(slug):
    s, c = COV[slug], COVERAGE_PAGES[slug]
    name = f'{s["name"]} insurance'
    label, number, caption = c["fig"]
    body = opener(c["h1"], c["lede"], [("Home", "index.html"), ("Coverage", "coverage.html"), (name, "")], label, number, caption)
    if c.get("trio"):
        body += f'''<section class="sec dark" aria-labelledby="trio-h"><div class="w">
<h2 id="trio-h">What does 30/60/25 mean?</h2>
<p class="intro">It is the least auto liability coverage Texas lets you drive with. Each number is in thousands of dollars.</p>
{trio()}
</div></section>
'''
    note = f'<p class="fine">{c["main_note"]}</p>' if c.get("main_note") else ""
    body += f'''<section class="sec tint" aria-labelledby="main-h"><div class="w">
<h2 id="main-h">{c["main_title"]}</h2>
{table(c["main_head"], c["main"], f"{name} at Sideoats", "tbl last" if len(c["main_head"]) == 3 and slug == "umbrella-insurance" else "tbl")}
{note}
</div></section>
'''
    if c.get("lists"):
        cols = "".join(f"<div><h2>{t}</h2>{checks(items) if i == 0 else rows_plain(items)}</div>" for i, (t, items) in enumerate(c["lists"]))
        body += f'<section class="sec" aria-label="What is and is not covered"><div class="w two-col">{cols}</div></section>\n'
    if c.get("limits"):
        side = ("<div><h2>Which limits do people choose?</h2>"
                + table(("Limits", "What it is", "Property damage"), c["limits"], "Common auto liability limits", "tbl last")
                + '<p class="fine">Limits are written as injury per person, injury per accident, and property damage, in thousands of dollars.</p></div>')
    elif c.get("checks"):
        side = f'<div><h2>{c["checks_title"]}</h2>{checks(c["checks"])}</div>'
    elif c.get("img"):
        side = figure(c["img"][0], c["img"][1])
    else:
        side = (f'<div class="note"><h2>One thing to do this week</h2><p>Find the liability limits on your auto and home policies. They are on the first page. '
                f'Call <a href="tel:{TEL}">{PHONE}</a> and we will tell you what an umbrella would sit on top of.</p></div>')
    bg = "" if not c.get("lists") else "tint"
    body += f'''<section class="sec {bg}" aria-labelledby="body-h"><div class="w two-col">
{prose(c["body_title"], c["body"], "body-h")}
{side}
</div></section>
'''
    other_bg = "tint" if bg == "" else ""
    body += (coverage_section(other_bg, exclude=slug, title="What else does Sideoats write?")
             + faq_block(f"{name}, answered", c["faq"], "" if other_bg == "tint" else "tint") + quote(need=s["need"]))
    schemas = [org_schema(), business_schema(), service_schema(name, c["desc"], f"{slug}.html"), faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Coverage", "coverage.html"), (name, f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "coverage", body))


def rows_plain(items):
    return '<ul class="outs">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


def build_deductible():
    values = [200000, 300000, 400000, 500000, 750000]
    grid = [(money(v),) + tuple(money(v * p // 100) for p in (1, 2, 3, 5)) for v in values]
    tdi_rows = [("Policy A", "$500", "$6,000", "$500"), ("Policy B", "5%, which is $7,500", "$0", "$6,500")]
    know = [("It is based on the house", "The percentage is applied to your dwelling coverage, the amount the house is insured for. The size of the damage does not change it."),
            ("It applies to each claim", "Two storms in one year means two deductibles."),
            ("It is often separate", "Many policies carry one deductible for wind and hail and a different one for everything else. Both are on the declarations page."),
            ("A roofer cannot cover it", "It is illegal to waive a homeowners deductible under Texas law. Your insurance company may ask for proof that you paid it.")]
    body = (calc_hero("How a wind and hail deductible works in Texas",
                      "A percentage deductible is a share of what your house is insured for. Move the numbers to see it in dollars, then read how it plays out on a claim.",
                      [("Home", "index.html"), ("Hail deductible", "")])
            + f'''<section class="sec tint" aria-labelledby="tdi-h"><div class="w two-col">
{prose("What is a percentage deductible?", ["A deductible is what you pay on a claim before the policy pays. The Texas Department of Insurance puts it this way: a deductible may be a specific dollar amount or a percentage, and if it is a percentage, make sure you know how that translates to a dollar amount.",
                                           "Most people know their premium to the dollar and have never seen their wind and hail deductible written as a number. On a Fort Worth roof, it is often the larger of the two.",
                                           "The department's own example is on this page. A $6,500 hail repair is mostly paid by one policy and not paid at all by the other."], "tdi-h")}
<div><h2>The state's example</h2>
{table(("On a $150,000 home", "Deductible", "Policy pays", "You pay"), tdi_rows, "A $6,500 hail repair under two deductibles, from the Texas Department of Insurance", "tbl last")}
<p class="fine">Policy B pays nothing because the repair costs less than the deductible.</p></div>
</div></section>
<section class="sec" aria-labelledby="grid-h"><div class="w">
<h2 id="grid-h">What does each percentage cost?</h2>
<p class="intro">Find the row closest to what your house is insured for.</p>
{table(("House insured for", "1%", "2%", "3%", "5%"), grid, "Wind and hail deductible in dollars, by insured value and percentage", "tbl nums")}
</div></section>
<section class="sec tint" aria-labelledby="know-h"><div class="w two-col">
<div><h2 id="know-h">What else should I know?</h2><p>Four things that surprise people the first time they file.</p>
<p><a href="after-a-hail-storm.html">What to do after a hail storm</a></p></div>
{rows(know)}
</div></section>
''' + faq_block("Hail deductibles, answered", DEDUCTIBLE_FAQ) + quote(need="home"))
    desc = "How a wind and hail deductible works in Texas, with a calculator that turns a percentage into dollars and a table for common house values."
    schemas = [org_schema(), business_schema(), faq_schema(DEDUCTIBLE_FAQ), crumbs_schema([("Home", ""), ("Hail deductible", "hail-deductible.html")]),
               article_schema("How a wind and hail deductible works in Texas", desc, "hail-deductible.html")]
    write("hail-deductible.html", page("hail-deductible.html", "Wind and Hail Deductibles in Texas, in Dollars | Sideoats", desc, schemas, "deductible", body))


def build_storm():
    ded = 7600
    math_rows = []
    for est in (6000, 18500, 32000):
        pays = max(0, est - ded)
        math_rows.append((money(est), money(min(est, ded)), money(pays), "No claim pays" if pays == 0 else "A claim pays"))
    body = (opener("What to do after a hail storm in Fort Worth",
                   "The first day decides how the claim goes. Take the photos, keep the receipts, and compare the estimate with your deductible before you file.",
                   [("Home", "index.html"), ("After a storm", "")], "Where hail becomes severe", "1 in",
                   "The National Weather Service calls a thunderstorm severe once its hail reaches one inch across, the size of a quarter.")
            + f'''<section class="sec" aria-labelledby="hail-h"><div class="w hail-g">
<div><h2 id="hail-h">How big was the hail?</h2>
<p>Size it against something you own, and take a photo of a stone beside it. Adjusters use the same comparisons.</p>
{hail_scale()}</div>
{figure("hail-lawn", "White hailstones of mixed sizes covering a green lawn after a storm, with torn leaves among them", "Photograph the hail before it melts, next to something that shows its size.")}
</div></section>
<section class="sec tint" aria-labelledby="steps-h"><div class="w two-col">
<div><h2 id="steps-h">What should I do first?</h2>{steps(STORM_STEPS)}
<p class="fine">These steps follow the Texas Department of Insurance guidance for hail damage to a home or a car.</p></div>
<div><h2>What should I ask a roofer?</h2>{checks(STORM_CONTRACTOR)}
<figure class="pic wide gap"><img src="img/shingles-chalk.webp" alt="{SHINGLES_ALT}" loading="lazy" width="1200" height="900"><figcaption>An adjuster circles each hail hit in chalk before counting them.</figcaption></figure></div>
</div></section>
<section class="sec" aria-labelledby="math-h"><div class="w two-col">
<div><h2 id="math-h">Should I file a claim?</h2>
<p>Compare the repair estimate with your deductible first. If the repair costs less than the deductible, the policy pays nothing.</p>
<p>The table uses a $7,600 deductible, which is 2% on a house insured for $380,000. <a href="hail-deductible.html">Work out your own</a>, or call us with the estimate and we will do it with you.</p></div>
<div>{table(("Repair estimate", "You pay", "Policy pays", "Result"), math_rows, "Three repair estimates against a $7,600 deductible", "tbl last")}
<p class="fine">An illustration with round numbers. It is not a quote.</p></div>
</div></section>
<section class="sec tint" aria-labelledby="time-h"><div class="w two-col">
<div><h2 id="time-h">How long does the insurance company have?</h2>
<p>Texas sets deadlines for the company once you file. The state can extend them by 15 days after a weather catastrophe.</p>
<p>For a car, hail is paid by comprehensive coverage. Liability alone does not pay for hail dents.</p></div>
<div>{table(("The company must", "Within", "Counted from"), STORM_DEADLINES, "Texas claim deadlines for an insurance company", "tbl")}</div>
</div></section>
<section class="sec dark" aria-labelledby="may-h"><div class="w two-col">
<div><h2 id="may-h">Why does Fort Worth take hail seriously?</h2></div>
<div class="prose"><p>On May 5, 1995, a storm hit the Mayfest festival beside the Trinity River at 7:10 in the evening. Hail up to the size of softballs fell on the crowd, and more than 400 people were injured.</p>
<p>The National Weather Service puts the damage from that day's storms at an estimated $2 billion in Tarrant and Dallas counties, and still counts it among the costliest hail storms on record.</p></div>
</div></section>
''' + faq_block("Hail claims, answered", STORM_FAQ) + quote(need="home"))
    desc = "What to do after a hail storm in Fort Worth: photos, receipts, what to ask a roofer, whether a claim clears your deductible, and Texas claim deadlines."
    schemas = [org_schema(), business_schema(), faq_schema(STORM_FAQ), crumbs_schema([("Home", ""), ("After a storm", "after-a-hail-storm.html")]),
               article_schema("What to do after a hail storm in Fort Worth", desc, "after-a-hail-storm.html")]
    write("after-a-hail-storm.html", page("after-a-hail-storm.html", "What to Do After a Hail Storm in Fort Worth | Sideoats", desc, schemas, "storm", body))


def build_switching():
    body = (opener("How switching to Sideoats works",
                   "Changing agencies takes one review, one form and no gap in coverage. Here is each step, and how your information is handled along the way.",
                   [("Home", "index.html"), ("Switching", "")], "Form to sign", "1",
                   "It names us as your agent. We line up the new policy's first day with the old policy's last day.")
            + f'''<section class="sec tint" aria-labelledby="steps-h"><div class="w two-col">
<div><h2 id="steps-h">What are the steps?</h2>{steps(SWITCH_STEPS)}</div>
<div><h2>How is my information handled?</h2><p>A quote needs details that should not sit in an inbox. This is how we keep them out of one.</p>{rows(SWITCH_INFO)}
<p class="more"><a href="privacy.html">Read the privacy page</a></p></div>
</div></section>
''' + coverage_section("", title="What can I move to Sideoats?") + faq_block("Switching agencies, answered", SWITCH_FAQ, "tint") + quote("Start with a review", "Send four details and an agent calls back the same business day. Have your declarations page nearby and we will read it with you."))
    schemas = [org_schema(), business_schema(), faq_schema(SWITCH_FAQ), crumbs_schema([("Home", ""), ("Switching", "switching.html")])]
    write("switching.html", page("switching.html", "Switching Insurance Agencies in Fort Worth | Sideoats",
                                 "How switching to Sideoats Insurance Agency works: a free policy review, one form to sign, no gap in coverage, and sensitive details taken by phone.",
                                 schemas, "switching", body))


def build_about():
    story = ["Rosalind Ibarra spent twelve years as a claims adjuster before she opened Sideoats in 2011. Most of the hard conversations in that job were with people who learned what their deductible was on the day they needed the policy.",
             "So the agency does that part first. The first meeting starts with the policy you already have, and every deductible on it gets written in dollars before anyone talks about price.",
             "Sideoats is independent and locally owned. The name comes from sideoats grama, the state grass of Texas."]
    body = (opener("An independent insurance agency in Fort Worth since 2011",
                   "Sideoats is three people in a brick building on Magnolia Avenue who read policies for a living.",
                   [("Home", "index.html"), ("About", "")], "The year Sideoats opened", "2011",
                   "Rosalind Ibarra started the agency after twelve years as a claims adjuster on Fort Worth roofs.")
            + f'''<section class="sec tint" aria-labelledby="story-h"><div class="w two-col">
{prose("Why does Sideoats exist?", story, "story-h")}
<div><h2>How do you work?</h2>{rows(ABOUT_ROWS)}</div>
</div></section>
<section class="sec" id="people" aria-labelledby="people-h"><div class="w people-g">
{figure("kitchen", KITCHEN_ALT, "Most of our reviews happen at a kitchen table, with the policy open.")}
<div><h2 id="people-h">Who reads your policy?</h2>{people_list()}<p class="fine">Fictional people, written for this demo.</p></div>
</div></section>
<section class="sec tint" aria-labelledby="where-h"><div class="w people-g">
<div><h2 id="where-h">Where is the office?</h2>
<p>We are on Magnolia Avenue in the Near Southside of Fort Worth, with parking at the curb. Walk in with your policy, or we will come to your kitchen table.</p>
{hours_table()}
<p class="fine">Licensed by the Texas Department of Insurance. You can check any Texas agent's license through the department's help line at <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a>.</p></div>
{figure("office", OFFICE_ALT)}
</div></section>
''' + areas_section("") + faq_block("About the agency, answered", ABOUT_FAQ, "tint") + quote())
    people = [{"@context": "https://schema.org", "@type": "Person", "name": n, "jobTitle": r, "worksFor": {"@id": f"{BASE}/#org"}} for n, r, _ in PEOPLE]
    schemas = [org_schema(), business_schema(), faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("About", "about.html")])] + people
    write("about.html", page("about.html", "About Sideoats Insurance Agency | Fort Worth, Texas",
                             "Sideoats Insurance Agency is an independent, locally owned agency in Fort Worth, opened in 2011 by a former claims adjuster who reads every renewal.",
                             schemas, "about", body))


def build_area(slug):
    a, c = AREA_BY[slug], AREA_PAGES[slug]
    label, number, caption = c["fig"]
    notes = table(("What we see here", "What we do about it"), c["notes"], f'Insurance notes for {a["name"]}')
    pic = figure(c["img"][0], c["img"][1]) if c.get("img") else ""
    body = (opener(c["h1"], c["lede"], [("Home", "index.html"), ("About", "about.html"), (a["name"], "")], label, number, caption)
            + f'''<section class="sec tint" aria-labelledby="loc-h"><div class="w two-col">
{prose(c["body_title"], c["body"], "loc-h")}
<div><h2>What do we plan for here?</h2>{notes}{pic}</div>
</div></section>
''' + coverage_section("", title=f'What do you write in {a["name"]}?') + areas_section("tint", exclude=slug, title="Where else do you write policies?")
            + faq_block(f'{a["name"]} insurance, answered', c["faq"]) + quote())
    schemas = [org_schema(), business_schema(), faq_schema(c["faq"]), crumbs_schema([("Home", ""), ("About", "about.html"), (a["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "about", body))


def build_privacy():
    body_html = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (f'''<section class="hero plain"><div class="w narrow">{crumbs([("Home", "index.html"), ("Privacy", "")])}
<h1>Your privacy at Sideoats</h1>
<p class="lede">What this website collects, how the sensitive details in a quote are taken, and what we will never ask you for.</p>
</div></section>
<section class="sec tint"><div class="w narrow"><div class="prose legal">{body_html}
<p class="fine">This is a demo site by Meraki is Love. Sideoats is a fictional agency, and nothing entered on this site is sent anywhere. Read more about <a href="switching.html">switching to Sideoats</a>, <a href="coverage.html">our coverage</a> or <a href="about.html">the agency</a>.</p>
</div></div></section>
''' + quote())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy | Sideoats Insurance Agency",
                               "How Sideoats Insurance Agency handles your information: what the website collects, how sensitive details are taken, and what we never ask for.",
                               schemas, "", body))


if __name__ == "__main__":
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    print("Building Sideoats demo:")
    build_home()
    build_coverage_hub()
    for cv in COVERAGES:
        build_coverage(cv["slug"])
    build_deductible()
    build_storm()
    build_switching()
    build_about()
    for ar in AREAS:
        build_area(ar["slug"])
    build_privacy()
    if PROBLEMS:
        print("\nProblems:")
        for p in PROBLEMS:
            print("  " + p)
        sys.exit(1)
