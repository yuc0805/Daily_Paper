# AI Digest — 2026-08-30

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

---

## Tier A — deep read

### CardioState-JEPA: Delay-Aware Cross-Modal Learning of a Shared Cardiac Representation
Shafiq, Pham, Zhu, Zhou, Hu, Saeed — arXiv:2608.12944 — https://arxiv.org/abs/2608.12944

**Problem.** Electrocardiography, photoplethysmography and phonocardiography all observe the same heartbeat through different physics: electrical activation, peripheral blood volume change, and mechanical sound. Existing cardiac foundation models train one encoder per sensing modality, so the fact that three sensors report on one underlying process is never used as a training signal. The cost falls on the weaker modalities. PPG and PCG have far less labelled data than 12-lead ECG, and a single-modality encoder has no way to borrow structure from the better-resourced signal.

**Method.** The model maps heterogeneous waveforms into a common token space and processes all three with a single shared Transformer encoder. Training follows a joint-embedding predictive architecture: the objective is to predict masked latent cardiac states, not to reconstruct the waveform. That choice moves the target onto shared physiology and away from sensor-specific appearance, which is what makes one encoder across three modalities plausible in the first place. The temporal problem is handled explicitly. Electrical, mechanical and hemodynamic events do not occur at the same instant, so cross-modal prediction runs through a learned delay aligner that matches signals at the corresponding point in the cardiac cycle rather than at the corresponding wall-clock sample. Because synchronized multi-sensor recordings are scarce, training is staged: within-modality structure is learned first from abundant unimodal data, then paired data is used only to align the modalities in latent cardiac time.

**Result.** Evaluated as a frozen encoder across 25 downstream tasks spanning all three modalities. Against the best self-supervised signal baseline, average PPG classification improves by 8.2 AUROC points, PCG murmur detection by 18.8 AUROC points, and ECG classification by 15.5 AUROC points. On several ECG benchmarks the encoder matches or exceeds cardiac models that were trained with privileged clinical text or with supervised labels.

**Limitations.** The reported gains are averages over task groups against a single unnamed best baseline, so the 15.5-point ECG figure could be carried by a few weak tasks and the abstract does not let you check. Synchronized ECG/PPG/PCG data remains scarce and the two-stage curriculum is a workaround for that scarcity rather than a fix; there is no reported sensitivity curve showing how alignment quality degrades as the paired set shrinks. Frozen-encoder protocols favour representation-learning papers, and no fine-tuned comparison appears in the abstract. Finally, the delay aligner is learned, which means it can absorb dataset-specific timing artifacts, and the abstract does not report whether learned delays match known physiological pulse arrival times.

**How this builds on what you know:** The direct parents in your library are Foundation Models for Biosignals (Gu 2025, `2XWEG7AF`, graphify `gu2025_biosignals`, Community 1 Health AI and Self-Supervised), HeAR (Baur 2024, `3LA8GNCU`, graphify `baur2024_hear`, Community 1), and MAE Theory (Zhang 2023, `6INGKIJV`, graphify `zhang2023_mae`, Community 1). Where Gu's survey catalogued biosignal foundation models and found the field organized one encoder per modality, this paper treats that boundary as removable and shows the modalities can supervise each other. Where HeAR learned health acoustic representations by masking and reconstructing in input space for one modality, CardioState-JEPA predicts in latent space across three, because reconstruction targets would force the encoder to keep sensor-specific waveform detail that does not transfer. Where Zhang's analysis argued that masking helps by pushing the encoder toward semantic structure instead of low-level appearance, the delay aligner is the biosignal statement of the same argument: the semantics here are cardiac-cycle phase, so the model is told to align on physiological time rather than sample index.

On graphify bridges, note what this paper does not do. Your library's bio-sensing to language bridge runs Sensor2Text (`chen2024_sensor2text`) to LLMs are Few-Shot Health Learners (`liu2023_health_llm`), crossing Community 5 wearable sensing into Community 1 health AI. CardioState-JEPA stays entirely inside Community 1 on the encoder side and never touches text. That is a clean separation and it is also the opening: nobody has put a shared-physiology latent encoder underneath the language bridge.

**Why it matters to Leo.** This is the strongest version yet of the argument that multi-sensor physiological data should train one model rather than several, and it is in your primary area. Two things are directly reusable. First, the delay aligner is a general answer to a problem you meet in any multi-sensor wearable setup, where accelerometer, PPG and skin temperature respond to the same event at different lags; the same construction should apply with lag ranges set by the physiology rather than the cardiac cycle. Second, the staged curriculum — unimodal pretraining, then paired alignment — is a practical recipe for the usual situation where you have plenty of single-sensor data and very little synchronized multi-sensor data. On the porting question: JEPA-style latent prediction has now landed in cardiac biosignals, so that particular import from vision is closed. The unclosed part is the delay-aware variant applied outside cardiac signals.

