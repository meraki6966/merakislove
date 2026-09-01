import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import PackageSection from "@/components/PackageSection";
import PackageActions from "@/components/PackageActions";
import Breadcrumb from "@/components/Breadcrumb";
import { getPackage, presenceFirstSummary } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const pkg = getPackage("custom");

const title = "Custom Builds | Meraki is Love";

const description =
  "Full-stack products, private AI, or a Presence-First site. Scoped after a call.";

const url = "https://merakislove.com/packages/custom";

/**
 * The canonical Presence-First page. Post phase 1 this lives under /packages;
 * the old /services path still 308s here for anyone arriving on an old link,
 * but internal links point straight at the current URL so nothing takes an
 * unnecessary hop.
 */
const presenceFirstHref = "/packages/presence-first-web-design";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages/custom" },
  keywords: [
    "custom software development",
    "full-stack product development",
    "private AI integration",
    "Next.js product studio",
    "Presence-First web design",
    "architecture-first development",
  ],
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
  },
};

interface Discipline {
  name: string;
  detail: string;
  href?: string;
  hrefLabel?: string;
}

const disciplines: Discipline[] = [
  {
    name: "Product engineering",
    detail:
      "Next.js, TypeScript, Postgres, Supabase, Railway. Schema to interface as one system.",
  },
  {
    name: "AI integration",
    detail:
      "Claude or OpenAI, retrieval, fine-tuning only where the data earns it. Multilingual and RTL when the audience needs it.",
  },
  {
    name: "Presence-First web design",
    detail:
      `For retreats, venues, farms, wellness, hospitality. Atmosphere first. Booking second. ${presenceFirstSummary}`,
    href: presenceFirstHref,
    hrefLabel: "See Presence-First",
  },
];

const security =
  "Not a week-before-launch checklist. Threat model in architecture. Canopy Guard at launch when the tier includes it.";

const scoping =
  "Call. One-page architecture and range. You approve the shape. Build starts. If the range is wrong for the budget, we stop there. That is a successful scoping call.";

const timeline =
  "Most custom work lands between two and eight weeks once scope is honest.";

/* ------------------------------------------------------------------ *
 * Structured data. Service with no fixed Offer, because the price is
 * scoped after a call and quoting one here would be a fiction.
 * ------------------------------------------------------------------ */

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Custom build",
  serviceType: "Custom software, private AI, and experiential web design",
  url,
  description:
    "Full-stack products, private AI inside an existing tool, or a Presence-First site. Architecture first, then build, then harden. Scoped after a call.",
  provider: { "@id": "https://merakislove.com/#organization" },
  areaServed: "Worldwide",
  hasOfferCatalog: {
    "@type": "OfferCatalog",
    name: "Custom build disciplines",
    itemListElement: disciplines.map((discipline) => ({
      "@type": "Offer",
      itemOffered: {
        "@type": "Service",
        name: discipline.name,
        description: discipline.detail,
        url: discipline.href
          ? `https://merakislove.com${discipline.href}`
          : url,
      },
    })),
  },
};


export default function CustomPackagePage() {
  return (
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <Breadcrumb
        items={[
          { name: "Packages", path: "/packages" },
          { name: "Custom build", path: "/packages/custom" },
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
        eyebrow="Custom build"
        title="When the product is the business."
        subtitle="Full-stack products, private AI inside an existing tool, or a Presence-First site for a place people travel to feel. Scoped after a call. No guesswork price on a problem I have not seen."
      />

      {/* What custom usually means */}
      <PackageSection title="What custom usually means">
        <div className="flex flex-col gap-8">
          {disciplines.map((discipline, i) => (
            <ScrollReveal key={discipline.name} delay={i * 0.06}>
              <div className="flex flex-col gap-3 border-l-2 border-amber pl-6">
                <h3 className="font-display text-2xl font-light text-smoke">
                  {discipline.name}
                </h3>
                <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
                  {discipline.detail}
                </p>
                {discipline.href ? (
                  <Link
                    href={discipline.href}
                    className="group inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:text-smoke"
                  >
                    {discipline.hrefLabel}
                    <span className="transition-transform duration-300 group-hover:translate-x-1">
                      →
                    </span>
                  </Link>
                ) : null}
              </div>
            </ScrollReveal>
          ))}
        </div>
      </PackageSection>

      {/* Security in the build */}
      <PackageSection title="Security in the build">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {security}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* How scoping works */}
      <PackageSection title="How scoping works">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {scoping}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* Timeline */}
      <PackageSection title="Timeline">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {timeline}
          </p>
          <PackageActions label={pkg.cta} />
        </ScrollReveal>
      </PackageSection>
    </div>
  );
}
