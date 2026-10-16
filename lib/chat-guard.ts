/**
 * What both demo chat routes check before a request can cost anything.
 * Shared by app/api/restaurant-reservation-chat and app/api/meraki-inn-chat,
 * and tested in scripts/tests/chat-guard.test.mjs.
 *
 * The routes are public pages that spend money on every call, so the order
 * is cheapest check first, and nothing reaches the AI provider until every
 * check here has passed:
 *  1. checkRequest: only JSON, and only from the page's own site. A browser
 *     sends a plain-text form post to any site without asking, so a
 *     third-party page could otherwise make its visitors call these routes.
 *  2. a rate limit per visitor, keyed on a salted hash of the address.
 *  3. a cap on the request body before it is parsed.
 *  4. checkConversation: shape, length, size and card numbers, both roles.
 *
 * Only node:crypto is imported, for the address hash. Nothing here talks to
 * the network or reads the environment.
 */
import { createHash, randomBytes } from "node:crypto";

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface ConversationLimits {
  /** Longest visitor message, in characters. */
  userChars: number;
  /** Longest assistant message accepted back from the browser. */
  assistantChars: number;
  /** Most messages, both roles, in one conversation. */
  messages: number;
}

/** Largest request body either route reads, in characters. */
export const BODY_CHARS = 60000;

export type GuardResult = { ok: true } | { ok: false; status: number; error: string };

// ------------------------------------------------------------------ the request

/**
 * Only a JSON request from this page's own site gets through.
 *
 * Requiring application/json means a browser on another site has to ask
 * first, and the routes only grant that to merakislove.com. Sec-Fetch-Site,
 * which every current browser sends on its own, says outright when another
 * site made the request. Older browsers without it fall back to comparing
 * Origin with Host. A script outside a browser sends neither header and is
 * held by the caps and the rate limit instead.
 */
export function checkRequest(headers: Headers): GuardResult {
  const type = (headers.get("content-type") ?? "").split(";")[0].trim().toLowerCase();
  if (type !== "application/json") {
    return { ok: false, status: 415, error: "Send the conversation as JSON." };
  }
  const site = headers.get("sec-fetch-site");
  if (site !== null) {
    return site === "same-origin"
      ? { ok: true }
      : { ok: false, status: 403, error: "This assistant only answers its own page." };
  }
  const origin = headers.get("origin");
  const host = headers.get("host");
  if (origin && host) {
    let originHost = "";
    try {
      originHost = new URL(origin).host;
    } catch {
      originHost = "";
    }
    if (originHost !== host) {
      return { ok: false, status: 403, error: "This assistant only answers its own page." };
    }
  }
  return { ok: true };
}

// ------------------------------------------------------------------ the visitor

// A fresh random value per server instance. The address itself is never kept:
// only a hash of it with this value, which changes on every restart.
const SALT = randomBytes(16);

/** The rate limit key for an address: a salted SHA-256, never the address. */
export function addressKey(address: string): string {
  return createHash("sha256").update(SALT).update(address).digest("base64url").slice(0, 22);
}

/**
 * In memory, so it is per server instance: a speed bump against one visitor
 * running up the bill. The Vercel Firewall and the Anthropic spend limit are
 * the ceilings above it. Entries older than the window are cleared at least
 * once per window, whenever the instance handles a request, so the map never
 * grows without bound.
 */
export function createLimiter(limit: number, windowMs: number, maxKeys = 5000) {
  const hits = new Map<string, number[]>();
  let lastSweep = 0;
  function sweep(now: number) {
    for (const [k, times] of hits) {
      if (times.every((t) => now - t >= windowMs)) hits.delete(k);
    }
    lastSweep = now;
  }
  const limited = function limited(key: string, now: number = Date.now()): boolean {
    if (now - lastSweep >= windowMs || hits.size > maxKeys) sweep(now);
    const recent = (hits.get(key) ?? []).filter((t) => now - t < windowMs);
    if (recent.length >= limit) {
      hits.set(key, recent);
      return true;
    }
    recent.push(now);
    hits.set(key, recent);
    return false;
  };
  /** How many visitors the limiter is holding right now. For tests. */
  limited.size = () => hits.size;
  return limited;
}

