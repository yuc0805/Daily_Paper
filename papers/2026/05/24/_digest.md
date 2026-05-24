# AI Digest — 2026-05-24

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Taming the Thinker: Conditional Entropy Shaping for Adaptive LLM Reasoning
Wei, Sun, Qiu, Wang, Liu, Liang, Fu, Huang, Sang — arXiv:2605.19358 — 2026-05-19

**Problem.** Entropy-based deep reasoning methods for LLMs face a fundamental tension: methods that encourage longer reasoning chains improve accuracy on hard problems but waste tokens on easy ones, while methods that shorten responses sacrifice accuracy. No existing RL-based training objective adaptively allocates reasoning depth per-problem in a principled way. DAPO and related approaches apply uniform policy updates regardless of problem difficulty.

**Method.** Conditional Entropy Shaping (CES) uses token-level entropy as an uncertainty signal and applies a conditional bidirectional policy built on top of DAPO. At each "forking point" token (tokens with high entropy, indicating the model is uncertain about the next step), CES applies different incentives depending on whether the reasoning path leads to a correct or incorrect answer. On correct paths, high-entropy forking points are penalized to compress reasoning and remove unnecessary exploration. On incorrect paths, high-entropy forking points are rewarded to encourage the model to explore alternative directions and self-correct. The net effect is that easy problems (where correct paths appear quickly) get shortened, while hard problems (where incorrect paths are common) get deeper exploration.

**Result.** Implemented on DeepSeek-R1-Distill-7B and evaluated on 12 mathematical benchmarks: CES consistently improves average accuracy over DAPO while simultaneously reducing average response length. The gains hold on a smaller 1.5B backbone and transfer to out-of-domain benchmarks, suggesting the learned entropy-shaping behavior generalizes rather than overfitting to specific problem types.

**Limitations.** The evaluation is restricted to mathematical reasoning benchmarks. Whether CES generalizes to other reasoning domains (code, scientific reasoning, planning) is untested. The method requires running DAPO first as a base, adding one more stage to the training pipeline. The paper does not report wall-clock training cost comparisons, only token-length reductions at inference. The entropy threshold that defines "forking points" is a hyperparameter whose sensitivity is not fully explored.

**Why it matters to Leo.** If you are training reasoning models for scientific applications — for example, an LLM agent that reasons over time-series patterns or clinical measurements — you want the model to think deeply on genuinely ambiguous cases but respond quickly on routine ones. CES provides a mechanism for this without needing to pre-classify problem difficulty. The token-level entropy signal is domain-agnostic: it could apply to any sequential generation task where some outputs require more computation than others, including multi-step sensor data interpretation.

**How this builds on what you know:** CES directly extends DeepSeek-R1 (2025) in your library (Community 0). DeepSeek-R1 showed that RL unlocks reasoning in LLMs; CES adds an entropy-based adaptive mechanism on top of RL training to control when and how much reasoning happens. The relationship to Chain-of-Thought Prompting (Wei 2023) is also clear: CoT produces reasoning traces at inference time by prompting, while CES shapes the distribution of reasoning depth at training time by conditioning on entropy signals. The bidirectional reward based on path correctness also relates to the ActFocus paper (2605.14558) from Thursday's digest — both papers diagnose that uniform token-level RL signals are wasteful, but ActFocus reweights by token type (action vs. reasoning) while CES reweights by uncertainty level within reasoning tokens. Together they suggest a convergence toward fine-grained token-level credit assignment as the next frontier in LLM RL.

---

## Tier B — TLDRs

### 1. Lance: Unified Multimodal Modeling by Multi-Task Synergy
Fu et al. (ByteDance) — arXiv:2605.18678 — 2026-05-18

