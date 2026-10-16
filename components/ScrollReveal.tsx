"use client";

import { motion, useReducedMotion } from "framer-motion";
import type { ReactNode } from "react";

interface ScrollRevealProps {
  children: ReactNode;
  className?: string;
  /** Stagger helper — seconds to wait before this element reveals. */
  delay?: number;
  /** Render as something other than a div (e.g. "section", "li"). */
  as?: "div" | "section" | "li" | "article";
}

/**
 * IntersectionObserver-backed reveal.
 * Motion rule #1: opacity 0→1, translateY 28px→0, 0.75s ease-out, fires at 12%.
 *
 * Under prefers-reduced-motion the content appears on entry at once, with no
 * fade and no movement. The same motion element renders either way. This used
 * to swap in a plain element when reduced motion was on, but the server can't
 * know that preference, so it always sent the motion element with an inline
 * opacity:0, and hydration kept that style on the plain element. Anyone with
 * Reduce Motion on saw most of the site blank. scripts/tests/reduced-motion
 * .test.mjs guards against the swap coming back.
 */
export default function ScrollReveal({
  children,
  className,
  delay = 0,
  as = "div",
}: ScrollRevealProps) {
  const reduceMotion = useReducedMotion();
  const MotionTag = motion[as];

  return (
    <MotionTag
      className={className}
      initial={{ opacity: 0, y: 28 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.12 }}
      transition={
        reduceMotion
          ? { duration: 0 }
          : { duration: 0.75, ease: "easeOut", delay }
      }
    >
      {children}
    </MotionTag>
  );
}
