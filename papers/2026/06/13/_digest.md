# AI Digest — 2026-06-13

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (~20 min)

### Next-Token Prediction Learns Generalisable Representations of Sleep Physiology
arXiv:2606.09605 (Cai et al., 2026-06-08) — https://arxiv.org/abs/2606.09605

**Problem.** Foundation models would help compress multi-modal physiological signals into compact health representations, but the two usual self-supervised recipes do not fit the data. Masked reconstruction assumes a signal that is largely predictable from its context, which clashes with the stochastic nature of physiology. Contrastive learning needs a definition of positive pairs, and the invariances of physiological signals are not well enough understood to set one.

**Method.** The model, Hypnos, tokenizes each of eight modalities (including EEG, ECG, and respiratory signals) with residual vector quantization, turning each continuous waveform into a stream of discrete codes. A large autoregressive RQ-Transformer is then trained by next-token prediction over the combined multi-modal stream, the same objective used for language models. Training uses more than 20,000 overnight polysomnography recordings, and at inference the model can run on any subset of the modalities.

**Result.** The learned representations transfer to downstream health tasks and, notably, generalize past sleep to daytime physiology: the model surpasses a dedicated ECG foundation model at detecting atrial fibrillation, despite being trained mainly on overnight data. This is the headline number — a general autoregressive recipe beats a purpose-built ECG model on a cardiology task.

**Limitations.** The released summary reports task-level wins but not a full per-task table, so the size of the margin across tasks is hard to judge from the abstract alone. The training data is sleep-heavy, so the claim that next-token prediction beats masked reconstruction may hold for this data mix rather than for physiology in general.

**Why it matters to you.** This is your primary area. It imports next-token prediction from language modeling and residual vector quantization from neural audio and image codecs, and shows the pair works for multi-modal physiology.

**How this builds on what you know:** The closest parents in your library are Foundation Models for Biosignals: A Survey (Gu 2025, Health AI & Self-Supervised community) and How Mask Matters: MAE Theory (Zhang 2023, same community), with the autoregressive machinery coming from Attention Is All You Need (Vaswani 2017, Transformer community). Where Gu 2025 laid out masked reconstruction and contrastive learning as the two main recipes, this paper argues both carry assumptions physiology breaks and replaces them with next-token prediction. Where Zhang 2023 studied masked reconstruction in pixel space, Hypnos discretizes the signal first and models it autoregressively, because token-level prediction sidesteps both the predictability assumption of masking and the positive-pair assumption of contrastive learning.

---

## Tier B — TLDRs (~10 min)

### Personalized Forecasting of Impending Atrial Fibrillation from Wearable ECG
arXiv:2606.10900 (Suh et al., 2026-06-09) — https://arxiv.org/abs/2606.10900

A global ECG model trained on ICENTIA11K is fine-tuned on each patient's own signals to forecast impending atrial fibrillation over a five-minute horizon from 60-second segments. Personalization lifts AUROC from 0.614 to 0.711 on ICENTIA11K and from 0.585 to 0.686 on MobiCARE, and the gain grows with the amount of patient-specific data. Feature attributions point to premature atrial complexes and short supraventricular tachycardias as precursors. The message is that test-time personalization, not a bigger global model, closes the gap.

**How this builds on what you know:** Closest parents are Foundation Models for Biosignals (Gu 2025) and LLMs are Few-Shot Health Learners (Liu 2023), both in the Health AI & Self-Supervised community. Where Gu 2025 aimed for one global model across patients, this paper shows inter-patient ECG variability holds that model back and that per-patient fine-tuning recovers much of the lost accuracy. Where Liu 2023 adapted a general model to health tasks with small labeled sets, this paper applies the same adaptation at the level of a single patient and measures how the benefit scales.

### From Player to Master: RL over Memory for LLM Agents (MemoPilot)
arXiv:2606.08656 (Cai et al., 2026-06-07, ICML 2026) — https://arxiv.org/abs/2606.08656

