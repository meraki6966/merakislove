// Tests for the Google Analytics 4 setup on merakislove.com.
// Run from the repo root:  npm run test:analytics
// Against a running copy:  BASE_URL=https://<host> npm run test:analytics
//
// What they hold the site to:
//   1. Every public page loads the self-hosted loader, exactly once.
//   2. No demo page under /demos loads it, except the Presence-First example,
//      and every noindex page makes the loader stand down.
//   3. The security policy lets gtag.js load and send, and nothing else was
//      widened for it.
//   4. The loader only runs on merakislove.com and www.merakislove.com, never
//      with Global Privacy Control on, and always with Google signals and ad
//      personalization off.
// Each was broken on purpose once and seen to fail before it was trusted.
import assert from "node:assert/strict";
import { readFileSync, readdirSync, statSync } from "node:fs";
import { test } from "node:test";
import vm from "node:vm";

import nextConfig from "../../next.config.ts";
import sitemap from "../../app/sitemap.ts";

const root = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, root), "utf8");
const MEASUREMENT_ID = "G-CD61SSYP84";
const LOADER_TAG = /<script\b[^>]*\bsrc="\/analytics\.js"[^>]*>/g;
const BASE_URL = process.env.BASE_URL?.replace(/\/$/, "");

// ---------------------------------------------------------------- loader

function runLoader({ hostname, gpc = false, robots = null, readyState = "complete" }) {
  const appended = [];
  const listeners = {};
  const doc = {
    readyState,
    head: { appendChild: (el) => appended.push(el) },
    createElement: (tag) => ({ tagName: tag.toUpperCase() }),
    querySelector: (sel) =>
      sel === 'meta[name="robots"]' && robots !== null ? { getAttribute: () => robots } : null,
    addEventListener: (type, fn) => {
      listeners[type] = fn;
    },
  };
  const win = { location: { hostname }, navigator: gpc ? { globalPrivacyControl: true } : {} };
  win.window = win;
  win.document = doc;
  vm.createContext(win);
  vm.runInContext(read("public/analytics.js"), win);
  return { win, appended, listeners };
}
const gtagSrc = `https://www.googletagmanager.com/gtag/js?id=${MEASUREMENT_ID}`;
const commands = (win) => (win.dataLayer || []).map((args) => Array.from(args));

test("the loader runs on merakislove.com and www.merakislove.com", () => {
  for (const hostname of ["merakislove.com", "www.merakislove.com"]) {
    const { win, appended } = runLoader({ hostname });
    assert.equal(appended.length, 1, `${hostname} should add one gtag.js tag`);
    assert.equal(appended[0].src, gtagSrc);
    assert.equal(appended[0].async, true);
    const config = commands(win).find((c) => c[0] === "config");
    assert.equal(config[1], MEASUREMENT_ID);
  }
});

test("the loader stays silent on preview deploys, localhost and look-alike hosts", () => {
  for (const hostname of [
    "merakislove-git-analytics-ga4-adam.vercel.app",
    "merakislove.vercel.app",
    "localhost",
    "127.0.0.1",
    "meraki-1k4.pages.dev",
    "merakislove.com.example.org",
    "staging.merakislove.com",
  ]) {
    const { win, appended } = runLoader({ hostname });
    assert.equal(appended.length, 0, `${hostname} must not load gtag.js`);
    assert.equal(win.dataLayer, undefined, `${hostname} must not create a dataLayer`);
  }
});

test("Global Privacy Control turns the loader off completely", () => {
  const { win, appended } = runLoader({ hostname: "merakislove.com", gpc: true });
  assert.equal(appended.length, 0);
  assert.equal(win.dataLayer, undefined);
});

test("a noindex page turns the loader off, an indexable one does not", () => {
  for (const robots of ["noindex", "noindex, follow", "NOINDEX"]) {
    const { appended } = runLoader({ hostname: "merakislove.com", robots });
    assert.equal(appended.length, 0, `robots "${robots}" must stop the loader`);
  }
  const { appended } = runLoader({ hostname: "merakislove.com", robots: "index, follow" });
  assert.equal(appended.length, 1);
});

test("Google signals and ad personalization are off in both the set and config calls", () => {
  const { win } = runLoader({ hostname: "merakislove.com" });
  const cmds = commands(win);
  const set = cmds.find((c) => c[0] === "set");
  const config = cmds.find((c) => c[0] === "config");
  for (const opts of [set[1], config[2]]) {
    assert.equal(opts.allow_google_signals, false);
    assert.equal(opts.allow_ad_personalization_signals, false);
  }
});

test("while the page is still parsing, the loader waits before reading the robots tag", () => {
  const { appended, listeners } = runLoader({ hostname: "merakislove.com", readyState: "loading" });
  assert.equal(appended.length, 0, "nothing loads before DOMContentLoaded");
  assert.equal(typeof listeners.DOMContentLoaded, "function");
  listeners.DOMContentLoaded();
  assert.equal(appended.length, 1);
});

// ---------------------------------------------------------- which pages

