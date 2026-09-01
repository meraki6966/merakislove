import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ProjectCard from "@/components/ProjectCard";
import ScrollReveal from "@/components/ScrollReveal";
import { projects } from "@/lib/projects";
import { ogBase } from "@/lib/site";

const title = "Work | Meraki is Love";

const description =
  "Real systems, in production, doing work for the person on the other side of the screen.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/work" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/work",
  },
};

const nda =
  "Some of the work does not appear here. Healthcare, finance, and internal tools often stay off the public page. If you need architecture detail, book the call.";

export default function WorkPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Work"
        title="Built with the same standard."
        subtitle="Real systems. In production. Doing work for the person on the other side of the screen. If you want the running version, the demos are live pages. If you want the confidential work, that conversation happens on a call."
      />

      <ScrollReveal className="mt-10">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
          <Link
            href="/demos"
            className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
          >
            Explore demos
          </Link>
          <Link
            href="/start"
            className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
          >
            Book a call
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </div>
      </ScrollReveal>

      <div className="mt-16 grid gap-6 md:grid-cols-2">
        {projects.map((project, i) => (
          <ScrollReveal key={project.slug} delay={i * 0.08} className="h-full">
            <ProjectCard project={project} />
          </ScrollReveal>
        ))}
      </div>

      {/* Confidentiality note */}
      <ScrollReveal className="mt-16">
        <div className="flex flex-col gap-6 rounded-xl border border-border-mid bg-navy/40 p-8 sm:p-10">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Under NDA
          </p>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            {nda}
          </p>
          <Link
            href="/packages"
            className="group inline-flex w-fit items-center gap-3 rounded-full border border-amber px-6 py-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
          >
            See packages
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </div>
      </ScrollReveal>
    </div>
  );
}
