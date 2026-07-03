## Large Language Models

### Timeline

2024 | DeepSeek-V2 (DeepSeek-AI et al.) | 
2024 | DeepSeek-V3 (DeepSeek-AI et al.) | 
2025 | DeepSeek-R1 (DeepSeek-AI et al.) | 
2025 | SPRINT (Biju et al.) | 

2026-05 | ScaleLogic (2605.06638) | RL training compute scales as a power law with reasoning depth; expressiveness sets the exponent
2026-05 | RL Unlocks Parametric Knowledge (2605.07153) | RL redistributes probability mass to surface latent facts
2026-06 | Efficiency Frontier (2605.23071) | frames LLM context management as one cost-performance optimization problem
2026-06 | Language Models Need Sleep (2605.26099) | sleep consolidation distills attention context into SSM fast weights
2026-06 | KVarN (2606.03458) | calibration-free KV-cache quantizer with Hadamard rotation and dual-scaling variance normalization
2026-06 | SparDA (2606.04511) | fourth Forecast projection enables lookahead KV-cache prefetch for 1.7x decode speedup
2026-06 | Compress-Distill (2606.05988) | compressed reasoning traces yield 2-7.6x training speedup at up to 96% raw accuracy
2026-07 | CausalMix (2607.01104) | selects the training-data domain mixture by treating mixture choice as causal treatment-effect estimation
### Paper List

[KNOWN] [2024] DeepSeek-AI et al. — DeepSeek-V2. zotero_key:743XA29Y.
[KNOWN] [2024] DeepSeek-AI et al. — DeepSeek-V3. zotero_key:2JCKA7GI.
[KNOWN] [2025] DeepSeek-AI et al. — DeepSeek-R1. zotero_key:Z5IWHZAE.
[KNOWN] [2025] Biju et al. — SPRINT. zotero_key:BZKDNHD6.

[2026] 2605.06638 — Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key. [https://arxiv.org/abs/2605.06638](https://arxiv.org/abs/2605.06638). external.
[2026] 2605.07153 — Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs. [https://arxiv.org/abs/2605.07153](https://arxiv.org/abs/2605.07153). external.
[2026] 2605.23071 — The Efficiency Frontier: A Unified Framework for Cost-Performance Optimization in LLM Context Management. [https://arxiv.org/abs/2605.23071](https://arxiv.org/abs/2605.23071). external.
[2605] 2605.26099 — Language Models Need Sleep. [https://arxiv.org/abs/2605.26099](https://arxiv.org/abs/2605.26099). external.
[2026] 2606.03458 — KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks. [https://arxiv.org/abs/2606.03458](https://arxiv.org/abs/2606.03458). external.

[2026] 2606.04511 — SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference. [https://arxiv.org/abs/2606.04511](https://arxiv.org/abs/2606.04511). external.

[2026] 2606.05988 — Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation. [https://arxiv.org/abs/2606.05988](https://arxiv.org/abs/2606.05988). external.
[2026] 2607.01104 — CausalMix: Data Mixture as Causal Inference for Language Model Training. [https://arxiv.org/abs/2607.01104](https://arxiv.org/abs/2607.01104). external.

### Recent Activity

2026-07-02 | 2607.01104 added | CausalMix treats the domain mixture as a treatment and the training result as an outcome, fits a causal model on 512 runs of a 0.5B model to estimate the effect of an unseen mixture, then extrapolates the optimal mixture to an 800K pool and a 7B model; Tier A
2026-06-08 | 2606.05988 added | compressing CoT traces before distillation gives 2-7.6x training speedup at up to 96% raw accuracy; Tier B
2026-06-08 | 2606.04511 added | fourth Forecast projection for lookahead KV-cache prefetch; 1.7x decode speedup; Tier A
2026-06-07 | 2606.03458 added | calibration-free 2-bit KV-cache quantization with FP16-level accuracy on reasoning benchmarks; Tier B
2026-06-04 | 2605.26099 added | Sleep-like consolidation converts recent context into persistent SSM fast weights via learned local update rule, then cl; Tier A
