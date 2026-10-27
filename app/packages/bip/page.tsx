import type { Metadata } from "next";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ScrollReveal from "@/components/ScrollReveal";
import PackageSection from "@/components/PackageSection";
import PackageActions from "@/components/PackageActions";
import Breadcrumb from "@/components/Breadcrumb";
import { getPackage } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const pkg = getPackage("bip");

const title = "Meraki BIP | AI Systems for Service Businesses";

const description = "Your practice. Not another dashboard you babysit.";

const url = "https://merakislove.com/packages/bip";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages/bip" },
  keywords: [
    "AI for service businesses",
    "lead prospecting automation",
    "private AI assistant",
    "AI for churches",
    "AI for medical billing",
    "AI for tax advisors",
  ],
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
  },
};

const problem =
  "Public ChatGPT drafts a caption. It does not know your fees. It does not know which leads are real. It does not run while you are with a client. BIP is the system I build so that work is not sitting in six tabs.";

const basePackage = [
  "Scheduled lead prospecting (Maps-powered sweep, scoring, verified email and phone enrichment).",
  "Conversational assistant trained on your documents, services, and pricing, up to 50 pages of source material.",
  "Distribution across two social platforms from one dashboard.",
  "Live activity view: lead quality, platform stats, system status.",
];

const addOns =
  "Add-ons after discovery: more platforms, larger libraries, branded dashboard.";

const merakiBip = "https://merakibip.com";

const byName =
  "This page is for a system built around your practice. The system I built and run for my own clients is sold by the month, with its plans and prices at";

const fits =
  "Service businesses with a clear offer and a real intake process. If you cannot describe what you sell in one paragraph, we fix that in discovery before we train anything.";

const doesNotFit = [
  "Someone who wants a magic button and no documents.",
  "Someone who wants the model to invent pricing.",
  "Someone who needs the cheapest automation by Friday.",
];

const weeks = [
  {
    when: "Discovery",
    what: "discovery, offer language, source documents, platform choice.",
  },
  {
    when: "Build",
    what: 'lead engine and assistant, guardrails so it can say "I don\'t know, book the call."',
  },
  { when: "Distribution", what: "distribution, dashboard, staging." },
  { when: "Launch", what: "harden, train you on the board, ship." },
];

const guardrails =
  "The assistant is trained on your material. It does not invent deductions, medical advice, or pastoral counsel. When the question is outside the docs, it routes to you.";

const price =
  "Base package from $7,000. Exact number follows discovery so it matches the work, not a poster price.";

/* ------------------------------------------------------------------ *
 * Structured data. Service with a single from-price Offer, matching the
 * pattern the Presence-First page established.
 * ------------------------------------------------------------------ */

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Meraki BIP",
  serviceType: "AI business system for service businesses",
  url,
  description:
    "A build that delivers scheduled lead prospecting, a conversational assistant trained on your own documents and pricing, distribution across two platforms, and a live activity view, in one dashboard.",
  provider: { "@id": "https://merakislove.com/#organization" },
  areaServed: "Worldwide",
  audience: {
    "@type": "BusinessAudience",
    name: "Pastors, medical billers, tax advisors, and professional firms",
  },
  offers: {
    "@type": "Offer",
    name: "Meraki BIP base package",
    priceCurrency: "USD",
    priceSpecification: {
      "@type": "PriceSpecification",
      minPrice: Number(pkg.amount),
      priceCurrency: "USD",
    },
    description: pkg.detail,
    url,
  },
};


export default function BipPackagePage() {
  return (
    <PageStack>
      <Breadcrumb
        items={[
          { name: "Packages", path: "/packages" },
          { name: "Meraki BIP", path: "/packages/bip" },
        ]}
      />

      {[serviceSchema].map((schema, i) => (
        <script
          key={i}
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(schema).replace(/</g, "\\u003c"),
          }}
        />
      ))}

      <PageHero
        art={{
          src: "/art/bip.jpg",
          alt: "Engraving of a brass switchboard of dials and lamps, one hand adjusting a dial.",
        }}
        kicker="Meraki BIP"
        title="Your practice. Not another dashboard you babysit."
        subtitle="From $7,000. Built for pastors, billers, advisors, and firms who need leads, answers, and follow-up without standing up a tech team."
      />

      <Panel tone="paper" width="4xl">
        {/* The problem */}
        <PackageSection title="The problem">
          <ScrollReveal>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              {problem}
            </p>
          </ScrollReveal>
        </PackageSection>

      </Panel>
      <Panel tone="ink" width="4xl">
        {/* What's in the base package */}
        <PackageSection title="What's in the base package">
          <ul className="flex flex-col gap-px overflow-hidden rounded-xl border bg-border">
            {basePackage.map((item, i) => (
              <ScrollReveal
                key={item}
                as="li"
                delay={i * 0.05}
                className="bg-void px-6 py-5 font-body text-base leading-relaxed text-smoke-dim sm:px-8"
              >
                {item}
              </ScrollReveal>
            ))}
          </ul>
          <ScrollReveal className="mt-8 flex flex-col gap-4">
            <p className="max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
              {addOns}
            </p>
            <p className="max-w-2xl border-l-2 border-amber pl-5 font-body text-base leading-relaxed text-smoke">
              {byName}{" "}
              <a
                href={merakiBip}
                target="_blank"
                rel="noopener noreferrer"
                className="text-amber underline underline-offset-4 transition-colors duration-300 hover:text-smoke"
              >
                merakibip.com
              </a>
              .
            </p>
          </ScrollReveal>
        </PackageSection>

      </Panel>
      <Panel tone="paper" width="4xl">
        {/* Who it fits */}
        <PackageSection title="Who it fits">
          <ScrollReveal>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              {fits}
            </p>
          </ScrollReveal>
        </PackageSection>

      </Panel>
      <Panel tone="ink" width="4xl">
        {/* Who it does not fit */}
        <PackageSection title="Who it does not fit">
          <ScrollReveal>
            <ul className="flex flex-col gap-3">
              {doesNotFit.map((item) => (
                <li
                  key={item}
                  className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim"
                >
                  <span
                    aria-hidden
                    className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-muted"
                  />
                  {item}
                </li>
              ))}
            </ul>
          </ScrollReveal>
        </PackageSection>

      </Panel>
      <Panel tone="paper" width="4xl">
        {/* How the build runs */}
        <PackageSection title="How the build runs">
          <ol className="flex flex-col gap-5">
            {weeks.map((step, i) => (
              <ScrollReveal
                key={step.when}
                as="li"
                delay={i * 0.06}
                className="flex flex-col gap-1 border-l-2 border-border pl-6 sm:flex-row sm:gap-6"
              >
                <span className="font-sans font-semibold text-sm text-amber sm:w-32 sm:shrink-0">
                  {step.when}
                </span>
                <span className="font-body text-base leading-relaxed text-smoke-dim">
                  {step.what}
                </span>
              </ScrollReveal>
            ))}
          </ol>
        </PackageSection>

      </Panel>
      <Panel tone="ink" width="4xl">
        {/* Guardrails that matter */}
        <PackageSection title="Guardrails that matter">
          <ScrollReveal>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              {guardrails}
            </p>
          </ScrollReveal>
        </PackageSection>

      </Panel>
      <Panel tone="paper" width="4xl">
        {/* Price */}
        <PackageSection title="Price">
          <ScrollReveal>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              {price}
            </p>
            <PackageActions label={pkg.cta} bookCall />
          </ScrollReveal>
        </PackageSection>
      </Panel>
    </PageStack>
  );
}
