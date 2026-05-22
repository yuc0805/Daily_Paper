# AI Digest — 2026-05-22

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Introspective X Training: Feedback Conditioning Improves Scaling Across All LLM Training Stages
Cui, Lu, Jung, Akter, Kim, Qu, Acuna, Prabhumoye, Choi, Ammanabrolu — arXiv:2605.20285 — 2026-05-19

**Problem.** Current LLM training pipelines consist of multiple stages (pretraining, supervised fine-tuning, RLHF), and each stage is optimized in isolation. The quality-aware signals that emerge during post-training — such as reward model scores and critique feedback — are never used to inform earlier stages. This means pretraining treats all tokens as equally valuable for billions of gradient steps before any quality signal is introduced, wasting compute on low-value data.

**Method.** Introspective Training (IXT) takes inspiration from offline reward-conditioned reinforcement learning. A thinking reward model annotates pretraining data with natural language critique-based feedback. The model is then trained by prefix-conditioning each data sample with the generated feedback, so that quality-aware token weighting begins at the earliest stage of training rather than being deferred to post-training. This approach is applicable to any stage of the pipeline — pretraining, SFT, or RL — making it a unified intervention across the full training stack.

**Result.** Comprehensive experiments on 7.5B and 12B dense transformer LLMs trained from scratch on up to 18 trillion tokens show that IXT bends the scaling curve, yielding up to 2.8x more compute efficiency in general and reaching performance levels on math and code that are unachievable by models trained without feedback conditioning, regardless of how much additional compute they receive.

**Limitations.** The paper evaluates only dense transformers at 7.5-12B scale. It is unknown whether IXT scales to MoE architectures or to the 70B+ regime. The reward model used for annotation adds a nontrivial cost to the data preprocessing pipeline, and the paper does not fully account for this overhead in the efficiency claims. There is also a risk that biases in the thinking reward model propagate into pretraining representations.

**Why it matters to Leo.** If you ever pretrain or continue-pretraining a domain-specific model (e.g., a time-series or biosignal foundation model), the idea of conditioning pretraining on quality feedback from a domain reward model is directly applicable. Rather than pretraining on all sensor data equally and hoping post-training fixes quality issues, you could annotate your pretraining corpus with signal quality scores from the start. The 2.8x efficiency gain is substantial — for compute-constrained academic labs, this could make the difference between a viable and an unviable pretraining run.

**How this builds on what you know:** IXT connects your Community 0 (LLM Agents & Reasoning) and Community 2 (Transformer & SSM Architectures). The reward-conditioned training idea extends DeepSeek-R1 (2025), which showed that RL can unlock reasoning in LLMs; IXT pushes the insight one stage earlier, arguing that reward signals should shape representations from pretraining, not just from the RL phase. The feedback-conditioning mechanism is conceptually related to Chain-of-Thought Prompting (Wei 2023), but where CoT adds reasoning traces at inference time, IXT adds critique-based feedback at training time. The Transformer architecture (Vaswani 2017) is the backbone being made more sample-efficient here, and the scaling analysis directly extends the compute-optimal scaling tradition.

---

## Tier B — TLDRs

### 1. Nexus: An Agentic Framework for Time Series Forecasting
Das, Goyal, Parmar, Peng, Tirumalashetty, Li, Zhang, Yoon, Pfister — arXiv:2605.14389 — 2026-05-14

Nexus decomposes time series forecasting into a multi-agent pipeline: separate stages isolate macro-level trends, micro-level fluctuations, and contextual information (news, events) before synthesizing a final forecast. The key finding is that LLMs have substantially stronger intrinsic forecasting ability than previously recognized, but this ability depends on how numerical and contextual reasoning are organized. Evaluated on post-cutoff data (Zillow real estate, stock equities), Nexus matches or beats state-of-the-art TSFMs and LLM baselines while producing interpretable reasoning traces that explain the drivers behind each forecast.

**How this builds on what you know:** Nexus extends your Community 4 (Time Series + LLM Integration) in a new direction. Where TS-Agent (Liu 2025) uses an LLM as a controller that selects among statistical tools, Nexus uses the LLM itself as the forecaster, decomposed into specialized reasoning stages. Where ChatTS (Xie 2025) fine-tunes a single LLM to align time series tokens with language, Nexus uses multiple agents with no fine-tuning, relying entirely on prompt-based decomposition. The multi-agent design also connects to your Community 0 agents: it mirrors the task decomposition approach of ADaPT (Prasad 2023) but applies it to forecasting rather than general planning. This paper extends the cross-area bridge between TS-Agent (Community 4) and the agent architectures (Community 0) by showing that agentic decomposition improves forecasting quality.

### 2. Resolving Action Bottleneck: Agentic RL Informed by Token-Level Energy
He et al. — arXiv:2605.14558 — 2026-05-14

Agentic RL trains LLMs on multi-turn trajectories that interleave long reasoning traces with short environment-facing actions. This paper shows that standard policy-gradient methods (PPO, GRPO) treat every token equally, but from an energy-based modeling perspective, the training signal concentrates sharply on action tokens, which are a tiny fraction of the trajectory. This mismatch — the "action bottleneck" — means most gradient updates are wasted on reasoning tokens that carry little learning signal. The proposed ActFocus method downweights gradients on reasoning tokens, yielding success-rate improvements of up to 65.2 and 63.7 percentage points over PPO and GRPO respectively.

