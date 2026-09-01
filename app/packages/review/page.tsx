import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import PackageSection from "@/components/PackageSection";
import PackageActions from "@/components/PackageActions";
import TiltCard from "@/components/TiltCard";
import Tag from "@/components/Tag";
import { getPackage } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const pkg = getPackage("review");

const title = "Security and AI Review | Meraki is Love";

const description = "Five days. A report you can stand on.";

const url = "https://merakislove.com/packages/review";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages/review" },
  keywords: [
    "application security review",
    "AI risk assessment",
    "prompt injection review",
    "multi-tenant isolation audit",
    "CISSP security review",
    "MITRE ATT&CK mapping",
  ],
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
  },
};

const audience = [
  "You added a chatbot to a site that handles client files.",
  "You run a multi-tenant app and have never had isolation reviewed.",
  'A partner, board, or client asked "are we actually secure?"',
  "You are about to put PHI, financials, or congregational data near an LLM.",
];

const bothTiersInclude =
  "Both include a CISSP lens on the boring layer: headers, TLS, dependencies, data handling.";

const deliverables = [
  "Written report.",
  "Findings ranked by severity and exploitability.",
  "Fix checklist in order.",
  "MITRE ATT&CK mapping when it applies.",
  "A 30-minute walkthrough call.",
];

const notIncluded = [
  "A fear pitch.",
  "A 90-page PDF nobody reads.",
  "A rebuild sold as the only fix.",
];

const notIncludedClose =
  'If the honest answer is "patch these five things," that is the answer.';

const timeline = [
  { when: "Day 1", what: "access, scope, threat sketch." },
  { when: "Days 2 to 4", what: "review." },
  { when: "Day 5", what: "report and walkthrough." },
];

/* ------------------------------------------------------------------ *
 * Structured data. Service with one priced Offer per tier, matching the
 * pattern the Presence-First page established.
 * ------------------------------------------------------------------ */

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Security and AI Review",
  serviceType: "Security and AI risk review",
  url,
  description:
    "A five-day, CISSP-informed review of an application or an AI stack. Ranked findings, a fix checklist in order, MITRE ATT&CK mapping where it applies, and a walkthrough call.",
  provider: { "@id": "https://merakislove.com/#organization" },
  areaServed: "Worldwide",
  audience: {
    "@type": "BusinessAudience",
    name: "SaaS founders, AI builders, and service businesses putting real data through a model or a site",
  },
  offers: (pkg.tiers ?? []).map((tier) => ({
    "@type": "Offer",
    name: tier.name,
    price: tier.amount,
    priceCurrency: "USD",
    description: tier.scope,
    url,
  })),
};

const breadcrumbSchema = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": `${url}/#breadcrumb`,
  itemListElement: [
    {
      "@type": "ListItem",
      position: 1,
      name: "Home",
      item: "https://merakislove.com",
    },
    {
      "@type": "ListItem",
      position: 2,
      name: "Packages",
      item: "https://merakislove.com/packages",
    },
    { "@type": "ListItem", position: 3, name: "Review", item: url },
  ],
};

export default function ReviewPackagePage() {
  return (
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      {[serviceSchema, breadcrumbSchema].map((schema, i) => (
        <script
          key={i}
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(schema).replace(/</g, "\\u003c"),
          }}
        />
      ))}

      <PageHeader
        eyebrow="Review"
        title="Security before the headline."
        subtitle="Five days. A report you can stand on. For SaaS founders, AI builders, and service businesses putting real data through a model or a site."
      />

      {/* Price */}
      <PackageSection title="Price">
        <div className="grid gap-6 sm:grid-cols-2">
          {pkg.tiers?.map((tier, i) => (
            <ScrollReveal key={tier.name} delay={i * 0.08} className="h-full">
              <TiltCard className="h-full bg-navy/40">
                <div className="flex h-full flex-col gap-4 p-7">
                  <h3 className="font-display text-2xl font-light leading-tight text-smoke">
                    {tier.name}
                  </h3>
                  <p className="mt-auto font-display text-4xl font-light text-amber">
                    {tier.price}
                  </p>
                </div>
              </TiltCard>
            </ScrollReveal>
          ))}
        </div>
      </PackageSection>

      {/* Who this is for */}
      <PackageSection title="Who this is for">
        <ul className="flex flex-col gap-px overflow-hidden rounded-xl border border-border bg-border">
          {audience.map((line, i) => (
            <ScrollReveal
              key={line}
              as="li"
              delay={i * 0.05}
              className="bg-void px-6 py-5 font-body text-base leading-relaxed text-smoke-dim sm:px-8"
            >
              {line}
            </ScrollReveal>
          ))}
        </ul>
      </PackageSection>

      {/* What I look at */}
      <PackageSection title="What I look at" lead="Depends on the tier.">
        <div className="flex flex-col gap-6">
          {pkg.tiers?.map((tier, i) => (
            <ScrollReveal key={tier.name} delay={i * 0.06}>
              <div className="flex flex-col gap-3 border-l-2 border-amber pl-6">
                <div className="flex flex-wrap items-center gap-3">
                  <span className="font-mono text-sm tracking-[0.16em] text-amber">
                    {tier.price}
                  </span>
                  <span className="font-display text-xl font-light text-smoke">
                    {tier.label}
                  </span>
                </div>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {tier.scope}
                </p>
              </div>
            </ScrollReveal>
          ))}
          <ScrollReveal delay={0.12}>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke">
              {bothTiersInclude}
            </p>
          </ScrollReveal>
        </div>
      </PackageSection>

      {/* What you get */}
      <PackageSection title="What you get">
        <ScrollReveal>
          <ul className="flex flex-wrap gap-2.5">
            {deliverables.map((item) => (
              <li key={item}>
                <Tag>{item}</Tag>
              </li>
            ))}
          </ul>
        </ScrollReveal>
      </PackageSection>

      {/* What you do not get */}
      <PackageSection title="What you do not get">
        <ScrollReveal className="flex flex-col gap-5">
          <ul className="flex flex-col gap-3">
            {notIncluded.map((item) => (
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
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke">
            {notIncludedClose}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* Timeline */}
      <PackageSection title="Timeline">
        <ol className="flex flex-col gap-5">
          {timeline.map((step, i) => (
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

      {/* How to start */}
      <PackageSection title="How to start">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            Send the URL or the repo context. We agree on tier before I begin.
          </p>
          <PackageActions label={pkg.cta} bookCall />
        </ScrollReveal>
      </PackageSection>
    </div>
  );
}
