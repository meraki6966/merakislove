import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import Breadcrumb from "@/components/Breadcrumb";
import { email, ogBase } from "@/lib/site";

const title = "Privacy | Meraki is Love";

const description =
  "What this site collects, which is almost nothing. No cookies, no analytics, no tracking. Written to describe what the site actually does.";

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
 * no analytics package in package.json, no cookie or storage API called
 * anywhere in app/, components/ or lib/, fonts self-hosted by next/font so
 * no request reaches Google at runtime, the /start form composing a mailto
 * link in the browser, and exactly one server route, the demo booking chat.
 *
 * If any of that changes, this page has to change with it. A privacy policy
 * that overclaims is worse than none, because it is a promise nobody is
 * keeping.
 */

const LAST_UPDATED = "1 September 2026";

interface Section {
  title: string;
  paragraphs: string[];
  bullets?: string[];
}

const sections: Section[] = [
  {
    title: "The short version",
    paragraphs: [
      "This site does not set cookies, does not run analytics, and does not track you across pages or across the web. There is no advertising pixel, no session recording, and no third-party script loading in the background. Nothing you do here builds a profile of you.",
      "The only way this site learns anything about you is if you choose to write to me or book a call, and in both cases you are the one who starts it.",
    ],
  },
  {
    title: "What the site collects on its own",
    paragraphs: [
      "Nothing that identifies you. There is no account to create, no newsletter list, no form that posts to a database on this site.",
      "The typefaces are served from this site rather than fetched from Google, so simply reading a page does not tell a font provider that you were here.",
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
    title: "Booking a call",
    paragraphs: [
      "The Book a call links go to Calendly, which is a separate company running its own service. If you schedule a call there, Calendly collects whatever you enter on its own page, under its own privacy policy, and passes the booking to me. Clicking the link is what starts that; nothing is shared with Calendly by your simply reading this site.",
    ],
  },
  {
    title: "The demo booking assistant",
    paragraphs: [
      "One page on this site does send data to a server: the restaurant demo, which has a working AI booking chat so you can see one running rather than read about it. It is the only route on this site that receives anything.",
    ],
    bullets: [
      "What you type in that chat is sent to Anthropic's API to generate a reply, and is handled under Anthropic's terms as a processor. Do not type anything sensitive into a demo.",
      "Your IP address is read from the request and held in memory for up to one minute, purely to stop one visitor from running the cost up. It is not written to a database and does not survive a restart.",
      "The conversation itself is not stored. It lives in your browser tab and is replayed to the route on each turn; when you close the tab it is gone.",
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
      "Because there is nothing stored here, there is usually nothing to delete. If you have emailed me and would rather I did not keep the message, say so and I will delete it from the inbox and confirm that I have. If you booked through Calendly and want that record removed, tell me and I will remove it on my side and point you to Calendly for theirs.",
    ],
  },
  {
    title: "Changes",
    paragraphs: [
      "If the site starts doing something this page does not describe, adding analytics for instance, this page changes first. The date below is the last time it was reviewed against the actual code.",
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
        subtitle="Almost nothing, and this page says exactly what. It describes what the code actually does rather than what a template would cover."
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
