"""Copy for the Tallybrook Tax and Accounting demo.

Real: Philadelphia tax types, rates and due dates as published on phila.gov in
October 2026, the Pennsylvania 3.07% income tax, the federal filing calendar,
SEPTA lines and stations, and the neighborhoods. Fictional: the firm, its
people, prices and reviews.

Rates used on the site:
  Wage Tax from July 1, 2026: 3.735% residents, 3.425% non-residents.
  BIRT, tax year 2025: 1.410 mills on gross receipts, 5.71% on net income.
  Net Profits Tax, tax year 2025: 3.74% residents, 3.43% non-residents.
  School Income Tax, tax year 2025: 3.74%.
"""

# (text, who, where)
REVIEWS = [
    ("I freelanced for three years without knowing I owed the city a BIRT return. Malachi filed the back years, got the penalties reduced and set up quarterly reminders. I sleep fine now.",
     "Devon R.", "Fishtown"),
    ("Our books used to arrive in March in a shoebox. Yusra closes them by the 10th of every month and sends one page I can read on the train. Our tax bill stopped being a surprise.",
     "Carmela and Thu, bakery owners", "East Passyunk"),
    ("I live in Ardmore and work in Center City. Odessa found that my employer had withheld the resident Wage Tax rate for two years and got the difference refunded.",
     "Marcus L.", "Ardmore"),
    ("They quoted a fixed price in writing before starting, and the invoice matched it to the dollar. That had never happened to me with an accountant.",
     "Ingrid S.", "Center City"),
    ("The upload page felt safer than emailing my W-2. I took photos on my phone, got a text confirming they arrived, and that was the whole process.",
     "Tomasz K.", "Port Richmond"),
    ("We added our sixth employee and payroll got complicated. Tallybrook took it over in one pay cycle, and the city Wage Tax filings have been on time every quarter since.",
     "Renee A., cafe owner", "Old City"),
]

HOME_FAQ = [
    ("What taxes does a Philadelphia resident pay on a paycheck?",
     "Federal income tax, Social Security and Medicare, Pennsylvania income tax at a flat 3.07%, and the Philadelphia Wage Tax, which is 3.735% for residents as of July 1, 2026. Your employer normally withholds all of them."),
    ("Do I have to file a Philadelphia return if I am self-employed?",
     "Yes. Starting with tax year 2025, everyone doing business in Philadelphia files a Business Income and Receipts Tax return, whatever their revenue. Sole proprietors and partners also file a Net Profits Tax return. Both are due April 15."),
    ("How much does Tallybrook charge?",
     "A household return with W-2 income starts at $375 and covers the federal, Pennsylvania and Philadelphia filings. You get a fixed price in writing before we start, and the invoice matches it. The pricing page lists every service."),
    ("How do I send you my tax documents?",
     "Through the secure upload page. Please do not email W-2s, 1099s or anything with a Social Security number on it. The upload page encrypts files on the way to us and confirms by text when they arrive."),
    ("Can you help with a letter from the IRS or the city?",
     "Yes. Send us the letter through the upload page. Most notices have a deadline printed on the first page, so send it the day it arrives. If we prepared the return, answering the first letter is free."),
    ("Do I need to come to the office?",
     "No. About two thirds of our clients never visit. Everything can be done by phone, video and the upload page. If you prefer a desk and a handshake, the office is in Old City, two blocks from the 2nd Street station."),
]

