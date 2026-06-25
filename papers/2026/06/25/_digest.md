# AI Digest — 2026-06-25

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on today's signal: the fresh arXiv listings for time series and bio-sensing are thin this morning. Nothing dated today clears the Tier A bar on its own. The Tier A slot is therefore filled by a recent wearable self-supervised paper that is new to your knowledge graph and sits at the center of your primary area. The Tier B set mixes one fresh June paper with two recent ones you have not seen yet.

---

## Tier A — deep read

### HiMAE: Hierarchical Masked Autoencoders Discover Resolution-Specific Structure in Wearable Time Series
arXiv 2510.25785 — https://arxiv.org/abs/2510.25785

Problem. Wearable sensors produce long physiological time series, but it is unclear which temporal scales carry the signal that downstream health tasks need. Most self-supervised models pick one resolution and collapse everything to it, which hides the question rather than answering it. The paper asks whether temporal resolution is a real axis of representation learning, meaning different outcomes depend on structure at different scales, and whether a model can be built that exposes this instead of averaging it away.

Method. HiMAE combines masked autoencoding with a hierarchical convolutional encoder-decoder shaped like a U-Net. Each level of the hierarchy corresponds to a distinct temporal granularity, so the model produces several embeddings at once, one per scale. Linear probes on each level then measure which resolution carries predictive signal for a given task, turning resolution from a hyperparameter into a measurement tool. The convolutional bias is a deliberate choice over a transformer: the authors argue wearable signals are long but low-dimensional and highly structured, so a transformer can overfit and blur scale-specific structure rather than reveal it.

Result. Across 14 classification and regression tasks plus generative benchmarks, HiMAE reports state-of-the-art accuracy while being orders of magnitude smaller than foundation models that collapse scale. The compactness is the headline practical number: it runs entirely on a smartwatch-class CPU with sub-millisecond inference, which the authors state is the first wearable self-supervised encoder to do true on-device inference. The probing analysis also surfaces resolution-specific structure that human experts do not readily name.

Limitations. The "resolution hypothesis" is demonstrated on the chosen benchmark set, not proven in general; tasks outside that set may not split cleanly by scale. The convolutional hierarchy fixes the available resolutions by architecture, so a scale that matters but is not represented by a level cannot be probed. Gains are reported against foundation-model baselines, and head-to-head numbers depend on how those baselines were tuned for size.

Why it matters to Leo. This is directly in your primary area and it gives two things at once: a compact wearable encoder that fits on-device, and a method for asking which time scale a physiological outcome actually lives at. The second point is the more useful one for your own work, because it is a probe you can reuse on your own signals rather than a single model to adopt.

How this builds on what you know: Where MAE (He, self-supervised area) introduced masked reconstruction as a pretraining objective for images, and How Mask Matters (Zhang 2023, Health AI and Self-Supervised community in your library) studied what the masking ratio and structure actually buy, HiMAE keeps the masked-reconstruction objective but swaps the flat encoder for a hierarchical convolutional one, because the goal is no longer a single embedding but one embedding per temporal scale. Where HARMamba (Li 2024) pursued an efficient wearable architecture through a state-space model, HiMAE pursues efficiency through convolutional hierarchy and adds the resolution probe that HARMamba does not have. It sits in the same community as the SSL-for-HAR god node in your library and competes with it directly: same masked-pretraining family, but the contribution is the scale analysis, not the dataset scale. The Foundation Models for Biosignals survey (Gu 2025) is the map of this area; HiMAE is one more point on it that argues against the "one universal resolution" default the survey describes.

---

## Tier B — TLDRs

### IMPACT: Influence Modeling for Open-Set Time Series Anomaly Detection
arXiv 2603.29183 — https://arxiv.org/abs/2603.29183

Open-set anomaly detection uses a few labeled anomalies seen in training to catch both those and unseen anomaly types at test time. The paper shows that methods carried over from other domains fail on time series because they do not preserve sequence structure, so the synthetic anomalies they create are trivial or unrealistic. IMPACT instead quantifies how much each training sample changes test risk, then uses those influence scores two ways: it relabels contaminated training points by flipping labels that raise risk, and it synthesizes realistic unseen anomalies by perturbing features in the direction that influence says matters. The reported effect is better detection of unseen anomaly types without losing the seen ones. It was accepted at ICML 2026.

How this builds on what you know: No direct parent sits in your library; influence functions for data attribution are not in your collection yet. The closest neighbor you do have is VAN-AD (your 2026-06-24 note), which also targets time-series anomaly detection but does so through masked-autoencoder reconstruction plus a normalizing-flow density head, where IMPACT works at the level of training-data attribution rather than the model's reconstruction error. Read together they mark two different routes to the same goal: VAN-AD makes the score calibrated, IMPACT makes the training set and the synthetic anomalies honest.

### Uncertainty-Aware Foundation Models for Clinical Data
arXiv 2604.04175 — https://arxiv.org/abs/2604.04175

