import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ProjectCard from "@/components/ProjectCard";
import ScrollReveal from "@/components/ScrollReveal";
import { projects } from "@/lib/projects";
import { calendly, ogBase } from "@/lib/site";

const description =
  "Selected work from Meraki is Love: VeloxSync for Education, Meraki Lingua, Canopy Guard, and Meridian AI.";

export const metadata: Metadata = {
  title: "Work",
  description,
  alternates: { canonical: "/work" },
  openGraph: {
    ...ogBase,
    title: "Selected Work · Soulful Tech",
    description,
    url: "https://merakislove.com/work",
  },
};

export default function WorkPage() {
  return (
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Selected work"
        title="Built with intention"
        subtitle="Four products, each one answering to the same standard. Real systems, in production, doing the work for the people on the other side of the screen."
      />

      {/* A second kind of proof alongside the case studies below: the demo
          builds are clickable, where a case study is a description. Muted
          border rather than the amber of PageHeader, so it reads as a note
          under the header and not as a competing section. */}
      <ScrollReveal className="mt-12">
        <div className="flex flex-col gap-4 border-l-2 border-border-mid pl-6 sm:pl-8">
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            A case study tells you what a project became. If you would rather
            see one running, the demo builds are complete pages you can open and
            scroll the way a visitor would.
          </p>
          <Link
            href="/demos"
            className="group inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:text-smoke"
          >
            Explore working templates
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
            Some of the work lives under confidentiality and does not appear
            here. If you want to see what is behind the curtain, understand the
            architecture, and talk through whether it fits your problem, the
            fastest path is a conversation.
          </p>
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex w-fit items-center gap-3 rounded-full border border-amber px-6 py-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
          >
            Book a call
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </a>
        </div>
      </ScrollReveal>
    </div>
  );
}