MemoPilot is a plug-in that learns how to update an LLM agent's explicit memory so a frozen base model improves across a long run of interactions. Memory updating is framed as a multi-turn decision problem and trained with multi-turn GRPO, using a turn-wise reward and a turn-level advantage estimate for finer credit assignment. On Rock-Paper-Scissors and Limit Texas Hold'em it ranks first in Elo (1762 on Hold'em, 1590 on RPS), beating hand-designed memory rules and proprietary models including DeepSeek-V3.2.

**How this builds on what you know:** Parents are Rethinking Memory Mechanisms of Foundation Agents (Huang 2026) and DeepSeek-R1: Reasoning via RL (2025), both in the LLM Agents & Reasoning community. Where Huang 2026 described memory updated by hand-written rules, this paper makes the update itself a learned policy. Where DeepSeek-R1 applied GRPO to a single reasoning trace, MemoPilot extends GRPO to multi-turn memory edits with turn-level credit assignment. This paper extends DeepSeek-R1, which already crossed reasoning-via-RL and chain-of-thought prompting in your library; the new work pushes that bridge from one-shot reasoning toward long-horizon control of an external memory.

### Where Should Knowledge Enter? Layered Knowledge Infusion in Multimodal Generative Models
arXiv:2606.06356 (2026-06-04) — https://arxiv.org/abs/2606.06356

The paper asks where to inject knowledge into iterative generative models such as diffusion when output must respect structured or safety-critical constraints. It defines four injection layers — surface (input/output boundary), trajectory (transition function), latent (intermediate state), and parametric (model parameters) — and shows in a safety-alignment study on two diffusion backbones that each layer catches failures the others miss, cutting knowledge-violating outputs by 70.97% versus plain generation.

**How this builds on what you know:** Parents are Denoising Diffusion Probabilistic Models (Ho 2020) and DiT (Peebles 2023), both in the Vision-Language & Generative community. Where DDPM defined a fixed denoising transition with no place for external constraints, this paper treats the transition and intermediate states as injection points. Where DiT scaled the backbone, this paper holds the backbone fixed and varies the infusion layer instead, producing a map from constraint type to where it should be enforced.

---

## Tier C — scan (~5 min)

- ExpWeaver: LLM agents learn from experience via latent RAG, optimized end-to-end with RL. https://arxiv.org/abs/2606.01041
- AdaPlanBench: benchmark for adaptive planning in LLM agents under progressively revealed world and user constraints. https://arxiv.org/abs/2606.05622
- Spectral audit framework finds task-dependent aperiodic (1/f) reliance in EEG and ECG deep learning. https://arxiv.org/abs/2606.08583
- Counterexample-guided learning at scale: a verifier returns counterexamples to teach LLM agents regular-expression induction. https://arxiv.org/abs/2606.11521
- ART: art-based reinforcement training for fine-tuning multimodal LLMs. https://arxiv.org/abs/2606.11854
- Generative criticality in LLM temperature scaling treats token embeddings as continuous spin variables. https://arxiv.org/abs/2606.06238
- Flaws in the LLM Automation Narrative: argues benchmarks measure training-data overlap, not reliability or error magnitude. https://arxiv.org/abs/2606.11166
- Infectious disease spread simulation driven by LLM decision-making over a census-based synthetic population. https://arxiv.org/abs/2606.06360

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closing as low-hanging fruit). Hypnos (2606.09605) ports next-token prediction plus residual vector quantization from language and audio/image codecs into multi-modal physiology; that recipe is now demonstrated, so "tokenize a bio-signal with RVQ then train an autoregressive model" is no longer an open transfer. The AFib forecasting paper (2606.10900) ports test-time personalization by fine-tuning, already standard in CV and NLP, onto wearable ECG; that transfer is also largely closed.

Unported opportunity. The layered knowledge-infusion framework (2606.06356) has not been applied to diffusion-based physiological signal generation or imputation. Transfer hypothesis: use trajectory- or latent-layer infusion to enforce clinical constraints (for example bounds on heart-rate variability or QT interval) while a diffusion model imputes missing ECG or PPG segments, so generated signals stay physiologically valid.

Unported opportunity. MemoPilot's multi-turn GRPO over an explicit memory (2606.08656) has not been applied to a time-series monitoring agent. Transfer hypothesis: train the memory-update policy of a wearable monitoring agent so it keeps a useful per-patient state across days, optimizing the memory edits for a downstream forecasting or alerting reward.

---

## News — major releases

Three frontier releases are reported in the trade press this month. These are vendor and press claims, not independently verified benchmarks. Google introduced Gemini 3.1 Flash-Lite, an efficiency-focused model reported at about 2.5x faster responses and lower output latency, priced near $0.25 per million input tokens. Meta unveiled Muse Spark, described as its first flagship proprietary model under the new Superintelligence Labs and a step away from the open Llama line. Anthropic released Claude Fable 5, a general-access model in its Mythos class, alongside Project Glasswing, a limited program giving select organizations early access to find and fix software vulnerabilities.

---

End of digest. Close this tab when done.
