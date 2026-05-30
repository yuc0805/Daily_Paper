# AI Digest — 2026-05-30

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 6 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1)

### Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning
Arxiv: 2605.02073 | cs.CL | https://arxiv.org/abs/2605.02073

**Problem.** Reinforcement learning is the standard way to push a language model toward better mathematical reasoning, but the result depends heavily on the reward function. Most work tunes the model and treats the reward as fixed. This paper holds the base model fixed and treats the reward specification itself as the thing to optimize.

**Method.** A frontier language model proposes candidate reward functions. Each candidate is checked automatically, then screened with a short 500-step Group Relative Policy Optimization (GRPO) run on a Llama-3.2-3B-Instruct base with Low-Rank Adaptation (LoRA), and ranked by F1 on the GSM8K test set. The ranked summary from each round is fed back into the next round of proposals, so the search learns from its own history. Five rounds produce 50 candidate rewards, after which the top rewards are combined into ensembles.

**Result.** Mean F1 rises from 0.596 in round 1 to 0.632 in round 5, and the best single reward reaches F1 = 0.787. The best ensemble reaches F1 = 0.795 (95% bootstrap CI [0.756, 0.832]) and accuracy 0.660, a 0.19 absolute F1 gain over a base-rewards-only GRPO baseline (F1 = 0.609). A three-seed retraining of the best ensemble holds at F1 = 0.785. A control ensemble of five randomly drawn rewards collapses to F1 = 0.047, which shows the ranked-feedback loop, not simply the count of rewards, drives the gain.

**Limitations.** Results are on one base model (3B) and one benchmark (GSM8K), with LoRA rather than full fine-tuning. Whether the searched rewards transfer to larger models or to reasoning outside grade-school math is not tested. The reward-proposing model is a frontier system, so part of the gain is borrowed capability from a stronger model.

**Why it matters to Leo.** This reframes RL post-training as reward search rather than policy search. For someone porting reasoning methods into time-series and health agents, it is a cheap lever: you can hold a small fixed base model and improve it by searching reward functions, which matters when biosignal labels are scarce and full RL fine-tuning is costly.

**How this builds on what you know:** The direct parents in your library are DeepSeek-R1 (Z5IWHZAE, Community 0, reasoning) and Chain-of-Thought Prompting (HBLPTRMY, Community 0), with DeepSeek-V3 (2JCKA7GI) as the architecture backdrop. Where DeepSeek-R1 produced reasoning by running large-scale RL that reshapes the policy, this paper freezes the policy and moves the search to the reward function, because it argues the reward is the under-explored design lever once the base model is fixed. This paper extends the DeepSeek-R1 to Chain-of-Thought bridge already recorded in your library (cross_area_bridge deepseek2025_r1 to wei2023_cot, "reasoning-via-rl vs prompting"). The new work pushes that bridge further toward reward engineering: it keeps R1's RL machinery but asks what signal it should optimize, sitting between R1's policy-learning view and CoT's prompt-level view of where reasoning comes from.

---

## Tier B — TLDRs (3)

### Assessing the Operational Viability of Foundation Models for Time Series Forecasting
Arxiv: 2605.24381 | cs.LG | https://arxiv.org/abs/2605.24381

Large time-series foundation models promise zero-shot forecasting without task-specific training, but it is not clear they earn their inference cost in production. This paper (Google) compares foundation models against industry-standard supervised forecasters on real workloads and finds the answer depends on series complexity. It proposes a Complexity Router that reads simple empirical features of each series and sends it to the cheapest model class that will handle it, so easy series go to light supervised models and only hard series pay for the foundation model. The reported effect is higher accuracy and much lower inference cost than deploying one universal foundation model everywhere.

**How this builds on what you know:** The parents in your library are LLMs for Time Series: A Survey (N2JLZBY3, graphify community 4) and TS-Agent (I2CIT4I7, community 4, a god node for time-series). Where the survey and TS-Agent argued for large language-model-style systems applied to time series, this paper does the opposite accounting: it measures when that heavy machinery is not worth it and routes around it, because real deployment cares about cost per forecast, not only accuracy. This is a counter-weight to Community 4's "bigger model, more language integration" direction.

### Squeezing Capacity from Multimodal Large Language Models for Subject-driven Generation
Arxiv: 2605.26111 | cs.CV | https://arxiv.org/abs/2605.26111

Subject-driven image generation means putting a specific subject (a particular person, object, or pet) into new generated scenes from a few reference images. This paper conditions a diffusion generator on a multimodal language model that jointly encodes the text prompt and the reference images, and adds VAE-based identity conditioning so the subject's appearance is preserved. The new piece is a Dual Layer Aggregation module that combines features from several layers of the language model rather than reading only the last layer, which gives a richer conditioning signal. The result is better identity preservation and prompt-following on subject-driven benchmarks.