---

## Tier B — TLDRs

### 1. LLM Agents for Time-Series: A Survey
Chen, Qin, Liu, Wu, Samia, Ding — arXiv:2608.26226 — Findings of EMNLP 2026 — https://arxiv.org/abs/2608.26226

The survey organizes LLM-based time-series agents by the problem they solve rather than by their components, splitting the literature into forecasting and reasoning, augmentation and synthesis, anomaly detection and diagnosis, and decision support. Within each category it asks how the task requirement shapes three specific design choices: agent architecture, tool use, and memory design. It also collects the datasets and environments in use and compares reported numbers where the settings are shared or close enough to permit it. The stated output is a design guide rather than a taxonomy for its own sake, plus a list of gaps the authors judge to be open.

**How this builds on what you know:** The parents are LLMs for Time Series: A Survey (Zhang 2024, `N2JLZBY3`, graphify `zhang2024_llm_ts_survey`), TS-Agent (Liu 2025, `I2CIT4I7`, graphify `liu2025_tsagent`), and ChatTS (Xie 2025, `VSCNJG5J`, graphify `xie2025_chatts`) — all three sit in Community 4, Time Series plus LLM Integration, and TS-Agent is one of your two god nodes for that area. Where Zhang's 2024 survey organized the field by how a language model is attached to a series — prompting, alignment, fine-tuning — this one organizes by task and asks what the task demands of the agent loop, because two years of systems have made the attachment method the less interesting variable. Where TS-Agent and ChatTS each presented one architecture and one set of numbers, this survey puts them side by side under shared settings, which is the comparison neither paper could make for itself.

This is also a Community 4 to Community 0 crossing. Memory design and tool use are Community 0 concepts, carried by ToolkenGPT and the Memory Mechanisms survey in your library; applying them as organizing axes for time-series systems pushes the time-series-plus-LLM bridge toward the agent literature rather than the forecasting literature. If you read one thing here, read the memory-design sections, since that is the axis your own library is thinnest on for time series.

### 2. WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution
Tang, Rashtchian, Ferng, Tomkins, Juan, Vu (Google Research and Virginia Tech) — arXiv:2608.27454 — https://arxiv.org/abs/2608.27454

Agent skills package reusable workflows, and recent systems discover them automatically from execution traces. The complaint here is that the reasoning behind each skill revision stays buried in the optimization history, so later iterations cannot reuse it. WikiSkill separates three things that prior work mixes: raw execution experience, accumulated knowledge, and executable skills. Experience is continuously consolidated into a persistent wiki, and skill updates read from the wiki rather than from raw traces. Across several benchmarks and models it beats existing skill-evolution methods and the no-skill baseline in most settings, and ablations confirm the wiki itself is doing the work. Two secondary findings are the interesting ones: skills and model scale are complementary, with small models plus evolved skills sometimes beating substantially larger models without them, and skills transfer across model families, with externally evolved skills sometimes beating self-evolved ones.

**How this builds on what you know:** Parents are the Memory Mechanisms of Foundation Agents survey (Huang 2026, `BDY3HUCV`, graphify `huang2026_memory`, Community 0), Chain-of-Experience (2608.18027, your Tier A from 2026-08-23), and ToolkenGPT (Hao 2024, `6RDHVVA2`, graphify `hao2024_toolkengpt`, Community 0). Where Huang's survey catalogued agent memory mechanisms without establishing which are worth the storage, WikiSkill runs the ablation and reports that a consolidated knowledge layer is the part that matters. Where Chain-of-Experience kept a flat append-only log of prior attempts and re-prompted on it within a task, WikiSkill compiles that log into structured knowledge that outlives the task and can be handed to a different model, because a flat trace does not survive the transfer. Where ToolkenGPT froze capability into learned tool embeddings that require training, WikiSkill keeps capability in text that any model can read.

The graphify bridge ToolkenGPT to PyVision (`hao2024_toolkengpt` to `zhao2025_pyvision`, tool-using agents) applies directly. WikiSkill extends that bridge by making the tool-and-workflow layer persistent and portable across model families rather than tied to one model's weights or one session's context.

### 3. Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization
Robbyant Research — arXiv:2608.26103 — https://arxiv.org/abs/2608.26103

The target is zero-shot cross-task generalization in manipulation, where the policy must run a task it never saw in training. The argument is that language models solved the analogous problem by moving task specification into the context, and that the natural in-context specification for manipulation is a human video, since it carries visual detail about how the task should evolve that a sentence does not. Zero-WAM is a causal video-action model that executes an unseen task by following human video guidance supplied in context. The data problem is that task-rich paired human-robot recordings barely exist, so the authors build an automatic pipeline that converts task-sampled robot trajectories into semantically matched human videos, producing HumanGen, a set of 74.2K human-robot in-context pairs.

