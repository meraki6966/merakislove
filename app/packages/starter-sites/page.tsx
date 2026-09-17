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
import Faq, { type FaqItem } from "@/components/Faq";
import { starterSiteTiers, starterSiteAddOn } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const title = "Starter Sites $500 and $1,000 | Adam McClarin | Meraki is Love";

// 140 characters, verified programmatically against the 155-char limit
// before this went in (see the PR description / session notes).
const description =
  "Adam McClarin at Meraki is Love builds Starter Sites for small businesses. $500 one page or $1,000 up to five pages. Live demos. Nationwide.";

const url = "https://merakislove.com/packages/starter-sites";

// Real screenshot of this page (captured via the browser tool, not a
// generated graphic) used for the social card.
const ogImage = {
  url: "https://merakislove.com/og/starter-sites.png",
  width: 1512,
  height: 790,
  alt: "Starter Sites pricing and page preview on merakislove.com",
};

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
    images: [ogImage],
  },
  twitter: {
    card: "summary_large_image",
    title,
    description,
    images: [ogImage.url],
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
];

const canopyGuardMention =
  "A Canopy Guard visibility scan, a real scored look at your SEO and whether AI tools like ChatGPT would even recommend you, is available separately as an add-on.";

const whoBuildsBody =
  "Starter Sites is the small business website package at Meraki is Love, built by Adam McClarin. The person on the call is the person who ships.";

/**
 * Verbatim comparison copy. Word order and phrasing are load-bearing for the
 * page's first-100-words SEO requirement (Adam McClarin, Meraki is Love,
 * Starter Sites, small business website, $500, $1,000 all land before word
 * 100 once this section is placed right after the price block), so don't
 * reorder or trim these paragraphs without re-checking that.
 */
const whatThisIsNextTo = [
  "Wix and Squarespace are tools. You still have to finish the site. Plan cost runs about $16 to $29 a month.",
  "A marketplace gig at $200 to $600 is usually a theme with your logo dropped in. You manage a seller. In six months there is no one to call.",
  "A mid freelance five-page site often runs $1,000 to $3,000. Agencies start higher than that.",
  "Starter Sites is a working page adapted from a live demo you can click before you pay. $500 for one page. $1,000 for up to five pages and a contact or booking path. Built by Adam McClarin at Meraki is Love. The person on the call is the person who ships.",
];

const whatYouGet = [
  "You click Corner Table, Iron Prism, Anchor, or Hazel first.",
  "You talk to one owner. Nationwide.",
  "After launch I can scan the live URL with Canopy Guard for search, AI answers, and visible security.",
];

// First sentence ("Not Meraki BIP. Not a five day security review. Not a
// custom product.") is rendered inline in JSX below with a link wrapped
// around "custom product" — same words, just addressable.
const whatThisIsNot =
  "If you need photos, extra pages, or a store, we add that after. Hosting and domain are separate unless we agree in writing.";

const starterFaqs: FaqItem[] = [
  {
    id: "what-is-a-starter-site-answer",
    question: "What is a Starter Site from Meraki is Love?",
    answer:
      "A Starter Site is a simple small business website built by Adam McClarin. One page is $500. Up to five pages is $1,000. You can click live demos before you buy.",
  },
  {
    question: "Who is Adam McClarin?",
    answer:
      "Adam McClarin is the founder of Meraki is Love, a studio that builds websites and private AI for service businesses. He takes the call and ships the work himself.",
  },
  {
    question: "How much does a small business website from Adam McClarin cost?",
    answer:
      "Starter Sites are $500 for one page and $1,000 for up to five pages. Custom work and Meraki BIP are separate offers.",
  },
  {
    question: "Is a Starter Site the same as Wix or Fiverr?",
    answer:
      "No. Wix is a tool you still have to finish. A Fiverr gig is usually a theme and a seller. A Starter Site is built by Adam McClarin from a live demo you can click first.",
  },
  {
    question: "Where does Meraki is Love work?",
    answer:
      "Nationwide. The studio serves service businesses and shops across the United States.",
  },
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

/**
 * Standalone Offer entities for the two Starter Sites tiers (not the
 * add-on), independently addressable via @id rather than only nested inside
 * serviceSchema.offers above.
 */
const starterOfferSchema = {
  "@context": "https://schema.org",
  "@type": "Offer",
  "@id": `${url}/#offer-starter`,
  name: "Starter",
  price: starterSiteTiers[0].amount,
  priceCurrency: "USD",
  url,
  itemOffered: { "@id": `${url}/#service` },
};

const starterPlusOfferSchema = {
  "@context": "https://schema.org",
  "@type": "Offer",
  "@id": `${url}/#offer-starter-plus`,
  name: "Starter Plus",
  price: starterSiteTiers[1].amount,
  priceCurrency: "USD",
  url,
  itemOffered: { "@id": `${url}/#service` },
};

/**
 * Founder Person schema. No sameAs: no Dribbble URL exists anywhere in this
 * repo, and the brief for this page was explicit not to invent one.
 */
const personSchema = {
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://merakislove.com/#person-adam-mcclarin",
  name: "Adam McClarin",
  jobTitle: "Founder",
  url: "https://merakislove.com",
};

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": `${url}/#faq`,
  mainEntity: starterFaqs.map((item) => ({
    "@type": "Question",
    name: item.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: item.answer,
    },
  })),
};

