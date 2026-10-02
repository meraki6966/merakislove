"""Copy for the Pikewell Real Estate demo.

Real: Denver, its neighborhoods, parks, streets, transit lines, and the
August 2024 rule changes for buyer agreements. Fictional: the brokerage, its
people, listings, prices, fees and reviews.

Neighborhood guides describe homes, parks, streets and transit. They make no
claims about residents, schools or safety.
"""

# (text, who, where)
REVIEWS = [
    ("Tobias had us sign the buyer agreement at his office and walked through every line first, including what he would be paid. We toured eleven homes in Berkeley and he talked us out of two of them. We closed on the twelfth.",
     "Maren T.", "Berkeley"),
    ("Nia priced our Denver Square about $40,000 under what an online estimate said, and showed us the six sales she based it on. We had three offers in five days and sold above her number.",
     "Calvin and Jo R.", "Washington Park"),
    ("I asked for a home value report expecting a sales pitch. Ilsa sent a four page write-up with the comparable sales and told me to wait a year. I did, and then I called her back.",
     "Priyanka S.", "Park Hill"),
    ("The sewer scope found a cracked clay line on a house we loved. Tobias got the seller to replace it before closing and had the plumber's invoice in our file the same week.",
     "Dominic A.", "Highland"),
    ("We were moving from out of state and saw the townhome on a video call first. Ilsa measured the garage for our truck and counted the stairs to the roof deck. Nothing surprised us on move-in day.",
     "Hannah and Luis V.", "Sloan's Lake"),
    ("Nia gave us a room by room list, which fixes were worth the money and which to skip. We spent $6,200 getting ready and she showed us where every dollar came back at closing.",
     "Roland K.", "Central Park"),
]

HOME_FAQ = [
    ("Do I need to sign something before you show me a home?",
     "Yes. Since August 17, 2024, a buyer working with an agent signs a written agreement before touring a home with that agent. Ours is one page of plain terms on top of the Colorado approved form, and it states what we are paid before you see a single house."),
    ("How much does it cost to buy a home with Pikewell?",
     "Our fee is written into your buyer agreement as a specific amount, and it is negotiable. In many sales the seller agrees to cover some or all of it as part of the offer. You see the number before you sign anything."),
    ("Which Denver neighborhoods do you cover?",
     "We work every day in Washington Park, Highland, Sloan's Lake, Park Hill, Central Park and Berkeley, and we take clients across the rest of metro Denver. Each of those six neighborhoods has its own guide on this site."),
    ("What is my Denver home worth right now?",
     "An online estimate is a starting point. For a number you can plan around, ask for a home value report. A Pikewell broker walks the house, pulls recent sales nearby and sends a written range within two business days, with no obligation to list."),
    ("How fast do you answer?",
     "During office hours, a broker calls or texts back within one business hour. Showings are available seven days a week by appointment."),
    ("Are the listings on this site live?",
     "This is a demo site, so the three listings are samples written to show how a listing page works. On a live Pikewell site, listings come straight from the MLS and update through the day."),
]

BUY_STEPS = [
    ("Talk it through", "A 30 minute call or coffee about budget, timing and which neighborhoods fit how you live. No paperwork yet."),
    ("Sign the buyer agreement", "Before the first tour, we sign a written agreement that states our services and our fee in plain numbers."),
    ("Tour and compare", "We tour together and send notes after each home: recent sales nearby, what the roof and sewer line are likely to need, and what we would offer."),
    ("Offer, inspect, close", "We write the offer, schedule the inspection, sewer scope and radon test, negotiate repairs and track every deadline to closing day."),
]

BUY_COSTS = [
    ("Earnest money", "Due a few days after your offer is accepted", "Often 1% to 3% of the price, credited back at closing"),
    ("General inspection", "During the inspection period", "About $450 to $700"),
    ("Sewer scope", "With the inspection", "About $150 to $250"),
    ("Radon test", "With the inspection", "About $150 to $200"),
    ("Appraisal", "Ordered by your lender", "About $600 to $800"),
    ("Closing costs", "At closing", "Often 2% to 3% of the loan amount"),
]

