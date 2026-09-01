import type { Metadata } from "next";
import Link from "next/link";
import PresenceMotion from "@/components/PresenceMotion";
import Breadcrumb from "@/components/Breadcrumb";
import { calendly, ogBase } from "@/lib/site";
import {
  getPresenceTier,
  presenceFirstFrom,
  presenceFirstSummary,
  tierPrice,
  type PresenceTier,
} from "@/lib/packages";
import styles from "@/styles/presence.module.css";

const title = "Presence-First Web Design — Meraki is Love";

const description = `Immersive, experience-first websites for hospitality, wellness, and boutique brands. GSAP-powered design that makes visitors feel something before they ever book. Starting at ${presenceFirstFrom}.`;

const url = "https://merakislove.com/packages/presence-first-web-design";

export const metadata: Metadata = {
  // Absolute so the page carries the full brand name rather than the
  // layout's "· Soulful Tech" template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages/presence-first-web-design" },
  keywords: [
    "presence-first web design",
    "hospitality web design",
    "wellness website design",
    "farm retreat website",
    "GSAP scroll animation",
    "boutique venue website",
    "experiential web design",
  ],
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
  },
};

/* ------------------------------------------------------------------ *
 * Copy
 * ------------------------------------------------------------------ */

const heroCopy = [
  "Most sites tell people what you do. A Presence-First site makes them feel something before they even book. It is the difference between a brochure and an invitation.",
  "Built for hospitality venues, wellness retreats, farms, event spaces, boutique restaurants, and any business where the experience is the product.",
];

const positioning = [
  "There is a category of business where a standard template is not just a missed opportunity, it is actively working against you.",
  "A farm retreat, a wellness studio, a boutique event venue. These places have something most businesses do not: an atmosphere. A feeling. Something that cannot be put into a pricing table or a feature list. People do not choose these places based on specs. They choose them based on whether they felt something when they landed on the page.",
  "That is what Presence-First Web Design is built to do.",
  "Every site I build in this tier opens with an enter gate, a full-screen moment that separates where the visitor just was from where they are now. It uses GSAP-powered scroll animations so elements reveal themselves as the user moves down the page, not all at once. The typography is chosen for the client's world, not pulled from a default list. The layout is built around the feeling of the place, not a grid template.",
  "The result is a site that earns the price point your business deserves.",
];

const audience = [
  "Farm retreats and agritourism destinations",
  "Wellness studios and yoga spaces",
  "Boutique event venues and wedding destinations",
  "Nature-based experience providers",
  "Boutique restaurants and hospitality brands",
  "Retreat centers and workshop hosts",
  "Spa and beauty brands with a story to tell",
];

const audienceClose =
  "If you are competing on atmosphere and not on price, this is the right investment.";

/**
 * Name and price come from lib/packages.ts, which is the only place the
 * numbers live. Everything below is the page's own descriptive content.
 */
interface Tier extends PresenceTier {
  bestFor: string;
  /** Optional "Everything in X, plus" line above the feature list. */
  carry?: string;
  features: string[];
  delivery: string;
  featured?: boolean;
}