// ------------------------------------------------------------------ card numbers

function luhn(digits: string): boolean {
  let sum = 0;
  let double = false;
  for (let i = digits.length - 1; i >= 0; i--) {
    let n = digits.charCodeAt(i) - 48;
    if (double) {
      n *= 2;
      if (n > 9) n -= 9;
    }
    sum += n;
    double = !double;
  }
  return sum % 10 === 0;
}

/**
 * True when the text holds 13 to 19 digits, allowing spaces and hyphens
 * between them, that pass the Luhn check every payment card number passes.
 * A phone number or a date is too short. A long order number will only match
 * by the one in ten chance of the checksum, which is the safe direction to be
 * wrong in.
 */
export function findCardNumber(text: string): boolean {
  const runs = text.match(/\d(?:[ -]?\d){12,18}/g);
  if (!runs) return false;
  return runs.some((run) => {
    const digits = run.replace(/[ -]/g, "");
    return digits.length >= 13 && digits.length <= 19 && luhn(digits);
  });
}

// ------------------------------------------------------------------ the conversation

export type ConversationResult =
  | { ok: true; messages: ChatMessage[] }
  | { ok: false; status: number; error: string; card?: boolean };

function isMessage(m: unknown): m is ChatMessage {
  if (typeof m !== "object" || m === null) return false;
  const { role, content } = m as Record<string, unknown>;
  return (
    (role === "user" || role === "assistant") &&
    typeof content === "string" &&
    content.trim().length > 0
  );
}

/**
 * Everything the browser sends is checked here before a cent is spent. The
 * result holds only role and content: any other field the browser added is
 * dropped, so nothing but the conversation can reach the provider. The
 * greeting the page draws first is dropped too: a conversation starts with
 * the visitor.
 */
export function checkConversation(
  raw: unknown,
  limits: ConversationLimits,
  cardError: string,
): ConversationResult {
  if (!Array.isArray(raw) || raw.length === 0 || !raw.every(isMessage)) {
    return { ok: false, status: 400, error: "Expected a non-empty messages array." };
  }
  if (raw.length > limits.messages) {
    return {
      ok: false,
      status: 400,
      error: "This conversation has run long. Start over to keep going.",
    };
  }
  let start = 0;
  while (start < raw.length && raw[start].role === "assistant") start++;
  const messages = raw.slice(start).map((m) => ({ role: m.role, content: m.content }));
  if (messages.length === 0 || messages[messages.length - 1].role !== "user") {
    return { ok: false, status: 400, error: "The last message must be from the visitor." };
  }
  for (const m of messages) {
    const cap = m.role === "user" ? limits.userChars : limits.assistantChars;
    if (m.content.length > cap) {
      return {
        ok: false,
        status: 400,
        error: `Please keep it under ${limits.userChars} characters.`,
      };
    }
  }
  // Checked across the whole conversation, both roles, so a number typed three
  // turns ago is not replayed to the provider on this turn either.
  if (messages.some((m) => findCardNumber(m.content))) {
    return { ok: false, status: 400, card: true, error: cardError };
  }
  return { ok: true, messages };
}

/**
 * The most recent turns only, starting with a visitor message. A booking needs
 * a handful of answers, so older turns add cost without adding anything.
 */
export function lastTurns(messages: ChatMessage[], keep: number): ChatMessage[] {
  const tail = messages.slice(-keep);
  let start = 0;
  while (start < tail.length && tail[start].role === "assistant") start++;
  return tail.slice(start);
}

/** House style for anything the model writes: no dashes as punctuation, no markdown marks. */
export function tidyReply(text: string): string {
  return text
    .replace(/\s*[—–]\s*/g, ", ")
    .replace(/[*_#`]+/g, "")
    .trim();
}
