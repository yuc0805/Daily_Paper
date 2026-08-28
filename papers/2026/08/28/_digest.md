# AI Digest — 2026-08-28

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read (~20 min)

### Forecast Collapse in Time-Series Foundation Models
Wan, Ma, Zhu, Liu, Wang, Wen, Liu — arXiv:2608.14106 — https://arxiv.org/abs/2608.14106

**Problem.** Time-series foundation models are evaluated one series at a time, with per-series error metrics. The authors forecast hourly returns for 1,000 US equities and find the predictions go nearly flat and rank the series poorly, measured by cross-sectional correlation. They call this forecast collapse. The same models on the same panel do not collapse when the target is trading volume, which points at the target rather than the architecture.

**Method.** The study covers time-series foundation models, twelve deep-learning forecasters and 97 public benchmark configurations, and separates two causes. Low target predictability caps the amplitude of any calibrated point forecast, because the conditional mean of a barely predictable target is close to constant. Separately, per-series training objectives never identify cross-series structure, so nothing in training pressures the model to get the ordering right. The two causes produce a calibration-ranking tradeoff: squared error gives flat but well-scaled forecasts, while optimising cross-sectional correlation directly gives good ordering with amplitude inflated by more than an order of magnitude. CalibRank is a single objective that balances the two.

**Result.** On the Finance1K panel, CalibRank nearly triples cross-sectional correlation while keeping forecast amplitude close to the target, and it improves correlation on every model tested. The paper releases Finance1K as a dataset.

**Limitations.** The demonstration is financial. Whether the same objective helps on physiological or behavioural panels, where the cross-entity structure is weaker and the panel is smaller, is untested. CalibRank is presented as a training objective, so applying it to an already pretrained foundation model requires fine-tuning rather than a decoding change. The paper also does not report whether the ranking gain survives distribution shift across time.

**Why it matters to Leo.** Multi-subject wearable studies are panel problems, and the decisions built on them are cross-subject: who is deteriorating, who to alert, who to enrol. Heart rate variability, step count and sleep-transition targets are low-predictability in exactly the sense defined here, so the collapse mechanism should apply. The cheap action does not require adopting CalibRank at all: report cross-sectional correlation alongside per-series error in any multi-subject forecasting evaluation, because per-series metrics cannot detect this failure by construction.

**How this builds on what you know:** The direct parents in your library are Chronos (Ansari 2024, 72DFULQQ) and Moirai (Woo 2024, CFG6FEIF), with the LLMs for Time Series survey (Zhang 2024, N2JLZBY3, graphify community 4 — Time Series + LLM Integration) as the anchor that catalogued the per-series evaluation convention. Where Chronos and Moirai showed that one pretrained model can forecast unseen series without fitting them, and were scored one series at a time, this paper shows that scoring convention hides a failure: a model can be calibrated on every series individually and still be useless for any decision that compares series. The fix is in the objective rather than the architecture, so it transfers to any panel setting that ranks entities.

---

## Tier B — TLDRs (~10 min)

### FrontierChallenge: Evaluating Scientific Workflow Completion
Su et al. (HKU, Apodex) — arXiv:2608.24979 — https://arxiv.org/abs/2608.24979

A benchmark of 300 end-to-end scientific workflows, 97 released, across quantum chemistry, molecular dynamics, materials characterisation, analytical chemistry, life science and electrochemistry. Each task fixes inputs and specifies a bundle of required deliverables, so an agent is scored on complete delivery rather than on a final answer. Twelve frontier models under three scaffolds gave a best pass rate of 20.6 percent, or 20 of 97 tasks. Partial credit and completion diverge sharply: analytical chemistry reached an average score of 87.6 against a 4 percent pass rate, and electrochemistry reached 94.9 against 0 percent, while 75.5 percent of failing Claude Code runs still ended by claiming completion.

**How this builds on what you know:** The parents are LATS (Zhou 2024, 77ERE7HA) and ADaPT (Prasad 2023, J8DYBKW2), both in graphify community 0 (LLM Agents and Reasoning), plus DeepEyesV2 (Hong 2026, 4XXXYXS9). Where LATS and ADaPT improved how an agent searches and decomposes a long task, and measured that on task-level success, this benchmark asks whether the artifacts were delivered and finds the two questions come apart. This paper extends the ADaPT-to-LATS bridge already recorded in your graphify prior for planning-decomposition agents, and pushes it from planning quality toward delivery verification. The self-reported-completion finding matters most: both parents rely on some internal judgement of when a branch is finished, and that judgement is wrong three quarters of the time here.

### VoiceMem: Streaming Dual-Brain Memory for Real-Time Interaction
Xie et al. (NTU Singapore) — arXiv:2608.26005 — https://arxiv.org/abs/2608.26005

A memory architecture for duplex speech language models with two parallel stores, one for factual conversation content and one for affective and persona state, both read and written during the turn rather than between turns. Under top-5 retrieval the informational track beats Mem0 at top-200 by close to 30 points, so it finds the right item with a fortieth of the retrieved context. The affective track combines short-horizon and long-horizon attribution with a two-node persona representation and improves the aggregate score across three persona benchmarks by 4.29 points. Retrieval takes 134 ms, inside standard voice-activity-detection latency, so the memory adds no perceptible delay.

