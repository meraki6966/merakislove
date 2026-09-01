export interface FaqItem {
  question: string;
  answer: string;
}

/**
 * Accordion built on native details/summary. No client JavaScript, no new
 * dependency, keyboard and screen-reader accessible for free, and nothing
 * for the Content-Security-Policy to object to. The marker is suppressed and
 * replaced with a rotating plus rule so it matches the site's hairline
 * language rather than the browser's triangle.
 */
export default function Faq({ items }: { items: FaqItem[] }) {
  return (
    <div className="flex flex-col overflow-hidden rounded-xl border border-border">
      {items.map((item) => (
        <details
          key={item.question}
          className="group border-b border-border last:border-b-0 [&_summary::-webkit-details-marker]:hidden"
        >
          <summary className="flex cursor-pointer list-none items-center justify-between gap-6 px-6 py-5 font-body text-base text-smoke transition-colors duration-300 hover:bg-navy/40 sm:px-8">
            {item.question}
            <span
              aria-hidden
              className="relative h-3 w-3 shrink-0 text-amber"
            >
              <span className="absolute left-0 top-1/2 h-px w-3 -translate-y-1/2 bg-amber" />
              <span className="absolute left-1/2 top-0 h-3 w-px -translate-x-1/2 bg-amber transition-transform duration-300 group-open:rotate-90" />
            </span>
          </summary>
          <p className="px-6 pb-6 font-body text-sm leading-relaxed text-smoke-dim sm:px-8">
            {item.answer}
          </p>
        </details>
      ))}
    </div>
  );
}
