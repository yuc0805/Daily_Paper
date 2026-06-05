## Reasoning in Language Models

### Timeline

2025 | CODI (Shen et al.) | 
2025 | Large Multimodal Reasoning Survey (Li et al.) | 
2025 | Latent Reasoning Survey (Zhu et al.) | 
2025 | Machine Mental Imagery (Yang et al.) | 
2025 | Soft Thinking (Zhang et al.) | 
2026 | Chain of Superposition (Deng et al.) | 
2026 | CoLaR (Tan et al.) | 
2026 | Latent Space Survey (Yu et al.) | 
2026 | Latent-GRPO (Deng et al.) | 
2026 | PonderLM (Zeng et al.) | 

2026-05 | ScaleLogic (2605.06638) | RL training compute scales as a power law with reasoning depth; expressiveness sets the exponent
2026-05 | RL Unlocks Parametric Knowledge (2605.07153) | RL redistributes probability mass to surface latent facts
2026-05 | Sparse Policy Selection (2605.06241) | RL changes only 1 to 3 percent of tokens, at high-entropy points already in the base top-5
2026-05 | Reward-Function Search RL (2605.02073) | a frontier model searches the RL reward function instead of the policy for math reasoning
2026-06 | MemReread (2605.10268) | linear-cost long-context reasoning via a running memory plus on-demand rereading of source text
2026-06 | Agentic Transformers Search (2606.00183) | formal proof of RL-trained DFS with depth generalization
2026-06 | GRAIL (2606.04889) | token-wise saliency reweighting for RLVR advantage signals
### Paper List

[KNOWN] [2025] Shen et al. — CODI. zotero_key:FFWLYL3J.
[KNOWN] [2025] Li et al. — Large Multimodal Reasoning Survey. zotero_key:FPEC4PIH.
[KNOWN] [2025] Zhu et al. — Latent Reasoning Survey. zotero_key:EMXEJYHV.
[KNOWN] [2025] Yang et al. — Machine Mental Imagery. zotero_key:PDAMP7VF.
[KNOWN] [2025] Zhang et al. — Soft Thinking. zotero_key:EGRXFZU9.
[KNOWN] [2026] Deng et al. — Chain of Superposition. zotero_key:CXGMDHJ3.
[KNOWN] [2026] Tan et al. — CoLaR. zotero_key:Y4ZNT3EC.
[KNOWN] [2026] Yu et al. — Latent Space Survey. zotero_key:KRVDKDGH.
[KNOWN] [2026] Deng et al. — Latent-GRPO. zotero_key:U4ZPM5DN.
[KNOWN] [2026] Zeng et al. — PonderLM. zotero_key:3TLRP8U5.

[2026] 2605.06638 — Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key. [https://arxiv.org/abs/2605.06638](https://arxiv.org/abs/2605.06638). external.
[2026] 2605.07153 — Beyond Reasoning: Reinforcement Learning Unlocks Parametric Knowledge in LLMs. [https://arxiv.org/abs/2605.07153](https://arxiv.org/abs/2605.07153). external.
[2026] 2605.06241 — Rethinking RL for LLM Reasoning: It is Sparse Policy Selection, Not Capability Learning. [https://arxiv.org/abs/2605.06241](https://arxiv.org/abs/2605.06241). external.
[2026] 2605.02073 — Enhanced LLM Reasoning by Optimizing Reward Functions with Search-Driven Reinforcement Learning. [https://arxiv.org/abs/2605.02073](https://arxiv.org/abs/2605.02073). external.
[2026] 2605.10268 — MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading. [https://arxiv.org/abs/2605.10268](https://arxiv.org/abs/2605.10268). external.
[2606] 2606.00183 — Agentic Transformers Provably Learn to Search via RL. [https://arxiv.org/abs/2606.00183](https://arxiv.org/abs/2606.00183). external.
[2606] 2606.04889 — GRAIL: Gradient-Reweighted Advantages for RL with Verifiable Rewards. [https://arxiv.org/abs/2606.04889](https://arxiv.org/abs/2606.04889). external.
### Recent Activity

2026-06-04 | 2606.04889 added | Token-wise advantage reweighting via gradient-activation saliency for RLVR; outperforms GRPO by 3.60 percent accuracy wi; Tier B
2026-06-04 | 2606.00183 added | Formal proof that RL on shallow k-ary trees produces DFS-capable transformer policies that generalize to greater depth; ; Tier B
2026-06-01 | 2605.10268 added | drops the retrieval module and rereads raw source on demand; an RL controller bounds the number of rereading passes; Tier A
2026-05-30 | 2605.02073 added | freezes the policy and searches the RL reward function instead; ranked-feedback loop lifts GSM8K F1 from 0.609 to 0.795; Tier A
2026-05-29 | 2605.06241 added | token-level analysis finds RL selects among base-model solutions rather than teaching new reasoning; Tier B
2026-05-28 | 2605.06638 added | controlled synthetic logic; RL compute power law, exponent rises with logical expressiveness; Tier B
2026-05-28 | 2605.07153 added | RL improves factual recall by probability-mass redistribution, not new facts; Tier B
