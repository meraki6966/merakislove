import styles from "@/styles/animations.module.css";

/**
 * Full-screen SVG grain. Fixed, 4% opacity, never intercepts pointer events.
 * Sits above page content but below the cursor. Ambient motion only —
 * the stepped drift behaves like film grain, not UI motion.
 */
export default function GrainOverlay() {
  return (
    <div
      aria-hidden
      className={`pointer-events-none fixed inset-0 z-[60] opacity-[0.04] ${styles.grainShift}`}
      style={{
        backgroundImage: "url(/noise.svg)",
        backgroundRepeat: "repeat",
        // Oversize so the stepped translate never reveals an edge.
        inset: "-10%",
        width: "120%",
        height: "120%",
        // Promote to its own compositor layer so the stepped drift stays cheap.
        willChange: "transform",
      }}
    />
  );
}
