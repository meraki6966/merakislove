"use client";

import { useEffect, useRef, useState } from "react";

const INTERACTIVE = "a, button, label, input, textarea, select, [data-cursor='hover']";

/**
 * Custom amber cursor: a precise dot that tracks the pointer exactly and a
 * larger ring that trails with light smoothing and swells over interactive
 * elements. Renders nothing on touch / coarse-pointer devices, where the
 * native cursor is left intact.
 */
export default function Cursor() {
  const dotRef = useRef<HTMLDivElement>(null);
  const ringRef = useRef<HTMLDivElement>(null);
  const hoveringRef = useRef(false);
  const [hovering, setHovering] = useState(false);

  useEffect(() => {
    // The cursor elements are hidden via CSS on coarse pointers; only wire
    // up tracking when there's a real, fine pointer to follow.
    const fine = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
    if (!fine) return;

    const mouse = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    const ring = { ...mouse };
    let raf = 0;

    const onMove = (e: MouseEvent) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      if (dotRef.current) {
        dotRef.current.style.transform = `translate3d(${mouse.x}px, ${mouse.y}px, 0) translate(-50%, -50%)`;
      }
      const target = e.target as Element | null;
      const isInteractive = !!target?.closest?.(INTERACTIVE);
      if (isInteractive !== hoveringRef.current) {
        hoveringRef.current = isInteractive;
        setHovering(isInteractive);
      }
    };

    const loop = () => {
      // Light lerp — trails the dot without overshoot. No spring.
      ring.x += (mouse.x - ring.x) * 0.18;
      ring.y += (mouse.y - ring.y) * 0.18;
      if (ringRef.current) {
        ringRef.current.style.transform = `translate3d(${ring.x}px, ${ring.y}px, 0) translate(-50%, -50%)`;
      }
      raf = requestAnimationFrame(loop);
    };

    window.addEventListener("mousemove", onMove);
    raf = requestAnimationFrame(loop);
    return () => {
      window.removeEventListener("mousemove", onMove);
      cancelAnimationFrame(raf);
    };
  }, []);

  return (
    <>
      <div
        ref={dotRef}
        aria-hidden
        className="cursor-el pointer-events-none fixed left-0 top-0 z-[100] h-1.5 w-1.5 rounded-full bg-amber"
      />
      <div
        ref={ringRef}
        aria-hidden
        className={`cursor-el pointer-events-none fixed left-0 top-0 z-[100] rounded-full border border-amber transition-[width,height,opacity] duration-300 ease-out ${
          hovering ? "h-11 w-11 opacity-100" : "h-8 w-8 opacity-50"
        }`}
      />
    </>
  );
}
