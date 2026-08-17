## Signal Processing and Time Series

### Timeline

1970 | ARIMA (Box et al.) | 
2017 | Attention Is All You Need (Vaswani et al.) | 
2020 | GPT-3 (Brown et al.) | 
2021 | GNN Intro (Sanchez-Lengeling et al.) | 
2021 | Informer (Zhou et al.) | 
2021 | LoRA (Hu et al.) | 
2021 | TimeGrad (Rasul et al.) | 
2022 | Autoformer (Wu et al.) | 
2022 | FEDformer (Zhou et al.) | 
2022 | FPT (Lu et al.) | 
2022 | Foundation Models Survey (Bommasani et al.) | 
2022 | TFC (Zhang et al.) | 
2023 | Crossformer (Zhang et al.) | 
2023 | DLinear (Zeng et al.) | 
2023 | GLOBEM (Xu et al.) | 
2023 | LVM-Med (Nguyen et al.) | 
2023 | MAE Theory (Zhang et al.) | 
2023 | PatchTST (Nie et al.) | 
2023 | TimesNet (Wu et al.) | 
2024 | Bi-Mamba+ (Liang et al.) | 
2024 | Brant-2 (Yuan et al.) | 
2024 | Chronos (Ansari et al.) | 
2024 | GPT4TS (Zhou et al.) | 
2024 | HARMamba (Li et al.) | 
2024 | HeAR (Baur et al.) | 

2026-05 | Superposition Not Necessary (2605.05151) | mechanistic interpretability shows TS transformers underuse superposition
2026-05 | Chronicle (2605.20268) | 324M joint language+TS transformer trained from scratch
2026-05 | Wearable Health FM (2605.22759) | 5M-participant wearable FM with LLM-agent AutoML for 35 health tasks
2026-05 | xMAE (2605.00973) | physiology-aware masked cross-modal reconstruction across ECG and PPG
2026-05 | BenchHAR (2605.08296) | SSL benchmark for generalizable sensor-based activity recognition
2026-05 | Generalizable Manifold (2605.20449) | frozen LLM transfers to forecasting because pretraining builds a reusable manifold
2026-05 | Operational Viability of TS FMs (2605.24381) | a Complexity Router sends each series to the cheapest adequate model class
2026-05 | BBC Calibrator (2605.27668) | post-hoc Beta-Bernoulli layer turns an LLM point forecast into a calibrated distribution with epistemic variance
2026-06 | TimeRecipe (2506.06482) | module-level benchmarking of TS forecasting; 10K experiments show tokenization and normalization matter more than backbone
2026-06 | Time-R1 (2506.10630) | RL fine-tuning teaches LLMs slow-thinking reasoning for TS forecasting via GRIP reward
2026-06 | Biosignal Fingerprinting (2605.09579) | cross-modal MAE for paired ECG and PPG; single-modality inference at test time
2026-06 | PETSA (2506.23424) | parameter-efficient test-time adaptation for TS foundation models via low-rank adapters

