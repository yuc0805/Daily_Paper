# AI Digest — 2026-06-02

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### Towards a General Intelligence and Interface for Wearable Health Data (Narayanswamy, McDuff et al., 2026)
arXiv: https://arxiv.org/abs/2605.22759

Problem. Wearable sensors record a lot of behavioral and physiological signal, but turning low-level streams into personal health states is hard. People differ in baseline health, physiology, and lifestyle, so the same raw signal means different things across individuals. Paired labels (signal plus a confirmed health outcome) are expensive to collect and cannot be added after the fact, so labeled data stays scarce.

Method. The authors pretrain a foundation model on more than one trillion minutes of unlabeled sensor signal from about five million participants. They then test whether scaling model size together with data volume improves downstream health prediction. On top of the frozen representation, they run a "classroom" of LLM agents that automatically search the space of small predictive heads (which embedding, which architecture, which target), rather than hand-designing one head per task. The best heads are then wrapped in a Personal Health Agent that answers health questions in natural language.

Result. Across 35 health prediction tasks (cardiovascular, metabolic, sleep, mental health, plus lifestyle and demographic targets), joint scaling of model and data gives steady gains. The representation supports label-efficient few-shot learning and generation of daily metric estimates. The LLM-agent head search improves results further, and the gain grows with the capacity of the LLM doing the search. The Personal Health Agent was rated by clinicians across 1,860 ratings as more relevant, contextually aware, and safe.

Limitations. The pretraining cohort and signal types are tied to one large wearable ecosystem, so transfer to other devices and populations is not shown. The 35 tasks are prediction tasks, not clinical trial endpoints, so "improvement" is measured against held-out labels, not patient outcomes. The LLM-agent head search adds compute and a second model whose failure modes are not fully characterized. Clinician ratings measure perceived quality, not diagnostic accuracy.

Why it matters to Leo. This sits in the center of Leo's primary area: a population-scale self-supervised model for wearable physiological signals, with an LLM interface on top. It is the clearest current example of the time-series-plus-LLM stack he tracks, built at a scale individual labs cannot match.

How this builds on what you know: The pretraining recipe extends "Foundation Models for Biosignals (Gu 2025)" and "SSL for HAR with 700K person-days (Yuan 2024)", both in your Health-AI-and-Self-Supervised community (Community 1). Where Yuan 2024 showed self-supervised pretraining on 700K person-days helps activity recognition, this paper does the same idea at roughly a thousand times the data (one trillion minutes, five million people) and adds scaling-law evidence, because the question has moved from "does SSL help" to "how far does it scale". The LLM interface layer extends "LLMs are Few-Shot Health Learners (Liu 2023)": where Liu 2023 fed sensor-derived numbers into a prompt, this paper trains predictive heads on a learned representation and lets LLM agents pick the heads. This paper also extends the Sensor2Text bridge (Chen 2024), which already crossed bio-sensing (Community 4) and llm-health (Community 1) in your library by turning sensor data into language; the new work pushes that bridge further by replacing the hand-built captioning path with a scaled representation and an agentic head-search.

---

## Tier B — TLDRs

### QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks (Xie et al., 2026)
arXiv: https://arxiv.org/abs/2605.24218

QUEST is an open family of deep research agents (2B to 35B parameters) trained to handle long-horizon search: fact seeking, citation grounding, and report synthesis. The training recipe combines mid-training, supervised fine-tuning, and reinforcement learning, fed by a data-synthesis pipeline built on "rubric trees" that produce tasks with checkable rewards and no human labels. Using only 8K synthesized tasks, QUEST approaches or beats closed-source agents on eight deep-research benchmarks and is the best open-weight agent reported. Models, data, and training scripts are released.

How this builds on what you know: QUEST builds on "Agent AI Survey (Durante 2024)" and "Memory Mechanisms Survey (Huang 2026)", both in your LLM-Agents-and-Reasoning community (Community 0), and reuses the RL-for-reasoning recipe from "DeepSeek-V3 (2024)". Where the surveys map out agent capabilities and DeepSeek-V3 showed RL post-training at model scale, QUEST does the narrower thing of training a search agent end to end on synthetic verifiable tasks, because the bottleneck for deep research agents is labeled long-horizon trajectories, which the rubric-tree synthesis sidesteps.

### MemForest: An Efficient Agent Memory System with Hierarchical Temporal Indexing (Chen et al., 2026)
arXiv: https://arxiv.org/abs/2605.23986

MemForest treats agent memory as a write-efficient temporal data-management problem rather than a flat global summary. It breaks the usual sequential update pipeline with parallel chunk extraction, and introduces MemTree, a time-ordered hierarchical index that replaces full-state rewrites with localized per-node updates along affected tree paths. On LongMemEval-S it reaches 79.8% pass@1, best among stateful baselines, while sustaining memory-construction throughput about 6 times higher than prior systems including EverMemOS. It is also evaluated on LoCoMo.

