import type { MetadataRoute } from "next";

const baseUrl = "https://merakislove.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: "*",
        allow: "/",
        crawlDelay: 10,
      },
      // AI crawlers are welcome: being cited in AI answers is part of how
      // this studio gets found. Named explicitly so the choice is on record
      // per bot. Anthropic runs three (training, search, and fetches a user
      // asks for); "Anthropic" was never one of their agent names.
      {
        userAgent: [
          "GPTBot",
          "OAI-SearchBot",
          "ChatGPT-User",
          "ClaudeBot",
          "Claude-SearchBot",
          "Claude-User",
          "PerplexityBot",
          "Perplexity-User",
          "Google-Extended",
        ],
        allow: "/",
      },
    ],
    sitemap: `${baseUrl}/sitemap.xml`,
    host: baseUrl,
  };
}
