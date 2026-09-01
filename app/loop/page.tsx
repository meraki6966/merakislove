import type { Metadata } from "next";
import ScrollReveal from "@/components/ScrollReveal";
import LoopAnimation from "@/components/LoopAnimation";
import Breadcrumb from "@/components/Breadcrumb";
import { calendly, ogBase } from "@/lib/site";

const description =
  "The Meraki is Love Loop: a free audit, a focused fix, and an engine built to scale, on repeat. Start with a free Canopy Guard audit, harden and rebuild what is holding you back, then launch the Meraki Business Intelligence Portal to grow.";

export const metadata: Metadata = {
  title: "The Meraki is Love Loop",
  description,
  alternates: { canonical: "/loop" },
  openGraph: {
    ...ogBase,
    title: "The Meraki is Love Loop · Soulful Tech",
    description,
    url: "https://merakislove.com/loop",
  },
};

const canopyGuard = "https://thecanopyguard.com";

interface Stage {
  number: string;
  name: string;
  price: string;
  priceNote: string;
  body: string;
  points: string[];
  footnote: string;
}

const stages: Stage[] = [
  {
    number: "01",
    name: "Audit",
    price: "Free",
    priceNote: "No cost, no obligation",
    body: "Every loop starts with the truth. A free, automated Canopy Guard audit assesses your site across dozens of security, visibility, and performance signals and hands you a client-ready report, so we both start from what is real instead of what we assume.",
    points: [
      "Automated Canopy Guard assessment",
      "Security, visibility, and performance signals",
      "Findings mapped to a clear, prioritized report",
    ],
    footnote: "Run your free audit at thecanopyguard.com.",
  },
  {
    number: "02",
    name: "Fix",
    price: "From $85/hr",
    priceNote: "Hourly or fixed project scope",
    body: "Once we know what is holding you back, we fix it. Work runs hourly from $85, or as a fixed project scope when you want a number you can plan around. This is where the audit findings become a faster, safer, more discoverable product.",
    points: [
      "Security hardening from the audit findings",
      "AEO and GEO restructuring so AI and search can find you",
      "Product engineering — features, fixes, and rebuilds",
    ],
    footnote:
      "Loop customers save 25% off the quoted project price.",
  },
  {
    number: "03",
    name: "Scale",
    price: "$500 to launch, then $197/mo",
    priceNote: "Launch fee plus monthly",
    body: "With the foundation solid, we build the engine that grows it. The Meraki Business Intelligence Portal launches for $500 and runs at $197 a month, turning a clean, secure site into a system that finds and answers your next customers for you.",
    points: [
      "Meraki Business Intelligence Portal",
      "Lead prospecting that fills your pipeline",
      "AI conversation handling for inbound questions",
      "Omnichannel distribution across the channels that matter",
    ],
    footnote:
      "Pricing increases with add-ons and custom builds.",
  },
];

