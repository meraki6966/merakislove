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
   * The hub states the custom band without a duration, because the duration
   * is not knowable before a scoping call.
   */
  hubOmitsDuration?: boolean;
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
    hubOmitsDuration: true,
    summary:
      "Full-stack product, Presence-First site, or private AI inside what you already run. Architecture first. Then code. Then harden. Presence-First sites for hospitality and experiential businesses start at $4,500.",
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

/**
 * The meta line under a package name. The hub drops the duration for the
 * custom build, where there is nothing honest to put there yet.
 */
export function packageMeta(pkg: Package, variant: "home" | "hub"): string {
  if (variant === "hub" && pkg.hubOmitsDuration) return pkg.priceLabel;
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
