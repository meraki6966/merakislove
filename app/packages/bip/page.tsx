import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
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

const byName =
  "Prefer the exact system I run for my own clients? Ask for Meraki BIP by name.";

const fits =
  "Service businesses with a clear offer and a real intake process. If you cannot describe what you sell in one paragraph, we fix that in discovery before we train anything.";

const doesNotFit = [
  "Someone who wants a magic button and no documents.",
  "Someone who wants the model to invent pricing.",
  "Someone who needs the cheapest automation by Friday.",
];

const weeks = [
  {
    when: "Week 1",
    what: "discovery, offer language, source documents, platform choice.",
  },
  {
    when: "Weeks 2 to 3",
    what: 'lead engine and assistant, guardrails so it can say "I don\'t know, book the call."',
  },
  { when: "Weeks 4 to 5", what: "distribution, dashboard, staging." },
  { when: "Week 6", what: "harden, train you on the board, ship." },
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
    "A six-week build: scheduled lead prospecting, a conversational assistant trained on your own documents and pricing, distribution across two platforms, and a live activity view, in one dashboard.",
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
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
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

      <PageHeader
        eyebrow="Meraki BIP"
        title="Your practice. Not another dashboard you babysit."
        subtitle="From $7,000. Six weeks. Built for pastors, billers, advisors, and firms who need leads, answers, and follow-up without standing up a tech team."
      />

      {/* The problem */}
      <PackageSection title="The problem">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            {problem}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* What's in the base package */}
      <PackageSection title="What's in the base package">
        <ul className="flex flex-col gap-px overflow-hidden rounded-xl border border-border bg-border">
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
            {byName}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* Who it fits */}
      <PackageSection title="Who it fits">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {fits}
          </p>
        </ScrollReveal>
      </PackageSection>

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

      {/* How the six weeks run */}
      <PackageSection title="How the six weeks run">
        <ol className="flex flex-col gap-5">
          {weeks.map((step, i) => (
            <ScrollReveal
              key={step.when}
              as="li"
              delay={i * 0.06}
              className="flex flex-col gap-1 border-l-2 border-border pl-6 sm:flex-row sm:gap-6"
            >
              <span className="font-mono text-sm tracking-[0.16em] text-amber sm:w-32 sm:shrink-0">
                {step.when}
              </span>
              <span className="font-body text-base leading-relaxed text-smoke-dim">
                {step.what}
              </span>
            </ScrollReveal>
          ))}
        </ol>
      </PackageSection>

      {/* Guardrails that matter */}
      <PackageSection title="Guardrails that matter">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {guardrails}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* Price */}
      <PackageSection title="Price">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {price}
          </p>
          <PackageActions label={pkg.cta} bookCall />
        </ScrollReveal>
      </PackageSection>
    </div>
  );
}
