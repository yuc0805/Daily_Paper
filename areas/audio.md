## Audio Representation Learning

### What

Audio representation learning covers models that extract useful features from raw audio or spectrograms for tasks like sound classification, speech recognition, and health acoustics. Methods range from CNN-based spectrogram classifiers (PSLA) to transformer encoders (AST) and self-supervised approaches (TRILL, HeAR, CLAP).

### Why

Audio signals carry information about health (cough detection, respiratory disease), environment (urban sound classification), and communication (speech). Pre-trained audio representations reduce the need for labeled audio data, which is expensive to annotate at scale.

### Baseline

Extract mel-spectrogram features and train a CNN classifier from scratch. The main failure mode is that spectrogram-level CNNs miss temporal structure beyond their receptive field and require large labeled datasets to avoid overfitting.

### Running Example

Classify environmental sounds into 50 categories on the ESC-50 dataset. The mel-spectrogram CNN baseline achieves 72% accuracy. AST (Audio Spectrogram Transformer) pre-trained on AudioSet achieves 88% accuracy.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2020 | TRILL (Shor et al.) | 
2021 | AST (Gong et al.) | 
2021 | FRILL (Peplinski et al.) | 
2021 | PSLA (Gong et al.) | 
2022 | Audio MAE (Huang et al.) | 
2022 | CLAP (Elizalde et al.) | 
2023 | LTU (Gong et al.) | 
2024 | HeAR (Baur et al.) | 
2024 | OPERA (Zhang et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| HeAR | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2020] Shor et al. — TRILL. zotero_key:WJQ5APZU.
[KNOWN] [2021] Gong et al. — AST. zotero_key:7J6K6W8I.
[KNOWN] [2021] Peplinski et al. — FRILL. zotero_key:4A2A73JF.
[KNOWN] [2021] Gong et al. — PSLA. zotero_key:MB3HH9SR.
[KNOWN] [2022] Huang et al. — Audio MAE. zotero_key:65EDEWIJ.
[KNOWN] [2022] Elizalde et al. — CLAP. zotero_key:KNGZCC5J.
[KNOWN] [2023] Gong et al. — LTU. zotero_key:ESEEEH85.
[KNOWN] [2024] Baur et al. — HeAR. zotero_key:3LA8GNCU.
[KNOWN] [2024] Zhang et al. — OPERA. zotero_key:T2T4DUKA.

### Recent Activity

2026-05-14 | Area page seeded | 9 papers from Zotero, 1 from graphify seed.
