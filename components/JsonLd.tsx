// Structured data (JSON-LD) for SEO / AEO. Rendered site-wide from the root
// layout so the homepage exposes Organization, ProfessionalService, FAQPage,
// and BreadcrumbList schemas. Each schema is emitted as its own
// `application/ld+json` <script> per the Next.js JSON-LD guidance. JSON is
// XSS-hardened by escaping `<` to its unicode equivalent.

const baseUrl = "https://merakislove.com";

const organization = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": `${baseUrl}/#organization`,
  name: "Meraki is Love, LLC",
  alternateName: "Soulful Tech",
  url: baseUrl,
  description:
    "Full-stack AI product studio. AI integration with a security posture, built with intention.",
  founder: {
    "@type": "Person",
    name: "Adam McClarin",
    jobTitle: "Founder & Principal Engineer",
    hasCredential: "CISSP",
  },
  foundingLocation: {
    "@type": "Place",
    address: {
      "@type": "PostalAddress",
      addressLocality: "Friendswood",
      addressRegion: "TX",
      addressCountry: "US",
    },
  },
  sameAs: [
    "https://www.linkedin.com/in/adammcclarin/",
    "https://github.com/meraki6966",
    "https://adammcclarin.substack.com",
    "https://adammcclarin.com",
  ],
};

const professionalService = {
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": `${baseUrl}/#service`,
  name: "Meraki is Love · Soulful Tech",
  url: baseUrl,
  description:
    "Product engineering, AI integration, security posture, and content strategy from a CISSP-certified studio with 20 years of experience.",
  priceRange: "$$$",
  areaServed: "Worldwide",
  address: {
    "@type": "PostalAddress",
    addressLocality: "Friendswood",
    addressRegion: "TX",
    addressCountry: "US",
  },
  provider: { "@id": `${baseUrl}/#organization` },
  hasOfferCatalog: {
    "@type": "OfferCatalog",
    name: "Services",
    itemListElement: [
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Product Engineering" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "AI Integration" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Security Posture" } },
      { "@type": "Offer", itemOffered: { "@type": "Service", name: "Content Strategy" } },
      {
        "@type": "Offer",
        itemOffered: {
          "@type": "Service",
          name: "Presence-First Web Design",
          url: `${baseUrl}/services/presence-first-web-design`,
        },
      },
    ],
  },
};

const faqPage = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": `${baseUrl}/#faq`,
  mainEntity: [
    {
      "@type": "Question",
      name: "What is Meraki is Love?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Meraki is Love, LLC is a full-stack AI product studio operating under the Soulful Tech brand, founded by Adam McClarin (CISSP). It builds production-grade software where AI capability and security posture are designed together.",
      },
    },
    {
      "@type": "Question",
      name: "What services does Soulful Tech offer?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Soulful Tech offers product engineering, AI integration, security posture review and hardening, and AEO/GEO content strategy. Engagements are led by a CISSP-certified engineer with 20 years of experience.",
      },
    },
    {
      "@type": "Question",
      name: "Who is Adam McClarin?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Adam McClarin is the founder and principal engineer of Meraki is Love. He holds the CISSP certification, a dual MS in Cybersecurity from UMGC, an MBA from Baruch, and the Azure AI Engineer credential.",
      },
    },
    {
      "@type": "Question",
      name: "What products has Meraki is Love built?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Meraki is Love builds VeloxSync (high-throughput data synchronization), Meraki Lingua (multilingual translation API), and Canopy Guard (an automated web visibility and security audit engine covering 47 signals).",
      },
    },
    {
      "@type": "Question",
      name: "Where is Meraki is Love located?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "Meraki is Love is based in Friendswood, Texas, USA, and serves clients worldwide.",
      },
    },
    {
      "@type": "Question",
      name: "How do I book a consultation?",
      acceptedAnswer: {
        "@type": "Answer",
        text: "You can book a free 30-minute walkthrough at https://calendly.com/hello-merakislove/new-meeting.",
      },
    },
  ],
};

const breadcrumb = {
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": `${baseUrl}/#breadcrumb`,
  itemListElement: [
    { "@type": "ListItem", position: 1, name: "Home", item: baseUrl },
    { "@type": "ListItem", position: 2, name: "Work", item: `${baseUrl}/work` },
    { "@type": "ListItem", position: 3, name: "Services", item: `${baseUrl}/services` },
    { "@type": "ListItem", position: 4, name: "About", item: `${baseUrl}/about` },
    { "@type": "ListItem", position: 5, name: "Contact", item: `${baseUrl}/contact` },
  ],
};

const schemas = [organization, professionalService, faqPage, breadcrumb];

export default function JsonLd() {
  return (
    <>
      {schemas.map((schema, i) => (
        <script
          key={i}
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(schema).replace(/</g, "\\u003c"),
          }}
        />
      ))}
    </>
  );
}
