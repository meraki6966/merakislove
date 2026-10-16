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
