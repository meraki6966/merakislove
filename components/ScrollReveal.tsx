import type { ReactNode } from "react";

interface ScrollRevealProps {
  children: ReactNode;
  className?: string;
  /** Kept so existing call sites compile. It no longer does anything. */
  delay?: number;
  /** Render as something other than a div (e.g. "section", "li"). */
  as?: "div" | "section" | "li" | "article";
}

/**
 * Formerly a fade-and-slide-up reveal on every block. The 2026-10 redesign
 * keeps one motion moment per page (the hero settling in on load) and drops
 * the scroll reveals, which read as template motion. This now renders its
 * content as-is: visible from the first paint, with JavaScript off, and with
 * Reduce Motion on. scripts/tests/reduced-motion.test.mjs holds that.
 */
export default function ScrollReveal({ children, className, as = "div" }: ScrollRevealProps) {
  const Tag = as;
  return <Tag className={className}>{children}</Tag>;
}