BUY_FAQ = [
    ("What is a buyer agreement, and why do I have to sign one?",
     "It is a written contract between you and your agent. Since August 17, 2024, an agent working with a buyer must have one signed before touring a home together. It lists the services you get, how long the agreement lasts, and exactly what the agent is paid."),
    ("Who pays the buyer's agent now?",
     "The buyer agreement sets the fee, and you are responsible for it. In practice, we ask the seller to cover it as a term of your offer, and many sellers agree. Offers of buyer agent pay no longer appear on the MLS, so we confirm what a seller will offer before you write."),
    ("Can I negotiate your fee?",
     "Yes. Agent compensation is fully negotiable and is never set by law. We put ours in writing as a specific amount, so there is nothing open ended."),
    ("How long does it take to buy a home in Denver?",
     "Most of our buyers tour for four to eight weeks. Once an offer is accepted, a financed purchase usually closes in 30 to 45 days. Cash can close in about two weeks."),
    ("Why do you order a sewer scope on every older home?",
     "Many Denver homes built before the 1970s still have clay sewer lines, and tree roots find the joints. A camera inspection costs a couple hundred dollars. A line replacement can cost many thousands. We want that known before your inspection deadline."),
    ("Should I test for radon?",
     "Yes. Much of Colorado has elevated radon levels in the soil, and a test during inspection takes about two days. If the level comes back high, a mitigation system is a common repair request."),
    ("Can I tour a home without signing anything?",
     "You can go to any open house on your own, and you can ask a listing agent questions about their listing. To tour privately with one of us as your agent, the written agreement comes first."),
]

SELL_STEPS = [
    ("Walk-through and price", "A broker walks every room, pulls recent sales within a few blocks and gives you a written price range with the sales behind it."),
    ("Prepare", "A room by room list of what to fix, what to skip and what to stage. We schedule the cleaners, the painter and the photographer."),
    ("Launch", "Professional photos, a floor plan and the MLS on a Thursday, with showings through the weekend and one deadline for offers if demand is strong."),
    ("Negotiate and close", "We compare every offer line by line, handle the inspection requests and keep the title company, the lender and the buyer's agent on schedule."),
]

SELL_INCLUDED = [
    "A written price range backed by named comparable sales",
    "Professional photos, a measured floor plan and a short video",
    "A staging consult, with rental furniture arranged if the house is empty",
    "A pre-listing sewer scope, so a buyer's inspection holds no surprise",
    "A weekly report: showings, online views and what agents said",
    "One broker from the first walk-through to the closing table",
]

SELL_TIMELINE = [
    ("Three weeks out", "Walk-through, price range, repair list", "Broker and you"),
    ("Two weeks out", "Repairs, paint touch-ups, sewer scope", "Our vendors, scheduled by us"),
    ("One week out", "Deep clean, staging, photos and floor plan", "Our vendors"),
    ("Launch week", "Live on the MLS Thursday, showings Friday to Sunday", "Broker"),
    ("Week two", "Review offers, choose one, start the contract clock", "Broker and you"),
    ("Weeks three to seven", "Inspection, appraisal, title work, closing", "Broker"),
]

SELL_FAQ = [
    ("Do I still pay the buyer's agent when I sell?",
     "It is your choice. Since August 17, 2024, offers of pay to a buyer's agent no longer appear on the MLS. You can decide to offer it, offer a credit toward the buyer's closing costs, or wait and respond to what each offer asks for. We show you how each choice has played out in recent sales near you."),
    ("What does Pikewell charge to sell a home?",
     "Our listing fee is written into the listing agreement before you sign, and it is negotiable. The agreement lists what that fee covers: photos, the floor plan, the staging consult, the sewer scope and our time."),
    ("How do you set the price?",
     "From closed sales, starting with the ones closest to your home in distance, size and age, then adjusting for condition, lot and updates. You get the list of sales we used, so you can check our work."),
    ("What should I fix before listing?",
     "Usually less than you think. Paint, lighting, cleaning and the yard return the most. Kitchens and baths rarely pay back if you remodel them right before a sale. Your broker gives you a list in priority order with cost estimates."),
    ("How long will it take to sell?",
     "It depends on price, condition and season. Well priced homes in our six neighborhoods often go under contract within the first two weekends. From contract to closing takes about 30 to 45 days when the buyer has a loan."),
    ("What do I have to disclose in Colorado?",
     "Colorado sellers fill out the Seller's Property Disclosure form with what they know about the home, from the roof to the sewer line. For homes built before 1978, federal law also requires a lead based paint disclosure. We go through both forms with you."),
]

