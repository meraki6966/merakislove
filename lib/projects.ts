export interface Project {
  name: string;
  slug: string;
  type: string;
  year: string;
  description: string;
  stack: string[];
  stat: string;
  /** Accent color used for the card glow and cover radial. */
  glow: string;
  /** Solid base color behind the placeholder cover. */
  coverBg: string;
  /** Cover image path (Figma exports pending — placeholder treatment until ready). */
  cover: string;
}

export const projects: Project[] = [
  {
    name: "VeloxSync for Education",
    slug: "veloxsync-education",
    type: "SaaS Platform",
    year: "2025",
    description:
      "K-12 AI platform with grade-band intelligence. 10 DB tables, 30+ endpoints, 112 state standards, Ei-Core fine-tuned models.",
    stack: ["Next.js", "Supabase", "Together.ai", "Railway"],
    stat: "K-12 · 112 state standards",
    glow: "#3B82F6",
    coverBg: "#0A1E3A",
    cover: "/covers/veloxsync-cover.png",
  },
  {
    name: "Meraki Lingua",
    slug: "meraki-lingua",
    type: "AI Widget",
    year: "2025",
    description:
      "37-language AI chat widget. Dialect-accurate, RTL-supported, Claude API-powered. HTML PDF export built in.",
    stack: ["Claude API", "React", "Node.js", "Vercel"],
    stat: "37 languages · RTL support",
    glow: "#10B981",
    coverBg: "#0F1A0A",
    cover: "/covers/lingua-cover.png",
  },
  {
    name: "Canopy Guard",
    slug: "canopy-guard",
    type: "Security Tool",
    year: "2025",
    description:
      "Client security posture auditor. MITRE ATT&CK mapped findings. CISSP-informed. Branded client-ready reports.",
    stack: ["Next.js", "TypeScript", "Vercel", "MITRE"],
    stat: "CISSP-informed · ATT&CK mapped",
    glow: "#EF4444",
    coverBg: "#1A0A0A",
    cover: "/covers/canopyguard-cover.png",
  },
  {
    name: "Meridian AI",
    slug: "meridian-ai",
    type: "Executive Platform",
    year: "2024",
    description:
      "Executive intelligence platform with MFA, RBAC, and multi-format export. PPTX, PDF, and HTML output from a single workflow.",
    stack: ["React", "Node.js", "SendGrid", "Cloudinary"],
    stat: "PPTX · PDF · HTML export",
    glow: "#8B5CF6",
    coverBg: "#0D0A1E",
    cover: "/covers/meridian-cover.png",
  },
];
