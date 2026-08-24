import Anthropic from "@anthropic-ai/sdk";
import { NextResponse } from "next/server";

/**
 * Conversational booking assistant for the Corner Table demo
 * (/demos/restaurant).
 *
 * The demo is a public, unauthenticated page, so this route is the money-
 * spending surface of the whole site. Everything below the system prompt is
 * there to bound that: a per-IP rate limit, a cap on how long a single
 * message can be, and a cap on how many turns one conversation can run.
 *
 * Nothing is persisted. The conversation lives in the browser tab and is
 * replayed to this route on each turn; when the tab closes it is gone.
 */

/**
 * Sonnet 4.6, not Opus 5. This is a four-slot booking conversation, not
 * reasoning work, and it is the same model Meraki BIP runs in production for
 * comparable conversational tasks.
 *
 * Note the family difference: on Opus 5, omitting `thinking` still runs
 * adaptive thinking. On Sonnet 4.6, omitting it means no thinking at all.
 * That is the behavior wanted here, and it is why the reply gets the whole
 * token budget instead of sharing it with a reasoning pass.
 */
const MODEL = "claude-sonnet-4-6";

/** Deliberately small: replies are a sentence or three, never an essay. */
const MAX_TOKENS = 500;

/** Longest single visitor message we will forward, in characters. */
const MAX_MESSAGE_CHARS = 1000;

/** Most messages (visitor + assistant) we will carry in one conversation. */
const MAX_HISTORY_MESSAGES = 24;

const RATE_LIMIT = 15; // requests
const RATE_WINDOW_MS = 60 * 1000; // per minute, per IP

/**
 * In-memory, so it is per serverless instance rather than global. That makes
 * it a speed bump against casual abuse, not a hard quota. If this demo ever
 * draws real traffic, move the counter to Redis or Vercel's rate limiter.
 */
const hits = new Map<string, number[]>();

function clientIp(req: Request): string {
  const forwarded = req.headers.get("x-forwarded-for");
  if (forwarded) return forwarded.split(",")[0]?.trim() || "unknown";
  return req.headers.get("x-real-ip")?.trim() || "unknown";
}

function isRateLimited(ip: string): boolean {
  const now = Date.now();
  const recent = (hits.get(ip) ?? []).filter((t) => now - t < RATE_WINDOW_MS);
  if (recent.length >= RATE_LIMIT) {
    hits.set(ip, recent);
    return true;
  }
  recent.push(now);
  hits.set(ip, recent);
  return false;
}

/**
 * Everything the assistant is allowed to know. Kept in sync by hand with
 * public/demos/restaurant/index.html: if the menu or the hours change there,
 * change them here too, or the assistant will confidently quote a dish the
 * page does not list.
 */
const SYSTEM_PROMPT = `You are the booking assistant for The Corner Table, a neighborhood restaurant. You answer in the restaurant's voice: warm, casual, unhurried, like a person who works there and likes the place. Never corporate, never bubbly, never a salesperson.

ABOUT THE RESTAURANT
The Corner Table sits on the corner lot at 4th and Maple. Rosa Delgado opened it in 2016 after fifteen years cooking in other people's kitchens. Regulars know the servers by name and the specials board actually changes. Nothing here is trying to impress anyone. It is trying to feed people well.

HOURS
Tuesday through Sunday, 5pm to 10pm. Closed Mondays.

MENU
Starters: Cast Iron Cornbread $8 (whipped honey butter, flaked sea salt); Charred Broccolini $11 (Calabrian chili, shaved parmesan, lemon); Fried Green Tomatoes $10 (buttermilk dressing, pickled onion); Soup of the Day $7 (changes with the season).
Mains: Whole Roasted Chicken $22 (herb butter, charred lemon, market greens); Braised Short Rib $26 (root vegetable mash, red wine jus); Pan-Seared Trout $24 (brown butter, capers, roasted fingerlings); Corner Table Burger $16 (aged cheddar, caramelized onion, house pickles, brioche bun); Grilled Vegetable Plate $18 (seasonal vegetables, romesco, toasted grain).
Sides: Garlic Mashed Potatoes $6; Market Greens $6 (lemon vinaigrette); Hand-Cut Fries $6 (rosemary salt).
Dessert: Buttermilk Pie $8 (whipped cream, candied lemon zest); Chocolate Skillet Cookie $9 (vanilla bean ice cream).

YOUR JOB
Have a natural conversation and gather four things: the date, the time, the party size, and a name for the table. Ask for whatever is still missing, one or two things at a time, the way a person on the phone would. Do not interrogate and do not present a form.

When you have all four, confirm them back in one warm, plain sentence, for example: "You're set for Friday at 7, party of four, under Adam." Then stop. Do not ask follow-up questions after confirming unless the visitor asks for a change.

RULES
- Only Tuesday through Sunday, 5pm to 10pm. If someone asks for a Monday, say warmly that the kitchen is dark on Mondays and offer the nearest open evening. If someone asks for a time outside 5 to 10, offer the closest time that works.
- For parties of seven or more, say you would rather have someone call so they can set the room up properly.
- Only discuss this restaurant: the menu, the hours, the location, and booking a table. If asked about anything else, say warmly that you only know about The Corner Table and steer back.
- Never invent dishes, prices, staff, or policies that are not written above. If you do not know something, say so plainly and suggest calling.
- If the visitor asks whether this is real, whether you are an AI, or whether the booking is actually made: tell them plainly that this is a demonstration, that you are an AI assistant, and that no reservation is recorded anywhere. Do not pretend otherwise. Be direct about it rather than coy.
- Keep replies short. Two or three sentences is usually plenty.`;

