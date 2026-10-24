import type { Metadata } from "next";
import Link from "next/link";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ProjectCard from "@/components/ProjectCard";
import ScrollReveal from "@/components/ScrollReveal";
import Breadcrumb from "@/components/Breadcrumb";
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
    <>
      <Breadcrumb items={[{ name: "Work", path: "/work" }]} />
    <PageStack>
      <PageHero
        art={{
          src: "/art/work.jpg",
          alt: "Engraving of a workshop shelf holding finished brass pieces: a telescope, a clock, lanterns, a strongbox and scales.",
        }}
        kicker="Work"
        title="Built with the same standard."
        subtitle="Real systems. In production. Doing work for the person on the other side of the screen. If you want the running version, the demos are live pages. If you want the confidential work, that conversation happens on a call."
      >
        <ScrollReveal className="">
          <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
            <Link
              href="/demos"
              className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-sans font-semibold text-sm text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
            >
              Explore demos
            </Link>
            <Link
              href="/start"
              className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-sans font-semibold text-sm text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a call
            </Link>
          </div>
        </ScrollReveal>
      </PageHero>
      <Panel tone="paper" width="6xl">
        <div className="grid gap-6 md:grid-cols-2">
          {projects.map((project, i) => (
            <ScrollReveal key={project.slug} delay={i * 0.08} className="h-full">
              <ProjectCard project={project} />
            </ScrollReveal>
          ))}
        </div>

      </Panel>
      <Panel tone="ink" width="6xl">
        {/* Confidentiality note */}
        <ScrollReveal className="">
          <div className="flex flex-col gap-6 rounded-xl border border-border-mid bg-navy/40 p-8 sm:p-10">
            <p className="font-sans font-semibold text-sm text-amber">
              Under NDA
            </p>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
              {nda}
            </p>
            <Link
              href="/packages"
              className="group inline-flex w-fit items-center gap-3 rounded-full border border-amber px-6 py-3 font-sans font-semibold text-sm text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
            >
              See packages
            </Link>
          </div>
        </ScrollReveal>
      </Panel>
    </PageStack>
    </>
  );
}
