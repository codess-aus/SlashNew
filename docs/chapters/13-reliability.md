---
title: "13 · Reliability & Safety"
description: "Evals, red teaming, regression budgets — reliability as a first-class engineering metric."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back to Blog</a>

<img src="../../assets/13-reliability.png" alt="Hero illustration for chapter 13 — Reliability & Safety">

<div class="sn-date">February 16, 2026</div>

</div>

# Reliability & Safety

*Evals, red teaming, regression budgets — reliability as a first-class engineering metric.*
## Reliability is the unsexy superpower

Everyone wants to talk about capability. The teams quietly winning are the ones who treat **reliability** as a first-class metric, with the same rigour they'd apply to latency or uptime.

## The reliability stack

- **Offline evals.** A golden set of prompts with expected behaviour, run in CI. Block merges on regression.
- **Online evals.** Sample real traffic, score it, dashboard it. Watch trends weekly.
- **Red teaming.** Adversarial prompts, jailbreaks, prompt injection — done by a dedicated rotation, not "whoever is free."
- **Regression budgets.** A defined tolerance for behavioural drift. When you blow the budget, you stop, you don't ship around it.
- **Kill switches.** Per-feature, per-tenant, per-tool. Tested quarterly. Documented.

## Safety as architecture

Treat safety the way you treat security: as architecture, not vibes.

- **Input filters** for known-bad patterns.
- **Output filters** for sensitive categories.
- **Tool sandboxing** so the agent can't do what it shouldn't, even if it tries.
- **Rate limits** and **scope limits** as primary safety controls — not afterthoughts.

## Further reading

- [Microsoft Learn — Evaluate generative AI models](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