VALUE_STEPS = [
    ("Send the address", "Use the form below. Add anything an outsider would miss: a new roof, a finished basement, a rebuilt sewer line."),
    ("We walk the home", "A 30 minute visit, or a video call if you prefer. Condition, light and layout change the number more than square footage does."),
    ("We pull the sales", "Closed sales from the last six months, starting on your block and working outward."),
    ("You get a written range", "Within two business days: a low, a likely and a high number, the sales behind them, and what would move you up the range."),
]

VALUE_COMPARE = [
    ("Source of the number", "A formula run on public records", "A broker who has walked the home"),
    ("Knows about your new roof or kitchen", "Rarely", "Yes"),
    ("Adjusts for your block and lot", "Only loosely", "Yes, sale by sale"),
    ("Shows the sales it used", "Sometimes", "Always, by address"),
    ("Cost", "Free", "Free, with no obligation to list"),
    ("Time", "Instant", "Two business days"),
]

VALUE_FAQ = [
    ("Is the home value report free?",
     "Yes. There is no charge and no obligation to list with us. About half the people who ask for one are a year or more from selling."),
    ("How is this different from an appraisal?",
     "An appraisal is done by a licensed appraiser, usually for a lender, and follows a set format. Ours is a broker's opinion of value: what we believe the home would sell for on the open market, based on recent sales. It is meant for planning, and a lender will still order an appraisal when a buyer gets a loan."),
    ("Why is your number different from the one I saw online?",
     "Online estimates work from public records and cannot see inside the house. They can miss a remodel, a basement finish or a busy street. We have seen them land within a few percent, and we have seen them miss by six figures."),
    ("What happens to the information I send?",
     "It goes to the broker preparing your report and nowhere else. We do not sell leads, and you will not get calls from anyone but us."),
    ("Do I need to clean up before you visit?",
     "No. We are looking at the bones: layout, condition, light, lot. A sink of dishes changes nothing."),
]

HOODS_FAQ = [
    ("Which Denver neighborhood is right for me?",
     "Start with how you spend a normal week. If you want a big park outside your door, look at Washington Park or Sloan's Lake. If you want to walk to dinner, look at Highland or Berkeley. If you want a newer home with a garage, look at Central Park. If you want a 1920s house on a wide street, look at Park Hill."),
    ("Why don't your guides talk about schools or crime?",
     "Fair housing law keeps brokers from steering buyers with opinions about who lives where. So our guides stick to homes, parks, streets and transit. For schools, Denver Public Schools publishes a school finder. For crime data, the Denver Police Department publishes maps you can search by address."),
    ("How current are the price ranges?",
     "On this demo they are sample figures. On a live site they refresh from MLS sales each month, and each guide shows the date of the last update."),
    ("Do you work outside these six neighborhoods?",
     "Yes. We take buyers and sellers across metro Denver. These six are where we work most often, so they have full guides."),
]

LISTINGS_FAQ = [
    ("Are these homes for sale?",
     "No. They are sample listings written for this demo, with photos made for it. A live Pikewell site shows current MLS listings."),
    ("How do I schedule a showing?",
     "Call or text us, or use the form on any listing page. If we have not worked together yet, we sign a buyer agreement before a private tour. Open houses need no agreement."),
    ("Can you show me homes listed by other brokerages?",
     "Yes. As your buyer's agent we can show you any home on the MLS, whoever listed it."),
    ("Why is there no street address?",
     "Sample listings on this demo show the neighborhood and ZIP code only. Live listings show the full address and a map."),
]

ABOUT_FAQ = [
    ("How big is Pikewell?",
     "Three brokers and one transaction coordinator. We stay small on purpose, so the person you meet first is the person at your closing."),
    ("Are you licensed?",
     "Yes. Every Pikewell broker holds an active Colorado real estate license, issued by the Colorado Division of Real Estate. Ilsa Brandvold is the employing broker, which means she supervises every contract the firm writes."),
    ("Can one of you represent both the buyer and the seller?",
     "Colorado law allows a broker to work with both sides as a transaction broker, with written consent from each. We tell you in writing which role we are in before you share anything confidential."),
    ("Do you work with first time buyers?",
     "Often. About a third of our buyers each year are buying their first home. Tobias runs a one hour session on the Colorado contract and its deadlines before you start touring."),
]

