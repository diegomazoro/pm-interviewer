// LOUDCASE -- live, voice-based case interview practice for Product
// Managers. Positioning: the best place for PMs to rehearse the kind of
// live case interviews asked at top tech companies, out loud, with
// instant scored feedback.
//
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
//
// NOTE: the 3 original consulting-style cases (case_01-03, in
// agent/cases/) are intentionally left out of this list -- Loudcase is
// positioned as PM-focused first, so the public case picker only shows
// PM cases. The consulting case files are untouched on disk if that
// changes later.

const CONFIG = {
  backendUrl: "https://pm-interviewer-production.up.railway.app",
  agentId: "agent_6301kyvwxka2fmnbzcszcve9rdey",

  cases: [
    {
      id: "case_04_pm_satisfaction_drop_figma",
      title: "Figma",
      subtitle: "Why did customer satisfaction drop this quarter?",
      type: "Analytical",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at Figma. Every quarter, the company surveys users and tracks an NPS-style satisfaction score. This quarter, satisfaction among Professional-plan (paid, small team) users dropped from 42 to 28 — a big drop — while Enterprise and Free-tier users stayed flat. Your VP of Product wants to know why, and what you'd do about it. How would you approach this?",
    },
    {
      id: "case_05_pm_retention_drop_notion",
      title: "Notion",
      subtitle: "Why did new-user retention drop after an onboarding change?",
      type: "Analytical",
      firstMessage: "Welcome to Loudcase, let's get started! You're a PM at Notion, focused on the personal/individual user segment (not teams). Looking at cohort data, the Week-4 retention rate for new signups has dropped from 38% to 26% over the last two months, for users who signed up organically (not from a paid ad campaign). Leadership wants to understand why and what to do. How would you approach this?",
    },
    {
      id: "case_06_pm_support_bottleneck_revolut",
      title: "Revolut",
      subtitle: "Why are support tickets and response times spiking?",
      type: "Problem Solving",
      firstMessage: "Welcome to Loudcase, let's get started! You're a PM at Revolut, owning the customer support experience for the core banking app. Over the past 6 weeks, support ticket volume has grown 60%, and average first-response time has gone from 4 hours to over 24 hours. Customers are complaining loudly on social media. Your Head of Product wants a plan by end of week. How would you approach this?",
    },
    {
      id: "case_07_pm_fraud_increase_stripe",
      title: "Stripe",
      subtitle: "Why is the fraud rate rising for a specific merchant segment?",
      type: "Analytical",
      firstMessage: "Welcome to Loudcase, let's get started! You're a PM at Stripe, on the team responsible for payment fraud prevention. Over the past month, the fraud rate (confirmed fraudulent transactions as a % of total volume) has risen from 0.08% to 0.22% for a specific transaction type: card-not-present transactions from newly onboarded small merchants. Your Head of Risk wants a plan. How would you approach this?",
    },
    {
      id: "case_08_pm_prioritization_linear",
      title: "Linear",
      subtitle: "Which roadmap initiative should get next quarter's capacity?",
      type: "Business Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a PM at Linear. Your team has capacity for one major initiative next quarter, and two candidates are on the table: a native mobile app, currently Linear is web/desktop only with a weak mobile web experience, and a customer-requested advanced automation and workflow rules feature for power users. Your engineering lead wants your recommendation with reasoning, not just a gut call. How would you approach deciding?",
    },

    // Product Sense cases -- open-ended design/improvement prompts, a
    // different (and harder) PM interview format than the diagnostic
    // cases above. Type "Product Sense" distinguishes them in the picker.
    {
      id: "case_09_pm_product_sense_anthropic",
      title: "Anthropic",
      subtitle: "Design longer-running, more autonomous AI agent tasks.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at Anthropic. Claude can already write code, browse, and take actions on a user's behalf through tool use, but today it mostly works in short bursts with a human checking in frequently. Your team is exploring giving Claude the ability to work on multi-step tasks over much longer stretches of time -- for example, managing a multi-day project end-to-end -- with less constant supervision. How would you approach designing this?",
    },
    {
      id: "case_10_pm_product_sense_openai",
      title: "OpenAI",
      subtitle: "Design safeguards for an agent that acts on your behalf.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at OpenAI. ChatGPT's agent mode can already browse the web and take actions on a user's behalf -- filling out forms, adding items to a cart, submitting information -- and its capabilities are expanding to include actions with real-world consequences, like completing a purchase or booking a reservation. Your team needs to decide how the product should handle these higher-stakes actions. How would you approach this?",
    },
    {
      id: "case_11_pm_product_sense_google",
      title: "Google",
      subtitle: "Improve indoor navigation in large venues on Maps.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at Google, working on Maps. Users navigate Maps confidently outdoors, but once they step inside a large venue -- an airport, a big-box mall, a stadium -- GPS gets unreliable and Maps mostly stops being useful. People end up wandering, asking staff, or falling back on paper signage. How would you approach improving the experience for indoor navigation in these large venues?",
    },
    {
      id: "case_12_pm_product_sense_meta",
      title: "Meta",
      subtitle: "Design peer favor-sharing inside Facebook Groups.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at Meta, working on Facebook Groups. Members of local community groups -- neighborhood groups, parent groups, hobby groups -- already post informal asks and offers in the feed: someone needs a ladder for an afternoon, someone else is driving to the airport and can take a neighbor along, someone can watch a pet for a weekend. Right now this all happens as regular posts and comments, which get buried and are easy to miss. How would you design a way to help members of these groups exchange small favors and skills with each other?",
    },
    {
      id: "case_13_pm_product_sense_netflix",
      title: "Netflix",
      subtitle: "Help groups of people agree on what to watch together.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager at Netflix. A common frustration among households and roommates is that multiple people want to watch something together but can't agree on what -- they end up scrolling through the home screen for fifteen minutes, or give up and watch something nobody's excited about. How would you design a feature to help groups of people decide together what to watch?",
    },
    {
      id: "case_14_pm_product_sense_amazon",
      title: "Amazon",
      subtitle: "Design proactive replenishment of household essentials via Alexa.",
      type: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started! You're a Product Manager on the Alexa devices team at Amazon. Customers can already say 'Alexa, reorder paper towels' to repurchase something they've bought before, but usage of this is low -- most people simply forget to reorder essentials until they've already run out. Your team wants to help customers replenish household essentials -- things like paper towels, detergent, coffee -- before they run out, using Alexa. How would you approach designing this?",
    },
  ],
};
