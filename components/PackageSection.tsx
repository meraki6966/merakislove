import type { ReactNode } from "react";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";

interface PackageSectionProps {
  title: string;
  /** Optional lead line between the heading and the body. */
  lead?: string;
  children: ReactNode;
}

/**
 * A titled block on a package detail page. The three pages run through the
 * same sequence of short sections, so the heading, the amber rule beneath
 * it, and the reveal live here rather than being repeated twenty times.
 */
export default function PackageSection({
  title,
  lead,
  children,
}: PackageSectionProps) {
  return (
    <section className="mt-20">
      <ScrollReveal className="mb-8 flex flex-col gap-4">
        <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
          {title}
        </h2>
        <SectionDivider align="left" />
        {lead ? (
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {lead}
          </p>
        ) : null}
      </ScrollReveal>
      {children}
    </section>
  );
}
