// Tests for the "Listen to Adam" builder notes on the demo pages.
// Run from the repo root:  npm run test:demo-audio
//
// Every demo page that plays Adam's cloned voice must:
//   1. play a file that sits next to the demo on this site, and exists,
//   2. say on the page that the voice is an AI clone,
//   3. carry the full transcript, word for word as approved,
//   4. never autoplay, and keep the native controls in the HTML so the
//      audio still works if the script does not run.
// Each rule was broken once on purpose and seen to fail before it was trusted.
import assert from "node:assert/strict";
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { test } from "node:test";

const root = new URL("../../", import.meta.url);

// The approved scripts, keyed by page. Change a recording, change it here too.
const APPROVED = {
  "/demos/keelhouse/index.html":
    "I'm Adam McClarin, and I built Keelhouse for the moment something breaks at the house. " +
    "A homeowner standing in a wet basement wants three answers: who fixes this, what it costs, and how fast they can book. " +
    "So the first question on this page is what's going on at the house. Pick water heater, and the booking form opens with it already checked. The visit fees sit in plain view. " +
    "Every trade, every town and every finished job has its own page, so a neighbor searching for the same fix can find it. " +
    "Keelhouse is a demo, and the company doesn't exist. If you run a trade, I can adapt this layout to yours. Book a call with me at merakislove.com.",
};

function walk(dirUrl) {
  const out = [];
  for (const name of readdirSync(dirUrl)) {
    const child = new URL(name, dirUrl);
    if (statSync(child).isDirectory()) out.push(...walk(new URL(`${name}/`, dirUrl)));
    else out.push(child);
  }
  return out;
}
const pages = walk(new URL("public/demos/", root))
  .filter((u) => u.pathname.endsWith(".html"))
  .map((u) => ({ path: u.pathname.slice(u.pathname.indexOf("/demos/")), html: readFileSync(u, "utf8") }))
  .filter((p) => /<audio\b/.test(p.html));

const text = (html) =>
  html.replace(/<[^>]+>/g, "").replace(/&#8217;/g, "'").replace(/&amp;/g, "&").replace(/\s+/g, " ").trim();

test("every page with a builder recording is one we approved", () => {
  assert.ok(pages.length >= 1, "expected at least the Keelhouse recording");
  for (const p of pages) assert.ok(p.path in APPROVED, `${p.path} plays audio that has no approved script here`);
});

test("each recording is a file on this site, next to its demo, and it exists", () => {
  for (const p of pages) {
    const srcs = [...p.html.matchAll(/<audio\b[^>]*\bsrc="([^"]+)"/g)].map((m) => m[1]);
    assert.equal(srcs.length, 1, `${p.path} should have one recording`);
    const demo = p.path.split("/").slice(0, 3).join("/");
    assert.ok(srcs[0].startsWith(`${demo}/audio/`), `${srcs[0]} must live under ${demo}/audio/`);
    assert.ok(existsSync(new URL(`public${srcs[0]}`, root)), `${srcs[0]} is missing from public/`);
  }
});

test("each page says the voice is an AI clone", () => {
  for (const p of pages) {
    assert.match(text(p.html), /AI voice clone of Adam McClarin/, `${p.path} must disclose the cloned voice`);
  }
});

test("each page carries the approved transcript, word for word", () => {
  for (const p of pages) {
    const m = p.html.match(/<details class="listen-transcript">([\s\S]*?)<\/details>/);
    assert.ok(m, `${p.path} has no transcript`);
    const body = text(m[1]).replace(/^Read the transcript\s*/, "");
    assert.equal(body, APPROVED[p.path], `${p.path} transcript differs from the approved script`);
  }
});

test("nothing autoplays, and the native controls stay in the HTML", () => {
  for (const p of pages) {
    const tag = p.html.match(/<audio\b[^>]*>/)[0];
    assert.ok(!/\bautoplay\b/.test(tag), `${p.path} must not autoplay`);
    assert.match(tag, /\bcontrols\b/, `${p.path} must keep native controls as the fallback`);
    assert.match(tag, /preload="none"/, `${p.path} should not download audio before someone presses play`);
  }
});
