import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import StartForm from "@/components/StartForm";
import Breadcrumb from "@/components/Breadcrumb";
import { calendly, email, ogBase } from "@/lib/site";

const title = "Book a call | Meraki is Love";

const description =
  "Twenty minutes. Tell me what you run and where it hurts, and I will tell you which door is the right one.";

export const metadata: Metadata = {
  // Absolute so the pipe-separated title survives the layout template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/start" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com/start",
  },
};

export default function StartPage() {
  return (
    <>
      <Breadcrumb items={[{ name: "Book a call", path: "/start" }]} />
    <div className="mx-auto max-w-4xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        title="One conversation. No deck."
        subtitle="20 minutes. Tell me what you run and where it hurts. I will tell you whether the review, BIP, or a custom build is the right door, or whether I am the wrong person."
      />

      {/* Booking.
          Calendly is linked rather than embedded. Embedding the widget would
          mean allowing a third-party script and iframe through the site's
          Content-Security-Policy, and this studio sells not handing client
          data to public tools. The header stays strict; the booking page is
          one click away. */}
      <ScrollReveal className="mt-16">
        <div className="flex flex-col items-start gap-6 rounded-2xl border border-border-mid bg-navy/40 p-8 sm:p-12">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Pick a time
          </p>
          <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim">
            The calendar opens in a new tab. Grab whichever 20 minutes suits
            you and bring the problem, not a brief.
          </p>
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
          >
            Book a 20-minute call
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </a>
        </div>
      </ScrollReveal>

      {/* Write instead */}
      <section className="mt-20">
        <ScrollReveal className="mb-10 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Or write instead
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            Rather put it in writing?
          </h2>
        </ScrollReveal>

        <ScrollReveal>
          <StartForm />
        </ScrollReveal>
      </section>

      <ScrollReveal className="mt-16 border-t border-border pt-8">
        <a
          href={`mailto:${email}`}
          className="font-mono text-xs tracking-[0.14em] text-smoke-dim transition-colors hover:text-amber"
        >
          {email}
        </a>
      </ScrollReveal>
    </div>
    </>
  );
}
