# AI Digest — 2026-06-28

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on signal: the new-paper stream into your areas was quiet over the last few days. The four papers below are recent and, more useful for you, none is yet in your library; each sits directly on the time-series, bio-sensing, or test-time-training parts of your graph.

---

## Tier A — deep read

### HEARTS: Benchmarking LLM Reasoning on Health Time Series (arXiv:2603.06638)

**Problem.** Several methods now claim that language models can reason over time series, but each reports on its own datasets, so the claims cannot be compared and shared failure modes stay hidden. There has been no graded test set that spans many health signal types and task kinds.

**Method.** HEARTS collects 16 real-world datasets across 12 health domains and 20 signal types (ECG, EEG, PPG, EMG, audio, eye tracking, CGM, and more), with sampling rates from daily aggregates to 48 kHz and lengths from tens of points to over a million. It defines 110 tasks grouped into four capabilities: perception, inference, generation, and deduction. It then scores 14 current LLMs on the same samples.

**Result.** On more than 20,000 test samples, LLMs fall well short of specialized models. They lean on simple heuristics and get worse as the number of temporal reasoning steps grows. General reasoning scores predict health-time-series scores only weakly, and the same failure modes recur within a model family, which says that scaling alone does not close the gap.

**Limitations.** It is a benchmark, so it measures the gap rather than fixing it. Results depend on the prompting and input format chosen for each model, and a benchmark of this size will need upkeep as models change.

**How this builds on what you know:** The direct parents in your library are TS-Agent (Liu 2025) and ChatTS (Xie 2025), both in your Time Series + LLM Integration community (graphify community 4), and LLMs are Few-Shot Health Learners (Liu 2023) in your Health AI community (community 1). Where TS-Agent and ChatTS each propose one method and report wins on chosen benchmarks, HEARTS builds the common yardstick and shows those single-method wins do not carry over to multi-step reasoning across modalities. Where Liu 2023 suggested LLMs are capable few-shot health learners, HEARTS shows that capability does not extend to reasoning. This paper sits on the same bridge your graph already records between Sensor2Text and the few-shot health work: it connects community 4 (TS + LLM) and community 1 (Health AI), pushing that bridge from method claims toward shared measurement.

**Why it matters to Leo.** This is a measurement paper in your primary area. It tells you where the current ceiling is for LLM reasoning on health signals and gives you a single axis (temporal complexity) to argue about in a paper or proposal. The benchmark-suite idea from CV and NLP is now ported to health time series, so the open work is methods that close the gap, not more benchmarks.

---

## Tier B — TLDRs

### SLIP: Learning Transferable Sensor Models via Language-Informed Pretraining (arXiv:2603.11950)

SLIP pretrains a sensor encoder whose representations align with language and transfer across sensor setups. It pairs contrastive signal-text alignment with sensor-conditioned captioning, reuses a frozen decoder-only language model through cross-attention, and adds a patch embedder that takes variable lengths and sampling rates at inference without retraining. Across 11 datasets it reaches 77.14% average linear-probe accuracy (a 5.93% relative gain over the strongest baseline) and 64.83% on sensor question answering.

**How this builds on what you know:** Its parents in your library are Sensor2Text (Chen 2024, community 4), SSL for HAR (Yuan 2024, community 1), and Time-LLM (Jin 2024). Where Sensor2Text aligns one fixed sensor configuration with language, SLIP removes the fixed-configuration limit so one model serves many channel counts, lengths, and rates. Where SSL for HAR learns from reconstruction without language, SLIP adds a language target to capture semantics that help classification. This paper extends Sensor2Text, which your graph marks as a cross-area bridge between bio-sensing (community 4) and llm-health (community 1); the new work pushes that bridge toward configuration-agnostic encoders. The imported method is CLIP and SigLIP style contrastive pretraining from the vision-language community applied to sensor signals.

### EASE-TTT: Evidence-Aligned Selective Test-Time Training for Long-Context QA (arXiv:2606.06906)

EASE-TTT adapts a language model at inference to answer questions over long contexts. It selects evidence chunks, turns them into a soft target over token positions, trains only the query-side attention parameters against that target, then answers from the original full context. On six LongBench QA tasks with three small decoder-only models it gives the best macro-average over full-context inference, retrieval-only baselines, and query-only test-time training.

**How this builds on what you know:** Its parents in your library are TTT Layers (Sun 2024) and TTT for Abstract Reasoning (Akyurek 2024), both in your test-time-training cluster; the loose neighbor is the reasoning community anchored by Chain-of-Thought. Where TTT Layers and Akyurek 2024 adapt with generic self-supervised objectives that do not know which positions matter, EASE-TTT supplies a targeted, evidence-aligned attention signal, so adaptation focuses on the positions that carry the answer. No direct parents in your Time Series + LLM community, which is exactly why it appears in today's Gap Watch.

### FEEL: Quantifying Heterogeneity in Physiological Signals for Emotion Recognition (arXiv:2604.05926)

FEEL benchmarks emotion recognition from EDA and PPG across 19 public datasets, testing 16 models from classical machine learning, deep learning, and self-supervised pretraining, with within-dataset and cross-dataset splits. Fine-tuned contrastive signal-language models score highest on arousal and valence, but Random Forests, LDA, and MLP stay competitive, and handcrafted-feature models beat raw-signal models in noisy, low-resource settings. Models trained on real-life data transfer well to lab (F1 = 0.79) and constraint-based (F1 = 0.78) settings.

**How this builds on what you know:** Its parents in your library are Foundation Models for Biosignals (Gu 2025), SSL for HAR (Yuan 2024), and HeAR (Baur 2024), all in your Health AI community (community 1). Where the Gu 2025 survey describes biosignal models and HeAR and Yuan 2024 report on their own data, FEEL measures all families on shared datasets with cross-dataset transfer. Its result that handcrafted features still win under noise tempers the assumption that larger self-supervised pretraining always helps for physiological signals. It reuses the same contrastive signal-language idea as SLIP, so the two together mark that method as well established for biosignals.

---

## Tier C — scan

No additional qualifying papers today; the stream was thin and the four above already cover the time-series, bio-sensing, and test-time-training fronts.

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off for now):
- LLM reasoning evaluation applied to health time series — HEARTS does this; matches your community 4 (TS + LLM) hyperedges.
- Contrastive signal-language pretraining (CLIP and SigLIP family) applied to sensors and biosignals — SLIP and FEEL both confirm this; matches communities 4 and 5.
- Benchmark-suite evaluation (CV and NLP style) applied to biosignal emotion recognition — FEEL does this.

Unported opportunity:
- Evidence-aligned test-time training (EASE-TTT, today's Tier B) has not been applied to physiological time series. Transfer hypothesis: at inference, treat a subject's most recent labeled windows as the "evidence" and use them as an attention-supervision target to adapt a frozen biosignal foundation model to that subject, which would address the cross-subject and device-shift gaps that FEEL and SLIP both report.

---

## News

Claude Opus 4.8 took the top overall spot on the Artificial Analysis leaderboard this month. Microsoft released a set of MAI models, headlined by MAI-Thinking-1, a one-trillion-total, 35-billion-active mixture-of-experts reasoning model trained from scratch without distillation. On the open-weight side, Z.ai released GLM-5.2, a 753-billion-parameter mixture-of-experts model under an MIT license with a one-million-token context window. None changes your near-term reading; the open-weight long-context models are worth noting if you want a local backbone for long physiological records.

---

End of digest. Close this tab when done.
