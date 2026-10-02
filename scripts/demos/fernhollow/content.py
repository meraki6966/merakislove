"""Copy for the Fernhollow Veterinary Clinic demo.

Real and checked in October 2026: DoveLewis and its address and phone, the
ASPCA poison line, Oregon's rabies rule for dogs (OAR 333-019-0017), Multnomah
County license fees, the salmon poisoning facts (Washington State University
Veterinary Teaching Hospital), the AVMA dental facts, the AAHA and AAFP core
vaccine lists, and the park details on the neighborhood pages (Portland Parks
and Recreation). People, prices and reviews are samples.
"""
from fh import ER, POISON, PHONE, TEL

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
FULL = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

TRIAGE = {
    "dog": {
        "go": ["Trouble breathing, or gums that look pale, white or blue", "Collapse, or a seizure that lasts more than a few minutes",
               "A swollen belly with retching and nothing coming up", "Hit by a car, even if they seem fine",
               "Ate rat bait, antifreeze, xylitol gum, grapes or a lot of chocolate", "Bleeding that will not stop"],
        "today": ["Vomiting or diarrhea more than twice in a day", "Ate raw salmon or trout, even with no symptoms yet",
                  "Squinting, or a red or cloudy eye", "Sudden head shaking or sneezing fits after a walk in tall grass",
                  "Limping that has not improved after a day of rest", "Not eating for a full day"],
        "week": ["Itchy skin, ear scratching or licking paws", "Bad breath or a broken tooth", "Stiffness getting up or on stairs",
                 "A new lump", "Weight gain or loss you can see", "Vaccines, a nail trim or a refill"],
    },
    "cat": {
        "go": ["Trouble breathing, or breathing with the mouth open", "A male cat straining in the litter box with little or no urine",
               "Chewed or licked any part of a lily, even the pollen", "Collapse, or a seizure that lasts more than a few minutes",
               "A fall from a window or balcony, even if they seem fine", "Licked antifreeze or ate rat bait"],
        "today": ["Not eating for a full day", "Vomiting more than twice in a day", "Hiding and not coming out for meals",
                  "Squinting, or a red or cloudy eye", "Urinating outside the box, or going much more often", "A bite wound or swelling after a fight"],
        "week": ["Bad breath or drooling", "Drinking more water than usual", "Weight loss you can feel along the spine",
                 "A new lump", "Matted fur or dandruff", "Vaccines, a nail trim or a refill"],
    },
}
LANE_COPY = [("go", "Do not wait for us. Go to the emergency hospital."),
             ("today", "We keep same day visits open for exactly this."),
             ("week", "Worth a visit, and it can wait for an appointment.")]

# slug, name, who, first month, last month, lane, what you see, what to do, more, image
HAZARDS = [
    ("salmon", "Raw salmon and trout", "dog", 9, 12, "today",
     "Vomiting, fever and swollen glands within six days of eating raw fish from a river or a cooler.",
     "Call us the day it happens. Treated early with an antibiotic and a wormer, most dogs improve within two days. Without treatment, nine in ten sick dogs die.",
     'Fall is when the fish run and when carcasses wash up on the banks of the Willamette, the Clackamas and the Sandy. We wrote a full page on <a href="salmon-poisoning.html">salmon poisoning in dogs</a>.', "salmon"),
    ("foxtails", "Foxtails and grass seeds", "dog", 6, 9, "today",
     "Sudden head shaking, sneezing fits, or licking at one paw after a walk through dry grass.",
     "Call the same day. The barbed seed only travels one way, and it has to be found and removed.",
     "Check ears, between the toes and under the collar after every summer walk. Dogs with long coats and floppy ears pick up the most.", "foxtail"),
    ("mushrooms", "Wild mushrooms", "dog", 10, 12, "go",
     "Drooling, vomiting or wobbling after time in the yard or on a trail once the fall rains start.",
     "Go to the emergency hospital and bring a photo of the mushroom. Some kinds that grow in the Northwest damage the liver.",
     "No one can tell a safe mushroom from a dangerous one by looking at a chewed stem. Clear your yard after the first week of rain and keep dogs leashed under big trees.", "mushroom"),
    ("algae", "River algae", "dog", 7, 9, "go",
     "Green scum or paint like streaks on slow water. The Willamette around Ross Island gets advisories in late summer.",
     "Keep dogs out of the water during an advisory. If your dog swam or drank and seems weak or is vomiting, go to the emergency hospital.",
     "The Oregon Health Authority posts advisories by water body. When the water looks green and still, pick a different swim spot that day.", None),
    ("lilies", "Lilies", "cat", 3, 5, "go",
     "A bouquet or a potted Easter lily in the house. Every part is toxic to cats, including the pollen and the vase water.",
     "Go to the emergency hospital right away, even if your cat seems fine. Treatment in the first hours protects the kidneys.",
     "Spring bouquets are the usual source. If you live with a cat, ask for a bouquet with no lilies, and check the label on any gift plant.", "lily"),
    ("antifreeze", "Antifreeze", "both", 11, 2, "go",
     "A sweet tasting puddle under a car in the driveway or garage during the cold months.",
     "Go to the emergency hospital right away. A very small amount is dangerous to a cat or a dog.",
     "Wipe up drips, store the jug closed and off the floor, and keep cats out of the garage when you top up the car.", None),
    ("fleas", "Fleas", "both", 1, 12, "week",
     "Scratching, scabs along the back, or black specks in the coat. Portland winters are mild enough for fleas to live all year.",
     "Keep prevention going every month, including for indoor cats. Ask us which product fits your pet.",
     "One missed month in winter is usually how a spring flea problem starts. Some dog flea products are toxic to cats, so check the label before you share.", None),
]