SERVICE_PAGES = {
    "individual-tax": {
        "title": "Individual Tax Preparation in Philadelphia | Tallybrook",
        "desc": "Individual tax returns in Philadelphia from $375: federal, Pennsylvania and city filings for employees, freelancers and landlords, at a fixed price.",
        "folio": "Service 01", "h1": 'Your tax return, filed right and <span class="accent">explained.</span>',
        "lede": "Federal, Pennsylvania and Philadelphia returns prepared by a CPA or an enrolled agent, at a fixed price you see before we start.",
        "points": ["Fixed price in writing, from $375", "Every return reviewed by a second preparer"],
        "who_h": 'Who is this <span class="accent">for?</span>',
        "who": ["Most of our individual clients are Philadelphia households with one or two paychecks, a mortgage or rent, and one thing that makes the return less than simple: a side business, a rental unit, stock sales, a move in or out of the city, or a year of working from home.",
                "A Philadelphia return has more layers than most. Besides the federal and Pennsylvania returns, residents with investment income file a School Income Tax return, and anyone with freelance income files city business returns. We check which ones apply to you before we quote."],
        "included": ["Federal Form 1040 and Pennsylvania PA-40", "Philadelphia School Income Tax return when you have unearned income",
                     "A Wage Tax check: was the right rate withheld for where you live and work", "A second preparer's review before anything is filed",
                     "A one page summary of what changed from last year and why", "Answers to IRS, state and city letters about a return we prepared"],
        "steps": [("Twenty minute call", "We ask what changed this year and tell you which returns you need."),
                  ("Fixed quote", "You get a price in writing the same day. It does not change unless the facts do."),
                  ("Upload and prepare", "You send documents through the secure page. We prepare the returns, usually within ten business days."),
                  ("Review and file", "We walk you through the summary by phone or video, you sign electronically, and we file.")],
        "prices": [("Household with W-2 income", "Federal, Pennsylvania and city filings", "$375"),
                   ("With a rental property or K-1", "Per property or K-1 added", "From $525"),
                   ("Self-employed, Schedule C", "Includes BIRT and Net Profits Tax returns", "From $850"),
                   ("Prior year or amended return", "Per year", "From $300"),
                   ("Letter from the IRS or the city", "Free if we prepared the return", "$175")],
        "faq": [("What do I need to bring?", "Last year's return, your W-2s and 1099s, mortgage interest and property tax statements, and records for anything new this year: a home sale, a new child, a side business. We send a checklist that fits your situation after the first call."),
                ("How long does it take?", "Usually ten business days from the day we have all your documents. In the first two weeks of April it can take longer, so earlier is better."),
                ("I work from home outside the city for a Philadelphia employer. Do I owe Wage Tax?", "It depends on why you work from home. If your employer requires you to work outside Philadelphia, a non-resident does not owe Wage Tax for those days and can request a refund. If working from home is your choice, the tax still applies. We review your situation and file the refund request when you qualify."),
                ("What is the School Income Tax?", "A Philadelphia tax on residents' unearned income, such as dividends, some interest, short term capital gains and S corporation income. The rate for tax year 2025 was 3.74%, and the return is due April 15."),
                ("Can you file an extension for me?", "Yes, at no charge for clients. An extension moves the filing date to October 15. It does not move the payment date, so we estimate what you owe and you pay it by April 15.")],
    },
    "business-tax": {
        "title": "Small Business Tax and BIRT in Philadelphia | Tallybrook",
        "desc": "Small business tax in Philadelphia: BIRT, Net Profits Tax, Pennsylvania and federal returns for sole proprietors, LLCs, partnerships and S corporations.",
        "folio": "Service 02", "h1": 'Business taxes for Philadelphia, including <span class="accent">the BIRT.</span>',
        "lede": "City, state and federal returns for sole proprietors, LLCs, partnerships and S corporations, planned across the year so April holds no surprises.",
        "points": ["BIRT and Net Profits Tax returns included", "Quarterly estimates calculated for you"],
        "who_h": 'What changed for small businesses <span class="accent">in 2025?</span>',
        "who": ["For years, a Philadelphia business with $100,000 or less in gross receipts owed no Business Income and Receipts Tax and could skip the return. That exemption ended with tax year 2025. Now every business in the city files a BIRT return, whether or not it made a profit.",
                "For a freelancer or a new shop, that means a filing that did not exist before, and an estimated payment the year after. We register you with the Philadelphia Tax Center, confirm your Commercial Activity License, and file the BIRT alongside your Net Profits Tax and federal returns so the numbers agree."],
        "included": ["Philadelphia BIRT return, on gross receipts and on net income", "Net Profits Tax return for sole proprietors, partners and LLC members",
                     "Federal return: Schedule C, Form 1065 or Form 1120-S", "Pennsylvania return and sales tax review",
                     "Quarterly estimated payments calculated, with reminders", "A mid-year meeting to plan for the tax you will owe"],
        "steps": [("Review your setup", "Entity type, licenses, city tax accounts and last year's filings. We list anything missing."),
                  ("Fix the gaps", "We open accounts, file late returns and ask for penalty relief where the rules allow it."),
                  ("Plan the year", "A mid-year projection sets your estimates, so you save the right amount each month."),
                  ("File everything together", "City, state and federal returns prepared from one set of books and filed on time.")],
        "prices": [("Sole proprietor", "Schedule C, BIRT and Net Profits Tax, with a personal return", "From $850"),
                   ("Partnership or multi-member LLC", "Form 1065, K-1s, Pennsylvania and BIRT", "From $1,150"),
                   ("S corporation", "Form 1120-S, K-1s, Pennsylvania and BIRT", "From $1,350"),
                   ("Late or missing city returns", "Per year, with a penalty relief request", "From $295"),
                   ("New business setup", "Entity advice, EIN, city and state tax accounts", "$450")],
        "faq": [("What is the BIRT?", "The Business Income and Receipts Tax is Philadelphia's tax on doing business in the city. It has two parts. For tax year 2025 the rates were 1.410 mills on gross receipts, which is $1.41 per $1,000, and 5.71% on net income. The return is due April 15."),
                ("Do I owe BIRT if I made less than $100,000?", "You must file, and you may owe. Starting with tax year 2025, the city can no longer exempt the first $100,000 of gross receipts, so the tax applies from the first dollar."),
                ("What is the Net Profits Tax?", "A city tax on the net profit of unincorporated businesses: sole proprietors, partnerships and most LLCs. For tax year 2025 the rate was 3.74% for residents and 3.43% for non-residents. You may be able to take a credit against it for part of the BIRT you paid on net income."),
                ("Do I need a Commercial Activity License?", "Yes, if you do business in Philadelphia, including freelance work from your apartment. The city can deny or revoke the license when returns are unfiled, which is one more reason to stay current."),
                ("Should my LLC be taxed as an S corporation?", "Sometimes. It can reduce self-employment tax once profit is high enough to cover a reasonable salary and the cost of payroll. In Philadelphia the math also has to include Wage Tax on that salary and School Income Tax on the remaining profit for residents. We run the numbers both ways before you decide.")],
    },
    "bookkeeping": {
        "title": "Bookkeeping Services in Philadelphia | Tallybrook",
        "desc": "Monthly bookkeeping for Philadelphia small businesses from $350 a month: books closed by the 10th, a one page report and tax ready numbers all year.",
        "folio": "Service 03", "h1": 'Books closed by the 10th, <span class="accent">every month.</span>',
        "lede": "Bank and card accounts reconciled, every transaction categorized, and a one page report you can read in five minutes.",
        "points": ["From $350 a month, fixed", "A named bookkeeper, reviewed by a CPA"],
        "who_h": 'What do I get <span class="accent">each month?</span>',
        "who": ["By the 10th you get one page: what came in, what went out, what you kept, what you owe and how much cash should be set aside for tax. Below it is the detail, for the months you want to look.",
                "We work in QuickBooks Online or Xero, in your own account, so the books stay yours if you ever leave. When tax season comes, the return is prepared from the same numbers, with no cleanup bill."],
        "included": ["Bank, card and loan accounts reconciled monthly", "Transactions categorized, with questions sent in one batch",
                     "A one page report and a full profit and loss statement", "Sales tax and city tax amounts set aside in the report",
                     "1099 tracking for contractors through the year", "A quarterly call with your bookkeeper"],
        "steps": [("Connect accounts", "Read only bank and card feeds, plus your invoicing and point of sale systems."),
                  ("Catch up", "We bring the current year up to date. Most catch-ups take two to three weeks."),
                  ("Monthly close", "Reconciled by the 10th. Questions arrive in one list, so you answer them in one sitting."),
                  ("Quarterly review", "A CPA reviews the books each quarter and updates your tax estimate.")],
        "prices": [("Up to 75 transactions a month", "One or two accounts", "$350 a month"),
                   ("Up to 200 transactions a month", "Several accounts, sales tax tracking", "$550 a month"),
                   ("More than 200 transactions", "Quoted after a look at your books", "From $800 a month"),
                   ("Catch-up bookkeeping", "Per month of backlog", "From $175"),
                   ("Year end 1099 forms", "Per form, $95 minimum", "$15")],
        "faq": [("Which software do you use?", "QuickBooks Online and Xero. If you have neither, we set one up in your name. You own the subscription and the data."),
                ("Can you see or move my money?", "No. We connect with read only access, which lets us see transactions and nothing else. We cannot pay bills or move funds unless you add that service and approve each payment."),
                ("My books are a year behind. Can you help?", "Yes. Catch-up work is priced per month of backlog, and we quote the whole job before starting. Once you are current, the monthly fee takes over."),
                ("Do I still need a separate tax preparer?", "No. Tallybrook prepares the returns from the books we keep, so nothing is retyped and nothing is lost between two firms.")],
    },
    "payroll": {
        "title": "Payroll Services in Philadelphia | Tallybrook",
        "desc": "Payroll for Philadelphia employers from $95 a month: paychecks, Wage Tax withholding at the right rate, quarterly city and federal filings, and W-2s.",
        "folio": "Service 04", "h1": 'Payroll that gets the <span class="accent">Wage Tax right.</span>',
        "lede": "Paychecks, withholding, quarterly filings and W-2s for teams of 1 to 50, with each employee taxed at the rate that fits where they live.",
        "points": ["Resident and non-resident rates applied per employee", "City, state and federal filings included"],
        "who_h": 'Why is Philadelphia payroll <span class="accent">different?</span>',
        "who": ["Every employer in the city withholds Wage Tax, and the rate depends on where each employee lives. As of July 1, 2026 it is 3.735% for Philadelphia residents and 3.425% for non-residents. When someone moves across the city line and nobody updates payroll, the wrong rate comes out of every check until it is caught.",
                "We confirm each employee's home address when they are hired and each January, apply the rate change every July, and file the quarterly Wage Tax returns with the city. Employees who qualify for Pennsylvania tax forgiveness can apply for the city's reduced 1.5% rate, and we help them with the form."],
        "included": ["Pay runs weekly, every two weeks or twice a month", "Direct deposit and pay stubs employees can open on a phone",
                     "Philadelphia Wage Tax withheld at the right rate and filed quarterly", "Federal Form 941 and Pennsylvania withholding and unemployment filings",
                     "W-2s for employees and 1099s for contractors", "New hire reporting and a yearly address check"],
        "steps": [("Set up", "We gather employee details, open or link your city and state accounts and run a test pay cycle."),
                  ("Each pay run", "You approve hours by noon two days before payday. We do the rest."),
                  ("Each quarter", "City, state and federal returns filed, with a copy in your folder."),
                  ("Each January", "W-2s and 1099s delivered by February 1, and rates and addresses checked for the new year.")],
        "prices": [("Base fee", "Any number of pay runs", "$95 a month"),
                   ("Per employee", "Each active employee, each month", "$8"),
                   ("Setup", "One time, includes city and state accounts", "$250"),
                   ("Year end forms", "W-2s and 1099s", "Included"),
                   ("Amended quarterly returns", "Per return, for periods before we started", "$150")],
        "faq": [("What is the Philadelphia Wage Tax rate?", "As of July 1, 2026, the rate is 3.735% for Philadelphia residents and 3.425% for non-residents who work in the city. The rates usually change each July."),
                ("My employee lives in New Jersey and works in my Philadelphia shop. Which rate applies?", "The non-resident rate. Anyone who works in Philadelphia and lives outside it pays the non-resident Wage Tax on wages earned in the city."),
                ("One of my employees works from home in the suburbs. Do I withhold Wage Tax?", "If you require that employee to work outside the city, you do not withhold for those days. If the employee chooses to work from home, you do. We document the arrangement so the answer holds up if the city asks."),
                ("How often are Wage Tax filings due?", "Returns are filed quarterly, due at the end of the month after each quarter. How often you send the withheld money depends on the amount: quarterly for the smallest employers, monthly or more often for larger ones."),
                ("Can you take over in the middle of the year?", "Yes. We load the year to date figures from your current provider, so W-2s at year end cover all twelve months.")],
    },
}

