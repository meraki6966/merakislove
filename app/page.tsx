import Link from "next/link";
import type { Metadata } from "next";
import Image from "next/image";
import PackageCard from "@/components/PackageCard";
import { packages } from "@/lib/packages";
import { proofRow, email, ogBase } from "@/lib/site";

const title =
  "Private, Secure AI for Small and Medium Businesses | Meraki is Love";

const description =
  "I build with intention. Private, secure AI for small and medium businesses: the site, the assistant, and the security layer a business can own. Reviews from $500.";

export const metadata: Metadata = {
  // Absolute so the page carries its own full title rather than the layout's
  // "· Soulful Tech" template.
  title: { absolute: title },
  description,
  alternates: { canonical: "/" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url: "https://merakislove.com",
  },
};

const audience = [
  "Faith-based organizations",
  "Medical billing",
  "Tax and advisory",
  "Law and professional firms",
];

const work = [
  {
    name: "Meraki BIP",
    detail:
      "A scheduled lead engine and an assistant trained on your documents, distributing across two platforms from one dashboard.",
  },
  {
    name: "Canopy Guard",
    detail: "Security posture auditor. Findings mapped. Report ready to send.",
  },
  {
    name: "VeloxSync",
    detail:
      "Performance intelligence that flags at-risk talent six weeks before resignation, not a table count.",
  },
  {
    name: "VeloxSync for Education",
    detail:
      "AI-powered homeschool planning, built for families, not classrooms. One plan covers up to six children.",
  },
  {
    name: "Meridian AI",
    detail:
      "Board-ready reports from uploaded files. Scheduled delivery, comparison mode, cover page customization, export history, and a one-click executive summary — MFA and RBAC throughout.",
  },
];

/**
 * Small business demos shown on the home page. Each picture is the demo's
 * own first screen, captured from the live build (public/art/demos).
 * The full set of 11 is on /demos.
 */
const smallBusinessDemos = [
  { name: "The Corner Table", kind: "Restaurant", href: "/demos/restaurant", img: "/art/demos/restaurant.jpg" },
  { name: "Keelhouse Home Services", kind: "Home services", href: "/demos/keelhouse", img: "/art/demos/keelhouse.jpg" },
  { name: "Tessel Dental", kind: "Dental practice", href: "/demos/tessel", img: "/art/demos/tessel.jpg" },
  { name: "Iron Prism", kind: "Gym", href: "/demos/iron-prism", img: "/art/demos/iron-prism.jpg" },
  { name: "Saltbrush Pool Care", kind: "Pool service", href: "/demos/saltbrush", img: "/art/demos/saltbrush.jpg" },
  { name: "Fernhollow Vet", kind: "Veterinary clinic", href: "/demos/fernhollow", img: "/art/demos/fernhollow.jpg" },
];

const steps = [
  {
    title: "Discover",
    detail:
      "We start in conversation. People, constraints, the real goal. Nothing gets proposed until I can argue both sides of the problem.",
  },
  {
    title: "Architect",
    detail:
      "Data model, integrations, failure modes, security posture. On paper, where changing your mind is cheap.",
  },
  {
    title: "Build",
    detail:
      "Tight loops. Previews you can click. The person who took the first call is the person writing the code.",
  },
  {
    title: "Deploy and harden",
    detail:
      "We ship, then we secure. Monitoring, headers, dependencies, a posture you can defend. A product is not done when it works on a good day. It is done when it holds up on a bad one.",
  },
];

