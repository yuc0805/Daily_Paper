# AI Digest — 2026-06-22

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on signal: few brand-new June 22 listings qualified for a deep read today. The strongest material sits in your primary area (wearable sensing and self-supervised learning), even though one of the papers is a few weeks old. It has not been featured before and it answers a question you have been tracking, so it earns Tier A.

---

## Tier A — deep read (~20 min)

### Bio-Inspired Self-Supervised Learning for Wrist-worn IMU Signals (Bio-PM)
arXiv:2603.10961 — https://arxiv.org/abs/2603.10961 — Tarale, Chu, Varghese, Liu, Xu, Iyyer, Lee (UMass Amherst, Stevens, Google Research, UMD), March 2026.

**Problem.** Wearable accelerometers produce large amounts of unlabeled data, but labels for human activity recognition (HAR) are scarce and expensive. Self-supervised learning is the usual remedy. The authors argue that current self-supervised methods for wearable data share a hidden weakness: they treat the accelerometer stream as an unstructured time series and pick token boundaries by arbitrary rules (fixed-length windows or chunks). The model therefore spends its capacity on local waveform shape and never learns the event-level structure of how movements compose into activities.

**Method.** The paper proposes a tokenization grounded in the submovement theory of motor control, which says continuous wrist motion is built from short bell-shaped velocity units. Rather than fit those units directly (expensive), they define a token as a "movement segment": the stretch of signal between successive zero-crossings of acceleration on each axis. Each segment is resampled to a fixed length, encoded by a small 1D CNN, tagged with its axis and duration, and ordered in time. A 5-layer Transformer with time-aware positional encodings then models the sequence of segments, trained by masked reconstruction (mask half the segments, also corrupt some visible ones to block trivial copying). The resulting encoder, Bio-PM, is pretrained on the NHANES corpus (about 28,000 hours, 11,000 participants, 10 million windows).

**Result.** Across six subject-disjoint HAR benchmarks, Bio-PM improves macro-F1 by an average of 6 percent (range 4 to 12 percent) over strong self-supervised baselines that were pretrained on the same corpus with the same protocol, so the gain is attributable to the tokenization rather than to more data. The method also holds up better than the baselines in low-label settings. The authors compare against contrastive learning (TF-C), augmentation prediction (the Yuan 2024 objective), and equal-length-chunk masked reconstruction, and also report generic time-series foundation models (Chronos, Moment) as reference points.

**Limitations.** The evaluation is linear probing on a frozen encoder, not full fine-tuning, so transfer under fine-tuning is untested. Tokenization rests on a motor-control prior that fits wrist motion; whether it carries to chest, thigh, or multi-sensor placements is not shown. Zero-crossing segmentation needs a high-pass filter and hysteresis tuning, which adds preprocessing the baselines do not need. Gains are reported as macro-F1 deltas without latency or model-size comparisons.

**Why it matters to Leo.** This is squarely your primary area. It is a clean, controlled test of one idea — that the tokenizer, not the objective, is the bottleneck in wearable self-supervised learning — and it imports the language-modeling lesson that meaningful tokens carry the structure. If the claim holds, it changes where the next gain in bio-sensing representation learning will come from.

How this builds on what you know: The direct parent is SSL for HAR with 700K Person-days (Yuan 2024) [RTMH75VW], the god node of your self-supervised area and one of the baselines here; where Yuan used augmentation prediction over fixed windows, Bio-PM keeps the large-scale pretraining idea but replaces the input unit with movement segments, because the authors argue fixed windows hide the compositional structure of movement. It also builds on How Mask Matters: Masked Autoencoders Theory (Zhang 2023) [6INGKIJV], which sits in the same Health AI and Self-Supervised community in your library: Bio-PM uses masked reconstruction, but applies it to motion-aligned tokens rather than raw samples, so the prediction target is a movement unit instead of a waveform patch. A third neighbor is Foundation Models for Biosignals: A Survey (Gu 2025) [2XWEG7AF], the anchor of your llm-health area, which frames the broader push toward general biosignal encoders that this paper advances on the accelerometer side.

---

## Tier B — TLDRs (~10 min)

