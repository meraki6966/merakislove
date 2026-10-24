// Guards the fix for content staying invisible under prefers-reduced-motion.
// Run from the repo root:  npm run test:reduced-motion
//
// The server can't know a visitor's motion preference, so a component that
// renders a different element when reduced motion is on hydrates over the
// server's motion element and keeps its inline opacity:0. The content never
// shows. ScrollReveal has since become a plain wrapper; the check below fails
// if a hidden starting state comes back.
// The behavior itself was proven in a browser with Reduce Motion emulated:
// see the commit that added this file. Broken on purpose once and seen to fail.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

const code = readFileSync(new URL("../../components/ScrollReveal.tsx", import.meta.url), "utf8")
  .replace(/\/\*[\s\S]*?\*\//g, "")
  .replace(/^\s*\/\/.*$/gm, "");

test("ScrollReveal renders its content visible, with no hidden starting state", () => {
  // Since the 2026-10 redesign ScrollReveal is a plain wrapper. Anything that
  // brings back a hidden first paint (an initial opacity, a motion element)
  // reopens the blank-page bug this file was written for.
  assert.ok(!/framer-motion/.test(code), "no motion library in the wrapper");
  assert.ok(!/\binitial\s*=/.test(code), "no initial state");
  assert.ok(!/opacity/.test(code), "no opacity anywhere in the wrapper");
  assert.match(code, /return\s*<Tag className=\{className\}>\{children\}<\/Tag>;/);
});

// ------------------------------------------------------ the home hero loop
//
// The 2026-10 redesign plays a slow loop of the hero engraving. Anyone with
// Reduce Motion on must get the still image instead. Proven in a browser on
// 23 October: with motion allowed the loop advanced from 3.0 s to 5.0 s; with
// reduce emulated it was display:none and paused. These checks hold the CSS
// rule and the class on the video in place. Broken on purpose once and seen
// to fail.
const css = readFileSync(new URL("../../app/globals.css", import.meta.url), "utf8");
const home = readFileSync(new URL("../../app/page.tsx", import.meta.url), "utf8");

test("the hero loop is hidden under prefers-reduced-motion", () => {
  assert.match(
    css,
    /@media\s*\(prefers-reduced-motion:\s*reduce\)\s*\{\s*\.hero-loop\s*\{\s*display:\s*none;?\s*\}/,
  );
});

test("the hero video carries the hero-loop class and a still sits under it", () => {
  assert.match(home, /<video\s+className="hero-loop\b/);
  assert.match(home, /src="\/art\/hero-loop-poster\.jpg"/);
  assert.match(home, /\bmuted\b/);
});
