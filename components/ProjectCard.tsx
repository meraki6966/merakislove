import TiltCard from "@/components/TiltCard";
import Tag from "@/components/Tag";
import type { Project } from "@/lib/projects";

/**
 * Project card built on the TiltCard interaction.
 *
 * Cover treatment is a placeholder until the Figma exports land (brief
 * §Known Issues #2): a dark base color, a soft radial wash in the project's
 * glow color, and the project name as display text. Swap the cover block for
 * a next/image once the real artwork is ready.
 */
export default function ProjectCard({ project }: { project: Project }) {
  return (
    <TiltCard glow={`${project.glow}55`} className="group flex h-full flex-col bg-navy">
      {/* Placeholder cover */}
      <div
        className="relative flex aspect-[16/10] flex-col justify-between overflow-hidden rounded-t-xl p-6"
        style={{ backgroundColor: project.coverBg }}
      >
        <div
          aria-hidden
          className="absolute inset-0"
          style={{
            background: `radial-gradient(120% 90% at 25% 15%, ${project.glow}40, transparent 65%)`,
          }}
        />
        <div className="relative flex items-center justify-between font-mono text-[0.65rem] uppercase tracking-[0.2em] text-smoke-dim">
          <span>{project.type}</span>
          <span>{project.year}</span>
        </div>
        <h3 className="relative font-display text-3xl font-light leading-tight text-smoke sm:text-4xl">
          {project.name}
        </h3>
      </div>

      {/* Body */}
      <div className="flex flex-1 flex-col gap-5 p-6">
        <p className="font-body text-sm leading-relaxed text-smoke-dim">
          {project.description}
        </p>
        <div className="mt-auto flex flex-wrap gap-2">
          {project.stack.map((tech) => (
            <Tag key={tech}>{tech}</Tag>
          ))}
        </div>
        <p className="border-t border-border pt-4 font-mono text-xs uppercase tracking-[0.18em] text-amber">
          {project.stat}
        </p>
      </div>
    </TiltCard>
  );
}
