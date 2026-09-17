import type { Metadata } from "next";
import Link from "next/link";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import PackageCard from "@/components/PackageCard";
import Breadcrumb from "@/components/Breadcrumb";
import Faq, { type FaqItem } from "@/components/Faq";
import { packages, engagementTypes } from "@/lib/packages";
import { ogBase } from "@/lib/site";

const title = "Packages | Meraki is Love";

const description =
  "Review, BIP, or a custom build. Clear scope. Clear price band. No deck.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/packages" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/packages",
  },
};

const howToChoose = [
  "Buy the review if you have something live and you cannot defend it.",
  "Buy BIP if the inbox, the leads, and the follow-up are the bottleneck.",
  "Buy custom if the product is the business, or the place itself is the product.",
  "If you are unsure, book the call. That is what it is for.",
];

const faqs: FaqItem[] = [
  {
    question: "Can I start small?",
    answer:
      "Yes. The five-day review exists so you do not have to buy a six-week build to find out where you stand.",
  },
  {
    question: "Do you only work in Texas?",
    answer:
      "No. The work is remote. Clients are already in New York, California, Chicago, North Carolina, Houston, and Austin.",
  },
  {
    question: "I already pay for ChatGPT.",
    answer:
      "Good. That is a tool. It is not trained on your fee schedule, it is not mapped to your threat model, and it does not prospect while you are in session.",
  },
  {
    question: "What do you not take?",
    answer:
      "The cheapest possible version by Friday. AI bolted onto a weak site with nothing else changed. Work I would not put my name on.",
  },
  {
    question: "Do you build WordPress and simple sites?",
    answer:
      "Yes, when that is the right door. If the business sells atmosphere, I will point you to Presence-First instead of a template.",
  },
  {
    question: "How do we start?",
    answer:
      "A 20-minute call. No deck. If I am the wrong fit, I will say that and point you somewhere better.",
  },
];

export default function PackagesPage() {
  return (
    <>
      <Breadcrumb items={[{ name: "Packages", path: "/packages" }]} />
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Packages"
        title="Three ways to work together."
        subtitle="Start with the smallest thing that answers the real question. Do not buy a platform if you need a report. Do not buy a report if you already know you need the system."
      />

      {/* The three packages */}
      <div className="mt-16 grid gap-6 md:grid-cols-3">
        {packages.map((pkg, i) => (
          <ScrollReveal key={pkg.slug} delay={i * 0.08} className="h-full">
            <PackageCard pkg={pkg} variant="hub" />
          </ScrollReveal>
        ))}
      </div>

      {/* How to choose */}
      <section className="mt-24">
        <ScrollReveal className="mb-10 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            How to choose
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            Pick the door, not the catalogue.
          </h2>
        </ScrollReveal>

        <ul className="flex flex-col gap-px overflow-hidden rounded-xl border border-border bg-border">
          {howToChoose.map((line, i) => (
            <ScrollReveal
              key={line}
              as="li"
              delay={i * 0.05}
              className="bg-void px-6 py-5 font-body text-base leading-relaxed text-smoke-dim sm:px-8"
            >
              {line}
            </ScrollReveal>
          ))}
        </ul>
      </section>

      {/* Engagement types */}
      <section className="mt-24">
        <ScrollReveal className="mb-10 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Engagement types
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            How the work is structured.
          </h2>
        </ScrollReveal>

        <div className="grid gap-6 sm:grid-cols-3">
          {engagementTypes.map((type, i) => (
            <ScrollReveal key={type.name} delay={i * 0.06} className="h-full">
              <div className="flex h-full flex-col gap-4 rounded-xl border border-border-mid bg-navy/40 p-7">
                <h3 className="font-display text-2xl font-light text-smoke">
                  {type.name}
                </h3>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {type.detail}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>

        <ScrollReveal className="mt-8">
          <p className="font-body text-sm leading-relaxed text-smoke-dim">
            The starting door is still a project.
          </p>
        </ScrollReveal>
      </section>

      {/* FAQ */}
      <section className="mt-24">
        <ScrollReveal className="mb-10 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            FAQ
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            The questions that come up first.
          </h2>
        </ScrollReveal>

        <ScrollReveal>
          <Faq items={faqs} />
        </ScrollReveal>
      </section>

      {/* CTA */}
      <ScrollReveal className="mt-24">
        <div
          className="rounded-2xl p-px"
          style={{
            background:
              "linear-gradient(135deg, var(--color-gold), var(--color-amber) 120%)",
          }}
        >
          <div className="flex flex-col items-start gap-6 rounded-2xl bg-void p-10 sm:p-14">
            <h2 className="max-w-2xl font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
              One conversation. No deck.
            </h2>
            <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim">
              Twenty minutes. I will tell you which of the three is the right
              door, or whether I am the wrong person.
            </p>
            <Link
              href="/start"
              className="group inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a 20-minute call
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </Link>
          </div>
        </div>
      </ScrollReveal>
    </div>
    </>
  );
}
