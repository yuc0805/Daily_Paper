# AI Digest — 2026-07-19

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1 paper)

### SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning (arXiv:2607.14777)

**Problem.** Training an LLM to act as a long-horizon agent (multi-turn tool use with environment feedback) is usually done with outcome-based reinforcement learning: the model gets one reward at the end of a trajectory. That single trajectory-level signal says nothing about which intermediate decisions were good or bad, so there is a supervision gap between the episode-level outcome and the token-level updates the policy actually needs.

**Method.** SEED makes one policy checkpoint play two roles at the same time. First it acts in the environment and collects its own on-policy trajectories. Then the same model reads back its completed trajectories and writes short natural-language "skills" that capture a reusable workflow, a decisive observation, or a rule for avoiding a past failure. Finally it distills the effect of those skills back into the ordinary policy: it measures how the skill changes the model's action probabilities and trains the plain (skill-free) policy to reproduce that shifted behavior. Because the teacher and the student are the same evolving checkpoint, the loop is self-evolving rather than dependent on a fixed stronger model.

**Result.** The authors report that converting completed trajectories into hindsight skills and distilling them closes part of the outcome-to-token supervision gap, improving long-horizon agentic performance over plain outcome-based RL baselines. Code is released (github.com/jinyangwu/SEED). Read the paper for the exact per-benchmark deltas; the first two pages state the mechanism clearly enough to pass the two-page test.

**Limitations.** The quality of a distilled skill depends on the model's own ability to describe why a trajectory worked. A weak self-analysis step can distill a wrong lesson, and the paper's gains are shown on agentic benchmarks rather than on open-ended real-world tasks. Self-distillation from one's own rollouts also risks reinforcing a narrow behavior mode over many rounds.

**Why it matters to Leo.** This is the current center of the agentic-RL line, and the "turn trajectories into reusable skills, then distill" idea transfers directly to time-series reasoning agents (see Gap Watch).

**How this builds on what you know:** SEED's closest parents in your library are DeepSeek-R1 (Z5IWHZAE, LLM community), Chain-of-Thought Prompting (HBLPTRMY, reasoning), and the Memory Mechanisms Survey (BDY3HUCV, agent community). Where DeepSeek-R1 used outcome-based RL to make reasoning emerge from a sparse final reward, SEED keeps the same outcome reward but adds a hindsight self-distillation step, because the sparse reward alone leaves intermediate agent decisions unsupervised. Where Chain-of-Thought produced reasoning as ephemeral text inside a single forward pass, SEED writes the useful part of a trajectory into an explicit skill and folds it back into the weights, so the lesson persists instead of being regenerated each time. Where the Memory Mechanisms Survey catalogued external memory stores for agents, SEED puts the "memory" into the policy parameters through distillation rather than into a retrieved buffer. This paper also extends the DeepSeek-R1 to Chain-of-Thought bridge already in your library (reasoning-via-RL versus reasoning-via-prompting); SEED pushes that bridge further toward reasoning-via-RL-plus-self-distillation.

---

## Tier B — TLDRs (3 papers)

### VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding (arXiv:2607.14935)

A 4B-parameter, fully open video multimodal LLM built to handle short motion, hour-long video, temporal grounding, and live streaming in one model. Its two design pieces are an Inflated 3D Vision Transformer (I3D-ViT) for spatiotemporal features and an Adaptive Frame Resolution scheme for streaming perception, which lowers the cost of long or live video. Trained with a scalable video data-synthesis pipeline that produces three datasets (Academic2M, LV116K, OL617K) for general, long-form, and streaming cases. The reported claim is that it surpasses prior open-source video MLLMs of equal or larger size at only 4B parameters.

**How this builds on what you know:** Parents in your library are I3D (WYQSCSRF, video action recognition), Flamingo (SC8KWYVK, multi-modal), and BLIP-2 (4N5WXKPI, multi-modal). Where I3D inflated 2D convolutions into 3D to read motion, VideoChat3 inflates a 2D Vision Transformer into I3D-ViT, moving the same inflation trick from ConvNets to transformers. Where Flamingo and BLIP-2 bridged a frozen vision encoder to a language model for image-and-text dialogue, VideoChat3 does the same for video but adds streaming-aware frame-resolution control, because hour-long and live inputs make Flamingo-style fixed sampling too costly.

### TiRex-2: Generalizing TiRex to Multivariate Data and Streaming (arXiv:2607.01204)

An xLSTM-based time-series foundation model that forecasts one or many target series directly from history, optionally conditioned on past and future-known covariates, in a streaming fashion, zero-shot. The design is memory-centric and recurrent, so cost per new patch stays constant under streaming instead of growing; it pairs a bidirectional time mixer with an asymmetric grouped-attention variate mixer that mixes across variables while keeping strict causality on the targets. To pretrain at scale it composes synthetic multivariate samples on the fly from large univariate corpora. This is directly in Leo's primary area.

