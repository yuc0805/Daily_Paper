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
2026-07 | HiLS-Attention (2607.02980) | learned differentiable chunk retriever gives sub-quadratic attention that matches full attention and extrapolates past training length
2026-07 | DSpark (2607.05147) | speculative decoding with a sequential head over a parallel drafter plus load-aware verification scheduling; 60 to 85 percent faster per-user generation
2026-07 | Nemotron-Labs-Diffusion (2607.05722) | one network trained under a joint autoregressive-plus-diffusion objective switches decoding modes; 8B decodes 6x more tokens per forward pass than Qwen3-8B
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

[2026] 2607.02980 — HiLS-Attention: Hierarchical Sparse Attention Done Right. [https://arxiv.org/abs/2607.02980](https://arxiv.org/abs/2607.02980). external.

[2026] 2607.05147 — DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation. [https://arxiv.org/abs/2607.05147](https://arxiv.org/abs/2607.05147). external.
[2026] 2607.05722 — Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding. [https://arxiv.org/abs/2607.05722](https://arxiv.org/abs/2607.05722). external.

### Recent Activity

2026-07-13 | 2607.05147 added | a small sequential head lets drafted blocks keep within-block dependencies and verification length is scheduled per request from prefix-survival estimates, giving 60 to 85 percent faster per-user generation at matched throughput inside DeepSeek-V4 serving; Tier B
2026-07-13 | 2607.05722 added | a single network trained under a joint autoregressive-plus-diffusion objective switches decoding modes at deployment, with diffusion drafting and autoregression verifying in self-speculation; the 8B model decodes 6x more tokens per forward pass than Qwen3-8B at comparable accuracy; Tier B
2026-07-09 | 2607.02980 added | HiLS learns chunk selection end-to-end under the language-modeling loss, with each query attending independently to retrieved chunks fused by trained retrieval scores; it reaches sub-quadratic cost while matching or beating full attention and extrapolating past training length; Tier A
2026-07-02 | 2607.01104 added | CausalMix treats the domain mixture as a treatment and the training result as an outcome, fits a causal model on 512 runs of a 0.5B model to estimate the effect of an unseen mixture, then extrapolates the optimal mixture to an 800K pool and a 7B model; Tier A
2026-06-08 | 2606.05988 added | compressing CoT traces before distillation gives 2-7.6x training speedup at up to 96% raw accuracy; Tier B
