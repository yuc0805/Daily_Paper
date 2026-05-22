# AI Digest — 2026-05-21

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding
Quinlan, Levasseur, Li, Zhu — arXiv:2605.20268 — 2026-05-18

**Problem.** Current time series foundation models process numbers in isolation. The few multimodal models that combine text and time series do so by adapting a pretrained language model after the fact, inheriting representations that never saw temporal data during pretraining. These models are only compared against other multimodal baselines, never against the best unimodal foundation models, so it remains unclear whether joint training actually helps.

**Method.** Chronicle is a compact 324M-parameter decoder-only transformer trained from scratch on both natural language and time series in a single architecture. Both modalities share the same transformer blocks, attention mechanism, and residual stream. The bulk of pretraining uses unimodal batches; cross-modal capability emerges from shared parameters, with a short alignment stage that interleaves the two modalities.

**Result.** Chronicle matches Gemma-3-270M-PT on 19 NLU tasks, sets a new state-of-the-art for frozen-embedding time series classification on 24 UCR/UEA datasets, and produces multimodal forecasts on Time-MMD that beat every supervised fusion baseline — all from one 324M backbone.

**Limitations.** The model is small (324M). The paper does not evaluate on long-horizon forecasting benchmarks (TSLib, GIFT-Eval) where unimodal foundation models like Olivia and Sundial are strongest. Cross-modal interaction is limited to a short alignment stage; it is unclear how much genuine cross-modal reasoning occurs versus simple parameter sharing.

**Why it matters to Leo.** This is the first model that jointly pretrains on text and time series from scratch, which is a fundamentally different design choice from every other model in your time-series area (ChatTS, Time-LLM, Sensor2Text all adapt pretrained LLMs). If joint pretraining proves scalable, it could change how you think about building sensor-language models for health applications. It also directly benchmarks against unimodal foundation models, which is the evaluation standard the field has been missing.

**How this builds on what you know:** Chronicle sits at the intersection of your Community 4 (Time Series + LLM Integration) papers. Where ChatTS (Xie 2025) fine-tunes a pretrained LLM to accept time series as a new modality, Chronicle trains both modalities from scratch, arguing that post-hoc adaptation inherits suboptimal representations. Where the LLMs for Time Series survey (Zhang 2024) categorized five paradigms for combining LLMs with time series (prompting, quantization, alignment, vision bridging, tool use), Chronicle introduces a sixth: native joint pretraining. The closest ancestor in your library is Sensor2Text (Chen 2024), which also bridges sensor data and language but does so through student-teacher distillation from a vision-language model rather than from-scratch training. Chronicle's evaluation against dedicated unimodal foundation models is something none of these predecessors did.

---

## Tier B — TLDRs

### 1. Olivia: Harmonizing Time Series Foundation Models with Power Spectral Density
Fei, Yi, Wang, Wen, Zhu, Fan — arXiv:2605.17340 — 2026-05-17 — **Accepted ICML 2026**

Time series foundation models pretrain over heterogeneous datasets, but spectral mismatches across domains hurt transfer. Olivia introduces a Harmonizer module that reshapes the power spectral density of different datasets into a shared spectral space before attention, which corresponds to reparameterizing second-order temporal correlations. A HarmonicAttention mechanism performs self-attention in this low-dimensional interaction space. On TSLib and GIFT-Eval benchmarks plus 6 GluonTS datasets, Olivia achieves state-of-the-art under zero-shot, few-shot, and full-shot forecasting.

**How this builds on what you know:** Olivia directly extends the TS foundation model line in your library. Where Sundial (Liu 2025) used flow-matching to handle continuous-valued time series and Chronos (Ansari 2024) used quantization-based tokenization, Olivia addresses a different bottleneck: spectral heterogeneity across pretraining domains. PatchTST (Nie 2023) showed that patching helps local semantic retention but assumed homogeneous spectral characteristics; Olivia relaxes that assumption via PSD harmonization. If you use TS foundation models for health signals (which have very different spectral profiles from financial or weather data), Olivia's approach could matter.

### 2. Compact Latent Manifold Translation (CLMT): A Parameter-Efficient Foundation Model for Cross-Modal and Cross-Frequency Physiological Signal Synthesis
arXiv:2605.13248 — 2026-05-13

This paper proposes a small (0.09B parameter) unified framework for translating between different physiological signal modalities and frequencies. It uses a Universal Tokenizer with Hierarchical Residual Vector Quantization to map heterogeneous biosignals (ECG, PPG, EEG, etc.) into discrete latent manifolds, then performs cross-modal translation in this latent space. The approach is parameter-efficient and handles both cross-modal (e.g., ECG to PPG) and cross-frequency (e.g., 128Hz to 256Hz) translation.

