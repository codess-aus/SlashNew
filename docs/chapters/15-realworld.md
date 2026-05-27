---
title: "15 · Real-World Stories"
description: "Patterns and anti-patterns from shipping AI into real systems."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/15-realworld.png" alt="Hero illustration for chapter 15, Real-World Stories">

<div class="sn-cat">Stories</div>

</div>

# Real-World Stories

*Patterns and anti-patterns from shipping AI into real systems.*
## From the field

Rather than tell you specific stories, I want to share the *patterns* that keep showing up when teams ship AI features. None of these are unique. All of them are worth knowing about before you hit them yourself.

## Patterns that tend to work

- **Suggest, don't act.** When the AI proposes and a human approves, the existing review culture does the safety work for you.
- **Route through a PR.** If the agent's output is a pull request, you already have audit, review, rollback and CODEOWNERS for free.
- **Scope tightly.** A small, well-defined task with a narrow blast radius almost always lands better than a broad, ambitious one.
- **Show your work.** Citations, plans and diffs in the UI build more trust than higher accuracy ever will.
- **Have an off switch.** Per feature, per tenant, per tool. Tested.

## Anti-patterns to watch for

- **Approval theatre.** A human is "in the loop" but couldn't realistically review every item in the stream.
- **No blast-radius thinking.** An automation is given the power to take an action it can't reasonably undo.
- **Silent drift.** A model or prompt change ships and nobody notices the behaviour shifted because there were no evals.
- **Hidden AI.** Users can't tell they're talking to an AI, or can't tell *which* parts of the experience were generated.
- **One-way decisions.** The system can act, but the user has no path to challenge, correct or appeal.

## A useful frame

> The system is the unit of reliability, not the model.

The same model can be safe in one product and unsafe in another. The thing you're shipping is the *system around the model*: the prompts, the tools, the guardrails, the UI, the review process, the rollback. That is what you are accountable for.
