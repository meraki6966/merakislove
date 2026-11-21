import type { Metadata } from "next";
import PageHero from "@/components/PageHero";
import Panel, { PageStack } from "@/components/Panel";
import ScrollReveal from "@/components/ScrollReveal";
import Breadcrumb from "@/components/Breadcrumb";
import Faq, { type FaqItem } from "@/components/Faq";
import { calendly, ogBase } from "@/lib/site";

const path = "/services/small-business-it";
const url = `https://merakislove.com${path}`;
const title = "Small Business IT and Network Security in Houston";
const description =
  "Network rebuilds, secure computers, remote access, and an owner dashboard for small businesses around Houston and the Gulf Coast. CISSP-certified, with every account in the owner's name.";

export const metadata: Metadata = {
  title,
  description,
  alternates: { canonical: path },
  openGraph: {
    ...ogBase,
    title: `${title} · Soulful Tech`,
    description,
    url,
  },
};

const forWho = [
  "Shops, studios, and offices with roughly 5 to 25 computers",
  "Owners whose old IT provider still holds the keys, or who aren't sure who does",
  "Teams that need to reach their files and computers from home or on the road",
  "Businesses that want to see what's happening on their network without learning to be an IT department",
];

const services = [
  {
    name: "Take back control",
    body: "Every account moves into the owners' names: the network, the computer management tool, the admin logins, and the recovery codes. Old remote tools and leftover accounts from the last provider get found and shut off, and the owners get a password vault of their own.",
  },
  {
    name: "Rebuild the network",
    body: "A fresh UniFi network set up under your account, with separate networks for the office, the production equipment, the server, and guests. New Wi-Fi passwords, a guest network that can't reach business systems, the firewall on, and nothing open to the internet that doesn't need to be.",
  },
  {
    name: "Secure every computer",
    body: "Each computer gets checked, cleaned, and set up the same way: a shop-owned admin account, everyday accounts with standard rights, encryption with the recovery keys in your vault, updates on, and antivirus confirmed. Files get copied before anything changes.",
  },
  {
    name: "Remote access that only reaches what it should",
    body: "A VPN on your own gateway, one profile per person per device, so a lost phone means turning off one profile and nothing else. Each person reaches their own desk computer and the shared files, and the rest of the network stays closed to them.",
  },
  {
    name: "Computer management and alerts",
    body: "Every computer reports its health, updates, and security to a management tool in your name. I get the alerts, and remote help is there when someone needs it, with the person asked before anyone sees their screen.",
  },
  {
    name: "The owner dashboard",
    body: "One page on your phone that shows the shop at a glance: each computer by the person who uses it, whether the network is healthy, open alerts, and who has touched your systems and when. Owner buttons can lock a screen, send a message, or restart a computer. An optional AI briefing can sum up the day in a few plain sentences and answer questions about the shop.",
  },
];

const steps = [
  {
    name: "A free call",
    body: "Thirty minutes to hear what's going on and what you want to fix.",
  },
  {
    name: "A written scope and price",
    body: "Each phase of the work, what it includes, and what it costs, before anything starts. Nothing gets touched until you approve it in writing.",
  },
  {
    name: "A deposit, then the work",
    body: "Fifty percent starts each phase. I schedule shop work around your hours, so the busy days keep running.",
  },
  {
    name: "Each phase closes in writing",
    body: "You get a note saying what's done and what's still open, and the balance is due within seven days.",
  },
];

const prices = [
  {
    name: "Network and computer reset",
    detail: "Control back in your name, network rebuilt, password vault, server check",
    price: "From $1,800, plus $115 per computer",
  },
  {
    name: "Remote access and computer management",
    detail: "VPN, management tool, speed check, plain-English guide",
    price: "From $1,475",
  },
  {
    name: "Owner dashboard",
    detail: "Your shop at a glance, on your phone",
    price: "From $3,400, plus $150 a month for hosting and upkeep",
  },
  {
    name: "IT Care Plan",
    detail: "Monitoring, updates, alerts, a monthly report, and remote support",
    price: "$75 per user per month",
  },
  {
    name: "Extra time",
    detail: "Remote or on site",
    price: "$80 an hour, one-hour minimum on site",
  },
];

const protections = [
  {
    lead: "Your accounts stay in your name.",
    rest: "I get my own named login, and you can remove it any time.",
  },
  {
    lead: "I never hold your passwords.",
    rest: "You type them at a hidden prompt and save them in your own vault.",
  },
  {
    lead: "Two-step sign-in on everything that matters,",
    rest: "starting with email, banking, and the network.",
  },
  {
    lead: "Nothing gets deleted until it's copied,",
    rest: "and nothing gets changed until the replacement works.",
  },
  {
    lead: "Everything gets written down,",
    rest: "so you or anyone after me can see exactly how your systems are set up.",
  },
];

