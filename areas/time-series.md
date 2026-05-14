## Signal Processing and Time Series

### What

Time series analysis covers methods for modeling, forecasting, and classifying sequential data where observations are indexed by time. In the ML context, this includes sensor signals from wearables, financial data, weather records, and physiological measurements. The field has shifted from classical statistical models (ARIMA, exponential smoothing) toward deep learning architectures, and more recently toward foundation models that generalize across domains.

### Why

Many real-world decision systems depend on temporal data: clinical monitoring, energy demand planning, industrial fault detection. Classical methods assume stationarity and linear dynamics, which fail on high-dimensional, non-stationary sensor streams. Modern deep models can capture long-range dependencies and cross-variate interactions, but they remain data-hungry and hard to transfer across domains, motivating the current push toward pre-trained time series foundation models.

### Baseline

Fit an ARIMA(p,d,q) model per univariate channel, selecting orders by AIC. For multivariate settings, fit a VAR model. For classification, extract hand-crafted features (mean, variance, FFT coefficients) and train a random forest. The main failure mode is that these methods cannot capture nonlinear cross-channel dependencies or adapt to distribution shift without manual re-tuning.

### Running Example

Forecast the next 96 steps of the ETTh1 electricity transformer temperature dataset given the previous 336 steps (7 variates). The desired output is a 96-step prediction with MSE below 0.40. The ARIMA baseline, fit independently per channel, produces MSE around 0.65 because it ignores cross-variate correlations and nonlinear trends.

### Baseline vs Method Comparison on the Running Example

| Approach | Output on running example | Why it differs from baseline |
|---|---|---|
| Baseline | See running example above | (anchor) |
| TS-Agent | _To be added as papers accumulate._ | Anchor paper for this area |
| Sensor2Text | _To be added as papers accumulate._ | Anchor paper for this area |

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

### Key Methods

| Method | Year | Core idea (one clause) | Best benchmark result | Cost / limitation |
|---|---|---|---|---|
| TS-Agent | Liu 2025 | Anchor method | _To be filled_ | _To be filled_ |
| Sensor2Text | Chen 2024 | Anchor method | _To be filled_ | _To be filled_ |
| Attention Is All You Need | 2017 | _To be filled_ | _To be filled_ | _To be filled_ |
| GLOBEM | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |
| MAE Theory | 2023 | _To be filled_ | _To be filled_ | _To be filled_ |
| HARMamba | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| HeAR | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| LLMs for TS Survey | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| SSL for HAR | 2024 | _To be filled_ | _To be filled_ | _To be filled_ |
| ChatTS | 2025 | _To be filled_ | _To be filled_ | _To be filled_ |
| Foundation Models Biosignals | 2025 | _To be filled_ | _To be filled_ | _To be filled_ |

### Benchmark Results

| Method | Benchmark | Metric | Score | Source paper |
|---|---|---|---|---|
| _To be added as papers accumulate._ | | | | |

### Limitations

_To be added as papers accumulate._

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
[KNOWN] [2023] Xu et al. — GLOBEM. zotero_key:8VB7UFKN.
[KNOWN] [2023] Nguyen et al. — LVM-Med. zotero_key:5GFYJJVV.
[KNOWN] [2023] Zhang et al. — MAE Theory. zotero_key:6INGKIJV.
[KNOWN] [2023] Nie et al. — PatchTST. zotero_key:3SLMN5NV.
[KNOWN] [2023] Wu et al. — TimesNet. zotero_key:TFFPWHUN.
[KNOWN] [2024] Liang et al. — Bi-Mamba+. zotero_key:AVTJLZIR.
[KNOWN] [2024] Yuan et al. — Brant-2. zotero_key:YJ3P8H2J.
[KNOWN] [2024] Ansari et al. — Chronos. zotero_key:HEZXEKXP.
[KNOWN] [2024] Zhou et al. — GPT4TS. zotero_key:YRPNRRZC.
[KNOWN] [2024] Li et al. — HARMamba. zotero_key:HE9X47KN.
[KNOWN] [2024] Baur et al. — HeAR. zotero_key:3LA8GNCU.
[KNOWN] [2024] Zhang et al. — LLMs for TS Survey. zotero_key:DNQKLKBV.
[KNOWN] [2024] Woo et al. — Moirai. zotero_key:65T96HWJ.
[KNOWN] [2024] Goswami et al. — Moment. zotero_key:5XPWKHX5.
[KNOWN] [2024] Yuan et al. — SSL for HAR. zotero_key:RTMH75VW.
[KNOWN] [2024] Chen et al. — Sensor2Text. zotero_key:2ZYUFEMW.
[KNOWN] [2024] Sun et al. — TEST. zotero_key:M35RDBWX.
[KNOWN] [2024] Talukder et al. — TOTEM. zotero_key:SKZEZQTH.
[KNOWN] [2024] Jin et al. — Time-LLM. zotero_key:BPGWP88R.
[KNOWN] [2024] Garza et al. — TimeGPT-1. zotero_key:7FJCF2J9.
[KNOWN] [2024] Liu et al. — Timer. zotero_key:KKXN4S6L.
[KNOWN] [2024] Gao et al. — UniTS. zotero_key:9X4Z2LPR.
[KNOWN] [2024] Masserano et al. — WaveToken. zotero_key:MXKVRSKK.
[KNOWN] [2024] Liu et al. — iTransformer. zotero_key:3BLCBJFP.
[KNOWN] [2024] Chen et al. — l-DAE. zotero_key:DZ2UYXUL.
[KNOWN] [2025] Xie et al. — ChatTS. zotero_key:XQBXBKNH.
[KNOWN] [2025] Gu et al. — Foundation Models Biosignals. zotero_key:EDTXS4NM.
[KNOWN] [2025] Unknown — SensorLM. zotero_key:HDPXBLAP.
[KNOWN] [2025] Liu et al. — Sundial. zotero_key:4QQTVIYC.
[KNOWN] [2025] Liu et al. — TS-Agent. zotero_key:M87QEL4E.

### Recent Activity

2026-05-14 | Area page seeded | 44 papers from Zotero, 11 from graphify seed.