const client = new Anthropic();

interface IncomingMessage {
  role: "user" | "assistant";
  content: string;
}

function isValidMessage(m: unknown): m is IncomingMessage {
  if (typeof m !== "object" || m === null) return false;
  const { role, content } = m as Record<string, unknown>;
  return (
    (role === "user" || role === "assistant") &&
    typeof content === "string" &&
    content.trim().length > 0
  );
}

export async function POST(req: Request) {
  // A key that is present but empty is the same as no key at all, and it is
  // the more likely failure: Vercel's sensitive variables pull down blank.
  if (!process.env.ANTHROPIC_API_KEY?.trim()) {
    return NextResponse.json(
      {
        error:
          "The booking assistant is not configured right now. Please try again later.",
      },
      { status: 503 },
    );
  }

  if (isRateLimited(clientIp(req))) {
    return NextResponse.json(
      { error: "That's a lot of questions at once. Give it a minute and try again." },
      { status: 429 },
    );
  }

  const body = await req.json().catch(() => null);
  const raw = (body as { messages?: unknown } | null)?.messages;

  if (!Array.isArray(raw) || raw.length === 0 || !raw.every(isValidMessage)) {
    return NextResponse.json(
      { error: "Expected a non-empty messages array." },
      { status: 400 },
    );
  }

  if (raw.length > MAX_HISTORY_MESSAGES) {
    return NextResponse.json(
      { error: "This conversation has run long. Start a new one to keep going." },
      { status: 400 },
    );
  }

  const last = raw[raw.length - 1];
  if (last.role !== "user") {
    return NextResponse.json(
      { error: "The last message must be from the visitor." },
      { status: 400 },
    );
  }
  if (last.content.length > MAX_MESSAGE_CHARS) {
    return NextResponse.json(
      { error: `Please keep it under ${MAX_MESSAGE_CHARS} characters.` },
      { status: 400 },
    );
  }

  const messages: Anthropic.MessageParam[] = raw.map((m) => ({
    role: m.role,
    content: m.content,
  }));

  try {
    // `thinking` is deliberately omitted: on Sonnet 4.6 that means no
    // reasoning pass, so the whole budget goes to the visible reply.
    const response = await client.messages.create({
      model: MODEL,
      max_tokens: MAX_TOKENS,
      system: SYSTEM_PROMPT,
      output_config: { effort: "low" },
      messages,
    });

    // This endpoint spends money on a public page, so every call reports what
    // it cost and whether it came near the ceiling. `stop_reason` is the part
    // that matters: "max_tokens" here would mean a reply was cut off.
    console.log(
      `[reservation-chat] in=${response.usage.input_tokens} out=${response.usage.output_tokens}/${MAX_TOKENS} stop=${response.stop_reason} model=${response.model}`,
    );

    const reply = response.content
      .filter((block): block is Anthropic.TextBlock => block.type === "text")
      .map((block) => block.text)
      .join("")
      .trim();

    if (response.stop_reason === "refusal") {
      return NextResponse.json(
        { error: "I can't help with that one. Ask me about a table instead." },
        { status: 200 },
      );
    }

    if (!reply) {
      return NextResponse.json(
        { error: "Sorry, I lost my train of thought there. Try that again?" },
        { status: 502 },
      );
    }

    return NextResponse.json({ reply });
  } catch (error) {
    // Most specific first. The visitor never sees provider detail; the server
    // log gets the message only, never the error object, because a thrown
    // client error can carry request context.
    if (error instanceof Anthropic.AuthenticationError) {
      console.error("[reservation-chat] auth rejected by Anthropic");
      return NextResponse.json(
        { error: "The booking assistant is not configured right now." },
        { status: 503 },
      );
    }
    if (error instanceof Anthropic.RateLimitError) {
      return NextResponse.json(
        { error: "The kitchen's a bit busy. Try again in a moment." },
        { status: 429 },
      );
    }
    if (error instanceof Anthropic.APIError) {
      console.error(`[reservation-chat] API error ${error.status}`);
      return NextResponse.json(
        { error: "Something went wrong on our end. Try again in a moment." },
        { status: 502 },
      );
    }
    console.error(
      "[reservation-chat] unexpected:",
      error instanceof Error ? error.message : "unknown",
    );
    return NextResponse.json(
      { error: "Something went wrong on our end. Try again in a moment." },
      { status: 500 },
    );
  }
}
