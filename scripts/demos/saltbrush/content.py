"""Copy for the Saltbrush Pool Care demo. Plain strings and tuples only."""

REVIEWS = [
    ("The report lands on my phone before the truck has left the street. Chlorine, pH, a photo of the pool, and a note that the gate latched behind them. I stopped wondering whether anyone came.",
     "Priya N.", "Arcadia"),
    ("We bought a house with a pool the color of pea soup. Wendell gave us a written price on the first visit, and five days later the kids were swimming. The price on the invoice matched the one on the quote.",
     "Marcus and Dee L.", "Ahwatukee"),
    ("After the big dust storm in August they were here the next morning without me calling. Same technician as always. She emptied the baskets twice, cleaned the filter and left the pool blue by the weekend.",
     "Helen T.", "Tempe"),
]

HOME_FAQ = [
    ("How much does weekly pool service cost in Phoenix?",
     "Our weekly service is $155 a month for a standard residential pool, with chemicals included. Pools over 20,000 gallons, pools with an attached spa and pools under heavy tree cover are quoted individually. The full list is on the <a href=\"pricing.html\">pricing page</a>."),
    ("Do I get the same technician every week?",
     "Yes. Each pool is assigned to one technician and one route day. When your technician is on vacation, the service manager tells you who is covering and that person reads your pool's notes before they arrive."),
    ("How do I know the pool was serviced?",
     "Every visit ends with a report sent to your phone and email: the time we arrived and left, six water readings, what we added, a photo of the pool and a line confirming the gate latched. Read more about <a href=\"service-reports.html\">the weekly report</a>."),
    ("Do you work through the summer and the monsoon?",
     "We work all year. Routes start at 6 AM in summer so the work is done before the worst heat. After a dust storm, weekly customers get a cleanup visit on the next route day or sooner. See <a href=\"monsoon-pool-care.html\">monsoon and dust storm care</a>."),
    ("Are you licensed to repair pool equipment?",
     "Yes. Saltbrush holds an Arizona Registrar of Contractors R-6 license, the residential classification for swimming pool service and repair. It covers service and minor repair of pools and their accessories. It does not cover full replastering or new construction, and we refer those out."),
    ("Which parts of the Valley do you serve?",
     "Central Phoenix, <a href=\"arcadia.html\">Arcadia</a>, <a href=\"ahwatukee.html\">Ahwatukee</a> and <a href=\"tempe.html\">Tempe</a>. We keep routes tight on purpose, because a technician who drives less has more time at each pool."),
]

SEASONS = [
    ("Winter", "December to February", "Cooler water needs less chlorine. Citrus leaves and winter rye clippings fill the baskets.", "Shorter pump schedule, filter inspection, and the best months for a drain and refill."),
    ("Spring", "March to May", "Water warms, pollen and palo verde blossoms coat the surface, and algae wakes up.", "Raise the pump hours, brush every wall weekly, and clean the filter before summer."),
    ("Summer", "June to mid September", "Water runs warm for months, sun burns off chlorine by afternoon, and the pool can lose about a quarter inch of water a day.", "Routes from 6 AM, stabilizer checked monthly, water level and autofill checked every visit."),
    ("Monsoon", "June 15 to September 30", "Dust storms drop fine silt into the water and rain throws the chemistry off overnight.", "Storm cleanup visits, extra filter cleanings, and phosphate checks after each big storm."),
    ("Fall", "October and November", "The heat breaks, swimmers thin out, and a summer of hard tap water shows up as scale on the tile.", "Calcium and stabilizer review, tile line cleaning, and repair work that waited for cooler weather."),
]

WORRIES = [
    ("I never know if anyone came.", "Every visit sends a report with arrival and departure times, six readings and a photo of your pool. If we could not get in the gate, the report says that too, with the time we tried."),
    ("My last company sent someone new every month.", "One technician owns your pool and your route day. They keep notes on your equipment, your dog and the side of the yard the wind fills with leaves."),
    ("I'm worried about a surprise bill.", "Chemicals are included in weekly service. Repairs get a written price before any work starts, and you approve it from your phone. Nothing is added on site without asking you."),
]

