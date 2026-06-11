# AI Digest — 2026-06-11

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### U-TTT: Towards Generalizable PET Image Denoising via Test-Time Training
arXiv:2606.11032 — https://arxiv.org/abs/2606.11032 (Yang, Li, Lu, Zhang, Wang, Wei, Xu; June 9)

Problem. Deep denoising models for PET imaging are trained on one acquisition setting and deployed on others. Performance drops sharply when dose level or scanner type changes, because parameters are frozen after training. This restricts clinical use, where dose protocols and hardware differ across sites.

Method. U-TTT is a U-shaped denoising network whose inner blocks are Test-Time Training layers: parameters update during inference through a self-supervised loss computed on each test instance, so the model adapts to the specific volume in front of it. The adaptation is dual-domain: a Spatial TTT layer corrects structural degradation, and a Frequency TTT layer suppresses global noise spectra while restoring high-frequency detail.

Result. The paper reports state-of-the-art PET denoising and improved generalization to both unseen dose levels and unseen scanners. The abstract does not give numeric deltas, so apply the two-page test against Table 1 before committing the full 20 minutes. Code: github.com/Yaziwel/U-TTT.

Limitations. PET only; per-instance adaptation adds inference compute, which matters for clinical throughput; sensitivity to the choice of self-supervised objective is not stated in the abstract.

Why it matters to you. This is the TTT-for-distribution-shift recipe applied to a bio-imaging modality — the clearest porting template of the day. The same per-instance adaptation logic transfers to wearable biosignal denoising, where dose level and scanner type have direct analogs in sampling rate, sensor placement, and device hardware.

How this builds on what you know: Parent lookup went through graphify first; the TTT papers are not among the 49 seed nodes, so matching fell back to your Zotero index. The parents are TTT Layers (Sun 2024) and TTT-Unet (Zhou 2024), both in your test-time-training collection. Where TTT Layers established the hidden-state-as-model formulation that makes adaptation a layer property, and TTT-Unet put TTT layers inside a U-Net for medical image segmentation, this paper does the same for PET denoising and adds a frequency-domain TTT branch, because PET noise is better characterized in the spectrum than in image space.

## Tier B — TLDRs

### 1. Rethinking the Divergence Regularization in LLM RL (DRPO)
arXiv:2606.09821 — https://arxiv.org/abs/2606.09821 (Tencent Hunyuan; June 8)

LLM RL post-training is usually off-policy because of training-inference mismatch and policy staleness, so trust-region control decides whether training is stable. PPO and GRPO approximate the trust region with ratio clipping, a poor proxy for distributional shift on long-tailed vocabularies; DPPO replaced clipping with a hard divergence-based mask, but a hard mask discards the gradient of any token that crosses the boundary. DRPO replaces the mask with a smooth advantage-weighted quadratic regularizer on policy shift, keeping the same trust-region geometry while turning discarded gradients into bounded corrective signals. Experiments across model scales, architectures, and precision settings show more stable and more efficient RL training.

How this builds on what you know: The nearest parent in your library is DeepSeek-R1 (graphify: deepseek2025_r1, community 0 — LLM Agents & Reasoning), which made RL the main engine for reasoning and exposed exactly the stability problems DRPO targets; Latent-GRPO (Deng 2026) is the second parent, working inside the same GRPO objective family. This paper also extends a graphify bridge: deepseek2025_r1 already crossed the RL and prompting sides of community 0 through wei2023_cot (reasoning-via-RL vs prompting). DRPO pushes the bridge further into RL-optimization territory — the question is no longer whether RL beats prompting but which trust-region geometry makes RL dependable.

### 2. Attention Amnesia in Hybrid LLMs: When CoT Fine-Tuning Breaks Long-Range Recall
arXiv:2606.11052 — https://arxiv.org/abs/2606.11052 (HKUST-GZ LARK Lab; June 9)

CoT supervised fine-tuning reliably improves reasoning, but in hybrid linear-attention models it destroys long-context retrieval: HypeNet-9B falls from 67.2% to 9.4% on NIAH-S2 at 256K context after CoT-SFT, with worse damage at longer contexts. The authors trace the cause to the query-key projections (W_Q, W_K), whose gradients become biased toward short-range patterns. The fix, QK-Restore, is training-free: revert only W_Q and W_K to the pre-SFT checkpoint and keep everything else; a Procrustes variant balances routing preservation against reasoning adaptation. On HypeNet-5B it lifts S3@256K from 65.4% to 76.4% with reasoning intact.

