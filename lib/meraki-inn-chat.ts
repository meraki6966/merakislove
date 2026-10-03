/**
 * The rules of the Meraki Inn chat assistant, kept apart from the route so
 * they can be tested on their own (scripts/tests/meraki-inn-chat.test.mjs).
 *
 * Nothing in this file talks to the network, reads the environment or imports
 * anything. The route passes in what it needs. That is deliberate: every
 * guarantee the chat makes is a plain function here with a test that can fail.
 *
 * The guarantees:
 *  1. The model can change three fields on the date request form and nothing
 *     else, and only to values this file accepts (validateFill).
 *  2. A message that looks like a payment card number is never forwarded to
 *     the AI provider (findCardNumber, checkMessages).
 *  3. A conversation is bounded in length and size before it costs anything
 *     (checkMessages).
 *  4. One address can only ask so often (createLimiter).
 *  5. Every dollar figure the visitor is quoted in a confirmation is computed
 *     here, not by the model (quote, confirmation, priceTable).
 */

export interface Room {
  key: string;
  name: string;
  rate: number;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}

export interface Fill {
  arrive: string; // YYYY-MM-DD
  nights: number;
  room: string; // a Room key
}

export const LIMITS = {
  /** Longest single visitor message, in characters. */
  userChars: 1000,
  /** Longest assistant message we will accept back from the browser. */
  assistantChars: 2400,
  /** Most messages (visitor and assistant) in one conversation. */
  messages: 24,
  /** Largest request body, in characters, read before anything is parsed. */
  bodyChars: 60000,
  /** Nights the form offers. Longer stays are a phone call. */
  maxNights: 7,
  /** How far ahead a date request can be, in days. */
  maxDaysAhead: 540,
  /** State 6 percent plus City of Galveston 9 percent. */
  taxRate: 0.15,
} as const;

// ------------------------------------------------------------------ dates

/** Today's date on the island, as YYYY-MM-DD. The server decides this, never the browser. */
export function todayInGalveston(now: Date = new Date()): string {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: "America/Chicago",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(now);
  const get = (t: string) => parts.find((p) => p.type === t)?.value ?? "";
  return `${get("year")}-${get("month")}-${get("day")}`;
}

/** Midnight UTC for a YYYY-MM-DD string, or null if it is not a real calendar date. */
export function parseDay(s: unknown): Date | null {
  if (typeof s !== "string" || !/^\d{4}-\d{2}-\d{2}$/.test(s)) return null;
  const d = new Date(`${s}T00:00:00Z`);
  if (Number.isNaN(d.getTime())) return null;
  // Reject dates the engine would roll over, such as February 30.
  return d.toISOString().slice(0, 10) === s ? d : null;
}

export function addDays(day: string, n: number): string {
  const d = parseDay(day);
  if (!d) throw new Error("addDays needs a real date");
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}

/** "Friday, October 9", with the year added when it is not the current one. */
export function sayDay(day: string, today: string): string {
  const d = parseDay(day);
  if (!d) throw new Error("sayDay needs a real date");
  const sameYear = day.slice(0, 4) === today.slice(0, 4);
  return new Intl.DateTimeFormat("en-US", {
    timeZone: "UTC",
    weekday: "long",
    month: "long",
    day: "numeric",
    ...(sameYear ? {} : { year: "numeric" }),
  }).format(d);
}

// ------------------------------------------------------------------ money

function dollars(n: number): string {
  const whole = Number.isInteger(n);
  return (
    "$" +
    n.toLocaleString("en-US", {
      minimumFractionDigits: whole ? 0 : 2,
      maximumFractionDigits: 2,
    })
  );
}

export function quote(room: Room, nights: number) {
  const rooms = room.rate * nights;
  // Work in cents so 15 percent of a whole dollar amount never drifts.
  const taxCents = Math.round(rooms * 100 * LIMITS.taxRate);
  const totalCents = rooms * 100 + taxCents;
  return {
    rooms,
    tax: taxCents / 100,
    total: totalCents / 100,
    roomsText: dollars(rooms),
    taxText: dollars(taxCents / 100),
    totalText: dollars(totalCents / 100),
  };
}

/** Every room for one to seven nights, so the model reads prices and never multiplies. */
export function priceTable(rooms: readonly Room[]): string {
  const lines: string[] = [];
  for (const r of rooms) {
    const cells: string[] = [];
    for (let n = 1; n <= LIMITS.maxNights; n++) {
      const q = quote(r, n);
      cells.push(`${n} night${n === 1 ? "" : "s"} ${q.roomsText} before tax, ${q.totalText} with tax`);
    }
    lines.push(`${r.name}: ${cells.join("; ")}.`);
  }
  return lines.join("\n");
}

// ------------------------------------------------------------------ the one thing the model can do

export type FillResult =
  | { ok: true; fill: Fill }
  | { ok: false; reason: string };

