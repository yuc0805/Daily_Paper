# AI Digest — 2026-06-29

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

The signal today is heavy in your primary area. One narrative-HAR paper anchors Tier A; two biosignal foundation-model papers and one field survey fill Tier B. The model-release news is quiet, with one frontier update and one code model.

---

## Tier A — deep read

### ActivityNarrated: An Open-Ended Narrative Paradigm for Wearable Human Activity Understanding
arXiv:2604.00767 — https://arxiv.org/abs/2604.00767 — Area: Signal/Time Series

**Problem.** Standard wearable human activity recognition fixes a small label set and one sensor position. Real wearable use is long-tailed, personalized, and made of overlapping activities, so a closed classifier cannot represent behavior outside its vocabulary and cannot be scored on it.

**Method.** The paper contributes three parts. First, a dataset of unscripted multi-position IMU recordings with time-aligned natural-language narration, built without a predefined taxonomy. Second, an evaluation framework based on sensor-language retrieval that generalizes closed-set classification and gives metrics beyond accuracy and F1. Third, ActNarrator, a language-conditioned model that maps variable-duration, heterogeneous, partially observed sensor streams to open-ended text.

**Result.** When the open-ended representation is evaluated on classification as a downstream task, it nearly doubles Macro-F1 over closed-set HAR baselines. The retrieval-based metrics also let the authors measure semantic alignment on activities that have no fixed label.

**Limitations.** The headline number is reported as a downstream re-use of the representation, not a like-for-like classifier, so the comparison favors the new method's framing. Narrative quality depends on the human narration in the dataset, which is itself a new and unstandardized resource. Generalization across very different sensor placements is claimed but is the hard case for any wearable model.

**Why it matters to Leo.** This is in your primary area and shows the vision-language retrieval evaluation style working on IMU data. That porting direction (sensor-language retrieval as the metric) is now demonstrated and is therefore closing as easy ground; the open part is the open-vocabulary dataset construction and partial-observation handling.

**How this builds on what you know:** ActivityNarrated's direct parents in your library are Sensor2Text (Chen 2024, ELYUE3NF, graphify community 4) and SSL for HAR (Yuan 2024, RTMH75VW, community 1). Where Sensor2Text produced fixed descriptions tied to a closed activity vocabulary and a single sensor position, this paper does open-ended narration over multi-position partially observed streams, because real behavior is long-tailed rather than confined to a benchmark label set. Where SSL for HAR learned a representation that a closed classifier then probes, this paper supervises the representation by retrieval against free text, so the score measures motion-language alignment instead of top-1 accuracy. This paper extends Sensor2Text, which already crossed the time-series and llm-health communities in your library (the chen2024_sensor2text to liu2023_few_shot_health bridge). The new work pushes that bridge further toward open-vocabulary, retrieval-scored activity understanding.

---

## Tier B — TLDRs

### AnyPPG: An ECG-Guided PPG Foundation Model Trained on Over 100,000 Hours of Recordings
arXiv:2511.01747 — https://arxiv.org/abs/2511.01747 — Area: LLM-Health

AnyPPG pretrains a PPG encoder on over 100,000 hours of synchronized PPG and ECG from 58,796 participants across five datasets, aligning the two signals in a shared space so ECG guides the noisier PPG. Across eleven physiological tasks over six datasets it reports average gains of 12.8% on regression and 9.1% on classification over the next-best model. On a screen across 1,014 ICD-10 categories, 13 reach AUC above 0.8 and 137 above 0.7, including non-cardiac conditions such as Parkinson's disease (0.78) and chronic kidney disease (0.74). The diagnostic breadth is the interesting claim and the part to read critically, since label quality across 1,000 ICD codes is uneven.

**How this builds on what you know:** Parents in your library are Foundation Models for Biosignals (Gu 2025, 2XWEG7AF, community 1) and HeAR (Baur 2024, 3LA8GNCU, community 1). Where the Gu survey described single-modality biosignal pretraining and HeAR built one for acoustics, AnyPPG adds cross-signal guidance, because PPG alone is noisy and synchronized ECG carries a cleaner cardiac timing signal that constrains the PPG representation. The imported idea is cross-modal supervision (a clean modality teaching a noisy one), already standard in vision-language; applied ECG-to-PPG it is now demonstrated, so the generic version of that port is closing.

### SignalMC-MED: A Multimodal Benchmark for Evaluating Biosignal Foundation Models on Single-Lead ECG and PPG
arXiv:2603.09940 — https://arxiv.org/abs/2603.09940 — Area: Signal/Time Series

From the Oxford group (Gustafsson, Gu, Clifton and colleagues), SignalMC-MED supplies a common measuring stick: 22,256 visits with paired 10-minute ECG and PPG and 20 clinical tasks covering demographics, emergency-department disposition, lab-value regression, and prior ICD-10 detection. The findings are useful as a check on the foundation-model push: domain-specific biosignal models beat general time-series models, ECG+PPG fusion beats single signals, the full 10-minute window beats short segments, larger model variants do not reliably beat smaller ones, and hand-crafted ECG features stay competitive. This is the controlled comparison the area has been missing.