Lance is a 3B-active-parameter native unified model for image and video understanding, generation, and editing, trained entirely from scratch within a 128-A100 budget. It uses a dual-stream mixture-of-experts architecture on shared interleaved multimodal sequences, enabling joint context learning while decoupling understanding and generation pathways. A modality-aware rotary positional encoding mitigates interference among heterogeneous visual tokens. Lance demonstrates that collaborative multi-task training — not simply scaling model capacity — can unify diverse multimodal capabilities. It outperforms larger specialized models on image generation and editing benchmarks despite its small size.

**How this builds on what you know:** Lance sits in your Community 3 (Vision-Language & Generative). It extends the vision-language encoder tradition of SigLIP (Zhai 2023) and SigLIP 2 (Tschannen 2025) but goes further: rather than encoding visual features for a separate generator, Lance jointly trains understanding and generation in one model. The MoE routing connects to your MoE area — Lance is essentially a small but effectively-routed MoE that achieves specialization through routing rather than scale. The from-scratch training on 128 GPUs is notable for academic feasibility. The dual-stream design also relates to DiT (Peebles 2023): where DiT introduced Transformer-based diffusion, Lance shows you can fold diffusion-style generation into a unified language model with MoE routing.

### 2. HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse MoE
Zhong, Zheng, Allen-Blanchette (Princeton) — arXiv:2605.13997 — 2026-05-13

Standard approaches to compressing MoE layers merge experts based on pairwise similarity scores (e.g., KL divergence between expert outputs). HodgeCover identifies a fundamental failure mode: three experts can be pairwise compatible but form an irreducible cycle when merged together, so any pairwise score is structurally blind to problematic triples. The paper formalizes this using the Hodge decomposition of the simplicial Laplacian on a 2-complex whose vertices are experts, edges carry pairwise KL barriers, and faces carry triplet barriers. HodgeCover greedily covers harmonic-critical edges and triplet-critical triangles. In practice, it achieves substantially better accuracy retention than pairwise-only merging at the same compression ratio.

**How this builds on what you know:** This paper connects your MoE area page with your Mathematics-ML area. The Hodge-decomposition formalism is from algebraic topology and connects to the CUR/sparse matrix tradition (Mahoney 2009) in your library — both are about finding low-dimensional structure in high-dimensional objects, but HodgeCover operates on the expert interaction graph rather than on weight matrices. For the MoE research direction in your library, this is the first principled explanation of why greedy pairwise expert merging fails, which has direct implications for deploying large MoE models like DeepSeek-V3 efficiently.

### 3. Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation
Cai et al. (Tencent Hunyuan) — arXiv:2605.11739 — 2026-05-12

On-policy distillation (OPD) is known to be more efficient than off-policy distillation for LLM post-training, but why it works at the parameter level has been unclear. This paper shows OPD's efficiency stems from a form of "foresight": it establishes a stable update trajectory toward the final model early in training. At the module-allocation level, OPD identifies regions with low marginal utility and concentrates updates on modules most critical to reasoning. At the update-direction level, OPD exhibits stronger low-rank concentration, with its dominant subspaces aligning closely with the final update subspace from early training. The paper proposes a method to predict OPD-aligned update directions cheaply, enabling faster convergence.

**How this builds on what you know:** This paper extends the training efficiency theme from yesterday's Tier A (IXT, 2605.20285). Where IXT improved pretraining efficiency via feedback conditioning, this paper explains why distillation is efficient during post-training. Both converge on the same insight: not all parameters benefit equally from gradient updates, and focusing updates on the important subspace accelerates learning. The low-rank update concentration connects to optimizer research in your library — Adam (Kingma 2017) treats all parameters equally, but these results suggest that adapting step sizes per-subspace (not just per-parameter) could yield further gains. No direct parent in graphify, but thematically closest to the Transformer architecture community and the optimizer area.

---

## Tier C — Scan Headlines

