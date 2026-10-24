import type { ReactNode } from "react";

/** A small sentence-case pill for stacks and meta labels. */
export default function Tag({ children }: { children: ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-full bg-amber-dim px-3.5 py-1.5 font-sans text-sm font-medium text-smoke-dim ring-1 ring-border-mid">
      {children}
    </span>
  );
}