/**
 * speakable.cssSelector targets the "What is a Starter Site" answer's id,
 * set on the Faq component via FaqItem.id.
 */
const webPageSchema = {
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@id": `${url}/#webpage`,
  url,
  name: title,
  description,
  speakable: {
    "@type": "SpeakableSpecification",
    cssSelector: ["#what-is-a-starter-site-answer"],
  },
};

const starterSitesSchemas = [
  serviceSchema,
  starterOfferSchema,
  starterPlusOfferSchema,
  personSchema,
  faqSchema,
  webPageSchema,
];

export default function StarterSitesPage() {
  return (
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <Breadcrumb
        items={[
          { name: "Packages", path: "/packages" },
          { name: "Starter Sites", path: "/packages/starter-sites" },
        ]}
      />

      {starterSitesSchemas.map((schema, i) => (
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
      <PackageSection title="Starter Sites pricing">
        <div className="grid gap-6 sm:grid-cols-2">
          {starterSiteTiers.map((tier, i) => (
            <ScrollReveal key={tier.name} delay={i * 0.08} className="h-full">
              <TiltCard className="h-full bg-navy/70 ring-1 ring-inset ring-gold/50">
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

        {/* Add-on: deliberately a slim, lower-weight strip beneath the two
            main tiers rather than a third equal-size card. */}
        <ScrollReveal delay={0.16} className="mt-6">
          <div className="flex flex-col items-start justify-between gap-3 rounded-xl border border-border-mid bg-navy/30 px-6 py-5 sm:flex-row sm:items-center">
            <div className="flex flex-col gap-1">
              <p className="font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim">
                Add to either tier
              </p>
              <p className="font-display text-lg font-light text-smoke">
                {starterSiteAddOn.name}
              </p>
            </div>
            <p className="font-display text-2xl font-light text-amber">
              {starterSiteAddOn.price}
            </p>
          </div>
        </ScrollReveal>
      </PackageSection>

      {/* Who builds Starter Sites. Short, front-loaded on purpose: this is
          the earliest point after the price block where Adam McClarin,
          Meraki is Love, and "small business website" can land, which keeps
          them inside the page's first 100 words alongside the $500/$1,000
          already shown above. */}
      <PackageSection title="Who builds Starter Sites">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {whoBuildsBody}
          </p>
        </ScrollReveal>
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

      {/* What this is next to */}
      <PackageSection title="What this is next to">
        <div className="flex flex-col gap-5">
          {whatThisIsNextTo.map((paragraph, i) => (
            <ScrollReveal key={i} delay={i * 0.05}>
              <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
                {paragraph}
              </p>
            </ScrollReveal>
          ))}
        </div>

        <ScrollReveal delay={0.2} className="mt-10 flex flex-col gap-4">
          <h3 className="font-display text-xl font-light text-smoke">
            What you get that the cheap gig does not
          </h3>
          <ul className="flex flex-col gap-2">
            {whatYouGet.map((line) => (
              <li
                key={line}
                className="flex items-start gap-3 font-body text-sm leading-relaxed text-smoke-dim"
              >
                <span
                  aria-hidden
                  className="mt-2 h-1 w-1 shrink-0 rounded-full bg-amber"
                />
                {line}
              </li>
            ))}
          </ul>
        </ScrollReveal>
      </PackageSection>

      {/* Live demos */}
      <PackageSection
        title="Live demos"
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

      {/* FAQ */}
      <PackageSection title="FAQ">
        <ScrollReveal>
          <Faq items={starterFaqs} />
        </ScrollReveal>
      </PackageSection>

      {/* What this is not */}
      <PackageSection title="What this is not">
        <ScrollReveal>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            Not Meraki BIP. Not a five day security review. Not a{" "}
            <Link
              href="/packages/custom"
              className="text-amber transition-colors duration-300 hover:text-smoke"
            >
              custom product
            </Link>
            .
          </p>
          <p className="mt-4 max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {whatThisIsNot}
          </p>
          <p className="mt-4 max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
            {canopyGuardMention}
          </p>
          <PackageActions label="Book this site" />
        </ScrollReveal>
      </PackageSection>
    </div>
  );
}
