import type { Metadata } from "next";
import Link from "next/link";
import Image from "next/image";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import PackageSection from "@/components/PackageSection";
import PackageActions from "@/components/PackageActions";
import TiltCard from "@/components/TiltCard";
import Tag from "@/components/Tag";
import Breadcrumb from "@/components/Breadcrumb";
import { starterSiteTiers, starterSiteAddOn } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const title = "Starter Sites | Meraki is Love";

const description =
  "A real website, built fast, priced fair. Live examples included.";

const url = "https://merakislove.com/packages/starter-sites";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages/starter-sites" },
  keywords: [
    "small business website",
    "restaurant website design",
    "gym website design",
    "salon website design",
    "affordable website design",
    "local business website",
  ],
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
  },
};

const trustLine =
  "Veteran-owned. Built by someone who does the work himself, not routed through a sales team.";

interface LiveExample {
  name: string;
  category: string;
  href: string;
}

const liveExamples: LiveExample[] = [
  {
    name: "The Corner Table",
    category: "Restaurant, hospitality",
    href: "/demos/restaurant",
  },
  {
    name: "Iron Prism",
    category: "Fitness, gym",
    href: "/demos/iron-prism",
  },
  {
    name: "Anchor Home Services",
    category: "Trades, home services",
    href: "/demos/anchor",
  },
  {
    name: "Hazel & Row",
    category: "Salon, personal care",
    href: "/demos/hazel-and-row",
  },
];

const liveExamplesClose =
  "Pick whichever style is closest to your business. We adapt it to you.";

interface Flyer {
  file: string;
  business: string;
  caption: string;
  alt: string;
  width: number;
  height: number;
}

/**
 * Flyer source files ship as delivered by the design pass, each at its own
 * aspect ratio rather than cropped to a shared one: a flyer is a finished
 * layout, and cropping any of these would cut real content rather than
 * trim empty margin. width/height are each file's real pixel dimensions,
 * so the grid tile reserves the exact shape instead of forcing a square.
 */
const flyers: Flyer[] = [
  {
    file: "corner-table.jpg",
    business: "The Corner Table",
    caption: "Fall specials flyer",
    alt: "The Corner Table fall specials flyer, an ornate template design with a ribbon banner and decorative border framing a circular photo of roasted chicken with vegetables.",
    width: 1189,
    height: 1600,
  },
  {
    file: "iron-prism.jpg",
    business: "Iron Prism",
    caption: "6-week strength challenge flyer",
    alt: "Iron Prism 6-week strength challenge flyer, a black and white gym photo with orange accent stripes.",
    width: 928,
    height: 1200,
  },
  {
    file: "anchor.jpg",
    business: "Anchor Home Services",
    caption: "Fall HVAC tune-up flyer",
    alt: "Anchor Home Services fall HVAC tune-up flyer, listing electrical and HVAC services on a black background.",
    width: 849,
    height: 1200,
  },
  {
    file: "hazel-row.jpg",
    business: "Hazel & Row",
    caption: "New stylist announcement flyer",
    alt: "Hazel & Row new stylist announcement flyer, a tan leather and brass armchair in an emerald parlor under a New Season, New Stylist headline.",
    width: 1200,
    height: 1600,
  },
  {
    file: "blend-state.jpg",
    business: "Blend State",
    caption: "New flavor launch flyer",
    alt: "Blend State mango sunrise milkshake flyer, with strawberries and a smoothie glass on a pink background.",
    width: 675,
    height: 1200,
  },
];

const flyerCaption =
  "Every flyer built in the business's own colors, type, and voice. This is what the $400 add-on actually gets you.";

const aLaCarte = [
  "Extra pages.",
  "Ongoing monthly visibility work.",
  "Photography help.",
  "Copywriting.",
  "Google Business Profile setup.",
  "Social account setup.",
  "Rush turnaround.",
  "Extra revision rounds.",
  "A Canopy Guard visibility scan, a real scored look at your SEO and whether AI tools like ChatGPT would even recommend you.",
];

/* ------------------------------------------------------------------ *
 * Structured data. Service with a priced Offer per tier plus the add-on,
 * matching the pattern the review page established.
 * ------------------------------------------------------------------ */

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Starter Sites",
  serviceType: "Small business website design",
  url,
  description,
  provider: { "@id": "https://merakislove.com/#organization" },
  areaServed: "Worldwide",
  audience: {
    "@type": "BusinessAudience",
    name: "Restaurants, gyms, salons, and trades needing a fast, affordable site",
  },
  offers: [...starterSiteTiers, starterSiteAddOn].map((tier) => ({
    "@type": "Offer",
    name: tier.name,
    price: tier.amount,
    priceCurrency: "USD",
    description: tier.scope,
    url,
  })),
};

