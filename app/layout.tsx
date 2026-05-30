import type { Metadata, Viewport } from "next";
import {
  Cormorant_Garamond,
  Space_Grotesk,
  JetBrains_Mono,
} from "next/font/google";
import "./globals.css";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import Cursor from "@/components/Cursor";
import GrainOverlay from "@/components/GrainOverlay";
import { ogBase } from "@/lib/site";

const cormorant = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["300", "400", "600", "700"],
  variable: "--font-cormorant",
  display: "swap",
});

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600"],
  variable: "--font-space-grotesk",
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  subsets: ["latin"],
  weight: ["400", "500"],
  variable: "--font-jetbrains-mono",
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
  themeColor: "#07090f",
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
      className={`${cormorant.variable} ${spaceGrotesk.variable} ${jetbrainsMono.variable}`}
    >
      <body className="custom-cursor-active min-h-screen bg-void font-body text-smoke">
        <GrainOverlay />
        <Cursor />
        <Nav />
        <main className="relative">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