**How this builds on what you know:** Parents are DINO-WM (Zhou 2025, `W44RSJJI`), Navigation World Models (Bar 2024, `JQ7JD8AR`) — both Community 7 world models in your library — and VideoMAE (Tong 2022, `9QCZ3A32`, Community 9 video action recognition). Where DINO-WM built a world model in a frozen visual latent space and planned inside it for a fixed task family, Zero-WAM makes the task itself an input, because planning machinery does not help when the task specification is the missing piece. Where Navigation World Models conditioned prediction on the agent's own trajectory, this conditions on someone else's demonstration, which is what turns a world model into a policy for unseen tasks. Where VideoMAE learned video representations by masked reconstruction with no notion of task, the representation here has to carry task intent across a human-to-robot embodiment gap, and the HumanGen pipeline is the substitute for the paired data that would otherwise be needed to learn that mapping.

---

## Tier C — scan only

| Paper | Hook | Link |
| --- | --- | --- |
| PILOT in the Loop (2608.26530) | Supervisor-worker harness makes long-horizon agent self-improvement live rather than post-hoc. | https://arxiv.org/abs/2608.26530 |
| What Makes Good Agentic Data? An ACE Lens (2608.27260) | Asks which properties of generated trajectories actually train better agents. | https://arxiv.org/abs/2608.27260 |
| Self-OPD (2608.26872) | On-policy distillation for flow matching models with no teacher network. | https://arxiv.org/abs/2608.26872 |
| CaSKG (2608.25500) | Counterfactual-causal skill graphs for retrieving the right agent skill at scale. | https://arxiv.org/abs/2608.25500 |
| Agentic Game Development as Trajectory Data Engine (2608.25518) | Generates verifiable trajectories at scale by having agents build games. | https://arxiv.org/abs/2608.25518 |
| GameWAM (2608.26200) | Tencent world-action model for video games, companion to the Zero-WAM line. | https://arxiv.org/abs/2608.26200 |
| UrbanGround (2608.27456) | Spatial agency benchmark at real city scale, local perception to navigation. | https://arxiv.org/abs/2608.27456 |
| P2E-VQ (2608.14656) | Augments PPG representations by retrieving discrete ECG patches. | https://arxiv.org/abs/2608.14656 |

---

## Tier D — Time-Series / Bio-Sensing Gap Watch

**Already ported (closed off).** CardioState-JEPA closes the JEPA import. Joint-embedding predictive architectures came out of vision, and latent-space masked prediction has now been demonstrated on ECG, PPG and PCG with a delay-alignment mechanism that is specific to physiological timing. Community 1 in your graphify seed already held the masked-modelling line for biosignals through HeAR and the MAE theory paper; this closes the latent-prediction variant of it. P2E-VQ closes a smaller one: discrete-token retrieval augmentation, a technique from vector-quantised generative modelling, applied to cross-modal PPG enhancement. Do not spend a paper on either.

**Unported opportunity 1: persistent knowledge bases for time-series agents.** WikiSkill shows that consolidating agent experience into a durable, model-independent wiki beats keeping it in traces or weights, and that the resulting skills transfer across model families. Nothing in Community 4 does this. TS-Agent and ChatTS both start each analysis from scratch. Transfer hypothesis: a time-series agent that writes down what it learned about a specific sensor stream — its sampling artifacts, its seasonality, which detectors gave false positives on it — and reads that back on the next run should beat a stateless agent on longitudinal monitoring, and the accumulated notes should transfer to a different backbone model without retraining.

**Unported opportunity 2: in-context task specification for wearable sensing.** Zero-WAM specifies a novel manipulation task with a human video placed in context rather than with a fine-tuning pass. The equivalent for human activity recognition would be specifying a new activity class with one demonstration segment of raw sensor data in context. Transfer hypothesis: a causal sensor-action model given a single labelled IMU or PPG segment as an in-context exemplar should recognize an unseen activity class without a gradient update, and Zero-WAM's synthesis pipeline suggests the paired-data shortage can be handled by generating matched exemplar-query pairs from existing labelled trajectories rather than collecting new ones.

---

## News

Model releases this month, none from yesterday specifically. Z.AI shipped GLM-5.3 Flash on 26 August, the most recent tracked release of the month. Google released Gemini 3.5 Transcribe, a speech-to-text model that ships as two separate endpoints rather than one, which is worth a note if you are running audio front ends. Meta released Muse Spark 1.2 on 6 August. Trackers count roughly fourteen model releases across August 2026. Nothing here changes a research plan.

---

Quiet Sunday. Hugging Face has not posted a new daily list since 28 August, so Tier A came from a mid-month paper in your primary area rather than from yesterday's batch, and it is the better read for you than anything on the 28 August list.

End of digest. Close this tab when done.
