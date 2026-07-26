## Generative Computer Vision

### Timeline

2014 | GAN (Goodfellow et al.) | 
2015 | Nonequilibrium Thermodynamics (Sohl-Dickstein et al.) | 
2018 | FID (Heusel et al.) | 
2019 | StyleGAN (Karras et al.) | 
2020 | CycleGAN (Zhu et al.) | 
2020 | DDPM (Ho et al.) |  [anchor]
2021 | Diffusion Beats GANs (Dhariwal et al.) | 
2021 | Score SDE (Song et al.) | 
2021 | TimeGrad (Rasul et al.) | 
2022 | DDIM (Song et al.) | 
2022 | Palette (Saharia et al.) | 
2022 | Stable Diffusion (Rombach et al.) | 
2022 | StyTr2 (Deng et al.) | 
2023 | BLIP-Diffusion (Li et al.) | 
2023 | CTG++ (Zhong et al.) | 
2023 | DiT (Peebles et al.) | 
2023 | LED (Mao et al.) | 
2024 | l-DAE (Chen et al.) | 

2026-05 | MLLM Subject-Driven Generation (2605.26111) | aggregates features across several language-model layers to preserve subject identity
2026-05 | GARD (2605.26230) | runs diffusion denoising inside a reconstructor's geometry-aware feature space
2026-05 | Mamoda2.5 (2605.02641) | unified AR-diffusion model with a 128-expert MoE DiT backbone, 25B parameters and 3B active per step
2026-06 | CogOmniControl (2605.19995) | infers creative intent first, then generates video conditioned on that inferred intent

2026-06 | RTDMD (2605.26108) | reward-tilted distribution matching distills few-step generators with preference RL
2026-06 | UQ for Flow-Based VLA (2606.18043) | calibrated confidence and out-of-distribution flags for flow-matching action generators
2026-07 | MetaWorld (2606.02753) | multi-agent video world model trained from single-view video via monocular ego-motion and subject decomposition
2026-07 | Prisma-World (2606.09507) | camera-controllable multi-agent video with geometry-conditioned full attention and a synthetic dataset
2026-07 | PointDiT (2607.02515) | pixel-space diffusion transformer denoises raw point maps for monocular geometry, no latent tokenizer
2026-07 | Nemotron-Labs-Diffusion (2607.05722) | joins the image-diffusion and autoregressive-Transformer lineages in one language model through a joint training objective
2026-07 | SpectraReward (2607.11886) | training-free RL reward for text-to-image models: score a generation by how well the prompt is recovered from it in one image-conditioned forward pass
2026-07 | Coupled-MJP I2I (2607.13188) | couples image understanding and generation as two Markov jump processes that run at once and correct each other mid-inference
2026-07 | AlayaWorld (2607.18367) | 15B video diffusion transformer generates interactive long-horizon video chunk by chunk under a bounded visual memory, distilled to four steps per chunk
2026-07 | SensorGen (2607.04245) | controlled comparison of five generative-model families on real-world sensor time series; flow-matching is the strongest default

### Paper List

[KNOWN] [2014] Goodfellow et al. — GAN. zotero_key:GG7GSYUJ.
[KNOWN] [2015] Sohl-Dickstein et al. — Nonequilibrium Thermodynamics. zotero_key:ZPY5XD8Y.
[KNOWN] [2018] Heusel et al. — FID. zotero_key:IMBVAAFD.
[KNOWN] [2019] Karras et al. — StyleGAN. zotero_key:IFU2GS2W.
[KNOWN] [2020] Zhu et al. — CycleGAN. zotero_key:XBYZMQ6D.
[KNOWN] [2020] Ho et al. — DDPM. zotero_key:GX7WR7KA.
[KNOWN] [2021] Dhariwal et al. — Diffusion Beats GANs. zotero_key:MVWM4TZJ.
[KNOWN] [2021] Song et al. — Score SDE. zotero_key:NMJXW3GJ.
[KNOWN] [2021] Rasul et al. — TimeGrad. zotero_key:RILRU5H6.
[KNOWN] [2022] Song et al. — DDIM. zotero_key:9UA578GP.
[KNOWN] [2022] Saharia et al. — Palette. zotero_key:FZBCF7MH.
[KNOWN] [2022] Rombach et al. — Stable Diffusion. zotero_key:DULT32HM.
[KNOWN] [2022] Deng et al. — StyTr2. zotero_key:SNSMLW7Z.
[KNOWN] [2023] Li et al. — BLIP-Diffusion. zotero_key:BRHAE43A.
[KNOWN] [2023] Zhong et al. — CTG++. zotero_key:S4EZPJHE.
[KNOWN] [2023] Peebles et al. — DiT. zotero_key:YJ9TK993.
[KNOWN] [2023] Mao et al. — LED. zotero_key:G4MF7DQQ.
[KNOWN] [2024] Chen et al. — l-DAE. zotero_key:DZ2UYXUL.