SERVICES_FAQ = [
    ("Do you work with clients outside Philadelphia?", "Yes. We prepare returns for clients across Pennsylvania and for people who moved away and still have Pennsylvania or Philadelphia filings. City taxes are our specialty, and most of our clients live or work in Philadelphia or its suburbs."),
    ("Who will prepare my return?", "A CPA or an enrolled agent on our staff, and a second one reviews it. We do not send work to outside preparers or overseas."),
    ("What is the difference between a CPA and an enrolled agent?", "A CPA is licensed by the state after an exam and supervised experience, and can perform audits as well as tax work. An enrolled agent is licensed by the IRS and specializes in tax. Both can represent you before the IRS."),
    ("Is the first call free?", "Yes. It takes about twenty minutes, and you leave it knowing which filings you need and what they will cost."),
]

GUIDE_ROWS = [
    ("I live and work in Philadelphia for an employer", "Wage Tax at 3.735%, withheld from each paycheck", "Nothing to file if the right rate was withheld"),
    ("I live in the suburbs and work in Philadelphia", "Wage Tax at 3.425%, withheld from each paycheck", "A refund request if your employer required work outside the city"),
    ("I live in Philadelphia and work for an employer outside it", "Earnings Tax at the resident rate, if your employer does not withhold", "Quarterly Earnings Tax returns"),
    ("I freelance or own an unincorporated business in the city", "BIRT and Net Profits Tax", "Both returns by April 15, plus estimated payments"),
    ("I own an S corporation or a corporation in the city", "BIRT, and Wage Tax on salaries", "BIRT return by April 15 and quarterly Wage Tax returns"),
    ("I live in Philadelphia and have dividends or capital gains", "School Income Tax at 3.74%", "School Income Tax return by April 15"),
]

