import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import Breadcrumb from "@/components/Breadcrumb";
import { email, ogBase } from "@/lib/site";

const title = "Privacy | Meraki is Love";

const description =
  "What this site collects and why. One analytics tool, Google Analytics, with Google signals off and Global Privacy Control respected. Written to describe what the site actually does.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/privacy" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/privacy",
  },
};

/**
 * Written against what the code actually does, checked rather than assumed:
 * one analytics tool, Google Analytics 4, loaded by public/analytics.js only
 * on merakislove.com and www.merakislove.com, never when the browser sends
 * Global Privacy Control, never on a noindex page, with Google signals and
 * ad personalization off. It is included on the main pages (app/layout.tsx)
 * and on /demos/presence-first-example.html, and on no other demo. No other
 * cookie or storage API is called anywhere in app/, components/ or lib/,
 * fonts are self-hosted by next/font, the /start form composes a mailto
 * link in the browser, and there are exactly two server routes, the two demo
 * chat assistants (the restaurant demo and the inn demo). The static demos
 * under public/demos are separate pages with their own privacy notes; two of
 * them keep a small setting or the chat conversation in the tab's
 * sessionStorage. scripts/tests/analytics.test.mjs enforces the analytics
 * half of this.
 *
 * If any of that changes, this page has to change with it. A privacy policy
 * that overclaims is worse than none, because it is a promise nobody is
 * keeping.
 */

const LAST_UPDATED = "15 October 2026";

interface Section {
  title: string;
  paragraphs: string[];
  bullets?: string[];
}

const sections: Section[] = [
  {
    title: "The short version",
    paragraphs: [
      "I use one analytics tool, Google Analytics, to see which pages people read and how they found the site. It sets two cookies to tell a returning visitor from a new one. Google signals and ad personalization are switched off, so Analytics does not connect your visit to a signed-in Google account or use it to personalize ads. There is no advertising pixel and no session recording.",
      "If your browser sends Global Privacy Control, the analytics tag does not load at all. The sample business sites under /demos do not load it either.",
      "The only way this site learns anything about you personally is if you choose to write to me or book a call, and in both cases you are the one who starts it.",
    ],
  },
  {
    title: "What the site itself stores",
    paragraphs: [
      "Nothing that identifies you. There is no account to create, no newsletter list, no form that posts to a database on this site.",
      "The typefaces are served from this site rather than fetched from Google, so simply reading a page does not tell a font provider that you were here.",
    ],
  },
  {
    title: "Google Analytics",
    paragraphs: [
      "Analytics runs on the main pages of merakislove.com and on the Presence-First design demo. It does not run on the other demo sites under /demos, on preview copies of this site, or on any page hidden from search engines.",
    ],
    bullets: [
      "What Google receives: the address and title of the page, the page that sent you here, your browser, device type, screen size and language, and an approximate location worked out from your IP address. Google says Analytics does not log or store IP addresses.",
      "While you are on a page it also records scrolling, clicks on links that leave the site, and file downloads.",
      "Cookies: two first-party cookies, _ga and _ga_CD61SSYP84, each holding a random ID. They last up to two years unless you clear them.",
      "Google signals and ad personalization are off for this site.",
      "Event data is kept for two months, the shortest setting Analytics offers. Google processes it under the data processing terms I have accepted for this account.",
    ],
  },
  {
    title: "Turning analytics off for yourself",
    paragraphs: [],
    bullets: [
      "Turn on Global Privacy Control in your browser or with a browser extension. When it is on, the tag never loads here.",
      "Install Google's opt-out add-on from tools.google.com/dlpage/gaoptout.",
      "Block or clear cookies for merakislove.com in your browser settings. A content blocker that blocks Google Analytics works too.",
    ],
  },
  {
    title: "The contact form on the booking page",
    paragraphs: [
      "The form on the booking page does not submit anything to a server. It assembles what you typed into a pre-addressed email and opens it in your own mail application. Nothing leaves your device until you press send in your own mail client, and if you close the tab instead, nothing was ever transmitted or stored.",
      "That means the fields you fill in are not saved here, not logged here, and not visible to me unless you actually send the email. When you do send it, I receive an ordinary email in the studio inbox and it lives there like any other message.",
    ],
  },
  {
    title: "The Shadow AI self-assessment",
    paragraphs: [
      "The questions and the scoring on the self-assessment page run entirely in your browser. Your answers are not sent to this site, to Google Analytics or to anyone else, and they are not saved anywhere, so closing the tab clears them.",
      "Google Analytics records a visit to that page the same way it does for any other page here. It never receives your answers or your result.",
    ],
  },
  {
    title: "Booking a call",
    paragraphs: [
      "The Book a call links go to Calendly, which is a separate company running its own service. If you schedule a call there, Calendly collects whatever you enter on its own page, under its own privacy policy, and passes the booking to me. Clicking the link is what starts that; nothing is shared with Calendly by your simply reading this site.",
    ],
  },
  {
    title: "The demo chat assistants",
    paragraphs: [
      "Two demos on this site do send data to a server: the restaurant demo and the inn demo. Each has a working AI assistant so you can see one running rather than read about it. Those two chats are the only routes on this site that receive anything.",
    ],
    bullets: [
      "What you type in either chat is sent to Anthropic's API to generate a reply, and is handled under Anthropic's terms as a processor. Do not type anything sensitive into a demo.",
      "Your IP address is read from the request and held in memory for up to one minute, purely to stop one visitor from running the cost up. It is not written to a database and does not survive a restart.",
      "The conversation itself is not stored on the server. It lives in your browser tab and is replayed to the route on each turn; when you close the tab it is gone. The inn demo keeps it in the tab's session storage so it can follow you from page to page.",
      "The inn demo's assistant can fill in an arrival date, a number of nights and a room on that demo's form, and nothing else. A message that looks like a payment card number is stopped before it is sent to Anthropic.",
      "The server log records how many tokens a reply used and whether it finished cleanly. It does not record what you typed.",
    ],
  },
  {
    title: "Hosting",
    paragraphs: [
      "The site is hosted on Vercel. Like any web host, Vercel handles the requests that deliver pages to you and keeps its own operational logs, which can include IP addresses and user agents. That is infrastructure rather than a choice I made about your data, and it is the same for essentially every site you visit.",
    ],
  },
  {
    title: "What I do not do",
    paragraphs: [],
    bullets: [
      "I do not sell your information. There is no arrangement under which anyone pays for it, and there will not be.",
      "I do not share it with third parties for their own purposes.",
      "I do not add you to a mailing list because you emailed me. If you write, you get a reply from a person, not a sequence.",
      "I do not use anything you send me to train a model.",
    ],
  },
  {
    title: "Client work",
    paragraphs: [
      "If we work together, the data your project handles is governed by whatever we agree in writing for that engagement, not by this page. This policy covers this website only.",
    ],
  },
  {
    title: "Your choices",
    paragraphs: [
      "Apart from the analytics above, nothing is stored here, so there is usually nothing to delete. Analytics data is not tied to your name, and it expires on the schedule above. If you have emailed me and would rather I did not keep the message, say so and I will delete it from the inbox and confirm that I have. If you booked through Calendly and want that record removed, tell me and I will remove it on my side and point you to Calendly for theirs.",
    ],
  },
  {
    title: "Changes",
    paragraphs: [
      "If the site starts doing something this page does not describe, this page changes first. The date below is the last time it was reviewed against the actual code.",
    ],
  },
];