AGENT_BIOS = {
    "ilsa": {
        "bio": ["Ilsa has held a Colorado license since 2006 and opened Pikewell in 2014 with one rule: a client should never wait a day for an answer. She still takes her own listings and reviews every contract the firm writes.",
                "She lives in Park Hill in a 1924 Tudor she has been fixing, one room at a time, for eleven years."],
        "lic": "Employing broker. Licensed in Colorado since 2006.",
        "focus": "Sloan's Lake, Park Hill, Highland",
    },
    "tobias": {
        "bio": ["Tobias joined Pikewell in 2017 after eight years as a home inspector, which is why his showing notes mention furnace dates and roof layers. He works only with buyers.",
                "He lives in Berkeley and can tell you which blocks of Tennyson get the afternoon sun."],
        "lic": "Associate broker. Licensed in Colorado since 2017.",
        "focus": "Berkeley, Highland, Central Park",
    },
    "nia": {
        "bio": ["Nia came to real estate from home staging and joined Pikewell in 2019. She prepares and lists homes, and she can price a paint job, a refinished floor or a rented sofa from memory.",
                "She lives near Washington Park and runs the loop around Smith Lake most mornings."],
        "lic": "Associate broker. Licensed in Colorado since 2019.",
        "focus": "Washington Park, Park Hill, Central Park",
    },
}

