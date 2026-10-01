"""Copy for the Tessel Dental demo. Prices and reviews are demo content."""

REVIEWS = [
    ("I hadn't been to a dentist in six years and told them so at the desk. Nobody lectured me. Dr. Sethuraman walked me through the x-rays and we made a plan I could afford.", "Jordan M.", "South End"),
    ("Cracked a molar on a Friday morning and was in the chair by noon. They told me the price before they started and it matched the bill.", "Alicia R.", "Dilworth"),
    ("My daughter asks when she gets to go back. That alone tells you how they treat kids here.", "Sam K.", "Ballantyne"),
    ("Dr. Marchbanks showed me the 3D scan of my implant site and answered every question. Six months later it feels like my own tooth.", "Gerald T.", "Piper Glen"),
    ("Booked online at 9 PM, got a text the next morning, and was seen that week. The light rail drops me two minutes away.", "Priya D.", "Wilmore"),
    ("They checked my Delta Dental benefits before my first visit, so I knew my cost ahead of time. That's never happened to me before.", "Marcus L.", "Myers Park"),
]

HOME_FAQ = [
    ("Are you taking new patients?", "Yes, at both offices. Most new patients are seen within a week, and emergency visits are same day."),
    ("Do you take my insurance?", "We're in network with most PPO plans, including Delta Dental, Cigna, MetLife, Aetna, Guardian, Blue Cross NC Dental Blue, United Concordia and Ameritas. Send us your plan details when you book and we'll check your benefits before you come in."),
    ("What if I don't have dental insurance?", "Our membership plan covers two cleanings and exams, all routine x-rays and one emergency exam a year for $32 a month, plus 15% off other treatment. Self pay prices are listed on our insurance page."),
    ("I'm nervous about the dentist. Can you help?", "Tell us when you book. We'll give you extra time, explain each step before we do it, and stop whenever you raise a hand. Nitrous oxide is available for longer visits."),
    ("Which office should I choose?", "South End is easiest by light rail and from Dilworth, Myers Park and uptown. Ballantyne is easiest from south Charlotte, Marvin and Fort Mill, with free parking at the door. Your records are shared, so you can visit either."),
]

SERVICES_FAQ = [
    ("How often should I get a cleaning?", "Twice a year works for most people. If you have gum disease or a history of heavy buildup, we may suggest every three or four months for a while."),
    ("Do you see kids?", "Yes. We see children from their first tooth on, and many families book back to back visits so parents and kids are done in one trip."),
    ("Will you tell me the cost before treatment?", "Always. You get a written estimate with your insurance share and your share before any treatment beyond the exam."),
]

