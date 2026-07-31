// Fill these in once you've completed agent/VOICE_SETUP.md:
// - backendUrl: the public URL of your deployed server.py (Render/Fly.io/Railway)
// - each case's agentId: the ElevenLabs Agent ID you created for that case
//   (one Agent per case, each pointed at backendUrl as its custom LLM)
//
// Nothing else in this file needs to change to add/remove cases later --
// just add or remove entries in this list, matching the filenames in
// agent/cases/.

const CONFIG = {
  backendUrl: "REPLACE_WITH_YOUR_BACKEND_URL", // e.g. https://case-interviewer.onrender.com

  cases: [
    {
      id: "case_01_profitability_peak_performance",
      title: "Peak Performance Sports",
      subtitle: "Why did profit drop 30% on flat revenue?",
      type: "Consulting",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_02_market_entry_brewco_japan",
      title: "BrewCo",
      subtitle: "Should a craft brewer enter the Japanese market?",
      type: "Consulting",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_03_growth_medequip_new_product",
      title: "MedEquip Co",
      subtitle: "Should a hospital-equipment maker launch a home-health product?",
      type: "Consulting",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_04_pm_satisfaction_drop_figma",
      title: "Figma",
      subtitle: "Why did customer satisfaction drop this quarter?",
      type: "Product",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_05_pm_retention_drop_notion",
      title: "Notion",
      subtitle: "Why did new-user retention drop after an onboarding change?",
      type: "Product",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_06_pm_support_bottleneck_revolut",
      title: "Revolut",
      subtitle: "Why are support tickets and response times spiking?",
      type: "Product",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_07_pm_fraud_increase_stripe",
      title: "Stripe",
      subtitle: "Why is the fraud rate rising for a specific merchant segment?",
      type: "Product",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
    {
      id: "case_08_pm_prioritization_linear",
      title: "Linear",
      subtitle: "Which roadmap initiative should get next quarter's capacity?",
      type: "Product",
      agentId: "REPLACE_WITH_AGENT_ID",
    },
  ],
};
