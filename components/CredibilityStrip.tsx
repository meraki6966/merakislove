import styles from "@/styles/animations.module.css";
import { credentials } from "@/lib/site";

/**
 * Horizontal credential ticker. A single seamless marquee of the studio's
 * credentials, separated by amber dots and faded at both edges. Continuous
 * ambient motion; pauses on hover and stills entirely under reduced-motion.
 */
export default function CredibilityStrip() {
  // Two copies of the list make the -50% loop seamless.
  const items = [...credentials, ...credentials];

  return (
    <section
      aria-label="Credentials"
      className="relative overflow-hidden border-y border-border bg-navy/40 py-5"
    >
      {/* Edge fades */}
      <div className="pointer-events-none absolute inset-y-0 left-0 z-10 w-24 bg-gradient-to-r from-void to-transparent" />
      <div className="pointer-events-none absolute inset-y-0 right-0 z-10 w-24 bg-gradient-to-l from-void to-transparent" />

      <div className={styles.marquee}>
        <div className={styles.marqueeTrack} aria-hidden>
          {items.map((credential, i) => (
            <span key={i} className="flex items-center whitespace-nowrap">
              <span className="px-8 font-mono text-xs uppercase tracking-[0.22em] text-smoke-dim">
                {credential}
              </span>
              <span className="h-1 w-1 rounded-full bg-amber" />
            </span>
          ))}
        </div>
      </div>

      {/* Accessible, non-animated copy for assistive tech */}
      <span className="sr-only">{credentials.join(", ")}</span>
    </section>
  );
}
