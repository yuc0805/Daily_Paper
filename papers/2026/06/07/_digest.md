# AI Digest — 2026-06-07

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### ExpWeaver: LLM Agents Learn from Experience via Latent RAG
**arxiv:** [2606.01041](https://arxiv.org/abs/2606.01041) | Feng, Luo, Xu, Hua, Xie, Yang, Liu, You | 2026-05-31

**Problem.** Experience learning — reusing past interactions to improve future agent planning — currently operates entirely in text space. Existing methods retrieve experiences by semantic similarity and concatenate them into the context window. This creates two problems: high token overhead (1.5-2x more tokens than non-retrieval baselines) and a decoupled architecture where retrieval and generation are optimized separately.

**Method.** ExpWeaver encodes experiences using the LLM's own hidden states rather than text. At each decoding step, it retrieves relevant experiences directly in latent space, then integrates them through cross-attention aggregation and gated residual mechanisms. The retrieval and generation components are trained end-to-end with reinforcement learning, eliminating the retrieval-generation decoupling. No separate RAG module is needed — the experience memory lives inside the model's own representation space.

**Result.** State-of-the-art on 12 of 13 tasks spanning QA, reasoning, coding, scientific prediction, and recommendation. Outperforms the strongest baseline by over 6.8% on average. Token efficiency is comparable to non-retrieval baselines (text-based retrieval methods use 1.5-2x more tokens). Cross-domain generalization: +16.32% over the strongest baseline under zero-shot transfer, +15.21% under few-shot transfer.

**Limitations.** The cross-attention mechanism adds architectural complexity compared to simple prompt-concatenation approaches. Training requires RL, which is harder to tune than supervised fine-tuning. The paper does not evaluate on agentic tool-use benchmarks (e.g., BFCL, tau2-bench), which would be the natural next test given yesterday's PROVE paper.

**Why it matters to you.** The latent experience encoding is a clean alternative to the explicit experience replay used in most agent systems. For biosignal analysis agents that repeatedly encounter similar physiological patterns, encoding past diagnostic reasoning as latent states rather than text could reduce context-window pressure while improving diagnostic consistency.

**How this builds on what you know:** ExpWeaver extends the agent memory line represented by the Memory Mechanisms Survey (Huang 2026, graphify_id: huang2026_memory) in Community 0 of your graph. Where Huang catalogued memory architectures for agents, ExpWeaver provides a concrete implementation that moves memory from text space to latent space. It also connects to ToolkenGPT (Hao 2024) and LATS (Zhou 2024) in your library — both use explicit planning steps that could benefit from latent experience retrieval instead of text-based few-shot examples. The cross-area bridge from hao2024_toolkengpt to zhao2025_pyvision already links tool-use agents with agentic vision; ExpWeaver's latent memory would be a natural addition to that pipeline.

---

## Tier B — TLDRs

### 1. SARAF: Stationarity-Aware Retrieval-Augmented Time Series Forecasting
**arxiv:** [2606.04135](https://arxiv.org/abs/2606.04135) | Zhou et al. | 2026-06-02

SARAF addresses a failure mode of retrieval-augmented time-series forecasting: similarity-only retrieval is brittle under non-stationarity because a similar past segment does not guarantee a similar future. SARAF forms a candidate pool via temporal similarity with time-aligned enhancement, then applies diversity-aware selection to cover heterogeneous historical regimes. The diversification strength is automatically modulated by dataset-level stationarity. A stationarity-aware aggregation step fuses retrieved futures. On eight real-world datasets, SARAF improves average accuracy and robustness over strong baselines, with the clearest gains under non-stationary conditions.

**How this builds on what you know:** This sits in Community 4 (Time Series + LLM Integration) of your graph. The retrieval-augmented approach extends the line from LLMs for Time Series Survey (Zhang 2024) and iTransformer in your library. Where those methods treat time series as a single input to a model, SARAF adds a retrieval layer that conditions forecasts on historical regime diversity. The stationarity-aware modulation is the key innovation — it addresses the exact failure mode you would encounter when deploying time-series foundation models (Chronos, Sundial) on non-stationary biosignal data like ambulatory ECG or activity-level signals.

### 2. KVarN: Variance-Normalized KV-Cache Quantization for Reasoning Tasks
**arxiv:** [2606.03458](https://arxiv.org/abs/2606.03458) | Huawei CSL | 2026-06-02

KVarN is a calibration-free KV-cache quantizer that combines Hadamard rotation with dual-scaling variance normalization across both axes of K and V matrices. The core insight is that under autoregressive decoding (not just prefill), quantization errors accumulate across timesteps, driven by incorrect token-level scales. The Hadamard-then-normalize pipeline fixes outlying token scales. At 2-bit precision, KVarN achieves 3-5x KV-cache capacity over FP16 while matching FP16 accuracy on MATH500, AIME24, and HumanEval. No calibration data required; ships as a single vLLM flag.

**How this builds on what you know:** No direct parents in your library for KV-cache quantization specifically. The closest neighbors are DeepSeek-V3 (graphify_id: deepseek2024_v3, Community 0), which introduced Multi-head Latent Attention (MLA) as another approach to KV-cache compression, and DeepSeek-R1, whose long reasoning traces create the memory pressure that KVarN addresses. KVarN and MLA solve the same problem (KV-cache memory) from opposite directions: MLA compresses at the architecture level, KVarN at the quantization level. For your work, long-context reasoning over sensor data (e.g., TS-Agent processing extended time-series windows) would directly benefit from this kind of inference-time memory reduction.

### 3. Predict and Reconstruct: Joint JEPA + MLM Objectives for Language Representations
**arxiv:** [2606.05173](https://arxiv.org/abs/2606.05173) | Boukhari | 2026-04-16

This paper combines a JEPA-style latent-space prediction loss with standard masked language modelling (MLM) over a shared encoder, using a learnable scalar to balance the two objectives during training. Pre-trained on English Wikipedia with a BERT-base architecture, the hybrid encoder produces significantly more uniform embeddings (uniformity < -0.16 vs -0.05 for MLM-only) while achieving similar linear-probe accuracy on five GLUE benchmarks. The JEPA objective reshapes the latent space in ways that standard accuracy metrics alone do not capture.

**How this builds on what you know:** This connects your self-supervised learning work (Community 1) with the JEPA paradigm. The SSL for HAR paper (Yuan 2024, graphify_id: yuan2024_ssl_har) used contrastive and masked reconstruction objectives for sensor data. This paper shows that adding a JEPA-style prediction loss to masked reconstruction yields better-structured latent spaces even when downstream accuracy looks similar. The implication for biosignal foundation models: a hybrid JEPA+masked objective might produce representations that generalize better across downstream tasks (activity recognition, health prediction, anomaly detection) even if task-specific probes show marginal gains.

---

## Tier C — Scan Headlines

1. **LoomVideo: Unified Video Generation and Editing** — 5B-param model replaces text encoder with MLLM + Deepstack injection for DiT alignment. Half the compute of 13B competitors. [2606.06042](https://arxiv.org/abs/2606.06042)

2. **Linear Probes Detect Task Format, Not Reasoning Mode** — 100% probe accuracy on reasoning-type classification drops to chance after controlling for format confounds. [2606.02907](https://arxiv.org/abs/2606.02907)

3. **Query-based Cross-Modal Projector for Mamba Multimodal LLM** — Cross-attention compresses visual tokens for Mamba LLMs; removes need for 2D scan order design. [2606.04719](https://arxiv.org/abs/2606.04719)

4. **Predictable Scaling Laws for Continued Pre-training Hyperparameters** — Optimal LR and batch size follow stable power laws as compute budget grows during continued pre-training. [2606.05610](https://arxiv.org/abs/2606.05610)

5. **RUBAS: Rubric-Based RL for Agent Safety** — Decomposes agent behavior into 4 safety dimensions for fine-grained reward in tool-use scenarios. [2606.04051](https://arxiv.org/abs/2606.04051)

6. **LatentWave: JEPA Pretraining for Wireless Foundation Models** — Applies JEPA to wireless signal data; learns transferable representations by predicting masked regions in latent space. [2606.06373](https://arxiv.org/abs/2606.06373)

7. **CodeGolfBench: Concise Code Generation Benchmark** — Multi-language benchmark; reasoning LLMs achieve 70.97% percentile in code conciseness. [2605.30394](https://arxiv.org/abs/2605.30394)

8. **Hedge-Bench: Financial Reasoning for Agents** — 102 real-world financial tasks; frontier models score under 16%. [2606.03918](https://arxiv.org/abs/2606.03918)

---

## Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**

SARAF (Tier B) applies retrieval augmentation to time-series forecasting, joining a growing line of RAG-for-TS methods (TS-RAG, RATF). The stationarity-aware modulation is new, but the core idea of conditioning forecasts on retrieved historical segments is now well-explored in the forecasting community.

**Unported opportunities:**

1. **Latent experience retrieval for biosignal reasoning agents.** ExpWeaver (Tier A) encodes agent experiences as hidden states and retrieves them in latent space during decoding. No work has applied this to biosignal analysis agents. Transfer hypothesis: a diagnostic agent for ECG/PPG analysis that encodes past patient cases as latent states — rather than text summaries — could retrieve relevant diagnostic reasoning patterns without consuming context tokens. This would extend the ts_llm_reasoning_pipeline hyperedge (Community 4) by adding a memory layer currently absent from TS-Agent and ChatTS.

2. **JEPA + masked reconstruction for sensor foundation models.** The Predict and Reconstruct paper (Tier B) shows that combining JEPA prediction loss with MLM reconstruction produces more uniform latent spaces in NLP. This combination has not been tested on sensor data pre-training. Transfer hypothesis: applying hybrid JEPA+masked objectives to the pre-training recipe used in SSL for HAR (Yuan 2024) or Foundation Models for Biosignals (Gu 2025) could yield representations with better cross-task generalization, especially for the long-tail of rare health events where representation uniformity matters.

---

## News

1. **Anthropic confidentially filed for IPO** at a $965 billion valuation, surpassing OpenAI. IPO could come later in 2026. Separately, Anthropic secured a deal for over 300 MW of compute at xAI's Colossus 1 data center ($1.25B/month through May 2029).

2. **Google I/O 2026 recap.** Gemini 3.5 Flash is generally available, rivaling large flagship models on coding and agentic benchmarks. Gemini Omni announced for any-to-any generation (text, image, video, audio). Gemini Spark is a personal agent that works in the background on phones and laptops.

3. **SpaceX plans to acquire Cursor** roughly 30 days after SpaceX begins trading publicly on June 12. Option expected to be exercised in July.

---

End of digest. Close this tab when done.
