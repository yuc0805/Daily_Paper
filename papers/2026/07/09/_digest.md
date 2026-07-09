# AI Digest — 2026-07-09

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### HiLS-Attention: Hierarchical Sparse Attention Done Right (Hu et al., Tencent Hunyuan, arXiv:2607.02980)

**Problem.** Scaling language models to long context is held back by two facts about dense attention: its compute cost grows with the square of sequence length, and it extrapolates poorly past the length seen in training. Chunk-wise sparse attention is cheaper, but every prior method selects chunks inaccurately, so it stays below full attention in quality.

**Method.** Hierarchical Landmark Sparse (HiLS) Attention makes chunk selection a learned, differentiable step. Each query attends independently to each retrieved chunk to pull out chunk-specific information, and the per-chunk outputs are then fused using the chunk retrieval scores. Because those retrieval scores enter the forward attention computation, they are trained directly under the language-modeling loss, which gives end-to-end retrieval learning and native sparse training rather than a separate, heuristic retriever.

**Result.** HiLS matches, and in some settings beats, full attention at in-domain context lengths, while cutting key-value access and computation. It extrapolates to more than 64 times the training context length with 90% retrieval accuracy, well past what full attention manages. An existing full-attention model can be converted to HiLS with lightweight continued pretraining, keeping in-domain quality while gaining long-context reach.

**Limitations.** All numbers are on text language modeling; there is no evidence yet on non-text long sequences. The 90% retrieval accuracy still means one chunk in ten is missed, which matters for tasks that need a single distant fact. Conversion is cheap but not free — it still needs continued pretraining compute.

**Why it matters to Leo.** Long physiological and wearable recordings are the setting where quadratic attention breaks first. A retrieval step that is trained end-to-end and holds up far beyond the training length is a candidate to carry over to multi-day sensor streams, where the model must reach back to a distant window without reading everything.

**How this builds on what you know:** Parents are the Transformer (PHB9VRVM, Community 2, Transformer & SSM Architectures) and HARMamba / Mamba state-space models (HE9X47KN, Community 2). Where the Transformer made dense attention the only mixing operator but paid quadratic cost, and where Mamba cut that cost with a fixed-size recurrent state but gave up content-based random access, HiLS keeps attention's content addressing at sub-quadratic cost, because it learns which chunks to read under the language-modeling loss instead of reading all of them or compressing history into a single state.

---

## Tier B — TLDR

### CLeaD: Layer-wise Cross-Lingual Depression Detection from Speech (Pattanayak et al., arXiv:2607.02920)

CLeaD is a supervised contrastive alignment framework that maps WavLM speech embeddings from English and Mandarin into one shared clinical space for depression detection, with no parallel data and no target-language fine-tuning. On 52 Mandarin speakers under leave-one-speaker-out evaluation it modestly beats the baseline (F1 0.640 versus 0.622) and raises depressed-class recall at middle encoder layers 7 to 8. Two findings are robust: larger speech models transfer worse across languages while getting better at monolingual English, and speaker-identity leakage from segment-level random splits inflated earlier Mandarin F1 to 0.954, an artifact the authors reproduce and quantify.

**How this builds on what you know:** Parents are HeAR (3LA8GNCU, Community 1, Health AI & Self-Supervised), Foundation Models for Biosignals (2XWEG7AF), and LLMs are Few-Shot Health Learners (JX3X3KH5). Where HeAR learned general health-acoustic representations inside one language and the Biosignals survey mapped within-domain foundation models, CLeaD tests whether those representations transfer across languages and reports the plain result once speaker leakage is removed. This paper extends the Sensor2Text bridge (chen2024_sensor2text), which already crossed bio-sensing and llm-health in your library; the new work pushes that bridge toward clinical speech and cross-lingual validity.

### SkillOpt-Lite: Agent Self-evolution via Zeroth-Order Optimization (Shen et al., LMMs-Lab, arXiv:2607.03451)

SkillOpt-Lite reframes agent skill self-evolution as zeroth-order optimization and strips the pipeline to three parts that are each justified by theory or need: file-system trajectory exploration, consensus attribute mining, and independent validation gating. It converges faster than the full SkillOpt method and improves LiveMath by 8.8 points on GPT-5.5 and 25.4 points on GPT-5.4-nano, letting the nano model pass the larger standard GPT-5.4. Extended to full harness optimization, it reaches 0.7758 on SpreadsheetBench with GPT-5.4-nano, above GPT-5.5 running standard pipelines at 0.7620.

