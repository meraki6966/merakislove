import type { MetadataRoute } from "next";

const baseUrl = "https://merakislove.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    "",
    "/work",
    "/packages",
    "/packages/review",
    "/packages/bip",
    "/packages/custom",
    "/packages/starter-sites",
    "/packages/presence-first-web-design",
    // The one demo that is a main page: indexed, in the sitemap, and tagged.
    // The other demos are noindex samples and stay out.
    "/demos/presence-first-example.html",
    "/start",
    "/demos",
    "/loop",
    "/cybersecurity",
    "/shadow-ai",
    "/about",
    "/contact",
    "/privacy",
  ];

  return routes.map((route) => ({
    url: `${baseUrl}${route}`,
    changeFrequency: "monthly",
    priority: route === "" ? 1 : 0.8,
  }));
}
