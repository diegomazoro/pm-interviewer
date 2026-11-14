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
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Figma. Every quarter, the company surveys users and tracks an NPS-style satisfaction score. This quarter, satisfaction among Professional-plan (paid, small team) users dropped from 42 to 28 — a big drop — while Enterprise and Free-tier users stayed flat. Your VP of Product wants to know why, and what you'd do about it. How would you approach this?",
    },
    {
      id: "case_22_pm_product_sense_figma",
      title: "Figma",
      subtitle: "Help non-designers create on-brand assets.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Figma. More and more people who aren't designers -- marketers, salespeople, people in operations -- open Figma to make quick assets like social posts, slides, or one-pagers. Design teams complain that these assets often break the brand: wrong fonts, off-brand colors, detached components. How would you design a better experience for non-designers creating assets in Figma?",
    },
    {
      id: "case_23_pm_prioritization_figma",
      title: "Figma",
      subtitle: "Pick next quarter's core editor bet.",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Figma's core editor team. Next quarter your team has capacity for roughly one major project, and three candidates keep coming up: full offline editing, performance improvements for very large files, and better branching and merging for design-system teams. Each has loud supporters inside the company. Your VP wants a recommendation she can defend to the exec team. How would you approach this?",
    },
    {
      id: "case_24_pm_metrics_experiment_figma",
      title: "Figma",
      subtitle: "Comments are up 30% after a redesign. Did it work?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Figma. Two months ago your team launched a redesigned commenting experience in the editor. Since launch, comments per weekly active user are up 30%, and the team wants to present it as a big success at the next all-hands. Your director asks you to make sure the story holds up. How would you evaluate whether this launch actually worked?",
    },
    {
      id: "case_25_pm_strategy_figma",
      title: "Figma",
      subtitle: "Should Figma introduce regional pricing in emerging markets?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Figma's monetization team. In countries like India, Brazil, and Indonesia, Figma has a huge and fast-growing base of free users, but very few of them pay. Some people internally want to introduce lower regional prices in these markets; others worry it would cannibalize revenue and be abused. Leadership has asked for your recommendation. How would you approach this?",
    },
    {
      id: "case_05_pm_retention_drop_notion",
      title: "Notion",
      subtitle: "Why did new-user retention drop after an onboarding change?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Notion, focused on the personal/individual user segment (not teams). Looking at cohort data, the Week-4 retention rate for new signups has dropped from 38% to 26% over the last two months, for users who signed up organically (not from a paid ad campaign). Leadership wants to understand why and what to do. How would you approach this?",
    },
    {
      id: "case_26_pm_product_sense_notion",
      title: "Notion",
      subtitle: "Keep team workspaces from turning into a mess.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Notion. Teams love how easy it is to create pages, but after a year or two, many team workspaces turn into a mess: outdated docs, duplicate pages, and nobody's sure which version is the right one. People start saying 'I can never find anything in Notion.' How would you design a solution to keep team workspaces healthy over time?",
    },
    {
      id: "case_27_pm_prioritization_notion",
      title: "Notion",
      subtitle: "Choose which growth bets to fund next quarter.",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Notion's growth team. Next quarter you have engineers for about ten weeks of work, and three projects are on the table: a referral program, improvements to the template gallery, and a redesign of the flow for inviting teammates. Everyone has a favorite. Your manager wants a prioritized plan with the reasoning behind it. How would you approach this?",
    },
    {
      id: "case_28_pm_metrics_experiment_notion",
      title: "Notion",
      subtitle: "1.2M forms created. Is Forms really a success?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're the PM for Notion Forms, a new feature that lets users build forms whose responses land in a Notion database. Six weeks after launch, 1.2 million forms have been created, and leadership is calling it one of the most successful launches of the year. Your VP asks you to put together a proper success scorecard before the next planning cycle. How would you evaluate whether Forms is actually succeeding?",
    },
    {
      id: "case_29_pm_strategy_notion",
      title: "Notion",
      subtitle: "How should Notion win very large enterprises?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Notion's strategy team. Notion grew mostly bottom-up: individuals and small teams adopt it, then their companies pay. Leadership now wants a bigger share of very large enterprises -- companies with ten thousand or more employees -- where established tools dominate. They're debating how to go after this market. What would you recommend, and how would you approach the decision?",
    },
    {
      id: "case_06_pm_support_bottleneck_revolut",
      title: "Revolut",
      subtitle: "Why are support tickets and response times spiking?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Revolut, owning the customer support experience for the core banking app. Over the past 6 weeks, support ticket volume has grown 60%, and average first-response time has gone from 4 hours to over 24 hours. Customers are complaining loudly on social media. Your Head of Product wants a plan by end of week. How would you approach this?",
    },
    {
      id: "case_30_pm_product_sense_revolut",
      title: "Revolut",
      subtitle: "Help young adults build a real saving habit.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Revolut. A large share of your customers are between 18 and 25. Many of them use Revolut every day for spending, but very few of them save regularly -- most end each month with close to nothing left. How would you design a product experience that helps young adults build a real saving habit?",
    },
    {
      id: "case_31_pm_prioritization_revolut",
      title: "Revolut",
      subtitle: "Three stakeholders, one team: what do you build?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Revolut leading a team in the retail app. For next quarter, three projects are competing for your team: leadership wants to expand the crypto trading features, the support team wants you to fix cards being wrongly declined at merchants, and the growth team wants a tool that makes it easy to switch your salary deposit to Revolut. You can realistically do one well. How would you decide?",
    },
    {
      id: "case_32_pm_metrics_experiment_revolut",
      title: "Revolut",
      subtitle: "Fraud on large transfers fell 64%. Did the selfie check work?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Revolut's fraud team. Two months ago you launched a selfie check for every transfer above €1,000. The fraud dashboard shows fraud losses on those protected transfers are down 64%, and the team wants to celebrate and extend the selfie check to other products. Your Head of Risk asks you to evaluate whether the change actually worked. How would you approach this?",
    },
    {
      id: "case_33_pm_strategy_revolut",
      title: "Revolut",
      subtitle: "Should Revolut launch mortgages?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Revolut's strategy team. In one large European market where Revolut has a full banking license, leadership is debating whether to launch mortgages. Mortgages are the biggest financial product most people ever take, and banks use them to win lifelong customers. But it's a very different business from what Revolut does today. They've asked you for a recommendation. How would you approach it?",
    },
    {
      id: "case_07_pm_fraud_increase_stripe",
      title: "Stripe",
      subtitle: "Why is the fraud rate rising for a specific merchant segment?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Stripe, on the team responsible for payment fraud prevention. Over the past month, the fraud rate (confirmed fraudulent transactions as a % of total volume) has risen from 0.08% to 0.22% for a specific transaction type: card-not-present transactions from newly onboarded small merchants. Your Head of Risk wants a plan. How would you approach this?",
    },
    {
      id: "case_18_pm_product_sense_stripe",
      title: "Stripe",
      subtitle: "Help small merchants deal with payment disputes.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Stripe. When a customer disputes a card payment -- a chargeback -- the merchant has a limited window to respond with evidence, or they automatically lose the money plus a dispute fee. Large merchants have dedicated teams for this, but small businesses on Stripe tend to find disputes confusing and stressful, and most of them lose. How would you design a better experience to help small merchants deal with disputes?",
    },
    {
      id: "case_19_pm_prioritization_stripe",
      title: "Stripe",
      subtitle: "Allocate next half's Billing roadmap across three big bets.",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Stripe Billing, the product businesses use to run subscriptions and invoicing. You own the roadmap for the next half-year, and there are three big candidates competing for your team's capacity: upgrades to usage-based billing, support for new e-invoicing regulations in Europe, and a smarter system for recovering failed subscription payments. You can't fully build all three. Your director wants a recommendation on what to build and why. How would you approach this?",
    },
    {
      id: "case_20_pm_metrics_experiment_stripe",
      title: "Stripe",
      subtitle: "A Checkout A/B test shows +4.2% conversion. Ship it?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Stripe Checkout, the hosted payment page merchants send their customers to. Your team redesigned the page to show express payment options, like saved cards and wallets, at the top before the regular card form. You ran a two-week A/B test, and the experiment dashboard says conversion went up 4.2% in the new version. Your director wants to know: should we roll it out to 100% of traffic? How would you approach this decision?",
    },
    {
      id: "case_21_pm_strategy_stripe",
      title: "Stripe",
      subtitle: "Should Stripe push into in-person payments for small businesses?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Stripe's growth strategy team. Stripe is strongest in online payments, while in-person payments for small businesses in the US -- shops, restaurants, salons paying through card terminals -- are dominated by a few established players. Leadership is debating whether Stripe should push hard into in-person payments for small businesses, and if so, how. They've asked you for a recommendation. How would you approach this?",
    },
    {
      id: "case_08_pm_prioritization_linear",
      title: "Linear",
      subtitle: "Which roadmap initiative should get next quarter's capacity?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Linear. Your team has capacity for one major initiative next quarter, and two candidates are on the table: a native mobile app, currently Linear is web/desktop only with a weak mobile web experience, and a customer-requested advanced automation and workflow rules feature for power users. Your engineering lead wants your recommendation with reasoning, not just a gut call. How would you approach deciding?",
    },
    {
      id: "case_34_pm_diagnosis_linear",
      title: "Linear",
      subtitle: "Why did weekly active teams drop at large workspaces?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Linear. Over the last six weeks, the number of weekly active teams in large workspaces -- companies with more than 500 people on Linear -- has dropped 15%. Smaller workspaces look normal. Your Head of Product wants to know what's going on and what to do. How would you approach this?",
    },
    {
      id: "case_35_pm_product_sense_linear",
      title: "Linear",
      subtitle: "Help teams know whether a project will ship on time.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Linear. Engineering leaders constantly get asked 'Will this project ship on time?' and they usually answer with a gut feeling, then get surprised when deadlines slip. Linear has a lot of data about how work actually moves. How would you design a product that helps teams know -- and communicate -- whether a project is on track?",
    },
    {
      id: "case_36_pm_metrics_experiment_linear",
      title: "Linear",
      subtitle: "Activation fell after a new onboarding. Roll it back?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Linear. A month ago your team launched a new onboarding flow for new workspaces. Since then, the activation rate -- the share of new workspaces that become active in their first two weeks -- has dropped from 40% to 36%. Some people on the team want to roll the new onboarding back immediately. What would you do?",
    },
    {
      id: "case_37_pm_strategy_linear",
      title: "Linear",
      subtitle: "How should pricing adapt when AI agents do the work?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Linear's strategy team. Linear charges per seat -- per human user. But more and more customers use AI coding agents that pick up issues, write code, and close them, with fewer humans needed for the same amount of work. Leadership worries this could slowly shrink revenue even as Linear becomes more valuable. They want your recommendation on how Linear's business model should adapt. How would you approach this?",
    },
    {
      id: "case_16_pm_market_share_mercadolibre",
      title: "Mercado Libre",
      subtitle: "Why has active buyer growth stalled in two markets?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager on Mercado Libre's marketplace growth team. Monthly active buyers have kept growing in Brazil, Mexico, and Argentina, but in Colombia and Peru specifically, active buyer growth has stalled over the last two quarters, even though overall online shopping demand in those two countries is still growing. Your VP of Growth wants to understand why, and what to do about it.",
    },
    {
      id: "case_38_pm_product_sense_mercadolibre",
      title: "Mercado Libre",
      subtitle: "Win the first online purchase in smaller cities.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Mercado Libre. In smaller cities and towns across Latin America, millions of people now have smartphones and internet access, but have never bought anything online. Many of them browse Mercado Libre but don't complete a first purchase. How would you design an experience that gets more of these people to make their first online purchase?",
    },
    {
      id: "case_39_pm_prioritization_mercadolibre",
      title: "Mercado Libre",
      subtitle: "Same-day delivery, seller ads, or seller loans?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Mercado Libre Mexico. Next half, you can fund one of three big initiatives: same-day delivery in Mexico City, an advertising tool that lets small sellers promote their products, or working-capital loans for sellers through Mercado Pago. Each team has a strong pitch. Your country manager wants a recommendation. How would you decide?",
    },
    {
      id: "case_40_pm_metrics_experiment_mercadolibre",
      title: "Mercado Libre",
      subtitle: "A lower free-shipping threshold raised orders 12%. Ship it?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Mercado Libre Mexico. Your team ran an A/B test that lowered the free-shipping threshold from 299 pesos to 199 pesos. In the test group, orders went up 12%. The growth team wants to roll it out to everyone right away. Your director asks you whether that's the right call. How would you evaluate the result?",
    },
    {
      id: "case_41_pm_strategy_mercadolibre",
      title: "Mercado Libre",
      subtitle: "Should Mercado Libre launch a cross-border low-cost offer?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Mercado Libre's strategy team. Low-cost cross-border marketplaces that ship cheap goods directly from Asia are growing fast in Latin America, especially for low-priced items like accessories, gadgets, and fashion. Leadership is debating whether Mercado Libre should launch its own cross-border program with sellers shipping directly from Asia. They've asked for your recommendation. How would you approach this?",
    },

    // Product Sense cases -- open-ended design/improvement prompts, a
    // different (and harder) PM interview format than the diagnostic
    // cases above. Type "Product Sense" distinguishes them in the picker.
    {
      id: "case_09_pm_product_sense_anthropic",
      title: "Anthropic",
      subtitle: "Design longer-running, more autonomous AI agent tasks.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Anthropic. Claude can already write code, browse, and take actions on a user's behalf through tool use, but today it mostly works in short bursts with a human checking in frequently. Your team is exploring giving Claude the ability to work on multi-step tasks over much longer stretches of time, for example managing a multi-day project end-to-end, with less constant supervision. How would you approach designing this?",
    },
    {
      id: "case_42_pm_diagnosis_anthropic",
      title: "Anthropic",
      subtitle: "Why is churn rising among paid subscribers?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Anthropic, working on the Claude consumer app. Over the last two months, monthly churn among paid Pro subscribers has risen from 5% to 8%, even though new signups keep growing and satisfaction surveys on answer quality are higher than ever. Your Head of Product wants to understand why and what to do. How would you approach this?",
    },
    {
      id: "case_43_pm_prioritization_anthropic",
      title: "Anthropic",
      subtitle: "Pick two of three API platform projects.",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Anthropic's API platform team, which serves companies building products on Claude. Next quarter you have capacity for two of these three projects: self-serve higher rate limits for growing startups, data residency in the EU, and a usage and cost dashboard with budget alerts. Each has internal champions. Your director wants a recommendation. How would you approach it?",
    },
    {
      id: "case_44_pm_metrics_experiment_anthropic",
      title: "Anthropic",
      subtitle: "Thumbs-up rate rose to 78%. Is the new style better?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on the Claude consumer app. Your team tested a new response style -- more detailed, more thorough answers -- against the current one. In the test, the thumbs-up rate on responses rose from 72% to 78%. The team wants to make it the default for everyone. Your director asks you to check whether that's the right call. How would you evaluate it?",
    },
    {
      id: "case_45_pm_strategy_anthropic",
      title: "Anthropic",
      subtitle: "Build vertical products or stay a platform?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Anthropic's strategy team. Today, many companies build specialized products on top of Claude -- for example, AI tools for lawyers, financial analysts, or doctors. Some leaders think Anthropic should build its own products for one or two of these industries to capture more value. Others worry it would put Anthropic in competition with its own customers. Leadership wants your recommendation. How would you approach this?",
    },
    {
      id: "case_10_pm_product_sense_openai",
      title: "OpenAI",
      subtitle: "Design safeguards for an agent that acts on your behalf.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at OpenAI. ChatGPT's agent mode can already browse the web and take actions on a user's behalf, filling out forms, adding items to a cart, submitting information, and its capabilities are expanding to include actions with real-world consequences, like completing a purchase or booking a reservation. Your team needs to decide how the product should handle these higher-stakes actions. How would you approach this?",
    },
    {
      id: "case_46_pm_diagnosis_openai",
      title: "OpenAI",
      subtitle: "Why did mobile usage drop in Japan?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at OpenAI working on the ChatGPT mobile app. Over the last four weeks, daily active users of the mobile app in Japan have dropped 12%, while every other major market kept growing. Web usage in Japan looks normal. Your Head of Product wants to know why and what to do. How would you approach this?",
    },
    {
      id: "case_47_pm_prioritization_openai",
      title: "OpenAI",
      subtitle: "Which project grows seats in business accounts?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on ChatGPT's business plans, sold to companies by the seat. Next quarter you can build one of three projects: an admin analytics dashboard showing how the company uses ChatGPT, connectors to internal tools like company drives and wikis, or better sharing of projects and conversations between colleagues. Your director wants to know which one to build and why. How would you decide?",
    },
    {
      id: "case_48_pm_metrics_experiment_openai",
      title: "OpenAI",
      subtitle: "Memory users retain 25% better. Turn it on for everyone?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on ChatGPT. A few months ago you launched memory, which lets ChatGPT remember things about users across conversations. Users can turn it on in settings. Your analytics show that users with memory turned on have 25% higher 30-day retention than users without it. Leadership wants to turn memory on by default for everyone, expecting retention to go up. How would you evaluate whether that's the right decision?",
    },
    {
      id: "case_49_pm_strategy_openai",
      title: "OpenAI",
      subtitle: "Should the free tier have ads?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on ChatGPT's monetization team. Hundreds of millions of people use the free version, and serving them costs a lot. Leadership is debating whether to introduce advertising in the free tier, and if so, how. They're worried about user trust and about hurting paid subscriptions. They want your recommendation. How would you approach this?",
    },
    {
      id: "case_11_pm_product_sense_google",
      title: "Google",
      subtitle: "Improve indoor navigation in large venues on Maps.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Google, working on Maps. Users navigate Maps confidently outdoors, but once they step inside a large venue, like an airport, a big-box mall, or a stadium, GPS gets unreliable and Maps mostly stops being useful. People end up wandering, asking staff, or falling back on paper signage. How would you approach improving the experience for indoor navigation in these large venues?",
    },
    {
      id: "case_50_pm_diagnosis_google",
      title: "Google",
      subtitle: "Why are users writing fewer reviews on Maps?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager on Google Maps. Over the last two months, the number of new reviews users write for places -- restaurants, shops, and so on -- has dropped 25%. Visits to places, measured by navigation and searches, are flat. Reviews are important because they keep place information fresh and useful. Your Head of Product wants to understand why and what to do. How would you approach this?",
    },
    {
      id: "case_51_pm_prioritization_google",
      title: "Google",
      subtitle: "Offline, AI summaries, or Word fidelity?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Google Docs. Next half you can invest heavily in one of three areas: better offline editing, AI summaries of what changed in a document, or much better fidelity when importing and exporting Word files. The AI option has a lot of internal excitement. Your director wants a recommendation tied to the business. How would you decide?",
    },
    {
      id: "case_52_pm_metrics_experiment_google",
      title: "Google",
      subtitle: "More Shorts raised watch time 5%. Roll it out?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on YouTube's home feed. Your team tested showing more Shorts -- short vertical videos -- in the home feed. In the test group, total watch time per user went up 5%. The Shorts team wants to roll it out to everyone. Your director asks you to make sure this is a good decision. How would you evaluate it?",
    },
    {
      id: "case_53_pm_strategy_google",
      title: "Google",
      subtitle: "Grow revenue from local businesses on Maps.",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Google Maps' business team. Millions of local businesses -- restaurants, salons, repair shops -- have free business listings on Maps. Leadership wants to grow revenue from these businesses and is debating two paths: showing more local ads on Maps, or launching a paid subscription for businesses with premium tools. They want your recommendation. How would you approach this?",
    },
    {
      id: "case_12_pm_product_sense_meta",
      title: "Meta",
      subtitle: "Design peer favor-sharing inside Facebook Groups.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Meta, working on Facebook Groups. Members of local community groups, neighborhood groups, parent groups, hobby groups, already post informal asks and offers in the feed: someone needs a ladder for an afternoon, someone else is driving to the airport and can take a neighbor along, someone can watch a pet for a weekend. Right now this all happens as regular posts and comments, which get buried and are easy to miss. How would you design a way to help members of these groups exchange small favors and skills with each other?",
    },
    {
      id: "case_54_pm_diagnosis_meta",
      title: "Meta",
      subtitle: "Why are mid-size creators posting fewer Reels?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager on Instagram Reels, focused on creators. Over the last six weeks, the number of Reels posted by mid-size creators -- accounts with 10,000 to 100,000 followers -- has dropped 18%. Small and very large creators look normal. Creators are the supply side of Reels, so leadership is worried. How would you figure out what's going on?",
    },
    {
      id: "case_55_pm_prioritization_meta",
      title: "Meta",
      subtitle: "Prioritize the WhatsApp Business roadmap in Brazil.",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on WhatsApp Business in Brazil, where millions of small businesses sell to customers through WhatsApp chats. Next half you can build one of three things: in-chat payments with a product catalog, an AI assistant that answers common customer questions automatically, or better tools for sending marketing messages to customers. Your director wants a recommendation. How would you decide?",
    },
    {
      id: "case_56_pm_metrics_experiment_meta",
      title: "Meta",
      subtitle: "A Marketplace test shows +10% messages. Can we trust it?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Facebook Marketplace. Your team tested a new 'Recommended for you' section that shows buyers more items they might like. In the test, buyers sent 10% more messages to sellers than the control group. The team wants to launch it to everyone. Your director asks whether we can trust this result. How would you evaluate it?",
    },
    {
      id: "case_57_pm_strategy_meta",
      title: "Meta",
      subtitle: "Should Instagram offer an ad-free subscription?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Instagram's monetization team. Instagram makes almost all its money from ads. Some leaders want to offer a paid, ad-free subscription worldwide, to diversify revenue and give users a choice. Others think it would lose money because ads earn more than people would pay. Leadership wants your recommendation. How would you approach this?",
    },
    {
      id: "case_13_pm_product_sense_netflix",
      title: "Netflix",
      subtitle: "Help groups of people agree on what to watch together.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Netflix. A common frustration among households and roommates is that multiple people want to watch something together but can't agree on what. They end up scrolling through the home screen for fifteen minutes, or give up and watch something nobody's excited about. How would you design a feature to help groups of people decide together what to watch?",
    },
    {
      id: "case_58_pm_diagnosis_netflix",
      title: "Netflix",
      subtitle: "Why are early cancellations rising in Mexico?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Netflix, responsible for new member experience in Latin America. In Mexico, the share of new members who cancel within their first 30 days has risen from 12% to 19% over the last two months. Other Latin American countries look stable. Your Head of Product wants to know why and what to do. How would you approach this?",
    },
    {
      id: "case_59_pm_prioritization_netflix",
      title: "Netflix",
      subtitle: "Which ads product grows revenue per member?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Netflix's advertising product. Next half you can build one of three things: better ad targeting using viewing data, new interactive ad formats, or measurement tools that show advertisers whether their ads led to sales. Your director wants to know which one to build and why. How would you approach this?",
    },
    {
      id: "case_60_pm_metrics_experiment_netflix",
      title: "Netflix",
      subtitle: "New artwork lifted clicks 8%. Is it better for members?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Netflix's personalization team. You tested a new way of choosing the artwork -- the image shown for each title on the home screen. In the test, the click-through rate on titles went up 8%. The team wants to roll it out to everyone. Your director asks you to make sure it's actually better for members. How would you evaluate the result?",
    },
    {
      id: "case_61_pm_strategy_netflix",
      title: "Netflix",
      subtitle: "Should Netflix bid for live soccer rights?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Netflix's strategy team for Latin America. The streaming rights to a major regional soccer league are up for auction. Some leaders think live soccer could bring in millions of new members and cut cancellations; others think sports rights are too expensive and not what Netflix is built for. Leadership wants your recommendation on whether to bid, and how much it's worth. How would you approach this?",
    },
    {
      id: "case_14_pm_product_sense_amazon",
      title: "Amazon",
      subtitle: "Design proactive replenishment of household essentials via Alexa.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager on the Alexa devices team at Amazon. Customers can already say 'Alexa, reorder paper towels' to repurchase something they've bought before, but usage of this is low: most people simply forget to reorder essentials until they've already run out. Your team wants to help customers replenish household essentials, things like paper towels, detergent, coffee, before they run out, using Alexa. How would you approach designing this?",
    },
    {
      id: "case_62_pm_diagnosis_amazon",
      title: "Amazon",
      subtitle: "Why are grocery repeat orders dropping in Seattle?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager on Amazon's grocery delivery business. In Seattle, the share of customers who place a second grocery order within 30 days of their first has dropped from 55% to 44% over the last two months. Other cities look normal. Your director wants to know why and what to do. How would you approach this?",
    },
    {
      id: "case_63_pm_prioritization_amazon",
      title: "Amazon",
      subtitle: "Which tool should Amazon build for third-party sellers?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Amazon's seller tools team, which builds software for the independent businesses that sell on Amazon. Next half you can invest in one of three tools: automated pricing that adjusts prices to stay competitive, a simpler way to handle returns, or a tool that helps sellers list their products in other countries. Your director wants a recommendation. How would you decide?",
    },
    {
      id: "case_64_pm_metrics_experiment_amazon",
      title: "Amazon",
      subtitle: "A widget drives 8% of orders. Did it increase sales?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Amazon's homepage. Your team tested a 'Buy it again' widget at the top of the homepage that shows items customers bought before. In the test, the widget was responsible for 8% of all orders, and the team reports it as one of the most successful homepage features ever. Your director asks whether it actually increased sales. How would you evaluate it?",
    },
    {
      id: "case_65_pm_strategy_amazon",
      title: "Amazon",
      subtitle: "Should same-day pharmacy delivery expand to 20 cities?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Amazon's pharmacy business. Today, prescription medicines are mostly delivered in two days, with same-day delivery available in a few large cities. Leadership is debating whether to expand same-day pharmacy delivery to 20 more cities. It's expensive, and pharmacy is a regulated business. They want your recommendation. How would you approach this?",
    },
    {
      id: "case_15_pm_product_sense_jeeves",
      title: "Jeeves",
      subtitle: "Make the corporate card customers actually keep using.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Jeeves, a corporate card and spend-management platform for startups and SMBs across Latin America, the US, and Europe. Companies sign up, get approved, and issue Jeeves cards to their employees, but for a meaningful share of them, Jeeves ends up as a secondary card that gets used for a few months and then fades, rather than becoming the company's primary corporate card. Your Head of Product wants to improve retention by making Jeeves the card that new customers actually keep using. How would you approach this?",
    },
    {
      id: "case_66_pm_diagnosis_jeeves",
      title: "Jeeves",
      subtitle: "Why is card spend per customer falling in Mexico?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Jeeves, a corporate card and spend-management platform for startups and SMBs. In Mexico, card spend per active customer has dropped 20% over the last two months, even though the number of customers keeps growing. Other countries look stable. Your Head of Product wants to know why and what to do. How would you approach this?",
    },
    {
      id: "case_67_pm_prioritization_jeeves",
      title: "Jeeves",
      subtitle: "Accounting integration, supplier payments, or travel?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Jeeves. Next half you can build one of three things: an integration with the accounting software most Latin American SMBs use, a feature to pay suppliers' invoices from Jeeves, or business travel booking. Each has supporters on the team. Your Head of Product wants a recommendation. How would you decide?",
    },
    {
      id: "case_68_pm_metrics_experiment_jeeves",
      title: "Jeeves",
      subtitle: "Spend grew 25% with higher cashback. Was it worth it?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Jeeves. Three months ago you raised cashback on card spend from 1% to 1.5% for all customers in Mexico, as a promotion. Since then, monthly card spend in Mexico has grown 25%. The marketing team wants to make the higher cashback permanent and roll it out to every country. Your CFO asks whether it actually paid off. How would you evaluate it?",
    },
    {
      id: "case_69_pm_strategy_jeeves",
      title: "Jeeves",
      subtitle: "Should Jeeves enter Brazil, and how?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Jeeves' strategy team. Jeeves is growing well in Mexico and Colombia, and leadership wants to enter Brazil, the largest economy in Latin America. Brazil is very attractive, but also different: instant payments are extremely popular, and there are strong local competitors. Leadership wants your recommendation on whether and how to enter. How would you approach it?",
    },
    {
      id: "case_17_pm_product_sense_nubank",
      title: "Nubank",
      subtitle: "Cross-sell more products without extending bad credit.",
      skill: "Product Sense",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Nubank. A large share of customers still only actively use their Nubank credit card and haven't adopted any of Nubank's other products. Leadership wants to grow revenue per customer by getting more of these credit-card-only customers to also adopt personal loans or NuInvest, Nubank's investment product, but the risk team is wary of extending more credit to customers who are still early or inconsistent in their credit history with Nubank. How would you approach growing cross-product adoption without increasing credit risk?",
    },
    {
      id: "case_70_pm_diagnosis_nubank",
      title: "Nubank",
      subtitle: "Why are approved loans not getting disbursed?",
      skill: "Diagnosis",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a Product Manager at Nubank Mexico, working on personal loans. Loan applications are growing, and approval rates are stable. But the share of approved customers who actually complete the process and receive their money has fallen from 70% to 52% over the last six weeks. Your director wants to know why and what to do. How would you approach this?",
    },
    {
      id: "case_71_pm_prioritization_nubank",
      title: "Nubank",
      subtitle: "Pix installments, investments, or business accounts?",
      skill: "Prioritization",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM at Nubank Brazil. Next half you can build one of three things: letting customers pay with Pix in installments, a simple investment product for beginners, or better accounts for small business owners. Each has strong support internally. Your director wants a recommendation tied to the company's goal. How would you decide?",
    },
    {
      id: "case_72_pm_metrics_experiment_nubank",
      title: "Nubank",
      subtitle: "Higher credit limits boosted spend 30%. Roll it out?",
      skill: "Metrics & Experiments",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Nubank's credit card team. Three months ago, you ran a test that automatically raised credit limits for a random group of customers. Customers who got the increase spent 30% more on their cards than the control group, and early delinquency barely changed. The growth team wants to roll it out to all eligible customers. Your Head of Credit asks you to evaluate whether that's the right decision. How would you approach this?",
    },
    {
      id: "case_73_pm_strategy_nubank",
      title: "Nubank",
      subtitle: "Should Nubank launch a mobile phone plan in Mexico?",
      skill: "Strategy & Growth",
      firstMessage: "Welcome to Loudcase, let's get started with the case. You're a PM on Nubank Mexico's strategy team. Leadership is debating whether to launch a mobile phone plan -- prepaid data and calls -- sold inside the Nu app, using another carrier's network. Some see it as a way to bring in new customers and engage existing ones; others see it as a distraction from banking. They want your recommendation. How would you approach this?",
    },
  ],
};