**How this builds on what you know:** Parents are ADaPT (J8DYBKW2), LATS (77ERE7HA), and ToolkenGPT (6RDHVVA2), all Community 0 (LLM Agents & Reasoning). Where ADaPT decomposed tasks on demand and LATS searched over action trees at inference time, SkillOpt-Lite instead optimizes the reusable skills and harness themselves offline, treating a skill as editable code updated by a numerical-optimization loop. This paper extends ADaPT and LATS, which already bridge planning-decomposition and tree-search agents in your library; the new work pushes that bridge toward persistent skill libraries rather than per-episode planning.

### Vision as Unified Multimodal Generation — SenseNova-Vision (Han et al., SenseNova, arXiv:2607.06560)

SenseNova-Vision poses detection, OCR, keypoint estimation, segmentation, depth, surface normals, point maps, and camera pose as one generation problem: natural-language instructions and optional visual prompts go in, and text, image, or mixed outputs come out, with no task-specific heads. Training uses a 50M instruction-response corpus converted from standard vision annotations, starting from an off-the-shelf unified multimodal model with auxiliary data as a capability-preserving mixture. A single model matches leading task-specialized systems across structured understanding, dense geometric prediction, segmentation, and multi-view geometry.

**How this builds on what you know:** Parents are DALL-E 2 (DUERBZGM) and DiT (YJ9TK993), Community 3 (Vision-Language & Generative), plus the Transformer (PHB9VRVM). Where DALL-E 2 and DiT generated pixels from text, this work reuses the same generative image space to emit dense predictions such as depth and segmentation instead of art, because posing perception as conditional image generation removes the need for a separate decoder per task.

---

## Tier C — scan

1. Gemma 4 Technical Report — Google's next open-weight family, sizes and benchmarks in one report. https://arxiv.org/abs/2607.02770
2. AlayaWorld: Long-Horizon and Playable Video World Generation — controllable, playable video world model. https://arxiv.org/abs/2607.06291
3. TurnOPD: Turn-Aware On-Policy Distillation — cheaper long-horizon agent training by making distillation turn-aware. https://arxiv.org/abs/2607.05804
4. Nemotron-Labs-Diffusion — one language model that runs autoregressive, diffusion, and self-speculation decoding. https://arxiv.org/abs/2607.05722
5. DSpark: Confidence-Scheduled Speculative Decoding — semi-autoregressive speculative decoding from DeepSeek. https://arxiv.org/abs/2607.05147
6. Light-Omni: Reflex over Reasoning in Agentic Video Understanding — long-term memory for video agents. https://arxiv.org/abs/2607.05511
7. Quantifying the Capacity of Late-Interaction Retrieval Models — theory bounds for ColBERT-style retrieval. https://arxiv.org/abs/2607.05803
8. When Classic Cache Policies Fail — learning-augmented cache replacement for semantic retrieval buffers. https://arxiv.org/abs/2607.00394

---

## Tier D — Time-series / Bio-sensing Gap Watch

Ported today: CLeaD (above) brings cross-lingual supervised contrastive alignment, a speech and NLP technique, into clinical bio-acoustics. It matches Community 1 (Health AI & Self-Supervised) and Community 5 (Wearable Sensing & Behavior), so cross-lingual contrastive alignment for health speech is now occupied ground rather than open.

Unported opportunity 1 — learned chunk retrieval for long sensor streams. HiLS-Attention (Tier A) has not been applied to long physiological or wearable time series. Transfer hypothesis: replace text chunks with fixed-duration signal windows and learn which past windows to attend to under a forecasting or classification loss, giving a sub-quadratic multi-day model that keeps content-based recall of distant events.

Unported opportunity 2 — perception as conditional generation for signals. SenseNova-Vision (Tier B3) poses many vision tasks as image generation. Transfer hypothesis: pose imputation, anomaly localization, and forecasting as masked-region generation over a 2D time-frequency map, so one generative model handles several sensor tasks without a separate head per task.

---

## News

xAI released Grok 4.5 on July 8, 2026, the most recent frontier model launch. Google published the Gemma 4 Technical Report and cleared Gemini 3.5 Pro for general availability in July after a slip from June. Google DeepMind also released two generative media models, Nano Banana 2 Lite for image generation and OmniFlash for video.

---

End of digest. Close this tab when done.
