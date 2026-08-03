# AI Digest — 2026-08-03

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on the day: fresh, well-indexed papers were moderate today. One paper qualified cleanly for Tier A in your primary area (wearable time series), and it is a dataset and benchmark release rather than a new model, which is worth a careful look because it changes what you can compare against.

---

## Tier A — deep read

### OpenMHC: Accelerating the Science of Wearable Foundation Models (arXiv:2607.16235)

**Problem.** The largest wearable datasets are private, and the strongest wearable foundation models are rarely released with open weights or reproducible training code. This makes it hard to compare methods fairly or to reproduce reported numbers, which slows progress in exactly the area you work in.

**Method.** The authors release OpenMyHeartCounts (OpenMHC), built from more than a decade of the My Heart Counts study app. It contains more than 60 million hours of wearable data across 19 sensor channels (for example step count, heart rate, sleep, workouts) and up to 169 linked variables covering health, lifestyle, mood, and behavior, from 11,894 consenting participants. Alongside the data they release open-source implementations of recent wearable foundation models and a single benchmark with three tracks: downstream health and behavior prediction, multivariate imputation, and time-series forecasting.

**Result.** The contribution is the dataset, the reference model code and weights, and the shared benchmark, all released together at a scale that has not been openly available before. They report benchmark comparisons of classical methods against recent wearable and multivariate time-series foundation models across the three tracks. There is no single headline accuracy number, because the point is a standard testbed rather than one new model.

**Limitations.** The data comes from one study app and one recruited cohort, so coverage of devices, demographics, and clinical conditions is not uniform. A benchmark also fixes a set of tasks, which can steer the field toward those tasks and away from problems the benchmark does not measure.

**Why it matters to Leo.** This lands in your working area and gives you a public dataset, reference models, and a benchmark you can run your own methods against. The imputation and forecasting tracks match the fragmented-wearable-gap problem from yesterday's zero-shot HRV forecasting paper, so the two connect directly.

**How this builds on what you know:** The closest parents in your library are GLOBEM (Xu 2023, Wearable Sensing community) and the Foundation Models for Biosignals survey (Gu 2025, Health AI community), with Self-supervised Learning for HAR at 700K person-days (Yuan 2024) as a third anchor. Where GLOBEM gave a multi-year, multi-site behavior dataset with a cross-dataset generalization benchmark, and where Yuan 2024 showed self-supervised pretraining works at very large scale on a single accelerometer stream, OpenMHC releases a broader open dataset plus open model weights and a three-track benchmark in one package, because the blocking problem is now reproducibility and fair comparison rather than whether pretraining works at all. This paper extends the Sensor2Text-to-few-shot-health bridge that already crossed Wearable Sensing and Health AI in your library. The new work pushes the bridge toward standardized evaluation: it links raw sensor channels to health and mood outcomes inside one benchmark, rather than inside one model.

---

## Tier B — TLDRs

### SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution (arXiv:2607.26784)

Standard agentic reinforcement learning treats each task as an independent episode, so an agent cannot carry a reusable solution pattern from one task to a related one. SkillRise trains a single policy that alternates between solving a task and curating an evolving "skill document" that it passes to the next task, with separate credit assignment for solving (rewarded by the current task) and for curation (rewarded by discounted downstream outcomes). On ALFWorld, WebShop, and ScienceWorld it gives the best Pass@1 among compared methods, with gains of 2.3 to 8.5 percentage points over the strongest baseline, and it shows test-time scaling across tasks, meaning performance rises with longer sequences of related tasks even when each is attempted only once.

**How this builds on what you know:** The nearest parents are DeepSeek-R1 (2025, LLM Agents and Reasoning community), which established reinforcement learning with verifiable rewards for reasoning, and the survey Rethinking Memory Mechanisms of Foundation Agents (Huang 2026) in the same community. Where DeepSeek-R1 improves a policy within a task using outcome rewards, SkillRise adds a second, cross-task learning signal that rewards writing down transferable skills, because the goal is reuse across tasks rather than mastery of one. Where the memory survey catalogs how agents store and recall information, SkillRise makes the memory itself a learned object that the reward function shapes.

### CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization (arXiv:2607.25659)

Rubric-based reinforcement learning scores a model's output against explicit criteria, but in GRPO-style training those rich per-criterion judgments collapse into one response-level reward that is spread evenly across every token, so there is no way to give more credit to the tokens that actually satisfied a criterion. CoRT rescoring the same sampled response twice, once under the rubric-conditioned prompt and once under a matched criteria-free prompt, and uses the token-by-token log-likelihood difference as a proxy for how much each token depends on the rubric. It maps these differences to bounded, response-normalized weights and redistributes the GRPO advantage across tokens, with no auxiliary scoring model and no change to the response-level reward. Across instruction-tuned models it improves over matched response-level GRPO by 4.4 percentage points on average.

