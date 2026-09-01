import Link from "next/link";
import TiltCard from "@/components/TiltCard";
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
 * One of the three ways to start. Built on the shared TiltCard so the hover
 * language matches the project cards, with the default amber glow rather than
 * a per-card accent. Restraint is the point: the only saturated element on
 * the page is the Book a call button.
 *
 * Both variants lead into the package's own page. The hub adds the explicit
 * "See what's included" link from the copy above the action, since a visitor
 * already on the hub is comparing rather than discovering.
 */
export default function PackageCard({ pkg, variant = "home" }: PackageCardProps) {
  const body = variant === "home" ? pkg.summary : pkg.detail ?? pkg.summary;

  return (
    <TiltCard className="group flex h-full flex-col bg-navy/40">
      <div className="flex h-full flex-col gap-5 p-7 sm:p-8">
        {/* Fixed height so the badge on the featured card does not push its
            title out of line with the other two. */}
        <div className="flex min-h-7 flex-wrap items-center justify-between gap-3">
          <span className="font-mono text-xs tracking-[0.2em] text-amber">
            {pkg.number}
          </span>
          {pkg.featured ? (
            <span className="inline-flex items-center rounded-full border border-amber/50 bg-amber-dim px-3 py-1 font-mono text-[0.65rem] uppercase tracking-[0.16em] text-amber">
              Most chosen
            </span>
          ) : null}
        </div>

        <h3 className="font-display text-3xl font-light leading-tight text-smoke">
          {pkg.name}
        </h3>

        <p className="font-mono text-xs uppercase tracking-[0.16em] text-smoke">
          {packageMeta(pkg)}
        </p>

        <p className="font-body text-sm leading-relaxed text-smoke-dim">
          {body}
        </p>

        <div className="mt-auto flex flex-col gap-3 border-t border-border pt-5">
          {variant === "hub" ? (
            <Link
              href={pkg.detailHref}
              className="inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 group-hover:text-amber"
            >
              See what&apos;s included
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
          ) : null}
          <Link
            href={variant === "hub" ? "/start" : pkg.detailHref}
            className={`inline-flex w-fit items-center gap-3 font-mono text-xs uppercase tracking-[0.18em] transition-colors duration-300 ${
              variant === "hub"
                ? "text-smoke-dim hover:text-amber"
                : "text-smoke group-hover:text-amber"
            }`}
          >
            {pkg.cta}
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </Link>
        </div>
      </div>
    </TiltCard>
  );
}