PRICES = [("Wellness exam", "A full nose to tail exam and a written plan", "$78", "wellness-exams.html"),
          ("Puppy or kitten first visit", "Forty minutes, with time for every question", "$65", "new-clients.html"),
          ("Same day sick visit", "Call before 3 PM and we see your pet today", "$95", "sick-visits.html"),
          ("Rabies vaccine", "With the certificate Multnomah County asks for", "$32", "vaccines.html"),
          ("Dental cleaning", "With anesthesia, monitoring and full mouth x-rays", "From $520", "dental-care.html"),
          ("Nail trim", "No appointment needed on weekdays", "$24", "pricing.html")]

PRICE_GROUPS = [
    ("Exams", [("Wellness exam", "A full nose to tail exam and a written plan", "$78"),
               ("Senior exam with bloodwork", "For dogs and cats from age seven, twice a year", "$189"),
               ("Puppy or kitten first visit", "Forty minutes, with time for every question", "$65"),
               ("Same day sick visit", "Call before 3 PM and we see your pet today", "$95"),
               ("Recheck within 14 days", "For the same problem", "$45")]),
    ("Vaccines", [("Rabies", "Dogs and cats, with the certificate", "$32"),
                  ("Distemper and parvo combination", "Dogs. Covers distemper, adenovirus, parvovirus and parainfluenza", "$38"),
                  ("Leptospirosis", "Dogs, by lifestyle", "$36"),
                  ("Bordetella", "Dogs that board, groom or play in groups", "$30"),
                  ("Feline distemper combination", "Cats. Covers panleukopenia, herpesvirus and calicivirus", "$36"),
                  ("Feline leukemia", "Kittens, and adult cats that go outside", "$40")]),
    ("Dental", [("Dental exam", "Part of every wellness exam", "Included"),
                ("Cleaning with x-rays, cat or small dog", "Anesthesia, monitoring, scaling and polishing", "From $520"),
                ("Cleaning with x-rays, medium or large dog", "Anesthesia, monitoring, scaling and polishing", "From $580"),
                ("Pre-anesthetic bloodwork", "Within 30 days of the procedure", "$110")]),
    ("Tests and small things", [("Bloodwork panel", "Results the same day", "$145"),
                                ("X-rays, two views", "Read by the veterinarian during your visit", "$185"),
                                ("Urinalysis", "Run in the clinic", "$58"),
                                ("Fecal test", "Sent to the lab, results in two days", "$42"),
                                ("Microchip", "Placed and registered before you leave", "$45"),
                                ("Nail trim", "No appointment needed on weekdays", "$24")]),
]

REVIEWS = [
    ("I called at 8 in the morning about my cat not eating. Junie asked four questions, told me it was a today problem, and had us in a room by 10.", "Priya N.", "Sellwood"),
    ("The estimate for my dog's dental had two numbers on it, with and without extractions. The call during the procedure matched the paper.", "Marcus D.", "Westmoreland"),
    ("Our puppy ate half a salmon head on the Sandy. They saw him that afternoon, and he was himself again two days later.", "Elena R.", "Woodstock"),
]

HOME_FAQ = [
    ("Are you taking new patients?", 'Yes. We see dogs and cats, and most first visits are booked within the week. A puppy or kitten first visit is forty minutes, so there is time for every question. The <a href="new-clients.html">new clients page</a> explains what to bring.'),
    ("What should I do if my pet has an emergency after hours?",
     f'Go to {ER["full"]} at {ER["addr"]} in Northwest Portland. It is open 24 hours every day, and the number is <a href="tel:{ER["tel"]}">{ER["phone"]}</a>. '
     f'If you think your pet ate something toxic, the ASPCA Animal Poison Control Center answers at <a href="tel:{POISON["tel"]}">{POISON["phone"]}</a> day and night. A consultation fee may apply.'),
    ("How much does an exam cost?", 'A wellness exam is $78 and a same day sick visit is $95. Anything beyond the exam gets a written estimate first, and you approve it before we start. Every price is on the <a href="pricing.html">prices page</a>.'),
    ("Does my dog need a rabies vaccine in Oregon?", "Yes. Oregon requires dogs to be vaccinated against rabies by six months of age. Multnomah County also licenses dogs and cats, and asks for a current rabies certificate. We hand you the certificate at the visit."),
    ("What is salmon poisoning?", 'It is an infection dogs get from a parasite in raw salmon, trout and other fish that run upstream, and it is most common west of the Cascades. Signs show up within six days. It is treatable when caught early, so call us the day your dog eats raw fish. Read the <a href="salmon-poisoning.html">full guide</a>.'),
    ("Is the clinic calm for cats?", "We try to make it so. Cats have their own waiting nook away from the dogs and a quiet exam room at the back, and we book cat visits at the slower times of day when we can."),
]

