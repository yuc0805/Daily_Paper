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

### Recent Activity

2026-09-03 | 2609.02737 added | Declarative Attention is a protocol rather than an architecture: during its chain of thought the model emits declarations that partition generation into three modes, global over the full context, focus over one named region, and local over recent output only, and the inference engine parses those declarations the way it parses tool calls and skips the corresponding parts of the KV cache read; across 15 long-context tasks, with no retraining and zero-shot on off-the-shelf checkpoints, it reduces attended tokens during decoding by 52.0 percent on Gemma-4-31B and 31.1 percent on Qwen-3.6-27B at accuracy costs of 1.27 and 2.75 percentage points, and the accuracy gap narrows as model scale grows; where Attention Is All You Need (PHB9VRVM) fixed the attention span as a property of the architecture, this paper makes the span a decision taken at run time, because a fixed span is no longer affordable at million-token context, where Chain-of-Thought Prompting (HBLPTRMY) used the reasoning trace to hold intermediate answers, this paper uses it to hold control instructions the serving engine executes, which turns the trace from an output artifact into a compute-scheduling signal, and where DeepSeek-V3 (2JCKA7GI) cut the cost of reading each cache entry by compressing it, this paper leaves the entry alone and declines to read most of them; the three parents span two graphify communities and the contribution is the crossing itself, a Community 0 mechanism controlling a Community 2 cost, which is a different bridge from the existing deepseek2025_r1 to wei2023_cot link inside Community 0; the savings are measured in attended tokens rather than wall-clock latency and the two do not convert one-to-one on real serving stacks, the declarations are produced by the same model whose attention they govern so a misjudged region is skipped silently, and no per-task worst case or fallback trigger is reported; Tier A

2026-09-02 | 2609.01591 added | StudentSim fits one simulator per student from sparse per-student records through pooled training across all students followed by per-student specialization, and separates two abilities that prior work conflated, behavioral fidelity, whether the simulator reproduces the student's own responses, and guidance responsiveness, whether it updates when a tutor corrects it; on chess it reaches 0.51 fidelity and 0.91 responsiveness against 0.23 and 0.72 for prompted GPT-5.4 and 0.45 and 0.27 for the fitted behaviour model Maia2, so the two prior classes fail on opposite axes and neither is deficient in general; where Machine Theory of Mind (NEKX3K3N) learned a model of another agent from observed behaviour and stopped at prediction, this paper requires the learned model to also move correctly under instruction and scores that separately, and where CounselBench (GST6E6A6) treats per-person records as an evaluation endpoint, StudentSim spends the fitted per-person model as a reinforcement-learning reward, which turns the simulator from a benchmark into training infrastructure and produces a tutor human experts rate above a no-reinforcement baseline and above one trained against a GPT-5.4 reward; the companion protocol covers 60 students across chess, second-language English writing and mathematics, and the evaluation design rather than the fitting method is the transferable part; Tier B

2026-08-14 | 2608.08888 added | the full-bandwidth transformer fuses the previous top-layer hidden state with the sampled token embedding through a gated linear unit and feeds the result back as the next input, so computation the model did not verbalize re-enters the stack with a renewed depth budget while the core architecture, the KV cache, and the language-modeling objective stay unchanged; a scheduled multi-pass objective switches latent feedback on late in pretraining so parallel teacher forcing survives, and 1B-parameter models trained to 400B tokens match or approach standard transformers trained on roughly 1.5 times more tokens, with negligible per-token decoding overhead and shorter reasoning traces at equal or better accuracy; there is no scaling-law study, so the 1.5 times figure is a single-scale observation; Tier A

2026-07-25 | 2607.10848 added | shows the single-sample importance ratio in a PPO-style direction test can disagree in sign with the change of the divergence the proximity test uses, and replaces it with a predictive divergence mask that asks whether the next gradient step will raise or lower that divergence, derived in closed form for softmax policies with two top-K estimators for the truncated vocabulary; improves RL training across model scales and precision settings; Tier B

2026-07-20 | 2607.15161 added | on-policy distillation gives token-level supervision on the student's own rollouts and avoids a reward model; OPD^2 changes the target to the delta between the reasoning-tuned teacher and its base model before instruction tuning, isolating what tuning added, and beats standard on-policy distillation across mathematics, science, and code-reasoning benchmarks over several Qwen3 sizes with transfer to Gemma 4; Tier B
