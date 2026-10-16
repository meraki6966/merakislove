import { NextResponse, type NextRequest } from "next/server";

import { makeNonce, pagePolicy } from "./lib/csp";

/**
 * A fresh nonce and a strict script policy for every page request. Next.js reads
 * the nonce from the request's Content-Security-Policy header while it renders
 * and puts it on its own scripts; app/layout.tsx reads x-nonce for the two
 * scripts the site writes itself. See lib/csp.ts.
 */
export function proxy(request: NextRequest) {
  const nonce = makeNonce();
  const policy = pagePolicy(nonce, process.env.NODE_ENV === "development");

  const requestHeaders = new Headers(request.headers);
  requestHeaders.set("x-nonce", nonce);
  requestHeaders.set("Content-Security-Policy", policy);

  const response = NextResponse.next({ request: { headers: requestHeaders } });
  response.headers.set("Content-Security-Policy", policy);
  return response;
}

export const config = {
  matcher: [
    {
      // Pages only. Not the API routes, Next's own files, the static demos under
      // /public/demos, or any path with a file extension (images, video, audio,
      // analytics.js, sitemap.xml, robots.txt). next.config.ts gives those theirs.
      source: "/((?!api|_next/static|_next/image|demos/|.*\\..*).*)",
      missing: [
        { type: "header", key: "next-router-prefetch" },
        { type: "header", key: "purpose", value: "prefetch" },
      ],
    },
  ],
};