# Points on the exam plates: label, note, x and y of the point on the animal (percent of the image).
CALLOUTS = {
    "dog": [("Ears", "Checked at every visit. Foxtails hide here from June to September.", 30, 17),
            ("Teeth", "Looked at yearly and cleaned when they need it.", 15, 29),
            ("Heart and lungs", "Listened to before any vaccine or anesthesia.", 36, 48),
            ("Weight", "Recorded on every chart, so a slow change gets noticed.", 64, 34),
            ("Paws", "Checked between the toes for grass seeds and cracked pads.", 36, 86)],
    "cat": [("Ears and eyes", "Clean ears and clear, even eyes. Squinting in a cat is a same day call.", 24.3, 34.3),
            ("Teeth and gums", "Dental disease is common in adult cats, and it hides well.", 18, 46.8),
            ("Heart", "Listened to at every visit. Murmurs are common and worth tracking.", 33.3, 56.5),
            ("Kidneys", "Bloodwork from age seven catches changes early.", 59, 48.2),
            ("Weight", "A pound lost on a cat is a lot. We weigh every time.", 47.2, 62.6)],
}
PLATE = {"dog": ("plate-dog", "An illustration of a scruffy tan and white mixed breed dog in side profile, with five numbered points",
                 "Five things we check on every dog."),
         "cat": ("plate-cat", "An illustration of a grey tabby cat walking in side profile, with five numbered points",
                 "Five things we check on every cat.")}

SERVICES_FAQ = [
    ("Do you see animals other than dogs and cats?", "No. Fernhollow is a dog and cat clinic. For rabbits, birds and reptiles we keep a short list of Portland clinics that see them, and the front desk will share it."),
    ("Can I get a same day appointment?", 'Usually, for a sick pet. Call before 3 PM and we fit you in that day. Wellness exams, vaccines and dental cleanings are booked ahead, most within the week. See <a href="sick-visits.html">same day sick visits</a>.'),
    ("Do you do surgery?", "We do spays, neuters, lump removals and dental extractions on Tuesdays and Thursdays. Orthopedic and specialty surgery is referred, and we send the records for you."),
    ("Will I know the cost before you start?", 'Yes. The exam price is fixed, and anything beyond it gets a written estimate that you approve first. The <a href="pricing.html">prices page</a> lists the common items.'),
]

