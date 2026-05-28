# AI Digest — 2026-05-28

**Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

**Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.

**Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### xMAE: Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning
Zhou, Lee, Tanade, Chun et al. — [arXiv:2605.00973](https://arxiv.org/abs/2605.00973) — **ICML 2026**

**Problem.** Most self-supervised methods for biosignals treat multi-sensor streams as interchangeable views and apply symmetric contrastive or reconstruction objectives. This ignores the directional temporal dynamics that link biosignals acquired from different body locations. For example, ECG captures the electrical activation that initiates a heartbeat, while PPG records the resulting peripheral pulse after a delay determined by vascular dynamics. Existing approaches discard this timing structure.

**Method.** xMAE introduces masked cross-modal reconstruction with a temporal ordering constraint. Rather than reconstructing masked patches within a single modality (standard MAE) or treating two modalities symmetrically, xMAE enforces that the reconstruction direction follows the known physiological causal path: ECG leads, PPG follows. The pretraining loss encodes the ECG-to-PPG pulse transit relationship as an inductive bias, encouraging the learned representations to capture physiologically meaningful timing structure.

**Result.** xMAE outperforms both unimodal and multimodal baselines on 15 of 19 downstream tasks. These tasks span cardiovascular outcome prediction, abnormal laboratory test detection, sleep staging, and demographic inference. The representations generalize across devices, body locations, and acquisition settings. Analysis of the learned PPG representations confirms that the ECG-PPG timing structure is reflected in the embeddings.

**Limitations.** The paper focuses on a single signal pair (ECG-PPG). Whether the temporal ordering approach extends to other biosignal pairs (e.g., EEG-EMG, or accelerometer-gyroscope) remains to be tested. The downstream evaluation uses clinical datasets where ECG and PPG are simultaneously available, which limits applicability to consumer wearables that may have only PPG.

**Why it matters to Leo.** This is an ICML 2026 paper directly in Leo's primary research area. The core idea — using known physiological temporal ordering as a pretraining inductive bias — is general and transferable. If you work with any pair of signals where one causally precedes the other, the xMAE design pattern applies. Code is available at github.com/hzhou3/xMAE.

**How this builds on what you know:** The Masked Autoencoders Theory paper (Zhang 2023) [zhang2023_mae, Community 1] established why masked reconstruction works as a pretraining objective. xMAE extends this from unimodal to cross-modal with a directional constraint — the reconstruction is asymmetric, matching the causal direction of the underlying physiology. The Foundation Models for Biosignals survey (Gu 2025) [gu2025_biosignals, Community 1] identified cross-modal pretraining with physiological priors as an open problem; xMAE is a concrete solution. HeAR (Baur 2024) [baur2024_hear, Community 1] showed self-supervised pretraining works for health audio, but used standard symmetric SSL. xMAE's contribution is showing that adding domain-specific temporal structure into the objective produces measurably better representations than treating modalities as exchangeable.

---

## Tier B — TLDRs

### 1. BenchHAR: Benchmarking Self-Supervised Learning for Generalizable Sensor-based HAR
Cai, Feng, Yu, Guo, Hong — [arXiv:2605.08296](https://arxiv.org/abs/2605.08296)

BenchHAR is a unified benchmark for evaluating how well SSL methods generalize in sensor-based human activity recognition on unseen target distributions. It curates roughly 258K samples and tests eight SSL methods across 12 encoder-classifier architectures. The main takeaways: hybrid pretraining (reconstruction plus contrastive) works best, CNN encoders learn the most generalizable representations, and scaling unlabeled pretraining data helps but only if it comes from the same activity classes as the downstream task — adding unlabeled data from unrelated activities does not improve generalization. Custom-grade sensor data generalizes better than research-grade, and limb-mounted data transfers better to trunk positions.

**How this builds on what you know:** Where SSL for HAR (Yuan 2024) [yuan2024_ssl_har, Community 1] showed that scaling self-supervised pretraining to 700K person-days improves HAR, BenchHAR refines the story with a negative result: more data from non-target activity classes does not help. This means the scaling recipe from Yuan 2024 must be qualified — it is domain-matched scale that matters, not raw volume.

### 2. Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key
Wang, Wang, Lan, Wei, Zhang, Qiu, Saparov — [arXiv:2605.06638](https://arxiv.org/abs/2605.06638)

ScaleLogic is a synthetic logical reasoning framework that independently controls proof depth and logical expressiveness (from simple if-then to first-order logic with conjunction, disjunction, negation, and universal quantification). The paper demonstrates that RL training compute follows a power law with respect to reasoning depth (T proportional to D^gamma, R^2 > 0.99), and the scaling exponent gamma increases from 1.04 to 2.60 as logic gets more expressive. Training on more expressive logics yields up to +10.66 points on downstream math/reasoning benchmarks and more compute-efficient transfer. Curriculum-based training substantially improves scaling efficiency.

**How this builds on what you know:** DeepSeek-R1 [deepseek2025_r1, Community 0] demonstrated RL-trained reasoning empirically at scale but on uncontrolled natural tasks. ScaleLogic provides the controlled environment to measure how RL compute scales with difficulty. The key insight — that training data expressiveness matters more than training data volume for downstream transfer — extends the cross-area bridge from deepseek2025_r1 to wei2023_cot by adding a quantitative scaling law.

### 3. Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs
Yang, Zang, Zhang, Shi, Su, Wang, Cheng, Sun — [arXiv:2605.07153](https://arxiv.org/abs/2605.07153)

RL is not just for reasoning. In a controlled zero-shot, closed-book QA setting (no chain-of-thought), RL yields roughly 27% average relative gains in factual recall across three model families. The mechanism is redistribution of probability mass: RL moves correct answers from the low-probability tail into reliable greedy generations rather than teaching the model new facts. A data-attribution study shows that the hardest examples (18% of training data where the answer never appears in 128 pre-RL samples) drive 83% of the total gain, because rare correct rollouts during training get reinforced.

**How this builds on what you know:** This broadens the role of RL established by DeepSeek-R1 [deepseek2025_r1, Community 0]. Where R1 used RL for reasoning, this paper shows RL has a second mode of action — surfacing latent knowledge the model already has but cannot reliably produce. The mechanism (probability mass redistribution vs. new capability acquisition) is a useful distinction for understanding what RL training actually changes in the weights.

---

## Tier C — Scan

| Paper | Hook | Link |
|---|---|---|
| VCR: Valid Contextual Representation for Incomplete Wearable Signals | Self-supervised framework robust to arbitrary modality missingness in wearables | [2605.18837](https://arxiv.org/abs/2605.18837) |
| The Unlearnability Phenomenon in RLVR | A substantial subset of hard examples remains unlearnable even with correct rollouts — fundamental representation issue | [2605.16787](https://arxiv.org/abs/2605.16787) |
| Same Architecture, Different Capacity: Optimizer-Induced Spectral Scaling Laws | AdamW vs Muon produce different spectral scaling laws in the same Transformer | [2605.21803](https://arxiv.org/abs/2605.21803) |
| Linear RNNs as Time-Delay Embeddings | Linear recurrent nets implicitly perform Takens-style time-delay embedding | [2605.27290](https://arxiv.org/abs/2605.27290) |
| Memory-Efficient Looped Transformer (MELT) | Decouples reasoning depth from memory consumption in looped LMs | [2605.07721](https://arxiv.org/abs/2605.07721) |
| Prompting Policies for Multi-step Reasoning and Tool-Use | RL framework trains a lightweight prompter to steer a frozen worker LLM | [2605.14443](https://arxiv.org/abs/2605.14443) |
| ElasticDiT: Efficient Diffusion Transformers on Mobile | Elastic architecture + sparse attention for high-res image gen on phones | [2605.15684](https://arxiv.org/abs/2605.15684) |
| More Expressive Feedforward Layers: Token-Adaptive Mixing | Replaces fixed activation functions with token-dependent mixing | [2605.26647](https://arxiv.org/abs/2605.26647) |

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**

xMAE (Tier A) imports the masked autoencoder paradigm from vision into cross-modal biosignal pretraining. The transfer path (MAE from vision/NLP to biosignals) is now well-covered: xMAE, the wearable health FM from yesterday (Narayanswamy et al.), and earlier work like HeAR all use variants of masked reconstruction for health signals. This specific transfer is no longer low-hanging fruit.

BenchHAR (Tier B) applies the standard SSL benchmarking methodology from CV (systematic comparison of pretraining paradigms across architectures) to HAR. The benchmarking transfer pattern is closed off.

**Unported opportunity:**

Linear RNNs as Time-Delay Embeddings (2605.27290) shows that linear recurrent neural networks implicitly perform Takens-style time-delay embedding — a classical dynamical systems technique for reconstructing attractor geometry from scalar time series. Transfer hypothesis: if linear RNNs are implicitly doing delay embedding, then combining them with the xMAE-style physiology-aware pretraining could yield a model that simultaneously captures the attractor structure of cardiac dynamics and the cross-modal temporal ordering between ECG and PPG. This would give a representation that is both dynamically grounded (via delay embedding) and physiologically grounded (via cross-modal timing). No one has combined these two ideas for biosignals yet.

The Optimizer-Induced Spectral Scaling Laws paper (2605.21803) shows that AdamW and Muon produce fundamentally different rank scaling in transformer representations. Transfer hypothesis for time-series: the choice of optimizer may matter more than architecture for TS transformers, where the effective rank of learned representations determines whether the model captures rare but clinically meaningful patterns. This has not been studied for TS/biosignal models.

---

## News

**DeepSeek V4-Pro** released in late May 2026, continuing DeepSeek's rapid iteration cadence. Details still emerging.

**Alibaba Qwen 3.7 Max** released, expanding the Qwen family with a larger variant.

**Google Gemini 3.5 Flash** reached general availability on May 19 at Google I/O 2026. Google led the keynote with the smaller, faster Flash model rather than the Pro tier, signaling that efficient agent-era inference is the priority. Pro is expected in June.

---

End of digest. Close this tab when done.
