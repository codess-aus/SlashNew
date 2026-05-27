---
title: "07 · Human in the Loop"
description: "HITL done well is empowering, not theatre. A practical pattern catalogue."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back to Blog</a>

<img src="../../assets/7-hitl.png" alt="Hero illustration for chapter 07 — Human in the Loop">

<div class="sn-date">February 16, 2026</div>

</div>

# Human in the Loop

*HITL done well is empowering, not theatre. A practical pattern catalogue.*
## HITL is not a checkbox

Half the "human in the loop" systems I've reviewed are theatre. There's a human, technically, looking at a stream of approvals at 3 a.m., clicking "yes" 400 times in a row. That isn't oversight. That's a rubber stamp with a salary.

Real HITL has three properties:

1. **The human has the information they need to decide.**
2. **The human has the time and authority to say no.**
3. **Saying no has a clean, low-friction path.**

If any of those is missing, you don't have a human in the loop. You have a human on the hook.

## A pattern catalogue

| Pattern | When to use it |
|---|---|
| **Plan-then-approve** | Multi-step agentic work (refactors, migrations). |
| **Sample review** | High-volume low-stakes decisions (tagging, triage). |
| **Escalation on uncertainty** | Model confidence below threshold → route to human. |
| **Dual control** | Irreversible or sensitive actions (prod deploys, customer comms). |
| **Audit-only** | Fully automated, but every action is reviewable after the fact. |

Pick the pattern that matches the **blast radius** of the decision, not the convenience of the team.

## A heuristic

> If a human couldn't reasonably review **one** action in this stream, you should not be reviewing **all** of them. Either reduce the stream, raise the threshold, or change the pattern.