VISIT_STEPS = [
    ("Test the water", "Free chlorine, pH, alkalinity, calcium, stabilizer and salt, every week, with a drop test kit."),
    ("Balance it", "We add what the readings call for and write down how much. Chemicals are included in the monthly price."),
    ("Brush walls, steps and tile", "Algae starts on surfaces before you can see it in the water. Brushing is what keeps it from taking hold."),
    ("Skim and empty baskets", "Surface, skimmer basket, pump basket and the cleaner bag, so the pump can move water."),
    ("Check the equipment", "Pump, filter pressure, salt cell, timers and the autofill. A pressure reading is logged every visit."),
    ("Close the gate and report", "We pull the gate shut, check that it latched, and send the report before we leave the street."),
]

SERVICE_PAGES = {
    "weekly-pool-service": {
        "title": "Weekly Pool Service in Phoenix, AZ | Saltbrush Pool Care",
        "desc": "Weekly pool service in Phoenix for $155 a month with chemicals included. The same technician every week and a water report after every visit.",
        "tag": "Weekly service",
        "h1": 'Weekly pool service, <span class="accent">with the proof sent to your phone.</span>',
        "lede": "One technician, one route day, and a full service visit every week of the year. Chemicals are included, and so is the report that shows what we did.",
        "points": ["$155 a month, chemicals included", "Same technician every week", "Report with a photo after every visit"],
        "included_title": 'What is included <span class="accent">every week?</span>',
        "included": ["Six point water test with a drop kit", "All balancing chemicals, including salt and stabilizer", "Walls, steps and tile line brushed", "Surface skimmed and floor vacuumed as needed", "Skimmer, pump and cleaner baskets emptied", "Filter pressure logged and equipment checked", "Water level and autofill checked", "Gate closed and latched, then the report sent"],
        "body_title": 'Why does a Phoenix pool need <span class="accent">a visit every week?</span>',
        "body": ["Summer sun here burns through chlorine by mid afternoon, and warm water grows algae fast. A pool that looks fine on Monday can be cloudy by Friday in July. A weekly visit catches the drop before it becomes a green pool and a bigger bill.",
                 "Phoenix tap water is hard, and every gallon that evaporates leaves its minerals behind. We track calcium and stabilizer month over month, so we can tell you a season ahead when a partial drain makes sense, and schedule it for the cooler months.",
                 "The visit takes 25 to 35 minutes for most pools. Your technician keeps notes on your equipment and reads the last four reports before they open the gate."],
        "rows_title": "Weekly service prices", "rows_head": ("Pool", "What it covers", "Price"),
        "rows": [("Standard pool, up to 20,000 gallons", "Full weekly visit, chemicals included", "$155 a month"), ("Pool with attached spa", "Pool and spa tested and balanced together", "$175 a month"), ("Large or heavily shaded pool", "Quoted after one look at the yard", "From $185 a month"), ("Chemicals only", "Test and balance weekly, you handle the cleaning", "$95 a month")],
        "faq": [
            ("Do I have to sign a contract?", "No. Weekly service is month to month, billed on the first. You can pause or cancel with a week's notice."),
            ("What if my gate is locked or the dog is out?", "We text you from the driveway and wait a few minutes. If we cannot get in, the report says so with the time, and we come back on the next open route day at no charge the first time."),
            ("Are chemicals included in the price?", "Yes. Chlorine, acid, salt, stabilizer and the other balancing chemicals are included. Specialty treatments such as a phosphate remover after a storm are quoted before we add them."),
            ("Do you service salt water pools?", "Yes. About half the pools on our routes are salt. We test salt every week, inspect the cell monthly, and clean it when scale shows on the plates."),
        ],
    },
    "green-pool-cleanup": {
        "title": "Green Pool Cleanup in Phoenix, AZ | Saltbrush Pool Care",
        "desc": "Green pool cleanup in Phoenix from $295. A written price on the first visit, daily progress reports, and most pools swimmable in three to five days.",
        "tag": "Green pool cleanup",
        "h1": 'From green to swimmable, <span class="accent">with a price in writing first.</span>',
        "lede": "A green pool is an algae bloom, and it responds to chlorine, brushing and a clean filter in that order. We give you one price on the first visit and a report after each one that follows.",
        "points": ["From $295, quoted on the first visit", "Most pools clear in three to five days", "A report after every visit until it is blue"],
        "included_title": 'What does a cleanup <span class="accent">include?</span>',
        "included": ["Water test to see what the pool needs", "Debris netted out before any chemicals go in", "Chlorine raised and held until the algae is dead", "Every surface brushed on every visit", "Filter cleaned at least once during the cleanup", "Dead algae vacuumed out", "Water balanced for swimming", "A plan to keep it clear afterward"],
        "body_title": 'Should a green pool be drained <span class="accent">or treated?</span>',
        "body": ["Most green pools can be treated without draining. We drain only when the water itself is the problem: stabilizer or calcium so high that chlorine cannot do its job, or debris so thick that treating it would cost more than fresh water.",
                 "When a drain is the right call, we tell you why and schedule it for a cool morning. An empty plaster pool should never sit in summer sun, so in the hottest months we use a partial drain or wait for a cooler stretch.",
                 "How long it takes depends on how long the pool sat. A pool that turned last week is usually clear in three days. One that sat through a summer can take a week and two filter cleanings."],
        "rows_title": "Green pool cleanup prices", "rows_head": ("Condition", "What it usually takes", "Price"),
        "rows": [("Light green, floor visible", "Two or three visits", "From $295"), ("Dark green, floor hidden", "Four or five visits and a filter clean", "From $445"), ("Black or full of debris", "Quoted on site, may need a drain", "From $650"), ("Drain and refill coordination", "Pump out, pressure rinse, refill and startup", "From $350, plus water")],
        "faq": [
            ("How fast can you start?", "Usually within two business days. If the pool is behind a home that is for sale or about to close, tell us the date and we plan around it."),
            ("Is a green pool a health problem?", "Standing green water can breed mosquitoes, and Maricopa County takes complaints about green pools seriously. Clearing it protects your neighbors as well as your swimmers."),
            ("Will it turn green again?", "It can if nothing changes. Algae returns when chlorine drops or the filter stops moving water. Weekly service after a cleanup is the most reliable way to keep it blue."),
            ("Can I swim during the cleanup?", "No. Chlorine is held well above swimming level while the algae dies. Your final report tells you when the readings are back in range."),
        ],
    },
    "equipment-repair": {
        "title": "Pool Equipment Repair in Phoenix, AZ | Saltbrush Pool Care",
        "desc": "Pool pump, filter, salt cell and automation repair in Phoenix. An $89 diagnosis credited to the repair, and a written price before any work starts.",
        "tag": "Equipment repair",
        "h1": 'Pool equipment repair, <span class="accent">priced before the wrench comes out.</span>',
        "lede": "Pumps, filters, salt systems, timers, valves and leaks at the pad. We find the cause, write down the price, and wait for your yes.",
        "points": ["$89 diagnosis, credited to the repair", "Written price before any work", "Arizona ROC R-6 licensed"],
        "included_title": 'What do we <span class="accent">repair and replace?</span>',
        "included": ["Pump motors, seals and full variable speed pump replacements", "Cartridge, D.E. and sand filters, grids and valves", "Salt chlorine generators and cells", "Timers, automation panels and actuators", "Leaks at unions, valves and equipment plumbing", "Pool cleaners and their booster pumps", "Autofill valves and skimmer parts", "Heater diagnosis and service on the water side"],
        "body_title": 'What does an R-6 license <span class="accent">cover, and what does it not?</span>',
        "body": ["Arizona's R-6 classification lets a contractor service and perform minor repair of residential pools and accessories. It excludes plumbing connections to a drinking water line, gas lines, gas chlorine systems, and electrical work beyond the first disconnect. It also does not allow a complete replacement of a plaster or pebble interior or a deck.",
                 "So we replace your pump, filter and salt system, and we stop where the license stops. A new gas line for a heater goes to a licensed plumber. A resurfacing job goes to a pool builder. We tell you which trade you need and what to ask them.",
                 "Every repair starts with a diagnosis visit. You get photos of the failed part, the price for the fix and, when it applies, the price to replace instead. The old part stays at your house until you have seen it."],
        "rows_title": "Sample repair prices", "rows_head": ("Repair", "What it covers", "Price"),
        "rows": [("Diagnosis visit", "Find the cause, photos and a written price", "$89, credited to the repair"), ("Pump seal or motor bearing", "Parts and labor", "From $240"), ("Variable speed pump replacement", "New pump installed and programmed", "From $1,450"), ("Salt cell cleaning", "Acid wash and inspection of the plates", "$65"), ("Salt cell replacement", "New cell matched to your system", "From $780"), ("Leak at the equipment pad", "Unions, valves and fittings", "From $160")],
        "faq": [
            ("Do you repair equipment you do not service weekly?", "Yes. Repair is open to any pool in our service area. Weekly customers get the diagnosis fee waived."),
            ("How long does a pump replacement take?", "About two hours for a like for like swap. We program the new pump's schedule before we leave and explain it on the report."),
            ("Why is everyone installing variable speed pumps?", "Federal efficiency rules that took effect in 2021 mean most new pool pumps sold are variable speed. They run longer at low speed, which uses far less electricity and is quieter."),
            ("Do you warranty your repairs?", "Labor is covered for one year. Parts carry the manufacturer's warranty, and we handle the claim if a part fails."),
        ],
    },
    "filter-cleaning": {
        "title": "Pool Filter Cleaning in Phoenix, AZ | Saltbrush Pool Care",
        "desc": "Cartridge, D.E. and sand filter cleaning in Phoenix from $95. Filters taken apart, cleaned and inspected, with photos of what we found inside.",
        "tag": "Filter cleaning",
        "h1": 'Filter cleaning, <span class="accent">with photos of what was inside.</span>',
        "lede": "The filter is where a dust storm ends up. We take it apart, clean every element, check for cracks and tears, and show you what we found.",
        "points": ["From $95 per cleaning", "Elements inspected for damage", "Clean starting pressure recorded"],
        "included_title": 'What happens during <span class="accent">a filter cleaning?</span>',
        "included": ["Pump shut off and tank pressure released safely", "Filter opened and elements or grids removed", "Each element rinsed from the top down", "Pleats, bands and manifolds checked for tears and cracks", "Tank o-ring cleaned and lubricated", "D.E. recharged to the manufacturer's amount", "System restarted and checked for leaks", "Clean pressure written on the report"],
        "body_title": 'How often should a filter be cleaned <span class="accent">in Phoenix?</span>',
        "body": ["A good rule is to clean the filter when its pressure reads 8 to 10 psi above the clean starting pressure. That is why we log the pressure on every weekly report. The number tells you when, and a calendar only guesses.",
                 "In practice, most cartridge filters here need cleaning three or four times a year, and more often during the monsoon. One large dust storm can load a clean filter in a day.",
                 "A filter that is never cleaned makes the pump work harder, moves less water and lets algae start. A filter with a torn element sends dirt straight back to the pool. Both are cheap to prevent."],
        "rows_title": "Filter cleaning prices", "rows_head": ("Filter type", "What it covers", "Price"),
        "rows": [("Cartridge, up to four elements", "Disassembly, rinse, inspection, restart", "$95"), ("D.E. filter", "Grids cleaned and inspected, fresh D.E.", "$125"), ("Sand filter", "Backwash, rinse and sand inspection", "$85"), ("Replacement cartridge set", "Four elements, installed", "From $380"), ("After storm cleaning, weekly customers", "Same work, storm rate", "$75")],
        "faq": [
            ("How do I know which filter I have?", "A cartridge filter is a tall tank with a clamp or locking ring. A D.E. filter has a backwash valve and uses white powder. A sand filter is a round tank with a valve on top or on the side. Send us a photo and we will tell you."),
            ("How long do cartridges last?", "Three to five years for most pools here. Hard water and heavy dust shorten that. We tell you when the pleats are worn so you can plan the cost."),
            ("Is D.E. powder safe?", "It should be handled with a mask and never dumped where it can blow around. Many Valley cities also have rules about where backwash water can go, so we collect and dispose of it properly."),
            ("Can you clean the filter on a regular weekly visit?", "Yes. Weekly customers can add a cleaning to any visit, and we suggest one when the pressure log says it is time."),
        ],
    },
}

