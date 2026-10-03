"""Copy for the Sideoats Insurance Agency demo.

Real and checked in October 2026:
- Texas Department of Insurance (TDI): the auto guide (30/60/25, the eight coverages, PIP and
  uninsured motorist rules), the home guide (six coverages, what is and is not covered, replacement
  cost and actual cash value, flood and its 30 day wait, the Consumer Bill of Rights), the
  deductibles tip (the $150,000 example, each claim, the 20 percent note), the renters tip (three
  coverages, about $20 a month, the laptop example, common sub-limits), the hail tip (steps, the
  contractor warnings, comprehensive for cars), claim deadlines, and the workers' compensation guide.
- National Weather Service Fort Worth: the hail size guide and the 1995 Mayfest storm summary.
  NWS: a storm is severe at hail one inch across or larger.
- FloodSmart: National Flood Insurance Program limits of $250,000 building and $100,000 contents.
- City of Fort Worth historic preservation: Fairmount/Southside facts. Historic Fort Worth: Camp
  Bowie Boulevard. Benbrook Lake: U.S. Army Corps of Engineers facts as summarized on Wikipedia.
People, reviews and the worked examples are samples. Nothing here is a quote.
"""
from so import TDI, PHONE, TEL

# NWS Fort Worth hail size guide: name, diameter in inches.
HAIL = [("Pea", 0.25), ("Penny", 0.75), ("Quarter", 1.0), ("Golf ball", 1.75), ("Baseball", 2.75)]

REVIEWS = [
    ("Rosalind put my deductible in dollars on one page. I had paid for that policy for six years and never knew the number.", "Carla M.", "Fairmount"),
    ("After the April storm they told me the repair was under my deductible before I filed anything. I was glad to know that first.", "Dwight P.", "Benbrook"),
    ("Desmond asked how each of my trucks was used and found two that were on the wrong policy.", "Ines R.", "Near Southside"),
]

HOME_FAQ = [
    ("What is a percentage deductible?", 'It is a deductible set as a share of what your house is insured for. On a house insured for $380,000, a 2% wind and hail deductible is $7,600. You pay that amount on each claim before the policy pays anything. The <a href="hail-deductible.html">hail deductible guide</a> has a table for other house values.'),
    ("Does home insurance cover flooding in Texas?", 'No. Home policies do not cover flooding. <a href="flood-insurance.html">Flood insurance</a> is a separate policy, and most flood policies have a 30 day waiting period before they start, so it has to be in place before a storm is on the forecast.'),
    ("What is the minimum auto insurance in Texas?", 'Texas requires liability coverage of at least $30,000 for each injured person, up to $60,000 per accident, and $25,000 for property damage. It is written as 30/60/25. The <a href="auto-insurance.html">auto page</a> explains where those numbers run out.'),
    ("What is an independent insurance agency?", "An independent agency is not tied to one insurance company. We place your policy with the carrier that fits, and at renewal we can check it against the others we represent."),
    ("How do I check that an agent is licensed in Texas?", f'Call the Texas Department of Insurance help line at <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a>, or use the agent lookup on the department\'s website. Every Texas agent and agency has a license number you can ask for.'),
]

COVERAGE_FAQ = [
    ("Which policies does a homeowner in Fort Worth usually carry?", 'Home and auto, and flood if the house is near water or in a mapped flood zone. An <a href="umbrella-insurance.html">umbrella</a> is worth a look once there is equity or savings to protect.'),
    ("Can you insure my home and car with different companies?", "Yes. An independent agency can place each policy where it fits. Bundling them with one carrier often brings a discount, so we price it both ways."),
    ("Do you give quotes online?", "We give them by phone or in person, after we have read your current policy. A quote that ignores your deductible and limits is a guess."),
    ("What does it cost to use an agent?", "Nothing extra. The insurance company pays the agency a commission that is already part of the premium."),
]

