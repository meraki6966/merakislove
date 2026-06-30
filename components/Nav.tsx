"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { navLinks, calendly } from "@/lib/site";

/**
 * Fixed navigation. Transparent over the hero, then fades in a blurred
 * navy background once the page scrolls. Collapses to a hamburger sheet
 * on small screens. Includes the persistent "Book a Call" CTA.
 */
export default function Nav() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header
      className={`fixed inset-x-0 top-0 z-50 transition-colors duration-500 ${
        scrolled || open
          ? "border-b border-border bg-void/80 backdrop-blur-md"
          : "border-b border-transparent bg-transparent"
      }`}
    >
      <nav className="mx-auto flex h-16 max-w-6xl items-center justify-between px-6 sm:h-20 sm:px-8">
        {/* Wordmark */}
        <Link
          href="/"
          className="group flex items-center gap-2 font-display text-lg tracking-tight text-smoke"
        >
          <span className="h-1.5 w-1.5 rounded-full bg-amber transition-transform duration-300 group-hover:scale-125" />
          <span className="font-light">
            Meraki <span className="text-amber">is Love</span>
          </span>
        </Link>

        {/* Desktop links */}
        <div className="hidden items-center gap-8 md:flex">
          {navLinks.map((link) => {
            const active = pathname === link.href;
            return (
              <Link
                key={link.href}
                href={link.href}
                className={`font-mono text-xs uppercase tracking-[0.18em] transition-colors duration-300 ${
                  active ? "text-amber" : "text-smoke-dim hover:text-smoke"
                }`}
              >
                {link.label}
              </Link>
            );
          })}
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-full border border-amber px-5 py-2 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void"
          >
            Book a Call
          </a>
        </div>

        {/* Mobile toggle */}
        <button
          type="button"
          onClick={() => setOpen((v) => !v)}
          aria-label={open ? "Close menu" : "Open menu"}
          aria-expanded={open}
          className="relative z-50 flex h-10 w-10 flex-col items-center justify-center gap-1.5 md:hidden"
        >
          <span
            className={`h-px w-6 bg-smoke transition-all duration-300 ${
              open ? "translate-y-[3.5px] rotate-45" : ""
            }`}
          />
          <span
            className={`h-px w-6 bg-smoke transition-all duration-300 ${
              open ? "-translate-y-[3.5px] -rotate-45" : ""
            }`}
          />
        </button>
      </nav>

      {/* Mobile sheet */}
      <div
        className={`overflow-hidden border-border bg-void/95 backdrop-blur-md transition-[max-height] duration-500 md:hidden ${
          open ? "max-h-96 border-b" : "max-h-0"
        }`}
      >
        <div className="flex flex-col gap-1 px-6 py-6">
          {navLinks.map((link) => {
            const active = pathname === link.href;
            return (
              <Link
                key={link.href}
                href={link.href}
                onClick={() => setOpen(false)}
                className={`border-b border-border py-4 font-mono text-sm uppercase tracking-[0.18em] transition-colors ${
                  active ? "text-amber" : "text-smoke-dim hover:text-smoke"
                }`}
              >
                {link.label}
              </Link>
            );
          })}
          <a
            href={calendly.newProject}
            target="_blank"
            rel="noopener noreferrer"
            onClick={() => setOpen(false)}
            className="mt-5 rounded-full border border-amber px-5 py-3 text-center font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors hover:bg-amber! hover:text-void"
          >
            Book a Call
          </a>
        </div>
      </div>
    </header>
  );
}
