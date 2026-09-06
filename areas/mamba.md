## Mamba and State Space Models

### Timeline

2020 | HiPPO (Gu et al.) | 
2021 | SSM (LSSL) (Gu et al.) | 
2022 | S4 (Gu et al.) | 
2024 | Audio Mamba (Erol) (Erol et al.) | 
2024 | Audio Mamba (Yadav) (Yadav et al.) | 
2024 | Bi-Mamba+ (Liang et al.) | 
2024 | ClinicalMamba (Yang et al.) | 
2024 | HARMamba (Li et al.) |  [anchor]
2024 | Mamba (Gu et al.) | 
2024 | Mamba-2 (Dao et al.) | 
2024 | Mamba-UNet (Wang et al.) | 
2024 | MambaOut (Yu et al.) | 
2024 | Motion Mamba (Zhang et al.) | 
2024 | Swin-UMamba (Liu et al.) | 
2024 | U-Mamba (Ma et al.) | 
2024 | VMamba (Liu et al.) | 
2024 | Vision Mamba (Zhu et al.) | 

2026-06 | Language Models Need Sleep (2605.26099) | sleep consolidation distills attention context into SSM fast weights
2026-07 | FlashMorph (2606.30562) | selects which layers keep full attention via budget-constrained joint gate optimization for hybrid models
2026-08 | Massive Activations in Hybrid Linear Attention (2608.12149) | activation outliers spike before every full-attention layer and persist across linear-attention layers as plateaus, making quantization behavior predictable from the hybridization ratio
2026-08 | Fast Weight Attention (2608.27763) | reads the recurrent state update as online regression and corrects its target to the prefix-aligned pair, giving the normalized Falcon update family
2026-09 | Qwen3.8-Next Architecture (2608.30320) | three Gated DeltaNet layers per global attention layer, with extra capacity moved into host-memory n-gram embedding tables

2026-09 | NVFP4 W4A4 Gated DeltaNet (2609.04098) | all 496 linear layers of a hybrid 27B quantized to 4 bit match BF16; the recurrent gates are the least sensitive layers

### Paper List

[KNOWN] [2020] Gu et al. — HiPPO. zotero_key:5YQ4IKMA.
[KNOWN] [2021] Gu et al. — SSM (LSSL). zotero_key:UTAMLB63.
[KNOWN] [2022] Gu et al. — S4. zotero_key:J7K2E7A3.
[KNOWN] [2024] Erol et al. — Audio Mamba (Erol). zotero_key:6VTXUZEG.
[KNOWN] [2024] Yadav et al. — Audio Mamba (Yadav). zotero_key:5ZZDBB7N.
[KNOWN] [2024] Liang et al. — Bi-Mamba+. zotero_key:AVTJLZIR.
[KNOWN] [2024] Yang et al. — ClinicalMamba. zotero_key:E4QKRZTC.
[KNOWN] [2024] Li et al. — HARMamba. zotero_key:HE9X47KN.
[KNOWN] [2024] Gu et al. — Mamba. zotero_key:XNI34DQX.
[KNOWN] [2024] Dao et al. — Mamba-2. zotero_key:JPKDWV2Q.
[KNOWN] [2024] Wang et al. — Mamba-UNet. zotero_key:MHMYYQUF.
[KNOWN] [2024] Yu et al. — MambaOut. zotero_key:ZS87LF7R.
[KNOWN] [2024] Zhang et al. — Motion Mamba. zotero_key:J2EZPHK4.
[KNOWN] [2024] Liu et al. — Swin-UMamba. zotero_key:ZP32YT5I.
[KNOWN] [2024] Ma et al. — U-Mamba. zotero_key:INWKDM35.
[KNOWN] [2024] Liu et al. — VMamba. zotero_key:3LTBUP6E.
[KNOWN] [2024] Zhu et al. — Vision Mamba. zotero_key:J34W7WZC.

