# AI Digest — 2026-07-15

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1)

### STELLA: Efficient Sensor-to-LLM Translation for On-Device Human Activity Recognition
arXiv 2607.03089 — https://arxiv.org/abs/2607.03089

Problem. Language-model activity recognition has so far meant either long text prompts around sensor data or fine-tuning a large backbone. Both are too heavy for a watch or phone, and both tend to move private physiological data to a server. The question is whether the reasoning of a language model can be kept while the cost drops enough to run on the device.

Method. STELLA treats the task as sensor tokenization rather than prompting or compression. A light hierarchical tokenizer turns raw multi-scale sensor windows into compact, activity-aware tokens, which a frozen language model reads. Only the tokenizer and a per-user personalization layer are learned; the language model's weights never change. Personalization runs locally, so private data stays on the device.

Result. The paper reports that this design consistently improves recognition, produces stronger sensor representations than generic time-series tokenizers, and stays practical for real-time on-device use. The headline claim is accurate, private, and personalized language-model sensing that fits an edge compute budget. (Exact accuracy tables are in the paper; treat the numbers as the two-page test.)

Limitations. The language model is frozen, so gains are bounded by what a fixed reader can do with good tokens. Streaming, multi-day input and continual on-device personalization are touched but not fully solved.

How this builds on what you know: Where Sensor2Text (community 4, Time Series + LLM in your library) produced language from sensors using heavy trainable backbones, STELLA freezes the model and moves the work into a small tokenizer, because that is what makes on-device use possible. Where SSL for HAR (Yuan 2024, community 1) pretrained an encoder to fine-tune later, STELLA does not fine-tune the language model at all. This paper extends Sensor2Text, which already crossed bio-sensing and llm-health in your library (the Sensor2Text to LLMs-Few-Shot-Health edge). The new work pushes that bridge further toward on-device efficiency: the same sensor-to-language idea, now with a cost budget a watch can meet.

Why it matters to Leo. This is directly in the primary working area. It plants the frozen-LLM-plus-lightweight-tokenizer recipe in wearable HAR, which means that particular move is now closing off as low-hanging fruit. The open room is streaming multi-day input and continual personalization.

---

## Tier B — TLDR (3)

### Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation
arXiv 2607.11886 — https://arxiv.org/abs/2607.11886

The paper proposes SpectraReward, a training-free reward for reinforcement-learning fine-tuning of image generators. Instead of scoring an image, it measures how well the original prompt can be recovered from the generated image in a single teacher-forced forward pass, and uses that average log-likelihood as the reward. It reuses a frozen multimodal model's image-text alignment with no preference labels and no reward-model training, and is validated across two diffusion models, three RL algorithms, nine backbones from 4B to 235B, and five out-of-distribution benchmarks.

How this builds on what you know: DDPM and DiT (both community 3 in your library) define how to sample images but say nothing about how to grade them during RL. Where prior reward methods trained a scorer on human preferences or decomposed the prompt into questions, SpectraReward reads the prompt back out of the image and uses the recovery likelihood, because a well-aligned model already assigns higher likelihood to matching prompts. SigLIP, the natural alignment anchor, is not in your library yet, so the closest neighbors are the community-3 generative anchors DDPM and DiT.

### SIRI: Self-Internalizing Reinforcement Learning with Intrinsic Skills for LLM Agent Training
arXiv 2606.02355 — https://arxiv.org/abs/2606.02355

SIRI is a three-phase RL method that lets a long-horizon agent discover, validate, and absorb reusable skills without an external skill generator and without a skill bank at inference. It warms up the policy to collect successful skill-free trajectories, then has the policy summarize skills from its own rollouts and check them by comparing skill-augmented against skill-free runs, and finally distills only the helpful skill-guided action tokens back into the plain policy. The deployed agent keeps the accuracy benefit while carrying no extra context or retrieval latency.

How this builds on what you know: Where DeepSeek-R1 (community 0) used RL to produce long reasoning traces, SIRI uses RL to mine and internalize skills, then removes them from the runtime. Where ADaPT (Prasad 2023, community 0) relied on an external decomposition module, SIRI mines skills from the policy's own successful trajectories, because that removes the extra module and its cost. This sits next to the DeepSeek-R1 to Chain-of-Thought bridge in your library, which contrasted reasoning-via-RL with reasoning-via-prompting; SIRI extends the RL side from eliciting reasoning to compressing and reusing procedural skill.

