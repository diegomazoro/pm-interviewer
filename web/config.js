// Fill these in once you've completed agent/VOICE_SETUP.md:
// - backendUrl: the public URL of your deployed server.py (Render/Fly.io/Railway)
// - agentId: ONE shared ElevenLabs Agent ID (not per-case -- a single Agent
//   serves the whole library; which case runs is chosen per conversation
//   via the widget's dynamic-variables attribute, see session.html).
//
// Each case also carries its own `firstMessage` -- the exact welcome +
// case-prompt text the ElevenLabs Agent should SPEAK DIRECTLY as its first
// message (via the {{first_message}} dynamic variable), rather than
// generating it through our custom LLM. This matters because ElevenLabs
// only calls the custom LLM once the user has said something -- an empty
// "First message" field means the agent just waits silently, it does not
// auto-trigger our backend. So the case's opening line has to be data
// ElevenLabs can speak itself on turn one.
//
// To add a case to the library later: add an entry here with the exact
// Section A prompt text from the matching file in agent/cases/, and drop
// the case file itself in that folder -- nothing else needs to change.

const CONFIG = {
  backendUrl: "https://pm-interviewer-production.up.railway.app",
  agentId: "agent_6301kyvwxka2fmnbzcszcve9rdey",

  cases: [
    {
      id: "case_01_profitability_peak_performance",
      title: "Peak Performance Sports",
      subtitle: "Why did profit drop 30% on flat revenue?",
      type: "Consulting",
      firstMessage: "Welcome, let's get started. Our client is Peak Performance Sports, a mid-sized chain of 40 sporting goods retail stores across the Midwest. The company has been profitable for years, but the CEO just got the results for the last fiscal year and profits dropped 30% versus the prior year, even though revenue was roughly flat. The CEO has hired us to figure out why profit fell and to recommend what to do about it. How would you approach this?",
    },
    {
      id: "case_02_market_entry_brewco_japan",
      title: "BrewCo",
      subtitle: "Should a craft brewer enter the Japanese market?",
      type: "Consulting",
      firstMessage: "Welcome, let's get started. Our client is BrewCo, a U.S. craft beer company with $150M in annual revenue, strong in the domestic premium beer segment. Growth in the U.S. has slowed, and the CEO is considering entering Japan as the company's first international market. She's asked us: should BrewCo enter Japan, and if so, how? What's your approach?",
    },
    {
      id: "case_03_growth_medequip_new_product",
      title: "MedEquip Co",
      subtitle: "Should a hospital-equipment maker launch a home-health product?",
      type: "Consulting",
      firstMessage: "Welcome, let's get started. Our client is MedEquip Co, a manufacturer of hospital equipment with $500M in revenue, primarily selling patient monitoring systems to large hospitals. Their R&D team has developed a portable version of their flagship monitor, designed for home health care and small clinics — a new market for the company. The CEO wants to know: should MedEquip launch this new product line, and what would it take to succeed? How would you think about this?",
    },
    {
      id: "case_04_pm_satisfaction_drop_figma",
      title: "Figma",
      subtitle: "Why did customer satisfaction drop this quarter?",
      type: "Product",
      firstMessage: "Welcome, let's get started. You're a Product Manager at Figma. Every quarter, the company surveys users and tracks an NPS-style satisfaction score. This quarter, satisfaction among Professional-plan (paid, small team) users dropped from 42 to 28 — a big drop — while Enterprise and Free-tier users stayed flat. Your VP of Product wants to know why, and what you'd do about it. How would you approach this?",
    },
    {
      id: "case_05_pm_retention_drop_notion",
      title: "Notion",
      subtitle: "Why did new-user retention drop after an onboarding change?",
      type: "Product",
      firstMessage: "Welcome, let's get started. You're a PM at Notion, focused on the personal/individual user segment (not teams). Looking at cohort data, the Week-4 retention rate for new signups has dropped from 38% to 26% over the last two months, for users who signed up organically (not from a paid ad campaign). Leadership wants to understand why and what to do. How would you approach this?",
    },
    {
      id: "case_06_pm_support_bottleneck_revolut",
      title: "Revolut",
      subtitle: "Why are support tickets and response times spiking?",
      type: "Product",
      firstMessage: "Welcome, let's get started. You're a PM at Revolut, owning the customer support experience for the core banking app. Over the past 6 weeks, support ticket volume has grown 60%, and average first-response time has gone from 4 hours to over 24 hours. Customers are complaining loudly on social media. Your Head of Product wants a plan by end of week. How would you approach this?",
    },
    {
      id: "case_07_pm_fraud_increase_stripe",
      title: "Stripe",
      subtitle: "Why is the fraud rate rising for a specific merchant segment?",
      type: "Product",
      firstMessage: "Welcome, let's get started. You're a PM at Stripe, on the team responsible for payment fraud prevention. Over the past month, the fraud rate (confirmed fraudulent transactions as a % of total volume) has risen from 0.08% to 0.22% for a specific transaction type: card-not-present transactions from newly onboarded small merchants. Your Head of Risk wants a plan. How would you approach this?",
    },
    {
      id: "case_08_pm_prioritization_linear",
      title: "Linear",
      subtitle: "Which roadmap initiative should get next quarter's capacity?",
      type: "Product",
      firstMessage: "Welcome, let's get started. You're a PM at Linear. Your team has capacity for one major initiative next quarter, and two candidates are on the table: a native mobile app, currently Linear is web/desktop only with a weak mobile web experience, and a customer-requested advanced automation and workflow rules feature for power users. Your engineering lead wants your recommendation with reasoning, not just a gut call. How would you approach deciding?",
    },
  ],
};
