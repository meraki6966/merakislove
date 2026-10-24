// Tests for the Shadow AI self-assessment at /shadow-ai.
// Run from the repo root:  npm run test:shadow-ai
// Against a running copy:  BASE_URL=https://<host> npm run test:shadow-ai
//
// What they hold the page to:
//   1. Ten questions, scored 0 to 3, where the safest answer is always worth 0.
//   2. The total, the bands and the three biggest gaps come out as designed,
//      and one serious answer can't hide behind a low total.
//   3. Nothing in the component or its module can send, store or expose an
//      answer: no network call, no browser storage, no cookies, no change to
//      the address bar, no form element, no analytics call, and a Calendly
//      link that carries nothing from the page.
//   4. The page calls itself a self-assessment, says where answers go, and
//      the privacy page describes it.
// Each was broken on purpose once and seen to fail before it was trusted.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";

import {
  BANDS,
  MAX_SCORE,
  QUESTIONS,
  WORST,
  answeredCount,
  bandFor,
  isComplete,
  resultBand,
  score,
  topGaps,
} from "../../lib/shadow-ai.ts";
import sitemap from "../../app/sitemap.ts";
import { calendly } from "../../lib/site.ts";

const root = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, root), "utf8");
const BASE_URL = process.env.BASE_URL?.replace(/\/$/, "");

const COMPONENT = "components/ShadowAiCheck.tsx";
const MODULE = "lib/shadow-ai.ts";
const PAGE = "app/shadow-ai/page.tsx";

/** Every question answered with the option at the given position from the safest. */
function answerAll(pick) {
  return Object.fromEntries(QUESTIONS.map((q) => [q.id, pick(q)]));
}
const best = (q) => q.options.findIndex((o) => o.points === 0);
const worst = (q) => {
  const max = Math.max(...q.options.map((o) => o.points));
  return q.options.findIndex((o) => o.points === max);
};

// ------------------------------------------------------------ the questions

test("ten questions, each scored 0 to 3, with a safest answer worth 0 and the words for its gap", () => {
  assert.equal(QUESTIONS.length, 10);
  assert.equal(new Set(QUESTIONS.map((q) => q.id)).size, 10, "question ids must be unique");
  assert.equal(new Set(QUESTIONS.map((q) => q.priority)).size, 10, "priorities must be unique so ties always break the same way");
  for (const q of QUESTIONS) {
    assert.ok(q.options.length >= 3, `${q.id} needs at least three options`);
    const points = q.options.map((o) => o.points);
    assert.ok(points.every((p) => Number.isInteger(p) && p >= 0 && p <= WORST), `${q.id} has a score outside 0 to ${WORST}`);
    assert.ok(points.includes(0), `${q.id} has no safe answer`);
    for (const key of ["title", "why", "first"]) assert.ok(q.gap[key].trim().length > 10, `${q.id} is missing gap.${key}`);
  }
  const sensitive = QUESTIONS.find((q) => q.id === "sensitive");
  assert.equal(Math.max(...sensitive.options.map((o) => o.points)), 2, "holding sensitive records is context, so it tops out below WORST");
});

// ------------------------------------------------------------ the scoring

test("the score adds the chosen options, from 0 up to MAX_SCORE", () => {
  assert.equal(score(answerAll(best)), 0);
  assert.equal(score(answerAll(worst)), MAX_SCORE);
  assert.equal(MAX_SCORE, 29);
  const some = answerAll(best);
  some["client-data"] = 3; // "Yes, it happens regularly." = 3
  some.policy = 2; // "We've talked about it. Nothing is written." = 2
  assert.equal(score(some), 5);
});

test("the bands split at 8 and 17", () => {
  assert.deepEqual(BANDS.map((b) => b.from), [0, 8, 17]);
  assert.equal(bandFor(0).label, "Mostly covered");
  assert.equal(bandFor(7).label, "Mostly covered");
  assert.equal(bandFor(8).label, "Gaps to close");
  assert.equal(bandFor(16).label, "Gaps to close");
  assert.equal(bandFor(17).label, "Wide open");
  assert.equal(bandFor(MAX_SCORE).label, "Wide open");
});

test("one answer at the worst level keeps a low total out of 'Mostly covered'", () => {
  const pasting = answerAll(best);
  pasting["client-data"] = 3; // client data goes into AI tools regularly
  assert.equal(score(pasting), 3);
  assert.equal(resultBand(pasting).label, "Gaps to close");

  const careful = answerAll(best);
  careful.sensitive = 2; // a medical biller with everything else in place
  assert.equal(resultBand(careful).label, "Mostly covered");
});

