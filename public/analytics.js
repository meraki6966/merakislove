/*
 * Google Analytics 4 loader for merakislove.com.
 *
 * Self-hosted so the page needs no inline script of its own. It only runs
 * when every one of these holds, and does nothing at all otherwise:
 *   1. The page is served from merakislove.com or www.merakislove.com.
 *      Vercel preview deploys, localhost and any copy of the site stay silent.
 *   2. The browser does not send Global Privacy Control.
 *   3. The page is not marked noindex (the 404 page, and anything hidden).
 * Google signals and ad personalization are switched off in the config call,
 * so Analytics collects page views and site interactions only.
 *
 * The 128 demo pages under /demos do not load this file. Their own privacy
 * pages promise no analytics. Tests in scripts/tests/analytics.test.mjs
 * enforce both sides.
 */
(function () {
  "use strict";

  var MEASUREMENT_ID = "G-CD61SSYP84";
  var ALLOWED_HOSTS = ["merakislove.com", "www.merakislove.com"];

  function run() {
    if (ALLOWED_HOSTS.indexOf(window.location.hostname) === -1) return;
    if (window.navigator && window.navigator.globalPrivacyControl === true) return;

    var robots = document.querySelector('meta[name="robots"]');
    if (robots && /noindex/i.test(robots.getAttribute("content") || "")) return;

    window.dataLayer = window.dataLayer || [];
    function gtag() {
      window.dataLayer.push(arguments);
    }
    window.gtag = gtag;

    gtag("js", new Date());
    gtag("set", {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
    });
    gtag("config", MEASUREMENT_ID, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false,
    });

    var tag = document.createElement("script");
    tag.async = true;
    tag.src = "https://www.googletagmanager.com/gtag/js?id=" + MEASUREMENT_ID;
    document.head.appendChild(tag);
  }

  // Read the robots tag only once the whole head has been parsed.
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run, { once: true });
  } else {
    run();
  }
})();
