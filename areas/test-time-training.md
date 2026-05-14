## Test-Time Training

### What

Test-time training (TTT) adapts model parameters at inference time using a self-supervised objective on the test input itself. This allows the model to adjust to distribution shifts between training and test data without requiring labeled test data. Recent work integrates TTT as a layer within sequence models.

### Why

Models trained on one distribution often degrade on shifted test distributions (different hospitals, different sensors, different domains). TTT provides a way to adapt without labels at test time, which is useful when the shift is unpredictable and collecting new training data is infeasible.

### Baseline

Apply the trained model directly to the test data without any adaptation. The main failure mode is degraded accuracy when test data differs from training data in style, resolution, or domain characteristics.

### Running Example

Segment medical images from Hospital B using a U-Net trained on Hospital A data. The unadapted model achieves Dice score of 0.68 due to differences in imaging protocols. TTT-Unet, which fine-tunes on each test image using a self-supervised reconstruction objective, achieves Dice score of 0.79.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2023 | UNI Pathology (Chen et al.) | 
2024 | TTT Layers (Sun et al.) | 
2024 | TTT for Abstract Reasoning (Akyurek et al.) | 
2024 | TTT-Unet (Zhou et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| UNI Pathology | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2023] Chen et al. — UNI Pathology. zotero_key:6T29JLTN.
[KNOWN] [2024] Sun et al. — TTT Layers. zotero_key:JEGI4IS7.
[KNOWN] [2024] Akyurek et al. — TTT for Abstract Reasoning. zotero_key:W7RPRTCH.
[KNOWN] [2024] Zhou et al. — TTT-Unet. zotero_key:K9AZKZB2.

### Recent Activity

2026-05-14 | Area page seeded | 4 papers from Zotero, 1 from graphify seed.
