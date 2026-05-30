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
 * Honors prefers-reduced-motion by rendering content with no transform.
 */
export default function ScrollReveal({
  children,
  className,
  delay = 0,
  as = "div",
}: ScrollRevealProps) {
  const reduceMotion = useReducedMotion();
  const MotionTag = motion[as];

  if (reduceMotion) {
    const Tag = as;
    return <Tag className={className}>{children}</Tag>;
  }

  return (
    <MotionTag
      className={className}
      initial={{ opacity: 0, y: 28 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.12 }}
      transition={{ duration: 0.75, ease: "easeOut", delay }}
    >
      {children}
    </MotionTag>
  );
}
