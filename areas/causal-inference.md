## Causal Inference

### What

Causal inference provides formal frameworks for reasoning about cause-and-effect relationships from observational or experimental data. Core tools include structural causal models, do-calculus, and potential outcomes. In ML, causal reasoning informs fairness, robustness, and transfer learning.

### Why

Correlation-based ML models can learn spurious associations that break under distribution shift or intervention. Causal models explicitly represent the data-generating process, enabling predictions about the effect of actions rather than mere statistical associations.

### Baseline

Estimate the effect of a treatment by comparing mean outcomes between treated and untreated groups. The main failure mode is confounding: if treatment assignment correlates with a variable that also affects the outcome, the naive estimate is biased.

### Running Example

Estimate the effect of a new drug on blood pressure from observational hospital records, where sicker patients are more likely to receive the drug. The naive comparison shows the drug increases blood pressure (confounding by severity). A propensity-score adjusted estimate reveals the drug decreases blood pressure by 5 mmHg.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2010 | Causal Inference Intro (Pearl et al.) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| Causal Inference Intro | 2010 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2010] Pearl et al. — Causal Inference Intro. zotero_key:BB78CC56.

### Recent Activity

2026-05-14 | Area page seeded | 1 papers from Zotero, 1 from graphify seed.
