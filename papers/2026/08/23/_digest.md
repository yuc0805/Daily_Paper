# AI Digest — 2026-08-23

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

A note on today's sourcing. It is Sunday, so arXiv has not posted a new listing and the freshest curated batch is the 21 August set. Everything below is drawn from that batch and from adjacent submissions in the same week that were not covered in the 22 August digest.

---

## Tier A — deep read

### TinyCast: Probabilistic Zero-Shot Forecasting with Computed Periodicity
Steinhauser, RAWS Labs. https://arxiv.org/abs/2608.15767

**Problem.** Zero-shot time-series forecasting has been answered by scale: pretrain a large sequence model on many series until it generalizes to unseen ones. That answer puts the smallest useful forecaster well above the memory budget of an embedded device, and the small end of the public leaderboards emits point forecasts only. Anyone who needs calibrated uncertainty on-device therefore has nothing to deploy.

**Method.** TinyCast holds 146,505 parameters and contains no attention. A spectral detector with zero learned parameters reads the dominant periods out of the context window, the context is folded on the phase of those periods, and a dilated causal convolutional encoder plus a block-autoregressive quantile decoder model the residual. The premise is stated plainly by the author: at this parameter budget the periodic structure of a context is worth computing rather than learning, so no capacity is spent rediscovering seasonality. Because every learned operation is a convolution, a matrix multiplication or a normalization, the model exports to static INT8 with no per-signal fitting step.

**Result.** On GIFT-Eval it is the smallest zero-shot entry whose parameter count can be established. Among zero-shot entries that declare no test-data leakage, it is the only model below 1.4M parameters that emits a predictive distribution, and every entry that scores better carries at least that budget. On Chronos-ZS and fev-bench every neural model ahead of it carries at least 28 times its parameters. It runs a full forecast end to end on a Cortex-M7 in 4.08 seconds inside 731 KB of RAM, at a cost of about 2% of point accuracy. Weights, code and the training recipe are public.

**Limitations.** The evaluation is leaderboard-shaped, so the series distribution is the usual public benchmark mix and not physiological data. The computed-periodicity argument depends on the spectral detector finding a clean dominant period, which is a strong assumption for signals with drifting or overlapping periodicity, and the paper does not report how the model degrades when the detector picks the wrong period. The 2% accuracy cost of INT8 export is reported on point accuracy only; the effect on quantile calibration is the number that would matter for a deployment.

**Why it matters to Leo.** This changes a deployment constraint rather than a benchmark number. A 731 KB INT8 forecaster with calibrated quantiles running inside a microcontroller removes the upload-then-infer round trip that most bio-sensing pipelines assume, which is the difference between a wearable that streams raw signal and one that forecasts locally. The open question that maps directly onto Leo's work is whether the substitution survives cardiac and gait periodicity under motion artifact, where the periods are shorter, less stationary, and contaminated in ways daily and weekly seasonality is not.

**How this builds on what you know:** The strongest parent is TimesNet (Wu 2023, HLTA8MDK), on your time-series page, which established FFT-based dominant-period detection and folding a 1D series into a periodic layout as the standard time-series inductive bias. Where TimesNet computed the periods and then handed the folded representation to a large learned attention-and-convolution stack, TinyCast keeps the folding and deletes the stack, because the argument is that the stack was mostly relearning the seasonality that had already been computed. The second parent is Chronos (Ansari 2024, 72DFULQQ), which set the scale-first template for zero-shot forecasting; TinyCast is the direct counter-argument, matching leakage-free probabilistic entries at 1/28th the parameters of the nearest neural competitor on Chronos-ZS. TimeGPT-1 (Garza 2024, 5I6GAKC4) is the third: it made probabilistic zero-shot forecasting a headline capability at API scale, and TinyCast delivers the same output type at embedded scale.

---

## Tier B — TLDR

### Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners (NAPE)
Cappellazzo, Liu, Petridis, Pantic, Imperial College London. https://arxiv.org/abs/2608.19863