SERVICE_PAGES = {
    "wellness-exams": {
        "title": "Dog and Cat Wellness Exams in Portland | Fernhollow Vet",
        "desc": "A wellness exam at Fernhollow in Sellwood, Portland is a full nose to tail check with a written plan. $78, yearly for adults and twice a year for seniors.",
        "h1": "Wellness exams for Portland dogs and cats",
        "lede": "A wellness exam is a full nose to tail check on a day when nothing is wrong. It is how a slow change in weight, teeth or kidneys gets caught while it is still small.",
        "facts": [("$78", "for the exam and a written plan"), ("Thirty minutes", "in the room with a veterinarian"), ("Twice a year", "from age seven, with bloodwork")],
        "kind": "checks", "main_title": "What is checked at a wellness exam?",
        "main": ["Weight and body condition, compared with the last visit", "Eyes, ears, nose and throat", "Teeth and gums, with a note on when a cleaning makes sense",
                 "Heart and lungs", "Belly, lymph nodes, skin and coat", "Joints and the way your pet walks",
                 "Vaccines that are due and the ones your pet can skip", "Flea, tick and parasite prevention for the months ahead"],
        "body_title": "How often does my pet need an exam?",
        "body": ["Healthy adult dogs and cats come once a year. From age seven we suggest every six months, with bloodwork once a year, because kidney, thyroid and liver changes show up in the blood before they show up at home.",
                 "Puppies and kittens come every three to four weeks until their vaccine series is finished. Those visits are short, and they are where most house training and scratching questions get answered.",
                 "You leave with a written plan: what we found, what is due and when, and what each item costs. Nothing is added at the front desk."],
        "rows_title": "Fernhollow sample exam prices", "rows_head": ("Visit", "What it covers", "Price"),
        "rows": [("Wellness exam", "A full nose to tail exam and a written plan", "$78"), ("Senior exam with bloodwork", "From age seven, with a blood panel", "$189"),
                 ("Puppy or kitten first visit", "Forty minutes, with time for every question", "$65"), ("Fecal test", "Sent to the lab, results in two days", "$42")],
        "faq": [("How long does a wellness exam take?", "Plan on thirty minutes in the room. A first visit for a puppy or kitten is forty."),
                ("My cat hates the carrier. Is a yearly exam worth it?", 'Yes, and we can make it easier. Cats wait in their own nook and are seen in a quiet room at the back. The <a href="new-clients.html">new clients page</a> has carrier tips that help.'),
                ("Do indoor cats need exams?", "They do. Indoor cats avoid cars and fights, and they still get dental disease, kidney disease and weight changes. Those are the things an exam is built to find."),
                ("What if you find something?", "We tell you in the room, in plain words, and give you a written estimate for any test or treatment. You decide what happens next.")],
    },
    "sick-visits": {
        "title": "Same Day Sick Visits for Pets in Portland | Fernhollow",
        "desc": "Same day sick visits for dogs and cats in Sellwood, Portland. Call Fernhollow before 3 PM and we see your pet today. $95, with an estimate before any test.",
        "h1": "Same day sick visits in Sellwood",
        "lede": "If what you are seeing is on the yellow list, call before 3 PM and we see your pet today. A technician answers the phone and helps you decide how soon.",
        "facts": [("$95", "for the exam, with an estimate before any test"), ("Before 3 PM", "is the cutoff for a visit the same day"), ("A technician", "answers the phone and asks the right questions")],
        "kind": "steps", "main_title": "What happens at a sick visit?",
        "main": [("You call", "Tell us what you are seeing, when it started, and whether your pet is eating and drinking. We book the first open slot or tell you to go straight to the emergency hospital."),
                 ("You arrive", "Cats go to the quiet room. Dogs come in through the side door if the lobby is busy."),
                 ("We examine", "A veterinarian does a full exam, including the parts that seem unrelated. The cause is often somewhere you were not looking."),
                 ("You get an estimate", "Any test or treatment is written down with its price. You approve it before we start."),
                 ("You go home with a plan", "Medication, what to watch for, and when to come back. A technician calls the next business day to check in.")],
        "body_title": "When is it more than a sick visit?",
        "body": [f'Some things cannot wait for a clinic slot. Trouble breathing, collapse, a swollen belly with retching, a cat that cannot urinate, and any poisoning are emergencies. Go to {ER["full"]} at {ER["addr"]}, open 24 hours, or call <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.',
                 'If you call us during the day with one of those, we will say so and help you get there. The <a href="emergencies.html">emergency page</a> lists the signs for dogs and for cats.',
                 "For everything on the yellow list, a same day visit is the right speed. Waiting two or three days is how a simple problem becomes an expensive one."],
        "rows_title": "Fernhollow sample sick visit prices", "rows_head": ("Item", "What it covers", "Price"),
        "rows": [("Same day sick visit", "A full exam by a veterinarian", "$95"), ("Bloodwork panel", "Results the same day", "$145"),
                 ("X-rays, two views", "Read during your visit", "$185"), ("Urinalysis", "Run in the clinic", "$58"), ("Recheck within 14 days", "For the same problem", "$45")],
        "faq": [("What if I call after 3 PM?", f'We book the first visit the next morning and tell you what to watch for overnight. If it gets worse, call {ER["name"]} at <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.'),
                ("Can I walk in?", "Please call first. A two minute call lets us tell you whether to come to us or go straight to the emergency hospital, and it means a room is ready."),
                ("How do I know if it can wait?", 'The <a href="index.html">board on the home page</a> sorts the common signs into go now, call us today and book this week. When you are unsure, call.'),
                ("Will you tell me the cost first?", "Yes. The exam is $95. Tests and treatment are written on an estimate that you approve before we do anything.")],
    },
    "dental-care": {
        "title": "Dog and Cat Dental Cleaning in Portland | Fernhollow Vet",
        "desc": "Dental care for dogs and cats in Sellwood, Portland. Cleanings under anesthesia with full mouth x-rays from $520, and a phone call before any extraction.",
        "h1": "Dental care for dogs and cats in Portland",
        "lede": "By age three, a pet very likely has some early periodontal disease, according to the American Veterinary Medical Association. We check teeth at every exam and clean them when they need it.",
        "facts": [("From $520", "for a cleaning with anesthesia and x-rays"), ("Every tooth", "is x-rayed before we decide anything"), ("One phone call", "before any extraction, with the price")],
        "kind": "checks", "main_title": "What is included in a dental cleaning?",
        "main": ["An exam and bloodwork before anesthesia", "An IV catheter and fluids", "A technician who monitors anesthesia from start to finish",
                 "X-rays of every tooth, because most dental disease sits below the gumline", "Scaling above and below the gumline, then polishing",
                 "A phone call before any extraction, with the reason and the price", "Photos and x-rays to take home the same afternoon"],
        "body_title": "Why does a cleaning need anesthesia?",
        "body": ["A pet will not hold still with its mouth open while someone cleans under the gums. The AVMA explains that anesthesia makes the procedure less stressful and painful for the pet, and allows a better cleaning because the pet is not moving near the instruments.",
                 "The signs to watch for at home are bad breath, broken or loose teeth, teeth covered in tartar, drooling or dropping food, chewing on one side, and pulling away when the mouth is touched. Cats often show nothing at all until a tooth is badly damaged.",
                 "Your pet's teeth should be checked at least once a year. That check is part of every wellness exam at no added cost."],
        "rows_title": "Fernhollow sample dental prices", "rows_head": ("Item", "What it covers", "Price"),
        "rows": [("Dental exam", "Part of every wellness exam", "Included"), ("Cleaning with x-rays, cat or small dog", "Anesthesia, monitoring, scaling and polishing", "From $520"),
                 ("Cleaning with x-rays, medium or large dog", "Anesthesia, monitoring, scaling and polishing", "From $580"),
                 ("Pre-anesthetic bloodwork", "Within 30 days of the procedure", "$110"), ("Extractions", "Quoted by phone before we proceed", "By tooth")],
        "faq": [("How often do pets need a dental cleaning?", "It depends on the mouth. Many small dogs need one every year. Many large dogs and cats go two or three years. We tell you at the yearly exam and show you why."),
                ("Is anesthesia safe for an older pet?", "Age alone is not the deciding factor. We run bloodwork first, listen to the heart, and adjust the plan to the pet. If we see a reason to wait or refer, we say so."),
                ("What about cleanings without anesthesia?", "Scraping the visible tartar makes teeth look cleaner and leaves the disease under the gumline untouched. It also cannot include x-rays. We do not offer it."),
                ("How long is my pet at the clinic?", "Drop off is between 7:30 and 8 AM, and most pets go home between 3 and 5 PM the same day.")],
    },
    "vaccines": {
        "title": "Dog and Cat Vaccines in Portland, OR | Fernhollow Vet",
        "desc": "Vaccines for dogs and cats in Sellwood, Portland: core vaccines, puppy and kitten series, and the rabies certificate Multnomah County asks for. From $30.",
        "h1": "Vaccines for Portland dogs and cats",
        "lede": "Every pet needs a short list of core vaccines, and some need a few more based on how they live. We go through the list with you and skip what your pet does not need.",
        "facts": [("By six months", "Oregon requires a rabies vaccine for dogs"), ("Every 3 to 4 weeks", "for puppy and kitten boosters until 16 weeks"), ("Same visit", "you leave with the rabies certificate")],
        "kind": "table", "main_title": "Which vaccines does my pet need?",
        "main_head": ("Vaccine", "Who gets it", "What it covers"),
        "main": [("Distemper and parvo combination", "Every dog", "Distemper, adenovirus, parvovirus and parainfluenza. A core vaccine in the AAHA guidelines."),
                 ("Rabies", "Every dog and cat", "Required for dogs in Oregon by six months of age, and needed for a Multnomah County license."),
                 ("Leptospirosis", "Dogs, by lifestyle", "A bacteria spread through water and wet soil. We talk it through with every dog owner in this city."),
                 ("Bordetella", "Dogs, by lifestyle", "For dogs that board, go to a groomer or play in groups."),
                 ("Feline distemper combination", "Every cat", "Panleukopenia, herpesvirus and calicivirus. A core vaccine in the AAHA and AAFP guidelines."),
                 ("Feline leukemia", "Kittens, then by lifestyle", "Core for cats under one year. After that, for cats that go outside or live with a cat that does.")],
        "body_title": "What do Oregon and Multnomah County require?",
        "body": ["Oregon requires every dog to be vaccinated against rabies by six months of age. The first rabies vaccine is good for one year. Boosters after that are usually good for three.",
                 "Multnomah County licenses dogs and cats and asks for a current rabies certificate. A one year license is $27 for a spayed or neutered dog and $42 for one that is not, and $15 or $30 for a cat. Owners 65 and older pay half for up to two pets. Fees were checked in October 2026, so confirm the current amount with the county.",
                 "Puppies and kittens start their series at six to eight weeks and come back every three to four weeks until they are at least 16 weeks old. Missing the last booster is the most common gap we see."],
        "rows_title": "Fernhollow sample vaccine prices", "rows_head": ("Vaccine", "For", "Price"),
        "rows": [("Rabies", "Dogs and cats, with the certificate", "$32"), ("Distemper and parvo combination", "Dogs", "$38"), ("Leptospirosis", "Dogs, by lifestyle", "$36"),
                 ("Bordetella", "Dogs, by lifestyle", "$30"), ("Feline distemper combination", "Cats", "$36"), ("Feline leukemia", "Kittens, and cats that go outside", "$40")],
        "faq": [("Does my indoor cat need vaccines?", "Yes, the core ones. Indoor cats still meet viruses carried in on shoes and through window screens, and the county asks for a rabies certificate to license a cat."),
                ("Can my pet get vaccines without an exam?", "A veterinarian needs to have examined your pet within the past year. If that exam was here, a vaccine visit with a technician is quick and there is no exam fee."),
                ("What reactions should I watch for?", f'Most pets are a little tired for a day. Swelling of the face, hives, vomiting or trouble breathing in the hours after a vaccine is an emergency. Call us, or {ER["name"]} at <a href="tel:{ER["tel"]}">{ER["phone"]}</a> after hours.'),
                ("Do you send reminders?", "Yes. You get a text or an email three weeks before anything is due, and you can turn reminders off at any time.")],
    },
}

