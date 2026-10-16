import type { NextConfig } from "next";

import { API_POLICY, STATIC_POLICY } from "./lib/csp.ts";

// Security headers applied to every route. The Content-Security-Policy set here
// is the one for the static files under /public, the demos above all; every
// page Next.js renders gets a stricter one with a per-request nonce from
// proxy.ts, which replaces this header on those responses. Both policies live
// in lib/csp.ts, and scripts/tests/csp.test.mjs pins them.
//
// Google Analytics 4 (public/analytics.js) needs exactly two additions:
// gtag.js from www.googletagmanager.com in script-src, and the collection
// endpoints in connect-src. Nothing else was widened for it.
const ContentSecurityPolicy = STATIC_POLICY;

const securityHeaders = [
  // Vercel's CDN adds `Access-Control-Allow-Origin: *` to every static and
  // prerendered response on its own; nothing in this project sets it. Config
  // cannot delete a header, only replace it, so pin it to this site's own
  // origin. Browsers ignore the header on same-origin requests, so this grants
  // no cross-origin read access to anyone. Nothing on the site or on any other
  // Meraki property reads this domain cross-origin (checked 2026-09-14). If a
  // public endpoint ever needs CORS, scope a wildcard to that route alone.
  { key: "Access-Control-Allow-Origin", value: "https://merakislove.com" },
  { key: "X-Frame-Options", value: "DENY" },
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
  { key: "Content-Security-Policy", value: ContentSecurityPolicy },
  { key: "Strict-Transport-Security", value: "max-age=31536000; includeSubDomains" },
  // Keep this site's windows in their own browsing context group, so a page
  // opened from another site can't hold a reference to ours (and the reverse).
  // Every outbound link already uses rel="noopener", and nothing here relies
  // on window.opener, so this changes no behavior.
  { key: "Cross-Origin-Opener-Policy", value: "same-origin" },
  // Only pages on merakislove.com (and its subdomains) may embed this site's
  // files. The share and cover images below are the exception.
  { key: "Cross-Origin-Resource-Policy", value: "same-site" },
];

// Share and cover images are meant to be shown elsewhere (link previews,
// other Meraki properties), so they stay embeddable from any site. This entry
// comes after the global one, and for the same header key the later match wins.
const embeddableImageHeaders = [{ key: "Cross-Origin-Resource-Policy", value: "cross-origin" }];

const nextConfig: NextConfig = {
  // Pin the workspace root to this project. A stray package-lock.json in the
  // user's home directory was otherwise being inferred as the root.
  turbopack: {
    root: import.meta.dirname,
  },
  // Static demos are plain HTML files under /public. Next.js does not do
  // directory-index resolution there, so `/demos/restaurant` would 404 and
  // `/demos/restaurant/` would 308 straight into that 404. Map each clean
  // demo URL onto its actual file. Deliberately one entry per demo: a
  // wildcard like `/demos/:slug` would also swallow the existing
  // `/demos/presence-first-example.html` and rewrite it into a 404.
  async rewrites() {
    return [
      {
        source: "/demos/restaurant",
        destination: "/demos/restaurant/index.html",
      },
      {
        source: "/demos/iron-prism",
        destination: "/demos/iron-prism/index.html",
      },
      {
        source: "/demos/keelhouse",
        destination: "/demos/keelhouse/index.html",
      },
      {
        source: "/demos/hazel-and-row",
        destination: "/demos/hazel-and-row/index.html",
      },
      {
        source: "/demos/tessel",
        destination: "/demos/tessel/index.html",
      },
      {
        source: "/demos/pikewell",
        destination: "/demos/pikewell/index.html",
      },
      {
        source: "/demos/tallybrook",
        destination: "/demos/tallybrook/index.html",
      },
      {
        source: "/demos/saltbrush",
        destination: "/demos/saltbrush/index.html",
      },
      {
        source: "/demos/fernhollow",
        destination: "/demos/fernhollow/index.html",
      },
      {
        source: "/demos/sideoats",
        destination: "/demos/sideoats/index.html",
      },
      {
        source: "/demos/meraki-inn",
        destination: "/demos/meraki-inn/index.html",
      },
    ];
  },
  // /services was renamed to /packages. Old backlinks and the footers of the
  // three published demo pages still point at the old URLs, so both the hub
  // and its one child route redirect permanently rather than 404.
  //
  // Note: Next emits 308 for `permanent: true`, not 301. It is the
  // method-preserving equivalent and search engines consolidate it the same
  // way. Only these two exact paths redirect; a wildcard would swallow the
  // /packages/[slug] routes that ship in phase 2.
  async redirects() {
    return [
      {
        source: "/services",
        destination: "/packages",
        permanent: true,
      },
      {
        source: "/services/presence-first-web-design",
        destination: "/packages/presence-first-web-design",
        permanent: true,
      },
      // The home services demo was renamed from Anchor to Keelhouse on
      // 2026-10-01 after finding real businesses already using the Anchor
      // name for the same trades (Orlando, FL and Rittman, OH). Old links,
      // including any shared on social or in outreach, land on the new demo.
      {
        source: "/demos/anchor",
        destination: "/demos/keelhouse",
        permanent: true,
      },
      {
        source: "/demos/anchor/:path*",
        destination: "/demos/keelhouse",
        permanent: true,
      },
    ];
  },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: securityHeaders,
      },
      // JSON only: nothing to run, load or frame.
      { source: "/api/:path*", headers: [{ key: "Content-Security-Policy", value: API_POLICY }] },
      { source: "/og/:path*", headers: embeddableImageHeaders },
      { source: "/covers/:path*", headers: embeddableImageHeaders },
    ];
  },
};

export default nextConfig;
