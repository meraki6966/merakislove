export interface PillarTier {
  name: string;
  price: string;
}

export interface ServicePillar {
  number: string;
  title: string;
  description: string;
  /** A grounded proof line tied to a real project or credential. */
  proof: string;
  /** Expanded 2-3 sentence narrative with technologies and outcomes. */
  detail: string;
  capabilities: string[];
  /** Optional fixed-price tiers shown beneath the capabilities. */
  tiers?: PillarTier[];
  /** Optional dedicated page for the pillar, linked from the card. */
  href?: string;
  hrefLabel?: string;
}

export const pillars: ServicePillar[] = [
  {
    number: "01",
    title: "Product Engineering",
    description:
      "Full-stack products from the schema to the ship date. I build the data model, the API, and the interface as one system, so the thing holds together under real use.",
    detail:
      "I design and ship full-stack products end to end, from the Postgres schema through the typed API to the React interface, treating them as one coherent system rather than three handoffs. The stack is Next.js, TypeScript, and Tailwind on the front, with Supabase, Postgres, and Railway carrying the data and deployment. The outcome is software that stays fast and predictable under real production load, with a data model that does not buckle the first time traffic or scope grows.",
    proof:
      "VeloxSync runs 10 database tables, 30 plus endpoints, and 112 state standards in production.",
    capabilities: [
      "Next.js, React, and TypeScript",
      "Database design and API architecture",
      "Supabase, Postgres, and Railway",
    ],
  },
  {
    number: "02",
    title: "AI Integration",
    description:
      "AI that respects the person using it. I integrate language models, fine-tune where it earns its keep, and build the guardrails so the output is something you can stand behind.",
    detail:
      "I bring large language models into products in a way that earns trust, integrating the Claude and OpenAI APIs, adding retrieval-augmented context, and fine-tuning only where the data clearly justifies it. Every integration ships with guardrails, evaluation, and fallbacks so the output is something you can put in front of a client without flinching. The result is AI features that handle real conversation, including multilingual and right-to-left support, instead of demos that fall apart at the edges.",
    proof:
      "Meraki Lingua holds conversation across 37 language communities, dialect by dialect, on the Claude API.",
    capabilities: [
      "Claude and OpenAI integration",
      "Fine-tuned and retrieval-augmented systems",
      "Multilingual and RTL support",
    ],
  },
  {
    number: "03",
    title: "Security Posture",
    description:
      "Security built in from the first commit, not bolted on before launch. I bring a CISSP lens to the architecture, the dependencies, and the report you hand to a client.",
    detail:
      "Security is part of the architecture from the first commit, not a checklist bolted on the week before launch. I bring a CISSP lens to the threat model, the dependency tree, the headers, the TLS configuration, and the data-handling paths, then map every finding to the MITRE ATT&CK framework so the risk is concrete. You walk away with a client-ready posture report and a hardened system, the same depth of review enterprises routinely pay six figures to commission.",
    proof:
      "Canopy Guard maps findings to MITRE ATT&CK and delivers the posture report enterprises pay six figures for.",
    capabilities: [
      "CISSP-informed architecture review",
      "MITRE ATT&CK mapped findings",
      "Client-ready posture reports",
    ],
  },
  {
    number: "04",
    title: "Content & Strategy",
    description:
      "The writing and the thinking that surround the build. I help you say the true thing clearly, then point the product at the goal that actually matters.",
    detail:
      "Good software still needs the right words and the right direction around it. I write the technical documentation, the product narrative, and the brand voice, then help you aim the product at the outcome that actually matters to the business. Drawing on four published books and twenty years across leadership, IT, and information security, I turn a vague goal into positioning and messaging a team can rally behind and a customer can understand.",
    proof:
      "Four published books and twenty years across leadership, IT, and information security.",
    capabilities: [
      "Technical writing and documentation",
      "Product strategy and positioning",
      "Brand voice and messaging",
    ],
  },
  {
    number: "05",
    title: "Presence-First Web Design",
    description:
      "For hospitality venues, wellness retreats, farms, and experiential businesses. The site should carry the feeling of the place itself, so a visitor arrives already knowing how it will feel to walk in the door.",
    detail:
      "Presence-First Web Design is for the businesses people travel to feel something, the boutique hotels, wellness retreats, working farms, and experiential venues whose whole value is atmosphere. I build these on Next.js with GSAP-driven motion, treating scroll, pacing, and imagery as the way the place introduces itself. The result is a site that does not just list amenities but sets a mood, so the booking decision is half made before the visitor ever reads the rates.",
    proof: "Sites that feel like the place before you've ever been there.",
    capabilities: [
      "Next.js with GSAP animations",
      "Atmosphere-led art direction",
      "Hospitality and experiential venues",
    ],
    tiers: [
      { name: "Essential Presence", price: "$4,500" },
      { name: "Signature Site", price: "$7,500" },
      { name: "Full Experience", price: "$12,000+" },
    ],
    href: "/services/presence-first-web-design",
    hrefLabel: "See what a Presence-First site includes",
  },
];

export interface EngagementModel {
  name: string;
  rate: string;
  description: string;
  available: boolean;
}

export const engagementModels: EngagementModel[] = [
  {
    name: "Hourly",
    rate: "$85 / hr",
    description:
      "For focused work, audits, and advisory. Senior hands on the problem without a long contract.",
    available: true,
  },
  {
    name: "Project",
    rate: "Fixed scope",
    description:
      "A defined build with a clear deliverable and timeline. We agree on the shape of it before a line of code is written.",
    available: true,
  },
  {
    name: "Retainer",
    rate: "$200+/mo",
    description:
      "Ongoing partnership for teams that need steady hands month over month.",
    available: true,
  },
];

export interface ProcessStep {
  number: string;
  title: string;
  description: string;
}

export const processSteps: ProcessStep[] = [
  {
    number: "01",
    title: "Discovery",
    description:
      "We start in conversation. I learn the people, the constraints, and the real goal before proposing anything.",
  },
  {
    number: "02",
    title: "Architecture",
    description:
      "I map the system. The data model, the integrations, and the security posture, decided up front.",
  },
  {
    number: "03",
    title: "Build",
    description:
      "The work gets made. Tight feedback loops, real progress you can see, and no black box.",
  },
  {
    number: "04",
    title: "Deploy and Harden",
    description:
      "We ship, then we secure. Monitoring, hardening, and a posture you can stand behind.",
  },
];
