# AI Digest — 2026-08-02

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on the day: this is a Sunday, so the flow of genuinely new papers is thin. The clearest fresh signal sits in your primary area (time-series and bio-sensing), so Tier A is a wearable heart-rate-variability forecasting paper. The three Tier B papers cover one more bio-signal foundation model, one reasoning-agent training method, and one embodied vision-language benchmark.

---

## Tier A — deep read

### Zero-Shot Heart Rate Variability Forecasting from Consumer Wearables Using Time Series Foundation Models
Peräkylä, Sohrab, Hautamäki, Heinäniemi, Huang, Abrahamsson. arXiv:2607.20027 (22 Jul 2026, accepted to Computing in Cardiology 2026). https://arxiv.org/abs/2607.20027

**Problem.** Short-term heart-rate-variability (HRV) forecasting could give clinicians lead time to catch autonomic dysfunction and adverse cardiac events. The obstacle is that consumer wearables produce HRV signals that are fragmented and full of artifacts, which breaks conventional forecasting methods that assume clean, evenly sampled input.

**Method.** The authors take three time-series foundation models off the shelf — TimesFM, Chronos, and MOIRAI — and test them without any fine-tuning against classical baselines (mean, exponential smoothing, exponentially weighted moving average) on real wearable data from 49 healthy people. To handle the gaps left by artifact removal, they add a variability-preserving imputation step: linear interpolation plus locally adaptive stochastic noise, so the filled-in segments keep the short-term variability that HRV forecasting depends on rather than flattening it.

**Result.** The foundation models beat every baseline with no fine-tuning. Average Mean Absolute Scaled Error sits between 0.81 and 0.87 across the models and both context lengths (32 and 64 steps, where 32 steps is about 2.7 hours of history), with Chronos and TimesFM the strongest and MOIRAI barely ahead of the baselines. Forecast horizon reaches up to 2 hours. A MASE below 1 means the model beats a naive one-step forecast, so the zero-shot result is a real gain, not a tie.

**Limitations.** Only 49 participants, all healthy, so the harder clinical population (where autonomic dysfunction actually shows up) is untested. The imputation adds synthetic variability, which could bias forecasts on longer gaps. The authors themselves frame the numbers as a baseline and point to domain-specific fine-tuning as the next step, meaning the zero-shot result is a floor, not a ceiling.

**Why it matters to Leo.** This is a clean, small, directly relevant data point for your primary area: it quantifies how far generic time-series foundation models get on messy wearable physiological signals with no adaptation, and it isolates data fragmentation (not model capacity) as the thing to engineer around. The variability-preserving imputation trick is reusable for any wearable pipeline that has to survive artifact removal.

**How this builds on what you know:** The three forecasters are anchor points already in your library. Where **Chronos** (Ansari 2024, 72DFULQQ) and **MOIRAI** (Woo 2024, CFG6FEIF) established general pretrained time-series foundation models for zero-shot forecasting on broad, mostly clean benchmarks, this paper does the narrower thing of running them on fragmented consumer-wearable HRV and shows they still hold up, because the variability-preserving imputation keeps the input inside the distribution the models expect. Where **TS-Agent** (Liu 2025, I2CIT4I7, graphify Community 4: Time Series + LLM Integration) treats time-series understanding as an LLM-style reasoning problem, this paper stays with pure forecasting and asks only whether the pretrained forecaster generalizes to a new signal type. The paper also sits next to the bio-sensing side of your library: the biosignal foundation-model survey by **Gu 2025** (2XWEG7AF, Community 1) catalogs exactly this kind of transfer question, and HRV forecasting is one more entry in the Community 4 / Community 5 (Wearable Sensing) overlap.

---

## Tier B — TLDRs

### MorphologyFM: A Foundation Model for Morphology-Aware Representation Learning from ECG and Pulse Oximetry Waveforms
arXiv:2607.09749 (Jul 2026). https://arxiv.org/abs/2607.09749