GUIDE_SECTIONS = [
    ("What is the Philadelphia Wage Tax?",
     ["The Wage Tax is a tax on salaries, wages, commissions and other pay. Philadelphia residents owe it wherever they work. Non-residents owe it on what they earn inside the city. Employers withhold it from each paycheck and send it to the city.",
      "As of July 1, 2026, the rate is 3.735% for residents and 3.425% for non-residents. A year earlier the rates were 3.74% and 3.43%. The city has been lowering them a little each July.",
      "Residents whose employer does not withhold, for example an out of state company, pay the same tax themselves under the name Earnings Tax."]),
    ("What is the BIRT, and who has to file it?",
     ["The Business Income and Receipts Tax applies to every individual, partnership, LLC and corporation doing business for profit in Philadelphia. You file whether or not you made a profit.",
      "It has two parts. For tax year 2025, the gross receipts part was 1.410 mills, or $1.41 for every $1,000 of receipts, and the net income part was 5.71%. The return is due April 15.",
      "Until tax year 2024, the first $100,000 of gross receipts was exempt, and many small businesses skipped the return. That exemption ended with tax year 2025. A new business owes no estimated payment with its first return. From the second year on, an estimated payment equal to the prior year's tax is due with the return."]),
    ("What is the Net Profits Tax?",
     ["The Net Profits Tax falls on the net profit of unincorporated businesses: sole proprietors, partnerships, and LLCs taxed as either. Residents pay it on profit from anywhere. Non-residents pay it on profit from business done in the city.",
      "For tax year 2025 the rate was 3.74% for residents and 3.43% for non-residents. The return is due April 15, with estimated payments on April 15 and June 15. It does not replace the BIRT, though you may be able to take a credit for part of the BIRT you paid on net income."]),
    ("What is the School Income Tax?",
     ["The School Income Tax is paid by Philadelphia residents on certain unearned income: dividends, some kinds of interest, short term capital gains, royalties, S corporation income and some rental and trust income. Wages are not part of it.",
      "The rate for tax year 2025 was 3.74%, and the return is due April 15. People often miss it in the first year they have investment income, because nothing is withheld and no employer mentions it."]),
    ("What does Pennsylvania add?",
     ["Pennsylvania taxes personal income at a flat 3.07%, with no standard deduction and few of the deductions the federal return allows. Residents who work in the city pay it on top of the Wage Tax.",
      "If you live in a suburb with its own earned income tax and work in Philadelphia, the Wage Tax you pay is credited against that local tax, so in most cases you owe nothing more at home on those wages."]),
]

