/**
 * The 40px amber rule under headings was dropped in the 2026-10 redesign;
 * headings carry the hierarchy on their own now. Kept as a no-op so the
 * call sites can come out page by page.
 */
export default function SectionDivider(_props: { align?: "center" | "left" }) {
  return null;
}
