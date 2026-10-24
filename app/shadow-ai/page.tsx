import type { Metadata } from "next";
import Link from "next/link";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ScrollReveal from "@/components/ScrollReveal";
import Breadcrumb from "@/components/Breadcrumb";
import ShadowAiCheck from "@/components/ShadowAiCheck";
import { ogBase } from "@/lib/site";

const title = "Shadow AI Self-Assessment | Meraki is Love";

const description =
  "Ten questions on the AI tools your team uses, what goes into them and whether anyone has set rules. Your answers stay in your browser and are never sent.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/shadow-ai" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/shadow-ai",
  },
};

export default function ShadowAiPage() {
  return (
    <PageStack>
      <Breadcrumb items={[{ name: "Shadow AI self-assessment", path: "/shadow-ai" }]} />

      <PageHero
        art={{
          src: "/art/shadow.jpg",
          alt: "Engraving of a hand holding up a lantern in a dark office, its light revealing papers and devices on the desk.",
        }}
        kicker="Self-assessment"
        title="Find the AI tools your team already uses."
        subtitle="Shadow AI is any AI tool people use for work that the business never chose or set up. These ten questions cover which tools your team uses, what goes into them, and whether anyone has written down the rules."
      />

      <Panel tone="paper" width="4xl">
        <ScrollReveal className="">
          <div className="rounded-xl border border-border-mid bg-navy/40 p-6 sm:p-7">
            <p className="font-sans font-semibold text-sm text-amber">
              Your answers stay with you
            </p>
            <p className="mt-3 max-w-2xl font-body text-base leading-relaxed text-smoke">
              The questions and the scoring run in this browser tab. Nothing is sent and nothing is saved, so closing the tab clears your answers. Google Analytics counts visits to this page, as it does across the site, and never receives your answers.{" "}
              <Link href="/privacy" className="text-amber underline underline-offset-4 hover:text-smoke">
                Privacy
              </Link>
            </p>
          </div>
        </ScrollReveal>

        <ScrollReveal className="mt-12">
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            I built this for owners who know their team uses AI and want to see where the gaps are before spending anything. Answer for how things work today. If you&apos;re not sure, pick the answer that says so.
          </p>
        </ScrollReveal>

      </Panel>
      <Panel tone="ink" width="4xl">
        <section aria-label="The ten questions" className="">
          <ShadowAiCheck />
        </section>

      </Panel>
      <Panel tone="paper" width="4xl">
        <ScrollReveal className="">
          <div className="border-l-2 border-amber pl-6">
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              Canopy Guard checks your website from the outside, free. This page looks at how your team works on the inside.
            </p>
            <a
              href="https://thecanopyguard.com"
              target="_blank"
              rel="noopener noreferrer"
              className="mt-3 inline-block font-sans font-semibold text-sm text-amber hover:text-smoke"
            >
              Run a Canopy Guard audit
            </a>
          </div>
        </ScrollReveal>
      </Panel>
    </PageStack>
  );
}
