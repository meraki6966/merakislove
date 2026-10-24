// Guards the site assistant (components/SiteAssistant.tsx, the Meraki BIP
// widget). Run from the repo root:  npm run test:site-assistant
//
// It must stay dark unless NEXT_PUBLIC_SITE_ASSISTANT is "on", because the
// tenant's knowledge decides what it tells visitors, and must load from the
// one origin the CSP allows. The privacy page section follows the same
// switch. Proven by building both ways on 23 October 2026: off, the page has
// no widget script and no privacy section; on, both appear. Broken on purpose
// once and seen to fail.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

const read = (p) => readFileSync(new URL(`../../${p}`, import.meta.url), "utf8");
// Comments stripped, so a commented-out guard does not count as a guard.
const code = (src) => src.replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
const component = code(read("components/SiteAssistant.tsx"));
const privacy = code(read("app/privacy/page.tsx"));
const config = read("next.config.ts");

test("the widget renders nothing unless the switch is on", () => {
  assert.match(component, /SITE_ASSISTANT_ON = process\.env\.NEXT_PUBLIC_SITE_ASSISTANT === "on"/);
  assert.match(component, /if \(!SITE_ASSISTANT_ON\) return null;/);
});

test("the widget loads from the one origin the CSP allows", () => {
  assert.match(component, /BIP_ORIGIN = "https:\/\/www\.merakibip\.com"/);
  assert.match(component, /src=\{`\$\{BIP_ORIGIN\}\/api\/rag\/widget\/\$\{BIP_TENANT\}`\}/);
  assert.match(config, /script-src[^"]*https:\/\/www\.merakibip\.com/);
});

test("the privacy page discloses the assistant under the same switch", () => {
  assert.match(privacy, /\.\.\.\(SITE_ASSISTANT_ON \? \[\{\s*title: "The site assistant"/);
  assert.match(privacy, /does not screen for card numbers/);
});