**How this builds on what you know:** Parents in your library are HARMamba (HE9X47KN, mamba/time-series), Bi-Mamba+ (AVTJLZIR, mamba/time-series), and the LLMs-for-Time-Series Survey (N2JLZBY3, time-series). Where HARMamba and Bi-Mamba+ used a recurrent state-space backbone to get linear-cost sequence modeling on sensor and forecasting data, TiRex-2 uses an xLSTM recurrent backbone with the same constant-per-step goal, but extends it to true multivariate forecasting with future-known covariates and streaming updates, because Transformer time-series foundation models pay quadratic context cost and must recompute full history as new points arrive. Where the survey framed time-series ability as something to obtain by attaching an LLM, TiRex-2 stays fully numeric and recurrent, so it is the "native forecasting" branch rather than the LLM-integration branch.

### Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes (arXiv:2607.13188)

A Google model that unifies image understanding and image generation as two coupled Markov jump processes that run at the same time and correct each other, rather than as two separate heads or two separate passes. The coupling lets the generation side use the understanding side's read of the current image to fix its own errors mid-process (self-correction), aiming for a single model that both reads and draws while staying consistent.

**How this builds on what you know:** Parents in your library are DDPM (GX7WR7KA, generative-cv) and DiT (YJ9TK993, generative-cv). Where DDPM defined generation as a fixed forward-and-reverse diffusion over continuous noise, this paper replaces the continuous diffusion with coupled Markov jump processes and lets an understanding process steer the generation process, because a one-way denoiser has no built-in channel to check whether what it is drawing matches what it is reading. Where DiT showed a transformer can serve as the diffusion backbone, this work keeps the transformer-style backbone but changes the underlying stochastic process and couples two of them for self-correction.

---

## Tier C — scan headlines (8)

From Pixels to States: Rethinking Interactive World Models as Game Engines (arXiv:2607.14076) — recasts interactive world models as explicit game engines with state, not just pixel prediction.
Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations (arXiv:2607.13399) — analysis of when on-policy distillation helps versus quietly hurts; useful companion to today's Tier A.
Video = World + Event Stream (arXiv:2607.15038) — factorizes video into a static world plus an event stream for generation.
GRASP: Granularity-Aware Search Policy for Agentic RAG (arXiv:2607.10463) — lets a retrieval agent choose search granularity instead of a fixed chunk size.
MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators (arXiv:2607.15273) — applies forward-process RL to average-velocity flow generators.
DeepLoop: Depth Scaling for Looped Transformers (arXiv:2607.13491) — scales effective depth by looping a shared transformer block.
Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models (arXiv:2607.15277) — splits a prompt, samples, and aggregates for a statistical self-consistency estimate.
KeyFrame-Compass: Comprehensive Evaluation of Keyframe-Conditioned Video Generation (arXiv:2607.14202) — a benchmark for keyframe-conditioned video generation.

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported (closed off).** TiRex-2 (Tier B above) imports recurrent state-space / xLSTM sequence modeling into multivariate streaming forecasting. This matches the pattern your library already holds through HARMamba and Bi-Mamba+ (recurrent SSM backbones on sensor and forecasting data, Community 2/4). Constant-cost recurrent sequence modeling for time series is now well-covered; a straight "apply an SSM to forecasting" paper is no longer novel.

**Unported opportunity.** SEED's hindsight-skill on-policy self-distillation (today's Tier A, Community 0) has not been applied to time-series reasoning agents. Transfer hypothesis: take a tool-using time-series agent such as TS-Agent (I2CIT4I7, your library), let it write natural-language skills from its completed analysis trajectories ("when the series shows this change-point pattern, run decomposition before trend estimation"), and distill those skills back into the controller. This would give a self-improving time-series reasoning agent that needs no new labeled data, transferring the agentic-RL self-distillation idea into your primary area before someone else does.

---

## News — major releases

Three frontier releases dominate July 2026. OpenAI shipped GPT-5.6 as a three-model line (Sol for high-end reasoning and science, Terra for GPT-5.5-level quality at roughly half the cost, Luna for fast high-volume work). SpaceXAI (the unified xAI brand) released Grok 4.5, a 1.5T-parameter mixture-of-experts on a new V9 base trained on large volumes of real agent-interaction data, pitched on efficiency (about a quarter of the output tokens of Opus 4.8 per solved coding task). Meta announced Muse Spark 1.1, a 1M-token-context agentic model priced aggressively at $1.25 / $4.25 per million tokens. None of these is a research paper; note them for context on where agent tooling is heading.

---

End of digest. Close this tab when done.