const tiers: Tier[] = [
  {
    ...getPresenceTier("Essential Presence"),
    bestFor:
      "New or early-stage businesses that need a strong first impression without the full build.",
    features: [
      "Custom enter gate with GSAP curtain animation",
      "4 core pages: Home, About, Experiences, Contact",
      "Scroll-triggered section reveals throughout",
      "Marquee or ticker strip for services and offerings",
      "Mobile responsive, performance optimized",
      "Deployed to Vercel with custom domain setup",
      "Google Analytics connected",
    ],
    delivery: "Delivery: 2 weeks",
  },
  {
    ...getPresenceTier("Signature Site"),
    bestFor:
      "Established businesses ready to upgrade their digital presence to match what they offer in person.",
    carry: "Everything in Essential, plus",
    features: [
      "Up to 8 pages including a gallery, booking, events, and blog-ready structure",
      "Parallax image sections",
      "Hover-reveal card interactions on offerings grid",
      "Featured split-layout section with parallax image",
      "Stats or social proof section with scroll-triggered count animation",
      "Third-party booking integration (Calendly, FareHarbor, or similar)",
      "Email capture with lead magnet setup",
      "2 rounds of revisions",
    ],
    delivery: "Delivery: 4 weeks",
    featured: true,
  },
  {
    ...getPresenceTier("Full Experience"),
    bestFor:
      "Destination businesses, multi-offering venues, and anyone who wants a site that can grow with them for the next five years.",
    carry: "Everything in Signature, plus",
    features: [
      "Full CMS integration (Sanity or Contentful) so the client manages their own content",
      "Custom page templates for events, workshops, and private bookings",
      "Advanced GSAP interactions and custom transition sequences",
      "Multi-section homepage with three or more distinct story beats",
      "Waitlist or membership capture flow",
      "SEO foundation with schema markup, AEO structure, and llms.txt",
      "Canopy Guard audit at launch to confirm security and visibility scores",
      "90-day support window post-launch",
    ],
    delivery: "Delivery: 6 to 8 weeks",
  },
];

interface Step {
  number: string;
  when: string;
  title: string;
  body: string;
}

const steps: Step[] = [
  {
    number: "01",
    when: "Week 1",
    title: "Discovery and direction",
    body: "One 60-minute call to understand the business, the feeling they want to create, and who they are trying to reach. I leave with a clear picture of the visual world, the language, and the one thing the site needs to make people feel.",
  },
  {
    number: "02",
    when: "Week 1 to 2",
    title: "Design and copy",
    body: "I develop the visual direction, font pairing, palette, and layout structure. I write all placeholder copy in the client's voice. The client sees a design direction document before a single line of code is written.",
  },
  {
    number: "03",
    when: "Week 2 to 3",
    title: "Build",
    body: "Development in Next.js with GSAP animations layered in. The enter gate and hero are built first so the client can see the feel of the site before the rest of the pages are complete.",
  },
  {
    number: "04",
    when: "Week 3 to 4",
    title: "Review and revisions",
    body: "The client reviews the full build on a staging URL. Two rounds of revisions are included for Signature and Full Experience tiers.",
  },
  {
    number: "05",
    when: "Final week",
    title: "Launch",
    body: "Domain connected, Vercel deployment confirmed, analytics live. A Canopy Guard audit runs at launch to confirm the site's security posture and visibility signals. The client gets a short walkthrough video showing them how to use any CMS tools.",
  },
];

const stack: [string, string][] = [
  ["Framework", "Next.js"],
  ["Animation", "GSAP (ScrollTrigger, timeline, marquee)"],
  ["Deployment", "Vercel"],
  ["CMS (Tier 3)", "Sanity or Contentful"],
  ["Fonts", "Google Fonts (custom per client)"],
  ["Forms", "Formspree or native API route"],
  ["Booking", "Calendly, FareHarbor, or custom"],
  ["Audit", "Canopy Guard at launch"],
];

const caseText =
  "The brief: make someone feel a place before they have ever visited it. An enter gate creates a moment of arrival. Scroll-triggered reveals pace the story so nothing is visible all at once. The layout alternates between wide atmospheric sections and tight specific details, the way a good tour guide moves between the large view and the small one.";

/* ------------------------------------------------------------------ *
 * Structured data — Service with priced offers, so the tiers are
 * legible to search and to AI engines the same way the page is.
 * ------------------------------------------------------------------ */

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Presence-First Web Design",
  serviceType: "Experiential web design",
  url,
  description,
  provider: { "@id": "https://merakislove.com/#organization" },
  areaServed: "Worldwide",
  audience: {
    "@type": "BusinessAudience",
    name: "Hospitality venues, wellness retreats, farms, event spaces, and boutique restaurants",
  },
  offers: tiers.map((tier) => ({
    "@type": "Offer",
    name: tier.name,
    price: String(tier.amount),
    priceCurrency: "USD",
    description: tier.bestFor,
    url,
  })),
};


