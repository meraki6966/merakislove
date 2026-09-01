import type { Metadata } from "next";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import Breadcrumb from "@/components/Breadcrumb";
import { calendly, ogBase } from "@/lib/site";

const description =
  "Enterprise-grade security services from a CISSP-certified engineer. Site security audits, posture reviews, hardening, and AI security integration review, all mapped to MITRE ATT&CK and powered by Canopy Guard.";

export const metadata: Metadata = {
  title: "Security Services",
  description,
  alternates: { canonical: "/cybersecurity" },
  openGraph: {
    ...ogBase,
    title: "Security Services · Soulful Tech",
    description,
    url: "https://merakislove.com/cybersecurity",
  },
};

// Page-specific credential set — emphasizes the security side of the practice.
const securityCredentials = [
  "CISSP",
  "Azure AI Engineer",
  "Dual MS Cybersecurity · UMGC",
  "MITRE ATT&CK Mapped",
  "20+ Years",
];

interface SecurityService {
  name: string;
  price: string;
  /** Short framing tag shown above the name. */
  tag: string;
  description: string;
}

const securityServices: SecurityService[] = [
  {
    name: "Site Security Audit",
    price: "$500 – $750",
    tag: "One-time",
    description:
      "One-time Canopy Guard assessment plus manual review. Findings mapped to MITRE ATT&CK. Client-ready PDF report.",
  },
  {
    name: "Security Posture Review",
    price: "$1,500 – $3,000",
    tag: "Architecture",
    description:
      "Architecture-level review. Headers, TLS, dependency audit, and data-handling paths.",
  },
  {
    name: "Security Hardening",
    price: "$1,000 – $2,500",
    tag: "Remediation",
    description:
      "Remediation of audit findings. Also available hourly at $85/hr.",
  },
  {
    name: "AI Security Integration Review",
    price: "$1,500 – $3,500",
    tag: "AI Systems",
    description:
      "Guardrails, data-exposure review, output validation, and prompt-injection risk.",
  },
  {
    name: "Monthly Security Retainer",
    price: "$200+/mo",
    tag: "Ongoing",
    description:
      "Ongoing advisory, quarterly audit reruns, and priority response.",
  },
];

export default function CybersecurityPage() {
  return (
    <>
      <Breadcrumb items={[{ name: "Security", path: "/cybersecurity" }]} />
    <div className="mx-auto max-w-6xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <PageHeader
        eyebrow="Security Services"
        title="Enterprise-grade security. Built for the businesses that can't afford a breach."
        subtitle="A CISSP-led security practice for teams that need the depth enterprises pay six figures for, scoped and priced for the businesses that ship real software."
      />

      {/* Credentials strip */}
      <ScrollReveal className="mt-12">
        <div className="flex flex-wrap items-center gap-3">
          {securityCredentials.map((credential) => (
            <span
              key={credential}
              className="rounded-full border border-border-mid bg-navy/40 px-4 py-2 font-mono text-xs uppercase tracking-[0.16em] text-smoke-dim"
            >
              {credential}
            </span>
          ))}
        </div>
      </ScrollReveal>

      {/* Services with pricing */}
      <section className="mt-24">
        <ScrollReveal className="mb-12 flex flex-col gap-4">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Engagements
          </p>
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">
            Scoped services, transparent pricing
          </h2>
        </ScrollReveal>

        <div className="grid gap-6 md:grid-cols-2">
          {securityServices.map((service, i) => (
            <ScrollReveal key={service.name} delay={i * 0.06} className="h-full">
              <div className="flex h-full flex-col gap-4 rounded-xl border border-border-mid bg-navy/40 p-7">
                <div className="flex items-start justify-between gap-4">
                  <h3 className="font-display text-2xl font-light text-smoke">
                    {service.name}
                  </h3>
                  <span className="whitespace-nowrap font-mono text-xs uppercase tracking-[0.14em] text-amber">
                    {service.tag}
                  </span>
                </div>
                <p className="font-display text-3xl font-light text-amber">
                  {service.price}
                </p>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  {service.description}
                </p>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </section>

      {/* Powered by Canopy Guard */}
      <ScrollReveal className="mt-24">
        <div className="grid gap-8 rounded-2xl border border-border bg-void p-8 sm:p-12 md:grid-cols-[1fr_auto] md:items-center">
          <div className="flex flex-col gap-5">
            <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
              Powered by Canopy Guard
            </p>
            <h2 className="max-w-2xl font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
              Every audit runs on the same engine I built for the enterprise
            </h2>
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              Canopy Guard is my automated visibility and security audit engine.
              It assesses a site across dozens of signals, maps the findings to
              the MITRE ATT&CK framework, and produces the client-ready report
              that anchors every engagement on this page.
            </p>
          </div>
          <a
            href="https://thecanopyguard.com"
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center gap-3 self-start rounded-full border border-amber px-6 py-3 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void md:self-center"
          >
            Visit thecanopyguard.com
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </a>
        </div>
      </ScrollReveal>

      {/* Referral program */}
      <ScrollReveal className="mt-12">
        <div className="flex flex-col gap-5 rounded-2xl border border-border-mid bg-navy/40 p-8 sm:p-12">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Referrals
          </p>
          <h2 className="max-w-2xl font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
            Know a business that needs this? Earn 15 – 25% on every referral.
          </h2>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            If you send a client my way and the engagement closes, you earn a
            referral commission of 15 to 25% of the contract value. No cap on how
            many you send, and you are paid when the client pays.
          </p>
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center gap-3 self-start font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:text-amber"
          >
            Talk through a referral
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </a>
        </div>
      </ScrollReveal>

      {/* Primary CTA */}
      <ScrollReveal className="mt-12">
        <div
          className="rounded-2xl p-px"
          style={{
            background:
              "linear-gradient(135deg, var(--color-purple), var(--color-amber) 120%)",
          }}
        >
          <div className="flex flex-col items-start gap-6 rounded-2xl bg-void p-10 sm:p-14">
            <h2 className="max-w-2xl font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
              Find out what an attacker sees before they do.
            </h2>
            <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim">
              Start with a conversation. We will scope the right level of review
              for where your business actually is, not where a checklist says it
              should be.
            </p>
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="group inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a call
              <span className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </a>
          </div>
        </div>
      </ScrollReveal>
    </div>
    </>
  );
}