export default function PrivacyPage() {
  return (
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <Breadcrumb items={[{ name: "Privacy", path: "/privacy" }]} />

      <PageHeader
        eyebrow="Privacy"
        title="What this site collects."
        subtitle="Very little, and this page says exactly what. It describes what the code actually does rather than what a template would cover."
      />

      <div className="mt-16 flex flex-col">
        {sections.map((section, i) => (
          <section key={section.title} className="mt-14 first:mt-0">
            <ScrollReveal delay={i * 0.03} className="mb-6 flex flex-col gap-4">
              <h2 className="font-display text-2xl font-light text-smoke sm:text-3xl">
                {section.title}
              </h2>
              <SectionDivider align="left" />
            </ScrollReveal>

            <div className="flex flex-col gap-5">
              {section.paragraphs.map((paragraph) => (
                <ScrollReveal key={paragraph}>
                  <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
                    {paragraph}
                  </p>
                </ScrollReveal>
              ))}

              {section.bullets ? (
                <ScrollReveal>
                  <ul className="flex max-w-2xl flex-col gap-3">
                    {section.bullets.map((bullet) => (
                      <li
                        key={bullet}
                        className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim"
                      >
                        <span
                          aria-hidden
                          className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-amber"
                        />
                        {bullet}
                      </li>
                    ))}
                  </ul>
                </ScrollReveal>
              ) : null}
            </div>
          </section>
        ))}
      </div>

      {/* Contact */}
      <section className="mt-16 border-t border-border pt-10">
        <ScrollReveal className="flex flex-col items-start gap-4">
          <h2 className="font-display text-2xl font-light text-smoke sm:text-3xl">
            Questions about any of this
          </h2>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            Write to me and a person will answer. If something on this page is
            unclear or looks wrong, I would rather hear it than have it sit
            here being wrong.
          </p>
          <a
            href={`mailto:${email}`}
            className="font-mono text-sm tracking-[0.14em] text-amber transition-colors hover:text-smoke"
          >
            {email}
          </a>
          <p className="mt-4 font-mono text-[0.7rem] uppercase tracking-[0.18em] text-muted">
            Last reviewed against the code on {LAST_UPDATED}
          </p>
          <Link
            href="/"
            className="group mt-4 inline-flex items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
          >
            Back to the studio
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </ScrollReveal>
      </section>
    </div>
  );
}