MorphologyFM is a multimodal foundation model pretrained on paired ECG and SpO2 (pulse oximetry) waveforms from the MIMIC critical-care database. The stated problem is that most physiological-waveform models optimize plain reconstruction or forecasting, which does not preserve the waveform shape — intervals, slopes, beat-to-beat structure — that carries the clinical signal. The method combines morphology-guided masking, cross-modal representation learning between the two waveform types, and contrastive latent alignment, all self-supervised, so no manual labels are needed. The result is a representation meant to transfer to downstream cardiovascular and hemodynamic tasks while keeping morphological structure intact.

**How this builds on what you know:** Where the masked-autoencoder line in your library — the MAE theory paper by **Zhang 2023** (6INGKIJV, graphify Community 1) and **He 2021** (A5HBRQB9) — masks random patches and rewards pixel or value reconstruction, MorphologyFM masks with morphology in mind and adds a contrastive objective, because for waveforms the diagnostic content is in shape, not average level, so plain reconstruction can score well while discarding the clinically useful part. It also extends the biosignal foundation-model program surveyed by **Gu 2025** (2XWEG7AF, Community 1) from single-signal pretraining toward paired cross-modal (ECG plus SpO2) pretraining. This is the same Community 1 (Health AI and Self-Supervised) neighborhood as the SensorFM wearable model (2605.22759) already in your library.

### CAST: Game Solvers as Turn-Level Teachers for LLM Agents
arXiv:2607.25308 (28 Jul 2026). https://arxiv.org/abs/2607.25308

CAST addresses a known weakness in training LLM agents for long-horizon games with reinforcement learning from verifiable rewards (RLVR): the reward arrives only at the end, so the model gets almost no signal about which individual turns actually mattered. The idea is that a game solver's state-value estimate already encodes this — when the solver's value goes up after an action, that action moved the state toward success. CAST (Credit Assignment from Solver Teachers) converts these value changes into per-turn "solver advantages" and injects them into RLVR as dense turn-level feedback. The authors show that, under a soft-optimal solver assumption, maximizing the solver advantage is equivalent to on-policy distillation from the solver, needing only scalar values rather than the teacher's full logits, which keeps the signal cheap.

**How this builds on what you know:** Where **DeepSeek-R1** (Z5IWHZAE, graphify Community 0, reasoning-via-RL) trains with sparse final verifiable rewards, CAST keeps the RLVR frame but adds a dense per-turn credit term, because sparse terminal reward is the exact thing that makes long-horizon credit assignment hard. Where **LATS** (Zhou 2024, 77ERE7HA, Community 0) uses a value estimate at search time to steer tree rollouts, CAST uses a solver's value changes at training time to shape the gradient. This extends the graphify cross-area bridge deepseek2025_r1 → **Chain-of-Thought** (Wei 2023, HBLPTRMY), which already crossed reasoning-via-RL and reasoning-via-prompting in your library; CAST pushes that bridge further toward process-level supervision of the reasoning trace rather than outcome-only supervision.

### HumanCLAW: Can Vision-Language Models Act Through a Body?
Li, Gu, Liu, Hu, et al. (Meta Research). arXiv:2607.27180 (29 Jul 2026). https://arxiv.org/abs/2607.27180

HumanCLAW is an evaluation framework that separates a vision-language model's action decisions from low-level motor control. At each step a harnessed off-the-shelf VLM issues an atomic skill command, which is turned into a sub-second chunk of continuous full-body motion with real physics (gravity, collisions). Because balance and motor errors are factored out, what remains measurable is the model's "action intelligence": its moment-to-moment choice of what the body should do next. The benchmark, HumanCLAW-Bench, has 1,218 long-horizon egocentric find-navigate-interact episodes across 41 indoor scenes. Testing nine state-of-the-art VLMs, none solves it; the best reaches only 16.8% success. The failure is not recognition — the models see the target — but embodied self-awareness: they lose track of where their own body is, whether it reached the goal, or whether it hit an obstacle.