const faqs: FaqItem[] = [
  {
    question: "Will my business go offline?",
    answer:
      "Most of the work happens with everyone working. The few steps that drop the internet or the network get scheduled when you're closed, and I tell you ahead of time.",
  },
  {
    question: "Do I have to replace my equipment?",
    answer:
      "Usually not. I start with what you have, and I'll tell you plainly when something is past its useful life, like computers that no longer get security updates.",
  },
  {
    question: "What if my old IT company won't cooperate?",
    answer:
      "That's common, and it's exactly where this work starts. Everything they set up can be reset into your name, step by step, without waiting on them.",
  },
  {
    question: "Can I see what my staff do on company computers?",
    answer:
      "The dashboard can show who's signed in, how long a computer has been idle, and which programs are open. Your staff should know that first, so I give you a plain-language notice for your attorney to review and your team to sign.",
  },
];

const serviceSchema = {
  "@context": "https://schema.org",
  "@type": "Service",
  "@id": `${url}/#service`,
  name: "Small business IT and network security",
  serviceType: "IT and network security for small businesses",
  description,
  url,
  areaServed: [
    { "@type": "City", name: "Houston" },
    { "@type": "Place", name: "Gulf Coast, Texas" },
  ],
  provider: {
    "@type": "Organization",
    name: "Meraki is Love, LLC",
    url: "https://merakislove.com",
  },
};

const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": `${url}/#faq`,
  mainEntity: faqs.map((item) => ({
    "@type": "Question",
    name: item.question,
    acceptedAnswer: { "@type": "Answer", text: item.answer },
  })),
};

const label = "font-sans font-semibold text-sm text-amber";
const h2 = "type-heading text-3xl text-smoke sm:text-4xl";
const body = "font-body text-base leading-relaxed text-smoke-dim";

