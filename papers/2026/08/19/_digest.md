# AI Digest — 2026-08-19

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

A note on today's mix: this is a time-series-heavy day. Three of the four Tier A/B papers sit in your primary area, and one of the three is a bio-signal benchmark. That is unusual and worth the reading time.

---

## Tier A — deep read

### RouteTS: Frequency-Time Routing for Time Series Forecasting
arXiv:2608.14682 — https://arxiv.org/abs/2608.14682

**Problem.** Real time series carry two kinds of structure at once: global periodic components that repeat over long spans, and local non-stationary events such as spikes and regime breaks. Existing forecasters process both inside a single computational domain and pay for it in a predictable way. Time-domain models drift out of phase with the periodic component over long horizons, which the paper calls periodic misalignment. Frequency-domain models do the opposite: the Fourier basis spreads a transient spike across many coefficients, so reconstructing the spike requires coefficients that the model has already smoothed away. Neither failure is fixed by making the model larger, because the failure comes from the representation, not from capacity.

**Method.** RouteTS starts from the claim that the correct computational domain is a property of the data, not of the model, and then routes accordingly. It takes the amplitude spectrum of the input window and splits it by amplitude: high-amplitude components, which correspond to the dominant periodicities, stay in the frequency domain and are forecast by a complex-valued linear predictor, which preserves phase and so does not accumulate misalignment over the horizon. The residual spectral energy, which is where transient and local structure lives, is inverted back to the time domain and handled by a lightweight MLP. The two branch outputs are then recombined. The routing decision is made per frequency component from the data itself rather than learned as a gate, which keeps the parameter count low.

**Result.** RouteTS reports the best average MSE on six of eight benchmarks and stays competitive on MAE across most datasets. The two results that matter for reading the mechanism rather than the leaderboard are the endpoints. On COVID-19, which is the most non-stationary dataset in the suite, RouteTS is best on both MSE and MAE, and the paper attributes this to the residual energy being handled purely in the time domain, so the abrupt localised spikes are never smoothed. On Solar, which is strongly periodic, RouteTS is also best on both metrics, which is the complementary case: the dual-branch split does not cost anything on data where a single domain would already have worked. That pair of results is the actual evidence for the routing claim. The design is lightweight by construction — a complex linear layer plus an MLP — so the computational cost is well below transformer-based baselines.

**Limitations.** The routing criterion is amplitude, which is a proxy for "this component is a stable periodicity" rather than a direct test of it. A high-amplitude component that is itself drifting will be sent to the frequency branch and mishandled. The paper's benchmark suite is the standard long-horizon forecasting set, so the evidence is about forecasting and does not transfer automatically to classification or anomaly detection. There is also no reported ablation isolating how much of the gain comes from the complex-valued predictor as opposed to the split itself, which is the number you would want before adopting the component.

**Why it matters to you.** The routing idea is separable from the forecasting task. Your wearable and bio-signal work has exactly the structure RouteTS targets: a strong circadian or cardiac periodicity plus sparse, clinically meaningful transient events, and the standard complaint about frequency-domain bio-signal models is precisely that they smooth away the transients you care about. Amplitude routing is a cheap thing to try as a front end on an existing encoder, and the COVID-19 result is the closest analogue in the paper to a spike-detection regime.

**How this builds on what you know:** The closest parents in your library are FEDformer (2022, TVHWGWAV) and DLinear (2023, 4QRHV2JG), with TimesNet (2023, HLTA8MDK) as a third. Where FEDformer moved forecasting into the frequency domain wholesale and used a random subset of Fourier modes to keep the cost down, RouteTS keeps the frequency domain only for the components where it is provably the right basis and sends everything else back to time, because a fixed mode subset cannot distinguish "low amplitude because unimportant" from "low amplitude because the energy is a spread-out transient". Where DLinear showed that a single linear layer in the time domain beats most transformers on long-horizon forecasting, RouteTS keeps that lesson — both branches are deliberately shallow — but shows the linear layer is being asked to do two incompatible jobs at once and splits them. Where TimesNet reshaped the series into 2D blocks indexed by discovered periods to make periodicity explicit, RouteTS gets the same information from the amplitude spectrum without the reshape, which is why it stays cheap. Note that none of these three parents is in the graphify subset: graphify's time-series coverage (Community 4) is weighted toward LLM integration, so the classical forecasting lineage had to come from the full Zotero index. That is a coverage gap in the seed graph worth closing.

