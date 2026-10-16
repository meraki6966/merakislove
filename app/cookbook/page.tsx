import type { Metadata } from "next";
import Image from "next/image";
import PageHeader from "@/components/PageHeader";
import ScrollReveal from "@/components/ScrollReveal";
import SectionDivider from "@/components/SectionDivider";
import Breadcrumb from "@/components/Breadcrumb";
import { ogBase } from "@/lib/site";

/**
 * The AI Cookbook. Every fact on this page comes from the book itself (its
 * contents, foreword and copyright page) or from the promo record Adam
 * approved: $9.99 for the digital edition, sold on Gumroad, with the
 * hardcover on Amazon sold separately. If the price, the formats or the
 * recipes change, change them here too.
 */

const title = "The AI Cookbook | Meraki is Love";

const description =
  "Recipes for Everyday Life with AI, by Adam McClarin. Twenty-six prompts, each with the result it produced, for kids, home, school, work and the deep end. Digital edition $9.99.";

const url = "https://merakislove.com/cookbook";
const GUMROAD = "https://merakislove.gumroad.com/l/cookbook";
const COVER = "/covers/the-ai-cookbook.jpg";

export const metadata: Metadata = {
  title: { absolute: title },
  description,
  alternates: { canonical: "/cookbook" },
  openGraph: {
    ...ogBase,
    title,
    description,
    url,
    images: [{ url: `https://merakislove.com${COVER}`, width: 614, height: 768, alt: "The AI Cookbook cover: a mixing bowl and a measuring cup pouring light in a sunlit kitchen." }],
  },
};

const courses: { name: string; recipes: string[] }[] = [
  {
    name: "Appetizers",
    recipes: [
      "The Bedtime Story Generator",
      "The Custom Coloring Book",
      "The Choose Your Own Adventure Game",
      "The Animal Fact Checker",
    ],
  },
  {
    name: "Quick Meals",
    recipes: [
      "The Weekly Meal Plan and Macro Calculator",
      "The Budget Optimizer",
      "The Vacation Itinerary",
      "The DIY Home Repair Guide",
    ],
  },
  {
    name: "The Student Menu",
    recipes: [
      "The Socratic Tutor",
      "The Concept Simplifier",
      "The Debate Partner",
      "The Citation Organizer",
    ],
  },
  {
    name: "The Chef's Table",
    recipes: [
      "The Market Analyst",
      "The Secure Copywriter",
      "The Product Architect",
      "The Client Onboarding Guide",
    ],
  },
  {
    name: "Molecular Gastronomy",
    recipes: [
      "The Markdown Masterpiece",
      "The Logic Solver",
      "The Data Synthesizer",
      "The System Prompt Builder",
    ],
  },
  {
    name: "Second Helpings",
    recipes: [
      "The Journaling Companion",
      "The Meditation Script Builder",
      "The Resume Rebuilder",
      "The Cover Letter Tailor",
      "The Character Consistency Checker",
      "The Query Letter Builder",
    ],
  },
];

const RECIPE_COUNT = courses.reduce((n, c) => n + c.recipes.length, 0);

const included = [
  "The book as a PDF and an EPUB, 70 pages.",
  "Three skill files, one each for ChatGPT, Claude and Gemini.",
  "Every recipe with its exact prompt and the result it produced.",
];

const bookSchema = {
  "@context": "https://schema.org",
  "@type": "Book",
  "@id": `${url}/#book`,
  name: "The AI Cookbook",
  alternativeHeadline: "Recipes for Everyday Life with AI",
  author: { "@type": "Person", name: "Adam McClarin" },
  publisher: { "@id": "https://merakislove.com/#organization" },
  datePublished: "2026",
  bookEdition: "First edition",
  bookFormat: "https://schema.org/EBook",
  numberOfPages: 70,
  image: `https://merakislove.com${COVER}`,
  url,
  offers: {
    "@type": "Offer",
    price: "9.99",
    priceCurrency: "USD",
    url: GUMROAD,
    availability: "https://schema.org/InStock",
  },
};