### Wavelet-Driven Masked Multiscale Reconstruction for PPG Foundation Models (MMR)
arXiv:2601.12215 — https://arxiv.org/abs/2601.12215 — Thukral et al. (Samsung Research America, Georgia Tech), January 2026.

Most photoplethysmography (PPG) foundation models work in the time domain or bolt on a fixed-window Fourier view, which does not match the multi-scale nature of PPG: beat-level morphology lives at fine scales while heart-rate variability and rhythm live at coarse scales. MMR decomposes each PPG segment with a discrete wavelet transform and pretrains a Transformer to reconstruct randomly masked wavelet coefficients across scales, forcing the encoder to combine information from several time-frequency bands. Pretrained on about 17 million 10-second segments from roughly 32,000 smartwatch users, it matches or beats state-of-the-art open PPG and time-series foundation models on 17 of 19 downstream health tasks, with ablations on wavelet family, decomposition depth, and patch size.

How this builds on what you know: The closest parent is Foundation Models for Biosignals: A Survey (Gu 2025) [2XWEG7AF], the anchor of your llm-health area; where the survey maps the general goal of transferable biosignal encoders, MMR supplies a concrete pretraining objective for PPG, because it argues the missing piece is explicit multi-scale time-frequency structure. It also extends How Mask Matters: Masked Autoencoders Theory (Zhang 2023) [6INGKIJV] by moving the masking target from raw signal to wavelet coefficients, and it sits next to HeAR: Health Acoustic Representations (Baur 2024) [3LA8GNCU] in your Health AI and Self-Supervised community, which made a similar bet that spectral structure carries health-relevant features.

### Hierarchical Control in Multi-Agent Games: LLM-based Planning and RL Execution
arXiv:2606.20014 — https://arxiv.org/abs/2606.20014 — Hösch, Sestini, Fuchs, Baghi, Bergdahl, Tollmar, Barrette-LaPierre, Gisslén (EA, KTH), 18 June 2026.

Reinforcement learning struggles in multi-agent settings with sparse rewards and large state-action spaces. The paper splits the problem by level: a pretrained LLM acts as a central strategic controller that picks among pretrained RL skill policies, while the RL policies handle low-level reactive control. In a competitive 2v2 King of the Hill game, the LLM-plus-RL system reaches a win rate statistically equal to a hand-built behavior tree (46.4 percent versus 51.5 percent, p = 0.103) and both clearly beat flat RL trained without skill decomposition. A small user study (n = 15) found 60 percent of participants rated the LLM-plus-RL agents as the most human-like (p = 0.027). The takeaway is that LLM reasoning can orchestrate pretrained RL skills without hand-written rules.

How this builds on what you know: This work joins two communities in your library. On the agent side, the parents are Agent AI: Surveying Multimodal Interaction (Durante 2024) [Z9WZPMNU] and LATS: Language Agent Tree Search (Zhou 2024) [77ERE7HA]; where LATS used an LLM to search over its own action steps, this paper uses the LLM to select among learned RL skills instead, because the low-level control is delegated to policies rather than to token-level planning. On the RL side it builds on Offline Reinforcement Learning (Levine 2020) [ZULLM3UF], the anchor of your world-model-rl area. It also follows the planning-decomposition bridge in your graph (ADaPT to LATS): the new work pushes that bridge further by pairing symbolic planning with learned motor skills rather than with more planning.

### When Is Compositional Reasoning Learnable from Verifiable Rewards?
arXiv:2602.07992 — https://arxiv.org/abs/2602.07992 — Barzilai, Wolf, Basri (Weizmann Institute), February 2026.

Reinforcement learning with verifiable rewards (RLVR) trains a model using only a check on the final answer, yet it has driven much of the recent gain in step-by-step reasoning. This paper asks, in theory, which compositional problems RLVR can actually learn from outcome-only feedback. It defines a "task-advantage ratio", a joint property of the problem and the base model, and shows that problems where correct intermediate steps clearly raise the chance of a verified answer are efficiently learnable, while problems without that structural advantage can drive RLVR to a suboptimal solution. In some cases the base model's quality alone decides whether the advantage exists. The result gives a principled account of when RLVR succeeds and when it does not.

