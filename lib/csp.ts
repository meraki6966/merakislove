/**
 * The site's Content-Security-Policy, in one place.
 *
 * Pages rendered by Next.js get a strict script policy: a fresh nonce for every
 * request (made in proxy.ts) and 'strict-dynamic', with no 'unsafe-inline'. A
 * script runs only if it carries this request's nonce or was loaded by one that
 * does. Next.js adds the nonce to its own scripts; app/layout.tsx adds it to the
 * two the site writes itself. This closes finding 8 of the 16 October review.
 *
 * The static demo pages under /public are plain files a nonce can't reach, so
 * they keep the older policy, which allows their own inline scripts. Their
 * chats insert replies as text, never as HTML.
 *
 * Styles keep 'unsafe-inline': animation libraries set inline styles, and the
 * finding was about scripts.
 *
 * scripts/tests/csp.test.mjs holds all of this in place.
 */

/** Everything both policies share, after script-src. */
const SHARED = [
  "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
  "font-src 'self' https://fonts.gstatic.com data:",
  "img-src 'self' data: https:",
  "connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com",
  "object-src 'none'",
  "frame-ancestors 'none'",
  "base-uri 'self'",
  "form-action 'self'",
];

/**
 * The policy for one page request. 'strict-dynamic' lets the analytics loader
 * (nonced) add gtag.js; the gtag host stays listed for browsers that predate
 * 'strict-dynamic' and ignore it otherwise.
 */
export function pagePolicy(nonce: string, dev = false): string {
  const script = `script-src 'self' 'nonce-${nonce}' 'strict-dynamic' https://www.googletagmanager.com${dev ? " 'unsafe-eval'" : ""}`;
  return ["default-src 'self'", script, ...SHARED].join("; ");
}

/** The policy for the static demo pages under /public/demos. */
export const STATIC_POLICY = [
  "default-src 'self'",
  "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com",
  ...SHARED,
].join("; ");

/** The API routes return JSON and never need to run or load anything. */
export const API_POLICY = "default-src 'none'; frame-ancestors 'none'";

/** A fresh, unguessable nonce: 16 random bytes, base64. */
export function makeNonce(): string {
  const bytes = new Uint8Array(16);
  crypto.getRandomValues(bytes);
  return btoa(String.fromCharCode(...bytes));
}
