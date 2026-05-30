import type { ReactNode } from "react";

/** Stack tag chip — mono, hairline border, used for tech stacks and meta labels. */
export default function Tag({ children }: { children: ReactNode }) {
  return (
    <span className="inline-flex items-center rounded-full border border-border-mid bg-amber-dim px-3 py-1 font-mono text-[0.7rem] uppercase tracking-wider text-smoke-dim">
      {children}
    </span>
  );
}
