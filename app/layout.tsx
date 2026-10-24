import type { Metadata, Viewport } from "next";
import { Archivo, Source_Serif_4 } from "next/font/google";
import "./globals.css";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import JsonLd from "@/components/JsonLd";
import SiteAssistant from "@/components/SiteAssistant";
import { ogBase } from "@/lib/site";

// Archivo is variable on weight and width. The width axis is what lets
// the headlines run wide and heavy (font-stretch in globals.css).
const archivo = Archivo({
  subsets: ["latin"],
  axes: ["wdth"],
  variable: "--font-archivo",
  display: "swap",
});

const sourceSerif = Source_Serif_4({
  subsets: ["latin"],
  variable: "--font-source-serif",
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL("https://merakislove.com"),
  title: {
    default: "Soulful Tech · Meraki is Love",
    template: "%s · Soulful Tech",
  },
  description:
    "Full-stack product studio. AI integration with a security posture, built with intention by Adam McClarin.",
  alternates: {
    canonical: "/",
  },
  keywords: [
    "product studio",
    "AI integration",
    "cybersecurity",
    "Next.js",
    "CISSP",
    "Meraki is Love",
    "Soulful Tech",
  ],
  authors: [{ name: "Adam McClarin" }],
  openGraph: {
    ...ogBase,
    title: "Soulful Tech · Meraki is Love",
    description:
      "Full-stack product studio. AI integration with a security posture, built with intention.",
    url: "https://merakislove.com",
  },
  // Card only — Twitter falls back to the per-page og:title/description.
  twitter: {
    card: "summary_large_image",
  },
};

export const viewport: Viewport = {
  themeColor: "#130b19",
  colorScheme: "dark",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${archivo.variable} ${sourceSerif.variable}`}
    >
      <head>
        {/* Google Analytics 4, self-hosted loader. It runs only on the
            production hosts, skips Global Privacy Control and noindex pages,
            and keeps Google signals off. See public/analytics.js. */}
        <script src="/analytics.js" async />
      </head>
      <body className="min-h-screen bg-void font-body text-smoke">
        <JsonLd />
        <Nav />
        <main className="relative">{children}</main>
        <Footer />
        <SiteAssistant />
      </body>
    </html>
  );
}