export default function LoopPage() {
  return (
    <>
      <Breadcrumb items={[{ name: "The Loop", path: "/loop" }]} />
    <>
      {/* Hero */}
      <section className="relative flex min-h-screen items-center overflow-hidden">
        <div
          aria-hidden
          className="absolute -right-40 top-1/4 h-96 w-96 rounded-full opacity-20 blur-[120px]"
          style={{ background: "var(--color-amber)" }}
        />

        <div className="mx-auto grid w-full max-w-6xl items-center gap-16 px-6 py-32 sm:px-8 lg:grid-cols-2">
          <div>
            <ScrollReveal>
              <p className="mb-6 font-mono text-xs uppercase tracking-[0.3em] text-amber">
                The System
              </p>
            </ScrollReveal>

            <ScrollReveal delay={0.08}>
              <h1 className="max-w-xl font-display text-5xl font-light leading-[1.04] text-smoke sm:text-6xl lg:text-7xl">
                The Meraki is Love{" "}
                <span className="text-amber">Loop</span>
              </h1>
            </ScrollReveal>

            <ScrollReveal delay={0.16}>
              <p className="mt-8 max-w-xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
                Audit. Fix. Scale. Three stages that feed each other, a free
                look at where you stand, a focused rebuild of what is holding
                you back, and an engine built to grow what is left. Then it
                loops, because a business worth building is never finished.
              </p>
            </ScrollReveal>

            <ScrollReveal delay={0.24}>
              <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center">
                <a
                  href={calendly.newProject}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
                >
                  Book a call
                  <span className="transition-transform duration-300 group-hover:translate-x-1">
                    →
                  </span>
                </a>
                <a
                  href={canopyGuard}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
                >
                  Start the free audit
                </a>
              </div>
            </ScrollReveal>
          </div>

          {/* Looping animation */}
          <ScrollReveal delay={0.2} className="order-first lg:order-last">
            <LoopAnimation />
          </ScrollReveal>
        </div>
      </section>

      {/* Stages */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-6xl px-6 py-24 sm:px-8 sm:py-32">
          <ScrollReveal className="mb-16 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              Three stages
            </p>
            <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.08] text-smoke sm:text-5xl">
              One loop, three movements.
            </h2>
            <p className="max-w-xl font-body text-smoke-dim">
              Each stage stands on its own and earns the next. Start anywhere
              the audit tells us to, and the rest follows.
            </p>
          </ScrollReveal>

          <div className="flex flex-col gap-6">
            {stages.map((stage, i) => (
              <ScrollReveal key={stage.name} delay={i * 0.06}>
                <article className="grid gap-8 rounded-2xl border border-border-mid bg-void p-8 sm:p-12 md:grid-cols-[auto_1fr]">
                  <div className="flex items-baseline gap-4 md:flex-col md:items-start md:gap-2">
                    <span className="font-mono text-sm tracking-[0.2em] text-amber">
                      {stage.number}
                    </span>
                    <h3 className="font-display text-3xl font-light text-smoke sm:text-4xl">
                      {stage.name}
                    </h3>
                  </div>

                  <div className="flex flex-col gap-6">
                    <div className="flex flex-col gap-1">
                      <p className="font-display text-3xl font-light text-amber">
                        {stage.price}
                      </p>
                      <p className="font-mono text-[0.7rem] uppercase tracking-[0.18em] text-muted">
                        {stage.priceNote}
                      </p>
                    </div>

                    <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
                      {stage.body}
                    </p>

                    <ul className="flex flex-col gap-2 font-body text-sm leading-relaxed text-smoke-dim">
                      {stage.points.map((point) => (
                        <li key={point} className="flex gap-2.5">
                          <span aria-hidden className="text-amber">
                            —
                          </span>
                          <span>{point}</span>
                        </li>
                      ))}
                    </ul>

                    <div className="flex flex-col gap-4 border-t border-border pt-5 sm:flex-row sm:items-center sm:justify-between">
                      <p className="font-mono text-[0.72rem] uppercase tracking-[0.14em] text-amber">
                        {stage.footnote}
                      </p>
                      {stage.name === "Audit" ? (
                        <a
                          href={canopyGuard}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="group inline-flex items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:text-amber sm:whitespace-nowrap"
                        >
                          Visit thecanopyguard.com
                          <span className="transition-transform duration-300 group-hover:translate-x-1">
                            →
                          </span>
                        </a>
                      ) : null}
                    </div>
                  </div>
                </article>
              </ScrollReveal>
            ))}
          </div>
        </div>
      </section>

      {/* Closing — Then it loops */}
      <section className="relative overflow-hidden border-y border-border-mid">
        <div
          aria-hidden
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(135deg, var(--color-purple) 0%, #14072b 45%, var(--color-void) 100%)",
          }}
        />
        <div className="relative mx-auto max-w-4xl px-6 py-28 sm:px-8 sm:py-40">
          <ScrollReveal className="flex flex-col items-start gap-8">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              And then
            </p>
            <h2 className="font-display text-4xl font-light leading-[1.1] text-smoke sm:text-6xl">
              Then it loops.
            </h2>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              Scaling surfaces the next thing to audit. The audit points to the
              next thing to fix. The fix unlocks the next thing to scale. This
              is the part most agencies skip, the relationship that keeps going
              after launch. We are not selling you a project and disappearing.
              We are building a partnership that compounds, where each turn of
              the loop leaves your business more secure, more discoverable, and
              more capable than the last.
            </p>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              You can step on anywhere and step off anytime. But most people who
              run one loop come back for the next, because growth was never a
              one-time event.
            </p>

            <div className="mt-4 flex flex-col gap-4 sm:flex-row sm:items-center">
              <a
                href={calendly.newProject}
                target="_blank"
                rel="noopener noreferrer"
                className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
              >
                Book a call
                <span className="transition-transform duration-300 group-hover:translate-x-1">
                  →
                </span>
              </a>
              <a
                href={canopyGuard}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center justify-center gap-3 rounded-full border border-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
              >
                Get your free audit
              </a>
            </div>
          </ScrollReveal>
        </div>
      </section>
    </>
    </>
  );
}