GUIDE_FAQ = [
    ("Is the Philadelphia Wage Tax going down?", "A little each year. The resident rate went from 3.75% to 3.74% on July 1, 2025, and to 3.735% on July 1, 2026. The non-resident rate went from 3.44% to 3.43% to 3.425% over the same period."),
    ("Where do I file Philadelphia taxes?", "Online at the Philadelphia Tax Center, the city's filing and payment site. BIRT, Net Profits Tax, School Income Tax, Earnings Tax and employer Wage Tax returns are all filed there."),
    ("Can I get a Wage Tax refund?", "In two common cases. Non-residents can request a refund for days their employer required them to work outside the city. And employees who qualify for Pennsylvania's tax forgiveness program can apply for the city's reduced rate of 1.5% and a refund of what was withheld above it."),
    ("I never filed a BIRT return. What should I do?", "File the missing years before the city writes to you. Voluntary filing usually costs less in penalties, and it keeps your Commercial Activity License in good standing. We prepare the back returns and request penalty relief where the rules allow."),
    ("Are these rates current?", "They are the rates published by the City of Philadelphia as of October 2026: the Wage Tax rates took effect July 1, 2026, and the BIRT, Net Profits and School Income Tax rates are for tax year 2025, the latest returns filed. The city updates rates each year, usually by June."),
]

