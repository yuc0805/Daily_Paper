## Video Action Recognition

### What

Video action recognition classifies human actions in video clips. Methods have evolved from hand-crafted features through two-stream CNNs (spatial + optical flow) to 3D convolutions (I3D) and video transformers (TimeSformer, VideoMAE). Self-supervised pre-training with masked video modeling is the current frontier.

### Why

Action recognition is needed in surveillance, sports analytics, human-computer interaction, and activity monitoring for health. Video data is high-dimensional and temporally redundant, so efficient architectures that capture motion patterns without processing every frame are important.

### Baseline

Extract per-frame features with a 2D CNN (ResNet-50) and average-pool across the temporal dimension. The main failure mode is that temporal averaging destroys motion information: actions like 'opening a door' and 'closing a door' become indistinguishable.

### Running Example

Classify a 16-frame clip from Kinetics-400 into one of 400 action categories. The frame-averaged ResNet-50 achieves 56% top-1 accuracy. TimeSformer with divided space-time attention achieves 78% top-1 accuracy because it models temporal relationships between frames.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2014 | Two-Stream (Simonyan et al.) | 
2017 | TSN (Wang et al.) | 
2018 | I3D (Carreira et al.) | 
2020 | Video Action Survey (Zhu et al.) | 
2021 | TimeSformer (Bertasius et al.) | 
2022 | VideoMAE (Tong et al.) | 
2023 | VideoMAE V2 (Wang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Video Action Survey | 2020 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2014] Simonyan et al. — Two-Stream. zotero_key:FISF2M9S.
[KNOWN] [2017] Wang et al. — TSN. zotero_key:7AJ9P5N3.
[KNOWN] [2018] Carreira et al. — I3D. zotero_key:WYQSCSRF.
[KNOWN] [2020] Zhu et al. — Video Action Survey. zotero_key:RYGRHCG3.
[KNOWN] [2021] Bertasius et al. — TimeSformer. zotero_key:2HU6MLMN.
[KNOWN] [2022] Tong et al. — VideoMAE. zotero_key:9QCZ3A32.
[KNOWN] [2023] Wang et al. — VideoMAE V2. zotero_key:JUB597ZG.

### Recent Activity

2026-05-14 | Area page seeded | 7 papers from Zotero, 1 from graphify seed.
