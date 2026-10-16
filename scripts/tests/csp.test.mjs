// Tests for the site's Content-Security-Policy (finding 8 of the 16 October review).
// Run from the repo root:  npm run test:csp
// Against a running copy:  BASE_URL=http://localhost:3100 npm run test:csp
//
// What they hold the site to:
//   1. Pages Next.js renders run only scripts that carry a fresh per-request
//      nonce. No 'unsafe-inline' and no 'unsafe-eval' for scripts.
//   2. The proxy makes the nonce, sets the policy on the request (so Next.js
//      can read it while rendering) and on the response, and covers every page
//      while leaving the API, Next's own files and the static demos alone.
//   3. The root layout puts the nonce on the two scripts the site writes itself.
//   4. The static demos keep their policy; the API routes get one that allows nothing.
// Each rule was broken on purpose once and seen to fail before it was trusted.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

import { API_POLICY, STATIC_POLICY, makeNonce, pagePolicy } from "../../lib/csp.ts";
import nextConfig from "../../next.config.ts";

const root = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, root), "utf8");
const BASE_URL = process.env.BASE_URL?.replace(/\/$/, "");

function directives(csp) {
  return Object.fromEntries(
    csp.split(";").map((d) => d.trim().split(/\s+/)).filter((p) => p[0]).map(([k, ...v]) => [k, v]),
  );
}

// ------------------------------------------------------------------ the policies

test("a page's script policy is a nonce and strict-dynamic, with no inline or eval allowance", () => {
  const d = directives(pagePolicy("abc123"));
  const s = d["script-src"];
  assert.ok(s.includes("'nonce-abc123'"), "the nonce must be in script-src");
  assert.ok(s.includes("'strict-dynamic'"), "scripts a nonced script loads (gtag.js) must be allowed");
  assert.ok(!s.includes("'unsafe-inline'"), "no inline scripts without the nonce");
  assert.ok(!s.includes("'unsafe-eval'"), "no eval in production");
  assert.ok(s.includes("https://www.googletagmanager.com"), "kept for browsers without strict-dynamic");
  assert.deepEqual(d["object-src"], ["'none'"]);
  assert.deepEqual(d["frame-ancestors"], ["'none'"]);
  assert.deepEqual(d["base-uri"], ["'self'"]);
  assert.ok(directives(pagePolicy("x", true))["script-src"].includes("'unsafe-eval'"), "dev mode only");
});

test("pages and static demos differ only in script-src", () => {
  const page = directives(pagePolicy("n"));
  const stat = directives(STATIC_POLICY);
  assert.deepEqual(Object.keys(page), Object.keys(stat));
  for (const k of Object.keys(page)) if (k !== "script-src") assert.deepEqual(page[k], stat[k], k);
  assert.ok(stat["script-src"].includes("'unsafe-inline'"), "the static demos keep their inline scripts");
});

test("every nonce is new and unguessable", () => {
  const seen = new Set(Array.from({ length: 200 }, makeNonce));
  assert.equal(seen.size, 200, "no nonce may repeat");
  for (const n of seen) assert.match(n, /^[A-Za-z0-9+/]{22}==$/, "16 random bytes, base64");
});

test("the API routes get a policy that allows nothing", () => {
  assert.equal(API_POLICY, "default-src 'none'; frame-ancestors 'none'");
});

// ------------------------------------------------------------------ the wiring

test("the proxy sets a fresh nonce on the request and the policy on both sides", () => {
  const code = read("proxy.ts");
  assert.match(code, /const nonce = makeNonce\(\);/);
  assert.match(code, /requestHeaders\.set\("x-nonce", nonce\)/);
  assert.match(code, /requestHeaders\.set\("Content-Security-Policy", policy\)/);
  assert.match(code, /response\.headers\.set\("Content-Security-Policy", policy\)/);
  assert.match(code, /pagePolicy\(nonce, process\.env\.NODE_ENV === "development"\)/);
});

test("the proxy covers every page and skips the API, Next's files and the static demos", () => {
  const code = read("proxy.ts");
  const src = code.match(/source: "([^"]+)"/)?.[1].replace(/\\\\/g, "\\");
  assert.ok(src, "a matcher source is required");
  const re = new RegExp("^" + src + "$");
  for (const path of ["/", "/work", "/packages/review", "/shadow-ai", "/demos", "/privacy", "/no-such-page"]) {
    assert.ok(re.test(path), `${path} must get a nonce`);
  }
  for (const path of ["/api/meraki-inn-chat", "/_next/static/chunks/a.js", "/_next/image", "/demos/keelhouse", "/demos/presence-first-example.html", "/analytics.js", "/sitemap.xml", "/og/home.png"]) {
    assert.ok(!re.test(path), `${path} must be left to next.config.ts`);
  }
});

test("the root layout gives the nonce to both of the site's own scripts", () => {
  const code = read("app/layout.tsx");
  assert.match(code, /const nonce = \(await headers\(\)\)\.get\("x-nonce"\) \?\? undefined;/);
  assert.match(code, /<script src="\/analytics\.js" async nonce=\{nonce\} \/>/);
  assert.match(code, /<script nonce=\{nonce\} dangerouslySetInnerHTML=\{\{ __html: REVEAL_FALLBACK_SCRIPT \}\} \/>/);
  assert.equal((code.match(/<script\b/g) || []).length, 2, "a new script in the layout needs the nonce too");
});

test("next.config.ts gives static files the static policy and the API its own, later in the list", async () => {
  const rules = await nextConfig.headers();
  const at = (source) => rules.findIndex((r) => r.source === source);
  const csp = (source) => rules[at(source)].headers.find((h) => h.key === "Content-Security-Policy").value;
  assert.equal(csp("/:path*"), STATIC_POLICY);
  assert.equal(csp("/api/:path*"), API_POLICY);
  assert.ok(at("/api/:path*") > at("/:path*"), "the later rule wins for the same header");
});

// ------------------------------------------------------------------ a running copy

async function get(path) {
  const res = await fetch(BASE_URL + path, { redirect: "manual" });
  return { status: res.status, csp: res.headers.get("content-security-policy") || "", html: await res.text() };
}

test("a running copy serves each page with its own nonce, on every script it runs", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  const seen = new Set();
  for (const path of ["/", "/shadow-ai", "/packages/review", "/demos", "/"]) {
    const { status, csp, html } = await get(path);
    assert.equal(status, 200, path);
    const nonce = csp.match(/'nonce-([^']+)'/)?.[1];
    assert.ok(nonce, `${path} must carry a nonce`);
    assert.ok(!seen.has(nonce), "a nonce must never repeat");
    seen.add(nonce);
    const scripts = [...html.matchAll(/<script\b([^>]*)>/g)].map((m) => m[1]).filter((a) => !/type="application\/(ld\+)?json"/.test(a));
    assert.ok(scripts.length > 0);
    for (const attrs of scripts) assert.ok(attrs.includes(`nonce="${nonce}"`), `${path}: a script without the nonce: <script${attrs}>`);
  }
});

test("a running copy keeps the static policy on demos and the empty one on the API", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  assert.equal((await get("/demos/keelhouse")).csp, STATIC_POLICY);
  assert.equal((await get("/demos/presence-first-example.html")).csp, STATIC_POLICY);
  const res = await fetch(BASE_URL + "/api/meraki-inn-chat", { method: "POST", headers: { "content-type": "text/plain" }, body: "x" });
  assert.equal(res.headers.get("content-security-policy"), API_POLICY);
});