COVERAGE_PAGES = {
    "home-insurance": {
        "title": "Home Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Home insurance in Fort Worth from an independent agency. We work out your wind and hail deductible in dollars and explain what the policy covers.",
        "h1": "Home insurance in Fort Worth",
        "lede": "A home policy is six coverages sold together. The part most people have never worked out is the wind and hail deductible, so we start there.",
        "fig": ("A common wind and hail deductible", "2%", 'On a house insured for $380,000, that is $7,600 out of your pocket before the policy pays for a roof. <a href="hail-deductible.html">Work out yours</a>.'),
        "main_title": "What is in a home policy?", "main_head": ("Coverage", "What it pays for"),
        "main": [("Dwelling", "Repairs or rebuilds the house when it is damaged by something the policy covers."),
                 ("Other structures", "Fences, sheds and detached garages that are not attached to the house."),
                 ("Personal property", "Furniture, clothing and other belongings that are stolen, damaged or destroyed."),
                 ("Additional living expenses", "The extra cost of living somewhere else while covered damage is repaired."),
                 ("Personal liability", "Medical bills, lost wages and other costs for people you are legally responsible for injuring."),
                 ("Medical payments", "Medical bills for people hurt on your property.")],
        "lists": [("What do most home policies cover?", ["Fire and lightning", "Sudden and accidental water or smoke damage", "Explosion", "Theft and vandalism",
                                                          "Damage from aircraft and vehicles", "Windstorm and hail, away from the Gulf Coast"]),
                  ("What do most home policies leave out?", ["Flooding", "Continuous water leaks", "Termites, insects and rodents", "Losses while the house sits vacant",
                                                             "Wear and tear", "Earthquakes", "Wind or hail damage to trees"])],
        "body_title": "Replacement cost or actual cash value?",
        "body": ["Replacement cost coverage pays to repair or replace your house and belongings at current prices. Actual cash value coverage pays replacement cost minus depreciation.",
                 "On an older roof, that difference can be most of the bill. Ask which one your policy uses for the roof, because some policies treat the roof differently from the rest of the house.",
                 "The dwelling limit should match what it costs to rebuild the house. That number has little to do with what the house would sell for, and it moves when lumber and labor prices move."],
        "img": ("bungalow", "A restored craftsman bungalow in Fort Worth with a wide front porch, brick piers and a new dark shingle roof under a live oak"),
        "faq": [("Does home insurance cover hail damage in Fort Worth?", 'Most home policies cover windstorm and hail. The deductible comes out first, and for wind and hail it is often a percentage of what the house is insured for. The <a href="hail-deductible.html">hail deductible guide</a> shows what that is in dollars.'),
                ("Is flood damage covered by home insurance?", 'No. Flooding needs its own policy. See <a href="flood-insurance.html">flood insurance</a>.'),
                ("How much dwelling coverage do I need?", "Enough to rebuild the house at today's prices. We run a rebuilding cost estimate with you and compare it to the limit on your current policy."),
                ("What is the Consumer Bill of Rights?", "Texas has a Consumer Bill of Rights for home and renters insurance. Your insurance company gives you a copy when you get or renew a policy. It lists what the company owes you and how to complain.")],
    },
    "auto-insurance": {
        "title": "Auto Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Auto insurance in Fort Worth from an independent agency. What the Texas minimum of 30/60/25 pays for, where it runs out, and what the next step covers.",
        "h1": "Auto insurance in Fort Worth",
        "lede": "Texas lets you drive with 30/60/25. We show you what those numbers pay for, where they run out, and what the next step up covers.",
        "fig": ("The state minimum for property damage", "$25,000", "That is all a minimum policy pays to fix the other driver's vehicle. Many new trucks cost more than that."),
        "trio": True,
        "main_title": "What are the eight auto coverages?", "main_head": ("Coverage", "What it pays for"),
        "main": [("Liability", "The other person's injuries and property when a wreck is your fault. This is the 30/60/25."),
                 ("Collision", "Repairing or replacing your own car after a wreck."),
                 ("Comprehensive", "Theft, fire, flood and hail. This is the coverage that pays for hail dents."),
                 ("Medical payments", "Medical bills for you and your passengers."),
                 ("Personal injury protection", "Medical bills and some lost income, whoever caused the wreck. Included unless you reject it in writing."),
                 ("Uninsured and underinsured motorist", "Your costs when the other driver has no insurance or too little. Your insurer must offer it."),
                 ("Towing and labor", "A tow or roadside help."),
                 ("Rental reimbursement", "A rental car while yours is in the shop after a covered loss.")],
        "body_title": "Is the state minimum enough?",
        "body": ["The minimum keeps you legal. It was not built to cover a serious wreck. $25,000 for property damage is less than the price of many new vehicles, and $30,000 does not go far in an emergency room.",
                 "When a judgment is larger than your limits, the difference can come from your savings and your wages. We price the next two steps alongside the minimum, so you can see what the extra coverage costs before you choose."],
        "limits": [("30/60/25", "The Texas minimum", "$25,000"), ("50/100/50", "A common first step up", "$50,000"), ("100/300/100", "What we suggest pricing for most homeowners", "$100,000")],
        "faq": [("What is the minimum auto insurance in Texas?", "Liability coverage of at least $30,000 for each injured person, up to $60,000 per accident, and $25,000 for property damage. It is written as 30/60/25."),
                ("Does auto insurance cover hail damage?", 'Only if you carry comprehensive coverage. Your comprehensive deductible comes out first. See <a href="after-a-hail-storm.html">what to do after a hail storm</a>.'),
                ("What is PIP?", "Personal injury protection pays medical bills and some lost income for you and your passengers, whoever caused the wreck. Every Texas auto policy includes it unless you reject it in writing."),
                ("Do I need uninsured motorist coverage?", "Your insurer has to offer it, and you only go without it if you turn it down in writing. It is what pays when the driver who hit you has no insurance.")],
    },
    "renters-insurance": {
        "title": "Renters Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Renters insurance in Fort Worth from an independent agency. What it covers, what your landlord's policy leaves out, and what to check before you buy.",
        "h1": "Renters insurance in Fort Worth",
        "lede": "Your landlord's policy covers the building. It pays nothing for your furniture, your laptop or a guest who gets hurt in your apartment.",
        "fig": ("About what a renters policy costs in Texas", "$20", "A month, on average, according to the Texas Department of Insurance. Ask us for your own number before you decide."),
        "main_title": "What does renters insurance cover?", "main_head": ("Coverage", "What it pays for"),
        "main": [("Personal property", "Your belongings, including items stolen out of your car or while you travel."),
                 ("Additional living expenses", "The extra cost of food and rent if you have to move out while the apartment is repaired."),
                 ("Personal liability", "Your costs if someone is injured in your home, including legal costs.")],
        "body_title": "What should a renter check before buying?",
        "body": ["Ask whether the policy pays actual cash value or replacement cost. The Texas Department of Insurance gives this example: a laptop bought two years ago for $1,300 might be valued at $500 under basic coverage. A replacement cost policy pays for a new one and costs more.",
                 "Look for the sub-limits. Common ones are $100 for cash, $500 for jewelry and watches, and $2,500 for items used for business. If you own more than that, we add coverage for those items.",
                 "Renters policies do not cover floods. If you rent on a ground floor near a creek, ask us about flood coverage for your belongings."],
        "checks_title": "What should I know before I call?",
        "checks": ["Roughly what your belongings would cost to replace", "Whether you own jewelry, watches or equipment above the usual sub-limits",
                   "Whether you work from home with your own gear", "The liability amount your lease asks for, if it asks for one"],
        "faq": [("Does my landlord's insurance cover my things?", "No. It covers the building. Your belongings and your liability are yours to insure."),
                ("How much does renters insurance cost in Texas?", "The Texas Department of Insurance puts the average at about $20 a month. Your price depends on where you live and how much coverage you choose."),
                ("Does renters insurance cover flooding?", 'No. Renters policies do not cover losses from floods. <a href="flood-insurance.html">Flood coverage</a> for belongings is a separate policy.'),
                ("Is my roommate covered by my policy?", "Not unless they are named on it. Each roommate usually needs a policy, or both names need to be on one.")],
    },
    "flood-insurance": {
        "title": "Flood Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Flood insurance in Fort Worth from an independent agency. Home policies do not cover flooding, and most flood policies take 30 days to start.",
        "h1": "Flood insurance in Fort Worth",
        "lede": "Home and renters policies do not cover flooding. Flood insurance is its own policy, and it has to be bought before the rain is in the forecast.",
        "fig": ("Days before most flood policies start", "30", "Most flood policies have a 30 day waiting period. A policy bought the week of the storm will not help with that storm."),
        "main_title": "What does a federal flood policy cover?", "main_head": ("Coverage", "Limit", "What it pays for"),
        "main": [("Building", "Up to $250,000", "The foundation, electrical and plumbing systems, and finishings."),
                 ("Contents", "Up to $100,000", "Appliances, electronics and personal belongings.")],
        "main_note": "Limits for a residential policy from the National Flood Insurance Program. Private flood carriers can write higher limits.",
        "body_title": "Who needs flood insurance in Fort Worth?",
        "body": ["The forks of the Trinity River run through the city, and the creeks that feed them run through its neighborhoods. Benbrook Lake, on the Clear Fork southwest of town, was built by the Corps of Engineers for flood control.",
                 "If your house is in a mapped high risk flood zone and you have a mortgage, your lender will ask for a flood policy. Outside those zones it is your choice, and houses there flood too, usually from heavy rain with nowhere to drain.",
                 "We look up your address on the federal flood map, tell you what zone it is in, and price the federal program beside any private carrier that writes your street."],
        "img": ("flood-street", "A residential street in Texas under brown flood water after heavy rain, with the water reaching the front lawns of brick houses"),
        "faq": [("Does homeowners insurance cover flood damage?", "No. Most home policies do not cover flooding. It takes a separate flood policy."),
                ("How long before flood insurance takes effect?", "Most flood policies have a 30 day waiting period, so buy it well before storm season."),
                ("How much does the federal flood program cover?", "A residential policy from the National Flood Insurance Program covers up to $250,000 for the building and up to $100,000 for contents."),
                ("Can renters buy flood insurance?", "Yes. A renter can buy contents coverage for belongings. A renters policy by itself does not cover floods.")],
    },
    "business-insurance": {
        "title": "Business Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Business insurance in Fort Worth from an independent agency: general liability, commercial auto, property and workers' compensation for small businesses.",
        "h1": "Business insurance in Fort Worth",
        "lede": "Shops, trades and offices need a different set of policies from a household. We start with how the business makes its money and what it drives.",
        "fig": ("Workers' compensation policies Texas requires of most private employers", "0", "Texas does not require most private employers to carry it. An employer who goes without loses key defenses in court when an employee is hurt."),
        "main_title": "What does a small business need?", "main_head": ("Policy", "What it pays for"),
        "main": [("General liability", "Injuries to customers and the public, and damage to their property, caused by your business."),
                 ("Commercial property", "Your building, equipment and inventory after fire, theft or a storm."),
                 ("Commercial auto", "Vehicles used for work: hauling tools, making deliveries, carrying customers."),
                 ("Workers' compensation", "Medical care and lost wages for employees hurt on the job."),
                 ("Business owner's policy", "Liability and property bundled in one policy for a small business.")],
        "body_title": "What does going without workers' compensation mean?",
        "body": ["Texas does not require most private employers to have workers' compensation. Private employers who contract with government entities must provide it for the employees working on the project.",
                 "An employer without coverage loses the legal protection against most lawsuits. In court, that employer cannot argue that the employee's own negligence caused the injury, that another employee's negligence caused it, or that the employee knew about the danger and accepted it.",
                 "An employer without coverage also has to file a yearly notice with the Division of Workers' Compensation, post notices in the workplace, and tell new employees in writing that they are not covered."],
        "checks_title": "What does Desmond ask first?",
        "checks": ["How each vehicle is used, and who drives it", "Whether you have employees, subcontractors or both", "Who asks you for a certificate of insurance, and what limits they want",
                   "What a week of being closed would cost you"],
        "faq": [("Is workers' compensation required in Texas?", "Not for most private employers. It is required for private employers on government contracts, for the employees working on that project."),
                ("Does my personal auto policy cover my work truck?", "Probably not. A vehicle that hauls tools, makes deliveries or carries customers usually needs a commercial auto policy. Tell us how the truck is used and we will check."),
                ("What is a certificate of insurance?", "A one page proof of coverage that a landlord, a general contractor or a client asks for. We issue them the same business day."),
                ("What is a business owner's policy?", "A package that combines general liability and commercial property for a small business, usually for less than buying the two apart.")],
    },
    "umbrella-insurance": {
        "title": "Umbrella Insurance in Fort Worth, TX | Sideoats Insurance",
        "desc": "Umbrella insurance in Fort Worth from an independent agency. Extra liability coverage above your home and auto limits, explained with one example.",
        "h1": "Umbrella insurance in Fort Worth",
        "lede": "An umbrella policy adds liability coverage above the limits on your home and auto policies. It pays when a judgment is bigger than those limits.",
        "fig": ("The usual size of one umbrella layer", "$1M", "Umbrella policies are commonly sold in layers of one million dollars, on top of the liability limits you already carry."),
        "main_title": "How does an umbrella pay?", "main_head": ("Step", "Who pays", "Amount"),
        "main": [("A wreck is your fault", "The injuries total", "$450,000"),
                 ("Your auto policy pays first", "Auto liability, $300,000 per accident", "$300,000"),
                 ("The umbrella pays what is left", "One $1,000,000 layer", "$150,000"),
                 ("Without an umbrella", "You pay what is left", "$150,000")],
        "main_note": "An illustration with round numbers. It is not a quote, and an actual policy has conditions.",
        "body_title": "Who buys an umbrella?",
        "body": ["People with something to lose in a lawsuit: equity in a house, savings, or wages that could be garnished. It is also common for households with a teenage driver, a pool or a rental property.",
                 "Most carriers want higher liability limits on the home and auto policies underneath before they will write an umbrella. We check those limits first and price the change with the umbrella.",
                 "An umbrella is liability coverage only. It pays other people. It does not repair your own house or your own car, and it has nothing to do with your deductible."],
        "faq": [("What does an umbrella policy cover?", "Liability above the limits of your home and auto policies: injuries to other people, damage to their property, and the legal costs that come with a claim."),
                ("Does a personal umbrella cover my business?", 'No. A personal umbrella does not cover business activities. A business needs its own liability coverage. See <a href="business-insurance.html">business insurance</a>.'),
                ("How much umbrella coverage do I need?", "Enough to cover what a judgment could take: home equity, savings and future wages. Most households start with one layer."),
                ("Do I need to change my auto policy to get one?", "Often, yes. Carriers usually ask for higher liability limits underneath. We price both together so you see one number.")],
    },
}