test("the gaps come most points first, ties broken by priority, and a safest answer is never a gap", () => {
  assert.deepEqual(topGaps(answerAll(best)), []);

  const answers = answerAll(best);
  answers.offboarding = 2; // 3 points, priority 10
  answers["client-data"] = 2; // 2 points, priority 1
  answers.inventory = 3; // 3 points, priority 6
  answers.policy = 1; // 1 point
  assert.deepEqual(topGaps(answers).map((q) => q.id), ["inventory", "offboarding", "client-data"]);
  assert.deepEqual(topGaps(answers, 10).map((q) => q.id), ["inventory", "offboarding", "client-data", "policy"]);
});

test("only a full set of valid answers counts as complete", () => {
  assert.equal(answeredCount({}), 0);
  const partial = answerAll(best);
  delete partial.response;
  assert.equal(answeredCount(partial), 9);
  assert.equal(isComplete(partial), false);
  assert.equal(isComplete({ ...partial, response: 99 }), false, "an option that does not exist is not an answer");
  assert.equal(isComplete(answerAll(best)), true);
});

// ------------------------------------------------- nothing leaves the tab

const FORBIDDEN = [
  [/\bfetch\s*\(/, "a network request"],
  [/XMLHttpRequest/, "a network request"],
  [/sendBeacon/, "a beacon"],
  [/WebSocket|EventSource/, "a socket"],
  [/localStorage|sessionStorage|indexedDB|caches\./, "browser storage"],
  [/document\.cookie|cookieStore/, "a cookie"],
  [/\bhistory\.|pushState|replaceState|location\.|useRouter|useSearchParams|usePathname/, "a change to the address bar"],
  [/<form\b|action=/, "a form element, which Google Analytics form tracking would see"],
  [/\bgtag\b|dataLayer/, "an analytics call"],
  [/postMessage|window\.open/, "a message to another window"],
];

test("the component and its module have no way to send, store or expose an answer", () => {
  for (const file of [COMPONENT, MODULE]) {
    const code = read(file).replace(/\/\*[\s\S]*?\*\//g, "").replace(/^\s*\/\/.*$/gm, "");
    for (const [pattern, what] of FORBIDDEN) {
      assert.ok(!pattern.test(code), `${file} contains ${what}: ${pattern}`);
    }
  }
});

test("the Calendly link carries nothing from the page", () => {
  const code = read(COMPONENT);
  const hrefs = [...code.matchAll(/href=\{([^}]+)\}/g)].map((m) => m[1].trim());
  assert.deepEqual(hrefs, ["calendly.newProject"], "the only computed link must be the plain Calendly address");
  assert.ok(!calendly.newProject.includes("?") && !calendly.newProject.includes("#"), "the Calendly address must have no query or fragment");
});

// ------------------------------------------------------- honest wording

test("the page calls itself a self-assessment and says where answers go", () => {
  const page = read(PAGE);
  const component = read(COMPONENT);
  assert.match(page, /kicker="Self-assessment"/);
  assert.match(page, /never receives your answers/);
  assert.match(page, /Nothing is sent and nothing is saved/);
  assert.match(component, /This is a self-assessment\./);
  assert.match(component, /isn&apos;t a compliance audit or legal advice/);
  assert.match(read("app/privacy/page.tsx"), /title: "The Shadow AI self-assessment"/);
  assert.ok(sitemap().some((e) => e.url === "https://merakislove.com/shadow-ai"), "the page belongs in the sitemap");
});

test("no em or en dashes in anything a visitor reads on the page", () => {
  for (const file of [PAGE, COMPONENT, MODULE]) {
    const code = read(file);
    assert.ok(!/[–—]|&[mn]dash;|&#821[12];/.test(code), `${file} has an em or en dash`);
  }
});

// ------------------------------------------------- against a running copy

test("a running copy serves the page with the questions and no form element", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  const res = await fetch(`${BASE_URL}/shadow-ai`, { redirect: "manual" });
  assert.equal(res.status, 200);
  const html = await res.text();
  assert.ok(!/<form\b/i.test(html), "the page must not render a form element");
  assert.equal((html.match(/type="radio"/g) || []).length, QUESTIONS.reduce((n, q) => n + q.options.length, 0));
  assert.match(html, /<link rel="canonical" href="https:\/\/merakislove\.com\/shadow-ai"/);
});
