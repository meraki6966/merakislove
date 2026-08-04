"use client";

import { useEffect, useLayoutEffect, useRef, type ReactNode } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

/**
 * GSAP motion shell for the Presence-First Web Design page.
 *
 * Renders a plain wrapper so the page itself stays a server component —
 * all of the copy ships in the HTML, only the motion is client-side.
 * Two behaviors, one easing curve (power3.out):
 *   [data-pf-hero]   — staggered fade-up on load, in DOM order.
 *   [data-pf-reveal] — fade-up as the element scrolls into view, with an
 *                      optional per-element `data-pf-delay` in seconds.
 *
 * Both start hidden in CSS (styles/presence.module.css) so there is no
 * flash before the timeline runs. Everything is registered inside
 * gsap.matchMedia(), so visitors who prefer reduced motion never have
 * anything animated or hidden — the CSS leaves those elements at rest.
 */

// useLayoutEffect warns during SSR; fall back to useEffect on the server.
const useIsomorphicLayoutEffect =
  typeof window === "undefined" ? useEffect : useLayoutEffect;

interface PresenceMotionProps {
  children: ReactNode;
  className?: string;
}

export default function PresenceMotion({
  children,
  className,
}: PresenceMotionProps) {
  const root = useRef<HTMLDivElement>(null);

  useIsomorphicLayoutEffect(() => {
    const scope = root.current;
    if (!scope) return;

    gsap.registerPlugin(ScrollTrigger);

    let cancelled = false;
    const mm = gsap.matchMedia();

    mm.add("(prefers-reduced-motion: no-preference)", () => {
      // Hero — eyebrow, headline, sub-copy, CTAs, in sequence on load.
      gsap.fromTo(
        gsap.utils.toArray<HTMLElement>("[data-pf-hero]", scope),
        { opacity: 0, y: 32 },
        {
          opacity: 1,
          y: 0,
          duration: 1.1,
          ease: "power3.out",
          stagger: 0.14,
          delay: 0.1,
        },
      );

      // Everything below the fold — same curve, fired on entry.
      gsap.utils
        .toArray<HTMLElement>("[data-pf-reveal]", scope)
        .forEach((el) => {
          gsap.fromTo(
            el,
            { opacity: 0, y: 28 },
            {
              opacity: 1,
              y: 0,
              duration: 0.9,
              ease: "power3.out",
              delay: Number(el.dataset.pfDelay ?? 0),
              scrollTrigger: { trigger: el, start: "top 88%", once: true },
            },
          );
        });
    });

    // Font swap shifts layout, which moves every trigger point with it.
    if (typeof document !== "undefined" && document.fonts) {
      document.fonts.ready.then(() => {
        if (!cancelled) ScrollTrigger.refresh();
      });
    }

    return () => {
      cancelled = true;
      mm.revert();
    };
  }, []);

  return (
    <div ref={root} className={className}>
      {children}
    </div>
  );
}
