import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import { ogBase } from "@/lib/site";

const description =
  "Adam McClarin: engineer, CISSP, and Reiki practitioner. The story behind Meraki is Love and Soulful Tech.";

export const metadata: Metadata = {
  title: "About",
  description,
  alternates: { canonical: "/about" },
  openGraph: {
    ...ogBase,
    title: "Adam McClarin · Soulful Tech",
    description,
    url: "https://merakislove.com/about",
  },
};

const story = [
  "The day starts in stillness. Before the laptop opens, before the first message lands, before the build resumes where it stopped the night before, there is a few minutes of nothing. Breath, quiet, and intention. That practice is not separate from the engineering. It is the reason the engineering looks the way it does.",
  "Twenty years across leadership, IT, and information security, and for most of them I believed I was helping people. I was building the systems, closing the tickets, passing the audits, doing the work the way it was supposed to be done. Then it hit me. The systems were serving the org chart, the compliance checklist, the quarterly number. The person on the other side of the screen was an afterthought, if they were thought of at all. That is the moment Meraki is Love started, not as a business plan, but as a refusal to keep building that way.",
  "So now the work answers to a different standard. VeloxSync gives K-12 teachers AI that moves the way teachers actually think, by grade band, against real state standards. Canopy Guard hands a small business the kind of security posture report that enterprise clients pay consultants six figures to produce. The meditation and the Reiki practice are not a hobby that lives next to the technical work. They are the source of the pace, the attention, and the decision to stop and ask whether a feature actually serves the person using it. Soulful Tech is not a tagline I picked because it sounded warm. It is the only way I know how to build.",
];

/**
 * Relocated from the homepage in the 2026 rewrite. The homepage now sells;
 * the longer writing about how the studio works lives here. Text is
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

const credentials = [
  {
    title: "CISSP",
    detail: "Certified Information Systems Security Professional",
  },
  { title: "Azure AI Engineer", detail: "Microsoft Certified" },
  {
    title: "Dual MS, Cybersecurity",
    detail: "University of Maryland Global Campus, 2018",
  },
  { title: "MBA", detail: "Baruch College, 2014" },
  { title: "20 Years", detail: "Leadership, IT, and information security" },
];

const books = [
  { title: "The Weight of the Mantle", note: "Published" },
  { title: "The AI Prompt Playbook", note: "Published" },
  { title: "Radical Endurance", note: "Written as Aris Vala" },
  { title: "Whispers of the Veil", note: "Published" },
];

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="About"
        title="Adam McClarin"
        subtitle="Engineer, CISSP, and Reiki practitioner. Building Soulful Tech with intention."
      />

      {/* The Story */}
      <section className="mt-20 max-w-3xl">
        <div className="flex flex-col gap-8">
          {story.map((paragraph, i) => (
            <ScrollReveal key={i} delay={i * 0.05}>
              <p
                className={`font-body leading-relaxed text-smoke-dim ${
                  i === 0
                    ? "text-xl text-smoke sm:text-2xl"
                    : "text-base sm:text-lg"
                }`}
              >
                {paragraph}
              </p>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* How the work gets made */}
      <section className="mt-24 max-w-3xl">
        <ScrollReveal className="mb-10 flex flex-col gap-5">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            How the work gets made
          </p>
          <SectionDivider align="left" />
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

      {/* Credentials */}
      <section className="mt-24">
        <ScrollReveal className="mb-12 flex flex-col gap-5">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Credentials
          </p>
          <SectionDivider align="left" />
        </ScrollReveal>

        <div className="grid gap-px overflow-hidden rounded-xl border border-border bg-border sm:grid-cols-2 lg:grid-cols-3">
          {credentials.map((credential, i) => (
            <ScrollReveal
              key={credential.title}
              delay={i * 0.05}
              className="flex h-full flex-col gap-3 bg-void p-7"
            >
              <h3 className="font-display text-2xl font-light text-smoke">
                {credential.title}
              </h3>
              <p className="font-mono text-xs uppercase tracking-[0.14em] text-smoke-dim">
                {credential.detail}
              </p>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* Published Work */}
      <section className="mt-24">
        <ScrollReveal className="mb-12 flex flex-col gap-5">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Published work
          </p>
          <SectionDivider align="left" />
        </ScrollReveal>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {books.map((book, i) => (
            <ScrollReveal key={book.title} delay={i * 0.05} className="h-full">
              <div className="flex h-full flex-col justify-between gap-8 rounded-xl border border-border-mid bg-navy/40 p-6">
                <h3 className="font-display text-xl font-light leading-tight text-smoke">
                  {book.title}
                </h3>
                <p className="font-mono text-[0.7rem] uppercase tracking-[0.18em] text-amber">
                  {book.note}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </section>
    </div>
  );
}