---

## Tier B — TLDR

### ReasonCast: Towards Explainable Time Series Forecasting with Reasoning
arXiv:2608.01875 — https://arxiv.org/abs/2608.01875 — code at https://github.com/seunghan96/reasoncast

Time-series models are usually specialised for one of two jobs: understanding, meaning returning text answers about a series, or generation, meaning returning a numeric forecast. The recent unified models handle both but route them down task-separated paths, so the model cannot produce a forecast and an explanation of that forecast as one coherent object. ReasonCast argues for task fusion instead: a recipe for fine-tuning any LLM backbone so that it emits a reasoning chain and a numeric forecast together in a single autoregressive pass. The authors also release ReasonTS-Bench, which decomposes time series into five fundamental patterns and scores forecast error (MAE) alongside three reasoning metrics averaged over those five primitives. The headline claim is that applying the recipe to a range of LLM backbones gives them forecasting accuracy above specialised time-series models while producing reasoning that can be checked against the series.

**How this builds on what you know:** Three parents, two of them graphify anchors. ChatTS (2025, VSCNJG5J, graphify `xie2025_chatts`, Community 4 — Time Series + LLM Integration) established that a time series can be aligned into an LLM's input space well enough to answer questions about it. TS-Agent (2025, I2CIT4I7, graphify `liu2025_tsagent`, a god node in your time-series area with 7 edges) took the other route and made the LLM a controller calling analysis operators, so every claim traces to an operator output. Chain-of-Thought (2023, HBLPTRMY, graphify `wei2023_cot`, Community 0 — LLM Agents & Reasoning) supplied the intermediate-steps idea both inherit. Where ChatTS aligned the series so the model could describe it, and TS-Agent made the reasoning auditable by pushing every numeric claim into a tool call, ReasonCast puts both back inside one forward pass and makes the reasoning chain a supervised training target rather than an inference-time scaffold, because a chain that is trained can be scored on a benchmark whereas a chain that is prompted or tool-mediated cannot be compared across backbones.

This also extends the graphify cross-area bridge `deepseek2025_r1 → wei2023_cot`, which already crossed Community 0 (LLM Agents & Reasoning) and the reasoning area in your library by moving from prompted reasoning to reasoning learned through training. ReasonCast pushes that same bridge further, into Community 4: reasoning as a fine-tuned capability rather than a prompt, now applied to numeric forecasting rather than to text.

---

### FOUND-AF: Benchmarking ECG Foundation Models for Atrial Fibrillation Detection
arXiv:2608.03597 — https://arxiv.org/abs/2608.03597

This is an evaluation paper, not a method paper, and that is why it is here. The authors put nine public ECG foundation models from five families — HuBERT-ECG, CLEF, ST-MEM, ECG-JEPA and ECGFounder among them — through one leakage-controlled protocol across four heterogeneous datasets (AFDB, CinC2017, CPSC2021, LTAFDB). Every model is used as a frozen feature extractor with standardised preprocessing, model-native resampling, a fixed XGBoost classifier, and recording-level grouped cross-validation, so no subject appears on both sides of a split. Evaluation includes paired recording-level bootstrap comparisons with Holm correction, embedding-space visualisation, and profiling of model size, inference time and memory. ECGFounder comes out strongest overall while also sitting at a good point on the accuracy-versus-cost curve. The value here is the protocol: recording-level grouping plus a frozen encoder and a fixed downstream classifier is the setup that makes representation-quality claims in bio-signal work comparable at all, and most published ECG numbers were not produced this way.

