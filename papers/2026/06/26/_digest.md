# AI Digest — 2026-06-26

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (~20 min)

### PulseLM: A Foundation Dataset and Benchmark for PPG-Text Learning (arXiv:2603.03331)

**Problem.** Photoplethysmography (PPG) is the signal most wearables already collect, but the public datasets for it supply only numerical measurements or task-specific labels. That form of supervision does not support language-based reasoning over the waveform, so it is hard to train or test a model that answers natural-language questions about a PPG segment. The paper sets out to give the field a shared dataset and benchmark for connecting raw PPG to text.

**Method.** The authors aggregate PPG recordings from fifteen public sources and harmonize the mismatched annotations into twelve common physiological question-answering tasks. Every record is standardized into a 10-second segment. Each segment is paired with closed-ended question-answer items, so the benchmark scores a model on multiple-choice physiological questions rather than on free text. They also define fixed preprocessing, supervision, and evaluation protocols, and they build baseline models that pair a dedicated PPG encoder with an instruction-tuned language backbone.

**Result.** The released dataset contains 1.31 million standardized 10-second PPG segments and 3.15 million question-answer pairs, spanning clinical, laboratory, and in-the-wild settings. The authors report this as the first large-scale PPG-text QA dataset. They establish baseline numbers across the twelve question types using the PPG-aware language models, which gives later work a fixed point of comparison for cross-dataset generalization.

**Limitations.** The questions are closed-ended, so the benchmark measures classification accuracy over fixed options rather than open physiological reasoning. The labels are harmonized across fifteen heterogeneous sources, which can introduce mapping noise. The paper is mostly a dataset and protocol contribution, so the baseline models are reference points rather than strong methods.

**Why it matters to Leo.** This sits in the center of the time-series and bio-sensing focus. It moves PPG from a label-prediction setting toward a question-answering setting, which is the same shift that LLM-driven sensing has been heading toward for a year. A standardized PPG-text benchmark with three million pairs is the kind of shared evaluation that makes porting NLP methods to bio-signals measurable instead of anecdotal.

**How this builds on what you know:** PulseLM's closest parents in your library are Sensor2Text (chen2024_sensor2text, Time Series + LLM Integration community) and the Foundation Models for Biosignals survey (gu2025_biosignals, Health AI community), with TS-Agent (liu2025_tsagent, same time-series-plus-LLM community) as a third anchor. Where Sensor2Text produced free-text descriptions from wearable sensor streams for one activity-tracking setting, PulseLM does the same waveform-to-language pairing but at dataset scale and fixes it into a graded closed-ended benchmark, because a shared scoring protocol is what Sensor2Text lacked. This paper extends Sensor2Text, which already crossed the bio-sensing and LLM-health communities in your library (the chen2024_sensor2text to liu2023_health_llm bridge). The new work pushes that bridge further toward standardized, reproducible evaluation rather than single-dataset demonstrations.

---

## Tier B — TLDR (~10 min)

### SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model (arXiv:2601.21031)

SIGMA-PPG is a generative foundation model for PPG that replaces random masking with a learned masking policy. A reinforcement-learning teacher uses statistical priors of the signal (amplitude and skewness) to build a curriculum of hard masks, framed as a teacher-student game, so the student cannot solve reconstruction trivially. The motivation is that PPG is close to periodic, so a random mask leaves an easy gap that the model fills by copying a neighboring beat, which teaches little. On downstream tasks the prior-guided adversarial masking gives better transfer than standard masked reconstruction.

**How this builds on what you know:** The direct parent is How Mask Matters / MAE Theory (zhang2023_mae, [6INGKIJV], in your time-series and computer-vision pages) and the original MAE ([A5HBRQB9]). Where masked autoencoding picks masks at random and shows that a high random mask ratio works for images, SIGMA-PPG argues that random masking is the wrong choice for quasi-periodic signals and learns the mask instead, because the difficulty of the masking task is what controls how much the encoder learns. It is also a direct neighbor of yesterday's HiMAE (hierarchical masked autoencoding for wearable time series), so the two together mark a clear move in bio-signal pretraining from "where to mask at which scale" toward "how hard to make the mask".

### Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models (arXiv:2606.03988)

Vision language models do well on direct perception but fail when the needed information is not visible, such as inferring a view from an unseen angle or tracing a path through an occluded space. The paper introduces Imaginative Perception Tokens (IPT), intermediate tokens that represent what the model would perceive under a different spatial configuration while staying consistent with the actual input. Built on the unified VLM BAGEL and trained on roughly 20K examples across three tasks (perspective taking, path tracing, multiview counting), IPT supervision beats textual chain-of-thought training and raises multiview-counting accuracy by 3.4%, without generating any image at inference. The authors note that forcing the spatial computation through language (textual chain-of-thought) can make performance worse, which points to a modality mismatch.

