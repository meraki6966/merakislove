import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import Breadcrumb from "@/components/Breadcrumb";
import { email, studio, ogBase } from "@/lib/site";

const title = "About | Meraki is Love";

const description =
  "Meraki is Love is the company. Soulful Tech is the standard. I design and ship the work myself.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/about" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/about",
  },
};

const theWork =
  "I build full-stack products, put AI into them only where it earns trust, and treat security as part of the first commit.";

/**
 * Credentials as a flat list, per the copy. The scrolling ticker that used
 * to carry these was deleted in phase 1 and is not coming back.
 *
 * Deliberately not shared with the homepage's `facts` list in lib/site.ts:
 * that one is the short form for a sales page ("Dual M.S., Cybersecurity"),
 * this one names the institutions. Same facts, different copy.
 */
const credentials = [
  "Twenty years across leadership, IT, and information security",
  "CISSP",
  "Azure AI Engineer",
  "Dual M.S. in Cybersecurity, UMGC",
  "MBA, Baruch",
  "Published author",
];

/**
 * The origin story, which predates the 2026 rewrite.
 *
 * Two edits, both for coherence with the copy that now surrounds it. The
 * VeloxSync line described the education product as K-12 with state
 * standards, which is no longer what it is; it is homeschool planning, and
 * /work now says so. The closing sentences about Soulful Tech not being a
 * tagline were cut because "The name" section below makes that point in the
 * new copy's own words, and the page should not argue it twice.
 */
const story = [
  "The day starts in stillness. Before the laptop opens, before the first message lands, before the build resumes where it stopped the night before, there is a few minutes of nothing. Breath, quiet, and intention. That practice is not separate from the engineering. It is the reason the engineering looks the way it does.",
  "Twenty years across leadership, IT, and information security, and for most of them I believed I was helping people. I was building the systems, closing the tickets, passing the audits, doing the work the way it was supposed to be done. Then it hit me. The systems were serving the org chart, the compliance checklist, the quarterly number. The person on the other side of the screen was an afterthought, if they were thought of at all. That is the moment Meraki is Love started, not as a business plan, but as a refusal to keep building that way.",
  "So now the work answers to a different standard. VeloxSync for Education gives homeschool families AI planning built for how a parent actually plans, one plan across up to six children. Canopy Guard hands a small business the kind of security posture report that enterprise clients pay consultants six figures to produce. The meditation and the Reiki practice are not a hobby that lives next to the technical work. They are the source of the pace and the attention.",
];

/**
 * Relocated from the homepage in phase 1 of the 2026 rewrite. The homepage
 * sells; the longer writing about how the studio works lives here. Text is
 * unchanged from the original apart from the lead-in that gives the first
 * paragraph its referent.
 */
const practice = {
  lead: "Most engagements move through the same four movements. Discover, architect, build, then deploy and harden.",
  paragraphs: [
    "That last movement is where most studios quietly cut corners and where twenty years in information security refuses to let me. A product is not done when it works on a good day. It is done when it holds up on a bad one, when the traffic spikes, when someone probes the endpoints, and when the data it was trusted with stays exactly where it belongs. Building that kind of resilience in from the start costs a little more attention early and saves an enormous amount of pain later, and it is the through line that connects every project this studio has shipped.",
    "The same discipline shows up in the smaller decisions, the ones a client rarely sees but always feels. A form that tells you exactly what went wrong instead of failing silently. An API that returns a clear, structured error instead of a stack trace. A page that loads fast on a tired phone and a slow connection, because the person on the other side of the screen did not ask to be punished for their hardware. These are not features anyone puts on a roadmap, and they are precisely the things that separate software people tolerate from software people trust. I treat them as part of the job, not as polish to add if the budget survives.",
    "Working with a studio of one has a specific shape worth naming. You are not handed to a junior team after the pitch, and the person who understood your problem in the first call is the person writing the code in the last one. That continuity means less is lost in translation, decisions get made faster, and the context you spent an hour explaining does not evaporate between meetings. It also means I take on the work I can genuinely do well and say so plainly when something falls outside that, because a good referral protects your project more than an honest overreach ever could. The studio stays small on purpose, so the care stays real.",
    "It also helps to know what kind of work this studio is built for. The best engagements tend to be the ones where the problem is real and a little messy, where someone has tried the obvious solutions and found them wanting, and where quality matters more than shipping the cheapest possible version by Friday. Early-stage founders proving an idea, established teams who need senior hands on a hard subsystem, and organizations that finally want their security posture taken seriously all tend to find the fit natural. If your situation looks nothing like those, that is useful to learn early too, and I will tell you so rather than bend the work into a shape it was never meant to take.",
  ],
};

const takes = [
  "Early-stage founders proving a real idea.",
  "Established teams who need senior hands on a hard subsystem.",
  "Service businesses that finally want their AI and their posture taken seriously.",
];

const takesClose =
  "The problem should be real and a little messy. Quality should matter more than Friday.";

