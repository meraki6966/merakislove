import Link from "next/link";
import type { Metadata } from "next";
import ScrollReveal from "@/components/ScrollReveal";
import PackageCard from "@/components/PackageCard";
import Tag from "@/components/Tag";
import Faq, { type FaqItem } from "@/components/Faq";
import { packages } from "@/lib/packages";
import { proofRow, facts, email, ogBase } from "@/lib/site";

const title =
  "Private AI and Secure Systems for Service Businesses | Meraki is Love";

const description =
  "I build the site, the assistant, and the security layer a practice can own. Reviews from $500. AI systems from $7,000. Book a 20-minute call.";

export const metadata: Metadata = {
  // Absolute so the page carries its own full title rather than the layout's
  // "· Soulful Tech" template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com",
  },
};

const audience = [
  "Faith-based organizations",
  "Medical billing",
  "Tax and advisory",
  "Law and professional firms",
];

const work = [
  {
    name: "VeloxSync",
    detail:
      "Performance intelligence that flags at-risk talent six weeks before resignation, not a table count.",
  },
  {
    name: "VeloxSync for Education",
    detail:
      "AI-powered homeschool planning, built for families, not classrooms. One plan covers up to six children.",
  },
  {
    name: "Canopy Guard",
    detail: "Security posture auditor. Findings mapped. Report ready to send.",
  },
  {
    name: "Meridian AI",
    detail:
      "Executive intelligence with MFA and RBAC. PPTX, PDF, and HTML from one workflow.",
  },
];

const steps = [
  {
    number: "01",
    title: "Discover",
    detail:
      "We start in conversation. People, constraints, the real goal. Nothing gets proposed until I can argue both sides of the problem.",
  },
  {
    number: "02",
    title: "Architect",
    detail:
      "Data model, integrations, failure modes, security posture. On paper, where changing your mind is cheap.",
  },
  {
    number: "03",
    title: "Build",
    detail:
      "Tight loops. Previews you can click. The person who took the first call is the person writing the code.",
  },
  {
    number: "04",
    title: "Deploy and harden",
    detail:
      "We ship, then we secure. Monitoring, headers, dependencies, a posture you can defend. A product is not done when it works on a good day. It is done when it holds up on a bad one.",
  },
];

const faqs: FaqItem[] = [
  {
    question: "Can I start small?",
    answer:
      "Yes. The five-day review exists so you do not have to buy a six-week build to find out where you stand.",
  },
  {
    question: "Do you only work in Texas?",
    answer:
      "No. The studio is in Friendswood. The work is remote. Clients are already in New York, California, Chicago, North Carolina, Houston, and Austin.",
  },
  {
    question: "I already pay for ChatGPT.",
    answer:
      "Good. That is a tool. It is not trained on your fee schedule, it is not mapped to your threat model, and it does not prospect while you are in session.",
  },
  {
    question: "What do you not take?",
    answer:
      "The cheapest possible version by Friday. AI bolted onto a weak site with nothing else changed. Work I would not put my name on.",
  },
  {
    question: "Do you build WordPress and simple sites?",
    answer:
      "Yes, when that is the right door. If the business sells atmosphere, I will point you to Presence-First instead of a template.",
  },
  {
    question: "How do we start?",
    answer:
      "A 20-minute call. No deck. If I am the wrong fit, I will say that and point you somewhere better.",
  },
];