# Neighborhood guides
HOOD_PAGES = {
    "washington-park": {
        "title": "Washington Park Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Washington Park in Denver: the 165 acre park, the brick bungalows and Denver Squares, South Gaylord Street and what to check before you buy.",
        "h1": 'Living in <span class="accent">Washington Park.</span>',
        "lede": "Brick bungalows and Denver Squares around a 165 acre park with two lakes, a 1913 boathouse and a loop that is busy by sunrise.",
        "about": [
            "Washington Park the neighborhood wraps around Washington Park the park: 165 acres with Smith Lake at the north end, Grasmere Lake at the south, flower gardens in between and a boathouse that has stood on the shore since 1913. Most people here call both of them Wash Park.",
            "The homes east of the park are mostly 1910s to 1930s brick: bungalows with deep porches and two story Denver Squares. Over the last twenty years many smaller houses have been replaced by larger new builds, so one block can hold a 1,200 square foot bungalow and a 4,500 square foot house finished last year.",
            "South Gaylord Street, a few blocks east of the park, is one of the oldest shopping streets in Denver, with restaurants and shops in low brick storefronts. Downing Street runs along the park's west edge, and the Louisiana Pearl light rail station sits to the southwest.",
        ],
        "know": [
            ("Price tracks distance to the park", "Homes facing the park or within two blocks carry a premium. Six blocks east, the same house costs less."),
            ("Old houses, old systems", "Ask about the sewer line, the wiring and the boiler. Many 1920s homes have had all three replaced. Some have had none."),
            ("New next to old", "If you are buying a bungalow, look at what could be built next door. Zoning here allows a much larger house on most lots."),
            ("Parking on park weekends", "Streets near the park fill up on summer weekends. A garage or an alley parking pad matters more here than in most places."),
        ],
        "around": "Downtown is about 15 minutes by car. The Louisiana Pearl station connects to downtown and the Tech Center by light rail, and the park's loop links to bike routes heading north to Cherry Creek.",
        "faq": [
            ("How big is Washington Park?", "The park covers 165 acres and includes two lakes, Smith Lake and Grasmere Lake, along with flower gardens, tennis courts, a recreation center and paths for walking and cycling."),
            ("What kinds of homes are in Washington Park?", "Mostly brick bungalows and Denver Squares from the 1910s through the 1930s, along with larger homes built in the last two decades on lots where smaller houses once stood."),
            ("What is a Denver Square?", "A two story brick house with a nearly square footprint, a hipped roof and a full width front porch. Builders put up thousands of them across Denver between about 1895 and 1920. Elsewhere the style is called a foursquare."),
            ("Is Washington Park walkable?", "The park itself and South Gaylord Street are both reachable on foot from most of the neighborhood. For a commute, most people drive, bike or take light rail from Louisiana Pearl."),
        ],
    },
    "highland": {
        "title": "Highland Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Highland and LoHi in Denver: brick Victorians, modern townhomes, the Highland Bridge to downtown and what to check before you buy.",
        "h1": 'Living in <span class="accent">Highland.</span>',
        "lede": "Brick Victorians and modern townhomes on the bluff northwest of downtown, with the skyline at the end of the street.",
        "about": [
            "Highland sits on the high ground across Interstate 25 and the South Platte River from downtown. The lower end, which most people call LoHi, connects to downtown on foot by the Highland Bridge, a pedestrian bridge over the interstate.",
            "The older homes are Victorians and brick cottages from the 1880s and 1890s, many inside the Potter Highlands historic district. Between them stand townhomes and condos from the last fifteen years, most with a rooftop deck aimed at the skyline.",
            "Restaurants and shops cluster along Tejon Street, 32nd Avenue and the blocks near the bridge. Federal Boulevard marks the west edge, with West Highland beyond it.",
        ],
        "know": [
            ("Historic district rules", "Inside a Denver landmark district, exterior changes go through design review. Ask before you plan new windows or an addition."),
            ("Townhomes vary widely", "Build quality differs from one project to the next. We check who built it, how the roof deck drains and whether there is an owners association."),
            ("Parking", "Many Victorians have no garage, and street parking is tight near the restaurants. Count the spaces that come with the house."),
            ("Views can change", "A skyline view over a one story building is safe only as long as that building stays one story. We look up what the lot next door is zoned for."),
        ],
        "around": "Downtown is about eight minutes by car, or a 15 to 20 minute walk over the Highland Bridge to Union Station, where every rail line in the region meets.",
        "faq": [
            ("What is the difference between Highland and LoHi?", "LoHi is short for Lower Highland, the part of the Highland neighborhood closest to downtown. West Highland, across Federal Boulevard, is a separate neighborhood, and people often call all three the Highlands."),
            ("Can I walk downtown from Highland?", "Yes. The Highland Bridge crosses Interstate 25 on foot, and from there two more pedestrian bridges lead to Union Station."),
            ("What kinds of homes are in Highland?", "Victorians and brick cottages from the 1880s and 1890s, row homes, and a large number of modern townhomes and condos built since about 2008."),
            ("Can I remodel a Victorian in Potter Highlands?", "Interior work is up to you. Exterior changes that can be seen from the street need approval from Denver's landmark preservation staff, so plan extra time for the review."),
        ],
    },
    "sloans-lake": {
        "title": "Sloan's Lake Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Sloan's Lake in Denver: the city's largest lake, the loop path, mid-century ranches, new townhomes and what to check before you buy.",
        "h1": 'Living at <span class="accent">Sloan\'s Lake.</span>',
        "lede": "Denver's largest lake, a loop path of about two and a half miles and the Front Range lined up behind the water at sunset.",
        "about": [
            "Sloan's Lake Park holds the largest lake in Denver, circled by a path of about two and a half miles. On a clear evening the west shore gives you the mountains, and the east shore gives you the mountains with the water in front of them.",
            "The neighborhood grew in two waves. The first left brick bungalows and mid-century ranches on quiet streets north and east of the lake. The second, still underway, added townhomes and condo buildings along the south shore, where a hospital campus stood until 2011.",
            "Sheridan Boulevard runs along the west side, with the small city of Edgewater across it. West Colfax Avenue is a few blocks south, and the W Line light rail runs beyond that.",
        ],
        "know": [
            ("Denver or Edgewater", "Homes west of Sheridan are in Edgewater and Jefferson County, with different taxes and city services. Check which side a listing is on."),
            ("New construction details", "For townhomes, we ask about the builder's warranty, how the roof deck was waterproofed and what the owners association covers."),
            ("Ranches with basements", "Many mid-century ranches have a full basement. Check ceiling height and window size if you plan to add a bedroom downstairs."),
            ("The view premium", "A direct lake view adds a lot to the price. One block back, you keep the park and lose most of the premium."),
        ],
        "around": "Downtown is about 12 minutes by car along 17th Avenue or Colfax. The W Line has stations at Knox, Perry and Sheridan, south of Colfax, and runs to Union Station.",
        "faq": [
            ("How long is the loop around Sloan's Lake?", "The path around the lake is about two and a half miles and is flat the whole way."),
            ("What kinds of homes are near Sloan's Lake?", "Brick bungalows, mid-century ranches, and a growing number of modern townhomes and condos, most of them along the south shore and near West Colfax."),
            ("Is Sloan's Lake in Denver or Edgewater?", "The lake and park are in Denver. Sheridan Boulevard is the city line, and the blocks west of it belong to Edgewater, a separate city in Jefferson County."),
            ("Can you get to downtown without a car?", "Yes. The W Line light rail has three stations south of West Colfax, and bus routes run along West Colfax Avenue."),
        ],
    },
    "park-hill": {
        "title": "Park Hill Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Park Hill in Denver: broad parkways, 1920s Tudors and Denver Squares east of City Park, and what to check before you buy.",
        "h1": 'Living in <span class="accent">Park Hill.</span>',
        "lede": "Brick Tudors and Denver Squares on broad parkways, with City Park, the zoo and the science museum at the west edge.",
        "about": [
            "Park Hill begins at Colorado Boulevard, on the east side of City Park, where the Denver Zoo and the Denver Museum of Nature and Science sit. From there it runs east along Montview Boulevard and 17th Avenue Parkway, two streets with planted medians and mature trees.",
            "Most of the houses went up between 1900 and 1940. You will see brick Tudors with steep gables, Denver Squares with wide porches and rows of brick bungalows, on lots that are larger than in most central Denver neighborhoods.",
            "Small clusters of shops sit inside the neighborhood, at 23rd Avenue and Kearney Street and at Oneida Park, so a coffee or a dinner out can be a walk.",
        ],
        "know": [
            ("Three Park Hills", "The city counts South Park Hill, North Park Hill and Northeast Park Hill as separate neighborhoods. House sizes and prices differ among them, so compare sales within the same one."),
            ("Mature trees and sewer lines", "Big trees are part of the appeal, and their roots find old clay sewer lines. A sewer scope is a must here."),
            ("Tudor roofs", "Steep roofs with several valleys cost more to replace. Colorado hail makes roof age one of the first things we check."),
            ("Parkway setbacks", "Homes on the parkways sit far back on deep lots. The front yard is large, and so is the watering bill in July."),
        ],
        "around": "Downtown is about 15 minutes by car along 17th Avenue or Montview. Bus routes run on Colfax and Colorado Boulevard, and the A Line stops at 40th and Colorado, north of the neighborhood.",
        "faq": [
            ("Where is Park Hill in Denver?", "East of City Park. It starts at Colorado Boulevard and runs east to about Quebec Street, between East Colfax Avenue on the south and the rail corridor on the north."),
            ("What kinds of homes are in Park Hill?", "Mostly brick homes from 1900 to 1940: Tudors, Denver Squares and bungalows, with some mid-century ranches toward the north and east."),
            ("How close is Park Hill to City Park?", "The west edge of Park Hill faces City Park across Colorado Boulevard. From most of South Park Hill, the park, the zoo and the science museum are a short bike ride."),
            ("Are lots bigger in Park Hill?", "Often, yes. Many blocks were laid out with wider lots and deeper setbacks than neighborhoods closer to downtown, and the parkways have the largest lots."),
        ],
    },
    "central-park": {
        "title": "Central Park Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Central Park in Denver: homes built since 2001 on the former airport site, 1,100 acres of parks, the A Line and what to check before buying.",
        "h1": 'Living in <span class="accent">Central Park.</span>',
        "lede": "Homes built since 2001 on the site of Denver's former airport, with 1,100 acres of parks and a train to downtown and the airport.",
        "about": [
            "Central Park stands where Stapleton International Airport operated until 1995. Home building began in 2001, and the neighborhood took its current name in 2020, after the 80 acre park at its center. The old control tower still stands.",
            "Because everything was planned at once, the neighborhood has 1,100 acres of parks and open space threaded between the homes, with greenways, pools and pocket parks. Homes range from condos and row homes to large single family houses, most with a front porch and a garage on an alley.",
            "Shops and restaurants gather at a few town centers, and the Central Park station on the A Line, open since 2016, connects to Union Station in one direction and Denver International Airport in the other.",
        ],
        "know": [
            ("Read the tax bill", "Property taxes here include a metropolitan district levy that paid for streets and parks. Compare the full tax bill with a home in an older neighborhood."),
            ("Association fee", "A community association maintains the pools and shared spaces, and every home pays into it. We get the current fee and rules before you offer."),
            ("Newer systems", "A home from 2010 will not need a new sewer line or wiring. Do check the roof for hail history and ask about any builder warranty claims."),
            ("Affordable home program", "Some homes carry resale restrictions under an income qualified program. We confirm whether a listing is one of them."),
        ],
        "around": "Downtown is about 20 minutes by car on Interstate 70 or Martin Luther King Jr. Boulevard. The A Line reaches Union Station in about 15 minutes and the airport in about 25.",
        "faq": [
            ("Is Central Park the same as Stapleton?", "Yes. The neighborhood was called Stapleton, after the airport that once stood there, until residents chose the name Central Park in 2020."),
            ("How old are the homes in Central Park?", "The first homes were finished in the early 2000s, and building has continued since, so you will find homes from about 2002 through today."),
            ("Does Central Park have a train station?", "Yes. The Central Park station is on the A Line, which runs between Union Station downtown and Denver International Airport."),
            ("Why are property taxes higher in Central Park?", "Homes here pay an added metropolitan district levy, which funded the roads, parks and utilities built for the new neighborhood. The amount shows on every tax bill."),
        ],
    },
    "berkeley": {
        "title": "Berkeley Homes and Guide | Pikewell Denver",
        "desc": "A broker's guide to Berkeley in northwest Denver: 1920s brick bungalows, Tennyson Street, two lake parks and what to check before you buy.",
        "h1": 'Living in <span class="accent">Berkeley.</span>',
        "lede": "1920s brick bungalows a short walk from Tennyson Street, with a lake park at each end of the neighborhood.",
        "about": [
            "Berkeley sits in the northwest corner of Denver, with Sheridan Boulevard on the west and Interstate 70 along the north. Tennyson Street runs up the middle, and its blocks between 38th and 46th avenues hold the restaurants, shops and bars the neighborhood is known for.",
            "Two parks anchor it. Berkeley Lake Park is on the west side, with a path around the water and a small brick library. Rocky Mountain Lake Park is on the east side, with its own lake and a view of the mountains from the shore.",
            "The original houses are brick bungalows from the 1910s and 1920s. In the last fifteen years many have been joined, or replaced, by two story duplexes and new single family homes.",
        ],
        "know": [
            ("Bungalow or duplex", "A new half duplex gives you more space and newer systems. A bungalow gives you a yard and no shared wall. Prices overlap, so tour both."),
            ("Highway sound", "The northern blocks sit close to Interstate 70. Visit at rush hour before you fall for a house there."),
            ("Tennyson parking", "Within a block or two of Tennyson, street parking fills on weekend nights. Check for a garage or a parking pad off the alley."),
            ("Basement finishes", "Many bungalow basements were finished without permits decades ago. We look up the permit history before you count a basement bedroom."),
        ],
        "around": "Downtown is about 15 minutes by car on Interstate 70 or 38th Avenue. Bus routes run along 38th and 44th avenues, and bike lanes connect east toward Highland.",
        "faq": [
            ("Where is Tennyson Street?", "Tennyson Street runs north and south through the middle of Berkeley. The stretch with most of the shops and restaurants is between 38th Avenue and 46th Avenue."),
            ("What kinds of homes are in Berkeley?", "Brick bungalows from the 1910s and 1920s, plus many newer duplexes and single family homes built on lots where smaller houses once stood."),
            ("What parks are in Berkeley?", "Berkeley Lake Park on the west side and Rocky Mountain Lake Park on the east side. Each has a lake with a walking path around it."),
            ("Is Berkeley the same as the Highlands?", "No. Berkeley is its own neighborhood, north of West Highland. The two meet at 38th Avenue."),
        ],
    },
}

