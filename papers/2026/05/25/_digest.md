# AI Digest — 2026-05-25

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### DashAttention: Differentiable and Adaptive Sparse Hierarchical Attention
Huang, Gonçalves, Alvetreti, Li, Han, Ponti, Martins, Treviso — arXiv:2605.18753 — 2026-05-18

**Problem.** Hierarchical sparse attention methods like NSA and InfLLMv2 reduce the cost of long-context LLM inference by selecting the top-k most relevant key-value blocks before applying fine-grained attention. However, the top-k operation has two structural problems: it assumes every query attends to exactly the same number of blocks (which is false — some queries are local while others require global context), and it blocks gradient flow between the coarse selection stage and the fine attention stage, making end-to-end training impossible through the sparsity mechanism.

**Method.** DashAttention replaces top-k with alpha-entmax, a differentiable sparse transformation that maps scores to a probability distribution where some entries are exactly zero. The number of selected blocks varies per query — queries with concentrated attention patterns select fewer blocks, while queries needing broad context select more. Because alpha-entmax is differentiable everywhere (including at the sparsity boundary), the full two-stage hierarchy is end-to-end trainable. The alpha-entmax output also serves as a prior for second-stage softmax attention on the selected tokens, which the authors show makes the method "non-dispersive": attention mass stays concentrated on the truly relevant tokens rather than spreading across all selected blocks equally.

**Result.** At 75% sparsity, DashAttention matches full-attention accuracy on language modeling benchmarks. On the Pareto frontier of accuracy vs. sparsity, DashAttention strictly dominates NSA and InfLLMv2, with the gap widening in high-sparsity regimes (>80%). The authors provide a Triton implementation that achieves speedup over FlashAttention-3 at inference time. The non-dispersive property translates to measurably better performance on long-context tasks like RULER and needle-in-a-haystack.

**Limitations.** The paper evaluates on standard LLM language modeling and RULER-style benchmarks. Whether the adaptive block selection transfers well to non-text modalities (e.g., time-series tokens or vision patches) is untested. The alpha-entmax hyperparameter alpha controls the sparsity shape but its sensitivity across model scales is not thoroughly ablated. Training overhead relative to standard attention is not explicitly reported.

**Why it matters to Leo.** If you work with long-context Transformer architectures — either for time-series foundation models that process long sensor sequences or for LLM agents that need to attend over extended reasoning traces — DashAttention is a drop-in replacement that provides adaptive, input-dependent sparsity without losing trainability. The non-dispersive property is especially attractive for time-series applications where a small number of tokens carry the actual signal (e.g., event onsets in biosignal data) and the model must not dilute attention across irrelevant background.

**How this builds on what you know:** DashAttention is a direct architectural improvement to the Transformer (Vaswani 2017), the anchor paper in your Community 2. Where the original Transformer uses dense softmax attention with O(n^2) cost, DashAttention introduces learned, adaptive sparsity while keeping end-to-end differentiability. This connects to your time-series area: models like PatchTST (Nie 2023) and iTransformer (Liu 2024) in your library inherit the dense-attention bottleneck from the Transformer. DashAttention would let these architectures handle much longer input sequences — hundreds of patches covering full-day sensor recordings — without the quadratic blowup. No parent in your library directly addresses hierarchical sparse attention, so this paper opens a new branch from the Transformer node.

---

## Tier B — TLDRs

### 1. Post-Trained MoE Can Skip Half Experts via Self-Distillation (ZEDA)
Lv et al. (Tsinghua, Shanghai AI Lab, Kuaishou) — arXiv:2605.18643 — 2026-05-18

Mixture-of-Experts models like DeepSeek-V3 activate a fixed number of experts per token during inference, regardless of input difficulty. ZEDA (Zero-Expert Self-Distillation Adaptation) converts an already-trained static MoE into a dynamic one that skips up to half of its experts on easy inputs. The method works by self-distilling: the full model serves as teacher, and a learnable router decides per-token how many experts to activate. Because it operates on post-trained models, ZEDA avoids the cost of MoE pre-training from scratch. The result is a roughly 50% reduction in activated parameters on routine tokens with negligible accuracy loss, making large MoE models cheaper to serve.

**How this builds on what you know:** This directly extends DeepSeek-V3 (2024) in your library (Community 0, graphify_id deepseek2024_v3). Where DeepSeek-V3 introduced an efficient MoE architecture with fixed routing, ZEDA adds input-adaptive expert skipping post-hoc. It also connects to your MoE area (ST-MoE, MoE Explained). The self-distillation approach parallels the Learning to Foresee paper from yesterday's digest, which analyzed how distillation creates efficient parameter updates — ZEDA applies distillation specifically to learn which experts are unnecessary per input.

### 2. Stop When Reasoning Converges: Semantic-Preserving Early Exit for Reasoning Models
Min, Vaccarino, Chen, Wu, Yona, Cheng (UIC, Google Research, UIUC) — arXiv:2605.17672 — 2026-05-17

Large reasoning models like DeepSeek-R1 often overthink: they continue generating chain-of-thought tokens long after the answer has stabilized. Existing early-exit methods use answer-level signals (e.g., trial-answer consistency), but these can trigger prematurely while the model is still self-correcting. This paper identifies reasoning-level semantic redundancy as a complementary signal: when successive reasoning steps no longer introduce novel information and instead repeat established conclusions, the trajectory has converged. The method detects this convergence by measuring the semantic similarity between consecutive reasoning windows and exits early when the similarity exceeds a threshold. This saves tokens and reduces latency without sacrificing accuracy, because it exits only after the reasoning has genuinely stabilized rather than when the answer first appears correct.

