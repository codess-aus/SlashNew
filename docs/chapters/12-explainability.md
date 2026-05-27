---
title: "12 · Explainability"
description: ""Because the model said so" is not an answer. Designing systems that can tell you why."
---

<div class="sn-hero" markdown>

<a class="sn-back" href="../../">← Back to Blog</a>

<img src="../../assets/12-explainability.png" alt="Hero illustration for chapter 12 — Explainability">

<div class="sn-date">February 16, 2026</div>

</div>

# Explainability

*"Because the model said so" is not an answer. Designing systems that can tell you why.*
## Explanation is a product surface

Explainability isn't a research problem you solve once and tick off. It's a **surface in your product** that you have to design, build and maintain like any other.

The good news: you don't need a PhD in interpretability to do it well. You need to be honest about what you can show.

## A layered approach

Think of explainability as three concentric layers:

1. **What it did** — the action, the inputs, the output, timestamped.
2. **Why it chose that** — the prompt, the retrieved context, the tools called, the confidence.
3. **How the model works at all** — the model card, the training data summary, the known limitations.

Most products only ship layer 1. The trust gap is layers 2 and 3.

## Concrete things you can ship this quarter

- **Citation chips** next to AI-generated answers, linking to the source documents.
- **"Show reasoning"** disclosure that surfaces the plan or chain-of-thought summary.
- **A model card** linked from every AI feature — what it is, what it isn't, who owns it.
- **An audit log** the user can view, not just the platform team.

> If you can't explain it to the user, you can't expect them to trust it. And if you can't explain it to yourself, you shouldn't have shipped it.
