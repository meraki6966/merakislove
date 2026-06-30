import styles from "@/styles/loop.module.css";

/**
 * The Meraki is Love Loop — hero visual.
 *
 * Three nodes (Audit, Fix, Scale) sit on a circle. A faint guide ring
 * holds a travelling amber comet that sweeps clockwise forever; each
 * node flares gold in sequence as the comet reaches it. Entirely CSS
 * driven (see loop.module.css), so it ships no animation runtime and
 * goes still under prefers-reduced-motion.
 */
export default function LoopAnimation() {
  return (
    <div className={styles.stage} aria-hidden>
      <div className={styles.glow} />

      <svg className={styles.ring} viewBox="0 0 400 400" role="presentation">
        <circle className={styles.ringTrack} cx="200" cy="200" r="150" />
        <circle
          className={styles.comet}
          cx="200"
          cy="200"
          r="150"
          transform="rotate(-90 200 200)"
        />
      </svg>

      <div className={`${styles.node} ${styles.nodeAudit}`}>
        <span className={`${styles.dot} ${styles.delayAudit}`}>Audit</span>
        <span className={styles.step}>Stage 01</span>
      </div>

      <div className={`${styles.node} ${styles.nodeFix}`}>
        <span className={`${styles.dot} ${styles.delayFix}`}>Fix</span>
        <span className={styles.step}>Stage 02</span>
      </div>

      <div className={`${styles.node} ${styles.nodeScale}`}>
        <span className={`${styles.dot} ${styles.delayScale}`}>Scale</span>
        <span className={styles.step}>Stage 03</span>
      </div>
    </div>
  );
}
