/** 40px amber line divider. Centered by default; pass align="left" for a left-anchored rule. */
export default function SectionDivider({
  align = "center",
}: {
  align?: "center" | "left";
}) {
  return (
    <div
      aria-hidden
      className={align === "center" ? "flex justify-center" : "flex justify-start"}
    >
      <span className="block h-px w-10 bg-amber" />
    </div>
  );
}