2026-06 | SARAF (2606.04135) | retrieval-augmented forecasting modulated by dataset-level stationarity
2026-06 | Vivaldi (2603.04142) | multi-agent framework for interpreting multivariate physiological time series
2026-06 | Last-Mile Forecasting (2606.02497) | LLM agent revises foundation model forecasts with business context
2026-06 | Personalized AF Forecasting (2606.10900) | per-patient fine-tuning of a global ECG model to forecast impending atrial fibrillation
2026-06 | Adaptive Patching Caution (2606.04074) | a validation-tuned uniform patch size matches content-adaptive patching on long-horizon benchmarks; negative result
2026-06 | CVAformer (2606.08262) | splits each variable into invariant and dynamic parts, then backdoor-adjusts the dynamic confounder before aligning with a frozen LLM
2026-06 | VAN-AD (2603.26842) | masked autoencoder plus a normalizing-flow density head for calibrated time-series anomaly scores
2026-06 | HiMAE (2510.25785) | hierarchical masked autoencoder gives one embedding per temporal scale for wearable signals, with a per-level resolution probe
2026-06 | IMPACT (2603.29183) | influence scores relabel contaminated training points and synthesize realistic unseen anomalies for open-set time-series anomaly detection
2026-06 | PulseLM (2603.03331) | dataset and benchmark pairing 1.31M PPG segments with 3.15M closed-ended question-answer pairs across twelve physiological tasks
2026-06 | SIGMA-PPG (2601.21031) | replaces random masking in PPG pretraining with a reinforcement-learning teacher that learns where and how hard to mask from signal statistics
2026-06 | RUL FM Embeddings (2606.11990) | frozen time-series foundation model embeddings with a light regression head predict remaining useful life
2026-06 | WEQA (2606.18147) | a language-model controller writes a per-question plan and routes wearable health questions to matching analysis tools
2026-06 | HEARTS (2603.06638) | benchmark of LLM reasoning over health time series; 16 datasets, 20 signal types, 110 tasks, 14 models
2026-06 | SLIP (2603.11950) | language-informed sensor pretraining with a variable-rate patch embedder that transfers across sensor setups
2026-06 | FEEL (2604.05926) | benchmark of EDA and PPG emotion recognition across 19 datasets and 16 models, with cross-dataset tests
2026-06 | ActivityNarrated (2604.00767) | open-ended narrative wearable HAR over multi-position partially observed IMU, scored by sensor-language retrieval
2026-06 | SignalMC-MED (2603.09940) | paired ECG and PPG benchmark of 22,256 visits and 20 clinical tasks; fusion and the full window help, larger models do not reliably
2026-06 | HAR Foundation Models Survey (2604.02711) | 132-paper lifecycle taxonomy of sensor-HAR foundation models across input, pretraining, adaptation, and utilization
2026-06 | TimeMaster (2506.13705) | RL (GRPO) trains a multimodal LLM to classify and explain image-rendered time series
2026-06 | TS-Haystack (2602.14200) | multi-scale retrieval benchmark testing whether time-series language models can locate a pattern inside a long signal
2026-07 | TS FM Break-Even (2607.04919) | measures the task-data size at which a pretrained forecaster beats classical methods
2026-07 | RV FM vs HAR (2607.05291) | zero-shot forecasters barely beat HAR econometric baselines on realized volatility once per-asset losses are averaged
2026-07 | STELLA (2607.03089) | on-device HAR by turning wearable sensor streams into activity-aware tokens read by a frozen LLM, with local per-user personalization
2026-07 | TiRex-2 (2607.01204) | xLSTM time-series foundation model for zero-shot streaming multivariate forecasting with future-known covariates
2026-07 | SensorGen (2607.04245) | controlled comparison of five generative-model families on real-world sensor time series; flow-matching is the strongest default
2026-07 | Post-Training TSFM Survey (2607.20002) | unifying framework sorting post-training methods for time series foundation models into five families keyed by locus of intervention
2026-07 | DEFT (2607.19659) | edits a frozen time-series foundation model's forecast at test time, reusing each expert score across trend and seasonal components
2026-08 | Zero-Shot HRV Forecasting (2607.20027) | tests TimesFM, Chronos, and MOIRAI zero-shot on wearable heart-rate-variability forecasting with a variability-preserving imputation for artifact gaps
2026-08 | OpenMHC (2607.16235) | largest open-access wearable health dataset with open model weights and a three-track benchmark

2026-08 | BLPM (2608.11656) | latent-target pretraining for EEG, with multi-query semantic decomposition aligned to a text space
2026-08 | TailBooster (2608.11951) | tail-only tabular VAE plus an autoencoder validity filter for rare extreme-event augmentation

### Paper List

