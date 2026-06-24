# AI Digest — 2026-06-24

Reading budget today: 1 deep paper (Tier A, ~20 min), 3 TLDRs (~10 min), 8 scan headlines (~5 min). Total under 1 hour. If Tier A is not done by 6 AM, stop.
Open-tab rule: maximum 3 papers open at once. Close one before opening a fourth.
Two-page test: if Tier A's first two pages do not justify the read, drop it and promote a Tier B paper.

Note on today's signal: a quiet day for your primary area. No new time-series or bio-sensing paper landed in the last day that clears Tier A. The strongest fresh work is in multimodal spatial reasoning, so Tier A is a multimodal paper, one Tier B slot goes to a recent time-series anomaly-detection method, and the Gap Watch section turns today's methods into transfer ideas for wearable sensing.

---

## Tier A — deep read (one paper)

### Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models (2606.03988)

**Problem.** Vision-language models answer many questions about an image well, but they fail when the answer depends on something not directly visible: what a scene looks like from another viewpoint, where a path goes when it passes behind an object, or how partial views add up to one count. These tasks need the model to picture an unobserved spatial configuration and reason over it. Standard practice is to make the model write a chain-of-thought in words. The paper asks whether forcing this spatial computation through language is the right move at all.

**Method.** The authors introduce Imaginative Perception Tokens (IPT): intermediate perceptual representations that record what the model would perceive under an alternative spatial configuration, while staying consistent with the observed input. The model is trained to produce these tokens as a supervision signal. To study the idea they define three tasks — Perspective Taking, Path Tracing, and Multiview Counting — and build datasets of about 20,000 examples each, with ground-truth imaginations, answers, and benchmarks. The backbone is the unified vision-language model BAGEL. They compare IPT supervision against textual chain-of-thought training and against training on final answers only.

**Result.** IPT supervision improves spatial reasoning across the three tasks and often beats textual chain-of-thought, even though IPT does not generate any image at inference time. On Multiview Counting it raises accuracy by 3.4 percent, and on Path Tracing it reaches performance competitive with strong closed-source models. Combining IPT with answer-only supervision gives further gains. The notable negative result is that textual chain-of-thought can substantially lower performance on these tasks, which points to a modality mismatch: pushing spatial computation through language hurts rather than helps.

**Limitations.** The three tasks are constructed and somewhat synthetic, so transfer to natural spatial questions in the wild is not established. The method depends on having ground-truth "imaginations" to supervise against, which were generated for these datasets and may not exist for other domains. Results use one backbone (BAGEL); whether IPT helps weaker or non-unified vision-language models is open.

**Why it matters to Leo.** The reusable lesson is about the representation, not the robot or the room. When a problem is fundamentally non-linguistic, supervising a model to externalize an intermediate representation in the native modality can beat verbalizing the reasoning, and verbalizing can actively hurt. That is directly relevant to time-series and bio-sensing, where forcing numeric or physiological reasoning through text tokens is the usual failure mode. The Gap Watch section turns this into a transfer hypothesis for wearable signals.

**How this builds on what you know:** The direct parent in your library is Chain-of-Thought Prompting (Wei 2023, HBLPTRMY, reasoning area, graphify community 0). Where Chain-of-Thought makes a model reason in natural-language steps, IPT shows that for spatial problems the reasoning trace should live in a perceptual representation instead of words, because the language channel distorts spatial computation. The paper also sits in the vision-language cluster (graphify community 3, the SigLIP and DALL-E 2 neighborhood), so it acts as a small bridge: it carries the reasoning-trace idea from community 0 into the vision-language models of community 3, and reports that the text-based version of the trace is the wrong tool there.

---

## Tier B — TLDRs (three papers)

### VAN-AD: Visual Masked Autoencoder with Normalizing Flow for Time Series Anomaly Detection (2603.26842)
VAN-AD turns a numeric time series into an image-like input, masks part of it with a checkerboard pattern, and reconstructs it with a masked autoencoder; large reconstruction error flags an anomaly. It adds two pieces on top: a step that maps the reconstructed sequence back into the statistical space of the original to amplify the gap on abnormal windows, and a normalizing-flow module that models the probability density of the current window so the anomaly score is a likelihood rather than a raw error. The design imports the masked-autoencoder recipe from vision directly into multivariate time-series anomaly detection. This is squarely in your primary area and is a clean example of a vision method being ported to sensing.

**How this builds on what you know:** Its parents in your library are the masked-autoencoder line — MAE (A5HBRQB9) and the MAE theory paper "How Mask Matters" (6INGKIJV, self-supervised area, graphify community 1). Where MAE learns image representations by reconstructing masked patches, VAN-AD reuses the masked-reconstruction objective as an anomaly score for time series and pairs it with a normalizing-flow density model, because reconstruction error alone does not give a calibrated probability of abnormality. It is closely related to the biosignal foundation-model work you hold (Foundation Models for Biosignals, 2XWEG7AF), which uses the same masked-reconstruction family on physiological signals.

### On Information Self-Locking in Reinforcement Learning for Active Reasoning of LLM Agents (2603.12109)
The paper names a failure mode in reinforcement-learning training of question-asking agents: the agent stops asking informative questions and stops absorbing the evidence it already has, so it locks itself into a low-information loop. The authors split active reasoning into action selection (which questions to ask) and belief tracking (how to update from answers), and show that weakness in either one starves exploration during training, which then prevents both from improving — a self-reinforcing trap. Their fix reallocates the learning signal by injecting cheap directional critiques that push the agent out of the locked state, and they report that this measurably reduces self-locking.