DEDUCTIBLE_FAQ = [
    ("What is a wind and hail deductible?", "It is the amount you pay on a wind or hail claim before the policy pays. Many Texas home policies set it as a percentage of what the house is insured for, and it is often separate from the deductible for everything else."),
    ("Is the deductible a percentage of the damage or of the house?", "Of the house. A 2% deductible on a house insured for $380,000 is $7,600, whether the repair costs $9,000 or $30,000."),
    ("Do I pay the deductible every time?", "Yes. The deductible applies to each claim. Two storms in one year means two deductibles."),
    ("Can my roofer cover my deductible?", "No. It is illegal to waive a homeowners deductible under Texas law, and your insurance company may ask for proof that you paid it. Walk away from any contractor who offers."),
    ("Should I raise my deductible to lower my premium?", "It can lower the premium. The Texas Department of Insurance notes that moving from a $500 deductible to $1,000 can save as much as 20 percent. Pick a deductible you could pay next week without borrowing."),
]

STORM_STEPS = [
    ("Take pictures and video", "Shoot the roof, gutters, windows, fences and cars before anything is cleaned up or moved."),
    ("Make a list", "Write down the damage inside and outside the house, and to each car."),
    ("Keep the damaged items", "Do not throw anything away until your insurance company says you can."),
    ("Stop more damage", "Remove standing water. Cover broken windows and holes so rain stays out."),
    ("Save every receipt", "Temporary repairs and a hotel stay may be covered. The receipts are how you get paid back."),
    ("Be there for the adjuster", "Walk the property with them and point out what you found."),
    ("Keep a contact list", "Write down the name of everyone you talk to at the insurance company, with the date."),
]
STORM_CONTRACTOR = ["Get more than one written estimate", "Check references, and look the company up", "Never pay in full up front",
                    "Never sign a contract with blank spaces", "Walk away from anyone who offers to waive or absorb your deductible. It is illegal in Texas"]
