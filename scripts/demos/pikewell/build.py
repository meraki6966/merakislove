"""Build the Pikewell Real Estate demo into public/demos/pikewell/.

Run from the repo root:  python3 scripts/demos/pikewell/build.py
Pages are plain static HTML sharing assets/site.css and assets/site.js.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from pw import *  # noqa: E402,F403
from content import (REVIEWS, HOME_FAQ, BUY_STEPS, BUY_COSTS, BUY_FAQ, SELL_STEPS, SELL_INCLUDED, SELL_TIMELINE,  # noqa: E402
                     SELL_FAQ, VALUE_STEPS, VALUE_COMPARE, VALUE_FAQ, HOODS_FAQ, LISTINGS_FAQ, ABOUT_FAQ, AGENT_BIOS,
                     HOOD_PAGES, LISTING_PAGES, PRIVACY)

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "public", "demos", "pikewell")
# The home page is also served at the clean URL /demos/pikewell (no trailing
# slash), where relative paths would resolve against /demos/. So every local
# href and src is written root-absolute. PREFIX="" builds a relative copy.
PREFIX = os.environ.get("PREFIX", "/demos/pikewell/")
OUT = os.environ.get("OUT", OUT)
PROBLEMS = []


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


def write(name, html):
    # Guard the limits a scanner checks, so a long title never ships unnoticed.
    title = re.search(r"<title>(.*?)</title>", html).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1)
    if len(title) > 60 or "&" in title:
        PROBLEMS.append(f"{name}: title is {len(title)} chars or has an ampersand: {title}")
    if not 120 <= len(desc.replace("&#x27;", "'")) <= 160:
        PROBLEMS.append(f"{name}: description is {len(desc.replace('&#x27;', chr(39)))} chars")
    if html.count("<h1") != 1:
        PROBLEMS.append(f"{name}: {html.count('<h1')} h1 elements")
    if 'alt=""' in html:
        PROBLEMS.append(f"{name}: empty alt text")
    html = absolutize(html)
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    words = len(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S).split())
    print(f"  {name:42s} {len(html)//1024:>3} KB  {words:>5} words")


CHECK = ic("check")
CMP_TITLE = "Online estimate or a broker's report: <span class=\"accent\">which should I trust?</span>"
LIST = {x["slug"]: x for x in LISTINGS}
SAMPLE_NOTE = "Sample figures written for this demo. A live site refreshes them from MLS sales each month."


# ---------------------------------------------------------------- blocks
def head_block(eyebrow, title, small="", hid=""):
    h = f' id="{hid}"' if hid else ""
    sm = f'<p class="small">{small}</p>' if small else ""
    return f'<div class="section-head"><div><span class="eyebrow">{eyebrow}</span><h2 class="h-lg"{h}>{title}</h2></div>{sm}</div>'


def hood_cards(exclude=None):
    return "".join(
        f'<a class="hood-card reveal" href="{h["slug"]}.html"><img src="img/{h["img"]}.webp" alt="{h["alt"]}" loading="lazy" width="1600" height="904">'
        f'<span class="tag">{h["tag"]}</span><span class="cap"><b>{h["name"]}</b><span>{h["line"]}</span></span></a>'
        for h in HOODS if h["slug"] != exclude)


def hoods_section(bg="", exclude=None, eyebrow="Neighborhood guides", title='Six neighborhoods we know <span class="accent">block by block.</span>',
                  small="Each guide covers the homes, the parks, the streets and what to check before you buy there."):
    return f'''<section class="section {bg}" aria-labelledby="hoods-h"><div class="wrap">
{head_block(eyebrow, title, small, "hoods-h")}
<div class="hood-grid">{hood_cards(exclude)}</div></div></section>
'''


def listing_card(x):
    return (f'<a class="listing reveal" href="{x["slug"]}.html"><span class="ph"><img src="img/{x["img"]}.webp" alt="{x["alt"]}" loading="lazy" width="1500" height="1115">'
            f'<span class="status">{x["status"]}</span></span><span class="body"><span class="price">{x["price"]}</span><span class="where">{x["title"]}</span>'
            f'<ul class="facts"><li><b>{x["beds"]}</b> beds</li><li><b>{x["baths"]}</b> baths</li><li><b>{x["sqft"]}</b> sq ft</li><li>Built <b>{x["year"]}</b></li></ul>'
            f'<span><span class="sample">Sample listing</span></span></span></a>')


def listings_section(items=None, bg="snow", title='Homes we are <span class="accent">showing now.</span>', link=True):
    items = items or LISTINGS
    more = '<div class="btn-row"><a class="btn btn-line" href="listings.html">See all listings</a></div>' if link else ""
    return f'''<section class="section {bg}" aria-labelledby="list-h"><div class="wrap">
{head_block("Listings", title, "Sample listings written for this demo. A live site shows current MLS listings.", "list-h")}
<div class="list-grid">{"".join(listing_card(x) for x in items)}</div>{more}</div></section>
'''


def market_table(caption="Six Denver neighborhoods at a glance"):
    rows = "".join(f'<tr><th scope="row"><a href="{h["slug"]}.html">{h["name"]}</a></th><td>{h["zip"]}</td><td>{h["homes"]}</td><td class="num">{h["range"]}</td><td>{h["downtown"]}</td></tr>' for h in HOODS)
    return (f'<div class="table-wrap reveal"><table class="data"><caption>{caption}</caption><thead><tr><th scope="col">Neighborhood</th><th scope="col">ZIP</th>'
            f'<th scope="col">Typical homes</th><th scope="col">Sample price range</th><th scope="col">Drive to downtown</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="fine">{SAMPLE_NOTE}</p>')


def table(caption, cols, rows, note=""):
    head_html = "".join(f'<th scope="col">{c}</th>' for c in cols)
    body = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return (f'<div class="table-wrap reveal"><table class="data"><caption>{caption}</caption><thead><tr>{head_html}</tr></thead><tbody>{body}</tbody></table></div>'
            + (f'<p class="fine">{note}</p>' if note else ""))


def steps_section(eyebrow, title, small, steps, bg="", hid="steps-h"):
    lis = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in steps)
    return f'''<section class="section {bg}" aria-labelledby="{hid}"><div class="wrap">
{head_block(eyebrow, title, small, hid)}
<ol class="steps">{lis}</ol></div></section>
'''


def reviews_band(items, title='What clients <span class="accent">say.</span>', bg="snow"):
    return f'''<section class="section {bg}" aria-labelledby="rev-h"><div class="wrap">
{head_block("Client stories", title, "Sample reviews written for this demo. A live site would pull them from Google.", "rev-h")}
<div class="reviews">{"".join(review_card(*r) for r in items)}</div></div></section>
'''


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items) + "</ul>"


def rules_2024(bg=""):
    return f'''<section class="section {bg}" aria-labelledby="rules-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Good to know</span><h2 class="h-lg" id="rules-h">What changed for buyers and sellers in <span class="accent">August 2024?</span></h2>
<p style="margin-top:18px">On August 17, 2024, new practices took effect across the country after a settlement involving the National Association of Realtors. Three things changed, and they shape how every purchase and sale works now.</p>
<div class="btn-row"><a class="btn btn-line" href="buy.html">How buying works</a><a class="btn btn-line" href="sell.html">How selling works</a></div></div>
<div class="reveal" style="display:grid;gap:16px">
<div class="callout"><h3>A written agreement comes before the first tour</h3><p>A buyer working with an agent signs a buyer agreement before touring a home with that agent.</p></div>
<div class="callout blue"><h3>The agent's fee is stated and negotiable</h3><p>The agreement names a specific amount or rate. It cannot be open ended, and the agent cannot collect more than it says.</p></div>
<div class="callout"><h3>Buyer agent pay is off the MLS</h3><p>Sellers can still offer to pay a buyer's agent, or offer a credit toward closing costs. That offer is now made outside the MLS.</p></div>
</div></div></section>
'''


def agent_card(key, h="h3"):
    a, b = AGENTS[key], AGENT_BIOS[key]
    return (f'<article class="agent reveal" id="{key}"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1000" height="1345">'
            f'<div class="body"><{h}>{a["name"]}</{h}><p class="role">{a["role"]}</p>{"".join(f"<p>{p}</p>" for p in b["bio"])}'
            f'<p class="lic">{b["lic"]}<br>Works most in: {b["focus"]}</p></div></article>')


# ---------------------------------------------------------------- pages
def build_home():
    hero = f'''<section class="hero hero-home">
<img class="hero-img" src="img/hero.webp" alt="A row of red brick homes with front porches on a Denver street at golden hour, with the Front Range in the distance" fetchpriority="high" width="2000" height="1129">
<div class="wrap">
<span class="eyebrow">Denver real estate brokerage</span>
<h1 class="h-xl">Denver homes, neighborhood by <span class="accent">neighborhood.</span></h1>
<p class="lede">Pikewell is a three broker firm that buys and sells homes in Washington Park, Highland, Sloan's Lake, Park Hill, Central Park and Berkeley. One broker stays with you from the first call to the closing table.</p>
<div class="btn-row"><a class="btn btn-gold" href="listings.html">See listings</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}{PHONE}</a></div>
</div></section>
<div class="intent"><div class="wrap"><div class="intent-grid">
<a class="intent-card" href="buy.html"><span class="num">01</span><h2>I want to buy</h2><p>Tours with notes on the roof, the sewer line and the recent sales, and a fee in writing before the first showing.</p><span class="more">How buying works{ic("arrow")}</span></a>
<a class="intent-card" href="sell.html"><span class="num">02</span><h2>I want to sell</h2><p>A price backed by named sales, a room by room prep list, and one broker through closing.</p><span class="more">How selling works{ic("arrow")}</span></a>
<a class="intent-card" href="home-value.html"><span class="num">03</span><h2>What is my home worth</h2><p>A written range from a broker who has walked the house, in two business days.</p><span class="more">Get a home value report{ic("arrow")}</span></a>
</div></div></div>
'''
    intro = f'''<section class="section" aria-labelledby="intro-h"><div class="wrap two-col">
<div class="reveal"><span class="eyebrow">Why Pikewell</span><h2 class="h-lg" id="intro-h">A small brokerage that knows <span class="accent">its streets.</span></h2>
<p style="margin-top:18px">Denver changes from one block to the next. A 1912 Denver Square two blocks from Washington Park and a 2019 townhome by Sloan's Lake are different purchases, with different inspections, different taxes and different resale stories.</p>
<p>So we keep our map small. Ilsa Brandvold opened Pikewell in {YEAR_FOUNDED} to work a handful of neighborhoods closely, and that is still how the firm runs. When you ask what a house on Tennyson Street should sell for, the broker answering has probably been inside the three most recent sales on that block.</p>
{checks(["A written fee before the first showing, with nothing open ended", "Showing notes after every tour: sales nearby, roof age, sewer line, our offer price", "A call or text back within one business hour", "The same broker from the first conversation to the closing table"])}
</div>
<div class="reveal"><div class="facts-strip" style="grid-template-columns:1fr 1fr">
<div style="border-bottom:1px solid var(--line)"><b>{YEAR_FOUNDED}</b><span>Founded in Denver</span></div>
<div style="border-bottom:1px solid var(--line);border-right:0"><b>6</b><span>Neighborhoods with full guides</span></div>
<div><b>3</b><span>Licensed Colorado brokers</span></div>
<div><b>1 hour</b><span>Reply time during office hours</span></div>
</div>
<div class="callout" style="margin-top:22px"><h3>Moving to Denver from out of state?</h3><p>We tour by video, measure the garage and send a plain report on each home, so nothing surprises you on move-in day. <a href="about.html">Meet the team</a>.</p></div>
</div></div></section>
'''
    market = f'''<section class="section" aria-labelledby="market-h"><div class="wrap">
{head_block("Market snapshot", 'How do the six neighborhoods <span class="accent">compare?</span>', "Home styles, sample price ranges and the drive downtown, side by side. Each name links to its full guide.", "market-h")}
{market_table()}</div></section>
'''
    a, b = AGENTS["ilsa"], AGENT_BIOS["ilsa"]
    team = f'''<section class="section" aria-labelledby="team-h"><div class="wrap two-col">
<div class="reveal"><img src="img/{a["img"]}.webp" alt="{a["alt"]}" loading="lazy" width="1000" height="1345" style="max-width:440px;width:100%;aspect-ratio:4/5;object-fit:cover;object-position:top;border-bottom:6px solid var(--gold)"></div>
<div class="reveal"><span class="eyebrow">Who you work with</span><h2 class="h-lg" id="team-h">Three brokers, <span class="accent">one phone number.</span></h2>
<p style="margin-top:18px">{b["bio"][0]}</p>
<p>Tobias Hallgren works with buyers and spent eight years as a home inspector first. Nia Abernethy prepares and lists homes and came from staging. Between the three of them, every part of a sale has someone who has done it by hand.</p>
<div class="btn-row"><a class="btn btn-blue" href="about.html">Meet the team</a><a class="btn btn-line" href="?intent=buy#contact">Ask a question</a></div></div>
</div></section>
'''
    body = (hero + intro + hoods_section("snow") + market + listings_section()
            + steps_section("Buying with Pikewell", 'Four steps from first call to <span class="accent">front door keys.</span>',
                            "Most buyers tour for four to eight weeks and close 30 to 45 days after an accepted offer.", BUY_STEPS, "dark")
            + rules_2024() + team + reviews_band(REVIEWS[:3])
            + faq_block("Before you call.", HOME_FAQ, "Short answers to what buyers and sellers ask us first.") + contact())
    schemas = [org_schema(), business_schema(), website_schema(), faq_schema(HOME_FAQ)]
    write("index.html", page("index.html", "Pikewell Real Estate | Denver Homes and Neighborhoods",
                             "Pikewell is a Denver real estate brokerage for Washington Park, Highland, Sloan's Lake, Park Hill, Central Park and Berkeley. Buy, sell or get a home value.",
                             schemas, "home", body))


def build_buy():
    agreement = f'''<section class="section snow" aria-labelledby="agree-h"><div class="wrap two-col top">
<div class="prose reveal"><span class="eyebrow">The buyer agreement</span><h2 class="h-lg" id="agree-h">What will I sign before <span class="accent">the first tour?</span></h2>
<p style="margin-top:18px">Since August 17, 2024, a buyer working with an agent signs a written agreement before touring a home with that agent. Colorado buyers were used to this already, because the state has long had an approved form for it.</p>
<p>Ours runs on that Colorado form, with a one page summary on top in plain words. We read it with you before you sign, and you can take it home first.</p>
<div class="callout blue" style="margin-top:22px"><h3>You can ask for a short term</h3><p>If you are not ready to commit for months, ask for an agreement that covers one weekend of tours or one address. We write those often.</p></div></div>
<div class="reveal"><h3 class="h-md" style="margin-bottom:18px">What the agreement spells out</h3>
{checks(["What we do for you: tours, pricing research, the offer, inspections, deadlines", "Our fee, as a specific amount or rate, and a line saying it is negotiable", "That we cannot be paid more than the agreement says, from any source", "How long the agreement lasts and which areas it covers", "How either of us can end it"])}
<p class="fine" style="margin-top:20px">This page explains how we work. It is general information and does not replace legal advice about your own contract.</p></div>
</div></section>
'''
    costs = f'''<section class="section" aria-labelledby="cost-h"><div class="wrap">
{head_block("Costs to plan for", 'What does it cost to buy a home <span class="accent">in Denver?</span>', "Beyond the down payment, plan for these. We give you a written estimate for the specific house before you offer.", "cost-h")}
{table("Typical buyer costs on a Denver purchase", ["Cost", "When it is due", "Typical amount"], BUY_COSTS, "Typical ranges for planning. Your lender's loan estimate gives the exact closing costs for your loan.")}
</div></section>
'''
    inspect = f'''<section class="section dark" aria-labelledby="insp-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Before you close</span><h2 class="h-lg" id="insp-h">What we check on every <span class="accent">Denver house.</span></h2>
<p style="margin-top:18px">Tobias spent eight years as a home inspector before he joined Pikewell. These four checks come from what he found most often in older Denver homes.</p></div>
<div class="reveal">{checks(["Sewer line: a camera scope, because many pre-1970s homes still have clay pipe", "Radon: a two day test, since much of Colorado has elevated levels", "Roof: age, layers and hail history, which decide whether an insurer will write the policy", "Permits: whether the basement finish, the addition or the new furnace was ever signed off"])}</div>
</div></section>
'''
    body = (page_hero("Buying a home", 'Buy a home in Denver with a broker who <span class="accent">reads the house.</span>',
                      "Tours with written notes, a fee in plain numbers before the first showing, and every deadline tracked from offer to closing.",
                      [("Home", "index.html"), ("Buy", "")], img="home-bungalow", alt=LIST["berkeley-brick-bungalow"]["alt"],
                      points=["Buyer agreement explained line by line", "Sewer scope and radon test on every older home"],
                      buttons=f'<a class="btn btn-gold" href="?intent=buy#contact">Start a search</a><a class="btn btn-ghost" href="listings.html">See listings</a>')
            + steps_section("How it works", 'Four steps from first call to <span class="accent">front door keys.</span>',
                            "Most buyers tour for four to eight weeks and close 30 to 45 days after an accepted offer.", BUY_STEPS)
            + agreement + costs + inspect
            + hoods_section("", title='Where do you want <span class="accent">to live?</span>', small="Start with a guide. Each one covers the homes, the parks, the streets and what to check before you buy there.")
            + listings_section() + reviews_band([REVIEWS[0], REVIEWS[3], REVIEWS[4]], bg="")
            + faq_block('Buying in Denver, <span class="accent">answered.</span>', BUY_FAQ, "What buyers ask us before the first tour.", "snow")
            + contact(title='Tell us what you are <span class="accent">looking for.</span>', intent="buy"))
    schemas = [org_schema(), business_schema(), faq_schema(BUY_FAQ), crumbs_schema([("Home", ""), ("Buy", "buy.html")])]
    write("buy.html", page("buy.html", "Buying a Home in Denver | Pikewell Real Estate",
                           "How buying a home in Denver works with Pikewell: the written buyer agreement, tours with notes, typical costs, inspections and the path to closing.",
                           schemas, "buy", body))


def build_sell():
    included = f'''<section class="section snow" aria-labelledby="inc-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">What you get</span><h2 class="h-lg" id="inc-h">What is included when you list <span class="accent">with Pikewell?</span></h2>
<p style="margin-top:18px">Everything below is covered by the listing fee, which is written into the listing agreement before you sign. You pay nothing up front.</p>
<div class="callout" style="margin-top:22px"><h3>Not ready to list?</h3><p>Ask for a home value report first. It is free, it is written, and about half the people who request one are a year or more from selling. <a href="home-value.html">Get a home value report</a>.</p></div></div>
<div class="reveal">{checks(SELL_INCLUDED)}</div>
</div></section>
'''
    timeline = f'''<section class="section" aria-labelledby="time-h"><div class="wrap">
{head_block("Timeline", 'How long does it take to <span class="accent">sell a home?</span>', "A typical schedule from the first walk-through to closing day. Yours may be shorter if the house is ready.", "time-h")}
{table("A typical Pikewell listing, week by week", ["When", "What happens", "Who does it"], SELL_TIMELINE)}
</div></section>
'''
    comp = f'''<section class="section dark" aria-labelledby="comp-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Since August 2024</span><h2 class="h-lg" id="comp-h">Do sellers still pay the <span class="accent">buyer's agent?</span></h2>
<p style="margin-top:18px">It is now a choice you make, with your broker's advice. Offers of pay to a buyer's agent no longer appear on the MLS, and a buyer's own agreement sets what their agent is owed.</p>
<p>Many buyers still ask the seller to cover that fee as a term of their offer. We show you how recent sales near you handled it, so you can decide before the first offer arrives.</p></div>
<div class="reveal">{checks(["Offer buyer agent pay up front, outside the MLS, to widen the pool of buyers", "Offer a credit toward the buyer's closing costs instead", "Offer nothing in advance and weigh each offer's request against its price", "Whichever you choose, compare offers by what you keep after every cost"])}</div>
</div></section>
'''
    body = (page_hero("Selling a home", 'Sell your Denver home for a price you can <span class="accent">trace to recorded sales.</span>',
                      "A written price range with the sales behind it, a room by room prep list, and one broker from the walk-through to the closing table.",
                      [("Home", "index.html"), ("Sell", "")], img="home-square", alt=LIST["washington-park-denver-square"]["alt"],
                      points=["Photos, floor plan and staging consult included", "A weekly report on showings and feedback"],
                      buttons=f'<a class="btn btn-gold" href="home-value.html">Get a home value report</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}{PHONE}</a>')
            + steps_section("How it works", 'Four steps from walk-through to <span class="accent">closing day.</span>',
                            "Most listings go live about three weeks after the first visit.", SELL_STEPS)
            + included + timeline + comp + reviews_band([REVIEWS[1], REVIEWS[5], REVIEWS[2]], bg="")
            + faq_block('Selling in Denver, <span class="accent">answered.</span>', SELL_FAQ, "What sellers ask us at the first walk-through.", "snow")
            + contact(title='Tell us about <span class="accent">your home.</span>', intent="sell", address=True))
    schemas = [org_schema(), business_schema(), faq_schema(SELL_FAQ), crumbs_schema([("Home", ""), ("Sell", "sell.html")])]
    write("sell.html", page("sell.html", "Selling a Home in Denver | Pikewell Real Estate",
                            "How selling a home in Denver works with Pikewell: pricing from named sales, a prep list, photos and staging, the timeline and buyer agent pay since 2024.",
                            schemas, "sell", body))


def build_value():
    compare = f'''<section class="section snow" aria-labelledby="cmp-h"><div class="wrap">
{head_block("Two kinds of estimate", CMP_TITLE, "Use the online number to get curious. Use the report to make a plan.", "cmp-h")}
{table("How an online estimate compares with a Pikewell home value report", ["", "Online estimate", "Pikewell report"], VALUE_COMPARE)}
</div></section>
'''
    inside = f'''<section class="section" aria-labelledby="in-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">Inside the report</span><h2 class="h-lg" id="in-h">Four pages, <span class="accent">no sales pitch.</span></h2>
<p style="margin-top:18px">The report is written for planning. Refinancing, settling an estate, deciding whether to remodel or move: all of them start with a number you can defend.</p>
<div class="btn-row"><a class="btn btn-blue" href="#contact">Request my report</a><a class="btn btn-line" href="sell.html">How selling works</a></div></div>
<div class="reveal">{checks(["A low, a likely and a high price, and what separates them", "Six to ten closed sales nearby, each with its address, date and price", "Adjustments for size, condition, lot and updates, shown line by line", "What to fix, what to leave alone and what each choice is worth", "An estimate of what you would keep after costs at each price"])}</div>
</div></section>
'''
    body = (page_hero("Home value report", 'What is my Denver home <span class="accent">worth?</span>',
                      "A written price range from a broker who has walked the house, with the sales behind it. Free, in two business days, with no obligation to list.",
                      [("Home", "index.html"), ("Home Value", "")], img="home-townhome", alt=LIST["sloans-lake-townhome"]["alt"],
                      points=["Based on closed sales near your home", "Your details go to one broker and nowhere else"],
                      buttons='<a class="btn btn-gold" href="#contact">Request my report</a>')
            + steps_section("How it works", 'From address to written range in <span class="accent">two business days.</span>',
                            "A visit takes about 30 minutes. A video call works too.", VALUE_STEPS)
            + compare + inside + market_section_small() + reviews_band([REVIEWS[2], REVIEWS[1], REVIEWS[5]], bg="snow")
            + faq_block('Home values, <span class="accent">answered.</span>', VALUE_FAQ, "What owners ask before they request a report.")
            + contact(title='Request your <span class="accent">home value report.</span>',
                      lead="Send the address and how to reach you. A broker replies within one business hour to set a time.",
                      intent="value", address=True, button="Request my report"))
    schemas = [org_schema(), business_schema(), faq_schema(VALUE_FAQ), crumbs_schema([("Home", ""), ("Home Value", "home-value.html")])]
    write("home-value.html", page("home-value.html", "What Is My Denver Home Worth? | Pikewell Real Estate",
                                  "Request a free home value report from Pikewell. A Denver broker walks the home, pulls recent nearby sales and sends a written price range in two days.",
                                  schemas, "", body))


def market_section_small():
    return f'''<section class="section" aria-labelledby="market-h" style="padding-top:0"><div class="wrap">
{head_block("Market snapshot", 'What are homes selling for <span class="accent">near me?</span>', "Sample ranges for the six neighborhoods we work in most.", "market-h")}
{market_table()}</div></section>
'''


def build_hoods_hub():
    how = f'''<section class="section" aria-labelledby="how-h"><div class="wrap two-col top">
<div class="reveal"><span class="eyebrow">How we write these</span><h2 class="h-lg" id="how-h">Guides about places, <span class="accent">written by brokers.</span></h2>
<p style="margin-top:18px">Every guide is written by a Pikewell broker who works in that neighborhood, and each covers the same four things: the homes, the parks, the streets and how you get around.</p>
<p>You will not find opinions about who lives where, which schools are best or how safe a block feels. Fair housing law asks brokers to leave those judgments to you, and we agree with it. We point you to the public sources and let you decide.</p></div>
<div class="reveal" style="display:grid;gap:16px">
<div class="callout blue"><h3>For schools</h3><p>Denver Public Schools publishes a school finder with boundaries and enrollment details for every address.</p></div>
<div class="callout"><h3>For crime data</h3><p>The Denver Police Department publishes maps you can search by address and date.</p></div>
<div class="callout blue"><h3>For zoning and permits</h3><p>The City and County of Denver has a public map showing what can be built on any lot, and a permit history for each address.</p></div>
</div></div></section>
'''
    table_sec = f'''<section class="section snow" aria-labelledby="market-h"><div class="wrap">
{head_block("Side by side", 'How do the neighborhoods <span class="accent">compare?</span>', "Home styles, sample price ranges and the drive downtown.", "market-h")}
{market_table()}</div></section>
'''
    body = (page_hero("Neighborhood guides", 'Denver neighborhoods, one guide <span class="accent">at a time.</span>',
                      "Six guides written by the brokers who work there: the homes, the parks, the streets and what to check before you buy.",
                      [("Home", "index.html"), ("Neighborhoods", "")], img="hood-park-hill", alt=HOOD["park-hill"]["alt"],
                      points=["Washington Park, Highland, Sloan's Lake", "Park Hill, Central Park, Berkeley"])
            + hoods_section("", title='Pick a <span class="accent">neighborhood.</span>') + table_sec + how + listings_section(bg="snow")
            + faq_block('Choosing a neighborhood, <span class="accent">answered.</span>', HOODS_FAQ, "What people ask when they are comparing parts of Denver.")
            + contact(intent="buy"))
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Denver neighborhood guides",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": h["name"], "url": f"{BASE}/{h['slug']}.html"} for i, h in enumerate(HOODS)]}
    schemas = [org_schema(), items, faq_schema(HOODS_FAQ), crumbs_schema([("Home", ""), ("Neighborhoods", "neighborhoods.html")])]
    write("neighborhoods.html", page("neighborhoods.html", "Denver Neighborhood Guides | Pikewell Real Estate",
                                     "Broker written guides to six Denver neighborhoods: Washington Park, Highland, Sloan's Lake, Park Hill, Central Park and Berkeley. Homes, parks and streets.",
                                     schemas, "hoods", body))


def build_hood(slug):
    h, c = HOOD[slug], HOOD_PAGES[slug]
    facts = f'''<section class="section" style="padding-bottom:0" aria-label="{h["name"]} at a glance"><div class="wrap"><div class="facts-strip reveal">
<div><b>{h["zip"]}</b><span>ZIP code</span></div><div><b>{h["range"]}</b><span>Sample price range</span></div>
<div><b style="font-size:19px;line-height:1.3">{h["homes"]}</b><span>Typical homes</span></div><div><b style="font-size:19px;line-height:1.3">{h["downtown"]}</b><span>Drive to downtown</span></div>
</div><p class="fine">{SAMPLE_NOTE}</p></div></section>
'''
    about = f'''<section class="section" aria-labelledby="about-h"><div class="wrap two-col top">
<div class="prose reveal"><span class="eyebrow">The neighborhood</span><h2 class="h-lg" id="about-h">What is {h["name"]} <span class="accent">like?</span></h2>
<div style="margin-top:18px">{"".join(f"<p>{p}</p>" for p in c["about"])}</div></div>
<div class="reveal"><div class="callout blue"><h3>Getting around</h3><p>{c["around"]}</p></div>
<div class="callout" style="margin-top:16px"><h3>Thinking about {h["short"]}?</h3><p>Tell us your budget and timing and a broker who works here will send you what has sold lately. <a href="?intent=buy&amp;area={slug}#contact">Ask about {h["short"]}</a>.</p></div></div>
</div></section>
'''
    know = "".join(f'<li class="reveal"><h3>{t}</h3><p>{d}</p></li>' for t, d in c["know"])
    know_sec = f'''<section class="section dark" aria-labelledby="know-h"><div class="wrap">
{head_block("Before you buy here", f'What should I check before buying in <span class="accent">{h["short"]}?</span>', "Four things our brokers look at first in this neighborhood.", "know-h")}
<ol class="steps">{know}</ol></div></section>
'''
    here = [x for x in LISTINGS if x["hood"] == slug]
    lst = listings_section(here, bg="snow", title=f'For sale in <span class="accent">{h["short"]}.</span>') if here else ""
    body = (page_hero(f'{h["name"]}, Denver {h["zip"]}', c["h1"], c["lede"], [("Home", "index.html"), ("Neighborhoods", "neighborhoods.html"), (h["name"], "")],
                      img=h["img"], alt=h["alt"],
                      buttons=f'<a class="btn btn-gold" href="?intent=buy&amp;area={slug}#contact">Ask about {h["short"]}</a><a class="btn btn-ghost" href="home-value.html">I own a home here</a>')
            + facts + about + know_sec + lst
            + hoods_section("" if here else "snow", exclude=slug, eyebrow="Keep exploring", title='Five more <span class="accent">neighborhoods.</span>', small="Compare this one with the others we work in.")
            + faq_block(f'{h["name"]}, <span class="accent">answered.</span>', c["faq"], "Questions people ask about this part of Denver.", "snow" if here else "")
            + contact(title=f'Ask a broker about <span class="accent">{h["short"]}.</span>', intent="buy", area=slug))
    place = {"@context": "https://schema.org", "@type": "Place", "name": f"{h['name']}, Denver", "description": strip(c["lede"]),
             "address": {"@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": h["zip"], "addressCountry": "US"},
             "containedInPlace": {"@type": "City", "name": "Denver"}, "image": f"{BASE}/img/{h['img']}.webp"}
    schemas = [org_schema(), business_schema(), place, faq_schema(c["faq"]),
               crumbs_schema([("Home", ""), ("Neighborhoods", "neighborhoods.html"), (h["name"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["title"], c["desc"], schemas, "hoods", body))


def build_listings():
    body = (page_hero("Listings", 'Denver homes for sale, shown by the brokers who <span class="accent">know them.</span>',
                      "Three sample listings show how a Pikewell listing page works: plain facts, recent repairs spelled out and one broker to call.",
                      [("Home", "index.html"), ("Listings", "")],
                      buttons='<a class="btn btn-gold" href="?intent=buy#contact">Schedule a showing</a><a class="btn btn-ghost" href="buy.html">How buying works</a>')
            + listings_section(bg="", title='Three homes, three <span class="accent">neighborhoods.</span>', link=False)
            + f'''<section class="section snow" aria-labelledby="lt-h"><div class="wrap">
{head_block("Compare", 'How do these homes <span class="accent">compare?</span>', "Price, size and age in one table.", "lt-h")}
{table("Sample listings side by side", ["Home", "Neighborhood", "Price", "Beds and baths", "Size", "Built"],
       [(f'<a href="{x["slug"]}.html">{x["title"]}</a>', f'<a href="{x["hood"]}.html">{HOOD[x["hood"]]["name"]}</a>', x["price"], f'{x["beds"]} beds, {x["baths"]} baths', f'{x["sqft"]} sq ft', str(x["year"])) for x in LISTINGS],
       "Sample listings written for this demo.")}
</div></section>
''' + hoods_section("", title='Browse by <span class="accent">neighborhood.</span>')
            + faq_block('Listings and showings, <span class="accent">answered.</span>', LISTINGS_FAQ, "How showings work, and what is real on this demo.", "snow")
            + contact(title='Schedule a <span class="accent">showing.</span>', intent="buy"))
    items = {"@context": "https://schema.org", "@type": "ItemList", "name": "Pikewell sample listings",
             "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x["title"], "url": f"{BASE}/{x['slug']}.html"} for i, x in enumerate(LISTINGS)]}
    schemas = [org_schema(), business_schema(), items, faq_schema(LISTINGS_FAQ), crumbs_schema([("Home", ""), ("Listings", "listings.html")])]
    write("listings.html", page("listings.html", "Denver Homes for Sale | Pikewell Real Estate",
                                "Sample Denver listings from Pikewell Real Estate in Washington Park, Berkeley and Sloan's Lake, with prices, sizes, recent repairs and a broker to call.",
                                schemas, "listings", body))


def build_listing(slug):
    x, c = LIST[slug], LISTING_PAGES[slug]
    h, a = HOOD[x["hood"]], AGENTS[x["agent"]]
    first = a["name"].split()[0]
    hero = f'''<section class="hero hero-page"><div class="wrap"><div class="grid"><div class="copy">
{crumbs([("Home", "index.html"), ("Listings", "listings.html"), (x["where"].split(",")[0], "")])}
<span class="eyebrow">{x["status"]}</span>
<h1 class="h-xl" style="font-size:clamp(32px,3.8vw,46px)">{x["title"]}</h1>
<p class="price-xl" style="margin:22px 0 6px">{x["price"]}</p>
<p class="lede" style="margin-top:0">{x["where"]} <span class="sample" style="margin-left:8px">Sample listing</span></p>
<div class="btn-row"><a class="btn btn-gold" href="?intent=buy&amp;area={x["hood"]}#contact">Schedule a showing</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}{PHONE}</a></div>
</div><div class="frame"><img src="img/{x["img"]}.webp" alt="{x["alt"]}" fetchpriority="high" width="1500" height="1115"></div></div></div></section>
<div class="after-hero"></div>
'''
    detail = f'''<section class="section" style="padding-top:24px" aria-labelledby="home-h"><div class="wrap two-col top">
<div class="prose reveal"><div class="spec"><div><b>{x["beds"]}</b><span>Bedrooms</span></div><div><b>{x["baths"]}</b><span>Bathrooms</span></div><div><b>{x["sqft"]}</b><span>Square feet</span></div><div><b>{x["year"]}</b><span>Year built</span></div></div>
<h2 class="h-lg" id="home-h">About this <span class="accent">home.</span></h2>
<div style="margin-top:18px">{"".join(f"<p>{p}</p>" for p in c["body"])}</div>
<p class="fine">{x["lot"]}. Sample listing written for this demo, so the street address is left out. Photos were made for the demo.</p></div>
<div class="reveal"><h3 class="h-md" style="margin-bottom:18px">What stands out</h3>{checks(c["features"])}
<div class="callout blue" style="margin-top:26px"><h3>Shown by {a["name"]}</h3><p>{a["role"]} at Pikewell. Call or text {PHONE} and ask for {first}, or <a href="about.html#{x["agent"]}">read about {first}</a>.</p></div>
<div class="callout" style="margin-top:16px"><h3>About {h["name"]}</h3><p>{h["line"]}. <a href="{h["slug"]}.html">Read the {h["short"]} guide</a>.</p></div></div>
</div></section>
'''
    others = [o for o in LISTINGS if o["slug"] != slug]
    qa = [("How do I see this home?", f"Call or text {PHONE}, or use the form on this page. If we have not worked together before, we sign a buyer agreement before a private tour."),
          ("Is this listing live?", "No. It is a sample written for this demo site. A live Pikewell listing page shows the full address, a map, a floor plan and the MLS number."),
          (f"What should I check before buying in {h['short']}?", f"{HOOD_PAGES[x['hood']]['know'][0][1]} {HOOD_PAGES[x['hood']]['know'][1][1]}")]
    body = (hero + detail + listings_section(others, bg="snow", title='More homes we are <span class="accent">showing.</span>')
            + faq_block('This home, <span class="accent">answered.</span>', qa, "Showings, and what is real on this demo.")
            + contact(title='Schedule a <span class="accent">showing.</span>', lead=f"Tell us when you are free and {first} will confirm a time by text within one business hour.", intent="buy", area=x["hood"]))
    listing = {"@context": "https://schema.org", "@type": "RealEstateListing", "name": x["title"], "url": f"{BASE}/{slug}.html",
               "description": c["desc"], "image": f"{BASE}/img/{x['img']}.webp", "datePosted": "2026-09-28",
               "provider": {"@id": f"{BASE}/#business"},
               "mainEntity": {"@type": "SingleFamilyResidence", "name": x["title"], "numberOfBedrooms": x["beds"], "numberOfBathroomsTotal": x["baths"],
                              "yearBuilt": x["year"], "floorSize": {"@type": "QuantitativeValue", "value": x["sqft_num"], "unitCode": "FTK"},
                              "address": {"@type": "PostalAddress", "addressLocality": "Denver", "addressRegion": "CO", "postalCode": h["zip"], "addressCountry": "US"}}}
    schemas = [org_schema(), business_schema(), listing, faq_schema(qa),
               crumbs_schema([("Home", ""), ("Listings", "listings.html"), (x["title"], f"{slug}.html")])]
    write(f"{slug}.html", page(f"{slug}.html", c["seo_title"], c["desc"], schemas, "listings", body))


def build_about():
    story = f'''<section class="section" aria-labelledby="story-h"><div class="wrap two-col top">
<div class="prose reveal"><span class="eyebrow">Our story</span><h2 class="h-lg" id="story-h">Why is Pikewell <span class="accent">this small?</span></h2>
<p style="margin-top:18px">Ilsa Brandvold spent eight years at a large Denver brokerage before she opened Pikewell in {YEAR_FOUNDED}. She liked the work and disliked the handoffs: one person at the listing appointment, another on the phone, a third at closing.</p>
<p>Pikewell was built to remove the handoffs. Three brokers and one transaction coordinator share a single office line and a single calendar. Whoever you meet first stays with you to the end, and the other two know your file well enough to cover a showing.</p>
<p>The name comes from Pikes Peak, the mountain you can see to the south from the high streets of Highland on a clear day.</p></div>
<div class="reveal"><h3 class="h-md" style="margin-bottom:18px">How we work</h3>
{checks(["Fees in writing before any work starts", "Advice that includes waiting, when waiting is the better move", "Every price backed by sales you can look up", "A reply within one business hour", "Neighborhood guides that follow fair housing rules"])}
<div class="callout" style="margin-top:26px"><h3>Licensed in Colorado</h3><p>Every Pikewell broker holds an active license from the Colorado Division of Real Estate. We are an Equal Housing Opportunity brokerage.</p></div></div>
</div></section>
'''
    team = f'''<section class="section snow" aria-labelledby="team-h"><div class="wrap">
{head_block("The team", 'Three brokers you can <span class="accent">call directly.</span>', "One office line reaches all three. Ask for whoever fits your question.", "team-h")}
<div class="team">{"".join(agent_card(k) for k in AGENTS)}</div></div></section>
'''
    who = f'''<section class="section" aria-labelledby="who-h"><div class="wrap">
{head_block("Who to ask for", 'Which broker should <span class="accent">I call?</span>', "A quick way to find the right person.", "who-h")}
{table("Who does what at Pikewell", ["Broker", "Role", "Works most in", "Ask about"],
       [(f'<a href="#{k}">{AGENTS[k]["name"]}</a>', AGENTS[k]["role"], AGENT_BIOS[k]["focus"], q) for k, q in
        [("ilsa", "Pricing, contracts, townhomes and condos"), ("tobias", "Buying, inspections, first purchases"), ("nia", "Selling, staging, repairs before listing")]])}
</div></section>
'''
    body = (page_hero("Our team", 'A Denver brokerage of <span class="accent">three.</span>',
                      f"Pikewell has sold homes in central and northwest Denver since {YEAR_FOUNDED}. Three brokers, one phone number, and the same person from your first call to closing day.",
                      [("Home", "index.html"), ("Our Team", "")], img="hood-highland", alt=HOOD["highland"]["alt"],
                      buttons=f'<a class="btn btn-gold" href="index.html?intent=buy#contact">Talk to a broker</a><a class="btn btn-ghost" href="tel:{TEL}">{ic("phone")}{PHONE}</a>')
            + story + team + who + reviews_band(REVIEWS[3:6], bg="snow")
            + faq_block('About Pikewell, <span class="accent">answered.</span>', ABOUT_FAQ, "Licensing, size and how we represent you.")
            + contact())
    people = [{"@context": "https://schema.org", "@type": "Person", "name": AGENTS[k]["name"], "jobTitle": AGENTS[k]["role"],
               "image": f"{BASE}/img/{AGENTS[k]['img']}.webp", "worksFor": {"@id": f"{BASE}/#org"}, "url": f"{BASE}/about.html#{k}"} for k in AGENTS]
    schemas = [org_schema(), business_schema()] + people + [faq_schema(ABOUT_FAQ), crumbs_schema([("Home", ""), ("Our Team", "about.html")])]
    write("about.html", page("about.html", "Our Team | Pikewell Real Estate, Denver",
                             "Meet Ilsa Brandvold, Tobias Hallgren and Nia Abernethy, the three licensed Colorado brokers at Pikewell Real Estate, a Denver brokerage founded in 2014.",
                             schemas, "about", body))


def build_privacy():
    body_html = "".join(f'<h2 class="h-md">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for h, ps in PRIVACY)
    body = (page_hero("Privacy", 'Your privacy at <span class="accent">Pikewell.</span>',
                      "What this website collects, what we never ask for here, and how to protect yourself from wire fraud during a closing.",
                      [("Home", "index.html"), ("Privacy", "")])
            + f'''<section class="section"><div class="wrap prose" style="max-width:800px">{body_html}
<p class="fine" style="margin-top:36px">This is a demo site by Meraki is Love. Pikewell is a fictional brokerage, and nothing entered on this site is sent anywhere. Read more about <a href="buy.html">buying</a>, <a href="sell.html">selling</a> or <a href="about.html">the team</a>.</p>
</div></section>
''' + contact())
    schemas = [org_schema(), crumbs_schema([("Home", ""), ("Privacy", "privacy.html")])]
    write("privacy.html", page("privacy.html", "Privacy | Pikewell Real Estate, Denver",
                               "How the Pikewell Real Estate website handles your information: what the forms collect, what we never ask for online, and a warning about wire fraud.",
                               schemas, "", body))


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("Building Pikewell demo:")
    build_home()
    build_buy()
    build_sell()
    build_value()
    build_hoods_hub()
    for hd in HOODS:
        build_hood(hd["slug"])
    build_listings()
    for ls in LISTINGS:
        build_listing(ls["slug"])
    build_about()
    build_privacy()
    if PROBLEMS:
        print("\nProblems:")
        for p in PROBLEMS:
            print("  " + p)
        sys.exit(1)