How this builds on what you know: The parents are Chain-of-Thought Prompting (Wei 2023) [HBLPTRMY] and DeepSeek-R1: Reasoning via RL (2025) [Z5IWHZAE], both in your LLM Agents and Reasoning community. Where DeepSeek-R1 showed empirically that RL with a verifier can grow reasoning, this paper supplies the missing theory for when that works, because it isolates the structural property a task must have for outcome-only feedback to reinforce correct intermediate steps. It extends the reasoning-via-RL versus prompting bridge already in your library (DeepSeek-R1 to Chain-of-Thought) by giving a formal condition that separates the two regimes.

---

## Tier C — scan (~5 min)

- Biosignal Fingerprinting: A Cross-Modal PPG-ECG Foundation Model — learns a shared PPG-ECG space so one modality can stand in for the other. https://arxiv.org/abs/2605.09579
- AnyPPG: An ECG-Guided PPG Foundation Model (100K+ hours) — uses ECG as a teacher signal to pretrain a PPG encoder for broad health profiling. https://arxiv.org/abs/2511.01747
- Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables — models derived behavioral features, not raw signal, and improves health prediction. https://arxiv.org/abs/2507.00191
- ECG Foundation Models and Medical LLMs for Agentic Cardiovascular Intelligence at the Edge — review of pairing ECG encoders with LLM agents on-device. https://arxiv.org/abs/2604.02501
- Reinforcing Chain-of-Thought Reasoning with Self-Evolving Rubrics — replaces a fixed verifier with rubrics that update during RLVR training. https://arxiv.org/abs/2602.10885
- Beyond Language Modeling: An Exploration of Multimodal Pretraining — shows mixture-of-experts models learn a separate-then-integrate split between text and vision across depth. https://arxiv.org/abs/2603.03276
- Verifiable Reasoning for LLM-based Generative Recommendation — applies verifier-checked reasoning chains to recommendation rather than math. https://arxiv.org/abs/2603.07725
- Geometry-Aware Representation Denoising for Robust Multi-view 3D Reconstruction — denoises learned features using 3D geometry priors for sturdier reconstruction. https://arxiv.org/abs/2605.26230

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off today). Bio-PM (Tier A) imports the masked-autoencoder objective from vision and the "meaningful token" lesson from language modeling into wrist-IMU sensing; that move is now demonstrated, so plain "apply masked reconstruction to accelerometer windows" is no longer open ground. MMR (Tier B) imports wavelet multi-resolution analysis and cross-scale masked reconstruction into PPG; "add a fixed Fourier branch to a PPG encoder" is likewise closed. Both land in your Community 1 (Health AI and Self-Supervised) and Community 5 (Wearable Sensing) regions.

Unported opportunity. The compositional-RLVR learnability result (Tier B) is a reasoning-side theory with no time-series counterpart yet. Transfer hypothesis: define a "task-advantage ratio" for time-series reasoning agents (for example TS-Agent in your library), where intermediate operator calls play the role of intermediate reasoning steps, and test whether outcome-only rewards can train an agent to choose the right analysis operators. No wearable or forecasting paper has framed tool selection as an RLVR learnability question, so this is open. A second opportunity: the separate-then-integrate finding in multimodal MoE (Tier C) has not been tested on mixed biosignal-plus-text models, where one might expect early layers to split signal-specific from language experts.

---

## News (model and product releases)

- Anthropic released Claude Fable 5 on 9 June 2026; Claude Opus 4.8 currently holds the top overall spot on the Artificial Analysis leaderboard.
- OpenAI moved ChatGPT users from GPT-5.2 to GPT-5.5 as of 12 June 2026, and existing conversations continue on the matching GPT-5.5 model.
- Google's Gemini 3.1 Pro is being cited as a benchmark leader in the latest comparisons.

---

Quiet day for brand-new June 22 listings, so Tier A is a recent paper in your primary area rather than a same-day release. If you have spare time, the previous-week backlog item worth a look is the Causal Semantic Alignment paper (CVAformer, 2606.08262) from the 21 June digest.

End of digest. Close this tab when done.