export default function StarterSitesPage() {
  return (
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <Breadcrumb
        items={[
          { name: "Packages", path: "/packages" },
          { name: "Starter Sites", path: "/packages/starter-sites" },
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
        eyebrow="Starter Sites"
        title="A real website, built fast, priced fair."
        subtitle="Not a custom build. Not an AI system. A clean, working site for a business that needs to be found and look right doing it."
      />

      <ScrollReveal delay={0.1}>
        <p className="mt-5 max-w-2xl font-body text-sm leading-relaxed text-smoke">
          {trustLine}
        </p>
      </ScrollReveal>

      {/* Price */}
      <PackageSection title="Price">
        <div className="grid gap-6 sm:grid-cols-3">
          {[...starterSiteTiers, starterSiteAddOn].map((tier, i) => (
            <ScrollReveal key={tier.name} delay={i * 0.08} className="h-full">
              <TiltCard className="h-full bg-navy/40">
                <div className="flex h-full flex-col gap-4 p-7">
                  <h3 className="font-display text-2xl font-light leading-tight text-smoke">
                    {tier.name}
                  </h3>
                  <div className="mt-auto flex flex-col gap-1">
                    <p className="font-display text-4xl font-light text-amber">
                      {tier.price}
                    </p>
                    {tier === starterSiteAddOn ? (
                      <p className="font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim">
                        Add to either tier
                      </p>
                    ) : null}
                  </div>
                </div>
              </TiltCard>
            </ScrollReveal>
          ))}
        </div>
      </PackageSection>

      {/* What's included */}
      <PackageSection title="What's included">
        <div className="flex flex-col gap-6">
          {[...starterSiteTiers, starterSiteAddOn].map((tier, i) => (
            <ScrollReveal key={tier.name} delay={i * 0.06}>
              <div className="flex flex-col gap-3 border-l-2 border-amber pl-6">
                <div className="flex flex-wrap items-center gap-3">
                  <span className="font-mono text-sm tracking-[0.16em] text-amber">
                    {tier.price}
                  </span>
                  <span className="font-display text-xl font-light text-smoke">
                    {tier.name}
                  </span>
                </div>
                <p className="max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
                  {tier.scope}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </PackageSection>

      {/* See it before you buy it */}
      <PackageSection
        title="See it before you buy it"
        lead="These aren't mockups. Real, live templates you can click through right now."
      >
        <div className="grid gap-6 sm:grid-cols-2">
          {liveExamples.map((example, i) => (
            <ScrollReveal key={example.name} delay={i * 0.06} className="h-full">
              <TiltCard className="h-full bg-navy/40">
                <div className="flex h-full flex-col gap-4 p-7">
                  <div className="flex flex-col gap-2">
                    <h3 className="font-display text-2xl font-light leading-tight text-smoke">
                      {example.name}
                    </h3>
                    <Tag>{example.category}</Tag>
                  </div>
                  <a
                    href={example.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group mt-auto inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:text-smoke"
                  >
                    View the live demo
                    <span className="transition-transform duration-300 group-hover:translate-x-1">
                      →
                    </span>
                  </a>
                </div>
              </TiltCard>
            </ScrollReveal>
          ))}
        </div>
        <ScrollReveal delay={0.1} className="mt-8">
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {liveExamplesClose}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* See the marketing package in action */}
      <PackageSection
        title="See the marketing package in action"
        lead="Five businesses, five identities, real branded content, not a template with a logo swapped in."
      >
        {/* Widest render measured at 547px, single column at a 639px
            viewport, NOT the steady 227px desktop tile once lg:grid-cols-3
            kicks in at 1024px. sizes below is set from that measurement. */}
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {flyers.map((flyer, i) => (
            <ScrollReveal key={flyer.file} delay={i * 0.05} className="h-full">
              <TiltCard className="h-full bg-navy/40">
                <div className="flex h-full flex-col gap-4 p-4">
                  <div
                    className="relative w-full overflow-hidden rounded-lg"
                    style={{ aspectRatio: `${flyer.width} / ${flyer.height}` }}
                  >
                    <Image
                      src={`/demos/starter-sites/flyers/${flyer.file}`}
                      alt={flyer.alt}
                      fill
                      sizes="(min-width: 1024px) 227px, (min-width: 640px) 41vw, 92vw"
                      className="object-cover"
                    />
                  </div>
                  <div className="flex flex-col gap-1 px-1 pb-1">
                    <p className="font-display text-lg font-light text-smoke">
                      {flyer.business}
                    </p>
                    <p className="font-mono text-xs uppercase tracking-[0.14em] text-smoke-dim">
                      {flyer.caption}
                    </p>
                  </div>
                </div>
              </TiltCard>
            </ScrollReveal>
          ))}
        </div>
        <ScrollReveal delay={0.1} className="mt-8">
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {flyerCaption}
          </p>
        </ScrollReveal>
      </PackageSection>

      {/* A la carte */}
      <PackageSection title="A la carte, if you need more">
        <ScrollReveal>
          <ul className="flex flex-wrap gap-2.5">
            {aLaCarte.map((item) => (
              <li key={item}>
                <Tag>{item}</Tag>
              </li>
            ))}
          </ul>
        </ScrollReveal>
      </PackageSection>

      {/* What this is not */}
      <PackageSection title="What this is not">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            Not a custom architecture build. Not an AI integration. Need
            either of those later?{" "}
            <Link
              href="/packages/custom"
              className="text-amber transition-colors duration-300 hover:text-smoke"
            >
              Custom build
            </Link>{" "}
            is the next door up.
          </p>
          <PackageActions label="Get started" />
        </ScrollReveal>
      </PackageSection>
    </div>
  );
}
