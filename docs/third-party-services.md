# Third-party services that touch visitor data on merakislove.com

Every outside service that receives anything about a visitor is listed here, with what it gets and the controls in place. Add a row the same week a service is integrated, not later from memory.

Last reviewed: 15 October 2026, on the analytics-ga4 branch.

## Google Analytics 4 (added 15 October 2026)

- **What it is:** visitor analytics. Property "merakislove.com" in the Analytics account "Default Account for Firebase" (360469957), measurement ID G-CD61SSYP84.
- **Where it runs:** the 15 main pages (app/layout.tsx) and /demos/presence-first-example.html. Not on any other demo, preview deploy, localhost, or noindex page (the 404 page).
- **What it receives:**
  - each page view: the page address and title, the referring page, browser, device type, screen size and language
  - an approximate location from the IP address. Google states that GA4 does not log or store IP addresses.
  - enhanced measurement events: scrolls, outbound link clicks, file downloads, site search, form interactions and video engagement
  - two first-party cookies, _ga and _ga_CD61SSYP84, holding a random client ID. They last up to two years.
- **Controls in place:**
  - The loader (public/analytics.js) runs only on merakislove.com and www.merakislove.com.
  - It does nothing when the browser sends Global Privacy Control.
  - It stands down on noindex pages.
  - It sets allow_google_signals and allow_ad_personalization_signals to false. Hits carry npa=1, seen in a browser run on 15 October.
  - The Content-Security-Policy allows gtag.js from www.googletagmanager.com, and hits to `*.google-analytics.com`, `*.analytics.google.com` and `www.googletagmanager.com` only.
  - Google's own guide for Analytics without Ads features also lists `*.google.com` in connect-src. It's left out on purpose, so gtag's extra beacon to www.google.com/g/collect is blocked by the browser. The main hit to www.google-analytics.com still goes through.
  - scripts/tests/analytics.test.mjs enforces all of the above.
- **Analytics Admin, done 15 October 2026 (confirmed by Adam):**
  - Data Processing Terms accepted (Admin, Account settings, Account details).
  - Google signals off. User-ID collection and user-provided data collection off.
  - Event data retention set to 2 months.
- **End to end:** after the merge, Realtime showed Adam's own visit as one active user in the United States.
- **Security posture:** Google is a large processor with its own certifications. No credential for this property lives in the repository. The measurement ID is public by design.

## Vercel

- **What it is:** hosting and the CDN for every page.
- **What it receives:** every request, including the IP address, user agent and path, in Vercel's operational logs.
- **Controls:** no logging is added by this site. The two API routes log only token counts and finish status.
- **Data processing agreement:** to confirm on the Vercel account.

## Anthropic

- **What it is:** the API behind the two demo chat assistants (the restaurant demo and the inn demo).
- **What it receives:** the messages a visitor types into either chat, and the conversation replayed on each turn.
- **Controls:**
  - Both routes accept JSON from their own page only (lib/chat-guard.ts), and cap the request body, every message and the number of turns before anything is sent.
  - Rate limiting keys on a salted hash of the IP address, never the address. Entries older than a minute are cleared as the server handles requests.
  - Nothing is stored on the server.
  - In both chats, a message that looks like a card number is stopped before it's sent.
  - The restaurant chat sends only the last 10 turns.
  - Anthropic deletes API inputs and outputs within 30 days by default, or keeps them up to 2 years if flagged by its safety systems, and doesn't train on them (checked 16 October 2026).
- **Data processing agreement:** under Anthropic's commercial terms, as a processor.

## Calendly

- **What it is:** call booking, reached only when a visitor clicks a Book a call link.
- **What it receives:** whatever the visitor enters on Calendly's own page. Nothing is shared by simply reading this site.
- **Data processing agreement:** Calendly's own terms. To confirm on the account.

## Google Fonts (demo pages only)

- **What it is:** typefaces for the static demos under /demos, including the Presence-First example.
- **What it receives:** the visitor's IP address, user agent and referring page when a demo page loads fonts.googleapis.com and fonts.gstatic.com.
- **Controls:** the main site self-hosts its fonts through next/font, so main pages make no font request to Google.
