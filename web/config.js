// Fill these in once you've completed agent/VOICE_SETUP.md:
// - backendUrl: the public URL of your deployed server.py (Render/Fly.io/Railway)
// - agentId: ONE shared ElevenLabs Agent ID (not per-case -- a single Agent
//   serves the whole library; which case runs is chosen per conversation
//   via the widget's dynamic-variables attribute, see session.html).
//
// To add a case to the library later, just add an entry to this list --
// matching a filename in agent/cases/ -- nothing else needs to change.

const CONFIG = {
  backendUrl: "https://pm-interviewer-production.up.railway.app",
  agentId: "REPLACE_WITH_AGENT_ID",

  cases: [
    {
      id: "case_01_profitability_peak_performance",
      title: "Peak Performance Sports",
      subtitle: "Why did profit drop 30% on flat revenue?",
      type: "Consulting",
    },
    {
      id: "case_02_market_entry_brewco_japan",
      title: "BrewCo",
      subtitle: "Should a craft brewer enter the Japanese market?",
      type: "Consulting",
    },
    {
      id: "case_03_growth_medequip_new_product",
      title: "MedEquip Co",
      subtitle: "Should a hospital-equipment maker launch a home-health product?",
      type: "Consulting",
    },
    {
      id: "case_04_pm_satisfaction_drop_figma",
      title: "Figma",
      subtitle: "Why did customer satisfaction drop this quarter?",
      type: "Product",
    },
    {
      id: "case_05_pm_retention_drop_notion",
      title: "Notion",
      subtitle: "Why did new-user retention drop after an onboarding change?",
      type: "Product",
    },
    {
      id: "case_06_pm_support_bottleneck_revolut",
      title: "Revolut",
      subtitle: "Why are support tickets and response times spiking?",
      type: "Product",
    },
    {
      id: "case_07_pm_fraud_increase_stripe",
      title: "Stripe",
      subtitle: "Why is the fraud rate rising for a specific merchant segment?",
      type: "Product",
    },
    {
      id: "case_08_pm_prioritization_linear",
      title: "Linear",
      subtitle: "Which roadmap initiative should get next quarter's capacity?",
      type: "Product",
    },
  ],
};
