# AI Digest — 2026-05-27

**Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

**Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.

**Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Towards a General Intelligence and Interface for Wearable Health Data
Narayanswamy, Xu, Heydari et al. (Google/UW) — [arXiv:2605.22759](https://arxiv.org/abs/2605.22759)

**Problem.** Wearable sensors produce continuous physiological and behavioral streams, but turning these into health-relevant representations is hard. Individual baselines vary widely, and collecting outcome-labeled data at scale is expensive and often infeasible retrospectively. Existing models are either modality-specific or small-cohort.

**Method.** The authors pretrain a foundation model on more than one trillion minutes of unlabeled sensor signals from five million participants. They scale both model capacity and pretraining data jointly. Downstream, they deploy a "classroom" of LLM agents that autonomously search the space of predictive heads built on the frozen embeddings, finding task-specific classifiers without manual architecture design. A Personal Health Agent integrates these predictors to produce contextual, clinician-validated responses.

**Result.** Evaluated on 35 health prediction tasks spanning cardiovascular, metabolic, sleep, and mental health domains, plus lifestyle and demographic factors. Joint scaling of model size and data volume yields systematic improvements. The population-scale representation enables few-shot learning and generative daily metric estimation. The LLM-agent-designed heads improve performance proportional to LLM capacity. Clinician validation via 1,860 ratings confirms the Personal Health Agent produces more relevant and safe outputs than baselines.

**Limitations.** The paper appears to use proprietary data from a large wearable platform (likely Fitbit/Google), so reproducibility outside Google is limited. The "classroom of LLM agents" for head design is interesting but adds inference cost. Clinician ratings are subjective and the cohort size for validation (1,860 ratings) is modest relative to the pretraining scale.

**Why it matters to Leo.** This is the largest wearable health foundation model reported to date and sits squarely at the intersection of Leo's primary areas: time-series modeling and health AI. The LLM-agent-based AutoML for downstream heads is a novel design pattern worth watching. The few-shot learning result is especially relevant if Leo works with smaller labeled datasets in bio-sensing.

**How this builds on what you know:** The Foundation Models for Biosignals survey (Gu 2025) [gu2025_biosignals] mapped the landscape and identified scaling and cross-task transfer as open problems. This paper directly addresses both by going to population scale (5M participants) and evaluating across 35 tasks rather than a handful. Where Gu 2025 surveyed existing small-to-medium models and flagged gaps, this paper fills the largest gap: what happens when you scale wearable pretraining by orders of magnitude. It also connects to Sensor2Text (Chen 2024) [chen2024_sensor2text] and GLOBEM (Xu 2023) [xu2023_globem] in the wearable sensing community (graphify Community 5), but goes far beyond their data scale and task breadth. The LLM-agent downstream search additionally bridges Community 0 (LLM Agents) into the wearable health space — a new cross-area connection.

---

## Tier B — TLDRs

### 1. Chronicle: A Multimodal Foundation Model for Joint Language and Time Series Understanding
Quinlan, Levasseur, Li, Zhu — [arXiv:2605.20268](https://arxiv.org/abs/2605.20268)

Chronicle is a 324M-parameter decoder-only transformer trained from scratch on both natural language and time series within a single unified architecture — shared transformer blocks, attention, and residual stream. Unlike prior work that adapts a pretrained language model post hoc, Chronicle jointly pretrains on both modalities using mostly unimodal batches plus a short alignment stage. It matches Gemma-3-270M-PT on 19 NLU tasks, sets a new bar for frozen-embedding time series classification on 24 UCR/UEA datasets, and beats every supervised fusion baseline on Time-MMD multimodal forecasts.

**How this builds on what you know:** This paper sits in graphify Community 4 (Time Series + LLM Integration). Where ChatTS (Xie 2025) [xie2025_chatts] and TS-Agent (Liu 2025) [liu2025_tsagent] used pretrained LLMs and added time series as an auxiliary modality, Chronicle argues that post-hoc adaptation inherits representations that never saw temporal data. The shift to joint pretraining from scratch is the key delta. If Chronicle's approach scales, it could subsume the adapter-based pipeline that ChatTS and TS-Agent represent.

### 2. Superposition Is Not Necessary: Mechanistic Interpretability of Transformer Representations for Time Series Forecasting
Yildirim — [arXiv:2605.05151](https://arxiv.org/abs/2605.05151)

This paper applies sparse autoencoders (SAEs) from mechanistic interpretability to probe PatchTST's internal FFN representations. The main finding: expanding SAE dictionary size from 0.5x to 4.0x the native dimensionality produces negligible performance change (average 0.214%), and large portions of overcomplete dictionaries remain inactive. Causal interventions on dominant latent features produce minimal forecast perturbation. The conclusion is that standard TS forecasting benchmarks do not demand the rich compositional representations that drive transformer success in language, which mechanistically explains why simple linear models like DLinear remain competitive.

**How this builds on what you know:** PatchTST [YY67LF3R] is in your library as a key time-series transformer. DLinear [4QRHV2JG] is also present. This paper resolves the long-running debate about why linear models keep up with transformers on forecasting benchmarks: the tasks simply do not require superposition. For Leo's work, this suggests that if you need transformers for TS, the value likely comes from tasks with richer structure (e.g., cross-modal reasoning, multi-task health prediction) rather than univariate forecasting. It also connects to Community 6 (Interpretability) tools applied to Community 4 (TS+LLM).

### 3. Reinforcement Learning for LLM-based Multi-Agent Systems through Orchestration Traces
[arXiv:2605.02801](https://arxiv.org/abs/2605.02801)

This paper formalizes RL for LLM multi-agent systems by treating interactions as orchestration traces: temporal graphs with events including sub-agent spawning, delegation, communication, tool use, aggregation, and stopping. It identifies eight reward families and decomposes orchestration learning into five sub-decisions (when to spawn, whom to delegate, how to communicate, how to aggregate, when to stop). The gap analysis reveals that no explicit RL training method yet exists for the stopping decision.

**How this builds on what you know:** This extends the agent lineage in Community 0. ADaPT (Prasad 2023) [prasad2023_adapt] and LATS (Zhou 2024) [zhou2024_lats] decomposed planning and search for single agents. This paper lifts the same decomposition logic to multi-agent orchestration and adds RL training signals. The cross-area bridge from prasad2023_adapt to zhou2024_lats (planning-decomposition agents) is directly extended here to the multi-agent case.

---

## Tier C — Scan

| Paper | Hook | Link |
|---|---|---|
| MILM: LLMs for Multimodal Irregular Time Series | LLM-based approach for asynchronous, irregularly sampled heterogeneous time series | [2605.13711](https://arxiv.org/abs/2605.13711) |
| TMAS: Scaling Test-Time Compute via Multi-Agent Synergy | Organizes TTS as structured multi-agent collaboration | [2605.10344](https://arxiv.org/abs/2605.10344) |
| Spectral Progressive Diffusion | Exploits frequency-domain autoregression in diffusion for 2x speedup | [2605.18736](https://arxiv.org/abs/2605.18736) |
| Logical Consistency as a Bridge: Hallucination Detection | Bridges neural features and symbolic judgments for LLM hallucination detection | [2605.03971](https://arxiv.org/abs/2605.03971) |
| Self-Supervised Contrastive Learning for Cardiac MR Classification | ViT with contrastive pretraining beats supervised on cardiac imaging | [2605.24789](https://arxiv.org/abs/2605.24789) |
| MoE for Low-Resource LLMs | Studies routing dynamics in MoE vs hybrid Mamba-Transformer on Hebrew | [2605.17598](https://arxiv.org/abs/2605.17598) |
| Multivariate Financial Forecasting with Chronos | Multivariate inputs consistently beat univariate with Chronos foundation models | [2605.21504](https://arxiv.org/abs/2605.21504) |
| AutoTTS: Agentic Discovery for Test-Time Scaling | Automated discovery of test-time scaling strategies beyond hand-crafted ones | [2605.08083](https://arxiv.org/abs/2605.08083) |

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**

The Tier A paper (Narayanswamy et al.) ports the "LLM agents as AutoML" pattern from Community 0 into wearable health. The "classroom of LLM agents" searching downstream head architectures is effectively the agent-based tool-use paradigm (Community 0) applied to biosignal model design. This specific transfer path is now covered.

The Self-Supervised Contrastive Learning for Cardiac MR paper (2605.24789) ports standard ViT contrastive pretraining to medical imaging — this transfer (contrastive SSL to medical CV) has been done repeatedly and is low-hanging fruit at this point.

**Unported opportunity:**

Spectral Progressive Diffusion (2605.18736) shows that diffusion models generate content autoregressively in the frequency domain — low frequencies first, high frequencies later. This frequency-domain structure maps naturally to physiological signals (ECG, PPG) where clinical features live at specific frequency bands. Transfer hypothesis: apply spectral progressive generation to physiological signal synthesis, where you could generate the hemodynamic baseline first and cardiac morphology detail later, potentially improving the CLMT framework's cross-modal translation quality.

The mechanistic interpretability via SAEs (2605.05151) applied to PatchTST has been done for forecasting, but has NOT been applied to wearable health classification tasks. Transfer hypothesis: train SAEs on the wearable health foundation model's intermediate representations to understand whether health prediction tasks require richer representations than forecasting does. If they do, this would confirm the Tier A paper's scaling gains are not just data-driven but representation-driven.

---

## News

**Anthropic Claude Mythos.** Anthropic's Project Glasswing update reports that Claude Mythos Preview has been used to scan over 1,000 open-source projects, identifying 23,019 issues (6,202 high/critical severity, >90% true positive rate). Mythos 1 is being prepared for wider release through Claude Code and Claude Security. The model string claude-mythos-1-preview has appeared in public interfaces.

**OpenAI GPT-5.5.** Released April 23, with GPT-5.5 Pro for parallel reasoning and Codex integration. Only six weeks after GPT-5.4.

**Google Gemini 3.1 Ultra** launched with the largest context window in the Gemini family.

---

End of digest. Close this tab when done.