STORM_DEADLINES = [("Acknowledge your claim", "15 business days", "From the day the company receives it."),
                   ("Accept or reject it", "15 business days", "After the company has everything it asked you for. It can extend this by 45 days if it tells you why."),
                   ("Pay it", "5 business days", "After the company agrees to pay all or part of the claim.")]
STORM_FAQ = [
    ("How big does hail have to be to damage a roof?", "There is no single size. The National Weather Service calls a storm severe once hail reaches one inch across, the size of a quarter. Older shingles can be bruised by smaller stones."),
    ("Should I file a claim for hail damage?", "Compare the repair estimate with your deductible first. If the repair costs less than the deductible, the policy pays nothing. Call us with the estimate and we will do the math before you file."),
    ("Does car insurance cover hail?", "Comprehensive coverage does. Liability alone does not. Your comprehensive deductible comes out first."),
    ("How long does an insurance company have to pay a claim in Texas?", "The company has 15 business days to acknowledge the claim, 15 business days to accept or reject it after it has what it needs, and 5 business days to pay once it agrees. The state can extend these after a weather catastrophe."),
    ("Can a contractor waive my deductible?", "No. It is illegal to waive a homeowners deductible under Texas law."),
]

SWITCH_STEPS = [
    ("Send us your declarations page", "It is the first page or two of your policy. It lists your coverages, limits and deductibles."),
    ("We compare it line by line", "You get your current policy and the options side by side, with every deductible written in dollars."),
    ("You choose", "Keep what you have, change carriers, or change limits. There is no charge for the review."),
    ("We collect the sensitive details by phone", "Driver's license numbers, birth dates and vehicle numbers are taken on a call or through a secure link. They never go through the website form or plain email."),
    ("You sign one form", "It names Sideoats as your agent. We set the new policy to start the day the old one ends, so there is no day without coverage."),
    ("You get your documents", "ID cards, the new declarations page and a one page summary arrive the same day the policy starts."),
]
SWITCH_INFO = [
    ("The website form asks for four things", "A ZIP code, your name, a phone number and an email. That is enough to call you back."),
    ("Sensitive numbers are taken by phone", "Driver's license numbers, birth dates and policy numbers are collected on a call you are expecting, or through a secure link we send during that call."),
    ("We will not ask you to pay by gift card or wire", "Premiums are paid to the insurance company by the methods on its own bill. If a caller using our name asks for anything else, hang up and call the office."),
    ("You can ask what we hold", "Call and we will tell you what is in your file, who it was shared with, and why."),
]
SWITCH_FAQ = [
    ("Will I have a gap in coverage if I switch?", "No. We set the new policy to start on the same day the old one ends, and we confirm the old policy's cancellation in writing."),
    ("Do I have to wait for my renewal date?", "No. You can change at any time. The old company refunds the unused part of what you paid, though some charge a small fee for cancelling early."),
    ("What do you need from me to quote?", "Your current declarations page. It tells us more than a form could, and it lets us quote the same coverage so the comparison is fair."),
    ("Does it cost anything to have you review my policy?", "No. The review is free whether you switch or stay."),
]

