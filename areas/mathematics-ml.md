## Mathematical Methods for ML

### What

This area covers the mathematical tools that underlie machine learning methods: compressed sensing, sparse representation, matrix decomposition (CUR, SVD), canonical correlation analysis, and related optimization theory. These tools provide the theoretical foundations for dimensionality reduction, feature selection, and signal recovery.

### Why

Many ML algorithms rely on linear algebra and optimization theory for their correctness guarantees. Understanding compressed sensing explains why sparse models work; CUR decompositions explain why low-rank approximations preserve structure. These foundations are necessary for designing principled new methods rather than relying on empirical tuning alone.

### Baseline

Use full SVD for dimensionality reduction or feature extraction. The main failure mode is computational cost: SVD on an m-by-n matrix costs O(min(m,n)^2 * max(m,n)), which is prohibitive for large datasets.

### Running Example

Approximate a 10000x5000 gene expression matrix for downstream clustering. Full SVD takes 120 seconds. CUR decomposition with 100 selected columns and rows produces a rank-100 approximation in 3 seconds with relative error under 5%, sufficient for clustering accuracy within 2% of the full-SVD result.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2003 | L1 Minimization (Donoho et al.) | 
2004 | CCA (Hardoon et al.) | 
2004 | Compressive Sampling (Candes et al.) | 
2007 | Sparsity Incoherence (Candes et al.) | 
2009 | CUR (Mahoney et al.) | 
2009 | Median Filtering (Arias-Castro et al.) | 
2018 | CROWN (Zhang et al.) | 
2022 | Functional Data Embedding (Arias-Castro et al.) | 
2022 | Multi-modal Density (Arias-Castro et al.) | 
Unknown | Deep CCA (Unknown) | 

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| L1 Minimization | 2003 | _To be filled_ | _To be filled_ | _To be filled_ |
| CUR | 2009 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

### Paper List

[KNOWN] [2003] Donoho et al. — L1 Minimization. zotero_key:CJZYAK9U.
[KNOWN] [2004] Hardoon et al. — CCA. zotero_key:UJ3HR45N.
[KNOWN] [2004] Candes et al. — Compressive Sampling. zotero_key:6CN5PLNU.
[KNOWN] [2007] Candes et al. — Sparsity Incoherence. zotero_key:RII6PLZW.
[KNOWN] [2009] Mahoney et al. — CUR. zotero_key:7C4VSDBY.
[KNOWN] [2009] Arias-Castro et al. — Median Filtering. zotero_key:H27VWDAF.
[KNOWN] [2018] Zhang et al. — CROWN. zotero_key:WIZICQZL.
[KNOWN] [2022] Arias-Castro et al. — Functional Data Embedding. zotero_key:DZYGYY2C.
[KNOWN] [2022] Arias-Castro et al. — Multi-modal Density. zotero_key:FG2MX7RW.
[KNOWN] [?] Unknown — Deep CCA. zotero_key:GLTH6GX9.

### Recent Activity

2026-05-14 | Area page seeded | 10 papers from Zotero, 2 from graphify seed.