[2026] 2605.26111 — Squeezing Capacity from Multimodal Large Language Models for Subject-driven Generation. [https://arxiv.org/abs/2605.26111](https://arxiv.org/abs/2605.26111). external.
[2026] 2605.26230 — GARD: Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction. [https://arxiv.org/abs/2605.26230](https://arxiv.org/abs/2605.26230). external.
[2026] 2605.02641 — Mamoda2.5: Enhancing a Unified Multimodal Model with DiT-MoE. [https://arxiv.org/abs/2605.02641](https://arxiv.org/abs/2605.02641). external.
[2026] 2605.19995 — CogOmniControl: Reasoning-Driven Controllable Video Generation via Creative Intent Cognition. [https://arxiv.org/abs/2605.19995](https://arxiv.org/abs/2605.19995). external.

[2026] 2605.26108 — Reinforcing Few-step Generators via Reward-Tilted Distribution Matching. [https://arxiv.org/abs/2605.26108](https://arxiv.org/abs/2605.26108). external.
[2026] 2606.18043 — Uncertainty Quantification for Flow-Based Vision-Language-Action Models. [https://arxiv.org/abs/2606.18043](https://arxiv.org/abs/2606.18043). external.

[2026] 2606.02753 — MetaWorld: Scaling Multi-Agent Video World Models from Single-view Video Data. [https://arxiv.org/abs/2606.02753](https://arxiv.org/abs/2606.02753). external.
[2026] 2606.09507 — Prisma-World: Camera-Controllable Multi-Agent Video World Model. [https://arxiv.org/abs/2606.09507](https://arxiv.org/abs/2606.09507). external.
[2026] 2607.02515 — PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation. [https://arxiv.org/abs/2607.02515](https://arxiv.org/abs/2607.02515). external.

[2026] 2607.05722 — Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding. [https://arxiv.org/abs/2607.05722](https://arxiv.org/abs/2607.05722). external.
[2026] 2607.11886 — Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation. [https://arxiv.org/abs/2607.11886](https://arxiv.org/abs/2607.11886). external.
[2026] 2607.13188 — Concurrent Image Understanding and Generation: Self-Correcting Coupled Markov Jump Processes. [https://arxiv.org/abs/2607.13188](https://arxiv.org/abs/2607.13188). external.

[2026] 2607.18367 — AlayaWorld: Interactive Long-Horizon World Modeling. [https://arxiv.org/abs/2607.18367](https://arxiv.org/abs/2607.18367). external.

[2026] 2607.04245 — Signal or Noise? Understanding Generative Models for Real-World Sensor Time Series. [https://arxiv.org/abs/2607.04245](https://arxiv.org/abs/2607.04245). external.

### Recent Activity

2026-07-25 | 2607.04245 added | SensorGen runs five generative-model families under one protocol across 14 settings, 4 domains, 7 datasets, and 12 signal modalities, measuring signal fidelity and downstream usefulness; flow-matching is the strongest overall, signal properties decide which design choices help (demographic covariates for longitudinal signals, time-frequency modeling for high-frequency ones), and synthetic signals improve downstream prediction, not only visual realism; Tier A

2026-07-22 | 2607.18367 added | a 15B video diffusion transformer generates interactive environments from text, image, or video by producing short latent chunks in sequence under a bounded visual context of a sink frame, compressed history, geometry-aligned spatial memory, and recent frames; it limits drift by training on corrupted histories and self-generated residuals, distills inference to four steps per chunk, and reports the best long-horizon score on iWorld-Bench; Tier B

2026-07-19 | 2607.13188 added | replaces continuous diffusion with two coupled Markov jump processes for image understanding and generation that run at the same time, letting the understanding process steer and correct the generation process during inference so one model both reads and draws while staying consistent; Tier B

2026-07-15 | 2607.11886 added | SpectraReward grades an image generator during RL fine-tuning without a trained reward model, using the average image-conditioned prompt log-likelihood as reward; tested across two diffusion models, three RL algorithms, nine backbones from 4B to 235B, and five out-of-distribution benchmarks; Tier B

2026-07-13 | 2607.05722 added | trains one network under a joint denoising-diffusion and autoregressive objective so diffusion supplies parallel lookahead while autoregression verifies, joining two lineages that rarely meet in a single model; Tier B
