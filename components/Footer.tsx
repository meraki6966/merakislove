import Link from "next/link";
import ScrollReveal from "@/components/ScrollReveal";
import { navLinks, socials, calendly, studio } from "@/lib/site";

/**
 * Footer CTA + copyright. The closing invitation of every page:
 * a single Calendly action, navigation, social links, and studio info.
 */
export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="relative border-t border-border bg-void">
      {/* CTA */}
      <div className="mx-auto max-w-6xl px-6 py-24 sm:px-8 sm:py-32">
        <ScrollReveal className="flex flex-col items-start gap-8">
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Let&apos;s build
          </p>
          <h2 className="max-w-2xl font-display text-4xl font-light leading-[1.05] text-smoke sm:text-6xl">
            Have a project in mind?
          </h2>
          <p className="max-w-xl font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            Start with a conversation. No decks, no pressure. Just a clear-eyed
            look at what you&apos;re building and whether it&apos;s a fit.
          </p>
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
          >
            Book a Call
            <span className="transition-transform duration-300 group-hover:translate-x-1">
              →
            </span>
          </a>
        </ScrollReveal>
      </div>

      {/* Meta row */}
      <div className="border-t border-border">
        <div className="mx-auto flex max-w-6xl flex-col gap-8 px-6 py-10 sm:px-8 md:flex-row md:items-center md:justify-between">
          <div className="flex flex-col gap-2">
            <Link
              href="/"
              className="flex items-center gap-2 font-display text-base text-smoke"
            >
              <span className="h-1.5 w-1.5 rounded-full bg-amber" />
              <span className="font-light">
                Meraki <span className="text-amber">is Love</span>
              </span>
            </Link>
            <p className="font-mono text-[0.7rem] uppercase tracking-wider text-muted">
              {studio.brand} ·{" "}
              <a
                href={studio.site}
                target="_blank"
                rel="noopener noreferrer"
                className="transition-colors hover:text-amber"
              >
                {studio.siteLabel}
              </a>
            </p>
          </div>

          <nav className="flex flex-wrap gap-x-6 gap-y-3">
            {navLinks.map((link) => (
              <Link
                key={link.href}
                href={link.href}
                className="font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
              >
                {link.label}
              </Link>
            ))}
          </nav>

          <div className="flex gap-x-6">
            {socials.map((social) => (
              <a
                key={social.label}
                href={social.href}
                target="_blank"
                rel="noopener noreferrer"
                className="font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim transition-colors hover:text-amber"
              >
                {social.label}
              </a>
            ))}
          </div>
        </div>
      </div>

      {/* Copyright */}
      <div className="border-t border-border">
        <div className="mx-auto max-w-6xl px-6 py-6 sm:px-8">
          <p className="font-mono text-[0.7rem] uppercase tracking-wider text-muted">
            © {year} {studio.name}. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