[KNOWN] [1970] Box et al. — ARIMA. zotero_key:U2R8DC2P.
[KNOWN] [2017] Vaswani et al. — Attention Is All You Need. zotero_key:PHB9VRVM.
[KNOWN] [2020] Brown et al. — GPT-3. zotero_key:ZT8Y3ABF.
[KNOWN] [2021] Sanchez-Lengeling et al. — GNN Intro. zotero_key:VHTGRMY5.
[KNOWN] [2021] Zhou et al. — Informer. zotero_key:6RRFG94V.
[KNOWN] [2021] Hu et al. — LoRA. zotero_key:PZATM3SC.
[KNOWN] [2021] Rasul et al. — TimeGrad. zotero_key:RILRU5H6.
[KNOWN] [2022] Wu et al. — Autoformer. zotero_key:P6BV4TCL.
[KNOWN] [2022] Zhou et al. — FEDformer. zotero_key:TVHWGWAV.
[KNOWN] [2022] Lu et al. — FPT. zotero_key:3AA4F4KC.
[KNOWN] [2022] Bommasani et al. — Foundation Models Survey. zotero_key:TFPTRFGU.
[KNOWN] [2022] Zhang et al. — TFC. zotero_key:AJ5XKWDZ.
[KNOWN] [2023] Zhang et al. — Crossformer. zotero_key:RFAMVS5H.
[KNOWN] [2023] Zeng et al. — DLinear. zotero_key:4QRHV2JG.
[KNOWN] [2023] Xu et al. — GLOBEM. zotero_key:ICD9EG8Q.
[KNOWN] [2023] Nguyen et al. — LVM-Med. zotero_key:5GFYJJVV.
[KNOWN] [2023] Zhang et al. — MAE Theory. zotero_key:6INGKIJV.
[KNOWN] [2023] Nie et al. — PatchTST. zotero_key:YY67LF3R.
[KNOWN] [2023] Wu et al. — TimesNet. zotero_key:HLTA8MDK.
[KNOWN] [2024] Liang et al. — Bi-Mamba+. zotero_key:AVTJLZIR.
[KNOWN] [2024] Yuan et al. — Brant-2. zotero_key:YJ3P8H2J.
[KNOWN] [2024] Ansari et al. — Chronos. zotero_key:72DFULQQ.
[KNOWN] [2024] Zhou et al. — GPT4TS. zotero_key:6QQNUTL7.
[KNOWN] [2024] Li et al. — HARMamba. zotero_key:HE9X47KN.
[KNOWN] [2024] Baur et al. — HeAR. zotero_key:3LA8GNCU.
[KNOWN] [2024] Zhang et al. — LLMs for TS Survey. zotero_key:N2JLZBY3.
[KNOWN] [2024] Woo et al. — Moirai. zotero_key:CFG6FEIF.
[KNOWN] [2024] Goswami et al. — Moment. zotero_key:SIBB8W67.
[KNOWN] [2024] Yuan et al. — SSL for HAR. zotero_key:RTMH75VW.
[KNOWN] [2024] Chen et al. — Sensor2Text. zotero_key:ELYUE3NF.
[KNOWN] [2024] Sun et al. — TEST. zotero_key:ZE7SFTCQ.
[KNOWN] [2024] Talukder et al. — TOTEM. zotero_key:SKZEZQTH.
[KNOWN] [2024] Jin et al. — Time-LLM. zotero_key:MKICLA63.
[KNOWN] [2024] Garza et al. — TimeGPT-1. zotero_key:5I6GAKC4.
[KNOWN] [2024] Liu et al. — Timer. zotero_key:KKXN4S6L.
[KNOWN] [2024] Gao et al. — UniTS. zotero_key:GPJBBU2T.
[KNOWN] [2024] Masserano et al. — WaveToken. zotero_key:MXKVRSKK.
[KNOWN] [2024] Liu et al. — iTransformer. zotero_key:QBX2TI2X.
[KNOWN] [2024] Chen et al. — l-DAE. zotero_key:DZ2UYXUL.
[KNOWN] [2025] Xie et al. — ChatTS. zotero_key:VSCNJG5J.
[KNOWN] [2025] Gu et al. — Foundation Models Biosignals. zotero_key:2XWEG7AF.
[KNOWN] [2025] Unknown — SensorLM. zotero_key:HDPXBLAP.
[KNOWN] [2025] Liu et al. — Sundial. zotero_key:4QQTVIYC.
[KNOWN] [2025] Liu et al. — TS-Agent. zotero_key:I2CIT4I7.