SERVICES_FAQ = [
    ("Which service do I need if I just bought a house with a pool?", "Start with one visit. We test the water, look over the equipment, and tell you what the pool needs now and what can wait. Most new owners go on weekly service and add a filter cleaning in the first month."),
    ("Can you take over from another pool company?", "Yes. We ask for a photo of the equipment pad and your last few readings if you have them. Your first visit is longer so the technician can learn the pool."),
    ("Do you build or resurface pools?", "No. We are a service and repair company. For new construction, replastering or deck work we point you to a licensed pool builder."),
    ("Do you service commercial or community pools?", "No. Public and semi public pools in Maricopa County follow a separate set of health rules. We work on residential pools only."),
]

STORM_BEFORE = [
    "Lower or tie down umbrellas, cushions and pool toys. Whatever is loose ends up in the water.",
    "Leave the water level alone. A full pool is heavier and safer in the ground than a low one.",
    "Turn off the pump if lightning is close, and never touch the equipment during a storm.",
    "Do not cover the pool. A cover in a dust storm becomes a sail and then a mess.",
]
STORM_AFTER = [
    ("Net out the large debris", "Leaves, palm fronds, seed pods and trash come out first, before they sink and stain."),
    ("Empty the baskets", "Skimmer and pump baskets fill fast. Check them more than once during the cleanup."),
    ("Brush everything", "Walls, steps and floor, from the waterline down, to lift the silt off the surface."),
    ("Vacuum slowly", "Fast vacuuming stirs the dust back up. Slow passes pick it up."),
    ("Clean the filter", "When pressure reads 8 to 10 psi above the clean number, the filter is full and needs cleaning."),
    ("Test the water", "Dust and rain carry in phosphates and change pH and alkalinity."),
    ("Shock if the test calls for it", "Extra chlorine deals with what the storm brought before algae can use it."),
    ("Run the pump until it clears", "After a large storm this can take a day or more and a second filter cleaning."),
]
STORM_TABLE = [
    ("Brown or tan water", "Fine silt is suspended in the pool", "Brushing, slow vacuuming and a filter cleaning"),
    ("Cloudy water a day later", "The filter is loaded and chlorine is low", "Clean the filter again and raise chlorine"),
    ("Green tint within a week", "Phosphates from dust fed an algae bloom", "Shock, brush, and a phosphate treatment"),
    ("Pump running loud or dry", "Baskets are packed or the water level dropped", "Empty baskets, check the level, then restart"),
    ("Water level higher than the tile", "Heavy rain overfilled the pool", "Pump down to mid tile, then rebalance"),
]
MONSOON_FAQ = [
    ("When is monsoon season in Phoenix?", "The National Weather Service defines the Arizona monsoon as June 15 through September 30 each year. Dust storms and heavy rain are most common in July and August."),
    ("What is a haboob?", "A haboob is a wall of dust pushed ahead of a thunderstorm's outflow winds. It can be thousands of feet tall and miles wide, and it drops a layer of fine silt on everything, including the bottom of your pool."),
    ("Should I run my pump during a dust storm?", "If there is lightning, leave the equipment alone. Otherwise the pump can stay on its schedule. What matters more is emptying the baskets and cleaning the filter afterward."),
    ("How soon after a storm will you come?", "Weekly customers get a cleanup visit on their next route day, or sooner when a storm is large enough that we add a storm day. You get a text the night before."),
    ("Does rain hurt pool water?", "Rain is slightly acidic and dilutes the water, so pH, alkalinity and chlorine can all drop after a heavy storm. A test the next day tells us what to add."),
]