**How this builds on what you know:** Where **Flamingo** (Alayrac 2022, SC8KWYVK, in your multi-modal and NLP areas) benchmarks a VLM on passive image and video question answering, HumanCLAW puts the same class of model in a control loop and measures whether its choices move a physical body toward a goal, because passive perception scores say nothing about whether the model can act on what it sees. It also gives the **Agent AI** survey by **Durante 2024** (Z9WZPMNU, graphify Community 0) a concrete, physics-grounded benchmark for the multimodal-interaction agenda that the survey described in the abstract. Closest neighbors in your library are the vision-language nodes in graphify Community 3 (Vision-Language and Generative).

---

## Tier C — scan

- HumanCLAW is promoted to Tier B above; the rest of the day's agent-and-eval cluster follows here.
- SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution — trains agents to grow a reusable skill set across tasks rather than per-task. arXiv:2607.26784
- CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization (ByteDance) — token-level rubric rewards with counterfactual replay to sharpen credit. arXiv:2607.25659
- DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills (Qwen) — separates solver learning from rubric auditing to block reward hacking. arXiv:2607.25675
- OmegaUse-OfficeVal: Benchmarking LLM Agents on Long-Horizon Office-Suite Tasks with Economic Grounding — measures agents on realistic multi-step office work. arXiv:2607.27155
- CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition — probes in-context learning in multimodal models. arXiv:2607.25294
- Can AI Agents Conduct Open-Ended AI Research? Early Evidence from Two Case Studies — two case studies on agents running their own research loops. arXiv:2607.27191
- TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with under 1 GB VRAM — pushes VLA policies toward commodity real-time control (featured 30 Jul). arXiv:2607.27205
- GPT-Red: Automated Red Teaming via Self-Play at Scale (OpenAI) — scales adversarial testing of models through self-play. arXiv:2607.26115

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

Already ported (closed off): today's bio-signal work maps onto known graphify communities. The HRV forecasting paper (Tier A) applies pretrained time-series foundation models to a wearable physiological signal — this is Community 4 (Time Series + LLM Integration) territory, so "generic TSFM, zero-shot, on a new signal type" is now a filled cell. MorphologyFM applies masked-autoencoder and contrastive self-supervision to ECG and SpO2 waveforms — this is Community 1 (Health AI and Self-Supervised) territory, so "MAE / contrastive SSL on physiological waveforms" is also filled. Neither imports a method that was not already in your library's transfer map.

Unported opportunity 1: diffusion transformers for morphology-conditioned physiological-signal synthesis. The DiT architecture (Peebles 2023, YJ9TK993, Community 3) is the standard generative-CV backbone, but it has not been applied to generate ECG or SpO2 waveforms conditioned on the exact morphology features MorphologyFM learns. Transfer hypothesis: train a 1-D DiT to synthesize waveform segments conditioned on MorphologyFM embeddings, giving controllable, morphology-faithful synthetic training data for rare arrhythmia classes.

Unported opportunity 2: solver-teacher turn-level credit for clinical time-series decision-making. CAST's idea of turning a solver's value changes into dense per-turn credit (Community 0) has not been applied to sequential clinical monitoring, where a physiological "solver" (e.g., an early-warning score) could supply per-timestep credit. Transfer hypothesis: use a validated deterioration score as the solver and train a monitoring agent with CAST-style per-timestep advantages, so the agent learns which observations drive risk rather than only predicting the final event.

---

## News — model releases

DeepSeek released DeepSeek-V4-Flash-0731 on 31 Jul 2026, a fast, low-cost variant in the V4 line. Anthropic released Claude Opus 5 on 24 Jul 2026. Google released Gemini 3.6 Flash on 21 Jul 2026. No major model or product launch appears dated 1-2 Aug 2026 as of this run.

---

End of digest. Close this tab when done.
