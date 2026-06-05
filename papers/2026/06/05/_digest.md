# Daily AI Research Digest — 2026-06-05

Today's sweep covers cross-domain reinforcement learning for LLM reasoning, curriculum-based RL for small models, cross-modal biosignal foundation models, and parameter-efficient test-time adaptation for time-series forecasting. Six additional papers and three industry items round out the digest.

---

> **Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 6 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
> **Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.
> **Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.



## Tier A — Deep Read

### GURU: Revisiting RL for LLM Reasoning from A Cross-Domain Perspective
**arxiv 2506.14965** | June 2026
[arXiv](https://arxiv.org/abs/2506.14965) | [note](2506.14965.md) | Areas: reasoning, rl

**Problem.** Current reinforcement learning approaches to LLM reasoning — most notably GRPO and its descendants — train and evaluate almost exclusively on math and code. It remains unclear whether RL-trained reasoning generalizes across domains, and if not, what determines which domains benefit from cross-domain transfer versus requiring in-domain training.

**Method.** The authors construct the Guru corpus: 92,000 verifiable examples spanning six domains — Math, Code, Science, Logic, Simulation, and Tabular reasoning. Each example has a ground-truth verifier, enabling reward-based RL without human annotation. They train GURU-7B and GURU-32B using GRPO-style optimization on various domain combinations and measure transfer matrices across all six domains. The experimental design is systematic: single-domain training, leave-one-out cross-domain training, and full mixed training, all evaluated on a 17-task benchmark suite.

**Result.** GURU-7B and GURU-32B achieve state-of-the-art among open RL-trained models, outperforming baselines by 7.9% and 6.7% respectively on the 17-task evaluation. The central finding is a clean dichotomy: domains that are well-represented during pretraining (Math, Code, Science) transfer easily from cross-domain RL, while underrepresented domains (Logic, Simulation, Tabular) require explicit in-domain training to benefit. This suggests RL does not merely surface cached pretraining knowledge but facilitates genuine skill acquisition — and the ease of that acquisition depends on the foundation of pretraining exposure.

**Limitations.** The study uses only GRPO as the RL algorithm; it is possible that other RL methods (PPO, DPO variants) would show different transfer patterns. The corpus, while large, uses synthetic verifiers that may not capture the full difficulty distribution of each domain. The paper does not investigate whether the pretraining-exposure hypothesis holds for models trained on different data mixtures.

**Why it matters.** This paper directly addresses a gap in the reasoning literature that Leo tracks through Community 0. DeepSeek-R1 demonstrated that RL can produce strong reasoning, and chain-of-thought prompting showed that multi-step reasoning benefits from explicit intermediate steps. GURU asks the next question: does RL reasoning generalize, and if so, how? The answer — that transfer depends on pretraining exposure — has practical implications for anyone building domain-specific reasoning systems.

**How this builds on what you know.** In Leo's knowledge graph, deepseek2025_r1 and wei2023_cot are the two anchors of Community 0's reasoning cluster. GURU sits directly downstream of both: it uses DeepSeek-R1's GRPO training recipe and evaluates the kind of multi-step reasoning that chain-of-thought prompting first demonstrated. The cross-domain transfer analysis also connects to the agent literature (durante2024_agentai, zhou2024_lats) because agentic systems must reason across heterogeneous task types. The finding that underrepresented domains need in-domain RL training is directly relevant to Leo's time-series and biosignal work — these domains are almost certainly underrepresented in standard pretraining corpora, suggesting that any RL-based reasoning for sensor data will require domain-specific training rather than relying on transfer from math and code.

---

## Tier B — Detailed Notes

### E2H Reasoner: Curriculum RL from Easy to Hard Tasks
**arxiv 2506.06632** | June 2026
[arXiv](https://arxiv.org/abs/2506.06632) | [note](2506.06632.md) | Area: reasoning

Small language models (1.5B to 3B parameters) frequently fail to learn from vanilla RL because the reward signal is too sparse on hard tasks — the model almost never produces a correct answer, so there is nothing to reinforce. E2H Reasoner addresses this by scheduling RL training tasks from easy to hard using a curriculum derived from approximate policy iteration, providing convergence guarantees that vanilla GRPO lacks. The method produces significant improvements on models that otherwise stall completely during RL training.

**How this builds on what you know.** This extends the DeepSeek-R1 line (deepseek2025_r1) by making RL viable for much smaller models. Where R1 required 671B parameters to benefit from GRPO, E2H brings the same training paradigm to the 1.5B-3B range. Combined with yesterday's GRAIL paper (token-level credit) and GURU's cross-domain analysis, a picture is forming: the field is systematically removing the constraints on RL-based reasoning — model size (E2H), credit granularity (GRAIL), and domain coverage (GURU).

---

### Biosignal Fingerprinting: A Cross-Modal PPG-ECG Foundation Model
**arxiv 2605.09579** | May 2026
[arXiv](https://arxiv.org/abs/2605.09579) | [note](2605.09579.md) | Areas: llm-health, time-series

A Multi-modal Masked Autoencoder (M2AE) trained on 3.4 million paired ECG and PPG signal segments using cross-modal contrastive learning plus reconstruction. It achieves AUROC 0.974 for 5-class cardiovascular disease classification and 0.877 for hypertension detection. The critical feature is single-modality inference: a model pretrained on paired data works with PPG alone at deployment, meaning consumer wearables benefit from hospital-grade ECG-informed representations without requiring an ECG sensor.

**How this builds on what you know.** This paper extends zhang2023_mae (masked autoencoders for time-series) to paired multi-modal biosignals and builds directly on the biosignal foundation model survey (gu2025_biosignals, Community 1). The cross-modal contrastive pressure is what distinguishes it from simply training separate per-modality MAEs — it forces modality-invariant features that enable the single-sensor deployment story. For Leo's wearable sensing work (Community 5), this is a concrete demonstration that foundation model pretraining on hospital data can improve consumer-device inference.

---

### PETSA: Parameter-Efficient Test-Time Adaptation for Time Series Forecasting
**arxiv 2506.23424** | June 2026
[arXiv](https://arxiv.org/abs/2506.23424) | [note](2506.23424.md) | Areas: time-series, test-time-training

Foundation models for time-series forecasting often degrade when the test distribution shifts from training. PETSA addresses this by updating only small calibration modules — low-rank adapters plus dynamic gating — at test time. It uses a specialized loss combining a robust reconstruction term, a frequency-domain term, and a patch-wise structural term. The result is competitive performance with far fewer updated parameters than full-model test-time adaptation baselines.

**How this builds on what you know.** This paper sits at the intersection of two areas Leo tracks: time-series foundation models (PatchTST, Sundial, Community 4) and test-time training (TTT for Abstract Reasoning, TTT Layers, Community 2). PETSA is the first paper in Leo's reading to apply test-time adaptation specifically to time-series foundation models with a parameter-efficient approach. The frequency-domain loss component is worth noting — it addresses the spectral shift problem that PatchTST and similar patching-based models are vulnerable to when deployed on out-of-distribution signals.

---

## Tier C — Headlines and Hooks

**MHGPO: Heterogeneous Group RL for Multi-Agent LLM Systems** (2506.02718) — Extends GRPO to multi-agent settings with heterogeneous reward structures. Relevant if following the RL-for-reasoning thread. [arXiv](https://arxiv.org/abs/2506.02718)

**RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning** (2606.00147) — Iterative data refinement with adaptive temperature distillation for domain-specific fine-tuning without catastrophic forgetting. [arXiv](https://arxiv.org/abs/2606.00147)

**Test-Time Distillation for Continual Model Adaptation (CoDiRe)** (2506.02671) — Combines test-time training with knowledge distillation for continual domain shift. Related to today's PETSA paper. [arXiv](https://arxiv.org/abs/2506.02671)

**Compress-Distill: Reasoning Trace Compression for Knowledge Distillation** (2606.05988) — Compresses verbose chain-of-thought traces before distillation, reducing teacher-student transfer cost. [arXiv](https://arxiv.org/abs/2606.05988)

**Geometry-Aware Representation Denoising for Multi-view 3D Reconstruction** (2605.26230) — Denoises latent representations using geometric priors for multi-view consistency. [arXiv](https://arxiv.org/abs/2605.26230)

**DiffThinker: Generative Multimodal Reasoning with Diffusion Models** (2512.24165) — Uses diffusion models as a reasoning backbone rather than autoregressive generation. [arXiv](https://arxiv.org/abs/2512.24165)

---

## Gap Watch — Time-Series and Biosignal Transfer Opportunities

**Already ported to TS/bio:**

The "Biosignal Fingerprinting" paper (2605.09579) represents masked autoencoders — originally a computer vision technique (zhang2023_mae) — now fully adapted to paired PPG/ECG biosignals. PETSA (2506.23424) demonstrates test-time training concepts moving into time-series forecasting, though the adaptation is parameter-efficient rather than full-model. Both indicate the technique-transfer pipeline from vision and NLP into time-series is accelerating.

**Unported — high potential:**

1. **GURU's domain-transfer analysis applied to time-series reasoning agents.** GURU (2506.14965) shows that RL-based reasoning transfers easily across well-represented pretraining domains but fails for underrepresented ones. Time-series and biosignal reasoning are almost certainly in the underrepresented category. This suggests that TS-Agent (liu2025_tsagent) and similar systems will not benefit from cross-domain RL transfer and will need dedicated in-domain RL corpora with verifiable rewards — a dataset that does not yet exist.

2. **Curriculum RL for small on-device reasoning models.** E2H Reasoner (2506.06632) makes RL viable for 1.5B-3B parameter models via easy-to-hard scheduling. Wearable and edge devices cannot run 7B+ models but could plausibly run 1.5B-3B models. Applying E2H-style curriculum RL to train small time-series reasoning models for on-device clinical inference is an open opportunity. No current work combines curriculum RL with time-series foundation models at this scale.

---

## Industry News

**Anthropic released Claude Opus 4.8** on May 28. The model introduces dynamic workflows and leads the Super-Agent benchmark. Pricing is $5 per million input tokens and $25 per million output tokens.

**Google released Gemini 3.5 Flash** at I/O 2026 on May 19. It outperforms Gemini 3.1 Pro on agentic benchmarks while costing 40% less. Google is positioning it as an agent-first model with native tool-use and multi-step planning.

**Microsoft released MAI-Code-1-Flash** at Build 2026 on June 2. It is a 5-billion-parameter coding model and the first model Microsoft has built entirely in-house, without involvement from OpenAI.

---

End of digest. Close this tab when done.
