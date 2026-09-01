export interface Project {
  name: string;
  slug: string;
  type: string;
  year: string;
  description: string;
  stack: string[];
  /** What the project demonstrates, shown in the card footer. */
  proves: string;
  /** Accent color used for the card glow and the cover radial. */
  glow: string;
  /** Solid base color behind the cover. */
  coverBg: string;
  /**
   * Cover image path, served from /public/covers via next/image.
   *
   * Optional on purpose. A product can ship on this page before its artwork
   * exists, and ProjectCard falls back to the coverBg panel with a glow
   * radial rather than borrowing another product's image or dropping the
   * card. Add the path when the art is real.
   */
  cover?: string;
  /**
   * Describes what the cover actually shows. Falls back to a generic line
   * when absent, but a real description is better for anyone who cannot
   * see the image.
   */
  coverAlt?: string;
}

export const projects: Project[] = [
  {
    name: "VeloxSync",
    slug: "veloxsync",
    type: "Performance intelligence",
    year: "2025",
    description:
      "Correlates workforce signals to flag at risk talent before it becomes a resignation. Built for teams who need a real early warning, not a survey once a year.",
    stack: ["Together.ai", "Supabase", "Vercel"],
    proves:
      'the hard part of "predictive" is trustworthy signal, not a dashboard. This ships real scores against real data.',
    glow: "#F59E0B",
    coverBg: "#1A1206",
    cover: "/covers/veloxsync-cover.png",
    coverAlt:
      "The VeloxSync dashboard on a dark screen: a wide amber trend line tracking a performance signal over time, a risk score search field above it, and two smaller trend charts and a status meter below.",
  },
  {
    name: "VeloxSync for Education",
    slug: "veloxsync-education",
    type: "Homeschool planning",
    year: "2025",
    description:
      "AI-powered planning for homeschool families, not classrooms. One plan covers up to six children, built on Claude.",
    stack: ["Claude API", "Supabase", "Vercel"],
    proves:
      "the same core intelligence adapts to a completely different audience without losing what makes it work.",
    glow: "#3B82F6",
    coverBg: "#0A1E3A",
    cover: "/covers/veloxsync-education-cover.png",
    coverAlt:
      "The VeloxSync for Education planner on a laptop screen, with a week of lesson blocks laid out per child.",
  },
  {
    name: "Canopy Guard",
    slug: "canopy-guard",
    type: "Security tool",
    year: "2025",
    description:
      "Client security posture auditor. MITRE ATT&CK mapped findings. CISSP-informed. Branded, client-ready reports.",
    stack: ["TypeScript", "Vercel", "MITRE"],
    proves:
      "the review I sell is the same discipline I built a product around.",
    glow: "#EF4444",
    coverBg: "#1A0A0A",
    cover: "/covers/canopyguard-cover.png",
    coverAlt:
      "A Canopy Guard report card for merakislove.com scoring 95 overall, with separate SEO, AEO, GEO and security panels of passing checks and a compliance quick check along the bottom.",
  },
  {
    name: "Meridian AI",
    slug: "meridian-ai",
    type: "Executive platform",
    year: "2024",
    description:
      "Executive intelligence with MFA, RBAC, and export to PPTX, PDF, and HTML from one workflow.",
    stack: ["React", "Node.js", "SendGrid", "Cloudinary"],
    proves:
      "the output has to leave the building in the format a leadership team already uses.",
    glow: "#8B5CF6",
    coverBg: "#0D0A1E",
    cover: "/covers/meridian-cover.png",
    coverAlt:
      "The Meridian AI title over a dark screen holding a faint bar chart, in the deep violet the platform uses.",
  },
];