NAPE pretrains an audio encoder by having a causal Transformer predict the next log-mel patch embedding from the preceding ones, with causal masking and a stop-gradient as the only training signal. There is no reconstruction decoder, no acoustic tokenizer, no student-teacher pair and no auxiliary regularization loss, which removes four components that current audio self-supervision recipes all carry. Across six audio and speech benchmarks it reaches state-of-the-art fine-tuning performance on several tasks, scales consistently as encoder size grows, and gives strong linear-probe results. Structured attention patterns appear without any supervision asking for them.

**How this builds on what you know:** The direct parent is Audio MAE (Huang 2022, 65EDEWIJ) on your audio page, which established masked patch reconstruction on log-mel spectrograms as the default recipe. Where Audio MAE masked random patches and trained an encoder-decoder pair to reconstruct spectrogram content in input space, NAPE removes the mask and the decoder and predicts the next patch's *embedding* instead, because audio is temporally ordered and the next-element objective is the one that scaled in language and vision. The second parent is How Mask Matters (Zhang 2023, 6INGKIJV, graphify `zhang2023_mae`, Community 1), which analysed what the masking objective supplies to a representation; NAPE removes both knobs that analysis was about and reports a stop-gradient is sufficient to prevent collapse. The third is HeAR (Baur 2024, 3LA8GNCU, graphify `baur2024_hear`, Community 1), which carried the masked-spectrogram recipe into health acoustics — which is exactly why this paper is the interesting one on today's list for you.

### Chain-of-Experience for Continual LLM Improvement
Tu, Fang, Wang, Xie, Yan, UCSC-VLAA. https://arxiv.org/abs/2608.18027

Chain-of-Experience measures how much a model improves when it is allowed to accumulate experiential traces across repeated attempts at a task at inference time, with feedback coming either from the model itself or from an environment signal such as correctness or a public coding test pass rate. Across eight models including GPT-5, Gemini-2.5 Pro and Claude-4.5 Sonnet, on math, coding and knowledge tasks, the loop beats the feedback-free baseline by 5.6% overall while cutting API cost by 19%, and delivers higher accuracy per token than existing test-time strategies. Combining complementary feedback channels adds further gain, base ability correlates with improvement capacity, and models stay robust when the feedback is weak or spurious. Most of the improvement arrives in the early iterations, which is the finding that determines how to budget the loop.

**How this builds on what you know:** Chain-of-Thought (Wei 2023, HBLPTRMY, graphify `wei2023_cot`, Community 0) placed the reasoning trace inside a single attempt and discarded it afterwards; this paper carries the trace across attempts and makes the accumulated record the input to the next one. LATS (Zhou 2024, 77ERE7HA, graphify `zhou2024_lats`, Community 0) spent test-time compute on branching and backtracking within one episode; Chain-of-Experience spends it on sequential episodes with a flat append-only log and reports better accuracy per token, which is a cost claim rather than a capability claim. The third parent is the Memory Mechanisms survey (Huang 2026, BDY3HUCV, graphify `huang2026_memory`), which catalogued mechanisms without establishing which feedback signals are worth collecting. Worth reading against MemTrapBench from yesterday's digest, which found that faithful and relevant memories can still degrade current-task performance — the two results disagree about whether accumulated context helps, and the disagreement is more informative than either paper alone.

### The Embedder's Dilemma: LLMs Are Better, but at What Cost?
El Assadi, Muennighoff, Lee. https://arxiv.org/abs/2608.12875

A controlled, cost-aware comparison of ten LLMs across six families against 26 dedicated embedding models from 118M to 14B parameters, on 37 tasks covering classification, semantic textual similarity, clustering, pair classification and retrieval. In aggregate the two paradigms tie, 77.6 against 77.2. The strengths split by task: LLMs lead on reasoning-heavy retrieval, embedding models lead on classification, and the two match on clustering, STS and pair classification. Parity is expensive — up to 1,431x more per benchmark pass (USD 154 against USD 0.11), with open LLMs processing tokens 2.5x to 736x more slowly on the same GPU. Reasoning tokens account for 28 to 81% of LLM inference cost, and lowering the reasoning budget preserves or improves retrieval quality for most models. The Pareto frontier contains the leading embedding models and exactly one LLM.

