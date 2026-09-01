// Shared site-wide data: navigation, external links, and credentials.

// The nav is the sales path, narrowed on purpose. Process is an anchor on
// the homepage rather than its own route. /loop, /cybersecurity, /demos,
// /contact and the Presence-First page all still exist and stay in the
// sitemap; they are simply no longer part of the primary path.
export const navLinks = [
  { label: "Work", href: "/work" },
  { label: "Packages", href: "/packages" },
  { label: "Process", href: "/#process" },
  { label: "About", href: "/about" },
] as const;

export const calendly = {
  // New prospects
  newProject: "https://calendly.com/hello-merakislove/new-meeting",
  // Existing clients
  clientDiscussion: "https://calendly.com/hello-merakislove/client-discussion",
} as const;

export const email = "hello@merakislove.com";

export const socials = [
  { label: "LinkedIn", href: "https://www.linkedin.com/in/adammcclarin/" },
  { label: "GitHub", href: "https://github.com/meraki6966" },
  { label: "Substack", href: "https://adammcclarin.substack.com" },
  {
    label: "Facebook",
    href: "https://www.facebook.com/merakislove",
  },
  {
    label: "Instagram",
    href: "https://www.instagram.com/adam.mcclarin.merakislove/",
  },
  { label: "Website", href: "https://adammcclarin.com" },
] as const;

/** Hero proof row. Four items, shown inline under the buttons. */
export const proofRow = [
  "CISSP",
  "Azure AI Engineer",
  "20 years",
  "Products in production",
] as const;

/** Credentials as a flat list. No ticker, no animation. */
export const facts = [
  "20 years across leadership, IT, and information security",
  "CISSP",
  "Azure AI Engineer",
  "Dual M.S., Cybersecurity",
  "MBA",
  "Published author",
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
  site: "https://adammcclarin.com",
  siteLabel: "adammcclarin.com",
  domain: "merakislove.com",
  descriptor:
    "Private AI, secure sites, and full-stack systems for service businesses.",
} as const;