How this builds on what you know: One parent is Chain-of-Thought Prompting (graphify: wei2023_cot, community 0 god node) — the supervision signal that causes the damage. On the architecture side the nearest anchors sit in community 2 (Transformer & SSM Architectures): TTT Layers and the HARMamba line define the linear-recurrence family these hybrids descend from. Where Wei 2023 showed step-by-step supervision helps reasoning, this paper shows the same supervision quietly breaks the memory pathway of linear-attention hybrids, because both abilities share W_Q/W_K. The paper effectively adds a new edge between community 0 (reasoning) and community 2 (architectures) in your graph.

### 3. Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory
arXiv:2606.10677 — https://arxiv.org/abs/2606.10677 (June 9)

Infini Memory proposes a text-based persistent memory for LLM agents: memory is a set of topic documents, each a semantic unit that collects related evidence, preserves metadata, and revises facts over time, rather than an append-only log or a vector store of isolated snippets. The design targets long-term maintenance problems — contradiction, staleness, unbounded growth — that flat retrieval memories do not handle. Note: this summary is abstract-level; benchmark numbers were not in the sources I could access today.

How this builds on what you know: The parent is Rethinking Memory Mechanisms of Foundation Agents (graphify: huang2026_memory, community 0), which catalogued memory designs and flagged maintainability as an open problem. Where the survey described write and read policies in the abstract, this paper commits to one opinionated structure — topic documents with revision semantics — because fact revision is hard to express in append-only or embedding-only memories. Contrast with yesterday's two memory papers (ExpWeaver, MemoPilot), which went latent for efficiency; Infini Memory argues plain text is what keeps memory maintainable.

## Tier C — scan headlines

1. Kwai Keye-VL-2.0 Technical Report — production multimodal LLM report, top-voted paper of the day. https://arxiv.org/abs/2606.10651
2. ARM — one autoregressive model with discrete representations unifies image understanding, generation, and editing. https://arxiv.org/abs/2606.11188
3. MemToolAgent — memory over tool-use feedback; +29/+80/+17% relative on three tool benchmarks. https://arxiv.org/abs/2606.07909
4. Dynamic Linear Attention — ByteDance Seed's input-dependent linear attention variant. https://arxiv.org/abs/2606.10650
5. EEVEE — test-time prompt learning in the real world for self-improving agents. https://arxiv.org/abs/2606.11182
6. Text World Models for LLM-based Agents — closing the agent-world gap with learned text simulators. https://arxiv.org/abs/2606.09032
7. Workflow-GYM — long-horizon evaluation of computer-use agents on real professional workflows. https://arxiv.org/abs/2606.11042
8. WorldOlympiad — a triathlon-style stress test for world models. https://arxiv.org/abs/2606.11129

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported: U-TTT closes the TTT-to-PET-denoising port. Your library already had TTT-Unet carrying TTT into medical segmentation, so today's paper extends that occupied territory by one task. Treat per-instance TTT for medical imaging as done.

Unported opportunity 1: QK-Restore-style selective weight reversion has no match in the community 5 (Wearable Sensing & Behavior) hyperedges. Transfer hypothesis: fine-tuning a pretrained sensor encoder (for example the Yuan 2024 SSL-HAR model) on a narrow downstream task plausibly damages long-range temporal recall the same way CoT-SFT damages NIAH; reverting input projections after fine-tuning is a one-afternoon experiment with a clean before/after metric.

Unported opportunity 2: divergence-regularized RL (the DPPO-to-DRPO line) has no match in the community 4 (Time Series + LLM Integration) hyperedges. Transfer hypothesis: RL fine-tuning of a TS-Agent-style tool-using policy faces the same off-policy instability DRPO fixes, and DRPO is objective-level rather than architecture-level, so it ports without modification.

## News

1. Anthropic released Claude Fable 5 (June 9), the first model in the new Claude 5 family. It is positioned as the most capable generally available Claude model; a sibling, Claude Mythos 5, shares the same underlying model and is limited to approved organizations.
2. OpenAI models, including Codex, became available through Oracle cloud (announced June 11), alongside a confidential draft S-1 filing on June 10 signaling movement toward a public listing.
3. Watch list: Gemini 3.5 Pro and Grok 5 are rumored or scheduled for later in June; nothing released yet.

---

Knowledge graph updated: 4 paper notes written to papers/2026/06/11/, 4 website paper pages and today's front-page cards generated. Area pages and lineage edges will be promoted by the evening archive task.

End of digest. Close this tab when done.
