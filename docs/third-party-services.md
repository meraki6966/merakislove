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
- **Controls:** no logging is added by this site. The two API routes log only token counts, finish status and the model that answered.
- **Firewall:** one rate limit rule, "Chat API rate limit", published by Adam in the dashboard on 16 October 2026: any path starting with /api/ allows 10 requests a minute per IP, counted at the edge, then answers 429. Seen working on production the same day: ten requests through, the 11th to 13th refused, normal pages unaffected. The Vercel API could not create or read the firewall config for this project (404), so changes to it go through the dashboard.
- **Data processing agreement:** to confirm on the Vercel account.

## Anthropic

- **What it is:** the API behind the two demo chat assistants (the restaurant demo and the inn demo).
- **What it receives:** the messages a visitor types into either chat, and the conversation replayed on each turn.
- **Controls:**
  - Both routes accept JSON from their own page only (lib/chat-guard.ts), and cap the request body, every message and the number of turns before anything is sent.
  - Rate limiting keys on a salted hash of the IP address, never the address. Entries older than a minute are cleared as the server handles requests.
  - Nothing is stored on the server.
  - In both chats, a message that looks like a card number is stopped before it's sent.
  - The restaurant chat sends only the last 10 turns, to Haiku 5.5 with thinking off (switched from Sonnet 4.6 on 16 October 2026). The inn chat runs on Sonnet 4.6.
  - The site uses its own API key in its own Console workspace with a monthly spend limit, set up by Adam on 16 October 2026. Both chats were seen answering on the new key after the redeploy.
  - Anthropic deletes API inputs and outputs within 30 days by default, or keeps them up to 2 years if flagged by its safety systems, and doesn't train on them (checked 16 October 2026).
- **Data processing agreement:** under Anthropic's commercial terms, as a processor.

## Meraki BIP (the site assistant, added 23 October 2026)

- **What it is:** Adam's own BIP chat widget, loaded on every page from https://www.merakibip.com/api/rag/widget/meraki-is-love (components/SiteAssistant.tsx, idle-time load).
- **What it receives:** each message a visitor sends, with the tenant slug. Read in the meraki-rag-intelligence code on 23 October 2026, not yet proven by a test against production: the query route embeds the message with Voyage AI (voyage-3), retrieves only that tenant's chunks, answers with Anthropic (claude-sonnet-4-6), and does not insert the message into the database.
- **Processors behind it:** Vercel (hosting), Supabase (the tenant's documents), Voyage AI (embeddings), Anthropic (replies).
- **Controls:** CSP on this site allows only https://www.merakibip.com, in script-src and connect-src (pinned by scripts/tests/analytics.test.mjs, mutation-checked). On the BIP side, retrieval is scoped to the tenant found by slug, and a per-IP rate limit runs in memory.
- **BIP fixes merged 24 October 2026 (meraki-rag-intelligence PR #48), seen working on production the same night:** card numbers and SSNs are stopped before any outside call; messages over 2,000 characters are refused; the widget sends the last 6 turns; replies are plain text with clickable links; the stray quote in the fallback is trimmed.
- **Migration 20261024_widget_quota.sql run by Adam on 23 October 2026, with allowed_origins set to merakislove.com and www.merakislove.com.** Checked on production the same night: a request from another site gets 403, merakislove.com, www.merakislove.com and the BIP portal origin get answers, and the quota table is counting messages. Limits: 20 messages a minute per visitor, 500 a day for the tenant.
- **Data processing agreements:** Voyage AI and Supabase to confirm on the BIP accounts.

## Calendly

- **What it is:** call booking, reached only when a visitor clicks a Book a call link.
- **What it receives:** whatever the visitor enters on Calendly's own page. Nothing is shared by simply reading this site.
- **Data processing agreement:** Calendly's own terms. To confirm on the account.

## Google Fonts (demo pages only)

- **What it is:** typefaces for the static demos under /demos, including the Presence-First example.
- **What it receives:** the visitor's IP address, user agent and referring page when a demo page loads fonts.googleapis.com and fonts.gstatic.com.
- **Controls:** the main site self-hosts its fonts through next/font, so main pages make no font request to Google.