SERVICE_PAGES = {
    "cleanings-exams": {
        "title": "Teeth Cleaning and Exams in Charlotte, NC | Tessel Dental",
        "desc": "Unhurried cleanings and exams for adults and kids in South End and Ballantyne. Most PPO plans accepted, and a membership plan if you have no insurance.",
        "eyebrow": "Cleanings and exams",
        "h1": 'Cleanings and checkups, <span class="accent">without the rush.</span>',
        "lede": "An hour for new patients and 50 minutes for returning ones, so there's time to talk about what we see and what it means.",
        "points": ["Low dose digital x-rays", "Kids seen from their first tooth", "Benefits checked before you arrive"],
        "alt": "A hygienist cleaning a relaxed patient's teeth in a bright treatment room",
        "intro_h": "What happens at a checkup",
        "steps": [
            ("Catch up", "We ask what's changed since your last visit and anything that's been bothering you."),
            ("X-rays as needed", "Digital x-rays, usually once a year, show what the eye can't see between teeth."),
            ("Cleaning", "Your hygienist removes buildup, polishes, and checks your gums at six points per tooth."),
            ("Exam and plan", "Your dentist checks for decay, cracks and oral cancer signs, then talks through anything worth watching."),
        ],
        "prices": [("New patient visit", "Exam, full x-rays and cleaning", "$289"), ("Returning cleaning and exam", "Includes yearly bitewing x-rays", "$199"),
                   ("Child cleaning and exam", "Ages 12 and under, fluoride included", "$149"), ("Deep cleaning", "Per quarter of the mouth, when gum pockets need it", "$265")],
        "faq": [
            ("How long does a first visit take?", "Plan on about an hour. We take full x-rays, do a complete exam and cleaning, and leave time for questions."),
            ("Is a deep cleaning the same as a regular cleaning?", "No. A deep cleaning, or scaling and root planing, reaches below the gumline when pockets are deeper than 4 millimeters. We'll show you the measurements before recommending it."),
            ("Does Charlotte water have fluoride?", "Yes. Charlotte Water adds fluoride to the public supply, so kids who drink tap water get some protection already. We may still suggest a fluoride varnish at checkups."),
            ("When should my child first see a dentist?", "By their first birthday or within six months of the first tooth. Early visits are short and mostly about getting comfortable."),
        ],
    },
    "cosmetic-dentistry": {
        "title": "Cosmetic Dentist in Charlotte, NC | Tessel Dental",
        "desc": "Teeth whitening, bonding, porcelain veneers and clear aligners at Tessel Dental in Charlotte. Free cosmetic consult with a digital smile preview.",
        "eyebrow": "Cosmetic dentistry",
        "h1": 'A brighter smile that still <span class="accent">looks like you.</span>',
        "lede": "Whitening, bonding, veneers and clear aligners, planned with a digital preview so you see the result before we start.",
        "points": ["Free 30 minute consult", "Digital smile preview", "Monthly payment options"],
        "alt": "A woman laughing on a leafy sidewalk with a natural bright smile",
        "intro_h": "How a cosmetic plan comes together",
        "steps": [
            ("Consult", "You tell us what you'd change. We look at shade, shape, spacing and bite."),
            ("Scan and preview", "A 3D scan builds a preview of the result on screen, so we can adjust before anything is permanent."),
            ("Treatment", "Whitening and bonding often finish in one visit. Veneers and aligners take a few weeks to a few months."),
            ("Follow up", "We check the result, the bite and your comfort, and set a plan to keep it that way."),
        ],
        "prices": [("In office whitening", "One 90 minute visit", "$495"), ("Take home whitening", "Custom trays and gel", "$295"),
                   ("Cosmetic bonding", "Per tooth", "From $295"), ("Porcelain veneers", "Per tooth", "From $1,350"), ("Clear aligners", "Full treatment, with retainers", "From $3,900")],
        "faq": [
            ("Is whitening safe for my enamel?", "Yes, when it's supervised. Professional gels are buffered, and we check for exposed roots or sensitivity before we start."),
            ("How long do veneers last?", "Porcelain veneers commonly last 10 to 15 years with good care. Bonding usually needs a touch up every 5 to 7 years."),
            ("Does insurance cover cosmetic work?", "Usually not, since it's elective. Our membership plan takes 15% off, and monthly payment options are available on approved credit."),
        ],
    },
    "dental-implants": {
        "title": "Dental Implants in Charlotte, NC | Tessel Dental",
        "desc": "Single tooth implants to full arch restorations at Tessel Dental in Charlotte, planned with a 3D scan. Single implant with crown from $4,300.",
        "eyebrow": "Dental implants",
        "h1": 'Replace a missing tooth, <span class="accent">root and all.</span>',
        "lede": "An implant replaces the root as well as the crown, so it chews like a natural tooth and protects the bone around it. Every case starts with a 3D scan.",
        "points": ["3D cone beam scan included", "Placed and restored in house", "Written estimate before you decide"],
        "alt": "A dentist explaining a dental implant model to an older patient at a consultation table",
        "intro_h": "The implant timeline",
        "timeline": [
            ("Consult and 3D scan", "Week 1", "We check bone height, nerve position and your bite, then plan the implant on the scan."),
            ("Implant placement", "Week 2 to 4", "A titanium post is placed under local anesthetic. Most people are back at work the next day."),
            ("Healing", "3 to 6 months", "The bone bonds to the implant. You wear a temporary tooth so nobody sees a gap."),
            ("Final crown", "1 or 2 visits", "We scan, design and fit a porcelain crown matched to the teeth beside it."),
        ],
        "prices": [("Implant consult with 3D scan", "Credited toward treatment", "$195"), ("Single implant with crown", "Post, abutment and porcelain crown", "From $4,300"),
                   ("Bone graft", "When the site needs more bone", "From $650"), ("Implant supported denture", "Per arch, removable", "From $11,500")],
        "faq": [
            ("Am I too old for an implant?", "Age alone isn't a reason to say no. Bone health, gum health and conditions like uncontrolled diabetes matter more, and we check all three at the consult."),
            ("Does getting an implant hurt?", "Placement is done under local anesthetic and most people describe the next few days as sore, like after a tooth extraction. Over the counter pain relief is usually enough."),
            ("Will insurance pay for an implant?", "Many PPO plans now cover part of an implant, often up to the yearly maximum. We send a pre treatment estimate to your plan so you know before you commit."),
            ("How long do implants last?", "The implant itself can last decades with good care. The crown on top may need replacing after 15 years or so."),
        ],
    },
    "emergency-dentist": {
        "title": "Emergency Dentist in Charlotte, NC | Tessel Dental",
        "desc": "Same day emergency dental visits in South End and Ballantyne for tooth pain, broken teeth, swelling and knocked out teeth. Emergency exam with x-ray $119.",
        "eyebrow": "Emergency dentist",
        "h1": 'Tooth pain today? <span class="accent">Be seen today.</span>',
        "lede": "We hold emergency slots every weekday morning at both offices. Call before 11 AM and you'll almost always be seen the same day.",
        "points": ["Emergency exam with x-ray $119", "After hours line to the dentist on call", "Price before treatment, every time"],
        "alt": "A dental assistant handing a cold pack to a young man holding his cheek in the waiting room",
        "intro_h": "What to do right now",
        "now": [
            ("Knocked out tooth", "Hold it by the crown, the part you chew with, and keep your fingers off the root. Rinse it briefly and try to put it back in the socket. If you can't, keep it in milk and call us. The sooner we see you the better, ideally within 30 minutes."),
            ("Broken or chipped tooth", "Rinse with warm water and save any pieces. A cold compress on the cheek helps with swelling."),
            ("Bad toothache", "Floss gently around the tooth in case something is stuck. Don't put aspirin on the gum, which can burn it."),
            ("Swelling in the face or jaw", "Call us right away. Swelling can mean an infection that needs treatment the same day."),
        ],
        "prices": [("Emergency exam with x-ray", "Diagnosis and a written plan", "$119"), ("Tooth colored filling", "Per tooth", "From $185"),
                   ("Root canal, front tooth", "Before the crown", "From $895"), ("Simple extraction", "Per tooth", "From $225")],
        "faq": [
            ("When should I go to the ER instead?", "Go to the emergency room or call 911 for swelling that makes it hard to breathe or swallow, a high fever with facial swelling, or a jaw injury from a fall or car crash. For everything else, call us first."),
            ("Can you see me after hours?", "Call the main line and choose option 2 to reach the dentist on call. They'll help you manage pain overnight and get you in first thing."),
            ("Do I need to be a patient already?", "No. We see new patients for emergencies at both offices."),
        ],
    },
}