export default function PresenceFirstWebDesignPage() {
  return (
    <PresenceMotion className={styles.page}>
      <Breadcrumb
        items={[
          { name: "Packages", path: "/packages" },
          { name: "Presence-First Web Design", path: "/packages/presence-first-web-design" },
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

      {/* Motion hides these elements until GSAP reveals them; without JS
          there is nothing to reveal them, so put them back. */}
      <noscript>
        <style
          dangerouslySetInnerHTML={{
            __html:
              "[data-pf-reveal],[data-pf-hero]{opacity:1 !important;transform:none !important}",
          }}
        />
      </noscript>

      {/* ---------------------------------------------------------- *
       * 1 — Hero
       * ---------------------------------------------------------- */}
      <section className={styles.hero}>
        <div aria-hidden className={styles.heroGlow} />
        <div className={styles.container}>
          <p data-pf-hero className={styles.eyebrow}>
            Web Design / Experiential
          </p>

          <h1 data-pf-hero className={styles.heroTitle}>
            Your website should feel like walking through your front door.
          </h1>

          <div data-pf-hero className={styles.heroCopy}>
            {heroCopy.map((paragraph) => (
              <p key={paragraph}>{paragraph}</p>
            ))}
            {/* Routing line: this page is one custom path among three, and a
                visitor who wants leads and an assistant belongs on BIP. */}
            <p>
              This is one custom path. If you run a practice and need leads and
              an assistant, go to{" "}
              <Link href="/packages/bip" className={styles.inlineLink}>
                Meraki BIP
              </Link>
              . If you run a place people travel to feel, stay here.
            </p>
          </div>

          <div data-pf-hero className={styles.ctaRow}>
            <a href="#see-it-in-motion" className={styles.buttonGhost}>
              See the work
            </a>
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.buttonSolid}
            >
              Schedule a call
              <span aria-hidden className={styles.arrow}>
                →
              </span>
            </a>
          </div>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 2 — The problem / positioning
       * ---------------------------------------------------------- */}
      <section className={`${styles.section} ${styles.sectionMoss}`}>
        <div className={styles.narrow}>
          {positioning.map((paragraph, i) => (
            <p
              key={paragraph}
              data-pf-reveal
              data-pf-delay={i === 0 ? undefined : "0.05"}
              className={styles.prose}
            >
              {paragraph}
            </p>
          ))}
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 3 — Who this is for
       * ---------------------------------------------------------- */}
      <section className={styles.section}>
        <div className={styles.container}>
          <h2 data-pf-reveal className={styles.sectionTitle}>
            Who this is for
          </h2>

          <ul className={styles.audienceList}>
            {audience.map((item, i) => (
              <li
                key={item}
                data-pf-reveal
                data-pf-delay={(i * 0.04).toFixed(2)}
                className={styles.audienceItem}
              >
                <span aria-hidden className={styles.marker} />
                {item}
              </li>
            ))}
          </ul>

          <p data-pf-reveal className={styles.audienceClose}>
            {audienceClose}
          </p>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 4 — Pricing tiers
       * ---------------------------------------------------------- */}
      <section className={`${styles.section} ${styles.sectionMoss}`}>
        <div className={styles.container}>
          <h2 data-pf-reveal className={styles.sectionTitle}>
            What&rsquo;s included
          </h2>

          <div className={styles.tierGrid}>
            {tiers.map((tier, i) => (
              <article
                key={tier.name}
                data-pf-reveal
                data-pf-delay={(i * 0.08).toFixed(2)}
                className={`${styles.tierCard} ${
                  tier.featured ? styles.tierFeatured : ""
                }`}
              >
                {tier.featured ? (
                  <p className={styles.tierFlag}>Most chosen</p>
                ) : null}

                <h3 className={styles.tierName}>{tier.name}</h3>
                <p className={styles.tierPrice}>{tierPrice(tier)}</p>

                <p className={styles.tierBestFor}>
                  Best for: {tier.bestFor}
                </p>

                {tier.carry ? (
                  <p className={styles.tierCarry}>{tier.carry}</p>
                ) : null}

                <ul className={styles.tierList}>
                  {tier.features.map((feature) => (
                    <li key={feature} className={styles.tierListItem}>
                      <span aria-hidden className={styles.tierDash}>
                        —
                      </span>
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>

                <p className={styles.tierDelivery}>{tier.delivery}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 5 — The process
       * ---------------------------------------------------------- */}
      <section className={styles.section}>
        <div className={styles.container}>
          <h2 data-pf-reveal className={styles.sectionTitle}>
            How this works
          </h2>

          <ol className={styles.timeline}>
            {steps.map((step) => (
              <li key={step.number} data-pf-reveal className={styles.timelineStep}>
                <span aria-hidden className={styles.timelineDot} />
                <p className={styles.timelineWhen}>
                  {step.number} · {step.when}
                </p>
                <h3 className={styles.timelineTitle}>{step.title}</h3>
                <p className={styles.timelineBody}>{step.body}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 6 — Tech stack
       * ---------------------------------------------------------- */}
      <section className={`${styles.section} ${styles.sectionMoss}`}>
        <div className={styles.container}>
          <p data-pf-reveal className={styles.eyebrow}>
            Under the hood
          </p>

          <table data-pf-reveal className={styles.stackTable}>
            <thead>
              <tr>
                <th scope="col">Layer</th>
                <th scope="col">Technology</th>
              </tr>
            </thead>
            <tbody>
              {stack.map(([layer, technology]) => (
                <tr key={layer}>
                  <td>{layer}</td>
                  <td>{technology}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 7 — Portfolio / example
       * ---------------------------------------------------------- */}
      <section
        id="see-it-in-motion"
        className={`${styles.section} ${styles.anchor}`}
      >
        <div className={styles.container}>
          <h2 data-pf-reveal className={styles.sectionTitle}>
            See it in motion
          </h2>

          <div data-pf-reveal className={styles.caseBlock}>
            <p className={styles.caseText}>{caseText}</p>
            <p className={styles.caseNote}>
              Template demo — swap for a client build once the first one ships
            </p>
          </div>

          <p data-pf-reveal data-pf-delay="0.04" className={styles.prose}>
            The Corner Table is a second build in the same style, carried all
            the way through to a full menu and a live booking conversation.
          </p>

          <div data-pf-reveal data-pf-delay="0.08" className={styles.caseCta}>
            <a
              href="/demos/presence-first-example.html"
              target="_blank"
              rel="noopener noreferrer"
              className={styles.buttonSolid}
            >
              View the live demo
              <span aria-hidden className={styles.arrow}>
                →
              </span>
            </a>
            {/* Static file under /public, so a plain anchor rather than
                next/link, same as the demo link above it. */}
            <a
              href="/demos/restaurant"
              target="_blank"
              rel="noopener noreferrer"
              className={styles.buttonGhost}
            >
              See a working example
            </a>
          </div>
        </div>
      </section>

      {/* ---------------------------------------------------------- *
       * 8 — Closing CTA
       * ---------------------------------------------------------- */}
      <section className={styles.closing}>
        <div className={styles.container}>
          <h2 data-pf-reveal className={styles.closingTitle}>
            Let&rsquo;s build the site your business deserves.
          </h2>

          <p data-pf-reveal data-pf-delay="0.06" className={styles.closingSub}>
            One call. No pressure. Just a conversation about what you&rsquo;re
            building.
          </p>

          <p
            data-pf-reveal
            data-pf-delay="0.09"
            className={styles.closingPrices}
          >
            {presenceFirstSummary}
          </p>

          <div
            data-pf-reveal
            data-pf-delay="0.12"
            className={styles.closingCta}
          >
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className={styles.buttonSolid}
            >
              Schedule a call
              <span aria-hidden className={styles.arrow}>
                →
              </span>
            </a>
            <Link href="/packages" className={styles.buttonGhost}>
              See all packages
            </Link>
          </div>
        </div>
      </section>
    </PresenceMotion>
  );
}