LISTING_PAGES = {
    "washington-park-denver-square": {
        "seo_title": "1912 Denver Square, Washington Park | Pikewell",
        "desc": "Sample listing: a restored 1912 brick Denver Square near Washington Park in Denver. Four bedrooms, three baths, 2,940 square feet, offered at $1,485,000.",
        "body": [
            "Two blocks east of Washington Park, this 1912 Denver Square has its original oak staircase, pocket doors and a full width front porch, along with the systems a 1912 house needs to keep going for another century.",
            "The kitchen was opened to the dining room in 2021 and finished with soapstone counters and a six burner range. Upstairs are three bedrooms and two baths, including a primary suite across the back of the house. The finished basement adds a fourth bedroom, a bath and a room for guests or a home office.",
            "The sewer line was replaced in 2019, the roof in 2022, and the old boiler gave way to a high efficiency system with air conditioning in 2020.",
        ],
        "features": ["Original oak staircase, pocket doors and trim", "Kitchen opened and rebuilt in 2021", "Primary suite with a walk-in closet",
                     "Finished basement with a bedroom and bath", "Two car garage on the alley", "New sewer line, roof and boiler since 2019"],
    },
    "berkeley-brick-bungalow": {
        "seo_title": "1926 Brick Bungalow, Berkeley | Pikewell",
        "desc": "Sample listing: a 1926 brick bungalow near Tennyson Street in Berkeley, Denver. Three bedrooms, two baths, 1,720 square feet, offered at $865,000.",
        "body": [
            "Three blocks from Tennyson Street, this 1926 bungalow kept its brick, its porch and its built-in dining room cabinets, and gained a kitchen that opens to the backyard through a wide glass door.",
            "Two bedrooms and a bath are on the main floor. The basement was finished with permits in 2018 and holds a third bedroom with a full size window, a second bath and a laundry room.",
            "The front yard was replanted with low water grasses and sage in 2023, and the backyard has a paved patio, raised beds and a one car garage with a second parking pad beside it.",
        ],
        "features": ["Covered brick front porch", "Original built-in cabinets in the dining room", "Kitchen updated in 2020 with a gas range",
                     "Basement finished with permits in 2018", "Low water front yard, patio and raised beds", "One car garage plus a parking pad"],
    },
    "sloans-lake-townhome": {
        "seo_title": "Rooftop Deck Townhome, Sloan's Lake | Pikewell",
        "desc": "Sample listing: a modern end unit townhome two blocks from Sloan's Lake in Denver. Three bedrooms, four baths, a rooftop deck, offered at $1,050,000.",
        "body": [
            "Two blocks from the lake path, this 2019 end unit has windows on three sides and a rooftop deck that faces west, toward the lake and the mountains behind it.",
            "The main level is one open room with a kitchen island that seats five. Each of the three bedrooms has its own bath, and a fourth level opens to the roof deck, with a wet bar on the landing.",
            "An attached two car garage is wired for a car charger, and the owners association covers exterior insurance, snow removal and the shared driveway.",
        ],
        "features": ["Rooftop deck with lake and mountain views", "End unit with windows on three sides", "Each bedroom has its own bath",
                     "Kitchen island with seating for five", "Attached two car garage, wired for a charger", "Low monthly association fee"],
    },
}

PRIVACY = [
    ("What this website collects", [
        "The contact and home value forms ask for your name, phone number, email, the neighborhood you care about, your timing and, for a home value report, the property address. That is all.",
        "The forms travel over an encrypted connection and go to the Pikewell broker on duty. We use what you send to answer your request.",
    ]),
    ("What we never do", [
        "We do not sell or rent your information, and we do not pass it to lenders, movers, insurers or lead brokers. If you want an introduction to a lender or an inspector, we ask you first.",
        "We do not ask for your Social Security number, bank details or loan documents through this website. Those go straight to your lender or the title company through their own secure portals.",
    ]),
    ("Wire fraud warning", [
        "Criminals send fake emails with wiring instructions that look like they come from a broker or a title company. Pikewell will never email you wiring instructions. Before you send money for a closing, call the title company at a number you looked up yourself and confirm every digit.",
    ]),
    ("Cookies and tracking", [
        "This site has no advertising trackers and no tracking pixels. We count visits in aggregate, without cookies and without building a profile of you.",
    ]),
    ("Your choices", [
        "You can ask us what we hold about you, ask us to correct it, or ask us to delete it. Call or text the office and ask for the managing broker.",
    ]),
]