DENTISTS = [
    {"name": "Dr. Leena Sethuraman", "role": "Founder, general dentist, South End", "img": "dr-sethuraman", "slug": "sethuraman",
     "bio": ["Leena opened Tessel in South End in 2016 after nine years in practices where the schedule ran the visit. She wanted the opposite: longer appointments, fewer patients a day, and enough time to explain an x-ray instead of pointing at it.",
             "She grew up in Raleigh, trained at the UNC Adams School of Dentistry, and finished a general practice residency before moving to Charlotte. Outside the office she's usually on the Rail Trail with her dog or at a Charlotte FC match."],
     "creds": [("DDS", "UNC Adams School of Dentistry"), ("Residency", "General practice, one year"), ("Practicing since", "2007"), ("Focus", "Anxious patients, cosmetic work")]},
    {"name": "Dr. Theo Marchbanks", "role": "General dentist, Ballantyne", "img": "dr-marchbanks", "slug": "marchbanks",
     "bio": ["Theo joined Tessel in 2022 to open the Ballantyne office. He places and restores implants in house, so patients don't get passed between offices for one tooth.",
             "He earned his DMD at East Carolina University and spent five years in a rural clinic in eastern North Carolina, where he learned to explain treatment plainly and plan around what a family can afford."],
     "creds": [("DMD", "East Carolina University"), ("Implant training", "Surgical and restorative"), ("Practicing since", "2016"), ("Focus", "Implants, families")]},
]

INSURANCE_FAQ = [
    ("How do I know what my plan will cover?", "Send your plan details when you book. We check your benefits before the visit and call or text you with what to expect."),
    ("What does in network mean for me?", "It means we've agreed to your plan's fee schedule, so you pay the plan's negotiated price and your share is usually lower."),
    ("Do you accept NC Medicaid?", "Not at this time. If you have Medicaid dental coverage, NC Medicaid's provider search can point you to a nearby dentist who accepts it."),
    ("Can I use my HSA or FSA card?", "Yes. Health savings and flexible spending cards work for any treatment, including the membership plan."),
]

