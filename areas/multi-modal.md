## Multi-Modal Learning

### What

Multi-modal learning builds models that process and align information from multiple input types: images, text, audio, video, or sensor data. Core techniques include contrastive alignment (CLIP, SigLIP), cross-modal attention (Flamingo, BLIP-2), and joint generative models (DALL-E 2).

### Why

Real-world tasks often involve multiple modalities simultaneously: a medical diagnosis uses both imaging and clinical notes; a robot uses vision and language instructions. Single-modality models miss cross-modal correlations, and naive concatenation of modality-specific features does not learn alignment.

### Baseline

Encode each modality independently with a pre-trained encoder, concatenate the feature vectors, and train a linear classifier on top. The main failure mode is that this approach cannot capture fine-grained correspondences between modalities (e.g., which image region a word refers to).

### Running Example

Given an image of a dog catching a frisbee and the caption 'a brown dog leaps to catch a red frisbee,' retrieve the correct image from a pool of 1000 candidates. The concatenation baseline achieves Recall@1 of 35%. SigLIP with contrastive pre-training achieves Recall@1 of 82%.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| SigLIP | _To be added as papers accumulate._ | Anchor paper for this area |

### Timeline

2021 | ViT (Dosovitskiy et al.) | 
2022 | DALL-E 2 (Ramesh et al.) | 
2022 | Flamingo (Alayrac et al.) | 
2023 | BLIP-2 (Li et al.) | 
2023 | FLIP (Li et al.) | 
2025 | Machine Mental Imagery (Yang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| SigLIP | Zhai 2023 | Anchor method | _To be filled_ | _To be filled_ |
| DALL-E 2 | 2022 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2021] Dosovitskiy et al. — ViT. zotero_key:B7F2Q998.
[KNOWN] [2022] Ramesh et al. — DALL-E 2. zotero_key:DUERBZGM.
[KNOWN] [2022] Alayrac et al. — Flamingo. zotero_key:SC8KWYVK.
[KNOWN] [2023] Li et al. — BLIP-2. zotero_key:4N5WXKPI.
[KNOWN] [2023] Li et al. — FLIP. zotero_key:64H6TK5Y.
[KNOWN] [2025] Yang et al. — Machine Mental Imagery. zotero_key:NSI6PVD7.

### Recent Activity

2026-05-14 | Area page seeded | 6 papers from Zotero, 1 from graphify seed.
