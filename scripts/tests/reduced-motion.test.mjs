// Guards the fix for content staying invisible under prefers-reduced-motion.
// Run from the repo root:  npm run test:reduced-motion
//
// The server can't know a visitor's motion preference, so a component that
// renders a different element when reduced motion is on hydrates over the
// server's motion element and keeps its inline opacity:0. The content never
// shows. These checks fail if ScrollReveal goes back to swapping elements.
// The behavior itself was proven in a browser with Reduce Motion emulated:
// see the commit that added this file. Broken on purpose once and seen to fail.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

const code = readFileSync(new URL("../../components/ScrollReveal.tsx", import.meta.url), "utf8")
  .replace(/\/\*[\s\S]*?\*\//g, "")
  .replace(/^\s*\/\/.*$/gm, "");

test("ScrollReveal renders the same motion element whatever the motion preference", () => {
  const returns = code.match(/\breturn\b/g) || [];
  assert.equal(returns.length, 1, "one return: the motion element, never a plain stand-in");
  assert.match(code, /return\s*\(\s*<MotionTag\b/);
  assert.ok(!/if\s*\(\s*reduceMotion\s*\)/.test(code), "reduced motion may change the transition, not the element");
});

test("under reduced motion the reveal is instant", () => {
  assert.match(code, /reduceMotion\s*\?\s*\{\s*duration:\s*0\s*\}/);
});

// ------------------------------------------------- when JavaScript never runs
//
// ScrollReveal's hidden state is an inline opacity:0, so without the page's
// code nothing fades in. Measured on 16 October: with JavaScript off, or with
// the page's code blocked, the live home page showed 0 of 60 text blocks.
// lib/reveal-fallback.ts closes that. These tests hold the pieces in place,
// and run the inline fallback in a sandbox to prove what it does.
import vm from "node:vm";
import {
  AFTER_LOAD_MS,
  HARD_STOP_MS,
  REVEAL_FALLBACK_SCRIPT,
  REVEAL_NOSCRIPT,
  REVEAL_VISIBLE_CSS,
} from "../../lib/reveal-fallback.ts";

const layout = readFileSync(new URL("../../app/layout.tsx", import.meta.url), "utf8");
const reveal = readFileSync(new URL("../../components/ScrollReveal.tsx", import.meta.url), "utf8");

test("the visible rule overrides the inline hidden state, and only on ScrollReveal's elements", () => {
  assert.match(REVEAL_VISIBLE_CSS, /^\[data-reveal\]\{opacity:1!important;transform:none!important\}$/);
  assert.match(reveal, /data-reveal=""/, "ScrollReveal must mark what it hides");
  assert.match(reveal, /__revealReady = true/, "ScrollReveal must tell the fallback it is running");
});

test("the root layout carries the noscript rule and the inline fallback", () => {
  assert.match(layout, /<noscript dangerouslySetInnerHTML=\{\{ __html: REVEAL_NOSCRIPT \}\} \/>/);
  assert.match(layout, /<script dangerouslySetInnerHTML=\{\{ __html: REVEAL_FALLBACK_SCRIPT \}\} \/>/);
  assert.equal(REVEAL_NOSCRIPT, `<style>${REVEAL_VISIBLE_CSS}</style>`);
});

function runFallback({ ready }) {
  const appended = [];
  const timers = [];
  const listeners = {};
  const window = { __revealReady: false, addEventListener: (t, fn) => (listeners[t] = fn) };
  const document = {
    head: { appendChild: (el) => appended.push(el) },
    createElement: () => ({ attrs: {}, setAttribute(k, v) { this.attrs[k] = v; }, textContent: "" }),
  };
  const setTimeout = (fn, ms) => timers.push({ fn, ms });
  vm.runInNewContext(REVEAL_FALLBACK_SCRIPT, { window, document, setTimeout });
  if (ready) window.__revealReady = true; // the page's code started
  listeners.load?.();
  for (const t of timers.sort((a, b) => a.ms - b.ms)) t.fn();
  return { appended, delays: timers.map((t) => t.ms).sort((a, b) => a - b) };
}

test("the fallback shows the text when the page's code never starts, once", () => {
  const { appended, delays } = runFallback({ ready: false });
  assert.deepEqual(delays, [AFTER_LOAD_MS, HARD_STOP_MS]);
  assert.equal(appended.length, 1, "exactly one style, even though both timers fire");
  assert.equal(appended[0].textContent, REVEAL_VISIBLE_CSS);
});

test("the fallback stays out of the way on a normal visit", () => {
  assert.equal(runFallback({ ready: true }).appended.length, 0);
});