**How this builds on what you know:** This paper directly extends DeepSeek-R1 (2025) in your library, which demonstrated RL for LLM reasoning but used uniform token-level credit assignment. ActFocus diagnoses a specific failure mode of that approach. The energy-based analysis also connects to the broader RL tradition in your Community 7 (Reinforcement Learning), though it is applied to language agents rather than continuous control. For your agent papers in Community 0, the implication is practical: if you train an agent with RL on tool-use trajectories (like ToolkenGPT, Hao 2024), action tokens deserve disproportionate gradient weight.

### 3. AudioMosaic: Contrastive Masked Audio Representation Learning
Huang, Wang, Ma, Xie, Leckie, Erfani — arXiv:2605.14231 — 2026-05-14

AudioMosaic revives contrastive learning for audio self-supervised pretraining, which has been overshadowed by generative reconstruction objectives (masked autoencoders, etc.). It constructs positive pairs by applying structured time-frequency masking to spectrogram patches, reducing memory usage and enabling large-batch contrastive training. The learned encoder produces more discriminative utterance-level representations than generative approaches, with state-of-the-art on multiple audio benchmarks under both linear probing and fine-tuning. Integrating the pretrained encoder into audio-language models also improves audio-language task performance.

**How this builds on what you know:** AudioMosaic sits in your Community 2 (Transformer & SSM Architectures) and connects to Community 1 (Health AI & Self-Supervised). Where Audio Mamba (Erol 2024) applied Mamba/SSM architectures to audio, AudioMosaic stays with the Transformer but focuses on the pretraining objective rather than the architecture. The contrastive-plus-masking strategy is closely related to how your SSL for HAR (Yuan 2024) combines masked reconstruction with contrastive learning for wearable sensor data. The key difference is that AudioMosaic uses masking to construct contrastive pairs (mask as augmentation), whereas Yuan 2024 uses masking as a reconstruction target. This alternative design could transfer to biosignal pretraining.

---

## Tier C — Scan Headlines

1. **DECO: Sparse MoE with Dense-Comparable Performance** (2605.10933) — ReLU routing with learnable expert scaling; 20% expert activation matches dense quality with 3x inference speedup. [arXiv](https://arxiv.org/abs/2605.10933)

2. **EnvFactory: Scaling Tool-Use Agents via Executable Environments** (2605.18703) — Synthesizes executable tool environments and multi-turn training trajectories from authentic resources; +15% on BFCLv3. [arXiv](https://arxiv.org/abs/2605.18703)

3. **Fast MoE Inference via Predictive Prefetching** (2605.11537) — Expert replication and predictive prefetching achieve near 100% GPU utilization, up to 3x MoE inference speedup. [arXiv](https://arxiv.org/abs/2605.11537)

4. **Interpretability Can Be Actionable** (2605.11161) — Position paper arguing interpretability research should be evaluated by whether insights enable concrete interventions. [arXiv](https://arxiv.org/abs/2605.11161)

5. **Unified Pix Token And Word Token Generative Language Model** (2605.14028) — Unifies pixel and word tokens in a single generative LM to fix detail recognition failures. [arXiv](https://arxiv.org/abs/2605.14028)

6. **Escaping Mode Collapse in LLM Generation via Geometric Regulation** (ICML 2026) — Geometric regularization prevents diversity collapse during LLM generation. [arXiv](https://arxiv.org/abs/2605.xxxxx)

7. **Hi-MoE: Hierarchical MoE with Two-Stage Optimization** (2605.08292) — Grouped routing with inter-group balancing and intra-group specialization. [arXiv](https://arxiv.org/abs/2605.08292)

8. **ProDG: Data-Free Generative Post-Hoc Explainability** (2605.08858) — Synthesizes prototypes from frozen model weights for explainability without data access. [arXiv](https://arxiv.org/abs/2605.08858)

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**
Agentic decomposition for time series forecasting (Nexus, 2605.14389) applies the multi-agent task decomposition paradigm from LLM agents to forecasting. This transfer from general agent architectures to time series is now done.

Contrastive-plus-masking for audio (AudioMosaic, 2605.14231) applies structured masking as a contrastive augmentation strategy for spectrograms. A similar idea has already been explored for wearable sensor data by Yuan 2024 (SSL for HAR), though the specific "masking as augmentation" variant is distinct.

**Unported opportunity:**
IXT's feedback-conditioned pretraining (2605.20285) has a direct transfer hypothesis for biosignal foundation models. Current sensor/biosignal pretraining treats all data segments equally. A domain-specific reward model — e.g., one that scores signal quality, artifact contamination, or clinical relevance — could be used to prefix-condition biosignal pretraining data, letting the model learn more from high-quality segments from the start. No one has applied reward-conditioned pretraining to physiological time series data.

The ActFocus token reweighting idea (2605.14558) could also transfer to time-series agent training. If you train an agent to interact with time-series data (like TS-Agent), the action tokens (tool calls, parameter selections) are a tiny fraction of the trajectory but carry most of the learning signal. Applying energy-based token reweighting to TS agent training could substantially improve sample efficiency.

---

## News

1. **NVIDIA open model release** (May 21): NVIDIA launched Nemotron 3 Nano Omni, a multimodal model unifying vision, audio, and language for on-device AI agents, alongside new open data and tools for AI across industries.

2. **Anthropic Claude Mythos Preview**: Anthropic is testing Claude Mythos via Project Glasswing with select organizations. The model shows strong improvements in math, long-context reasoning, software engineering, and cybersecurity. It is not publicly available.

3. **Meta AI capex**: Meta announced $115-135B in AI capital expenditures for 2026, nearly double the previous year, signaling aggressive infrastructure investment.

---

End of digest. Close this tab when done.