BARRIER_TABLE = [
    ("Who the law applies to", "A residence with a pool where one or more children under six years of age live"),
    ("Fence or wall height", "At least 5 feet"),
    ("Openings in the barrier", "Nothing a 4 inch sphere can pass through"),
    ("Gate direction", "Opens outward, away from the pool"),
    ("Gate hardware", "Self closing and self latching"),
    ("Latch height", "At least 54 inches above the ground"),
    ("Distance from the water", "Barrier at least 20 inches from the water's edge"),
    ("When the house is one side of the enclosure", "Options include a 4 foot barrier between house and pool, or self latching doors with latches 54 inches up and windows that open no more than 4 inches"),
]
SAFETY_FAQ = [
    ("Does Arizona require a pool fence?", "State law, A.R.S. 36-1681, requires an enclosure around a pool at a residence where a child under six lives. Many Valley cities have their own pool barrier codes that add to the state rule, so check with your city before you build or change a fence."),
    ("How tall does a pool fence have to be in Arizona?", "The state statute sets the height at 5 feet or more for a pool enclosure, with no opening that a 4 inch sphere can pass through."),
    ("Does Saltbrush install pool fences?", "No. Barrier installation falls outside a pool service license. What we do is check your gate on every visit and tell you the same day if it stops closing or latching on its own."),
    ("Is this page legal advice?", "No. It is a plain summary of the state notice for homeowners, checked in October 2026. Your city's building department has the final word for your address."),
]

