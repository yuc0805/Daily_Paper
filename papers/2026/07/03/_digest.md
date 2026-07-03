# AI Digest — 2026-07-03

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (1)

### Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimodal Reasoning (MRPO)
arXiv:2606.31825 — https://arxiv.org/abs/2606.31825

**Problem.** Multimodal models that answer questions about clinical images are usually post-trained on the final answer only. That signal is sparse: it says the answer was wrong but not which step caused it. The authors show that on medical visual question answering, most wrong answers come from an error early in the reasoning chain that then propagates through the rest of the steps.

**Method.** MRPO (Medical Reasoning-aware Policy Optimization) is a reinforcement learning method built on the GRPO objective. When the final answer is wrong, it does not penalize all tokens equally. It assigns exponentially larger penalties to tokens in the earlier invalid reasoning steps, so training pressure lands on the root of the cascade. Correct paths are left alone.

**Result.** Across three multimodal backbones, MRPO beats standard GRPO and a recent RL baseline. On Qwen3-VL-8B it surpasses the much larger HuatuoGPT-Vision-34B by 2.79 points. Early-stage reasoning failures fall from 64.0% to 13.0%. Code and models are released.

**Limitations.** Gains are shown on medical VQA benchmarks; report generation and other open-ended clinical tasks are not covered. The exponential penalty schedule is a design choice whose sensitivity is not fully mapped. Step validity depends on how reasoning steps are segmented.

**Why it matters to Leo.** This is a clean example of moving reward shaping from the outcome to the process inside a medical multimodal model, which sits in your primary llm-health focus. The mechanism is not tied to images; any chain where an early wrong decision poisons the rest can use it, including time-series reasoning agents.

**How this builds on what you know:** The strongest parents in your library are DeepSeek-R1 (Z5IWHZAE, reasoning/agents community), Latent-GRPO (U4ZPM5DN), and Med-VQA Hallucination (ATEFZQA4). Where DeepSeek-R1 trains reasoning with outcome-only RL rewards, this paper does step-level reward shaping, because outcome-only credit is too sparse to fix clinical reasoning chains. Where standard GRPO (the family Latent-GRPO belongs to) treats every token in a failed trajectory equally, MRPO weights earlier invalid steps more, because the early mistake is what makes the rest wrong. It targets exactly the confident-but-wrong behavior that Med-VQA Hallucination measured. This paper extends DeepSeek-R1, which your library already places as the bridge between reasoning-via-RL and chain-of-thought prompting; the new work pushes that bridge further into process-level supervision.

---

## Tier B — TLDRs (3)

### Discrete Diffusion Language Models for Interactive Radiology Report Drafting
arXiv:2607.01436 — https://arxiv.org/abs/2607.01436

The authors fine-tune a diffusion language model (DiffusionGemma-26B, 3.8B active) for medical visual question answering and compare it against its autoregressive sibling Gemma-4-26B under an identical LoRA recipe, so the generative paradigm is nearly the only variable. Diffusion matches or beats autoregression on VQA-RAD, SLAKE, and VQA-Med, decodes 3.5 to 4.4 times faster, and adds any-order infill: a radiologist pins the report fragments they are sure of and the model fills the gaps using both-sided context. This is training-free and is a property autoregression lacks off the shelf.

**How this builds on what you know:** Parents in your library are DDPM (GX7WR7KA) and DDIM (9UA578GP) from the generative-CV community, plus LoRA (PZATM3SC) and Med-VQA Hallucination (ATEFZQA4). Where DDPM and DDIM denoise continuous image pixels, this paper denoises discrete text tokens and shows the approach is competitive with autoregression on a clinical task. This paper extends the diffusion line, which lived in your generative-CV community, and pushes it into llm-health — a cross-community move from generative modeling into clinical text.

### AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
arXiv:2607.02255 — https://arxiv.org/abs/2607.02255

Memory for a long-horizon agent is treated as a contract about what each decision may see. The usual contract appends the whole past transcript, which grows without bound and mixes signals so no single memory piece can be isolated. AgenticSTS uses a bounded contract instead: each decision starts from a fresh prompt built by typed retrieval, so prompt size stays fixed and each memory layer can be ablated on its own. Tested in Slay the Spire 2, adding a triggered skill layer moves wins from 3/10 to 6/10, which the authors call directional, not decisive, at that sample size (Fisher exact p about 0.37). They release 298 tagged trajectories as a reusable testbed.