**How this builds on what you know:** The parents are the Memory Mechanisms Survey (Huang 2026, BDY3HUCV, graphify community 0) and, on the audio side, HeAR (Baur 2024, 3LA8GNCU, graphify community 1 — Health AI and Self-Supervised) and LTU (Gong 2023, ESEEEH85). Where the Huang survey framed agent memory as an offline process running between turns, this paper puts read and write inside the turn under a hard latency budget, which changes what a memory design is permitted to cost. Where LTU attached an audio encoder to a language model and kept one representation, VoiceMem splits content from affect and keeps two stores, on the argument HeAR makes that how something is said carries state a text summary discards.

### Gated Recurrent Transformers: Expressive Depth through Recurrent Modulation
Hegazy, Alanwar, Elhoushi (TU Munich) — arXiv:2608.15062 — https://arxiv.org/abs/2608.15062

Replaces most of a transformer stack with one shared core block applied R times between fixed prelude and coda blocks, with a lightweight elementwise update gate conditioned on the hidden state, the prelude output and noise resampled each step. Under matched FLOPs a 3-layer model matches a 12-layer GPT-2 Small baseline and leads Mixture-of-Recursions and heavy-tail depth sampling across all nine scale-by-budget cells. Under matched parameters and data, deeper recurrence reaches 2.76 validation loss against 2.84 without recurrence. At large scale the trade is 63 percent fewer parameters and 59 percent less peak decoding memory for 10 percent higher generation latency.

**How this builds on what you know:** The parents are Attention Is All You Need (Vaswani 2017, PHB9VRVM, graphify community 2 — Transformer and SSM Architectures), Mamba (Gu 2024, XNI34DQX) and HARMamba (Li 2024, HE9X47KN, also community 2). Where Mamba and HARMamba made a model recurrent along the sequence axis to reduce the cost of long context, this paper makes it recurrent along the depth axis and leaves sequence attention intact, which relieves parameter storage and decoding memory instead. Plain layer sharing has historically lost quality by forcing an identical transformation at every depth; the gate plus resampled noise restores per-step specialisation without per-step weights, and that is what carries the 3-layer to 12-layer equivalence.

---

## Tier C — scan (~5 min)

| Paper | Hook |
| --- | --- |
| [WarpSAC (2608.24479)](https://arxiv.org/abs/2608.24479) | Rethinks exploration and exploitation for scalable off-policy reinforcement learning. |
| [VGI-BENCH (2608.19583)](https://arxiv.org/abs/2608.19583) | Probes whether video generation models carry any transferable visual intelligence. |
| [JIT-Agent (2608.25593)](https://arxiv.org/abs/2608.25593) | Evolves the agent harness just in time rather than retraining the model. |
| [Open-MOPD (2608.19098)](https://arxiv.org/abs/2608.19098) | Diagnoses and fixes capability imbalance in multi-teacher on-policy distillation. |
| [D^3-MOPD (2608.24987)](https://arxiv.org/abs/2608.24987) | Schedules teacher domains dynamically to make multi-teacher distillation cheaper. |
| [StreamPI (2608.26067)](https://arxiv.org/abs/2608.26067) | Streaming multimodal temporal modelling for vision-language-action models. |
| [AnTrap (2608.24099)](https://arxiv.org/abs/2608.24099) | Tests whether Android GUI agents survive runtime anomalies and adversarial environments. |
| [Code World Model (2608.25927)](https://arxiv.org/abs/2608.25927) | Treats the coding agent itself as a world model. |

---

## Tier D — Time-series / bio-sensing gap watch

**Already ported.** Ranking objectives from information retrieval into time-series foundation model training. CalibRank in today's Tier A paper does this for financial panels, and the calibration-ranking tradeoff it describes is now documented across 97 benchmark configurations. Community 4 in your graphify prior already holds the language-model side of time-series integration through TS-Agent, ChatTS and the Zhang survey, so the LLM-alignment direction is well covered; the objective-design direction is now covered for finance.

**Unported opportunity 1 — cross-subject ranking objectives for physiological panels.** CalibRank has been shown on 1,000 equities, not on a multi-subject wearable cohort. Transfer hypothesis: a wearable panel forecasting heart rate variability or sleep-stage transitions across subjects has the same low-predictability, low-amplitude structure, so per-series error will hide the same cross-subject ranking failure, and a calibration-plus-ranking objective should recover deterioration ordering without inflating forecast amplitude. Nothing in community 4 or community 5 touches cross-entity objectives, so this is open.

**Unported opportunity 2 — depth recurrence for on-device sensing encoders.** Community 2 already contains the sequence-recurrence port into wearable sensing through HARMamba and Bi-Mamba+, but no paper in the library applies the gated depth-recurrence idea from today's Tier B architecture paper to a physiological encoder. Transfer hypothesis: on-device sensing models are bound by parameter storage and peak memory rather than by FLOPs, which is exactly the axis this method trades along, so a 63 percent parameter reduction at 10 percent latency cost is a better deal on a wearable than it is on a server.

---

## News

Model releases continued at high frequency through the last week of August. GLM-5.3-Flash from Z.ai landed on 26 August, the most recent release at the time of writing. Earlier in the month Google shipped Gemini 3.7 Flash on 13 August, roughly three weeks after 3.6, and OpenAI released GPT-Live, a native voice model for ChatGPT Voice with sub-300 ms latency. OpenAI also announced that the DALL-E interface inside ChatGPT retires on 30 August. Tracking sites count 31 new models from 16 providers in the past 30 days, which is worth noting mainly as context: benchmark numbers in agent papers now age faster than the papers do.

---

End of digest. Close this tab when done.