**How this builds on what you know:** The direct parent is DeepSeek-R1 (Z5IWHZAE, reasoning area, graphify community 0), which trains reasoning behavior through reinforcement learning with verifiable rewards. Where DeepSeek-R1 shows that reinforcement learning can produce strong single-pass reasoning, this paper studies the multi-turn, information-gathering case and identifies how the same training process can collapse exploration, then patches it. This sits on the graphify cross-area bridge from DeepSeek-R1 to Chain-of-Thought (reasoning-via-reinforcement-learning versus reasoning-via-prompting); the new work pushes that bridge toward interactive, evidence-seeking agents rather than one-shot answers.

### Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads (2606.06448)
This paper looks at agent memory from a systems angle rather than a modeling one. It characterizes how long-horizon LLM agents store, retrieve, and update memory across sessions, and groups existing systems into a small set of patterns: flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. By measuring the runtime behavior of these patterns, it surfaces the cost and latency implications of each — for example how memory size and retrieval strategy affect serving. The contribution is a map of the design space plus evidence about which patterns are expensive to run at scale.

**How this builds on what you know:** Its parent is the Memory Mechanisms Survey (BDY3HUCV, agent area, graphify community 0), which categorizes how foundation-agent memory works. Where that survey organizes mechanisms by what they do, this paper measures what they cost when deployed, because a memory design that reads well on paper can be too slow or too large to serve. It is a useful companion read if you ever instrument memory for a long-running sensing or health agent.

---

## Tier C — scan headlines (eight papers)

AnyPPG: ECG-guided PPG foundation model trained on over 100,000 hours of recordings for holistic health profiling — https://arxiv.org/abs/2511.01747

Wavelet-Driven Masked Multiscale Reconstruction for PPG Foundation Models — multiscale masked reconstruction tuned to pulse waveforms — https://arxiv.org/abs/2601.12215

SIGMA-PPG: statistical-prior informed generative masking for a PPG foundation model — https://arxiv.org/abs/2601.21031

Learning Longitudinal Health Representations from EHR and Wearable Data — one continuous-time latent state shared across clinical events and sensor streams — https://arxiv.org/abs/2601.12227

Speech Foundation Models Generalize to Time Series Tasks from Wearable Sensor Data — audio pretraining transfers to wearable signals — https://arxiv.org/abs/2509.00221

Low Rank Transformer for Multivariate Time Series Anomaly Detection and Localization — low-rank attention for cheaper anomaly localization — https://arxiv.org/abs/2602.08467

Foundation Models Defining a New Era in Sensor-based Human Activity Recognition: A Survey and Outlook — current map of foundation models for activity recognition — https://arxiv.org/abs/2604.02711

Monet: Reasoning in Latent Visual Space Beyond Images and Language — reasoning steps held in a latent visual space rather than text — https://arxiv.org/abs/2511.21395

---

## Tier D — Time-series / Bio-sensing Gap Watch

Already ported (closed off). VAN-AD (above) carries the masked-autoencoder recipe into time-series anomaly detection, and the PPG foundation models in Tier C (AnyPPG, Wavelet-PPG, SIGMA-PPG) carry masked reconstruction and contrastive pretraining into physiological signals. These match graphify community 1 (self-supervised and masked-autoencoder methods) and community 5 (wearable sensing), so masked-reconstruction self-supervision on biosignals is now well-occupied ground. New entries there compete on data scale and engineering, not on a novel transfer.

Unported opportunity 1 — IPT-style native-modality reasoning traces for sensing. Tier A showed that for spatial problems, supervising an intermediate representation in the native modality beats a text reasoning trace, and that the text trace can hurt. The transfer hypothesis: for a time-series reasoning agent, supervise an intermediate "physiological imagination" — a short reconstructed or counterfactual signal segment (for example, what the next beat-to-beat interval pattern would look like under exertion) — instead of asking the model to describe the dynamics in words. The prediction is that a native-signal intermediate representation gives better and more auditable answers than a verbal chain-of-thought on numeric inputs.

Unported opportunity 2 — diffusion density models for anomaly scoring on biosignals. VAN-AD uses a normalizing flow to turn reconstruction into a calibrated likelihood. Diffusion models (DDPM, Ho 2020, graphify community 3) are a stronger density estimator for multimodal distributions and have not been used as the normality model in PPG or IMU anomaly detection. Transfer hypothesis: replace the normalizing-flow head with a conditional diffusion model over short windows, scoring abnormality by denoising likelihood; this should capture multiple "normal" regimes (rest, motion, sleep) that a single flow tends to blur together.

---

## News — model and product releases

Anthropic released Claude Fable 5 for general access, its Mythos-class model, reported at 95 percent on SWE-bench Verified and 80 percent on SWE-bench Pro, priced at 10 and 50 dollars per million input and output tokens. Google released Gemini 3.5 Pro, its first Gemini 3-tier model, with strong long-context and multimodal results and a number-one placement on the LMSYS Arena at launch. Moonshot AI released Kimi K2.7 Code on 12 June 2026, a coding-focused frontier model. (Release figures are vendor-reported; treat the benchmark numbers as claims, not independent measurements.)

---

End of digest. Close this tab when done.
