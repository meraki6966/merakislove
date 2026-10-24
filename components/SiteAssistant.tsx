import Script from "next/script";

/**
 * The site assistant: the Meraki BIP chat widget (merakibip.com), the same
 * document-trained assistant sold to BIP clients, answering from the
 * knowledge base of one BIP tenant.
 *
 * What it does on the wire: the script below draws a chat button and, when a
 * visitor sends a message, posts it to https://www.merakibip.com/api/rag/query.
 * That route embeds the question (Voyage AI), retrieves only this tenant's
 * documents, and asks Anthropic for an answer. It does not store the message.
 * The privacy page says the same; docs/third-party-services.md lists the
 * processors. The CSP in next.config.ts allows exactly this origin in
 * script-src and connect-src, and nothing else was widened for it.
 *
 * Loaded at idle time so it never competes with the page itself.
 *
 * Off until NEXT_PUBLIC_SITE_ASSISTANT is "on" in the Vercel project. On 23
 * October 2026 the meraki-is-love tenant still answered from merakibip.com
 * documents (asked about a bakery website, it suggested Wix), so the widget
 * stays dark until the merakislove.com knowledge is uploaded to the tenant.
 * The privacy page shows its section under the same switch.
 */
export const SITE_ASSISTANT_ON = process.env.NEXT_PUBLIC_SITE_ASSISTANT === "on";
export const BIP_ORIGIN = "https://www.merakibip.com";
export const BIP_TENANT = "meraki-is-love";

export default function SiteAssistant() {
  if (!SITE_ASSISTANT_ON) return null;
  return (
    <Script
      src={`${BIP_ORIGIN}/api/rag/widget/${BIP_TENANT}`}
      strategy="lazyOnload"
    />
  );
}
