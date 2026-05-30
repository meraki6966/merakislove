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
 * Reusable interior-page header. Amber left border accent, mono eyebrow,
 * Cormorant display title, optional subtitle.
 */
export default function PageHeader({ eyebrow, title, subtitle }: PageHeaderProps) {
  return (
    <ScrollReveal>
      <header className="border-l-2 border-amber pl-6 sm:pl-8">
        {eyebrow ? (
          <p className="mb-4 font-mono text-xs uppercase tracking-[0.25em] text-amber">
            {eyebrow}
          </p>
        ) : null}
        <h1 className="font-display text-4xl font-light leading-[1.05] text-smoke sm:text-6xl">
          {title}
        </h1>
        {subtitle ? (
          <p className="mt-5 max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            {subtitle}
          </p>
        ) : null}
      </header>
    </ScrollReveal>
  );
}