EMERGENCY_STEPS = [
    ("Call ahead", f'Call {ER["name"]} at <a href="tel:{ER["tel"]}">{ER["phone"]}</a> from the car. The team gets ready for you and can tell you what to do on the way.'),
    ("Bring the evidence", "If your pet ate something, bring the package, the plant or a photo of it. For a mushroom, a photo of the cap and the stem helps."),
    ("Do not make your pet vomit", "Unless a veterinarian or poison control tells you to. With some poisons and some pets, vomiting causes more harm."),
    ("Keep your pet still and warm", "Carry a cat in a carrier or a box with a towel. Keep a dog on a leash, or carry an injured dog on a blanket held like a stretcher."),
    ("Protect your hands", "A pet in pain may bite, including a gentle one. Move slowly, and wrap a cat or a small dog in a towel before you lift."),
]
POISON_READY = ["What your pet ate, drank or licked", "How much, as close as you can guess", "When it happened", "Your pet's weight", "Any signs you have seen so far"]
EMERGENCY_FAQ = [
    ("Where is the nearest 24 hour emergency vet to Sellwood?", f'{ER["full"]} is at {ER["addr"]} in Northwest Portland and is open 24 hours every day. The number is <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.'),
    ("Should I call Fernhollow or go straight to the emergency hospital?", "During our hours, call us if you are unsure. We will tell you whether to come here or go straight there. If your pet is on the red list, go, and call from the car."),
    ("Is there a number for pet poison questions?", f'The ASPCA Animal Poison Control Center answers day and night at <a href="tel:{POISON["tel"]}">{POISON["phone"]}</a>. A consultation fee may apply. Keep the case number they give you and share it with the veterinarian.'),
    ("What does an emergency visit cost?", "Emergency hospitals set their own fees, and they are higher than a daytime clinic visit. Ask for an estimate when you arrive. They will give you one."),
    ("What happens after the emergency visit?", "Ask the emergency hospital to send us the record. We read it the next business day, call you, and book any recheck here."),
]

