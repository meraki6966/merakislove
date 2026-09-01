import Link from "next/link";
import type { ReactNode } from "react";
import { navLinks, socials, calendly, email, studio } from "@/lib/site";

/**
 * Brand glyphs for the footer social row, keyed by the social's label.
 * Each path uses currentColor so it inherits the link's text/hover color
 * and the shared 24x24 viewBox keeps every icon visually aligned.
 */
const socialIcons: Record<string, ReactNode> = {
  LinkedIn: (
    <path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.22.79 24 1.77 24h20.45c.98 0 1.78-.78 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z" />
  ),
  GitHub: (
    <path d="M12 .3a12 12 0 0 0-3.79 23.4c.6.11.82-.26.82-.58l-.01-2.04c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.34-1.76-1.34-1.76-1.08-.75.08-.73.08-.73 1.2.08 1.84 1.24 1.84 1.24 1.07 1.83 2.8 1.3 3.49.99.1-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93 0-1.31.47-2.38 1.24-3.22-.13-.3-.54-1.52.11-3.18 0 0 1.01-.32 3.3 1.23a11.5 11.5 0 0 1 6 0c2.29-1.55 3.3-1.23 3.3-1.23.65 1.66.24 2.88.12 3.18.77.84 1.23 1.91 1.23 3.22 0 4.61-2.8 5.63-5.48 5.92.43.37.81 1.1.81 2.22l-.01 3.29c0 .32.22.7.83.58A12 12 0 0 0 12 .3z" />
  ),
  Substack: (
    <path d="M22.54 8.21H1.46V5.46h21.08v2.75zM1.46 10.81H22.54V24l-10.54-5.93L1.46 24V10.81zM22.54 2.85H1.46V.1H22.54v2.75z" />
  ),
  Facebook: (
    <path d="M24 12.07C24 5.4 18.63 0 12 0S0 5.4 0 12.07c0 6.02 4.39 11.01 10.13 11.93v-8.44H7.08v-3.49h3.05V9.41c0-3.02 1.79-4.69 4.53-4.69 1.31 0 2.69.24 2.69.24v2.97h-1.52c-1.49 0-1.96.93-1.96 1.89v2.25h3.33l-.53 3.49h-2.8V24C19.61 23.08 24 18.09 24 12.07z" />
  ),
  Instagram: (
    <path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41 1.27-.06 1.65-.07 4.85-.07zM12 0C8.74 0 8.33.01 7.05.07c-1.28.06-2.15.26-2.91.56-.79.31-1.46.72-2.12 1.38A5.86 5.86 0 0 0 .63 4.13c-.3.76-.5 1.63-.56 2.91C.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.28.26 2.15.56 2.91.31.79.72 1.46 1.38 2.12.66.66 1.33 1.07 2.12 1.38.76.3 1.63.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.28-.06 2.15-.26 2.91-.56a5.86 5.86 0 0 0 2.12-1.38 5.86 5.86 0 0 0 1.38-2.12c.3-.76.5-1.63.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.28-.26-2.15-.56-2.91a5.86 5.86 0 0 0-1.38-2.12A5.86 5.86 0 0 0 19.86.63c-.76-.3-1.63-.5-2.91-.56C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.41-10.85a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88z" />
  ),
  Website: (
    <path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm7.93 7.2h-3.4a15.6 15.6 0 0 0-1.36-3.52A9.83 9.83 0 0 1 19.93 7.2zM12 2.04c.84 1.22 1.5 2.58 1.94 4.04H10.06A12.7 12.7 0 0 1 12 2.04zM2.26 14.4a9.8 9.8 0 0 1 0-4.8h3.9a16.6 16.6 0 0 0-.16 2.4c0 .82.06 1.62.16 2.4h-3.9zm.81 2.4h3.4c.34 1.27.8 2.46 1.36 3.52A9.83 9.83 0 0 1 3.07 16.8zm3.4-9.6h-3.4a9.83 9.83 0 0 1 4.76-3.52A15.6 15.6 0 0 0 6.47 7.2zM12 21.96a12.7 12.7 0 0 1-1.94-4.04h3.88A12.7 12.7 0 0 1 12 21.96zm2.37-6.04H9.63a14.5 14.5 0 0 1-.18-2.4c0-.83.07-1.63.18-2.4h4.74c.11.77.18 1.57.18 2.4 0 .82-.07 1.62-.18 2.4zm.2 4.6c.56-1.06 1.02-2.25 1.36-3.52h3.4a9.83 9.83 0 0 1-4.76 3.52zm2.1-5.92c.1-.78.16-1.58.16-2.4 0-.82-.06-1.62-.16-2.4h3.9a9.8 9.8 0 0 1 0 4.8h-3.9z" />
  ),
};

/**
 * Site footer: identity, navigation, and the two direct ways to reach the
 * studio.
 *
 * There is deliberately no call to action here any more. The homepage,
 * /packages and /start each close with their own, and a second one stacked
 * underneath read as the site asking twice.
 */
export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="relative border-t border-border bg-void">
      {/* Meta row */}
      <div className="mx-auto flex max-w-6xl flex-col gap-8 px-6 py-14 sm:px-8 md:flex-row md:items-start md:justify-between">
        <div className="flex max-w-sm flex-col gap-3">
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
          <p className="font-body text-sm leading-relaxed text-smoke-dim">
            {studio.descriptor}
          </p>
        </div>

        <div className="flex flex-col gap-5">
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

          <div className="flex flex-wrap items-center gap-x-4 gap-y-2 font-mono text-xs tracking-[0.14em] text-smoke-dim">
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="uppercase tracking-[0.18em] transition-colors hover:text-amber"
            >
              Calendly
            </a>
            <span aria-hidden className="text-amber">
              ·
            </span>
            <a
              href={`mailto:${email}`}
              className="transition-colors hover:text-amber"
            >
              {email}
            </a>
          </div>

          <div className="flex items-center gap-x-6">
            {socials.map((social) => (
              <a
                key={social.label}
                href={social.href}
                target="_blank"
                rel="noopener noreferrer"
                aria-label={social.label}
                title={social.label}
                className="text-smoke-dim transition-colors hover:text-amber"
              >
                <svg
                  viewBox="0 0 24 24"
                  aria-hidden
                  fill="currentColor"
                  className="h-5 w-5"
                >
                  {socialIcons[social.label]}
                </svg>
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
