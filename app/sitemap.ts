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
    "/packages/presence-first-web-design",
    "/start",
    "/demos",
    "/loop",
    "/cybersecurity",
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
