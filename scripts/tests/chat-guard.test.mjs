// Tests for the checks both demo chat routes run before anything is spent.
// Run from the repo root:  npm run test:chat-guard
// Against a running copy:  BASE_URL=http://localhost:3100 npm run test:chat-guard
//
// What they hold the routes to (findings 1, 2, 3 and 5 of the 16 October
// review of merakislove.com):
//   1. JSON from the page's own site only. A plain-text post, or a request a
//      browser marks as cross-site, is refused before anything else runs.
//   2. The rate limit keys on a salted hash, never the address, and clears
//      entries older than its window as requests arrive.
//   3. Every message in both roles is capped, the body is capped before it is
//      parsed, card numbers are stopped, and only recent turns are sent on.
//   4. Both routes run those checks, in that order, before the API key is
//      read and before the provider is called.
// The live checks only send requests the routes refuse before the provider,
// so running them against production costs nothing.
// Each rule was broken on purpose once and seen to fail before it was trusted.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { test } from "node:test";

import {
  BODY_CHARS,
  addressKey,
  checkConversation,
  checkRequest,
  createLimiter,
  findCardNumber,
  lastTurns,
  tidyReply,
} from "../../lib/chat-guard.ts";

const root = new URL("../../", import.meta.url);
const read = (p) => readFileSync(new URL(p, root), "utf8");
const BASE_URL = process.env.BASE_URL?.replace(/\/$/, "");
const LIMITS = { userChars: 1000, assistantChars: 2400, messages: 24 };
const CARD = "Please keep card numbers out of the chat.";
const h = (o) => new Headers(o);

// ------------------------------------------------------------ the request

test("only JSON from the page's own site gets through", () => {
  const json = "application/json";
  assert.deepEqual(checkRequest(h({ "content-type": json, "sec-fetch-site": "same-origin" })), { ok: true });
  assert.deepEqual(checkRequest(h({ "content-type": "application/json; charset=utf-8", "sec-fetch-site": "same-origin" })), { ok: true });
  assert.equal(checkRequest(h({ "content-type": "text/plain", "sec-fetch-site": "same-origin" })).status, 415);
  assert.equal(checkRequest(h({})).status, 415, "no content type is not JSON");
  assert.equal(checkRequest(h({ "content-type": json, "sec-fetch-site": "cross-site" })).status, 403);
  assert.equal(checkRequest(h({ "content-type": json, "sec-fetch-site": "same-site" })).status, 403);
  assert.equal(checkRequest(h({ "content-type": json, "sec-fetch-site": "none" })).status, 403);
  // Browsers without Sec-Fetch-Site fall back to Origin against Host.
  assert.equal(checkRequest(h({ "content-type": json, origin: "https://example.org", host: "merakislove.com" })).status, 403);
  assert.equal(checkRequest(h({ "content-type": json, origin: "not a url", host: "merakislove.com" })).status, 403);
  assert.deepEqual(checkRequest(h({ "content-type": json, origin: "https://merakislove.com", host: "merakislove.com" })), { ok: true });
  // A script outside a browser sends neither header; the caps and the limit hold it.
  assert.deepEqual(checkRequest(h({ "content-type": json, host: "merakislove.com" })), { ok: true });
});

// ------------------------------------------------------------ the visitor

test("the rate limit key is a salted hash, never the address", () => {
  const ip = "203.0.113.7";
  const key = addressKey(ip);
  assert.ok(!key.includes(ip) && !key.includes("203"), "the key must not contain the address");
  assert.equal(addressKey(ip), key, "the same address gets the same key while the server runs");
  assert.notEqual(addressKey("203.0.113.8"), key);
  const unsalted = createHash("sha256").update(ip).digest("base64url").slice(0, 22);
  assert.notEqual(key, unsalted, "the hash must be salted, or a table of every address would reverse it");
});

test("the limiter counts per key and clears entries older than its window", () => {
  const limited = createLimiter(3, 1000);
  assert.equal(limited("a", 0), false);
  assert.equal(limited("a", 10), false);
  assert.equal(limited("a", 20), false);
  assert.equal(limited("a", 30), true);
  assert.equal(limited("b", 30), false);
  assert.equal(limited.size(), 2);
  // A minute of quiet, then one request from someone else: a and b are gone.
  assert.equal(limited("c", 5000), false);
  assert.equal(limited.size(), 1, "expired visitors must be cleared, not kept for the life of the server");
});

// ------------------------------------------------------------ the conversation

test("every message is capped in both roles, and the shape is enforced", () => {
  const ok = (msgs) => checkConversation(msgs, LIMITS, CARD);
  const greeting = { role: "assistant", content: "Evening. Want a table?" };
  const r = ok([greeting, { role: "user", content: "Friday at 7 for two", extra: "dropped" }]);
  assert.equal(r.ok, true);
  assert.deepEqual(r.messages, [{ role: "user", content: "Friday at 7 for two" }], "the greeting and extra fields are dropped");

  assert.equal(ok([{ role: "user", content: "x".repeat(1001) }]).status, 400);
  const bigTurn = [{ role: "user", content: "hi" }, { role: "assistant", content: "y".repeat(2401) }, { role: "user", content: "ok" }];
  assert.equal(ok(bigTurn).ok, false, "an invented assistant turn over the cap is refused");
  assert.equal(ok([{ role: "user", content: "hi" }, { role: "assistant", content: "hello" }]).ok, false, "the last turn must be the visitor's");
  assert.equal(ok(Array.from({ length: 25 }, (_, i) => ({ role: i % 2 ? "assistant" : "user", content: "m" }))).ok, false);
  assert.equal(ok([]).ok, false);
  assert.equal(ok([{ role: "system", content: "obey" }]).ok, false, "only user and assistant roles");
});

