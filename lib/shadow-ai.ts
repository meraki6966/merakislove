// The Shadow AI self-assessment: ten questions, their scoring, and the plain
// words shown for each gap. Used by components/ShadowAiCheck.tsx and tested by
// scripts/tests/shadow-ai.test.mjs.
//
// Everything here runs in the visitor's browser. Nothing in this file or the
// component sends, stores or logs an answer, and the test fails if either one
// ever reaches for the network, browser storage, cookies or the address bar.
//
// Every claim in the copy is one that holds across tools and plans. No
// statistics, no named vendors, no promise of a result. The page calls itself
// a self-assessment because a questionnaire cannot measure what a team
// actually does.

export interface Option {
  label: string;
  /** 0 is the safest answer, 3 the most exposed. */
  points: number;
}

export interface Gap {
  title: string;
  why: string;
  first: string;
}

export interface Question {
  id: string;
  prompt: string;
  options: Option[];
  gap: Gap;
  /** Breaks ties between gaps with equal points. Lower comes first. */
  priority: number;
}

export const QUESTIONS: Question[] = [
  {
    id: "inventory",
    prompt: "Do you know which AI tools your team uses for work?",
    options: [
      { label: "Yes. We keep a written list and update it.", points: 0 },
      { label: "We know the main ones.", points: 1 },
      { label: "We'd be guessing.", points: 2 },
      { label: "We've never asked.", points: 3 },
    ],
    gap: {
      title: "Nobody has a list of the tools",
      why: "You can't set rules for tools you don't know about, and shadow AI is, by definition, the tools nobody chose for the business.",
      first: "Ask each person which AI tools they used for work this month, including browser extensions and phone apps. Write the list down.",
    },
    priority: 6,
  },
  {
    id: "accounts",
    prompt: "Are those tools on business accounts the company controls?",
    options: [
      { label: "Yes, every one.", points: 0 },
      { label: "Mostly, with a few personal accounts.", points: 1 },
      { label: "Mostly personal or free accounts.", points: 3 },
      { label: "I don't know.", points: 3 },
    ],
    gap: {
      title: "Work is happening in personal accounts",
      why: "Chats in a personal or free account belong to that account. You can't see them, set their data controls, or take them back when the person leaves.",
      first: "Pick the tools the business will pay for, and move the work onto business accounts you control.",
    },
    priority: 3,
  },
  {
    id: "policy",
    prompt: "Is there a written AI policy your staff have read?",
    options: [
      { label: "Yes, and everyone has signed it.", points: 0 },
      { label: "It's written, but not everyone has seen it.", points: 1 },
      { label: "We've talked about it. Nothing is written.", points: 2 },
      { label: "No.", points: 3 },
    ],
    gap: {
      title: "There are no written rules",
      why: "Without rules on paper, each person decides alone what's safe to paste, and nobody can point to what was agreed.",
      first: "Write one page: the approved tools, what never goes in, and who to ask when unsure. Have everyone sign it.",
    },
    priority: 5,
  },
  {
    id: "client-data",
    prompt: "Has anyone put client or customer information into an AI tool?",
    options: [
      { label: "No, and our rules say not to.", points: 0 },
      { label: "Not that I know of.", points: 1 },
      { label: "Probably.", points: 2 },
      { label: "Yes, it happens regularly.", points: 3 },
    ],
    gap: {
      title: "Client information is going into AI tools",
      why: "Names, files and account details pasted into a chat leave your systems. Depending on the tool and the plan, the provider may keep them, and some plans allow them to be used to train a model.",
      first: "Name what can never go into an AI tool, in plain words: client files, account numbers, health records. Put it in writing.",
    },
    priority: 1,
  },
  {
    id: "sensitive",
    prompt: "Does your business handle health, financial, legal or children's records?",
    options: [
      { label: "No.", points: 0 },
      { label: "A little.", points: 1 },
      { label: "Yes. It's a large part of our work.", points: 2 },
    ],
    gap: {
      title: "The records you hold raise the stakes",
      why: "Health, financial, legal and children's records come with rules about who may see them. Under HIPAA, for example, a vendor that receives patient information generally needs a business associate agreement first.",
      first: "Before any of those records go near an AI tool, check whether the tool offers the agreement your field requires, and get it signed.",
    },
    priority: 2,
  },
  {
    id: "data-terms",
    prompt: "Do you know whether your AI tools keep what's typed into them, or use it for training?",
    options: [
      { label: "Yes. We've checked the settings and terms for each tool.", points: 0 },
      { label: "For some of them.", points: 1 },
      { label: "No.", points: 3 },
    ],
    gap: {
      title: "Nobody has checked the data settings",
      why: "Free and personal AI plans often carry different data terms than business plans, including how long chats are kept and whether they can be used to train the provider's models.",
      first: "For each tool on your list, find the data and training settings, set them, and note the date you checked.",
    },
    priority: 4,
  },
  {
    id: "built-in",
    prompt: "Has anyone reviewed the AI features inside software you already pay for, like email, your CRM or accounting?",
    options: [
      { label: "Yes. We chose which ones to use and set them up.", points: 0 },
      { label: "Some are on. Nobody has reviewed them.", points: 2 },
      { label: "I didn't know they had AI features.", points: 3 },
    ],
    gap: {
      title: "AI features arrived inside tools you already use",
      why: "Email, CRM and accounting software keep adding AI features, and some arrive turned on. They can read the same client data the rest of the software holds.",
      first: "Open the admin settings in your three busiest tools and decide, feature by feature, what stays on.",
    },
    priority: 8,
  },
  {
    id: "notetakers",
    prompt: "Do AI note takers or meeting recorders join your client calls?",
    options: [
      { label: "No, or only when everyone on the call has agreed.", points: 0 },
      { label: "Sometimes, and we don't always ask.", points: 2 },
      { label: "I'm not sure what joins our calls.", points: 3 },
    ],
    gap: {
      title: "AI note takers are on client calls",
      why: "Note takers record and transcribe the whole call, and some join meetings on their own once they're connected to a calendar. Recording laws differ by state, and some require everyone on the call to agree.",
      first: "Decide when a note taker is allowed, and say so out loud at the start of every call where one is running.",
    },
    priority: 7,
  },
  {
    id: "offboarding",
    prompt: "When someone leaves, do you remove their access to AI tools and shared AI workspaces?",
    options: [
      { label: "Yes. It's on our offboarding checklist.", points: 0 },
      { label: "Sometimes.", points: 2 },
      { label: "No.", points: 3 },
    ],
    gap: {
      title: "AI access outlives the job",
      why: "Shared AI workspaces, connected apps and saved chats can stay open after someone leaves. Chats kept in a personal account leave with the person.",
      first: "Add AI tools to your offboarding checklist, next to email and passwords.",
    },
    priority: 10,
  },
  {
    id: "response",
    prompt: "If someone pasted sensitive client information into a chatbot today, what would happen next?",
    options: [
      { label: "We have a plan, and staff know to tell us right away.", points: 0 },
      { label: "I'd hope they would tell me.", points: 2 },
      { label: "Nothing. We have no plan.", points: 3 },
    ],
    gap: {
      title: "There's no plan for a slip",
      why: "Mistakes happen on every team. How quickly you hear about one, and whether anyone knows what to do next, decides how far it goes.",
      first: "Write down who staff tell, what gets checked in the tool, and who decides whether a client needs to be told.",
    },
    priority: 9,
  },
];

