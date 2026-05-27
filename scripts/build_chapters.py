#!/usr/bin/env python3
"""One-shot generator for the 22 chapter markdown pages.

Run once: `python scripts/build_chapters.py`. Re-running overwrites.
"""
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "chapters"
OUT.mkdir(parents=True, exist_ok=True)

DATE = "February 16, 2026"  # kept for reference; not rendered on chapter pages

# (slug, image, number, title, category, lede, body_markdown)
CHAPTERS = [
    (
        "00-welcome", "0-title.png", "00", "Welcome to SlashNew", "Opening",
        "Why we're here, who this talk is for, and the one question we keep coming back to.",
        """
## Hello, SlashNew

Thanks for being here. I'm **@Codess-Aus**, and I want to talk to you about something that has been on my mind a lot: we are shipping AI faster than we are learning to govern it.

That isn't a doom statement. I'm wildly optimistic about where this is going. But optimism without rigor is just marketing. So this talk is the rigor I wish someone had handed me eighteen months ago.

## Who this is for

- Engineers and platform teams adopting Copilot, agents, or LLM-backed features.
- Tech leads who have to answer "is it safe to ship?" on a Friday afternoon.
- Anyone whose name is on the change that goes live on Monday.

## The one question

> *Would I trust this system to make this decision about me, my family, or my customer?*

That's it. That's the whole talk. The next 21 chapters are just different ways of getting to a confident **yes**.
""",
    ),
    (
        "01-agenda", "1-agenda.png", "01", "The Agenda", "Opening",
        "A roadmap through trust, oversight, governance and the three waves of AI that brought us here.",
        """
## What we'll cover

1. **Rule Zero**, the non-negotiable that sits above every other decision.
2. **The Right Way**, what Microsoft's Responsible AI Standard actually asks of us.
3. **Trust as UX**, designing for confidence, not just correctness.
4. **Human in the loop**, patterns that work, and theatre that doesn't.
5. **Principles, explainability, reliability, inclusivity**, the engineering translation.
6. **Real-world stories**, lessons from the field.
7. **The three waves**, autocomplete, chat, agents.
8. **Governance and empathy**, leading teams through the change.
9. **Take action**, five things to do on Monday.

## How to read this

Each chapter is short on purpose. You should be able to skim the whole thing in a coffee break, or sink into one chapter for a team discussion. There are no slides hidden from you, this site *is* the talk.
""",
    ),
    (
        "02-rulezero", "2-rulezero.png", "02", "Rule Zero", "Foundation",
        "Before you ship anything else, ship trust. The rule that frames every decision after it.",
        """
## Rule Zero

> **Don't ship AI you wouldn't be comfortable being on the receiving end of.**

That's it. Everything else in this talk, the principles, the eval suites, the governance boards, is just engineering against that one rule.

## Why we need a rule above the rules

Standards are great. The [Microsoft Responsible AI Standard](https://www.microsoft.com/ai/responsible-ai), the NIST AI Risk Management Framework, the EU AI Act, they're all genuinely useful. But standards describe the floor. Rule Zero describes the **posture**.

You can comply with every standard on earth and still ship something gross. We've all seen it. The model card was fine. The DPIA was filed. And the product still made someone's day worse.

## A quick test

Before your next AI feature ships, ask three questions out loud, in a room, with at least one person who didn't build it:

1. **Who is this decision being made *about*?**
2. **What happens to them on the worst-case output?**
3. **Could they tell, appeal, or opt out?**

If you can answer those three crisply, you're probably on the right side of Rule Zero. If they make the room uncomfortable, good. That discomfort is the signal.
""",
    ),
    (
        "03-therightway", "3-therightway.png", "03", "The Right Way", "Foundation",
        "Microsoft's Responsible AI Standard, in plain English. What it actually asks of you on a Tuesday.",
        """
## The Standard, decoded

Microsoft's Responsible AI Standard is a comprehensive document, and most of your team will never read it cover to cover. That's fine. Here's the working version.

The Standard asks you, for every AI feature, to be able to answer:

| Question | Where it lives in your team |
|---|---|
| What is this system *for*? | Product spec, one paragraph, plain English. |
| Who could it harm, and how? | Impact Assessment (lightweight is fine to start). |
| How do we know it works? | Eval suite, with regression guardrails. |
| How will users know what it is? | UX copy, disclosures, model cards. |
| What happens when it's wrong? | Fallback path, human handoff, appeal. |
| Who is accountable? | A name. Not a team. A name. |

## A Tuesday-sized practice

You don't need a Responsible AI center of excellence to start. You need:

- A **one-page impact note** at the top of every feature doc.
- An **eval harness** that runs on every PR that touches the prompt, the model, or the tools.
- A **named owner** in the README.

Those three artefacts will get you a long way toward what the Standard is asking for, today.

## Further reading

- [Microsoft Responsible AI Standard v2](https://www.microsoft.com/ai/responsible-ai)
- [Microsoft Learn, Responsible AI principles](https://learn.microsoft.com/training/modules/responsible-ai-principles/)
""",
    ),
    (
        "04-trust", "4-trust.png", "04", "Earning Trust", "Foundation",
        "Trust isn't a feature you toggle on. It's a UX, a process and a contract.",
        """
## Trust is a UX problem

Engineers love to treat trust as a *correctness* problem. "If the model is right enough, people will trust it."

That isn't how humans work. People trust systems that are:

- **Predictable**, same input, same shape of answer.
- **Legible**, I can see what it did and why.
- **Recoverable**, when it's wrong, I can fix it without drama.
- **Bounded**, I know what it *won't* do.

A highly accurate model that nobody trusts is less useful than a slightly less accurate one that an entire team relies on. The difference is almost always one of those four things.

## The trust contract

Treat every AI feature as a contract with the user:

> *"I will tell you what I'm about to do, do it inside these bounds, show you what I did, and let you undo it."*

If your feature can't honour that sentence, the answer isn't "ship anyway and add a disclaimer." The answer is "go back to design."

## A concrete pattern

For agentic actions in GitHub Copilot, the trust contract often looks like:

1. **Plan**, show the steps before running.
2. **Confirm**, let the human approve, edit or reject.
3. **Execute**, stream the work, file by file.
4. **Diff**, show what changed, in a reviewable form.
5. **Revert**, one button, no questions.

That loop is why people trust agent mode. Take any of those steps out and trust collapses.
""",
    ),
    (
        "05-themoment", "5-themoment.png", "05", "The Moment", "Context",
        "We're inside the inflection. Why \"general-purpose reasoning in the IDE\" changes the shape of every team.",
        """
## This is the moment

I want to be careful with hype. But something genuinely new is happening in software.

For a long time, the bottleneck on a team has been **typing-speed-of-thought**, how fast we can translate an idea into working code. We're now living through the first technology that meaningfully moves that bottleneck.

That doesn't mean engineers are obsolete. It means the *shape* of engineering is changing.

## What's actually different

- **The unit of work is shrinking.** Issues become PRs in minutes, not days.
- **The skill mix is shifting.** Reading code, reviewing changes, and writing crisp specs are now leverage.
- **Time-to-first-feedback is collapsing.** You can prototype five approaches in the time it used to take to scaffold one.

## What hasn't changed

- Production is still production.
- Security still matters.
- Your customers still notice when things break.
- The senior engineer in the room is still the one who knows *which* of the five prototypes is the right one to ship.

The moment is real. The fundamentals are the same.
""",
    ),
    (
        "06-feature", "6-feature.png", "06", "It's a Feature, Not a Bug", "Mindset",
        "Hallucinations, uncertainty, refusal, sometimes they're the product working.",
        """
## Reframing the "bug" list

When people complain about LLMs, the complaints usually land in three buckets:

1. **It made things up.**
2. **It refused to do the thing I asked.**
3. **It said it wasn't sure.**

Here's the uncomfortable take: all three are often the product working as intended.

## Hallucination as a calibration problem

A model that generates fluent, plausible text *will* generate fluent, plausible text even when it doesn't know. That's not a bug, that's how generative systems behave. The bug is shipping that text without **grounding** (retrieval, tools, citations) and without a UX that signals uncertainty.

Fix the system, not the model.

## Refusal as a safety feature

A model that refuses to help you write a phishing email is doing exactly what we want. Yes, refusals are sometimes over-broad. Yes, that's annoying. But "annoyingly cautious" is a better default than "cheerfully harmful."

## "I'm not sure" as a gift

If your model can tell you it's uncertain, **expose that in the UI**. A confidence band, a "verify this" badge, a citation link, these are how you turn a probabilistic system into a trustworthy one.

The features we used to call bugs are the surface area you build trust on top of.
""",
    ),
    (
        "07-hitl", "7-hitl.png", "07", "Human in the Loop", "Practice",
        "HITL done well is empowering, not theatre. A practical pattern catalogue.",
        """
## HITL is not a checkbox

A lot of "human in the loop" systems end up as theatre. There's a human, technically, looking at a stream of approvals, clicking "yes" over and over. That isn't oversight. That's a rubber stamp.

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
""",
    ),
    (
        "08-amplify", "8-amplify.png", "08", "Amplify, Don't Replace", "Mindset",
        "The teams winning with Copilot aren't replacing engineers. They're amplifying judgment.",
        """
## The replacement framing is wrong

A lot of commentary frames AI as replacing engineers. That framing is mostly wrong, and it's mostly wrong in the same way: it confuses **tasks** with **jobs**.

Yes, a lot of tasks I used to do by hand, boilerplate, scaffolding, first-draft docs, glue code, are now one prompt away. That's good. None of that was the job.

The job was, and is:

- Understanding the problem.
- Designing a system that fits the constraints.
- Making trade-offs you can defend.
- Owning the outcome when it ships.

## Amplification in practice

Teams that thrive with Copilot tend to share a few habits:

- They **review every diff** the agent produces, the same way they'd review a junior engineer's PR.
- They invest in **specs and tests** more than they used to, because those are the artefacts that steer the agent.
- They treat the model as a **fast collaborator**, not an oracle.
- They keep a **"what we don't let it touch"** list, and review it every quarter.

## A useful question

Before you let an agent do something on your behalf, ask: *"If this were a new hire on day one, would I let them do this unsupervised?"*

The answer is your governance model.
""",
    ),
    (
        "09-oversight", "9-oversight.png", "09", "Meaningful Oversight", "Practice",
        "Approval buttons aren't oversight. What real, decision-grade human review looks like.",
        """
## Oversight ≠ approval UI

I want to drive this point home with a hammer. **Approval is a UI pattern. Oversight is a system property.**

You can have approval everywhere and oversight nowhere. The signs:

- The same person approves everything.
- Approvals happen in seconds, on a phone, between meetings.
- There's no audit trail of *why* something was approved.
- "Reject" is a worse user experience than "approve."

## What meaningful oversight looks like

- **Diversity.** More than one person can review. Reviewers rotate.
- **Context.** Reviewers see the inputs, the plan, the model's reasoning and the proposed action, together.
- **Time.** There's a reasonable SLA, not "instant or it blocks production."
- **Symmetry.** Rejecting is as easy as approving, and rejection produces a useful artefact (a comment, a label, a follow-up issue).
- **Audit.** Every decision is queryable months later.

## The GitHub-shaped version

GitHub gives you most of this for free: pull requests, required reviewers, branch protections, audit logs, CODEOWNERS. If your AI system is producing changes that live outside that system, you have rebuilt, badly, what you already had.

> Whenever possible, **make the agent's output a PR**, and let your existing review culture do the work.
""",
    ),
    (
        "10-dm", "10-dm.png", "10", "Decision Making with AI", "Practice",
        "How to use models for decisions that matter, without outsourcing accountability with them.",
        """
## Decisions vs. drafts

Models are excellent at **drafting**. They are dangerous when used for **deciding** without scaffolding.

The trick is to be honest about which mode you're in.

| Mode | The model's role | The human's role |
|---|---|---|
| Drafting | Generate options, expand the search space. | Pick, edit, approve. |
| Filtering | Narrow a large set against criteria. | Define criteria, audit samples. |
| Deciding | Recommend, with reasoning. | Decide, on the record. |
| Acting | Execute approved decisions. | Define guardrails, monitor. |

You get into trouble when you slide from one mode to the next without noticing, usually from "filtering" into "deciding" because the volume got too high to review.

## A decision-grade checklist

For any AI-assisted decision that affects a person:

- [ ] The decision criteria are written down, separately from the model.
- [ ] The model's recommendation is recorded *with its reasoning*.
- [ ] A human is named as the decider.
- [ ] The affected person can ask why, and get a real answer.
- [ ] There is a path to challenge the decision.

If you can't tick those five, you are not making a decision, you are *delegating accountability* to a system that can't hold it.
""",
    ),
    (
        "11-principles", "11-principles.png", "11", "Principles That Hold", "Framework",
        "The six Microsoft Responsible AI principles, and how they translate into engineering behaviour.",
        """
## The six, briefly

Microsoft's Responsible AI principles are:

1. **Fairness**, treat people equitably.
2. **Reliability & Safety**, perform as intended, safely.
3. **Privacy & Security**, protect data and systems.
4. **Inclusiveness**, work for the full range of human experience.
5. **Transparency**, be understandable.
6. **Accountability**, humans remain responsible.

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
""",
    ),
    (
        "12-explainability", "12-explainability.png", "12", "Explainability", "Framework",
        "\"Because the model said so\" is not an answer. Designing systems that can tell you why.",
        """
## Explanation is a product surface

Explainability isn't a research problem you solve once and tick off. It's a **surface in your product** that you have to design, build and maintain like any other.

The good news: you don't need a PhD in interpretability to do it well. You need to be honest about what you can show.

## A layered approach

Think of explainability as three concentric layers:

1. **What it did**, the action, the inputs, the output, timestamped.
2. **Why it chose that**, the prompt, the retrieved context, the tools called, the confidence.
3. **How the model works at all**, the model card, the training data summary, the known limitations.

Most products only ship layer 1. The trust gap is layers 2 and 3.

## Concrete things you can ship this quarter

- **Citation chips** next to AI-generated answers, linking to the source documents.
- **"Show reasoning"** disclosure that surfaces the plan or chain-of-thought summary.
- **A model card** linked from every AI feature, what it is, what it isn't, who owns it.
- **An audit log** the user can view, not just the platform team.

> If you can't explain it to the user, you can't expect them to trust it. And if you can't explain it to yourself, you shouldn't have shipped it.
""",
    ),
    (
        "13-reliability", "13-reliability.png", "13", "Reliability & Safety", "Framework",
        "Evals, red teaming, regression budgets, reliability as a first-class engineering metric.",
        """
## Reliability is the unsexy superpower

Everyone wants to talk about capability. The teams quietly winning are the ones who treat **reliability** as a first-class metric, with the same rigour they'd apply to latency or uptime.

## The reliability stack

- **Offline evals.** A golden set of prompts with expected behaviour, run in CI. Block merges on regression.
- **Online evals.** Sample real traffic, score it, dashboard it. Watch trends weekly.
- **Red teaming.** Adversarial prompts, jailbreaks, prompt injection, done by a dedicated rotation, not "whoever is free."
- **Regression budgets.** A defined tolerance for behavioural drift. When you blow the budget, you stop, you don't ship around it.
- **Kill switches.** Per-feature, per-tenant, per-tool. Tested quarterly. Documented.

## Safety as architecture

Treat safety the way you treat security: as architecture, not vibes.

- **Input filters** for known-bad patterns.
- **Output filters** for sensitive categories.
- **Tool sandboxing** so the agent can't do what it shouldn't, even if it tries.
- **Rate limits** and **scope limits** as primary safety controls, not afterthoughts.

## Further reading

- [Microsoft Learn, Evaluate generative AI models](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
""",
    ),
    (
        "14-inclusivity", "14-inclusivity.png", "14", "Inclusivity by Design", "Framework",
        "If it doesn't work for everyone, it doesn't work. Practical inclusivity for agentic products.",
        """
## Inclusivity is a quality metric

Inclusive design isn't a separate workstream you do after the feature ships. It is one of the **definitions of "works."**

A model that performs brilliantly for one demographic and poorly for another isn't "mostly working." It is **broken for the people it doesn't serve**, and you should treat it that way.

## A practical playbook

- **Disaggregate your evals.** Don't just report aggregate accuracy. Slice by language, region, dialect, ability, age, device.
- **Include disabled users in research.** Not as a checkbox at the end, as participants from week one.
- **Test with assistive tech.** Screen readers, voice control, switch input, high contrast. If your AI UI breaks under a screen reader, the whole feature is broken.
- **Write copy for the widest plausible reader.** Plain language, defined acronyms, no idioms that don't travel.
- **Localize, don't just translate.** A literal translation of an English UI is rarely an inclusive UI.

## Where AI specifically helps

Agentic AI is genuinely amazing for accessibility, voice interfaces, summarization, real-time translation, alt-text generation. We have a responsibility to ship those wins, not just talk about them.

> Build for the edges and the middle takes care of itself. Build only for the middle and you leave people behind.
""",
    ),
    (
        "15-realworld", "15-realworld.png", "15", "Real-World Stories", "Stories",
        "Patterns and anti-patterns from shipping AI into real systems.",
        """
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
""",
    ),
    (
        "16-3waves", "16-3waves.png", "16", "The Three Waves", "Context",
        "From autocomplete, to chat, to agents. Where you sit on the wave changes what \"good\" looks like.",
        """
## Three waves, three mindsets

We've lived through three distinct waves of developer AI in a very short time.

### Wave 1, Autocomplete

Inline suggestions. Low stakes. The human is in the driver's seat for every keystroke. "Good" means *useful suggestions that don't slow me down*.

### Wave 2, Chat

Conversational assistants in the IDE and the browser. The human asks, the model answers. "Good" means *accurate, grounded, well-cited answers I can act on*.

### Wave 3, Agents

The model takes multi-step actions on your behalf, using tools, across files, sometimes across systems. The human reviews **outcomes**, not keystrokes. "Good" now means *predictable plans, reviewable diffs, and reversibility*.

## Why this matters

The governance model that worked for Wave 1, basically, "let people use it", does not work for Wave 3. Agents change:

- The **blast radius** (multi-file, multi-system).
- The **review surface** (plans and diffs, not lines).
- The **failure modes** (silent drift, tool misuse, scope creep).
- The **trust contract** (you're now approving *intent*, not *output*).

If your team is in Wave 3 with Wave 1 governance, you will have a bad week. Build the governance for the wave you're actually on.
""",
    ),
    (
        "17-governance", "17-governance.png", "17", "Governance", "Leadership",
        "How to do AI governance without becoming the team everyone routes around.",
        """
## The two failure modes

Most AI governance programs fail in one of two ways:

1. **Too heavy.** Every feature requires a long, heavy review. Teams route around you. Shadow AI flourishes.
2. **Too light.** Anyone can ship anything. Eventually something embarrassing happens. The pendulum swings to (1).

The goal is the middle: **light-touch, high-trust, well-instrumented.**

## A starter governance model

- **A short standard.** Two pages, not eighty. Plain English.
- **A tiered risk model.** Low / Medium / High based on blast radius, data sensitivity, and reversibility. The tier determines the rigor.
- **A self-serve checklist** for Low and Medium. A real review for High.
- **A central inventory.** You can't govern what you can't see. Every AI feature, with an owner, a tier, and a link to its evals.
- **A no-blame reporting channel** for AI incidents and near-misses. Treat it like security.

## Make the right thing the easy thing

The most successful governance teams don't *gate*, they *enable*. They ship:

- A blessed prompt library.
- A blessed eval harness.
- A blessed agent framework with safety defaults on.
- A template repo that has all of the above wired up.

When the paved road is the safest road, governance is just "use the paved road."
""",
    ),
    (
        "18-empathy", "18-empathy.png", "18", "Leading with Empathy", "Leadership",
        "Your team is anxious about AI. That's data. How leaders turn fear into capability.",
        """
## The fear is rational

If you lead a team right now, some of your people are scared. Some of them won't say it. Some of them are over-performing *because* they're scared.

The fear is rational. The discourse around "AI replacing engineers" is loud, often careless, and aimed straight at them. Even if you know the framing is wrong, they're still hearing it every day.

## What leaders can actually do

- **Say the quiet part out loud.** Acknowledge the fear in a 1:1. Not to fix it. To name it.
- **Be specific about what changes and what doesn't.** "Your job is to ship great software" doesn't change. The toolkit does.
- **Invest in learning time.** Not "go figure it out on weekends." Actual hours, on the clock, with goals.
- **Reward judgment, not output volume.** If your metrics reward lines of code, you are about to learn an expensive lesson.
- **Make space for skepticism.** The engineer who says "I don't trust this for production" is doing their job. Don't punish them for it.

## A small ritual

Run a monthly "what surprised us" session. Half an hour. Three slots:

1. Something the AI did well.
2. Something it did badly.
3. Something we changed because of it.

The ritual normalizes both wins and losses. It turns AI from a scary outside force into a thing the team is *learning together*.
""",
    ),
    (
        "19-actions", "19-actions.png", "19", "Take Action", "Closing",
        "Five concrete things to do on Monday. No theory. Just the next move.",
        """
## Monday morning, five things

If you only do five things from this talk, do these.

### 1. Inventory

List every AI feature in your product. Owner, tier, link to evals. Put it in a wiki. Update it monthly. You cannot govern what you cannot see.

### 2. Write Rule Zero on the wall

Literally. A sticker, a Slack pin, a banner in your repo template. Make it impossible to ship without bumping into it.

### 3. Stand up an eval harness

Pick **one** AI feature. Write 20 prompts with expected behaviour. Run them in CI. Block merges on regression. You'll thank yourself within a month.

### 4. Make the agent's output a PR

If you have any agentic system writing changes, route it through a pull request with required reviewers. Reuse the review culture you already have.

### 5. Schedule a "what surprised us" session

Half an hour. Once a month. With the team. See [Chapter 18, Leading with Empathy](18-empathy.md).

## That's it

You don't need to boil the ocean. You need to ship the next thing **responsibly**, then the one after that. Compound interest does the rest.
""",
    ),
    (
        "20-resources", "20-resources.png", "20", "Resources", "Closing",
        "Microsoft Learn paths, GitHub docs, books and tools, the curated reading list behind the talk.",
        """
## Microsoft Learn

- [Responsible AI principles and approach](https://learn.microsoft.com/training/modules/responsible-ai-principles/)
- [Evaluate generative AI models](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai)
- [Plan and prepare to develop AI solutions responsibly](https://learn.microsoft.com/training/paths/responsible-ai-business-principles/)
- [Microsoft Cloud Adoption Framework, AI](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/)

## GitHub

- [GitHub Copilot trust center](https://copilot.github.trust.page/)
- [GitHub Copilot documentation](https://docs.github.com/copilot)
- [Building responsibly with GitHub Copilot (GitHub Blog)](https://github.blog/)
- [GitHub Advanced Security](https://docs.github.com/code-security)

## Standards & frameworks

- [Microsoft Responsible AI Standard v2](https://www.microsoft.com/ai/responsible-ai)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [EU AI Act, high-level summary](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Books I keep coming back to

- *Weapons of Math Destruction*, Cathy O'Neil
- *The Alignment Problem*, Brian Christian
- *Atlas of AI*, Kate Crawford
- *Designing Machine Learning Systems*, Chip Huyen

## The meta-resource

> Whatever you read, **read with your own product in your head**. Theory only becomes practice when you can name the line of code it would change.
""",
    ),
    (
        "21-trust", "21-trust.png", "21", "Closing, Trust, Again", "Closing",
        "We end where we started. Trust isn't a slide at the end of the deck. It's the whole product.",
        """
## Back to the beginning

We started with one question:

> *Would I trust this system to make this decision about me, my family, or my customer?*

Everything in between, the principles, the evals, the governance, the empathy, was just engineering toward a confident **yes**.

## The takeaway

You are going to ship AI. A lot of it. Faster than you ever shipped anything else. That is genuinely exciting, and it is genuinely a lot of responsibility.

The good news: the playbook isn't mysterious. It looks like the playbook for every other piece of high-stakes software you've ever shipped:

- **Know who it's for.**
- **Know what it does, and what it doesn't.**
- **Test it like you mean it.**
- **Make it reviewable.**
- **Own it when it's wrong.**
- **Tell the truth in the UI.**

Do those six things, again and again, and trust shows up.

## Thank you

Thank you for sitting through this. Thank you for the work you're going to do next week that nobody will see, the eval you'll add, the disclosure you'll write, the "no" you'll say. That work is how this whole thing stays good.

I'm **@Codess-Aus**. Come find me. Let's keep building.

, *Scaling Guacamole, SlashNew Conf 2026.*
""",
    ),
]


def render(slug, image, number, title, category, lede, body):
    hero = textwrap.dedent(f"""\
    ---
    title: "{number} · {title}"
    description: "{lede}"
    ---

    <div class="sn-hero" markdown>

    <a class="sn-back" href="../../">← Back</a>

    <img src="../../assets/{image}" alt="Hero illustration for chapter {number}, {title}">

    <div class="sn-cat">{category}</div>

    </div>

    # {title}

    *{lede}*
    """)
    return hero + body.lstrip("\n")


def main():
    for ch in CHAPTERS:
        slug, image, number, title, category, lede, body = ch
        path = OUT / f"{slug}.md"
        path.write_text(render(slug, image, number, title, category, lede, body), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
