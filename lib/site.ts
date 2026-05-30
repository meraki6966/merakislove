// Shared site-wide data: navigation, external links, and credentials.

export const navLinks = [
  { label: "Work", href: "/work" },
  { label: "Services", href: "/services" },
  { label: "About", href: "/about" },
  { label: "Contact", href: "/contact" },
] as const;

export const calendly = {
  // New prospects
  newProject: "https://calendly.com/hello-merakislove/new-meeting",
  // Existing clients
  clientDiscussion: "https://calendly.com/hello-merakislove/client-discussion",
} as const;

export const socials = [
  { label: "LinkedIn", href: "https://www.linkedin.com/in/adammcclarin/" },
  { label: "GitHub", href: "https://github.com/meraki6966" },
  { label: "Substack", href: "https://adammcclarin.substack.com" },
] as const;

// Credibility ticker — order matters, shown left-to-right.
export const credentials = [
  "CISSP",
  "Azure AI Engineer",
  "Dual MS Cybersecurity · UMGC",
  "MBA · Baruch",
  "Published Author",
  "20 Years",
] as const;

// Shared Open Graph fields. Page metadata shallowly overwrites the layout's
// openGraph object, so each page spreads this base and sets its own title/url.
export const ogBase = {
  siteName: "Meraki is Love",
  type: "website",
  locale: "en_US",
} as const;

export const studio = {
  name: "Meraki is Love, LLC",
  brand: "Soulful Tech",
  owner: "Adam McClarin",
  location: "Friendswood, TX",
  domain: "merakislove.com",
} as const;
