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
2026-07 | Associative Recurrent Memory (2607.11614) | extends context by placing associative recurrent memory in a few chosen layers, trained with synthetic long-context data and a curriculum
2026-07 | On-Policy Distillation Pathologies (2607.13399) | frames on-policy distillation as an exploration catalyst and adds advantage clipping plus log-scale compression to stop length hacking
2026-07 | On-Policy Delta Distillation (2607.15161) | distills the reasoning-tuned-teacher minus base-model delta rather than the full teacher distribution, isolating what reasoning tuning added
2026-07 | Predictive Divergence Masks (2607.10848) | replaces PPO's ratio-based direction test with a predicted change in the trust-region divergence, in closed form for softmax policies
2026-08 | Full-bandwidth transformer (2608.08888) | feeds the previous top-layer hidden state back alongside the sampled token embedding through a gated linear unit, widening the cross-step channel

2026-09 | StudentSim (2609.01591) | per-student simulators from sparse records; behavioral fidelity and guidance responsiveness scored separately, then used as a tutor reward
2026-09 | Declarative Attention (2609.02737) | the model declares in its chain of thought which context region to attend to, and the serving engine skips the rest of the KV cache read

2026-09 | CRISP (2609.01925) | structural attention-mass routing plus a sink-aware mass-cliff threshold for sparse prefill; 5.30x attention speedup at 512k tokens

