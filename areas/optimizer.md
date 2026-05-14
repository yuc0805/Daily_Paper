## Optimization Methods

### What

This area covers the optimization algorithms used to train neural networks, from SGD through adaptive methods (Adam, AdaGrad) to more recent variants. It includes convergence theory, learning rate schedules, and the practical considerations that determine which optimizer to use.

### Why

The choice of optimizer affects training speed, final accuracy, and generalization. Adam is the de facto default, but it can converge to sharp minima that generalize poorly. Understanding optimizer behavior is necessary for diagnosing training failures and tuning large-scale training runs.

### Baseline

Use SGD with a fixed learning rate and momentum. The main failure mode is that SGD requires careful learning rate tuning per problem and converges slowly on ill-conditioned loss surfaces.

### Running Example

Train a ResNet-50 on ImageNet for 90 epochs. SGD with fixed learning rate 0.1 achieves 75.2% top-1 accuracy but diverges if the learning rate is set above 0.3. Adam with default settings achieves 74.8% accuracy with less sensitivity to the initial learning rate, but uses 2x memory for moment estimates.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2017 | Adam (Kingma et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Adam | 2017 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2017] Kingma et al. — Adam. zotero_key:JRH3CE5M.

### Recent Activity

2026-05-14 | Area page seeded | 1 papers from Zotero, 1 from graphify seed.
