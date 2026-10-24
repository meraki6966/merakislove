import Link from "next/link";
import Image from "next/image";
import { packageMeta, type Package } from "@/lib/packages";

interface PackageCardProps {
  pkg: Package;
  /**
   * "home" uses the short sell, "hub" uses the who-it-is-for copy from the
   * packages page. Both render the same card so the two surfaces stay in sync.
   */
  variant?: "home" | "hub";
}

/**
 * The engraving for each package, from the illustration series in
 * public/art. Keyed by slug so the packages data stays free of design.
 */
const art: Record<string, { src: string; alt: string }> = {
  review: {
    src: "/art/review.jpg",
    alt: "Engraving of a brass magnifying glass over an open ledger, with a pen and a small padlock.",
  },
  bip: {
    src: "/art/bip.jpg",
    alt: "Engraving of a brass switchboard of dials and lamps, one hand adjusting a dial.",
  },
  custom: {
    src: "/art/custom.jpg",
    alt: "Engraving of hands pinning a blueprint on a drafting table under a lamp, with a compass and a square.",
  },
};

/**
 * One of the three ways to start. 2026-10 redesign: an engraving on top,
 * Archivo for the name and the price line, and no 01/02/03 markers, since
 * the three packages are options rather than steps. No tilt on hover; the
 * card is a link target, not a toy.
 *
 * Both variants lead into the package's own page. The hub adds the explicit
 * "See what's included" link, since a visitor already on the hub is
 * comparing rather than discovering.
 */
export default function PackageCard({ pkg, variant = "home" }: PackageCardProps) {
  const body = variant === "home" ? pkg.summary : pkg.detail ?? pkg.summary;
  const picture = art[pkg.slug];

  return (
    <article className="group flex h-full flex-col overflow-hidden rounded-2xl bg-navy ring-1 ring-border-mid transition-shadow duration-300 hover:ring-amber/60">
      {picture ? (
        <div className="relative aspect-[4/3] overflow-hidden">
          <Image
            src={picture.src}
            alt={picture.alt}
            fill
            sizes="(min-width: 768px) 33vw, 100vw"
            className="object-cover"
          />
        </div>
      ) : null}

      <div className="flex flex-1 flex-col gap-4 p-7 sm:p-8">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <h3 className="type-heading text-3xl text-smoke">{pkg.name}</h3>
          {pkg.featured ? (
            <span className="rounded-full bg-amber px-3 py-1 font-sans text-xs font-semibold text-void">
              Most chosen
            </span>
          ) : null}
        </div>

        <p className="font-sans text-sm font-semibold text-amber">
          {packageMeta(pkg)}
        </p>

        <p className="font-body text-base leading-relaxed text-smoke-dim">
          {body}
        </p>

        <div className="mt-auto flex flex-col gap-3 pt-4">
          {variant === "hub" ? (
            <Link
              href={pkg.detailHref}
              className="w-fit font-sans text-sm font-semibold text-smoke underline decoration-amber/60 underline-offset-4 transition-colors hover:text-amber"
            >
              See what&apos;s included
            </Link>
          ) : null}
          <Link
            href={variant === "hub" ? "/start" : pkg.detailHref}
            className="w-fit font-sans text-sm font-semibold text-smoke underline decoration-amber/60 underline-offset-4 transition-colors hover:text-amber"
          >
            {pkg.cta}
          </Link>
        </div>
      </div>
    </article>
  );
}
