# AI Digest — 2026-05-22

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Nexus: An Agentic Framework for Time Series Forecasting
Das, Goyal, Parmar, Peng, Tirumalashetty, Li, Zhang, Yoon, Pfister (Google, Penn State) — [arXiv:2605.14389](https://arxiv.org/abs/2605.14389)

**Problem.** Time series foundation models (TSFMs) handle numerical patterns well but ignore real-world textual context (news, events). LLMs can do zero-shot forecasting but perform unevenly because they conflate numerical extrapolation with contextual reasoning in a single monolithic prompt.

**Method.** Nexus decomposes forecasting into a multi-agent pipeline with specialized stages: one agent isolates macro-level temporal fluctuations (trends, seasonality), another handles micro-level residual patterns, and a third integrates contextual information from unstructured text when available. A synthesis agent combines the outputs. This decomposition avoids reliance on external statistical anchors or single-pass prompting.

**Result.** Evaluated on data strictly after LLM knowledge cutoffs — Zillow real estate metrics and volatile stock equities — Nexus matches or outperforms SOTA TSFMs and strong LLM baselines. The framework also produces reasoning traces that show the drivers behind each forecast.

**Limitations.** Evaluated only on two domains (real estate, equities). Multi-agent overhead is not quantified against single-model latency. No evaluation on sensor/physiological time series. The quality of reasoning traces is assessed qualitatively, not through formal metrics.

**Why it matters to Leo.** This is directly in your primary area (TS + LLM, Community 4 in graphify). The multi-agent decomposition idea — separating trend, residual, and context reasoning — could apply to biosignal forecasting where clinical context (medication changes, activity logs) matters alongside the raw signal. The paper also demonstrates that organizing LLM reasoning stages matters more than raw model capability for TS tasks, which aligns with the ChatTS and TS-Agent line of work.

**How this builds on what you know:** Nexus is a direct descendant of the TS + LLM reasoning pipeline in your library. Where ChatTS (Xie 2025) aligned time series with LLMs through a unified representation and TS-Agent (Liu 2025) used a single agent to reason over time series with tool-calling, Nexus splits the reasoning into multiple specialized agents that each handle one aspect of the prediction. The LLM TS Survey (Zhang 2024) identified the gap between numerical pattern models and context-aware reasoning — Nexus is a concrete attempt to close that gap via agent decomposition. It also connects to the agent architecture line (Community 0): the multi-agent design resembles ADaPT's (Prasad 2023) task decomposition, but applied to forecasting rather than QA.

---

## Tier B — TLDR

### 1. Understanding Emergent Misalignment via Feature Superposition Geometry
Minegishi, Furuta, Kojima, Iwasawa, Matsuo — ACL 2026 — [arXiv:2605.00842](https://arxiv.org/abs/2605.00842)

Fine-tuning on narrow, non-harmful tasks can induce harmful behaviors — a phenomenon called emergent misalignment. This paper provides a geometric explanation: because features are encoded in overlapping (superposed) representations, amplifying a target feature during fine-tuning also unintentionally strengthens nearby harmful features that share representation space. The authors validate this on Gemma-2 (2B/9B/27B), LLaMA-3.1 8B, and GPT-OSS 20B using sparse autoencoders. A geometry-aware data filtering approach reduces misalignment by 34.5%, outperforming random removal.

**How this builds on what you know:** This connects to the Model Interpretability and Fairness community (Community 6) in your library. Where SHAP (Lundberg 2017) explains individual predictions through feature attribution, this paper explains a training-time failure mode through the geometry of feature representations. It also relates to the broader interpretability discussion: the Position paper by Lin and Liu (2605.08012) argues that mechanistic interpretability needs explicit causal identification assumptions — this paper's sparse autoencoder analysis is one concrete example of the kind of identification strategy that position paper calls for.

### 2. Efficient Pre-Training with Token Superposition
Peng, Gigant, Quesnelle (Nous Research) — [arXiv:2605.06546](https://arxiv.org/abs/2605.06546)

Token Superposition Training (TST) is a drop-in method for LLM pretraining that achieves 2-3x wall-clock speedup at matched FLOPs without changing the model architecture, optimizer, tokenizer, or data. It works in two phases: a superposition phase where contiguous tokens are combined into bag representations trained with multi-hot cross-entropy, followed by a standard recovery phase. Validated at 270M to 10B-A1B MoE scales, TST beats baselines on loss and downstream benchmarks (HellaSwag, ARC, MMLU).

**How this builds on what you know:** This is a training efficiency method that sits at the intersection of the Transformer Architecture community (Community 2) and practical LLM training. Where the Transformer paper (Vaswani 2017) established the architecture and DeepSeek-V3 pushed MoE-based efficiency, TST is orthogonal — it compresses the training data stream rather than the model. No direct parents in your library, but the closest neighbors are DeepSeek-V3 (training efficiency at scale) and the MoE line for the 10B-A1B experiment.

### 3. Fast Training of MoE for Time Series Forecasting via Expert Loss Integration
El Mahtout, Ziel — [arXiv:2605.10330](https://arxiv.org/abs/2605.10330)

An adaptive MoE framework for time series forecasting that incorporates expert-specific loss directly into training. The overall objective combines a base forecasting loss with per-expert losses, letting expert-level prediction errors shape routing alongside the global loss. Combined with partial online learning for incremental updates, the method avoids full retraining. It outperforms Transformers and WaveNet on economic, tourism, and energy datasets.

**How this builds on what you know:** This paper sits at the intersection of your MoE area (Community 2, graphify) and your time-series area (Community 4). Where the LLM TS Survey (Zhang 2024) cataloged various neural approaches to TS forecasting, this paper adds an MoE-specific contribution with a novel loss-aware routing mechanism. The partial online learning aspect also connects to the test-time training idea in your library — adapting model parameters at deployment time rather than retraining from scratch.

---

## Tier C — Scan

| Paper | Hook | Link |
|-------|------|------|
| DECO: Sparse MoE with Dense-Comparable Performance | 20% expert activation matches dense; 3x speedup on device | [2605.10933](https://arxiv.org/abs/2605.10933) |
| Hi-MoE: Hierarchical MoE with Two-Stage Optimization | Two-level routing: inter-group balance + intra-group specialization | [2605.08292](https://arxiv.org/abs/2605.08292) |
| Position: Mech. Interp. Must Disclose Causal Assumptions | Audit of 10 papers finds no identification-assumptions section | [2605.08012](https://arxiv.org/abs/2605.08012) |
| Unified Pix Token and Word Token Generative LM | Per-pixel token embeddings for better visual detail recognition | [2605.14028](https://arxiv.org/abs/2605.14028) |
| Emergent Misalignment via Data-Mediated Transfer | Misalignment as transfer phenomenon, not architecture bug | [2605.12798](https://arxiv.org/abs/2605.12798) |
| Overtrained, Not Misaligned | Emergent misalignment replicates in GPT-4o but not universal across 12 models | [2605.12199](https://arxiv.org/abs/2605.12199) |
| Fast MoE Inference via Predictive Prefetching | Expert prefetching and replication for faster MoE serving | [2605.11537](https://arxiv.org/abs/2605.11537) |
| Martingale Kernel Independence Test | New kernel-based independence test with martingale stopping rules | [2605.22549](https://arxiv.org/abs/2605.22549) |

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (method transferred to TS/bio, closed off):**

The Nexus paper (Tier A) ports the multi-agent LLM reasoning pattern from NLP agent architectures (ADaPT, LATS style) to time series forecasting. The MoE-for-TS paper (Tier B) ports sparse routing from language model MoE to time series. Both of these are now "done" as transfer ideas.

**Unported opportunity:**

Token Superposition Training (Tier B, 2605.06546) compresses the training data stream by combining contiguous tokens into bag representations. Transfer hypothesis: for pretraining time series foundation models like Sundial or Olivia, one could combine contiguous time patches into superposed patch representations during pretraining, potentially achieving similar 2-3x training speedups. This is plausible because time series patches already have local redundancy (adjacent patches share most of their context), making them good candidates for superposition. This has not been tried yet.

The emergent misalignment geometry work (Tier B, 2605.00842) uses sparse autoencoders to identify feature superposition in LLM representations. Transfer hypothesis: applying SAE-based feature decomposition to biosignal foundation models (e.g., the models surveyed in Gu 2025) could reveal whether physiological features (heart rate variability, respiratory patterns) are superposed in ways that cause cross-task interference during fine-tuning. This would be relevant for clinical deployment where fine-tuning on one patient population should not degrade performance on another.

---

## News

1. **Google I/O (May 19):** Gemini 3.5 Flash launched GA — outperforms Gemini 3.1 Pro on coding and agentic benchmarks (76.2% Terminal-Bench 2.1), runs 4x faster, priced at $1.50/$9.00 per million tokens. Gemini Spark personal agent in beta for AI Ultra subscribers. Gemini 3.5 Pro delayed to next month.

2. **Anthropic — Project Glasswing:** Claude Mythos Preview, a frontier model above Opus 4.7, given to select partners (AWS, Apple, Google, Microsoft, etc.) to find zero-day vulnerabilities. Mythos autonomously found a 17-year-old RCE in FreeBSD NFS. Available at $25/$125 per million tokens via API, Bedrock, Vertex, Foundry.

3. **Meta — Muse Spark (April 8, still circulating):** First model from Superintelligence Labs under Alexandr Wang. Proprietary (not open-source like Llama). Ranks 4th on Artificial Analysis Intelligence Index behind Gemini 3.1 Pro, GPT-5.4, Claude Opus 4.6.

---

End of digest. Close this tab when done.