**How this builds on what you know:** Parents are Foundation Models for Biosignals (Gu 2025, 2XWEG7AF, community 1) and HeAR (Baur 2024, 3LA8GNCU, community 1), and it shares an author (Gu) with the survey. Where Gu 2025 framed the model class and HeAR built one, SignalMC-MED fixes the evaluation so two papers claiming state of the art can be compared, because the field had models but no shared multimodal clinical benchmark. Its finding that hand-crafted features remain competitive matches the FEEL result already in your graph, so the two reinforce a consistent caution about raw-signal foundation models.

### Foundation Models Defining A New Era In Sensor-based Human Activity Recognition: A Survey And Outlook
arXiv:2604.02711 — https://arxiv.org/abs/2604.02711 — Area: Signal/Time Series

This survey reads 132 papers and organizes foundation models for sensor HAR with a lifecycle taxonomy across input design, pretraining, adaptation, and utilization on nine axes. It names three directions: HAR-specific foundation models from scratch, general time-series and multimodal models adapted to sensors, and large language models used for reasoning, annotation, and interaction. Open challenges it lists are data curation, multimodal alignment, on-device personalization, and responsible deployment. Useful as a related-work base and a defensible taxonomy for a proposal; it is a map, not a result.

**How this builds on what you know:** Parents in your library are HARMamba (Li 2024, HE9X47KN, community 2) and Sensor2Text (Chen 2024, ELYUE3NF, community 4), with SSL for HAR (Yuan 2024) also placed by it. Where those are individual points in your graph, the survey supplies the coordinate system that locates them, because the field outgrew its organizing structure. Its three directions line up with graphify communities 1, 4, and 5, so it doubles as an index over the HAR papers you already hold.

---

## Tier C — scan

1. PerceptionDLM: parallel region captioning with a multimodal diffusion language model, large throughput gains over autoregressive captioning. https://arxiv.org/abs/2606.19534
2. Bio-Inspired SSL for Wrist-worn IMU: masks "movement segments" from motor-control theory, beats SSL baselines on six benchmarks (ICML 2026). https://arxiv.org/abs/2603.10961
3. RAID: semantic-graph diffusion with a frozen multilingual LLM for true cold-start recommendation. https://arxiv.org/abs/2606.16925
4. TSRBench: multi-task multimodal time-series reasoning benchmark for generalist models. https://arxiv.org/abs/2601.18744
5. ARLArena: a unified framework for stable agentic reinforcement learning. https://arxiv.org/abs/2602.21534
6. BioX-Bridge: unsupervised cross-modal knowledge transfer across biosignals. https://arxiv.org/abs/2510.02276
7. DomusFM: a foundation model for smart-home sensor data. https://arxiv.org/abs/2602.01910
8. HiMAE: hierarchical masked autoencoders find resolution-specific structure in wearable time series. https://arxiv.org/abs/2510.25785

---

## Tier D — Time-series / Bio-sensing Gap Watch

**Already ported (closed off).** ActivityNarrated and Sensor2Text bring vision-language contrastive retrieval into IMU activity understanding (graphify community 4). AnyPPG brings cross-modal supervision (a clean modality teaching a noisy one) into PPG via ECG (community 1). Bio-Inspired SSL brings masked-autoencoder pretraining into IMU, with a domain-specific token. These transfers are demonstrated, so the generic versions are no longer open ground.

**Unported opportunity 1 — diffusion language models for parallel signal imputation.** PerceptionDLM (community 3) shows that a multimodal diffusion language model can decode many region descriptions in parallel rather than autoregressively. No equivalent exists for multivariate biosignal or wearable time series. Transfer hypothesis: a masked diffusion language model over signal-patch tokens could impute or forecast multiple channels in a single denoising pass, instead of the autoregressive rollouts current time-series models use, which would cut inference latency for multi-channel wearable streams.

**Unported opportunity 2 — discrete flow-matching for signal generation.** Discrete flow-based and edit-flow generation (the FUDOKI and OneFlow line in multimodal generation) has not been applied to time-series synthesis or augmentation. Transfer hypothesis: a discrete flow over quantized signal tokens could generate realistic synthetic biosignals for data-scarce HAR and physiological tasks, addressing the label-scarcity problem the HAR survey above names as a top open challenge.

---

## News

Anthropic released Claude Opus 4.8, which took the top spot on the Artificial Analysis Intelligence Index at 61 and led SWE-bench Pro at 69.2%. Moonshot AI released Kimi K2.7 Code on June 12, 2026, a code-focused model. Separately, on June 12 the US government ordered Anthropic to pull both Fable 5 and its Mythos 5 frontier model citing national security; this is a regulatory event rather than a release, but it affects which frontier weights are available. Treat the benchmark figures as vendor-reported until independently checked.

---

Quiet news day on model releases; the paper signal in your primary area was strong, so Tier A and all three Tier B slots went to bio-sensing and HAR.

End of digest. Close this tab when done.