DEADLINE_FAQ = [
    ("What happens if a deadline falls on a weekend?", "It moves to the next business day. That is why the third quarter payroll return for 2026, normally due October 31, is due Monday, November 2."),
    ("Does an extension give me more time to pay?", "No. An extension gives you until October 15 to file. The tax itself is still due April 15, and interest runs on anything paid late."),
    ("When are estimated tax payments due?", "For most people, four times a year: April 15, June 15, September 15 and January 15. Pennsylvania uses the same dates. Philadelphia's Net Profits Tax estimates are due April 15 and June 15."),
    ("Are Philadelphia business returns due the same day as my personal return?", "Yes. BIRT, Net Profits Tax and School Income Tax returns are all due April 15, the same day as Form 1040 and the PA-40."),
    ("What if I miss a deadline?", "File as soon as you can. Penalties for filing late are larger than penalties for paying late, so a return filed without full payment still saves money. Then call us, because a first missed deadline often qualifies for penalty relief."),
]

PRICING_FAQ = [
    ("Why fixed prices?", "Because hourly billing punishes you for asking questions. A fixed price lets you call as often as you need, and it lets you plan."),
    ("When would a quote change?", "Only when the facts change: a rental property we did not know about, a second state, a business that started mid-year. We tell you before doing the extra work."),
    ("Do you offer payment plans?", "Yes. Monthly services are billed monthly. Tax preparation can be split into two payments, half at the start and half before filing."),
    ("Is there a discount for bundling services?", "Clients on monthly bookkeeping get their business tax return at 20% off, because clean books make the return faster to prepare."),
]

UPLOAD_FAQ = [
    ("Why should I not email my tax documents?", "A W-2 or a 1099 carries your name, address, Social Security number and income, which is everything a thief needs to file a false return in your name. Ordinary email is not encrypted from end to end, and copies stay in sent folders and inboxes for years."),
    ("What kinds of files can I send?", "PDFs and photos. A clear phone photo of each page works. The live upload page accepts files up to 25 MB each."),
    ("How do I know my documents arrived?", "You get a text within a minute listing the file names we received. If no text comes, nothing was received, and you can try again."),
    ("Who can see my documents?", "The preparer and the reviewer assigned to your return, and nobody else on staff. Every time a file is opened, the system records who opened it and when."),
    ("How long do you keep my records?", "Seven years after the return is filed, then they are deleted. You can ask for a copy or for early deletion at any time."),
]

ABOUT_FAQ = [
    ("Are you licensed?", "Yes. Odessa Varnum and Yusra Pennington are Certified Public Accountants licensed in Pennsylvania. Malachi Trestrail is an enrolled agent, licensed by the IRS. Every preparer holds a current IRS preparer tax identification number."),
    ("How large is the firm?", "Three licensed preparers, two bookkeepers and an office manager. Small enough that the person who quotes your return is the one who signs it."),
    ("Do you take new clients during tax season?", "Until March 15 for individual returns. After that we file extensions for new clients and prepare the returns in May, when there is time to do them carefully."),
    ("Can you represent me in an audit?", "Yes. CPAs and enrolled agents can both represent taxpayers before the IRS, and we handle Pennsylvania and Philadelphia audits as well. Representation is quoted separately from preparation."),
]

BIOS = {
    "odessa": {"bio": ["Odessa became a CPA in 1998 and spent thirteen years at a regional firm in Center City, where the smallest clients waited longest for a call back. She opened Tallybrook in 2011 to give those clients a firm of their own.",
                       "She grew up in West Philadelphia and has prepared returns for three generations of some families."],
               "cred": "Certified Public Accountant, Pennsylvania. Reviews every business return."},
    "malachi": {"bio": ["Malachi earned his enrolled agent license in 2012 and spent six years answering IRS and city notices before joining Tallybrook in 2016. He leads individual tax and handles back filings and penalty relief.",
                        "He lives in Fishtown and rides the El to the office."],
                "cred": "Enrolled agent, licensed by the IRS. Leads individual tax and notices."},
    "yusra": {"bio": ["Yusra joined Tallybrook in 2019 after four years in the accounting department of a restaurant group, and became a CPA the year before. She runs the monthly close and every payroll.",
                      "She can tell you what a restaurant's food cost should be before you finish the sentence."],
              "cred": "Certified Public Accountant, Pennsylvania. Leads bookkeeping and payroll."},
}

