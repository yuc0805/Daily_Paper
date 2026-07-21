# AI Digest — 2026-07-21

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### SensorFM: A Wearable Health Foundation Model Pretrained on One Trillion Minutes of Sensor Data (Google Research, arXiv 2605.22759)

**Problem.** Wearable health models are usually built one task at a time. A team collects a labeled dataset for sleep staging, or step counting, or stress, and trains a bespoke model for each. This does not reuse structure across tasks, does not handle missing sensor windows well, and does not give a single representation that downstream health tools can call. The paper asks whether one self-supervised model, trained on raw multi-sensor streams at population scale, can replace those bespoke models across a wide task set.

**Method.** SensorFM ingests 34 one-minute aggregate features drawn from five sensors: photoplethysmography (PPG), accelerometer, electrodermal activity (EDA), skin temperature, and altimeter. It is pretrained by masked reconstruction on more than one trillion minutes of sensor data from about 5 million people, then evaluated by attaching light task heads. The design follows the masked-autoencoder recipe: hide part of the input, reconstruct it, and use the learned encoder as a general feature extractor.

**Result.** The largest variant, SensorFM-B, beat commonly used conventional baselines on 34 of 35 prediction tasks. It cut reconstruction error by 31% versus the smallest variant, lifted downstream classification by an average of 9% in AUC, and lifted regression by an average of 21% in Pearson correlation. Robustness to missing data is strong: with 60 contiguous minutes ablated, it retained 99.7% step-count accuracy and 99.9% deep-sleep accuracy. When wired into a health agent, four board-certified physicians, blinded to condition, rated 1,860 outputs across context, relevance, justifiability, personalization, and potential for harm; adding SensorFM predictions beat the baseline overall, and the predictions were statistically indistinguishable from ground truth.

**Limitations.** The model consumes one-minute aggregate features, not raw waveforms, so fine-grained morphology (for example beat-level PPG shape) is discarded before the encoder ever sees it. The evaluation is largely internal to Google's sensor stack and population, so transfer to other devices and to clinical-grade signals is not established. The physician study rates agent outputs, not raw model calibration, so the "indistinguishable from ground truth" claim is about a downstream pipeline rather than the encoder alone.

**Why it matters to Leo.** This is the current high-water mark for the exact area you work in: a single self-supervised model over multi-sensor wearable time series, at a scale no academic group can match. It sets the baseline any new wearable-representation method now has to beat, and it makes the design choice (aggregate features vs raw waveform) an open target — a raw-waveform version is an obvious next paper.

**How this builds on what you know:** SensorFM sits in your library's Community 1 (Health AI and Self-Supervised). Its closest parents are SSL for HAR (Yuan 2024), which showed self-supervised pretraining on 700K person-days of accelerometer data works for activity recognition; Foundation Models for Biosignals (Gu 2025), which surveyed the design space this model fills in; and HeAR (Baur 2024), a self-supervised acoustic health representation. Where Yuan 2024 pretrained on one sensor family (accelerometer) at 700K person-days, SensorFM does the same masked-prediction idea across five sensor families at roughly a thousand times more data, because the open question those parents left was whether one encoder could fuse heterogeneous sensors rather than model each alone. It also touches Community 5 through GLOBEM (Xu 2023): where GLOBEM gave multi-year multi-sensor behavior datasets and showed generalization across years is hard, SensorFM supplies the pretrained representation that such cross-year behavior tasks were missing.

---

## Tier B — TLDR

### HEARTS: Benchmarking LLM Reasoning on Health Time Series (arXiv 2603.06638, ICML 2026)

HEARTS is a benchmark for reasoning over health time series, not a new model. It integrates 16 real-world datasets across 12 health domains and 20 signal modalities, and defines 110 tasks grouped into four capabilities: perception, inference, generation, and deduction. Evaluating 16 state-of-the-art LLMs on more than 20K test samples, the authors find that LLMs substantially underperform specialized models, lean on simple heuristics, and fail at multi-step temporal reasoning. Performance drops as sequences get longer and sampling frequency rises, and the difficulty ordering across domains is consistent no matter whether the series is fed as text, image, or raw file. The takeaway is that scaling alone does not close the gap on health-signal reasoning.

**How this builds on what you know:** HEARTS sits between your Community 4 (Time Series + LLM Integration) and Community 5 (wearable sensing). Its parents in your library are TS-Agent (Liu 2025) and ChatTS (Xie 2025), which both built LLM systems that reason over or align with time series, and LLMs are Few-Shot Health Learners (Liu 2023), which first showed general LLMs can read health signals with few examples. Where TS-Agent and ChatTS proposed methods and reported wins on their own task sets, HEARTS builds the shared, adversarial testbed that measures where those methods actually break, because the field had claims of LLM time-series reasoning without a common yardstick. It also extends the LLMs for Time Series survey (Zhang 2024) from a map of methods into a measurable failure taxonomy.

### Group Entropy-Controlled Policy Optimization (GEPO) (InternLM, arXiv 2607.16850)

GEPO is a lightweight change to GRPO, the group-relative policy optimization used in reasoning RL. The observation is that RL fine-tuning runs on mixtures of tasks that live in different entropy regimes under the same policy, so one global or token-level entropy control cannot serve all of them, and GRPO's normalized advantages pick up an entropy-dependent bias that makes advantage signals across prompt groups not comparable. GEPO estimates per-group entropy from the samples already drawn and shapes advantages asymmetrically: it damps positive advantages in low-entropy groups to stop over-exploitation, and damps negative advantages in high-entropy groups to keep exploration alive. The cost is small because the entropy estimate reuses existing grouped rollouts.

