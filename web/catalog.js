// Shared helpers for browsing the case library (practice.html,
// company.html, session.html). The cases themselves live in config.js;
// this file only adds how they're grouped and described.

// Skills in the order they're shown, with a one-line description of what
// each case type tests.
const SKILLS = [
  { name: "Diagnosis", blurb: "Find the root cause behind a metric change." },
  { name: "Product Sense", blurb: "Design a product for a specific user and problem." },
  { name: "Prioritization", blurb: "Decide what to build with limited capacity." },
  { name: "Metrics & Experiments", blurb: "Judge whether a launch or test really worked." },
  { name: "Strategy & Growth", blurb: "Make a market, pricing, or expansion call." },
];

// One-line neutral description per company, shown under its name.
const COMPANY_TAGLINES = {
  "Figma": "Collaborative design tools",
  "Notion": "Connected workspace for docs and wikis",
  "Revolut": "Global digital banking",
  "Stripe": "Payments infrastructure",
  "Linear": "Issue tracking for software teams",
  "Mercado Libre": "E-commerce and payments in Latin America",
  "Anthropic": "AI research and products",
  "OpenAI": "AI research and products",
  "Google": "Search, Maps, YouTube and more",
  "Meta": "Social apps and messaging",
  "Netflix": "Streaming entertainment",
  "Amazon": "E-commerce and logistics",
  "Jeeves": "Corporate cards for startups and SMBs",
  "Nubank": "Digital banking in Latin America",
};

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

// "Mercado Libre" -> "mercado-libre"
function companySlug(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function companyUrl(name) {
  return `company.html?company=${encodeURIComponent(companySlug(name))}`;
}

function skillIndex(skill) {
  const i = SKILLS.findIndex((s) => s.name === skill);
  return i === -1 ? SKILLS.length : i;
}

// [{ name, slug, tagline, cases: [...sorted by skill] }] in the order each
// company first appears in CONFIG.cases.
function companiesFromConfig() {
  const byName = new Map();
  CONFIG.cases.forEach((c) => {
    if (!byName.has(c.title)) byName.set(c.title, []);
    byName.get(c.title).push(c);
  });
  return [...byName].map(([name, cases]) => ({
    name,
    slug: companySlug(name),
    tagline: COMPANY_TAGLINES[name] || "",
    cases: cases.slice().sort((a, b) => skillIndex(a.skill) - skillIndex(b.skill)),
  }));
}