HAZARDS_FAQ = [
    ("What is the most dangerous season for Portland dogs?", 'Fall. Salmon and trout are running, mushrooms come up with the first rain, and antifreeze shows up in driveways. Summer is second, for foxtails and river algae.'),
    ("How dangerous are lilies for cats?", "Very. Every part of a true lily or a daylily is toxic to cats, including the pollen and the water in the vase. A cat that chewed or licked any of it needs an emergency hospital right away."),
    ("Do Portland pets need flea prevention in winter?", "Yes. Winters here are mild and homes are warm, so fleas keep breeding. A missed winter month is usually where a spring problem begins."),
    ("Is the Willamette safe for dogs to swim in?", "Check before you go. In late summer, slow water around Ross Island can grow toxic algae, and the Oregon Health Authority posts advisories by water body. Skip the swim when the water is green or scummy."),
]

SALMON_FAQ = [
    ("How soon do signs of salmon poisoning appear?", "Signs generally appear within six days of a dog eating an infected fish."),
    ("Can a dog survive salmon poisoning?", "Yes, with treatment. Most dogs improve within two days of starting an antibiotic and a wormer. Without treatment, ninety percent of dogs that show symptoms die."),
    ("Does cooked salmon cause salmon poisoning?", "The disease comes from raw fish. Cook any fish you plan to share with your dog, and keep raw scraps, heads and skin out of reach."),
    ("My dog ate raw salmon and seems fine. Should I still call?", "Yes. Call the day it happens. We note the date, tell you exactly what to watch for over the next week, and see your dog at the first sign."),
]

PRICING_FAQ = [
    ("Why do you post your prices?", "A worried owner should not have to call three clinics to find out what an exam costs. The exam prices are fixed, and the list covers what most visits include."),
    ("What if my pet needs more than the exam?", "You get a written estimate with a low and a high number before any test or treatment. If something changes during a procedure, we call you before going past the estimate."),
    ("Do you take pet insurance?", "You pay at the visit and your insurer pays you back. We email the itemized invoice and the medical notes the same day, which is what most insurers ask for."),
    ("Is payment due at the visit?", "Yes. We take cards and cash. For a large unexpected bill, ask the front desk about spreading the payments."),
]