[2605] 2605.26099 — Language Models Need Sleep. [https://arxiv.org/abs/2605.26099](https://arxiv.org/abs/2605.26099). external.

[2026] 2606.30562 — Morphing into Hybrid Attention Models (FlashMorph). [https://arxiv.org/abs/2606.30562](https://arxiv.org/abs/2606.30562). external.

[2026] 2608.12149 — Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus. [https://arxiv.org/abs/2608.12149](https://arxiv.org/abs/2608.12149). external.
[2026] 2608.27763 — Fast Weight Attention for Continual Learning. [https://arxiv.org/abs/2608.27763](https://arxiv.org/abs/2608.27763). external.
[2026] 2608.30320 — On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability. [https://arxiv.org/abs/2608.30320](https://arxiv.org/abs/2608.30320). external.

[2026] 2609.04098 — Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM. [https://arxiv.org/abs/2609.04098](https://arxiv.org/abs/2609.04098). external.

### Recent Activity

2026-09-05 | 2609.04098 added | community 4-bit quantizations of the hybrid Qwen3.8-27B left the Gated DeltaNet block at 8 or 16 bit, especially its decay and write-strength gates, on the intuition that errors in a recurrence accumulate; the authors instead quantize all 496 linear layers to NVFP4 W4A4 with calibration-only post-training quantization and match BF16 within seed noise, a five-task average of minus 0.52 across MMLU-Pro, GSM8K, AIME'25, GPQA-Diamond, LiveCodeBench and RULER retrieval to 64K, at 17.5 GiB and 14 to 19 percent faster prefill, and the mechanism study finds the supposedly fragile gate projections are the least sensitive layers, compressing about 11 percent GEMM error to about 2 percent output error, while the delta rule forgets an injected state impulse within hundreds of steps because each write overwrites the state along the current key direction; where Audio Mamba (erol2024_audiomamba) established what a fixed-size recurrent state can represent over a long continuous sequence, this paper measures how much numerical precision that state actually needs and answers four bits, where MambaOut (ZS87LF7R) asked when the recurrence contributes at all, this paper turns the same ablation question on precision rather than presence and inverts the assumption those analyses inherited, that a recurrence is the fragile part of a hybrid model, and where DeepSeek-V2 (743XA29Y) answered the same memory problem by compressing the KV cache rather than replacing it with a recurrence, the comparison sharpens, because if the recurrent half is also the cheap half to quantize then the memory argument for latent KV compression weakens relative to hybrid designs; the reason given is structural rather than empirical, that the delta rule is contractive along the write direction so quantization noise is overwritten rather than integrated and the per-token quantization cost washes out with context instead of compounding, and Community 5, wearable sensing and behavior, contains no quantization work at all even though continuous sensing is where on-device precision matters most, so the claim is stated in a form that is testable on accelerometer or PPG streams rather than only on text benchmarks; Tier B

2026-09-01 | 2608.30320 added | an architecture report for Qwen3.8-Flash-Next, a sparse mixture-of-experts model with 125B total parameters, 6B activated per token, and a further 51B parameters of n-gram embedding tables kept in host memory rather than on the accelerator, mixing tokens with Gated DeltaNet layers and global attention at a ratio of three to one, swapping the full-attention layers for a sparse variant that scores context at micro-block granularity through a compressed indexer at continued-pretraining time, and widening the residual stream to four gated branches; against the 397B-A17B predecessor it leads on eight of fourteen pre-training benchmarks and trails on the rest by at most 2.6 points, at one third the activated parameters, one third the training tokens, and roughly one ninth the training FLOPs; where Mamba (XNI34DQX) and Mamba-2 (JPKDWV2Q) argued that a selective recurrence could replace attention outright, this report answers the how-much-attention question with a measured ratio rather than an argument and keeps one full-attention layer in four, and it moves capacity off the backbone entirely into prefetched embedding tables, an axis separate from both the attention-versus-recurrence and the mixture-of-experts questions, with Attention Is All You Need (PHB9VRVM) supplying the layer retained at that ratio; the finding worth carrying is that loss and downstream accuracy come apart, since enlarging the n-gram vocabulary lowers loss monotonically while downstream accuracy saturates, so architecture variants selected on validation loss alone will be misranked, and the hybrid ratio is the number to test against HARMamba and Bi-Mamba+, which take the all-recurrence position on long physiological sequences without measuring how much attention would have been worth keeping; the report also finds this design together with the Muon optimizer shifts the optimal learning rate and batch size upward and removes the need for batch-size warmup; Tier B

2026-08-31 | 2608.27763 added | treats the state update of a recurrent fast-weight memory or a selective state-space model as an online learning rule and then asks what that rule regresses on, arguing that under read-after-write autoregressive semantics the correctly aligned training pair at step t is the prefix-aligned (phi(k_{t-1}), v_t) rather than the same-step (phi(k_t), v_t) used by most existing linear-attention and state-space designs; from that correction it derives the normalized first-order Falcon family, a scalar normalized least-mean-squares update, a per-column extension and a sliding-window mini-batch update, together with inner-product variants and recurrent, masked-parallel and chunk-parallel forms with positive-decay renormalization for numerical stability; where Vaswani stored every past token in a growing key-value cache and Mamba compressed that history behind a learned selective gate, and where Mamba-2 proved selective state-space models and restricted linear attention are the same matrix computation, this paper takes the duality one level further and makes temporal alignment, plasticity, forgetting and bounded rehearsal four separable knobs instead of one entangled gate, with normalization playing the role step-size control plays in adaptive filtering; the reported benefit is length extrapolation on variable-digit addition rather than in-distribution perplexity, which fits the diagnosis that a misaligned target hurts most once the sequence runs past training length, and the abstract reports no headline numbers, so the first check is whether an ablation isolates prefix alignment from normalization; Tier A

2026-08-14 | 2608.12149 added | a measurement study of activation outliers in layer-interleaved hybrid linear-attention stacks, reporting that activations spike immediately before every full-attention layer and can persist across the intervening linear-attention layers as flat plateaus, and that as full attention gets denser the spikes join through the plateaus until the pattern converges to ordinary full-attention morphology; established across five linear-attention architectures, six hybridization ratios, five data domains, and open models from 1.2B to 397B total parameters, with controlled gated-delta-net pretraining up to 1.3B, and the mechanism offered is cancellation timing, so low-bit quantization behavior becomes predictable from the hybridization ratio instead of a per-model surprise; the paper is descriptive rather than a fix, and all evidence comes from language pretraining; Tier B

2026-07-03 | 2606.30562 added | FlashMorph makes hybrid-attention layer selection a budget-constrained joint optimization over per-layer gates rather than a fixed pattern or one-at-a-time scoring, then discretizes under a full-attention budget and distills; Tier B
