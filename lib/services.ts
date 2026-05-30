export interface ServicePillar {
  number: string;
  title: string;
  description: string;
  /** A grounded proof line tied to a real project or credential. */
  proof: string;
  capabilities: string[];
}

export const pillars: ServicePillar[] = [
  {
    number: "01",
    title: "Product Engineering",
    description:
      "Full-stack products from the schema to the ship date. I build the data model, the API, and the interface as one system, so the thing holds together under real use.",
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
    proof:
      "Four published books and twenty years across leadership, IT, and information security.",
    capabilities: [
      "Technical writing and documentation",
      "Product strategy and positioning",
      "Brand voice and messaging",
    ],
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
    rate: "Coming soon",
    description:
      "Ongoing partnership for teams that need steady hands month over month.",
    available: false,
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
