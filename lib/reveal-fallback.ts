/**
 * Keeps the site readable when its JavaScript never runs.
 *
 * ScrollReveal (components/ScrollReveal.tsx) renders its content with an
 * inline opacity:0 and lets the browser fade it in once the page's code is
 * running. If that code is turned off, blocked, or fails to load, the fade
 * never happens and most of the text stays invisible. Two guards close that:
 *
 *  - REVEAL_NOSCRIPT: a style that only browsers with JavaScript off apply.
 *  - REVEAL_FALLBACK_SCRIPT: a tiny inline script in the head. If the page's
 *    code hasn't started a few seconds after the page loads, it adds the same
 *    style. ScrollReveal sets window.__revealReady when it starts, so on a
 *    normal visit the script finds it and does nothing.
 *
 * The style uses !important because the hidden state is an inline style.
 * It only touches elements marked data-reveal, which only ScrollReveal sets.
 * scripts/tests/reduced-motion.test.mjs checks the pieces are in place.
 */
export const REVEAL_VISIBLE_CSS =
  "[data-reveal]{opacity:1!important;transform:none!important}";

export const REVEAL_NOSCRIPT = `<style>${REVEAL_VISIBLE_CSS}</style>`;

/** Seconds after the load event, and after the script first runs, before the fallback steps in. */
export const AFTER_LOAD_MS = 2500;
export const HARD_STOP_MS = 8000;

export const REVEAL_FALLBACK_SCRIPT = `(function(){var done=false;function show(){if(done||window.__revealReady)return;done=true;var s=document.createElement("style");s.setAttribute("data-reveal-fallback","");s.textContent=${JSON.stringify(
  REVEAL_VISIBLE_CSS,
)};document.head.appendChild(s);}window.addEventListener("load",function(){setTimeout(show,${AFTER_LOAD_MS})});setTimeout(show,${HARD_STOP_MS});})();`;
