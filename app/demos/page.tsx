import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import Tag from "@/components/Tag";
import { calendly, ogBase } from "@/lib/site";

const description =
  "Demo builds from Meraki is Love. Each one is a complete, working page you can open and scroll, not a screenshot of a layout.";

export const metadata: Metadata = {
  title: "Demos",
  description,
  alternates: { canonical: "/demos" },
  openGraph: {
    ...ogBase,
    title: "Demos · Soulful Tech",
    description,
    url: "https://merakislove.com/demos",
  },
};

interface Demo {
  /** Display name of the demo brand. Not a real client. */
  name: string;
  /** Category line shown above the name. */
  eyebrow: string;
  description: string;
  /** Stack chips. */
  stack: string[];
  /** Static demos live under /public, so these are plain hrefs, not routes. */
  href: string;
  /** Two-stop gradient previewing the demo's own palette. */
  swatch: [string, string];
  /** Palette caption shown on the swatch panel. */
  swatchLabel: string;
  /**
   * Caption colour for the swatch band. Each demo picks its own palette, so
   * this cannot be a single hardcoded value: the restaurant's dark brown is
   * unreadable on Iron Prism's near-black, and vice versa.
   */
  swatchInk: string;
}

// Two demos, side by side from `md` up. The swatch is kept as a band across
// the top of each card rather than dropped: it is the thing that signals
// each demo has its own design world, and it earns its place precisely
// because these two palettes are opposites.
const demos: Demo[] = [
  {
    name: "The Corner Table",
    eyebrow: "Hospitality · Template",
    description:
      "A neighborhood restaurant site built around one question: does the page feel like the room. It carries a visitor from the first screen through the full menu to the reservation step, in a palette and a typeface chosen for the restaurant rather than for us.",
    stack: ["Static HTML", "GSAP ScrollTrigger", "Presence-First"],
    href: "/demos/restaurant",
    swatch: ["#FAF6EF", "#B5533C"],
    swatchLabel: "Cream · Terracotta · Olive",
    swatchInk: "rgba(62, 47, 38, 0.7)",
  },
  {
    name: "Iron Prism",
    eyebrow: "Fitness · Template",
    description:
      "A strength gym, built loud. Heavy condensed caps on near-black, electric violet carrying every accent, and a prism spectrum used four times on the whole page so it reads as a mark rather than a pattern. Deliberately the opposite of the restaurant in every decision.",
    stack: ["Static HTML", "GSAP ScrollTrigger", "Presence-First"],
    href: "/demos/iron-prism",
    swatch: ["#0B0B0F", "#7C3AED"],
    swatchLabel: "Charcoal · Electric Violet · Prism",
    swatchInk: "rgba(244, 244, 247, 0.72)",
  },
];

export default function DemosPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Demos"
        title="Click through the real thing"
        subtitle="A screenshot shows you a layout. It does not show you how a page feels to move through. Every demo here is a complete build, running on this site, that you can open and scroll the way a visitor would."
      />

      <div className="mt-16 grid gap-6 md:grid-cols-2">
        {demos.map((demo, i) => (
          <ScrollReveal key={demo.name} delay={i * 0.08} className="h-full">
            <article className="flex h-full flex-col overflow-hidden rounded-xl border border-border-mid bg-navy/40">
              {/* Palette preview. Hints that the demo has its own world,
                  deliberately not the amber-on-void of this site. */}
              <div
                aria-hidden
                className="relative flex min-h-[10rem] items-end p-6 sm:min-h-[12rem]"
                style={{
                  background: `linear-gradient(150deg, ${demo.swatch[0]} 0%, ${demo.swatch[0]} 45%, ${demo.swatch[1]} 100%)`,
                }}
              >
                <span
                  className="font-mono text-[0.65rem] uppercase tracking-[0.2em]"
                  style={{ color: demo.swatchInk }}
                >
                  {demo.swatchLabel}
                </span>
              </div>

              <div className="flex flex-1 flex-col gap-5 p-7 sm:p-9">
                <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
                  {demo.eyebrow}
                </p>

                <h2 className="font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
                  {demo.name}
                </h2>

                <p className="font-body text-sm leading-relaxed text-smoke-dim sm:text-base">
                  {demo.description}
                </p>

                <div className="flex flex-wrap gap-2">
                  {demo.stack.map((tech) => (
                    <Tag key={tech}>{tech}</Tag>
                  ))}
                </div>

                <a
                  href={demo.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="group mt-auto inline-flex w-fit items-center gap-3 rounded-full border border-amber px-6 py-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
                >
                  View the live demo
                  <span className="transition-transform duration-300 group-hover:translate-x-1">
                    →
                  </span>
                </a>
              </div>
            </article>
          </ScrollReveal>
        ))}
      </div>

      <ScrollReveal className="mt-20 flex flex-col gap-6">
        <SectionDivider align="left" />
        <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
          What these are
        </p>
        <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
          Every demo here is a template, not client work. The brands are
          invented so a build can be shown in full without putting a real
          client site on display. If one of them is close to what you need, the
          fastest path is a conversation.
        </p>
        <a
          href={calendly.newProject}
          target="_blank"
          rel="noopener noreferrer"
          className="group inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:text-smoke"
        >
          Book a call
          <span className="transition-transform duration-300 group-hover:translate-x-1">
            →
          </span>
        </a>
      </ScrollReveal>
    </div>
  );
}