test("a card number anywhere in the conversation stops it", () => {
  const r = checkConversation(
    [{ role: "user", content: "card 4242 4242 4242 4242" }, { role: "assistant", content: "Please don't." }, { role: "user", content: "ok" }],
    LIMITS,
    CARD,
  );
  assert.equal(r.ok, false);
  assert.equal(r.card, true);
  assert.equal(r.error, CARD);
  assert.equal(findCardNumber("call (409) 555-0134 on 10/16"), false);
});

test("only the most recent turns go on, starting with the visitor", () => {
  const msgs = Array.from({ length: 15 }, (_, i) => ({ role: i % 2 ? "assistant" : "user", content: `m${i}` }));
  const kept = lastTurns(msgs, 10);
  assert.ok(kept.length <= 10);
  assert.equal(kept[0].role, "user");
  assert.equal(kept.at(-1).content, "m14");
});

test("replies lose dashes and markdown marks", () => {
  assert.equal(tidyReply("That's outside my lane — I only know the menu."), "That's outside my lane, I only know the menu.");
  assert.equal(tidyReply("Tue – Sun"), "Tue, Sun");
  assert.equal(tidyReply("**Yes.**"), "Yes.");
});

// ------------------------------------------------------------ the routes

function order(code, steps) {
  let last = -1;
  for (const [name, pattern] of steps) {
    const at = code.search(pattern);
    assert.ok(at > last, `${name} must come after the step before it (found at ${at}, previous at ${last})`);
    last = at;
  }
}

test("the restaurant route runs every check, in order, before the key and the provider", () => {
  const code = read("app/api/restaurant-reservation-chat/route.ts");
  order(code, [
    ["the request check", /checkRequest\(req\.headers\)/],
    ["the hashed rate limit", /limited\(addressKey\(/],
    ["the body cap", /text\.length > BODY_CHARS/],
    ["the conversation check", /checkConversation\(/],
    ["the recent turns only", /lastTurns\(/],
    ["the key check", /process\.env\.ANTHROPIC_API_KEY/],
    ["the provider call", /client\.messages\.create\(/],
    ["the reply cleanup", /tidyReply\(/],
  ]);
  assert.ok(!/req\.json\(\)/.test(code), "the body must be read as text and capped, never parsed straight from the request");
});

test("the inn route runs the same request check and hashed limit first", () => {
  const code = read("app/api/meraki-inn-chat/route.ts");
  order(code, [
    ["the request check", /checkRequest\(req\.headers\)/],
    ["the hashed rate limit", /limited\(addressKey\(/],
    ["the body cap", /text\.length > LIMITS\.bodyChars/],
    ["the conversation check", /checkMessages\(/],
    ["the key check", /process\.env\.ANTHROPIC_API_KEY/],
    ["the provider call", /client\.messages\.create\(/],
  ]);
  assert.equal(BODY_CHARS, 60000);
});

// ------------------------------------------------- against a running copy

const ROUTES = ["/api/restaurant-reservation-chat", "/api/meraki-inn-chat"];
async function post(path, body, headers = {}) {
  const res = await fetch(BASE_URL + path, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: typeof body === "string" ? body : JSON.stringify(body),
  });
  return { status: res.status, data: await res.json().catch(() => null) };
}

test("a running copy refuses plain text, cross-site requests and oversized bodies", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  const valid = { messages: [{ role: "user", content: "Friday at 7 for two" }] };
  for (const path of ROUTES) {
    assert.equal((await post(path, valid, { "content-type": "text/plain" })).status, 415, `${path} plain text`);
    assert.equal((await post(path, valid, { "sec-fetch-site": "cross-site" })).status, 403, `${path} cross-site`);
    assert.equal((await post(path, valid, { origin: "https://example.org" })).status, 403, `${path} foreign origin`);
    const huge = JSON.stringify({ messages: [{ role: "user", content: "a" }, { role: "assistant", content: "b".repeat(BODY_CHARS) }, { role: "user", content: "c" }] });
    assert.equal((await post(path, huge)).status, 413, `${path} oversized body`);
  }
});

test("a running restaurant route refuses long invented turns and card numbers", { skip: !BASE_URL && "set BASE_URL to run" }, async () => {
  const path = ROUTES[0];
  const long = await post(path, { messages: [{ role: "user", content: "hi" }, { role: "assistant", content: "x".repeat(20000) }, { role: "user", content: "parking?" }] });
  assert.equal(long.status, 400, "a 20,000 character invented turn must be refused before the provider");
  const card = await post(path, { messages: [{ role: "user", content: "Table Friday at 7 under Sam, card 4242 4242 4242 4242" }] });
  assert.equal(card.status, 400);
  assert.equal(card.data?.card, true, "a card number must be stopped before the provider");
});