NEW_STEPS = [
    ("Request a visit", "Use the form or call. We ask for your pet's name, age and what the visit is for."),
    ("Send the records", "Ask your last clinic to email your pet's records to us, or tell us the clinic name and we will request them with your permission."),
    ("Arrive ten minutes early", "Cats come in a carrier and dogs on a leash. If your dog is nervous around other dogs, call from the car and we bring you in through the side door."),
    ("Meet the veterinarian", "A first visit is forty minutes. We go nose to tail, and you ask everything on your list."),
    ("Leave with a plan", "You get a written plan with what is due, when, and what each item costs."),
]
NEW_BRING = ["Any records, vaccine certificates or adoption papers you have", "A list of food, treats and medication, with amounts",
             "A fresh stool sample for puppies and kittens", "Your questions, written down so none get forgotten", "A favorite treat, unless your pet is coming in for a stomach problem"]
NEW_INFO = [
    ("The form asks for very little", "Your name, a phone number, an email and why you are coming. Medical history is taken in the room or by phone."),
    ("Records go to you or where you send them", "We release records to the owner on file, or to another clinic with your permission. A caller who is not on the account gets nothing."),
    ("Cards are taken at the desk", "We never ask for a card number by email, by text or through the website form."),
    ("Reminders are your choice", "Vaccine and visit reminders come by text or email, and one reply turns them off."),
]
NEW_FAQ = [
    ("How soon can a new client be seen?", "Most first visits are booked within the week. If your pet is sick today, call before 3 PM and we see you today, new client or not."),
    ("Do I need my pet's old records?", "They help, and a first visit can go ahead without them. With the records we avoid repeating vaccines and tests your pet already had."),
    ("How do I license my pet in Multnomah County?", "The county licenses dogs and cats and asks for a current rabies certificate. We hand you the certificate at the visit, and you can apply online with the county."),
    ("How do I get my cat into the carrier?", "Leave the carrier out for a few days with a towel and a few treats inside, so it stops being a signal. On the day, lower your cat in back end first through the top if your carrier opens that way."),
]

ABOUT_ROWS = [
    ("Prices are written down first", "The exam price is posted. Anything more gets a written estimate with a low and a high number."),
    ("A technician answers the phone", "The person who picks up can tell a today problem from a this week problem, and will say which one yours is."),
    ("Cats and dogs wait apart", "Cats have their own nook and a quiet exam room. Nervous dogs come in through the side door."),
    ("We say when it is not us", f'Emergencies after hours go to {ER["name"]}. Specialty surgery and cases beyond a general clinic are referred, with the records sent for you.'),
]
ABOUT_FAQ = [
    ("Who owns Fernhollow?", "Dr. Maren Halvorsen, who opened the clinic in 2012 and still sees patients four days a week. Fernhollow is independent and is not part of a chain."),
    ("Which animals do you treat?", "Dogs and cats. Keeping to two species lets a small team be good at both."),
    ("Where do your clients come from?", 'Mostly Sellwood, <a href="westmoreland.html">Westmoreland</a>, <a href="eastmoreland.html">Eastmoreland</a> and <a href="woodstock.html">Woodstock</a>, with a few from across the river and from Milwaukie.'),
    ("Are you open on weekends?", f'Saturday from 9 AM to 2 PM. We are closed on Sunday. For an emergency outside our hours, call {ER["name"]} at <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.'),
]