**How this builds on what you know:** The closest parent is DeepSeek-R1 (2025, Reasoning community), whose GRPO training is exactly the pipeline CoRT modifies, with Chain-of-Thought Prompting (Wei 2023) as the older reasoning anchor. Where DeepSeek-R1 assigns one advantage to the whole response, CoRT splits that advantage across tokens using the model's own likelihood contrasts, because uniform credit wastes the fine-grained signal a rubric already contains. Where Chain-of-Thought exposes reasoning steps in text, CoRT does not change the text; it changes which tokens the update rewards.

### Can AI agents conduct open-ended AI research? Early evidence from two case studies (arXiv:2607.27191)

The paper introduces "shadow evaluations": a frontier agent takes the central open-ended research question of a high-quality unpublished paper, and the paper's original authors grade the agent's output. On two unpublished NeurIPS 2026 submissions, given six days and thousands of dollars of compute, agents completed all of the engineering without human help but could not make substantial progress on the research questions, and both outputs were rejected by the authors. The authors name five recurring failure modes: poor judgment about the bar for publishable work, uncreative responses to design flaws, weak backtracking from dead ends, poor resource awareness, and instruction drift; a second model and scaffold reproduced the pattern.

**How this builds on what you know:** The nearest parents are the Agent AI survey (Durante 2024) and Rethinking Memory Mechanisms of Foundation Agents (Huang 2026), both in the LLM Agents and Reasoning community. Where those works map what agents can do and how they remember, this paper measures whether agents can drive an open research question end to end, because prior evaluations either test narrow verifiable tasks or lean on overstretched peer review. The result marks the boundary: the engineering is handled, the research judgment is not.

---

## Tier C — scan

- DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space — co-evolves a solver and a rubric writer instead of fixing the rubric. arXiv:2607.25675
- OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding — ties agent success to dollar value on office workflows. arXiv:2607.27155
- TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM — pushes a VLA policy to real-time on consumer hardware. arXiv:2607.27205
- CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition — tests in-context learning in vision-language models past simple grounding. arXiv:2607.25294
- GPT-Red: Automated Red Teaming via Self-Play at Scale — generates adversarial prompts by self-play rather than human authoring. arXiv:2607.26115
- SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Response — measures agents on security incident handling. arXiv:2607.26791
- Explicit Layer Modeling for Video Object Insertion and Layer Decomposition — inserts objects into video by learning explicit layers. arXiv:2607.25802
- StealthBench: Measuring Operational Stealth in Autonomous Offensive-Security Agents — scores how detectable an autonomous security agent is. arXiv:2607.26314

---

## Tier D — Time-series / Bio-sensing Gap Watch

Today's time-series and bio-sensing paper is OpenMHC, which is a dataset and benchmark rather than a method. Its three tracks sit on top of work that is already ported into your library: masked-reconstruction and multivariate-time-series-foundation-model pretraining applied to wearables (Community 4, Time Series + LLM Integration, and Community 5, Wearable Sensing) already cover zero-shot forecasting and imputation on wearable streams. So the modeling recipe OpenMHC benchmarks is closed off as low-hanging fruit; the open value is the shared testbed itself.

Two unported opportunities stand out from today's top reasoning papers:

First, CoRT's token-level credit assignment through counterfactual replay has not been applied to time-series reasoning agents. Transfer hypothesis: in an agent like TS-Agent, rescore a response with and without the numeric evidence log, then give more credit to the tokens that depend on real operator outputs than to narrative tokens, which would push the policy toward evidence-grounded claims rather than fluent guesses.

Second, SkillRise's evolving skill document has not been applied to time-series analysis. Transfer hypothesis: let an agent curate reusable statistical-analysis skills (for example a change-point routine or a seasonality check) across many datasets, so a single policy accumulates a transferable analysis toolkit rather than re-deriving each analysis per dataset.

---

## News

Only carrying items with a clear model or product release. The most recently tracked frontier model is DeepSeek-V4-Flash-0731, released July 31, 2026. From late July, Anthropic shipped Claude Opus 5 (reported within 0.5% of Claude Fable 5 on CursorBench 3.2 at about half the cost per task), OpenAI launched GPT-5.6 (Sol, Terra, Luna), Moonshot released Kimi K3 (2.8 trillion parameters, the largest open-weights release so far), and Thinking Machines released its first model, the 975B Inkling. No new frontier model has been tracked yet for August 3.

---

End of digest. Close this tab when done.
