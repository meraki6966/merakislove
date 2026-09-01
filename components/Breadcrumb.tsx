const baseUrl = "https://merakislove.com";

export interface Crumb {
  name: string;
  /** Path from the site root, e.g. "/packages/review". */
  path: string;
}

/**
 * BreadcrumbList structured data for one page.
 *
 * The site used to emit a single BreadcrumbList from the root layout on
 * every page, listing Home, Work, Packages, About and Book a call. That was
 * not a breadcrumb at all, it was the nav menu wearing a breadcrumb's
 * schema, and on the package detail pages it also sat alongside that page's
 * real trail so each one shipped two. This renders the real trail for the
 * page it is on, and nothing else does.
 *
 * Home is prepended automatically, so a page passes only what comes after
 * it. The homepage gets no breadcrumb: it is the root of the hierarchy and
 * a single-item trail says nothing.
 */
export default function Breadcrumb({ items }: { items: Crumb[] }) {
  const schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "@id": `${baseUrl}${items[items.length - 1]?.path ?? ""}/#breadcrumb`,
    itemListElement: [{ name: "Home", path: "" }, ...items].map(
      (crumb, i) => ({
        "@type": "ListItem",
        position: i + 1,
        name: crumb.name,
        item: `${baseUrl}${crumb.path}`,
      }),
    ),
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{
        __html: JSON.stringify(schema).replace(/</g, "\\u003c"),
      }}
    />
  );
}