export default function Home() {
  return (
    <div className="flex flex-col gap-3 px-2.5 pb-3 pt-[4.5rem] sm:gap-4 sm:px-4 sm:pb-4 sm:pt-24">
      {/* 1 · Hero. A dusk panel with the key-and-lock engraving. On wide
          screens the art fills the panel behind a fade, and a slow loop of
          the same engraving plays over it for anyone who has not asked for
          less motion. On phones the art sits under the words. This is the
          page's one motion moment; nothing else animates on scroll. */}
      <section className="relative overflow-hidden rounded-[28px] bg-navy">
        <div aria-hidden className="absolute inset-0 hidden lg:block">
          <Image
            src="/art/hero-loop-poster.jpg"
            alt=""
            fill
            priority
            sizes="100vw"
            className="object-cover object-[70%_center]"
          />
          <video
            className="hero-loop absolute inset-0 h-full w-full object-cover object-[70%_center]"
            poster="/art/hero-loop-poster.jpg"
            autoPlay
            muted
            loop
            playsInline
            preload="metadata"
          >
            <source src="/art/hero-loop.webm" type="video/webm" />
            <source src="/art/hero-loop.mp4" type="video/mp4" />
          </video>
          <div className="absolute inset-0 bg-[linear-gradient(90deg,#261a2e_0%,#261a2e_32%,rgba(38,26,46,0.86)_42%,rgba(38,26,46,0)_60%)]" />
        </div>

        <div className="relative px-6 pb-12 pt-16 sm:px-12 sm:pb-16 sm:pt-24 lg:min-h-[44rem] lg:px-16 lg:pb-20 lg:pt-28">
          <h1 className="type-display hero-in max-w-[8ch] text-[clamp(3.25rem,8vw,8rem)] text-amber">
            I build with intention.
          </h1>

          <div className="hero-in-late mt-9 flex max-w-[34rem] flex-col gap-7">
            <h2 className="font-sans text-[clamp(1.6rem,2.6vw,2.6rem)] font-medium leading-[1.08] tracking-[-0.015em] text-smoke">
              Private, secure AI for small and medium businesses.
            </h2>
            <p className="font-body text-lg leading-relaxed text-smoke-dim">
              I build the site, the assistant, and the security layer a
              business can actually own. For pastors, medical billers, tax
              advisors, and firms that cannot rent client data to a public
              chatbot.
            </p>
            <div className="flex flex-col gap-3 sm:flex-row">
              <Link
                href="/start"
                className="inline-flex items-center justify-center rounded-full bg-amber! px-7 py-4 font-sans text-base font-semibold text-void transition-colors hover:bg-gold!"
              >
                Book a 20-minute call
              </Link>
              <Link
                href="#small-business"
                className="inline-flex items-center justify-center rounded-full px-7 py-4 font-sans text-base font-semibold text-smoke ring-1 ring-smoke/40 transition-colors hover:ring-amber"
              >
                I need a simple site
              </Link>
            </div>
            <p className="font-sans text-sm leading-relaxed text-smoke-dim">
              {proofRow.join(". ")}.
            </p>
            <a
              href="#small-business"
              className="group flex w-fit items-center gap-4 rounded-2xl bg-void/70 px-5 py-4 ring-1 ring-amber/40 transition-colors hover:ring-amber"
            >
              <span className="type-heading text-2xl text-amber">$500</span>
              <span className="font-sans text-base font-semibold leading-snug text-smoke">
                Small business? Websites from $500.
                <span className="block font-normal text-smoke-dim">
                  Click through 11 live demos first.
                </span>
              </span>
            </a>
          </div>
        </div>

        <div className="relative aspect-[4/3] lg:hidden">
          <Image
            src="/art/hero-key.jpg"
            alt="Engraving of two hands fitting a brass key into an open lock on a workbench, with a ledger, a padlock and a small lantern."
            fill
            sizes="100vw"
            className="object-cover object-[72%_center]"
          />
        </div>
      </section>

      {/* 2 · Small business, straight after the hero so a shop owner sees it
          first. Real screenshots of the demo builds, each a
          link into the live demo. */}
      <section id="small-business" className="scroll-mt-24 overflow-hidden rounded-[28px] bg-plum">
        <div className="px-6 py-14 sm:px-12 sm:py-20 lg:px-16 lg:py-24">
          <div className="grid gap-10 lg:grid-cols-[1.1fr_1fr] lg:items-end lg:gap-16">
            <div className="flex flex-col gap-6">
              <h2 className="type-heading text-[clamp(2.25rem,4.4vw,4rem)] text-amber">
                Small business? Start with a site that works.
              </h2>
              <p className="max-w-xl font-body text-lg leading-relaxed text-smoke-dim">
                Restaurants, shops, clinics and crews that need to be found and
                look right doing it. Every demo here is a complete build running
                on this site. Pick the one closest to your business and I adapt
                it to you.
              </p>
            </div>
            <ul className="grid gap-3 sm:grid-cols-2">
              <li className="rounded-2xl bg-void/60 p-6 ring-1 ring-border-mid">
                <p className="font-sans text-lg font-bold text-smoke">Starter</p>
                <p className="type-heading mt-1 text-4xl text-amber">$500</p>
                <p className="mt-3 font-body text-base leading-relaxed text-smoke-dim">
                  One page. Your info, your photos, mobile-ready.
                </p>
              </li>
              <li className="rounded-2xl bg-void/60 p-6 ring-1 ring-border-mid">
                <p className="font-sans text-lg font-bold text-smoke">Starter Plus</p>
                <p className="type-heading mt-1 text-4xl text-amber">$1,000</p>
                <p className="mt-3 font-body text-base leading-relaxed text-smoke-dim">
                  Up to five pages, with a menu or service list and a contact or
                  booking path.
                </p>
              </li>
            </ul>
          </div>

          <ul className="mt-12 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {smallBusinessDemos.map((demo) => (
              <li key={demo.href}>
                <Link
                  href={demo.href}
                  className="group block overflow-hidden rounded-2xl bg-void ring-1 ring-border-mid transition-shadow duration-300 hover:ring-amber/70"
                >
                  <div className="relative aspect-[16/10] overflow-hidden">
                    <Image
                      src={demo.img}
                      alt={`The first screen of the ${demo.name} demo site.`}
                      fill
                      sizes="(min-width: 1024px) 30vw, (min-width: 640px) 45vw, 100vw"
                      className="object-cover object-top transition-transform duration-500 group-hover:scale-[1.03]"
                    />
                  </div>
                  <div className="flex items-baseline justify-between gap-4 px-5 py-4">
                    <span className="font-sans text-lg font-bold text-smoke">
                      {demo.name}
                    </span>
                    <span className="shrink-0 font-sans text-sm text-smoke-dim">
                      {demo.kind}
                    </span>
                  </div>
                </Link>
              </li>
            ))}
          </ul>

          <div className="mt-10 flex flex-col gap-3 sm:flex-row">
            <Link
              href="/demos"
              className="inline-flex items-center justify-center rounded-full bg-amber! px-7 py-4 font-sans text-base font-semibold text-void transition-colors hover:bg-gold!"
            >
              See all 11 demos
            </Link>
            <Link
              href="/packages/starter-sites"
              className="inline-flex items-center justify-center rounded-full px-7 py-4 font-sans text-base font-semibold text-smoke ring-1 ring-smoke/40 transition-colors hover:ring-amber"
            >
              Starter Sites pricing
            </Link>
          </div>
        </div>
      </section>

      {/* 2 · Who this is for. White panel, the lit office window. */}
      <section className="overflow-hidden rounded-[28px] bg-paper text-void">
        <div className="grid items-center gap-10 px-6 py-14 sm:px-12 sm:py-20 lg:grid-cols-[1.05fr_1fr] lg:gap-16 lg:px-16 lg:py-24">
          <div className="flex flex-col gap-7">
            <h2 className="type-heading text-[clamp(2.25rem,4.4vw,4rem)] text-plum">
              You already have a practice. You do not have a system.
            </h2>
            <p className="max-w-xl font-body text-lg leading-relaxed text-[#3b2d4c]">
              The same five questions hit the inbox after hours. The website
              looks rented. AI tools sit scattered across personal accounts.
              Nobody has mapped what happens if that stack leaks. That is the
              job.
            </p>
            <ul className="flex flex-wrap gap-2.5">
              {audience.map((item) => (
                <li
                  key={item}
                  className="rounded-full bg-mist px-4 py-2 font-sans text-sm font-medium text-plum"
                >
                  {item}
                </li>
              ))}
            </ul>
          </div>
          <div className="relative aspect-[4/3] overflow-hidden rounded-2xl">
            <Image
              src="/art/practice.jpg"
              alt="Engraving of a small office at night, one window lit, with an appointment book, a lamp and stacked files on the desk."
              fill
              sizes="(min-width: 1024px) 45vw, 100vw"
              className="object-cover"
            />
          </div>
        </div>
      </section>

      {/* 3 · Packages. Ink ground, three illustrated cards. */}
      <section id="packages" className="scroll-mt-24 px-4 py-14 sm:px-8 sm:py-20 lg:px-12">
        <div className="mx-auto max-w-6xl">
          <div className="mb-12 flex flex-col gap-5">
            <h2 className="type-heading text-[clamp(2.25rem,4.4vw,4rem)] text-smoke">
              Three ways to start.
            </h2>
            <p className="max-w-2xl font-body text-lg text-smoke-dim">
              Most people start with a review or Meraki BIP. Custom
              work comes after we know the problem.
            </p>
          </div>

          <div className="grid gap-5 md:grid-cols-3">
            {packages.map((pkg) => (
              <PackageCard key={pkg.slug} pkg={pkg} variant="home" />
            ))}
          </div>

          <div className="mt-10 flex flex-col gap-5">
            <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              Hourly advisory is available for focused work. Retainers are for
              teams who already have a system in production. Neither is the
              starting point.
            </p>
            <Link
              href="/packages"
              className="w-fit font-sans text-base font-semibold text-smoke underline decoration-amber/60 underline-offset-4 transition-colors hover:text-amber"
            >
              Compare all packages
            </Link>
          </div>
        </div>
      </section>

      {/* 4 · Work. White panel, the shelf of finished instruments. */}
      <section className="overflow-hidden rounded-[28px] bg-paper text-void">
        <div className="grid gap-10 px-6 py-14 sm:px-12 sm:py-20 lg:grid-cols-[1fr_22rem] lg:gap-16 lg:px-16 lg:py-24">
          <div>
            <h2 className="type-heading mb-10 text-[clamp(2.25rem,4.4vw,4rem)] text-plum">
              Built. Shipped. In use.
            </h2>
            <ul className="flex flex-col">
              {work.map((product) => (
                <li
                  key={product.name}
                  className="grid gap-2 border-t border-[#e4dcec] py-6 last:border-b md:grid-cols-[14rem_1fr] md:gap-8"
                >
                  <h3 className="font-sans text-xl font-bold tracking-[-0.01em] text-plum">
                    {product.name}
                  </h3>
                  <p className="font-body text-base leading-relaxed text-[#3b2d4c]">
                    {product.detail}
                  </p>
                </li>
              ))}
            </ul>
            <Link
              href="/work"
              className="mt-8 inline-block font-sans text-base font-semibold text-plum underline decoration-plum/40 underline-offset-4 hover:decoration-plum"
            >
              See all work
            </Link>
          </div>
          <div className="relative hidden overflow-hidden rounded-2xl lg:block">
            <Image
              src="/art/work.jpg"
              alt="Engraving of a workshop shelf holding finished brass pieces: a telescope, a clock, lanterns, a strongbox and a set of scales."
              fill
              sizes="22rem"
              className="object-cover"
            />
          </div>
        </div>
      </section>

      {/* 5 · How it works. Plum panel with the workbench laid out in order.
          The steps are a sequence, so they keep their numbers. The nav's
          Process link anchors here. */}
      <section
        id="process"
        className="scroll-mt-24 overflow-hidden rounded-[28px] bg-plum"
      >
        <div className="px-6 pt-14 sm:px-12 sm:pt-20 lg:px-16 lg:pt-24">
          <h2 className="type-heading max-w-4xl text-[clamp(2.25rem,4.4vw,4rem)] text-smoke">
            You should never wonder what is happening to your project.
          </h2>
        </div>
        <div className="relative mt-10 aspect-[7/3] sm:mt-14">
          <Image
            src="/art/process.jpg"
            alt="Engraving of a workbench with tools laid out in order: a notebook and a drawing, chisels and a mallet, a box being built, and a finished box with a lock."
            fill
            sizes="100vw"
            className="object-cover"
          />
        </div>
        <ol className="grid gap-px bg-[#4a1f80] sm:grid-cols-2 lg:grid-cols-4">
          {steps.map((step, i) => (
            <li key={step.title} className="flex flex-col gap-3 bg-plum px-6 py-10 sm:px-10 lg:px-8">
              <span className="type-display text-5xl text-amber">{i + 1}</span>
              <h3 className="font-sans text-xl font-bold text-smoke">
                {step.title}
              </h3>
              <p className="font-body text-base leading-relaxed text-[#ddd0ee]">
                {step.detail}
              </p>
            </li>
          ))}
        </ol>
      </section>

      {/* 6 · Final call. Dusk panel, the open door. */}
      <section className="overflow-hidden rounded-[28px] bg-navy">
        <div className="grid items-center gap-10 lg:grid-cols-[1fr_1fr]">
          <div className="flex flex-col items-start gap-7 px-6 py-14 sm:px-12 sm:py-20 lg:py-24 lg:pl-16 lg:pr-0">
            <h2 className="type-heading text-[clamp(2.5rem,5vw,4.75rem)] text-amber">
              One conversation. No deck.
            </h2>
            <p className="max-w-xl font-body text-lg leading-relaxed text-smoke-dim">
              Tell me what you run, where it hurts, and whether you need a
              review, a system, or a full build. The worst case is a clear
              answer; the best case is the start of something you can stand
              behind.
            </p>
            <Link
              href="/start"
              className="inline-flex items-center justify-center rounded-full bg-amber! px-7 py-4 font-sans text-base font-semibold text-void transition-colors hover:bg-gold!"
            >
              Book a 20-minute call
            </Link>
            <a
              href={`mailto:${email}`}
              className="font-sans text-base text-smoke-dim underline decoration-smoke/30 underline-offset-4 transition-colors hover:text-amber"
            >
              {email}
            </a>
          </div>
          <div className="relative aspect-[3/2] lg:h-full lg:aspect-auto">
            <Image
              src="/art/door.jpg"
              alt="Engraving of a door standing open at dusk, warm light falling across the step, two chairs and a table inside."
              fill
              sizes="(min-width: 1024px) 50vw, 100vw"
              className="object-cover"
            />
          </div>
        </div>
      </section>
    </div>
  );
}