export default function Home() {
  return (
    <>
      {/* 1 · Hero. Deliberately not full viewport: the package cards need to
          arrive within one scroll on desktop. */}
      <section className="relative overflow-hidden">
        <div
          aria-hidden
          className="absolute left-6 top-0 h-full w-px bg-gradient-to-b from-transparent via-amber/40 to-transparent sm:left-8"
        />
        <div
          aria-hidden
          className="absolute -left-40 top-1/4 h-96 w-96 rounded-full opacity-20 blur-[120px]"
          style={{ background: "var(--color-amber)" }}
        />

        <div className="mx-auto w-full max-w-6xl px-6 pb-20 pt-32 sm:px-8 sm:pb-24 sm:pt-40">
          <ScrollReveal>
            <p className="mb-6 font-mono text-xs uppercase tracking-[0.3em] text-amber">
              Soulful Tech · Meraki is Love
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.08}>
            <h1 className="max-w-4xl font-display text-4xl font-light leading-[1.06] text-smoke sm:text-6xl lg:text-7xl">
              Private AI and secure systems for service businesses.
            </h1>
          </ScrollReveal>

          <ScrollReveal delay={0.16}>
            <p className="mt-8 max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              I build the site, the assistant, and the security layer a practice
              can actually own. For pastors, medical billers, tax advisors, and
              firms that cannot rent client data to a public chatbot.
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.2}>
            <p className="mt-5 max-w-2xl font-body text-sm leading-relaxed text-smoke">
              Nationwide. Clients in New York, California, Chicago, North
              Carolina, Houston, and Austin.
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.24}>
            <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center">
              <Link
                href="/packages"
                className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
              >
                See packages
              </Link>
              <Link
                href="/start"
                className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
              >
                Book a 20-minute call
                <span className="transition-transform duration-300 group-hover:translate-x-1">
                  →
                </span>
              </Link>
            </div>
          </ScrollReveal>

          <ScrollReveal delay={0.3}>
            <ul className="mt-10 flex flex-wrap items-center gap-x-3 gap-y-2">
              {proofRow.map((item, i) => (
                <li
                  key={item}
                  className="flex items-center gap-3 font-mono text-[0.7rem] uppercase tracking-[0.2em] text-smoke-dim"
                >
                  {i > 0 ? (
                    <span aria-hidden className="text-amber">
                      ·
                    </span>
                  ) : null}
                  {item}
                </li>
              ))}
            </ul>
          </ScrollReveal>
        </div>
      </section>

      {/* 2 · Who this is for */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-6xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="flex flex-col gap-6">
            <h2 className="max-w-3xl font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              You already have a practice. You do not have a system.
            </h2>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              The same five questions hit the inbox after hours. The website
              looks rented. AI tools sit scattered across personal accounts.
              Nobody has mapped what happens if that stack leaks. That is the
              job. Not another template. Not a chatbot demo.
            </p>
            <ul className="mt-2 flex flex-wrap gap-2.5">
              {audience.map((item) => (
                <li key={item}>
                  <Tag>{item}</Tag>
                </li>
              ))}
            </ul>
          </ScrollReveal>
        </div>
      </section>

      {/* 3 · Packages */}
      <section id="packages" className="scroll-mt-24 border-t border-border">
        <div className="mx-auto max-w-6xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="mb-12 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              Packages
            </p>
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              Three ways to start.
            </h2>
            <p className="max-w-2xl font-body text-smoke-dim">
              Most people start with a review or the six-week system. Custom
              work comes after we know the problem.
            </p>
          </ScrollReveal>

          <div className="grid gap-6 md:grid-cols-3">
            {packages.map((pkg, i) => (
              <ScrollReveal key={pkg.slug} delay={i * 0.08} className="h-full">
                <PackageCard pkg={pkg} variant="home" />
              </ScrollReveal>
            ))}
          </div>

          <ScrollReveal className="mt-10 flex flex-col gap-6">
            <p className="max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
              Hourly advisory is available for focused work. Retainers are for
              teams who already have a system in production. Neither is the
              starting point.
            </p>
            <Link
              href="/packages"
              className="group inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
            >
              Compare all packages
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
          </ScrollReveal>
        </div>
      </section>

      {/* 4 · Work */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-6xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="mb-12 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              Work
            </p>
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              Built. Shipped. In use.
            </h2>
            <p className="max-w-2xl font-body text-smoke-dim">
              Specs live on the work page. This is what the products do.
            </p>
          </ScrollReveal>

          <ul className="flex flex-col">
            {work.map((product, i) => (
              <ScrollReveal
                key={product.name}
                as="li"
                delay={i * 0.06}
                className="grid gap-2 border-t border-border py-6 last:border-b md:grid-cols-[16rem_1fr] md:gap-8"
              >
                <h3 className="font-display text-2xl font-light text-smoke">
                  {product.name}
                </h3>
                <p className="font-body text-sm leading-relaxed text-smoke-dim md:pt-2">
                  {product.detail}
                </p>
              </ScrollReveal>
            ))}
          </ul>

          <ScrollReveal className="mt-10 flex flex-col gap-6">
            <Link
              href="/work"
              className="group inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
            >
              See all work
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
            <p className="max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
              Some client work sits under NDA. If you need to see behind that,
              the call is the fastest path.
            </p>
          </ScrollReveal>
        </div>
      </section>

      {/* 5 · How it works. The nav's Process link anchors here. */}
      <section id="process" className="scroll-mt-24 border-t border-border">
        <div className="mx-auto max-w-4xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="mb-12 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              How it works
            </p>
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              You should never wonder what is happening to your project.
            </h2>
          </ScrollReveal>

          <ol className="flex flex-col gap-6">
            {steps.map((step, i) => (
              <ScrollReveal
                key={step.number}
                as="li"
                delay={i * 0.06}
                className="flex flex-col gap-2 border-l-2 border-border pl-6 sm:flex-row sm:gap-6"
              >
                <span className="font-mono text-sm tracking-[0.2em] text-amber sm:pt-1">
                  {step.number}
                </span>
                <div className="flex flex-col gap-1.5">
                  <h3 className="font-display text-xl font-light text-smoke">
                    {step.title}
                  </h3>
                  <p className="font-body text-sm leading-relaxed text-smoke-dim">
                    {step.detail}
                  </p>
                </div>
              </ScrollReveal>
            ))}
          </ol>
        </div>
      </section>

      {/* 6 · Why this studio */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-4xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="flex flex-col gap-6">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              Why this studio
            </p>
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              A studio of one, on purpose.
            </h2>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              You are not handed to a junior team after the pitch. Context does
              not evaporate between meetings. I take the work I can do well and
              say so when something is outside that.
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.08} className="mt-10 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-amber">
              Facts, not poetry
            </p>
            <ul className="grid gap-x-10 gap-y-3 sm:grid-cols-2">
              {facts.map((fact) => (
                <li
                  key={fact}
                  className="flex items-start gap-3 font-body text-sm leading-relaxed text-smoke"
                >
                  <span
                    aria-hidden
                    className="mt-2 h-1 w-1 shrink-0 rounded-full bg-amber"
                  />
                  {fact}
                </li>
              ))}
            </ul>
          </ScrollReveal>

          <ScrollReveal delay={0.12} className="mt-10">
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              Soulful Tech is the standard, not the sales line. The work is
              careful. The system is built to hold.
            </p>
          </ScrollReveal>
        </div>
      </section>

      {/* 7 · FAQ */}
      <section className="border-t border-border">
        <div className="mx-auto max-w-4xl px-6 py-20 sm:px-8 sm:py-24">
          <ScrollReveal className="mb-10 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              FAQ
            </p>
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-4xl">
              The questions that come up first.
            </h2>
          </ScrollReveal>

          <ScrollReveal>
            <Faq items={faqs} />
          </ScrollReveal>
        </div>
      </section>

      {/* 8 · Final CTA */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-4xl px-6 py-20 sm:px-8 sm:py-28">
          <ScrollReveal className="flex flex-col items-start gap-6">
            <h2 className="font-display text-3xl font-light leading-[1.1] text-smoke sm:text-5xl">
              One conversation. No deck.
            </h2>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              Tell me what you run, where it hurts, and whether you need a
              review, a system, or a full build. The worst case is a clear
              answer. The best case is the start of something you can stand
              behind.
            </p>
            <Link
              href="/start"
              className="group inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a 20-minute call
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
            <a
              href={`mailto:${email}`}
              className="font-mono text-xs tracking-[0.14em] text-smoke-dim transition-colors hover:text-amber"
            >
              {email}
            </a>
          </ScrollReveal>
        </div>
      </section>
    </>
  );
}
