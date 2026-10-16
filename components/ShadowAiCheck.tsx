"use client";

import Link from "next/link";
import { useEffect, useRef, useState } from "react";
import {
  MAX_SCORE,
  QUESTIONS,
  answeredCount,
  isComplete,
  resultBand,
  score,
  topGaps,
  type Answers,
} from "@/lib/shadow-ai";
import { calendly } from "@/lib/site";

/**
 * The Shadow AI self-assessment.
 *
 * Answers live in this component's state and nowhere else. There is no form
 * element (so Google Analytics' form tracking has nothing to see), no request,
 * no browser storage, and no change to the address bar. Closing the tab is a
 * full reset. scripts/tests/shadow-ai.test.mjs fails if any of that changes.
 */
export default function ShadowAiCheck() {
  const [answers, setAnswers] = useState<Answers>({});
  const [showResult, setShowResult] = useState(false);
  const resultHeading = useRef<HTMLHeadingElement>(null);
  const resultSection = useRef<HTMLElement>(null);
  const questionsTop = useRef<HTMLOListElement>(null);

  const answered = answeredCount(answers);
  const complete = isComplete(answers);
  const total = score(answers);
  const band = resultBand(answers);
  const gaps = topGaps(answers);

  // Bring the whole result up under the nav, then move focus to its heading
  // so a screen reader starts reading there.
  useEffect(() => {
    if (!showResult) return;
    resultSection.current?.scrollIntoView({ block: "start" });
    resultHeading.current?.focus({ preventScroll: true });
  }, [showResult]);

  function choose(id: string, index: number) {
    setAnswers((prev) => ({ ...prev, [id]: index }));
  }

  function startOver() {
    setAnswers({});
    setShowResult(false);
    const first = questionsTop.current?.querySelector<HTMLInputElement>("input");
    first?.focus();
  }

  return (
    <div>
      <ol ref={questionsTop} className="flex flex-col gap-12">
        {QUESTIONS.map((q, qi) => (
          <li key={q.id}>
            <fieldset>
              <legend className="mb-5 flex gap-4">
                <span className="pt-1.5 font-mono text-xs tracking-[0.18em] text-amber">
                  {String(qi + 1).padStart(2, "0")}
                </span>
                <span className="font-display text-2xl font-light leading-snug text-smoke sm:text-[1.7rem]">
                  {q.prompt}
                </span>
              </legend>
              <div className="flex flex-col gap-2.5 sm:pl-10">
                {q.options.map((option, oi) => {
                  const inputId = `shadow-ai-${q.id}-${oi}`;
                  return (
                    <label
                      key={option.label}
                      htmlFor={inputId}
                      className="flex cursor-pointer items-start gap-3 rounded-lg border border-border-mid bg-navy/40 px-4 py-3 font-body text-base leading-snug text-smoke-dim transition-colors duration-200 hover:border-smoke-dim has-[:checked]:border-amber has-[:checked]:bg-amber-dim has-[:checked]:text-smoke has-[:focus-visible]:outline has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-offset-2 has-[:focus-visible]:outline-amber"
                    >
                      <input
                        id={inputId}
                        type="radio"
                        name={`shadow-ai-${q.id}`}
                        autoComplete="off"
                        className="mt-1 h-4 w-4 shrink-0 accent-amber focus:outline-none"
                        checked={answers[q.id] === oi}
                        onChange={() => choose(q.id, oi)}
                      />
                      <span>{option.label}</span>
                    </label>
                  );
                })}
              </div>
            </fieldset>
          </li>
        ))}
      </ol>

      <div className="mt-14 flex flex-col gap-4 border-t border-border-mid pt-10 sm:flex-row sm:items-center sm:justify-between">
        <p id="shadow-ai-progress" className="font-mono text-xs uppercase tracking-[0.18em] text-smoke-dim">
          {answered} of {QUESTIONS.length} answered
        </p>
        <button
          type="button"
          onClick={() => setShowResult(true)}
          disabled={!complete}
          aria-describedby="shadow-ai-progress"
          className="inline-flex items-center justify-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02] disabled:cursor-not-allowed disabled:opacity-40 disabled:hover:scale-100"
        >
          See my result
        </button>
      </div>

      {showResult && complete ? (
        <section
          ref={resultSection}
          aria-labelledby="shadow-ai-result"
          className="mt-14 scroll-mt-28 rounded-2xl border border-border-mid bg-navy/40 p-7 sm:p-10"
        >
          <p className="font-mono text-xs uppercase tracking-[0.25em] text-amber">
            Your result
          </p>
          <h2
            id="shadow-ai-result"
            ref={resultHeading}
            tabIndex={-1}
            className="mt-4 font-display text-4xl font-light text-smoke outline-none sm:text-5xl"
          >
            {band.label}
          </h2>
          <p className="mt-3 font-mono text-sm tracking-[0.12em] text-smoke-dim">
            {total} of {MAX_SCORE} points. Higher means more exposed.
          </p>
          <p className="mt-6 max-w-2xl font-body text-base leading-relaxed text-smoke">
            {band.summary}
          </p>

          {gaps.length > 0 ? (
            <ol className="mt-10 flex flex-col gap-8">
              {gaps.map((q, i) => (
                <li key={q.id} className="border-l-2 border-amber pl-6">
                  <h3 className="font-display text-2xl font-light text-smoke">
                    <span className="mr-3 font-mono text-xs tracking-[0.18em] text-amber">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    {q.gap.title}
                  </h3>
                  <p className="mt-3 max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
                    {q.gap.why}
                  </p>
                  <p className="mt-3 max-w-2xl font-body text-base leading-relaxed text-smoke">
                    <span className="font-mono text-xs uppercase tracking-[0.16em] text-amber">
                      First step:
                    </span>{" "}
                    {q.gap.first}
                  </p>
                </li>
              ))}
            </ol>
          ) : (
            <p className="mt-8 max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
              By your answers, there are no open gaps. Run through it again when your team adds a new tool.
            </p>
          )}

          <div className="mt-12 flex flex-col gap-4 sm:flex-row sm:items-center">
            <a
              href={calendly.newProject}
              target="_blank"
              rel="noopener noreferrer"
              className="group inline-flex items-center justify-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Book a call about your result
              <span aria-hidden className="transition-transform duration-300 group-hover:translate-x-1">
                →
              </span>
            </a>
            <button
              type="button"
              onClick={startOver}
              className="inline-flex items-center justify-center gap-3 rounded-full border border-border-mid px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-smoke transition-colors duration-300 hover:border-amber hover:text-amber"
            >
              Start over
            </button>
          </div>
          <p className="mt-5 max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
            Bring the gaps above to the call. Nothing on this page is sent to me or to Calendly, so you decide what to share.
          </p>
          <p className="mt-4 max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
            If your business also runs its own AI feature, like a chatbot on your site or a client portal, the{" "}
            <Link href="/packages/review" className="text-amber underline underline-offset-4 hover:text-smoke">
              Security and AI Review
            </Link>{" "}
            looks at that directly.
          </p>
          <p className="mt-8 max-w-2xl border-t border-border-mid pt-6 font-body text-sm leading-relaxed text-smoke-dim">
            This is a self-assessment. It reflects your answers and can&apos;t see what happens on your team&apos;s devices. It isn&apos;t a compliance audit or legal advice.
          </p>
        </section>
      ) : null}
    </div>
  );
}
