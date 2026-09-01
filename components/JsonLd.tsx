// Structured data (JSON-LD) for SEO / AEO. Rendered site-wide from the root
// layout so every page exposes Organization, ProfessionalService and FAQPage.
// BreadcrumbList is NOT here: it belongs to the page, not the site, and is
// rendered per page by components/Breadcrumb.tsx. Each schema is emitted as its own
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
    "Private AI, secure sites, and full-stack systems for service businesses, from a CISSP-certified studio with 20 years of experience.",
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
    name: "Packages",
    itemListElement: [
      {
        "@type": "Offer",
        itemOffered: {
          "@type": "Service",
          name: "Review",
          description:
            "A CISSP-informed review of a site or AI stack. Ranked findings and a fix order, MITRE ATT&CK mapped where it applies.",
          url: `${baseUrl}/packages/review`,
        },
        priceSpecification: {
          "@type": "PriceSpecification",
          minPrice: 500,
          maxPrice: 1500,
          priceCurrency: "USD",
        },
      },
      {
        "@type": "Offer",
        itemOffered: {
          "@type": "Service",
          name: "Meraki BIP",
          description:
            "A lead engine, an assistant trained on your documents, and distribution across two platforms from one dashboard.",
          url: `${baseUrl}/packages/bip`,
        },
        priceSpecification: {
          "@type": "PriceSpecification",
          minPrice: 7000,
          priceCurrency: "USD",
        },
      },
      {
        "@type": "Offer",
        itemOffered: {
          "@type": "Service",
          name: "Custom build",
          description:
            "Full-stack product, Presence-First site, or private AI inside a tool you already run. Scoped after a call.",
          url: `${baseUrl}/packages/custom`,
        },
      },
      {
        "@type": "Offer",
        itemOffered: {
          "@type": "Service",
          name: "Presence-First Web Design",
          url: `${baseUrl}/packages/presence-first-web-design`,
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
        text: "Soulful Tech works three ways: a five-day review of an existing site or AI stack from $500, Meraki BIP (a six-week lead engine and private assistant) from $7,000, and custom full-stack or Presence-First builds scoped after a call. Engagements are led by a CISSP-certified engineer with 20 years of experience.",
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
        text: "Meraki is Love builds VeloxSync (performance intelligence that flags at-risk talent), VeloxSync for Education (AI homeschool planning for families), Canopy Guard (a security posture auditor with findings mapped to MITRE ATT&CK), and Meridian AI (executive intelligence with MFA and RBAC).",
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
        text: "Book a 20-minute call at https://merakislove.com/start. There is no deck and no obligation.",
      },
    },
  ],
};

const schemas = [organization, professionalService, faqPage];

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
