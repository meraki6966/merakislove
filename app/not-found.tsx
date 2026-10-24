import Link from "next/link";
import type { Metadata } from "next";
import PageHero from "@/components/PageHero";
import { PageStack } from "@/components/Panel";

export const metadata: Metadata = {
  title: "Not found",
  robots: { index: false, follow: true },
};

export default function NotFound() {
  return (
    <PageStack>
      <PageHero
        kicker="404"
        title="This page is gone. The work is not."
        art={{
          src: "/art/door.jpg",
          alt: "Engraving of a door standing open at dusk, warm light falling across the step.",
        }}
      >
        <div className="flex flex-col gap-3 sm:flex-row">
          <Link
            href="/start"
            className="inline-flex items-center justify-center rounded-full bg-amber! px-7 py-4 font-sans text-base font-semibold text-void transition-colors hover:bg-gold!"
          >
            Book a call
          </Link>
          <Link
            href="/packages"
            className="inline-flex items-center justify-center rounded-full px-7 py-4 font-sans text-base font-semibold text-smoke ring-1 ring-smoke/40 transition-colors hover:ring-amber"
          >
            Packages
          </Link>
        </div>
      </PageHero>
    </PageStack>
  );
}