Clinical foundation models inherited the "large pretraining, single deterministic embedding" recipe from language and vision, but clinical observations are sparse, irregular, and modality-dependent measurements of a hidden physiologic state. The paper represents each patient not as one point embedding but as a distribution over plausible latent states, learned by enforcing agreement across partial views of the same patient so the model captures what can be inferred and marks the rest as epistemic uncertainty. The objective mixes reconstruction, contrastive alignment, and a distributional regularizer inside a multimodal encoder. Across clinical tasks it reports better prediction, better robustness when data is missing, and better-calibrated uncertainty than point-embedding baselines.

How this builds on what you know: Where the Foundation Models for Biosignals survey (Gu 2025, Health AI and Self-Supervised community) maps clinical foundation models that all emit point embeddings, and MAE-style reconstruction (He; How Mask Matters, Zhang 2023) supplies the self-supervised objective, this paper keeps the reconstruction-plus-contrastive recipe but changes the output object from a point to a set-valued distribution, because missing and irregular clinical data make a single deterministic embedding an overconfident summary. The new ingredient relative to your library is treating "what was not observed" as a modeling target rather than a nuisance.

### PerceptionDLM: Parallel Region Perception with Multimodal Diffusion Language Models
arXiv 2606.19534 — https://arxiv.org/abs/2606.19534

Most multimodal language models generate text autoregressively, one token at a time, which is slow when a task asks for descriptions of many image regions at once. PerceptionDLM builds on a discrete diffusion multimodal backbone that decodes tokens in parallel, and adds prompting plus structured attention masking so the model can describe several masked regions simultaneously at both the sequence and token level. The result is a clear inference-efficiency gain over models that handle regions one after another, while keeping competitive perception quality. The work comes from ByteDance and Peking University and is one of the few fresh June papers in this digest.

How this builds on what you know: Where DiT (Peebles 2023, Vision-Language and Generative community in your library) showed a diffusion model can run on a transformer backbone for image generation, PerceptionDLM carries the diffusion-with-transformer idea into the language side of a multimodal model and uses its parallel decoding for perception rather than image synthesis, because the payoff here is describing many regions at once instead of denoising pixels. No multimodal diffusion language model sat in your library before; the nearest anchors are the diffusion nodes (DiT, DDPM) in community 3.

---

## Tier C — scan headlines

- RAID: Semantic Graph Diffusion for True Cold-Start Recommendation — diffusion over a semantic item graph to recommend items with no interaction history. https://arxiv.org/abs/2606.16925
- Generalist vs Specialist Time Series Foundation Models for PPG — asks whether a broad time-series model beats a PPG-specific one on health tasks. https://arxiv.org/abs/2510.14254
- LSM-2: Learning from Incomplete Wearable Sensor Data — pretrains directly on gappy wearable streams instead of imputing first. https://arxiv.org/abs/2506.05321
- Speech Foundation Models Generalize to Time Series Tasks from Wearable Sensors — speech encoders transfer to accelerometer and physiological signals. https://arxiv.org/abs/2509.00221
- CREMA: Contrastive Regularized Masked Autoencoder for ECG — adds contrastive regularization to MAE for cross-domain ECG diagnosis. https://arxiv.org/abs/2407.07110
- Retrieval-aligned Tabular Foundation Models for Clinical Risk — tabular foundation model with retrieval for robust EHR risk prediction. https://arxiv.org/abs/2604.01841
- Dynin-Omni: Omnimodal Unified Large Diffusion Language Model — one diffusion language model across several modalities at once. https://arxiv.org/abs/2604.00007
- IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents — scores agent actions against inferred user intent. https://arxiv.org/abs/2604.05157

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off as low-hanging fruit). HiMAE carries the masked-autoencoder objective from vision into wearable time series and adds a convolutional hierarchy, which matches the Health AI and Self-Supervised community in your library; the masked-reconstruction transfer to wearables is now well covered. IMPACT brings influence-function data attribution into time-series anomaly detection, so that particular transfer is taken. Uncertainty-Aware clinical modeling ports set-valued, distributional self-supervised representations into multimodal clinical data, closing that route as well.

Unported opportunity. Multimodal diffusion language models with parallel decoding (PerceptionDLM, Vision-Language and Generative community) have not been applied to multivariate physiological time series. Transfer hypothesis: a discrete or continuous diffusion decoder could fill several missing sensor windows in one denoising pass rather than imputing autoregressively, and the structured attention masking that lets PerceptionDLM describe several image regions at once maps almost directly onto reconstructing several masked channels of a PPG, ECG, and IMU record at once. This would be a parallel-imputation foundation model for wearables, which your library does not yet contain.

---

## News

No major model reached general availability this week. Gemini 3.5 Pro remains in limited preview for select Vertex AI enterprise customers as of late June; Google has not given a committed public date. Reported specifications include a 2M-token context window and a Deep Think reasoning mode. There is no Grok 5; xAI's current flagship is Grok 4.3 from late April. Treat the rest of this week's "release" chatter as preview and rumor rather than shipped product.

---

End of digest. Close this tab when done.
