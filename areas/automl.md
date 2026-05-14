## Automated Machine Learning

### What

AutoML automates the process of selecting model architectures, hyperparameters, and feature engineering pipelines. It includes neural architecture search (NAS), hyperparameter optimization (Bayesian optimization, random search), and automated feature extraction.

### Why

Manual model selection and tuning is time-consuming and requires expert knowledge. AutoML makes ML accessible to non-experts and can discover configurations that human practitioners would not try. The main limitation is computational cost: searching over architecture spaces requires training many candidate models.

### Baseline

Manually select a standard architecture (e.g., ResNet for images, LSTM for sequences) and tune hyperparameters by grid search over a small set of values. The main failure mode is that the search space is too small to find good configurations, and the process does not scale to new datasets without human intervention.

### Running Example

Find the best image classifier for a custom 10-class medical imaging dataset with 5000 images. Manual selection picks ResNet-50 with default hyperparameters, achieving 82% accuracy. An AutoML system searching over architectures and augmentation strategies finds an EfficientNet-B2 with specific augmentation that achieves 88% accuracy.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2018 | AutoPhrase (Shang et al.) | 
2021 | AutoML Survey (He et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2018] Shang et al. — AutoPhrase. zotero_key:PWXG35AH.
[KNOWN] [2021] He et al. — AutoML Survey. zotero_key:W5D5V7NQ.

### Recent Activity

2026-05-14 | Area page seeded | 2 papers from Zotero, 0 from graphify seed.
