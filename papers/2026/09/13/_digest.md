# AI Digest — 2026-09-13

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A not done by 6 AM, stop.

Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.

Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

A note on sourcing this morning. The Hugging Face daily listing has not rolled over past 11 September, and its entire front page today is the set already covered in the 11 September digest. Today's selection therefore comes from targeted searches over the past week rather than from the daily feed, and every paper below was checked against the knowledge graph to confirm it has not already been written up.

---

## Tier A — deep read

### A radiographic world model for clinical reasoning and evidence generation (MedDream)
Xi, Hu, Wang, Safari and others, 11 authors. [arXiv:2609.07719](https://arxiv.org/abs/2609.07719)

**Problem.** Medical imaging models are built as one-way maps: radiograph to label, or description to image. Both are estimated from the same underlying radiographic state, so training them apart duplicates work and leaves a discriminative model that cannot be interrogated by simulation. A classifier can report that it underperforms on a subgroup; it cannot construct the cases that would close the gap.

**Method.** MedDream maps radiograph and text observations into one shared continuous latent state and requires that state to support both clinical readout and conditional regeneration of the observation. Pretraining used 2.65 million leakage-controlled radiograph-text pairs curated from 4.40 million candidates. The leakage control is not incidental: report-conditioned generation is trivially gameable when the same study appears on both sides of an evaluation. At use time, generation is conditioned on a prespecified subgroup performance gap rather than run open-loop.

**Result.** Evaluation spans eight clinical datasets and two independent reader cohorts. On diagnosis, the model generalized across disease recognition, label-scarce adaptation, severity assessment, and localization, and MedDream-supported review raised mean resident concordance with independent radiologist consensus from 56.3 to 63.0 percent. On generation, synthetic augmentation raised external VinDr-CXR macro-AUROC from 76.4 to 81.4 percent. The result worth the read is the subgroup experiment: conditioning generation on a stated performance gap raised weighted F1 by 3.1 points for Asian patients, while matched-volume unguided augmentation lowered it by 2.3 points. That is a 5.4-point spread attributable to the targeting decision alone, at equal data volume.

**Limitations.** Single institution group, single modality, and chest radiography is the most data-rich imaging setting there is, so the pretraining scale may not be reachable elsewhere. The reader study measures concordance with consensus, not patient outcome. Whether the shared latent is a world model in any strong sense, or an unusually well-regularized joint encoder, is not settled by these experiments; Vafa 2024 in your library sets the standard that would settle it.

**How this builds on what you know:** The parents are UNI Pathology (Chen 2023, graphify Community 1, Health AI and Self-Supervised), DDPM (Ho 2020, graphify Community 3, Vision-Language and Generative), and World Models (Ha 2018, world-model-rl). Where UNI Pathology built a medical encoder whose only readout is discriminative, this paper keeps the same large-scale pretraining logic but requires the latent to also reproduce the observation, because a state that can regenerate the radiograph is the one that can be perturbed and audited. Where DDPM treated conditional generation as an end scored on fidelity, this paper scores generated radiographs by whether they raise accuracy on held-out real data, which turns synthesis into an experimental instrument. Where Ha's World Models learned a latent for a controllable simulator with an action space, here the conditioning variable is a clinical description and the rollout is a counterfactual radiograph. Note the crossing: this single model joins graphify Community 1 and Community 3, which the seed graph currently connects only through shared self-supervised concepts and not through any one paper.

**Why it matters to you.** A wearable foundation model that can only classify cannot generate the counterfactual window that would test where it fails. Nothing in graphify Community 5 (Wearable Sensing and Behavior) does generative readout — GLOBEM and MindScape are observational, and the biosignal survey in your library treats discriminative transfer as the goal. A biosignal world model that synthesizes a physiologically plausible segment conditioned on a stated subgroup gap is an open import, and the 5.4-point spread above is the argument for why targeting matters more than volume.

---

## Tier B — TLDRs

### Where Does the Sound Go? Tracing Acoustic Information Loss in Audio-Conditioned LLMs
Jo, Lee, Kim, Choi, Choi. EMNLP 2026 Findings. [arXiv:2609.05871](https://arxiv.org/abs/2609.05871)

Audio-conditioned language models underuse prosody, emotion, and non-speech sound, and the standard explanation blames the ASR-trained frontend for discarding it. This paper tests that stage by stage, probing after the encoder, after the projector, inside the language model, and at the head, and also swaps Whisper for reconstruction codecs (EnCodec, DAC-VAE, WavTokenizer) inside an otherwise fixed pipeline. The discriminative acoustic information survives to the last hidden layer and the codec swaps do not fix the underuse, so the frontend was not the binding constraint. Fine-tuning only the letter rows of the output head recovers most of the multiple-choice accuracy gap, which places the deficit at readout.

**How this builds on what you know:** Parents are LTU (Gong 2023, audio), HeAR (Baur 2024, graphify Community 1), and CLAP (Elizalde 2022, audio). Where LTU built the encoder-projector-language-model pipeline and measured what it can answer, this paper instruments the same pipeline and measures what it still contains, because a capability failure and a representation failure need different fixes. Where HeAR showed acoustic detail survives encoding, this work carries the question past the encoder, where HeAR's evidence stopped, and finds the loss is downstream of everything the tokenizer literature has been optimizing.

### TempCloze: Can Video-LLMs Identify the Missing Middle?
Pei, Zhao, Liu, Meng, Chen, Wang, Du, University of Hong Kong. [arXiv:2609.01515](https://arxiv.org/abs/2609.01515)

Temporal reasoning benchmarks for video language models are mediated by text, which leaves room for shortcuts from option wording, answer correlations, and language priors. TempCloze shows a model the beginning and ending clips and asks it to pick the true missing middle from four video candidates, over 1,521 filtered videos from seven sources, mainly long-take and egocentric. Distractors come from the same source along three axes — Semantic (what should happen), Alignment (when it should occur), Progression (how it unfolds) — with shared scenes and objects so appearance cannot decide it. Across 10 proprietary and 21 open-source models, Alignment is the bottleneck: models handle plausible content and local progression but fail at temporal placement.

**How this builds on what you know:** Parents are the Video Action Survey (Zhu 2020, graphify Community 9), Flamingo (Alayrac 2022, multi-modal), and BLIP-2 (Li 2023, multi-modal). Where the Video Action Survey line evaluated temporal understanding with closed label sets and no language mediation, TempCloze keeps the language interface but removes the linguistic shortcut, because the shortcut rather than the temporal reasoning is what recent scores were measuring. Where Flamingo and BLIP-2 descendants are scored on question answering whose options carry wording cues, making the candidates themselves video removes that channel outright, and controlling appearance through same-source footage removes the other one.

### Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs
Li, Liao, Zhu. [arXiv:2609.11499](https://arxiv.org/abs/2609.11499)

Code world models store a world as an executable program, which is inspectable and editable, but representing a scene as code says nothing about how to construct code for a scene too complex to write in one pass. RCWM couples a Recursive Scene Program with a solver that calls itself: establish the whole, recursively reconstruct unresolved parts, then revisit the whole to refine composition. One shared camera projection propagates across levels so every render is comparable to the same reference image, and a vision-language coding agent diffs reference against render to decide whether to refine, descend, or return. It beats prior code-based image-to-scene methods, and ablations suggest deeper calls help finer structures. The abstract reports no headline numbers, so the size of the effect needs the full text.

**How this builds on what you know:** Parents are PyVision (Zhao 2025, graphify Community 0), ADaPT (Prasad 2023, graphify Community 0), and World Models (Ha 2018, world-model-rl). Where ADaPT recursed over a task plan and returned once subtasks succeeded, RCWM adds a mandatory return visit to the parent, because local refinement creates boundary and spatial-relation errors that are invisible from inside a part. Where PyVision let an agent write throwaway tools per query, here the program is the deliverable, so every refinement edits a persistent artifact. This extends the graphify cross-area bridge from ToolkenGPT to PyVision, which already crossed tool-using agents and vision; the new work pushes that bridge toward tool use that builds a persistent structured artifact rather than a per-query script.

---

## Tier C — scan only

| Paper | Hook |
| --- | --- |
| [World in World: Explore the World with World Models](https://arxiv.org/abs/2609.11548) | Evaluates world models by whether an agent can actually explore with them. |
| [UniH^3: All-in-One Medical Image Restoration](https://arxiv.org/abs/2609.11156) | One model for heterogeneous medical degradations via hierarchical homogeneity. |
| [Generative Late-Interaction Embeddings for Visual Document Retrieval](https://arxiv.org/abs/2609.11808) | ColBERT-style late interaction, but the embeddings are generated rather than pooled. |
| [HyQuant: Hybrid-Precision Quantization for LLM Attention](https://arxiv.org/abs/2608.27875) | Mixed precision inside attention rather than uniformly across weights. |
| [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102) | Distils streaming audio encoders in latent space; relevant to on-device signal frontends. |
| [Grounded Dual-State Calibration for GRPO-Trained Medical VLMs](https://arxiv.org/abs/2609.06419) | Separates what a medical model can do from how confident it claims to be. |
| [DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent RL](https://arxiv.org/abs/2609.11155) | Roles as a dynamic graph rather than fixed assignments in cooperative MARL. |
| [MetroLLM-Bench: Language Models as Transit Kiosk Runtimes](https://arxiv.org/abs/2609.10016) | Benchmarks an LLM as the runtime of a physical public terminal, latency included. |

---

## Tier D — Time-series / bio-sensing Gap Watch

No paper landed today whose primary modality is time series or wearable bio-sensing, so the entries below are unported opportunities read off the day's top vision and language work. Community 4 (Time Series and LLM Integration) and Community 5 (Wearable Sensing and Behavior) in graphify are the reference for what is already closed off.

**Unported opportunity — stage-wise information probing for signal-conditioned language models.** The audio paper above gives a cheap protocol: probe after the encoder, after the projector, inside the language model, and at the head, and ask at each stage whether the attribute is still recoverable. Community 4 holds ChatTS, TS-Agent, Sensor2Text, and the LLM-for-time-series survey, and all of them assume the encoder or tokenizer is where signal detail is lost, which is the assumption the audio result overturned in its own domain. Transfer hypothesis: run the same probe on a wearable-signal-to-LLM pipeline and the discriminative physiological information will also survive to the last hidden layer, meaning the field is tuning tokenizers when it should be tuning readout. This is a one-model, one-week experiment with a clean negative or positive answer either way.

**Unported opportunity — cloze evaluation with same-source distractors for physiological series.** TempCloze removes the language shortcut by making the answer options video. The identical construction applies to signals: mask a window, draw candidate middles from the same subject and session, and score temporal placement. Nothing in Community 4 does this; every benchmark there is language-mediated question answering, the exact format TempCloze shows is shortcut-prone. Transfer hypothesis: current time-series reasoning scores are inflated by option wording and priors about what a physiological trace usually does, and a video-style cloze protocol would show the same Alignment-dominant error profile, since temporal placement is precisely what sleep staging and activity-transition detection need.

**Unported opportunity — generative readout for wearable foundation models.** Covered above under Tier A. Community 5 is observational throughout, so conditioning synthesis on a measured subgroup gap has no analogue in the wearable literature.

**Already ported — nothing new today.** No vision or language method landed today that Community 4 or Community 5 has already absorbed, so there is nothing to strike off the list this morning.

---

## News

A quiet weekend. No model or product release is recorded for 12 or 13 September at the time of writing. The most recent entries remain Sakana AI's Fugu Ultra v2.0 and Fugu Max on 11 September and DeepSeek V4.1 Flash on 10 September, both carried in yesterday's digest. Treat the release-tracker aggregators as provisional; they lag and occasionally disagree with each other on dates.

---

End of digest. Close this tab when done.
