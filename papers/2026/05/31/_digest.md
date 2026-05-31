# AI Digest — 2026-05-31

**Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.

**Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.

**Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Sunday is a quiet submission day, so the pool is small. One paper sits squarely in your forecasting work and earns the deep read; three method papers from multimodal and diffusion fill the TLDR slots.

---

## Tier A — Deep Read

### Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting
Agentic Learning AI Lab — [arXiv:2605.27668](https://arxiv.org/abs/2605.27668)

**Problem.** Probabilistic forecasting estimates how likely an uncertain future event is. When a language model is asked to forecast, it usually returns a single point probability, and that number is often poorly calibrated: the stated 70% does not match the empirical 70%. Verbalized confidence (asking the model how sure it is) is also an unreliable guide to error. The open question is how to turn a single point forecast from any model into a well-calibrated distribution, and how to read a usable uncertainty signal off that distribution.

**Method.** The authors propose the Beta-Bernoulli Calibrator (BBC), a lightweight, model-agnostic, post-hoc layer. It maps an initial point-probability forecast to a Beta distribution over the event likelihood. Training supervision comes from two sources at once: the realized binary outcomes (did the event happen) and human forecasts of the same events. The Beta mean serves as the recalibrated point forecast, and the Beta variance serves as an epistemic uncertainty estimate. Because it is post-hoc, BBC sits on top of any base LLM forecaster without retraining that model.

**Result.** Across several input LLMs, the Beta mean is better calibrated and more accurate as a point forecast than the raw model output. The Beta variance predicts forecasting error, which means the model knows, in a measurable way, when it is likely to be wrong. BBC is reported to calibrate better than models fine-tuned specifically for forecasting, both in-distribution and out-of-distribution, and its epistemic uncertainty is a more reliable error predictor than verbalized confidence.

**Limitations.** The method depends on having human forecasts as a second supervision signal, which is not available in every forecasting setting. The evaluation is on event-probability forecasting, not continuous numeric time-series forecasting, so transfer to multivariate sensor streams is a hypothesis rather than a demonstrated result. A Beta distribution assumes a single scalar event probability and does not directly model correlated multi-step horizons.

**Why it matters to Leo.** This sits at the intersection of LLM forecasting and calibrated uncertainty, both of which matter for time-series work. The post-hoc, model-agnostic design is attractive: it is a wrapper, not a new base model, so it could be tested on a wearable-derived forecaster without retraining. The finding that learned epistemic variance beats verbalized confidence is the part worth keeping, because verbalized confidence is the default people reach for and it does not hold up here.

**How this builds on what you know:** Your library holds two anchors in graphify Community 4 (Time Series + LLM Integration). TS-Agent (Liu 2025) [I2CIT4I7] established that an LLM can reason over numeric series through tool calls with an auditable evidence log, and the LLMs for Time Series survey (Zhang 2024) [N2JLZBY3] mapped the integration strategies and flagged calibration as underexplored. Where TS-Agent made the reasoning steps verifiable and the survey catalogued methods, this paper adds the missing calibration layer: it does not change how the LLM produces a forecast, it changes how much you should trust the number afterward. The contribution is orthogonal to the integration strategy, so it could be stacked on top of a tool-using forecaster rather than competing with it.

---

## Tier B — TLDRs

### DLLM-VSR: Diffusion Large Language Models for Visual Speech Recognition
Yeo, Kim, Rha, Ro (KAIST) — [arXiv:2605.28456](https://arxiv.org/abs/2605.28456)

Visual speech recognition reads lips from video, and standard systems decode left to right, which forces early guesses on ambiguous mouth shapes before later context arrives. DLLM-VSR is the first diffusion-LLM approach to the task: it treats transcription as iterative masked denoising with flexible decoding order, commits high-confidence tokens first, then uses them as bidirectional context to fix the ambiguous ones. A two-stage training scheme separates content alignment from length modeling, and a length-guided candidate decoder uses video duration to propose plausible transcript lengths. The method reaches a state-of-the-art 19.5% word error rate on LRS3 using only its labeled training data.

**How this builds on what you know:** The denoising mechanism comes straight from DDPM (Ho 2020) [GX7WR7KA] in graphify Community 3, which established iterative noise-to-signal generation. Where DDPM denoises continuous image pixels, this paper denoises discrete masked text tokens conditioned on video, so the same iterative-refinement idea moves from pixel space to sequence decoding. On the audio-visual side it neighbors Audio Mamba (Erol 2024) [6VTXUZEG] in your library, which also processes speech signals but through a state-space sequence model rather than diffusion-style unmasking.

### Mamoda2.5: Enhancing a Unified Multimodal Model with DiT-MoE
Shi, Zhu, Shen et al. (ByteDance) — [arXiv:2605.02641](https://arxiv.org/abs/2605.02641)

Mamoda2.5 is a single AR-Diffusion architecture that does both multimodal understanding and generation. The generation backbone is a Diffusion Transformer fitted with a fine-grained Mixture-of-Experts layer (128 experts, top-8 routing), giving a 25B-parameter model that activates only 3B parameters per step, which holds training cost down while raising capacity. It reaches top-tier scores on VBench 2.0 and sets a video-editing record on OpenVE-Bench, matching strong proprietary systems. A joint few-step distillation and reinforcement-learning stage compresses a 30-step editing model to 4 steps, reported as up to 95.9 times faster inference.

**How this builds on what you know:** The backbone is DiT (Peebles 2023) [YJ9TK993] from graphify Community 3, which showed that a transformer can replace the U-Net in a diffusion model and scale cleanly. Where DiT used a single dense transformer, this paper makes the transformer sparse with an expert-routing layer, so the scaling argument from DiT is pushed further by activating only a fraction of parameters per token. The underlying denoising process still traces back to DDPM (Ho 2020) [GX7WR7KA].

### MicroWorld: Bridging the Microscopic Domain Gap for Multimodal LLMs
Anonymous et al. — [arXiv:2605.10120](https://arxiv.org/abs/2605.10120)

General multimodal LLMs perform poorly on microscopy images because the visual domain is far from natural photos. MicroWorld builds a multimodal attributed property graph from large-scale scientific image-caption corpora and uses it to ground a multimodal LLM in microscopy-specific concepts and relations, closing part of the domain gap so the model can describe and reason about microscopic structures it was not pretrained on.

**How this builds on what you know:** The vision-language grounding lineage runs through DALL-E 2 (Ramesh 2022) [DUERBZGM] in graphify Community 3, which tied text and image representations together. Where DALL-E 2 aligned text and natural images, this paper adds a structured knowledge graph to align text with a specialist scientific image domain, because raw contrastive pretraining does not transfer to microscopy. It also neighbors the UNI pathology model (Chen 2023) [6T29JLTN] in your library, which addressed a related domain gap for medical imaging through self-supervised pretraining rather than a knowledge graph.

---

## Tier C — Scan

- **Continuous Latent Diffusion Language Model** — diffusion language modeling in a continuous latent space rather than over discrete tokens. [arXiv:2605.06548](https://arxiv.org/abs/2605.06548)
- **Bringing Multimodal LLMs to Infrared-Visible Image Fusion Quality Assessment** — uses an MLLM to score fused infrared-visible images. [arXiv:2605.06969](https://arxiv.org/abs/2605.06969)
- **Nexus: An Agentic Framework for Time Series Forecasting** — argues current LLMs forecast better than assumed when wrapped in an agent. [arXiv:2605.14389](https://arxiv.org/abs/2605.14389)
- **Squeezing Capacity from Multimodal LLMs for Subject-driven Generation** — conditions a diffusion generator on an MLLM for identity-preserving image generation. [arXiv:2605.26111](https://arxiv.org/abs/2605.26111)
- **GARD: Geometry-Aware Representation Denoising for Multi-view 3D Reconstruction** — runs diffusion restoration inside a 3D feature space. [arXiv:2605.26230](https://arxiv.org/abs/2605.26230)
- **Analyzing Diffusion and Autoregressive Vision-Language Models in Embedding Space** — compares the two decoding families on a shared embedding analysis. [arXiv:2602.06056](https://arxiv.org/abs/2602.06056)
- **Small but Mighty: Lightweight LLMs for Time Series Forecasting** — gets competitive forecasts from small models. [arXiv:2503.03594](https://arxiv.org/abs/2503.03594)
- **Assessing the Operational Viability of Foundation Models for Time Series Forecasting** — audits whether large TS foundation models earn their inference cost. [arXiv:2605.24381](https://arxiv.org/abs/2605.24381)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off).** Today's Tier A paper, the Beta-Bernoulli Calibrator, applies post-hoc probability calibration to LLM forecasting. This matches graphify Community 4 (Time Series + LLM Integration): calibrated uncertainty on top of an LLM forecaster is now demonstrated, so the generic "add calibration to an LLM forecaster" move is no longer open ground. What remains open inside it is the multivariate, continuous-horizon case, which the Beta-Bernoulli form does not cover.

**Unported opportunity 1 — diffusion-style masked denoising for physiological imputation.** DLLM-VSR (today, Tier B) decodes by confidence-based unmasking: commit certain tokens, then use them as bidirectional context to fix uncertain ones. No paper in Community 4 or Community 5 applies this to wearable sensor streams. Transfer hypothesis: treat gaps in a multivariate physiological stream as masked positions and recover them by confidence-ordered denoising, which would suit non-random missingness (a sensor drops out for minutes, not at random points) better than left-to-right imputation.

**Unported opportunity 2 — DiT-MoE sparse experts for wearable foundation models.** Mamoda2.5 (today, Tier B) shows a sparse expert layer that activates 3B of 25B parameters per step. No wearable-sensing foundation model in your library uses per-modality expert routing. Transfer hypothesis: route each sensor channel (accelerometer, PPG, ECG, temperature) to specialized experts so a large multivariate model keeps per-step compute low on long continuous streams.

---

## News

- **Anthropic Claude Opus 4.8** — reported launched on 28 May 2026, with improved benchmarks and stronger honesty behavior over Opus 4.7.
- **Google Gemini 3.5 Flash** — released 19 May 2026, a faster, lower-cost variant in the Gemini 3.x line.
- **Meta Muse Spark** — Meta's first flagship model from the new Superintelligence Labs, positioned for multimodal perception, reasoning, health, and agentic tasks.

May was quieter than the April release sprint, so these are the items worth noting rather than a full cycle.

---

End of digest. Close this tab when done.