AREA_PAGES = {
    "center-city": {
        "title": "Accountant and Tax Preparer near Center City | Tallybrook",
        "desc": "Tallybrook serves Center City Philadelphia professionals, commuters and firms from its Old City office: tax returns, Wage Tax reviews, bookkeeping and payroll.",
        "h1": 'A tax and accounting firm for <span class="accent">Center City.</span>',
        "lede": "Our Old City office is a few stops east of City Hall on the Market-Frankford Line, and most Center City clients never need to make the trip.",
        "about": ["Center City is where the Wage Tax matters most. Tens of thousands of people commute in from the suburbs and New Jersey each day, and each one pays the non-resident rate on wages earned here. Since many of them now split the week between an office tower and a kitchen table, the question of which days are taxable has become a common one.",
                  "For the professional practices and small firms with offices downtown, the list is longer: BIRT, Wage Tax withholding for staff, and Use and Occupancy Tax on rented commercial space. We keep all three on one calendar."],
        "points": [("Wage Tax reviews for commuters", "We compare your pay stubs with where you lived and worked, and file a refund request when the wrong rate or the wrong days were taxed."),
                   ("Returns for professionals", "Physicians, attorneys, consultants and engineers with K-1s, stock compensation or income in more than one state."),
                   ("Books and payroll for small offices", "Monthly close, payroll and city filings for practices and firms with 2 to 50 people.")],
        "getting": "From City Hall, take the Market-Frankford Line east to 2nd Street. The office is two blocks from the station. Regional Rail riders can change at Jefferson Station.",
        "faq": [("How far is the office from Center City?", "About ten minutes by train. Take the Market-Frankford Line east from 15th Street, 13th Street or 11th Street to 2nd Street station, then walk two blocks."),
                ("I commute to Center City from the suburbs. What do I owe the city?", "The non-resident Wage Tax, 3.425% as of July 1, 2026, on wages earned in Philadelphia. Your employer withholds it. If your employer requires you to work outside the city on certain days, you can request a refund for those days."),
                ("My firm rents an office in Center City. Which city taxes apply?", "BIRT on the firm's receipts and income, Wage Tax withholding for employees, and Use and Occupancy Tax on the space, which is usually billed through your landlord. Partnerships also file a Net Profits Tax return."),
                ("Can we meet by video?", "Yes. Most Center City clients meet us by video at lunch and send documents through the secure upload page.")],
    },
    "fishtown": {
        "title": "Accountant and Tax Preparer near Fishtown | Tallybrook",
        "desc": "Tallybrook serves Fishtown freelancers, restaurants, bars and makers: BIRT and Net Profits Tax filings, monthly bookkeeping, payroll and individual returns.",
        "h1": 'A tax and accounting firm for <span class="accent">Fishtown.</span>',
        "lede": "Freelancers, restaurants, bars and studios along Frankford Avenue, two stops up the El from our Old City office.",
        "about": ["Fishtown runs on small businesses: designers and developers working from rowhouses, restaurants and bars on Frankford Avenue, studios and shops in old factory buildings. Almost all of them share one fact. They are unincorporated or newly incorporated, and they file city business returns.",
                  "Since tax year 2025, that includes everyone. A freelancer who earned $30,000 now files a BIRT return, where before the first $100,000 was exempt. We see more first time filers from Fishtown and Kensington than from anywhere else in the city."],
        "points": [("First BIRT return", "We register you with the Philadelphia Tax Center, confirm your Commercial Activity License and file the BIRT and Net Profits Tax returns together."),
                   ("Restaurants and bars", "Monthly books with food and labor cost on one page, tip reporting in payroll, and the city's 10% Liquor Tax returns filed on time."),
                   ("Freelancers and makers", "Quarterly estimates so April is quiet, and a yearly check on whether an S corporation would save you money.")],
        "getting": "From Fishtown, take the Market-Frankford Line from Girard or Berks toward Center City and get off at 2nd Street. The office is two blocks from the station.",
        "faq": [("I freelance from my apartment in Fishtown. Do I need to file with the city?", "Yes. You need a Commercial Activity License, a BIRT return and a Net Profits Tax return, all starting with your first year of freelance income."),
                ("I only made a few thousand dollars on the side. Does that count?", "It does. Starting with tax year 2025 there is no minimum for the BIRT return. The tax on a few thousand dollars is small, and filing keeps you in good standing with the city."),
                ("Do you work with restaurants and bars?", "Yes. About a fifth of our bookkeeping clients are restaurants, bars and cafes. Yusra Pennington, who leads bookkeeping, spent four years in a restaurant group's accounting department."),
                ("What is the Philadelphia Liquor Tax?", "A 10% city tax on the sale price of drinks that contain alcohol, paid by the customer and sent to the city by the bar or restaurant. It is separate from Pennsylvania sales tax and has its own return.")],
    },
    "main-line": {
        "title": "Accountant and Tax Preparer for the Main Line | Tallybrook",
        "desc": "Tallybrook serves Main Line households and owners in Ardmore, Bryn Mawr and Wayne who work or do business in Philadelphia: Wage Tax reviews and returns.",
        "h1": 'A tax and accounting firm for <span class="accent">the Main Line.</span>',
        "lede": "For households in Ardmore, Bryn Mawr, Wayne and nearby towns whose work, or whose business, is in the city.",
        "about": ["If you live on the Main Line and work in Philadelphia, your return involves two sets of local rules. The city taxes your wages at the non-resident rate. Your home township may have its own earned income tax, and the Wage Tax you pay the city is credited against it.",
                  "Owners face a version of the same question. A business based in Lower Merion or Radnor that does work inside the city limits may owe BIRT on those receipts, and a suburban resident who owns a share of a city partnership owes Net Profits Tax at the non-resident rate."],
        "points": [("Wage Tax on the right days", "Hybrid schedules mean some days are taxable by the city and some may not be. We document the days and file the refund request."),
                   ("Credits at home", "We make sure the Wage Tax you paid is credited on your local earned income tax return, so the same wages are taxed once."),
                   ("Owners with city work", "We work out how much of your receipts come from Philadelphia and file BIRT on that share.")],
        "getting": "The Paoli/Thorndale Line runs from Wayne, Bryn Mawr and Ardmore to Jefferson Station. From there the office is a short ride east on the Market-Frankford Line to 2nd Street. Most Main Line clients meet us by video.",
        "faq": [("I live in Ardmore and work in Center City. Do I pay Philadelphia tax?", "Yes. You pay the non-resident Wage Tax, 3.425% as of July 1, 2026, on wages earned in the city. Your employer withholds it."),
                ("Will I be taxed twice, by the city and by my township?", "In most cases, no. The Wage Tax you pay to Philadelphia is credited against the earned income tax of your home municipality, up to the amount of that local tax."),
                ("My business is in Wayne. Do I owe Philadelphia BIRT?", "Only on business done in Philadelphia. If you deliver services or make sales inside the city, that share of your receipts is subject to BIRT, and you need a Commercial Activity License."),
                ("Do I have to come into the city to meet?", "No. We meet most Main Line clients by video and collect documents through the secure upload page.")],
    },
}