AREA_PAGES = {
    "westmoreland": {
        "title": "Veterinarian near Westmoreland, Portland | Fernhollow",
        "desc": "Fernhollow is a dog and cat veterinary clinic next door to Westmoreland in Sellwood, Portland, with same day sick visits and every price on the page.",
        "h1": "A veterinarian near Westmoreland",
        "lede": "Westmoreland and Sellwood share a boundary and a neighborhood association, and a good share of our clients walk over from the Westmoreland side.",
        "body_title": "What should Westmoreland pet owners know?",
        "body": ["Westmoreland Park sits at SE McLoughlin and Bybee, with Crystal Springs Creek running through it, a casting pond and a nature play area. Portland Parks asks that all dogs stay leashed in this park.",
                 "Creek and pond water is the thing we talk about most with Westmoreland dog owners. Dogs that wade and drink there are the ones we most often discuss leptospirosis vaccination with, and the ones we see for stomach upsets after a walk.",
                 "For off leash time, the nearest city off leash area is at Sellwood Riverfront Park, at SE Spokane Street and Oaks Parkway."],
        "notes": [("Dogs drinking from the creek and the pond", "We go over leptospirosis vaccination and what a water related stomach bug looks like"),
                  ("Ducks and geese along the water", "Keep the leash short near the pond. Dogs that eat droppings often end up on the yellow list"),
                  ("Cats near busy Bybee and Milwaukie", "We microchip, and we talk through indoor routines that work")],
        "faq": [("How far is Fernhollow from Westmoreland?", "We are in Sellwood, the next neighborhood south. Most Westmoreland clients are a short drive or a walk away."),
                ("Are dogs allowed off leash in Westmoreland Park?", "No. Portland Parks requires all dogs to be leashed in Westmoreland Park. Sellwood Riverfront Park has an off leash area."),
                ("Do you see cats from Westmoreland?", "Yes. About half of our patients are cats, and they have their own waiting nook and a quiet exam room.")],
    },
    "eastmoreland": {
        "title": "Veterinarian near Eastmoreland, Portland | Fernhollow",
        "desc": "Fernhollow is a dog and cat veterinary clinic in Sellwood, a short drive from Eastmoreland in Portland, with same day sick visits and prices on the page.",
        "h1": "A veterinarian near Eastmoreland",
        "lede": "Eastmoreland is a short drive from our door, across McLoughlin. Its big trees and old gardens shape what we see in the pets that live there.",
        "body_title": "What should Eastmoreland pet owners know?",
        "body": ["Crystal Springs Rhododendron Garden sits between Reed College and the Eastmoreland Golf Course, and leashed dogs are welcome there. It is one of the best walks in the city in April and May.",
                 "Rhododendrons and azaleas are toxic to dogs and cats if the leaves or flowers are chewed. Most pets leave them alone. Puppies and bored young dogs sometimes do not, and a dog that has chewed the leaves and is drooling or vomiting belongs on the red list.",
                 "Old trees also mean mushrooms once the fall rain starts. Clear the yard after the first wet week, and bring a photo if your dog eats one."],
        "notes": [("Rhododendrons and azaleas in most yards", "We show you what a chewed leaf looks like and which signs mean go now"),
                  ("Mushrooms under mature trees from October", "Clear the yard weekly in fall, and photograph anything your dog eats"),
                  ("Spring bouquets and garden lilies around cats", "Every part of a lily is toxic to cats. Ask for bouquets without them")],
        "faq": [("How far is Fernhollow from Eastmoreland?", "A short drive west across McLoughlin into Sellwood. There is parking behind the clinic."),
                ("Can I bring my dog to Crystal Springs Rhododendron Garden?", "Yes, on a leash. Keep puppies from chewing the plants, since rhododendron leaves are toxic to dogs."),
                ("My dog ate a mushroom in the yard. What do I do?", f'Take a photo of the mushroom and go to the emergency hospital. {ER["name"]} is open 24 hours at <a href="tel:{ER["tel"]}">{ER["phone"]}</a>.')],
    },
    "woodstock": {
        "title": "Veterinarian near Woodstock, Portland | Fernhollow Vet",
        "desc": "Fernhollow is a dog and cat veterinary clinic in Sellwood serving Woodstock in Southeast Portland, with same day sick visits and every price on the page.",
        "h1": "A veterinarian near Woodstock",
        "lede": "Woodstock is a dog neighborhood, and the off leash area at Woodstock Park is where a lot of our patients spend their evenings.",
        "body_title": "What should Woodstock pet owners know?",
        "body": ["Woodstock Park covers about 14 acres at SE 47th Avenue and Steele Street, and it has one of the city's off leash areas. Dogs that play there every week meet a lot of other dogs.",
                 "For those dogs we talk about the Bordetella vaccine, year round flea prevention, and what a play injury looks like the next morning. A limp that has not improved after a day of rest is a call us today problem.",
                 "Bite wounds from play are often smaller on the surface than underneath. If your dog comes home with a puncture, call the same day."],
        "notes": [("Weekly play at the off leash area", "Bordetella vaccine, flea prevention every month, and a nail check"),
                  ("Sprains and sore legs after hard play", "Rest for a day. If the limp is still there, we see your dog that day"),
                  ("Small punctures after a scuffle", "Call the same day. These close over fast and can trap infection")],
        "faq": [("How far is Fernhollow from Woodstock?", "A short drive west to Sellwood. Many Woodstock clients come on Saturday morning, when we are open 9 AM to 2 PM."),
                ("Does Woodstock Park have an off leash area?", "Yes. Woodstock Park at SE 47th Avenue and Steele Street has a city off leash area. Check the Portland Parks page for current hours."),
                ("Does my dog need the Bordetella vaccine for the dog park?", "We suggest it for dogs that play in groups, board or go to a groomer. It is $30 and can be given at any visit.")],
    },
}

PRIVACY = [
    ("What this website collects", ["The visit request form asks for your name, a phone number, an email, your pet's name and why you are coming. It does not ask for medical history, and it never asks for a card number.",
                                    "On this demo site the form does not send anything. On a live site, a request would go to the front desk only."]),
    ("How your pet's records are handled", ["Medical records belong in the clinic's record system, and the website does not store them. We release records to the owner on file, or to another clinic with your permission.",
                                            "If someone who is not on the account calls and asks about your pet, we take a message and call you."]),
    ("Payments", ["Cards are taken at the front desk. We do not ask for card numbers by email, by text or through this website. If a message asks you for one in our name, call us before you reply."]),
    ("Reminders and messages", ["Vaccine and visit reminders are sent by text or email if you ask for them. Every reminder includes a way to stop them."]),
    ("Cookies and tracking", ["This website does not use advertising trackers. It loads its typeface from Google Fonts, and that is the only outside service a visit touches."]),
]