/**
 * The model's tool call is untrusted input, the same as a form post from a
 * stranger. Only these three fields are read, and each has to pass on its own.
 */
export function validateFill(
  input: unknown,
  rooms: readonly Room[],
  today: string,
): FillResult {
  if (typeof input !== "object" || input === null || Array.isArray(input)) {
    return { ok: false, reason: "I did not get the dates in a form I can use." };
  }
  const { arrive, nights, room } = input as Record<string, unknown>;

  const day = parseDay(arrive);
  if (!day || typeof arrive !== "string") {
    return { ok: false, reason: "I could not read the arrival date." };
  }
  if (arrive < today) {
    return { ok: false, reason: "That arrival date has already passed." };
  }
  if (arrive > addDays(today, LIMITS.maxDaysAhead)) {
    return {
      ok: false,
      reason: "That is further ahead than the form takes. Please call the inn for dates that far out.",
    };
  }

  if (typeof nights !== "number" || !Number.isInteger(nights) || nights < 1) {
    return { ok: false, reason: "I could not read the number of nights." };
  }
  if (nights > LIMITS.maxNights) {
    return {
      ok: false,
      reason: `The form takes one to ${LIMITS.maxNights} nights. For a longer stay, please call the inn.`,
    };
  }

  if (typeof room !== "string" || !rooms.some((r) => r.key === room)) {
    return { ok: false, reason: "I could not match that to one of the five rooms." };
  }

  return { ok: true, fill: { arrive, nights, room } };
}