**How this builds on what you know:** Foundation Models for Biosignals: A Survey (2025, 2XWEG7AF, graphify `gu2025_biosignals`, Community 1 — Health AI & Self-Supervised, and a god node in your llm-health area) mapped which bio-signal foundation models exist and what they claim. HeAR (2024, 3LA8GNCU, graphify `baur2024_hear`, Community 1) built health acoustic representations and evaluated them by transfer to downstream health tasks. SSL for HAR with 700K Person-days (2024, RTMH75VW, graphify `yuan2024_ssl_har`, a god node in your self-supervised area with 8 edges) established the large-scale self-supervised pretraining recipe for wearable sensor streams. Where the biosignals survey catalogued the claims, FOUND-AF tests them under one protocol and finds the ranking, because a survey inherits each paper's own evaluation setup and therefore cannot say which encoder is actually better. Where HeAR and SSL-for-HAR each validated a single encoder against baselines the authors chose, FOUND-AF fixes the downstream classifier and the split policy across all nine encoders, which is the only way the comparison isolates representation quality rather than fine-tuning effort.

`gu2025_biosignals` sits on both your `time-series.md` and `llm-health.md` area pages, so it already functions as a bridge between Community 1 and Community 5 (Wearable Sensing & Behavior). FOUND-AF strengthens that bridge on the evaluation side rather than the modelling side: it gives the two communities a shared benchmark protocol, which is what they have been missing.

---

### WIRED: Weighted Adaptive Prediction with Structured Dependence for Probabilistic Multiseries Forecasting
arXiv:2608.12998 — https://arxiv.org/abs/2608.12998

Vercellino's paper is an R package with a benchmark attached, and it is worth ten minutes because of what it separates rather than what it scores. WIRED forecasts many related series jointly by keeping two things apart that deep forecasters usually entangle: the marginal predictive distribution of each series, and the dependence structure across series. Marginals come from a library of simple predictive distributions combined by CRPS-based adaptive mixture weights; dependence is reconstructed afterwards by a Gaussian or Student t copula used for cross-series simulation. Evaluation covers four synthetic data-generating processes at three horizons with 30 replicates per pair, nine ablations and external baselines, plus a rolling-origin study on EuStockMarkets. The authors state the contribution as architectural and diagnostic rather than a new state of the art, which is the honest framing.

**How this builds on what you know:** The two strongest parents are both from this week's digests. Forecast Collapse in Time-Series Foundation Models (2026, arXiv:2608.14106) showed that per-series training objectives leave cross-series structure unidentified, producing a calibration-versus-ranking tradeoff where minimising squared error flattens the forecasts. Multivariate Time Series Forecasting needs Cross Variable Loss (2026, arXiv:2608.05742) proved that point-wise squared error only matches the Gaussian likelihood under spherical residual covariance, and added a graph penalty over residual edges to recover the missing structure. Where Forecast Collapse diagnosed the problem and Cross Variable Loss patched it inside the loss function of a neural backbone, WIRED removes the coupling entirely by fitting marginals and dependence as separate stages, because if the dependence is modelled by an explicit copula then no property of the marginal training objective can destroy it. The tradeoff is that a copula imposes a parametric dependence family, where the graph penalty learns whatever structure the residuals show. Reading the three together gives you the diagnosis, the in-loss fix and the architectural fix for one problem in one week — that is the most useful hour of the digest.

---

## Tier C — scan only

