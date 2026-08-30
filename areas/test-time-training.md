## Test-Time Training

### Timeline

2023 | UNI Pathology (Chen et al.) | 
2024 | TTT Layers (Sun et al.) | 
2024 | TTT for Abstract Reasoning (Akyurek et al.) | 
2024 | TTT-Unet (Zhou et al.) | 

2026-06 | PETSA (2506.23424) | parameter-efficient test-time adaptation for TS forecasting with spectral and structural losses
2026-06 | EASE-TTT (2606.06906) | evidence-aligned selective test-time training for long-context QA; supervises query-side attention with retrieved evidence
2026-07 | RoboTTT (2607.15275) | Test-Time Training fast weights act as scalable recurrent memory, scaling robot-policy context to 8,000 timesteps at constant inference latency
2026-08 | TTPO (2608.27448) | test-time reasoning post-training with no labels; majority vote distils agreeing rollouts and penalises disagreeing ones

### Paper List

[KNOWN] [2023] Chen et al. — UNI Pathology. zotero_key:6T29JLTN.
[KNOWN] [2024] Sun et al. — TTT Layers. zotero_key:JEGI4IS7.
[KNOWN] [2024] Akyurek et al. — TTT for Abstract Reasoning. zotero_key:W7RPRTCH.
[KNOWN] [2024] Zhou et al. — TTT-Unet. zotero_key:K9AZKZB2.

[2026] 2506.23424 — PETSA: Parameter-Efficient Test-Time Adaptation for Time Series Forecasting. [https://arxiv.org/abs/2506.23424](https://arxiv.org/abs/2506.23424). external.
[2026] 2606.06906 — EASE-TTT: Evidence-Aligned Selective Test-Time Training for Long-Context Question Answering. [https://arxiv.org/abs/2606.06906](https://arxiv.org/abs/2606.06906). external.
[2026] 2607.15275 — RoboTTT: Context Scaling for Robot Policies. [https://arxiv.org/abs/2607.15275](https://arxiv.org/abs/2607.15275). external.
[2026] 2608.27448 — TTPO: Test-Time Policy Optimization. [https://arxiv.org/abs/2608.27448](https://arxiv.org/abs/2608.27448). external.

### Recent Activity

2026-08-29 | 2608.27448 added | TTPO removes the ground-truth label from reasoning post-training so the update can run at test time on the problems the model is actually facing, sampling rollouts, forming a majority-vote pseudo-label, then distilling the rollouts that agree with the vote through on-policy self-distillation and penalising the ones that disagree with grouped reinforcement learning, with token-level selection down-weighting positions the distillation branch has already converged on and restricting the penalty to confidently wrong tokens; where TTT for Abstract Reasoning (W7RPRTCH) built a test-time supervision signal by augmenting the target task, TTPO builds it from the model's own rollout distribution so nothing task-specific has to be constructed, and where DeepSeek-R1 needed a verifiable reward to define the advantage, TTPO substitutes a vote and repairs its main weakness through an asymmetry, that a rollout disagreeing with the vote is usually wrong whether or not the vote itself is right, so the negative branch stays valid even when the positive branch is being taught the wrong answer; without labels it matches label-supervised on-policy self-distillation on five competition benchmarks and lifts Qwen3-1.7B from 38.0 to 45.2 percent; the method is tied to discrete answers that can be voted on, which is what would need replacing for a continuous physiological target; Tier A

2026-07-18 | 2607.15275 added | RoboTTT puts Test-Time Training inside a Vision-Language-Action policy so the recurrent state is a set of fast weights updated by gradient descent at both training and inference, scaling visuomotor context to 8,000 timesteps without added latency and reporting an 87% overall gain over a single-step baseline; Tier B
2026-06-28 | 2606.06906 added | EASE-TTT turns retrieved evidence into a soft attention target and trains only query-side attention at test time, beating full-context, retrieval-only, and query-only test-time training on six LongBench QA tasks; Tier B
2026-06-05 | 2506.23424 added | parameter-efficient TTA for TS foundation models; low-rank adapters with frequency-domain and patch-wise structural losses; Tier B
2026-05-14 | Area page seeded | 4 papers from Zotero, 1 from graphify seed.