NEW_FAQ = [
    ("What should I bring to my first visit?", "Your photo ID, your insurance card if you have one, and a list of medications. If you completed the secure forms ahead of time, that's all."),
    ("Can I fill out forms on paper instead?", "Yes. We'll have a tablet or paper forms ready. Arrive 15 minutes early so the visit still starts on time."),
    ("How do you protect my health information?", "Your forms go through an encrypted intake service, never by email. Only the clinical team and front desk can see them, and every access is logged."),
    ("Can my previous dentist send my x-rays?", "Yes. Tell us where you were seen and we'll request them. X-rays from the last year often mean we don't need to take new ones."),
]

AREA_FAQ = {
    "south-end": [
        ("Is there parking at the South End office?", "Yes. The garage behind the building has spaces, and the front desk validates two hours."),
        ("Can I take the light rail?", "Yes. Ride the LYNX Blue Line to East/West Blvd station and walk north on the Rail Trail. It's about a two minute walk."),
        ("Do you have early appointments?", "We open at 7:30 AM Monday through Friday, so you can be seen before work."),
    ],
    "ballantyne": [
        ("Do you have Saturday hours?", "Yes. The Ballantyne office is open Saturdays from 8 AM to 1 PM."),
        ("Do you see patients from Fort Mill and Marvin?", "Yes, many of our Ballantyne patients come from across the South Carolina line and from Union County. It's usually a 15 minute drive."),
        ("Are implants done at the Ballantyne office?", "Yes. Dr. Marchbanks places and restores implants at Ballantyne, so the whole process happens in one office."),
    ],
    "myers-park": [
        ("Which office is closest to Myers Park?", "South End. From most of Myers Park it's about 10 minutes by car down Queens Road or Kings Drive."),
        ("Is it easy to park?", "Yes. The South End office garage has spaces and we validate two hours."),
        ("Can I get early or Friday appointments?", "South End opens at 7:30 AM Monday through Friday. Friday hours end at 2 PM."),
    ],
}

AREA_PAGES = {
    "south-end": {
        "title": "Dentist in South End, Charlotte NC | Tessel Dental",
        "desc": "Our South End office sits on the Rail Trail near the East/West Blvd light rail station. Cleanings, cosmetic work and same day emergencies from 7:30 AM.",
        "h1": 'Your dentist on the <span class="accent">Rail Trail.</span>',
        "lede": "Our first office, in a converted brick building on the Rail Trail. Open at 7:30 AM on weekdays, two minutes from the East/West Blvd light rail stop.",
        "alt": "A red brick building with tall black framed windows beside a greenway trail in South End",
        "about": ["South End grew up around the old rail line, and so did we. Most of our patients here walk or ride the Blue Line in, often on the way to work, which is why we open at 7:30 and keep the first hour for checkups.",
                  "The office has five treatment rooms, a quiet consult room for treatment plans, and Dr. Sethuraman in the chair four days a week."],
        "hoods": [("South End", "28203, on the Rail Trail"), ("Dilworth", "28203, about 5 minutes"), ("Wilmore", "28203, about 5 minutes"),
                  ("Myers Park", "28207, about 10 minutes"), ("Sedgefield", "28209, about 7 minutes"), ("Uptown", "28202, a few Blue Line stops")],
    },
    "ballantyne": {
        "title": "Dentist in Ballantyne, Charlotte NC | Tessel Dental",
        "desc": "Tessel Dental's Ballantyne office is minutes from I-485 at Johnston Road, with free parking, Saturday hours and implants placed in house.",
        "h1": 'South Charlotte care, <span class="accent">Saturdays included.</span>',
        "lede": "Our Ballantyne office opened in 2022 for families in south Charlotte, Marvin and Fort Mill. Free parking at the door and open Saturday mornings.",
        "alt": "A two story stone and wood office building surrounded by trees in Ballantyne",
        "about": ["Ballantyne patients told us the same thing for years: the drive into South End was the hard part. So we opened a second office off Ballantyne Commons Parkway, five minutes from I-485.",
                  "Dr. Marchbanks leads this office and places implants here, so the scan, surgery and crown all happen down the hall from each other. Saturday mornings fill up fast with families, so book a week or two ahead."],
        "hoods": [("Ballantyne", "28277, minutes away"), ("Blakeney", "28277, about 5 minutes"), ("Piper Glen", "about 10 minutes"),
                  ("Marvin", "28173, about 15 minutes"), ("Fort Mill, SC", "29715, about 15 minutes"), ("Waverly", "28277, about 5 minutes")],
    },
}
