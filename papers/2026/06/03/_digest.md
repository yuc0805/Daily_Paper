# AI Research Digest — 2026-06-03

**Reading budget today:** 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

**Open-tab rule:** maximum 3 papers open at once. Close one before opening a fourth.

**Two-page test:** if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — Deep Read

### Time-R1: Time Series Forecasting as Reasoning (Zhou, Luo, Cheng et al.)
**arXiv:** [2506.10630](https://arxiv.org/abs/2506.10630) | cs.LG, cs.AI | v2 April 2026

**Problem.** Most time series forecasting methods follow a "fast thinking" paradigm — extract historical patterns and map them forward. There is no explicit intermediate reasoning about why a pattern should continue or change. Meanwhile, slow-thinking LLMs (DeepSeek-R1, OpenAI o1) demonstrate multi-step reasoning, but prompt engineering alone is too costly and domain-shallow for time series.

**Method.** Time-R1 is a two-stage reinforcement fine-tuning framework. Stage 1 performs supervised fine-tuning on curated time-series reasoning traces for warmup adaptation. Stage 2 applies reinforcement learning with two novelties: (a) a fine-grained multi-objective reward function designed specifically for time series forecasting (penalizing directional errors, magnitude errors, and temporal misalignment separately), and (b) GRIP (Group-based Relative Importance for Policy Optimization), which uses non-uniform sampling to weight exploration toward reasoning paths that produce better forecasts. GRIP extends standard GRPO by assigning higher sampling weight to trajectory groups with higher relative reward improvement.

**Result.** Time-R1 significantly improves forecast accuracy on diverse standard benchmarks versus both conventional TS models and prompted LLMs. The multi-objective reward outperforms single-metric MSE rewards, and GRIP outperforms vanilla GRPO in ablations.

**Limitations.** Evaluation is on standard TS forecasting benchmarks only (ETTh, Weather, etc.). No evaluation on biosignal or health time series. The reasoning traces generated in Stage 1 are synthesized — it is unclear how sensitive performance is to the quality of these traces. Computational cost of RL fine-tuning is not reported in detail.

**Why it matters to Leo.** This paper directly bridges DeepSeek-R1's reasoning-via-RL paradigm (Community 0 in the graphify graph) into the Time Series + LLM space (Community 4). It extends the cross-area bridge from deepseek2025_r1 toward time series. For Leo, the open question is whether Time-R1's GRIP and multi-objective reward can be applied to biosignal forecasting — for example, predicting cardiac anomalies from wearable PPG. The "slow thinking for time series" paradigm is freshly ported from NLP reasoning and has not been tried on health data, making it a direct transfer opportunity.

**How this builds on what you know:** Time-R1's intellectual parents are DeepSeek-R1 (Z5IWHZAE), which established RL-only reasoning in LLMs, and TS-Agent (I2CIT4I7), which demonstrated LLM reasoning over time series through tool-use. Where DeepSeek-R1 trained reasoning via RL on general tasks, Time-R1 specializes it for time series with a domain-specific reward. Where TS-Agent kept the LLM frozen and routed reasoning through external operators, Time-R1 fine-tunes the LLM weights directly. This paper also connects to ChatTS (VSCNJG5J) and the LLMs-for-TS survey (N2JLZBY3), which mapped out alignment approaches. Time-R1 takes a fundamentally different route: rather than aligning modalities, it trains reasoning into the model via RL.

---

## Tier B — TLDRs

### 1. CLAMP: Contrastive Self-Supervised Learning As Neural Manifold Packing (Zhang, Heeger, Martiniani)
**arXiv:** [2506.13717](https://arxiv.org/abs/2506.13717) | cs.LG, q-bio.NC | v2 Jan 2026

CLAMP reframes contrastive self-supervised learning as a manifold packing problem inspired by the physics of jammed particle systems. Instead of point-wise comparisons (as in SimCLR or BYOL), each image's augmented views form a sub-manifold, and a packing loss based on short-range repulsive potentials optimizes the sizes and positions of these manifolds in embedding space. Under standard linear evaluation, CLAMP matches state-of-the-art SSL methods, while providing interpretable dynamics that parallel jamming physics and geometrically meaningful hyperparameters.

**How this builds on what you know:** No direct parents in your library for this specific approach. The closest neighbor is SSL for HAR (yuan2024_ssl_har) in the self-supervised pretraining hyperedge (Community 1), which uses conventional contrastive pretraining on sensor data at scale. CLAMP's packing loss is a fundamentally different objective that could serve as a drop-in replacement in that pipeline. The physics-to-ML bridge is the novelty; the manifold packing loss has not been applied to sensor or wearable data yet.

### 2. TimeRecipe: Module-Level Benchmarking of TS Forecasting (arXiv: 2506.06482)

TimeRecipe runs over 10,000 experiments to decompose time-series forecasting architectures into individual modules — tokenization, normalization, attention type, feed-forward variant, output head — and measures which choices actually drive accuracy. The result is an empirical recipe: a ranked set of best-performing module combinations per task type. It finds that module-level decisions (especially tokenization and normalization) often matter more than the overall architecture family (Transformer vs. MLP vs. CNN).

**How this builds on what you know:** TimeRecipe directly benchmarks many architectures in your library — PatchTST (YY67LF3R), iTransformer (QBX2TI2X), TimesNet (HLTA8MDK), and others. Where each of those papers proposed a monolithic architecture, TimeRecipe disentangles the contributions. For building biosignal forecasting models, this provides a shortcut: adopt the winning modules rather than running a full architecture search.

### 3. Uncertainty-Driven Anomaly Detection for Psychotic Relapse Using Smartwatches (Tsalkitzis et al.)
**arXiv:** [2605.13816](https://arxiv.org/abs/2605.13816) | May 2026

Two smartwatch-based pipelines for daily psychotic relapse detection. Pipeline 1 forecasts cardiac dynamics and flags deviations as anomalies. Pipeline 2 fuses sleep, motion, and cardiac signals in a multi-task Transformer. Both produce a daily anomaly score from predictive uncertainty estimated via an MLP ensemble. The multi-task formulation improves over single-modality baselines, and the uncertainty-based scoring provides calibrated confidence — important for clinical deployment.

**How this builds on what you know:** The closest parents are GLOBEM (xu2023_globem, Community 5) for multi-year wearable behavioral datasets in mental health, and MindScape (nepal2024_mindscape, Community 5) for LLM + behavioral sensing. Where GLOBEM provided datasets and baselines, this paper proposes a concrete clinical scoring pipeline. Where MindScape used LLMs for reflective journaling, this paper stays at the signal level with Transformer encoders and ensemble uncertainty. It sits squarely in the Wearable Sensing and Behavior community (Community 5) of your graph.

---

## Tier C — Scan Headlines

1. **Self-Supervised CL is Approximately Supervised CL** — [2506.04411](https://arxiv.org/abs/2506.04411) — Theoretical proof: standard CL approximates supervised CL; gap vanishes as class count grows.
2. **ProQ: Offline Goal-Conditioned RL with Projective Quasimetric Planning** — [2506.18847](https://arxiv.org/abs/2506.18847) — Compositional quasimetric distance for long-horizon offline GCRL.
3. **LLMs for Mathematical Reasoning: Survey** — [2506.08446](https://arxiv.org/abs/2506.08446) — Comprehensive survey covering ORMs, PRMs, RRMs for math reasoning evaluation.
4. **Generalizing VLMs to Novel Domains: Survey** — [2506.18504](https://arxiv.org/abs/2506.18504) — Reviews domain generalization in vision-language models.
5. **MLLMs on Physics Visual Tasks** — [2506.19662](https://arxiv.org/abs/2506.19662) — Benchmarks 15 MLLMs from Anthropic/Google/OpenAI on 102 physics items; best is 81.5%.
6. **Speech FMs Generalize to Wearable TS** — [2509.00221](https://arxiv.org/abs/2509.00221) — HuBERT and wav2vec 2.0 features beat sensor-specific SSL on mood, arrhythmia, activity tasks.
7. **SPRINT: Parallel Reasoning for LRMs** — [2506.05745](https://arxiv.org/abs/2506.05745) — Reorganizes reasoning traces into parallel execution rounds; 39-65% fewer sequential tokens.

---

## Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off):**

Transformer encoders for wearable anomaly detection are well-established. The psychotic relapse paper (2605.13816) uses standard Transformer + ensemble uncertainty on cardiac/sleep/motion — no new architectural idea from CV/NLP, just solid application engineering. Similarly, the speech FM transfer to wearable TS (2509.00221) confirms that pretrained audio representations work for sensor tasks, a finding consistent with HARMamba and HeAR in your library.

**Unported opportunities:**

1. **Slow-thinking RL reasoning for biosignal forecasting (from Time-R1).** Time-R1's GRIP mechanism and multi-objective reward are designed for standard forecasting benchmarks. Applying this to biosignal anomaly prediction — where "reasoning" about why a cardiac pattern deviates from baseline could improve interpretability — is untested. Transfer hypothesis: replace Time-R1's generic TS reward with a clinically grounded reward (e.g., penalizing missed anomalies more than false alarms), and use slow-thinking to generate interpretable reasoning traces about biosignal deviations.

2. **Manifold packing loss for sensor SSL (from CLAMP).** CLAMP's physics-inspired repulsive packing loss has only been tested on vision benchmarks. Wearable activity recognition involves a smaller number of classes than ImageNet, which is precisely the regime where the gap between self-supervised and supervised CL is largest (per the theoretical result in 2506.04411). Transfer hypothesis: replace the contrastive loss in Yuan 2024's SSL-for-HAR pipeline with CLAMP's packing loss; the smaller class count in HAR may yield larger gains than in vision.

---

## News

1. **Microsoft MAI-Thinking-1** — Microsoft's first in-house reasoning model, a 35B-active-parameter sparse MoE with 256K context, trained without OpenAI data. Scores 97.0% on AIME 2025 and matches Claude Opus 4.6 on SWE-Bench Pro. Available in private preview via Microsoft Foundry.

2. **Microsoft MAI-Code-1-Flash** — A 5B-parameter coding model now in all GitHub Copilot plans. Claims +16 points over Claude Haiku 4.5 on SWE-Bench Pro (51.2% vs 35.2%) with 60% fewer tokens.

3. **OpenAI GPT-5.6 expected this month** — Prediction markets give 80-89% probability of a public release by June 30. GPT-5.5 (released April 23) remains the current flagship.

---

End of digest. Close this tab when done.