PRICING_FAQ = [
    ("Why do you publish your prices?", "Because the first question on every call is what it costs. Publishing the numbers saves you a phone call and keeps our quotes consistent from one house to the next."),
    ("Do prices change in summer?", "No. The monthly price is the same all year. Summer uses more chlorine and winter uses less, and the flat price averages that out."),
    ("What is not included in weekly service?", "Filter cleanings, repairs, green pool cleanups and specialty treatments are separate, and each one is quoted in writing before we do it."),
    ("How do I pay?", "By card or bank transfer on the first of the month through the customer portal. We never take card numbers by text or email."),
]

REPORT_ITEMS = [
    ("Arrival and departure times", "Stamped by the technician's phone, so you can see how long the visit took."),
    ("Six water readings", "Free chlorine, pH, alkalinity, calcium, stabilizer and salt, each beside its target range."),
    ("What we added", "The chemical and the amount, so the next technician and the next homeowner both know."),
    ("Filter pressure", "Logged weekly, because the trend tells you when a cleaning is due."),
    ("One photo of the pool", "Taken from the same spot each week. It shows the water and nothing else in your yard."),
    ("Gate confirmation", "A line that says the gate was pulled shut and latched when we left."),
]
REPORT_SECURITY = [
    ("Gate and alarm codes never travel by text", "Codes are collected by phone, stored encrypted, and shown to your technician on route day only. They are never written on a clipboard or left in a group chat."),
    ("Photos show the pool and nothing else", "Technicians frame the water. No photos of the house, your family, or anything through a window. Photos are deleted from the technician's phone once the report uploads."),
    ("Your portal has a second lock", "Reports, invoices and saved payment details sit behind a login with a one time code. A password alone will not open the account."),
    ("We do not sell or share your address", "A list of homes with pools and the days someone is in the yard is sensitive. It stays with us, and only staff who run your route can see it."),
]
REPORT_FAQ = [
    ("How do I receive the report?", "By text and email within a few minutes of the visit ending, with a link to the full history in your portal."),
    ("Can my landlord or property manager get a copy?", "Yes. You can add a second recipient, and you can remove them at any time."),
    ("What if a reading is out of range?", "The report marks it and says what we added to correct it. If the same reading is off two weeks in a row, the service manager calls you with a plan."),
    ("Who can see my gate code?", "Your assigned technician on your route day, and the service manager. Every time a code is viewed, the system logs who looked and when."),
]

