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
                  {pillar.detail}
                </p>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {pillar.proof}
                </p>
                <div className="mt-auto flex flex-col gap-2">
                  <p className="font-mono text-[0.65rem] uppercase tracking-[0.2em] text-amber">
                    What you get
                  </p>
                  <ul className="flex flex-col gap-1.5 font-body text-sm leading-relaxed text-smoke-dim">
                    {pillar.capabilities.map((capability) => (
                      <li key={capability} className="flex gap-2.5">
                        <span aria-hidden className="text-amber">
                          —
                        </span>
                        <span>{capability}</span>
                      </li>
                    ))}
                  </ul>
                </div>
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

      {/* 5 — At a Glance */}
      <section className="border-t border-border">
        <div className="mx-auto max-w-4xl px-6 py-24 sm:px-8 sm:py-32">
          <ScrollReveal className="mb-12 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              At a Glance
            </p>
            <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.08] text-smoke sm:text-5xl">
              Two decades, measured.
            </h2>
            <p className="max-w-xl font-body text-smoke-dim">
              The numbers behind the studio. Twenty years of work, a handful of
              products carrying real load in production, and the credentials to
              stand behind the security claims. Here is the shape of it at a
              glance.
            </p>
          </ScrollReveal>

          <ScrollReveal>
            <div className="overflow-hidden rounded-xl border border-border">
              <table className="w-full border-collapse font-body text-sm text-smoke-dim">
                <caption className="sr-only">
                  Key facts about Meraki is Love and Soulful Tech
                </caption>
                <thead>
                  <tr className="border-b border-border bg-navy/40 text-left">
                    <th
                      scope="col"
                      className="px-6 py-4 font-mono text-[0.65rem] uppercase tracking-[0.2em] text-amber"
                    >
                      Metric
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-4 text-right font-mono text-[0.65rem] uppercase tracking-[0.2em] text-amber"
                    >
                      Figure
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {[
                    { metric: "Years of Experience", figure: "20+" },
                    { metric: "Products in Production", figure: "5" },
                    { metric: "Languages Supported", figure: "37" },
                    { metric: "State Standards Seeded", figure: "112" },
                    { metric: "Security Certifications", figure: "CISSP" },
                    { metric: "Clients Served", figure: "10+" },
                  ].map((row) => (
                    <tr
                      key={row.metric}
                      className="border-b border-border last:border-b-0 transition-colors duration-300 hover:bg-navy/30"
                    >
                      <th
                        scope="row"
                        className="px-6 py-4 text-left font-body font-normal text-smoke"
                      >
                        {row.metric}
                      </th>
                      <td className="px-6 py-4 text-right font-mono text-base font-medium text-amber">
                        {row.figure}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </ScrollReveal>
        </div>
      </section>

      {/* 6 — How the work gets made */}
      <section className="border-t border-border bg-navy/30">
        <div className="mx-auto max-w-4xl px-6 py-24 sm:px-8 sm:py-32">
          <ScrollReveal className="mb-12 flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              How the work gets made
            </p>
            <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.08] text-smoke sm:text-5xl">
              A process you can actually see.
            </h2>
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              Most engagements move through the same four movements, and the
              reason they are written down is simple. You should never have to
              wonder what is happening to your project or why. Every phase ends
              with something concrete in your hands, whether that is an
              architecture diagram, a working preview, or a hardened deployment
              you can put in front of customers. The pace is deliberate, the
              feedback loops are short, and there is no black box between the
              first conversation and the thing that ships.
            </p>
          </ScrollReveal>

          <ScrollReveal>
            <ol className="flex flex-col gap-6">
              <li className="flex flex-col gap-2 border-l-2 border-border pl-6 sm:flex-row sm:gap-6">
                <span className="font-mono text-sm tracking-[0.2em] text-amber sm:pt-1">
                  01
                </span>
                <div className="flex flex-col gap-1.5">
                  <h3 className="font-display text-xl font-light text-smoke">
                    Discovery
                  </h3>
                  <p className="font-body text-sm leading-relaxed text-smoke-dim">
                    We start in conversation, not in code. I learn the people
                    who will use the thing, the constraints you are actually
                    operating under, and the real goal hiding behind the stated
                    one. Nothing gets proposed until I understand the problem
                    well enough to argue both sides of it.
                  </p>
                </div>
              </li>
              <li className="flex flex-col gap-2 border-l-2 border-border pl-6 sm:flex-row sm:gap-6">
                <span className="font-mono text-sm tracking-[0.2em] text-amber sm:pt-1">
                  02
                </span>
                <div className="flex flex-col gap-1.5">
                  <h3 className="font-display text-xl font-light text-smoke">
                    Architecture
                  </h3>
                  <p className="font-body text-sm leading-relaxed text-smoke-dim">
                    I map the system before building it. The data model, the
                    integrations, the failure modes, and the security posture
                    are decided up front, on paper, where changing your mind is
                    cheap. You see the shape of the whole product before a
                    single migration is written.
                  </p>
                </div>
              </li>
              <li className="flex flex-col gap-2 border-l-2 border-border pl-6 sm:flex-row sm:gap-6">
                <span className="font-mono text-sm tracking-[0.2em] text-amber sm:pt-1">
                  03
                </span>
                <div className="flex flex-col gap-1.5">
                  <h3 className="font-display text-xl font-light text-smoke">
                    Build
                  </h3>
                  <p className="font-body text-sm leading-relaxed text-smoke-dim">
                    The work gets made in tight, visible loops. You get previews
                    you can click through, progress you can measure against the
                    plan, and a direct line to the person writing the code. No
                    status theater, no surprises three weeks before launch.
                  </p>
                </div>
              </li>
              <li className="flex flex-col gap-2 border-l-2 border-border pl-6 sm:flex-row sm:gap-6">
                <span className="font-mono text-sm tracking-[0.2em] text-amber sm:pt-1">
                  04
                </span>
                <div className="flex flex-col gap-1.5">
                  <h3 className="font-display text-xl font-light text-smoke">
                    Deploy and Harden
                  </h3>
                  <p className="font-body text-sm leading-relaxed text-smoke-dim">
                    We ship, and then we secure. Monitoring goes in, headers and
                    TLS get tightened, dependencies get audited, and the system
                    is reviewed through a CISSP lens before it carries real
                    traffic. You launch with a posture you can defend, not a
                    promise to fix it later.
                  </p>
                </div>
              </li>
            </ol>
          </ScrollReveal>

          <ScrollReveal className="mt-12 flex flex-col gap-6">
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              That last movement is where most studios quietly cut corners and
              where twenty years in information security refuses to let me. A
              product is not done when it works on a good day. It is done when it
              holds up on a bad one, when the traffic spikes, when someone
              probes the endpoints, and when the data it was trusted with stays
              exactly where it belongs. Building that kind of resilience in from
              the start costs a little more attention early and saves an
              enormous amount of pain later, and it is the through line that
              connects every project this studio has shipped.
            </p>
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              The same discipline shows up in the smaller decisions, the ones a
              client rarely sees but always feels. A form that tells you exactly
              what went wrong instead of failing silently. An API that returns a
              clear, structured error instead of a stack trace. A page that
              loads fast on a tired phone and a slow connection, because the
              person on the other side of the screen did not ask to be punished
              for their hardware. These are not features anyone puts on a
              roadmap, and they are precisely the things that separate software
              people tolerate from software people trust. I treat them as part
              of the job, not as polish to add if the budget survives.
            </p>
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              Working with a studio of one has a specific shape worth naming.
              You are not handed to a junior team after the pitch, and the
              person who understood your problem in the first call is the person
              writing the code in the last one. That continuity means less is
              lost in translation, decisions get made faster, and the context
              you spent an hour explaining does not evaporate between meetings.
              It also means I take on the work I can genuinely do well and say so
              plainly when something falls outside that, because a good
              referral protects your project more than an honest overreach ever
              could. The studio stays small on purpose, so the care stays real.
            </p>
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              It also helps to know what kind of work this studio is built for.
              The best engagements tend to be the ones where the problem is real
              and a little messy, where someone has tried the obvious solutions
              and found them wanting, and where quality matters more than
              shipping the cheapest possible version by Friday. Early-stage
              founders proving an idea, established teams who need senior hands
              on a hard subsystem, and organizations that finally want their
              security posture taken seriously all tend to find the fit
              natural. If your situation looks nothing like those, that is
              useful to learn early too, and I will tell you so rather than bend
              the work into a shape it was never meant to take.
            </p>
            <p className="max-w-2xl font-body text-smoke-dim leading-relaxed">
              If any of this sounds like the kind of partner your project has
              been missing, the next step is an unhurried conversation. No deck,
              no pressure, no obligation on either side. We talk through what you
              are building, where it hurts, and whether the way I work is the
              right fit for the problem in front of you. The worst case is an
              honest answer and a useful pointer in a better direction. The best
              case is the start of something built with intention from the very
              first line of code.
            </p>
          </ScrollReveal>
        </div>
      </section>

      {/* 7 — Philosophy Block */}
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
