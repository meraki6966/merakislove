import Image from "next/image";
import TiltCard from "@/components/TiltCard";
import Tag from "@/components/Tag";
import type { Project } from "@/lib/projects";

/**
 * Project card built on the TiltCard interaction.
 *
 * The cover is the real artwork from /public/covers, served through
 * next/image (fill + object-cover so any source aspect crops into the 16:10
 * frame). coverBg shows while the image loads, and a dark scrim keeps the
 * overlaid type/year and project name legible over any image.
 */
export default function ProjectCard({ project }: { project: Project }) {
  return (
    <TiltCard glow={`${project.glow}55`} className="group flex h-full flex-col bg-navy">
      {/* Cover */}
      <div
        className="relative flex aspect-[16/10] flex-col justify-between overflow-hidden rounded-t-xl p-6"
        style={{ backgroundColor: project.coverBg }}
      >
        <Image
          src={project.cover}
          alt={`${project.name} cover`}
          fill
          sizes="(min-width: 1024px) 360px, (min-width: 768px) 45vw, 92vw"
          className="object-cover"
        />
        {/* Scrim for overlay-text legibility */}
        <div
          aria-hidden
          className="absolute inset-0 bg-gradient-to-t from-void/90 via-void/20 to-void/60"
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