export default function CookbookPage() {
  return (
    <div className="mx-auto max-w-5xl px-6 pb-24 pt-32 sm:px-8 sm:pb-32 sm:pt-40">
      <Breadcrumb items={[{ name: "The AI Cookbook", path: "/cookbook" }]} />

      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(bookSchema).replace(/</g, "\\u003c") }}
      />

      <div className="grid items-start gap-12 md:grid-cols-[minmax(0,1fr)_280px] lg:grid-cols-[minmax(0,1fr)_320px]">
        <div>
          <PageHeader
            eyebrow="The book"
            title="The AI Cookbook."
            subtitle="Recipes for Everyday Life with AI. The exact prompts I use for my own kids, my own household, my own clients and my own research, each one written out with the result it produced."
          />
          <ScrollReveal className="mt-10 flex flex-wrap items-center gap-4">
            <a
              href={GUMROAD}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
            >
              Get the digital edition, $9.99
            </a>
            <p className="font-mono text-xs uppercase tracking-[0.16em] text-smoke-dim">
              Hardcover on Amazon, sold separately
            </p>
          </ScrollReveal>
        </div>

        <ScrollReveal className="mx-auto w-full max-w-[320px]">
          <div className="relative overflow-hidden rounded-lg border border-border-mid shadow-2xl" style={{ aspectRatio: "614 / 768" }}>
            <Image
              src={COVER}
              alt="The AI Cookbook cover: a mixing bowl and a measuring cup pouring light in a sunlit kitchen."
              fill
              sizes="(min-width: 1024px) 320px, (min-width: 768px) 280px, 80vw"
              className="object-cover"
              priority
            />
          </div>
        </ScrollReveal>
      </div>

      <section className="mt-24">
        <ScrollReveal className="flex flex-col gap-4">
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">Saturday mornings, written down</h2>
          <SectionDivider align="left" />
        </ScrollReveal>
        <ScrollReveal className="mt-8 flex max-w-2xl flex-col gap-5">
          <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            I wrote most of this book the way I write most things that matter to me: on a Saturday morning, coffee going cold beside the keyboard, the house still quiet. After twenty years in software, security and now AI, the tools keep changing. The discipline doesn&apos;t. Know what you&apos;re building, know why, and know exactly what you&apos;re asking the machine to do.
          </p>
          <p className="font-body text-base leading-relaxed text-smoke-dim sm:text-lg">
            So the book is organized the way a cookbook organizes a kitchen, by what you&apos;re trying to make. You don&apos;t read it start to finish. You turn to the one thing you need today, a bedtime story, a budget, a market analysis, and follow the recipe.
          </p>
        </ScrollReveal>
      </section>

      <section className="mt-24">
        <ScrollReveal className="flex flex-col gap-4">
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">The menu</h2>
          <SectionDivider align="left" />
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            {RECIPE_COUNT} recipes in six courses.
          </p>
        </ScrollReveal>
        <div className="mt-10 grid gap-px overflow-hidden rounded-xl border border-border bg-border sm:grid-cols-2 lg:grid-cols-3">
          {courses.map((course, i) => (
            <ScrollReveal key={course.name} delay={i * 0.04} className="h-full">
              <div className="flex h-full flex-col gap-4 bg-void p-6 sm:p-7">
                <h3 className="font-display text-2xl font-light text-amber">{course.name}</h3>
                <ul className="flex flex-col gap-2">
                  {course.recipes.map((recipe) => (
                    <li key={recipe} className="font-body text-sm leading-relaxed text-smoke-dim">
                      {recipe}
                    </li>
                  ))}
                </ul>
              </div>
            </ScrollReveal>
          ))}
        </div>
      </section>

      <section className="mt-24">
        <ScrollReveal className="flex flex-col gap-4">
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">What you get</h2>
          <SectionDivider align="left" />
        </ScrollReveal>
        <ScrollReveal className="mt-8">
          <ul className="flex max-w-2xl flex-col gap-3">
            {included.map((item) => (
              <li key={item} className="flex items-start gap-3 font-body text-base leading-relaxed text-smoke-dim">
                <span aria-hidden className="mt-2.5 h-1 w-1 shrink-0 rounded-full bg-amber" />
                {item}
              </li>
            ))}
          </ul>
          <p className="mt-6 max-w-2xl font-body text-sm leading-relaxed text-smoke-dim">
            AI tools change quickly. The model names and features in the book are the ones available when I wrote it, so check each platform for its current options before you start a recipe.
          </p>
        </ScrollReveal>
      </section>

      <section className="mt-24 border-t border-border pt-12">
        <ScrollReveal className="flex flex-col items-start gap-5">
          <h2 className="font-display text-3xl font-light text-smoke sm:text-4xl">Pick one thing you need today.</h2>
          <p className="max-w-2xl font-body text-base leading-relaxed text-smoke-dim">
            Start with the recipe that fits this week, and the rest of the kitchen will be there when you&apos;re hungry for the next one.
          </p>
          <a
            href={GUMROAD}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center justify-center gap-3 rounded-full bg-amber px-7 py-3.5 font-mono text-xs uppercase tracking-[0.18em] text-void transition-transform duration-300 hover:scale-[1.02]"
          >
            Get the digital edition, $9.99
          </a>
        </ScrollReveal>
      </section>
    </div>
  );
}