1. **Nudging Beyond the Comfort Zone: Strategy-Guided Exploration for RLVR** (2605.15726) — External reasoning pathways help models escape exploration stagnation during RL training; KAIST. [arXiv](https://arxiv.org/abs/2605.15726)

2. **Elastic Attention Cores (VECA)** (2605.12491) — Linear-time attention via learned core tokens that mediate all patch communication; no direct patch-to-patch interaction needed. [arXiv](https://arxiv.org/abs/2605.12491)

3. **Post-Trained MoE Can Skip Half Experts via Self-Distillation (ZEDA)** (2605.18643) — Converts static post-trained MoE into dynamic MoE; easy tokens bypass unnecessary experts at serving time. [arXiv](https://arxiv.org/abs/2605.18643)

4. **MMSkills: Multimodal Skills for General Visual Agents** (2605.13527) — Reusable state-conditioned skill packages for runtime visual decision-making; SJTU. [arXiv](https://arxiv.org/abs/2605.13527)

5. **MetaAgent-X: End-to-End RL for Multi-Agent Systems** (2605.14212) — Joint optimization of meta-level designer and downstream executor agents via hierarchical rollout. [arXiv](https://arxiv.org/abs/2605.14212)

6. **Distilling Long-CoT via Collaborative Step-wise Multi-Teacher Decoding** (2605.02290) — Multiple teacher models collaborate at each reasoning step for better distillation. [arXiv](https://arxiv.org/abs/2605.02290)

7. **CompactAttention: Chunked Prefill with Block-Union KV Selection** (2605.16839) — Reduces KV cache during chunked prefill by selecting relevant blocks; Seoul National University. [arXiv](https://arxiv.org/abs/2605.16839)

8. **SNLP: Layer-Parallel Inference via Structured Newton Corrections** (2605.17842) — Parallelizes transformer layers at inference time using Newton-method corrections; Red Hat AI. [arXiv](https://arxiv.org/abs/2605.17842)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**
VECA's core-token attention structure (2605.12491) eliminates quadratic attention by routing all communication through a small set of learned cores. A similar "virtual token" approach has already been applied to time-series transformers (e.g., PatchTST uses channel-independent patches; iTransformer uses variate tokens as communication interfaces). The core-token idea overlaps substantially with existing TS architectures.

**Unported opportunity:**
CES's conditional entropy shaping (2605.19358) has a clean transfer hypothesis for time-series reasoning agents. If you train a TS-Agent or Nexus-style multi-agent forecaster with RL, the model should spend more reasoning tokens on volatile, high-uncertainty time windows and fewer on stable, predictable periods. Token-level entropy during generation naturally signals this: high entropy at a forecasting step means the model is uncertain about the trend. CES's bidirectional reward could be adapted so that on windows where the forecast is correct, verbose reasoning is penalized, and on windows where the forecast fails, deeper exploration is rewarded. No one has applied adaptive-depth reasoning control to time-series forecasting agents.

HodgeCover's topological merging (2605.13997) has an indirect porting opportunity for multi-sensor fusion. If you have multiple biosignal channels (EEG, PPG, accelerometer), each processed by a channel-specific expert, deciding which channel-experts to merge for efficiency is a combinatorial problem with the same higher-order interaction structure. Pairwise channel compatibility does not guarantee joint compatibility. Hodge decomposition on the channel-expert interaction graph could guide principled sensor fusion compression.

---

## News

1. **Google I/O 2026** (May 20-21): Google released Gemini 3.5 Flash (faster, cheaper) rather than competing at the frontier scale. Revamped search box unifies traditional queries with chatbot conversations. YouTube gets "Ask YouTube" natural-language video search.

2. **Meta Muse Spark**: Meta released Muse Spark, its first flagship LLM from Alexandr Wang's Superintelligence Labs. Competitive on multimodal perception, reasoning, and agentic tasks at lower compute cost. Meta also announced $115-135B AI capex for 2026.

3. **US Government AI safety expansion**: AI safety evaluation program now includes Google DeepMind, Microsoft, and xAI models alongside existing OpenAI and Anthropic partnerships.

---

End of digest. Close this tab when done.
