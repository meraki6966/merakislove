import Image from "next/image";
import type { ReactNode } from "react";

interface PageHeroProps {
  /** Short sentence-case kicker above the title, e.g. "Review". */
  kicker?: string;
  title: ReactNode;
  subtitle?: ReactNode;
  /** An engraving from public/art. */
  art?: { src: string; alt: string };
  /** Buttons or links under the subtitle. */
  children?: ReactNode;
}

/**
 * Inner-page hero (2026-10 redesign): a dusk panel with the title on the
 * left and the page's engraving on the right, stacked on phones. It settles
 * in once on load, the same single motion moment as the home page.
 */
export default function PageHero({ kicker, title, subtitle, art, children }: PageHeroProps) {
  return (
    <section className="tone-dusk overflow-hidden rounded-[28px]">
      <div className="grid items-stretch lg:grid-cols-[1.1fr_1fr]">
        <div className="hero-in flex flex-col justify-center gap-6 px-6 pb-12 pt-14 sm:px-12 sm:pb-16 sm:pt-20 lg:py-24 lg:pl-16">
          {kicker ? (
            <p className="font-sans text-base font-semibold text-amber">{kicker}</p>
          ) : null}
          <h1 className="type-heading text-[clamp(2.25rem,4.6vw,4.25rem)] text-smoke">
            {title}
          </h1>
          {subtitle ? (
            <p className="max-w-xl font-body text-lg leading-relaxed text-smoke-dim">
              {subtitle}
            </p>
          ) : null}
          {children}
        </div>
        {art ? (
          <div className="relative aspect-[4/3] lg:aspect-auto lg:min-h-[30rem]">
            <Image
              src={art.src}
              alt={art.alt}
              fill
              priority
              sizes="(min-width: 1024px) 48vw, 100vw"
              className="object-cover"
            />
          </div>
        ) : null}
      </div>
    </section>
  );
}
