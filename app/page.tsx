import Link from "next/link";
import type { Metadata } from "next";
import styles from "@/styles/animations.module.css";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import CredibilityStrip from "@/components/CredibilityStrip";
import ProjectCard from "@/components/ProjectCard";
import { projects } from "@/lib/projects";
import { pillars } from "@/lib/services";
import { calendly, ogBase } from "@/lib/site";

const description =
  "A full-stack product studio led by Adam McClarin. Full-stack products, AI integration, and a security posture built in from the first line of code.";

export const metadata: Metadata = {
  title: { absolute: "Where Soul Meets Software · Soulful Tech" },
  description,
  openGraph: {
    ...ogBase,
    title: "Where Soul Meets Software · Soulful Tech",
    description,
    url: "https://merakislove.com",
  },
};

export default function Home() {
  const featured = projects.slice(0, 3);

  return (
    <>
      {/* 1 — Hero */}
      <section className="relative flex min-h-screen items-center overflow-hidden">
        {/* Vertical accent line */}
        <div
          aria-hidden
          className="absolute left-6 top-0 h-full w-px bg-gradient-to-b from-transparent via-amber/40 to-transparent sm:left-8"
        />
        {/* Ambient amber wash */}
        <div
          aria-hidden
          className="absolute -left-40 top-1/4 h-96 w-96 rounded-full opacity-20 blur-[120px]"
          style={{ background: "var(--color-amber)" }}
        />

        <div className="mx-auto w-full max-w-6xl px-6 py-32 sm:px-8">
          <ScrollReveal>
            <p className="mb-6 font-mono text-xs uppercase tracking-[0.3em] text-amber">
              Soulful Tech
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.08}>
            <h1 className="max-w-4xl font-display text-5xl font-light leading-[1.04] text-smoke sm:text-7xl lg:text-8xl">
              Where{" "}
              <span className={`${styles.amberPulse} inline-block px-1 text-amber`}>
                Soul
              </span>{" "}
              Meets Software
            </h1>
          </ScrollReveal>

          <ScrollReveal delay={0.16}>
            <p className="mt-8 max-w-xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              Full-stack products, AI integration, and a security posture built
              in from the first line of code. Twenty years of the work, shaped
              by the belief that technology should serve the person on the other
              side of the screen.
            </p>
          </ScrollReveal>

          <ScrollReveal delay={0.24}>
            <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center">
              <a
                href={calendly.newProject}
                target="_blank"
                rel="noopener noreferrer"
                className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
              >
                Book a call
                <span className="transition-transform duration-300 group-hover:translate-x-1">
                  →
                </span>
              </a>
              <Link
                href="/work"
                className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
              >
                See the work
              </Link>
            </div>
          </ScrollReveal>
        </div>

        {/* Scroll indicator */}
        <div
          aria-hidden
          className="absolute bottom-8 left-1/2 flex -translate-x-1/2 flex-col items-center gap-3"
        >
          <span className="font-mono text-[0.6rem] uppercase tracking-[0.3em] text-muted">
            Scroll
          </span>
          <span className={`${styles.scrollCue} block h-10 w-px bg-gradient-to-b from-amber to-transparent`} />
        </div>
      </section>

      {/* 2 — Credibility Strip */}
      <CredibilityStrip />

      {/* 3 — Featured Work */}
      <section className="mx-auto max-w-6xl px-6 py-24 sm:px-8 sm:py-32">
        <ScrollReveal className="mb-16 flex flex-col gap-5">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Selected work
          </p>
          <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.08] text-smoke sm:text-5xl">
            Three products, one standard.
          </h2>
          <p className="max-w-xl font-body text-smoke-dim">
            Each one answers to the same question. Does this actually serve the
            person using it?
          </p>
        </ScrollReveal>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {featured.map((project, i) => (
            <ScrollReveal key={project.slug} delay={i * 0.08} className="h-full">
              <ProjectCard project={project} />
            </ScrollReveal>
          ))}
        </div>

        <ScrollReveal className="mt-12">
          <Link
            href="/work"
            className="group inline-flex items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
          >
            View all work
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </ScrollReveal>
      </section>

      {/* 4 — Services Teaser */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-6xl px-6 py-24 sm:px-8 sm:py-32">
          <ScrollReveal className="mb-16 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              What I do
            </p>
            <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.08] text-smoke sm:text-5xl">
              Four ways to build with intention.
            </h2>
          </ScrollReveal>

          <div className="grid gap-px overflow-hidden rounded-xl border border-border bg-border sm:grid-cols-2 lg:grid-cols-4">
            {pillars.map((pillar, i) => (
              <ScrollReveal
                key={pillar.number}
                delay={i * 0.06}
                className="group flex h-full flex-col gap-5 bg-void p-7 transition-colors duration-300 hover:bg-navy"
              >
                <span className="font-mono text-xs tracking-[0.2em] text-amber">
                  {pillar.number}
                </span>
                <h3 className="font-display text-2xl font-light text-smoke">
                  {pillar.title}
                </h3>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {pillar.proof}
                </p>
              </ScrollReveal>
            ))}
          </div>

          <ScrollReveal className="mt-12">
            <Link
              href="/services"
              className="group inline-flex items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
            >
              Explore services
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
          </ScrollReveal>
        </div>
      </section>

      {/* 5 — Philosophy Block */}
      <section className="relative overflow-hidden border-y border-border-mid">
        <div
          aria-hidden
          className="absolute inset-0"
          style={{
            background:
              "linear-gradient(135deg, var(--color-purple) 0%, #14072b 45%, var(--color-void) 100%)",
          }}
        />
        <div className="relative mx-auto max-w-4xl px-6 py-28 sm:px-8 sm:py-40">
          <ScrollReveal className="flex flex-col items-center gap-10 text-center">
            <SectionDivider />
            <blockquote className="font-display text-3xl font-light italic leading-[1.25] text-smoke sm:text-4xl lg:text-5xl">
              Soulful Tech is not a tagline I picked because it sounded warm. It
              is the only way I know how to build.
            </blockquote>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              The meditation and the Reiki practice are not a hobby that lives
              next to the technical work. They are the source of the pace, the
              attention, and the decision to stop and ask whether a feature
              actually serves the person using it.
            </p>
          </ScrollReveal>
        </div>
      </section>
    </>
  );
}
