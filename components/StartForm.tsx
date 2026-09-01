"use client";

import { useState } from "react";
import { email } from "@/lib/site";

/**
 * The write-instead alternative to booking a call.
 *
 * There is no form handler and no email vendor behind this on purpose. The
 * fields compose a mailto link, so the message goes straight from the
 * visitor's own mail client to the studio inbox. No subprocessor, no new
 * credential, and nothing about the visitor is stored or transmitted
 * anywhere in between.
 *
 * It has to be an anchor rather than a form action: the site's CSP sets
 * `form-action 'self'`, which would refuse a `mailto:` submission.
 */

const RUNS = [
  "Pastor",
  "Biller",
  "Advisor",
  "Firm",
  "Hospitality",
  "Other",
];

const NEEDS = ["Review", "BIP", "Site", "Product", "Not sure"];

const BUDGETS = ["$500 to $1.5k", "$7k", "$12k+", "Not sure"];

/** Keeps the composed link inside what mail clients reliably accept. */
const MAX_NOTES = 1200;

const FIELD_CLASS =
  "w-full rounded-lg border border-border-mid bg-navy/40 px-4 py-3 font-body text-sm text-smoke outline-none transition-colors duration-300 placeholder:text-muted focus:border-amber";

const LABEL_CLASS =
  "font-mono text-[0.7rem] uppercase tracking-[0.18em] text-smoke-dim";

export default function StartForm() {
  const [name, setName] = useState("");
  const [business, setBusiness] = useState("");
  const [runs, setRuns] = useState("");
  const [city, setCity] = useState("");
  const [need, setNeed] = useState("");
  const [budget, setBudget] = useState("");
  const [site, setSite] = useState("");
  const [notes, setNotes] = useState("");

  const ready = name.trim().length > 0;

  const body = [
    `Name: ${name}`,
    `Business name: ${business}`,
    `What I run: ${runs}`,
    `City: ${city}`,
    `What I think I need: ${need}`,
    `Budget band: ${budget}`,
    `Current site: ${site}`,
    "",
    "Anything to read first:",
    notes,
  ].join("\n");

  const href = `mailto:${email}?subject=${encodeURIComponent(
    name.trim() ? `New enquiry from ${name.trim()}` : "New enquiry",
  )}&body=${encodeURIComponent(body)}`;

  return (
    <div className="flex flex-col gap-6">
      <div className="grid gap-5 sm:grid-cols-2">
        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>Name</span>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            autoComplete="name"
            className={FIELD_CLASS}
          />
        </label>

        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>Business name</span>
          <input
            type="text"
            value={business}
            onChange={(e) => setBusiness(e.target.value)}
            autoComplete="organization"
            className={FIELD_CLASS}
          />
        </label>

        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>What you run</span>
          <select
            value={runs}
            onChange={(e) => setRuns(e.target.value)}
            className={FIELD_CLASS}
          >
            <option value="" className="bg-navy">
              Choose one
            </option>
            {RUNS.map((option) => (
              <option key={option} value={option} className="bg-navy">
                {option}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>City</span>
          <input
            type="text"
            value={city}
            onChange={(e) => setCity(e.target.value)}
            autoComplete="address-level2"
            className={FIELD_CLASS}
          />
        </label>

        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>What you think you need</span>
          <select
            value={need}
            onChange={(e) => setNeed(e.target.value)}
            className={FIELD_CLASS}
          >
            <option value="" className="bg-navy">
              Choose one
            </option>
            {NEEDS.map((option) => (
              <option key={option} value={option} className="bg-navy">
                {option}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-2">
          <span className={LABEL_CLASS}>Budget band</span>
          <select
            value={budget}
            onChange={(e) => setBudget(e.target.value)}
            className={FIELD_CLASS}
          >
            <option value="" className="bg-navy">
              Choose one
            </option>
            {BUDGETS.map((option) => (
              <option key={option} value={option} className="bg-navy">
                {option}
              </option>
            ))}
          </select>
        </label>

        <label className="flex flex-col gap-2 sm:col-span-2">
          <span className={LABEL_CLASS}>Link to current site</span>
          <input
            type="url"
            value={site}
            onChange={(e) => setSite(e.target.value)}
            inputMode="url"
            placeholder="https://"
            className={FIELD_CLASS}
          />
        </label>

        <label className="flex flex-col gap-2 sm:col-span-2">
          <span className={LABEL_CLASS}>
            Anything I should read before we talk
          </span>
          <textarea
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            rows={5}
            maxLength={MAX_NOTES}
            className={`${FIELD_CLASS} resize-y`}
          />
        </label>
      </div>

      <div className="flex flex-col gap-3">
        <a
          href={href}
          aria-disabled={!ready}
          tabIndex={ready ? undefined : -1}
          className={`group inline-flex w-fit items-center gap-3 rounded-full border border-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-amber transition-colors duration-300 hover:bg-amber! hover:text-void ${
            ready ? "" : "pointer-events-none opacity-40"
          }`}
        >
          Send
          <span className="transition-transform duration-300 group-hover:translate-x-1">
            →
          </span>
        </a>
        <p className="font-body text-sm leading-relaxed text-smoke-dim">
          {ready
            ? "I read these. You get a direct reply, not a sequence."
            : "Add your name and the Send button opens your mail app with the rest filled in."}
        </p>
      </div>
    </div>
  );
}