function walk(dirUrl) {
  const out = [];
  for (const name of readdirSync(dirUrl)) {
    const child = new URL(name, dirUrl);
    if (statSync(child).isDirectory()) out.push(...walk(new URL(`${name}/`, dirUrl)));
    else out.push(child);
  }
  return out;
}
const demoFiles = walk(new URL("public/demos/", root)).filter((u) => u.pathname.endsWith(".html"));
const EXAMPLE = "/demos/presence-first-example.html";

test("the root layout carries the loader once, and no other layout replaces it", () => {
  const layout = read("app/layout.tsx");
  assert.equal((layout.match(LOADER_TAG) || []).length, 1, "app/layout.tsx must include /analytics.js once");
  const layouts = walk(new URL("app/", root)).filter((u) => u.pathname.endsWith("/layout.tsx"));
  for (const u of layouts) {
    if (u.pathname.endsWith("/app/layout.tsx")) continue;
    assert.ok(!/<html\b/.test(readFileSync(u, "utf8")), `${u.pathname} is a second root layout`);
  }
});

test("no demo page loads analytics, except the Presence-First example, which loads it once", () => {
  assert.ok(demoFiles.length > 100, "expected the full demo set");
  for (const u of demoFiles) {
    const html = readFileSync(u, "utf8");
    const path = u.pathname.slice(u.pathname.indexOf("/demos/"));
    const loads = (html.match(LOADER_TAG) || []).length;
    if (path === EXAMPLE) {
      assert.equal(loads, 1, `${path} must load /analytics.js once`);
    } else {
      assert.equal(loads, 0, `${path} is a demo and must not load /analytics.js`);
      assert.ok(!/googletagmanager|google-analytics|gtag\(/.test(html), `${path} must not carry a Google tag`);
    }
  }
});

test("the sitemap lists the 16 tagged pages, the Presence-First example among them", () => {
  const urls = sitemap().map((e) => e.url);
  assert.equal(urls.length, 16);
  assert.ok(urls.includes(`https://merakislove.com${EXAMPLE}`));
  assert.ok(!urls.some((u) => u.includes("/demos/") && !u.endsWith(EXAMPLE)), "no other demo is listed");
});

// ------------------------------------------------------- security policy

const EXPECTED_CSP = [
  "default-src 'self'",
  "script-src 'self' 'unsafe-inline' https://www.googletagmanager.com",
  "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
  "font-src 'self' https://fonts.gstatic.com data:",
  "img-src 'self' data: https:",
  "connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com",
  "frame-ancestors 'none'",
  "base-uri 'self'",
  "form-action 'self'",
].join("; ");

function directives(csp) {
  return Object.fromEntries(
    csp.split(";").map((d) => d.trim().split(/\s+/)).filter((p) => p[0]).map(([k, ...v]) => [k, v]),
  );
}
function assertPolicyAllowsAnalytics(csp) {
  const d = directives(csp);
  assert.ok(d["script-src"].includes("https://www.googletagmanager.com"), "script-src must allow gtag.js");
  for (const src of ["https://*.google-analytics.com", "https://*.analytics.google.com", "https://www.googletagmanager.com"]) {
    assert.ok(d["connect-src"].includes(src), `connect-src must allow ${src}`);
  }
}

test("the policy allows gtag.js to load and send, and is otherwise unchanged", async () => {
  const rules = await nextConfig.headers();
  const all = rules.find((r) => r.source === "/:path*");
  const csp = all.headers.find((h) => h.key === "Content-Security-Policy").value;
  assertPolicyAllowsAnalytics(csp);
  assert.equal(csp, EXPECTED_CSP, "the policy changed beyond the Google addresses");
});

// --------------------------------------------- against a running copy

test("a running copy serves the loader on every public page and the policy that allows it", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  const paths = sitemap().map((e) => new URL(e.url).pathname || "/");
  for (const path of paths) {
    const res = await fetch(BASE_URL + path, { redirect: "manual" });
    assert.equal(res.status, 200, `${path} answered ${res.status}`);
    const html = await res.text();
    assert.equal((html.match(LOADER_TAG) || []).length, 1, `${path} must load /analytics.js exactly once`);
    assert.ok(!/<meta name="robots" content="[^"]*noindex/i.test(html), `${path} is public and must not be noindex`);
    assertPolicyAllowsAnalytics(res.headers.get("content-security-policy") || "");
  }
  const loader = await fetch(`${BASE_URL}/analytics.js`);
  assert.equal(loader.status, 200);
  assert.equal(await loader.text(), read("public/analytics.js"), "the served loader must match the repo");
});

test("a running copy keeps the loader off demo pages and stands it down on the 404 page", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  for (const path of ["/demos/keelhouse", "/demos/fernhollow/pricing.html", "/demos/tallybrook", "/demos/restaurant"]) {
    const html = await (await fetch(BASE_URL + path)).text();
    assert.equal((html.match(LOADER_TAG) || []).length, 0, `${path} must not load /analytics.js`);
  }
  const res = await fetch(`${BASE_URL}/this-page-does-not-exist`);
  assert.equal(res.status, 404);
  assert.match(await res.text(), /<meta name="robots" content="noindex/, "the 404 page must be noindex so the loader stands down");
});