How this builds on what you know: MemForest builds on "Memory Mechanisms Survey (Huang 2026)" in your LLM-Agents-and-Reasoning community (Community 0). Where the survey catalogs memory designs and notes the cost of rewriting state, this paper does the engineering: a temporal index with per-node updates so write cost scales with what changed, not with total memory, because growing latency from full-state rewrites is the practical limit the survey identified.

### Reinforcing Few-step Generators via Reward-Tilted Distribution Matching (Huang et al., 2026)
arXiv: https://arxiv.org/abs/2605.26108

RTDMD is a two-stage method for aligning few-step image generators with human preferences. It shows that minimizing KL divergence to a reward-tilted teacher splits cleanly into a distribution-matching term and a reward-maximization term. Stage one (Ambient-Consistent Distribution Matching Distillation) does subinterval-wise matching with a consistency regularizer; stage two jointly optimizes both terms with a hybrid policy gradient (a GRPO-style estimator for stochastic steps plus direct reward backprop through the final deterministic step), reduced-variance via step-subset GRPO. With 4 inference steps it sets new state of the art on SD3, SD3.5, and FLUX.2 across preference, aesthetic, and compositional metrics; the distilled FLUX.2 4B beats the 9B teacher (50 steps) on most rewards.

How this builds on what you know: RTDMD builds on "DDPM (Ho 2020)" and "DiT (Peebles 2023)" in your Vision-Language-and-Generative community (Community 3). Where DDPM defined the many-step denoising process and DiT made the backbone a scalable transformer, this paper does the opposite of adding steps: it distills to four steps and then uses reward RL to recover preference alignment, because the open problem in distilled generators is that speed-ups lose the human-preference tuning that full diffusion sampling allowed.

---

## Tier C — scan

- WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation — tests world models over multiple interaction turns, not single rollouts. https://arxiv.org/abs/2605.25874
- Macaron-A2UI: A Model for Generative UI in Personal Agents — generates interface elements on the fly inside a personal agent. https://arxiv.org/abs/2605.24830
- ThriftAttention: Selective Mixed Precision for Long-Context FP4 Attention — keeps most attention in FP4 and spends precision only where it matters. https://arxiv.org/abs/2605.23081
- CUA-Gym: Scaling Verifiable Training Environments for Computer-Use Agents — builds checkable environments and tasks to train GUI agents. https://arxiv.org/abs/2605.25624
- Channel-wise Vector Quantization — quantizes each feature channel separately instead of one shared codebook. https://arxiv.org/abs/2605.26089
- SkillEvolBench: Benchmarking the Evolution from Episodic Experience to Procedural Skills — measures whether agents turn one-off episodes into reusable skills. https://arxiv.org/abs/2605.24117
- Faithfulness Metrics Do Not Measure Faithfulness: A Meta-Evaluation with Ground Truth — shows common faithfulness metrics disagree with known ground truth. https://arxiv.org/abs/2605.25052
- Language Models Need Sleep — studies offline consolidation phases for language models. https://arxiv.org/abs/2605.26099

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off). Today's Tier A wearable foundation model is the main bio-sensing item, and it closes a known opportunity: population-scale self-supervised pretraining, with scaling-law evidence and an LLM interface, is now done for wearable physiological signals. This matches the hyperedges in Community 1 (Health AI and Self-Supervised) and Community 5 (Wearable Sensing and Behavior). The "scale masked self-supervised pretraining to wearables" idea is no longer low-hanging fruit.

Unported opportunity 1: per-channel vector quantization. "Channel-wise Vector Quantization" (2605.26089) quantizes each channel with its own codebook. Multivariate biosignals (ECG, PPG, accelerometer, temperature) are exactly multi-channel and often lose channels when a sensor drops out. Transfer hypothesis: a per-channel VQ tokenizer would give a discrete biosignal vocabulary that degrades gracefully under channel dropout, which a shared patch embedding does not handle well.

Unported opportunity 2: hierarchical temporal indexing for long signal history. MemForest's MemTree (2605.23986) is a write-efficient, time-ordered index built for agent memory. A person's multi-month wearable stream has the same structure. Transfer hypothesis: a MemTree-style index over an individual's signal history would support label-efficient retrieval and updates without rewriting the whole representation when new days arrive, a fit for the continual-update setting wearable models face.

---

## News

These come from model-release trackers and are reported with the usual caution that fast-moving release claims can be wrong. Trackers list Anthropic Claude Opus 4.6 (1M-token context) as current, with reports of a larger Claude "Mythos 5" and a mid-sized model in circulation; Google Gemini 3.x adding real-time voice and image analysis; and Meta's Muse series (Muse Spark) from earlier in spring 2026. None of these is a research paper, and none changes today's reading list. Check primary sources before citing any of them.

---

End of digest. Close this tab when done.
