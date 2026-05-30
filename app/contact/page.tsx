import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import TiltCard from "@/components/TiltCard";
import { calendly, socials, studio, ogBase } from "@/lib/site";

const description =
  "Start a project or book a client discussion with Adam McClarin at Meraki is Love. Based in Friendswood, Texas.";

export const metadata: Metadata = {
  title: "Contact",
  description,
  alternates: { canonical: "/contact" },
  openGraph: {
    ...ogBase,
    title: "Contact · Soulful Tech",
    description,
    url: "https://merakislove.com/contact",
  },
};

const paths = [
  {
    label: "New project",
    title: "Start a Project",
    description:
      "New here? Bring the problem you are trying to solve. We will look at it honestly and figure out whether I am the right person to build it with you.",
    href: calendly.newProject,
    glow: "#F59E0B66",
  },
  {
    label: "Existing client",
    title: "Client Discussion",
    description:
      "Already working together? Book time to review progress, talk through the next phase, and keep the build moving.",
    href: calendly.clientDiscussion,
    glow: "#8B5CF666",
  },
];

export default function ContactPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Contact"
        title="Let's build something"
        subtitle="Every engagement starts the same way, with a conversation. Pick the path that fits and grab a time."
      />

      {/* Two Calendly paths */}
      <div className="mt-16 grid gap-6 md:grid-cols-2">
        {paths.map((path, i) => (
          <ScrollReveal key={path.title} delay={i * 0.08} className="h-full">
            <TiltCard glow={path.glow} className="group relative h-full bg-navy">
              <a
                href={path.href}
                target="_blank"
                rel="noopener noreferrer"
                className="absolute inset-0 z-10"
                aria-label={`${path.title}, book on Calendly`}
              />
              <div className="flex h-full flex-col gap-6 p-8 sm:p-10">
                <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
                  {path.label}
                </p>
                <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
                  {path.title}
                </h2>
                <p className="font-body text-base leading-relaxed text-smoke-dim">
                  {path.description}
                </p>
                <span className="mt-auto inline-flex items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 group-hover:text-amber">
                  Book on Calendly
                  <span className="transition-transform duration-300 group-hover:translate-x-1">
                    →
                  </span>
                </span>
              </div>
            </TiltCard>
          </ScrollReveal>
        ))}
      </div>

      {/* Direct contact */}
      <ScrollReveal className="mt-16">
        <div className="grid gap-10 rounded-xl border border-border bg-void p-8 sm:grid-cols-3 sm:p-10">
          <div className="flex flex-col gap-3">
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-amber">
              Location
            </p>
            <p className="font-body text-smoke">{studio.location}</p>
            <p className="font-mono text-[0.7rem] uppercase tracking-wider text-muted">
              Working with clients everywhere
            </p>
          </div>

          <div className="flex flex-col gap-3">
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-amber">
              Elsewhere
            </p>
            <ul className="flex flex-col gap-2">
              {socials.map((social) => (
                <li key={social.label}>
                  <a
                    href={social.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="font-body text-smoke transition-colors hover:text-amber"
                  >
                    {social.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          <div className="flex flex-col gap-3">
            <p className="font-mono text-xs uppercase tracking-[0.2em] text-amber">
              Studio
            </p>
            <p className="font-body text-smoke">{studio.name}</p>
            <p className="font-mono text-[0.7rem] uppercase tracking-wider text-muted">
              {studio.brand} · {studio.domain}
            </p>
          </div>
        </div>
      </ScrollReveal>
    </div>
  );
}
