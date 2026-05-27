---
title: "17 · Governance"
description: "How to do AI governance without becoming the team everyone routes around."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/17-governance.png" alt="Hero illustration for chapter 17, Governance">

<div class="sn-cat">Leadership</div>

</div>

# Governance

*How to do AI governance without becoming the team everyone routes around.*
## The two failure modes

Most AI governance programs fail in one of two ways:

1. **Too heavy.** Every feature requires a 40-page review. Teams route around you. Shadow AI flourishes.
2. **Too light.** Anyone can ship anything. Eventually something embarrassing happens. The pendulum swings to (1).

The goal is the middle: **light-touch, high-trust, well-instrumented.**

## A starter governance model

- **A short standard.** Two pages, not eighty. Plain English.
- **A tiered risk model.** Low / Medium / High based on blast radius, data sensitivity, and reversibility. The tier determines the rigor.
- **A self-serve checklist** for Low and Medium. A real review for High.
- **A central inventory.** You can't govern what you can't see. Every AI feature, with an owner, a tier, and a link to its evals.
- **A no-blame reporting channel** for AI incidents and near-misses. Treat it like security.

## Make the right thing the easy thing

The most successful governance teams I've worked with don't *gate*, they *enable*. They ship:

- A blessed prompt library.
- A blessed eval harness.
- A blessed agent framework with safety defaults on.
- A template repo that has all of the above wired up.

When the paved road is the safest road, governance is just "use the paved road."