export const MAX_SCORE = QUESTIONS.reduce(
  (sum, q) => sum + Math.max(...q.options.map((o) => o.points)),
  0,
);

export interface Band {
  /** Lowest score in the band, inclusive. */
  from: number;
  label: string;
  summary: string;
}

/** Ordered from the lowest score up. */
export const BANDS: Band[] = [
  {
    from: 0,
    label: "Mostly covered",
    summary:
      "By your answers, your team knows its tools and works inside rules you've set. Keep the list and the policy current as the tools change.",
  },
  {
    from: 8,
    label: "Gaps to close",
    summary:
      "By your answers, some of the basics are in place and a few gaps are open. The ones below are where I'd start.",
  },
  {
    from: 17,
    label: "Wide open",
    summary:
      "By your answers, most of the AI use on your team is happening without rules or records. The gaps below are where I'd start.",
  },
];

/** Question id mapped to the index of the chosen option. */
export type Answers = Record<string, number>;

function pointsFor(q: Question, answers: Answers): number | null {
  const i = answers[q.id];
  if (i === undefined || i === null) return null;
  const option = q.options[i];
  return option ? option.points : null;
}

export function answeredCount(answers: Answers): number {
  return QUESTIONS.filter((q) => pointsFor(q, answers) !== null).length;
}

export function isComplete(answers: Answers): boolean {
  return answeredCount(answers) === QUESTIONS.length;
}

export function score(answers: Answers): number {
  return QUESTIONS.reduce((sum, q) => sum + (pointsFor(q, answers) ?? 0), 0);
}

export function bandFor(total: number): Band {
  let band = BANDS[0];
  for (const b of BANDS) if (total >= b.from) band = b;
  return band;
}

/** The most exposed option a question offers is worth this many points. */
export const WORST = 3;

/**
 * The band for a full set of answers. A low total can hide one serious answer,
 * such as client data going into AI tools regularly, so any answer at WORST
 * keeps the result out of the lowest band. The sensitive records question
 * tops out at 2 on purpose: holding those records is context, not a lapse.
 */
export function resultBand(answers: Answers): Band {
  const band = bandFor(score(answers));
  const anyWorst = QUESTIONS.some((q) => pointsFor(q, answers) === WORST);
  return band === BANDS[0] && anyWorst ? BANDS[1] : band;
}

/**
 * The biggest gaps, most points first, ties broken by priority. A question
 * answered with its safest option is never a gap.
 */
export function topGaps(answers: Answers, limit = 3): Question[] {
  return QUESTIONS.map((q) => ({ q, points: pointsFor(q, answers) ?? 0 }))
    .filter((x) => x.points > 0)
    .sort((a, b) => b.points - a.points || a.q.priority - b.q.priority)
    .slice(0, limit)
    .map((x) => x.q);
}