**How this builds on what you know:** Parents are the Memory Mechanisms Survey (BDY3HUCV, Huang 2026), LATS (77ERE7HA), and ADaPT (J8DYBKW2), all in your agent area. Where the survey catalogs memory designs without a controlled comparison, this paper builds a harness where each layer can be ablated in isolation. Where LATS and ADaPT grow or branch context as the task runs, AgenticSTS keeps the prompt bounded by rebuilding it through typed retrieval each step.

### Morphing into Hybrid Attention Models (FlashMorph)
arXiv:2606.30562 — https://arxiv.org/abs/2606.30562

Hybrid attention models cut long-context cost by keeping full attention in some layers and linear attention in the rest; the hard part is choosing which layers keep full attention. FlashMorph frames this as budget-constrained subset selection rather than a heuristic. It builds a morphable model where each full-attention layer also has a linear-attention branch, freezes the weights, and jointly learns per-layer gates on synthetic long-context retrieval data with a regularizer that favors linear attention. The gates are discretized under a full-attention budget, then distillation and long-context fine-tuning follow. The claim is better hybrid configurations at lower selection cost with strong long-context recall.

**How this builds on what you know:** Parents are Mamba (XNI34DQX) and Attention Is All You Need (PHB9VRVM). Where Mamba replaces attention wholesale with a state space model, FlashMorph keeps a chosen subset of full-attention layers and converts only the rest, and treats the choice as a joint optimization because layer importance is interdependent under a global budget.

---

## Tier C — scan (8)

- Program-as-Weights: A Programming Paradigm for Fuzzy Functions — treats a program itself as learnable weights for approximate functions. https://arxiv.org/abs/2607.02512
- EvoPolicyGym: Evaluating Autonomous Policy Evolution in Interactive Environments — benchmark for agents that rewrite their own policies. https://arxiv.org/abs/2607.02440
- AgenticDataBench: A Comprehensive Benchmark for Data Agents — measures agents that do end-to-end data analysis. https://arxiv.org/abs/2607.01647
- Multi-Resolution Flow Matching: Training-Free Diffusion Acceleration via Staged Sampling — speeds up sampling without retraining. https://arxiv.org/abs/2607.01642
- Optimizing Visual Generative Models via Distribution-wise Rewards — reward at the distribution level rather than per sample. https://arxiv.org/abs/2607.02291
- WorldDirector: Building Controllable World Simulators with Persistent Dynamic Memory — long-lived memory for video world models. https://arxiv.org/abs/2607.02517
- Denser neq Better: Limits of On-Policy Self-Distillation for Continual Post-Training — dense self-distillation forgets more than GRPO. https://arxiv.org/abs/2607.01763
- Transferability for General Reasoning: An Automated Curriculum for Multi-Domain RLVR — auto-built curriculum for reasoning with verifiable rewards. https://arxiv.org/abs/2606.25178

---

## Tier D — Time-series / Bio-sensing Gap Watch

No time-series or bio-sensing paper qualified today, so here are two unported opportunities from the day's top method papers. Both methods sit in communities (0 and 2) that your time-series communities (4 and 5) have not pulled from yet.

**Step-wise process rewards for time-series reasoning agents.** MRPO (2606.31825) shows that penalizing the earliest invalid step, not just the final answer, cuts early-stage failures from 64% to 13% on medical VQA. TS-Agent (I2CIT4I7) in your library uses a self-critic and a quality gate but still judges the chain mostly at the outcome level. Transfer hypothesis: apply step-wise process rewards to TS-Agent's operator-call chain so that a wrong early operator choice, for example running the wrong decomposition before change-point detection, is penalized more than a late one.

**Budget-constrained hybrid attention for long wearable-sensor sequences.** FlashMorph (2606.30562) learns which layers should keep full attention versus a cheap linear operator under a compute budget. HARMamba (HE9X47KN) applies a uniform Mamba stack to activity signals. Transfer hypothesis: use FlashMorph-style gating on a wearable-signal encoder to decide, per layer, where full attention is worth its cost on long PPG or accelerometer windows, rather than choosing one operator for the whole model.

---

## News

Anthropic made Claude Sonnet 5 the default model on June 30; it is described as the most agentic Anthropic model so far, able to drive browsers and terminals while running close to Opus 4.8 at lower cost. Google's Gemini 3.5 Pro is now cleared for a general-availability launch in July after slipping from June. On June 29, Meituan open-sourced LongCat-2.0, a 1.6-trillion-parameter coding model reported to be trained entirely on Chinese chips.

---

End of digest. Close this tab when done.