| Paper | Hook | Link |
|---|---|---|
| ASI-Bench: At the Dawn of Artificial Superintelligence | 42-author benchmark aiming above frontier-model capability ceilings; check the task design | https://arxiv.org/abs/2608.17271 |
| FreeToken: Efficient Edge-Native MoE Serving | Bandwidth-adaptive expert execution for mixture-of-experts on edge devices | https://arxiv.org/abs/2608.16157 |
| Agentic ESOpt | Fine-tuning long-horizon LLM agents under minimal GPU budgets | https://arxiv.org/abs/2608.17310 |
| AVA-Encoder | Video representations learned for agent consumption rather than human labels | https://arxiv.org/abs/2608.12313 |
| Harness the Memory | Holistic evaluation of memory substrates across agent memory systems | https://arxiv.org/abs/2608.15008 |
| Energy-Guided Flow Matching | Steers flow-matching generation with an energy function at sampling time | https://arxiv.org/abs/2608.05811 |
| Agent Lightning v1.0 | Microsoft's agentic reinforcement learning training stack, first stable release | https://arxiv.org/abs/2608.17528 |
| Unifying Graph Neural Networks Through a Common Layer Equation | Single equation recovering many GNN layer families as special cases | https://arxiv.org/abs/2608.16097 |

---

## Tier D — Time-series / bio-sensing gap watch

**Already ported — closed off.** ReasonCast ports supervised reasoning-chain fine-tuning, the training-time version of chain-of-thought, from language into numeric forecasting, and ships a benchmark with it. That combination closes the opening: the obvious paper "what if we trained the forecaster to explain itself" now exists with an evaluation suite, and Community 4 in your graph absorbs it. FOUND-AF ports the frozen-encoder plus fixed-downstream-classifier evaluation protocol, standard in vision and language representation work, into ECG, with recording-level grouping added for the leakage problem specific to physiological data. Anyone planning a "we benchmark bio-signal foundation models properly" paper for ECG should now redirect to a modality FOUND-AF does not cover. RouteTS is not a port — amplitude-based spectral routing is native signal processing — so it is the one Tier A idea today that is still upstream of your area rather than already inside it.

**Unported opportunity 1 — energy guidance for bio-signal generation.** Energy-Guided Flow Matching (2608.05811) steers a flow-matching sampler with an external energy function at inference, with no retraining. Transfer hypothesis: use a physiological plausibility energy — QRS morphology constraints for ECG, band-power limits for EEG, physiologically admissible heart-rate ranges for PPG — to guide imputation of missing wearable segments, so the imputed signal is constrained to be clinically valid rather than merely likely under the training distribution. Nothing in Community 4 or Community 5 matches this hyperedge.

**Unported opportunity 2 — agent-native sensor representations.** AVA-Encoder (2608.12313) learns video representations optimised for downstream agent consumption rather than for human-labelled recognition. Transfer hypothesis: learn wearable sensor representations optimised for what a health agent actually queries — trend, anomaly, change-point, comparison to baseline — rather than for activity classification accuracy. Your Community 5 (Wearable Sensing & Behavior) papers all encode for classification, and Sensor2Text (`chen2024_sensor2text`) encodes for description; neither encodes for agent query patterns. That is an open slot.

---

## News

Google released Gemini 3.7 Flash three weeks after 3.6 Flash. Reported movements: FrontierCode 1.1 from 34.4 to 43.6 percent, DeepSWE v1.1 from 49 to 65.3 percent, and AutomationBench from 17 to 30.4 percent. Introductory pricing is 0.75 dollars per million input tokens and 3.75 dollars output through 31 December 2026, returning to 1.50 and 7.50 in 2027. The context window stays at one million tokens, and the model is available through Antigravity, AI Studio, Vertex AI and the Gemini Enterprise Agent Platform.

OpenAI opened a limited API preview of Ultrafast mode for GPT-5.6 Sol, running on Cerebras hardware, at roughly 750 output tokens per second and reported as up to 14 times faster than the standard endpoint.

On the business side, Bloomberg and TechCrunch reported on 16 August that Stripe has finalised an acquisition of OpenRouter for more than 7 billion dollars.

---

End of digest. Close this tab when done.
