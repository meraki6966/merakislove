import type { ReactNode } from "react";
import ScrollReveal from "@/components/ScrollReveal";

interface PageHeaderProps {
  /** Small mono eyebrow above the title, e.g. "SELECTED WORK". */
  eyebrow?: string;
  /** Main display title. */
  title: ReactNode;
  /** Optional supporting line beneath the title. */
  subtitle?: ReactNode;
}

/**
 * Reusable interior-page header. 2026-10 redesign: wide, heavy Archivo
 * title and a sentence-case gold kicker instead of the tracked all-caps
 * label and the amber left rule. The inner pages get their full redesign
 * one at a time; this keeps them in the same family meanwhile.
 */
export default function PageHeader({ eyebrow, title, subtitle }: PageHeaderProps) {
  return (
    <ScrollReveal>
      <header>
        {eyebrow ? (
          <p className="mb-4 font-sans text-base font-semibold text-amber">
            {eyebrow}
          </p>
        ) : null}
        <h1 className="type-heading text-[clamp(2.5rem,5.6vw,4.75rem)] text-smoke">
          {title}
        </h1>
        {subtitle ? (
          <p className="mt-6 max-w-2xl font-body text-lg leading-relaxed text-smoke-dim">
            {subtitle}
          </p>
        ) : null}
      </header>
    </ScrollReveal>
  );
}
