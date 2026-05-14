## Mixture of Experts

### What

Mixture of Experts (MoE) models route each input to a subset of specialized sub-networks (experts), enabling larger model capacity without proportional compute cost. This area covers routing mechanisms, load balancing, and training stability for MoE layers in transformers.

### Why

Scaling dense transformers is expensive: doubling parameters doubles compute. MoE allows scaling parameters while keeping per-token compute roughly constant, which is attractive for large-scale language models. The main challenge is training instability caused by uneven expert utilization.

### Baseline

Use a dense transformer where every parameter is active for every token. The main failure mode is that increasing model capacity requires proportionally more compute at both training and inference time.

### Running Example

Train a language model with 8B total parameters on a web text corpus. The dense baseline activates all 8B parameters per token. An MoE model with 8 experts and top-2 routing has 8B total parameters but activates only 2B per token, achieving similar perplexity at 40% of the training compute.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |

### Timeline

2022 | ST-MoE (Zoph et al.) | 
2023 | MoE+Instruction (Shen et al.) | 
2024 | WaveToken (Masserano et al.) | 
2025 | MoE Explained (Unknown) | 

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

[KNOWN] [2022] Zoph et al. — ST-MoE. zotero_key:WIGLUNFZ.
[KNOWN] [2023] Shen et al. — MoE+Instruction. zotero_key:UBDCML5N.
[KNOWN] [2024] Masserano et al. — WaveToken. zotero_key:MXKVRSKK.
[KNOWN] [2025] Unknown — MoE Explained. zotero_key:497XVFB6.

### Recent Activity

2026-05-14 | Area page seeded | 4 papers from Zotero, 0 from graphify seed.