ABOUT_ROWS = [
    ("We read the policy you already have", "The first meeting starts with your declarations page, and every deductible gets written in dollars."),
    ("We work for you, across several carriers", "An independent agency is not tied to one insurance company, so your policy can be placed where it fits."),
    ("We do the math before you file", "After a storm we compare the repair estimate with your deductible, so you know whether a claim pays."),
    ("We check every renewal", "If the premium jumps, you hear from us with the reason and the options before the bill is due."),
]
ABOUT_FAQ = [
    ("Who owns Sideoats?", "Rosalind Ibarra, who opened the agency in 2011 after twelve years as a claims adjuster. It is independent and locally owned."),
    ("Where does the name come from?", "Sideoats grama is the state grass of Texas. Its seeds hang from one side of the stem, which is the mark in our logo."),
    ("Which areas do you serve?", 'All of Tarrant County, with most of our clients in Fort Worth. We have pages for <a href="fairmount.html">Fairmount</a>, <a href="arlington-heights.html">Arlington Heights</a> and <a href="benbrook.html">Benbrook</a>.'),
    ("How do I check your license?", f'Call the Texas Department of Insurance help line at <a href="tel:{TDI["tel"]}">{TDI["phone"]}</a> or use the agent lookup on its website. On a live site, our license number would be printed in the footer.'),
]

