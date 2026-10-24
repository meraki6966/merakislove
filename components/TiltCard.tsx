import type { ReactNode } from "react";

interface TiltCardProps {
  children: ReactNode;
  className?: string;
  /** Kept so existing call sites compile; the glow is gone. */
  glow?: string;
}

/**
 * Formerly a pointer-tracking 3D tilt. The 2026-10 redesign keeps cards
 * still: a rounded surface with a ring that warms on hover.
 */
export default function TiltCard({ children, className = "" }: TiltCardProps) {
  return (
    <div className={`overflow-hidden rounded-2xl ring-1 ring-border-mid transition-shadow duration-300 hover:ring-amber/60 ${className}`}>
      {children}
    </div>
  );
}
