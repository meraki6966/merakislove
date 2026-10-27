import type { Metadata } from "next";
import Link from "next/link";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ScrollReveal from "@/components/ScrollReveal";
import Breadcrumb from "@/components/Breadcrumb";
import ShadowAiCheck from "@/components/ShadowAiCheck";
import { calendly, ogBase } from "@/lib/site";

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

/**
 * The paid follow-on to the self-assessment. Prices set by Adam on 26
 * October 2026: $850 one-time for up to five tools, $85 per extra tool, and
 * the quarterly check as a separate $175 a quarter. Vendor retention and
 * training settings vary, so the copy promises the setup where a vendor
 * allows it, never zero retention outright.
 */
const governanceKit = {
  name: "AI Governance Kit",
  priceLabel: "$850 one-time",
  lead: "When your answers show gaps, this closes them with written rules your team can follow.",
  includes: [
    "A written AI use policy: which tools are approved, and what may and may not go into them.",
    "A vendor checklist for each tool your team uses: how long it keeps your data, whether it trains on it, and whether a DPA or BAA is available. Up to five tools are included, and each one after that is $85.",
    "An approved workspace set up with data retention and model training turned off where the vendor allows it.",
    "A walkthrough call with whoever will own the rules.",
  ],
  optional: "Optional quarterly check, $175 a quarter: we rerun this assessment with your team and update the policy for any new tools.",
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
      <Panel tone="paper" width="4xl" id="governance-kit">
        <ScrollReveal className="">
          <div className="rounded-xl border border-amber/60 bg-navy/40 p-7 sm:p-8">
            <div className="flex flex-col gap-1 sm:flex-row sm:items-baseline sm:justify-between sm:gap-6">
              <h2 className="type-heading text-2xl text-smoke sm:text-3xl">
                {governanceKit.name}
              </h2>
              <p className="type-heading text-2xl text-amber">
                {governanceKit.priceLabel}
              </p>
            </div>
            <p className="mt-3 max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              {governanceKit.lead}
            </p>
            <ul className="mt-5 flex flex-col gap-2.5">
              {governanceKit.includes.map((line) => (
                <li
                  key={line}
                  className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim"
                >
                  <span
                    aria-hidden
                    className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-amber"
                  />
                  {line}
                </li>
              ))}
            </ul>
            <p className="mt-5 max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
              {governanceKit.optional}
            </p>
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-6 inline-flex items-center justify-center rounded-full bg-amber px-7 py-3.5 font-sans font-semibold text-sm text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a call about the kit
            </a>
          </div>
        </ScrollReveal>

        <ScrollReveal className="mt-12">
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