AREA_PAGES = {
    "fairmount": {
        "title": "Home Insurance in Fairmount, Fort Worth | Sideoats",
        "desc": "Insurance for Fairmount homes in Fort Worth: replacement cost on houses built from 1905 to 1920, roof claims in a historic district, and hail deductibles.",
        "h1": "Insurance for Fairmount homes",
        "lede": "Fairmount is next door to our office, and most of its houses are older than any policy form in use today.",
        "fig": ("When Fairmount's building boom began", "1905", "The largest concentration of houses in the district dates from 1905 to 1920. Rebuilding one costs more than its age suggests."),
        "body_title": "What should a Fairmount homeowner know?",
        "body": ["Fairmount was developed as a middle class neighborhood between 1890 and 1938 and covers about 375 acres. Wood frame bungalows are the most common house, with Four Squares scattered through the district, and it is listed on the National Register of Historic Places.",
                 "For insurance, age changes two things. Rebuilding a 1915 bungalow with matching materials and trim costs more than rebuilding a newer house of the same size, so the dwelling limit needs a careful look. Carriers also ask about the wiring, the plumbing and the roof before they quote.",
                 "The city publishes design guidelines for the district that cover roofing, windows and siding. Check them before a roof claim turns into a roof replacement."],
        "notes": [("Original siding, trim and porches", "We check that the dwelling limit matches the cost to rebuild, which is separate from the sale price"),
                  ("Wiring and plumbing of mixed ages", "Carriers ask. We find the ones that write older homes and tell you what they will want to see"),
                  ("Roofs in a historic district", "We read the roof section with you: replacement cost or actual cash value, and the hail deductible in dollars")],
        "img": ("bungalow", "A restored craftsman bungalow in Fort Worth with a wide front porch, brick piers and a new dark shingle roof under a live oak"),
        "faq": [("Does an older house cost more to insure?", "Often, because it costs more to rebuild and carriers look closely at wiring, plumbing and roofs. Updates you can document help."),
                ("What is replacement cost on a historic home?", "It is what it would cost to rebuild the house at current prices. On a house with original trim and materials, that is usually higher than a standard estimate assumes."),
                ("Do I need approval to replace my roof in Fairmount?", "The district has design guidelines that cover roofing. Ask the city's historic preservation office before work starts.")],
    },
    "arlington-heights": {
        "title": "Insurance in Arlington Heights, Fort Worth | Sideoats",
        "desc": "Home and auto insurance for Arlington Heights in Fort Worth: older homes under big trees, hail deductibles in dollars, and what a policy pays when a limb falls.",
        "h1": "Insurance for Arlington Heights",
        "lede": "Arlington Heights grew up along a brick boulevard, under trees that are now taller than the houses.",
        "fig": ("When Camp Bowie Boulevard got its brick", "1927", "The Thurber brick was laid in 1927. The neighborhood grew up around the boulevard, and many of its houses date from the same decades."),
        "body_title": "What should an Arlington Heights homeowner know?",
        "body": ["Camp Bowie Boulevard was first called Arlington Heights Boulevard. It was renamed in 1919 for Camp Bowie, the World War I army training camp that covered the area, and it was paved with Thurber brick in 1927.",
                 "Big trees are the thing we talk about most here. Most home policies do not cover wind or hail damage to the trees themselves. What a falling limb does to the house is a different question, and it is the one to ask before storm season.",
                 "Cars parked on the street or under those trees are exposed to hail. Liability coverage alone pays nothing for hail dents. That takes comprehensive coverage."],
        "notes": [("Mature trees over older roofs", "We explain what the policy pays when a limb comes down, and what it leaves out"),
                  ("Houses from the 1920s and 1930s", "We compare the dwelling limit with the cost to rebuild"),
                  ("Cars parked outside in hail season", "We check for comprehensive coverage and put its deductible in dollars")],
        "faq": [("Does home insurance cover my trees?", "Most policies do not cover wind or hail damage to trees. Ask us what yours pays when a tree or a limb damages the house."),
                ("Does my auto policy cover hail?", "Only with comprehensive coverage. The comprehensive deductible comes out first."),
                ("How far is Sideoats from Arlington Heights?", "A short drive. The office is on Magnolia Avenue in the Near Southside, and we also come to you.")],
    },
    "benbrook": {
        "title": "Insurance in Benbrook, TX | Sideoats Insurance Agency",
        "desc": "Home, flood and auto insurance for Benbrook, Texas from an independent Fort Worth agency. Flood maps checked first, and hail deductibles in dollars.",
        "h1": "Insurance for Benbrook",
        "lede": "Benbrook sits beside a lake that was built to hold back floodwater, so water is the first thing we ask about here.",
        "fig": ("When Benbrook Lake began to fill", "1952", "The Corps of Engineers built the dam on the Clear Fork of the Trinity River for flood control. The gates closed in September 1952."),
        "body_title": "What should a Benbrook homeowner know?",
        "body": ["Benbrook Lake is on the Clear Fork of the Trinity River, about ten miles southwest of the center of Fort Worth. The U.S. Army Corps of Engineers owns and operates the lake and the dam. Construction began in 1947.",
                 "The dam holds back floodwater from heavy rain to protect the land downstream. Houses near the lake, and along the creeks that feed it, are the ones we check against the flood map first. A home policy does not cover flooding, and most flood policies take 30 days to start.",
                 "Benbrook gets the same spring hail as the rest of Tarrant County, so the wind and hail deductible gets worked out in dollars here too."],
        "notes": [("Homes near the lake and its creeks", "We look up the flood zone and price flood coverage with the 30 day wait in mind"),
                  ("Spring hail", "We put the wind and hail deductible in dollars and compare it with a roof estimate"),
                  ("Boats and trailers", "We check what your home and auto policies already cover, and add a policy where they stop")],
        "img": ("flood-street", "A residential street in Texas under brown flood water after heavy rain, with the water reaching the front lawns of brick houses"),
        "faq": [("Do I need flood insurance in Benbrook?", "It depends on the address. If the house is in a mapped high risk zone and has a mortgage, the lender will ask for it. We look up the zone before quoting."),
                ("How long does flood insurance take to start?", "Most flood policies have a 30 day waiting period."),
                ("Is Benbrook part of Fort Worth?", "Benbrook is its own city in Tarrant County, southwest of Fort Worth. We write policies there every week.")],
    },
}

PRIVACY = [
    ("What this website collects", ["The quote form asks for a ZIP code, your name, a phone number, an email and what you want covered. It does not ask for policy numbers, driver's license numbers, birth dates or payment details.",
                                    "On this demo site the form does not send anything. On a live site, a request would go to the agency's office only."]),
    ("How sensitive details are collected", ["An insurance quote needs driver's license numbers, birth dates and vehicle numbers. We take those by phone on a call you are expecting, or through a secure link we send during that call. We do not take them through this website or plain email."]),
    ("Who sees your information", ["The agents working on your quote, and the insurance companies you ask us to quote with. We share what a carrier needs to price the policy and nothing more.",
                                   "You can call and ask what is in your file, who received it, and why."]),
    ("Payments", ["Premiums are paid to the insurance company by the methods on its own bill. We will never ask you to pay by gift card, wire transfer or a payment app. If someone using our name asks, hang up and call the office."]),
    ("Cookies and tracking", ["This website does not use advertising trackers. It loads its typeface from Google Fonts, and that is the only outside service a visit touches."]),
]
