---
title: "11 · Principles That Hold"
description: "The six Microsoft Responsible AI principles, and how they translate into engineering behaviour."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back</a>

<img src="../../assets/11-principles.png" alt="Hero illustration for chapter 11 — Principles That Hold">

<div class="sn-cat">Framework</div>

</div>

# Principles That Hold

*The six Microsoft Responsible AI principles, and how they translate into engineering behaviour.*
## The six, briefly

Microsoft's Responsible AI principles are:

1. **Fairness** — treat people equitably.
2. **Reliability & Safety** — perform as intended, safely.
3. **Privacy & Security** — protect data and systems.
4. **Inclusiveness** — work for the full range of human experience.
5. **Transparency** — be understandable.
6. **Accountability** — humans remain responsible.

They sound abstract. They aren't. Each one maps to engineering behaviour you already know how to do.

## The engineering translation

| Principle | What it means in your repo |
|---|---|
| Fairness | Disaggregated evals across user segments. Bias tests in CI. |
| Reliability & Safety | Eval suite, red team, regression budget, kill switch. |
| Privacy & Security | Data minimization, secret scanning, threat model that names the LLM. |
| Inclusiveness | A11y baked in, multilingual evals, diverse test data. |
| Transparency | Model cards, disclosure copy, citations in UI, audit logs. |
| Accountability | A named owner, a runbook, a process for harm reports. |

## A working test

For each principle, ask: *"What would I show a regulator to demonstrate we take this seriously?"*

If the honest answer is "a slide deck," you have a gap. If the answer is "a CI job, an owner, and a Friday review meeting," you're shipping responsibly.