[2026] 2605.05151 — Superposition Is Not Necessary: Mechanistic Interpretability for TS Forecasting. [https://arxiv.org/abs/2605.05151](https://arxiv.org/abs/2605.05151). external.
[2026] 2605.20268 — Chronicle: Joint Language and Time Series Foundation Model. [https://arxiv.org/abs/2605.20268](https://arxiv.org/abs/2605.20268). external.
[2026] 2605.22759 — Towards a General Intelligence and Interface for Wearable Health Data. [https://arxiv.org/abs/2605.22759](https://arxiv.org/abs/2605.22759). external.
[2026] 2605.00973 — Physiology-Aware Masked Cross-Modal Reconstruction for Biosignal Representation Learning (xMAE). [https://arxiv.org/abs/2605.00973](https://arxiv.org/abs/2605.00973). external.
[2026] 2605.08296 — BenchHAR: Benchmarking Self-Supervised Learning for Generalizable Sensor-based Activity Recognition. [https://arxiv.org/abs/2605.08296](https://arxiv.org/abs/2605.08296). external.
[2026] 2605.20449 — LLM Pretraining Shapes a Generalizable Manifold: Cross-Modal Transfer to Time Series. [https://arxiv.org/abs/2605.20449](https://arxiv.org/abs/2605.20449). external.
[2026] 2605.24381 — Assessing the Operational Viability of Foundation Models for Time Series Forecasting. [https://arxiv.org/abs/2605.24381](https://arxiv.org/abs/2605.24381). external.
[2026] 2605.27668 — Aligning LLMs with Human Uncertainty: A Beta-Bernoulli Calibrator for LLM Forecasting. [https://arxiv.org/abs/2605.27668](https://arxiv.org/abs/2605.27668). external.
[2026] 2506.06482 — TimeRecipe: A Time-Series Forecasting Recipe via Benchmarking Module Level Effectiveness. [https://arxiv.org/abs/2506.06482](https://arxiv.org/abs/2506.06482). external.
[2026] 2506.10630 — Time-R1: Time Series Forecasting as Reasoning via Reinforced LLMs. [https://arxiv.org/abs/2506.10630](https://arxiv.org/abs/2506.10630). external.
[2605] 2605.09579 — Biosignal Fingerprinting: A Cross-Modal PPG-ECG Foundation Model. [https://arxiv.org/abs/2605.09579](https://arxiv.org/abs/2605.09579). external.
[2026] 2506.23424 — PETSA: Parameter-Efficient Test-Time Adaptation for Time Series Forecasting. [https://arxiv.org/abs/2506.23424](https://arxiv.org/abs/2506.23424). external.

[2026] 2606.04135 — SARAF: Stationarity-Aware Retrieval-Augmented Time Series Forecasting. [https://arxiv.org/abs/2606.04135](https://arxiv.org/abs/2606.04135). external.

[2026] 2603.04142 — Vivaldi: A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series. [https://arxiv.org/abs/2603.04142](https://arxiv.org/abs/2603.04142). external.

[2026] 2606.02497 — Bridging the Last Mile of Time Series Forecasting with LLM Agents. [https://arxiv.org/abs/2606.02497](https://arxiv.org/abs/2606.02497). external.
[2026] 2606.10900 — Personalized Deep Learning for Short-Term Forecasting of Impending Atrial Fibrillation from Continuous Wearable ECG Signals. [https://arxiv.org/abs/2606.10900](https://arxiv.org/abs/2606.10900). external.

[2026] 2606.04074 — Adaptive Patching Is Harder Than It Looks for Time-Series Forecasting. [https://arxiv.org/abs/2606.04074](https://arxiv.org/abs/2606.04074). external.
[2026] 2606.08262 — Causal Semantic Alignment for LLM-based Time Series Forecasting (CVAformer). [https://arxiv.org/abs/2606.08262](https://arxiv.org/abs/2606.08262). external.
[2026] 2603.26842 — VAN-AD: Visual Masked Autoencoder with Normalizing Flow for Time Series Anomaly Detection. [https://arxiv.org/abs/2603.26842](https://arxiv.org/abs/2603.26842). external.
[2026] 2510.25785 — HiMAE: Hierarchical Masked Autoencoders Discover Resolution-Specific Structure in Wearable Time Series. [https://arxiv.org/abs/2510.25785](https://arxiv.org/abs/2510.25785). external.
[2026] 2603.29183 — IMPACT: Influence Modeling for Open-Set Time Series Anomaly Detection. [https://arxiv.org/abs/2603.29183](https://arxiv.org/abs/2603.29183). external.

[2026] 2603.03331 — PulseLM: A Foundation Dataset and Benchmark for PPG-Text Learning. [https://arxiv.org/abs/2603.03331](https://arxiv.org/abs/2603.03331). external.
[2026] 2601.21031 — SIGMA-PPG: Statistical-prior Informed Generative Masking Architecture for PPG Foundation Model. [https://arxiv.org/abs/2601.21031](https://arxiv.org/abs/2601.21031). external.
[2026] 2606.11990 — Time-Series Foundation Model Embeddings for Remaining Useful Life Estimation. [https://arxiv.org/abs/2606.11990](https://arxiv.org/abs/2606.11990). external.
[2026] 2606.18147 — WEQA: Wearable hEalth Question Answering with Query-Adaptive Agentic Reasoning. [https://arxiv.org/abs/2606.18147](https://arxiv.org/abs/2606.18147). external.
[2026] 2603.06638 — HEARTS: Benchmarking LLM Reasoning on Health Time Series. [https://arxiv.org/abs/2603.06638](https://arxiv.org/abs/2603.06638). external.
[2026] 2603.11950 — SLIP: Learning Transferable Sensor Models via Language-Informed Pretraining. [https://arxiv.org/abs/2603.11950](https://arxiv.org/abs/2603.11950). external.
[2026] 2604.05926 — FEEL: Quantifying Heterogeneity in Physiological Signals for Generalizable Emotion Recognition. [https://arxiv.org/abs/2604.05926](https://arxiv.org/abs/2604.05926). external.
[2026] 2604.00767 — ActivityNarrated: An Open-Ended Narrative Paradigm for Wearable Human Activity Understanding. [https://arxiv.org/abs/2604.00767](https://arxiv.org/abs/2604.00767). external.
[2026] 2603.09940 — SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG. [https://arxiv.org/abs/2603.09940](https://arxiv.org/abs/2603.09940). external.
[2026] 2604.02711 — Foundation Models Defining A New Era In Sensor-based Human Activity Recognition: A Survey And Outlook. [https://arxiv.org/abs/2604.02711](https://arxiv.org/abs/2604.02711). external.

[2026] 2506.13705 — TimeMaster: Training Time-Series Multimodal LLMs to Reason via Reinforcement Learning. [https://arxiv.org/abs/2506.13705](https://arxiv.org/abs/2506.13705). external.
[2026] 2602.14200 — TS-Haystack: A Multi-Scale Retrieval Benchmark for Time Series Language Models. [https://arxiv.org/abs/2602.14200](https://arxiv.org/abs/2602.14200). external.
[2026] 2607.04919 — When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters. [https://arxiv.org/abs/2607.04919](https://arxiv.org/abs/2607.04919). external.
[2026] 2607.05291 — Forecasting Realized Volatility with Time Series Foundation Models: A Comparison with Econometric Benchmarks. [https://arxiv.org/abs/2607.05291](https://arxiv.org/abs/2607.05291). external.
[2026] 2607.03089 — STELLA: Efficient Sensor-to-LLM Translation for On-Device Human Activity Recognition. [https://arxiv.org/abs/2607.03089](https://arxiv.org/abs/2607.03089). external.
[2026] 2607.01204 — TiRex-2: Generalizing TiRex to Multivariate Data and Streaming. [https://arxiv.org/abs/2607.01204](https://arxiv.org/abs/2607.01204). external.

[2026] 2607.04245 — Signal or Noise? Understanding Generative Models for Real-World Sensor Time Series. [https://arxiv.org/abs/2607.04245](https://arxiv.org/abs/2607.04245). external.
[2026] 2607.20002 — Post-Training in Time Series Foundation Models: A Unifying Framework. [https://arxiv.org/abs/2607.20002](https://arxiv.org/abs/2607.20002). external.
[2026] 2607.19659 — Expert-Guided Forecast Editing for Time-Series Foundation Models. [https://arxiv.org/abs/2607.19659](https://arxiv.org/abs/2607.19659). external.

[2026] 2607.20027 — Zero-Shot Heart Rate Variability Forecasting from Consumer Wearables Using Time Series Foundation Models. [https://arxiv.org/abs/2607.20027](https://arxiv.org/abs/2607.20027). external.

[2026] 2607.16235 — OpenMHC: Accelerating the Science of Wearable Foundation Models. [https://arxiv.org/abs/2607.16235](https://arxiv.org/abs/2607.16235). external.

[2026] 2608.11656 — Continuous-Latent Predictive Modeling with Semantic Alignment for EEG-Language Foundation Models (BLPM). [https://arxiv.org/abs/2608.11656](https://arxiv.org/abs/2608.11656). external.
[2026] 2608.11951 — TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation with Operational Validity Enforcement. [https://arxiv.org/abs/2608.11951](https://arxiv.org/abs/2608.11951). external.

### Recent Activity

2026-08-16 | 2608.11656 added | BLPM drops both standard EEG pretraining objectives, replacing masked reconstruction and token prediction with a Continuous EEG Latent Predictive encoder whose target is a latent representation rather than the waveform, and adds Multi-Query Semantic Decomposition so the representation is split into several queries aligned to text rather than pooled into one vector, because montage, channel count, and label space differ across datasets and a single bottleneck serves none of them well; the reported evidence is consistent generalisation across benchmarks, subjects, and recording environments rather than per-benchmark numbers, and no collapse-prevention ablation is given, so the claim is provisional; the imported method is joint-embedding latent prediction from vision, now closed off for EEG but still open for PPG, GSR, and IMU; Tier A

2026-08-16 | 2608.11951 added | TailBooster splits rare-event augmentation into two layers, a statistical layer that isolates extremes by interquartile range and trains a tabular variational autoencoder on that subset alone, and a learned layer that rejects synthetic records whose reconstruction error puts them outside an operational envelope inferred from historical data, because a tail-focused generator will otherwise produce records that are statistically extreme and physically impossible; on US flight records, training six regression algorithms on its output cut mean absolute error by 47 to 49 percent on extreme air time and 29 to 57 percent on extreme arrival delay against conventional synthetic data; evaluation is mixed-type tabular data only, so transfer to physiological waveforms, where the check would run over a window rather than a row, is a hypothesis; Tier B

2026-08-03 | 2607.16235 added | OpenMHC releases the largest open-access wearable health dataset to date, over 60 million hours across 19 sensor channels and up to 169 linked health, lifestyle, mood, and behavior variables from 11,894 participants, and ships open-source implementations of recent wearable foundation models with one benchmark covering health and behavior prediction, multivariate imputation, and forecasting; the reusable value is the shared testbed, because the masked-reconstruction and multivariate time-series pretraining it benchmarks is now well ported and closed off as low-hanging fruit; Tier A

2026-08-02 | 2607.20027 added | runs TimesFM, Chronos, and MOIRAI unchanged on fragmented consumer-wearable heart-rate-variability data with no fine-tuning and still beats classical baselines (MASE 0.81 to 0.87) across horizons up to two hours on 49 participants, because a variability-preserving imputation (linear interpolation plus locally adaptive stochastic noise) keeps the input inside the pretrained models' expected distribution; the reusable piece is the imputation trick, not a new architecture; Tier A

2026-07-30 | 2607.19659 added | DEFT edits a frozen time-series foundation model's forecast at test time, first exploiting predictive samples inside a trend-seasonal decomposition then exploring the trend and seasonal components separately, and reusing each expensive expert score across the components that appear in the scored trajectories so one query yields component-level feedback; it imports query-efficient search from reinforcement learning into forecast editing; Tier A

2026-07-30 | 2607.05291 added | tests whether pretrained time-series foundation models beat classical econometric models at forecasting realized volatility, finding that performance varies across foundation-model architectures and that the choice of architecture matters more than the broad foundation-model-versus-econometric split, since the frozen model's architecture sets the accuracy ceiling; Tier B

2026-07-27 | 2607.20002 added | a survey that places the methods sitting between a pretrained time series model and its deployment into one framework keyed by locus of intervention, naming five families (parameter adaptation, context augmentation, model composition, output processing with uncertainty control, and compression with specialization), and marking uncertainty-aware model composition and deployment-aware specialization as the thinner, higher-value areas; Tier A