ABOUT_FAQ = [
    ("How long has Saltbrush been in business?", "Since 2014. We started with forty pools in central Phoenix and grew one route at a time."),
    ("How many pools does each technician service?", "We cap routes so a technician has about half an hour at each pool. A route that is too long is how brushing gets skipped."),
    ("Are your technicians employees?", "Yes. Every technician is an employee who is trained, background checked and insured. We do not hand routes to subcontractors."),
    ("What does the name mean?", "Saltbush is a tough desert shrub that grows all over the Valley, and salt and a brush are two things a pool technician uses every day. The name is a nod to both."),
]

AREA_PAGES = {
    "arcadia": {
        "title": "Pool Service in Arcadia, Phoenix AZ | Saltbrush Pool Care",
        "desc": "Weekly pool service in Arcadia, Phoenix 85018. Older diving pools, citrus leaves and irrigated lots are what our Tuesday and Friday routes know best.",
        "h1": 'Pool service in <span class="accent">Arcadia.</span>',
        "lede": "Arcadia grew out of citrus groves below Camelback Mountain, and many of its pools are older than the people swimming in them. Our Tuesday and Friday routes run here.",
        "points": ["Routes on Tuesdays and Fridays", "ZIP 85018", "Older pools and citrus lots are our specialty"],
        "body_title": 'What makes an Arcadia pool <span class="accent">different?</span>',
        "body": ["Many Arcadia lots still have orange and grapefruit trees from the groves that were here first. Blossoms in spring and leaves in winter go straight into the skimmer, so baskets here need attention every visit and sometimes between visits.",
                 "A lot of these homes are flood irrigated, with grass right up to the deck. Irrigation days can push silt and fertilizer toward the pool, and fertilizer feeds algae. We note your irrigation schedule and watch phosphates more closely than we would on a gravel lot.",
                 "Arcadia also has some of the Valley's older pools: deep ends built for diving boards, original plaster, and plumbing that predates the equipment bolted to it. We keep photos and notes on each pad so a repair does not start from zero."],
        "notes": [("Citrus debris", "Baskets emptied every visit, and a leaf canister suggested for heavy trees"), ("Irrigation runoff", "Phosphates checked monthly on irrigated lots"), ("Older plaster", "Calcium and pH kept steady to protect the surface"), ("Deep diving pools", "More water to balance, quoted by volume")],
        "faq": [
            ("Which days do you service Arcadia?", "Tuesdays and Fridays. New customers are placed on the day that keeps their street grouped with the pools around it."),
            ("My pool has a lot of trees over it. Does that cost more?", "Sometimes. Heavy tree cover means longer visits. We look at the yard once and give you a single monthly price that does not change with the season."),
            ("Can you work on older equipment?", "Yes. We service plenty of pads that have been rebuilt in stages. When a part is no longer made, we tell you your options before anything fails."),
        ],
    },
    "ahwatukee": {
        "title": "Pool Service in Ahwatukee, Phoenix AZ | Saltbrush Pool Care",
        "desc": "Weekly pool service in Ahwatukee, Phoenix 85044, 85045 and 85048. Pebble pools, attached spas and South Mountain dust on our Monday and Thursday routes.",
        "h1": 'Pool service in <span class="accent">Ahwatukee.</span>',
        "lede": "Ahwatukee sits between South Mountain and the freeways, and when a storm comes over the mountain the dust lands here first. Our Monday and Thursday routes run through all three ZIP codes.",
        "points": ["Routes on Mondays and Thursdays", "ZIP 85044, 85045 and 85048", "Pebble pools and attached spas"],
        "body_title": 'What makes an Ahwatukee pool <span class="accent">different?</span>',
        "body": ["Most Ahwatukee pools were built from the 1980s on, so pebble finishes, raised spas and water features are common. A spa that shares water with the pool changes how the chemistry behaves, and we test with the spa running.",
                 "The foothills back onto South Mountain Park and Preserve. Open desert on one side of the wall means more dust, more seed pods from mesquite and palo verde, and a filter that fills faster than one a few miles north.",
                 "Homes here often sit in an association with rules about equipment noise and what can be seen from the street. We keep pump schedules inside quiet hours and leave the side yard the way we found it."],
        "notes": [("Desert dust", "Filter pressure watched closely, with cleanings ahead of monsoon"), ("Attached spas", "Spa and pool tested together, spillway brushed"), ("Pebble finishes", "Calcium held in range to limit scale on the pebble"), ("Association rules", "Pump schedules kept inside quiet hours")],
        "faq": [
            ("Which days do you service Ahwatukee?", "Mondays and Thursdays, covering 85044, 85045 and 85048."),
            ("Do you clean pebble finish pools differently?", "The steps are the same. We use a stiffer brush on pebble and pay extra attention to calcium, because scale on a pebble finish is hard to remove once it sets."),
            ("How quickly do you come after a dust storm?", "On your next route day, or sooner when we add a storm day. Ahwatukee is usually first on that list because the foothills take the most dust."),
        ],
    },
    "tempe": {
        "title": "Pool Service in Tempe, AZ | Saltbrush Pool Care",
        "desc": "Weekly pool service in Tempe, AZ 85281 to 85284. Mid century pools, rental homes near campus and a report your landlord or tenant can also receive.",
        "h1": 'Pool service in <span class="accent">Tempe.</span>',
        "lede": "Tempe's neighborhoods south of Town Lake are full of block homes from the 1950s through the 1970s, many with their first pool still in the ground. Our Wednesday route runs here.",
        "points": ["Route on Wednesdays", "ZIP 85281 to 85284", "Rentals and owner occupied homes"],
        "body_title": 'What makes a Tempe pool <span class="accent">different?</span>',
        "body": ["A lot of Tempe pools belong to rental homes. That means the person swimming and the person paying are often two different people, and neither one wants a surprise. Our report can go to both, so the owner sees the readings and the tenant sees that the gate latched.",
                 "Older pools here tend to be smaller, with simple equipment and single speed pumps near the end of their life. We keep them running, and we tell you ahead of time what a replacement will cost so it can go in a budget.",
                 "Tall palms are everywhere, and they drop fronds and seed strands for months. We plan for fuller baskets in late summer and suggest a trim before monsoon when a palm hangs over the water."],
        "notes": [("Rental homes", "Reports sent to owner and tenant, with separate logins"), ("Older pumps", "Replacement cost shared before the pump fails"), ("Palm debris", "Baskets and cleaner bags emptied every visit"), ("Small pools", "Less water changes faster, so testing matters more")],
        "faq": [
            ("Which day do you service Tempe?", "Wednesdays, across 85281, 85282, 85283 and 85284."),
            ("Can the owner and the tenant both get reports?", "Yes. Each has a separate login, and the owner decides who is on the account."),
            ("I manage several rentals. Can you service all of them?", "Yes, if they are inside our Tempe route. Each home gets its own report history, and you see them all in one portal."),
        ],
    },
}

PRIVACY = [
    ("What this website collects", ["This demo site has no trackers, no advertising pixels and no analytics cookies. The quote form on a live Saltbrush site would collect your name, phone, email, ZIP code and what you need, and nothing more.", "This is a demonstration. Nothing you type into a form on this site is sent or stored."]),
    ("Gate codes, alarm codes and keys", ["We never ask for a gate code, alarm code or lockbox code by email, text or web form. Codes are collected by phone once you are a customer, stored encrypted, and shown to your assigned technician on your route day only.", "Every view of a code is logged with the name of the person who looked and the time."]),
    ("Photos of your property", ["Each weekly report includes one photo of the pool. Technicians are trained to frame the water and the equipment only. Photos are deleted from the technician's phone once the report uploads."]),
    ("Your account", ["Reports, invoices and payment details live in a customer portal protected by a password and a one time code. Card numbers are held by the payment processor and never by Saltbrush staff."]),
    ("What we will never do", ["We will never sell or rent a customer list. We will never call you to ask for a full card number. We will never send a technician you were not told about. If a message asks for any of those things, call the office before you answer it."]),
    ("Questions", ["Call the office on the number at the top of this page and ask for the service manager."]),
]
