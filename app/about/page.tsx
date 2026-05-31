import type { Metadata } from "next";
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
  "So now the work answers to a different standard. VeloxSync gives K-12 teachers AI that moves the way teachers actually think, by grade band, against real state standards. Meraki Lingua opens conversation across 37 language communities, dialect by dialect, instead of flattening everyone into one voice. Canopy Guard hands a small business the kind of security posture report that enterprise clients pay consultants six figures to produce. The meditation and the Reiki practice are not a hobby that lives next to the technical work. They are the source of the pace, the attention, and the decision to stop and ask whether a feature actually serves the person using it. Soulful Tech is not a tagline I picked because it sounded warm. It is the only way I know how to build.",
];

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
