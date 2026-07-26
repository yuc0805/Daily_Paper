## Self-Supervised Learning Frameworks

### Timeline

2017 | Attention Is All You Need (Vaswani et al.) | 
2020 | GPT-3 (Brown et al.) | 
2021 | GNN Intro (Sanchez-Lengeling et al.) | 
2021 | LoRA (Hu et al.) | 
2022 | Foundation Models Survey (Bommasani et al.) | 
2023 | LVM-Med (Nguyen et al.) | 
2024 | l-DAE (Chen et al.) | 

2026-05 | xMAE (2605.00973) | physiology-aware masked cross-modal reconstruction across ECG and PPG
2026-05 | BenchHAR (2605.08296) | SSL benchmark for generalizable sensor-based activity recognition
2026-06 | CLAMP (2506.13717) | contrastive SSL recast as manifold packing via jammed-particle physics loss
2026-06 | Predict and Reconstruct (2606.05173) | joint JEPA latent prediction + MLM reconstruction on shared encoder
2026-06 | Hypnos (2606.09605) | autoregressive next-token prediction over RVQ tokens of eight physiological modalities
2026-06 | Neuro-JEPA (2606.14957) | joint-embedding predictive pretraining on multimodal neuroimaging with a sparsity constraint on the latent
2026-07 | VCSD (2607.21556) | on-policy self-distillation for vision-language models that builds the learning signal from original-image versus content-erased contrast through an EMA teacher, with no external teacher

### Paper List

[KNOWN] [2017] Vaswani et al. — Attention Is All You Need. zotero_key:PHB9VRVM.
[KNOWN] [2020] Brown et al. — GPT-3. zotero_key:ZT8Y3ABF.
[KNOWN] [2021] Sanchez-Lengeling et al. — GNN Intro. zotero_key:VHTGRMY5.
[KNOWN] [2021] Hu et al. — LoRA. zotero_key:PZATM3SC.
[KNOWN] [2022] Bommasani et al. — Foundation Models Survey. zotero_key:TFPTRFGU.
[KNOWN] [2023] Nguyen et al. — LVM-Med. zotero_key:5GFYJJVV.
[KNOWN] [2024] Chen et al. — l-DAE. zotero_key:DZ2UYXUL.

[2026] 2605.00973 — Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning (xMAE). [https://arxiv.org/abs/2605.00973](https://arxiv.org/abs/2605.00973). external.
[2026] 2605.08296 — BenchHAR: Benchmarking Self-Supervised Learning for Generalizable Sensor-based Activity Recognition. [https://arxiv.org/abs/2605.08296](https://arxiv.org/abs/2605.08296). external.
[2026] 2506.13717 — CLAMP: Contrastive Self-Supervised Learning As Neural Manifold Packing. [https://arxiv.org/abs/2506.13717](https://arxiv.org/abs/2506.13717). external.
[2026] 2606.05173 — Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning. [https://arxiv.org/abs/2606.05173](https://arxiv.org/abs/2606.05173). external.
[2026] 2606.09605 — Next-Token Prediction Learns Generalisable Representations of Sleep Physiology (Hypnos). [https://arxiv.org/abs/2606.09605](https://arxiv.org/abs/2606.09605). external.
[2026] 2606.14957 — Neuro-JEPA: Learning a Sparse Latent Predictive Foundation Model for Multimodal Neuroimaging. [https://arxiv.org/abs/2606.14957](https://arxiv.org/abs/2606.14957). external.

[2026] 2607.21556 — Visual Contrastive Self-Distillation. [https://arxiv.org/abs/2607.21556](https://arxiv.org/abs/2607.21556). external.

### Recent Activity

2026-07-25 | 2607.21556 added | VCSD removes the external teacher from self-distillation for vision-language models: at each student-generated prefix an EMA teacher produces two next-token distributions, one conditioned on the original image and one on a content-erased control, and the token-wise log-probability difference marks the tokens the image content raises, sharpening the teacher distribution that is distilled into the student; on ViRL39K it improves seven-benchmark aggregates on Qwen3-VL by about 5 points at 2B, 2 at 4B, and 4 at 8B, with no external teacher, answer hints, or extra inference cost; Tier B

2026-06-27 | 2606.14957 added | Neuro-JEPA predicts in a learned latent space instead of reconstructing raw neuroimaging and enforces latent sparsity, producing transferable representations across imaging modalities; Tier B

2026-06-13 | 2606.09605 added | autoregressive next-token prediction on RVQ tokens of physiology transfers across modalities and beats a dedicated ECG model at atrial fibrillation detection; Tier A

2026-06-07 | 2606.05173 added | hybrid JEPA+MLM objective yields more uniform embeddings; transfer to sensor data is the open opportunity; Tier B

2026-06-03 | 2506.13717 added | contrastive SSL recast as manifold packing; physics-inspired loss with interpretable geometry; Tier B