**How this builds on what you know:** The relevant parent in your library is Chain-of-Thought prompting (wei2023_cot, [HBLPTRMY], NLP page), with the multimodal encoders (the SigLIP family) as the nearest architectural neighbors. Where chain-of-thought externalizes reasoning as a text trace, IPT externalizes it as a perceptual trace in token form, because the paper finds that spatial problems lose information when they are forced into words. The delta is the claim that for spatial tasks the intermediate representation should be perceptual, not linguistic.

### On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM agents (arXiv:2603.12109)

Reinforcement learning with outcome rewards trains LLM agents well on closed reasoning tasks, but it fails in active reasoning, where the agent must ask questions to gather information. The agent falls into "information self-locking": it stops asking informative questions and does not use the evidence it already has. The authors decompose active reasoning into Action Selection (which queries shape the observation stream) and Belief Tracking (how the agent updates belief from evidence), and show that weak versions of both starve exploration during RL, while poor exploration in turn prevents either capability from improving, a feedback loop that pins the agent in a low-information state.

**How this builds on what you know:** The parents are DeepSeek-R1 (deepseek2025_r1, [Z5IWHZAE], LLM page) for RL-with-outcome-rewards reasoning, LATS (zhou2024_lats, [77ERE7HA], Agent page) for tree-structured active exploration, and Chain-of-Thought ([HBLPTRMY]). Where DeepSeek-R1 showed outcome-reward RL produces strong static reasoning, this paper shows the same recipe breaks once the agent must actively collect information, because outcome rewards do not credit the act of asking a good question. This extends the deepseek2025_r1 to wei2023_cot bridge in your library (reasoning-via-RL versus prompting) by naming the specific failure mode that appears when RL reasoning is pushed into interactive, information-seeking settings.

---

## Tier C — scan (~5 min)

- Bio-Inspired Self-Supervised Learning for Wrist-worn IMU Signals (arXiv:2603.10961) — pretraining tricks drawn from biology for wrist IMU streams.
- AnyPPG: An ECG-Guided PPG Foundation Model trained on 100,000+ hours (arXiv:2511.01747) — uses ECG as a guide signal to pretrain a PPG model at scale.
- SignalMC-MED: A Multimodal Benchmark for Biosignal Foundation Models on Single-Lead ECG and PPG (arXiv:2603.09940) — a shared test bed for ECG and PPG foundation models.
- PPG-Distill: Efficient PPG Analysis via Foundation Model Distillation (arXiv:2509.19215) — distills a large PPG model into a small one for on-device use.
- Generalist vs Specialist Time Series Foundation Models on PPG (arXiv:2510.14254) — asks whether a general TS model matches a PPG-specific one for health tasks.
- Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization (arXiv:2604.07165) — tree-structured credit assignment for multi-turn agents.
- ARLArena: A Unified Framework for Stable Agentic Reinforcement Learning (arXiv:2602.21534) — a common harness for comparing agentic RL methods.
- Counterfactual Credit Policy Optimization for Multi-Agent Collaboration (arXiv:2603.21563) — assigns credit by counterfactual contribution in cooperative agents.

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off today). PulseLM and SIGMA-PPG both import a known NLP/CV recipe into PPG. PulseLM ports the vision-language question-answering format (an encoder plus an instruction-tuned language backbone) onto PPG, which matches the Time Series + LLM Integration community already in your library. SIGMA-PPG ports masked-autoencoder pretraining onto PPG and goes one step past it with a learned mask; combined with yesterday's HiMAE, the masked-reconstruction direction for PPG is now well covered. AnyPPG and SignalMC-MED are also in the "ported" column: cross-modal guidance and shared benchmarking are standard practice carried into bio-signals.

Unported opportunity. Imaginative Perception Tokens (arXiv:2606.03988) has no analogue in time-series or bio-sensing. Transfer hypothesis: train a physiological model to emit "imagined" intermediate tokens that represent what the signal would look like under a different but consistent state (for example, the same subject at a higher heart rate or under motion), and use those tokens as a supervision channel for reasoning about unobserved physiological conditions, in the same way IPT supervises unobserved viewpoints. This would test whether perceptual-token supervision beats text-trace supervision for bio-signals, which is the exact comparison IPT runs in the visual domain.

A second, smaller opportunity: the parallel diffusion-language decoding used by PerceptionDLM (yesterday's multimodal paper) has not been applied to multi-channel sensor captioning, where describing many channels one at a time is the current bottleneck.

---

## News

Anthropic released Claude Opus 4.8, which took the top spot on the Artificial Analysis Intelligence Index and leads SWE-bench Pro at 69.2%. Google released Gemini 3.5 Pro and the low-latency Gemini 3.1 Flash-Lite. Reports also describe an Anthropic "Fable 5" reasoning model with a 1M-token context; note that coverage around the Fable 5 and Mythos 5 line includes a June 12 US government order to pull both on national security grounds, so treat the status of that specific release as unsettled until confirmed.

---

End of digest. Close this tab when done.
