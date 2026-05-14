## Mamba and State Space Models

### What

State space models (SSMs) are sequence models derived from continuous-time linear systems, discretized for use on sequential data. Mamba is a selective SSM that introduces input-dependent gating to the state transition, achieving linear-time sequence processing. This area covers the SSM family from S4 through Mamba-2 and domain-specific adaptations (vision, audio, medical imaging, human activity recognition).

### Why

Transformers have quadratic complexity in sequence length, which limits their application to very long sequences (genomics, high-resolution images, long audio). SSMs offer linear scaling while maintaining competitive accuracy, making them attractive for resource-constrained or long-context settings.

### Baseline

Use a standard Transformer encoder with full self-attention. The main failure mode is quadratic memory and compute cost: a 16k-token sequence requires 256M attention entries, making training slow and inference memory-intensive on consumer hardware.

### Running Example

Classify a 10-second accelerometer signal (sampled at 50Hz, 500 time steps, 3 axes) from the UCI HAR dataset into one of six activities. The Transformer baseline processes 500 tokens with full attention (250k entries), taking 45ms per sample. HARMamba processes the same sequence in 12ms with comparable accuracy.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| HARMamba | _To be added as papers accumulate._ | Anchor paper for this area |

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

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| HARMamba | Li 2024 | Anchor method | _To be filled_ | _To be filled_ |
| Audio Mamba (Erol) | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| Swin-UMamba | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

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

### Recent Activity

2026-05-14 | Area page seeded | 17 papers from Zotero, 3 from graphify seed.