/** The confirmation is written here, with figures from quote(), not by the model. */
export function confirmation(
  fill: Fill,
  rooms: readonly Room[],
  today: string,
): string {
  const room = rooms.find((r) => r.key === fill.room);
  if (!room) throw new Error("confirmation needs a known room");
  const q = quote(room, fill.nights);
  const nights = `${fill.nights} night${fill.nights === 1 ? "" : "s"}`;
  const out = addDays(fill.arrive, fill.nights);
  return (
    `I put ${room.name} for ${nights}, arriving ${sayDay(fill.arrive, today)} and leaving ${sayDay(out, today)}, into the date request form on this page. ` +
    `That is ${q.roomsText} before tax, or ${q.totalText} with the 15 percent hotel tax.\n\n` +
    `Add your name and email in the form and the innkeeper replies the same day to confirm. I cannot see availability, so nothing is reserved yet. This is a demo, so nothing is sent.`
  );
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

export type MessagesResult =
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
 * dropped, so nothing but the conversation can reach the provider.
 */
export function checkMessages(raw: unknown, phone: string): MessagesResult {
  if (!Array.isArray(raw) || raw.length === 0 || !raw.every(isMessage)) {
    return { ok: false, status: 400, error: "Expected a non-empty messages array." };
  }
  if (raw.length > LIMITS.messages) {
    return {
      ok: false,
      status: 400,
      error: "This conversation has run long. Start over to keep going.",
    };
  }
  // The greeting is drawn by the page. A conversation starts with the visitor.
  let start = 0;
  while (start < raw.length && raw[start].role === "assistant") start++;
  const messages = raw
    .slice(start)
    .map((m) => ({ role: m.role, content: m.content }));
  if (messages.length === 0 || messages[messages.length - 1].role !== "user") {
    return { ok: false, status: 400, error: "The last message must be from the visitor." };
  }
  for (const m of messages) {
    const cap = m.role === "user" ? LIMITS.userChars : LIMITS.assistantChars;
    if (m.content.length > cap) {
      return {
        ok: false,
        status: 400,
        error: `Please keep it under ${LIMITS.userChars} characters.`,
      };
    }
  }
  // Checked across the whole conversation, both roles, so a number typed three
  // turns ago is not replayed to the provider on this turn either.
  if (messages.some((m) => findCardNumber(m.content))) {
    return {
      ok: false,
      status: 400,
      card: true,
      error: `Please keep card numbers out of the chat. That message was not sent on. A card is only ever taken by phone, at ${phone}.`,
    };
  }
  return { ok: true, messages };
}

// ------------------------------------------------------------------ rate limit

/**
 * In memory, so it is per server instance. A speed bump against one visitor
 * running up the bill, not a global quota.
 */
export function createLimiter(limit: number, windowMs: number, maxKeys = 5000) {
  const hits = new Map<string, number[]>();
  return function limited(key: string, now: number = Date.now()): boolean {
    if (hits.size > maxKeys) {
      for (const [k, times] of hits) {
        if (times.every((t) => now - t >= windowMs)) hits.delete(k);
      }
    }
    const recent = (hits.get(key) ?? []).filter((t) => now - t < windowMs);
    if (recent.length >= limit) {
      hits.set(key, recent);
      return true;
    }
    recent.push(now);
    hits.set(key, recent);
    return false;
  };
}

// ------------------------------------------------------------------ what the model is told

export const FILL_TOOL_NAME = "fill_date_request";

export function fillTool(rooms: readonly Room[]) {
  return {
    name: FILL_TOOL_NAME,
    description:
      "Fill in the arrival date, the number of nights and the room on the date request form on the page. Call it as soon as the guest has given all three, and again whenever one of them changes. It does not reserve anything and it cannot check availability.",
    input_schema: {
      type: "object" as const,
      properties: {
        arrive: {
          type: "string",
          description: "Arrival date as YYYY-MM-DD, worked out from TODAY.",
        },
        nights: {
          type: "integer",
          description: `Number of nights, 1 to ${LIMITS.maxNights}.`,
        },
        room: {
          type: "string",
          enum: rooms.map((r) => r.key),
          description: "The room's form value.",
        },
      },
      required: ["arrive", "nights", "room"],
    },
  };
}

/** The part of the system prompt that never changes between requests, so it can be cached. */
export function systemPrompt(
  knowledge: string,
  rooms: readonly Room[],
  phone: string,
): string {
  return `You are the assistant on the website of The Meraki Inn, a five room inn in Galveston's East End Historic District. You answer in the inn's voice: warm, plain and unhurried, like the person who answers the inn's phone and knows every room. Never corporate, never bubbly, never a salesperson.

WHAT YOU KNOW
Everything you know about the inn and the island is under THE INN'S OWN PAGES below. It is the text of the inn's website. Answer only from it. If the answer is not there, say plainly that you do not know and give the phone number, ${phone}.

YOUR TWO JOBS
1. Answer questions about the rooms, breakfast, rates, tax, policies, the house, the island, cruise parking, Dickens on The Strand and hurricane season.
2. Help a guest ask for dates. For that you need three things: the arrival date, the number of nights, and the room. Ask for whatever is missing, one or two things at a time, the way a person on the phone would. If the guest is unsure which room, ask what the trip is for and suggest one from the pages.
When you have all three, call the ${FILL_TOOL_NAME} tool and write nothing else in that reply. The website writes the confirmation itself, with the exact total. Call the tool again whenever the guest changes the date, the nights or the room.

RULES
- You cannot see availability and you cannot reserve a room. The tool only fills in the date request form on the page, and the innkeeper confirms by email the same day. Never say a room is available, booked, held or confirmed.
- Never ask for a name, an email address, a phone number or a card number. The form on the page takes the name and the email. A card is only ever taken by phone. If a guest starts to give any of those, ask them kindly to keep it out of the chat.
- Hold to the inn's policies before you call the tool. A stay that includes a Friday or Saturday night is two nights or more. Dickens on The Strand weekend (December 4 to 6, 2026) and both Mardi Gras weekends (January 29 to 31 and February 5 to 7, 2027) are three nights or more. Children under 12 stay only in The Darkroom. Every room sleeps two, and The Darkroom can take a third guest on a rollaway bed. No pets. If a request breaks one of these, say so kindly and offer what would work.
- The form takes one to seven nights and one room. For a longer stay, for more than one room, or for anything the pages do not cover, ask the guest to call ${phone}.
- Work out every date from TODAY, given at the end. Say dates back in words with the weekday, for example "Friday, October 9".
- For prices, read the PRICE TABLE below. Do not do your own arithmetic.
- Only discuss the inn and a visit to Galveston as the pages cover it. For anything else, say warmly that you only know the inn, and steer back.
- Never invent rooms, prices, people, policies, events or facts that are not in the pages. That includes small talk: say nothing about the weather, the crowds, the season or what a place is like unless the pages say it.
- If asked whether this is real, whether you are a person or an AI, or whether a request was sent: say plainly that this website is a demonstration built by Meraki is Love, that you are an AI assistant, that The Meraki Inn is fictional, and that nothing is sent or reserved. Be direct about it.
- Keep replies short: two or three sentences in one paragraph, and one question at a time. Plain text only: no lists, no headings, no markdown, no emoji. Never use a dash as punctuation. Use commas and periods.

PRICE TABLE
Sample rates. Tax is 15 percent: 6 percent state and 9 percent city.
${priceTable(rooms)}

THE INN'S OWN PAGES
${knowledge}`;
}

/** True when a message holds an email address, which belongs in the form and not in the chat. */
export function mentionsEmail(text: string): boolean {
  return /[^\s@<>()]+@[^\s@<>()]+\.[a-z]{2,}/i.test(text);
}

export const KEEP_OUT_NOTE =
  "One more thing: please type your name and email into the form itself, and keep them out of the chat.";

/** The part that changes: the date, decided by the server. */
export function todayLine(today: string): string {
  return `TODAY is ${sayDay(today, "0000")} (${today}) in Galveston.`;
}

/** House style for anything the model writes: no dashes as punctuation. */
export function tidyReply(text: string): string {
  return text
    .replace(/\s*[\u2014\u2013]\s*/g, ", ")
    .replace(/[*_#`]+/g, "")
    .trim();
}
