import type { NextConfig } from "next";

// Security headers applied to every route. Tuned to pass the Canopy Guard
// security audit while remaining compatible with Next.js inline styles/scripts
// and Google Fonts. CSP allows 'unsafe-inline' for styles (Tailwind/inline) and
// the JSON-LD <script> tags; tighten with nonces later if desired.
const ContentSecurityPolicy = [
  "default-src 'self'",
  "script-src 'self' 'unsafe-inline'",
  "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
  "font-src 'self' https://fonts.gstatic.com data:",
  "img-src 'self' data: https:",
  "connect-src 'self'",
  "frame-ancestors 'none'",
  "base-uri 'self'",
  "form-action 'self'",
].join("; ");

const securityHeaders = [
  { key: "X-Frame-Options", value: "DENY" },
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  { key: "Permissions-Policy", value: "camera=(), microphone=(), geolocation=()" },
  { key: "Content-Security-Policy", value: ContentSecurityPolicy },
  { key: "Strict-Transport-Security", value: "max-age=31536000; includeSubDomains" },
];

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
    ];
  },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: securityHeaders,
      },
    ];
  },
};

export default nextConfig;
