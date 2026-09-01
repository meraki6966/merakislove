// The three ways to start, shared by the homepage and the /packages hub so
// the price bands and names live in one place. Card bodies differ between
// the two surfaces on purpose: the homepage sells the shape of the thing,
// the hub explains who it is for.

export interface Package {
  number: string;
  name: string;
  slug: string;
  /** Price and timeline line shown on the homepage card. */
  meta: string;
  /** Overrides meta on the /packages hub when the hub states it differently. */
  hubMeta?: string;
  /** Homepage card body. */
  summary: string;
  /** /packages hub card body. */
  detail: string;
  /** Label on the card's action. */
  cta: string;
  /**
   * Phase 2 detail page. The routes do not exist yet, so nothing links here
   * and every card action points at /start instead. Wire the "See what's
   * included" link up when /packages/[slug] ships.
   */
  detailHref: string;
  /** Marks the card carrying the "Most chosen" flag. */
  featured?: boolean;
}

export const packages: Package[] = [
  {
    number: "01",
    name: "Review",
    slug: "review",
    meta: "$500 to $1,500 · 5 days",
    summary:
      "A CISSP-informed look at your site or your AI stack. Ranked findings. A report you can hand to a partner or a client. MITRE ATT&CK mapping when it applies. Best when you already have tools and need to know if they are safe to keep.",
    detail:
      "For teams who already have a site or an AI feature and need a straight answer. You get a written report, ranked findings, and a fix order. CISSP-informed. MITRE-mapped when the stack includes AI or a multi-tenant app.",
    cta: "Request a review",
    detailHref: "/packages/review",
  },
  {
    number: "02",
    name: "Meraki BIP",
    slug: "bip",
    meta: "From $7,000 · 6 weeks",
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
    meta: "Scoped after a call · 2 to 8 weeks",
    hubMeta: "Scoped after a call",
    summary:
      "Full-stack product, Presence-First site, or private AI inside what you already run. Architecture first. Then code. Then harden. Presence-First sites for hospitality and experiential businesses start at $4,500.",
    detail:
      "Full-stack product. Presence-First site. Private AI inside a tool you already run. Architecture first. Then build. Then harden.",
    cta: "Book a scoping call",
    detailHref: "/packages/custom",
  },
];

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