export default function SmallBusinessItPage() {
  return (
    <>
      <Breadcrumb
        items={[
          { name: "Security", path: "/cybersecurity" },
          { name: "Small business IT", path },
        ]}
      />
      {[serviceSchema, faqSchema].map((schema, i) => (
        <script
          key={i}
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(schema).replace(/</g, "\\u003c"),
          }}
        />
      ))}
      <PageStack>
        <PageHero
          art={{
            src: "/art/hero-key.jpg",
            alt: "Engraving of two hands fitting a brass key into an open lock on a workbench, with a ledger, a padlock and a small lantern.",
          }}
          kicker="Small business IT"
          title="Your business, your network, your keys"
          subtitle="IT and network security for small businesses around Houston and the Gulf Coast. I take back control from the last provider, secure every computer, and give the owners a clear view of it all from their phones."
        >
          <ScrollReveal delay={0.1}>
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-sans font-semibold text-sm text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a free call
            </a>
          </ScrollReveal>
        </PageHero>

        <Panel tone="paper" width="6xl">
          <section className="grid gap-12 md:grid-cols-[1.2fr_1fr]">
            <ScrollReveal className="flex flex-col gap-5">
              <p className={label}>Where this work starts</p>
              <p className={body}>
                I recently stood in a small local shop with its owners, swapping
                a switch, moving the internet box into passthrough, and building
                the VPN they now use to reach their desks from anywhere. Their
                last IT company still held the passwords to the server, the
                network, and every computer. Today all of it sits in the
                owners&apos; names, in a vault they control.
              </p>
              <p className={body}>
                That&apos;s the heart of this service. A small business deserves to
                own its own technology, understand it, and sleep at night knowing
                it&apos;s protected. I bring twenty years in software and security, a
                CISSP, and a habit of writing everything down in plain English.
              </p>
            </ScrollReveal>
            <ScrollReveal delay={0.08} className="flex flex-col gap-5">
              <p className={label}>Who it&apos;s for</p>
              <ul className="flex flex-col gap-3">
                {forWho.map((item) => (
                  <li key={item} className={`${body} border-l border-amber pl-4`}>
                    {item}
                  </li>
                ))}
              </ul>
            </ScrollReveal>
          </section>
        </Panel>

        <Panel tone="ink" width="6xl">
          <section>
            <ScrollReveal className="mb-12 flex flex-col gap-4">
              <p className={label}>What I do</p>
              <h2 className={h2}>From the last provider&apos;s keys to your own</h2>
            </ScrollReveal>
            <div className="grid gap-6 md:grid-cols-2">
              {services.map((service, i) => (
                <ScrollReveal key={service.name} delay={i * 0.05} className="h-full">
                  <div
                    id={service.name.toLowerCase().replace(/[^a-z0-9]+/g, "-")}
                    className="flex h-full scroll-mt-28 flex-col gap-3 rounded-xl border border-border-mid bg-navy/40 p-7"
                  >
                    <h3 className="type-heading text-2xl text-smoke">{service.name}</h3>
                    <p className="font-body text-sm leading-relaxed text-smoke-dim">
                      {service.body}
                    </p>
                  </div>
                </ScrollReveal>
              ))}
            </div>
            <ScrollReveal className="mt-10">
              <div className="flex flex-col gap-3 rounded-xl border border-border p-7">
                <h3 className="type-heading text-xl text-smoke">
                  What I leave to the specialists
                </h3>
                <p className="font-body text-sm leading-relaxed text-smoke-dim">
                  I don&apos;t run cable or install cameras. When a job needs new cable
                  runs or camera work, I&apos;ll tell you exactly what to ask for, and a
                  licensed installer handles that part.
                </p>
              </div>
            </ScrollReveal>
          </section>
        </Panel>

        <Panel tone="paper" width="6xl">
          <section>
            <ScrollReveal className="mb-10 flex flex-col gap-4">
              <p className={label}>How it works</p>
              <h2 className={h2}>Nothing gets touched until you approve it in writing</h2>
            </ScrollReveal>
            <ol className="grid gap-6 md:grid-cols-4">
              {steps.map((step, i) => (
                <ScrollReveal key={step.name} delay={i * 0.05} className="h-full">
                  <li className="flex h-full flex-col gap-3 rounded-xl border border-border-mid bg-navy/40 p-6">
                    <span className="type-heading text-3xl text-amber">{i + 1}</span>
                    <h3 className="font-sans text-lg font-semibold text-smoke">{step.name}</h3>
                    <p className="font-body text-sm leading-relaxed text-smoke-dim">{step.body}</p>
                  </li>
                </ScrollReveal>
              ))}
            </ol>
          </section>
        </Panel>

        <Panel tone="ink" width="6xl">
          <section id="pricing" className="scroll-mt-28">
            <ScrollReveal className="mb-10 flex flex-col gap-4">
              <p className={label}>Pricing</p>
              <h2 className={h2}>Starting points</h2>
              <p className={body}>Your written scope sets the real number.</p>
            </ScrollReveal>
            <div className="flex flex-col overflow-hidden rounded-2xl ring-1 ring-border-mid">
              {prices.map((row) => (
                <div
                  key={row.name}
                  className="grid gap-2 border-b border-border px-6 py-5 last:border-b-0 sm:grid-cols-[1.3fr_1fr] sm:items-center sm:px-8"
                >
                  <div>
                    <p className="font-sans text-lg font-semibold text-smoke">{row.name}</p>
                    <p className="font-body text-sm text-smoke-dim">{row.detail}</p>
                  </div>
                  <p className="font-sans font-semibold text-amber sm:text-right">{row.price}</p>
                </div>
              ))}
            </div>
          </section>
        </Panel>

        <Panel tone="paper" width="6xl">
          <section className="grid gap-12 md:grid-cols-2">
            <ScrollReveal className="flex flex-col gap-5">
              <p className={label}>How I protect your business while I work</p>
              <ul className="flex flex-col gap-4">
                {protections.map((item) => (
                  <li key={item.lead} className={body}>
                    <span className="font-semibold text-smoke">{item.lead}</span>{" "}
                    {item.rest}
                  </li>
                ))}
              </ul>
            </ScrollReveal>
            <ScrollReveal delay={0.08} className="flex flex-col gap-5">
              <p className={label}>Questions owners ask</p>
              <Faq items={faqs} />
            </ScrollReveal>
          </section>
        </Panel>

        <Panel tone="dusk" width="6xl">
          <ScrollReveal>
            <div
              className="rounded-2xl p-px"
              style={{
                background: "linear-gradient(135deg, var(--color-gold), var(--color-amber) 120%)",
              }}
            >
              <div className="flex flex-col items-start gap-6 rounded-2xl bg-void p-10 sm:p-14">
                <h2 className={`max-w-2xl ${h2}`}>Ready when you are</h2>
                <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim">
                  If your network still feels like someone else&apos;s, let&apos;s change
                  that. Book a free 30-minute call, tell me what&apos;s going on, and
                  I&apos;ll tell you honestly what it takes to put it back in your hands.
                </p>
                <a
                  href={calendly.newProject}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-3 rounded-full bg-amber! px-7 py-3.5 font-sans font-semibold text-sm text-void transition-transform duration-300 hover:scale-[1.02]"
                >
                  Book a free call
                </a>
                <p className="font-sans text-sm text-smoke-dim">
                  Soulful Tech. Technology built with intention and purpose.
                </p>
              </div>
            </div>
          </ScrollReveal>
        </Panel>
      </PageStack>
    </>
  );
}