**How this builds on what you know:** BERT (Devlin 2019, WQRB4TUT) established the pretrained bidirectional encoder as the standard source of text representations and GPT-3 (Brown 2020, ZT8Y3ABF) established the decoder-only model as a general interface that can be asked to do representation tasks. Where both papers defined a family, neither answered which one to point at a given task once inference cost is counted; this paper holds the task suite and the hardware fixed and prices the trade. The contribution is a change in evaluation protocol rather than a new model: dollars per benchmark pass and tokens per second become first-class measurements, and the output is a Pareto frontier instead of a ranking.

---

## Tier C — scan only

| Paper | Hook | Link |
|---|---|---|
| Lévy Attention: Single-Pass Predictive Uncertainty for Continuous-Time Attention | Heavy-tailed process gives calibrated uncertainty in one forward pass. | https://arxiv.org/abs/2608.19171 |
| SWE-bench Science | Can coding agents resolve real engineering tasks drawn from scientific codebases? | https://arxiv.org/abs/2608.19799 |
| τ₀-VLA | Hierarchical robot foundation model that spends test-time compute inside a world model. | https://arxiv.org/abs/2608.16885 |
| ForgeWM | Progressive causal training for few-step action-conditioned video world models. | https://arxiv.org/abs/2608.14022 |
| Hierarchical Self-Improvement | Agent harnesses that evolve themselves per task rather than being hand-written. | https://arxiv.org/abs/2608.08466 |
| FlashPrefill V2 | Block-sparse prefill attention aimed at long-context serving cost. | https://arxiv.org/abs/2608.19758 |
| Thinking in a Low-Resource Language | Separates what SFT builds from what RL fixes, and what accuracy cannot see. | https://arxiv.org/abs/2608.17744 |
| FACET | Synthesises terminal tasks while preserving source intent and executable state. | https://arxiv.org/abs/2608.18580 |

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported.** TinyCast is native time series rather than an import, but the two ingredients it combines are both closed off. FFT-derived period folding entered time series with TimesNet and dilated causal convolution entered it from WaveNet years ago, so neither is an open transfer. What TinyCast contributes is the argument that the computed prior can substitute for learned capacity, and that argument is now made — the follow-on work is testing it on non-stationary physiological periodicity, not repeating it on public forecasting benchmarks.

**Unported opportunity: causal next-patch-embedding prediction for physiological signals.** NAPE's objective has not reached biosignals. Everything in graphify Community 1 that touches physiological pretraining — HeAR, SSL for HAR, the biosignal foundation model survey — is masked reconstruction, and Community 4 and 5 hyperedges show no causal-predictive entry at all. The transfer hypothesis: replace the log-mel front end with per-channel PPG, ECG or accelerometer spectrogram patches, keep the causal masking and stop-gradient exactly as published, and check whether the objective survives sensor noise and channel dropout, which audio does not have. The reason this is worth trying rather than assuming is that NAPE's whole claim is that the recipe needs no domain-specific machinery, so the port is close to mechanical and cheap to falsify.

**Unported opportunity: cost-aware Pareto evaluation for time-series foundation models.** The Embedder's Dilemma protocol — fix the task suite and hardware, report dollars per benchmark pass and throughput alongside quality, publish a frontier rather than a ranking — has not been applied to time-series foundation models, where the leaderboards still rank Chronos, Moirai, Moment and Timer on accuracy alone. TinyCast's result on the same day suggests the frontier would look very different from the ranking, and no one has drawn it.

---

## News

Nothing shipped today. The releases that matter from the past two weeks: Google put out Gemini 3.7 Flash on 13 August, following Gemini 3.6 Flash on 21 July. Z.AI released GLM-5.2 Turbo on 17 August, which is the most recent frontier-adjacent release tracked. Meta shipped Muse Spark 1.2 on 6 August. Anthropic's Claude Opus 5, released 24 July, remains the newest flagship from that lab.

---

End of digest. Close this tab when done.
