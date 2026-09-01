import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Not found",
  robots: { index: false, follow: true },
};

export default function NotFound() {
  return (
    <div className="mx-auto flex min-h-[70vh] max-w-4xl flex-col items-start justify-center gap-8 px-6 py-32 sm:px-8">
      <p className="font-mono text-xs uppercase tracking-[0.3em] text-amber">
        404
      </p>
      <h1 className="font-display text-4xl font-light leading-[1.06] text-smoke sm:text-6xl">
        This page is gone. The work is not.
      </h1>
      <div className="flex flex-col gap-4 sm:flex-row sm:items-center">
        <Link
          href="/packages"
          className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
        >
          Packages
        </Link>
        <Link
          href="/start"
          className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
        >
          Book a call
          <span className="transition-transform duration-300 group-hover:translate-x-1">
            →
          </span>
        </Link>
      </div>
    </div>
  );
}
