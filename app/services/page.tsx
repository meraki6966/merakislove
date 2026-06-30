import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import { pillars, engagementModels, processSteps } from "@/lib/services";
import { calendly, ogBase } from "@/lib/site";

const description =
  "Product engineering, AI integration, security posture, and content strategy. Engagement models, process, and how to start.";

export const metadata: Metadata = {
  title: "Services",
  description,
  alternates: { canonical: "/services" },
  openGraph: {
    ...ogBase,
    title: "Services · Soulful Tech",
    description,
    url: "https://merakislove.com/services",
  },
};

export default function ServicesPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Services"
        title="Five ways to build with intention"
        subtitle="The work falls into five pillars. Most engagements draw on more than one, because a real product needs the engineering, the AI, the security, the words, and the presence around it to move together."
      />

      {/* Pillars */}
      <div className="mt-20 flex flex-col">
        {pillars.map((pillar, i) => (
          <ScrollReveal
            key={pillar.number}
            delay={i * 0.05}
            className="border-t border-border py-12 first:border-t-0 first:pt-0"
          >
            <div className="grid gap-8 md:grid-cols-[auto_1fr] md:gap-12">
              <span className="font-mono text-sm tracking-[0.2em] text-amber">
                {pillar.number}
              </span>
              <div className="flex flex-col gap-6">
                <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
                  {pillar.title}
                </h2>
                <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
                  {pillar.description}
                </p>
                <p className="max-w-2xl border-l-2 border-amber pl-5 font-body text-sm italic leading-relaxed text-smoke">
                  {pillar.proof}
                </p>
                <ul className="flex flex-wrap gap-x-8 gap-y-2">
                  {pillar.capabilities.map((capability) => (
                    <li
                      key={capability}
                      className="flex items-center gap-2 font-mono text-xs uppercase tracking-[0.14em] text-smoke-dim"
                    >
                      <span className="h-1 w-1 rounded-full bg-amber" />
                      {capability}
                    </li>
                  ))}
                </ul>
                {pillar.tiers ? (
                  <div className="mt-2 grid gap-4 sm:grid-cols-3">
                    {pillar.tiers.map((tier) => (
                      <div
                        key={tier.name}
                        className="flex flex-col gap-2 rounded-xl border border-border-mid bg-navy/40 p-5"
                      >
                        <span className="font-mono text-xs uppercase tracking-[0.14em] text-amber">
                          {tier.name}
                        </span>
                        <span className="font-display text-2xl font-light text-smoke">
                          {tier.price}
                        </span>
                      </div>
                    ))}
                  </div>
                ) : null}
              </div>
            </div>
          </ScrollReveal>
        ))}
      </div>

      {/* Engagement models */}
      <section className="mt-24">
        <ScrollReveal className="mb-12 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Engagement
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            How we work together
          </h2>
        </ScrollReveal>

        <div className="grid gap-6 sm:grid-cols-3">
          {engagementModels.map((model, i) => (
            <ScrollReveal key={model.name} delay={i * 0.06} className="h-full">
              <div
                className={`flex h-full flex-col gap-4 rounded-xl border p-7 ${
                  model.available
                    ? "border-border-mid bg-navy/40"
                    : "border-border bg-void opacity-60"
                }`}
              >
                <div className="flex items-baseline justify-between">
                  <h3 className="font-display text-2xl font-light text-smoke">
                    {model.name}
                  </h3>
                  <span className="font-mono text-xs uppercase tracking-[0.14em] text-amber">
                    {model.rate}
                  </span>
                </div>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {model.description}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* Process */}
      <section className="mt-24">
        <ScrollReveal className="mb-12 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Process
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            From first conversation to hardened launch
          </h2>
        </ScrollReveal>

        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {processSteps.map((step, i) => (
            <ScrollReveal key={step.number} delay={i * 0.06} className="h-full">
              <div className="flex h-full flex-col gap-4">
                <span className="font-mono text-3xl font-light text-amber/70">
                  {step.number}
                </span>
                <span className="block h-px w-10 bg-amber" />
                <h3 className="font-display text-xl font-light text-smoke">
                  {step.title}
                </h3>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {step.description}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* CTA with purple gradient border */}
      <ScrollReveal className="mt-24">
        <div
          className="rounded-2xl p-px"
          style={{
            background:
              "linear-gradient(135deg, var(--color-purple), var(--color-amber) 120%)",
          }}
        >
          <div className="flex flex-col items-start gap-6 rounded-2xl bg-void p-10 sm:p-14">
            <h2 className="max-w-2xl font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
              Have something you want built the right way?
            </h2>
            <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim">
              Start with a conversation. We will look at the problem honestly and
              figure out whether I am the right person to build it with you.
            </p>
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="group inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a call
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </a>
          </div>
        </div>
      </ScrollReveal>
    </div>
  );
}