**How this builds on what you know:** The parents are DALL-E 2 (DUERBZGM, community 3) and DiT (YJ9TK993, community 3), with DDPM (GX7WR7KA) as the diffusion base. Where DALL-E 2 conditioned image generation on a single CLIP text-image embedding and DiT showed a Transformer can replace the diffusion backbone, this paper does multi-level conditioning, because it argues one pooled embedding throws away layer-specific detail needed to keep a subject's identity. It stays inside the Vision-Language and Generative community but moves the conditioning interface from one vector to an aggregated stack.

### GARD: Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction
Arxiv: 2605.26230 | cs.CV | https://arxiv.org/abs/2605.26230

Feed-forward 3D reconstruction models are trained on clean images but used on real photos that carry blur, noise, and other degradations, which breaks them. GARD runs a diffusion-based restoration step, but instead of cleaning the raw images it denoises directly in the feature space of the feed-forward reconstruction model. Because that feature space already carries geometry, denoising there recovers accurate scene structure rather than just prettier pixels. The method improves reconstruction quality under degraded inputs without retraining the reconstructor from scratch.

**How this builds on what you know:** The direct parent is DDPM (GX7WR7KA, community 3), the denoising-diffusion base; the closest neighbor on the model side is DiT (YJ9TK993). Where DDPM denoises in pixel or latent image space, GARD does the denoising inside a task model's geometry-aware feature space, because the goal is correct 3D structure, not a clean image. It is a small but useful relocation of diffusion: move the noise model to wherever the downstream task keeps its information.

---

## Tier C — scan headlines (6)

- AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks — single vs multi-agent gaps on real clinical data. https://arxiv.org/abs/2605.10286
- GroupMemBench: Benchmarking LLM Agent Memory in Multi-Party Conversations — tests assistant memory when several people are talking. https://arxiv.org/abs/2605.14498
- Cattle Trade: A Multi-Agent Benchmark for LLM Bluffing, Bidding, and Bargaining — strategic reasoning in a long-horizon trading game. https://arxiv.org/abs/2605.14537
- NeuroAgent: LLM Agents for Multimodal Neuroimaging Analysis — automates preprocessing across sMRI, fMRI, dMRI, and PET. https://arxiv.org/abs/2605.06584
- Empirical Evaluation of Time Series Foundation Models for Electricity Price Forecasting in Belgium — Chronos-2, Chronos-Bolt, TimesFM 2.5 on day-ahead prices. https://arxiv.org/abs/2605.17045
- STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation — already in your graph; autoregressive flows as Transformers for text-image generation. https://arxiv.org/abs/2605.08029

---

## Tier D — Time-series / Bio-sensing Gap Watch

Today's time-series papers are both already-ported cases. 2605.24381 (foundation-model routing for forecasting) and 2605.17045 (foundation models for electricity prices) sit inside graphify Community 4 (Time Series + LLM Integration): they apply large pretrained forecasters and cost-aware routing to numeric series, which is the established direction, so neither opens new transfer ground. There are no wearable or biosignal papers today (Community 5 quiet).

Two unported opportunities from today's vision and generative papers:

First, GARD's feature-space diffusion denoising (2605.26230). The method cleans degraded inputs inside the geometry-aware feature space of a downstream model rather than in raw signal space. Transfer hypothesis: run the same trick on motion-corrupted PPG or ECG by denoising in the embedding space of a biosignal foundation model (Gu 2025 biosignals survey, 2XWEG7AF) instead of filtering the raw waveform, so artifact removal is judged by downstream health-task geometry, not waveform smoothness. Not yet present in Community 4 or 5.

Second, STARFlow2's autoregressive-normalizing-flow-as-Transformer idea (2605.08029). It builds a flow that shares the causal mask and KV-cache of a language model. Transfer hypothesis: an autoregressive flow that shares an LLM's cache could give exact-likelihood probabilistic time-series forecasting jointly with language reasoning over the same series, which Community 4's current LLM-for-time-series systems do not provide (they give point or sampled forecasts, not exact likelihoods). Unported.

---

## News — model and product releases

One notable release this cycle. At Google I/O (May 19, 2026) Google announced Gemini 3.5 Flash, a lighter model it prices at roughly one-half to one-third of comparable frontier models, and Gemini Spark, a general-purpose agent in the Gemini app that reasons across connected apps, in beta for trusted testers and Google AI Ultra subscribers. No major Anthropic, OpenAI, Meta, or xAI model release landed in the last day; trackers note several labs are between releases. (Source: CNBC, May 19, 2026.)

---

Quiet-ish day for Leo's primary area: only one fresh time-series paper (2605.24381) qualified, and it is a cost-accounting result rather than a new method. If you want a method to read instead, a backlog option from last week is 2605.20449 (LLM Pretraining Shapes a Generalizable Manifold: Cross-Modal Transfer to Time Series), already in your graph as a Tier A.

End of digest. Close this tab when done.
