"use client";

import {
  motion,
  useMotionValue,
  animate,
  useReducedMotion,
} from "framer-motion";
import { useRef, useState, type ReactNode } from "react";

interface TiltCardProps {
  children: ReactNode;
  className?: string;
  /** Optional accent color for the hover glow (e.g. a project's glow color). */
  glow?: string;
}

const MAX_DEG = 10;
// Motion rule #2: ease back on leave, 0.55s. No spring, no bounce.
const EASE_BACK: [number, number, number, number] = [0.22, 1, 0.36, 1];
const BACK = { duration: 0.55, ease: EASE_BACK };

/**
 * The showpiece interaction. Perspective tilt that tracks the pointer
 * (max 10deg on each axis), lifts 8px toward the viewer on hover, and
 * gains an amber border + soft glow. Eases back to rest on leave.
 */
export default function TiltCard({ children, className = "", glow }: TiltCardProps) {
  const ref = useRef<HTMLDivElement>(null);
  const rotateX = useMotionValue(0);
  const rotateY = useMotionValue(0);
  const z = useMotionValue(0);
  const [hovered, setHovered] = useState(false);
  const reduceMotion = useReducedMotion();

  function handleMove(e: React.MouseEvent<HTMLDivElement>) {
    if (reduceMotion || !ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const px = (e.clientX - rect.left) / rect.width - 0.5; // -0.5 … 0.5
    const py = (e.clientY - rect.top) / rect.height - 0.5;
    rotateY.set(px * 2 * MAX_DEG);
    rotateX.set(-py * 2 * MAX_DEG);
  }

  function handleEnter() {
    if (reduceMotion) return;
    setHovered(true);
    animate(z, 8, BACK);
  }

  function handleLeave() {
    setHovered(false);
    animate(rotateX, 0, BACK);
    animate(rotateY, 0, BACK);
    animate(z, 0, BACK);
  }

  const glowColor = glow ?? "var(--color-amber-glow)";

  return (
    <motion.div
      ref={ref}
      onMouseMove={handleMove}
      onMouseEnter={handleEnter}
      onMouseLeave={handleLeave}
      style={{
        rotateX,
        rotateY,
        z,
        transformPerspective: 900,
        transformStyle: "preserve-3d",
        boxShadow: hovered ? `0 24px 60px -28px ${glowColor}` : "0 0 0 0 transparent",
      }}
      className={`rounded-xl border transition-[border-color,box-shadow] duration-500 ${
        hovered ? "border-amber" : "border-border-mid"
      } ${className}`}
    >
      {children}
    </motion.div>
  );
}
