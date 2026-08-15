## Mamba and State Space Models

### Timeline

2020 | HiPPO (Gu et al.) | 
2021 | SSM (LSSL) (Gu et al.) | 
2022 | S4 (Gu et al.) | 
2024 | Audio Mamba (Erol) (Erol et al.) | 
2024 | Audio Mamba (Yadav) (Yadav et al.) | 
2024 | Bi-Mamba+ (Liang et al.) | 
2024 | ClinicalMamba (Yang et al.) | 
2024 | HARMamba (Li et al.) |  [anchor]
2024 | Mamba (Gu et al.) | 
2024 | Mamba-2 (Dao et al.) | 
2024 | Mamba-UNet (Wang et al.) | 
2024 | MambaOut (Yu et al.) | 
2024 | Motion Mamba (Zhang et al.) | 
2024 | Swin-UMamba (Liu et al.) | 
2024 | U-Mamba (Ma et al.) | 
2024 | VMamba (Liu et al.) | 
2024 | Vision Mamba (Zhu et al.) | 

2026-06 | Language Models Need Sleep (2605.26099) | sleep consolidation distills attention context into SSM fast weights
2026-07 | FlashMorph (2606.30562) | selects which layers keep full attention via budget-constrained joint gate optimization for hybrid models
2026-08 | Massive Activations in Hybrid Linear Attention (2608.12149) | activation outliers spike before every full-attention layer and persist across linear-attention layers as plateaus, making quantization behavior predictable from the hybridization ratio

### Paper List

[KNOWN] [2020] Gu et al. — HiPPO. zotero_key:5YQ4IKMA.
[KNOWN] [2021] Gu et al. — SSM (LSSL). zotero_key:UTAMLB63.
[KNOWN] [2022] Gu et al. — S4. zotero_key:J7K2E7A3.
[KNOWN] [2024] Erol et al. — Audio Mamba (Erol). zotero_key:6VTXUZEG.
[KNOWN] [2024] Yadav et al. — Audio Mamba (Yadav). zotero_key:5ZZDBB7N.
[KNOWN] [2024] Liang et al. — Bi-Mamba+. zotero_key:AVTJLZIR.
[KNOWN] [2024] Yang et al. — ClinicalMamba. zotero_key:E4QKRZTC.
[KNOWN] [2024] Li et al. — HARMamba. zotero_key:HE9X47KN.
[KNOWN] [2024] Gu et al. — Mamba. zotero_key:XNI34DQX.
[KNOWN] [2024] Dao et al. — Mamba-2. zotero_key:JPKDWV2Q.
[KNOWN] [2024] Wang et al. — Mamba-UNet. zotero_key:MHMYYQUF.
[KNOWN] [2024] Yu et al. — MambaOut. zotero_key:ZS87LF7R.
[KNOWN] [2024] Zhang et al. — Motion Mamba. zotero_key:J2EZPHK4.
[KNOWN] [2024] Liu et al. — Swin-UMamba. zotero_key:ZP32YT5I.
[KNOWN] [2024] Ma et al. — U-Mamba. zotero_key:INWKDM35.
[KNOWN] [2024] Liu et al. — VMamba. zotero_key:3LTBUP6E.
[KNOWN] [2024] Zhu et al. — Vision Mamba. zotero_key:J34W7WZC.

[2605] 2605.26099 — Language Models Need Sleep. [https://arxiv.org/abs/2605.26099](https://arxiv.org/abs/2605.26099). external.

[2026] 2606.30562 — Morphing into Hybrid Attention Models (FlashMorph). [https://arxiv.org/abs/2606.30562](https://arxiv.org/abs/2606.30562). external.

[2026] 2608.12149 — Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus. [https://arxiv.org/abs/2608.12149](https://arxiv.org/abs/2608.12149). external.

### Recent Activity

2026-08-14 | 2608.12149 added | a measurement study of activation outliers in layer-interleaved hybrid linear-attention stacks, reporting that activations spike immediately before every full-attention layer and can persist across the intervening linear-attention layers as flat plateaus, and that as full attention gets denser the spikes join through the plateaus until the pattern converges to ordinary full-attention morphology; established across five linear-attention architectures, six hybridization ratios, five data domains, and open models from 1.2B to 397B total parameters, with controlled gated-delta-net pretraining up to 1.3B, and the mechanism offered is cancellation timing, so low-bit quantization behavior becomes predictable from the hybridization ratio instead of a per-model surprise; the paper is descriptive rather than a fix, and all evidence comes from language pretraining; Tier B

2026-07-03 | 2606.30562 added | FlashMorph makes hybrid-attention layer selection a budget-constrained joint optimization over per-layer gates rather than a fixed pattern or one-at-a-time scoring, then discretizes under a full-attention budget and distills; Tier B

2026-06-04 | 2605.26099 added | Sleep-like consolidation converts recent context into persistent SSM fast weights via learned local update rule, then cl; Tier A

2026-05-14 | Area page seeded | 17 papers from Zotero, 3 from graphify seed.