**How this builds on what you know:** This sits squarely in the intersection of your Community 1 (Health AI & Self-Supervised) and Community 5 (Wearable Sensing & Behavior). Where the Foundation Models for Biosignals survey (Gu 2025) identified cross-modal alignment as an open problem, CLMT provides a concrete solution. Where SensorLM builds large sensor-language models with >59M hours of data, CLMT takes the opposite approach: a tiny model (0.09B) that translates between signal modalities. This paper extends the bridge between Sensor2Text (Community 4, which aligns sensor with text) and the biosignals survey (Community 1), pushing it further into a direction your library has not covered: direct signal-to-signal translation without going through text.

### 3. Human-Inspired Memory Architecture for LLM Agents
arXiv:2605.08538 — 2026-05-08

Current LLM agents lack principled mechanisms for managing memory across long interaction horizons. This paper presents a biologically grounded memory architecture with six cognitive mechanisms: sleep-phase consolidation, interference-based forgetting, engram maturation, reconsolidation upon retrieval, entity knowledge graphs, and hybrid multi-cue retrieval. The architecture provides a structured alternative to the typical retrieval-augmented or context-window approaches used in current agents.

**How this builds on what you know:** Your agent papers in Community 0 (LLM Agents & Reasoning) have covered planning decomposition (ADaPT, Prasad 2023), tree search (LATS, Zhou 2024), and tool embedding (ToolkenGPT, Hao 2024), but memory architecture is a gap. Huang 2026 (Rethinking Memory Mechanisms of Foundation Agents) raised the question of how agents should manage memory; this paper provides a specific architectural answer grounded in cognitive science. Where Huang 2026 surveyed memory mechanisms broadly, this work implements sleep-phase consolidation and interference-based forgetting as concrete modules, which are mechanisms Huang identified but did not build.

---

## Tier C — Scan Headlines

1. **Code as Agent Harness** (2605.18747) — Survey framing code as the operational substrate for agent reasoning, planning, tool use, and multi-agent coordination. [arXiv](https://arxiv.org/abs/2605.18747)

2. **Vision-OPD: Learning Fine Details for Multimodal LLMs** (2605.18740) — Regional-to-global self-distillation to fix fine-grained visual understanding failures in MLLMs. [arXiv](https://arxiv.org/abs/2605.18740)

3. **Spectral Progressive Diffusion** (2605.18736) — Training-free progressive resolution growth along diffusion denoising trajectories; significant speedups on pretrained image and video models. [arXiv](https://arxiv.org/abs/2605.18736)

4. **Heterogeneous Agent Collaborative RL** (2603.02604) — ByteDance multi-agent RL with heterogeneous agent coordination. [arXiv](https://arxiv.org/abs/2603.02604)

5. **Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory** (2603.04257) — Experience indexing for long-horizon agent tasks. [arXiv](https://arxiv.org/abs/2603.04257)

6. **Strat-Reasoner: Reinforcing Strategic Reasoning in Multi-Agent Games** (2605.04906) — RL-based strategic reasoning with DPO and GRPO for multi-agent games. [arXiv](https://arxiv.org/abs/2605.04906)

7. **TS Foundation Models for Electricity Price Forecasting** (2605.17045) — Empirical eval of Chronos-2, Chronos-Bolt, and TimesFM 2.5 on Belgian electricity prices. [arXiv](https://arxiv.org/abs/2605.17045)

8. **Phi-4-reasoning-vision-15B** (2603.03975) — Microsoft 15B vision-reasoning model technical report. [arXiv](https://arxiv.org/abs/2603.03975)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**
The spectral harmonization approach (Olivia, 2605.17340) applies PSD-based normalization from classical signal processing to TS foundation model pretraining. This is now done.

CLMT (2605.13248) applies hierarchical residual VQ (originally from audio/speech codecs) to cross-modal physiological signal translation. This transfer is now executed.

**Unported opportunity:**
The Vision-OPD regional-to-global self-distillation idea (2605.18740) has a clear transfer hypothesis for biosignal analysis. In clinical ECG or EEG interpretation, the diagnostic answer often depends on small morphological features (e.g., ST-segment elevation, spike-wave complexes) within a long recording. A "regional-to-global" self-distillation framework — where a model first learns to classify from feature-centered segments, then distills that into full-recording classification — could address the same "needle in a haystack" problem that Vision-OPD solves for images. No such approach exists for time-series foundation models.

The Spectral Progressive Diffusion idea (2605.18736) could also transfer: progressively growing temporal resolution during diffusion-based time series generation, starting from coarse trend and adding fine-grained details. This would be useful for biosignal synthesis (e.g., generating realistic ECG at increasing fidelity), but no one has tried it.

---

## News

1. **GPT-5.5 Instant** is now the default ChatGPT model (May 5). Improved accuracy, reduced hallucinations, better personalization.

2. **Grok 4.3** from xAI entered wider rollout (May 6), with improved reasoning and coding.

3. **Anthropic secured compute access** at xAI's Colossus 1 data center in Tennessee — over 300 MW from 220K+ Nvidia GPUs. This is infrastructure news, not a model release, but it signals significant upcoming capacity.

---

End of digest. Close this tab when done.
