// The three ways to start, shared by the homepage, the /packages hub, and
// each package's detail page under /packages/[slug]. Card bodies differ
// between surfaces on purpose: the homepage sells the shape of the thing,
// the hub explains who it is for, the detail page does the work.
//
// Prices and durations live here and nowhere else. The cards compose their
// meta line from priceLabel and duration rather than carrying a second copy
// of the same string.

/** A priced tier inside a package. Shape matches the Offer schema. */
export interface PackageTier {
  /** Name as stated in the price block. */
  name: string;
  /** Shorter label used where the copy names the tier in passing. */
  label: string;
  price: string;
  /** Numeric price for the Offer schema. */
  amount: string;
  /** What the tier covers. */
  scope: string;
}

export interface Package {
  number: string;
  name: string;
  slug: string;
  /** Price band, as stated on every surface. */
  priceLabel: string;
  /** How long the engagement runs. */
  duration: string;
  /**
   * Suppresses the duration in the card meta line. Set where a range would
   * mislead: the custom build covers a one-page flyer and a full product,
   * so a single span across both is not a useful number on a card.
   */
  omitDuration?: boolean;
  /** Lowest price as a number, for the Offer schema. Absent when scoped. */
  amount?: string;
  /** Highest price as a number, where the package is a band. */
  amountMax?: string;
  /** Homepage card body. */
  summary: string;
  /** /packages hub card body. */
  detail: string;
  /** Label on the card's action. */
  cta: string;
  /** The package's own page. */
  detailHref: string;
  /** Marks the card carrying the "Most chosen" flag. */
  featured?: boolean;
  /** Priced tiers, where the package has them. */
  tiers?: PackageTier[];
}

/* ------------------------------------------------------------------ *
 * Presence-First tiers.
 *
 * The amounts live here and nowhere else. They were previously written out
 * in five places across two pages in three different formats, so a price
 * change meant finding all five and getting each format right. Everything
 * downstream now formats from `amount`:
 *   the tier cards and Offer schema on the Presence-First page,
 *   the one-line summary on that page's close and on /packages/custom,
 *   and the "starts at" figure in prose.
 * ------------------------------------------------------------------ */

export interface PresenceTier {
  /** Full name, used on the Presence-First page itself. */
  name: string;
  /** Short name, used where the copy lists all three in one line. */
  shortName: string;
  /** Price in whole dollars. The single source. */
  amount: number;
  /** True when the price is a floor rather than a fixed figure. */
  openEnded?: boolean;
}

export const presenceFirstTiers: PresenceTier[] = [
  { name: "Essential Presence", shortName: "Essential", amount: 4500 },
  { name: "Signature Site", shortName: "Signature", amount: 7500 },
  {
    name: "Full Experience",
    shortName: "Full Experience",
    amount: 12000,
    openEnded: true,
  },
];

function dollars(amount: number): string {
  return `$${amount.toLocaleString("en-US")}`;
}

/** Long form, as the tier cards state it: "$12,000 and up". */
export function tierPrice(tier: PresenceTier): string {
  return dollars(tier.amount) + (tier.openEnded ? " and up" : "");
}

/** Short form, as the one-line summaries state it: "$12,000+". */
export function tierPriceShort(tier: PresenceTier): string {
  return dollars(tier.amount) + (tier.openEnded ? "+" : "");
}

/** Lowest tier as a bare figure, for "starts at" prose. */
export const presenceFirstFrom = dollars(
  Math.min(...presenceFirstTiers.map((t) => t.amount)),
);

/** "Essential $4,500. Signature $7,500. Full Experience $12,000+." */
export const presenceFirstSummary =
  presenceFirstTiers
    .map((t) => `${t.shortName} ${tierPriceShort(t)}`)
    .join(". ") + ".";

/** Lookup that fails loudly at build time if a name stops matching. */
export function getPresenceTier(name: string): PresenceTier {
  const found = presenceFirstTiers.find((t) => t.name === name);
  if (!found) throw new Error(`Unknown Presence-First tier: ${name}`);
  return found;
}

export const packages: Package[] = [
  {
    number: "01",
    name: "Review",
    slug: "review",
    priceLabel: "$500 to $1,500",
    duration: "5 days",
    amount: "500",
    amountMax: "1500",
    summary:
      "A CISSP-informed look at your site or your AI stack. Ranked findings. A report you can hand to a partner or a client. MITRE ATT&CK mapping when it applies. Best when you already have tools and need to know if they are safe to keep.",
    detail:
      "For teams who already have a site or an AI feature and need a straight answer. You get a written report, ranked findings, and a fix order. CISSP-informed. MITRE-mapped when the stack includes AI or a multi-tenant app.",
    cta: "Request a review",
    detailHref: "/packages/review",
    tiers: [
      {
        name: "Application security review",
        label: "Application security",
        price: "$500",
        amount: "500",
        scope:
          "Multi-tenant isolation. OAuth flows. API surface. Authorization gaps. The class of bugs that makes headlines.",
      },
      {
        name: "AI risk assessment",
        label: "AI risk",
        price: "$1,500",
        amount: "1500",
        scope:
          "Prompt injection. Data leaving through model responses. Unsafe tool wiring. Training-data and retention questions. Guardrails that exist on the slide and not in the code.",
      },
    ],
  },
  {
    number: "02",
    name: "Meraki BIP",
    slug: "bip",
    priceLabel: "From $7,000",
    duration: "6 weeks",
    amount: "7000",
    summary:
      "The system I build for service businesses. A scheduled lead engine. An assistant trained on your documents, services, and pricing. Distribution across two platforms from one dashboard. A live activity view so you can see what the system is doing. Not a plugin stack you babysit. A production system with your name on the front door.",
    detail:
      "The operating system for a service business that is tired of babysitting tools. Lead engine. Assistant trained on your documents. Two platforms. One dashboard.",
    cta: "Ask about BIP",
    detailHref: "/packages/bip",
    featured: true,
  },
  {
    number: "03",
    name: "Custom build",
    slug: "custom",
    priceLabel: "Scoped after a call",
    duration: "2 to 8 weeks",
    omitDuration: true,
    summary:
      "A new website, an executive presentation, print collateral, a full product build, or private AI inside what you already run. Scoped to what the work actually needs.",
    detail:
      "Full-stack product. Presence-First site. Private AI inside a tool you already run. Architecture first. Then build. Then harden.",
    cta: "Book a scoping call",
    detailHref: "/packages/custom",
  },
];

/** Lookup for the detail pages, which each render exactly one package. */
export function getPackage(slug: string): Package {
  const found = packages.find((p) => p.slug === slug);
  if (!found) throw new Error(`Unknown package slug: ${slug}`);
  return found;
}

/** The meta line under a package name, on every surface that shows a card. */
export function packageMeta(pkg: Package): string {
  if (pkg.omitDuration) return pkg.priceLabel;
  return `${pkg.priceLabel} · ${pkg.duration}`;
}

export interface EngagementType {
  name: string;
  detail: string;
}

export const engagementTypes: EngagementType[] = [
  { name: "Project", detail: "Fixed scope, clear deliverable, clear date." },
  { name: "Hourly", detail: "$85/hr for audits, advisory, and contained work." },
  {
    name: "Retainer",
    detail:
      "After something is in production and needs steady hands. Priced to the system, not as a placeholder rate.",
  },
];