**How this builds on what you know:** GEPO sits in Community 0 (LLM Agents and Reasoning). Its direct parent in your library is DeepSeek-R1 (2025), which made GRPO-style reward RL the standard recipe for eliciting reasoning, with DeepSeek-V3 (2024) as the base-model lineage behind it. Where DeepSeek-R1 applied one reward-normalization scheme uniformly across all prompts, GEPO conditions the advantage shaping on each group's entropy, because a single normalization treats an easy low-entropy prompt and a hard high-entropy prompt as if they need the same exploration pressure. This is the same "one reward is too blunt" critique that role-aware GRPO variants you have already read raise, applied here to entropy rather than to perception-versus-reasoning roles.

### Environment-free Synthetic Data Generation for API-Calling Agents (Apple, arXiv 2607.16900)

Tool-calling agents are trained on trajectories that normally require a live, executable environment: real APIs to call, real state to observe, real errors to recover from. Standing up and maintaining that environment is the main bottleneck to scaling agent training data. This paper generates synthetic tool-call training data without a live environment, so the API surface and its responses are produced by the data pipeline itself rather than by executing real services. The result is a cheaper path to large, diverse API-calling datasets, which matters most for the long tail of tools that have no public sandbox.

**How this builds on what you know:** the paper sits in Community 0 (LLM Agents and Reasoning). Its parents in your library are ToolkenGPT (Hao 2024), which learned tool-call embeddings so an LLM can invoke tools, and ADaPT (Prasad 2023), which decomposed tasks as needed for planning agents, with the Agent AI survey (Durante 2024) as the framing. Where ToolkenGPT assumed tools you can actually call to gather supervision, this paper removes the live environment and synthesizes the call-and-response supervision directly, because the environment, not the model, is what does not scale.

---

## Tier C — scan

- EvolvingWorld: co-evolving role-play agents and a world model in an interactive literary world (Tencent). https://arxiv.org/abs/2607.17250
- HOMIE: human-object-centric video personalization via multimodal enhancement. https://arxiv.org/abs/2607.18217
- SWE-Pruner Pro: a coder LLM prunes its own context before solving (ByteDance). https://arxiv.org/abs/2607.18213
- Apple-Pi: a benchmark for law-grounded physical intelligence, testing thinking with video (MMLab@NTU). https://arxiv.org/abs/2607.16401
- ReflectWorld-MM: an entity-oriented multimodal memory system for open-ended video streams. https://arxiv.org/abs/2607.09759
- TimeLens2: generalist video temporal grounding with multimodal LLMs (Nanjing University). https://arxiv.org/abs/2607.17423
- RynnBrain 1.1: a more generalizable embodied foundation model (DAMO Academy). https://arxiv.org/abs/2607.17977
- Token-Level Off-Policy Learning for faithful generation under distribution shift (USC). https://arxiv.org/abs/2607.17524

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported (closed off).** SensorFM (Tier A) carries the masked-autoencoder self-supervision idea (Community 1) into large-scale multi-sensor wearables. Masked reconstruction on aggregate wearable features at population scale is now done and hard to beat without more data, so this is no longer low-hanging fruit. HEARTS (Tier B) similarly closes the "is there a shared benchmark for health-signal reasoning" gap.

**Unported opportunity 1 — entropy-conditioned RL for time-series reasoning agents.** GEPO's per-group entropy shaping (Tier B) has not been applied to time-series or bio-sensing reasoning. Transfer hypothesis: HEARTS shows health-signal reasoning tasks span very different difficulty and sequence-length regimes, which is exactly the heterogeneous-entropy setting GEPO targets; a TS-reasoning agent fine-tuned with group-entropy shaping could stay stable across short vitals and long overnight recordings where uniform GRPO collapses.

**Unported opportunity 2 — inference-time forward-process alignment for physiological generative models.** DiFA-style inference-time alignment of diffusion models (seen today in the generative stream) has not been applied to physiological signal generation. Transfer hypothesis: a diffusion model that synthesizes ECG or PPG could be steered at inference toward clinically valid morphology without retraining, using the same forward-process alignment idea, which would help the chronic scarcity of labeled abnormal-rhythm data.

---

## News

OpenAI made GPT-5.6 public mid-event after a customer-by-customer Commerce Department review. The flagship is Sol, with an Ultra subagent mode and a Max reasoning-effort setting; Terra targets GPT-5.5-level quality at about half the cost, and Luna is the fast tier. Separately, GPT-Live listens while it speaks and decides many times per second whether to talk, pause, interrupt, or call a tool, shipping as GPT-Live-1 and a free GPT-Live-1 mini.

Meta announced Muse Spark 1.1, a one-million-token-context agentic model that it reports rivals GPT-5.5 and Opus 4.8 on agentic evaluations, alongside Meta's first paid developer API in public preview and computer use across desktop, browser, and mobile.

Anthropic reported an interpretability result: a small internal subspace with about 25 active concepts that behaves like the "global workspace" from consciousness neuroscience. The associated J-lens tool is open-sourced with a Neuronpedia demo. This is a research finding, not a product claim.

---

End of digest. Close this tab when done.