PRIVACY = [
    ("What this website collects", [
        "The contact form asks for your name, phone number, email, the kind of help you need and a short note. It asks you to leave Social Security numbers and tax documents out, and it has no field for them.",
        "The form travels over an encrypted connection to the accountant on intake and is used to call you back.",
    ]),
    ("Your tax documents", [
        "Tax documents come to us only through the secure upload page or in person. Files are encrypted on the way to us and while stored, checked for malware on arrival, and visible only to the preparer and reviewer assigned to your return.",
        "We keep client records for seven years after a return is filed and then delete them. You can ask for a copy, or for early deletion, at any time.",
    ]),
    ("Our written security plan", [
        "Federal rules require every tax preparer to keep a written information security plan. Ours names the person responsible, lists where client data lives, and sets the rules for passwords, sign in codes, staff access, device encryption and what happens if something goes wrong. It is reviewed every January.",
    ]),
    ("What we never do", [
        "We do not sell or share your information for marketing. We do not disclose your tax information to anyone without your written consent, except where the law requires it.",
        "We will never ask for your Social Security number, bank login or a payment by gift card over email, text or phone. If someone claiming to be from Tallybrook does, hang up and call the office.",
    ]),
    ("Cookies and tracking", [
        "This site has no advertising trackers and no tracking pixels. We count visits in aggregate, without cookies and without building a profile of you.",
    ]),
]
