import type { ReactNode } from "react";

type Tone = "paper" | "dusk" | "plum" | "ink";

interface PanelProps {
  children: ReactNode;
  /** paper = white, dusk = the illustrations' ground, plum = brand plum, ink = the page itself. */
  tone?: Tone;
  id?: string;
  className?: string;
  /** Inner width. Most reading content sits at 5xl. */
  width?: "4xl" | "5xl" | "6xl" | "full";
}

const widths = {
  "4xl": "max-w-4xl",
  "5xl": "max-w-5xl",
  "6xl": "max-w-6xl",
  full: "max-w-none",
} as const;

/**
 * One rounded panel in the page stack (2026-10 redesign). The tone classes
 * live in globals.css: tone-paper re-points the theme tokens so content
 * written for the dark theme reads correctly on white without rewriting it.
 */
export default function Panel({
  children,
  tone = "dusk",
  id,
  className = "",
  width = "5xl",
}: PanelProps) {
  const toneClass = tone === "ink" ? "" : `tone-${tone} rounded-[28px]`;
  return (
    <section id={id} className={`scroll-mt-24 overflow-hidden ${toneClass} ${className}`}>
      <div className={`mx-auto w-full ${widths[width]} px-6 py-14 sm:px-10 sm:py-20 lg:py-24`}>
        {children}
      </div>
    </section>
  );
}

/** The stack every page sits in: panels with a small gutter, clear of the fixed nav. */
export function PageStack({ children }: { children: ReactNode }) {
  return (
    <div className="flex flex-col gap-3 px-2.5 pb-3 pt-[4.5rem] sm:gap-4 sm:px-4 sm:pb-4 sm:pt-24">
      {children}
    </div>
  );
}