### Extending LLM Context via Associative Recurrent Memory
arXiv 2607.11614 — https://arxiv.org/abs/2607.11614

The paper gives a training recipe for extending usable context with an associative recurrent memory transformer. It combines continued pre-training, synthetic long-context data, a length curriculum, and selective placement of memory into chosen layers rather than all of them. The augmented model processes inputs well past its original limit, and the reported lesson is that layer placement and data curriculum matter more than adding memory everywhere.

How this builds on what you know: Where Attention Is All You Need (Vaswani 2017, community 2) keeps information inside a fixed window, this work carries a compressed recurrent state across segments to grow effective context without full quadratic attention. Where the Memory Mechanisms Survey (Huang 2026, community 0) only catalogued options, this commits to one and supplies the curriculum that makes it hold up. Both parents are in your library.

---

## Tier C — scan (8)

Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution — asks and answers repo questions before attempting a fix. https://arxiv.org/abs/2607.11111
Multimodal Unlearning Across Vision, Language, Video, and Audio: A Survey — how to remove sensitive cross-modal associations from trained models. https://arxiv.org/abs/2607.07907
Efficient and Adaptive Human Activity Recognition via LLM Backbones — uses a language-model backbone for adaptive HAR. https://arxiv.org/abs/2605.12019
HiMAE: Hierarchical Masked Autoencoders for Wearable Time Series — resolution-specific structure discovery in wearable signals. https://arxiv.org/abs/2510.25785
GEAR: Granularity-Adaptive Advantage Reweighting for LLM Agents via Self-Distillation — reweights advantage by granularity for agent RL. https://arxiv.org/abs/2605.11853
Skill Reuse as Compression in Agentic RL — frames reusable skills as a compression objective. https://arxiv.org/abs/2605.31509
Visual-Redundancy-Controlled Parallel Decoding for Diffusion MLLMs — speeds up diffusion multimodal decoding by cutting visual redundancy. https://arxiv.org/abs/2605.25820
Steering Visual Generation in Unified Multimodal Models with Understanding Supervision — uses understanding signals to steer generation. https://arxiv.org/abs/2605.05781

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closing as low-hanging fruit). STELLA ports the frozen-LLM-plus-learned-tokenizer recipe into wearable HAR, matching Community 4 (Time Series + LLM) and Community 5 (Wearable Sensing) hyperedges. HiMAE ports hierarchical masked autoencoding into wearable time series, which sits inside the Community 1 masked-autoencoder plus Community 5 wearable region. Treat both mechanisms as done for the sensor case.

Unported opportunity 1: prompt-recovery likelihood as a training-free reward (from SpectraReward, 2607.11886). No time-series or bio-sensing work in your library uses recover-the-description log-likelihood as a reward. Transfer hypothesis: use a frozen sensor-language model's log-likelihood of an activity or symptom description, given a synthesized or augmented sensor window, as a label-free reward for generative sensor synthesis or data augmentation.

Unported opportunity 2: selective-layer associative recurrent memory for ultra-long streams (from ARMT, 2607.11614). Long-context memory has not been applied to multi-day continuous wearable streams. Transfer hypothesis: place associative recurrent memory in a few layers of a biosignal encoder to compress weeks of IMU or PPG into a fixed-size state for on-device longitudinal health modeling, avoiding a fixed window over the whole record.

---

## News

OpenAI reached general availability of the GPT-5.6 family on 9 July, a three-part lineup (Sol for high-end reasoning and science, Terra at roughly GPT-5.5 quality for half the cost, Luna for fast high-volume work). Meta shipped Muse Spark 1.1 on 9 July, a multimodal reasoning model with a self-managed 1-million-token context window and native agent orchestration, and began charging developers through the Meta Model API. Anthropic's Claude Sonnet 5 (launched 30 June) remains the current default with a 1-million-token context window at introductory pricing through 31 August.

---

End of digest. Close this tab when done.
