import Link from "next/link";
import { calendly } from "@/lib/site";

interface PackageActionsProps {
  /** The page's own conversion. Routes to /start, where the form lives. */
  label: string;
  /**
   * Adds the outline "Book a call" beside it, going straight to Calendly for
   * someone who only wants a slot. Same pattern the work page already uses.
   */
  bookCall?: boolean;
}

/**
 * The action row that closes every package detail page.
 *
 * The package-specific action is the one saturated button, because it is what
 * the page exists to do. "Book a call" sits beside it as an outline, so the
 * two buttons lead somewhere genuinely different rather than both landing on
 * the same page under two labels.
 */
export default function PackageActions({ label, bookCall }: PackageActionsProps) {
  return (
    <div className="mt-10 flex flex-col gap-4 sm:flex-row sm:items-center">
      <Link
        href="/start"
        className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-4 font-sans font-semibold text-base text-void transition-colors duration-300 hover:bg-gold!"
      >
        {label}
      </Link>
      {bookCall ? (
        <a
          href={calendly.newProject}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-4 font-sans font-semibold text-base text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
        >
          Book a call
        </a>
      ) : null}
    </div>
  );
}