**How this builds on what you know:** This extends the reasoning chain paradigm established by Chain-of-Thought Prompting (Wei 2023, Community 0) and DeepSeek-R1 (2025, Community 0). Where yesterday's Tier A paper (Taming the Thinker) controls reasoning depth at training time via entropy shaping, this paper works at inference time by detecting convergence on-the-fly. Together they represent complementary approaches to the same problem: adaptive reasoning depth. The semantic convergence signal could also apply to agentic tool-use loops (relevant to your Agent area), where an agent repeatedly calls the same tool without making progress.

### 3. STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
Shen et al. (Apple, UIUC) — arXiv:2605.08029 — 2026-05-08

Most unified multimodal models combine autoregressive text generation with diffusion-based image generation, creating a structural mismatch: text is generated left-to-right while images require iterative denoising. STARFlow2 observes that autoregressive normalizing flows are themselves autoregressive Transformers — they share the same causal mask, KV-cache, and left-to-right structure as LLMs. The Pretzel architecture vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both under the same causal mask. A deep-shallow flow design and unified FAE latent space enable cache-friendly interleaved generation where text and image tokens both enter the KV-cache directly. The result is a truly unified multimodal generator that avoids the encode-then-denoise bottleneck, with strong performance on both generation and understanding benchmarks.

**How this builds on what you know:** STARFlow2 sits in your Community 3 (Vision-Language & Generative). It extends SigLIP (Zhai 2023) for visual encoding and DDPM (Ho 2020) / DiT (Peebles 2023) for generation, but replaces diffusion with normalizing flows to achieve architectural unification. Where Lance (from yesterday's digest) unifies modalities via MoE routing, STARFlow2 unifies via matching the generative paradigm (flows) to the language paradigm (autoregressive). This is a distinct design point: Lance uses dual streams with MoE, while STARFlow2 uses a single interleaved stream with flows. Both avoid the old pattern of "LLM + separate diffusion model."

---

## Tier C — Scan Headlines

1. **Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization** (2605.15980) — ICML 2026. Applies GRPO to align video diffusion models in a single optimization step rather than multi-step rollouts. [arxiv](https://arxiv.org/abs/2605.15980)

2. **CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection** (2605.16839) — Reduces KV cache memory during prefill by selecting and merging relevant KV blocks. [arxiv](https://arxiv.org/abs/2605.16839)

3. **GQLA: Group-Query Latent Attention for Hardware-Adaptive LLM Decoding** (2605.15250) — Peking University. Extends GQA with latent compression for decode-time memory savings. [arxiv](https://arxiv.org/abs/2605.15250)

4. **Sparse Autoencoders Enable Robust and Interpretable Fine-tuning of CLIP** (2605.15961) — Uses SAEs to decompose CLIP features and selectively fine-tune interpretable directions. [arxiv](https://arxiv.org/abs/2605.15961)

5. **MetaAgent-X: Breaking the Ceiling of Automatic Multi-Agent Systems via End-to-End RL** (2605.14212) — Oregon State. Trains the multi-agent system itself via RL rather than hand-designing agent roles. [arxiv](https://arxiv.org/abs/2605.14212)

6. **SNLP: Layer-Parallel Inference via Structured Newton Corrections** (2605.17842) — Red Hat AI. Runs Transformer layers in parallel at inference using Newton-method corrections, trading accuracy for latency. [arxiv](https://arxiv.org/abs/2605.17842)

7. **Hölder Policy Optimisation** (2605.12058) — Generalizes PPO using Hölder divergences, providing a family of policy optimization objectives with tunable exploration. [arxiv](https://arxiv.org/abs/2605.12058)

8. **Steered LLM Activations are Non-Surjective** (2604.09839) — Johns Hopkins. Shows that activation steering cannot reach all points in activation space, placing theoretical limits on steering methods. [arxiv](https://arxiv.org/abs/2604.09839)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

No new TS/bio-sensing papers landed today. Here are unported opportunities from this week's top CV/NLP papers:

**Unported Opportunity 1: DashAttention for long-sequence biosignal models.** DashAttention's adaptive sparse attention (Tier A above) has not been applied to time-series foundation models. Current TS foundation models (PatchTST, Moirai, Chronos) inherit dense softmax attention and struggle with very long input windows. Transfer hypothesis: replace dense attention in a TS foundation model with DashAttention's alpha-entmax hierarchy, allowing the model to adaptively attend to event-relevant patches (e.g., arrhythmia onset in ECG) while ignoring baseline segments. This would directly extend the ts_llm_reasoning_pipeline hyperedge (Community 4) by adding efficient attention.

**Unported Opportunity 2: ZEDA-style dynamic expert skipping for time-series MoE models.** WaveToken (Masserano 2024) in your library already combines MoE with time-series tokenization. ZEDA's self-distillation for dynamic expert activation (Tier B above) could be ported to WaveToken, allowing easier signals (e.g., stationary segments) to use fewer experts while non-stationary transitions get the full expert set.

---

## News

1. **Google I/O 2026 (May 19):** Gemini 3.5 Flash released. Lightweight, fast, agentic-first. 1M token context, $0.50/M input. Google is positioning Flash as the default agent backbone — 76.2% on Terminal-Bench 2.1. 3.5 Pro is delayed.

2. **Meta Muse Spark:** First model from Meta Superintelligence Labs. Natively multimodal, proprietary (departing from Llama's open-weight tradition). Scores 52 on Artificial Analysis Index, close to Claude Opus 4.6 (53). "Visual chain of thought" feature for dynamic scene reasoning.

3. **US Government AI Safety Testing:** AISI expanded its pre-release testing program to include Google DeepMind, Microsoft, and xAI models alongside OpenAI and Anthropic, testing for cybersecurity, biosecurity, and infrastructure risks.

---

End of digest. Close this tab when done.