const declines = [
  "Work I would have to hide.",
  "A junior-shaped project at a senior price.",
  "A request to bolt AI onto a site that cannot hold a form.",
];

const declinesClose =
  "A good referral protects your project more than an honest overreach.";

const theName = [
  "Meraki means doing the work with the thing in you that has no better English word. Soulful Tech is not warmth as branding. It is the decision to stop and ask whether a feature serves the person using it, and then to harden the system so that care survives a bad day.",
  "If that sentence is why you hired me, good. If you hired me because the inbox is on fire, also good. Both can be true.",
];

/**
 * Section label plus the amber rule, the idiom this page already uses.
 * Rendered as an h2 rather than a paragraph: it looks identical and gives
 * the page the outline it was missing.
 */
function SectionLabel({ children }: { children: string }) {
  return (
    <ScrollReveal className="mb-8 flex flex-col gap-5">
      <h2 className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
        {children}
      </h2>
      <SectionDivider align="left" />
    </ScrollReveal>
  );
}

export default function AboutPage() {
  return (
    <>
      <Breadcrumb items={[{ name: "About", path: "/about" }]} />
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="About"
        title="The studio is small on purpose."
        subtitle="Meraki is Love is the company. Soulful Tech is the standard. I am Adam McClarin. I design and ship the work myself."
      />

      {/* The work */}
      <section className="mt-20 max-w-3xl">
        <SectionLabel>The work</SectionLabel>
        <ScrollReveal className="flex flex-col gap-8">
          <p className="font-body text-xl leading-relaxed text-smoke sm:text-2xl">
            {theWork}
          </p>
          <ul className="grid gap-x-10 gap-y-3 sm:grid-cols-2">
            {credentials.map((credential) => (
              <li
                key={credential}
                className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim"
              >
                <span
                  aria-hidden
                  className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-amber"
                />
                {credential}
              </li>
            ))}
          </ul>
          <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            The writing, the books, and the practice live on{" "}
            <a
              href={studio.site}
              target="_blank"
              rel="noopener noreferrer"
              className="text-amber transition-colors hover:text-smoke"
            >
              {studio.siteLabel}
            </a>
            . This site is for client work.
          </p>
        </ScrollReveal>
      </section>

      {/* Why the studio exists */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>Why the studio exists</SectionLabel>
        <div className="flex flex-col gap-8">
          {story.map((paragraph, i) => (
            <ScrollReveal key={i} delay={i * 0.05}>
              <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
                {paragraph}
              </p>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* How the work gets made */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>How the work gets made</SectionLabel>
        <ScrollReveal className="mb-10">
          <p className="font-body text-base leading-relaxed text-smoke sm:text-lg">
            {practice.lead}{" "}
            <Link
              href="/#process"
              className="text-amber transition-colors hover:text-smoke"
            >
              The four steps are on the homepage.
            </Link>
          </p>
        </ScrollReveal>

        <div className="flex flex-col gap-8">
          {practice.paragraphs.map((paragraph, i) => (
            <ScrollReveal key={i} delay={i * 0.05}>
              <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
                {paragraph}
              </p>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* Who I take */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>Who I take</SectionLabel>
        <ScrollReveal className="flex flex-col gap-6">
          <ul className="flex flex-col gap-3">
            {takes.map((item) => (
              <li
                key={item}
                className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim sm:text-lg"
              >
                <span
                  aria-hidden
                  className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-amber"
                />
                {item}
              </li>
            ))}
          </ul>
          <p className="font-body text-base leading-relaxed text-smoke sm:text-lg">
            {takesClose}
          </p>
        </ScrollReveal>
      </section>

      {/* Who I do not take */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>Who I do not take</SectionLabel>
        <ScrollReveal className="flex flex-col gap-6">
          <ul className="flex flex-col gap-3">
            {declines.map((item) => (
              <li
                key={item}
                className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim sm:text-lg"
              >
                <span
                  aria-hidden
                  className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-muted"
                />
                {item}
              </li>
            ))}
          </ul>
          <p className="font-body text-base leading-relaxed text-smoke sm:text-lg">
            {declinesClose}
          </p>
        </ScrollReveal>
      </section>

      {/* The name */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>The name</SectionLabel>
        <div className="flex flex-col gap-8">
          {theName.map((paragraph, i) => (
            <ScrollReveal key={i} delay={i * 0.05}>
              <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
                {paragraph}
              </p>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* Practical */}
      <section className="mt-24 max-w-3xl">
        <SectionLabel>Practical</SectionLabel>
        <ScrollReveal className="flex flex-col items-start gap-5">
          <p className="font-body text-base leading-relaxed text-smoke sm:text-lg">
            Friendswood, Texas. Clients nationwide.
          </p>
          <a
            href={`mailto:${email}`}
            className="font-mono text-xs tracking-[0.14em] text-smoke-dim transition-colors hover:text-amber"
          >
            {email}
          </a>
          <Link
            href="/start"
            className="group mt-3 inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
          >
            Book a call
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </ScrollReveal>
      </section>
    </div>
    </>
  );
}
