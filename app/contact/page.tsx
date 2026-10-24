import type { Metadata } from "next";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ScrollReveal from "@/components/ScrollReveal";
import TiltCard from "@/components/TiltCard";
import Breadcrumb from "@/components/Breadcrumb";
import { calendly, socials, studio, ogBase } from "@/lib/site";

const description =
  "Start a project or book a client discussion with Adam McClarin at Meraki is Love.";

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
    <>
      <Breadcrumb items={[{ name: "Contact", path: "/contact" }]} />
    <PageStack>
      <PageHero
        art={{
          src: "/art/door.jpg",
          alt: "Engraving of a door standing open at dusk, warm light falling across the step.",
        }}
        kicker="Contact"
        title="Let's build something"
        subtitle="Every engagement starts the same way, with a conversation. Pick the path that fits and grab a time."
      />

      <Panel tone="paper" width="6xl">
        {/* Two Calendly paths */}
        <div className="grid gap-6 md:grid-cols-2">
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
                  <p className="font-sans font-semibold text-sm text-amber">
                    {path.label}
                  </p>
                  <h2 className="type-heading text-3xl text-smoke sm:text-4xl">
                    {path.title}
                  </h2>
                  <p className="font-body text-base leading-relaxed text-smoke-dim">
                    {path.description}
                  </p>
                  <span className="mt-auto inline-flex items-center gap-3 font-sans font-semibold text-sm text-smoke transition-colors duration-300 group-hover:text-amber">
                    Book on Calendly
                  </span>
                </div>
              </TiltCard>
            </ScrollReveal>
          ))}
        </div>

      </Panel>
      <Panel tone="ink" width="6xl">
        {/* Direct contact */}
        <ScrollReveal className="">
          <div className="grid gap-10 rounded-xl border border-border bg-void p-8 sm:grid-cols-3 sm:p-10">
            <div className="flex flex-col gap-3">
              <p className="font-sans font-semibold text-sm text-amber">
                Location
              </p>
              <p className="font-body text-smoke">Remote-first</p>
              <p className="font-sans font-semibold text-xs text-muted">
                Working with clients everywhere
              </p>
            </div>

            <div className="flex flex-col gap-3">
              <p className="font-sans font-semibold text-sm text-amber">
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
              <p className="font-sans font-semibold text-sm text-amber">
                Studio
              </p>
              <p className="font-body text-smoke">{studio.name}</p>
              <p className="font-sans font-semibold text-xs text-muted">
                {studio.brand}, {studio.domain}
              </p>
            </div>
          </div>
        </ScrollReveal>
      </Panel>
    </PageStack>
    </>
  );
}