2026-09 | LatentPress (2609.01507) | writes long histories into continuous memory tokens a frozen decoder reads through its input-embedding port at 4x to 16x compression
2026-09 | Random Attention (2609.03430) | random KV eviction that keeps the prompt matches the best scoring evictor at 32 to 43 percent higher throughput

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
[2026] 2607.11614 — Extending LLM Context via Associative Recurrent Memory. [https://arxiv.org/abs/2607.11614](https://arxiv.org/abs/2607.11614). external.
[2026] 2607.13399 — Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations. [https://arxiv.org/abs/2607.13399](https://arxiv.org/abs/2607.13399). external.
[2026] 2607.15161 — On-Policy Delta Distillation. [https://arxiv.org/abs/2607.15161](https://arxiv.org/abs/2607.15161). external.

[2026] 2607.10848 — Predictive Divergence Masks for LLM RL. [https://arxiv.org/abs/2607.10848](https://arxiv.org/abs/2607.10848). external.

[2026] 2608.08888 — Full-bandwidth transformer. [https://arxiv.org/abs/2608.08888](https://arxiv.org/abs/2608.08888). external.

[2026] 2609.01591 — StudentSim: Training LLM-based Student Simulators. [https://arxiv.org/abs/2609.01591](https://arxiv.org/abs/2609.01591). external.

[2026] 2609.02737 — Declarative Attention: Language Models Can Control Their Own Attention. [https://arxiv.org/abs/2609.02737](https://arxiv.org/abs/2609.02737). external.

[2026] 2609.01925 — CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing. [https://arxiv.org/abs/2609.01925](https://arxiv.org/abs/2609.01925). external.

[2026] 2609.01507 — LatentPress: Context Compression Beyond Text and Vision. [https://arxiv.org/abs/2609.01507](https://arxiv.org/abs/2609.01507). external.
[2026] 2609.03430 — Random Attention: Rethinking KV Cache Eviction for Efficient Reasoning. [https://arxiv.org/abs/2609.03430](https://arxiv.org/abs/2609.03430). external.

### Recent Activity

2026-09-05 | 2609.01507 added | LatentPress writes conversational histories and long documents into continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference, training only a reader-matched writer adapter of 4.2M to 26.2M parameters, roughly 0.1 percent of the decoder, at compression ratios of 4x to 16x; on LongMemEval it reaches 0.504 accuracy at 7.70x compression against 0.490 for uncompressed evidence, 0.184 for text summaries and 0.426 down to 0.312 for OCR-based compression, with writing at 43 ms per conversation and reading 5x to 9x faster than raw context or cached OCR; where Time-LLM (MKICLA63) showed that the input-embedding port of a frozen decoder will accept vectors produced by a small reprogramming adapter, this paper measures how much that port can carry and does so against a strong same-modality baseline, so the capacity of the interface becomes a number rather than an existence claim, where ChatTS (VSCNJG5J) aligned numeric series with language without reporting compression ratio or read and write latency, LatentPress reports both, and where DeepSeek-V2 (743XA29Y) compresses the per-token state inside attention and keeps the token count, LatentPress shrinks the token count itself at the input and leaves the decoder untouched, so the two are composable rather than competing; the transferable claim is about the interface rather than the task, and every Community 4 method in the library converts one window of signal into something the model reads while none writes a long continuous record into a fixed budget of memory tokens, so this is a candidate new bridge between Community 4 and the LLM context-efficiency line, and soft-token context compression is not yet closed off for time series or bio-sensing; Tier A

2026-09-05 | 2609.03430 added | Random Attention removes the scoring step from KV cache eviction entirely: it keeps the prompt and evicts uniformly at random within each attention head, and across four models and six reasoning tasks it matches the strongest prior evictor while serving 32 to 43 percent higher throughput in vLLM; two controlled experiments supply the explanation, that the prompt is the fragile part of the cache and most of the measured gap between scorers is whether their signal happened to keep it, and that the reasoning trace protects itself with redundancy both in the text, where the model restates what it still needs, and across heads, where each head keeps its own copy; where Attention Is All You Need (vaswani2017_transformer) made the linear growth of the cache a direct consequence of the attention formulation, this paper accepts the formulation and attacks the count of surviving entries instead, where DeepSeek-V2 (743XA29Y) reduced the per-token cost of the cache with a learned low-rank latent, Random Attention reduces the token count with no learning and no scoring at all, and where DeepSeek-R1 (deepseek2025_r1) produced the long RL-trained traces that make the cache a bottleneck, this paper shows those same traces carry the redundancy that makes the choice of survivor stop mattering, which is why the result would not have been available before long RL-trained reasoning existed; the contribution is diagnostic rather than architectural, reassigning credit for the reported gains of a whole family of scoring methods to a single confound, prompt retention, and it is the cheapest available template for the same test on sensor context, since a 1 Hz physiological record over weeks is more redundant than a reasoning trace and the learned patch-selection modules in current time-series and LLM pipelines are exactly the component this experiment design would test; Tier B

2026-09-04 | 2609.01925 added | CRISP attacks the quadratic prefill cost of long-context attention with two changes to dynamic sparse routing, replacing Jensen-Shannon divergence routing with C_struct, a structural measure of attention mass at Vertical-Slash compatible positions that reproduces the same routing decisions while removing the pooled matrix multiply and the KL computation, and formalising a post-softmax mass cliff, showing that cumulative coverage thresholds accumulate O(n) background noise at long context and setting a sink-aware threshold at the noise floor instead; on InfiniteBench, RULER and LongBench across two model families it is the strongest sparse method, matches or exceeds dense attention on retrieval-heavy tasks, recovers up to 28.0 percentage points on retrieval over baselines, and reaches a 5.30x attention speedup at 512k tokens; where Attention Is All You Need (PHB9VRVM) made every query read every key, CRISP keeps the architecture and decides per input which heads can afford a sparse pattern, so the saving is a serving decision rather than a training one, where Declarative Attention (2609.02737) put the selection decision inside the model's own output stream and applied it at decode time, CRISP keeps the decision outside the model, reads it off the proxy attention map and applies it at prefill, the phase Declarative Attention does not touch, so the two act on complementary halves of the same cost and are in principle stackable, and where DeepSeek-V3 (2JCKA7GI) shrank the cost of reading each cache entry, CRISP declines to read most of them; the contribution over earlier dynamic routers is diagnostic, since a cumulative coverage threshold silently admits O(n) background mass, which explains long-context retrieval loss for reasons that have nothing to do with the routing rule, and the mass-cliff analysis is signal-processing reasoning applied to attention maps, which matters where minute-resolution multi-day physiological streams put sequence length rather than model capacity on the critical path; Tier B

2026-09-03 | 2609.02737 added | Declarative Attention is a protocol rather than an architecture: during its chain of thought the model emits declarations that partition generation into three modes, global over the full context, focus over one named region, and local over recent output only, and the inference engine parses those declarations the way it parses tool calls and skips the corresponding parts of the KV cache read; across 15 long-context tasks, with no retraining and zero-shot on off-the-shelf checkpoints, it reduces attended tokens during decoding by 52.0 percent on Gemma-4-31B and 31.1 percent on Qwen-3.6-27B at accuracy costs of 1.27 and 2.75 percentage points, and the accuracy gap narrows as model scale grows; where Attention Is All You Need (PHB9VRVM) fixed the attention span as a property of the architecture, this paper makes the span a decision taken at run time, because a fixed span is no longer affordable at million-token context, where Chain-of-Thought Prompting (HBLPTRMY) used the reasoning trace to hold intermediate answers, this paper uses it to hold control instructions the serving engine executes, which turns the trace from an output artifact into a compute-scheduling signal, and where DeepSeek-V3 (2JCKA7GI) cut the cost of reading each cache entry by compressing it, this paper leaves the entry alone and declines to read most of them; the three parents span two graphify communities and the contribution is the crossing itself, a Community 0 mechanism controlling a Community 2 cost, which is a different bridge from the existing deepseek2025_r1 to wei2023_cot link inside Community 0; the savings are measured in attended tokens rather than wall-clock latency and the two do not convert one-to-one on real serving stacks, the declarations are produced by the same model whose attention they govern so a misjudged region is skipped silently, and no per-task worst case or fallback trigger is reported; Tier A

2026-09-02 | 2609.01591 added | StudentSim fits one simulator per student from sparse per-student records through pooled training across all students followed by per-student specialization, and separates two abilities that prior work conflated, behavioral fidelity, whether the simulator reproduces the student's own responses, and guidance responsiveness, whether it updates when a tutor corrects it; on chess it reaches 0.51 fidelity and 0.91 responsiveness against 0.23 and 0.72 for prompted GPT-5.4 and 0.45 and 0.27 for the fitted behaviour model Maia2, so the two prior classes fail on opposite axes and neither is deficient in general; where Machine Theory of Mind (NEKX3K3N) learned a model of another agent from observed behaviour and stopped at prediction, this paper requires the learned model to also move correctly under instruction and scores that separately, and where CounselBench (GST6E6A6) treats per-person records as an evaluation endpoint, StudentSim spends the fitted per-person model as a reinforcement-learning reward, which turns the simulator from a benchmark into training infrastructure and produces a tutor human experts rate above a no-reinforcement baseline and above one trained against a GPT-5.4 reward; the companion protocol covers 60 students across chess, second-language English writing and mathematics, and the evaluation design rather than the fitting method is the transferable part; Tier B
